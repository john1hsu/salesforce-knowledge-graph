---
id: kt:custom-fields
type: Feature
title: Custom Fields
aliases: [custom field, __c field, custom field types, Fields & Relationships]
domain: data-model
summary: >-
  Admin-defined fields added to standard or custom objects, each with a data type, a generated API name ending in
  __c, field-level security and layout placement, counted against per-edition and per-object field allocations.
release: "Winter '27"
status: current
broader: [kt:metadata-driven-architecture, kt:standard-objects]
related: [kt:external-id-fields, kt:roll-up-summary-field, kt:object-relationships, kt:page-layouts, kt:field-history-tracking, kt:dynamic-forms]
relations:
  - {predicate: governedBy, object: kt:field-level-security}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: hasPart, object: kt:lookup-vs-master-detail}
  - {predicate: coveredBy, object: kt:platform-app-builder-certification}
sources:
  - id: s1
    title: "Custom Fields Allowed Per Object"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.custom_field_allocations.htm&type=5
    type: official-docs
    accessed: 2026-11-08
  - id: s2
    title: "Custom Field Types"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.custom_field_types.htm&type=5
    type: official-docs
    accessed: 2026-11-08
  - id: s3
    title: "Create a Custom Field"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.adding_fields.htm&type=5
    type: official-docs
    accessed: 2026-11-08
  - id: s4
    title: "Manage Deleted Custom Fields"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.fields_managing_deleted_fields.htm&type=5
    type: official-docs
    accessed: 2026-11-08
  - id: s5
    title: "Understanding Relationship Names, Custom Objects, and Custom Fields — SOQL and SOSL Reference"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-relationships-and-custom-objects.html
    type: official-docs
    accessed: 2026-11-08
  - id: s6
    title: "CustomField — Metadata API Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/customfield.htm
    type: official-docs
    accessed: 2026-11-08
created: 2026-11-08
---

# Custom Fields

A custom field is a field an admin or developer adds to a standard or custom object to capture data the out-of-the-box
schema does not hold. It is created declaratively from the object's **Fields & Relationships** page by choosing a
data type, entering a label and setting attributes; Salesforce derives the field name from the label, and that name
is what merge fields and the APIs use.[^s3] Creating or changing custom fields requires the Customize Application
permission.[^s3]

## How it works

**API names.** Salesforce appends `__c` to every custom object and field name so that custom names can never collide
with standard ones: a field labelled "Mother of Child" is addressed as `Mother_of_Child__c`. In SOQL, a custom
relationship is traversed by its relationship name with `__r` in place of `__c`, both child-to-parent with dot notation
and parent-to-child in a subquery such as `(SELECT LastName__c FROM Daughters__r)`.[^s5]

**Data types.** The type decides storage, validation and behaviour. The catalogue includes Text (up to 255
characters), Text Area (Long) and Text Area (Rich) (up to 131,072 characters), Number, Currency, Percent, Date,
Date/Time, Time, Checkbox, Email (80 characters), Phone (40), URL (255), Picklist and multi-select Picklist, Auto
Number, Geolocation, Address, Formula and Roll-Up Summary, plus the relationship types Lookup, Master-Detail,
Hierarchical (users only), External Lookup and Indirect Lookup.[^s2] Several types carry restrictions worth knowing
up front: Roll-Up Summary needs a custom master-detail relationship and lives on the master side; Formula, Currency,
Geolocation and Rich Text cannot be added to external objects; Text (Encrypted) holds at most 175 characters and uses
Classic Encryption, so Shield orgs should use plain Text with Shield Platform Encryption instead.[^s2] Rounding also
differs by type: Number and Currency round half away from zero, while formulas round ties half up.[^s2]

**The creation wizard.** After the type and attributes (required, lookup filter, deletion behaviour, master-detail
reparenting) come two access steps. In Enterprise, Unlimited, Performance and Developer Editions you set field-level
security per profile, or per permission set if that option is enabled in User Management Settings; then you choose
which page layouts, and which Dynamic Forms-enabled Lightning record pages, should show the field.[^s3] Adding a field
to a large object can touch many records, so big requests are queued and the admin is emailed on completion.[^s3]

