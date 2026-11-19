---
id: kt:ingestion-api
type: API
title: Ingestion API
aliases: [Data 360 Ingestion API, Data Cloud Ingestion API, Ingestion API connector, CDP Ingestion API, cdp_ingest_api]
domain: data-cloud-and-ai
summary: >-
  The REST API for pushing records from an external system into Data 360 (formerly Data Cloud), either as streaming JSON micro-batches or as bulk CSV jobs, through an Ingestion API connector whose objects are defined by an OpenAPI schema.
release: "Winter '27"
status: current
broader: [kt:data-cloud]
related: [kt:data-lake-objects, kt:data-model-objects, kt:change-data-capture]
relations:
  - {predicate: enables, object: kt:data-streams}
  - {predicate: governedBy, object: kt:data-cloud-limits}
  - {predicate: dependsOn, object: kt:external-client-apps}
  - {predicate: dependsOn, object: kt:jwt-bearer-flow}
  - {predicate: alternativeTo, object: kt:bulk-api-2}
sources:
  - id: s1
    title: "Ingestion API (Data 360 Integration Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-ingestion-api.html
    type: official-docs
    accessed: 2026-11-19
  - id: s2
    title: "Get Started with Ingestion API (Ingestion API Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-int/references/data-cloud-ingestionapi-ref/c360-a-api-get-started.html
    type: official-docs
    accessed: 2026-11-19
  - id: s3
    title: "Requirements for Ingestion API Schema File"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-ingestion-api-schema-req.html
    type: official-docs
    accessed: 2026-11-19
  - id: s4
    title: "Set Up Ingestion API Connector"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-connect-an-ingestion-source.html
    type: official-docs
    accessed: 2026-11-19
  - id: s5
    title: "Load Data Programmatically with the Ingestion API"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2023/07/load-data-programmatically-with-the-ingestion-api
    type: official-blog
    accessed: 2026-11-19
created: 2026-11-19
---

# Ingestion API

The **Ingestion API** is the REST API an external system uses to push its own data into Data 360 (formerly Data
Cloud). It offers two interaction patterns. **Streaming** takes incremental changes as they are captured, and
**bulk** takes CSV files for periodic syncs. A single data stream can receive data from both patterns.[^s1] It is
the programmatic counterpart to the packaged connectors: instead of Data 360 pulling from a source, the source
calls Data 360.[^s5]

## How it works

Setup is split between an admin and a developer. The team agrees on the data to send and writes a schema file,
sets up an Ingestion API connector, creates an app for OAuth, creates and deploys data streams, calls the object
endpoints, and finally maps the ingested data to standard or custom objects.[^s1]

The **connector** lives in Data Cloud Setup under Ingestion API. Creating one needs the System Admin profile or the
Data Cloud Architect permission set. You name the source, upload an OpenAPI schema, review the objects and fields it
detected, and save. The connector shows **Needs Data Stream** until a stream for it is active, then **In Use**.[^s4]

The **schema** must be valid OpenAPI 3.0.x in a `.yml` or `.yaml` file. Each object needs at least one field and
can have no more than 1,000. Nested objects aren't allowed. Object names can be up to 79 characters and field names
up to 39.[^s3] Supported field types are boolean, date, datetime, email, number, phone, percent, text and URL, all
expressed as OpenAPI `type`/`format` pairs.[^s3]

**Authentication** is a two-step token exchange. The client first gets a normal Salesforce access token, for
example with the JWT bearer grant, from an app that has the `cdp_ingest_api` and `api` scopes plus
`refresh_token`/`offline_access`. It then posts that token to `/services/a360/token` on the returned instance URL
and receives a Data 360 token and a tenant-specific endpoint.[^s2] The official guide now calls the OAuth app an
external client application in its setup links.[^s1]

