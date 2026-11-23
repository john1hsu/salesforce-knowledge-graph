---
id: kt:permission-set-led-deployment
type: Pattern
title: Permission Set-Led Deployment
aliases: [permission set-led security model, permission set led security model, permission set-led access model, migrating profiles to permission sets]
domain: devops-and-alm
summary: >-
  The practice of delivering user access through small, task-scoped permission sets and permission set groups kept in
  source control and deployed with the metadata they grant, leaving profiles as a thin minimum-access baseline.
release: "Winter '27"
status: current
broader: [kt:application-lifecycle-management, kt:permission-sets]
related: [kt:permission-set-groups, kt:principle-of-least-privilege, kt:user-access-policies, kt:custom-permissions, kt:unlocked-packages]
relations:
  - {predicate: alternativeTo, object: kt:profiles}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: dependsOn, object: kt:package-xml-manifest}
sources:
  - id: s1
    title: "Migrating to Permission Sets for DX"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2018/12/migrating-to-permission-sets-for-dx
    type: official-blog
    accessed: 2026-11-23
  - id: s2
    title: "Admin Best Practices for User Management"
    publisher: Salesforce Admins
    url: https://admin.salesforce.com/blog/2022/admin-best-practices-for-user-management
    type: official-blog
    accessed: 2026-11-23
  - id: s3
    title: "Profile (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_profile.htm
    type: official-docs
    accessed: 2026-11-23
  - id: s4
    title: "PermissionSet (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_permissionset.htm
    type: official-docs
    accessed: 2026-11-23
  - id: s5
    title: "Introducing The Next Generation of User Management: Permission Set Groups"
    publisher: Salesforce Admins
    url: https://admin.salesforce.com/blog/2019/introducing-the-next-generation-of-user-management-permission-set-groups
    type: official-blog
    accessed: 2026-11-23
created: 2026-11-23
---

# Permission Set-Led Deployment

Permission set-led deployment is the DevOps side of what Salesforce calls a permission set-led security model: users get a minimum-access profile, and everything they need for their job is layered on through permission sets and permission set groups organised by job function.[^s2] Salesforce has said it is not enhancing profiles further and recommends this model, even though enforcement of the planned end of life for permissions on profiles is paused.[^s2] For a delivery team the consequence is that access becomes ordinary, reviewable source: each permission set travels with the objects, fields, classes and pages it grants, rather than living in a large profile file that is hard to retrieve and merge.[^s1]

## Why profiles are awkward in source control

Profiles map one-to-one to users, so when metadata is split into packages a single profile cannot be divided between them; permission sets can.[^s1] Metadata API retrieval adds friction: a retrieved `.profile` file only holds security settings for the other components named in the same retrieve request, while user permissions, IP ranges and login hours always come back.[^s3] A `*` wildcard on CustomObject returns permissions for custom objects only, so standard objects and fields must be listed explicitly, and the API deliberately makes standard fields hard to pull in to avoid unintended profile changes.[^s3] Salesforce also recommends creating custom profiles with the Profile object rather than deploying the Profile metadata type.[^s3]

## How the pattern works

- **Baseline profile.** Keep a minimum-access profile plus the settings that are truly one-per-user: default record types and apps, page layout assignments, login hours and IP ranges.[^s2]
- **Task-scoped permission sets.** Put object and field permissions, system permissions, connected app access, Apex class and Visualforce page access, tab settings and custom permissions in permission sets.[^s2]
- **Persona groups.** Bundle the sets into permission set groups named after job functions; a set can belong to many groups, and edits propagate to every group that includes it.[^s5]
- **Ship access with the package.** A permission set covering a package's objects should live in that package, and user permissions such as Run Reports can move into a base-package permission set.[^s1]
- **Assign in automation.** Scripts and CI assign permission sets to users after deployment, so test users get the same access production users will.[^s1]

Avoid a one-to-one conversion of each profile into one permission set; the guidance is to make smaller, granular sets that stack.[^s1] Salesforce's suggested test for what moves is whether a setting must map to exactly one per user; if not, it belongs in a permission set.[^s5]

## Limits and gotchas

PermissionSet deploys behave differently from profiles. From API 40.0, a retrieve returns all of a permission set's content, and a deploy should include all of it, because any permission not specified is disabled.[^s4] To get `objectPermissions` and `fieldPermissions`, retrieve the related CustomObject components alongside the PermissionSet.[^s4] Required-field permissions cannot be retrieved or deployed from API 30.0, and from API 54.0 queries return only enabled field permissions.[^s4] A permission set label is limited to 80 characters and its description to 255.[^s4] Page layout and Lightning page assignments cannot move to permission sets because they are one-per-user; dynamic component visibility is the suggested workaround where it fits.[^s1]

## When to use it

Use the pattern for any source-driven or package-based org, especially when several teams or packages contribute access; it pairs naturally with the principle of least privilege and with muting permissions inside groups to narrow access.[^s2] Profile-centric deployment survives mainly in legacy change-set orgs, and Salesforce has long discouraged relying on profiles for permission management.[^s5]

## Connections

The pattern is a branch of **application lifecycle management** built on **permission sets**, and it is the delivery-side **alternative to profiles**, which shrink to a baseline.[^s2] **Permission set groups** provide the persona layer, and **custom permissions** replace profile references in formulas and validation rules.[^s2] Access is moved through the **Metadata API**, where the **package.xml manifest** decides which related components come back with each permission set or profile.[^s3] Shipping sets inside **unlocked packages** keeps access next to the metadata it grants.[^s1] **User access policies** can move users between profiles and permission sets in bulk during migration.[^s2] The whole approach puts the **principle of least privilege** into practice.[^s2]

## Sources

[^s1]: Salesforce Developers Blog, "Migrating to Permission Sets for DX" (Shane McLaughlin, 2018). https://developer.salesforce.com/blogs/2018/12/migrating-to-permission-sets-for-dx (accessed 2026-11-23)
[^s2]: Salesforce Admins, "Admin Best Practices for User Management". https://admin.salesforce.com/blog/2022/admin-best-practices-for-user-management (accessed 2026-11-23)
[^s3]: Salesforce, "Profile", Metadata API Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_profile.htm (accessed 2026-11-23)
[^s4]: Salesforce, "PermissionSet", Metadata API Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_permissionset.htm (accessed 2026-11-23)
[^s5]: Salesforce Admins, "Introducing The Next Generation of User Management: Permission Set Groups" (2019). https://admin.salesforce.com/blog/2019/introducing-the-next-generation-of-user-management-permission-set-groups (accessed 2026-11-23)
