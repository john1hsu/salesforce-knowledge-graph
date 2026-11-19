---
id: kt:field-sets
type: Feature
title: Field Sets
aliases: [field set, FieldSet metadata type, Schema.FieldSet, fieldSets]
domain: data-model
summary: >-
  An admin-maintained, ordered grouping of an object's fields (FieldSet metadata) that Visualforce pages and Apex read
  dynamically, so the fields a page shows can change in Setup without code changes, including in subscriber orgs of a
  managed package.
release: "Winter '27"
status: current
broader: [kt:visualforce]
related: [kt:custom-fields, kt:page-layouts, kt:dynamic-forms, kt:dynamic-soql, kt:field-level-security, kt:apex-user-mode]
relations:
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: queriedWith, object: kt:tooling-api}
  - {predicate: consumedBy, object: kt:apex}
  - {predicate: consumedBy, object: kt:first-generation-managed-packages}
sources:
  - id: s1
    title: "About Field Sets — Salesforce Help"
    publisher: Salesforce
    url: https://help.salesforce.com/s/articleView?id=fields_about_field_sets.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-19
  - id: s2
    title: "Create and Edit Field Sets — Salesforce Help"
    publisher: Salesforce
    url: https://help.salesforce.com/s/articleView?id=platform.fields_editing_field_sets.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-19
  - id: s3
    title: "Working with Field Sets — Visualforce Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.pages.meta/pages/pages_dynamic_vf_field_sets.htm
    type: official-docs
    accessed: 2026-11-19
  - id: s4
    title: "FieldSet Class — Apex Reference Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_methods_system_fieldsets_describe.htm
    type: official-docs
    accessed: 2026-11-19
  - id: s5
    title: "FieldSetMember Class — Apex Reference Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apex/apex_class_Schema_FieldSetMember.htm
    type: official-docs
    accessed: 2026-11-19
  - id: s6
    title: "FieldSet — Metadata API Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_fieldset.htm
    type: official-docs
    accessed: 2026-11-19
  - id: s7
    title: "FieldSet — Tooling API Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/tooling_api_objects_fieldset.htm
    type: official-docs
    accessed: 2026-11-19
created: 2026-11-19
---

# Field Sets

A field set is a named, ordered group of fields on one object, such as the parts of a person's name plus a job title, that code can iterate over instead of hard-coding field names.[^s1] Field sets exist on every standard object that supports custom fields and in any org that can build Visualforce pages, and only fields exposed in the API can be added to one.[^s1] Their main value is that an administrator can add, remove or reorder the fields a page renders without touching the page's code, which is why they matter most for pages shipped in managed packages.[^s1]

## How it works

Administrators with Customize Application, or delegated administrators, build field sets in the object's management settings with a drag-and-drop editor.[^s1][^s2] Each field set has a label, an API name that pages use to reference it, and a "Where is this used?" description that tells subscribers which pages depend on it.[^s2] The editor has two containers: fields placed **In the Field Set** are shown by default, in their vertical order, while fields in **Available for the Field Set** belong to the set but stay hidden until an admin moves them across.[^s1][^s2] An admin can also mark a field as required within the set, so users must supply a value before saving.[^s2]

In metadata, a field set is the `FieldSet` type (API version 21.0 and later), stored inside its `CustomObject` definition with `displayedFields` and `availableFields` lists of `FieldSetItem` entries; `label` and `description` are both mandatory.[^s6] The Tooling API exposes a read-only `FieldSet` object, added in API version 33.0, with fields such as `DeveloperName`, `NamespacePrefix` and `ManageableState`, which is handy for auditing which field sets came from packages.[^s7]

