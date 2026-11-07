---
id: kt:page-layouts
type: Feature
title: Page Layouts
aliases: [page layout, Layout metadata type, page layout editor, enhanced page layout editor, page layout assignment]
domain: data-model
summary: >-
  Object-level configuration that arranges fields, related lists, buttons, custom links and quick actions on a
  record's detail and edit pages, assigned to users by the combination of profile and record type.
release: "Winter '27"
status: current
broader: [kt:metadata-driven-architecture]
related: [kt:record-types, kt:profiles, kt:business-processes, kt:lightning-app-builder, kt:compact-layouts]
relations:
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: contrastsWith, object: kt:field-level-security}
  - {predicate: alternativeTo, object: kt:dynamic-forms}
sources:
  - id: s1
    title: "Lightning Experience Customization: Customize Record Details with Page Layouts"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/modules/lex_customization/units/lex_customization_page_layouts
    type: official-learning
    accessed: 2026-11-07
  - id: s2
    title: "Tips & Hints for Page Layouts and Field-Level Security"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.salesforce_pagelayouts_cheatsheet.meta/salesforce_pagelayouts_cheatsheet/pagelayouts_cheatsheet.htm
    type: official-docs
    accessed: 2026-11-07
  - id: s3
    title: "Metadata API Developer Guide (API v67.0): Layout"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_layouts.htm
    type: official-docs
    accessed: 2026-11-07
  - id: s4
    title: "Quick Start: Dynamic Forms — Upgrade to Dynamic Forms"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/quick-start-dynamic-forms/upgrade-to-dynamic-forms
    type: official-learning
    accessed: 2026-11-07
  - id: s5
    title: "Lightning Knowledge Setup and Customization: Configure Page Layouts and Record Types"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lightning-knowledge-setup-and-customization/configure-page-layouts-and-record-types
    type: official-learning
    accessed: 2026-11-07
created: 2026-11-07
---

# Page Layouts

A page layout is the per-object configuration that decides what appears on a record's detail and edit pages: which fields show and in what sections, whether each field is read-only or required, and which related lists, standard and custom buttons, custom links and Visualforce related lists are present.[^s2] Admins edit layouts in Setup through Object Manager, using a drag-and-drop editor whose palette offers fields, related lists and Mobile & Lightning Actions; the enhanced page layout editor is on by default.[^s2][^s5] Every object can have several layouts, and Salesforce chooses one for each user from the **page layout assignment** matrix of profile × record type.[^s2]

## How it works

**Assignment.** Layouts are mapped to users by profile and record type. When an admin creates a record type, they make it available to profiles and choose the layout each of those profiles sees; profiles are then given a default record type in their record type settings.[^s5] Salesforce suggests reusing one layout across all profiles within a record type to reduce maintenance.[^s2]

**Editing.** The editor places items by dragging them from the palette into sections; Quick Save stores the layout without leaving the editor, and a preview shows the layout as different profiles would see it, including field-level security effects.[^s1][^s2] A new custom field added to a layout lands as the last field in the first section by default.[^s5] Custom objects start with no related lists; those have to be added on the layout.[^s1]

**In Lightning Experience.** A Lightning record page is built from components in Lightning App Builder. The page layout still supplies the related lists, buttons, links and quick actions that those components render, while the highlights panel takes its fields from a compact layout.[^s1] Actions for Lightning Experience and mobile sit in the layout's Salesforce Mobile and Lightning Experience Actions section.[^s5]

**As metadata.** The `Layout` type (API 13.0 and later) is stored as `.layout` files in a `layouts` folder and named `Object-Layout Name` in `package.xml`, for example `Idea-Idea Layout`; wildcards are supported.[^s3] Key elements are `layoutSections` (one to three columns each), `relatedLists`, `quickActionList`, `platformActionList` (the mobile action bar, API 34.0 and later), `miniLayout` and `excludeButtons`.[^s3] Retrieving layouts together with profiles or permission sets adds the layout assignments to those retrieved components.[^s3]

## Limits and gotchas

- **Field-level security wins.** Field-level security (FLS) overrides any less restrictive setting on a layout. For example, a field marked required on the layout but read-only in FLS is read-only for the user.[^s2]
- **Layouts aren't security.** Where FLS exists (Enterprise, Unlimited, Performance and Developer Editions), use FLS to restrict access and use layouts only to organize the page. In editions without FLS, layouts are the only field control.[^s2] To see why a user can reach a field, check Field Accessibility in Setup.[^s2]
- **Mini layouts inherit.** Mini-layout fields must also be on the main layout and take their read-only or required settings from it.[^s2][^s3]
- **Classic-era features.** `summaryLayout` only controls the Case Feed highlights panel in Salesforce Classic.[^s3] Edit and View button overrides do not apply to mini page layouts.[^s2]

## When to use it (and when not)

Page layouts remain the place to manage related lists, buttons and actions, and the basic field arrangement of every object. Before Dynamic Forms, admins often built several layouts just to show different fields in different situations, which was labour-intensive.[^s4] With Dynamic Forms, the Record Detail component on a Lightning page is upgraded so that fields and sections become individual components with their own visibility filters. During the upgrade, the existing layout is selected as the starting point.[^s1][^s4] Fields hidden this way are only visually hidden and are still available in reports and dashboards.[^s4] Use extra record types and layouts when the business process itself differs. Use Dynamic Forms when only field visibility depends on record data.

## Connections

Page layouts are configuration in Salesforce's **metadata-driven architecture** and are **configured via** the **Metadata API** as the `Layout` type.[^s3] They are selected through **record types** and **profiles**,[^s5] so they sit next to **business processes** in an object's design. They **contrast with field-level security**, which actually enforces field access while layouts only arrange it.[^s2] In Lightning Experience they work alongside **Lightning App Builder** pages and **compact layouts**,[^s1] and **Dynamic Forms** is the Lightning-page **alternative** for arranging record fields.[^s4]

## Sources

[^s1]: Trailhead, "Lightning Experience Customization: Customize Record Details with Page Layouts". https://trailhead.salesforce.com/modules/lex_customization/units/lex_customization_page_layouts (accessed 2026-11-07)
[^s2]: Salesforce Developers, "Tips & Hints for Page Layouts and Field-Level Security". https://developer.salesforce.com/docs/atlas.en-us.salesforce_pagelayouts_cheatsheet.meta/salesforce_pagelayouts_cheatsheet/pagelayouts_cheatsheet.htm (accessed 2026-11-07)
[^s3]: Salesforce Developers, "Metadata API Developer Guide (API v67.0): Layout". https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_layouts.htm (accessed 2026-11-07)
[^s4]: Trailhead, "Quick Start: Dynamic Forms — Upgrade to Dynamic Forms". https://trailhead.salesforce.com/content/learn/projects/quick-start-dynamic-forms/upgrade-to-dynamic-forms (accessed 2026-11-07)
[^s5]: Trailhead, "Lightning Knowledge Setup and Customization: Configure Page Layouts and Record Types". https://trailhead.salesforce.com/content/learn/modules/lightning-knowledge-setup-and-customization/configure-page-layouts-and-record-types (accessed 2026-11-07)
