---
id: kt:dynamic-forms
type: Feature
title: Dynamic Forms
aliases: [Dynamic Forms for Lightning record pages, Field Section component, field sections, Dynamic Forms migration wizard]
domain: data-model
summary: >-
  A Lightning App Builder capability that replaces the monolithic Record Detail component with individual Field and
  Field Section components, so record-page fields can be placed, made required or read-only, and shown or hidden by
  visibility rules without the page layout editor.
release: "Winter '27"
status: current
broader: [kt:lightning-app-builder, kt:page-layouts]
related: [kt:custom-fields, kt:record-types, kt:profiles, kt:field-level-security, kt:dynamic-actions, kt:dynamic-highlights-panel]
relations:
  - {predicate: alternativeTo, object: kt:page-layouts}
  - {predicate: dependsOn, object: kt:lightning-web-components}
  - {predicate: contrastsWith, object: kt:field-level-security}
  - {predicate: coveredBy, object: kt:platform-app-builder-certification}
sources:
  - id: s1
    title: "Lightning App Builder: Get Started with Dynamic Forms"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lightning_app_builder/get-started-with-dynamic-forms-lab
    type: official-learning
    accessed: 2026-11-09
  - id: s2
    title: "Dynamic Forms Limitations"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.dynamic_forms_limitations.htm&type=5
    type: official-docs
    accessed: 2026-11-09
  - id: s3
    title: "Dynamic Forms Tips and Considerations"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.dynamic_forms_considerations.htm&type=5
    type: official-docs
    accessed: 2026-11-09
  - id: s4
    title: "Break Up Your Record Details with Dynamic Forms"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2019/break-up-your-record-details-with-dynamic-forms
    type: official-blog
    accessed: 2026-11-09
  - id: s5
    title: "3 Ways to Drive Productivity with Dynamic Forms"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2023/3-ways-to-drive-productivity-with-dynamic-forms
    type: official-blog
    accessed: 2026-11-09
created: 2026-11-09
---

# Dynamic Forms

Dynamic Forms extends Lightning App Builder so admins configure a record page's fields and sections directly in the builder. Instead of one Record Detail component that renders whatever the assigned page layout contains, the page is built from separate Field Section and Field components that can sit anywhere on the canvas, including inside tabs and accordions.[^s1] The goal is to tame layouts with very many fields and to show different users only the fields they need without multiplying layouts.[^s1]

## How it works

Enabling Dynamic Forms adds a Fields tab to the builder's component pane, containing a Field Section component and the object's fields. Sections get custom labels, and fields are dragged into them; lookup fields can be drilled into to place cross-object fields from the related record.[^s1] Each Field can be marked required or read-only on the page, and both fields and sections accept visibility rules.[^s5] Filters can use record values (for example, show a shipping section only when status is Purchased), the user's profile via advanced filters, or device type.[^s5]

A key architectural shift is the assignment model. Classic Lightning record pages require assigning both a Lightning page and a page layout; with Dynamic Forms the Lightning page alone controls field placement, so visibility rules can replace some layouts and record-type variations.[^s4][^s1]

## Adoption history

Dynamic Forms was announced in 2019 and was a non-GA preview for custom objects in Summer '20, when field components were desktop-only and phone users relied on a Record Detail – Mobile component.[^s4] Standard object support began with account, contact and opportunity in Winter '23, and Winter '24 brought general availability across LWC-enabled standard objects and on mobile, where it is switched on from the Salesforce Mobile App area of Setup.[^s5]

## Migrating an existing page

Selecting the Record Detail component and clicking **Upgrade Now** launches a wizard that copies a chosen page layout's fields and sections into field sections and removes Record Detail.[^s1] The wizard migrates only fields, sections with fields and layout save options; custom links and blank spaces don't come across, and some save options must be reset by hand.[^s2] Universally required fields that weren't on the source layout are not added, so records can't be saved until they are placed on the page.[^s1]

## Limits and gotchas

- A Field Section holds up to 100 fields per column, blank spaces count toward it, and each column counts as a component (a two-column section counts as three).[^s2]
- Migration carries up to 100 sections per region and 100 fields per column; anything beyond is dropped, even required fields.[^s2]
- Not every object is supported: if the Fields tab is missing, the object isn't; Note has a fixed layout, and non-LWC-enabled objects such as Products, Events and Tasks still use page layouts.[^s2]
- Several surfaces still read the page layout: list-view inline edit, path key fields, opportunity Clone with Related, and some child-record creation from related lists.[^s2]
- Field visibility rules re-evaluate while the user edits, but section rules apply only after save; edits to a field while it is hidden are not saved.[^s3]
- Keep Record Detail and field sections off the same page, and avoid several instances of one field with differing visibility or required settings.[^s3]
- Admins without a managed package's license don't see its fields in the palette, and saving the page removes them.[^s2]

## When to use it (and when not)

Use Dynamic Forms for LWC-enabled objects whose record pages need conditional fields, per-page required or read-only behaviour, or fields spread across tabs for faster loading.[^s1][^s5] Hidden fields still hold data that shows in reports, list views and dashboards, so visibility rules are a usability tool, not a security control.[^s3] Page layouts remain necessary for unsupported objects and for surfaces that ignore Dynamic Forms.[^s2]

## Connections

Dynamic Forms is a capability of `kt:lightning-app-builder` and the successor approach to field placement in `kt:page-layouts`, which it can reduce but not eliminate.[^s4][^s2] It works on fields defined as `kt:custom-fields` or standard fields, and visibility rules can collapse variations once handled by `kt:record-types` and `kt:profiles`.[^s4][^s5] Unlike `kt:field-level-security`, hiding a field does not restrict access to its data.[^s3] Support is tied to LWC-enabled record pages built on `kt:lightning-web-components`.[^s2] Its siblings are `kt:dynamic-actions`, which supply actions on custom objects, and `kt:dynamic-highlights-panel`, which holds up to 12 key fields.[^s3][^s1] It is core material for the `kt:platform-app-builder-certification`.[^s1]

## Sources

[^s1]: Trailhead, "Lightning App Builder: Get Started with Dynamic Forms". https://trailhead.salesforce.com/content/learn/modules/lightning_app_builder/get-started-with-dynamic-forms-lab (accessed 2026-11-09)
[^s2]: Salesforce Help, "Dynamic Forms Limitations". https://help.salesforce.com/s/articleView?language=en_US&id=platform.dynamic_forms_limitations.htm&type=5 (accessed 2026-11-09)
[^s3]: Salesforce Help, "Dynamic Forms Tips and Considerations". https://help.salesforce.com/s/articleView?language=en_US&id=platform.dynamic_forms_considerations.htm&type=5 (accessed 2026-11-09)
[^s4]: Salesforce Admins Blog, "Break Up Your Record Details with Dynamic Forms". https://admin.salesforce.com/blog/2019/break-up-your-record-details-with-dynamic-forms (accessed 2026-11-09)
[^s5]: Salesforce Admins Blog, "3 Ways to Drive Productivity with Dynamic Forms". https://admin.salesforce.com/blog/2023/3-ways-to-drive-productivity-with-dynamic-forms (accessed 2026-11-09)
