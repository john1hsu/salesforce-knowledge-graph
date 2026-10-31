#!/usr/bin/env python3
"""Render the knowledge graph as a static website (GitHub Pages).

Usage:
  python3 scripts/site.py            # writes the site to _site/
  python3 scripts/site.py out_dir    # writes it somewhere else

Reads the same articles as scripts/kg.py and never modifies them. The output is
plain HTML/CSS/JS: an index with search, one page per article (with typed edges
and back-links), one page per domain, the frontier, and an interactive graph.
"""
from __future__ import annotations

import html
import json
import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kg  # noqa: E402

try:
    import markdown
except ImportError:  # pragma: no cover
    sys.exit("markdown missing: pip install markdown --break-system-packages")

REPO_URL = "https://github.com/john1hsu/salesforce-knowledge-graph"
SITE_TITLE = "Salesforce Knowledge Graph"
VENDOR = Path(__file__).resolve().parent / "vendor"  # d3 v7.9.0 (ISC), vendored so the site has no CDN dependency

PRED_LABELS = {
    "broader": "Broader", "related": "Related", "partOf": "Part of", "hasPart": "Has part",
    "dependsOn": "Depends on", "enables": "Enables", "integratesWith": "Integrates with",
    "replacedBy": "Replaced by", "replaces": "Replaces", "alternativeTo": "Alternative to",
    "governedBy": "Governed by", "implements": "Implements", "mitigates": "Mitigates",
    "causes": "Causes", "configuredVia": "Configured via", "queriedWith": "Queried with",
    "requiresLicense": "Requires license", "introducedIn": "Introduced in", "coveredBy": "Covered by",
    "usedBy": "Used by", "acquiredBy": "Acquired by", "contrastsWith": "Contrasts with",
    "instanceOf": "Instance of",
}

e = html.escape


def slug(node_id: str) -> str:
    return node_id.split(":", 1)[1]


def humanize(s: str) -> str:
    return s.replace("-", " ").replace("_", " ").strip().capitalize()


def domain_label(d: str) -> str:
    small = {"and", "of", "in", "to"}
    words = d.split("-")
    out = []
    for i, w in enumerate(words):
        if w in {"ai", "alm"}:
            out.append(w.upper())
        elif w in small and i:
            out.append(w)
        else:
            out.append(w.capitalize())
    return " ".join(out)


