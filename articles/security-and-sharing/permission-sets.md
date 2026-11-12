---
id: kt:permission-sets
type: SecurityControl
title: Permission Sets
aliases: [permission set, PermissionSet, PermissionSet object, session-based permission set, session-based permission sets]
domain: security-and-sharing
summary: >-
  Named collections of object, field, system and app permissions that grant users access beyond their
  profile; a user can hold many of them, and they are the main unit of access in Salesforce's
  permission-set-led model.
release: "Winter '27"
status: current
broader: [kt:salesforce-sharing-model]
related: [kt:permission-set-groups, kt:connected-apps, kt:session-security-levels, kt:second-generation-managed-packages, kt:user-access-policies]
relations:
  - {predicate: contrastsWith, object: kt:profiles}
  - {predicate: implements, object: kt:principle-of-least-privilege}
  - {predicate: dependsOn, object: kt:permission-set-licenses}
  - {predicate: hasPart, object: kt:field-level-security}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: configuredVia, object: kt:metadata-api}
sources:
  - id: s1
    title: "PermissionSet (Object Reference for the Salesforce Platform)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_permissionset.htm
    type: official-docs
    accessed: 2026-11-07
  - id: s2
    title: "The Salesforce Admin's Guide to Profiles and Permissions"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2026/the-salesforce-admins-guide-to-profiles-and-permissions
    type: official-blog
    accessed: 2026-11-07
  - id: s3
    title: "Session-Based Permission Sets overview (Trailhead)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/es/content/learn/modules/session_based_perms/session_based_overview
    type: official-learning
    accessed: 2026-11-07
  - id: s4
    title: "Get Hands-On With Permission Set Expiration (Trailhead, Platform App Builder maintenance Winter '23)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/platform-app-builder-certification-maintenance-winter-23/get-hands-on-with-permission-set-expiration
    type: official-learning
    accessed: 2026-11-07
  - id: s5
    title: "PermissionSetLicense (Object Reference for the Salesforce Platform)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_permissionsetlicense.htm
    type: official-docs
    accessed: 2026-11-07
  - id: s6
    title: "Learn What's New with Access Control for Winter '25 (Trailhead, Architect maintenance)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-architect-certification-maintenance-winter-25/learn-whats-new-with-access-control-for-winter-25
    type: official-learning
    accessed: 2026-11-07
created: 2026-11-07
---

# Permission Sets

A permission set is a named bundle of permissions that gives one or more users extra access without changing or swapping their profile. It has been exposed in the API as the `PermissionSet` object since API version 22.0.[^s1] A user has exactly one profile but can hold many permission sets. That lets admins grant access by task or capability rather than building a new profile for every combination of duties.[^s2]

## What goes in a permission set

Salesforce now describes a permission-set-led model. Profiles keep baseline settings, and permission sets and permission set groups carry most of a user's access.[^s2] The admin guidance lists what permission sets should hold: object permissions, field-level security, system permissions, access to connected apps and Apex classes, custom permissions, tab settings, and record types beyond the default.[^s2] The recommended style is several small, clearly labelled sets rather than one large one, bundled into permission set groups by persona when they are always assigned together.[^s2] Permission sets only add access. To take a permission away from part of a group, admins mute it in the permission set group rather than editing the underlying set.[^s2]

## How it works under the hood

Since API version 25.0, every profile has its own underlying permission set that stores the profile's user, object and field permissions and its setup entity access. These profile-owned sets can be queried but not modified, and `IsOwnedByProfile = FALSE` filters them out of a query.[^s1] Each permission set can be tied to a user license or to a permission set license through the polymorphic `LicenseId` field, which replaced the deprecated `UserLicenseId` in API version 38.0. Leave `LicenseId` empty when the set will go to users on different license types. Set it when only one license type will use it, or when the set should draw on a permission set license.[^s1] The license controls which permissions the set can contain.[^s1] Assignments live in the `PermissionSetAssignment` object, and a permission set can be deleted only once no users are assigned to it.[^s1]

