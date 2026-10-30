---
id: kt:governor-limits
type: Limit
title: Governor Limits
aliases: [Apex governor limits, execution governors and limits, per-transaction limits]
domain: platform-architecture
summary: >-
  Runtime limits that the Salesforce platform enforces on every Apex and flow transaction (queries, DML, CPU time,
  heap, callouts and more) so that one tenant's code cannot monopolize shared multitenant resources.
release: "Winter '27"
status: current
broader: [kt:multitenancy]
related: [kt:apex-triggers, kt:flow-builder, kt:asynchronous-apex, kt:order-of-execution]
relations:
  - {predicate: queriedWith, object: kt:limits-class}
  - {predicate: causes, object: kt:limit-exception}
sources:
  - id: s1
    title: "Apex Developer Guide: Execution Governors and Limits"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexref/apex_gov_limits.htm
    type: official-docs
    accessed: 2026-10-30
  - id: s2
    title: "Apex Reference Guide: Limits Class"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_methods_system_limits.htm
    type: official-docs
    accessed: 2026-10-30
  - id: s3
    title: "Per-Transaction Flow Limits"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=platform.flow_considerations_limit_transaction.htm
    type: official-docs
    accessed: 2026-10-30
  - id: s4
    title: "Apex Triggers: Bulk Apex Triggers"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/apex_triggers/apex_triggers_bulk
    type: official-learning
    accessed: 2026-10-30
  - id: s5
    title: "Apex Basics for .NET Developers: Understand Execution Context"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/apex_basics_dotnet/execution_context
    type: official-learning
    accessed: 2026-10-30
created: 2026-10-30
---

# Governor Limits

Governor limits are hard caps the Apex runtime places on the resources a single transaction may consume. Because Apex runs in a multitenant environment, the runtime enforces them so that runaway code or processes cannot monopolize capacity shared with other customers.[^s1] When code exceeds a limit, the governor throws a runtime exception that code cannot handle, so the transaction fails rather than degrading gracefully.[^s1] Trailhead describes the limits as vital to stopping any one org from consuming too many resources on shared infrastructure.[^s5]

## How it works

Limits are counted per **execution context**: everything from the moment code starts until it finishes. Apex often runs alongside other logic on the same record, such as before and after triggers and other automation, and all of that code shares one set of governor limits.[^s5] Flows are counted the same way. An autolaunched flow runs inside the transaction that launched it and shares its limits. A screen flow starts a new transaction each time the user clicks Next, and a flow paused by a Wait element resumes in a new batch transaction.[^s3]

Code can check its consumption at runtime with the **Limits** class. Every resource has a pair of static methods: `getX` returns the amount used so far and `getLimitX` returns the total allowed. Examples are `getQueries`/`getLimitQueries` and `getCpuTime`/`getLimitCpuTime`.[^s2]

## Key per-transaction limits (Winter '27)

The Winter '27 (API 68.0) Apex Developer Guide lists these values, synchronous / asynchronous:[^s1]

- SOQL queries: 100 / 200; records retrieved by SOQL: 50,000.
- DML statements: 150; rows processed by DML: 10,000.
- CPU time: 10,000 ms / 60,000 ms; heap size: 10 MB / 25 MB.
- Callouts: 100, with a cumulative callout timeout of 120 seconds.
- SOSL queries: 20; `sendEmail` calls: 10; trigger recursion stack depth: 16.
- Jobs queued with `System.enqueueJob`: 50 / 1; `future` calls: 50 synchronously, 0 in batch and future contexts.
- Maximum execution time per transaction: 10 minutes.[^s1]

In Batch Apex the limits reset for each `execute` batch, and each test method gets its own allocation.[^s1] Beyond per-transaction caps, the org-wide `DailyAsyncApexExecutions` limit allows the greater of 250,000 or 200 times the number of applicable user licenses in 24 hours, shared by batch, queueable, scheduled and future Apex.[^s1]

## Managed packages and namespaces

Certified managed packages that passed AppExchange security review get their own allocation for most per-transaction limits, separate from the org's own code. Cumulative cross-namespace limits are 11 times the per-namespace value, for example 1,100 SOQL queries. Heap size, CPU time, execution time and the number of unique namespaces are shared across the whole transaction, and non-certified packages draw on the org's limits.[^s1]

## Limits and gotchas

The classic failure is code that works for one record but breaks in bulk. Triggers receive up to 200 records at a time, so a query or DML statement inside a loop multiplies with the batch size and can blow through the 100-query or 150-statement caps.[^s5] Trailhead's remedy is bulkification: query once outside the loop using an `IN` filter on `Trigger.new`, collect changed records in a list, and issue one DML statement after the loop.[^s4]

Flows are not exempt. Every Get Records execution counts as a SOQL query, Create, Update and Delete Records count as DML, and a fault connector does not save the transaction: exceeding a limit rolls back the whole transaction.[^s3]

## Connections

Governor limits are a direct consequence of **multitenancy**, their broader concept.[^s1] They shape how **Apex triggers** must be written (bulkified, no SOQL or DML in loops)[^s4] and they apply equally to automation built in **Flow Builder**.[^s3] Moving work into **asynchronous Apex** raises several caps, such as SOQL, CPU and heap, but draws on the daily async execution allowance.[^s1] Because all code in an execution context shares one budget, limits are tied to the platform's **order of execution**.[^s5] Usage is read through the **Limits class**[^s2], and an overrun **causes** an uncatchable **limit exception**.[^s1]

## Sources

[^s1]: Salesforce Developers, "Apex Developer Guide: Execution Governors and Limits" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexref/apex_gov_limits.htm (accessed 2026-10-30)
[^s2]: Salesforce Developers, "Apex Reference Guide: Limits Class". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_methods_system_limits.htm (accessed 2026-10-30)
[^s3]: Salesforce Help, "Per-Transaction Flow Limits". https://help.salesforce.com/apex/HTViewHelpDoc?id=platform.flow_considerations_limit_transaction.htm (accessed 2026-10-30)
[^s4]: Trailhead, "Apex Triggers: Bulk Apex Triggers". https://trailhead.salesforce.com/content/learn/modules/apex_triggers/apex_triggers_bulk (accessed 2026-10-30)
[^s5]: Trailhead, "Apex Basics for .NET Developers: Understand Execution Context". https://trailhead.salesforce.com/en/apex_basics_dotnet/execution_context (accessed 2026-10-30)
