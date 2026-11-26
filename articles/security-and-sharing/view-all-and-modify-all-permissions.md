---
id: kt:view-all-and-modify-all-permissions
type: SecurityControl
title: View All and Modify All Permissions
aliases: [View All Records, Modify All Records, PermissionsViewAllRecords, PermissionsModifyAllRecords, View All and Modify All object permissions]
domain: security-and-sharing
summary: >-
  Object-level permissions that let a user read (View All) or read, edit and delete (Modify All) every
  record of one object regardless of sharing, the scoped alternative to the org-wide View All Data and
  Modify All Data system permissions; distinct from the newer View All Fields permission.
release: "Winter '27"
status: current
broader: [kt:salesforce-sharing-model, kt:permission-sets]
related: [kt:profiles, kt:principle-of-least-privilege, kt:field-level-security, kt:guest-user-record-access, kt:organization-wide-defaults, kt:role-hierarchy]
relations:
  - {predicate: contrastsWith, object: kt:sharing-rules}
  - {predicate: alternativeTo, object: kt:view-all-data-and-modify-all-data}
  - {predicate: configuredVia, object: kt:permission-sets}
  - {predicate: queriedWith, object: kt:soql}
sources:
  - id: s1
    title: "Data Access in Salesforce (Record-Level Access: Under the Hood)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-record-access-under-the-hood/guide/uth-intro.html
    type: official-docs
    accessed: 2026-11-26
  - id: s2
    title: "Overriding Sharing with Object Permissions (Force.com Platform Fundamentals)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.196.0.fundamentals.meta/fundamentals/adg_securing_data_override_sharing_object_perm.htm
    type: official-docs
    accessed: 2026-11-26
  - id: s3
    title: "ObjectPermissions (Object Reference for the Salesforce Platform)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_objectpermissions.htm
    type: official-docs
    accessed: 2026-11-26
  - id: s4
    title: "Get Hands-on with the View All Fields Permission"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/administrator-certification-maintenance-spring-25/get-hands-on-with-the-view-all-fields-permission
    type: official-learning
    accessed: 2026-11-26
  - id: s5
    title: "FieldPermissions (Object Reference for the Salesforce Platform)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/object-reference/references/standard-objects/object-fieldpermissions.html
    type: official-docs
    accessed: 2026-11-26
  - id: s6
    title: "SaaS Security Series: Understanding Salesforce Administrative Permissions"
    publisher: Cloud Security Alliance (AppOmni)
    url: https://cloudsecurityalliance.org/blog/2020/08/19/saas-security-series-understanding-salesforce-administrative-permissions
    type: partner
    accessed: 2026-11-26
created: 2026-11-26
---

# View All and Modify All Permissions

**View All** and **Modify All** are object permissions, set per object on a profile or permission set, that open up every record of that object to the user regardless of record-level access settings.[^s1] They sit alongside the four basic object permissions (Read, Create, Edit, Delete) but behave very differently: the basic ones only gate what a user may do with records sharing already lets them see, while View All and Modify All skip the sharing calculation entirely.[^s1][^s2]

## What each permission grants

View All lets the user see all records of the object. Modify All lets the user read, edit and delete all of them, and it also unlocks bulk operations: mass transfer, mass update and mass delete of that object's records, plus approving those records even when the user isn't a designated approver.[^s2] Because both permissions ignore the sharing model, the role hierarchy and sharing rules, a Private org-wide default on the object no longer limits that user.[^s2]

In the API the two appear as fields on the **ObjectPermissions** object, which represents the object permissions enabled on a parent permission set: `PermissionsViewAllRecords` and `PermissionsModifyAllRecords`, alongside `PermissionsRead`, `PermissionsCreate`, `PermissionsEdit` and `PermissionsDelete`. The object is available from API version 24.0, and the Winter '27 reference (API 68.0) still documents both fields.[^s3]

## Permission dependencies

The ObjectPermissions reference spells out which permissions must be enabled together:[^s3]

- View All Records requires Read on the same object.[^s3]
- Modify All Records requires Read, Edit, Delete and View All Records, so granting it pulls those in.[^s3]
- Delete itself requires Read and Edit on the same object.[^s3]

