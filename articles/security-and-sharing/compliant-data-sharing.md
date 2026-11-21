---
id: kt:compliant-data-sharing
type: SecurityControl
title: Compliant Data Sharing
aliases: [CDS, participant roles, participant-based sharing, ethical wall sharing]
domain: security-and-sharing
summary: >-
  An Industries sharing mechanism, best known from Financial Services Cloud, that grants record access by
  assigning users or participant groups to a record through participant roles, each carrying a Read-Only or
  Read/Write access level, so admins can enforce ethical walls without sharing code.
release: "Winter '27"
status: current
broader: [kt:salesforce-sharing-model]
related: [kt:organization-wide-defaults, kt:role-hierarchy, kt:public-groups, kt:field-level-security, kt:public-sector-solutions]
relations:
  - {predicate: partOf, object: kt:financial-services-cloud}
  - {predicate: dependsOn, object: kt:organization-wide-defaults}
  - {predicate: alternativeTo, object: kt:apex-managed-sharing}
  - {predicate: alternativeTo, object: kt:sharing-rules}
  - {predicate: configuredVia, object: kt:permission-sets}
sources:
  - id: s1
    title: "Compliant Data Sharing (Salesforce Help, Winter '27)"
    publisher: Salesforce
    url: https://help.salesforce.com/s/articleView?id=ind.fsc_admin_cds.htm&type=5
    type: official-docs
    accessed: 2026-11-21
  - id: s2
    title: "Control Who Sees What with Compliant Data Sharing (Salesforce Help, Winter '27)"
    publisher: Salesforce
    url: https://help.salesforce.com/s/articleView?id=ind.fsc_cds_admin_overview.htm&type=5
    type: official-docs
    accessed: 2026-11-21
  - id: s3
    title: "Grant User Access to Objects and Participant Objects and Fields in Compliant Data Sharing (Salesforce Help, Winter '27)"
    publisher: Salesforce
    url: https://help.salesforce.com/s/articleView?id=ind.fsc_admin_cds_grant_access_to_objects.htm&type=5
    type: official-docs
    accessed: 2026-11-21
  - id: s4
    title: "Compliant Data Sharing in Financial Services Explained (Trailhead)"
    publisher: Salesforce
    url: https://trailhead.salesforce.com/content/learn/modules/compliant-data-sharing-in-financial-services-cloud/get-started-with-compliant-data-sharing
    type: official-learning
    accessed: 2026-11-21
  - id: s5
    title: "Learn How to Set Up Compliant Data Sharing for Your Organization (Trailhead)"
    publisher: Salesforce
    url: https://trailhead.salesforce.com/content/learn/modules/compliant-data-sharing-in-financial-services-cloud/set-up-compliant-data-sharing
    type: official-learning
    accessed: 2026-11-21
  - id: s6
    title: "Create and Manage Participant Roles and Groups Effectively (Trailhead)"
    publisher: Salesforce
    url: https://trailhead.salesforce.com/content/learn/modules/compliant-data-sharing-in-financial-services-cloud/set-up-participants
    type: official-learning
    accessed: 2026-11-21
created: 2026-11-21
---

# Compliant Data Sharing

Compliant Data Sharing (CDS) lets admins and compliance managers configure fine-grained record access without writing sharing code.[^s1] It was built for financial institutions that must keep material non-public information behind ethical walls, for example separating an investment-banking deal team from a capital-markets desk at the same firm.[^s4] Instead of deriving access from ownership or criteria, CDS grants it explicitly: a user or a participant group is attached to a record in a named role, and that role carries the access level.[^s2][^s4] Trailhead notes that Financial Services Cloud is now branded Agentforce Financial Services; in Winter '27 Help, CDS is listed for Financial Services Cloud (Professional, Enterprise and Unlimited editions), Nonprofit Cloud and Public Sector Solutions, in Lightning Experience.[^s1][^s4]

## How it works

The data model is one setup object plus junction objects. A **Participant Role** is a setup record that names a role for one parent object and its default access level, Read-Only or Read/Write. **Account Participant** and **Opportunity Participant** are standard junctions that link a user or participant group, a participant role and a record; custom objects use the generic **Participant** object.[^s1] Participant objects are detail records in a master-detail relationship to their parent, so access to them follows access to the parent record.[^s3][^s5]

When a participant is added, the platform writes a row to the parent's share table only if the role's access level exceeds the object's organization-wide default. Help's example: with Account at Public Read/Write, a Read/Write role creates no share row; switching Account to Private creates it, and switching back removes it, because OWD changes also re-evaluate existing participant records.[^s2] **Participant groups** let admins share with a whole team that plays the same role. Groups can hold users or other groups nested up to five levels, and when a user reaches a record through several groups with different levels, the most permissive level wins.[^s6]

