---
id: kt:data-streams
type: Feature
title: Data Streams
aliases: [data stream, Data 360 data streams, Data Cloud data streams, DataStreamTemplate]
domain: data-cloud-and-ai
summary: >-
  The ingestion pipeline of Data 360 (formerly Data Cloud): a configured feed from one source object, such as a CRM
  object, a website event or an external connector, that loads records on a refresh mode and schedule into a data lake object.
release: "Winter '27"
status: current
broader: [kt:data-cloud]
related: [kt:data-integration, kt:data-model-objects, kt:zero-copy-data-federation]
relations:
  - {predicate: enables, object: kt:data-lake-objects}
  - {predicate: integratesWith, object: kt:ingestion-api}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: governedBy, object: kt:data-cloud-limits}
  - {predicate: coveredBy, object: kt:data-cloud-consultant-certification}
sources:
  - id: s1
    title: "Create a Data Stream (Create a Data Stream in Data Cloud project)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/create-a-data-stream-in-data-cloud/create-a-data-stream
    type: official-learning
    accessed: 2026-11-09
  - id: s2
    title: "Create a ZoomInfo Data Stream"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-zoominfo-data-stream.html
    type: official-docs
    accessed: 2026-11-09
  - id: s3
    title: "DataStreamTemplate (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_datastreamtemplate.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s4
    title: "Create a Web or Mobile App Data Stream"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-mobile-web-datastream.html
    type: official-docs
    accessed: 2026-11-09
  - id: s5
    title: "Upsert Records (Ingestion API Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-int/references/data-cloud-ingestionapi-ref/c360-a-api-insert-records.html
    type: official-docs
    accessed: 2026-11-09
created: 2026-11-09
---

# Data Streams

A **data stream** is how data gets into Data 360 (formerly Data Cloud). Once an admin has configured a data source
(another Salesforce org, a Marketing Cloud Engagement business unit, an external platform or a CSV file), you create
streams from the **Data Streams** tab. Each stream picks source objects or events and deploys them into the
platform.[^s1] Deploying a stream gives the data its first home, a data lake object, and from there it is mapped to
the Customer 360 Data Model.[^s1][^s2]

## How it works

Creating a stream follows the same basic sequence whatever the connector: choose the source, choose the object or
events, set the object details (category, primary key, optional record-modified and organization-unit fields),
assign a data space if you aren't using the default, set the refresh schedule, and deploy.[^s2] If the source has
no usable unique key, or you need a composite key, you can build one with a formula field. Formula fields on a
stream are also used to standardize formats, add join keys, or flag records that meet a condition.[^s1][^s2]

For Salesforce CRM, a **data bundle** speeds this up. Choosing the Sales bundle in the Trailhead project deploys
three data streams at once, and starter bundles come pre-mapped to the Customer 360 Data Model, which you can then
customize.[^s1] For a website or mobile app, the architect first uploads the app's JSON event schema in Setup. Each
Profile or Other event then gets its own stream, while all Engagement events share a single stream.[^s4]

Streams are also metadata. In Metadata API, `DataStreamTemplate` represents a stream added to a data kit, so a
stream definition can be packaged and moved between orgs. The type requires the Customize Application permission
and doesn't support the `*` wildcard in `package.xml`.[^s3]

## Refresh modes and schedules

The refresh mode decides what a new load does to data already in the lake. The metadata enumeration includes
`FULL_REFRESH`, `UPSERT`, `INCREMENTAL`, `REPLACE`, `NEAR_REAL_TIME_INCREMENTAL`, `PARTIAL_UPDATE` and `STREAMING`,
but each connector offers only some of these.[^s3]

- **Full refresh** deletes the previous data and replaces it with the new load. It is the default for the ZoomInfo
  connector.[^s2]
- **Incremental** (web and mobile profile streams) writes fields that have new values and blanks out fields that
  didn't change. **Partial** writes only the changed fields and keeps everything else.[^s4]
- **Upsert vs. append.** Upsert-mode engagement streams merge records by primary key, so they don't create
  duplicates. Append-mode streams deliver at least once and don't deduplicate, so retries can produce duplicate
  rows.[^s4]
- **Ingestion API streaming** loads by upsert. To send partial updates you must select Partial as the stream's
  refresh mode, and each payload carries the primary key and a newer record-modified value.[^s5]

Schedules depend on the connector. ZoomInfo streams refresh daily, weekly or monthly and can also be refreshed by
hand.[^s2] The metadata frequency values range from `MINUTES_5` through hourly, every 4 or 12 hours, daily, weekly
and monthly, plus `STREAMING`.[^s3]

## Limits and gotchas

- **Latency.** Web and mobile streams ingest engagement data every 15 minutes and profile data every hour.[^s4] An
  Ingestion API call returns HTTP 202 with `accepted: true`. That means only that the request was queued; processing
  is asynchronous.[^s5]
- **Wrong refresh mode loses data.** Incremental mode blanks unchanged fields. If a source sends only deltas, choose
  Partial.[^s4]
- **Duplicates in append mode.** Count engagement events in queries with deduplication, or use upsert mode.[^s4]
- **Permissions.** Creating a web or mobile app stream needs the Data Cloud Architect permission.[^s4]
- The pages used here state no per-org cap on the number of streams. Check the Data 360 limits documentation
  instead of assuming one.[^s2][^s3]

## When to use it (and when not)

Use a data stream when Data 360 should hold and refresh its own copy of the source data. For CRM objects, start
from a bundle so the mappings already exist.[^s1] When a source should be queried where it lives rather than copied
in, zero-copy federation is the alternative. When records have to arrive programmatically and continuously, an
Ingestion API stream is the better fit than a scheduled batch connector.[^s5]

## Connections

Data streams are the intake layer of `kt:data-cloud`. A deployed stream **enables** `kt:data-lake-objects`, and its
fields are then mapped to `kt:data-model-objects`.[^s1][^s2] Streaming and bulk loads from custom systems
**integrate with** `kt:ingestion-api`.[^s5] Stream definitions travel between orgs as `DataStreamTemplate`
components, so streams are **configured via** `kt:metadata-api`.[^s3] Capacity is **governed by**
`kt:data-cloud-limits`. Stream design sits within the broader `kt:data-integration` discipline and is an
alternative to copying-free `kt:zero-copy-data-federation`. Building streams is **covered by**
`kt:data-cloud-consultant-certification`.[^s2][^s4]

## Sources

[^s1]: Trailhead, "Create a Data Stream". https://trailhead.salesforce.com/content/learn/projects/create-a-data-stream-in-data-cloud/create-a-data-stream (accessed 2026-11-09)
[^s2]: Salesforce Developers, "Create a ZoomInfo Data Stream". https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-zoominfo-data-stream.html (accessed 2026-11-09)
[^s3]: Salesforce Developers, "DataStreamTemplate" (Metadata API Developer Guide). https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_datastreamtemplate.htm (accessed 2026-11-09)
[^s4]: Salesforce Developers, "Create a Web or Mobile App Data Stream". https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-mobile-web-datastream.html (accessed 2026-11-09)
[^s5]: Salesforce Developers, "Upsert Records" (Ingestion API Reference). https://developer.salesforce.com/docs/data/data-cloud-int/references/data-cloud-ingestionapi-ref/c360-a-api-insert-records.html (accessed 2026-11-09)
