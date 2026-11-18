---
id: kt:security-stripinaccessible
type: SecurityControl
title: Security.stripInaccessible
aliases: [stripInaccessible, stripInaccessible method, SObjectAccessDecision, Security class stripInaccessible]
domain: security-and-sharing
summary: >-
  An Apex method in the System.Security class that returns copies of sObjects with every field the running user
  cannot access for a given operation removed, so code can enforce field-level security and degrade gracefully
  instead of throwing.
release: "Winter '27"
status: current
broader: [kt:field-level-security, kt:secure-coding, kt:apex]
related: [kt:lightning-data-service, kt:appexchange-security-review, kt:apex-security-with-sharing]
relations:
  - {predicate: alternativeTo, object: kt:apex-user-mode}
  - {predicate: alternativeTo, object: kt:with-security-enforced}
  - {predicate: dependsOn, object: kt:permission-sets}
sources:
  - id: s1
    title: "Enforce Security with the stripInaccessible Method (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_classes_with_security_stripInaccessible.htm
    type: official-docs
    accessed: 2026-11-18
  - id: s2
    title: "Security Class (Apex Reference Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_class_System_Security.htm
    type: official-docs
    accessed: 2026-11-18
  - id: s3
    title: "SObjectAccessDecision Class (Apex Reference Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_class_System_SObjectAccessDecision.htm
    type: official-docs
    accessed: 2026-11-18
  - id: s4
    title: "Protect Your Application from CRUD/FLS Vulnerabilities (Secure Coding Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/secure-coding/guide/secure-coding-access-control-protect-from-crud-fls-vulnerabilities.html
    type: official-docs
    accessed: 2026-11-18
  - id: s5
    title: "Secure Apex Classes (Lightning Web Components Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/apex-security
    type: official-docs
    accessed: 2026-11-18
  - id: s6
    title: "Securing Data in Apex Controllers (Lightning Aura Components Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/apex_crud_fls.htm
    type: official-docs
    accessed: 2026-11-18
created: 2026-11-18
---

# Security.stripInaccessible

`Security.stripInaccessible()` is a static Apex method that takes a list of sObjects and an operation type, and hands back new sObjects from which every field the running user can't access for that operation has been removed, relationship fields included.[^s1] Rather than aborting the transaction when a user lacks permission on one field, the code keeps going with the fields that are allowed, which Salesforce describes as graceful degradation.[^s1][^s5] It enforces field-level security (FLS) and, optionally, object-level (CRUD) permissions; it does not decide which records are visible.[^s2][^s5]

## How it works

The method is called with an `AccessType` value (the examples use `READABLE`, `CREATABLE` and `UPDATABLE`) and the source records, and returns a `System.SObjectAccessDecision`.[^s1][^s2] The decision object exposes three methods:

- `getRecords()` returns the sanitized sObjects in the same order as the input, always as a list.[^s3][^s1]
- `getRemovedFields()` returns a map from sObject type name to the set of field names that were stripped.[^s3]
- `getModifiedIndexes()` returns the row indexes of the records that lost at least one field.[^s3]

A stripped field is not set on the returned record, so `isSet()` on that field returns false, and fields that were never queried come back as null without an exception.[^s4][^s1]

The Security class offers three overloads. The basic one takes the access type and records. A second adds `enforceRootObjectCRUD`, which defaults to true; when that object-level check fails, the method throws an exception instead of stripping.[^s2] A third adds a permission set Id so that permission set's access is applied on top of the user's. It is a Developer Preview limited to scratch orgs with the `ApexUserModeWithPermset` feature, and Salesforce says not to use it in production.[^s2]

## Typical uses

Salesforce documents three use cases:[^s1][^s2]

- Removing unreadable fields, including lookup and master-detail fields, from query and subquery results.[^s1]
- Removing fields the user can't create or update from records before DML, so the insert or update doesn't fail.[^s1]
- Sanitizing sObjects deserialized from an untrusted source, such as JSON from a client, before they are saved.[^s1]

A common controller pattern for Lightning components runs the query, strips it with `READABLE`, and checks `getModifiedIndexes()`. If anything was removed, the code throws an `AuraHandledException` with a friendly message or simply returns the reduced data.[^s5][^s6]

## Limits and gotchas

- **No AggregateResult.** Passing `AggregateResult` records throws an exception, so aggregate queries need another enforcement method.[^s1][^s4]
- **Id is kept.** The Id field is never removed, so DML on the returned records still works.[^s1][^s4]
- **Fields, not rows.** Sharing keywords such as `with sharing` control record-level access only; record visibility must come from them or from the query's access mode.[^s5][^s6]
- **Use the returned list.** The method builds new sObjects, so later DML must run on `getRecords()`, not on the original list.[^s3][^s1]

## When to use it (and when not)

Salesforce's component guides recommend `WITH USER_MODE` for straightforward enforcement and `stripInaccessible()` when the code needs to handle missing access gracefully.[^s5] A user-mode query fails outright when the user lacks access, while stripping lets the caller decide what to do.[^s6] Since Apex API version 67.0, database operations run in user mode by default, and system mode must be requested explicitly. Code that opts into system mode, or that builds records from external input, is where stripping still adds protection.[^s5][^s1] Before these options, developers wrote Schema describe checks (`isAccessible()`, `isCreateable()`, `isUpdateable()`) field by field. That approach is now treated as legacy because of its boilerplate, though it still suits custom error messages.[^s6][^s4] For plain record reads and edits, Lightning Data Service handles sharing, CRUD and FLS without Apex.[^s5]

## Connections

`stripInaccessible()` is an Apex enforcement mechanism (**broader** `kt:apex`) for **field-level security** and a core **secure-coding** technique against CRUD/FLS vulnerabilities.[^s4][^s1] It is an **alternative to** **Apex user mode** and to the older `WITH SECURITY_ENFORCED` clause, which the Secure Coding Guide ranks below user mode and disallows in AppExchange packages.[^s4][^s5] It **depends on** the object and field permissions granted through profiles and **permission sets**, and pairs with the class **sharing keywords**, which cover records rather than fields.[^s2][^s5] Any deliberate CRUD/FLS bypass that remains must be documented for **AppExchange security review**.[^s4] **Lightning Data Service** is the no-code route that makes such Apex checks unnecessary for basic record access.[^s5]

## Sources

[^s1]: Salesforce Developers, "Enforce Security with the stripInaccessible Method (Apex Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_classes_with_security_stripInaccessible.htm (accessed 2026-11-18)
[^s2]: Salesforce Developers, "Security Class (Apex Reference Guide)". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_class_System_Security.htm (accessed 2026-11-18)
[^s3]: Salesforce Developers, "SObjectAccessDecision Class (Apex Reference Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_class_System_SObjectAccessDecision.htm (accessed 2026-11-18)
[^s4]: Salesforce Developers, "Protect Your Application from CRUD/FLS Vulnerabilities (Secure Coding Guide)". https://developer.salesforce.com/docs/platform/secure-coding/guide/secure-coding-access-control-protect-from-crud-fls-vulnerabilities.html (accessed 2026-11-18)
[^s5]: Salesforce Developers, "Secure Apex Classes (Lightning Web Components Developer Guide)". https://developer.salesforce.com/docs/platform/lwc/guide/apex-security (accessed 2026-11-18)
[^s6]: Salesforce Developers, "Securing Data in Apex Controllers (Lightning Aura Components Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/apex_crud_fls.htm (accessed 2026-11-18)
