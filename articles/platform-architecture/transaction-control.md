---
id: kt:transaction-control
type: Concept
title: Transaction Control
aliases: [Apex transaction control, Apex transactions, savepoints and rollback, Database.setSavepoint, Database.rollback, execution context transaction]
domain: platform-architecture
summary: >-
  How the Salesforce Platform groups the work of one request into a single all-or-none database transaction, and the
  Apex savepoint, rollback and partial-success tools developers use to control what commits.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform, kt:apex]
related: [kt:record-locking, kt:order-of-execution, kt:flow-fault-handling, kt:apex-triggers, kt:apex-callouts, kt:apex-testing]
relations:
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: coveredBy, object: kt:platform-developer-certification}
sources:
  - id: s1
    title: "Transaction Control (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/langCon_apex_transaction_control.htm
    type: official-docs
    accessed: 2026-11-05
  - id: s2
    title: "Apex Transactions (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_transaction.htm
    type: official-docs
    accessed: 2026-11-05
  - id: s3
    title: "DML Statements vs. Database Class Methods (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/langCon_apex_dml_database.htm
    type: official-docs
    accessed: 2026-11-05
  - id: s4
    title: "Execution Governors and Limits (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_gov_limits.htm
    type: official-docs
    accessed: 2026-11-05
created: 2026-11-05
---

# Transaction Control

On the Salesforce Platform, every request runs as one database transaction: a set of operations treated as a single unit, which the Apex Developer Guide also calls an execution context.[^s2] A transaction begins at its boundary — a trigger, a class method, an anonymous block, a Visualforce page or a custom web service method — and everything that code calls, including other classes and the triggers its DML fires, joins the same transaction.[^s2] Transaction control is the set of rules and Apex tools that decide what is committed when that unit ends. This article was checked against the Winter '27 edition of the guide (API version 68.0).[^s1][^s2]

## How it works

The default is all-or-none. Changes are committed only when the whole request completes successfully; if any DML operation fails and the error is not handled, the platform rolls back every database change made in the transaction.[^s1][^s2] The guide's example is an order that inserts an invoice and a line item, then updates inventory: when the inventory update violates a validation rule, the earlier inserts are undone as well, so no orphaned records remain.[^s2] Payment transactions are the documented exception, because the gateway has already processed the money.[^s2]

Inside a transaction, Apex can set intermediate restore points. `Database.setSavepoint()` captures the current database state, and `Database.rollback(sp)` discards DML performed after that savepoint and releases the table and row locks acquired since it was set.[^s1] Savepoints can be layered, but rolling back to an earlier one invalidates any later savepoint variables, and using one afterwards is a runtime error.[^s1]

A second, record-level form of control is the `allOrNone` flag on Database class methods such as `Database.insert`. It defaults to `true`, so a failing record aborts the operation with an exception; set to `false`, valid records are saved and failures are returned as `Database.SaveResult` objects whose `getErrors()` describe each problem.[^s3] Plain DML statements always throw, and savepoints and rollback exist only as Database class methods.[^s3]

## Limits and gotchas

- **Governor limits are per transaction.** The DML statement limit is 150 and the DML row limit is 10,000 for both synchronous and asynchronous Apex; Batch Apex resets the counters on each `execute` call.[^s4] Each savepoint, and each `Database.rollback`, counts against the DML statement limit but not the DML row limit in current API versions; before API 60.0 they also consumed DML rows.[^s1]
- **Static variables survive rollback.** Rolling back does not restore static values, so a recursion guard or cached state set before the savepoint keeps its value.[^s1]
- **IDs survive rollback too.** A record inserted after a savepoint keeps its ID in memory once rolled back, and reusing that variable for insert, update or upsert fails; create a fresh sObject instead.[^s1]
- **No savepoints across trigger invocations.** Each trigger invocation is a new context, so a static savepoint carried between them causes a runtime error.[^s1]
- **Callouts need released savepoints.** A callout made while a savepoint is active throws a `CalloutException`; roll back pending DML, then call `Database.releaseSavepoint(sp)`. Releasing does not roll back pending work, and releasing one savepoint also releases those created after it.[^s1] From API 60.0, `Test.startTest()` and `Test.stopTest()` release all savepoints in tests.[^s1]

## When to use it (and when not)

Rely on the default all-or-none behaviour for business operations whose parts only make sense together, such as the debit and credit of a transfer.[^s2] Use a savepoint when one step is optional and its failure should not sink the rest — for example, attempting an enrichment insert and rolling it back while keeping the primary record — remembering the extra DML statement each savepoint costs.[^s1][^s4] Use `allOrNone=false` for bulk imports and integrations where some bad records are expected and should be reported or retried rather than blocking the batch.[^s3] Avoid catching exceptions just to swallow them: the automatic rollback happens only when the request fails, so a handled error lets earlier work commit.[^s1][^s2]

## Connections

Transaction control is a core behaviour of `kt:salesforce-platform`, exposed to developers through `kt:apex` and the Database class.[^s1][^s3] Its limits are part of `kt:governor-limits`, which are counted per transaction.[^s4] `kt:record-locking` is closely tied to it, because a rollback to a savepoint releases the table and row locks taken after it.[^s1] The transaction boundary wraps the save `kt:order-of-execution` and every `kt:apex-triggers` invocation it fires, which is why savepoints cannot span trigger contexts.[^s1][^s2] `kt:apex-callouts` must respect the savepoint-release rules, and `kt:apex-testing` savepoint behaviour changed with API 60.0.[^s1] In this graph, `kt:flow-fault-handling` covers the declarative counterpart (fault paths and Roll Back Records), and the edge to `kt:platform-developer-certification` marks transaction handling as developer-exam material.

## Sources

[^s1]: Salesforce Developers, "Transaction Control (Apex Developer Guide)", Winter '27. https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/langCon_apex_transaction_control.htm (accessed 2026-11-05)
[^s2]: Salesforce Developers, "Apex Transactions (Apex Developer Guide)", Winter '27. https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_transaction.htm (accessed 2026-11-05)
[^s3]: Salesforce Developers, "DML Statements vs. Database Class Methods (Apex Developer Guide)", Winter '27. https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/langCon_apex_dml_database.htm (accessed 2026-11-05)
[^s4]: Salesforce Developers, "Execution Governors and Limits (Apex Developer Guide)", Winter '27. https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_gov_limits.htm (accessed 2026-11-05)
