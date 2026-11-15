---
id: kt:apex-user-mode
type: SecurityControl
title: Apex User Mode
aliases: [user mode database operations, WITH USER_MODE, AccessLevel.USER_MODE, as user DML, Apex access modes, Apex system mode]
domain: security-and-sharing
summary: >-
  The Apex access mode that runs a query, search or DML operation with the running user's object permissions,
  field-level security and record sharing enforced, selected per operation with WITH USER_MODE, as user or
  AccessLevel.USER_MODE and, from Apex API version 67.0, the default for database operations.
release: "Winter '27"
status: current
broader: [kt:apex, kt:salesforce-sharing-model]
related: [kt:field-level-security, kt:dynamic-soql, kt:soql-injection, kt:appexchange-security-review, kt:restriction-rules]
relations:
  - {predicate: contrastsWith, object: kt:apex-security-with-sharing}
  - {predicate: alternativeTo, object: kt:security-stripinaccessible}
  - {predicate: replaces, object: kt:with-security-enforced}
  - {predicate: dependsOn, object: kt:permission-sets}
  - {predicate: consumedBy, object: kt:soql}
  - {predicate: consumedBy, object: kt:sosl}
sources:
  - id: s1
    title: "Set an Access Mode for Database Operations (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexref/apex_classes_enforce_usermode.htm
    type: official-docs
    accessed: 2026-11-15
  - id: s2
    title: "AccessLevel Class (Apex Reference Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apex/apex_class_System_AccessLevel.htm
    type: official-docs
    accessed: 2026-11-15
  - id: s3
    title: "Apex Versioned Behavior Changes"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/versioned_behavior_changes.htm
    type: official-docs
    accessed: 2026-11-15
  - id: s4
    title: "Protect Your Application from CRUD/FLS Vulnerabilities (Secure Coding Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/secure-coding/guide/secure-coding-access-control-protect-from-crud-fls-vulnerabilities.html
    type: official-docs
    accessed: 2026-11-15
  - id: s5
    title: "Write Simplified and Secure Apex with Spring '23 Updates"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2023/05/write-simplified-and-secure-apex-with-spring-23-updates
    type: official-blog
    accessed: 2026-11-15
  - id: s6
    title: "Write Secure Apex Controllers (Trailhead: Secure Server-Side Development)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/secure-serverside-development/write-secure-apex-controllers
    type: official-learning
    accessed: 2026-11-15
created: 2026-11-15
---

# Apex User Mode

Apex can run each database operation in one of two **access modes**. In **user mode**, a query, search or DML statement applies the running user's object permissions, field-level security (FLS) and record sharing. In **system mode**, object permissions and FLS are ignored, and record visibility falls back to the sharing keyword of the class that runs the code.[^s1] The mode is chosen per operation, which makes user mode a finer-grained tool than class-level sharing declarations: it decides what the user may see and change on the specific statement where it is applied.[^s2]

## How to select the mode

Each kind of database operation has its own syntax:

- **SOQL and SOSL:** append `WITH USER_MODE` or `WITH SYSTEM_MODE` to the query.[^s1]
- **Static DML:** put `as user` or `as system` between the operator and the record, as in `insert as user acct;`.[^s1][^s5]
- **Database and Search methods:** pass `AccessLevel.USER_MODE` or `AccessLevel.SYSTEM_MODE` as the `accessLevel` argument.[^s2]

The `accessLevel` argument is optional on `Database.query`, `getQueryLocator`, `countQuery`, the cursor methods, `Search.query`, and the DML methods (insert, update, upsert, merge, delete, undelete, convertLead and their Immediate and Async forms). It is required on the `...WithBinds` query variants, so bind-variable dynamic SOQL always states its mode explicitly.[^s1]

## Default behavior and API versions

The default changed with the Apex API version. From version 67.0, Apex database operations run in user mode by default, and classes without a sharing declaration enforce the current user's sharing. Code saved at 66.0 or earlier keeps system mode as the default and keeps the old sharing inheritance.[^s3] Older guidance that calls Apex "system mode by default" therefore describes classes on earlier API versions.[^s4][^s6] Version 67.0 also removed support for `WITH SECURITY_ENFORCED` in SOQL SELECT queries, so `WITH USER_MODE` is the way to enforce user permissions in a query.[^s3] Raising a class's API version is a behavior change: queries can return fewer rows and DML can start failing for users who lack permissions, so test with realistic users before upgrading.[^s3][^s6]

