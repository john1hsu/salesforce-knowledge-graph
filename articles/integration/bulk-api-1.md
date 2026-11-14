---
id: kt:bulk-api-1
type: API
title: Bulk API 1.0
aliases: [Bulk API v1, original Bulk API, Bulk API (1.0), client-managed batch Bulk API]
domain: integration
summary: >-
  Salesforce's original asynchronous API for loading and extracting large record sets, in which the client creates a
  job and then splits its data into batches of CSV, XML or JSON that it submits, monitors and collects results for
  itself, with options such as serial concurrency mode and PK chunking that Bulk API 2.0 does not expose.
release: "Winter '27"
status: current
broader: [kt:salesforce-apis, kt:data-integration]
related: [kt:large-data-volumes, kt:record-locking, kt:external-id-fields, kt:data-loader, kt:soql]
relations:
  - {predicate: contrastsWith, object: kt:bulk-api-2}
  - {predicate: governedBy, object: kt:bulk-api-allocations}
  - {predicate: alternativeTo, object: kt:soap-api}
sources:
  - id: s1
    title: "How Bulk API Works (Bulk API 2.0 and Bulk API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-asynch/guide/api-asynch-introduction-how-bulk-api-works.html
    type: official-docs
    accessed: 2026-11-14
  - id: s2
    title: "JobInfo (Bulk API 2.0 and Bulk API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/asynch_api_reference_jobinfo.htm
    type: official-docs
    accessed: 2026-11-14
  - id: s3
    title: "Bulk API and Bulk API 2.0 Limits and Allocations (Salesforce Developer Limits and Allocations Quick Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-app-limits-cheatsheet/guide/salesforce-app-limits-platform-bulkapi.html
    type: official-docs
    accessed: 2026-11-14
  - id: s4
    title: "PK Chunking (Bulk API 2.0 and Bulk API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-asynch/guide/async-api-headers-enable-pk-chunking.html
    type: official-docs
    accessed: 2026-11-14
created: 2026-11-14
---

# Bulk API 1.0

Bulk API 1.0 (documented simply as "Bulk API" alongside Bulk API 2.0) is the original asynchronous Salesforce API for processing large data sets. Its unit of work is a **job**, which names one object and one operation, and the data travels in **batches**: sets of records sent as separate HTTP POST requests in CSV, XML or JSON, optionally with references to binary attachments.[^s1] Unlike Bulk API 2.0, the client decides how to cut the data set into batches and must track each one.[^s1][^s3]

## How it works

A typical load runs in six steps: create a job, submit the data in batches, close the job once all batches are sent, poll batch status at a sensible interval, retrieve each batch's results once it has completed or failed, and match those results back to the source data to find the records that failed.[^s1] Batches are processed independently and not necessarily in the order they arrived, and aborting a job stops unprocessed batches without rolling back batches that already ran.[^s1]

The job definition (the JobInfo resource) carries the settings that make 1.0 more configurable than its successor:[^s2]

- **operation:** `insert`, `update`, `upsert`, `delete`, `hardDelete`, `query` or `queryAll`, and the value is case-sensitive.[^s2]
- **contentType:** `XML` is the 1.0 default, with `CSV`, `JSON` and `ZIP_` variants that bundle binary attachments; Bulk API 2.0 jobs accept CSV only.[^s2]
- **concurrencyMode:** `Parallel` by default; `Serial` processes one batch at a time to avoid lock contention, at the cost of much longer runs.[^s2]
- **externalIdFieldName:** required for `upsert`, so loads can match on a field from the source system instead of the Salesforce ID.[^s2]
- **assignmentRuleId:** runs a lead or case assignment rule for the loaded records; it can't be changed after the job is created.[^s2]

`hardDelete` bypasses the Recycle Bin and requires the Bulk API Hard Delete permission, which an administrator must grant.[^s2] A job moves through the states Open, Closed, Aborted and Failed; when a job fails, batches that already succeeded are not rolled back.[^s2]

