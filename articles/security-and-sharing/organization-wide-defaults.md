---
id: kt:organization-wide-defaults
type: SecurityControl
title: Organization-Wide Defaults
aliases: [OWD, org-wide defaults, organization-wide sharing defaults, default internal access, default external access, external organization-wide defaults]
domain: security-and-sharing
summary: >-
  The per-object baseline of record access in a Salesforce org — Private, Public Read Only, Public Read/Write,
  Controlled by Parent and similar levels, set separately for internal and external users — that every other
  sharing mechanism can only open up, never restrict further.
release: "Winter '27"
status: current
broader: [kt:salesforce-sharing-model]
related: [kt:role-hierarchy, kt:sharing-rules, kt:lookup-vs-master-detail, kt:experience-cloud, kt:data-skew]
relations:
  - {predicate: causes, object: kt:sharing-recalculation}
  - {predicate: coveredBy, object: kt:sharing-and-visibility-architect-certification}
sources:
  - id: s1
    title: "Control Access to Records (Data Security module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data_security/data_security_records
    type: official-learning
    accessed: 2026-11-01
  - id: s2
    title: "Set External Organization-Wide Defaults (Share CRM Data with Your Partners project)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/communities_share_crm_data/set_external_owd
    type: official-learning
    accessed: 2026-11-01
  - id: s3
    title: "Tips and Hints for Sharing Data"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.salesforce_sharing_cheatsheet.meta/salesforce_sharing_cheatsheet/sharing_cheatsheet.htm
    type: official-docs
    accessed: 2026-11-01
  - id: s4
    title: "Platform Sharing Architecture"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/platform-sharing-architecture
    type: official-docs
    accessed: 2026-11-01
  - id: s5
    title: "Defer Sharing Calculations (tip sheet)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/242/latest/en-us/sfdc/pdf/salesforce_defer_sharing_tipsheet.pdf
    type: official-docs
    accessed: 2026-11-01
created: 2026-11-01
---

# Organization-Wide Defaults

Organization-wide defaults (OWD) define, object by object, how much access a user has to records they do not own. They are the floor of the record-level security model: an admin sets each object to the level the most restricted user should have, and then uses the role hierarchy, sharing rules and manual sharing to widen access for everyone else.[^s1] OWD never grants more than a user's object permissions allow; object permissions decide whether a user can touch an object at all, and OWD then narrows access to the records within it that the user doesn't own.[^s1]

## Access levels

The common settings are Private (only the owner and users above them in the role hierarchy can view, edit and report on a record), Public Read Only (everyone can view and report, only the owner and their hierarchy can edit) and Public Read/Write (everyone can view, edit and report).[^s1] Some standard objects have extra levels: cases and leads can be Public Read/Write/Transfer, which also lets all users transfer ownership, and campaigns can be Public Full Access, which adds delete and transfer.[^s3] Detail records on the child side of a master-detail relationship have no OWD of their own; they are set to Controlled by Parent, so access to the detail follows access to its master.[^s1]

Settings can be mixed per object. A typical pattern is Public Read/Write on accounts with Private opportunities, so reps collaborate on customer data while keeping their own pipeline hidden from peers.[^s3] Admins edit all of this in Setup under Sharing Settings, in the Organization-Wide Defaults section.[^s3]

## Choosing the default

Trailhead frames the choice as three questions per object: who is the most restricted user, are there records that user must not see (pick Private), and are there records they may see but must not edit (pick Public Read Only).[^s1] Salesforce's architecture guidance gives the same rule in short form: lock data down to the most restrictive level and open it selectively with other sharing tools.[^s4] The order matters because sharing rules and the hierarchy only ever add access; nothing layered above OWD can take away what the default already gives.[^s1]

For custom objects that aren't Controlled by Parent, the OWD screen also holds the Grant Access Using Hierarchies checkbox. It is selected by default; clearing it stops managers from inheriting their subordinates' access, which suits highly confidential data that should be visible only to the owner and explicitly shared groups.[^s4][^s1]

## Internal vs. external defaults

Each supported object carries two values, Default Internal Access and Default External Access, so partner and customer site users can get a tighter baseline than employees, such as internal users seeing all opportunities while partners see only their own.[^s2] The external value can never be more permissive than the internal one.[^s2] External defaults are available for accounts (with their contracts and assets), assets, cases, contacts, individuals, opportunities, orders, users and custom objects.[^s2] Salesforce recommends setting every external default to Private, and an object's reports and dashboards can be exposed to external users only when its external default is Private.[^s2] With secure guest user record access enabled, guest users aren't treated as external users; their defaults are fixed at Private for all objects, and only sharing rules can open access to them.[^s2]

## Limits and gotchas

Saving an OWD change triggers a sharing recalculation.[^s1] On large data volumes that can take a long time, so Salesforce advises testing the change in a sandbox first to measure its duration.[^s4] Changing the default sharing model is one of the events that starts sharing rule calculation, and the admin is emailed only when it completes; the tip sheet suggests scheduling such changes in a maintenance window.[^s5] Orgs making bulk changes can use Defer Sharing Calculations to suspend sharing rule calculation and recalculate once at the end, but the permission is off by default and Salesforce must enable it.[^s5] OWD choices also interact with ownership and parent-child skew: Salesforce suggests keeping ownership near 1:10,000 or lower, and not giving a role to a user who owns more than 10,000 records.[^s4]

## Connections

OWD is the base layer of the **Salesforce sharing model**, with the **role hierarchy** and **sharing rules** opening access above it.[^s1] Controlled by Parent ties OWD to the master-detail side of **lookup vs. master-detail**.[^s1] External defaults are what scope partner and customer users in **Experience Cloud** sites.[^s2] Every change to OWD causes **sharing recalculation**, whose cost grows with **data skew** and data volume.[^s4][^s5] Designing OWD is core material for the **Sharing and Visibility Architect certification**.[^s4]

## Sources

[^s1]: Trailhead, "Control Access to Records (Data Security module)". https://trailhead.salesforce.com/content/learn/modules/data_security/data_security_records (accessed 2026-11-01)
[^s2]: Trailhead, "Set External Organization-Wide Defaults". https://trailhead.salesforce.com/content/learn/projects/communities_share_crm_data/set_external_owd (accessed 2026-11-01)
[^s3]: Salesforce, "Tips and Hints for Sharing Data". https://developer.salesforce.com/docs/atlas.en-us.salesforce_sharing_cheatsheet.meta/salesforce_sharing_cheatsheet/sharing_cheatsheet.htm (accessed 2026-11-01)
[^s4]: Salesforce Architects, "Platform Sharing Architecture". https://architect.salesforce.com/fundamentals/platform-sharing-architecture (accessed 2026-11-01)
[^s5]: Salesforce, "Defer Sharing Calculations" tip sheet. https://resources.docs.salesforce.com/242/latest/en-us/sfdc/pdf/salesforce_defer_sharing_tipsheet.pdf (accessed 2026-11-01)
