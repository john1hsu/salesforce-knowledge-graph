---
id: kt:auto-number-fields
type: Feature
title: Auto-Number Fields
aliases: [auto number field, auto-number field type, Auto Number data type, autonumber field, displayFormat, startingNumber]
domain: data-model
summary: >-
  A read-only field type that stamps each new record with a system-generated, incrementing value rendered through a
  display format (prefix, zero-padded number, suffix and optional date tokens), commonly used as a custom object's
  Record Name; values increase but are not guaranteed to be consecutive.
release: "Winter '27"
status: current
broader: [kt:custom-fields]
related: [kt:standard-objects, kt:external-id-fields, kt:formula-fields, kt:data-loader, kt:lead-conversion]
relations:
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: queriedWith, object: kt:soql}
sources:
  - id: s1
    title: "Custom Field Attributes"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.custom_field_attributes.htm&type=5
    type: official-docs
    accessed: 2026-11-20
  - id: s2
    title: "Salesforce Auto-Number Fields Are Not Always Sequential"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000383836&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-20
  - id: s3
    title: "Restart or Reset an Auto-Number Field"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000385217&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-20
  - id: s4
    title: "Change the format of an auto number field on existing records"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000322921&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-20
  - id: s5
    title: "CustomField — Metadata API Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-metadata/references/meta-types/metadata-customfield.html
    type: official-docs
    accessed: 2026-11-20
  - id: s6
    title: "Considerations for Converting the Field Type of a Custom Field"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&amp=&id=notes_on_changing_custom_field_types.htm&type=5
    type: official-docs
    accessed: 2026-11-20
  - id: s7
    title: "Create a Custom Object for Reviews"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/build-a-data-model-for-a-recruiting-app/create-a-custom-object-for-reviews
    type: official-learning
    accessed: 2026-11-20
  - id: s8
    title: "Optimize Customer Data with Standard and Custom Objects"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data_modeling/objects_intro
    type: official-learning
    accessed: 2026-11-20
  - id: s9
    title: "Guidelines for Mapping Custom Lead Fields for Lead Conversion"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&amp=&id=platform.custom_field_types.htm&type=5
    type: official-docs
    accessed: 2026-11-20
created: 2026-11-20
---

# Auto-Number Fields

An auto-number field is a field type whose value the platform assigns when a record is created, incrementing a counter
and rendering it through a display format. Users cannot type into it: Salesforce treats auto-number values as read-only,
and they cannot be set directly through the API or Data Loader.[^s4] The type is best known as the data type of a
record's Name field: an object's name can be free text or auto-numbered, as with a case number such as CA-1024.[^s8]
Trailhead's recruiting-app project, for example, creates a Review object whose Record Name uses the Auto-Number type
with the display format REV-{0000} and a starting number of 1.[^s7]

## How it works

Two settings define the field. The **Display Format** combines an optional prefix and suffix with a `{0}` placeholder
whose zeros set the minimum number of digits, so `{00000}` with a "Sample-" prefix shows values like Sample-00003; date
tokens such as {YYYY}, {MM} and {DD} insert parts of the record's creation date, evaluated in GMT.[^s1] The **Starting
Number** sets the first value and must be below 1 billion.[^s1] A field can hold up to 10 digits plus up to 20 extra
characters of prefix and suffix, which is why field-type conversion treats 30 characters as the maximum length.[^s1][^s6]
When the number outgrows the zero padding, the field simply expands to more digits.[^s3]

When you add an auto-number field to an object that already has data, you can choose to number the existing records
from the starting number; otherwise only records created afterwards receive values.[^s1] Auto-number fields can also be
marked as External IDs, the same attribute offered on text, number and email fields.[^s1][^s5]

In metadata, the field is a `CustomField` with a `displayFormat` and an optional `startingNumber`. The starting number
cannot be retrieved through the Metadata API; to set it on deploy you add the element explicitly, and if it is omitted it
defaults to 1 for custom fields and 0 for standard fields.[^s5] Auto-number is not available on external objects except
through Salesforce Connect's cross-org adapter.[^s5]

## Limits and gotchas

