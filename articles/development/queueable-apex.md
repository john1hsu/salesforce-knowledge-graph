---
id: kt:queueable-apex
type: Feature
title: Queueable Apex
aliases: [Queueable interface, System.enqueueJob, Queueable job, queueables]
domain: development
summary: >-
  An asynchronous Apex mode in which a class implementing the Queueable interface is submitted with System.enqueueJob,
  returning a trackable job ID and supporting complex member state, chaining, delays, duplicate detection and finalizers.
release: "Winter '27"
status: current
broader: [kt:asynchronous-apex]
related: [kt:apex-callouts, kt:apex-testing, kt:apex-triggers]
relations:
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: alternativeTo, object: kt:batch-apex}
  - {predicate: alternativeTo, object: kt:future-methods}
  - {predicate: hasPart, object: kt:transaction-finalizers}
sources:
  - id: s1
    title: "Apex Developer Guide: Queueable Apex"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_queueing_jobs.htm
    type: official-docs
    accessed: 2026-11-04
  - id: s2
    title: "Apex Developer Guide: Transaction Finalizers"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_transaction_finalizers.htm
    type: official-docs
    accessed: 2026-11-04
  - id: s3
    title: "Apex Developer Guide: Detecting Duplicate Queueable Jobs"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_dedupe_queueable.htm
    type: official-docs
    accessed: 2026-11-04
  - id: s4
    title: "Trailhead: Control Processes with Queueable Apex"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/asynchronous_apex/async_apex_queueable
    type: official-learning
    accessed: 2026-11-04
created: 2026-11-04
---

# Queueable Apex

Queueable Apex is the general-purpose way to push Apex work into the background. A developer writes a class that implements the `Queueable` interface and hands an instance to `System.enqueueJob`, which places it on the Apex job queue; the platform runs it in its own thread once resources free up, and the job can draw on asynchronous governor limits such as a larger heap.[^s1] Salesforce's documentation, verified against Winter '27 (API 68.0), explicitly steers developers to Queueables rather than future methods for new work.[^s1] Trailhead describes the interface as essentially a superset of what future methods offer.[^s4]

## How it works

Three properties distinguish a Queueable from a future method. The enqueue call hands back an ID that matches an `AsyncApexJob` record, so code or the Apex Jobs page in Setup can track progress. The class can carry non-primitive state, including sObjects and custom Apex types, which is serialized with the job (fields marked `transient` are skipped and arrive as null). And a running job can start a successor, which is how chains are built.[^s1] If the transaction that enqueued the job rolls back, the job never runs.[^s1]

Callouts need the class to also implement `Database.AllowsCallouts`; this works for chained jobs too.[^s1] An overload of `enqueueJob` takes a minimum delay of 0 to 10 minutes, and admins can set an org-wide default delay of 1 to 600 seconds in Apex Settings that applies whenever no delay is passed. Delays are ignored in tests.[^s1] Another overload takes an `AsyncOptions` object that can cap the chain's stack depth, and `System.AsyncInfo` methods let a running job read its current and maximum depth.[^s1]

**Duplicate detection.** `AsyncOptions` can also carry a `QueueableDuplicateSignature` built from strings, IDs and integers. If a job with the same signature is already waiting in the queue, the enqueue throws `DuplicateMessageException`.[^s3] The signature is dropped as soon as the job is dequeued, so a second copy can still be enqueued while the first is running: the feature guarantees at least one run per signature, not mutual exclusion.[^s3]

**Transaction Finalizers.** Inside `execute`, a job can call `System.attachFinalizer` with a class implementing `System.Finalizer`. The finalizer runs in a separate transaction after the job ends, whether it succeeded or threw an unhandled exception, and its `FinalizerContext` exposes the parent job ID, a request ID, the result and any exception.[^s2] Only one finalizer may be attached per job; after failures it can re-enqueue the job up to five consecutive times, and it may itself enqueue one asynchronous job. Finalizer executions do not count toward the daily async Apex limit, and they allow callouts.[^s2] A common use is buffering log records in finalizer state so they persist even when the job fails.[^s2]

## Limits and gotchas

- A synchronous transaction can enqueue up to 50 jobs; an asynchronous one (for example, a batch `execute`) can enqueue only one. `Limits.getQueueableJobs()` reports the count.[^s1]
- Each job may enqueue only one child. Chain depth is not capped in production orgs, but Developer Edition and Trial orgs stop at five, the parent included, unless overridden with stack depth configuration.[^s1][^s4]
- Each executed job counts once against the org's shared daily async Apex execution allowance. Zero-delay chains can burn through it quickly, so build in a stop condition.[^s1]
- Finalizers may not run if a request is killed unexpectedly, for example during a database shutdown for an upgrade.[^s2]
- In tests, enqueue between `Test.startTest()` and `Test.stopTest()`; the job then runs synchronously at `stopTest`, after which results can be asserted.[^s4]

## When to use it (and when not)

Use a Queueable for most background work: deferring a callout out of a trigger, processing a moderate record set, or sequencing dependent steps through a chain.[^s1][^s4] Batch Apex remains the fit for scanning very large data sets in managed chunks. Future methods still have a niche when the same method must run both synchronously and asynchronously, since a synchronous method can be wrapped in a future one.[^s4]

## Connections

Queueable Apex is a part of **asynchronous Apex**, its broader node, and is **governed by** the asynchronous side of **governor limits**.[^s1] It is an **alternative to** **Batch Apex** for large-volume processing and to **future methods** for simple deferral.[^s1][^s4] It **has part** **Transaction Finalizers**, its built-in recovery hook.[^s2] It relates to **Apex callouts**, which it can make when marked `Database.AllowsCallouts`; to **Apex triggers**, which commonly hand slow work to a Queueable; and to **Apex testing**, whose start/stop pattern forces queued jobs to run.[^s1][^s4]

## Sources

[^s1]: Salesforce Developers, "Apex Developer Guide: Queueable Apex" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_queueing_jobs.htm (accessed 2026-11-04)
[^s2]: Salesforce Developers, "Apex Developer Guide: Transaction Finalizers" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_transaction_finalizers.htm (accessed 2026-11-04)
[^s3]: Salesforce Developers, "Apex Developer Guide: Detecting Duplicate Queueable Jobs" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_dedupe_queueable.htm (accessed 2026-11-04)
[^s4]: Trailhead, "Control Processes with Queueable Apex". https://trailhead.salesforce.com/content/learn/modules/asynchronous_apex/async_apex_queueable (accessed 2026-11-04)
