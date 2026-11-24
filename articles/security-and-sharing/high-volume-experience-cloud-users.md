---
id: kt:high-volume-experience-cloud-users
type: Concept
title: High-Volume Experience Cloud Users
aliases: [high-volume users, high-volume site users, high-volume community users, high-volume portal users, HVPU, high-volume community or site users]
domain: security-and-sharing
summary: >-
  The class of roleless, limited-access Experience Cloud users (Customer Community, High Volume Customer Portal,
  Authenticated Website and External Apps licenses) built for sites with thousands to millions of members, which
  bypass the role-based sharing model and instead reach records through account and contact lookups, sharing sets
  and share groups.
release: "Winter '27"
status: current
broader: [kt:salesforce-sharing-model, kt:experience-cloud]
related: [kt:customer-community-licenses, kt:sharing-sets, kt:share-groups, kt:implicit-sharing, kt:organization-wide-defaults, kt:partner-community-licenses]
relations:
  - {predicate: dependsOn, object: kt:sharing-sets}
  - {predicate: dependsOn, object: kt:share-groups}
  - {predicate: contrastsWith, object: kt:role-hierarchy}
  - {predicate: contrastsWith, object: kt:sharing-rules}
  - {predicate: consumedBy, object: kt:experience-cloud}
sources:
  - id: s1
    title: "About High-Volume Community or Site Users"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.networks_about_hvpu.htm&type=5
    type: official-docs
    accessed: 2026-11-24
  - id: s2
    title: "Platform Sharing Architecture"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/platform-sharing-architecture
    type: official-docs
    accessed: 2026-11-24
  - id: s3
    title: "Sharing Records with High-Volume Portals and Sites (Share CRM Data with Your Partners and Customers project)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/communities_share_crm_data/external_user_sharing
    type: official-learning
    accessed: 2026-11-24
  - id: s4
    title: "Salesforce Communities Licenses"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2014/02/salesforce-communities-licenses
    type: official-blog
    accessed: 2026-11-24
created: 2026-11-24
---

# High-Volume Experience Cloud Users

**High-volume users** are a category of authenticated Experience Cloud site members rather than a single license. Salesforce Help describes them as limited-access users aimed at orgs with thousands to millions of users.[^s1] The category covers the Customer Community, High Volume Customer Portal, Authenticated Website and External Apps license types.[^s1] What unites them is that none of these licenses supports roles, so their users sit outside the role-based sharing model that governs employees and partners.[^s2]

## Why the category exists

Role-based sharing is expensive at scale: every role and group membership feeds the sharing calculations the platform keeps for each record. Salesforce's sharing architecture guide explains that high-volume users skip the standard sharing model precisely because their licenses carry no role.[^s2] Instead, the guide describes a separate model that works by matching keys between the user's own account and contact and the Account and Contact lookups on records.[^s2] Removing users from the hierarchy is what lets a customer site grow to very large populations without dragging down sharing recalculation for everyone else.

The idea is old. A 2014 Salesforce Developers blog post, written for the Winter '14 Communities release, already called Customer Community the high-volume license and noted it had no access to sharing rules or the role hierarchy.[^s4] That post also presented sharing sets as the substitute, a design that still holds today.[^s4][^s3]

## What high-volume users can't do

Salesforce Help lists the restrictions, which also apply to records these users own:[^s1]

- No roles, and no membership in personal or public groups, so group-targeted sharing can't reach them.[^s1][^s2]
- They can't be included in owner-based sharing rules, can't share records manually, and their own records can't be shared manually.[^s1]
- They can't join account, opportunity or case teams, own accounts, or be assigned to territories.[^s1]
- They can't be added to Salesforce CRM Content libraries.[^s1]

## How they get access to records

Access comes from a handful of mechanisms that don't depend on roles:

- **Implicit access** to their own account and contact records, plus read access to the account they belong to.[^s1]
- **Organization-wide defaults** of Public Read Only or Public Read/Write, and parent access when an object is Controlled by Parent.[^s1]
- **Sharing sets**, which Trailhead calls containers of access mappings granted by profile instead of by role or public group.[^s3] A mapping matches a lookup on the target record, such as a case's account, to the user's account or contact, directly or through an indirect path like an asset related to a case.[^s3]
- **Share groups**, which work the other way round, opening records the high-volume users own to other users.[^s2][^s1]

Sharing sets have their own constraints. Trailhead notes that objects whose default is Public Read/Write, and custom objects with no account or contact lookup, can't be selected.[^s3] A data model meant for a high-volume site therefore needs account or contact lookups on every object customers must see.

## Design guidance

Choose a high-volume license when a site has a large, mostly self-service audience whose access follows clear ownership: a customer sees their own cases, orders or assets through their account or contact.[^s2][^s3] Choose a role-based license, such as Customer Community Plus or Partner Community, when external users need role hierarchy, sharing rules or group membership, for example to delegate within a partner company.[^s4][^s2] Because these users can't be public group members, the architecture guide's list of what public groups can contain covers portal roles and partner users but not high-volume licenses, a useful check when reviewing a sharing design.[^s2]

Gotchas follow from the model. Any requirement phrased as "share this record with that customer's colleague" needs a lookup path or a share group, not a sharing rule.[^s1][^s3] Records that a high-volume user creates are hard for others to see unless share groups are activated.[^s1]

## Connections

High-volume users are a sub-case of the **Salesforce sharing model** inside **Experience Cloud**, and they **contrast with** the **role hierarchy** and **sharing rules**, neither of which applies to them.[^s2][^s1] They **depend on** **sharing sets** for access to records and on **share groups** for access to the records they own.[^s3][^s1] **Customer Community licenses** are the most common high-volume license, while **Partner Community licenses** illustrate the role-based alternative.[^s4] **Implicit sharing** and **organization-wide defaults** supply the rest of their baseline access.[^s1]

## Sources
[^s1]: Salesforce Help, "About High-Volume Community or Site Users". https://help.salesforce.com/s/articleView?language=en_US&id=platform.networks_about_hvpu.htm&type=5 (accessed 2026-11-24)
[^s2]: Salesforce Architects, "Platform Sharing Architecture". https://architect.salesforce.com/fundamentals/platform-sharing-architecture (accessed 2026-11-24)
[^s3]: Trailhead, "Sharing Records with High-Volume Portals and Sites". https://trailhead.salesforce.com/content/learn/projects/communities_share_crm_data/external_user_sharing (accessed 2026-11-24)
[^s4]: Salesforce Developers Blog, "Salesforce Communities Licenses" (Winter '14). https://developer.salesforce.com/blogs/2014/02/salesforce-communities-licenses (accessed 2026-11-24)
