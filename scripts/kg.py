#!/usr/bin/env python3
"""Salesforce Knowledge Graph builder and validator.

Usage:
  python3 scripts/kg.py check            # validate only (exit 1 on errors)
  python3 scripts/kg.py build            # validate, then regenerate graph/
  python3 scripts/kg.py similar "Title"  # find existing articles close to a candidate topic
  python3 scripts/kg.py similar --draft articles/<domain>/<slug>.md
                                         # check a written draft by name and content (exit 1 = review)

Articles live in articles/<domain>/<slug>.md with YAML frontmatter (see SCHEMA.md).
Generated outputs (never hand-edit): graph/graph.jsonld, graph/triples.nt,
graph/index.json, graph/frontier.md, graph/stats.md.
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML missing: pip install pyyaml --break-system-packages")

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "articles"
GRAPH = ROOT / "graph"
ONTOLOGY = ROOT / "ontology" / "ontology.ttl"

BASE = "https://github.com/john1hsu/salesforce-knowledge-graph/id/"
KTO = "https://github.com/john1hsu/salesforce-knowledge-graph/ontology#"
SKOS = "http://www.w3.org/2004/02/skos/core#"
PROV = "http://www.w3.org/ns/prov#"
RDF_TYPE = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
RDFS_LABEL = "http://www.w3.org/2000/01/rdf-schema#label"
DCT = "http://purl.org/dc/terms/"

ID_RE = re.compile(r"^kt:[a-z0-9]+(?:-[a-z0-9]+)*$")
SOURCE_TYPES = {
    "official-docs",      # help.salesforce.com, developer.salesforce.com, architect.salesforce.com, release notes
    "official-learning",  # Trailhead modules, Salesforce certification exam guides
    "official-blog",      # Salesforce Developers / Admins / Architects / Engineering blogs
    "standards-body",     # IETF RFCs, OASIS, W3C, NIST (OAuth, SAML, SCIM, FedRAMP ...)
    "government",         # federal sources, e.g. FedRAMP marketplace, GSA
    "peer-reviewed", "academic", "textbook",
    "partner",            # recognized consulting partners, ISVs (weak)
    "community",          # Salesforce Stack Exchange, MVP blogs (weak)
    "news",               # reputable press, for announcements only (weak)
}
STRONG_SOURCE_TYPES = SOURCE_TYPES - {"partner", "community", "news"}
OFFICIAL_SOURCE_TYPES = {"official-docs", "official-learning"}
RELEASE_RE = re.compile(r"^(Spring|Summer|Winter) '\d{2}$")
REQUIRED = ["id", "type", "title", "domain", "summary", "sources", "created", "release", "status"]
STATUSES = {"current", "beta", "pilot", "deprecated", "retired", "concept"}
NEAR_DUP_THRESHOLD = 0.45   # shingle Jaccard on body text
TITLE_DUP_THRESHOLD = 0.85  # token Jaccard on normalized titles/aliases
CONTENT_REVIEW_THRESHOLD = 0.45  # TF-IDF cosine of a draft vs an existing article (see `similar --draft`)


# ---------------------------------------------------------------- helpers ---
def ontology_terms() -> tuple[set[str], set[str]]:
    text = ONTOLOGY.read_text()
    classes = set(re.findall(r"^kto:(\w+)\s+a owl:Class", text, re.M))
    props = set(re.findall(r"^kto:(\w+)\s+a owl:ObjectProperty", text, re.M))
    return classes, props


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\(.*?\)", " ", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    stop = {"the", "a", "an", "of", "and", "in", "on", "to", "for"}
    return " ".join(w for w in s.split() if w not in stop)


def tokens(s: str) -> set[str]:
    # crude stemming so "superconductors" ~ "superconductivity"
    return {w[:6] if len(w) > 6 else w.rstrip("s") for w in norm(s).split()}


# Words that appear in many labels without saying what the topic is.
BRAND_WORDS = {"salesforce", "sfdc", "force", "com"}


def _stem(w: str) -> str:
    if len(w) > 4 and w.endswith("ies"):
        return w[:-3] + "y"
    if len(w) > 3 and w.endswith("s") and not w.endswith("ss"):
        return w[:-1]
    return w


def label_tokens(s: str) -> list[str]:
    words = norm(s).split()
    return [_stem(w) for w in words if w not in BRAND_WORDS] or [_stem(w) for w in words]


def _token_match(a: str, b: str) -> float:
    """1.0 for equal tokens, partial credit for prefixes (async/asynchronous) and near-spellings."""
    from difflib import SequenceMatcher
    if a == b:
        return 1.0
    if min(len(a), len(b)) >= 5:
        if a.startswith(b) or b.startswith(a):
            return 0.9
        r = SequenceMatcher(None, a, b).ratio()
        if r >= 0.85:
            return r
    return 0.0


class LabelSimilarity:
    """Corpus-aware similarity between two topic labels (titles or aliases), 0..1.

    Score = IDF-weighted soft Jaccard over label tokens. Tokens that occur in many existing
    labels (apex, platform, data, ...) carry little weight, so sharing one of them no longer
    makes two different topics look alike. Whole-string character similarity is used only for
    typo tolerance on long labels, because on short labels it rewards accidental letter overlap
    ("Agentforce" vs "Agentforce Public Sector", "Apex Triggers" vs "Apex governor limits").
    Also scores 1.0 for spacing/hyphen variants (omnichannel = omni-channel) and 0.95 for an
    acronym of the other label (ALM).
    """

    def __init__(self, arts: list[dict]):
        import math
        self._log = math.log
        self.n = len(arts)
        self.df: Counter = Counter()
        for a in arts:
            labels = [a.get("title", "")] + list(a.get("aliases") or [])
            self.df.update({t for x in labels for t in label_tokens(x)})

    def weight(self, t: str) -> float:
        return self._log((self.n + 1) / (self.df.get(t, 0) + 0.5))

    def __call__(self, a: str, b: str) -> float:
        from difflib import SequenceMatcher
        ta, tb = label_tokens(a), label_tokens(b)
        if not ta or not tb:
            return 0.0
        ca, cb = "".join(ta), "".join(tb)
        if ca == cb:
            return 1.0
        for x, y in ((ta, tb), (tb, ta)):
            if len(x) == 1 and len(y) >= 2 and x[0] == "".join(t[0] for t in y):
                return 0.95
        pairs = sorted(((_token_match(x, y), i, j) for i, x in enumerate(ta) for j, y in enumerate(tb)),
                       reverse=True)
        used_a, used_b, matched = set(), set(), 0.0
        for s, i, j in pairs:
            if s and i not in used_a and j not in used_b:
                used_a.add(i)
                used_b.add(j)
                matched += s * (self.weight(ta[i]) + self.weight(tb[j])) / 2
        total = sum(map(self.weight, ta)) + sum(map(self.weight, tb)) - matched
        score = matched / total if total > 0 else 0.0
        if min(len(ca), len(cb)) >= 8:
            r = SequenceMatcher(None, ca, cb).ratio()
            if r >= 0.92:
                score = max(score, r)
        return min(score, 1.0)


def shingles(text: str, k: int = 5) -> set[int]:
    words = norm(re.sub(r"\[\^s\d+\]", " ", text)).split()
    return {hash(" ".join(words[i:i + k])) for i in range(max(0, len(words) - k + 1))}


def jaccard(a: set, b: set) -> float:
    return len(a & b) / len(a | b) if a and b else 0.0


def iri(node_id: str) -> str:
    return BASE + node_id.split(":", 1)[1]


def load_articles() -> tuple[list[dict], list[str]]:
    arts, errors = [], []
    for path in sorted(ARTICLES.rglob("*.md")):
        rel = path.relative_to(ROOT)
        raw = path.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
        if not m:
            errors.append(f"{rel}: missing YAML frontmatter")
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError as e:
            errors.append(f"{rel}: bad YAML: {e}")
            continue
        fm["_path"], fm["_body"] = str(rel), m.group(2)
        arts.append(fm)
    return arts, errors


# ------------------------------------------------------------- validation ---
def validate(arts: list[dict]) -> list[str]:
    classes, props = ontology_terms()
    errs: list[str] = []
    ids: dict[str, str] = {}
    names: list[tuple[str, str, set]] = []

    for a in arts:
        p = a["_path"]
        for f in REQUIRED:
            if not a.get(f):
                errs.append(f"{p}: missing required field '{f}'")
        aid = a.get("id", "")
        if aid and not ID_RE.match(aid):
            errs.append(f"{p}: id '{aid}' must look like kt:lowercase-slug")
        if aid:
            if aid in ids:
                errs.append(f"{p}: duplicate id {aid} (also {ids[aid]})")
            ids[aid] = p
            slug = aid.split(":", 1)[1]
            if Path(p).stem != slug:
                errs.append(f"{p}: filename must be {slug}.md")
            dom = a.get("domain", "")
            if Path(p).parent.name != dom:
                errs.append(f"{p}: must live in articles/{dom}/")
        if a.get("type") and a["type"] not in classes:
            errs.append(f"{p}: type '{a['type']}' not in ontology classes {sorted(classes)}")

        for key in ("broader", "related"):
            for ref in a.get(key) or []:
                if not ID_RE.match(str(ref)):
                    errs.append(f"{p}: {key} ref '{ref}' is not a kt: id")
        for r in a.get("relations") or []:
            if not isinstance(r, dict) or set(r) != {"predicate", "object"}:
                errs.append(f"{p}: each relation needs exactly predicate + object")
                continue
            if r["predicate"] not in props:
                errs.append(f"{p}: predicate '{r['predicate']}' not in ontology (add it to ontology.ttl first)")
            if not ID_RE.match(str(r["object"])):
                errs.append(f"{p}: relation object '{r['object']}' is not a kt: id")

        if a.get("release") and not RELEASE_RE.match(str(a["release"])):
            errs.append(f"{p}: release '{a['release']}' must look like \"Winter '27\"")
        if a.get("status") and a["status"] not in STATUSES:
            errs.append(f"{p}: status '{a['status']}' not in {sorted(STATUSES)}")
        if a.get("status") in {"deprecated", "retired"} and not any(
                r.get("predicate") == "replacedBy" for r in (a.get("relations") or []) if isinstance(r, dict)):
            errs.append(f"{p}: {a['status']} feature should declare a replacedBy relation")

        # --- citations
        srcs = a.get("sources") or []
        sids = set()
        strong = 0
        urls = set()
        for s in srcs:
            if not isinstance(s, dict):
                errs.append(f"{p}: malformed source entry")
                continue
            for f in ("id", "title", "publisher", "url", "type", "accessed"):
                if not s.get(f):
                    errs.append(f"{p}: source {s.get('id', '?')} missing '{f}'")
            if s.get("id"):
                sids.add(s["id"])
            if s.get("url") and not str(s["url"]).startswith("https://"):
                errs.append(f"{p}: source {s.get('id')} url must be https")
            if s.get("url") in urls:
                errs.append(f"{p}: duplicate source url {s.get('url')}")
            urls.add(s.get("url"))
            if s.get("type") not in SOURCE_TYPES:
                errs.append(f"{p}: source {s.get('id')} type '{s.get('type')}' not in {sorted(SOURCE_TYPES)}")
            elif s["type"] in STRONG_SOURCE_TYPES:
                strong += 1
        if len(srcs) < 3:
            errs.append(f"{p}: needs at least 3 sources (has {len(srcs)})")
        if a.get("type") != "ExternalConcept" and not any(
                isinstance(x, dict) and x.get("type") in OFFICIAL_SOURCE_TYPES for x in srcs):
            errs.append(f"{p}: needs at least 1 official Salesforce source ({sorted(OFFICIAL_SOURCE_TYPES)})")
        if strong < 2:
            errs.append(f"{p}: needs at least 2 sources of a strong type {sorted(STRONG_SOURCE_TYPES)}")
        body = a["_body"]
        cited = set(re.findall(r"\[\^(s\d+)\](?!:)", body))
        defined = set(re.findall(r"^\[\^(s\d+)\]:", body, re.M))
        for sid in sids - cited:
            errs.append(f"{p}: source {sid} is never cited in the body")
        for sid in cited - sids:
            errs.append(f"{p}: body cites [^{sid}] but it is not in frontmatter sources")
        for sid in sids - defined:
            errs.append(f"{p}: missing footnote definition [^{sid}]: in the Sources section")
        # every substantive paragraph must carry a citation
        prose = body.split("\n## Sources", 1)[0]
        for para in re.split(r"\n\s*\n", prose):
            t = para.strip()
            if not t or t.startswith("#") or t.startswith(">") or len(t) < 120:
                continue
            if "[^s" not in t:
                errs.append(f"{p}: uncited paragraph: '{t[:70]}...'")
        if len(re.findall(r"\w+", prose)) < 350:
            errs.append(f"{p}: body is under 350 words")

        names.append((p, a.get("title", ""), {norm(x) for x in [a.get("title", "")] + list(a.get("aliases") or [])}))

    # --- uniqueness: titles / aliases
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            pi, ti, ni = names[i]
            pj, tj, nj = names[j]
            if ni & nj:
                errs.append(f"{pi}: title/alias collides with {pj}: {sorted(ni & nj)}")
            elif jaccard(tokens(ti), tokens(tj)) >= TITLE_DUP_THRESHOLD:
                errs.append(f"{pi}: title too similar to {pj} ('{ti}' vs '{tj}')")
    # --- uniqueness: content
    sh = [(a["_path"], shingles(a["_body"])) for a in arts]
    for i in range(len(sh)):
        for j in range(i + 1, len(sh)):
            s = jaccard(sh[i][1], sh[j][1])
            if s >= NEAR_DUP_THRESHOLD:
                errs.append(f"{sh[i][0]}: near-duplicate of {sh[j][0]} (similarity {s:.2f})")
    return errs


# ------------------------------------------------------------------ build ---
def edges(a: dict):
    for b in a.get("broader") or []:
        yield SKOS + "broader", b
    for r in a.get("related") or []:
        yield SKOS + "related", r
    for r in a.get("relations") or []:
        yield KTO + r["predicate"], r["object"]


def lit(s: str) -> str:
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ") + '"'


def build(arts: list[dict]) -> None:
    GRAPH.mkdir(exist_ok=True)
    known = {a["id"] for a in arts}
    triples, nodes, index = [], [], []
    inbound: Counter = Counter()
    frontier: dict[str, list[str]] = defaultdict(list)

    for a in arts:
        s = f"<{iri(a['id'])}>"
        triples += [
            f"{s} <{RDF_TYPE}> <{KTO}{a['type']}> .",
            f"{s} <{RDFS_LABEL}> {lit(a['title'])} .",
            f"{s} <{SKOS}prefLabel> {lit(a['title'])} .",
            f"{s} <{SKOS}definition> {lit(a['summary'])} .",
            f"{s} <{DCT}created> {lit(a['created'])} .",
            f"{s} <{KTO}verifiedRelease> {lit(a['release'])} .",
            f"{s} <{KTO}status> {lit(a['status'])} .",
            f"{s} <{KTO}domain> {lit(a['domain'])} .",
        ]
        for al in a.get("aliases") or []:
            triples.append(f"{s} <{SKOS}altLabel> {lit(al)} .")
        node = {
            "@id": a["id"], "@type": f"kto:{a['type']}", "skos:prefLabel": a["title"],
            "skos:definition": a["summary"], "kto:domain": a["domain"], "dcterms:created": str(a["created"]),
            "kto:verifiedRelease": a["release"], "kto:status": a["status"],
            "prov:wasDerivedFrom": [], "kto:file": a["_path"],
        }
        if a.get("aliases"):
            node["skos:altLabel"] = a["aliases"]
        for pred, obj in edges(a):
            triples.append(f"{s} <{pred}> <{iri(obj)}> .")
            key = pred.replace(SKOS, "skos:").replace(KTO, "kto:")
            node.setdefault(key, []).append({"@id": obj})
            inbound[obj] += 1
            if obj not in known:
                frontier[obj].append(a["id"])
        for src in a["sources"]:
            sid = f"<{BASE}source/{a['id'].split(':', 1)[1]}/{src['id']}>"
            triples += [
                f"{s} <{PROV}wasDerivedFrom> {sid} .",
                f"{sid} <{RDF_TYPE}> <{KTO}Source> .",
                f"{sid} <{DCT}title> {lit(src['title'])} .",
                f"{sid} <{DCT}publisher> {lit(src['publisher'])} .",
                f"{sid} <https://schema.org/url> {lit(src['url'])} .",
                f"{sid} <{KTO}sourceType> {lit(src['type'])} .",
            ]
            node["prov:wasDerivedFrom"].append({"dcterms:title": src["title"], "dcterms:publisher": src["publisher"],
                                                 "schema:url": src["url"], "kto:sourceType": src["type"]})
        nodes.append(node)
        index.append({"id": a["id"], "title": a["title"], "aliases": a.get("aliases") or [], "type": a["type"],
                      "domain": a["domain"], "file": a["_path"], "created": str(a["created"]),
                      "release": a["release"], "status": a["status"], "source_urls": [x["url"] for x in a["sources"]]})

    (GRAPH / "triples.nt").write_text("\n".join(sorted(set(triples))) + "\n")
    ctx = {"kt": BASE, "kto": KTO, "skos": SKOS, "prov": PROV, "dcterms": DCT, "schema": "https://schema.org/",
           "@base": BASE}
    (GRAPH / "graph.jsonld").write_text(json.dumps({"@context": ctx, "@graph": nodes}, indent=2, ensure_ascii=False) + "\n")
    (GRAPH / "index.json").write_text(json.dumps(sorted(index, key=lambda x: x["id"]), indent=2, ensure_ascii=False) + "\n")

    # frontier: referenced-but-unwritten nodes, best candidates for the next article
    fl = sorted(frontier.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    lines = ["# Frontier", "", "Nodes referenced by existing articles but not yet written, ranked by how many "
             "articles point to them. Generated by `scripts/kg.py build`.", ""]
    if fl:
        lines += ["| Node | Referenced by |", "|---|---|"]
        lines += [f"| `{k}` | {', '.join(f'`{x}`' for x in v)} |" for k, v in fl]
    else:
        lines.append("_Empty._")
    (GRAPH / "frontier.md").write_text("\n".join(lines) + "\n")

    # stats + centrality
    by_type = Counter(a["type"] for a in arts)
    by_dom = Counter(a["domain"] for a in arts)
    out = ["# Graph statistics", "", f"- Articles (nodes written): **{len(arts)}**",
           f"- Frontier nodes (referenced, unwritten): **{len(frontier)}**",
           f"- Edges: **{sum(1 for a in arts for _ in edges(a))}**",
           f"- Citations: **{sum(len(a['sources']) for a in arts)}**", ""]
    try:
        import networkx as nx
        g = nx.DiGraph()
        g.add_nodes_from(a["id"] for a in arts)
        for a in arts:
            for _, o in edges(a):
                g.add_edge(a["id"], o)
        if g.number_of_nodes():
            pr = nx.pagerank(g)
            comps = list(nx.weakly_connected_components(g))
            iso = [n for n in known if g.degree(n) == 0]
            out += [f"- Weakly connected components: **{len(comps)}**",
                    f"- Isolated articles (no edges): **{len(iso)}**", "",
                    "## Most central nodes (PageRank)", "", "| Node | PageRank | Written |", "|---|---|---|"]
            out += [f"| `{n}` | {v:.4f} | {'yes' if n in known else 'no'} |"
                    for n, v in sorted(pr.items(), key=lambda kv: -kv[1])[:15]]
            try:
                comms = nx.algorithms.community.louvain_communities(g.to_undirected(), seed=42)
                out += ["", f"## Communities (Louvain): {len(comms)}", ""]
                for i, c in enumerate(sorted(comms, key=len, reverse=True)[:10], 1):
                    out.append(f"{i}. " + ", ".join(f"`{x}`" for x in sorted(c)[:12]) + (" …" if len(c) > 12 else ""))
            except Exception:
                pass
            out.append("")
    except ImportError:
        out += ["_(install networkx for centrality and community metrics)_", ""]
    out += ["## By type", ""] + [f"- {k}: {v}" for k, v in sorted(by_type.items())]
    out += ["", "## By domain", ""] + [f"- {k}: {v}" for k, v in sorted(by_dom.items())]
    out += ["", "## By verified release (oldest = most likely stale)", ""]
    out += [f"- {k}: {v}" for k, v in sorted(Counter(a["release"] for a in arts).items(), key=lambda kv: release_key(kv[0]))]
    out += ["", "## By status", ""] + [f"- {k}: {v}" for k, v in sorted(Counter(a["status"] for a in arts).items())]
    (GRAPH / "stats.md").write_text("\n".join(out) + "\n")


def release_key(r: str) -> tuple[int, int]:
    m = re.match(r"(Spring|Summer|Winter) '(\d{2})", str(r))
    if not m:
        return (0, 0)
    # Winter 'YY ships in the autumn of the previous calendar year
    order = {"Winter": 0, "Spring": 1, "Summer": 2}
    return (int(m.group(2)), order[m.group(1)])


CONTENT_STOPWORDS = set("""a an the of and or in on to for is are was were be been by with as at from that this
these those it its can cannot not no into than then when which who what how why also only each per more most other
such so if but their them they you your one two use used uses using up out has have had do does may must will would
should via all any both every within without about over under between across after before while""".split())


def content_text(a: dict) -> str:
    """Title, summary and body prose, minus the Sources list, footnote markers and node ids."""
    body = re.split(r"^## Sources\b", a.get("_body", ""), flags=re.M)[0]
    body = re.sub(r"\[\^s\d+\]", " ", body)
    body = re.sub(r"`?kt:[a-z0-9-]+`?", " ", body)
    return " ".join([str(a.get("title", "")), str(a.get("summary", "")), body])


def content_terms(text: str) -> list[str]:
    return [_stem(w) for w in norm(text).split() if w not in CONTENT_STOPWORDS and len(w) > 2 and not w.isdigit()]


class ContentSimilarity:
    """TF-IDF cosine between an article draft and the existing articles, 0..1.

    Unlike the build's shingle check (which only catches reused phrasing), this compares
    vocabulary, so it also flags the same subject written in fresh words or under another name.
    Linked neighbours share vocabulary by design, so scores are a prompt to review, not a verdict.
    """

    def __init__(self, arts: list[dict]):
        import math
        self._math = math
        counts = {a["id"]: Counter(content_terms(content_text(a))) for a in arts if a.get("id")}
        self.n = len(counts)
        self.df = Counter(t for c in counts.values() for t in c)
        self.vectors = {i: self.vector(c) for i, c in counts.items()}

    def vector(self, counts: Counter) -> dict[str, float]:
        m = self._math
        v = {t: (1 + m.log(f)) * (m.log((self.n + 1) / (self.df.get(t, 0) + 1)) + 1) for t, f in counts.items()}
        length = m.sqrt(sum(x * x for x in v.values())) or 1.0
        return {t: x / length for t, x in v.items()}

    def scores(self, draft: dict) -> list[tuple[float, str]]:
        v = self.vector(Counter(content_terms(content_text(draft))))
        out = []
        for i, u in self.vectors.items():
            if i == draft.get("id"):
                continue
            a, b = (v, u) if len(v) < len(u) else (u, v)
            out.append((sum(x * b.get(t, 0.0) for t, x in a.items()), i))
        return sorted(out, reverse=True)


def label_scores(query: str, arts: list[dict], exclude: str | None = None) -> list[tuple[float, str, str]]:
    label_sim = LabelSimilarity([a for a in arts if a.get("id") != exclude])
    scored = []
    for a in arts:
        if a.get("id") == exclude:
            continue
        labels = [a.get("title", "")] + list(a.get("aliases") or [])
        best = max(label_sim(query, x) for x in labels)
        if norm(query) in {norm(x) for x in labels}:
            best = 1.0
        scored.append((best, a.get("id"), a.get("title")))
    return sorted(scored, reverse=True)


def read_draft(path: str) -> dict:
    raw = Path(path).read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    if not m:
        sys.exit(f"{path}: missing YAML frontmatter")
    fm = yaml.safe_load(m.group(1)) or {}
    fm["_body"] = m.group(2)
    return fm


def similar(query: str, arts: list[dict]) -> None:
    hits = [x for x in label_scores(query, arts) if x[0] > 0][:10]
    if not hits:
        print("No similar articles. Topic looks unique.")
    for s, i, t in hits:
        print(f"{s:.2f}  {i}  {t}")


def similar_draft(path: str, arts: list[dict]) -> int:
    """Check a written draft: its title/aliases by name, and its text by content. Exit 1 if review needed."""
    draft = read_draft(path)
    titles = {a["id"]: a.get("title") for a in arts}
    flagged = False
    print("Name (title and aliases), threshold 0.50:")
    best_by_id: dict[str, float] = {}
    for label in [draft.get("title", "")] + list(draft.get("aliases") or []):
        for s, i, _ in label_scores(label, arts, exclude=draft.get("id")):
            best_by_id[i] = max(s, best_by_id.get(i, 0.0))
    for i, s in [x for x in sorted(best_by_id.items(), key=lambda x: -x[1]) if x[1] > 0][:5]:
        flag = "  <- REVIEW" if s >= 0.5 else ""
        flagged |= s >= 0.5
        print(f"  {s:.2f}  {i}  {titles.get(i)}{flag}")
    print(f"Content (TF-IDF cosine), threshold {CONTENT_REVIEW_THRESHOLD:.2f}:")
    for s, i in ContentSimilarity(arts).scores(draft)[:5]:
        flag = "  <- REVIEW" if s >= CONTENT_REVIEW_THRESHOLD else ""
        flagged |= s >= CONTENT_REVIEW_THRESHOLD
        print(f"  {s:.2f}  {i}  {titles.get(i)}{flag}")
    print("Review flagged articles: same subject -> drop the draft; parent/child or neighbour -> keep and link it."
          if flagged else "No article flagged. Draft looks unique.")
    return 1 if flagged else 0


def main() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    arts, errs = load_articles()
    if cmd == "similar":
        if len(sys.argv) > 3 and sys.argv[2] == "--draft":
            return similar_draft(sys.argv[3], arts)
        similar(" ".join(sys.argv[2:]), arts)
        return 0
    errs += validate(arts) if not errs else []
    if errs:
        print(f"{len(errs)} problem(s):")
        for e in errs:
            print("  -", e)
        return 1
    print(f"OK: {len(arts)} article(s) valid.")
    if cmd == "build":
        build(arts)
        print("Graph regenerated in graph/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
