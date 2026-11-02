---
id: kt:soql
type: Language
title: SOQL
aliases: [Salesforce Object Query Language, SOQL query, SOQL queries]
domain: development
summary: >-
  Salesforce Object Query Language, the read-only, SQL-like language for retrieving records from Salesforce
  objects by field API name, used from Apex, the REST and SOAP APIs, Bulk API and developer tools.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:object-relationships, kt:query-optimizer-selectivity]
relations:
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: usedBy, object: kt:apex}
  - {predicate: usedBy, object: kt:bulk-api-2}
  - {predicate: contrastsWith, object: kt:sosl}
sources:
  - id: s1
    title: "Salesforce Developer Limits and Allocations Quick Reference: SOQL and SOSL Limits for Search Queries"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_soslsoql.htm
    type: official-docs
    accessed: 2026-11-02
  - id: s2
    title: "SOQL and SOSL Reference: Using Relationship Queries"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_relationships_query_using.htm
    type: official-docs
    accessed: 2026-11-02
  - id: s3
    title: "Apex Developer Guide: Execution Governors and Limits"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_gov_limits.htm
    type: official-docs
    accessed: 2026-11-02
  - id: s4
    title: "Apex Developer Guide: Using Apex Variables in SOQL and SOSL Queries"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/langCon_apex_SOQL_variables.htm
    type: official-docs
    accessed: 2026-11-02
  - id: s5
    title: "Apex Developer Guide: Enforce User Mode for Database Operations"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_classes_enforce_usermode.htm
    type: official-docs
    accessed: 2026-11-02
  - id: s6
    title: "SOQL for Admins: Get Started with SOQL Queries"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/soql-for-admins/get-started-with-soql-queries
    type: official-learning
    accessed: 2026-11-02
created: 2026-11-02
---

# SOQL

SOQL (Salesforce Object Query Language) is the language for reading record data out of a Salesforce org. It only retrieves data: inserts, updates and deletes go through DML instead.[^s6] A query names the fields to return in a required `SELECT` clause and the object in a required `FROM` clause. It can then add an optional `WHERE` filter (with `AND`, `OR` and `IN`), `ORDER BY` sorting (ascending by default, with `DESC` and `NULLS FIRST`/`NULLS LAST`) and a `LIMIT` on rows. Fields are referenced by API name, not by label, and admins can try queries in the Developer Console's Query Editor.[^s6]

## How it works

Related data is reached through the relationships defined in the schema. For child-to-parent (usually many-to-one) traversal, dot notation can appear in `SELECT`, `FROM` or `WHERE`, for example `Account.Name` on a Contact query. For parent-to-child (usually one-to-many) traversal, a parenthesised subquery uses the child relationship name, which for standard objects is the plural child name, such as `Contacts`. A subquery's `WHERE` can filter on any object reachable from the root through parent relationships, and both directions can be combined in one query.[^s2]

In Apex, a query can reference local variables and expressions by prefixing them with a colon, which the documentation calls a bind. Binds are allowed in `WHERE` filter values, in `IN`/`NOT IN` lists (for filtering on a collection of IDs or strings), in `LIMIT` and `OFFSET` values, in `WITH DIVISION`, and in a SOSL `FIND` string. They are not supported for the units argument of `DISTANCE`.[^s4]

Security context matters. The Winter '27 (API 68.0) Apex Developer Guide says database operations apply the running user's sharing, field-level security and object permissions in user mode. In API version 67.0 and later Apex runs in user context by default, while 66.0 and earlier default to system mode.[^s5] A query in user mode reports every inaccessible field through `QueryException.getInaccessibleFields()`.[^s5]

## Limits and gotchas (verified for Winter '27)

Statement-level limits from the Developer Limits Quick Reference:[^s1]

- A SOQL statement can be up to 100,000 characters by default. Complex queries, such as those with many formula or currency fields, can still fail with `QUERY_TOO_COMPLICATED` below that size.
- Each string in a `WHERE` clause is capped at 4,000 characters.
- A query can specify up to 55 child-to-parent relationships and 20 parent-to-child relationships. Polymorphic fields can count more than once.
- Child-to-parent paths can be five levels deep. Parent-to-child nesting is up to five levels (the root counts as level one) in API 58.0 and later through REST, SOAP and Apex, but not for big objects, external objects or Bulk API.[^s1][^s2]
- `OFFSET` tops out at 2,000 rows. A request returns up to 2,000 results by default from API 28.0 onward. A query gets 2 minutes to execute and 30 minutes to process results.

Per-transaction Apex governor limits:[^s3]

- 100 SOQL queries in synchronous Apex and 200 in asynchronous Apex.[^s3]
- 50,000 records retrieved by SOQL across the transaction, and 10,000 through `Database.getQueryLocator`.[^s3]

Because the query cap is per transaction, running a query inside a loop over trigger records is the classic way to hit it. Querying once and filtering on a collection with an `IN` bind keeps the count flat.[^s3][^s4]

## When to use it (and when not)

Use SOQL when you know which object holds the data and want precise filters, sorting or related records in one round trip.[^s2][^s6] When the user types free text that might appear in many objects, SOSL is the better fit. It runs under its own limits: 20 SOSL queries per transaction and 2,000 records per SOSL query.[^s3] For very large extracts, Bulk API is an option, but the five-level parent-to-child nesting does not apply there.[^s1]

## Connections

SOQL is part of the **Salesforce Platform**, its broader node. It is **used by Apex**, where binds and security modes shape how it runs, and by **Bulk API 2.0** for high-volume reads.[^s4][^s5][^s1] Its per-transaction ceilings make it **governed by governor limits**.[^s3] Relationship queries can only follow the lookups and master-detail links defined on **object relationships**.[^s2] On large tables, whether a `WHERE` filter is selective (see **query optimizer selectivity**) decides how well a query performs. SOQL **contrasts with SOSL**, the search language that shares its reference guide and limits page.[^s1][^s2]

## Sources

[^s1]: Salesforce Developers, "Salesforce Developer Limits and Allocations Quick Reference: SOQL and SOSL Limits for Search Queries". https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_soslsoql.htm (accessed 2026-11-02)
[^s2]: Salesforce Developers, "SOQL and SOSL Reference: Using Relationship Queries". https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_relationships_query_using.htm (accessed 2026-11-02)
[^s3]: Salesforce Developers, "Apex Developer Guide: Execution Governors and Limits". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_gov_limits.htm (accessed 2026-11-02)
[^s4]: Salesforce Developers, "Apex Developer Guide: Using Apex Variables in SOQL and SOSL Queries" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/langCon_apex_SOQL_variables.htm (accessed 2026-11-02)
[^s5]: Salesforce Developers, "Apex Developer Guide: Enforce User Mode for Database Operations" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_classes_enforce_usermode.htm (accessed 2026-11-02)
[^s6]: Trailhead, "SOQL for Admins: Get Started with SOQL Queries". https://trailhead.salesforce.com/content/learn/modules/soql-for-admins/get-started-with-soql-queries (accessed 2026-11-02)
