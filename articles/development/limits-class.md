---
id: kt:limits-class
type: Feature
title: Limits Class
aliases: [System.Limits, Apex Limits class, Limits methods]
domain: development
summary: >-
  The Apex System.Limits class: static methods that report, at runtime, how much of each per-transaction governor
  limit the current transaction has consumed and what its maximum is, so code can adapt before it hits a LimitException.
release: "Winter '27"
status: current
broader: [kt:apex, kt:governor-limits]
related: [kt:limit-exception, kt:bulkification, kt:asynchronous-apex, kt:queueable-apex, kt:apex-testing]
relations:
  - {predicate: mitigates, object: kt:limit-exception}
  - {predicate: contrastsWith, object: kt:orglimits-class}
sources:
  - id: s1
    title: "Apex Reference Guide: Limits Class"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_methods_system_limits.htm
    type: official-docs
    accessed: 2026-11-10
  - id: s2
    title: "Apex Developer Guide: Execution Governors and Limits"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexref/apex_gov_limits.htm
    type: official-docs
    accessed: 2026-11-10
  - id: s3
    title: "Apex Reference Guide: OrgLimits Class"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexcode/apex_class_System_OrgLimits.htm
    type: official-docs
    accessed: 2026-11-10
  - id: s4
    title: "Apex Reference Guide: OrgLimit Class"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexcode/apex_class_System_OrgLimit.htm
    type: official-docs
    accessed: 2026-11-10
created: 2026-11-10
---

# Limits Class

`Limits` is a class in the Apex `System` namespace whose static methods return governor-limit information for the running transaction, such as how many queries have been issued or how much heap is in use.[^s1] Salesforce enforces these governors because Apex runs in a multitenant environment where runaway code must not monopolize shared resources; the `Limits` class is the runtime window onto that enforcement.[^s1] It is the main instrumentation a developer has for avoiding the uncatchable `System.LimitException`.[^s2]

## How it works

Every method is `public static`, takes no arguments and returns an `Integer`. Methods come in pairs: one reports consumption so far and a matching method with `Limit` in its name reports the maximum for the current context.[^s1] For example, `getQueries()` returns the number of SOQL queries issued and `getLimitQueries()` the total allowed; the Execution Governors page uses `getDMLStatements()` and `getLimitDMLStatements()` the same way.[^s1][^s2] Because the `Limit` methods return the ceiling for the current context, the same code sees 100 SOQL queries in a synchronous transaction and 200 in an asynchronous one, and 10 MB versus 25 MB of heap.[^s2]

The resources covered as of Winter '27 include:[^s1]

- SOQL queries, query rows, aggregate queries and `Database.getQueryLocator` rows, plus SOSL queries.[^s1]
- DML statements and DML rows (rows also count `Database.emptyRecycleBin`), CPU time in milliseconds and approximate heap bytes.[^s1]
- Callouts, `sendEmail` invocations, `@future` calls, Queueable jobs enqueued and immediate-publish `EventBus.publish` calls.[^s1]
- Apex cursor and pagination-cursor counters, cursor fetch calls, Data 360 cursors and mobile push Apex calls.[^s1]

## Limits and gotchas

- Several methods are deprecated and now mirror other counters: savepoint, rollback and `runAs` methods return DML statement values, and `findSimilar` methods return SOSL values.[^s1]
- `getChildRelationshipsDescribes()` is deprecated because describe limits are no longer enforced; newer API versions don't expose it.[^s1]
- `getAsyncCalls()` and the Data 360 flex-credit methods are reserved for future use, so they tell you nothing today.[^s1]
- `getFutureCalls()` counts methods executed, not completed, and `getHeapSize()` is approximate, so leave headroom.[^s1]
- Certified managed packages get their own allocation for most limits, but heap, CPU and execution time are shared across the whole transaction.[^s2]
- Cross-namespace totals are capped at 11 times the per-namespace figure, so many certified packages can still exhaust a transaction.[^s2]

## When to use it (and when not)

Use `Limits` to guard expensive steps: compare usage against the maximum before a loop of queries or callouts, then chunk the work, hand the remainder to Queueable Apex, or throw a catchable custom exception with a clear message instead of letting the runtime stop the transaction.[^s1][^s2] It is also useful in tests and debug logs to measure how close a code path runs to each ceiling.[^s1]

It does not report org-wide allowances. For daily API requests, Bulk API usage, streaming limits or asynchronous execution capacity, use `System.OrgLimits.getAll()` or `getMap()`, which return `OrgLimit` objects with `getName()`, `getValue()` and `getLimit()`.[^s3][^s4] Those values update asynchronously in near real time, unlike the per-transaction counters of `Limits`.[^s3][^s4] The Execution Governors page also points to the REST API `limits` resource for that org-level view.[^s2]

## Connections

**Apex** is the parent: `Limits` is a built-in class of the language, and **Governor Limits** is the broader concept whose per-transaction values it exposes, which is why that node is `queriedWith` this one.[^s1][^s2] It `mitigates` **LimitException**: since that exception cannot be caught, checking the counters first is the only in-code defense.[^s2] **Bulkification** keeps the counters flat as data volumes grow, and **asynchronous Apex** such as **Queueable Apex** is where work goes when a check shows the synchronous budget is nearly spent.[^s2] **Apex testing** is where developers assert these counters stay within bounds. The class `contrastsWith` the **OrgLimits class**, which reports org-wide API allowances rather than per-transaction governors.[^s3][^s4]

## Sources
[^s1]: Salesforce Developers, "Apex Reference Guide: Limits Class" (Winter '27). https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_methods_system_limits.htm (accessed 2026-11-10)
[^s2]: Salesforce Developers, "Apex Developer Guide: Execution Governors and Limits" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexref/apex_gov_limits.htm (accessed 2026-11-10)
[^s3]: Salesforce Developers, "Apex Reference Guide: OrgLimits Class". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexcode/apex_class_System_OrgLimits.htm (accessed 2026-11-10)
[^s4]: Salesforce Developers, "Apex Reference Guide: OrgLimit Class". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexcode/apex_class_System_OrgLimit.htm (accessed 2026-11-10)
