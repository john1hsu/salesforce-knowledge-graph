---
id: kt:apex-cursors
type: Feature
title: Apex Cursors
aliases: [Database.Cursor, Database.getCursor, Apex pagination cursors, PaginationCursor]
domain: platform-architecture
summary: >-
  A server-side Apex feature that holds the result set of a SOQL query (up to 50 million rows) and lets code fetch it
  in chunks across transactions, typically from chained Queueable jobs, as a flexible alternative to Batch Apex.
release: "Winter '27"
status: current
broader: [kt:apex, kt:large-data-volumes]
related: [kt:limits-class, kt:orglimits-class, kt:lightning-web-components, kt:data-cloud, kt:apex-user-mode]
relations:
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: alternativeTo, object: kt:batch-apex}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: consumedBy, object: kt:queueable-apex}
  - {predicate: dependsOn, object: kt:transaction-finalizers}
sources:
  - id: s1
    title: "Apex Developer Guide: Apex Cursors"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_cursors.htm
    type: official-docs
    accessed: 2026-11-17
  - id: s2
    title: "Apex Developer Guide: Large Data Processing with Cursors and Queueable Apex Versus Batch Apex"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_cursors_versus_batch.htm
    type: official-docs
    accessed: 2026-11-17
  - id: s3
    title: "The Salesforce Developer's Guide to the Spring '26 Release"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2026/01/developers-guide-to-the-spring-26-release
    type: official-blog
    accessed: 2026-11-17
  - id: s4
    title: "Step-Based Async Framework"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/fundamentals/guide/step-based-async-framework
    type: official-docs
    accessed: 2026-11-17
created: 2026-11-17
---

# Apex Cursors

Apex cursors break the result of a SOQL query into chunks that each fit inside one transaction. Code can then work through a very large result set without loading it all at once, and can move both forward and backward through it.[^s1] A cursor is created with `Database.getCursor()` (or `Database.getCursorWithBinds()` for bind variables), which can take an `AccessLevel` such as user mode.[^s1] Salesforce's Spring '26 developer guide announced cursors as generally available from API version 66.0.[^s3]

## How it works

A cursor is stateless: it does not remember where the caller stopped. Code tracks an offset itself and passes it to `Cursor.fetch(position, count)`, while `getNumRecords()` reports the total row count.[^s1] The canonical pattern pairs a cursor with chained Queueable Apex. The job creates the cursor once and keeps it, with a position counter, as an instance variable. Each `execute()` fetches a chunk, processes it, advances the position and re-enqueues itself until no rows remain; the serialized job state carries the same cursor along the chain.[^s1]

The set of record IDs is fixed when the cursor is created, just as with a Batch Apex QueryLocator. Later field edits or sharing changes do not alter it, so a record that stops matching the `WHERE` clause still comes back.[^s1][^s2]

A second variant, the **pagination cursor**, targets UI paging. `Database.getPaginationCursor()` creates it and `fetchPage(start, pageSize)` returns a page; unlike a standard cursor it skips deleted rows so each page stays full.[^s1] Because cursors can be serialized through `@AuraEnabled`, a Lightning web component can pass one back and forth to Apex to page through results.[^s3] Cursors over Data 360 data model objects exist too, but that capability is labelled beta, can consume Data Services credits, and does not support pagination cursors.[^s1]

## Limits and gotchas

Limits as documented for Winter '27 (API 68.0):[^s1]

- A cursor can hold at most 50 million rows, whether used synchronously or asynchronously.[^s1]
- A transaction can make at most 100 `fetch()` calls, counted across standard and pagination cursors.[^s1]
- Each fetch counts against the SOQL query limit, and fetched rows count against the query-row limit.[^s1][^s3]
- Pagination cursors allow a page size of at most 2,000 rows and 100,000 rows across active pagination cursors per transaction.[^s1]
- An org can create 10,000 standard cursors and 200,000 pagination cursors in a rolling 24-hour window.[^s1]
- Cursors expire 48 hours after creation; Data 360 cursors expire after 24 hours.[^s1]

Daily allowances are charged when a cursor is created, not when rows are fetched. A cursor over N rows consumes N rows of the daily row allowance immediately.[^s1] The main anti-pattern is calling `Database.getCursor()` inside `execute()`, which opens a new cursor on every hop and quickly drains the daily cursor and row limits.[^s1] Usage can be read with `Limits` methods such as `getApexCursorRows()` and `getFetchCallsOnApexCursor()`, and the org-wide figures with `OrgLimits.getMap()`.[^s1] A `TransientCursorException` can be retried, while `FatalCursorException` cannot.[^s1] Salesforce's architects also warn that cursor behaviour in tests can differ from production and that mocking is limited, so tests should check orchestration logic rather than cursor internals.[^s4]

## When to use it (and when not)

Batch Apex allows only five active jobs per org, with up to 100 more waiting in the flex queue, so a busy org can see critical jobs delayed.[^s2] A chained Queueable job over a cursor counts as one logical process, uses no batch slot and never enters the flex queue. The developer also controls order and fetch size.[^s2] Pair it with a Transaction Finalizer to isolate errors per Queueable transaction.[^s2] Batch Apex still offers a fixed scope size, sequential execution and built-in error isolation per chunk.[^s2] The Salesforce Architects step-based async framework treats Queueable Apex as the default and prefers cursors over Batch Apex for many large-volume cases.[^s4]

## Connections

Apex cursors are a feature of **Apex** and a tool for **large data volumes**, their broader nodes.[^s1] They are **queried with** **SOQL** and **governed by** the **governor limits** on queries and rows, monitored through the **Limits class** and **OrgLimits class**.[^s1] They are an **alternative to** **Batch Apex** and are **consumed by** **Queueable Apex**, which **depends on** **Transaction Finalizers** for per-transaction error handling.[^s2] Pagination cursors serve **Lightning Web Components**, DMO cursors reach into **Data Cloud** (Data 360), and creation in **user mode** applies the running user's access.[^s1][^s3]

## Sources

[^s1]: Salesforce Developers, "Apex Developer Guide: Apex Cursors" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_cursors.htm (accessed 2026-11-17)
[^s2]: Salesforce Developers, "Apex Developer Guide: Large Data Processing with Cursors and Queueable Apex Versus Batch Apex" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_cursors_versus_batch.htm (accessed 2026-11-17)
[^s3]: Salesforce Developers Blog, "The Salesforce Developer's Guide to the Spring '26 Release". https://developer.salesforce.com/blogs/2026/01/developers-guide-to-the-spring-26-release (accessed 2026-11-17)
[^s4]: Salesforce Architects, "Step-Based Async Framework". https://architect.salesforce.com/docs/architect/fundamentals/guide/step-based-async-framework (accessed 2026-11-17)