For extracts, 1.0 offers **PK chunking**, enabled with the `Sforce-Enable-PKChunking` request header. Salesforce splits the query into record-ID ranges, each run as its own batch that counts toward the daily batch allocation; the default chunk size is 100,000 records and the maximum is 250,000.[^s4] When chunking succeeds, the original batch is marked `NOT_PROCESSED` and the client downloads each chunk's results separately; using `ORDER BY`, `LIMIT` or a filter on a field whose name contains "id" effectively turns chunking off.[^s4]

## Limits and gotchas

Values below are from the Limits and Allocations quick reference, checked against Winter '27:[^s3]

- **Batch size:** at most 10,000 records, 10 MB and 10,000,000 characters per batch; Salesforce suggests starting at 10,000 records and reducing if batches time out.[^s3]
- **Daily volume:** 15,000 batches per rolling 24 hours, a pool shared with Bulk API 2.0 ingest jobs, which caps uploads at 150,000,000 records a day.[^s3]
- **Lifetime:** batches can't be added to a job more than 24 hours old, and jobs older than 7 days whose batches are terminal are removed.[^s3]
- **Retries:** a failed batch is retried after 5 minutes; a query batch gets up to 30 attempts before failing with "Tried more than thirty times".[^s3]
- **Query results:** a query batch has 2 minutes to process before a `QUERY_TIMEOUT`, may return at most 15 result files of up to 1 GB each, and results are retained for 7 days.[^s3]
- **Binary attachments:** zip files are capped at 10 MB zipped, 20 MB unzipped and 1,000 files.[^s3]

The default parallel mode is the main operational hazard: concurrent batches that touch the same parent record compete for its lock, and the failed records must be resubmitted by the client. Switching to serial mode trades that contention for throughput.[^s2] Because the client owns batching, it also owns retries, result reconciliation and polling discipline, which Bulk API 2.0 handles itself.[^s1][^s3]

## When to use it (and when not)

For most new ingest work Bulk API 2.0 is simpler: the client uploads one file of up to 150 MB per job and Salesforce manages batches and retries.[^s3] Bulk API 1.0 remains the better fit when you need features 2.0 does not offer, such as XML or JSON payloads, binary attachments, serial concurrency, explicit per-batch control or PK chunking for very large extracts.[^s2][^s4] For small, interactive transactions the synchronous APIs remain the right choice, since bulk jobs are polled rather than answered immediately.[^s1]

## Connections

Bulk API 1.0 sits under `kt:salesforce-apis` and `kt:data-integration`, and it contrasts with `kt:bulk-api-2`, which shares its daily batch pool but hides batching from the client.[^s3] Both are governed by `kt:bulk-api-allocations`.[^s3] Its parallel mode makes `kt:record-locking` the classic failure, and serial mode is the documented remedy.[^s2] Upserts depend on `kt:external-id-fields`, query batches run `kt:soql` with PK chunking for `kt:large-data-volumes`, and the synchronous `kt:soap-api` is the alternative for small payloads.[^s2][^s4] `kt:data-loader` is linked as the admin-facing load tool that sits on top of the bulk APIs, described in its own node.

## Sources

[^s1]: Salesforce Developers, "How Bulk API Works (Bulk API 2.0 and Bulk API Developer Guide)". https://developer.salesforce.com/docs/platform/api-asynch/guide/api-asynch-introduction-how-bulk-api-works.html (accessed 2026-11-14)
[^s2]: Salesforce Developers, "JobInfo (Bulk API 2.0 and Bulk API Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/asynch_api_reference_jobinfo.htm (accessed 2026-11-14)
[^s3]: Salesforce Developers, "Bulk API and Bulk API 2.0 Limits and Allocations". https://developer.salesforce.com/docs/platform/salesforce-app-limits-cheatsheet/guide/salesforce-app-limits-platform-bulkapi.html (accessed 2026-11-14)
[^s4]: Salesforce Developers, "PK Chunking (Bulk API 2.0 and Bulk API Developer Guide)". https://developer.salesforce.com/docs/platform/api-asynch/guide/async-api-headers-enable-pk-chunking.html (accessed 2026-11-14)
