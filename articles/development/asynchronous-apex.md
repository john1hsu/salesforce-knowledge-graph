---
id: kt:asynchronous-apex
type: Feature
title: Asynchronous Apex
aliases: [async Apex, Apex async processing, background Apex jobs]
domain: development
summary: >-
  The family of Apex execution modes (Queueable, Batch, Scheduled and future methods) that run code later, outside
  the request that triggered it, with their own transaction and generally higher per-transaction limits.
release: "Winter '27"
status: current
broader: [kt:apex]
related: [kt:apex-triggers, kt:order-of-execution, kt:scheduled-apex]
relations:
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: hasPart, object: kt:queueable-apex}
  - {predicate: hasPart, object: kt:batch-apex}
  - {predicate: hasPart, object: kt:future-methods}
sources:
  - id: s1
    title: "Apex Developer Guide: Asynchronous Apex"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_async_overview.htm
    type: official-docs
    accessed: 2026-10-30
  - id: s2
    title: "Apex Developer Guide: Queueable Apex"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_queueing_jobs.htm
    type: official-docs
    accessed: 2026-10-30
  - id: s3
    title: "Apex Developer Guide: Use Batch Apex"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_batch_interface.htm
    type: official-docs
    accessed: 2026-10-30
  - id: s4
    title: "Apex Developer Guide: Future Methods"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_invoking_future_methods.htm
    type: official-docs
    accessed: 2026-10-30
  - id: s5
    title: "Apex Basics for .NET Developers: Use Asynchronous Apex"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/microsoft_dotnet/apex_basics_dotnet/async_apex
    type: official-learning
    accessed: 2026-10-30
created: 2026-10-30
---

# Asynchronous Apex

Asynchronous Apex is the set of mechanisms for running Apex code outside the request that initiated it. The Winter '27 (API 68.0) Apex Developer Guide names four options: Queueable Apex, Scheduled Apex, Batch Apex and future methods.[^s1] Developers reach for them to process large record sets, to call external web services (which triggers cannot do directly), and to keep the user interface responsive by moving slow work into the background. Asynchronous jobs also run with higher governor limits than synchronous code.[^s5]

## How it works

Each option queues work that the platform runs when resources become available, in a separate transaction from the caller.[^s1] If the originating transaction rolls back, the jobs it queued are discarded rather than executed.[^s2][^s4]

- **Queueable Apex.** A class implements the `Queueable` interface and is submitted with `System.enqueueJob`, which returns the ID of the matching AsyncApexJob record. Member variables can be sObjects or custom types, and a running job can enqueue a child job, which forms a chain. A minimum delay of 0 to 10 minutes can be requested, and the `System.Finalizer` interface attaches recovery logic that runs after the job.[^s2]
- **Batch Apex.** A class implements `Database.Batchable` with `start`, `execute` and `finish` methods and is launched with `Database.executeBatch`. Records are handed to `execute` in chunks: 200 by default, or up to 2,000 when `start` returns a `QueryLocator`. Each chunk is its own transaction with fresh limits. Implementing `Database.Stateful` keeps instance variables across chunks.[^s3]
- **Scheduled Apex.** The Apex Scheduler runs a class at a set time or on a recurring schedule. It is typically used for daily or weekly maintenance and is often paired with Batch Apex.[^s1]
- **Future methods.** A `static void` method annotated `@Future` runs later. Parameters are limited to primitives, arrays of primitives and collections of primitives. Adding `callout=true` permits external callouts.[^s4]

## Limits and gotchas (Winter '27)

- A single transaction can enqueue up to 50 Queueable jobs, but an asynchronous transaction such as a batch can enqueue only one. Every job can spawn only one child. Developer and Trial Edition orgs cap a chain at five jobs including the parent, unless overridden with `AsyncOptions`. Enqueuing a second job with the same duplicate signature throws `DuplicateMessageException`.[^s2]
- A `QueryLocator` can return up to 50 million records. Larger results fail the job immediately. Up to 5 batch jobs can be queued or active at once, with 100 more waiting in the Apex flex queue.[^s3] The guide warns that jobs can pile up in the flex queue in busy orgs and delay critical work.[^s1]
- Future methods cannot call other future methods, and batch and future contexts allow zero future calls.[^s4] Passing sObjects is disallowed because the record might change before the method runs. Pass IDs and query fresh data inside the method instead.[^s4]
- All async types draw on one org-wide pool: the greater of 250,000 executions or 200 times the user license count per 24 hours.[^s3][^s4]
- In tests, async work queued between `Test.startTest()` and `Test.stopTest()` runs synchronously when `stopTest()` is called.[^s4]

## When to use which

Salesforce recommends Queueable Apex over future methods. Queueable covers the same use cases and adds job IDs for monitoring, non-primitive parameters and chaining.[^s2] Future methods remain a compact way to isolate DML on setup and non-setup objects to avoid the mixed DML error. They also suit a fire-and-forget callout.[^s4] Batch Apex fits jobs over very large data volumes, or jobs that need more query rows than a normal transaction allows.[^s1] For large volumes, the guide also offers Apex Cursors combined with chained Queueable jobs as a more flexible alternative to Batch Apex.[^s1] Trailhead notes that batch jobs depend on server availability and can take longer than expected, so time-critical work needs another approach.[^s5]

## Connections

Asynchronous Apex is a set of execution modes of **Apex**, its broader node. It has parts **Queueable Apex**, **Batch Apex** and **future methods**, each with its own interface and limits.[^s1] It is **governed by** the platform's **governor limits**: each async transaction gets a separate and usually larger budget, and all async work shares the daily execution allowance.[^s3][^s5] It pairs with **Apex triggers**, since a trigger that needs a callout must defer it to a future or Queueable job.[^s5] Because a queued job only runs after the originating transaction commits, it sits at the end of the save **order of execution**. A rollback cancels it.[^s2]

## Sources

[^s1]: Salesforce Developers, "Apex Developer Guide: Asynchronous Apex" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_async_overview.htm (accessed 2026-10-30)
[^s2]: Salesforce Developers, "Apex Developer Guide: Queueable Apex" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_queueing_jobs.htm (accessed 2026-10-30)
[^s3]: Salesforce Developers, "Apex Developer Guide: Use Batch Apex". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_batch_interface.htm (accessed 2026-10-30)
[^s4]: Salesforce Developers, "Apex Developer Guide: Future Methods" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_invoking_future_methods.htm (accessed 2026-10-30)
[^s5]: Trailhead, "Apex Basics for .NET Developers: Use Asynchronous Apex". https://trailhead.salesforce.com/microsoft_dotnet/apex_basics_dotnet/async_apex (accessed 2026-10-30)