CSS = """
:root{--bg:#f7f8fa;--panel:#fff;--text:#1b1f24;--muted:#5b6470;--line:#e2e6eb;--accent:#0b5cab;--accent-soft:#e8f1fb;
--warn:#8a5a00;--warn-soft:#fff4dc;--ok:#1e6b3a;--ok-soft:#e5f5ea;--code:#f0f2f5;--shadow:0 1px 2px rgba(0,0,0,.05)}
@media (prefers-color-scheme:dark){:root{--bg:#0f1216;--panel:#171b21;--text:#e6e9ee;--muted:#9aa3ae;--line:#2a3039;
--accent:#6cb2ff;--accent-soft:#16283d;--warn:#f0c46b;--warn-soft:#33290f;--ok:#7fd69b;--ok-soft:#14301f;--code:#222831;--shadow:none}}
article.body>:first-child{margin-top:0}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--text);font:16px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
header.top{background:var(--panel);border-bottom:1px solid var(--line)}
header.top .in{max-width:1120px;margin:0 auto;padding:12px 16px;display:flex;gap:20px;align-items:center;flex-wrap:wrap}
header.top .brand{font-weight:700;color:var(--text);font-size:17px}
header.top nav{display:flex;gap:16px;flex-wrap:wrap;font-size:15px}
main{max-width:1120px;margin:0 auto;padding:24px 16px 64px}
h1{font-size:30px;line-height:1.2;margin:0 0 8px}h2{font-size:21px;margin:32px 0 10px}h3{font-size:17px}
.lede{color:var(--muted);font-size:17px;margin:0 0 20px;max-width:760px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px 16px;box-shadow:var(--shadow)}
.card h3{margin:0 0 4px;font-size:16px}.card p{margin:4px 0 0;color:var(--muted);font-size:14px}
.stats{display:flex;gap:12px;flex-wrap:wrap;margin:0 0 24px}
.stat{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:10px 16px;min-width:120px}
.stat b{display:block;font-size:24px}.stat span{color:var(--muted);font-size:13px}
.chips{display:flex;gap:6px;flex-wrap:wrap;margin:6px 0 0}
.chip{display:inline-block;font-size:12px;padding:2px 8px;border-radius:999px;background:var(--accent-soft);color:var(--accent);white-space:nowrap}
.chip.muted{background:var(--code);color:var(--muted)}.chip.warn{background:var(--warn-soft);color:var(--warn)}.chip.ok{background:var(--ok-soft);color:var(--ok)}
input.search{width:100%;max-width:560px;font:inherit;padding:10px 14px;border:1px solid var(--line);border-radius:8px;background:var(--panel);color:var(--text);margin:0 0 20px}
.layout{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:32px}
@media (max-width:860px){.layout{grid-template-columns:1fr}}
article.body{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:24px 28px;box-shadow:var(--shadow);min-width:0}
@media (max-width:600px){article.body{padding:18px 16px}}
article.body p,article.body li{max-width:72ch}
article.body code{background:var(--code);padding:1px 5px;border-radius:4px;font-size:.9em}
article.body table{border-collapse:collapse;display:block;overflow-x:auto}article.body td,article.body th{border:1px solid var(--line);padding:6px 10px}
sup.cite a{font-size:11px;padding:0 2px}
aside .box{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:14px 16px;margin-bottom:16px}
aside h4{margin:0 0 8px;font-size:13px;text-transform:uppercase;letter-spacing:.04em;color:var(--muted)}
aside dl{margin:0;display:grid;grid-template-columns:auto 1fr;gap:4px 12px;font-size:14px}aside dt{color:var(--muted)}aside dd{margin:0}
aside ul{list-style:none;margin:0;padding:0;font-size:14px}aside li{margin:3px 0}
.edge-group{margin-bottom:10px}.edge-group b{display:block;font-size:12px;color:var(--muted);font-weight:600}
.unwritten{color:var(--muted)}.unwritten::after{content:" ·  not yet written";font-size:11px}
ol.sources{font-size:14px;padding-left:22px}ol.sources li{margin:6px 0;word-break:break-word}ol.sources li:target{background:var(--accent-soft)}
.src-meta{color:var(--muted)}
table.list{width:100%;border-collapse:collapse;background:var(--panel);border:1px solid var(--line);border-radius:10px;overflow:hidden;font-size:15px}
table.list th,table.list td{text-align:left;padding:8px 12px;border-bottom:1px solid var(--line);vertical-align:top}
table.list th{font-size:13px;color:var(--muted);font-weight:600}
.tablewrap{overflow-x:auto}
#graph{width:100%;height:72vh;min-height:420px;background:var(--panel);border:1px solid var(--line);border-radius:12px;display:block}
#graph text{font-size:11px;fill:var(--text);pointer-events:none}
.legend{display:flex;gap:14px;flex-wrap:wrap;font-size:13px;color:var(--muted);margin:10px 0}
.legend i{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:5px;vertical-align:middle}
footer{max-width:1120px;margin:0 auto;padding:0 16px 32px;color:var(--muted);font-size:13px}
.breadcrumb{font-size:14px;color:var(--muted);margin-bottom:8px}
"""


