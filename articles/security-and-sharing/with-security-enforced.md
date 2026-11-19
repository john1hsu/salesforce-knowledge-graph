---
id: kt:with-security-enforced
type: SecurityControl
title: WITH SECURITY_ENFORCED
aliases: [WITH SECURITY_ENFORCED clause, SOQL WITH SECURITY_ENFORCED, Filter SOQL Queries Using WITH SECURITY_ENFORCED]
domain: security-and-sharing
summary: >-
  A legacy Apex-only SOQL clause that checks object and field-level permissions for the fields and objects in a
  SELECT query and throws a QueryException if any are inaccessible; superseded by WITH USER_MODE and not allowed
  in Apex saved at API version 67.0 or later.
release: "Winter '27"
status: deprecated
broader: [kt:field-level-security, kt:soql, kt:secure-coding]
related: [kt:apex-security-with-sharing, kt:appexchange-security-review, kt:polymorphic-relationships]
relations:
  - {predicate: replacedBy, object: kt:apex-user-mode}
  - {predicate: alternativeTo, object: kt:security-stripinaccessible}
  - {predicate: dependsOn, object: kt:permission-sets}
  - {predicate: dependsOn, object: kt:profiles}
sources:
  - id: s1
    title: "Filter SOQL Queries Using WITH SECURITY_ENFORCED (Apex Developer Guide, Spring '26)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/pages/apex_classes_with_security_enforced.htm
    type: official-docs
    accessed: 2026-11-19
  - id: s2
    title: "Apex Security and Sharing (Apex Developer Guide, Winter '27)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/apex-dev/references/apex-dev/apex-security-sharing-chapter.html
    type: official-docs
    accessed: 2026-11-19
  - id: s3
    title: "Enforce User Mode for Database Operations (Apex Developer Guide, Spring '26)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/pages/apex_classes_enforce_usermode.htm
    type: official-docs
    accessed: 2026-11-19
  - id: s4
    title: "Protect Your Application from CRUD/FLS Vulnerabilities (Secure Coding Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/secure-coding/guide/secure-coding-access-control-protect-from-crud-fls-vulnerabilities.html
    type: official-docs
    accessed: 2026-11-19
  - id: s5
    title: "Write Secure Apex Controllers (Trailhead, Secure Server-Side Development)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/secure-serverside-development/write-secure-apex-controllers
    type: official-learning
    accessed: 2026-11-19
created: 2026-11-19
---

# WITH SECURITY_ENFORCED

`WITH SECURITY_ENFORCED` is a SOQL clause, usable only from Apex, that turns on object-level (CRUD) and field-level security (FLS) checks for a `SELECT` query, including its subqueries and cross-object relationship fields.[^s1] It was designed to cut the boilerplate of manual describe checks, and Salesforce pitched it at developers with little security experience and at apps that don't need to recover gracefully from missing permissions.[^s1][^s5] It is now legacy: Salesforce recommends `WITH USER_MODE` instead, and in Apex saved at API version 67.0 or later the clause can no longer be used at all.[^s2][^s3]

## How it works

Apex has traditionally ignored the running user's object and field permissions, so a query returned every field it named. Adding the clause makes the platform check each field and object referenced in the `SELECT` and `FROM` clauses against the user's permissions before returning data.[^s1] If any of them is inaccessible, the query throws a `System.QueryException` and returns nothing, so the check is all-or-nothing.[^s1][^s5]

Placement is fixed: the clause goes after `WHERE` (or after `FROM` when there is no `WHERE`) and before `ORDER BY`, `LIMIT`, `OFFSET` or aggregate clauses.[^s1] The guide's examples show the exception firing when a hidden field appears in a subquery, in a parent relationship such as `parent.Website`, or inside an aggregate like `GROUPING(Type)`.[^s1]

## Limits and gotchas

