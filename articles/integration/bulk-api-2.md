---
id: kt:bulk-api-2
type: API
title: Bulk API 2.0
aliases: [Bulk API v2, Bulk 2.0, bulk ingest jobs, Bulk API 2.0 query jobs]
domain: integration
summary: >-
  Salesforce's REST-based asynchronous API for inserting, updating, upserting, deleting and querying large record sets
  through CSV jobs, where the platform splits uploaded data into batches automatically instead of the client managing
  them as in the original Bulk API.
release: "Winter '27"
status: current
broader: [kt:salesforce-apis, kt:data-integration]
related: [kt:large-data-volumes, kt:data-migration-strategy, kt:record-locking, kt:soql, kt:external-id-fields, kt:data-loader]
relations:
  - {predicate: governedBy, object: kt:bulk-api-allocations}
  - {predicate: contrastsWith, object: kt:bulk-api-1}
  - {predicate: alternativeTo, object: kt:rest-api}
sources:
  - id: s1
    title: "Bulk API 2.0 (Bulk API 2.0 and Bulk API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/bulk_api_2_0.htm
    type: official-docs
    accessed: 2026-11-02
  - id: s2
    title: "Bulk API and Bulk API 2.0 Limits and Allocations (Salesforce Developer Limits and Allocations Quick Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-app-limits-cheatsheet/guide/salesforce-app-limits-platform-bulkapi.html
    type: official-docs
    accessed: 2026-11-02
  - id: s3
    title: "API Basics: Use Bulk API 2.0"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/content/learn/modules/api_basics/api_basics_bulk
    type: official-learning
    accessed: 2026-11-02
  - id: s4
    title: "General Guidelines for Data Loads"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-asynch/guide/asynch-api-planning-guidelines.html
    type: official-docs
    accessed: 2026-11-02
  - id: s5
    title: "Bulk API and Bulk API 2.0 Limits (Bulk API 2.0 and Bulk API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-asynch/guide/bulk-common-limits.html
    type: official-docs
    accessed: 2026-11-02
created: 2026-11-02
---

# Bulk API 2.0

Bulk API 2.0 is a REST-based API for asynchronously inserting, updating, upserting, deleting and querying large data sets in a Salesforce org. It is enabled by default in Performance, Unlimited, Enterprise and Developer editions, and the calling user needs the API Enabled permission.[^s1] It is the platform's answer for volumes from a few thousand to millions of records, where the synchronous REST and SOAP APIs, built for a handful of records per call, become slow and chatty.[^s3]

## How it works

There are two job types. **Ingest jobs** load a CSV file against one object with one operation (insert, update, upsert or delete); **query jobs** run a SOQL statement asynchronously and are intended for result sets of roughly 2,000 records or more.[^s1]

An ingest job follows a short lifecycle. The client POSTs to the `jobs/ingest` resource with the operation, object, content type and line ending (LF is the default if none is given); the new job is in the **Open** state and returns a job ID and a content URL. The client PUTs the CSV to that URL, then PATCHes the job to **UploadComplete**, which tells Salesforce to start processing. When the job reaches **JobComplete** (or **Failed**), the client GETs separate result sets of successful records, with their IDs and a created flag, and of failed records with error messages.[^s3]

The defining difference from the original Bulk API is batching. In Bulk API 1.0 the client creates and manages batches as well as jobs, using different resource URIs; in 2.0 the client simply uploads data and Salesforce decides how to split and load it.[^s3] Internally the platform still processes records in chunks of 200 for API version 21.0 and later, the same as Bulk API, and it retries failed work automatically.[^s2]

## Limits and gotchas

Values below are as published in the Limits and Allocations quick reference, checked against Winter '27:[^s2]

