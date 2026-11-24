---
id: kt:delegated-administration
type: Feature
title: Delegated Administration
aliases: [delegated administrators, delegated admin, delegated administration groups, DelegateGroup, delegated admin groups]
domain: identity
summary: >-
  The Salesforce Setup feature that gives a group of non-administrator users limited admin rights: creating and
  editing users in chosen roles and their subordinates, resetting their passwords, assigning a fixed list of
  profiles, permission sets and public groups, and managing selected custom objects.
release: "Winter '27"
status: current
broader: [kt:user-management, kt:salesforce-identity]
related: [kt:principle-of-least-privilege, kt:role-hierarchy, kt:grant-login-access, kt:partner-community-licenses, kt:public-groups]
relations:
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: dependsOn, object: kt:role-hierarchy}
  - {predicate: dependsOn, object: kt:profiles}
  - {predicate: dependsOn, object: kt:permission-sets}
  - {predicate: dependsOn, object: kt:permission-set-groups}
  - {predicate: contrastsWith, object: kt:delegated-authentication}
sources:
  - id: s1
    title: "DelegateGroup | Metadata Types | Metadata API Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_delegategroup.htm
    type: official-docs
    accessed: 2026-11-24
  - id: s2
    title: "Delegated Administration Groups | Lightning Platform Fundamentals (Summer '18)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.214.0.fundamentals.meta/fundamentals/adg_securing_data_delegated_admin_groups.htm
    type: official-docs
    accessed: 2026-11-24
  - id: s3
    title: "Try It Out: Define the Recruiting Manager Administration Group | Force.com Platform Fundamentals (Spring '16)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.200.0.fundamentals.meta/fundamentals/adg_securing_data_delegating_group_try_it_out.htm
    type: official-docs
    accessed: 2026-11-24
  - id: s4
    title: "Delegating Data Administration | Lightning Platform Fundamentals (Spring '18)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.212.0.fundamentals.meta/fundamentals/adg_securing_data_delegating_admin.htm
    type: official-docs
    accessed: 2026-11-24
  - id: s5
    title: "How to Set Up a Delegate Administrator in Salesforce"
    publisher: Salesforce Ben
    url: https://www.salesforceben.com/how-to-set-up-a-delegate-administrator-in-salesforce/
    type: partner
    accessed: 2026-11-24
created: 2026-11-24
---

# Delegated Administration

**Delegated administration** lets a Salesforce admin hand a slice of user and object administration to people who are not system administrators. The unit of delegation is a **delegated administration group**: a set of non-administrator users who share limited administrative privileges.[^s2] In metadata, a group is the `DelegateGroup` type, which Salesforce describes as a group of users with the same administrative privileges, distinct from the public groups used for sharing.[^s1]

## Why it exists

A primary administrator usually holds the System Administrator profile, with org-wide permissions such as View All Data, Modify All Data, Customize Application and Manage Users.[^s4] Giving a regional manager or an app owner those permissions just so they can onboard staff would far exceed what they need. Salesforce's fundamentals guide presents two narrower routes: object-level permissions, and delegated administration groups for user and custom-object administration.[^s4]

## What a delegated administrator can do

A group grants a defined bundle of rights:[^s2][^s1]

- **User administration by role.** Create and edit users, and reset their passwords, in the roles you list and all of their subordinate roles.[^s2][^s1]
- **Assignable profiles, permission sets and permission set groups.** Assign only the ones you add to the group, to users in the delegated roles; they cannot edit those profiles.[^s1][^s3]
- **Assignable public groups.** Add or remove the delegated users from the groups you list.[^s1][^s5]
- **Custom object administration.** Customize nearly every aspect of the listed custom objects, including creating a custom tab.[^s1]
- **Log in as users.** If the group has login access enabled, members can log in as users in the hierarchy they administer, but only those users who granted login access.[^s1][^s3]

## Setting it up

