---
id: kt:future-methods
type: Feature
title: Future Methods
aliases: ["@future annotation", "@Future methods", "future calls", "Apex future methods"]
domain: development
summary: >-
  Static, void Apex methods annotated with @Future that the platform queues and runs asynchronously in their own
  transaction, used for callouts from triggers and for separating setup and non-setup DML; Salesforce now recommends
  Queueable Apex for new work.
release: "Winter '27"
status: current
broader: [kt:asynchronous-apex]
related: [kt:apex-callouts, kt:apex-triggers, kt:apex-testing, kt:batch-apex]
relations:
  - {predicate: alternativeTo, object: kt:queueable-apex}
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: mitigates, object: kt:mixed-dml-error}
  - {predicate: causes, object: kt:record-locking}
sources:
  - id: s1
    title: "Apex Developer Guide: Future Methods"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_invoking_future_methods.htm
    type: official-docs
    accessed: 2026-11-07
  - id: s2
    title: "Trailhead: Use Future Methods (Asynchronous Apex module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/content/learn/modules/asynchronous_apex/async_apex_future_methods
    type: official-learning
    accessed: 2026-11-07
  - id: s3
    title: "Apex Developer Guide: sObjects That Can't Be Used Together in DML Operations"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_dml_non_mix_sobjects.htm
    type: official-docs
    accessed: 2026-11-07
created: 2026-11-07
---

# Future Methods

A future method is the oldest and simplest form of asynchronous Apex. Adding the `@Future` annotation to a method tells the platform to queue the call and run it later, in its own thread, when resources are available, so the calling code carries on without waiting.[^s1] Typical jobs are callouts to external web services and other long-running work, plus a narrower use: splitting DML on setup and non-setup objects so the transaction avoids the mixed DML error.[^s1][^s2] Some governor limits, such as SOQL query and heap size limits, are higher in the asynchronous context.[^s1] The Winter '27 (API 68.0) Apex Developer Guide still documents the feature as current, but it recommends Queueable Apex instead, because Queueables cover the same cases and add job IDs, non-primitive parameters and chaining.[^s1]

## How it works

The method must be `static` and return `void`. Its parameters are limited to primitive types, arrays of primitives, or collections of primitives; sObjects and other objects cannot be passed.[^s1] The reason is timing: the record could change between the call and the execution, so the method would work with stale data. The usual pattern is to pass a list of record IDs and query the records fresh inside the method.[^s1][^s2] To make an HTTP or web service callout, the annotation must read `@Future(callout=true)`.[^s1] A future method is invoked like any other method, but nothing is returned to the caller and there is no job ID to track.[^s1]

If the transaction that queued the call rolls back, the future job is never processed. Jobs waiting during a maintenance window stay queued and run afterwards; a job that is mid-execution when downtime starts is rolled back and restarted.[^s1]

**Mixed DML.** Setup objects such as User, UserRole, Group, GroupMember and PermissionSetAssignment affect record access, so DML on them cannot share a transaction with DML on ordinary objects like Account.[^s3] The documented workaround is to do the first DML in the current method and hand the setup-object DML to an `@future` method, which runs in a separate transaction.[^s3] In tests, enclosing the DML in `System.runAs` blocks is the alternative.[^s3]

## Limits and gotchas

- A single Apex invocation can make up to 50 future calls; batch and future contexts can make none, so a future method cannot call another future method.[^s1][^s2] `System.isFuture()` lets code detect that it is already running in a future context and skip the call.[^s2]
- Future executions draw on the org's shared 24-hour async Apex allowance, which is 250,000 or 200 times the number of user licenses, whichever is greater, and which Batch, Queueable and scheduled Apex also consume.[^s1]
- Execution order is not guaranteed and two future methods can run at the same time, which can produce record locking errors when they touch the same records.[^s2]
- When more than 2,000 unprocessed requests from one org are queued, further requests from that org are delayed while other orgs are served.[^s1]
- Future methods cannot be used in Visualforce getters, setters or constructors, and `getContent()` and `getContentAsPDF()` are unavailable inside them.[^s2]
- Fanning out multiple future methods from a Queueable job is discouraged.[^s1]

## Testing

Place the call between `Test.startTest()` and `Test.stopTest()`: asynchronous calls collected after `startTest` run synchronously when `stopTest` executes, after which results can be asserted.[^s1][^s2] Tests cannot send real callouts, so a class implementing `HttpCalloutMock` is registered with `Test.setMock`.[^s2] Trailhead also advises testing at scale, for example with a trigger handling 200 records, and bundling several callouts into one future method rather than one call per callout.[^s2]

## When to use it (and when not)

For new code, prefer a Queueable: it returns a trackable ID, accepts sObjects and custom types, and can chain.[^s1][^s2] A future method still fits when a trigger needs a quick, fire-and-forget callout, when a method should be callable both synchronously and asynchronously through a thin future wrapper, or for mixed DML separation.[^s2][^s3] For processing large record volumes, Batch Apex is more efficient than queuing one future request per record.[^s1][^s2]

## Connections

Future methods are part of **asynchronous Apex**, their broader node, and are **governed by** the asynchronous **governor limits**, including the shared daily execution allowance.[^s1] They are an **alternative to** **Queueable Apex**, which Salesforce recommends in their place.[^s1] They **mitigate** the **mixed DML error** by moving setup-object DML into a separate transaction.[^s3] Because order and concurrency are not guaranteed, they can **cause** **record locking** contention.[^s2] They relate to **Apex callouts** (via `callout=true`), to **Apex triggers**, where callouts are not allowed synchronously, to **Apex testing**, whose start/stop pattern forces them to run, and to **Batch Apex**, the better tool for volume.[^s1][^s2]

## Sources

[^s1]: Salesforce Developers, "Apex Developer Guide: Future Methods" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_invoking_future_methods.htm (accessed 2026-11-07)
[^s2]: Trailhead, "Use Future Methods" (Asynchronous Apex module). https://trailhead.salesforce.com/en/content/learn/modules/asynchronous_apex/async_apex_future_methods (accessed 2026-11-07)
[^s3]: Salesforce Developers, "Apex Developer Guide: sObjects That Can't Be Used Together in DML Operations" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_dml_non_mix_sobjects.htm (accessed 2026-11-07)
