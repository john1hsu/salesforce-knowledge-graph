---
id: kt:static-soql
type: Feature
title: Static SOQL
aliases: [inline SOQL, Apex inline query, square-bracket SOQL, static SOQL query]
domain: development
summary: >-
  A SOQL query written directly in Apex code between square brackets, evaluated in place and returning a list of
  sObjects, a single sObject or an Integer count, with values supplied through colon-prefixed bind variables; the
  default alternative to building query strings with dynamic SOQL.
release: "Winter '27"
status: current
broader: [kt:soql, kt:apex]
related: [kt:dynamic-soql, kt:apex-user-mode, kt:bulkification, kt:sosl]
relations:
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: alternativeTo, object: kt:dynamic-soql}
  - {predicate: coveredBy, object: kt:platform-developer-certification}
sources:
  - id: s1
    title: "Apex Developer Guide: SOQL and SOSL Queries"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/apex-dev/references/apex-dev/langcon-apex-soql.html
    type: official-docs
    accessed: 2026-11-22
  - id: s2
    title: "Apex Developer Guide: Using SOQL Queries That Return One Record"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/apex-dev/references/apex-dev/langcon-apex-soql-single-row.html
    type: official-docs
    accessed: 2026-11-22
  - id: s3
    title: "Apex Developer Guide: Using Apex Variables in SOQL and SOSL Queries"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/apex-dev/references/apex-dev/langcon-apex-soql-variables.html
    type: official-docs
    accessed: 2026-11-22
  - id: s4
    title: "Apex Developer Guide: SOQL For Loops"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/apex-dev/references/apex-dev/langcon-apex-loops-for-soql.html
    type: official-docs
    accessed: 2026-11-22
  - id: s5
    title: "Apex Developer Guide: Built-In Exceptions and Common Methods"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/apex-dev/references/apex-dev/apex-exception-builtin.html
    type: official-docs
    accessed: 2026-11-22
  - id: s6
    title: "Salesforce Certified Platform Developer Exam Guide"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298965&language=en_US&type=1
    type: official-learning
    accessed: 2026-11-22
created: 2026-11-22
---

# Static SOQL

Static SOQL, also called inline SOQL, is a SOQL statement written directly in Apex source code between square brackets, such as `List<Account> aa = [SELECT Id, Name FROM Account WHERE Name = 'Acme' WITH USER_MODE];`. Apex evaluates the bracketed expression in place, and the result can be assigned to a list of sObjects, a single sObject, or an Integer when the query uses `COUNT()`.[^s1] It contrasts with dynamic SOQL, where the query is assembled as a string at run time and passed to a `Database` method. The query language is the same; static SOQL fixes the query's structure in the code and varies only the values.[^s1][^s3]

## How it works

**Return shapes.** A list on the left-hand side receives every matching row. When the left-hand side is a single sObject type, Apex takes the one record from the result automatically, and a field can even be dereferenced straight off the query, as in `[SELECT Name FROM Account WITH USER_MODE].Name`.[^s2] Single-row assignment also works with the safe navigation and null coalescing operators.[^s2]

**Bind variables.** Values come from Apex through binds: a local variable or expression prefixed with a colon, which the Apex parser evaluates before the query runs.[^s3] Binds are allowed in `WHERE` filter values, in `IN` and `NOT IN` lists (including lists of IDs, strings or sObjects), in `LIMIT`, `OFFSET` and `WITH DIVISION`, and in a SOSL `FIND` string. They are not allowed for the units argument of the `DISTANCE` function.[^s3] A bind can be an expression, such as `:('x' + 'xx')`, or even the result of another inline query.[^s3]

**SOQL for loops.** A static query can drive a loop directly: `for (Account a : [SELECT ...])` runs once per record, while `for (List<Account> batch : [SELECT ...])` runs once per batch of 200 records.[^s4] The loop fetches rows in chunks through query and queryMore, which avoids the heap limit at some cost in CPU. For large result sets, Salesforce recommends the loop over assigning everything to one list.[^s1][^s4]