**Streaming** calls send JSON to `/api/v1/ingest/sources/{connector}/{object}` and get back `accepted: true`.
Adding `/actions/test` to the same path validates records against the schema without loading them.[^s5]
**Bulk** works through jobs: create a job for an object and an upsert or delete operation, upload CSV data, mark it
ready for processing, then close or abort it.[^s5]

## Limits and gotchas

Figures below are as stated in the Ingestion API reference, checked for Winter '27.[^s2]

- **Request size.** Streaming bodies are capped at 200 KB per request, and a streaming delete removes at most 200 records. Bulk CSV files are capped at 150 MB.[^s2]
- **Bulk jobs.** Upload one file at a time, up to 100 files per job. Jobs left Open or Upload Complete for more than 7 days are deleted from the queue.[^s2]
- **Rate limits.** Bulk allows 20 jobs per hour and 5 concurrent jobs. Streaming allows 250 requests per second across all object endpoints. An HTTP 429 means back off and retry.[^s2]
- **Latency.** Streaming data is processed asynchronously about every 3 minutes, and reads are eventually consistent, so wait at least 30 seconds before querying freshly ingested data.[^s2]
- **The schema is append-only.** You can't delete objects or fields once added or change a field's type, and an updated object must still list all of its existing fields.[^s3]
- **Field names, not API names.** Payloads must use the schema's field names. Otherwise records land as blank rows.[^s3]
- **Engagement objects need a datetime.** An object meant for the engagement category must include a datetime field. Each object supports only one data stream per connection.[^s3]
- **Expired tokens.** A 401 means the token is invalid or expired. The JWT's lifetime follows the app's session timeout setting.[^s2]

## When to use it (and when not)

Use **streaming** for near real-time changes in small batches, such as webhooks, modern event sources or Change
Data Capture events. Use **bulk** for large daily, weekly or monthly loads, legacy systems that can only export
off-peak, and backfills of 30 to 90 or more days of history.[^s5] When the source is a Salesforce org or a system
with a ready-made connector, a standard data stream needs no code. The Ingestion API is for custom or unsupported
sources.[^s1][^s5] It writes only into Data 360, so it is no substitute for the core platform's bulk loading APIs.[^s1]

## Connections

The Ingestion API is part of `kt:data-cloud` and **enables** Ingestion API `kt:data-streams`. Each stream lands in
`kt:data-lake-objects` and is then mapped to `kt:data-model-objects`.[^s1] Its quotas are **governed by**
`kt:data-cloud-limits`.[^s2] Clients **depend on** an OAuth app, now an `kt:external-client-apps` registration, and
typically the `kt:jwt-bearer-flow` to get the Salesforce token that is exchanged for a Data 360 token.[^s1][^s2]
Streaming suits feeds such as `kt:change-data-capture` events.[^s5] It is an **alternative to** `kt:bulk-api-2` in
shape, since both run CSV jobs, but the Ingestion API targets Data 360 rather than core CRM objects.[^s1][^s5]

## Sources

[^s1]: Salesforce Developers, "Ingestion API" (Data 360 Integration Guide). https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-ingestion-api.html (accessed 2026-11-19)
[^s2]: Salesforce Developers, "Get Started with Ingestion API" (Ingestion API Reference). https://developer.salesforce.com/docs/data/data-cloud-int/references/data-cloud-ingestionapi-ref/c360-a-api-get-started.html (accessed 2026-11-19)
[^s3]: Salesforce Developers, "Requirements for Ingestion API Schema File". https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-ingestion-api-schema-req.html (accessed 2026-11-19)
[^s4]: Salesforce Developers, "Set Up Ingestion API Connector". https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-connect-an-ingestion-source.html (accessed 2026-11-19)
[^s5]: Julián Duque and Aditya Naag Topalli, "Load Data Programmatically with the Ingestion API", Salesforce Developers Blog, 2023-07-18. https://developer.salesforce.com/blogs/2023/07/load-data-programmatically-with-the-ingestion-api (accessed 2026-11-19)
