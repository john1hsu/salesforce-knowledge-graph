---
id: kt:bulk-api-allocations
type: Limit
title: Bulk API Allocations
aliases: [Bulk API limits, Bulk API 2.0 limits, DailyBulkApiBatches, DailyBulkV2QueryJobs, DailyBulkV2QueryFileStorageMB, daily bulk batch allocation]
domain: integration
summary: >-
  The org-wide quotas and per-job limits that govern Bulk API and Bulk API 2.0: a shared pool of batches per rolling
  24 hours, a separate daily allowance of Bulk API 2.0 query jobs and result storage, and size, lifespan, retry and
  CPU limits on individual jobs and batches.
release: "Winter '27"
status: current
broader: [kt:governor-limits]
related: [kt:bulk-api-1, kt:bulk-api-2, kt:large-data-volumes, kt:data-migration-strategy, kt:data-loader]
relations:
  - {predicate: contrastsWith, object: kt:api-request-limits}
  - {predicate: queriedWith, object: kt:rest-api}
sources:
  - id: s1
    title: "Bulk API and Bulk API 2.0 Limits and Allocations (Salesforce Developer Limits and Allocations Quick Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-app-limits-cheatsheet/guide/salesforce-app-limits-platform-bulkapi.html
    type: official-docs
    accessed: 2026-11-15
  - id: s2
    title: "Understanding Bulk API 2.0 Ingest (Bulk API 2.0 and Bulk API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-asynch/guide/datafiles-understanding-bulk2-ingest.html
    type: official-docs
    accessed: 2026-11-15
  - id: s3
    title: "Limits (Bulk API 2.0 and Bulk API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-asynch/guide/bulk-common-limits.html
    type: official-docs
    accessed: 2026-11-15
  - id: s4
    title: "Limits (REST API Developer Guide, resources)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_limits.htm
    type: official-docs
    accessed: 2026-11-15
created: 2026-11-15
---

# Bulk API Allocations

Bulk API allocations are the quotas that cap how much asynchronous bulk work an org can push through Salesforce. The central one is a pool of 15,000 batches per rolling 24-hour period, shared by Bulk API 1.0 and Bulk API 2.0, so a migration tool on one API and a nightly sync on the other draw down the same allowance.[^s1] Around that pool sit per-job limits on file size, record size, job lifespan, retries and processing time, plus separate daily allowances for Bulk API 2.0 queries.[^s1][^s3] Values in this node were checked against the Winter '27 documentation.

## How it works

Which operations consume batches differs by API. In Bulk API 1.0 the client creates batches itself, and both ingest and query batches count against the pool; in Bulk API 2.0 the platform creates batches automatically and only ingest jobs consume them.[^s1][^s4] For a 2.0 ingest job, Salesforce opens a separate batch for every 10,000 records it receives, under an empty parent batch tied to the upload, and processes those sub-batches in parallel.[^s2] The record ceiling follows from the pool: 150,000,000 records uploaded per rolling 24 hours for both APIs, which for Bulk API 1.0 is expressed as 15,000 batches of 10,000 records.[^s1]

Bulk API 2.0 queries have their own meters instead. An org may run 10,000 Bulk API 2.0 query jobs per rolling 24 hours and retrieve up to 1 TB of query results in that window, while Bulk API 1.0 queries keep drawing from the shared batch pool.[^s1] Inside each batch, records are processed in chunks of 200 for API version 21.0 and later (100 in 20.0 and earlier), and Bulk API work is subject to a dedicated limit of 60,000 milliseconds of server CPU time, separate from the generic per-transaction Apex CPU limit.[^s1][^s3]

## Limits and gotchas

Per-job limits differ between the two APIs, and they are easy to confuse.[^s1]

- **Upload size:** Bulk API 1.0 accepts 10 MB and 10,000 records per batch; Bulk API 2.0 accepts 150 MB of base64-encoded CSV per job, so stay under about 100 MB raw.[^s1]
- **Record shape:** both allow at most 5,000 fields per record, 400,000 characters per record and 131,072 characters per field.[^s1]
- **Lifespan:** a job can stay open for 24 hours, and results remain available for 7 days after completion unless the job is deleted.[^s1]
- **Ingest retries:** a 2.0 batch that cannot finish within 5 minutes is retried up to 20 times; after that the whole job fails and the remaining data is not processed.[^s2]
- **Query timeouts:** Bulk API 1.0 allows 30 attempts and a 2-minute processing limit per query, and results must be retrieved within 20 minutes.[^s1]

The classic trap is tiny batches. In Bulk API 1.0 every client-created batch counts once regardless of size, so splitting a load into many small batches exhausts the 15,000 pool long before the record ceiling; the guidance is to start around 10,000 records per batch and shrink only if batches time out.[^s1] In 2.0, exceeding the daily record limit mid-job leaves unprocessed data and marks the job failed, so large loads should be paced across windows.[^s2] Failed or unprocessed rows from a 2.0 job are recovered by creating a new ingest job from the failed and unprocessed result sets.[^s2]

## Monitoring

The REST API Limits resource reports `DailyBulkApiBatches`, `DailyBulkV2QueryJobs` and `DailyBulkV2QueryFileStorageMB`, each with the maximum and the remaining amount, to users with the View Setup and Configuration permission.[^s4] Its figures are accurate to within about five minutes of consumption, so integrations should poll it sparingly rather than before every batch.[^s4] `DailyBulkApiBatches` was called `DailyBulkApiRequests` in API version 48.0 and earlier.[^s4]

## Connections

This node sits under `kt:governor-limits` as the quota family for asynchronous bulk work, and it governs both `kt:bulk-api-1` and `kt:bulk-api-2`, which share its batch pool.[^s1] It contrasts with `kt:api-request-limits`: the bulk pool counts batches and query jobs rather than individual calls, and the bulk documentation points to the separate daily API request allocation.[^s3] Usage is read through the Limits resource of `kt:rest-api`.[^s4] Budgeting batches is a core concern in `kt:large-data-volumes` and `kt:data-migration-strategy`, where loads of hundreds of millions of rows can run into the 150,000,000-record daily ceiling.[^s1] `kt:data-loader` is linked as a common bulk client, described in its own node.

## Sources

[^s1]: Salesforce Developers, "Bulk API and Bulk API 2.0 Limits and Allocations". https://developer.salesforce.com/docs/platform/salesforce-app-limits-cheatsheet/guide/salesforce-app-limits-platform-bulkapi.html (accessed 2026-11-15)
[^s2]: Salesforce Developers, "Understanding Bulk API 2.0 Ingest". https://developer.salesforce.com/docs/platform/api-asynch/guide/datafiles-understanding-bulk2-ingest.html (accessed 2026-11-15)
[^s3]: Salesforce Developers, "Limits" (Bulk API 2.0 and Bulk API Developer Guide). https://developer.salesforce.com/docs/platform/api-asynch/guide/bulk-common-limits.html (accessed 2026-11-15)
[^s4]: Salesforce Developers, "Limits" (REST API Developer Guide). https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_limits.htm (accessed 2026-11-15)
