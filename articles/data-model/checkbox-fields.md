---
id: kt:checkbox-fields
type: Feature
title: Checkbox Fields
aliases: [checkbox field, boolean field, Checkbox data type, checkbox formula]
domain: data-model
summary: >-
  The custom field type that stores a single true (checked) or false (unchecked) attribute on a record, exposed to the
  APIs as a boolean and also available as a formula return type.
release: "Winter '27"
status: current
broader: [kt:custom-fields]
related: [kt:formula-fields, kt:approval-processes, kt:external-id-fields, kt:validation-rules, kt:data-import-wizard]
relations:
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: consumedBy, object: kt:lightning-web-components}
  - {predicate: configuredVia, object: kt:metadata-api}
sources:
  - id: s1
    title: "Custom Field Types"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.custom_field_types.htm&amp=&type=5
    type: official-docs
    accessed: 2026-11-27
  - id: s2
    title: "Custom Field Attributes"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.custom_field_attributes.htm&type=5
    type: official-docs
    accessed: 2026-11-27
  - id: s3
    title: "Default Field Values"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.fields_about_default_field_values.htm&type=5
    type: official-docs
    accessed: 2026-11-27
  - id: s4
    title: "Get Started with Formulas"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/quick-data-insights-with-formulas/get-started-with-formulas
    type: official-learning
    accessed: 2026-11-27
  - id: s5
    title: "Primitive Data Types — Object Reference for the Salesforce Platform"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/primitive_data_types.htm
    type: official-docs
    accessed: 2026-11-27
  - id: s6
    title: "Input Field — Lightning Component Reference"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-input-field.html
    type: official-docs
    accessed: 2026-11-27
  - id: s7
    title: "How to Create a Salesforce Report on Records Submitted for Approval Using a Custom Checkbox Field"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000387774&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-27
  - id: s8
    title: "CustomField — Metadata API Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/customfield.htm
    type: official-docs
    accessed: 2026-11-27
created: 2026-11-27
---

# Checkbox Fields

A checkbox field is the custom field type that lets a user tick a box to record a true or false attribute of a record, such as whether a deal is "hot" or whether a record has been submitted for approval.[^s1][^s4] It is the simplest data type in the platform's field catalog: a checked box means true and an unchecked box means false.[^s1] Under the hood the APIs treat it as the `boolean` primitive, whose values are true (or 1) and false (or 0).[^s5]

## How it works

When an admin creates a checkbox in Setup, the Default Value attribute asks for **Checked** or **Unchecked** rather than a free-text value.[^s2][^s3] Like other default field values, that choice is applied once, when the record is created; afterwards users can change it freely, so a default is a starting state and not a constraint.[^s3]

Different tools express the two states differently. Reports and list view filters use the words True and False, while the Data Import Wizard and the weekly data export represent checked as 1 and unchecked as 0.[^s1] The API boolean type accepts either spelling, true/false or 1/0.[^s5] A typical report pattern is a filter such as "Submitted for Approval equals True", where an approval process field update sets the checkbox when a record enters approval; Salesforce's own support article uses exactly that design to report on pending submissions.[^s7]

On Lightning record forms, `lightning-input-field` renders a Checkbox field as a checkbox input, and a read-only checkbox cannot receive keyboard focus.[^s6] Requiredness for any field can come from the server-side Required setting in Setup or from the component's client-side `required` attribute.[^s6]

## Checkbox formulas

Checkbox is also one of the return types for formula fields: a formula of this type evaluates to true (checked) or false (unchecked), and Trailhead's example is a "Hot" flag on opportunities derived from other field values.[^s4] This is often better than a stored checkbox kept in sync by automation, because the value is always calculated. The trade-off is that formula fields are calculated and so cannot be used as search criteria.[^s4]

## Limits and gotchas

- **Not an external ID.** The External ID attribute is limited to auto-number, email, number and text fields, so a checkbox cannot serve as an upsert key.[^s2][^s8]
- **Legacy index flag.** The Metadata API `CustomField` type once had a checkbox-only property that built true values into an index, but it exists only in API version 14.0 and earlier.[^s8]
- **Defaults don't enforce.** Because defaults apply only at creation, a rule such as "must be checked before closing" belongs in a validation rule, not in the default value.[^s3]
- **Mind the representation.** When loading data, map checkbox columns to 1/0 or true/false consistently with the tool you use.[^s1][^s5]

## When to use it (and when not)

Use a checkbox for a genuinely binary fact that users or automation set directly. If the flag can be derived from other fields, prefer a checkbox formula so it never drifts.[^s4] If the answer can be unknown, or might grow beyond two states, a picklist is a safer choice, because a checkbox only ever records checked or unchecked.[^s1]

## Connections

Checkbox fields are a kind of **custom field** and share the default-value and attribute model of the other field types.[^s2][^s3] They are a common **formula field** return type and a common target of **approval process** field updates, as in the submitted-for-approval report pattern.[^s4][^s7] Their 1/0 representation matters when loading data with the **Data Import Wizard**, and they cannot be **external ID fields**.[^s1][^s2] Enforcement rules belong in **validation rules**.[^s3] Developers query them with **SOQL** as booleans, render them in **Lightning web components** through `lightning-input-field`, and define them in source through the **Metadata API** `CustomField` type.[^s5][^s6][^s8]

## Sources

[^s1]: Salesforce Help, "Custom Field Types". https://help.salesforce.com/s/articleView?language=en_US&id=sf.custom_field_types.htm&amp=&type=5 (accessed 2026-11-27)
[^s2]: Salesforce Help, "Custom Field Attributes". https://help.salesforce.com/s/articleView?language=en_US&id=platform.custom_field_attributes.htm&type=5 (accessed 2026-11-27)
[^s3]: Salesforce Help, "Default Field Values". https://help.salesforce.com/s/articleView?language=en_US&id=platform.fields_about_default_field_values.htm&type=5 (accessed 2026-11-27)
[^s4]: Trailhead, "Get Started with Formulas". https://trailhead.salesforce.com/content/learn/modules/quick-data-insights-with-formulas/get-started-with-formulas (accessed 2026-11-27)
[^s5]: Salesforce Developers, "Primitive Data Types". https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/primitive_data_types.htm (accessed 2026-11-27)
[^s6]: Salesforce Developers, "Input Field — Lightning Component Reference". https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-input-field.html (accessed 2026-11-27)
[^s7]: Salesforce Help, "How to Create a Salesforce Report on Records Submitted for Approval Using a Custom Checkbox Field". https://help.salesforce.com/s/articleView?id=000387774&language=en_US&type=1 (accessed 2026-11-27)
[^s8]: Salesforce Developers, "CustomField — Metadata API Developer Guide". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/customfield.htm (accessed 2026-11-27)
