---
id: kt:custom-permissions
type: SecurityControl
title: Custom Permissions
aliases: [custom permission, CustomPermission, CustomPermission metadata type, $Permission, $Permission global variable, FeatureManagement.checkPermission]
domain: security-and-sharing
summary: >-
  Admin-defined named permissions that carry no built-in behavior of their own: they are granted through
  permission sets or profiles and checked by validation rules, flows, component visibility, Apex and
  Lightning web components to switch features or bypasses on and off per user.
release: "Winter '27"
status: current
broader: [kt:salesforce-sharing-model]
related: [kt:profiles, kt:connected-apps, kt:second-generation-managed-packages]
relations:
  - {predicate: partOf, object: kt:permission-sets}
  - {predicate: consumedBy, object: kt:validation-rules}
  - {predicate: consumedBy, object: kt:flow-builder}
  - {predicate: consumedBy, object: kt:lightning-web-components}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: implements, object: kt:principle-of-least-privilege}
sources:
  - id: s1
    title: "CustomPermission (Metadata API Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_custompermission.htm
    type: official-docs
    accessed: 2026-11-21
  - id: s2
    title: "FeatureManagement Class (Apex Reference Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apex/apex_class_System_FeatureManagement.htm
    type: official-docs
    accessed: 2026-11-21
  - id: s3
    title: "Permissions (Lightning Web Components Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/lwc/guide/create-get-permissions.html
    type: official-docs
    accessed: 2026-11-21
  - id: s4
    title: "Why You Should Add Custom Permissions to Your #AwesomeAdmin Tool Belt"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2021/why-you-should-add-custom-permissions-to-your-awesomeadmin-tool-belt
    type: official-blog
    accessed: 2026-11-21
  - id: s5
    title: "CustomPermission (Object Reference for the Salesforce Platform)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_custompermission.htm
    type: official-docs
    accessed: 2026-11-21
created: 2026-11-21
---

# Custom Permissions

A **custom permission** is a named access check that an admin or developer defines in Setup. Unlike a standard permission such as "Modify All Data", it does nothing by itself: it only becomes meaningful when some piece of logic asks whether the running user holds it.[^s4] Custom permissions have been available since Winter '15 and are granted to users through profiles (everyone on the profile) or permission sets (selected users).[^s4] They are the standard way to turn a feature, a button, or a bypass on for some users and off for others without hard-coding user or profile names.

## How it works

Each custom permission is a metadata component with a required label (up to 80 characters), an optional description (up to 255 characters), and an API name.[^s1] In Metadata API it is the `CustomPermission` type, introduced in API version 31.0, stored in the `customPermissions` folder with the `.customPermission` suffix, and retrievable with the `*` wildcard in `package.xml`.[^s1] The same records can be read through the `CustomPermission` object, which supports `query()`, `retrieve()` and the describe calls, and which exposes fields such as `DeveloperName`, `NamespacePrefix`, `IsProtected` and `IsLicensed`.[^s5] Salesforce points to this object, together with the setup-entity access records behind permission sets, as the way to work out which users hold a given custom permission.[^s5]

A custom permission can declare **required permissions** (`requiredPermission`, added in API version 32.0): a list of other custom permissions that must be enabled whenever this one is.[^s1] It can also be associated with a connected app or an external client app, so access to that app's functionality is gated by the permission.[^s1] Since Summer '20, only users with View Setup and Configuration, Manage Session Permission Set Activations, or Assign Permission Sets can access the object.[^s1]

## Where it is checked

Almost every layer of the platform can read a custom permission:

- **Formulas and validation rules** reference it as `$Permission.<API name>`, which returns true for users who hold it.[^s4]
- **Flows** check it through a formula resource that inserts the same `$Permission` global variable.[^s4]
- **Component visibility** on Lightning pages and dynamic actions can filter on Permissions › Custom Permission.[^s4]
- **Apex** calls `FeatureManagement.checkPermission(apiName)`, which returns true when the running user has the permission enabled.[^s2]
- **Lightning web components** import it statically from `@salesforce/customPermission/<PermissionName>`; managed-package permissions use the `namespace__PermissionName` form.[^s3]

In an LWC, the imported value is true when the user has the permission and undefined otherwise, so code should test for truthiness rather than compare to `false`.[^s3] The guide recommends this static import over dynamic Aura-style permission checks because it avoids a server round trip.[^s3]

## Limits and gotchas

- The `DeveloperName` must start with a letter and cannot contain spaces, a trailing underscore or double underscores.[^s5]
- `IsLicensed` is read-only and marks permissions that need a Salesforce license before a user can access them.[^s1]
- In managed packages, a protected custom permission (`IsProtected`) can't be referenced from subscriber orgs, which lets ISVs keep internal feature switches hidden.[^s5]

The admin guidance is to give each custom permission a descriptive name and a description that says whether it grants or denies something, and to name a single-purpose permission set after the permission it carries.[^s4]

## When to use it (and when not)

Use a custom permission when access depends on *who the user is allowed to be* rather than on record data: a "Bypass Validation" switch for data loads, a beta feature for a pilot group, or an approval-only button.[^s4] It beats checking profile names in formulas or code, because assignment stays in permission sets and can change without a deployment.[^s4] It is not a substitute for object, field or record access; those belong to the sharing model and field-level security.

## Connections

Custom permissions are **part of** **permission sets**, the preferred assignment vehicle, though **profiles** can also enable them.[^s4] They are **consumed by** **validation rules** and **flows** through `$Permission`, and by **Lightning web components** through static imports.[^s3][^s4] They are **configured via** the **Metadata API** `CustomPermission` type and can be tied to **connected apps**.[^s1] In **second-generation managed packages**, protection lets ISVs ship them as hidden feature switches.[^s5] They **implement** the **principle of least privilege** by granting narrowly scoped capabilities only to the users who need them, and sit under the broader **Salesforce sharing model** of access controls.[^s4]

## Sources

[^s1]: Salesforce, "CustomPermission", Metadata API Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_custompermission.htm (accessed 2026-11-21)
[^s2]: Salesforce, "FeatureManagement Class", Apex Reference Guide. https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apex/apex_class_System_FeatureManagement.htm (accessed 2026-11-21)
[^s3]: Salesforce, "Permissions", Lightning Web Components Developer Guide. https://developer.salesforce.com/docs/platform/lwc/guide/create-get-permissions.html (accessed 2026-11-21)
[^s4]: Salesforce Admins Blog, "Why You Should Add Custom Permissions to Your #AwesomeAdmin Tool Belt" (2021). https://admin.salesforce.com/blog/2021/why-you-should-add-custom-permissions-to-your-awesomeadmin-tool-belt (accessed 2026-11-21)
[^s5]: Salesforce, "CustomPermission", Object Reference for the Salesforce Platform. https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_custompermission.htm (accessed 2026-11-21)