Visualforce reads a field set through the `$ObjectType` global, for example `$ObjectType.Contact.FieldSets.properNames`, and loops over it with `apex:repeat`; each member exposes `Label`, `Type`, `FieldPath`, `Required` and `DBRequired`.[^s3] In Apex, `fieldSets.getMap()` on an `SObjectType` (or its describe result) returns all field sets for the object, and each `Schema.FieldSet` offers `getFields()`, `getName()`, `getLabel()`, `getDescription()`, `getNamespace()` and `getSObjectType()`.[^s4] Each `Schema.FieldSetMember` returns its label, display type, field token, both required flags and a field path suitable for dynamic SOQL.[^s5]

## Limits and gotchas

- An object can hold up to 2,000 field sets, and one Visualforce page can reference at most 50 of them.[^s3]
- A field set allows at most 25 cross-object spans, and a spanned field can be only one relationship away from the object.[^s2][^s3]
- When a span reaches a field that can point at several objects, only that related record's Name field is reachable.[^s2]
- A field is required either because the field set says so or because the field itself is required, so check both flags.[^s3][^s5]
- Standard controllers load field set fields automatically; a custom controller must add them to its own SOQL query.[^s3]
- Subscribers can add any field type to a packaged set and the page cannot skip fields while looping, so the page must render every type safely.[^s3]
- Admins in a subscriber org can change only the fields inside a field set they did not create, not its other properties.[^s2]

Salesforce's own sample builds the query from each member's field path and runs it with `AccessLevel.USER_MODE`, so the dynamically chosen fields are queried in the running user's context rather than system mode.[^s3][^s4]

## When to use it (and when not)

Field sets fit when code renders a list of fields that admins, or package subscribers, should be able to tune: a packaged Visualforce page, a reusable Apex-driven form, or a dynamic query whose column list should live in Setup.[^s1][^s3] Package developers should put only non-essential fields in a packaged field set, because a subscriber may remove every field from it.[^s3] Field sets are a building block for pages that code renders, such as Visualforce; they do not by themselves change how standard record pages display fields.[^s1]

## Connections

Field sets sit under **Visualforce**, the framework they were designed for, and are consumed by **Apex** through the `Schema.FieldSet` and `Schema.FieldSetMember` describe classes.[^s3][^s4] They are deployed as metadata through the **Metadata API** and inspected through the **Tooling API**.[^s6][^s7] Because member field paths are fed into **dynamic SOQL**, they pair with **user-mode** queries and **field-level security** checks.[^s3][^s5] Their subscriber-editable behaviour makes them a common customization point in **first-generation managed packages**, referenced with the package namespace prefix.[^s3][^s4] They group both standard and **custom fields** that are exposed in the API, and serve a similar purpose for coded pages that **page layouts** and **Dynamic Forms** serve for standard record pages.[^s1][^s2]

## Sources
[^s1]: Salesforce, "About Field Sets — Salesforce Help". https://help.salesforce.com/s/articleView?id=fields_about_field_sets.htm&language=en_US&type=5 (accessed 2026-11-19)
[^s2]: Salesforce, "Create and Edit Field Sets — Salesforce Help". https://help.salesforce.com/s/articleView?id=platform.fields_editing_field_sets.htm&language=en_US&type=5 (accessed 2026-11-19)
[^s3]: Salesforce Developers, "Working with Field Sets — Visualforce Developer Guide". https://developer.salesforce.com/docs/atlas.en-us.pages.meta/pages/pages_dynamic_vf_field_sets.htm (accessed 2026-11-19)
[^s4]: Salesforce Developers, "FieldSet Class — Apex Reference Guide". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_methods_system_fieldsets_describe.htm (accessed 2026-11-19)
[^s5]: Salesforce Developers, "FieldSetMember Class — Apex Reference Guide". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apex/apex_class_Schema_FieldSetMember.htm (accessed 2026-11-19)
[^s6]: Salesforce Developers, "FieldSet — Metadata API Developer Guide". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_fieldset.htm (accessed 2026-11-19)
[^s7]: Salesforce Developers, "FieldSet — Tooling API Developer Guide". https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/tooling_api_objects_fieldset.htm (accessed 2026-11-19)
