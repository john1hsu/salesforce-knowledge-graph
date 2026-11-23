---
id: kt:sharing-sets
type: Feature
title: Sharing Sets
aliases: [sharing set, Experience Cloud sharing sets, high-volume user sharing sets, access mappings]
domain: security-and-sharing
summary: >-
  A profile-based Experience Cloud sharing mechanism that gives role-less high-volume site users (such as
  Customer Community license holders) access to records whose account or contact lookup matches the account
  or contact on the user's own record, defined through access mappings per object.
release: "Winter '27"
status: current
broader: [kt:salesforce-sharing-model, kt:experience-cloud]
related: [kt:customer-community-licenses, kt:implicit-sharing, kt:contacts-to-multiple-accounts, kt:organization-wide-defaults]
relations:
  - {predicate: enables, object: kt:share-groups}
  - {predicate: contrastsWith, object: kt:sharing-rules}
  - {predicate: contrastsWith, object: kt:role-hierarchy}
  - {predicate: dependsOn, object: kt:profiles}
sources:
  - id: s1
    title: "Create a Sharing Set for Experience Cloud Site Users"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000193861&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-23
  - id: s2
    title: "Differences Between User Sharing with Manual Sharing and Sharing Sets"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=security_sharing_users_manual_and_sets.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-23
  - id: s3
    title: "Use Site-Specific Sharing (Share CRM Data with Your Partners and Customers project)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/communities_share_crm_data/external_user_sharing
    type: official-learning
    accessed: 2026-11-23
  - id: s4
    title: "Platform Sharing Architecture"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/platform-sharing-architecture
    type: official-docs
    accessed: 2026-11-23
  - id: s5
    title: "Use Share Groups to Share Records Owned by High-Volume Experience Cloud Site Users"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.networks_sharing_light_users.htm&type=5
    type: official-docs
    accessed: 2026-11-23
created: 2026-11-23
---

# Sharing Sets

A **sharing set** gives Experience Cloud site users access to records that are tied to an account or contact matching the account or contact on the user's own record.[^s1] It is the main record-access tool for **high-volume** external users, the Customer Community, High Volume Customer Portal and Authenticated Website license types, which have no roles and so sit outside the role-hierarchy part of the sharing model.[^s4] Salesforce's architect guidance describes their access as a key match between the licensed user and Account or Contact lookups on the data, granted through sharing sets or share groups.[^s4]

## How it works

Where sharing rules target roles and public groups, sharing sets target **profiles**: Trailhead calls a sharing set "essentially a container of access mappings."[^s3] An admin with Customize Application creates one under Setup > Digital Experiences > Settings, gives it a label, picks the profiles whose users receive access and picks the objects to open up.[^s1][^s3]

For each object the admin clicks **Set Up** and defines an **access mapping**: a user field (an account or contact lookup on the user, such as the contact's account) and the matching lookup on the target object, plus an access level.[^s1][^s3] Both fields must point to an account or both to a contact.[^s1] Mappings can be direct, such as the account on a case, or indirect through a related record, such as the account on an asset related to the case.[^s3] When contacts are related to multiple accounts, a mapping can use the contact's related accounts so users reach records for every account they're linked to, provided those relationships are active.[^s1]

A sharing set applies across all sites the user belongs to, and the access is not extended to anyone above the user in a role hierarchy.[^s1] The feature runs in Enterprise, Performance, Unlimited and Developer editions, in both Lightning Experience and Salesforce Classic.[^s1]

A typical example: with the Case org-wide default set to Private, a sharing set for the Customer Community User profile maps the user's Account to the case's Account, so customers at the same company see each other's cases read-only.[^s3]

## Limits and gotchas

- **One per profile.** Each profile can be in only one sharing set, so all mappings for that profile's users live together.[^s1]
- **Excluded objects.** Objects whose org-wide default is Public Read/Write, and custom objects with no account or contact lookup, don't appear as choices.[^s1][^s3]
- **Access levels.** Mappings grant Read Only or Read/Write; if the object's default is Public Read Only, only Read/Write is offered.[^s1]
- **No automatic parent access.** Sharing contacts, cases or opportunities doesn't grant the parent account; add Account to the sharing set to share it.[^s1]
- **Unconfigured objects stay closed.** Until an object is set up in the sharing set, high-volume users have limited or no access to its records.[^s1]
- **Special objects.** Knowledge needs the Knowledge standard sharing org preference, and Lead must be enabled through Salesforce Customer Support.[^s1]
- **Records they own are separate.** Sharing sets control what high-volume users can see, not who sees their records; share groups handle that.[^s1][^s5]

## When to use it (and when not)

Use sharing sets when large numbers of external users need to see records that belong to their own company or person record, such as cases, orders, assets or custom objects with an account lookup.[^s1][^s3] They scale because no role or group membership has to be calculated per user.[^s4] They also cover user records: high-volume users can't receive manual shares of other users, so a sharing set is how they get access to other user records.[^s2]

If external users need role-based sharing, sharing rules, or access defined by criteria other than an account or contact match, a role-bearing license such as Customer Community Plus or Partner Community fits better, since it uses the standard sharing model.[^s4][^s5]

## Connections

Sharing sets are part of the **Salesforce sharing model** as applied to **Experience Cloud**, and they are the access path for **Customer Community licenses**.[^s4][^s1] They **contrast with sharing rules**, which are built on roles and public groups, and with the **role hierarchy**, which high-volume users don't use.[^s3][^s4] They **depend on profiles**, since each set is assigned to profiles rather than roles.[^s3] **Organization-wide defaults** decide which objects can be added: a Public Read/Write object needs no sharing set.[^s1] They work alongside **implicit sharing** and can follow **contacts related to multiple accounts**.[^s4][^s1] Each sharing set **enables** a **share group**, which shares records owned by high-volume users back to internal users and colleagues.[^s5][^s1]

## Sources
[^s1]: Salesforce Help, "Create a Sharing Set for Experience Cloud Site Users". https://help.salesforce.com/s/articleView?id=000193861&language=en_US&type=1 (accessed 2026-11-23)
[^s2]: Salesforce Help, "Differences Between User Sharing with Manual Sharing and Sharing Sets". https://help.salesforce.com/s/articleView?id=security_sharing_users_manual_and_sets.htm&language=en_US&type=5 (accessed 2026-11-23)
[^s3]: Trailhead, "Use Site-Specific Sharing". https://trailhead.salesforce.com/content/learn/projects/communities_share_crm_data/external_user_sharing (accessed 2026-11-23)
[^s4]: Salesforce Architects, "Platform Sharing Architecture". https://architect.salesforce.com/fundamentals/platform-sharing-architecture (accessed 2026-11-23)
[^s5]: Salesforce Help, "Use Share Groups to Share Records Owned by High-Volume Experience Cloud Site Users". https://help.salesforce.com/s/articleView?language=en_US&id=sf.networks_sharing_light_users.htm&type=5 (accessed 2026-11-23)