- **Gaps are normal.** Values increase but are not guaranteed to be consecutive; a failed save can burn a number while a parallel save takes the next one, and partial failures in bulk loads widen the gaps.[^s2]
- **No direct reset.** The Starting Number cannot be edited after creation; to restart, convert the field to Text and back to Auto Number, setting a new format and start.[^s1][^s3]
- **Restarts only affect new records** and can produce duplicate values, so pick a start above the highest existing number; fields in managed packages cannot be changed.[^s3][^s4]
- **Format changes are not retroactive.** Changing CASE-{0000} to SR-{00000} leaves existing records in the old format unless you convert to Text, mass-update with Data Loader, and convert back.[^s4]
- **Conversion risk.** Auto Number to Text keeps the data, but converting to any other type loses it, and Text values over 30 characters must be shortened before converting to Auto Number.[^s6]
- **Lead conversion mapping.** A custom lead auto-number field can only be mapped to a Text or Text Area field on the target object.[^s9]

## When to use it (and when not)

Use an auto-number Record Name when records have no natural human-readable name (reviews, line items, requests) and
users need a short reference they can quote.[^s7][^s8] Do not rely on it as a gap-free sequence for legal or financial
numbering such as invoice series: Salesforce states it will never attempt to make the numbers consecutive.[^s2] If you
need a sequence that you control, or need to carry legacy numbers over during a migration, a Text field populated by
your own logic (plus an External ID for matching) is usually the safer design, with the convert-to-text routine
reserved for one-off corrections.[^s4][^s6]

## Connections

Auto-number is one of the **custom field** data types, and the same type underlies standard numbering fields on
**standard objects** such as case numbers.[^s8][^s3] It is deployed as `CustomField` metadata through the **Metadata
API**, and can carry the attribute used by **external ID fields** for matching during upserts.[^s5][^s1] Because its
values are read-only, bulk corrections run through **Data Loader** after a temporary type conversion.[^s4] It is often
compared with **formula fields** that build a display key from other values, and it has specific mapping rules during
**lead conversion**.[^s9] Like any field, its values can be filtered and returned with **SOQL**.

## Sources
[^s1]: Salesforce Help, "Custom Field Attributes". https://help.salesforce.com/s/articleView?language=en_US&id=platform.custom_field_attributes.htm&type=5 (accessed 2026-11-20)
[^s2]: Salesforce Help, "Salesforce Auto-Number Fields Are Not Always Sequential". https://help.salesforce.com/s/articleView?id=000383836&language=en_US&type=1 (accessed 2026-11-20)
[^s3]: Salesforce Help, "Restart or Reset an Auto-Number Field". https://help.salesforce.com/s/articleView?id=000385217&language=en_US&type=1 (accessed 2026-11-20)
[^s4]: Salesforce Help, "Change the format of an auto number field on existing records". https://help.salesforce.com/s/articleView?id=000322921&language=en_US&type=1 (accessed 2026-11-20)
[^s5]: Salesforce Developers, "CustomField — Metadata API Developer Guide". https://developer.salesforce.com/docs/platform/api-metadata/references/meta-types/metadata-customfield.html (accessed 2026-11-20)
[^s6]: Salesforce Help, "Considerations for Converting the Field Type of a Custom Field". https://help.salesforce.com/s/articleView?language=en_US&amp=&id=notes_on_changing_custom_field_types.htm&type=5 (accessed 2026-11-20)
[^s7]: Trailhead, "Create a Custom Object for Reviews". https://trailhead.salesforce.com/content/learn/projects/build-a-data-model-for-a-recruiting-app/create-a-custom-object-for-reviews (accessed 2026-11-20)
[^s8]: Trailhead, "Optimize Customer Data with Standard and Custom Objects". https://trailhead.salesforce.com/content/learn/modules/data_modeling/objects_intro (accessed 2026-11-20)
[^s9]: Salesforce Help, "Guidelines for Mapping Custom Lead Fields for Lead Conversion". https://help.salesforce.com/s/articleView?language=en_US&amp=&id=platform.custom_field_types.htm&type=5 (accessed 2026-11-20)