An admin creates groups in Setup under **Delegated Administration**: name the group, optionally enable login access, add the delegated administrators, and then add the user-administration roles, assignable profiles and custom objects.[^s3][^s5] Picking a role automatically includes its subordinate roles.[^s3] Only users with the View Setup and Configuration permission can be delegated administrators.[^s1][^s3]

Groups are also deployable metadata. `DelegateGroup` has been available since API version 36.0, is stored as `.delegateGroup` files in a `delegateGroups` folder, and supports the wildcard in `package.xml`.[^s1] Its fields are `label` and `loginAccess` (both required), plus optional lists of `customObjects`, `groups`, `permissionSets`, `permissionSetGroups`, `profiles` and `roles`.[^s1]

## Limits and gotchas

- **Custom objects only, with exceptions.** Delegated admins can't create or change relationships on a delegated object or set its org-wide sharing defaults.[^s1] The older guide adds object permissions and workflow to that list, and warns that the delegation includes the right to delete the object.[^s3]
- **No privilege escalation.** Salesforce Ben reports that delegated admins can't assign a profile, permission set or permission set group that contains Modify All Data.[^s5] Editing permission sets, customizing standard objects and editing page layouts are also outside what a group can grant.[^s5]
- **Group size.** The Spring '16 fundamentals guide capped each group at five members. That guide is now retired, so confirm the current cap in Setup before planning around it.[^s3]
- **Login access still needs consent.** The group setting alone does not let delegates impersonate anyone. Each user must grant login access first.[^s1][^s3]

## When to use it (and when not)

Use it when a department or subsidiary needs to onboard, reset and reassign its own users without wider Setup access. It follows least privilege better than handing out Manage Users.[^s2][^s4] For external users in Experience Cloud sites, use the Delegated External User Administration permission instead. Salesforce Ben notes it is available with licenses such as Partner Community and Customer Community Plus.[^s5] For broad metadata or standard-object changes, delegation is the wrong tool, because the groups cannot grant those rights.[^s5]

## Connections

Delegated administration is part of `kt:user-management` and the wider `kt:salesforce-identity` toolset.[^s2] Its scope is bounded by the `kt:role-hierarchy`, and what it can hand out is limited to listed `kt:profiles`, `kt:permission-sets`, `kt:permission-set-groups` and `kt:public-groups`.[^s1] Its login-as option builds on `kt:grant-login-access`.[^s1] The external-user counterpart appears with `kt:partner-community-licenses`.[^s5] Groups move between orgs through the `kt:metadata-api`.[^s1] Despite the similar name, it has nothing to do with `kt:delegated-authentication`, which is a single sign-on method. Delegation is a practical application of the `kt:principle-of-least-privilege`.[^s4]

## Sources
[^s1]: Salesforce Developers, "DelegateGroup | Metadata Types | Metadata API Developer Guide". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_delegategroup.htm (accessed 2026-11-24)
[^s2]: Salesforce Developers, "Delegated Administration Groups | Lightning Platform Fundamentals (Summer '18)". https://developer.salesforce.com/docs/atlas.en-us.214.0.fundamentals.meta/fundamentals/adg_securing_data_delegated_admin_groups.htm (accessed 2026-11-24)
[^s3]: Salesforce Developers, "Try It Out: Define the Recruiting Manager Administration Group (Spring '16)". https://developer.salesforce.com/docs/atlas.en-us.200.0.fundamentals.meta/fundamentals/adg_securing_data_delegating_group_try_it_out.htm (accessed 2026-11-24)
[^s4]: Salesforce Developers, "Delegating Data Administration | Lightning Platform Fundamentals (Spring '18)". https://developer.salesforce.com/docs/atlas.en-us.212.0.fundamentals.meta/fundamentals/adg_securing_data_delegating_admin.htm (accessed 2026-11-24)
[^s5]: Salesforce Ben, "How to Set Up a Delegate Administrator in Salesforce". https://www.salesforceben.com/how-to-set-up-a-delegate-administrator-in-salesforce/ (accessed 2026-11-24)
