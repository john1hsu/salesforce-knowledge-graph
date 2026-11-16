---
id: kt:tableau-next
type: Product
title: Tableau Next
aliases: [Tableau Next agentic analytics platform]
domain: clouds-and-products
summary: >-
  Salesforce's agentic, API-first analytics platform built on the Agentforce 360 Platform and Data 360: workspaces
  hold semantic models (Tableau Semantics), metrics, vizzes and dashboards over Data 360 objects, with Agentforce
  analytics skills and Slack and Flow actions built in.
release: "Winter '27"
status: current
broader: [kt:tableau, kt:salesforce-analytics]
related: [kt:crm-analytics, kt:data-model-objects, kt:slack-platform, kt:flow-builder]
relations:
  - {predicate: partOf, object: kt:tableau}
  - {predicate: dependsOn, object: kt:data-cloud}
  - {predicate: hasPart, object: kt:tableau-semantics}
  - {predicate: integratesWith, object: kt:agentforce}
  - {predicate: dependsOn, object: kt:data-spaces}
sources:
  - id: s1
    title: "Tableau Next Overview"
    publisher: Tableau (Salesforce)
    url: https://help.tableau.com/current/online/en-us/tableau_next_overview.htm
    type: official-docs
    accessed: 2026-11-16
  - id: s2
    title: "Tableau Next Features Overview"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/analytics/tableau-next-isv-dev/guide/tn-features-overview.html
    type: official-docs
    accessed: 2026-11-16
  - id: s3
    title: "Get to Know Semantic Models (Semantic Models in Tableau Next: Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/semantic-models-in-tableau-next-quick-look/get-to-know-semantic-models
    type: official-learning
    accessed: 2026-11-16
  - id: s4
    title: "Learn the Basics of Tableau Semantics"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/tableau-semantics/learn-the-basics-of-tableau-semantics
    type: official-learning
    accessed: 2026-11-16
  - id: s5
    title: "What Is Tableau Next?"
    publisher: Tableau (Salesforce)
    url: https://www.tableau.com/blog/what-is-tableau-next
    type: official-blog
    accessed: 2026-11-16
created: 2026-11-16
---

# Tableau Next

Tableau Next is Salesforce's agentic analytics platform. Unlike Tableau Desktop, Cloud and Server, it is built on the Agentforce 360 Platform and integrated with Agentforce, and Tableau positions it as an open, API-driven platform whose analytic assets are discoverable and reusable.[^s5] The developer guide describes it as an end-to-end analytics experience that connects the analytics platform, Agentforce AI and the Data 360 semantic layer, designed to be composable and API-first.[^s2] It is sold in the Tableau+ bundle and as a standalone offer priced per user per month, and Tableau states that AI usage, data transforms and analytical queries are not metered.[^s5]

## How it works

Tableau's platform diagram stacks four layers: a data layer, Tableau Semantics, a visualization layer and an action layer, with a Tableau Agent on top and the Tableau Marketplace and apps for Salesforce alongside.[^s5] In practice, analysis flows through a fixed chain of asset types:[^s1]

- **Data** is always a Data 360 object: a DMO, DLO, calculated insight, or a CSV stored as a DLO. Tableau Next keeps only connection information.[^s1]
- **Semantic models** define the data model (objects and relationships) plus business definitions such as field names, aggregations and calculations; Tableau Semantics generates the queries.[^s1]
- **Metrics** derive from a semantic model and track a measure over time, with a sentiment (whether up is good) and an aggregation such as sum, average or non-cumulative.[^s2]
- **Vizzes** are single charts from the Visualization Builder; **dashboards** combine metrics, vizzes and widgets such as filters and buttons, including actions driven by Salesforce Flows.[^s1]

All content lives in **workspaces**, each holding data connections, a semantic model builder, a metric creator and visualization tools.[^s2] An asset belongs to exactly one workspace; adding it to another creates a reference, not a copy, so Tableau recommends a new workspace per discrete project and reuse for related analysis.[^s1]

Semantic models are first-class Salesforce metadata available across Data 360.[^s2] They can combine DMOs, DLOs and calculated insights, lock joins or unions in a logical view, add calculated fields (manually or with AI help) and define metrics, so every consumer applies the same business logic.[^s3] Models can be built in either the Data 360 Semantic Layer tab or a Tableau Next workspace, and a Tableau Semantics connector lets Tableau Desktop and Tableau Cloud query them too.[^s4] Conversational analytics works by translating natural-language questions into semantic queries, returning text, vizzes and explanations.[^s3] Agentforce for Analytics is built in through three tools named Data Pro, Concierge and Inspector.[^s1]

## Setup, limits and gotchas

Data 360 is a hard prerequisite. Setup runs in five steps: set up Data 360 for Tableau Next, set up Tableau Semantics, create the Tableau Next admin, enable Tableau Next, and assign users the Tableau Next permission set.[^s1] Access is layered: Salesforce permission sets, Data 360 governance policies and per-asset sharing all apply.[^s2] Semantic models are private by default; users need access to the data space, user-level Semantic Models permissions (Read, Create, Edit, Delete), and explicit sharing before they can use one.[^s4]

Data 360 was renamed (from Data Cloud) on October 14, 2025, with no change in functionality, so older guides that mention Data Cloud still apply.[^s1] Building a semantic model from a published Tableau Cloud data source needs a trust configuration that links the Salesforce user to a Tableau Cloud user.[^s1]

## When to use it (and when not)

Pick Tableau Next when analytics should live inside Salesforce workflows, share one governed semantic model with Data 360 and agents, run Flow-driven actions, and be shared or embedded in Slack.[^s1][^s4] Dashboards can be templated and published to the Tableau Next Marketplace for reuse across an org, and developers extend them with custom Lightning Web Components and deploy assets via APIs and MCP tooling.[^s2] For multi-source enterprise BI that never touches Data 360, the classic Tableau Cloud or Server portfolio remains the simpler fit, and it can still consume the same semantic models through the connector.[^s1][^s4]

## Connections

Tableau Next is `partOf` `kt:tableau`, built on the Salesforce platform rather than the Desktop/Cloud/Server code base, and sits under `kt:salesforce-analytics` beside the older platform-native `kt:crm-analytics`.[^s5] It `dependsOn` `kt:data-cloud` (Data 360) and `kt:data-spaces`, reads `kt:data-model-objects`, and `hasPart` `kt:tableau-semantics`, the layer that defines its semantic models.[^s1][^s4] It `integratesWith` `kt:agentforce` through its built-in analytics agents, shares and embeds assets in `kt:slack-platform`, and runs dashboard actions built with `kt:flow-builder`.[^s1]

## Sources
[^s1]: Tableau (Salesforce), "Tableau Next Overview". https://help.tableau.com/current/online/en-us/tableau_next_overview.htm (accessed 2026-11-16)
[^s2]: Salesforce Developers, "Tableau Next Features Overview". https://developer.salesforce.com/docs/analytics/tableau-next-isv-dev/guide/tn-features-overview.html (accessed 2026-11-16)
[^s3]: Trailhead, "Get to Know Semantic Models". https://trailhead.salesforce.com/content/learn/modules/semantic-models-in-tableau-next-quick-look/get-to-know-semantic-models (accessed 2026-11-16)
[^s4]: Trailhead, "Learn the Basics of Tableau Semantics". https://trailhead.salesforce.com/content/learn/modules/tableau-semantics/learn-the-basics-of-tableau-semantics (accessed 2026-11-16)
[^s5]: Tableau (Salesforce), "What Is Tableau Next?". https://www.tableau.com/blog/what-is-tableau-next (accessed 2026-11-16)
