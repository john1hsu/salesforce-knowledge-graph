---
id: kt:limit-exception
type: Concept
title: LimitException
aliases: [System.LimitException, Apex LimitException, governor limit exception, uncatchable limit exception]
domain: development
summary: >-
  The built-in Apex exception (System.LimitException) that the runtime throws when a transaction exceeds a governor
  limit; unlike most exceptions it cannot be caught, so the transaction stops and its uncommitted work is rolled back.
release: "Winter '27"
status: current
broader: [kt:apex]
related: [kt:limits-class, kt:bulkification, kt:asynchronous-apex, kt:transaction-control, kt:event-monitoring, kt:apex-testing]
relations:
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: consumedBy, object: kt:second-generation-managed-packages}
sources:
  - id: s1
    title: "Apex Reference Guide: Exception Class and Built-In Exceptions"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_classes_exception_methods.htm
    type: official-docs
    accessed: 2026-11-10
  - id: s2
    title: "Apex Developer Guide: Exception Statements"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_exception_statements.htm
    type: official-docs
    accessed: 2026-11-10
  - id: s3
    title: "Apex Developer Guide: Execution Governors and Limits"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_gov_limits.htm
    type: official-docs
    accessed: 2026-11-10
  - id: s4
    title: "Apex Reference Guide: Limits Class"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_methods_system_limits.htm
    type: official-docs
    accessed: 2026-11-10
  - id: s5
    title: "Apex Developer Guide: Exceptions in Apex"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_exception_definition.htm
    type: official-docs
    accessed: 2026-11-10
  - id: s6
    title: "Platform Developer Certification Prep: Get a Refresh on SOQL, SOSL, and DML"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/platform-developer-i-certification-prep-logic-and-process-automation/pd1-2-soql-sosl-dml
    type: official-learning
    accessed: 2026-11-10
created: 2026-11-10
---

# LimitException

`System.LimitException` is the Apex built-in exception that signals a governor limit has been exceeded. The Apex Reference lists it among the roughly forty exception types in the `System` namespace and states plainly that it can't be caught.[^s1] That single property makes it different from almost every other Apex error: a `DmlException` or `NullPointerException` can be trapped and handled, but a `LimitException` always ends the transaction.[^s1][^s2]

## How it works

Every Apex transaction runs under per-transaction governors. When code crosses one of them, the associated governor raises a runtime exception that the code cannot handle.[^s3] The Exception Statements guide groups it with the other uncatchable cases (failed `System.assert` calls and license exceptions) and gives heap size, CPU time, SOQL query count and record retrieval as typical triggers. For these exceptions neither the `catch` block nor any `finally` block runs.[^s2]

Because the exception propagates unhandled, the normal unhandled-exception behavior applies: execution stops, DML performed earlier in the transaction is rolled back, the error is written to the debug log and the user sees an error in the Salesforce UI.[^s5] Salesforce also emails the details to the last modifier of the failing class or trigger and to any addresses configured as Apex exception email recipients. Those emails are deduplicated and throttled to 10 per hour per application server, so Salesforce points to Event Monitoring's Apex Unexpected Exception log files as a more reliable way to track them.[^s5]

## Typical limits that throw it

The thresholds come from the Execution Governors and Limits page (verified for Winter '27, API version 68.0):[^s3]

- SOQL queries: 100 per synchronous transaction and 200 asynchronous; 50,000 records retrieved in either context.[^s3]
- DML: 150 statements and 10,000 rows per transaction in both contexts.[^s3]
- CPU time: 10,000 ms synchronous and 60,000 ms asynchronous; heap size 10 MB and 25 MB respectively.[^s3]
- Callouts: 100 per transaction, with a cumulative callout timeout of 120 seconds.[^s3]

Code that issues one query per loop iteration therefore throws it as soon as a synchronous run needs a 101st query.[^s3]

## Limits and gotchas

- You cannot recover inside the transaction: wrapping a loop in `try/catch (Exception e)` does not help, because the catch block never runs.[^s2]
- Certified managed packages get their own namespace allocations for most limits, while CPU time and heap size are shared across the transaction.[^s3]
- Cross-namespace use is capped at 11 times the per-namespace limit (for example 1,100 SOQL queries in total).[^s3]
- A package without certification counts against the org's own allocation, so installed code can push your logic into a `LimitException`.[^s3]
- Raising the async allowance by moving work to Queueable or Batch Apex buys headroom but does not remove the ceiling.[^s3]

## How to prevent it

Since the exception cannot be handled, the defense is to stay under the limits. The `Limits` class exposes paired methods for every governed resource: `getQueries()` returns queries used so far and `getLimitQueries()` the maximum, and the same pattern covers CPU time, heap and DML statements.[^s4] Code can compare the two before an expensive step and choose to defer work, chunk it, or throw a catchable custom exception with a clear message instead of hitting the hard stop.[^s4] Designing code to query and write whole collections rather than single records keeps consumption flat as volumes grow, and Salesforce's Platform Developer exam-prep material treats exceptions and governor limits as a core topic of Apex logic.[^s6]

## Connections

LimitException is the failure mode of **Governor Limits**, which is why that node `causes` it and this node is `governedBy` it.[^s3] Its parent is **Apex**, whose exception hierarchy it belongs to.[^s1] The **Limits class** is the instrumentation used to avoid it, and **bulkification** and **asynchronous Apex** are the design responses that keep transactions under the thresholds.[^s3][^s4] Because the rollback is total, it interacts with **transaction control** (no catch or finally block runs in which to roll back to a savepoint), and because emails are unreliable, **Event Monitoring** is the recommended way to observe it in production.[^s2][^s5] Packaged code, including **second-generation managed packages**, consumes per-namespace allocations when certified, which shapes how often a subscriber org hits the exception.[^s3] **Apex testing** is where developers should reproduce limit pressure before deployment, a skill the Platform Developer prep material pairs with exception handling.[^s6]

## Sources
[^s1]: Salesforce Developers, "Apex Reference Guide: Exception Class and Built-In Exceptions". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_classes_exception_methods.htm (accessed 2026-11-10)
[^s2]: Salesforce Developers, "Apex Developer Guide: Exception Statements" (Winter '27). https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_exception_statements.htm (accessed 2026-11-10)
[^s3]: Salesforce Developers, "Apex Developer Guide: Execution Governors and Limits". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_gov_limits.htm (accessed 2026-11-10)
[^s4]: Salesforce Developers, "Apex Reference Guide: Limits Class". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_methods_system_limits.htm (accessed 2026-11-10)
[^s5]: Salesforce Developers, "Apex Developer Guide: Exceptions in Apex". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_exception_definition.htm (accessed 2026-11-10)
[^s6]: Trailhead, "Platform Developer Certification Prep: Get a Refresh on SOQL, SOSL, and DML". https://trailhead.salesforce.com/content/learn/modules/platform-developer-i-certification-prep-logic-and-process-automation/pd1-2-soql-sosl-dml (accessed 2026-11-10)
