---
id: kt:mixed-dml-error
type: Concept
title: Mixed DML Error
aliases: ["MIXED_DML_OPERATION", "mixed DML operation", "setup and non-setup object DML", "mixed DML"]
domain: development
summary: >-
  The Apex runtime error raised when one transaction performs DML on setup sObjects (such as User, UserRole, Group
  or PermissionSetAssignment) and on ordinary non-setup sObjects (such as Account); it is avoided by splitting the
  work into separate transactions, for example with a future or Queueable job, or with System.runAs in tests.
release: "Winter '27"
status: concept
broader: [kt:transaction-control, kt:apex]
related: [kt:future-methods, kt:queueable-apex, kt:apex-testing, kt:just-in-time-provisioning, kt:user-management]
relations:
  - {predicate: dependsOn, object: kt:salesforce-sharing-model}
  - {predicate: contrastsWith, object: kt:order-of-execution}
sources:
  - id: s1
    title: "Apex Developer Guide: sObjects That Can't Be Used Together in DML Operations"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexref/apex_dml_non_mix_sobjects.htm
    type: official-docs
    accessed: 2026-11-17
  - id: s2
    title: "Apex Developer Guide: Mixed DML Operations in Test Methods"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexref/apex_dml_non_mix_sobjects_test_methods.htm
    type: official-docs
    accessed: 2026-11-17
  - id: s3
    title: "Apex Developer Guide: Using the runAs Method"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_testing_tools_runas.htm
    type: official-docs
    accessed: 2026-11-17
created: 2026-11-17
---

# Mixed DML Error

The mixed DML error is what Apex throws when a single transaction changes both **setup objects** and **non-setup objects**. Setup objects are the sObjects whose changes affect who can see which records, so the platform will not let DML on them share a transaction with DML on ordinary business records such as Account or Contact.[^s1] The rule is documented in the Winter '27 (API 68.0) Apex Developer Guide, which also asks developers not to put more than one setup sObject in the same transaction, whether through DML or the Metadata API.[^s1] The error is common in triggers that provision users, in identity handlers, and above all in test classes that create a user and test data side by side.[^s2]

## Which objects count as setup objects

The guide lists the setup sObjects that can't be mixed with other DML, and it warns that the list isn't exhaustive.[^s1] The ones developers hit most often are:

- **User, UserRole and UserPackageLicense** for user records, role placement and package licensing.[^s1]
- **Group, GroupMember and QueueSObject** for public groups, queues and their members.[^s1]
- **PermissionSet, PermissionSetAssignment, ObjectPermissions, FieldPermissions and SetupEntityAccess** for access grants.[^s1]
- **Territory2, Territory2Model, UserTerritory2Association and related assignment-rule objects** for Enterprise Territory Management.[^s1]

Other listed objects include AuthSession, ContentWorkspace and ForecastingShare.[^s1] Setup sObjects also can't be used in test classes annotated `@IsTest(IsParallel=true)`.[^s1]

## Exceptions

Not every write to a setup object trips the error. Group records can be inserted or updated alongside other sObjects, though other DML operations on Group aren't allowed in that case.[^s1] For Apex saved at API version 15.0 or later, a User can be inserted with other sObjects when its `UserRoleId` is null.[^s1] A User update can also be mixed, provided the user isn't part of a Lightning Sync or Einstein Activity Capture configuration and none of these fields change: UserRoleId, IsActive, ForecastEnabled, IsPortalEnabled, Username or ProfileId.[^s1] Code saved at API 14.0 or earlier had looser rules for User and GroupMember, which is one reason old classes can behave differently from new ones.[^s1]

## Workarounds

The fix is always to move one side of the DML into a different transaction.[^s1]

- **Asynchronous Apex.** The documented pattern does the non-setup DML in the current method and hands the setup DML, for example inserting a User with a role, to an `@future` method.[^s1] Any asynchronous job works the same way, so a Queueable can carry the second half.[^s2]
- **Separate requests in Visualforce.** A custom controller can't mix the two kinds in one request or action, so the page needs separate actions, such as one button that saves an Account and another that creates the User.[^s1]
- **Tests.** Mixed DML is allowed in a test method when the DML sits inside `System.runAs` blocks, or when the test calls code that performs one kind of DML in an asynchronous job.[^s2] The runAs page confirms that wrapping setup-object DML in a runAs block avoids the error.[^s3]

## Limits and gotchas

`System.runAs` works only in test methods, so it is never a fix for production code.[^s3] Each runAs call counts toward the DML statements issued in the process, and runAs ignores user license limits, which is why tests can create users freely.[^s3] Validation for mixed DML is skipped during deployment, so a test can pass while deploying yet fail when run from the UI, and failure counts can differ between the two.[^s2] Because the split moves work into another transaction, the two halves no longer roll back together: if the asynchronous user creation fails, the Account written earlier stays committed, so design compensating logic or monitoring where consistency matters.[^s1][^s2]

## When it matters

Expect it whenever business logic and user administration meet: onboarding flows that create a Contact and its community User, handlers that update User fields from an identity assertion, or triggers that add records and also assign permission sets.[^s1] When the setup change can be deferred, prefer a Queueable for new code; when it must happen in the same user action, restructure the process into two steps.[^s1][^s2]

## Connections

The error is a rule about **transaction control**: it constrains what one Apex transaction may commit, so its broader nodes are **transaction control** and **Apex**.[^s1] It exists because setup objects change record access, which is why it depends on the **Salesforce sharing model**.[^s1] The standard escapes are **future methods** and **Queueable Apex**, and in test code the runAs technique described in **Apex testing**.[^s1][^s2][^s3] It surfaces in **just-in-time provisioning** handlers that touch both User and Contact or Account data, and in **user management** automation generally.[^s1] It contrasts with the **order of execution**, which sequences work inside one save, whereas the mixed DML rule forces work out into separate transactions.[^s1]

## Sources

[^s1]: Salesforce Developers, "Apex Developer Guide: sObjects That Can't Be Used Together in DML Operations". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexref/apex_dml_non_mix_sobjects.htm (accessed 2026-11-17)
[^s2]: Salesforce Developers, "Apex Developer Guide: Mixed DML Operations in Test Methods". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexref/apex_dml_non_mix_sobjects_test_methods.htm (accessed 2026-11-17)
[^s3]: Salesforce Developers, "Apex Developer Guide: Using the runAs Method". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_testing_tools_runas.htm (accessed 2026-11-17)