A **permission set license** lets users receive specific permissions without a profile change. It can grant access but never deny it. Its `TotalLicenses` and `UsedLicenses` fields track the org's seats, and `PermissionSetLicenseAssign` links it to users.[^s5]

## Session-based permission sets and expiring assignments

Selecting **Session Activation Required** makes a permission set session-based. Its permissions apply only while a session is activated for it, and they lapse at logout, timeout or when an admin ends the session.[^s3] Trailhead's examples include hiring managers who may see sensitive contracts only during an active session, and token-based web apps that must reauthenticate when access expires.[^s3] The API exposes this setting as the `HasActivationRequired` field.[^s1]

Assignments can also be time-limited. With **Permission Set & Permission Set Group Assignments with Expiration Dates** turned on in User Management Settings, an admin can add an assignment with no end date, a preset period such as 30 days, or a custom date. The assignment expires at 11:59 PM on that date in the chosen time zone.[^s4] "My Local Time Zone" means the admin's time zone, not the user's, which is a common surprise.[^s4]

## Limits and gotchas

- **Additive only.** Permission sets and permission set licenses can't deny access, so least privilege depends on a minimal base profile and on muting in groups.[^s2][^s5]
- **License choice matters.** A set tied to one license is meant for users on that license, so leave `LicenseId` blank for sets meant for users on mixed license types.[^s1]
- **Session-based sets and integrations.** A session-based set can fail if its permission set license isn't enabled for integrations.[^s5]
- **Don't hard-code profile-owned set names.** Their `Name` and `Label` values can change.[^s1]
- **Seeing effective access.** Since Winter '25, the User Access Summary on a user record lists that user's permissions, public groups and queues. The Object Access Summary in Object Manager shows which permission sets, groups and profiles grant access to an object.[^s6]

## When to use it (and when not)

Use permission sets for any access that varies by job or task, and keep profiles for login hours, IP ranges, default apps and page layout assignments.[^s2] For assigning several permission sets, permission set groups, package licenses and public groups in one step, **User Access Policies** became generally available in Winter '25, with a cap then raised to 200 active policies.[^s6]

## Connections

Permission sets are the object-, field- and system-permission layer of the **Salesforce sharing model**, and they **contrast with profiles**: one profile per user, many permission sets.[^s2] **Permission set groups** bundle them and can mute them.[^s2] Permission sets carry **field-level security** and grant access to **connected apps**.[^s2] Some permissions **require a permission set license**.[^s5] Session-based sets tie access to an active session, which complements **session security levels**.[^s3] Assignments and profile-owned sets are inspected with **SOQL**, and permission sets are deployed as metadata through the **Metadata API** and packages such as **second-generation managed packages**.[^s1] **User Access Policies** automate assignment at scale.[^s6] Small, task-scoped sets are how orgs put the **principle of least privilege** into practice.[^s2]

## Sources
[^s1]: Salesforce, "PermissionSet", Object Reference for the Salesforce Platform. https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_permissionset.htm (accessed 2026-11-07)
[^s2]: Salesforce Admins Blog, "The Salesforce Admin's Guide to Profiles and Permissions". https://admin.salesforce.com/blog/2026/the-salesforce-admins-guide-to-profiles-and-permissions (accessed 2026-11-07)
[^s3]: Salesforce Trailhead, "Session-Based Permission Sets" overview. https://trailhead.salesforce.com/es/content/learn/modules/session_based_perms/session_based_overview (accessed 2026-11-07)
[^s4]: Salesforce Trailhead, "Get Hands-On With Permission Set Expiration". https://trailhead.salesforce.com/content/learn/modules/platform-app-builder-certification-maintenance-winter-23/get-hands-on-with-permission-set-expiration (accessed 2026-11-07)
[^s5]: Salesforce, "PermissionSetLicense", Object Reference for the Salesforce Platform. https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_permissionsetlicense.htm (accessed 2026-11-07)
[^s6]: Salesforce Trailhead, "Learn What's New with Access Control for Winter '25". https://trailhead.salesforce.com/content/learn/modules/salesforce-architect-certification-maintenance-winter-25/learn-whats-new-with-access-control-for-winter-25 (accessed 2026-11-07)