## Errors and diagnostics

User mode fails loudly. An operation on an object the user can't access throws a `SecurityException` that names the object.[^s1] A query in user mode applies every clause, including `WHERE`, supports polymorphic fields such as `Owner`, and reports all FLS errors. `QueryException.getInaccessibleFields()` returns the full set of fields the user can't read.[^s1][^s4] For DML, `DMLException.getDmlFieldNames()` or `SaveResult.getErrors()` with `getFields()` identify the fields that failed FLS checks.[^s1]

## User mode vs. the alternatives

Salesforce recommends `WITH USER_MODE` over `WITH SECURITY_ENFORCED`. User mode also supports SOSL and polymorphic lookups, checks fields in `WHERE` and `ORDER BY`, performs better, and is expected to pick up future platform controls.[^s5][^s4] `WITH SECURITY_ENFORCED` reports only the first FLS error and isn't allowed in AppExchange packages.[^s4] The Trailhead secure-coding unit adds that user mode enforces restriction rules as well as sharing and CRUD/FLS.[^s6]

`Security.stripInaccessible()` is the alternative when code should degrade gracefully instead of throwing: it silently removes fields the user can't access. It doesn't support `AggregateResult` and never strips the Id field.[^s4][^s6] Schema describe calls such as `isAccessible()` and `isUpdateable()` remain useful for custom error messages or UI branching.[^s4] Applied to an operation, user mode overrides a class's `without sharing` setting for that operation.[^s5]

## Gotchas

- **Permission set elevation is preview only.** `AccessLevel.USER_MODE.withPermissionSetId()` adds a permission set's permissions for one operation, but it is a Developer Preview that only works in scratch orgs with a feature flag enabled.[^s2][^s1]
- **Scanner false positives.** The AppExchange security review scanner may flag CRUD/FLS violations in user-mode code; document these as false positives in the submission.[^s1]
- **System mode is not a full bypass.** Record access in system mode still follows the class's sharing keyword.[^s1]

## Connections

User mode is an Apex mechanism (**broader** `kt:apex`) for enforcing the access layers of the **sharing model** (`kt:salesforce-sharing-model`): object permissions and **field-level security** come from profiles and **permission sets**, which user mode depends on.[^s1][^s4] It **contrasts with** the class-level **sharing keywords** (`kt:apex-security-with-sharing`), which control only record visibility.[^s1] It **replaces** `WITH SECURITY_ENFORCED` from API 67.0 and is an **alternative to** `Security.stripInaccessible`.[^s3][^s4] It is applied to **SOQL**, **SOSL** and **dynamic SOQL**, and enforces **restriction rules**.[^s1][^s6] It matters for the **AppExchange security review**, where CRUD/FLS enforcement is checked.[^s4]

## Sources

[^s1]: Salesforce Developers, "Set an Access Mode for Database Operations (Apex Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexref/apex_classes_enforce_usermode.htm (accessed 2026-11-15)
[^s2]: Salesforce Developers, "AccessLevel Class (Apex Reference Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apex/apex_class_System_AccessLevel.htm (accessed 2026-11-15)
[^s3]: Salesforce Developers, "Apex Versioned Behavior Changes". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/versioned_behavior_changes.htm (accessed 2026-11-15)
[^s4]: Salesforce Developers, "Protect Your Application from CRUD/FLS Vulnerabilities (Secure Coding Guide)". https://developer.salesforce.com/docs/platform/secure-coding/guide/secure-coding-access-control-protect-from-crud-fls-vulnerabilities.html (accessed 2026-11-15)
[^s5]: Salesforce Developers Blog, "Write Simplified and Secure Apex with Spring '23 Updates". https://developer.salesforce.com/blogs/2023/05/write-simplified-and-secure-apex-with-spring-23-updates (accessed 2026-11-15)
[^s6]: Trailhead, "Write Secure Apex Controllers (Secure Server-Side Development)". https://trailhead.salesforce.com/content/learn/modules/secure-serverside-development/write-secure-apex-controllers (accessed 2026-11-15)
