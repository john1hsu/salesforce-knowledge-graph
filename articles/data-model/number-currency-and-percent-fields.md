---
id: kt:number-currency-and-percent-fields
type: Feature
title: Number, Currency, and Percent Fields
aliases: [number field, currency field, percent field, numeric field types, numeric custom fields, decimal places setting]
domain: data-model
summary: >-
  The three numeric custom field data types on the Salesforce platform: Number for plain values, Currency for money
  amounts and Percent for ratios, each configured with a length (digits left of the decimal point) and decimal places,
  and all exposed to the API as type double.
release: "Winter '27"
status: current
broader: [kt:custom-fields]
related: [kt:multiple-currencies, kt:formula-fields, kt:roll-up-summary-field, kt:external-id-fields, kt:field-type-conversion]
relations:
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: consumedBy, object: kt:apex}
sources:
  - id: s1
    title: "Custom Field Types"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.custom_field_types.htm&type=5
    type: official-docs
    accessed: 2026-11-25
  - id: s2
    title: "Custom Field Attributes"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.custom_field_attributes.htm&type=5
    type: official-docs
    accessed: 2026-11-25
  - id: s3
    title: "Primitive Data Types — Object Reference for the Salesforce Platform"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/primitive_data_types.htm
    type: official-docs
    accessed: 2026-11-25
  - id: s4
    title: "Field Types — Object Reference for the Salesforce Platform"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/object-reference/guide/field-types.html
    type: official-docs
    accessed: 2026-11-25
  - id: s5
    title: "Custom Fields — Object Reference for the Salesforce Platform"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/custom_fields.htm
    type: official-docs
    accessed: 2026-11-25
  - id: s6
    title: "CustomField — Metadata API Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-metadata/references/meta-types/metadata-customfield.html
    type: official-docs
    accessed: 2026-11-25
  - id: s7
    title: "Decimal Class — Apex Reference Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_methods_system_decimal.htm
    type: official-docs
    accessed: 2026-11-25
created: 2026-11-25
---

# Number, Currency, and Percent Fields

Salesforce offers three numeric data types for custom fields. **Number** holds a plain numeric value, **Currency** lets
users enter a money amount, and **Percent** stores a ratio that users type as a decimal (0.10) and see as a percentage
(10%).[^s1] All three share the same two sizing attributes, and at the API level they are one type: the object
reference states that every numeric custom field is handled as a double, and that non-integer values such as currency
and percent are transmitted as doubles, with the currency symbol or percent sign added only on display.[^s3][^s5]

## How it works

When you create one of these fields you set a **Length**, which is the number of digits allowed to the left of the
decimal point, and **Decimal Places**, the number of digits allowed to the right; the platform rounds entries that
exceed the decimal setting, so 4.986 in a two-place field becomes 4.99.[^s2] The API describes the same limits in
different terms: `precision` is the total number of digits and `scale` the digits after the decimal point, so the
digits available on the left equal precision minus scale. The object reference notes that the setup UI uses
"precision" to mean only the left-hand digits, a frequent source of confusion.[^s3] In Metadata API a numeric field is
a `CustomField` whose `precision` and `scale` carry these values; 256.99 has a precision of 5 and a scale of 2.[^s6]

Rounding is defined per type. Number fields round half away from zero, so 12.345 becomes 12.35 and -13.5 becomes -14,
and leading zeros are stripped from entered values.[^s1] Currency fields with one or more decimal places use the same
half-away-from-zero rule, but a currency field with zero decimal places truncates, so 23.5 is stored as 23.[^s1]
Currency and Percent values both lose precision beyond 15 decimal places.[^s1] In orgs with multiple currencies
enabled, objects with currency fields also carry a `CurrencyIsoCode` field that records which currency each amount is
in.[^s4]

In Apex, numeric fields surface as `Decimal` values whose scale comes from the field returned by the query. Arithmetic
in code can produce more digits than the field holds, so `setScale` (half-even by default, or with an explicit
`RoundingMode`) is the usual way to match a field's decimal places before saving.[^s7]

## Limits and gotchas

- **Lightning stores more than it shows.** On custom objects, Lightning Experience can store more decimals than defined: 90.678 in a two-place field displays as 90.68 but is stored as entered, while Salesforce Classic saves 90.68.[^s1]
- **Shrinking length does not rewrite data.** Reducing a field's digits can truncate values in Classic but leaves them unchanged in Lightning, so the two interfaces can show different numbers for the same record.[^s2]
- **Percent input is a fraction.** Users enter 0.10 for 10%, and typing more than 15 decimal places with a percent sign raises a runtime error.[^s1]
- **Merge fields ignore decimal places.** Numbers in merge fields round by the user's locale rather than the field's configured decimal places.[^s1]
- **Only Number can be an External ID.** External IDs are limited to 25 auto-number, email, number or text fields per object; Currency and Percent are not eligible.[^s2][^s6]
- **Currency is not available on external objects**, except through the cross-org adapter for Salesforce Connect.[^s1][^s6]

## When to use it (and when not)

Use **Currency** for any monetary amount, because only it participates in currency symbols and, in multi-currency
orgs, per-record ISO codes and conversion.[^s3][^s4] Use **Percent** for rates, discounts and probabilities so users
see a percent sign, but remember that integrations and formulas work with the underlying decimal value.[^s1][^s3] Use
**Number** for counts, scores and quantities, and when the value must serve as an External ID for upserts.[^s2] A
value that is never used in arithmetic, such as a postal or account code with meaningful leading zeros, belongs in a
Text field, because Number removes leading zeros.[^s1] Derived values are better as formula or roll-up summary fields
than as numeric fields kept in sync by automation, and note that formula results use round-half-up rather than
the Number type's half-away-from-zero rule.[^s1]

## Connections

These types are a subset of **custom fields** and share the Decimal Places attribute with geolocation fields.[^s2]
They are defined as `CustomField` metadata through the **Metadata API**, read and filtered with **SOQL**, and consumed
as `Decimal` values in **Apex**.[^s6][^s3][^s7] Currency fields depend on **multiple currencies** settings for their
ISO code behavior, Number fields can act as **external ID fields**, and numeric
fields are the usual inputs and outputs of **formula fields** and **roll-up summary fields**.[^s2][^s4][^s1] Changing
one of these types, or its length, is governed by the caveats of **field type conversion**.[^s2]

## Sources
[^s1]: Salesforce Help, "Custom Field Types". https://help.salesforce.com/s/articleView?language=en_US&id=platform.custom_field_types.htm&type=5 (accessed 2026-11-25)
[^s2]: Salesforce Help, "Custom Field Attributes". https://help.salesforce.com/s/articleView?language=en_US&id=platform.custom_field_attributes.htm&type=5 (accessed 2026-11-25)
[^s3]: Salesforce Developers, "Primitive Data Types — Object Reference for the Salesforce Platform". https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/primitive_data_types.htm (accessed 2026-11-25)
[^s4]: Salesforce Developers, "Field Types — Object Reference for the Salesforce Platform". https://developer.salesforce.com/docs/platform/object-reference/guide/field-types.html (accessed 2026-11-25)
[^s5]: Salesforce Developers, "Custom Fields — Object Reference for the Salesforce Platform". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/custom_fields.htm (accessed 2026-11-25)
[^s6]: Salesforce Developers, "CustomField — Metadata API Developer Guide". https://developer.salesforce.com/docs/platform/api-metadata/references/meta-types/metadata-customfield.html (accessed 2026-11-25)
[^s7]: Salesforce Developers, "Decimal Class — Apex Reference Guide". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_methods_system_decimal.htm (accessed 2026-11-25)
