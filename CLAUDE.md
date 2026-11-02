# Salesforce Knowledge Graph — run playbook

This repo is a citation-backed knowledge graph of the Salesforce ecosystem. An hourly scheduled run makes **one change** per run: it either adds one new, unique article or refreshes a small batch (1–4) of existing articles that were verified against an older release (see 2a). Follow these steps in order. Read `SCHEMA.md` before writing.

## 1. Sync and orient
```bash
git pull --rebase origin main
python3 scripts/kg.py build      # must print OK; fix the repo first if it doesn't
```
Read `graph/stats.md`, `graph/frontier.md` and `topics/seeds.yaml`. `graph/index.json` lists every existing node (ids, titles, aliases, release, status, source URLs).

Determine the **current Salesforce release** (e.g. "Winter '27") from the official release notes (help.salesforce.com release notes) or the Salesforce release calendar. Use the release that is generally available in production, not one still in sandbox preview. Every article you write or refresh is stamped with it in `release`.

## 2. Pick the topic (graph-driven)
Use the current UTC hour:
- **Even hour → depth.** Take the highest-ranked node in `graph/frontier.md` (referenced by the most articles but not yet written) that fits a domain in `topics/seeds.yaml`. This turns dangling edges into real nodes.
- **Odd hour → refresh first, then breadth.** Look up the next release's production GA date on the official Salesforce release calendar or release notes, then run `python3 scripts/kg.py stale --current "<current release>" --next-release-date <YYYY-MM-DD>` (omit the date if you can't confirm it; the script then estimates it). If it lists any stale article, refresh exactly the articles in its **Refresh batch for this run** per step 2a; that is this run's change. The batch size adapts so the backlog clears before the next release (1–4 per run), and it pairs the stalest article with linked or same-domain articles so research overlaps. If it prints a WARNING that the backlog won't clear at the cap, still refresh the batch and mention the warning in the commit body. Only if nothing is stale, do breadth: take the domain in `topics/seeds.yaml` with the fewest articles (ties: alphabetical, skipping the domain of the most recent commit) and pick an unwritten seed topic, or another important topic in that domain.
- If no frontier node fits, do an odd-hour run (refresh first, then breadth).

After each new release this spends the odd hours refreshing until nothing is stale, while even hours keep adding frontier articles.

For a new article, prove it is unique (skip this for a refresh picked from `kg.py stale`):
```bash
python3 scripts/kg.py similar "<candidate title>" --current "<current release>"
```
Each match shows its `[release]`; matches verified against an older release than the current one are flagged `STALE`.
- If an existing title or alias names the same thing (or a ≥ 0.5 match is the same subject after review): if that match is flagged `STALE`, **refresh it** (step 2a) instead of writing a new article; otherwise pick a different topic.
- If any score is ≥ 0.5, **review before skipping**: read the summary (and aliases) of each matching node. Proceed only if it is clearly a different subject, and record the reason in the commit message body, one line per match, e.g. `similar: 0.55 vs kt:governor-limits — alias "Apex governor limits" covers limits, not triggers`. If you are unsure, pick a different topic.
- Scores below 0.5 need no note.

Never write a second article on a subject that already has a node — not a rename, a sub-angle that restates it, an old product name (e.g. "Salesforce CDP" vs "Data Cloud"), or a synonym. Salesforce renames products often: record former names as `aliases`. A newer release is never a reason for a second node on the same subject; refresh the existing one.

## 2a. Refresh a stale article (instead of adding one)
Use this for each article in the odd-hour refresh batch from `kg.py stale`, or (as a batch of one) whenever step 2 lands on an existing node whose `release` is older than the current release. The refresh batch is this run's one change. Apply every rule below to each article in the batch; if one article can't be re-verified, leave it out and refresh the rest.
- Keep the file path, `id`, `created` date and existing edges, so links from other articles stay intact. Never rename or delete the node.
- Re-verify the article against the current release: re-open every cited source (search for it first, per step 3), check the current release notes for changes to the feature, and confirm `status` and every stated limit and number.
- Rewrite only what changed. Replace or add sources as needed (same rules as step 3); update every refreshed source's `accessed` date; set `release` to the current release.
- If the product was renamed, update `title` only if Salesforce's official name changed, and add the former name to `aliases`. If the feature was retired or replaced, set `status` and add a `replacedBy` edge; the successor is a different subject and can be written as a new article in a later run.
- If the change is notable, add a short **What changed in <release>** section with citations.
- If nothing changed, still bump `release` and the `accessed` dates of the sources you re-opened.
- If you cannot open enough sources to re-verify an article, don't refresh it. If no article in the batch can be refreshed, pick a different topic.

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
- Back-links: if the new node is a natural child or relative of an existing article, you may add its id to that article's `related` list. Don't otherwise rewrite existing articles, except through a refresh (step 2a).

## 5. Validate, build, commit, push
```bash
python3 scripts/kg.py build    # fix every reported problem, then re-run until OK
git add -A
git commit -m "Add <Title> (<domain>)"   # refresh: "Refresh <Title>[, <Title>…] (<old release> → <new release>)"
git pull --rebase origin main && git push origin main
```
In a refresh commit body, list what changed per article, one line each (or `<id>: no content changes; re-verified`). If the push is rejected, pull --rebase, rebuild, and push again (once). Commit generated `graph/` files with the article.

## Don'ts
- Don't add more than one new article per run, refresh more articles than the suggested batch, combine an addition with refreshes, delete articles, or rewrite history.
- Don't write a new article on a subject that already has a node just because its node is stale; refresh it.
- Don't commit if validation fails; leave the repo clean.
- Don't cite a source you didn't open, or state a limit you didn't verify.
