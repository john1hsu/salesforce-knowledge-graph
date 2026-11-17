---
id: kt:tableau-semantics
type: Feature
title: Tableau Semantics
aliases: [Data 360 semantic layer, Data Cloud semantic layer, Salesforce semantic models]
domain: data-cloud-and-ai
summary: >-
  The semantic layer built into Data 360: semantic models map data model objects, data lake objects and
  calculated insights to governed business definitions (dimensions, measures, relationships, metrics) that
  Tableau Next, Tableau Desktop/Cloud, Data 360 reports and AI agents all query the same way.
release: "Winter '27"
status: current
broader: [kt:salesforce-analytics, kt:semantic-layer]
related: [kt:data-model-objects, kt:calculated-insights]
relations:
  - {predicate: partOf, object: kt:data-cloud}
  - {predicate: dependsOn, object: kt:data-spaces}
  - {predicate: consumedBy, object: kt:tableau-next}
  - {predicate: consumedBy, object: kt:tableau}
sources:
  - id: s1
    title: "What is the Tableau Semantics?"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/semantic-layer/guide/tableau-semantics-concepts.html
    type: official-docs
    accessed: 2026-11-17
  - id: s2
    title: "Create a Semantic Model (Tableau Semantics module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/tableau-semantics/create-a-semantic-model
    type: official-learning
    accessed: 2026-11-17
  - id: s3
    title: "Test and Consume Your Semantic Model (Tableau Semantics module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/tableau-semantics/test-and-consume-your-semantic-model
    type: official-learning
    accessed: 2026-11-17
  - id: s4
    title: "Tableau Semantics (connector)"
    publisher: Tableau Desktop and Web Authoring Help
    url: https://help.tableau.com/current/pro/desktop/en-us/examples_tableau_semantics.htm
    type: official-docs
    accessed: 2026-11-17
  - id: s5
    title: "Best Practices for Creating a Performant Semantic Model in Tableau Semantics"
    publisher: Tableau
    url: https://www.tableau.com/blog/tableau-semantics-best-practices-performant-semantic-model
    type: official-blog
    accessed: 2026-11-17
  - id: s6
    title: "Tableau Semantics"
    publisher: Salesforce
    url: https://www.salesforce.com/in/analytics/tableau-semantics/
    type: official-blog
    accessed: 2026-11-17
created: 2026-11-17
---

# Tableau Semantics

Tableau Semantics is the semantic layer of Data 360 (formerly Data Cloud). It sits between harmonized data and the tools that ask questions of it, giving one governed place to define dimensions, measures, relationships, metrics and goals so that every consumer reads the same business meaning from the same data.[^s1] Salesforce markets it as the layer that translates raw data into business terms so that both analytics and AI agents return more accurate answers.[^s6] It is not a standalone product: Salesforce states that it is deeply integrated into Data 360 and unavailable without it, and offers it to Data 360 customers and to Tableau Next customers through the Tableau+ SKU.[^s6]

## How it works

The unit of work is the **semantic model**, a first-class piece of Salesforce metadata that groups semantic definitions for one analytical use case and must contain at least one data object.[^s1] A model can introduce new definitions or override what the data lake already says, for example by renaming fields for business users, replacing a relationship or adding a metric.[^s1] The developer guide lists the definition types:[^s1]

- **Dimensions and calculated dimensions**: labels used to group or segment data, with data types such as date or geo; calculated ones are formula-based classifications.[^s1]
- **Measurements and calculated measurements**: numeric fields with a default aggregation; calculated ones combine fields and formulas, often across tables, and are computed at query time.[^s1]
- **Relationships**: physical or logical links on common fields, with join criteria and cardinality, designed to keep each table at its own grain.[^s1]
- **Metrics**: KPIs tracked over time, derived from one or more measures.[^s1]
- **Logical views**: a data object that fixes several tables together with explicit join types.[^s1]