Because ObjectPermissions rows can be queried with SOQL, a common audit is to list every permission set where `PermissionsModifyAllRecords` is true for sensitive objects.[^s3]

## View All Data and Modify All Data

The global **View All Data** and **Modify All Data** system permissions also ignore sharing, but they apply to the records of every object rather than one.[^s2] A security write-up for administrators describes View All Data as a bypass of both object- and record-level read settings, and notes that Modify All Data doubles as a generic check that many administrative actions still require.[^s6] Salesforce's own guidance is the deciding rule: when the global permissions are too permissive for a job, use the object permissions instead.[^s2] The same write-up recommends object-level View All rather than View All Data for integration users.[^s6]

## View All Fields is a different permission

A newer **View All Fields** object permission, covered in Trailhead's Spring '25 maintenance module,, which grants access to every field and its data on an object, including fields created later.[^s4] It answers a field-level question rather than a record-level one, so it is no substitute for View All Records. Trailhead recommends assigning View All Fields through permission sets rather than profiles.[^s4] In the FieldPermissions object, when View All Fields is on for an object in a permission set, `PermissionsRead` reports true for every queried field of that object.[^s5] ObjectPermissions exposes it as `PermissionsViewAllFields`.[^s3]

## When to use it and gotchas

The classic use case is a scoped delegation. Salesforce's example gives a contractor doing data cleansing a permission set with Modify All on just the recruiting objects, so the work gets done without exposing the rest of the company's data.[^s2] Other typical holders are reporting or integration users who must read every record of a few objects, where View All on those objects beats View All Data.[^s2][^s6]

Treat these grants as privileged access. They silently defeat whatever the sharing design intends, so a user with View All on Opportunity sees every opportunity even if the org-wide default is Private and no rule shares them.[^s1][^s2] Prefer permission sets over profiles so the grant is visible and removable, and review ObjectPermissions regularly.[^s3][^s4] When a user needs most but not all records, sharing rules or teams are the better tool, because they keep the sharing model in charge.[^s1]

## Connections

These permissions belong to the `kt:salesforce-sharing-model` as its main override, and they are **configured via** `kt:permission-sets` (or `kt:profiles`), where ObjectPermissions rows live.[^s1][^s3] They **contrast with** `kt:sharing-rules`, `kt:organization-wide-defaults` and the `kt:role-hierarchy`, which they ignore.[^s2] Broad grants strain the `kt:principle-of-least-privilege`, which is why the scoped object permission is preferred.[^s2] They are the scoped **alternative to** `kt:view-all-data-and-modify-all-data`.[^s2][^s6] View All Fields, a sibling permission, interacts with `kt:field-level-security` rather than sharing.[^s4][^s5] Grants are audited by querying ObjectPermissions with `kt:soql`.[^s3] Guest users are a special case covered in `kt:guest-user-record-access`.

## Sources

[^s1]: Salesforce Developers, "Data Access in Salesforce (Record-Level Access: Under the Hood)". https://developer.salesforce.com/docs/platform/salesforce-record-access-under-the-hood/guide/uth-intro.html (accessed 2026-11-26)
[^s2]: Salesforce Developers, "Overriding Sharing with Object Permissions". https://developer.salesforce.com/docs/atlas.en-us.196.0.fundamentals.meta/fundamentals/adg_securing_data_override_sharing_object_perm.htm (accessed 2026-11-26)
[^s3]: Salesforce Developers, "ObjectPermissions". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_objectpermissions.htm (accessed 2026-11-26)
[^s4]: Trailhead, "Get Hands-on with the View All Fields Permission". https://trailhead.salesforce.com/content/learn/modules/administrator-certification-maintenance-spring-25/get-hands-on-with-the-view-all-fields-permission (accessed 2026-11-26)
[^s5]: Salesforce Developers, "FieldPermissions". https://developer.salesforce.com/docs/platform/object-reference/references/standard-objects/object-fieldpermissions.html (accessed 2026-11-26)
[^s6]: Cloud Security Alliance (AppOmni), "SaaS Security Series: Understanding Salesforce Administrative Permissions". https://cloudsecurityalliance.org/blog/2020/08/19/saas-security-series-understanding-salesforce-administrative-permissions (accessed 2026-11-26)
