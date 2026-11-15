---
id: kt:dynamic-soql
type: Feature
title: Dynamic SOQL
aliases: [Database.query, Database.queryWithBinds, runtime SOQL, dynamic SOQL query]
domain: development
summary: >-
  The Apex capability to build a SOQL query as a string at run time and execute it through Database methods such as
  query, queryWithBinds, countQuery and getQueryLocator, instead of writing the query inline in square brackets.
release: "Winter '27"
status: current
broader: [kt:soql, kt:apex]
related: [kt:soql-injection, kt:batch-apex, kt:apex-security-with-sharing, kt:apex-user-mode, kt:visualforce]
relations:
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: alternativeTo, object: kt:static-soql}
sources:
  - id: s1
    title: "Apex Developer Guide: Dynamic SOQL"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/apexcode/apex_dynamic_soql.htm
    type: official-docs
    accessed: 2026-11-15
  - id: s2
    title: "Platform Developer I Certification Maintenance (Winter '24): Get Hands-on with Bind Variables in a SOQL Query"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/de/content/learn/modules/platform-developer-i-certification-maintenance-winter-24/get-hands-on-with-bind-variables-in-a-soql-query
    type: official-learning
    accessed: 2026-11-15
  - id: s3
    title: "Execution Governors and Limits"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexref/apex_gov_limits.htm
    type: official-docs
    accessed: 2026-11-15
  - id: s4
    title: "Visualforce Developer Guide: SOQL Injection"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.pages.meta/pages/pages_security_tips_soql_injection.htm
    type: official-docs
    accessed: 2026-11-15
  - id: s5
    title: "Apex Reference Guide: QueryLocator Class"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_methods_system_database_batch.htm
    type: official-docs
    accessed: 2026-11-15
created: 2026-11-15
---

# Dynamic SOQL

Dynamic SOQL is the Apex technique of assembling a SOQL statement as a string while the code runs and then executing it, rather than writing a fixed query inline between square brackets. Salesforce positions it as a way to build more flexible applications: a search screen whose filters come from the end user, or a utility that updates records whose field names are only known at run time.[^s1] The query language is the same SOQL; what changes is when the query text is decided and which API executes it.[^s1]

## How it works

The `Database` class supplies a family of methods that take a query string.[^s1][^s2]

- `Database.query` returns one sObject when a single record comes back, otherwise a `List<sObject>`, and can appear anywhere inline SOQL can, including `for` loops.[^s1]
- `Database.queryWithBinds` (API 57.0 and later) takes the query string, a `Map<String, Object>` of bind values and an access level, and returns a `List<sObject>`.[^s1]
- `Database.countQuery` and `Database.countQueryWithBinds` return how many records the dynamic query would match.[^s1][^s2]
- `Database.getQueryLocator` and `Database.getQueryLocatorWithBinds` produce a `QueryLocator`, the record set used by Batch Apex and Visualforce.[^s1][^s5]

Results can be assigned to a concrete type such as `List<Account>` or to generic `sObject`. The runtime checks that the query's result type matches the declared variable and throws an error on a mismatch, so no cast from generic sObject is needed.[^s1]

Binds work differently in the two styles. Plain `Database.query` resolves simple binds such as `:accountName`, but only variables in scope at the call site.[^s1] The `WithBinds` methods instead look up each `:name` placeholder by key in the supplied map, so a helper method can run a query built elsewhere without the caller's variables being visible. Trailhead's example passes a map keyed `name` with `AccessLevel.USER_MODE` to query accounts by name.[^s2]

Since API 55.0 the methods accept an `AccessLevel`. `USER_MODE` enforces the running user's object permissions, field-level security and sharing rules. `SYSTEM_MODE` ignores object and field permissions and leaves sharing to the class's sharing keywords. The Winter '27 guide lists user mode as the default.[^s1]

## Limits and gotchas (verified for Winter '27)

Dynamic queries share static SOQL's governor limits. Every call to `query`, `queryWithBinds`, `countQuery`, `countQueryWithBinds`, `getQueryLocator` and `getQueryLocatorWithBinds` counts toward the per-transaction SOQL statement limit.[^s3]

- 100 SOQL queries per synchronous transaction and 200 per asynchronous transaction.[^s3]
- 50,000 records retrieved by SOQL per transaction, and 10,000 retrieved through `Database.getQueryLocator`.[^s3]
- `Database.query` cannot bind a field on an object (`:myRecord.Field__c`); it fails with `Variable does not exist`. Copy the value into a local variable first.[^s1]
- `queryWithBinds` matches map keys case-insensitively, so two keys differing only in case throw a `QueryException`.[^s1]
- Map keys must start with an ASCII letter, avoid reserved words and follow Apex naming rules. Dot notation in keys still works but is discouraged.[^s1]
- A `getQueryLocator` query cannot use `FOR UPDATE`. Call `iterator()` once and reuse the result, because each call creates a new iterator.[^s5]

The largest risk is SOQL injection. Concatenating user input into the string lets an attacker close a quoted value and append clauses that change the query's logic.[^s4] Salesforce's first recommendation is to avoid dynamic SOQL and use a static query with bind variables. Where dynamic SOQL is unavoidable, escape user strings with `String.escapeSingleQuotes`.[^s4][^s1] Map-based binds keep values out of the query text entirely, which makes `queryWithBinds` the safer way to pass filter values.[^s1][^s2]

## When to use it (and when not)

Use dynamic SOQL when the shape of the query, such as the object, the field list or the set of filters, is not known at compile time: configurable list views, generic utilities driven by metadata, or search pages with optional criteria.[^s1] When only the filter values vary, static SOQL with binds is simpler, is checked at compile time and is the injection-safe default.[^s4] For large Batch Apex jobs, return a `QueryLocator` from `start` rather than a list.[^s5]

## Connections

Dynamic SOQL is a way of running **SOQL** from **Apex**, its two broader nodes, and it is the main place **SOQL injection** arises.[^s1][^s4] It is an **alternative to static SOQL** when only values, not structure, change.[^s4] Its query count and row ceilings make it **governed by governor limits**.[^s3] `getQueryLocator` connects it to **Batch Apex** and to **Visualforce** set controllers.[^s1][^s5] The `AccessLevel` argument ties it to **Apex user mode** and to the class-level sharing keywords described under **Apex security and sharing**.[^s1]

## Sources

[^s1]: Salesforce Developers, "Apex Developer Guide: Dynamic SOQL" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/apexcode/apex_dynamic_soql.htm (accessed 2026-11-15)
[^s2]: Trailhead, "Platform Developer I Certification Maintenance (Winter '24): Get Hands-on with Bind Variables in a SOQL Query". https://trailhead.salesforce.com/de/content/learn/modules/platform-developer-i-certification-maintenance-winter-24/get-hands-on-with-bind-variables-in-a-soql-query (accessed 2026-11-15)
[^s3]: Salesforce Developers, "Execution Governors and Limits" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexref/apex_gov_limits.htm (accessed 2026-11-15)
[^s4]: Salesforce Developers, "Visualforce Developer Guide: SOQL Injection". https://developer.salesforce.com/docs/atlas.en-us.264.0.pages.meta/pages/pages_security_tips_soql_injection.htm (accessed 2026-11-15)
[^s5]: Salesforce Developers, "Apex Reference Guide: QueryLocator Class". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_methods_system_database_batch.htm (accessed 2026-11-15)
