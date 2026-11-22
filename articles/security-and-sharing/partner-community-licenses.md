---
id: kt:partner-community-licenses
type: Product
title: Partner Community Licenses
aliases: [Partner Community license, Partner Community Login license, Experience Cloud partner license, PRM partner user license]
domain: security-and-sharing
summary: >-
  The Experience Cloud user license for business-to-business partner users such as resellers and distributors: role-based
  external users who work shared CRM records like leads and opportunities through account roles under the partner account,
  sharing rules and the internal role hierarchy, typically in a partner relationship management (PRM) portal.
release: "Winter '27"
status: current
broader: [kt:user-licenses, kt:experience-cloud]
related: [kt:role-hierarchy, kt:sharing-rules, kt:public-groups, kt:assignment-rules, kt:licensing-strategy, kt:person-accounts]
relations:
  - {predicate: contrastsWith, object: kt:customer-community-licenses}
  - {predicate: consumedBy, object: kt:experience-cloud}
  - {predicate: dependsOn, object: kt:role-hierarchy}
  - {predicate: consumedBy, object: kt:partner-relationship-management}
sources:
  - id: s1
    title: "Set Up Account Roles and the Role Hierarchy (Share CRM Data with Your Partners)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/communities_share_crm_data/account_roles_hierarchy
    type: official-learning
    accessed: 2026-11-22
  - id: s2
    title: "Create a Partner Portal, Enable Partner Account and Users, and Add Members"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/communities_share_crm_data/create_portal_and_users
    type: official-learning
    accessed: 2026-11-22
  - id: s3
    title: "Use Sharing Rules for External Users"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/communities_share_crm_data/sharing_rules
    type: official-learning
    accessed: 2026-11-22
  - id: s4
    title: "Delegate Site Administration to an External User"
    publisher: Salesforce Help
    url: https://help.salesforce.com/HTViewHelpDoc?id=networks_DPUA.htm
    type: official-docs
    accessed: 2026-11-22
  - id: s5
    title: "OEM User License Guide (ISVforce Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.packagingGuide.meta/packageGuide/oem_user_license_comparison.htm
    type: official-docs
    accessed: 2026-11-22
  - id: s6
    title: "Enhance Partner Engagement with Effective Solutions (Experience Cloud Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/community_cloud_basics/communities_partner_community
    type: official-learning
    accessed: 2026-11-22
  - id: s7
    title: "Salesforce Communities Licenses"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2014/02/salesforce-communities-licenses
    type: official-blog
    accessed: 2026-11-22
created: 2026-11-22
---

# Partner Community Licenses

**Partner Community** is the Experience Cloud user license for business-to-business sites whose users need sales data, for example resellers, distributors and other channel partners.[^s5] Partner users log in to a partner site to view and update CRM records the company shares with them, such as leads, opportunities and campaigns.[^s2] Salesforce's ISV license guide states the main structural restriction plainly: Partner Community licenses can't be used with person accounts.[^s5] Because the license decides which sharing tools apply, choosing it is a security and sharing decision as much as a commercial one.

## Partner users and partner accounts

A partner user is always tied to a business account that has been enabled as a partner account. An admin uses the **Enable as Partner** action on the account, then **Enable Partner User** on one of its contacts, and gives the user the Partner Community license with a partner profile such as a clone of Partner Community User.[^s2] The internal admin doing this setup must have a role. The user then gets access through the site's membership, which is set by profile or permission set in Experience Workspaces.[^s2] The Developers Blog guide to community licenses described Partner Community, like Customer Community, as available both per member and as a pool of monthly logins. That guide dates from 2014, so confirm current packaging with your account team.[^s7]

## How record access works: account roles

Unlike the high-volume Customer Community license, Partner Community users hold **roles**. Each enabled partner account gets its own small hierarchy of account roles. Only Customer Community Plus and Partner Community users can be given these roles.[^s1] The default is one role per partner account, and the Digital Experiences settings allow up to three. New partner users get their account's Partner User role unless another is chosen.[^s1] Raising the role count later doesn't add roles to existing partner accounts. Salesforce recommends staying with one role and using other sharing tools, because extra roles can hurt performance.[^s1]