## Setting it up

Setup follows a fixed sequence:[^s5][^s6]

1. Set the parent object's OWD to Private or Public Read-Only; under Public Read/Write, CDS has no effect.[^s5]
2. In Object Enablement Settings, turn on Compliant Data Sharing for CRM users on each object (Help lists Account, Opportunity and custom objects; some objects also support Experience Cloud users).[^s1][^s5]
3. Create participant roles from Setup > Participant Roles, choosing the parent object and default access level.[^s6]
4. Grant permissions and field access, then add participant related lists and the Sharing button to page layouts.[^s1][^s3]

Users who configure participant groups need the **Configure Compliant Data Sharing** permission, and group members need **Use Compliant Data Sharing**. To manage participant records, a profile needs Read, Create, Edit and Delete on the parent object plus Read (and Edit, to activate participants) on the participant object's Active field.[^s3]

## Limits and gotchas

The participant-setup unit on Trailhead gives these limits:[^s6]

- A participant role applies to exactly one object, and its parent object can't be changed after creation.[^s6]
- An object can have at most 10 active participant roles, and only active roles can be assigned.[^s6]
- A parent record can have at most 100 participant groups.[^s6]
- By default, a user in a participant group can't be deactivated until removed; an optional setting deactivates them and keeps inactive participant records.[^s6]

Other behaviours to plan for: disabling CDS on an object first requires deleting all of its participant roles.[^s5] Opportunity participants can't be added to a Private opportunity, and marking an opportunity Private deletes its share rows but leaves participant records behind; making it non-private again doesn't recreate those rows, so participants must be deleted and re-added.[^s2] Tasks and events inherit sharing from their parent record, so CDS doesn't govern them, and Trailhead suggests Interaction Summaries for confidential meeting notes.[^s4] Role-hierarchy access is on by default for some objects; Trailhead recommends disabling it where managers must not see their reports' walled-off deals.[^s4] Users above the record owner in the hierarchy, and non-owners given edit access through CDS, can share the record just as owners can.[^s2]

## When to use it (and when not)

Use CDS when access depends on each person's role on each record (deal team, compliance reviewer, relationship manager) and must be auditable by compliance staff rather than buried in Apex. Criteria-based sharing rules suit access that follows record attributes, and Apex managed sharing suits logic too complex for declarative tools. CDS sits between them, with explicit per-record grants managed declaratively.[^s1][^s4]

## Connections

CDS is a **broader**-linked extension of `kt:salesforce-sharing-model` and is **part of** `kt:financial-services-cloud`, although Help also lists it for `kt:public-sector-solutions`.[^s1] It **depends on** `kt:organization-wide-defaults`, because it can only open access beyond a Private or Public Read-Only baseline.[^s2][^s5] It is an **alternative to** `kt:sharing-rules` and `kt:apex-managed-sharing` for granting record-level access.[^s1][^s4] Its permissions are **configured via** `kt:permission-sets`, field access to participant objects goes through `kt:field-level-security`, and participant groups play a role similar to `kt:public-groups`.[^s3][^s6] It is **related** to `kt:role-hierarchy`, whose default access may need to be turned off to keep ethical walls intact.[^s4]

## Sources

[^s1]: Salesforce, "Compliant Data Sharing" (Salesforce Help, Winter '27). https://help.salesforce.com/s/articleView?id=ind.fsc_admin_cds.htm&type=5 (accessed 2026-11-21)
[^s2]: Salesforce, "Control Who Sees What with Compliant Data Sharing" (Salesforce Help, Winter '27). https://help.salesforce.com/s/articleView?id=ind.fsc_cds_admin_overview.htm&type=5 (accessed 2026-11-21)
[^s3]: Salesforce, "Grant User Access to Objects and Participant Objects and Fields in Compliant Data Sharing" (Salesforce Help, Winter '27). https://help.salesforce.com/s/articleView?id=ind.fsc_admin_cds_grant_access_to_objects.htm&type=5 (accessed 2026-11-21)
[^s4]: Salesforce Trailhead, "Compliant Data Sharing in Financial Services Explained". https://trailhead.salesforce.com/content/learn/modules/compliant-data-sharing-in-financial-services-cloud/get-started-with-compliant-data-sharing (accessed 2026-11-21)
[^s5]: Salesforce Trailhead, "Learn How to Set Up Compliant Data Sharing for Your Organization". https://trailhead.salesforce.com/content/learn/modules/compliant-data-sharing-in-financial-services-cloud/set-up-compliant-data-sharing (accessed 2026-11-21)
[^s6]: Salesforce Trailhead, "Create and Manage Participant Roles and Groups Effectively". https://trailhead.salesforce.com/content/learn/modules/compliant-data-sharing-in-financial-services-cloud/set-up-participants (accessed 2026-11-21)
