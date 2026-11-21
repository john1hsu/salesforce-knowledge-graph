---
id: kt:record-name-field
type: Feature
title: Record Name Field
aliases: [Record Name, Name field, nameField, object name field, isNameField]
domain: data-model
summary: >-
  The one field on each Salesforce object that identifies a record to people: it is the clickable label shown in page
  layouts, related lists, lookups and search results. On a custom object it is defined at creation as either Text or
  Auto Number; a few standard objects such as Contact build it from FirstName and LastName.
release: "Winter '27"
status: current
broader: [kt:custom-objects, kt:standard-objects]
related: [kt:auto-number-fields, kt:custom-fields, kt:person-accounts, kt:formula-fields, kt:external-objects, kt:heroku-connect]
relations:
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: queriedWith, object: kt:sosl}
sources:
  - id: s1
    title: "CustomObject (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/customobject.htm
    type: official-docs
    accessed: 2026-11-21
  - id: s2
    title: "Custom Objects (Object Reference for the Salesforce Platform)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_custom_objects.htm
    type: official-docs
    accessed: 2026-11-21
  - id: s3
    title: "DescribeFieldResult Class (Apex Reference Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_methods_system_fields_describe.htm
    type: official-docs
    accessed: 2026-11-21
  - id: s4
    title: "Create a Custom Object (Create a Custom Object Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/create-a-custom-object-quick-look/create-a-custom-object
    type: official-learning
    accessed: 2026-11-21
  - id: s5
    title: "How I Solved This: Intuitive Record Links"
    publisher: Salesforce Admins
    url: https://admin.salesforce.com/blog/2020/how-i-solved-this-intuitive-record-links
    type: official-blog
    accessed: 2026-11-21
  - id: s6
    title: "Why is my custom object's name field being saved with an ID value in Salesforce?"
    publisher: Heroku Help
    url: https://help.heroku.com/WWC4JRQ6/why-is-my-custom-object-s-name-field-being-saved-with-an-id-value-in-salesforce
    type: official-docs
    accessed: 2026-11-21
created: 2026-11-21
---

# Record Name Field

The record name field (labelled **Record Name** in the custom object wizard, `nameField` in metadata and `Name` in the API) is the field Salesforce uses to identify a record to people. Every custom object must have one, and it is usually a text string or an auto number.[^s1] Its value is what users see in page layouts, related lists, lookup dialogs, search results and the record lists on an object's tab home page.[^s1] The administrator defines it when the object is set up, so it is part of the object's basic shape rather than an optional add-on.[^s2]

## How it works

When you create a custom object in Setup and type its label, the Object Name and Record Name fields fill in automatically from that label; most quick setups keep the defaults and save.[^s4] Underneath, the `CustomObject` metadata type carries a required `nameField` element with its own label and type, for example a label such as "MyFirstObject Name" with type Text.[^s1] By default the name field is placed on the object's page layout as a required field.[^s1] External objects are the exception to the wizard model: their name field can instead be designated by setting `isNameField` to true on one of their custom fields.[^s1]

In code, the field is discoverable through describe calls. Apex's `DescribeFieldResult.isNameField()` returns true for the name field of both standard objects (such as an account's name) and custom objects.[^s3] An object can have only one name field, except where FirstName and LastName are used instead, as on Contact; on a person account the compound Name field also reports as the name field.[^s3] Because the field is a standard field rather than a custom one, `isCustom()` returns false for `Name`.[^s3]

## Text or Auto Number

The choice of data type shapes how users experience the object:

- **Text**: people type a meaningful label (a project title, a location), which makes links readable but, unlike an auto number, does not guarantee uniqueness.[^s1][^s5]
- **Auto Number**: the platform stamps each record with a system-generated value, a read-only, non-createable text field of at most 30 characters.[^s3]

Auto numbers give every record a unique, human-friendly identifier independent of the internal record ID, roughly like a SQL identity column.[^s3] The cost is readability: the auto-number value becomes the link users click on detail pages, related lists and reports, which an official Salesforce Admins article calls unintuitive for end users.[^s5] Its suggested workaround is a text formula field using `HYPERLINK("/"+Id, "View")` that replaces the Name column in related lists and reports.[^s5] See [[auto-number-fields]] for display formats and numbering behaviour.

## Limits and gotchas

- **Blank names**: a record appears in the UI only if its name field is populated; if the API creates a custom-object record without a name, Salesforce uses the record ID as the name.[^s2]
- **Changing the type later** can surprise downstream tools: Heroku Help documents Heroku Connect saving record IDs as names after a name field moved from Auto Number to Text, until the mapping's field metadata was refreshed.[^s6]
- **Required-field behaviour**: when a field is required, API requests that omit it fail with `REQUIRED_FIELD_MISSING`, so integrations must supply a value for a Text name field.[^s2]
- **Searchability is separate**: a new custom object (API 35.0 and later) is not searchable by default, so a good name does not by itself make records findable in search.[^s1]

## When to use which

Choose Text when users naturally identify records by a label they would type anyway, because that label becomes the link they click everywhere.[^s1][^s5] Choose Auto Number for records with no natural name, where a guaranteed-unique identifier matters more than a readable link, and consider a formula-field link if users find the number confusing.[^s3][^s5] Decide early: integrations and mappings cache the field's type, so switching later has knock-on effects.[^s6]

## Connections

The name field is a defining part of every [[custom-objects]] definition and of most [[standard-objects]], and it is configured through the [[metadata-api]] `nameField` element.[^s1] When it uses the Auto Number type it overlaps with [[auto-number-fields]]; otherwise it behaves like other text [[custom-fields]].[^s3] [[person-accounts]] and Contact show the compound-name exception to the one-name-field rule.[^s3] [[formula-fields]] offer the common workaround for unreadable auto-number links.[^s5] [[external-objects]] choose their name field with `isNameField`.[^s1] Its values are read with [[soql]] and, once search is enabled, found with [[sosl]].[^s1] Integrations such as [[heroku-connect]] cache its type, so type changes need a metadata refresh.[^s6]

## Sources

[^s1]: Salesforce Developers, "CustomObject (Metadata API Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/customobject.htm (accessed 2026-11-21)
[^s2]: Salesforce Developers, "Custom Objects (Object Reference for the Salesforce Platform)". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_custom_objects.htm (accessed 2026-11-21)
[^s3]: Salesforce Developers, "DescribeFieldResult Class (Apex Reference Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_methods_system_fields_describe.htm (accessed 2026-11-21)
[^s4]: Trailhead, "Create a Custom Object". https://trailhead.salesforce.com/content/learn/modules/create-a-custom-object-quick-look/create-a-custom-object (accessed 2026-11-21)
[^s5]: Salesforce Admins, "How I Solved This: Intuitive Record Links". https://admin.salesforce.com/blog/2020/how-i-solved-this-intuitive-record-links (accessed 2026-11-21)
[^s6]: Heroku Help, "Why is my custom object's name field being saved with an ID value in Salesforce?". https://help.heroku.com/WWC4JRQ6/why-is-my-custom-object-s-name-field-being-saved-with-an-id-value-in-salesforce (accessed 2026-11-21)
