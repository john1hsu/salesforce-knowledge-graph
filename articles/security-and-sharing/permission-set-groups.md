---
id: kt:permission-set-groups
type: SecurityControl
title: Permission Set Groups
aliases: [permission set group, PSG, PermissionSetGroup, muting permission set, muting permission sets]
domain: security-and-sharing
summary: >-
  Bundles of permission sets assigned to users as one unit, typically per job function; the group's
  effective permissions are the recalculated union of its member sets, optionally reduced by a single
  muting permission set.
release: "Winter '27"
status: current
broader: [kt:permission-sets]
related: [kt:salesforce-sharing-model, kt:organization-wide-defaults, kt:second-generation-managed-packages, kt:apex-testing, kt:restriction-rules]
relations:
  - {predicate: contrastsWith, object: kt:profiles}
  - {predicate: implements, object: kt:principle-of-least-privilege}
  - {predicate: queriedWith, object: kt:tooling-api}
  - {predicate: queriedWith, object: kt:soql}
sources:
  - id: s1
    title: "Get Started with Permission Set Groups (Trailhead, Permission Set Groups module)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/permission-set-groups/get-started-with-permission-set-groups
    type: official-learning
    accessed: 2026-11-05
  - id: s2
    title: "Create a Permission Set Group (Trailhead, Permission Set Groups module)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/es/content/learn/modules/permission-set-groups/create-a-permission-set-group
    type: official-learning
    accessed: 2026-11-05
  - id: s3
    title: "Mute Permissions in Permission Set Groups (Trailhead, Permission Set Groups module)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/permission-set-groups/mute-permissions-in-permission-set-groups
    type: official-learning
    accessed: 2026-11-05
  - id: s4
    title: "PermissionSetGroup (Object Reference for the Salesforce Platform)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_permissionsetgroup.htm
    type: official-docs
    accessed: 2026-11-05
  - id: s5
    title: "PermissionSetGroup (Tooling API Developer Guide, Winter '27)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.api_tooling.meta/api_tooling/tooling_api_objects_permissionsetgroup.htm
    type: official-docs
    accessed: 2026-11-05
  - id: s6
    title: "Testing Permission Set Groups (Apex Developer Guide, Winter '27)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_permission_set_group_testing.htm
    type: official-docs
    accessed: 2026-11-05
created: 2026-11-05
---

# Permission Set Groups

A permission set group bundles several permission sets so that an admin can assign the whole bundle to a user in one step, usually modelled on a job function or persona rather than a title. The group carries every permission contained in its member sets, and a single permission set can belong to many groups while still being assignable on its own.[^s1] The underlying `PermissionSetGroup` object has been available since API version 45.0, and Salesforce describes it as a way to organize permissions by job function or task and to package those groups as needed.[^s4] The object is also exposed through the Tooling API in the Winter '27 (API 68.0) documentation.[^s5]

## How it works

Admins build small, focused permission sets (for example one for order activation and one for contract maintenance), then create a group in Setup and add the sets under *Permission Sets in Group*. The group's *Combined Permissions* view shows the effective object, field and user permissions that result from all members together.[^s2] Users are then added through *Manage Assignments*. Licensing still applies: a user can be assigned the group only if their license supports every permission it contains, which is the same rule enforced for individual permission sets. In the Trailhead exercise, a user on a free platform license is refused the group while a fully licensed user is accepted.[^s2]

Effective permissions are not evaluated live. Editing a member set, or adding or removing sets, triggers a recalculation that propagates to every group containing that set, and assigned users keep the permissions from the last completed calculation until the new one finishes. A group's status reports where it stands: Updated, Outdated, Updating or Failed.[^s1]

## Muting permissions

Sometimes a group should include a shared permission set except for one or two permissions. Instead of cloning the set, the admin adds a muting permission set to the group, which disables selected object, field and user permissions for that group without touching the member sets. A group can have at most one muting permission set.[^s3] Muting follows permission dependencies: muting Read on an object also mutes Create, Edit, Delete, View All and Modify All for it, and the save confirmation lists every affected permission.[^s3]

