---
id: kt:share-groups
type: Feature
title: Share Groups
aliases: [share group, Experience Cloud share groups, share group settings, high-volume user share groups]
domain: security-and-sharing
summary: >-
  An Experience Cloud sharing mechanism, activated per sharing set, that shares records owned by roleless
  high-volume site users (such as Customer Community license holders) with chosen internal users and with
  external users from the same parent account, since those owners can't use roles, groups or manual sharing.
release: "Winter '27"
status: current
broader: [kt:salesforce-sharing-model, kt:experience-cloud]
related: [kt:customer-community-licenses, kt:implicit-sharing, kt:role-hierarchy, kt:high-volume-experience-cloud-users]
relations:
  - {predicate: dependsOn, object: kt:sharing-sets}
  - {predicate: contrastsWith, object: kt:public-groups}
  - {predicate: consumedBy, object: kt:experience-cloud}
  - {predicate: alternativeTo, object: kt:guest-user-sharing-rules}
sources:
  - id: s1
    title: "Use Share Groups to Share Records Owned by High-Volume Experience Cloud Site Users"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.networks_sharing_light_users.htm&type=5
    type: official-docs
    accessed: 2026-11-22
  - id: s2
    title: "About High-Volume Community or Site Users"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.networks_about_hvpu.htm&type=5
    type: official-docs
    accessed: 2026-11-22
  - id: s3
    title: "Create a Sharing Set for Experience Cloud Site Users"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.networks_setting_light_users.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-22
  - id: s4
    title: "Use Site-Specific Sharing (Share CRM Data with Your Partners and Customers project)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/communities_share_crm_data/external_user_sharing
    type: official-learning
    accessed: 2026-11-22
created: 2026-11-22
---

# Share Groups

A **share group** opens up records that are *owned by* high-volume Experience Cloud site users to other authenticated users: chosen internal users, and external users who belong to the same parent account as the owner.[^s1] It exists because high-volume users sit outside the normal sharing machinery. They have no role, so the platform skips role-hierarchy calculations for them, which is what lets an org scale to thousands or millions of external users.[^s2] The price is that the records they create are otherwise hard to share with anyone.

## Why high-volume users need it

High-volume users are contacts enabled for a site and given a high-volume license such as Customer Community, High Volume Customer Portal, Authenticated Website or External Apps.[^s2] Salesforce lists what they can't take part in:[^s2]

- They can't be members of personal or public groups, so sharing rules can't target them.[^s2]
- Records they own can't be shared manually, and they can't manually share records themselves.[^s2]
- They can't be on account, opportunity or case teams, can't own accounts and can't be assigned to territories.[^s2]

Their access *to* other records comes from **sharing sets**, which grant access based on the account or contact linked to the user, plus implicit sharing on their own account and contact.[^s2][^s3] Share groups handle the opposite direction: access *to records they own*.[^s2]

## How it works

A share group is not a standalone object. Each one is tied to a sharing set and applies across all Experience Cloud sites in the org.[^s1] An admin with Customize Application opens Digital Experiences settings, clicks the sharing set name, goes to the Share Group Settings tab and clicks **Activate**.[^s1] Activation runs in the background and Salesforce emails the admin when it completes.[^s1]

Members are then added with **Edit**: choose a member type, search, move users from Available Members and save.[^s1] Eligible members are internal users in the org and external users from the same parent account as the high-volume owner.[^s1] Those members can then reach records owned by the high-volume users.[^s1]

## Limits and gotchas

- **No guest users.** Share groups can't share high-volume-owned records with guest users; use guest user sharing rules for that.[^s1]
- **Deactivation is total.** Deactivating removes every other user's access to the high-volume-owned records, and no email confirms when it finishes.[^s1]
- **License fit.** Share groups aren't available to users on Customer Community Plus or Partner Community licenses, which have roles and use standard sharing.[^s3]
- **Set up the sharing set first.** Salesforce frames share groups as the step after creating a sharing set, and one sharing set is allowed per profile.[^s3]
- **Editions.** The feature is available in Enterprise, Performance, Unlimited and Developer editions.[^s1]

## When to use it (and when not)

Use share groups when customers on a high-volume license create records, such as cases or custom request objects, that service agents or colleagues at the same customer account must see.[^s1][^s4] If external users need richer collaboration (role-based sharing, sharing rules, record sharing with partners), a role-bearing license such as Customer Community Plus is the alternative, since it works with the standard model.[^s3] For anonymous visitors, guest user sharing rules are the only route.[^s1]

## Connections

Share groups are part of the **Salesforce sharing model** as applied to **Experience Cloud**, and they **depend on** **sharing sets**, which Trailhead describes as profile-based containers of access mappings rather than role- or group-based rules.[^s4][^s3] They **contrast with** **public groups**: high-volume users can't be public group members, so a share group stands in as the way to widen access to their records.[^s2][^s1] They matter mainly for **Customer Community licenses**, which avoid the **role hierarchy**, and they complement the **implicit sharing** these users get on their own account and contact.[^s2] **Guest user sharing rules** are the **alternative** for unauthenticated visitors.[^s1]

## Sources
[^s1]: Salesforce Help, "Use Share Groups to Share Records Owned by High-Volume Experience Cloud Site Users". https://help.salesforce.com/s/articleView?language=en_US&id=sf.networks_sharing_light_users.htm&type=5 (accessed 2026-11-22)
[^s2]: Salesforce Help, "About High-Volume Community or Site Users". https://help.salesforce.com/s/articleView?language=en_US&id=platform.networks_about_hvpu.htm&type=5 (accessed 2026-11-22)
[^s3]: Salesforce Help, "Create a Sharing Set for Experience Cloud Site Users". https://help.salesforce.com/s/articleView?id=sf.networks_setting_light_users.htm&language=en_US&type=5 (accessed 2026-11-22)
[^s4]: Trailhead, "Use Site-Specific Sharing". https://trailhead.salesforce.com/content/learn/projects/communities_share_crm_data/external_user_sharing (accessed 2026-11-22)
