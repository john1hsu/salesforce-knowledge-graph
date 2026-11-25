---
id: kt:deleted-fields-and-field-undelete
type: Feature
title: Deleted Fields and Field Undelete
aliases: [deleted custom fields, undelete a custom field, restore deleted field, Deleted Fields list, purge deleted custom fields, field hard delete]
domain: data-model
summary: >-
  The soft-delete lifecycle for custom fields: a deleted field and its data are held for up to 15 days, during which an
  admin can restore it from the object's Deleted Fields list or purge it early, before Salesforce hard-deletes it.
release: "Winter '27"
status: current
broader: [kt:custom-fields]
related: [kt:field-history-tracking, kt:formula-fields, kt:auto-number-fields, kt:roll-up-summary-field, kt:lead-conversion, kt:backup-and-recover]
relations:
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: configuredVia, object: kt:package-xml-manifest}
  - {predicate: governedBy, object: kt:custom-field-allocations}
  - {predicate: contrastsWith, object: kt:first-generation-managed-packages}
sources:
  - id: s1
    title: "Delete a Custom Field"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=platform.deleting_fields.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-25
  - id: s2
    title: "Manage Deleted Custom Fields"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.fields_managing_deleted_fields.htm&type=5
    type: official-docs
    accessed: 2026-11-25
  - id: s3
    title: "Purge Deleted Custom Fields"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.fields_purge_deleted_fields.htm&type=5
    type: official-docs
    accessed: 2026-11-25
  - id: s4
    title: "Deleting Components from an Organization — Metadata API Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_deploy_deleting_files.htm
    type: official-docs
    accessed: 2026-11-25
  - id: s5
    title: "Remove Components from First-Generation Managed Packages"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg1-dev/guide/packaging-managed-component-deletion.html
    type: official-docs
    accessed: 2026-11-25
  - id: s6
    title: "Time to Clean up Those Unneeded Salesforce Customizations"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2017/01/time-clean-unneeded-salesforce-customizations
    type: official-blog
    accessed: 2026-11-25
created: 2026-11-25
---

# Deleted Fields and Field Undelete

Deleting a custom field in Setup is a soft delete. The field disappears from the object, but Salesforce keeps the
field and its data until the org permanently deletes it or 15 days pass, whichever comes first; until then the field
and its values can be brought back.[^s1][^s2] Deleted fields are listed on the object's **Deleted Fields** page, where
an admin can restore (undelete) a field, erase it permanently, or purge the whole batch early.[^s2][^s3] Deleting
requires the Customize Application and View All Data permissions.[^s1]

## How it works

**Deleting.** From the object's Fields list you click Del and confirm. Salesforce blocks the delete when another
component still references the field, for example a field update or Apex, and while a background job such as a
roll-up summary recalculation is updating it.[^s1] A periodic background clean-up of deleted-field metadata can later
change the Last Modified Date and Last Modified By values on page layouts, record types and custom objects, which can
puzzle anyone auditing those changes.[^s1] The Delete page also warns that the field's history data is deleted and
changes stop being tracked.[^s1]

**Restoring.** A restored field comes back with its data, but with some differences from the original:[^s2]

- The developer name gains a `_del` suffix, so references that used the old API name need to be pointed at it.[^s2]
- Formula fields return disabled and show `#Error!` until you re-enable them.[^s2]
- Restored fields don't show up in search results right away.[^s2]
- Lead fields that were mapped for lead conversion keep their mappings after the restore.[^s2]
- Auto-number fields keep counting while deleted, so they carry the correct values after the restore.[^s2]

**Hard delete and purge.** After the retention window Salesforce hard-deletes the field and its system data. How long
that takes depends on system demand, and you can track it under Background Jobs in Setup.[^s2][^s3] Once an org reaches
75% of its custom field allocation and has fields ready for hard delete, a **Purge** button appears on the Deleted
Fields page to start the hard delete early. If the status change takes more than 30 seconds, Salesforce emails the
user who clicked Purge.[^s3] The Purge page lists Enterprise, Performance and Unlimited Editions and requires
Customize Application plus View All Data.[^s3]

## Limits and gotchas

- Until the hard delete finishes, a deleted field still counts against the object's custom field allocation and the allocation for its field type.[^s2][^s3]
- Errors such as "Unable to access page" when adding fields can mean deleted fields are holding allocation, and you have to erase some of them.[^s2]
- The Metadata API can delete a field with a `destructiveChanges.xml` manifest in a `deploy()` call. The `purgeOnDelete` option skips the Recycle Bin.[^s4]
- A roll-up summary field deleted through the Metadata API is purged right away, even if `purgeOnDelete` isn't set, so it can't be undeleted.[^s4]
- Fields removed from a released first-generation managed package can't be restored, and their API names can't be reused.[^s5]

## When to use it (and when not)

Undelete is a short safety net for a mistaken delete, not a backup. Salesforce's own decommissioning advice is to
research references, tell users, restrict the field with field-level security and layouts, and watch for a while
before you delete anything. It also says to back up the metadata and data first.[^s6] For anything older than the
15-day window, or for fields deleted through the Metadata API with purge, restore the data from a backup tool such as
`kt:backup-and-recover`.[^s2][^s4]

## Connections

This node is part of the lifecycle of `kt:custom-fields`. It's governed by the per-object custom field allocations
(`kt:custom-field-allocations`), which deleted fields keep using up until they're purged.[^s3] Restoring touches
`kt:formula-fields` (they come back disabled), `kt:auto-number-fields` (they keep counting) and `kt:lead-conversion`
(mappings are kept). Deleting a field ends its `kt:field-history-tracking`.[^s1][^s2] Deletions done as code
go through the `kt:metadata-api` with a `kt:package-xml-manifest` paired with destructive changes, and
`kt:roll-up-summary-field` deletions done that way skip the soft-delete window.[^s4] The irreversible removal of
components from `kt:first-generation-managed-packages` contrasts with the recoverable delete in a regular org.[^s5]

## Sources

[^s1]: Salesforce Help, "Delete a Custom Field". https://help.salesforce.com/s/articleView?id=platform.deleting_fields.htm&language=en_US&type=5 (accessed 2026-11-25)
[^s2]: Salesforce Help, "Manage Deleted Custom Fields". https://help.salesforce.com/s/articleView?language=en_US&id=platform.fields_managing_deleted_fields.htm&type=5 (accessed 2026-11-25)
[^s3]: Salesforce Help, "Purge Deleted Custom Fields". https://help.salesforce.com/s/articleView?language=en_US&id=platform.fields_purge_deleted_fields.htm&type=5 (accessed 2026-11-25)
[^s4]: Salesforce Developers, "Deleting Components from an Organization", Metadata API Developer Guide (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_deploy_deleting_files.htm (accessed 2026-11-25)
[^s5]: Salesforce Developers, "Remove Components from First-Generation Managed Packages". https://developer.salesforce.com/docs/platform/pkg1-dev/guide/packaging-managed-component-deletion.html (accessed 2026-11-25)
[^s6]: Salesforce Developers Blog, "Time to Clean up Those Unneeded Salesforce Customizations" (2017). https://developer.salesforce.com/blogs/2017/01/time-clean-unneeded-salesforce-customizations (accessed 2026-11-25)
