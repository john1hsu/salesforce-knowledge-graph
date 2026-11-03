---
id: kt:batch-apex
type: Feature
title: Batch Apex
aliases: [Database.Batchable, batchable Apex, Apex batch job]
domain: development
summary: >-
  An asynchronous Apex mode in which a class implementing Database.Batchable splits a large record set into chunks,
  each processed in its own transaction with fresh governor limits, coordinated by start, execute and finish methods.
release: "Winter '27"
status: current
broader: [kt:asynchronous-apex]
related: [kt:large-data-volumes, kt:apex-managed-sharing, kt:sharing-recalculation, kt:record-locking]
relations:
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: alternativeTo, object: kt:queueable-apex}
  - {predicate: dependsOn, object: kt:apex-flex-queue}
  - {predicate: integratesWith, object: kt:platform-events}
  - {predicate: queriedWith, object: kt:soql}
sources:
  - id: s1
    title: "Apex Developer Guide: Use Batch Apex"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_batch_interface.htm
    type: official-docs
    accessed: 2026-11-03
  - id: s2
    title: "Apex Developer Guide: Firing Platform Events from Batch Apex"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_batch_platformevents.htm
    type: official-docs
    accessed: 2026-11-03
  - id: s3
    title: "Apex Developer Guide: Large Data Processing with Cursors and Queueable Apex Versus Batch Apex"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_cursors_versus_batch.htm
    type: official-docs
    accessed: 2026-11-03
  - id: s4
    title: "Asynchronous Apex: Use Batch Apex"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/asynchronous_apex/async_apex_batch
    type: official-learning
    accessed: 2026-11-03
created: 2026-11-03
---

# Batch Apex

Batch Apex is the asynchronous Apex mode built for jobs too large for one transaction, such as data cleansing, archiving or mass recalculation. A class implements the `Database.Batchable` interface. The platform then feeds it records in chunks, and each chunk runs as a separate transaction with its own reset of governor limits.[^s4] One chunk failing does not roll back chunks that already succeeded.[^s1][^s4]

## How it works

A batch class has three methods, which must be `public` or `global`.[^s1]

- **`start`** runs once and returns the scope of the job: either a `Database.QueryLocator` or an `Iterable`. A QueryLocator is exempt from the SOQL total-rows governor limit and can return up to 50 million records. An Iterable stays subject to that limit but allows custom iteration logic.[^s1][^s4]
- **`execute`** runs once per chunk and receives the `BatchableContext` plus the list of records. Salesforce does not guarantee the order in which chunks run.[^s1]
- **`finish`** runs once after all chunks, typically to send a notification or do post-processing. Since API version 26.0, `finish` can start the next job with `Database.executeBatch` or `System.scheduleBatch`, which chains batch jobs together.[^s1]

`Database.executeBatch` submits the job and returns the ID of an `AsyncApexJob` record, which can be queried for status, progress and error counts, or passed to `System.abortJob`.[^s1] An optional `scope` argument sets the chunk size. The default is 200. With a QueryLocator the maximum is 2,000, and larger values are split into chunks of 2,000. With an Iterable there is no upper bound, though large chunks can hit other limits. `System.scheduleBatch` runs the job after a delay given in minutes and returns a CronTrigger ID instead.[^s1]

By default a batch class is stateless: member variables reset for every chunk. Implementing `Database.Stateful` keeps instance variables across chunks. Static variables still reset.[^s1][^s4] A class that makes HTTP callouts must also implement `Database.AllowsCallouts`.[^s1]

## Limits and gotchas (Winter '27)