Muting is local, not a deny rule. It affects only users who receive the permission through that group; anyone who gets the same permission from their profile, a directly assigned permission set or another group keeps it. The User Access Summary and the group summary both reflect muting when reporting enabled permissions.[^s3] A recommended sequence when widening a shared set is to create the muting set first, so users of the narrower group never briefly gain the broader access.[^s3]

## Limits and gotchas

- **Recalculation lag.** Because effective access comes from the last completed calculation, a change to a widely used permission set can leave groups Outdated for a while, and a group in that state cannot be assigned in tests.[^s1][^s6]
- **Apex tests.** `Test.calculatePermissionSetGroup()` forces an immediate recalculation so a test can assign the group. The call counts against Apex CPU limits; groups with many member sets or enabled permissions, or unlicensed member sets assigned to many users, can push a test over the CPU limit. Salesforce advises calculating once in a `@testSetup` method and reusing the result.[^s6]
- **Muting is one-per-group and non-exclusive**, so it cannot be used to guarantee a user lacks a permission; check all of a user's access sources.[^s3]

## When to use it (and when not)

Groups suit organizations moving access off profiles toward small, reusable permission sets: one assignment per persona keeps least-privilege access manageable as teams change, without stuffing many unrelated permissions into one oversized set.[^s1] They also help with managed packages. Subscribers can place a vendor's managed permission sets inside a local group, or local sets inside a managed group, so package upgrades flow through. Muting can hold back a newly packaged field permission until the org is ready for it.[^s1][^s3] What a group grants is object, field and user permissions[^s3]; which records a user can see is decided separately by record-level sharing.

## Connections

Permission set groups sit directly under **permission sets**, which they aggregate, and contrast with **profiles**: each user has exactly one, and Salesforce recommends the Minimum Access - Salesforce profile as the baseline, with groups layering job-function access on top.[^s1][^s2] They put the **principle of least privilege** into practice by assembling job-function access from narrow sets.[^s1] They sit alongside the record-level controls of the **Salesforce sharing model**, **organization-wide defaults** and **restriction rules**, since a group grants object, field and user permissions rather than record visibility.[^s3] Their package-upgrade behaviour links them to **second-generation managed packages**.[^s1] Their asynchronous recalculation matters for **Apex testing**.[^s6] The `PermissionSetGroup` object is documented in the platform object reference and in the **Tooling API**, so it can be queried with **SOQL** from tooling and admin scripts.[^s4][^s5]

## Sources
[^s1]: Salesforce Trailhead, "Get Started with Permission Set Groups". https://trailhead.salesforce.com/content/learn/modules/permission-set-groups/get-started-with-permission-set-groups (accessed 2026-11-05)
[^s2]: Salesforce Trailhead, "Create a Permission Set Group". https://trailhead.salesforce.com/es/content/learn/modules/permission-set-groups/create-a-permission-set-group (accessed 2026-11-05)
[^s3]: Salesforce Trailhead, "Mute Permissions in Permission Set Groups". https://trailhead.salesforce.com/content/learn/modules/permission-set-groups/mute-permissions-in-permission-set-groups (accessed 2026-11-05)
[^s4]: Salesforce, "PermissionSetGroup", Object Reference for the Salesforce Platform. https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_permissionsetgroup.htm (accessed 2026-11-05)
[^s5]: Salesforce, "PermissionSetGroup", Tooling API Developer Guide (Winter '27). https://developer.salesforce.com/docs/atlas.en-us.264.0.api_tooling.meta/api_tooling/tooling_api_objects_permissionsetgroup.htm (accessed 2026-11-05)
[^s6]: Salesforce, "Testing Permission Set Groups", Apex Developer Guide (Winter '27). https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_permission_set_group_testing.htm (accessed 2026-11-05)
