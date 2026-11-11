---
id: kt:streaming-insights
type: Feature
title: Streaming Insights
aliases: [streaming insight, Data 360 streaming insights, Data Cloud streaming insights]
domain: data-cloud-and-ai
summary: >-
  Near-real-time, time-windowed aggregations in Data 360 (formerly Data Cloud) that compute counts and sums over
  streaming engagement data, such as Web and Mobile SDK events, and feed data actions that start workflows in Flow,
  webhooks or Marketing Cloud.
release: "Winter '27"
status: current
broader: [kt:data-cloud]
related: [kt:data-cloud-segmentation, kt:platform-events]
relations:
  - {predicate: partOf, object: kt:calculated-insights}
  - {predicate: dependsOn, object: kt:data-streams}
  - {predicate: dependsOn, object: kt:identity-resolution}
  - {predicate: enables, object: kt:data-actions}
  - {predicate: integratesWith, object: kt:marketing-cloud-engagement}
  - {predicate: governedBy, object: kt:data-cloud-limits}
sources:
  - id: s1
    title: "Learn About Data 360 Insights"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/customer-data-platform-insights/learn-about-customer-data-platform-insights
    type: official-learning
    accessed: 2026-11-11
  - id: s2
    title: "Create Insights in Data 360"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/customer-data-platform-insights/create-insights-in-customer-data-platform
    type: official-learning
    accessed: 2026-11-11
  - id: s3
    title: "Review SQL Examples"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/customer-data-platform-insights-using-sql/review-sql-examples
    type: official-learning
    accessed: 2026-11-11
  - id: s4
    title: "Data 360 Architecture"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/data-360-architecture
    type: official-docs
    accessed: 2026-11-11
  - id: s5
    title: "Data Insights"
    publisher: Salesforce
    url: https://www.salesforce.com/en-us/wp-content/uploads/sites/4/Data-Insights.pdf?bc=OTH
    type: official-docs
    accessed: 2026-11-11
  - id: s6
    title: "Unleashing the Power of Data Actions Using a Webhook as a Target"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/01/unleashing-the-power-of-data-actions-using-a-webhook-as-a-target
    type: official-blog
    accessed: 2026-11-11
created: 2026-11-11
---

# Streaming Insights

**Streaming insights** are SQL- or builder-defined metrics in Data 360 (formerly Data Cloud) that aggregate
real-time data over a time window. Where a calculated insight looks at the data as a whole, a streaming insight looks
at what happened in a specific window of time, producing near-real-time time series.[^s1] Their main job is to detect
a pattern quickly and hand it to a **data action** or orchestration that does something about it.[^s1][^s5]

## How it works

Streaming insights read streaming sources such as the Web and Mobile SDKs and Marketing Cloud Personalization data
streams. They can only be built on **engagement** data, not on streaming profile data.[^s1][^s5] You author them in
the same interface as calculated insights, either with the drag-and-drop builder or in SQL. The SQL is nearly
identical, with one difference: a streaming insight can't use existing insights as building blocks.[^s2]

The defining rule is the time window. In SQL you add `window(<datetime field>, '<interval>')` to the `GROUP BY`
clause, together with dimensions such as a customer ID or product, and select `WINDOW.START` and `WINDOW.END` (given
aliases such as `start__c` and `end__c`) to return the window bounds. Trailhead's example counts mobile page views per
customer and product in 5-minute windows, joining the event stream to the Individual object on a device ID.[^s2][^s3]
In the builder, an Aggregate node takes a window duration and a granularity, then measures and group-by
dimensions.[^s5] Currency measures must go through `CURRENCY_CONVERT`.[^s5]

Under the hood, Salesforce's architecture guide describes streaming insights as running on Spark Structured
Streaming, processing only changed records through change events and the Lakehouse change data feed. Batch
calculated insights, by contrast, run as scheduled Spark jobs over their full scope.[^s4] Results are written to the
Lakehouse as insight objects, like calculated insights.[^s4] Salesforce's insights guide calls the processing
micro-batch, running over minutes to hours, and notes that a streaming insight's last-run status always reads
Processing.[^s5]

## Data actions

A streaming insight becomes useful when a **data action** watches it. A data action's primary source can be a
streaming insight or an engagement object. An event rule fires on changes, and an action rule tests conditions with
AND/OR logic before anything is sent.[^s6] Targets include a Salesforce platform event, a webhook, and Marketing
Cloud. A webhook target gets a generated secret key for the receiving endpoint.[^s6] Before the event is sent, it can
be enriched with profile attributes such as loyalty status.[^s4][^s5] The developer blog notes that action events are
kept for four days, so consumers should be built to be durable.[^s6]

## Limits and gotchas

- Only engagement data qualifies, and the source streams must be mapped to objects from supported real-time streams.[^s1][^s5]
- Streaming insights can't reference other insights, so build any multi-step logic into one query.[^s2]
- The Trailhead SQL examples only show `COUNT` and `SUM` measures; check per-tenant counts, window ranges and measure limits on `kt:data-cloud-limits` before you design.[^s3]
- Streaming is not the same as sub-second: Salesforce describes a separate real-time layer for millisecond personalization.[^s4][^s5]

## When to use it (and when not)

Use a streaming insight when a business event must trigger a response within minutes. Trailhead's examples include
starting a re-engagement journey when a lapsed customer enters a store geofence, and opening a case when someone
keeps revisiting the same knowledge articles.[^s1] Use a calculated insight for segment criteria and personalization
attributes, for logic that builds on other insights, or when you need to package the insight for another org.[^s1][^s2]
For millisecond in-session personalization, use the real-time layer and real-time data graphs instead.[^s4]

## Connections

Streaming insights are a feature of `kt:data-cloud` and the near-real-time **part of** `kt:calculated-insights`,
sharing its authoring tools and output objects.[^s2][^s4] They **depend on** `kt:data-streams` from the Web and
Mobile SDKs, and on `kt:identity-resolution` to tie events to unified individuals before enrichment.[^s3][^s5] They
**enable** `kt:data-actions`, which can publish `kt:platform-events` or **integrate with**
`kt:marketing-cloud-engagement`.[^s6] They are **governed by** `kt:data-cloud-limits`. They are related to
`kt:data-cloud-segmentation`, which uses calculated insights for batch audience criteria.[^s1]

## Sources

[^s1]: Trailhead, "Learn About Data 360 Insights". https://trailhead.salesforce.com/content/learn/modules/customer-data-platform-insights/learn-about-customer-data-platform-insights (accessed 2026-11-11)
[^s2]: Trailhead, "Create Insights in Data 360". https://trailhead.salesforce.com/content/learn/modules/customer-data-platform-insights/create-insights-in-customer-data-platform (accessed 2026-11-11)
[^s3]: Trailhead, "Review SQL Examples". https://trailhead.salesforce.com/content/learn/modules/customer-data-platform-insights-using-sql/review-sql-examples (accessed 2026-11-11)
[^s4]: Salesforce Architects, "Data 360 Architecture". https://architect.salesforce.com/fundamentals/data-360-architecture (accessed 2026-11-11)
[^s5]: Salesforce, "Data Insights". https://www.salesforce.com/en-us/wp-content/uploads/sites/4/Data-Insights.pdf?bc=OTH (accessed 2026-11-11)
[^s6]: Salesforce Developers Blog, "Unleashing the Power of Data Actions Using a Webhook as a Target". https://developer.salesforce.com/blogs/2024/01/unleashing-the-power-of-data-actions-using-a-webhook-as-a-target (accessed 2026-11-11)