def page(title: str, body: str, root: str, active: str = "", extra_head: str = "") -> str:
    nav = [("index.html", "Articles", "home"), ("graph.html", "Graph", "graph"),
           ("frontier.html", "Frontier", "frontier"), ("about.html", "About", "about")]
    links = "".join(
        f'<a href="{root}{h}"{" aria-current=page" if k == active else ""}>{t}</a>' for h, t, k in nav
    ) + f'<a href="{REPO_URL}">GitHub</a>'
    full = SITE_TITLE if title == SITE_TITLE else f"{title} · {SITE_TITLE}"
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(full)}</title><link rel="stylesheet" href="{root}style.css">{extra_head}</head>
<body><header class="top"><div class="in"><a class="brand" href="{root}index.html">{SITE_TITLE}</a><nav>{links}</nav></div></header>
<main>{body}</main>
<footer>Generated from <a href="{REPO_URL}">{REPO_URL.split('github.com/')[1]}</a> by <code>scripts/site.py</code>.
Every article is citation-backed; check the sources for the latest limits.</footer></body></html>
"""


def status_chip(status: str) -> str:
    cls = {"current": "ok", "deprecated": "warn", "retired": "warn", "beta": "warn", "pilot": "warn"}.get(status, "muted")
    return f'<span class="chip {cls}">{e(status)}</span>'


def render_body(a: dict, written: dict, root: str) -> str:
    body = a["_body"]
    body = re.sub(r"^# .*\n", "", body, count=1, flags=re.M)              # title rendered separately
    body = re.split(r"^## Sources\s*$", body, maxsplit=1, flags=re.M)[0]   # sources rendered from frontmatter
    body = re.sub(r"^\[\^s\d+\]:.*$", "", body, flags=re.M)

    def link_id(m: re.Match) -> str:
        nid = m.group(1)
        if nid in written:
            return f'[{written[nid]["title"]}]({root}articles/{slug(nid)}.html)'
        return m.group(0)

    body = re.sub(r"`(kt:[a-z0-9-]+)`", link_id, body)
    out = markdown.markdown(body, extensions=["tables", "sane_lists"])
    out = re.sub(r"\[\^(s\d+)\]", r'<sup class="cite"><a href="#src-\1">[\1]</a></sup>', out)
    return out


def node_link(nid: str, written: dict, root: str) -> str:
    if nid in written:
        return f'<a href="{root}articles/{slug(nid)}.html">{e(written[nid]["title"])}</a>'
    return f'<span class="unwritten">{e(humanize(slug(nid)))}</span>'


def out_edges(a: dict) -> list[tuple[str, str]]:
    res = [("broader", b) for b in a.get("broader") or []]
    res += [("related", r) for r in a.get("related") or []]
    res += [(r["predicate"], r["object"]) for r in a.get("relations") or []]
    return res


def card(a: dict, root: str) -> str:
    return (f'<div class="card" data-search="{e((a["title"] + " " + " ".join(a.get("aliases") or []) + " " + a["summary"]).lower())}">'
            f'<h3><a href="{root}articles/{slug(a["id"])}.html">{e(a["title"])}</a></h3>'
            f'<p>{e(a["summary"].strip())}</p><div class="chips"><span class="chip">{e(a["type"])}</span>'
            f'<span class="chip muted">{e(domain_label(a["domain"]))}</span>{status_chip(a["status"])}</div></div>')


SEARCH_JS = """<script>
const q=document.getElementById('q');q&&q.addEventListener('input',()=>{const v=q.value.trim().toLowerCase();
document.querySelectorAll('[data-search]').forEach(c=>{c.style.display=!v||c.dataset.search.includes(v)?'':'none'});
document.querySelectorAll('section.domain').forEach(s=>{s.style.display=[...s.querySelectorAll('[data-search]')].some(c=>c.style.display!=='none')?'':'none'})});
</script>"""


def main() -> int:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else kg.ROOT / "_site"
    arts, errs = kg.load_articles()
    if errs:
        print("\n".join(errs))
        return 1
    try:
        import yaml
        seeds = yaml.safe_load((kg.ROOT / "topics" / "seeds.yaml").read_text())["domains"]
    except Exception:
        seeds = {}

    written = {a["id"]: a for a in arts}
    by_domain: dict[str, list] = defaultdict(list)
    for a in arts:
        by_domain[a["domain"]].append(a)
    incoming: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for a in arts:
        for p, t in out_edges(a):
            incoming[t].append((p, a["id"]))
    frontier = sorted(((t, srcs) for t, srcs in incoming.items() if t not in written),
                      key=lambda x: (-len({s for _, s in x[1]}), x[0]))

    if out.exists():
        shutil.rmtree(out)
    (out / "articles").mkdir(parents=True)
    (out / "domains").mkdir()
    (out / "data").mkdir()
    (out / "style.css").write_text(CSS)
    (out / ".nojekyll").write_text("")
    for f in ["graph.jsonld", "triples.nt", "index.json"]:
        if (kg.GRAPH / f).exists():
            shutil.copy(kg.GRAPH / f, out / "data" / f)
    shutil.copy(kg.ONTOLOGY, out / "data" / "ontology.ttl")
    shutil.copy(VENDOR / "d3.min.js", out / "d3.min.js")

    domains = sorted(set(seeds) | set(by_domain), key=lambda d: (-len(by_domain.get(d, [])), d))
    n_edges = sum(len(out_edges(a)) for a in arts)
    n_src = sum(len(a.get("sources") or []) for a in arts)

    # ---- index
    sections = []
    for d in domains:
        items = sorted(by_domain.get(d, []), key=lambda a: a["title"].lower())
        if not items:
            continue
        sections.append(f'<section class="domain"><h2><a href="domains/{d}.html">{e(domain_label(d))}</a> '
                        f'<span class="chip muted">{len(items)}</span></h2><div class="grid">'
                        + "".join(card(a, "") for a in items) + "</div></section>")
    releases = sorted({a["release"] for a in arts}, key=kg.release_key)
    idx = (f'<h1>{SITE_TITLE}</h1><p class="lede">A citation-backed knowledge graph of the Salesforce ecosystem. '
           f'Each article is a node with typed edges to related concepts, verified against a named Salesforce release.</p>'
           f'<div class="stats"><div class="stat"><b>{len(arts)}</b><span>articles</span></div>'
           f'<div class="stat"><b>{n_edges}</b><span>edges</span></div>'
           f'<div class="stat"><b>{n_src}</b><span>citations</span></div>'
           f'<div class="stat"><b>{len(frontier)}</b><span>frontier topics</span></div>'
           f'<div class="stat"><b>{e(releases[-1] if releases else "–")}</b><span>latest release</span></div></div>'
           f'<input id="q" class="search" type="search" placeholder="Search titles, aliases and summaries…" aria-label="Search articles">'
           + "".join(sections))
    (out / "index.html").write_text(page(SITE_TITLE, idx + SEARCH_JS, "", "home"))

    # ---- domain pages
    for d in domains:
        items = sorted(by_domain.get(d, []), key=lambda a: a["title"].lower())
        seed_list = seeds.get(d) or []
        seed_html = "".join(
            f'<li>{node_link("kt:" + s, written, "../")}</li>' for s in seed_list)
        body = (f'<div class="breadcrumb"><a href="../index.html">Articles</a> / Domain</div>'
                f'<h1>{e(domain_label(d))}</h1><p class="lede">{len(items)} article(s) written.</p>'
                + (f'<div class="grid">{"".join(card(a, "../") for a in items)}</div>' if items else "<p>No articles yet.</p>")
                + (f'<h2>Seed topics</h2><ul>{seed_html}</ul>' if seed_list else ""))
        (out / "domains" / f"{d}.html").write_text(page(domain_label(d), body, "../"))

    # ---- article pages
    for a in arts:
        groups: dict[str, list[str]] = defaultdict(list)
        for p, t in out_edges(a):
            groups[p].append(t)
        edge_html = "".join(
            f'<div class="edge-group"><b>{e(PRED_LABELS.get(p, p))}</b><ul>'
            + "".join(f"<li>{node_link(t, written, '../')}</li>" for t in ts) + "</ul></div>"
            for p, ts in groups.items())
        back = sorted({s for _, s in incoming.get(a["id"], [])}, key=lambda s: written[s]["title"].lower())
        back_html = "".join(f"<li>{node_link(s, written, '../')}</li>" for s in back) or "<li class='src-meta'>None yet</li>"
        srcs = "".join(
            f'<li id="src-{e(s["id"])}"><a href="{e(s["url"])}" rel="noopener">{e(s["title"])}</a> '
            f'<span class="src-meta">— {e(s.get("publisher", ""))} · {e(s.get("type", ""))} · accessed {e(str(s.get("accessed", "")))}</span></li>'
            for s in a.get("sources") or [])
        aliases = ", ".join(e(x) for x in a.get("aliases") or []) or "–"
        github_file = f'{REPO_URL}/blob/main/{a["_path"]}'
        body = (f'<div class="breadcrumb"><a href="../index.html">Articles</a> / '
                f'<a href="../domains/{a["domain"]}.html">{e(domain_label(a["domain"]))}</a></div>'
                f'<h1>{e(a["title"])}</h1><p class="lede">{e(a["summary"].strip())}</p>'
                f'<div class="layout"><article class="body">{render_body(a, written, "../")}'
                f'<h2>Sources</h2><ol class="sources">{srcs}</ol></article>'
                f'<aside><div class="box"><h4>Node</h4><dl><dt>Type</dt><dd>{e(a["type"])}</dd>'
                f'<dt>Domain</dt><dd><a href="../domains/{a["domain"]}.html">{e(domain_label(a["domain"]))}</a></dd>'
                f'<dt>Status</dt><dd>{status_chip(a["status"])}</dd><dt>Release</dt><dd>{e(a["release"])}</dd>'
                f'<dt>Created</dt><dd>{e(str(a["created"]))}</dd><dt>Aliases</dt><dd>{aliases}</dd>'
                f'<dt>Id</dt><dd><code>{e(a["id"])}</code></dd></dl>'
                f'<p style="margin:10px 0 0;font-size:13px"><a href="{github_file}">View source on GitHub</a></p></div>'
                f'<div class="box"><h4>Connections</h4>{edge_html or "<p>None</p>"}</div>'
                f'<div class="box"><h4>Referenced by</h4><ul>{back_html}</ul></div></aside></div>')
        (out / "articles" / f"{slug(a['id'])}.html").write_text(page(a["title"], body, "../"))

    # ---- frontier
    rows = "".join(
        f'<tr><td>{e(humanize(slug(t)))}<br><code style="font-size:12px">{e(t)}</code></td><td>{len({s for _, s in srcs})}</td>'
        f'<td>{", ".join(node_link(s, written, "") for s in sorted({s for _, s in srcs}))}</td></tr>'
        for t, srcs in frontier)
    fbody = (f'<h1>Frontier</h1><p class="lede">Topics that existing articles link to but nobody has written yet, '
             f'ranked by how many articles point to them. The hourly run turns these into articles.</p>'
             f'<div class="tablewrap"><table class="list"><thead><tr><th>Topic</th><th>Refs</th><th>Referenced by</th></tr></thead>'
             f'<tbody>{rows}</tbody></table></div>')
    (out / "frontier.html").write_text(page("Frontier", fbody, "", "frontier"))

    # ---- graph
    nodes = [{"id": a["id"], "label": a["title"], "domain": a["domain"], "written": True,
              "url": f"articles/{slug(a['id'])}.html"} for a in arts]
    nodes += [{"id": t, "label": humanize(slug(t)), "domain": "", "written": False} for t, _ in frontier]
    links = [{"source": a["id"], "target": t, "p": PRED_LABELS.get(p, p)} for a in arts for p, t in out_edges(a)]
    gdata = json.dumps({"nodes": nodes, "links": links, "domains": [d for d in domains if by_domain.get(d)]})
    gbody = ("<h1>Graph</h1><p class=\"lede\">Filled circles are written articles, coloured by domain; hollow circles are "
             "frontier topics. Drag to rearrange, scroll to zoom, click a filled node to open it.</p>"
             '<div class="legend" id="legend"></div><svg id="graph" role="img" aria-label="Knowledge graph"></svg>'
             f"<script>const DATA={gdata};</script>" + GRAPH_JS)
    (out / "graph.html").write_text(page("Graph", gbody, "", "graph", '<script src="d3.min.js"></script>'))

    # ---- about
    readme = (kg.ROOT / "README.md").read_text(encoding="utf-8")
    about = markdown.markdown(readme, extensions=["tables", "fenced_code"])
    about += ('<h2>Downloads</h2><ul><li><a href="data/graph.jsonld">graph.jsonld</a> (JSON-LD)</li>'
              '<li><a href="data/triples.nt">triples.nt</a> (N-Triples)</li><li><a href="data/index.json">index.json</a></li>'
              '<li><a href="data/ontology.ttl">ontology.ttl</a></li></ul>')
    (out / "about.html").write_text(page("About", f'<article class="body">{about}</article>', "", "about"))

    print(f"Site written to {out} ({len(arts)} articles, {len(frontier)} frontier topics).")
    return 0


GRAPH_JS = """<script>
(function(){
const svg=d3.select('#graph'),el=svg.node();
const pal=['#0b5cab','#d4572a','#2e8b57','#8e44ad','#c0392b','#16a085','#b7950b','#5d6d7e','#e67e22','#2980b9','#7d3c98','#1abc9c'];
const color=d3.scaleOrdinal(DATA.domains,pal);
const lg=document.getElementById('legend');
DATA.domains.forEach(d=>{const s=document.createElement('span');s.innerHTML='<i style="background:'+color(d)+'"></i>'+d.replace(/-/g,' ');lg.appendChild(s)});
const w=()=>el.clientWidth,h=()=>el.clientHeight;
const g=svg.append('g');
const zoom=d3.zoom().scaleExtent([.2,4]).on('zoom',ev=>g.attr('transform',ev.transform));svg.call(zoom);
let fitted=false;const fit=()=>{const b=g.node().getBBox();if(!b.width)return;const s=Math.min(2,.92*Math.min(w()/b.width,h()/b.height));
svg.transition().duration(fitted?0:500).call(zoom.transform,d3.zoomIdentity.translate(w()/2-s*(b.x+b.width/2),h()/2-s*(b.y+b.height/2)).scale(s));fitted=true};
const sim=d3.forceSimulation(DATA.nodes).force('link',d3.forceLink(DATA.links).id(d=>d.id).distance(70))
 .force('charge',d3.forceManyBody().strength(-220)).force('center',d3.forceCenter(w()/2,h()/2)).force('collide',d3.forceCollide(18));
const link=g.append('g').attr('stroke','currentColor').attr('stroke-opacity',.25).style('color','var(--muted)')
 .selectAll('line').data(DATA.links).join('line');
link.append('title').text(d=>d.p);
const node=g.append('g').selectAll('g').data(DATA.nodes).join('g').style('cursor',d=>d.written?'pointer':'grab')
 .call(d3.drag().on('start',(ev,d)=>{if(!ev.active)sim.alphaTarget(.3).restart();d.fx=d.x;d.fy=d.y})
 .on('drag',(ev,d)=>{d.fx=ev.x;d.fy=ev.y}).on('end',(ev,d)=>{if(!ev.active)sim.alphaTarget(0);d.fx=null;d.fy=null}));
node.append('circle').attr('r',d=>d.written?9:6).attr('fill',d=>d.written?color(d.domain):'var(--panel)')
 .attr('stroke',d=>d.written?'var(--panel)':'var(--muted)').attr('stroke-width',1.5);
node.append('text').attr('x',12).attr('y',4).text(d=>d.label).attr('opacity',d=>d.written?1:.65);
node.append('title').text(d=>d.written?d.label:d.label+' (not yet written)');
node.on('click',(ev,d)=>{if(d.written&&!ev.defaultPrevented)location.href=d.url});
sim.on('tick',()=>{link.attr('x1',d=>d.source.x).attr('y1',d=>d.source.y).attr('x2',d=>d.target.x).attr('y2',d=>d.target.y);
 node.attr('transform',d=>'translate('+d.x+','+d.y+')')});
sim.on('end',()=>{if(!fitted)fit()});
})();
</script>"""


if __name__ == "__main__":
    sys.exit(main())
