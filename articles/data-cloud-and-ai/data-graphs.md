---
id: kt:data-graphs
type: Feature
title: Data Graphs
aliases: [data graph, Data 360 data graphs, Data Cloud data graphs, real-time data graph, standard data graph]
domain: data-cloud-and-ai
summary: >-
  Precomputed, read-only views in Data 360 (formerly Data Cloud) that join a primary data model object with related
  DMOs and store the result as one JSON record per entity, so apps and agents can fetch connected data in one lookup.
release: "Winter '27"
status: current
broader: [kt:data-cloud]
related: [kt:data-model-objects, kt:data-spaces, kt:identity-resolution, kt:data-cloud-segmentation, kt:data-kits, kt:streaming-insights]
relations:
  - {predicate: dependsOn, object: kt:data-model-objects}
  - {predicate: dependsOn, object: kt:data-spaces}
  - {predicate: consumedBy, object: kt:agentforce}
  - {predicate: queriedWith, object: kt:data-cloud-query-api}
sources:
  - id: s1
    title: "Get to Know Data Graphs (Data Graphs in Data 360)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-graphs-in-data-cloud/get-to-know-data-graphs-1
    type: official-learning
    accessed: 2026-11-14
  - id: s2
    title: "Create a Data Graph (Data Graphs in Data 360)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-graphs-in-data-cloud/create-a-data-graph
    type: official-learning
    accessed: 2026-11-14
  - id: s3
    title: "Query Data Graph Data"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-ref/guide/c360a-api-data-graphs-overview.htm
    type: official-docs
    accessed: 2026-11-14
  - id: s4
    title: "How Data Cloud's Data Graph Delivers Sub-Second Insights from 200 Million Records"
    publisher: Salesforce Engineering
    url: https://engineering.salesforce.com/how-data-clouds-data-graph-delivers-sub-second-insights-from-200-million-records/
    type: official-blog
    accessed: 2026-11-14
  - id: s5
    title: "Configure an Additional Real-Time Data Graph for GetContext"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/agentic-memory-context/guide/agentic-memory-create-rtdg-for-getcontext.html
    type: official-docs
    accessed: 2026-11-14
created: 2026-11-14
---

# Data Graphs

A **data graph** in Data 360 (the product formerly called Data Cloud) models how harmonized datasets relate to
each other, for example a customer linked to their orders, order items, cases and products. It joins data model
objects (DMOs), across several levels if needed, and aggregates the fields you pick into a read-only record that
is stored as a single JSON blob, giving one connected view of the entity.[^s1] Because the joins are computed ahead
of time and materialized, a request returns the whole connected record quickly instead of running a multi-table
query at read time.[^s3]

## How it works

You build a graph in Data 360 under Data Graphs, starting from scratch or from a data kit. A graph lives in one
data space and starts from a **primary DMO**, such as Individual from the Profile category, which acts as the root
that the other objects link to. You then add related DMOs along their relationship paths, choose the fields to
include for each object, set a refresh interval and save and build.[^s2] When several paths reach the same DMO you
choose the most suitable one, and each longer path adds another level to the graph. A build takes from about 15
minutes to several hours depending on data size and complexity; the status moves from Processing to Active.[^s2]

Salesforce engineering describes the design goal as precomputing views over very large datasets so lookups across
many tables return in under a second. Non-real-time graphs refresh daily by default, with hourly, 4-hourly, weekly
and monthly schedules available, and the team reported cutting a 200-million-record build from up to three hours
to 90 minutes.[^s4]

## Standard and real-time graphs

- **Standard data graphs** update after a delay of minutes to hours and suit batch processing, sync and reporting.[^s1]
- **Real-time data graphs** update instantly for in-session use and need the separately purchased Real-Time SKU.[^s1]

The real-time layer feeds web and mobile engagement data into the graph with sub-second latency.[^s4] For agents, a
real-time data graph can be attached at registration so the GetContext API adds structured data from the data space
to an agent's context. Creating one requires the Data Cloud Architect permission, a root entity DMO already in the
data space, and a data space that matches the agents that use the graph.[^s5]

## Querying a data graph

The Data 360 Query API exposes graphs through three REST resources: a metadata call that lists accessible graphs
with their primary DMO, related objects and fields; a lookup by record ID; and a lookup by key fields of the primary
or participating DMOs.[^s3] These standard reads hit the precalculated graph and answer in near real time. Live
queries return current data but trade that for higher latency and credit consumption.[^s3] Access requires
provisioned Data Cloud licenses, the right roles and permissions, and a valid access token.[^s3]

## Limits and gotchas

- **Recency filters cut engagement data.** Engagement DMOs are filtered by recency, so older orders can drop out of a graph unless you widen the filter.[^s1]
- **Freshness costs credits.** Choosing a less frequent refresh interval saves cost when data does not need to be current.[^s2]
- **Data space access.** If your permission set cannot see the graph's data space, eligible primary DMOs such as Individual do not appear.[^s2]
- **Read-only output.** A graph record is a read-only aggregation of DMO fields, so it is a lookup source, not a place to write data.[^s1]
- **Build time.** A new or large graph can take hours to build, so plan it before a launch rather than during one.[^s2]

## When to use it (and when not)

Use a data graph when an application, a flow, a personalization bot or an agent needs a customer's related records
in a single fast lookup, for example showing a service agent current order status or recommending products when a
customer messages a bot.[^s1] For population-level questions such as building an audience, use segmentation; for
ad-hoc analysis across many rows, query the DMOs with SQL through the Query API rather than reading graph records.[^s3]

## Connections

A data graph is a feature of `kt:data-cloud` and **depends on** `kt:data-model-objects`, since every node in the graph
is a DMO, and on `kt:data-spaces`, which scope which objects and users it can reach.[^s1][^s2] It is **queried with**
`kt:data-cloud-query-api`.[^s3] Real-time graphs are **consumed by** `kt:agentforce` agents through GetContext.[^s5]
It is related to `kt:identity-resolution`, whose unified profiles are common primary objects; to
`kt:data-cloud-segmentation` and `kt:streaming-insights`, which cover audience and streaming use cases; and to
`kt:data-kits`, which can package prebuilt graphs.[^s2][^s4]

## Sources

[^s1]: Trailhead, "Get to Know Data Graphs (Data Graphs in Data 360)". https://trailhead.salesforce.com/content/learn/modules/data-graphs-in-data-cloud/get-to-know-data-graphs-1 (accessed 2026-11-14)
[^s2]: Trailhead, "Create a Data Graph (Data Graphs in Data 360)". https://trailhead.salesforce.com/content/learn/modules/data-graphs-in-data-cloud/create-a-data-graph (accessed 2026-11-14)
[^s3]: Salesforce Developers, "Query Data Graph Data". https://developer.salesforce.com/docs/data/data-cloud-ref/guide/c360a-api-data-graphs-overview.htm (accessed 2026-11-14)
[^s4]: Salesforce Engineering, "How Data Cloud's Data Graph Delivers Sub-Second Insights from 200 Million Records". https://engineering.salesforce.com/how-data-clouds-data-graph-delivers-sub-second-insights-from-200-million-records/ (accessed 2026-11-14)
[^s5]: Salesforce Developers, "Configure an Additional Real-Time Data Graph for GetContext". https://developer.salesforce.com/docs/data/agentic-memory-context/guide/agentic-memory-create-rtdg-for-getcontext.html (accessed 2026-11-14)
