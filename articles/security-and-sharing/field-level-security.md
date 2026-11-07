---
id: kt:field-level-security
type: SecurityControl
title: Field-Level Security
aliases: [FLS, field-level security, field permissions, FieldPermissions, FieldPermissions object, field accessibility, CRUD/FLS]
domain: security-and-sharing
summary: >-
  The layer of Salesforce data security that decides, per field, whether a user can read and edit a value;
  granted through profiles and permission sets and enforced across the UI, reports, search and the API.
release: "Winter '27"
status: current
broader: [kt:salesforce-sharing-model]
related: [kt:principle-of-least-privilege, kt:profiles, kt:lightning-data-service, kt:soql, kt:shield-platform-encryption]
relations:
  - {predicate: partOf, object: kt:permission-sets}
  - {predicate: contrastsWith, object: kt:page-layouts}
  - {predicate: queriedWith, object: kt:apex}
sources:
  - id: s1
    title: "Control Access to Fields (Trailhead: Data Security)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data_security/data_security_fields
    type: official-learning
    accessed: 2026-11-07
  - id: s2
    title: "FieldPermissions (Object Reference for the Salesforce Platform)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_fieldpermissions.htm
    type: official-docs
    accessed: 2026-11-07
  - id: s3
    title: "Enforce User Mode for Database Operations (Apex Developer Guide, Winter '27)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_classes_enforce_usermode.htm
    type: official-docs
    accessed: 2026-11-07
  - id: s4
    title: "Apex Versioned Behavior Changes (Apex Developer Guide, Winter '27)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/versioned_behavior_changes.htm
    type: official-docs
    accessed: 2026-11-07
  - id: s5
    title: "Protect Your Application from CRUD/FLS Vulnerabilities (Secure Coding Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/secure-coding/guide/secure-coding-access-control-protect-from-crud-fls-vulnerabilities.html
    type: official-docs
    accessed: 2026-11-07
  - id: s6
    title: "Secure Apex Classes (Lightning Web Components Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/lwc/guide/apex-security
    type: official-docs
    accessed: 2026-11-07
created: 2026-11-07
---

# Field-Level Security

Field-level security (FLS) is the set of field permissions that decides whether a user can see a particular field on an object and whether they can change its value. It sits beneath object permissions: a user first needs Read on the object, and FLS then narrows which of that object's fields are visible or editable, so a sensitive field such as a Social Security number can stay hidden while the rest of the record is shown.[^s1] FLS is the "which columns" half of Salesforce access control; the sharing model decides "which rows".[^s1][^s3]

## How it works

Admins grant field permissions in profiles or permission sets, or from a field's **Set Field-Level Security** button and the Field Accessibility view in Setup; Trailhead recommends doing it in permission sets and permission set groups. An org setting lets admins choose permission sets, not just profiles, when creating a new field.[^s1] Each field has two flags, Read and Edit. In the API these are stored as `FieldPermissions` records that hang off a `PermissionSet` (or a muting permission set) and carry `SobjectType`, `Field`, `PermissionsRead` and `PermissionsEdit`; Edit can only be true when Read is true, and a record that loses Read is deleted.[^s2] A user's effective access is the union of everything granted by their profile and assigned permission sets, minus anything a muting permission set in a group removes, so a set granting read and edit combined with a muted edit leaves read only.[^s2]

Because FLS is enforced by the platform rather than by a particular screen, it applies wherever the field appears: record pages, related lists, list views, reports and search results. Trailhead stresses that field permissions are the only reliable way to keep a user away from a field.[^s1]

## Limits and gotchas

- **Page layouts are not security.** A layout only arranges fields on the detail and edit pages; removing a field from a layout still leaves it reachable through reports, list views, search and APIs.[^s1]
- **Some fields cannot be restricted.** The `FieldPermissions` object returns no rows for system fields such as `Id`, `CreatedDate` and `SystemModStamp`, or for `OwnerId`, master-detail fields and universally required custom fields, which are always readable (and for the latter, writable). Formula and auto-number fields accept only Read. Check the `permissionable` describe property first.[^s2]
- **View All Fields overrides per-field settings.** If a permission set grants View All Fields on an object, `PermissionsRead` reads as true for every field on it.[^s2]
- **Querying permissions needs setup access.** Since API version 49.0, only users with View Setup and Configuration can read `FieldPermissions`.[^s2]
- **Task and event custom fields share one permission**: a change to one applies to the other.[^s2]