Partner account roles sit **under the account owner** in the internal role hierarchy. That is why orgs usually make a channel account manager (an internal user with a channel sales role) the owner of partner accounts. Records a partner user owns are then visible to partner managers above that user, and to the channel manager and everyone above the channel manager internally.[^s1]

Sharing rules work for partner users the same way as for internal users. They can share in either direction between internal users and Partner Community or Customer Community Plus users. Owner-based rules can target portal role groups such as "Portal Roles and Subordinates" for one partner account, and criteria-based rules can share accounts to a public group that mixes partner managers with internal channel roles.[^s3] Salesforce maintains site-specific groups for this. The legacy All Partner Users group doesn't exist in production orgs created after Summer '20.[^s3]

## Limits and gotchas (Winter '27)

- **Role volume.** Roles are created per account, so two roles across 100 partner accounts make 200 roles. New orgs get at most 50,000 account roles for Experience Cloud users.[^s1]
- **Raising the role ceiling.** Going to 100,000 roles takes a Support request and a system design review. The absolute maximum of 500,000 needs special Salesforce approval.[^s1]
- **No person accounts.** Partners must be modeled as business accounts with contacts.[^s5]
- **Delegated administration.** Partner Community is a license that can hold Delegated External User Administration. A partner admin with it can add, update and disable members of their own account and reset passwords, within the profiles and permission sets an internal admin allows.[^s4]
- **Hierarchy changes ripple.** Partner roles inherit through the account owner's internal role, so changing the owner of a partner account changes who sees partner-owned records.[^s1]

## When to use it (and when not)

Use Partner Community when external companies sell or service on your behalf and need pipeline objects. Salesforce's partner-portal guidance pairs the license with a portal built from the Partner Central template, which includes **lead distribution** and **deal registration**. Lead distribution passes campaign and web leads to qualified partners, and partners register deals so the vendor can track them.[^s6] The same guidance covers distributed marketing campaigns and market development funds that partners request and track through the site.[^s6] For consumers who only need their own cases and knowledge, the cheaper high-volume Customer Community license is the better fit. Customer Community Plus covers customers who need roles but not partner sales objects.[^s5][^s1]

## Connections

Partner Community licenses belong to the **user licenses** family and are **consumed by** **Experience Cloud** sites.[^s5] They **contrast with Customer Community licenses**: the basic Customer Community tier has no roles, while this license is for B2B partners with account roles.[^s5][^s1] Access **depends on the role hierarchy**, because partner roles sit under the internal account owner, and it is extended with **sharing rules** and **public groups**.[^s1][^s3] In a **partner relationship management** portal, partners work leads routed to them by lead distribution (often driven by **assignment rules**) and register deals.[^s6] License choice for partner personas is part of an org's **licensing strategy**.[^s5]

## Sources

[^s1]: Trailhead, "Set Up Account Roles and the Role Hierarchy". https://trailhead.salesforce.com/content/learn/projects/communities_share_crm_data/account_roles_hierarchy (accessed 2026-11-22)
[^s2]: Trailhead, "Create a Partner Portal, Enable Partner Account and Users, and Add Members". https://trailhead.salesforce.com/content/learn/projects/communities_share_crm_data/create_portal_and_users (accessed 2026-11-22)
[^s3]: Trailhead, "Use Sharing Rules for External Users". https://trailhead.salesforce.com/content/learn/projects/communities_share_crm_data/sharing_rules (accessed 2026-11-22)
[^s4]: Salesforce Help, "Delegate Site Administration to an External User". https://help.salesforce.com/HTViewHelpDoc?id=networks_DPUA.htm (accessed 2026-11-22)
[^s5]: Salesforce Developers, "OEM User License Guide" (ISVforce Guide). https://developer.salesforce.com/docs/atlas.en-us.packagingGuide.meta/packageGuide/oem_user_license_comparison.htm (accessed 2026-11-22)
[^s6]: Trailhead, "Enhance Partner Engagement with Effective Solutions". https://trailhead.salesforce.com/content/learn/modules/community_cloud_basics/communities_partner_community (accessed 2026-11-22)
[^s7]: Salesforce Developers Blog, "Salesforce Communities Licenses" (2014). https://developer.salesforce.com/blogs/2014/02/salesforce-communities-licenses (accessed 2026-11-22)
