---
id: kt:data-cloud
type: Product
title: Data 360
aliases: [Data Cloud, Salesforce Data Cloud, Salesforce Data 360, Salesforce CDP, Customer 360 Audiences]
domain: data-cloud-and-ai
summary: >-
  Salesforce's data platform (named Data Cloud until October 2025) that ingests or federates data from Salesforce
  and external systems, harmonizes it into the Customer 360 Data Model, unifies records into profiles with identity
  resolution, and supplies insights, segments and grounding context to CRM apps and Agentforce.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:change-data-capture]
relations:
  - {predicate: hasPart, object: kt:data-model-objects}
  - {predicate: hasPart, object: kt:identity-resolution}
  - {predicate: hasPart, object: kt:calculated-insights}
  - {predicate: hasPart, object: kt:zero-copy-data-federation}
  - {predicate: enables, object: kt:agentforce}
sources:
  - id: s1
    title: "Object Model in Data 360"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-dev/guide/dc-object-model.html
    type: official-docs
    accessed: 2026-11-01
  - id: s2
    title: "Model Data in Data 360"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-dmo-mapping/guide/c360dm-model-data.html
    type: official-docs
    accessed: 2026-11-01
  - id: s3
    title: "Create Data Streams (Explore Data Cloud Core Functionality)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/explore-data-cloud-core-functionality/create-data-streams-1
    type: official-learning
    accessed: 2026-11-01
  - id: s4
    title: "Create an Insight (Explore Data Cloud Core Functionality)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/explore-data-cloud-core-functionality/create-an-insight
    type: official-learning
    accessed: 2026-11-01
  - id: s5
    title: "Data 360 Interoperability (Decision Guide)"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/decision-guides/guide/data-360-interoperability
    type: official-docs
    accessed: 2026-11-01
created: 2026-11-01
---

# Data 360

**Data 360** is Salesforce's data platform for bringing customer data from many systems into one harmonized, unified
model that the rest of the platform can act on. It was called **Data Cloud** until Salesforce rebranded it on
October 14, 2025; Salesforce states that the functionality did not change with the name, and many documentation
URLs, Trailhead projects and setup labels still say "Data Cloud".[^s2][^s3] Practitioners should treat the two names
as the same product when reading docs, licences or older designs.

## How it works

Data moves through a layered object model.[^s1]

1. **Data streams** start the flow. A stream is a source that is either connected to or ingested into Data 360:
   another Salesforce org, a Marketing Cloud Engagement business unit, an external platform or a CSV file.
   Salesforce-defined **data bundles** (for example the Sales CRM bundle) create a set of streams in one step and
   come with ready-made mappings.[^s3][^s2] Each stream is assigned a category such as Engagement (which needs an
   event-time field) or Other, and deploys into a data space.[^s3]
2. **Data lake objects (DLOs)** are the storage containers where ingested or federated data first lands, in its
   source shape. Formula fields on a DLO can normalise values or do simple calculations.[^s1][^s3]
3. **Data model objects (DMOs)** are harmonised groupings created by mapping DLO fields onto the
   **Customer 360 Data Model**, Salesforce's standard, extensible model; DMOs can be standard or custom and act as
   physical or virtual views over the underlying data.[^s2][^s1]
4. **Identity resolution** rulesets match and merge records about the same person from different sources into
   **unified DMOs**, such as Unified Individual. A resolution summary reports the number of unified profiles and
   the consolidation rate.[^s1][^s4]
5. **Calculated insight objects (CIOs)** compute multidimensional metrics, such as lifetime value or satisfaction
   score, at profile, segment or population level. They can be built in the Visual Insights Builder and move
   from Processing to Active once published.[^s1][^s4]

Insights and unified profiles then feed **segments** and **activations**, for example passing insight attributes to
Marketing Cloud Engagement for journey decisions and personalisation.[^s4]

## Ingestion vs. zero copy

The main architectural decision is whether to copy data in or leave it where it is.[^s5]

- **Ingestion** copies data into Data 360, which centralises transformation, governance and lineage. It runs in
  real time (CDC-based, sub-second, most expensive), streaming (micro-batches every one to three minutes) or batch
  (scheduled, cheapest; batch ingestion from Salesforce orgs through certain connectors carries no charge).[^s5]
- **Zero copy** queries data in place. *Live Query* is pay-per-query with maximum freshness; *caching* (Accelerated
  Query) keeps a local copy refreshed between every 15 minutes and every 7 days; *file federation* reads open table
  formats such as Iceberg in S3, ADLS or GCS for large batch and machine-learning workloads.[^s5]
- A **hybrid** design ingests governed, high-value data (unified profiles, compliance datasets, identity resolution,
  activation) and federates the rest.[^s5]

## Limits and gotchas

- Consumption is metered in credits, so the access pattern drives cost. Salesforce's decision guide shows caching
  being far cheaper for a dashboard over data that changes daily, while Live Query wins for frequently published
  segments over data that changes every half hour.[^s5]
- Incremental cache refresh only upserts; deleted records stay in the cache until a full refresh.[^s5]
- Federated data is not fully governed inside Data 360: row-level security and masking must be enforced at the
  source, which requires a consistent enterprise identifier.[^s5]
- Identity resolution must run before unified DMOs exist, so segments and insights that rely on Unified Individual
  are empty until the first ruleset job completes.[^s4]
- Developer tooling for DMO mapping is partly in developer preview, and Salesforce warns that commands and behaviour
  can change.[^s2]

## When to use it (and when not)

Use Data 360 when several systems hold overlapping customer records and the business needs a unified profile,
cross-source metrics, segmentation and activation, or trusted context for AI agents.[^s5][^s1] For simple
operational integration between Salesforce and one back-office system, event or API integration into the CRM
objects is usually lighter; Data 360 earns its cost when harmonisation and identity resolution are the problem.[^s5]

## Connections

Data 360 sits **under** `kt:salesforce-platform`. It **has parts** `kt:data-model-objects`, `kt:identity-resolution`
and `kt:calculated-insights`, the three stages of its object model, and `kt:zero-copy-data-federation`, its
query-in-place access pattern.[^s1][^s5] It **enables** `kt:agentforce`: Salesforce's architects call Data 360 the
foundational intelligence layer every Agentforce agent draws context from.[^s5] It is **related** to
`kt:change-data-capture`, the change-event mechanism behind its real-time ingestion mode.[^s5]

## Sources
[^s1]: Salesforce Developers, "Object Model in Data 360". https://developer.salesforce.com/docs/data/data-cloud-dev/guide/dc-object-model.html (accessed 2026-11-01)
[^s2]: Salesforce Developers, "Model Data in Data 360". https://developer.salesforce.com/docs/data/data-cloud-dmo-mapping/guide/c360dm-model-data.html (accessed 2026-11-01)
[^s3]: Trailhead, "Create Data Streams". https://trailhead.salesforce.com/content/learn/projects/explore-data-cloud-core-functionality/create-data-streams-1 (accessed 2026-11-01)
[^s4]: Trailhead, "Create an Insight". https://trailhead.salesforce.com/content/learn/projects/explore-data-cloud-core-functionality/create-an-insight (accessed 2026-11-01)
[^s5]: Salesforce Architects, "Data 360 Interoperability". https://architect.salesforce.com/docs/architect/decision-guides/guide/data-360-interoperability (accessed 2026-11-01)
