---
id: kt:field-dependencies
type: Feature
title: Field Dependencies
aliases: [field dependency, dependent picklist, dependent picklists, controlling field, controlling picklist, field dependency matrix]
domain: data-model
summary: >-
  A declarative filter that limits the values offered in a dependent picklist or multi-select picklist according to
  the value of a controlling picklist or checkbox on the same record, configured through a field dependency matrix.
release: "Winter '27"
status: current
broader: [kt:custom-fields, kt:data-quality]
related: [kt:record-types, kt:page-layouts, kt:dynamic-forms, kt:validation-rules, kt:lead-conversion]
relations:
  - {predicate: dependsOn, object: kt:field-level-security}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: queriedWith, object: kt:ui-api}
  - {predicate: consumedBy, object: kt:lightning-web-components}
  - {predicate: consumedBy, object: kt:visualforce}
sources:
  - id: s1
    title: "Dependent Picklist Considerations"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.fields_dependent_field_considerations.htm&type=5
    type: official-docs
    accessed: 2026-11-14
  - id: s2
    title: "Dependent Picklists"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.fields_about_dependent_fields.htm&type=5
    type: official-docs
    accessed: 2026-11-14
  - id: s3
    title: "Customize a Salesforce Object: Create Picklists and Field Dependencies"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/customize-a-salesforce-object/picklists-field-dependencies
    type: official-learning
    accessed: 2026-11-14
  - id: s4
    title: "User Interface API Developer Guide: Build UI for Picklists"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.uiapi.meta/uiapi/ui_api_features_records_dependent_picklist.htm
    type: official-docs
    accessed: 2026-11-14
  - id: s5
    title: "Visualforce Developer Guide: Adding Dependent Fields to a Page"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.pages.meta/pages/pages_quick_start_dependent_picklists.htm
    type: official-docs
    accessed: 2026-11-14
  - id: s6
    title: "LWC Developer Guide: getPicklistValues wire adapter"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/reference-wire-adapters-picklist-values
    type: official-docs
    accessed: 2026-11-14
created: 2026-11-14
---

# Field Dependencies

A **field dependency** filters the values a user can pick in one field based on the value of another field on the same record. The field doing the filtering is the **controlling field**; the filtered field is the **dependent field**, usually called a dependent picklist. The standard example is an Opportunity reason picklist whose options change with Stage, or a Zone picklist that only shows zones belonging to the selected Region.[^s2][^s3] Dependent picklists are available in Salesforce Classic and Lightning Experience in all editions.[^s2]

## Which fields can play which role

The two roles accept different field types, and the rules are asymmetric:[^s1][^s2]

- **Controlling field**: a standard or custom picklist, or a checkbox. It must sit on the same record as the dependent field.[^s1][^s2]
- **Dependent field**: a custom picklist or a multi-select picklist. Standard picklists and checkboxes cannot be dependent.[^s1][^s2]
- **Chains**: a custom picklist can be both controlling and dependent, which lets admins build multi-level trees (Country → State → City).[^s1][^s4]

The considerations page caps a controlling field at 300 values, and a field that is both controlling and dependent likewise cannot exceed 300 values.[^s1] Some standard fields can never control a dependency, including activity fields such as Call Type, Subject and Task Type, and lead fields such as Converted and Unread By Owner.[^s1]

## How it works

In Object Manager an admin opens **Fields & Relationships → Field Dependencies → New**, chooses the controlling and dependent fields, and then edits a **field dependency matrix**: controlling values run across the top, dependent values down each column, and each cell is either included or excluded. A Preview button lets the admin test the filtering before saving.[^s2][^s3] Not every controlling value needs a dependent value; saving such a matrix just produces a warning.[^s3] The dependent picklist needs at least one value before a dependency can be defined.[^s1]

Field dependencies interact with **record types**: the record type and the controlling value together decide which dependent values appear, and the record type is set in the Preview dialog of the matrix.[^s1] Deleting a dependency removes only the linking logic; neither field nor any stored data is touched.[^s2]

