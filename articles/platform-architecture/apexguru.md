---
id: kt:apexguru
type: Feature
title: ApexGuru
aliases: [ApexGuru Insights, Apex Guru, ApexGuru engine]
domain: platform-architecture
summary: >-
  An AI-powered, runtime-aware analysis feature in Scale Center that finds performance anti-patterns, expensive
  methods and unused code in an org's Apex, ranks them by observed runtime impact and proposes code fixes; it is
  also exposed as an engine in Salesforce Code Analyzer.
release: "Winter '27"
status: current
broader: [kt:scale-center]
related: [kt:apex, kt:soql, kt:bulkification, kt:apex-triggers, kt:scale-test, kt:technical-debt-in-salesforce]
relations:
  - {predicate: partOf, object: kt:scale-center}
  - {predicate: consumedBy, object: kt:code-analyzer}
  - {predicate: mitigates, object: kt:governor-limits}
sources:
  - id: s1
    title: "Meet ApexGuru"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/apexguru/meet-apexguru
    type: official-learning
    accessed: 2026-11-19
  - id: s2
    title: "Get AI-Powered Insights for Your Apex Code with ApexGuru"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/02/get-ai-powered-insights-for-your-apex-code-with-apexguru
    type: official-blog
    accessed: 2026-11-19
  - id: s3
    title: "Optimize Your Apex for Apps and Agentforce with ApexGuru"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2025/02/optimize-your-apex-for-apps-and-agentforce-with-apexguru
    type: official-blog
    accessed: 2026-11-19
  - id: s4
    title: "The ApexGuru AI Engine Explained"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2025/06/the-apexguru-ai-engine-explained
    type: official-blog
    accessed: 2026-11-19
  - id: s5
    title: "ApexGuru Engine (Salesforce Code Analyzer Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-code-analyzer/guide/engine-apexguru.html
    type: official-docs
    accessed: 2026-11-19
  - id: s6
    title: "Scale Center Gives Admins the Insights and Tools to Improve Org Performance"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2025/scale-center-gives-admins-the-insights-and-tools-to-improve-org-performance
    type: official-blog
    accessed: 2026-11-19
created: 2026-11-19
---

# ApexGuru

ApexGuru is a generative-AI feature of Scale Center that hunts for anti-patterns and performance hotspots in an org's Apex code and returns prescriptive, org-specific fix recommendations.[^s1] Unlike a purely static linter, it uses the org's runtime profiles to decide which code actually matters, and Salesforce states that it has no impact on org performance or storage limits and that customer code is not used to train its models.[^s1][^s2] It became generally available in February 2024 and, by mid-2025, Salesforce reported it had served more than 8,800 orgs.[^s4]

## How it works

Salesforce describes a three-stage pipeline. Static heuristic analyzers first discard roughly 70% of false candidates; compact, Apex-specific post-trained models (which Salesforce calls XGen-AG) then detect anti-patterns and generate fixes; and expert human evaluation vets test sets and prompts before inference goes live.[^s4] Live telemetry such as Apex CPU time and database time is used to rank findings by runtime footprint, so the most expensive problems surface first.[^s4] The Trailhead module attributes the AI capabilities to CodeGen models built and pretrained by Salesforce AI Research.[^s1]

Each code recommendation names the class and line where the anti-pattern occurs, links to the entry points that execute it, and shows a side-by-side suggested fix; findings can be exported as PDF.[^s2][^s3][^s4] Code issues are grouped as Critical, Major or Minor by expected impact.[^s2][^s3]

## What it finds

ApexGuru targets code that pushes against Apex governor limits: CPU time, the number of SOQL queries and rows, SOQL statement length, DML statements, and the org-wide Apex character limit.[^s1][^s2] Documented examples include:

- SOQL inside loops, unbulkified or mergeable queries, and inefficient DML patterns.[^s3][^s4]
- Calling `Schema.getGlobalDescribe()` to describe a single object, with `Type.forName()` suggested instead.[^s3][^s5]
- Binding a list of sObjects into a SOQL `IN` filter instead of a set of IDs such as a map's `keySet()`.[^s2][^s3]
- Unnecessary debug statements and unhandled nulls that can raise a `NullPointerException`.[^s3]