- **Only SELECT and FROM are checked.** Fields used only in `WHERE` or `ORDER BY` are not evaluated, because enforcement targets what the query returns.[^s1]
- **Polymorphic lookups.** Traversing a polymorphic relationship such as `What.Name` on Event isn't supported, except for `Owner`, `CreatedBy` and `LastModifiedBy`.[^s1][^s5]
- **No TYPEOF with ELSE.** `TYPEOF` expressions that include an `ELSE` branch aren't supported.[^s1]
- **First error only.** The clause stops at the first FLS violation, whereas user mode reports every inaccessible field.[^s3][^s4]
- **No record sharing.** It covers object and field permissions only; record visibility still comes from the class's sharing keywords.[^s1][^s3]
- **Old API versions.** Avoid it below API 45.0, and use API 48.0 or later for code going through AppExchange Security Review.[^s1][^s5]
- **Not combinable.** It can't be mixed with access-mode keywords or `AccessLevel` in the same query.[^s3][^s1]

## Status and migration

Salesforce now ranks `WITH USER_MODE` ahead of this clause because user mode also evaluates the `WHERE` clause, handles polymorphic fields, applies sharing rules and exposes the full list of inaccessible fields through `getInaccessibleFields()` on the exception.[^s3][^s4] The Secure Coding Guide states that the clause isn't allowed in AppExchange packages.[^s4] The Winter '27 Apex Developer Guide lists it as a versioned behavior change: from API version 67.0, Apex runs in user context by default and `WITH SECURITY_ENFORCED` can't be used in SOQL `SELECT` queries, while code at 66.0 and earlier keeps the old system-mode default.[^s2] The current guide no longer has a dedicated page for the clause.[^s2]

In practice, migrating means replacing the clause with `WITH USER_MODE` (or raising the class API version so user mode becomes the default); the two can't coexist in one query, so the old clause must come out.[^s2][^s3] Where the code should return partial data instead of failing, `Security.stripInaccessible()` removes the inaccessible fields rather than throwing.[^s5]

## Connections

The clause is a query-level enforcement mechanism for **field-level security** inside **SOQL** (**broader**), and one of the classic **secure-coding** answers to CRUD/FLS vulnerabilities.[^s4][^s1] It is **replaced by** **Apex user mode**, which the guide recommends and which becomes the default from API 67.0.[^s2][^s3] **stripInaccessible** is the **alternative** when graceful degradation matters.[^s5] Its checks **depend on** the object and field permissions granted through **profiles** and **permission sets**, and it is **related** to the **sharing keywords** that govern rows rather than fields.[^s1][^s3] Its restrictions on **polymorphic relationships** and its disallowance in packages bear on **AppExchange security review**.[^s1][^s4]

## Sources

[^s1]: Salesforce Developers, "Filter SOQL Queries Using WITH SECURITY_ENFORCED (Apex Developer Guide, Spring '26)". https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/pages/apex_classes_with_security_enforced.htm (accessed 2026-11-19)
[^s2]: Salesforce Developers, "Apex Security and Sharing (Apex Developer Guide, Winter '27)". https://developer.salesforce.com/docs/platform/apex-dev/references/apex-dev/apex-security-sharing-chapter.html (accessed 2026-11-19)
[^s3]: Salesforce Developers, "Enforce User Mode for Database Operations (Apex Developer Guide, Spring '26)". https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/pages/apex_classes_enforce_usermode.htm (accessed 2026-11-19)
[^s4]: Salesforce Developers, "Protect Your Application from CRUD/FLS Vulnerabilities (Secure Coding Guide)". https://developer.salesforce.com/docs/platform/secure-coding/guide/secure-coding-access-control-protect-from-crud-fls-vulnerabilities.html (accessed 2026-11-19)
[^s5]: Trailhead, "Write Secure Apex Controllers (Trailhead, Secure Server-Side Development)". https://trailhead.salesforce.com/content/learn/modules/secure-serverside-development/write-secure-apex-controllers (accessed 2026-11-19)
