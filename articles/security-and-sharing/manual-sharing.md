---
id: kt:manual-sharing
type: SecurityControl
title: Manual Sharing
aliases: [user managed sharing, user-managed sharing, manual shares, manual record sharing, Sharing button]
domain: security-and-sharing
summary: >-
  The user-managed layer of Salesforce record access, in which a record owner or a suitably privileged user grants
  specific users, roles or groups Read Only or Read/Write access to one individual record, stored as a share row
  with the Manual row cause.
release: "Winter '27"
status: current
broader: [kt:salesforce-sharing-model]
related: [kt:organization-wide-defaults, kt:role-hierarchy, kt:public-groups, kt:account-teams, kt:implicit-sharing]
relations:
  - {predicate: alternativeTo, object: kt:sharing-rules}
  - {predicate: contrastsWith, object: kt:apex-managed-sharing}
  - {predicate: dependsOn, object: kt:organization-wide-defaults}
sources:
  - id: s1
    title: "Understanding Sharing (Apex Developer Guide, Winter '27)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/apexref/apex_bulk_sharing_understanding.htm
    type: official-docs
    accessed: 2026-11-25
  - id: s2
    title: "Sharing a Record Using Apex (Apex Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_bulk_sharing_creating_with_apex.html
    type: official-docs
    accessed: 2026-11-25
  - id: s3
    title: "Platform Sharing Architecture (Salesforce Architects Fundamentals)"
    publisher: Salesforce
    url: https://architect.salesforce.com/fundamentals/platform-sharing-architecture
    type: official-docs
    accessed: 2026-11-25
  - id: s4
    title: "Sample Scenarios (Record-Level Access: Under the Hood)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/salesforce-record-access-under-the-hood/guide/uth-examples.html
    type: official-docs
    accessed: 2026-11-25
  - id: s5
    title: "Learn MOAR in Summer '21 with Record Sharing Updates"
    publisher: Salesforce Admins
    url: https://admin.salesforce.com/blog/2021/learn-moar-in-summer-21-with-record-sharing
    type: official-blog
    accessed: 2026-11-25
created: 2026-11-25
---

# Manual Sharing

Manual sharing is the record-by-record exception in the Salesforce sharing model. Where organization-wide defaults, the role hierarchy and sharing rules are calculated by the platform, a manual share is created by a person: the record owner, or another user with enough privilege, picks one record and grants a named user, group or role extra access to it.[^s1][^s3] The Apex Developer Guide classes it as "user managed" sharing, as opposed to platform-managed sharing and Apex managed sharing.[^s1]

## How it works

Who can share. The owner of a record, any user with Full Access to it, users with the Modify All Records permission on the object and users with Modify All Data can all create manual shares.[^s1] The architecture fundamentals guide frames it as owners or users with adequate privileges, such as system administrators, granting read or edit access to the current record.[^s3]

What it grants. A manual share opens Read Only or Read/Write access; Full Access cannot be handed out this way, because only the owner and users above the owner in the role hierarchy hold it, and Full Access is reachable only through managed sharing.[^s1] Recipients can be users, public groups or roles, which makes manual sharing a way to give one-off access to a whole team without writing a rule.[^s3]

Where it is stored. Each grant becomes a row in the object's share table (for example `AccountShare`, `ContactShare` or `MyObject__c__Share`) with `RowCause` set to `Manual`, shown in the UI as the reason "Manual Sharing".[^s1][^s2] The Under the Hood scenarios show a manual share from one rep to a colleague on an account adding a single row to the Account sharing table; team and programmatic grants create rows the same way, distinguished only by row cause.[^s4] Detail records in a master-detail relationship have no share object of their own, so they cannot be shared manually apart from their parent.[^s2]

User interface. Since Summer '21, Lightning Experience users can choose Sharing from the action menu on a record page, and a companion Sharing Hierarchy option shows who has access to the record and why.[^s5] Manual-cause shares, including ones created programmatically, can be edited or removed from the same Share action.[^s3]

Code. Apex or the API can insert a share row; when no row cause is given it defaults to `Manual`, so such code-created shares behave exactly like UI-created ones.[^s2] The `ParentId`, `RowCause` and `UserOrGroupId` fields cannot be changed after insert, and inserting a higher-access share for an existing user updates the existing row rather than adding a second one.[^s2]

## Limits and gotchas

- Ownership changes wipe manual shares: when a record's owner changes, rows with the Manual cause are deleted and recipients lose access.[^s1][^s4]
- The architecture guide notes an org setting, "Keep manual shares when transferring records", that preserves manual shares across ownership transfer when enabled.[^s3]
- A manual share is removed, or rejected on insert, if it does not grant more than the object's OWD; a custom object whose OWD is Public Read/Write cannot take share rows written this way.[^s1][^s2]
- Guest users cannot be granted record access through Apex share rows, and Customer Community Plus users cannot see share objects, although other users can still share records with them.[^s2]
- Because access lives in individual rows, every manual share adds to sharing table volume and to what must be reprocessed when owners change, which the scenarios illustrate step by step.[^s4]

## When to use it (and when not)

Manual sharing suits genuinely ad hoc access: covering a colleague's absence, pulling a specialist onto one deal, or or letting a colleague see one account the way the Under the Hood scenarios do.[^s3][^s4] When the same grant repeats for a predictable group, a sharing rule is easier to govern; when access must survive ownership changes or follow data such as a lookup to a user, Apex managed sharing with a custom sharing reason is the durable alternative, since those rows are kept when the owner changes and can be maintained only by users with Modify All Data.[^s1][^s2] For accounts, opportunities and cases, record teams offer a structured, per-record alternative that is also limited to owners, users above them in the hierarchy and administrators.[^s3]

## Connections

Manual sharing is one layer of the broader **Salesforce sharing model**, and it **depends on** restrictive **organization-wide defaults**, because a grant that does not exceed the OWD is discarded.[^s1] It is the ad hoc **alternative to sharing rules**, and it **contrasts with Apex managed sharing**: both write share rows, but manual rows carry the Manual cause and vanish on owner change, while Apex sharing reasons persist.[^s1][^s2] Recipients are often **public groups** or roles from the **role hierarchy**, and users above the owner in that hierarchy already hold access without a share.[^s1][^s3] **Account teams** are the structured per-record counterpart, while **implicit sharing** is the platform-derived access between accounts and their child contacts, opportunities and cases that no manual grant can alter.[^s1][^s3]

## Sources

[^s1]: Salesforce, "Understanding Sharing (Apex Developer Guide, Winter '27)". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/apexref/apex_bulk_sharing_understanding.htm (accessed 2026-11-25)
[^s2]: Salesforce, "Sharing a Record Using Apex (Apex Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_bulk_sharing_creating_with_apex.html (accessed 2026-11-25)
[^s3]: Salesforce, "Platform Sharing Architecture (Salesforce Architects Fundamentals)". https://architect.salesforce.com/fundamentals/platform-sharing-architecture (accessed 2026-11-25)
[^s4]: Salesforce, "Sample Scenarios (Record-Level Access: Under the Hood)". https://developer.salesforce.com/docs/platform/salesforce-record-access-under-the-hood/guide/uth-examples.html (accessed 2026-11-25)
[^s5]: Salesforce Admins, "Learn MOAR in Summer '21 with Record Sharing Updates". https://admin.salesforce.com/blog/2021/learn-moar-in-summer-21-with-record-sharing (accessed 2026-11-25)
