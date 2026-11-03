---
id: kt:calculated-insights
type: Feature
title: Calculated Insights
aliases: [calculated insight, CI, Data 360 calculated insights, Data Cloud calculated insights, Data 360 insights, Insights Builder]
domain: data-cloud-and-ai
summary: >-
  SQL-defined, batch-computed metrics in Data 360 (formerly Data Cloud) that aggregate measures over
  dimensions from data model objects, such as lifetime spend per unified individual, for use in segments,
  activations and the Query API; streaming insights are their near-real-time, time-windowed counterpart.
release: "Winter '27"
status: current
broader: [kt:data-cloud]
related: [kt:identity-resolution, kt:roll-up-summary-field]
relations:
  - {predicate: dependsOn, object: kt:data-model-objects}
  - {predicate: hasPart, object: kt:streaming-insights}
  - {predicate: enables, object: kt:data-cloud-segmentation}
  - {predicate: governedBy, object: kt:data-cloud-limits}
  - {predicate: contrastsWith, object: kt:roll-up-summary-field}
  - {predicate: coveredBy, object: kt:data-cloud-consultant-certification}
sources:
  - id: s1
    title: "Use SQL to Create Insights (Data 360)"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=data.c360_a_create_a_calculated_insights_sql_function.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-03
  - id: s2
    title: "Data 360 Limits and Guidelines"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=c360_a_calculated_insights_limits.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-03
  - id: s3
    title: "Query Calculated Insights"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-query-guide/references/data-cloud-query-api-reference/c360a-api-ci-call-overview.html
    type: official-docs
    accessed: 2026-11-03
  - id: s4
    title: "Create Insights in Data 360"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/customer-data-platform-insights/create-insights-in-customer-data-platform
    type: official-learning
    accessed: 2026-11-03
  - id: s5
    title: "Use Data Insights for Segmentation"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/customer-data-platform-insights/use-insights-in-customer-data-platform
    type: official-learning
    accessed: 2026-11-03
created: 2026-11-03
---

# Calculated Insights

**Calculated insights** are reusable, SQL-defined metrics in Data 360 (formerly Data Cloud). Each one aggregates
**measures** (quantitative values such as a total amount or a record count) and groups them by **dimensions**
(qualitative fields such as a product name, a date or a profile ID) over data model objects. The result is a new
insight object that segments, activations and APIs can read, for example total spend per customer.[^s1][^s5]
Calculated insights work on mapped objects and fields and can reference other insights. **Streaming insights** work
on real-time sources over a time window and cannot reference other insights.[^s4]

## How it works

An insight follows a fixed SQL shape. You select attributes and aggregated measures from a DMO, optionally join other
DMOs with an inner, left, right or full join, optionally filter rows with `WHERE`, and `GROUP BY` the dimensions.
Every query needs at least one measure. Any selected field that is not inside an aggregate is treated as a
dimension, so it must also appear in `GROUP BY`. A nested subquery can restrict rows in a `WHERE` or `JOIN`
clause.[^s1][^s4]

There are several ways to build one. The **Insights Builder** is drag-and-drop and generates the SQL for you. The SQL
editor lets you write the expression yourself and check its syntax. You can also install an insight from a package
that was built and tested in another org.[^s4] After you save an insight, it moves through statuses: pending,
processing, success, active, error, or aborted. An insight that stays pending for more than 8 hours is aborted.
Spot-check the results in Data Explorer before you build segments on them. To correct a live insight, clone it and
edit the clone.[^s5]

Streaming insights use the same editor, but they must group by a time window. Trailhead's example counts mobile page
views per customer in 5-minute windows and returns the start and end of each window.[^s4] Their results feed
**data actions**, which send events to a webhook, the Salesforce CRM event bus, or Marketing Cloud Engagement. A new
data action's target starts receiving events in less than 15 minutes.[^s5]

## Limits and gotchas

From the Data 360 Limits and Guidelines page, checked against Winter '27:[^s2]

- **Calculated insights:** up to 10 dimensions and 50 measures each. A new insight can use up to 4 existing
  insights. A tenant can have 300 insights in total, including inactive and draft ones. Each insight can run for up to
  2 hours before it may be terminated, and you can process it manually 30 times in any 24-hour period.
- **Refresh:** system-managed insights process multiple times a day, and scheduled ones run on the schedule you set.
  An insight is skipped when its source data, mappings and configuration haven't changed.
- **Streaming insights:** 20 per tenant, with windows from 1 minute to 24 hours. Each can have up to 10 dimensions,
  and the required window start and window end fields count toward that limit. Each is limited to 5 measures, which
  can only use Count or Sum.
- **Query API:** each call to the calculated-insights endpoint returns at most 4,999 rows, so page through results
  with `limit` and `offset`.[^s3]

For segmentation, the most common mistake is grouping only by a business key. A segment-ready insight must join the
object you segment on, such as Unified Individual, and include that object's primary key as a dimension.[^s1][^s4]

## When to use it (and when not)

Use a calculated insight when a metric spans many records or sources and has to be reused, for example lifetime
value, order counts or engagement scores per unified profile. In a segment, an insight appears as a direct attribute
that you can filter on and refine with additional dimensions. In an activation, you can add it as an attribute, for
example to personalize a Marketing Cloud Engagement journey.[^s5] Use a streaming insight only when a decision must
be made within minutes, such as reacting to browsing behaviour, and the Count or Sum measures are enough.[^s2][^s5]
Applications can read insight values directly through the Query API's metadata and data endpoints. Those endpoints
support filters, sorting, and time aggregation by hour, day, month, quarter or year.[^s3]

## Connections

Calculated insights are a feature of `kt:data-cloud`. They **depend on** `kt:data-model-objects` because their SQL
can only read DMOs, and they usually group by the profiles that `kt:identity-resolution` produces.[^s1][^s4] They
**have** `kt:streaming-insights` as a near-real-time variant. They **enable** `kt:data-cloud-segmentation` and
activation. They are **governed by** `kt:data-cloud-limits`.[^s2][^s5] They **contrast with** CRM
`kt:roll-up-summary-field`s. Both aggregate child data, but an insight is computed in batches over harmonized,
multi-source data, not recalculated each time a single parent record is saved.[^s2] Building insights is **covered
by** `kt:data-cloud-consultant-certification`.

## Sources

[^s1]: Salesforce Help, "Use SQL to Create Insights (Data 360)". https://help.salesforce.com/s/articleView?id=data.c360_a_create_a_calculated_insights_sql_function.htm&language=en_US&type=5 (accessed 2026-11-03)
[^s2]: Salesforce Help, "Data 360 Limits and Guidelines". https://help.salesforce.com/s/articleView?id=c360_a_calculated_insights_limits.htm&language=en_US&type=5 (accessed 2026-11-03)
[^s3]: Salesforce Developers, "Query Calculated Insights". https://developer.salesforce.com/docs/data/data-cloud-query-guide/references/data-cloud-query-api-reference/c360a-api-ci-call-overview.html (accessed 2026-11-03)
[^s4]: Trailhead, "Create Insights in Data 360". https://trailhead.salesforce.com/content/learn/modules/customer-data-platform-insights/create-insights-in-customer-data-platform (accessed 2026-11-03)
[^s5]: Trailhead, "Use Data Insights for Segmentation". https://trailhead.salesforce.com/content/learn/modules/customer-data-platform-insights/use-insights-in-customer-data-platform (accessed 2026-11-03)
