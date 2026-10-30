# Salesforce Knowledge Graph — run playbook

This repo is a citation-backed knowledge graph of the Salesforce ecosystem. An hourly scheduled run adds **exactly one new, unique article** per run. Follow these steps in order. Read `SCHEMA.md` before writing.

## 1. Sync and orient
```bash
git pull --rebase origin main
python3 scripts/kg.py build      # must print OK; fix the repo first if it doesn't
```
Read `graph/stats.md`, `graph/frontier.md` and `topics/seeds.yaml`. `graph/index.json` lists every existing node (ids, titles, aliases, release, status, source URLs).

Determine the **current Salesforce release** (e.g. "Winter '27") from the official release notes (help.salesforce.com release notes) or the Salesforce release calendar. Every article you write is stamped with it in `release`.

## 2. Pick the topic (graph-driven)
Use the current UTC hour:
- **Even hour → depth.** Take the highest-ranked node in `graph/frontier.md` (referenced by the most articles but not yet written) that fits a domain in `topics/seeds.yaml`. This turns dangling edges into real nodes.
- **Odd hour → breadth.** Take the domain in `topics/seeds.yaml` with the fewest articles (ties: alphabetical, skipping the domain of the most recent commit) and pick an unwritten seed topic, or another important topic in that domain.
- If no frontier node fits, do a breadth run.

Then prove it is unique:
```bash
python3 scripts/kg.py similar "<candidate title>"
```
If any score ≥ 0.5, or an existing title/alias names the same thing, pick a different topic. Never write a second article on a subject that already has a node — not a rename, a sub-angle that restates it, an old product name (e.g. "Salesforce CDP" vs "Data Cloud"), or a synonym. Salesforce renames products often: record former names as `aliases`.

## 3. Research
- Run several web searches; read the actual pages (WebFetch), don't rely on snippets or memory.
- Collect 3–6 credible sources: at least 1 official Salesforce source (docs or Trailhead) unless the node is an `ExternalConcept`, and at least 2 of a strong type (see `SCHEMA.md`). Prefer developer.salesforce.com, help.salesforce.com, architect.salesforce.com, release notes and Trailhead; add standards bodies (IETF, OASIS, NIST) and fedramp.gov where relevant. **Never cite Wikipedia**, content farms, exam-dump sites, or AI-generated pages.
- Every URL you cite must be one you actually opened this run. Never invent or guess a URL. If a docs page won't render, find another official page that does.
- State limits and numbers exactly as the source gives them, and only those you verified this run.
- Paraphrase. No quotation longer than 15 words; at most one quote per source.
- Check the feature's lifecycle (GA, beta, pilot, deprecated, retired) and set `status`. Retired/deprecated features need a `replacedBy` edge to their successor.

## 4. Write the node
- Path `articles/<domain>/<slug>.md`, id `kt:<slug>`. Pick the most specific `type` from the ontology.
- 350–900 words, practitioner level: what it is, how it works, limits and gotchas, when to use it vs. alternatives, and a **Connections** section explaining the edges.
- Every factual paragraph carries footnote citations `[^sN]`; list all sources in `## Sources`.
- Edges: 1–3 `broader`, 2–6 `related` or typed `relations`. Use typed predicates where they fit (`dependsOn`, `alternativeTo`, `governedBy`, `replacedBy`, `configuredVia`, `queriedWith`, `requiresLicense`, `coveredBy` a certification, …). **Link to existing node ids wherever they fit** (check `graph/index.json`); new target ids are fine and join the frontier.
- If a needed predicate or class is missing, add it to `ontology/ontology.ttl` (with a label and, if applicable, inverse) in the same commit. Keep the ontology small; reuse before adding.
- Back-links: if the new node is a natural child or relative of an existing article, you may add its id to that article's `related` list. Don't otherwise rewrite existing articles.

## 5. Validate, build, commit, push
```bash
python3 scripts/kg.py build    # fix every reported problem, then re-run until OK
git add -A
git commit -m "Add <Title> (<domain>)"
git pull --rebase origin main && git push origin main
```
If the push is rejected, pull --rebase, rebuild, and push again (once). Commit generated `graph/` files with the article.

## Don'ts
- Don't add more than one article per run, delete articles, or rewrite history.
- Don't commit if validation fails; leave the repo clean.
- Don't cite a source you didn't open, or state a limit you didn't verify.
