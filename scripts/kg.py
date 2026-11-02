#!/usr/bin/env python3
"""Salesforce Knowledge Graph builder and validator.

Usage:
  python3 scripts/kg.py check            # validate only (exit 1 on errors)
  python3 scripts/kg.py build            # validate, then regenerate graph/
  python3 scripts/kg.py similar "Title" [--current "Spring '27"]
                                         # find existing articles close to a candidate topic;
                                         # matches verified against an older release are flagged STALE
  python3 scripts/kg.py stale [--current "Spring '27"] [--next-release-date 2027-06-14] [--domain integration]
                                         # list stale articles, stalest first, and the suggested
                                         # refresh batch for this run (adaptive, 1-4 articles)

Articles live in articles/<domain>/<slug>.md with YAML frontmatter (see SCHEMA.md).
Generated outputs (never hand-edit): graph/graph.jsonld, graph/triples.nt,
graph/index.json, graph/frontier.md, graph/stats.md.
"""
from __future__ import annotations

import json
import re
import sys
import math
import unicodedata
from datetime import date, datetime, timedelta, timezone
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


SPELLING_SIM_THRESHOLD = 0.85  # char ratio counts only for near-identical spellings


def label_sim(a: str, b: str) -> float:
    # Word overlap is the main signal. Character-level similarity only counts when it is very
    # high (typos, punctuation or plural variants); below that it matches unrelated short titles,
    # e.g. "Apex Triggers" vs "save order" scored 0.52 with no words in common.
    from difflib import SequenceMatcher
    word = jaccard(tokens(a), tokens(b))
    char = SequenceMatcher(None, norm(a), norm(b)).ratio()
    return max(word, char if char >= SPELLING_SIM_THRESHOLD else 0.0)


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


def similar(query: str, arts: list[dict], current: str | None = None) -> None:
    # Reference release: the one passed in, else the newest release any article is stamped with.
    if not current:
        current = max((a.get("release", "") for a in arts), key=release_key, default="")
    cur_key = release_key(current)
    scored = []
    for a in arts:
        labels = [a.get("title", "")] + list(a.get("aliases") or [])
        best = max(label_sim(query, x) for x in labels)
        if norm(query) in {norm(x) for x in labels}:
            best = 1.0
        scored.append((best, a.get("id"), a.get("title"), a.get("release", "")))
    hits = [x for x in sorted(scored, reverse=True) if x[0] > 0][:10]
    print(f"Current release: {current or 'unknown'}")
    if not hits:
        print("No similar articles. Topic looks unique.")
    for s, i, t, r in hits:
        flag = "  STALE" if release_key(r) < cur_key else ""
        print(f"{s:.2f}  {i}  {t}  [{r}]{flag}")


MAX_REFRESH_BATCH = 4
# Approximate production GA month/day per release, used only when --next-release-date isn't given.
APPROX_GA = {"Spring": (2, 15), "Summer": (6, 15), "Winter": (10, 15)}


def next_release(current: str) -> str:
    m = re.match(r"(Spring|Summer|Winter) '(\d{2})", current)
    season, yy = m.group(1), int(m.group(2))
    return {"Winter": f"Spring '{yy:02d}", "Spring": f"Summer '{yy:02d}", "Summer": f"Winter '{yy + 1:02d}"}[season]


def approx_ga_date(release: str) -> date:
    m = re.match(r"(Spring|Summer|Winter) '(\d{2})", release)
    season, yy = m.group(1), int(m.group(2))
    year = 2000 + yy - (1 if season == "Winter" else 0)  # Winter 'YY ships in autumn of the prior year
    mo, d = APPROX_GA[season]
    return date(year, mo, d)


def remaining_odd_runs(until: date, now: datetime | None = None) -> int:
    now = now or datetime.now(timezone.utc)
    end = datetime(until.year, until.month, until.day, tzinfo=timezone.utc)
    hours = max(0, int((end - now).total_seconds() // 3600))
    return max(1, hours // 2)


def stale(arts: list[dict], current: str | None = None, domain: str | None = None,
          next_date: date | None = None) -> None:
    if not current:
        current = max((a.get("release", "") for a in arts), key=release_key, default="")
    cur_key = release_key(current)
    rows = []
    for a in arts:
        if domain and a.get("domain") != domain:
            continue
        if release_key(a.get("release", "")) < cur_key:
            accessed = min((str(x.get("accessed", "")) for x in a.get("sources") or []), default="")
            rows.append((release_key(a["release"]), accessed, a["id"], a.get("title", ""), a["release"], a.get("domain", "")))
    rows.sort()
    print(f"Current release: {current or 'unknown'}")
    if not rows:
        print("No stale articles.")
        return
    for _, acc, i, t, r, d in rows:
        print(f"{r:<12} {acc:<10}  {i}  {t}  ({d})")

    # Adaptive batch: enough per odd-hour run to clear the backlog before the next release, capped.
    nxt = next_release(current)
    estimated = next_date is None
    next_date = next_date or approx_ga_date(nxt)
    runs = remaining_odd_runs(next_date)
    needed = math.ceil(len(rows) / runs)
    size = max(1, min(MAX_REFRESH_BATCH, needed))

    # Pair related work: start with the stalest article, then prefer articles linked to it,
    # then ones in the same domain, then the rest in staleness order.
    by_id = {a["id"]: a for a in arts}
    top = rows[0]
    top_links = {o for _, o in edges(by_id[top[2]])}

    def pref(idx_row):
        idx, row = idx_row
        linked = row[2] in top_links or top[2] in {o for _, o in edges(by_id[row[2]])}
        return (0 if linked else 1 if row[5] == top[5] else 2, idx)

    rest = sorted(list(enumerate(rows))[1:], key=pref)
    batch = [top] + [r for _, r in rest[: size - 1]]

    print()
    print(f"Next release: {nxt}, GA {next_date.isoformat()}{' (estimated)' if estimated else ''}; "
          f"{runs} odd-hour run(s) left; {len(rows)} stale -> {needed} needed per run")
    if needed > MAX_REFRESH_BATCH:
        print(f"WARNING: backlog won't clear before {nxt} at the cap of {MAX_REFRESH_BATCH} per run.")
    print(f"Refresh batch for this run ({size}):")
    for _, acc, i, t, r, d in batch:
        print(f"  {i}  {t}  ({d})")


def opt(args: list[str], name: str) -> tuple[str | None, list[str]]:
    if name not in args:
        return None, args
    k = args.index(name)
    val = args[k + 1] if k + 1 < len(args) else None
    return val, args[:k] + args[k + 2:]


def main() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    arts, errs = load_articles()
    if cmd == "stale":
        current, args = opt(sys.argv[2:], "--current")
        domain, args = opt(args, "--domain")
        nd, args = opt(args, "--next-release-date")
        try:
            next_date = date.fromisoformat(nd) if nd else None
        except ValueError:
            print("--next-release-date needs YYYY-MM-DD")
            return 2
        if "--current" in sys.argv and (not current or not RELEASE_RE.match(current)):
            print("--current needs a release like \"Spring '27\"")
            return 2
        stale(arts, current, domain, next_date)
        return 0
    if cmd == "similar":
        args = sys.argv[2:]
        current = None
        if "--current" in args:
            k = args.index("--current")
            if k + 1 >= len(args) or not RELEASE_RE.match(args[k + 1]):
                print("--current needs a release like \"Spring '27\"")
                return 2
            current = args[k + 1]
            args = args[:k] + args[k + 2:]
        similar(" ".join(args), arts, current)
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
