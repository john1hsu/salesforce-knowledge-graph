---
id: kt:compact-layouts
type: Feature
title: Compact Layouts
aliases: [compact layout, CompactLayout metadata type, primary compact layout, compact layout assignment]
domain: data-model
summary: >-
  Per-object configuration that picks and orders the key fields shown in a record's highlights panel, expanded
  lookup cards, expanded activity details and the Salesforce mobile app header, assigned as a primary layout per
  object with optional record type overrides.
release: "Winter '27"
status: current
broader: [kt:metadata-driven-architecture]
related: [kt:page-layouts, kt:record-types, kt:lightning-app-builder, kt:activity-data-model, kt:salesforce-mobile-app, kt:custom-objects]
relations:
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: alternativeTo, object: kt:dynamic-forms}
sources:
  - id: s1
    title: "Lightning Experience Customization: Customize Record Highlights with Compact Layouts"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lex_customization/lex_customization_compact_layouts
    type: official-learning
    accessed: 2026-11-21
  - id: s2
    title: "Metadata API Developer Guide: CompactLayout"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_compactlayout.htm
    type: official-docs
    accessed: 2026-11-21
  - id: s3
    title: "Salesforce Mobile App Customization: Customize Compact Layouts"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce1_mobile_app/salesforce1_mobile_app_compact_layouts
    type: official-learning
    accessed: 2026-11-21
  - id: s4
    title: "Lightning Experience Customization for Salesforce Classic Users: Customize the User Interface"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lex_migration_customization/lex_migration_customization_layouts_ui
    type: official-learning
    accessed: 2026-11-21
created: 2026-11-21
---

# Compact Layouts

A compact layout is the per-object setting that chooses which fields users see in the highlights panel at the top of a record, and in what order.[^s1] The same field list is reused in several other compact surfaces: the expanded lookup card that appears when a user hovers over a link in record details, the details section shown when an activity is expanded in the activity timeline, and the record header in the Salesforce mobile app.[^s1][^s4] Where a page layout arranges the full detail and edit page, a compact layout is a short, prioritized summary of the record.

## How it works

**Creating and ordering fields.** Admins build compact layouts from the Compact Layouts related list on an object in Object Manager, add fields, and sort them by priority.[^s4] The first field is shown at the top in a bold or accented font, so Salesforce recommends putting the record's Name field first.[^s1][^s3][^s4] How many fields actually render depends on the surface and screen size: the Lightning highlights panel shows up to the first seven fields (fewer on smaller screens), and a hovered lookup shows the first five.[^s4]

**Assignment.** Every object starts with a read-only System Default compact layout; for a new custom object it contains only the object's name field.[^s1] After creating a custom layout, the admin marks it as the primary compact layout in Compact Layout Assignment.[^s1][^s3] Unlike page layouts, there is no assignment by profile: one compact layout applies to all users of the object.[^s3] When an object has several record types, record type overrides let each record type use a different compact layout.[^s3][^s4]

**Activities.** Task and event compact layouts control what appears in the activity timeline's expanded details. Changing the task compact layout also changes task highlights, task lists and the other places that layout is reused.[^s4]

**As metadata.** In the Metadata API, `CompactLayout` represents a compact layout and extends the base Metadata type, inheriting its `fullName`.[^s2] Its main fields are `fields`, whose order sets display priority, and `label`.[^s2] Compact layouts are defined inside the object's `CustomObject` definition, and the object or record type records which one is assigned through `compactLayoutAssignment`.[^s2] The type is available from API version 29.0, and for external objects from 42.0.[^s2]

## Limits and gotchas

- **Field cap.** Each object's compact layout takes up to 10 fields, including the Name field.[^s3]
- **Unsupported field types.** Text area, long text area, rich text area and multi-select picklist fields can't be added to a compact layout.[^s2][^s3]
- **Display count differs from the cap.** Ten fields can be assigned, but the highlights panel and lookup cards show only the first few, so order matters more than completeness.[^s3][^s4]
- **Caching.** Changes may not appear right away. Refreshing the browser, or switching display density to force a reload, makes them show.[^s1]
- **Dynamic Highlights Panel.** If an org uses the Dynamic Highlights Panel on mobile, the Dynamic Forms and Dynamic Highlights Panel on Mobile setting applies instead of the compact layout.[^s3]

## When to use it (and when not)

Use the compact layout as the default summary of a record everywhere it appears in compact form; it is the one setting that changes highlights, hover cards and mobile headers together across Lightning Experience and the mobile app.[^s4] Use record type overrides when different kinds of records need different key fields.[^s3] When a specific Lightning record page needs its own highlights, or fields should show conditionally, Dynamic Forms with the Dynamic Highlights Panel on that page is the alternative to changing the object-wide compact layout.[^s1]

## Connections

Compact layouts are object configuration within Salesforce's **metadata-driven architecture**, **configured via** the **Metadata API** as the `CompactLayout` type and stored inside each standard, **custom** or external object's definition.[^s2] They sit next to **page layouts**, which still provide the related lists, buttons and actions, while the compact layout supplies the highlights fields.[^s4] They can vary by **record type** through overrides,[^s3] show in pages built in **Lightning App Builder**, drive the expanded activity details tied to the **activity data model**,[^s4] and set the record header in the **Salesforce mobile app**.[^s3] The **Dynamic Forms** and Dynamic Highlights Panel approach is the page-level **alternative**.[^s1]

## Sources

[^s1]: Trailhead, "Lightning Experience Customization: Customize Record Highlights with Compact Layouts". https://trailhead.salesforce.com/content/learn/modules/lex_customization/lex_customization_compact_layouts (accessed 2026-11-21)
[^s2]: Salesforce Developers, "Metadata API Developer Guide: CompactLayout". https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_compactlayout.htm (accessed 2026-11-21)
[^s3]: Trailhead, "Salesforce Mobile App Customization: Customize Compact Layouts". https://trailhead.salesforce.com/content/learn/modules/salesforce1_mobile_app/salesforce1_mobile_app_compact_layouts (accessed 2026-11-21)
[^s4]: Trailhead, "Lightning Experience Customization for Salesforce Classic Users: Customize the User Interface". https://trailhead.salesforce.com/content/learn/modules/lex_migration_customization/lex_migration_customization_layouts_ui (accessed 2026-11-21)