## Limits and gotchas

- **Allocations by edition.** Custom fields per object range from a handful in the smallest editions to 500 in
  Enterprise and Developer and 800 in Unlimited and Performance.[^s1] Fields from an AppExchange-certified managed
  package can exceed the edition allocation up to the object's hard limit: 900 for objects such as Account, Contact,
  Case, Lead, Opportunity and custom objects, 800 for most others, and 50 for PriceBookEntry. If the package
  expires, its fields count against the edition allocation again.[^s1]
- **Compound fields count more than once.** A geolocation field consumes three custom fields and a custom address
  field nine.[^s1]
- **Long and rich text.** There is no per-object count limit on these, but all of an object's long and rich text
  area fields share a budget of 1,638,400 characters; reports display only the first 255 characters of such custom
  fields.[^s1][^s2]
- **Activities.** Up to 300 custom activity fields are allowed while the org has fewer than 700 million tasks and
  events; past that threshold, orgs with more than 100 fields cannot add more until activities are archived and
  deleted.[^s1]
- **Deleting is not instant.** A deleted field and its data are kept for up to 15 days and keep counting against
  both the overall field allocation and the allocation for its type until hard-deleted. Restored fields keep a
  `_del` suffix on the developer name, and restored formulas come back disabled until re-saved. Erase, or Purge in
  Performance and Unlimited, starts the hard delete sooner.[^s4]

## When to use it (and when not)

Use a custom field when the attribute belongs to each record of the object and users or integrations need to read,
filter, report or automate on it.[^s3] Check first whether a standard field already fits, and pick the type
deliberately: a Formula or Roll-Up Summary avoids storing derived values, a Picklist backed by a global value set
keeps values consistent, and a relationship field models links between records better than a copied key.[^s2][^s3]
Because allocations are per object and deleted fields linger against them, treat field count as a budget on wide
objects such as Account and Opportunity.[^s1][^s4]

## Connections

Custom fields are the everyday expression of `kt:metadata-driven-architecture`, extending `kt:standard-objects` and
custom objects without schema migrations. Visibility is **governed by** `kt:field-level-security`, set during
creation, and placement is handled by `kt:page-layouts` and `kt:dynamic-forms`.[^s3] Relationship types are the
subject of `kt:object-relationships` and `kt:lookup-vs-master-detail`; `kt:roll-up-summary-field` and
`kt:external-id-fields` are specialised custom fields, and `kt:field-history-tracking` audits changes to them.[^s2]
Fields are addressed in `kt:soql` by their `__c` and `__r` names and their definitions are created, updated and deleted
as the CustomField type of the `kt:metadata-api`;[^s5][^s6] they are core material for the `kt:platform-app-builder-certification`.

## Sources
[^s1]: Salesforce Help, "Custom Fields Allowed Per Object". https://help.salesforce.com/s/articleView?language=en_US&id=platform.custom_field_allocations.htm&type=5 (accessed 2026-11-08)
[^s2]: Salesforce Help, "Custom Field Types". https://help.salesforce.com/s/articleView?language=en_US&id=platform.custom_field_types.htm&type=5 (accessed 2026-11-08)
[^s3]: Salesforce Help, "Create a Custom Field". https://help.salesforce.com/s/articleView?language=en_US&id=sf.adding_fields.htm&type=5 (accessed 2026-11-08)
[^s4]: Salesforce Help, "Manage Deleted Custom Fields". https://help.salesforce.com/s/articleView?language=en_US&id=platform.fields_managing_deleted_fields.htm&type=5 (accessed 2026-11-08)
[^s5]: Salesforce Developers, "Understanding Relationship Names, Custom Objects, and Custom Fields", SOQL and SOSL Reference. https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-relationships-and-custom-objects.html (accessed 2026-11-08)
[^s6]: Salesforce Developers, "CustomField", Metadata API Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/customfield.htm (accessed 2026-11-08)