- **Volume:** 150,000,000 uploaded records per rolling 24 hours, and 15,000 batches per rolling 24 hours shared with Bulk API 1.0. Only ingest jobs consume batches; query jobs do not.[^s2]
- **Upload size:** 150 MB of base64-encoded CSV per ingest job. Because base64 encoding inflates data by about 50%, Salesforce recommends keeping raw uploads under 100 MB.[^s2]
- **Record shape:** at most 131,072 characters per field, 400,000 characters per record and 5,000 fields per record.[^s2]
- **Lifetime:** an ingest job can stay open for at most 24 hours; results can be retrieved for 7 days after completion, and terminal jobs are deleted after seven days.[^s2]
- **Retries:** if an ingest job is retried more than 20 times, split it into a smaller file; if a query is retried more than 15 times, add filter criteria.[^s2]
- **Query jobs:** 10,000 per rolling 24 hours and 1 TB of results per rolling 24 hours, tracked as `DailyBulkV2QueryJobs` and `DailyBulkV2QueryFileStorageMB` in the REST `/limits` resource. Clients page through results with the `locator` and `maxRecords` parameters, and there is a 20-minute results-retrieval timeout.[^s2]

Processing is also bounded server-side: Bulk API and Bulk API 2.0 share a 60,000 ms CPU-time limit on Salesforce servers, separate from the per-transaction Apex CPU limit that triggers still hit.[^s5]

The most common practical failure is lock contention. Records are processed in parallel by default, so children that reference the same parent can fight over its lock and fail; Salesforce advises grouping child records by parent ID in the source file, and treating user creation, ownership changes on privately shared records, role changes and territory updates as contention-prone operations to isolate in a separate job.[^s4] Lookup, foreign-key and roll-up summary fields, plus heavy triggers and workflow, slow processing; for complex trigger logic the guidance is to defer it to a batch Apex job after the load and to rehearse loads in a sandbox first.[^s4]

## When to use it (and when not)

Use Bulk API 2.0 for migrations, nightly synchronisations, mass updates and large extracts, especially when you want simpler client code and the platform to manage batching.[^s3] Most admins reach it through Data Loader with CSV files rather than writing custom clients.[^s3] Stay with synchronous REST or SOAP calls for small, user-facing transactions that need an immediate answer.[^s3] Choose Bulk API 1.0 only when you need explicit control over each batch, since 2.0 deliberately hides that layer.[^s3]

## Connections

Bulk API 2.0 sits under `kt:salesforce-apis` and `kt:data-integration` as the high-volume member of the API family, and it contrasts with `kt:bulk-api-1`, which shares its daily batch allocation but requires client-managed batches.[^s2][^s3] It is the usual load path in `kt:data-migration-strategy` and `kt:large-data-volumes`, where `kt:external-id-fields` make upserts idempotent, and query jobs execute `kt:soql`.[^s1] Its main failure mode is `kt:record-locking` under parallel processing, and its quotas form `kt:bulk-api-allocations`.[^s2][^s4] `kt:data-loader` is the most common client, and the synchronous `kt:rest-api` is the alternative for small payloads.[^s3]

## Sources

[^s1]: Salesforce Developers, "Bulk API 2.0 (Bulk API 2.0 and Bulk API Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/bulk_api_2_0.htm (accessed 2026-11-02)
[^s2]: Salesforce Developers, "Bulk API and Bulk API 2.0 Limits and Allocations". https://developer.salesforce.com/docs/platform/salesforce-app-limits-cheatsheet/guide/salesforce-app-limits-platform-bulkapi.html (accessed 2026-11-02)
[^s3]: Trailhead, "API Basics: Use Bulk API 2.0". https://trailhead.salesforce.com/en/content/learn/modules/api_basics/api_basics_bulk (accessed 2026-11-02)
[^s4]: Salesforce Developers, "General Guidelines for Data Loads". https://developer.salesforce.com/docs/platform/api-asynch/guide/asynch-api-planning-guidelines.html (accessed 2026-11-02)
[^s5]: Salesforce Developers, "Bulk API and Bulk API 2.0 Limits". https://developer.salesforce.com/docs/platform/api-asynch/guide/bulk-common-limits.html (accessed 2026-11-02)