Beyond code issues it reports **expensive methods**: methods using at least 5% of CPU time are "critically expensive" and those using 2–5% are "expensive".[^s2][^s3] It also lists **unused classes and methods** not called since the latest production deployment, which helps reduce dead code and pressure on the Apex character limit.[^s2][^s3][^s6]

## Access, limits and gotchas

- ApexGuru ships in Scale Center at no extra charge for eligible orgs, including Unlimited Edition production and Full Copy sandboxes, Signature orgs and Scale Test customers.[^s2][^s6]
- It is not supported in Government Cloud Plus, matching Scale Center's own restriction.[^s1][^s2]
- To enable it, open **ApexGuru Insights** under Scale Insights in Setup and accept the ApexGuru Agreement.[^s1][^s3]
- First reports can take up to 24 hours to appear and are then refreshed weekly, so it is not a real-time tool.[^s2][^s3]

Because findings are driven by production-like runtime profiles, code that rarely executes may receive little attention even if it is poorly written; pair ApexGuru with static checks rather than treating it as a full code review.[^s4][^s5]

## In Salesforce Code Analyzer

Code Analyzer includes an ApexGuru engine alongside PMD, ESLint and RetireJS. It scans the `.cls` and `.trigger` files of a connected org (not local files) and returns line-level findings with severities and recommendations.[^s5] When ApexGuru is enabled in the org or its parent org family it runs in Advanced Mode against runtime data; otherwise it falls back to Basic Mode static analysis, and the mode cannot be chosen manually.[^s5] Scans are rate-limited: 3 per user and 5 per requesting org per 60 seconds, 100 per requesting org per 24 hours, and 200 per resolved parent org per 24 hours.[^s5] It runs from `sf code-analyzer run --rule-selector apexguru`, from VS Code, or in CI via the `run-code-analyzer` GitHub Action after JWT or SFDX auth URL authentication.[^s5]

## When to use it

Use ApexGuru when Scale Center shows CPU timeouts or limit errors and you need to know which Apex to fix first; admins can hand its findings to developers as a prioritized backlog.[^s6] Use Scale Test or Scale Center release comparisons to confirm the fix actually improved performance.[^s6]

## Connections

ApexGuru is **part of** `kt:scale-center`, whose metrics supply its runtime context, and it complements `kt:scale-test` for validating changes under load.[^s2][^s6] Its findings **mitigate** `kt:governor-limits` breaches and enforce `kt:bulkification` in `kt:apex`, `kt:apex-triggers` and `kt:soql`.[^s1][^s3] It is **consumed by** `kt:code-analyzer` as a rule engine, bringing the same insights into the developer loop and CI.[^s5] Its unused-code and expensive-method reports are practical inputs for paying down `kt:technical-debt-in-salesforce`.[^s3]

## Sources
[^s1]: Trailhead, "Meet ApexGuru". https://trailhead.salesforce.com/content/learn/modules/apexguru/meet-apexguru (accessed 2026-11-19)
[^s2]: Salesforce Developers Blog, "Get AI-Powered Insights for Your Apex Code with ApexGuru". https://developer.salesforce.com/blogs/2024/02/get-ai-powered-insights-for-your-apex-code-with-apexguru (accessed 2026-11-19)
[^s3]: Salesforce Developers Blog, "Optimize Your Apex for Apps and Agentforce with ApexGuru". https://developer.salesforce.com/blogs/2025/02/optimize-your-apex-for-apps-and-agentforce-with-apexguru (accessed 2026-11-19)
[^s4]: Salesforce Developers Blog, "The ApexGuru AI Engine Explained". https://developer.salesforce.com/blogs/2025/06/the-apexguru-ai-engine-explained (accessed 2026-11-19)
[^s5]: Salesforce Developers, "ApexGuru Engine". https://developer.salesforce.com/docs/platform/salesforce-code-analyzer/guide/engine-apexguru.html (accessed 2026-11-19)
[^s6]: Salesforce Admins Blog, "Scale Center Gives Admins the Insights and Tools to Improve Org Performance". https://admin.salesforce.com/blog/2025/scale-center-gives-admins-the-insights-and-tools-to-improve-org-performance (accessed 2026-11-19)