- Up to 5 batch jobs can be queued or active at once per org. Up to 100 more can wait in Holding status in the Apex flex queue, and `executeBatch` throws a `LimitException` when that queue is full. Held jobs can be reordered in Setup or with `System.FlexQueue` methods.[^s1]
- Only one `start` method runs at a time in an org, though `execute` methods of different jobs can run in parallel.[^s1]
- Each of `start`, `execute` and `finish` can make up to 100 callouts.[^s1] Batch classes cannot use or call future methods.[^s1]
- `start`, `execute` and `finish` calls all count toward the org's shared daily asynchronous Apex allowance: 250,000 or 200 times the number of user licenses, whichever is greater.[^s1]
- `FOR UPDATE` cannot lock records in the QueryLocator query. To lock rows, requery them with `FOR UPDATE` inside `execute`.[^s1] Avoid relationship subqueries in the QueryLocator, because they force a slower non-chunked implementation. Run them inside `execute` instead.[^s1]
- During maintenance, running jobs roll back and restart, so `execute` can run more than once. Make non-transactional work such as callouts idempotent.[^s1]
- Calling a batch from a trigger needs care: a bulk data load can fire the trigger often enough to exceed the job limits.[^s1][^s4]
- A test method can exercise only one run of `execute`. Keep test data within one chunk and call `executeBatch` between `Test.startTest()` and `Test.stopTest()`, where the job runs synchronously.[^s1][^s4]

## Error handling

A batch class that also implements `Database.RaisesPlatformEvents` publishes a `BatchApexErrorEvent` (API 44.0 and later) when `start`, `execute` or `finish` hits an unhandled exception. This includes uncatchable limit exceptions and internal platform errors.[^s2] The event carries the job ID, the IDs of the records in the failed scope, and the exception type, message and stack trace. A trigger subscribed to the event can therefore log the failure or retry it. In tests, deliver the event with `Test.getEventBus().deliver()` after `Test.stopTest()`.[^s2]

## When to use it (and when not)

Trailhead advises using Batch Apex only when the work spans more than one chunk of records. For smaller volumes Queueable Apex is usually the better fit.[^s4] Batch Apex gives a fixed, sequential model with a set chunk size and error isolation per chunk. However, it competes for the five active slots and the flex queue, so a busy org can see critical jobs delayed.[^s3] For that situation the Winter '27 guide offers an alternative: an Apex cursor walks a result set of up to 50 million rows from chained Queueable jobs. This approach uses no batch slots, lets the developer control fetch size, and isolates errors per transaction through a Transaction Finalizer.[^s3] Both a cursor and a QueryLocator fix the set of record IDs when they are created.[^s3]

## Connections

Batch Apex is one mode of **Asynchronous Apex**, its broader node.[^s4] It is **governed by** the platform's **governor limits**: each chunk gets fresh limits, while the daily async allowance is shared.[^s1] It **depends on** the **Apex flex queue**, where jobs wait in Holding status for one of the five active slots.[^s1] It is an **alternative to** **Queueable Apex**, especially when Queueable is combined with cursors.[^s3] It **integrates with** **Platform Events** through `BatchApexErrorEvent`.[^s2] Its scope is usually a **SOQL** QueryLocator.[^s1] It is the standard tool for **large data volumes**, and for the **Apex managed sharing** and **sharing recalculation** work where the guide recommends deleting and re-creating share rows in `execute`.[^s1] It relates to **record locking** because rows are locked by requerying them with `FOR UPDATE` inside `execute`.[^s1]

## Sources

[^s1]: Salesforce Developers, "Apex Developer Guide: Use Batch Apex". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_batch_interface.htm (accessed 2026-11-03)
[^s2]: Salesforce Developers, "Apex Developer Guide: Firing Platform Events from Batch Apex" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_batch_platformevents.htm (accessed 2026-11-03)
[^s3]: Salesforce Developers, "Apex Developer Guide: Large Data Processing with Cursors and Queueable Apex Versus Batch Apex" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_cursors_versus_batch.htm (accessed 2026-11-03)
[^s4]: Trailhead, "Asynchronous Apex: Use Batch Apex". https://trailhead.salesforce.com/content/learn/modules/asynchronous_apex/async_apex_batch (accessed 2026-11-03)