For custom UIs the dependency is exposed as metadata rather than enforced by the component. The User Interface API marks a dependent field through its `controllingFields` property, returns a `controllerValues` map of controlling values to indexes, and lists on each picklist value a `validFor` array of the controlling indexes for which it is valid.[^s4] Picklist values are scoped to a record type, so the Lightning Web Components `getPicklistValues` adapter requires a `recordTypeId` (the master record type ID if the object has no default).[^s6] Visualforce renders dependencies automatically with `apex:inputField`, but allows at most 10 dependent picklist pairs per page across all objects and fails at runtime if the controlling field is missing from the page.[^s5]

## Limits and gotchas

- **Enforcement gaps**: no dependency check runs when only the controlling field is updated, and the Data Import Wizard ignores dependencies entirely.[^s1]
- **Required dependent fields**: if a required dependent picklist has no valid values for the current controlling value, the record can be saved blank.[^s1]
- **Layouts**: page layouts and Dynamic Forms pages must include the controlling field, or the dependent values do not appear; place the dependent field below its controller.[^s1]
- **Value API names**: dependencies are keyed on picklist value API names, so renaming those names breaks the mapping, and replacing a parent value drops its dependency.[^s1]
- **Security**: field-level security is set independently on each field; hide the controlling field whenever the dependent field is hidden.[^s1][^s4]
- **Existing data**: converting fields into a dependency does not change stored values; the rules apply only to new records and later edits.[^s1]
- **Packaging**: a dependency on a managed controlling picklist can be changed only in the UI, not through the Metadata API.[^s1]

## When to use it (and when not)

Use a field dependency when the valid choices of one categorical field are a fixed function of another on the same record, such as reasons per stage or sub-categories per category; it improves data quality with no code.[^s2][^s3] Because imports and controller-only updates bypass the check, pair it with a **validation rule** when an invalid combination must never be stored.[^s1] When the allowed values vary by business process rather than by another field, record types are the more natural tool, and the two can be combined.[^s1]

## Connections

Field dependencies are a configuration of **custom fields** and a **data quality** control. They are scoped per **record types** and must be paired with the controlling field on **page layouts** and **Dynamic Forms**. Lead mapping requires the same dependency on target fields in **lead conversion**.[^s1] They rely on **field-level security** staying consistent between both fields, are deployed through the **Metadata API** (with the managed-package exception), and are read in custom UIs via the UI API by **Lightning Web Components** and natively by **Visualforce**.[^s1][^s4][^s5][^s6]

## Sources
[^s1]: Salesforce Help, "Dependent Picklist Considerations". https://help.salesforce.com/s/articleView?language=en_US&id=platform.fields_dependent_field_considerations.htm&type=5 (accessed 2026-11-14)
[^s2]: Salesforce Help, "Dependent Picklists". https://help.salesforce.com/s/articleView?language=en_US&id=platform.fields_about_dependent_fields.htm&type=5 (accessed 2026-11-14)
[^s3]: Trailhead, "Customize a Salesforce Object: Create Picklists and Field Dependencies". https://trailhead.salesforce.com/content/learn/projects/customize-a-salesforce-object/picklists-field-dependencies (accessed 2026-11-14)
[^s4]: Salesforce Developers, "User Interface API Developer Guide: Build UI for Picklists". https://developer.salesforce.com/docs/atlas.en-us.uiapi.meta/uiapi/ui_api_features_records_dependent_picklist.htm (accessed 2026-11-14)
[^s5]: Salesforce Developers, "Visualforce Developer Guide: Adding Dependent Fields to a Page". https://developer.salesforce.com/docs/atlas.en-us.pages.meta/pages/pages_quick_start_dependent_picklists.htm (accessed 2026-11-14)
[^s6]: Salesforce Developers, "LWC Developer Guide: getPicklistValues wire adapter". https://developer.salesforce.com/docs/platform/lwc/guide/reference-wire-adapters-picklist-values (accessed 2026-11-14)
