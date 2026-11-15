---
id: kt:apex-flex-queue
type: Feature
title: Apex Flex Queue
aliases: [flex queue, System.FlexQueue, FlexQueue class, Holding status batch jobs]
domain: development
summary: >-
  The org-wide holding area where submitted Batch Apex jobs wait in Holding status, up to 100 at a time, until one of the
  five active batch slots frees up; jobs can be reordered from Setup or with the System.FlexQueue methods.
release: "Winter '27"
status: current
broader: [kt:asynchronous-apex]
related: [kt:scheduled-apex, kt:apex-testing, kt:queueable-apex]
relations:
  - {predicate: consumedBy, object: kt:batch-apex}
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: causes, object: kt:limit-exception}
sources:
  - id: s1
    title: "Apex Reference Guide: FlexQueue Class"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_class_System_FlexQueue.htm
    type: official-docs
    accessed: 2026-11-15
  - id: s2
    title: "Apex Developer Guide: Use Batch Apex"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_batch_interface.htm
    type: official-docs
    accessed: 2026-11-15
  - id: s3
    title: "Trailhead: Monitor Asynchronous Apex"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/asynchronous_apex/async_apex_monitoring
    type: official-learning
    accessed: 2026-11-15
  - id: s4
    title: "Apex Reference Guide: Test Class"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexcode/apex_methods_system_test.htm
    type: official-docs
    accessed: 2026-11-15
created: 2026-11-15
---

# Apex Flex Queue

The Apex flex queue is the waiting room for Batch Apex. When code calls `Database.executeBatch`, the job does not go straight to execution: it lands in the flex queue with the status **Holding** and stays there until the org has capacity to run it.[^s2] The queue holds up to 100 batch jobs, and an org processes at most five queued or active batch jobs at once.[^s1] Because jobs wait in a queue that administrators and code can see, the order in which held jobs run can be changed before they start.[^s2]

## How it works

Jobs leave the flex queue first in, first out by default. When system resources free up, the job at the top moves to the batch job queue and its status changes from Holding to **Queued**; queued jobs then run when the system is ready.[^s1] The full lifecycle visible on `AsyncApexJob` runs Holding, Queued, Preparing (the `start` method is running), Processing, and finally Completed, Failed or Aborted.[^s2] Only one batch job's `start` method can run at a time in an org, which adds a further serial step even inside the five active slots.[^s2]

Batch jobs scheduled with `System.scheduleBatch` also pass through the queue: when the scheduled time arrives, the job is appended to the end of the flex queue. Scheduled Apex limits apply until that moment, and batch limits apply afterwards.[^s2] Trailhead notes that future methods are not part of the flex queue, so it is a Batch Apex mechanism rather than a general async queue.[^s3]

## Reordering and monitoring

Administrators reorder held jobs on the **Apex Flex Queue** page in Setup, where they can move an important job to the front or push a less important one to the back.[^s3] The broader **Apex Jobs** page and a SOQL query on `AsyncApexJob` (for example its `Status` and `NumberOfErrors`) are the way to follow a job once it is running.[^s3]

In code, the `System.FlexQueue` class offers four static methods, each returning a Boolean that is `false` when the job is already in the requested position:[^s1]

- `moveBeforeJob` and `moveAfterJob` place one job directly before or after another job in the queue.[^s1]
- `moveJobToFront` puts a job at index 0, and `moveJobToEnd` puts it at the last position.[^s1]

The methods act only on jobs in Holding status, and they throw an element-not-found exception when the job is not in the queue. Salesforce recommends calling a reorder method as the last statement in a transaction.[^s1]

## Limits and gotchas

When the queue already holds 100 jobs, `executeBatch` throws a `LimitException` and the job is not added.[^s2] Parallel submissions can briefly push the count past 100, after which further submissions keep failing until the queue drops below the maximum again.[^s2] Code that enqueues batches from triggers or loops should therefore check capacity, or fall back gracefully, rather than assume a slot. If the flex queue is disabled, `executeBatch` sends the job directly to the batch queue as Queued and throws a `LimitException` once the queued-or-active limit is reached.[^s2]

Tests run against a separate, test-context queue. A running test can submit at most five batch jobs.[^s2] `Test.enqueueBatchJobs(n)` fills that context with no-operation jobs: the first five go to the batch queue and the rest to the test flex queue, which throws a limit exception past 100 jobs.[^s4] `Test.getFlexQueueOrder()` returns the IDs of held jobs in run order, index 0 being next, and only ever sees test-context jobs, even with `SeeAllData=true`.[^s4] Together these let a developer unit-test reordering logic and the queue-full path without touching real org jobs.[^s4]

## When to use it (and when not)

Reordering is useful when a busy org has many held batches and a time-sensitive job must jump the line; `moveJobToFront` exists for exactly that case.[^s1] It does not add capacity: reordering only changes which held job takes the next free slot, and the limit of five queued or active jobs stays the bottleneck.[^s1] For small or time-critical background work, Queueable Apex is the usual alternative: it is submitted with `System.enqueueJob` and tracked by its own job ID on the Apex Jobs page.[^s3]

## Connections

The flex queue is a part of **Asynchronous Apex**, its broader node, and is **consumed by** **Batch Apex**, which depends on it for every submitted job.[^s2] It is **governed by** the platform's **governor limits** and **causes** a **LimitException** when it is full.[^s2] It relates to **Scheduled Apex** because `System.scheduleBatch` places due jobs at its tail.[^s2] It relates to **Apex Testing** through the test-only `enqueueBatchJobs` and `getFlexQueueOrder` methods.[^s4] It relates to **Queueable Apex** as the lighter async mode that is tracked separately by its own job ID.[^s3]

## Sources
[^s1]: Salesforce Developers, "Apex Reference Guide: FlexQueue Class". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_class_System_FlexQueue.htm (accessed 2026-11-15)
[^s2]: Salesforce Developers, "Apex Developer Guide: Use Batch Apex". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_batch_interface.htm (accessed 2026-11-15)
[^s3]: Trailhead, "Monitor Asynchronous Apex". https://trailhead.salesforce.com/content/learn/modules/asynchronous_apex/async_apex_monitoring (accessed 2026-11-15)
[^s4]: Salesforce Developers, "Apex Reference Guide: Test Class". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexcode/apex_methods_system_test.htm (accessed 2026-11-15)