## FLS in code

Code is where FLS is most often bypassed. Through API version 66.0, Apex database operations run in system mode by default and ignore object and field permissions unless the code enforces them; from API version 67.0 (Summer '26) user mode is the default and the running user's FLS, object permissions and sharing apply.[^s3][^s4] The same versioned change removed `WITH SECURITY_ENFORCED` from SOQL at 67.0, with `WITH USER_MODE` as the replacement.[^s4] Developers can set the mode explicitly per operation: `WITH USER_MODE` or `WITH SYSTEM_MODE` on SOQL, `insert as user` / `as system` on DML, and `AccessLevel.USER_MODE` on `Database` and `Search` methods.[^s3]

The Secure Coding Guide prefers user mode to the older `WITH SECURITY_ENFORCED` because it also covers the WHERE clause and polymorphic fields and reports every FLS error, not just the first. `Security.stripInaccessible()` quietly removes fields the user cannot see from query results or from records before DML, and Describe checks (`isAccessible`, `isCreateable`, `isUpdateable`) give finer control at the cost of boilerplate.[^s5] On the client side, Lightning Data Service enforces CRUD and FLS for you, while `with sharing` on an Apex class enforces record sharing only, not field security.[^s6] Explicitly bypassing FLS is acceptable only in narrow cases, such as aggregates that don't expose the underlying data, and must be documented for AppExchange Security Review.[^s5]

## When to use it (and when not)

Use FLS whenever a field must be hidden or made read-only for some users, and design it with least privilege: a minimal profile plus permission sets that open only the fields each job needs.[^s1] Use page layouts and record types only to shape the user experience. FLS doesn't decide which records a user sees; that is the sharing model's job, and Apex's `with sharing` keyword enforces sharing without enforcing field security.[^s3][^s6]

## Connections

FLS is a component of **permission sets** and **profiles**, which carry the field permissions, and it implements the **principle of least privilege** at column level.[^s2][^s1] It is commonly confused with **page layouts**, which only control presentation.[^s1] It complements record-level access in the **Salesforce sharing model**; user-mode Apex enforces both together.[^s3] In code it is enforced through **Apex** access modes and **SOQL** `WITH USER_MODE`, and automatically by **Lightning Data Service**.[^s3][^s6] Because field permissions are records attached to permission sets, they can be audited with SOQL against `FieldPermissions` and `PermissionSet`.[^s2] It is distinct from **Shield Platform Encryption**: FLS governs who can see a field, not how its value is stored.

## Sources

[^s1]: Salesforce Trailhead, "Control Access to Fields" (Data Security module). https://trailhead.salesforce.com/content/learn/modules/data_security/data_security_fields (accessed 2026-11-07)
[^s2]: Salesforce, "FieldPermissions", Object Reference for the Salesforce Platform. https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_fieldpermissions.htm (accessed 2026-11-07)
[^s3]: Salesforce, "Enforce User Mode for Database Operations", Apex Developer Guide (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_classes_enforce_usermode.htm (accessed 2026-11-07)
[^s4]: Salesforce, "Apex Versioned Behavior Changes", Apex Developer Guide (Winter '27). https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/versioned_behavior_changes.htm (accessed 2026-11-07)
[^s5]: Salesforce, "Protect Your Application from CRUD/FLS Vulnerabilities", Secure Coding Guide. https://developer.salesforce.com/docs/platform/secure-coding/guide/secure-coding-access-control-protect-from-crud-fls-vulnerabilities.html (accessed 2026-11-07)
[^s6]: Salesforce, "Secure Apex Classes", Lightning Web Components Developer Guide. https://developer.salesforce.com/docs/platform/lwc/guide/apex-security (accessed 2026-11-07)
