---
id: kt:transaction-finalizers
type: Feature
title: Transaction Finalizers
aliases: [System.Finalizer, Finalizer interface, System.attachFinalizer, FinalizerContext, Queueable finalizer]
domain: development
summary: >-
  An Apex feature that attaches a class implementing System.Finalizer to a Queueable job so that post-execution
  logic, such as logging, notification or retry, runs in its own transaction after the job succeeds or fails.
release: "Winter '27"
status: current
broader: [kt:queueable-apex, kt:asynchronous-apex]
related: [kt:apex-callouts, kt:apex-user-mode, kt:transaction-control, kt:event-monitoring]
relations:
  - {predicate: partOf, object: kt:queueable-apex}
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: alternativeTo, object: kt:batch-apex-error-event}
sources:
  - id: s1
    title: "Apex Developer Guide: Transaction Finalizers"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_transaction_finalizers.htm
    type: official-docs
    accessed: 2026-11-16
  - id: s2
    title: "Apex Reference Guide: FinalizerContext Interface"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_interface_System_FinalizerContext.htm
    type: official-docs
    accessed: 2026-11-16
  - id: s3
    title: "Learn MOAR in Spring '20: Introducing Transaction Finalizers"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2020/01/learn-moar-in-spring-20-introducing-transaction-finalizers
    type: official-blog
    accessed: 2026-11-16
created: 2026-11-16
---

# Transaction Finalizers

**Transaction Finalizers** let a developer attach post-execution logic to a **Queueable Apex** job. The logic lives in a class that implements the `System.Finalizer` interface, and the Queueable registers it by calling `System.attachFinalizer` from inside its `execute` method. Their main purpose is recovery: deciding what to do when a Queueable job fails. They can equally run follow-up work when the job succeeds.[^s1] The feature first appeared as a pilot in Spring '20, presented as a way to add flow control on top of Queueables.[^s3] The Winter '27 (API 68.0) Apex Developer Guide documents it as a standard part of Queueable Apex.[^s1]

## How it works

A finalizer class has one required method, `execute(System.FinalizerContext ctx)`. The runtime injects the context object; developers never construct it.[^s1][^s2] The context exposes four methods:[^s2]

- `getResult()` returns a `System.ParentJobResult` value, either `SUCCESS` or `UNHANDLED_EXCEPTION`.[^s2]
- `getException()` returns the exception that failed the job when the result is `UNHANDLED_EXCEPTION`, and null otherwise.[^s2]
- `getAsyncApexJobId()` returns the parent Queueable's job ID, the right key for joining to the AsyncApexJob table.[^s2]
- `getRequestId()` returns a request ID, shared by the Queueable and its finalizer, for matching Event Monitoring logs.[^s2]

The Queueable and its finalizer run in **separate Apex and database transactions**. A common split is DML in the Queueable and a REST callout in the finalizer; callouts are allowed in finalizers.[^s1][^s3] Because the finalizer runs even after an unhandled exception, it can persist information that the failed job's rolled-back transaction would otherwise have lost.[^s1]

State is captured at the end of the Queueable's execution, not at the moment of attachment, so the job can keep updating the finalizer instance after calling `attachFinalizer`. Fields marked `transient` are not serialized and do not reach the finalizer. A finalizer can be an inner class, and one class can implement both `Queueable` and `Finalizer`.[^s1]

## Limits and gotchas

Verified against the Winter '27 Apex Developer Guide:[^s1]

- Only **one** finalizer instance can be attached to a given Queueable job.[^s1][^s3]
- A finalizer can enqueue **one** asynchronous job (Queueable, future or Batch) from its `execute` method.[^s1]
- A Queueable that fails with an unhandled exception can be re-enqueued by its finalizer up to **five consecutive times**; the counter resets once the job completes without an unhandled exception.[^s1]
- Running the finalizer does not count as an extra execution against the daily asynchronous Apex limit.[^s1]
- Synchronous governor limits apply inside a finalizer, except total heap size, `System.enqueueJob` jobs and `@future` calls per invocation, which follow asynchronous limits.[^s1]
- If a request is killed unexpectedly, for example during a database shutdown for a system upgrade, the finalizer may not run.[^s1]
- ISVs should be cautious with `global` finalizers that call state-changing package methods, because subscriber orgs can invoke them.[^s1]

## When to use it (and when not)

Before finalizers, detecting a failed Queueable meant polling AsyncApexJob with SOQL, while the `BatchApexErrorEvent` platform event covered only Batch Apex failures.[^s1] Finalizers make failure handling part of the job itself. The documented patterns are a **logging finalizer** that buffers messages during the job and inserts them in user mode whatever the outcome, and a **retry finalizer** that checks `getResult()` and re-enqueues the job until the five-retry chain limit is reached.[^s1] Other uses include alerting a team after a DML error, starting the next stage of an async chain, or syncing an external system after success.[^s3]

Finalizers are tied to Queueables, so work built on Batch Apex or future methods needs a different error-handling route. A finalizer is also not a guarantee: because it can be skipped on abnormal termination, critical reconciliation should not depend on it alone.[^s1]

## Connections

Transaction Finalizers are **part of** and narrower than **Queueable Apex**, and sit under **asynchronous Apex** more broadly.[^s1] They are **governed by** **governor limits**, using a mix of synchronous and asynchronous allocations.[^s1] They relate to **Event Monitoring**, whose logs can be matched via `getRequestId()`.[^s2] They are an **alternative to** the **BatchApexErrorEvent** approach to async failure handling.[^s1] Related nodes are **Apex callouts**, which finalizers may make; **Apex user mode**, used in the logging example; and **transaction control**, since the finalizer's own transaction is separate from the job's.[^s1][^s3]

## Sources

[^s1]: Salesforce Developers, "Apex Developer Guide: Transaction Finalizers" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_transaction_finalizers.htm (accessed 2026-11-16)
[^s2]: Salesforce Developers, "Apex Reference Guide: FinalizerContext Interface". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_interface_System_FinalizerContext.htm (accessed 2026-11-16)
[^s3]: Kevin Poorman, Salesforce Developers Blog, "Learn MOAR in Spring '20: Introducing Transaction Finalizers" (2020-01-29). https://developer.salesforce.com/blogs/2020/01/learn-moar-in-spring-20-introducing-transaction-finalizers (accessed 2026-11-16)
