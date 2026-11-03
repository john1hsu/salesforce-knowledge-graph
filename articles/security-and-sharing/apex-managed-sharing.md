---
id: kt:apex-managed-sharing
type: SecurityControl
title: Apex Managed Sharing
aliases: [Apex sharing, programmatic sharing, Apex sharing reasons, share object rows in Apex]
domain: security-and-sharing
summary: >-
  Programmatic record sharing in which Apex or the SOAP API inserts rows into an object's share table
  (for example Job__Share) under a custom Apex sharing reason, granting Read or Edit access that survives
  ownership changes and can be rebuilt by a batch recalculation class.
release: "Winter '27"
status: current
broader: [kt:salesforce-sharing-model]
related: [kt:sharing-rules, kt:organization-wide-defaults, kt:apex-triggers, kt:batch-apex]
relations:
  - {predicate: dependsOn, object: kt:apex}
  - {predicate: alternativeTo, object: kt:sharing-rules}
  - {predicate: causes, object: kt:sharing-recalculation}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: coveredBy, object: kt:sharing-and-visibility-architect-certification}
sources:
  - id: s1
    title: "Sharing a Record Using Apex (Apex Developer Guide, Winter '27)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_bulk_sharing_creating_with_apex.htm
    type: official-docs
    accessed: 2026-11-03
  - id: s2
    title: "Understanding Sharing (Apex Developer Guide, Winter '27)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/apexref/apex_bulk_sharing_understanding.htm
    type: official-docs
    accessed: 2026-11-03
  - id: s3
    title: "Recalculating Apex Managed Sharing (Apex Developer Guide, Winter '27)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_bulk_sharing_recalc.htm
    type: official-docs
    accessed: 2026-11-03
  - id: s4
    title: "Create Apex Sharing Reasons (Salesforce Help)"
    publisher: Salesforce
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=platform.security_apex_sharing_reasons.htm
    type: official-docs
    accessed: 2026-11-03
created: 2026-11-03
---

# Apex Managed Sharing

Apex managed sharing is the programmatic layer of the Salesforce sharing model. When ownership, the role hierarchy, sharing rules and manual sharing cannot express an application's access logic, developers grant access from Apex or the SOAP API by writing rows to a record's share object.[^s2] Unlike manual shares, these grants persist when the record owner changes or the owner is deactivated, and only users with the Modify All Data permission can add or change them.[^s1][^s2]

## How it works

Every shareable object has a share object: `AccountShare` for accounts, `ContactShare` for contacts and `MyCustomObject__Share` for a custom object. Detail records in a master-detail relationship have no share object of their own; they inherit access from the master.[^s1] A share row carries four key fields: the record being shared (`ParentId`), the recipient user or group (`UserOrGroupId`, which may be a public group, role group or territory group), the access level (`Read` or `Edit`; `All` is reserved for the platform) and the `RowCause`. `ParentId`, `UserOrGroupId` and `RowCause` cannot be updated after insert, so changing a grant means deleting and re-inserting the row.[^s1]

The `RowCause` is what makes sharing "Apex managed". Without a custom reason, rows inserted from code get the `Manual` cause and behave like user-managed sharing, which is deleted automatically when ownership changes.[^s1] An **Apex sharing reason** is a named cause (API name ending in `__c`, referenced as `Schema.Job__Share.rowCause.Recruiter__c`) whose label appears in the Reason column of the record's sharing view. Reasons also let one user or group hold several shares on the same record for different reasons, and make it easy to find and remove only the rows your code owns.[^s1][^s4] Reasons for custom objects are created from the object's Apex Sharing Reasons related list (a Salesforce Classic setup page) or via the Metadata API; the developer guide notes the Metadata or Tooling API route for standard objects.[^s1][^s4]

The typical implementation is an `after insert`/`after update` trigger that builds share rows from fields such as a recruiter or hiring-manager lookup and inserts them with partial success allowed, so one failed row does not roll back the batch.[^s1]

## Recalculation

When an object's organization-wide default changes, Salesforce recalculates sharing for all of its records and removes redundant grants.[^s3] To have Apex shares rebuilt, a developer writes a class implementing `Database.Batchable` that deletes the object's reason-based shares and re-inserts the correct ones, then associates it under the custom object's **Apex Sharing Recalculations** list. Associated classes run whenever the object's default access changes, an admin can start one from the object's detail page (useful after locking errors stopped code from granting access), and code can start one with `Database.executeBatch`. Running jobs are monitored from Setup's Apex Jobs page.[^s3]

## Limits and gotchas

- Up to 10 Apex sharing reasons can be created per custom object, and deleting a reason deletes all sharing on the object that uses it.[^s4]
- Creating a reason requires the Author Apex permission; adding, editing or deleting reason-based sharing requires Modify All Data.[^s4]
- The granted access must be more permissive than the organization-wide default; inserting a Read share on a Public Read Only object fails with an access-level error that well-written code treats as harmless. A recalculation class cannot be used when the default is already Public Read/Write.[^s1][^s3]
- Inserting a higher-access share for an existing user and cause upgrades the existing row rather than adding a second one.[^s1]
- Apex cannot grant access to unauthenticated guest users, and share objects are not available to Customer Community Plus users, so code running for them needs a `without sharing` context.[^s1]
- Share objects record managed, manual and Apex managed sharing, but not implicit access from defaults, the role hierarchy or View All/Modify All permissions.[^s1]

## When to use it (and when not)

Prefer declarative sharing rules when access can be expressed as owner- or field-criteria grants to groups or roles; Apex cannot create or test criteria-based sharing rules.[^s2] Reach for Apex managed sharing when access depends on relationships a rule cannot see, such as users named in lookup fields, team membership in a related object, or data held outside the record.[^s1][^s2] The cost is code to maintain, and a recalculation class that must be kept consistent with the trigger logic so grants can be rebuilt after default-access changes.[^s3]

## Connections

Apex managed sharing is a part of the broader **Salesforce sharing model** and the programmatic **alternative to sharing rules**; both only open access beyond the **organization-wide defaults**.[^s2] It **depends on Apex**, is usually driven by **Apex triggers**, and is rebuilt by **Batch Apex** recalculation classes, which tie it to **sharing recalculation** whenever defaults change.[^s3] Sharing reasons are **configured via** setup or the **Metadata API**,[^s4] and designing these grants is examined in the Sharing and Visibility Architect certification.

## Sources

[^s1]: Salesforce, "Sharing a Record Using Apex (Apex Developer Guide, Winter '27)". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_bulk_sharing_creating_with_apex.htm (accessed 2026-11-03)
[^s2]: Salesforce, "Understanding Sharing (Apex Developer Guide, Winter '27)". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/apexref/apex_bulk_sharing_understanding.htm (accessed 2026-11-03)
[^s3]: Salesforce, "Recalculating Apex Managed Sharing (Apex Developer Guide, Winter '27)". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_bulk_sharing_recalc.htm (accessed 2026-11-03)
[^s4]: Salesforce, "Create Apex Sharing Reasons (Salesforce Help)". https://help.salesforce.com/apex/HTViewHelpDoc?id=platform.security_apex_sharing_reasons.htm (accessed 2026-11-03)