## Limits and gotchas (verified for Winter '27)

Inline queries count against the same SOQL governor limits as any other query; the Apex guide points to the execution governors page for the per-transaction ceilings.[^s1]

- Assigning to a single sObject throws `QueryException` when zero rows or more than one row match; the no-rows message is "List has no rows for assignment to SObject".[^s2][^s5]
- Assigning zero rows to a list does not throw. The list is simply empty, so check its size before reading an element.[^s5]
- Reading a field that the query did not select throws `SObjectException`, because the record came back without that field.[^s5]
- In a list-form for loop, a DML statement per record can still hit run-time limits; act on the whole batch instead.[^s4]
- Aggregate queries do not support queryMore, so one returning more than 2,000 rows in a for loop throws a run-time exception.[^s4]
- Reading 200 or more child records from an inner query can throw a `QueryException`; iterate the child list with a for loop instead.[^s4]
- The 4,000-character limit on `WHERE` clauses does not apply to Apex SOQL when the clause uses `IN`.[^s1]

The Winter '27 Apex Developer Guide examples consistently add `WITH USER_MODE` to inline queries and pair loop updates with `update as user`.[^s1][^s2][^s4]

## When to use it (and when not)

Use static SOQL whenever the object, fields and filters are known when the code is written, and only the filter values change: binds cover that case without building strings.[^s3] Reach for dynamic SOQL only when the query's structure itself must vary at run time, such as user-chosen fields or optional filters.[^s1] When a result set is too large for the heap, switch from list assignment to a SOQL for loop rather than to a different API.[^s1][^s4]

Writing SOQL in Apex and predicting what it returns is a named objective in the Process Automation and Logic section (28%) of the Platform Developer exam.[^s6]

## Connections

Static SOQL is how **SOQL** is most often run from **Apex**, its two broader nodes.[^s1] It is the **alternative to dynamic SOQL**, which builds the query string at run time.[^s1][^s3] Each inline query counts toward **governor limits**, and SOQL for loops with list batching are a core **bulkification** technique.[^s1][^s4] `WITH USER_MODE` in the guide's examples links it to **Apex user mode**.[^s1][^s2] The same bracket syntax and bind rules apply to inline **SOSL** searches, which return a list of lists.[^s1][^s3] Writing and reading inline queries is **covered by the Platform Developer certification**.[^s6]

## Sources

[^s1]: Salesforce Developers, "Apex Developer Guide: SOQL and SOSL Queries" (Winter '27, API 68.0). https://developer.salesforce.com/docs/platform/apex-dev/references/apex-dev/langcon-apex-soql.html (accessed 2026-11-22)
[^s2]: Salesforce Developers, "Apex Developer Guide: Using SOQL Queries That Return One Record" (Winter '27, API 68.0). https://developer.salesforce.com/docs/platform/apex-dev/references/apex-dev/langcon-apex-soql-single-row.html (accessed 2026-11-22)
[^s3]: Salesforce Developers, "Apex Developer Guide: Using Apex Variables in SOQL and SOSL Queries" (Winter '27, API 68.0). https://developer.salesforce.com/docs/platform/apex-dev/references/apex-dev/langcon-apex-soql-variables.html (accessed 2026-11-22)
[^s4]: Salesforce Developers, "Apex Developer Guide: SOQL For Loops" (Winter '27, API 68.0). https://developer.salesforce.com/docs/platform/apex-dev/references/apex-dev/langcon-apex-loops-for-soql.html (accessed 2026-11-22)
[^s5]: Salesforce Developers, "Apex Developer Guide: Built-In Exceptions and Common Methods" (Winter '27, API 68.0). https://developer.salesforce.com/docs/platform/apex-dev/references/apex-dev/apex-exception-builtin.html (accessed 2026-11-22)
[^s6]: Salesforce Help, "Salesforce Certified Platform Developer Exam Guide". https://help.salesforce.com/s/articleView?id=005298965&language=en_US&type=1 (accessed 2026-11-22)