Models are built in the **Semantic Layer** tab of Data 360 (or inside a Tableau Next workspace). The builder takes data model objects, data lake objects or calculated insights as inputs, accepts at most one data space per model, and fixes the model's API name once it is created.[^s2] Relationships already mapped between DMOs come across automatically, circular ones that reference the same object twice are removed, and the join type is not chosen up front: the layer decides it when a query actually uses fields from related objects. Trailhead recommends this relationship approach over manual joins.[^s2] An optional Semantics AI feature, switched on in Feature Manager, proposes relationships for review.[^s2] Salesforce also describes AI help that drafts calculated fields from natural-language prompts and can generate a whole model from a description.[^s6]

Before publishing, **Test Model** runs a sample query through the Tableau Semantics Query Generator, showing errors and results in a preview panel; the default sample is 100 rows.[^s3]

## Where models are consumed

A single model serves several front ends. Data 360 reports can be built on a model, using up to twenty Data 360 objects at once and inheriting its calculated fields, logical views and joins.[^s3] Tableau Next workspaces can create models or reference existing ones from Data 360.[^s3] Classic Tableau reaches the same models through the **Tableau Semantics connector**, introduced in Tableau Desktop 2025.2 and also available in Tableau Cloud; it requires the org's My Domain URL rather than a generic login host.[^s4] Conversational analytics turns natural-language questions into semantic queries, so agents answer with the governed definitions.[^s6] The developer guide exposes Authoring, Semantic Query and Semantic Metric Query APIs for programmatic use.[^s1]

## Limits and gotchas

The connector returns data that is already aggregated, so extracts, data blending, sets, context filters, View Underlying Data and the ATTR() function are unavailable, and a field redefined locally in Tableau stops picking up later changes from the model.[^s4] Tableau's own guidance names runtime joins as the main cause of slow dashboards and suggests keeping typical queries under about six or seven joins.[^s5] Missing or wrong cardinality can fan out measures and duplicate totals, and joins are case-sensitive by default.[^s5] For sources above roughly 100 million rows it recommends aligning default filters with DLO partitioning and pushing heavy logic upstream into transformations or calculated insights.[^s5] Model filters are not a security boundary; row-level security belongs in Data 360 policies.[^s5] Agents depend on clear, human-readable names and descriptions, so cryptic field names lower answer quality.[^s5]

## When to use it

Use Tableau Semantics when the same KPIs must mean the same thing in dashboards, Data 360 reports and agent answers, and the data already lives in or is federated into Data 360.[^s1][^s6] Where data is outside Data 360 and only classic Tableau consumes it, Tableau's published data sources remain the lighter option, though Salesforce says they can be imported into the semantic layer without migration.[^s6]

## Connections

Tableau Semantics is `partOf` `kt:data-cloud` and `dependsOn` `kt:data-spaces`, since each model is scoped to one data space.[^s2] It sits under `kt:salesforce-analytics` and the general `kt:semantic-layer` concept, and builds on `kt:data-model-objects` and `kt:calculated-insights` as model inputs.[^s2] It is `consumedBy` `kt:tableau-next`, which authors and references models in workspaces, and by `kt:tableau` through the connector.[^s3][^s4]

## Sources

[^s1]: Salesforce Developers, "What is the Tableau Semantics?". https://developer.salesforce.com/docs/data/semantic-layer/guide/tableau-semantics-concepts.html (accessed 2026-11-17)
[^s2]: Trailhead, "Create a Semantic Model". https://trailhead.salesforce.com/content/learn/modules/tableau-semantics/create-a-semantic-model (accessed 2026-11-17)
[^s3]: Trailhead, "Test and Consume Your Semantic Model". https://trailhead.salesforce.com/content/learn/modules/tableau-semantics/test-and-consume-your-semantic-model (accessed 2026-11-17)
[^s4]: Tableau Help, "Tableau Semantics". https://help.tableau.com/current/pro/desktop/en-us/examples_tableau_semantics.htm (accessed 2026-11-17)
[^s5]: Tableau, "Best Practices for Creating a Performant Semantic Model in Tableau Semantics" (2026-10-23). https://www.tableau.com/blog/tableau-semantics-best-practices-performant-semantic-model (accessed 2026-11-17)
[^s6]: Salesforce, "Tableau Semantics". https://www.salesforce.com/in/analytics/tableau-semantics/ (accessed 2026-11-17)
