---
id: kt:field-type-conversion
type: Feature
title: Field Type Conversion
aliases: [change field type, Change Field Type, converting custom field data type, custom field type change]
domain: data-model
summary: >-
  The Setup action that changes the data type of an existing custom field (for example Text to Picklist), which
  Salesforce applies to every stored value in the background and which can truncate, remap or erase data depending
  on the source and target types.
release: "Winter '27"
status: current
broader: [kt:custom-fields]
related: [kt:picklist-value-sets, kt:auto-number-fields, kt:rich-text-area-fields, kt:multi-select-picklists, kt:external-id-fields]
relations:
  - {predicate: dependsOn, object: kt:lookup-vs-master-detail}
  - {predicate: consumedBy, object: kt:change-data-capture}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: contrastsWith, object: kt:formula-fields}
sources:
  - id: s1
    title: "Considerations for Converting the Field Type of a Custom Field"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.notes_on_changing_custom_field_types.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-24
  - id: s2
    title: "Convert a Text Field to a Picklist Field"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=platform.fields_converting_field_to_picklist.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-24
  - id: s3
    title: "Salesforce Error: 'Can't change the data type because it's referenced in the following Flows'"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000387461&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-24
  - id: s4
    title: "Conversions That Generate a Change Event (Change Data Capture Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/change-data-capture/guide/cdc-field-conversion-single-event.html
    type: official-docs
    accessed: 2026-11-24
  - id: s5
    title: "Conversions That Don't Generate Events (Change Data Capture Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_field_conversion_no_events.htm
    type: official-docs
    accessed: 2026-11-24
created: 2026-11-24
---

# Field Type Conversion

Field type conversion is the **Change Field Type** button on a custom field's detail page in Setup. It rewrites the
field's data type in place while keeping its API name, so references by name survive, but Salesforce must also
transform every value already stored in that field.[^s1][^s2] Whether those values survive depends on the pair of
types involved, which is why Salesforce's guidance is to convert only fields that hold no data, or to back the data up
first.[^s1]

## How it works

From the object's Fields list you edit the field, choose Change Field Type, pick the new type, then supply the label,
name and type-specific attributes and save.[^s2] The conversion itself runs asynchronously. Its duration depends on the
field's size, the number of records and the kind of conversion; some take longer than 24 hours, and when the job is
queued Salesforce emails you when it completes.[^s1]

Conversions fall into three broad groups:

- **Lossless or widening**: Text Area, Email, URL, Phone, Auto Number, Number, Percent or Currency to Text, and Text to the text-like types.[^s5]
- **Truncating**: Long Text Area to Email, Phone, Text, Text Area or URL keeps only the first 255 characters of each value.[^s1]
- **Destructive**: to or from Date or Date/Time, from Checkbox, from or to Multi-Select Picklist, from Auto Number (except to Text), and to Number, Percent or Currency.[^s1]

Some conversions remap rather than copy. Picklist to Checkbox asks which values map to checked, Picklist to
Multi-Select keeps existing selections, and a Text to Picklist conversion turns distinct text values into picklist
values.[^s1][^s2] Rich text can only become a Long Text Area; the markup stays hidden in each record until it is next
saved, at which point inline images are dropped.[^s1]

## Limits and gotchas

- **Picklist value cap.** Text to Picklist fails if the field has more than 4,000 unique values; the count is case-insensitive and includes active and soft-deleted values until the Recycle Bin is emptied.[^s2]
- **Referenced fields are locked.** A field used in Visualforce, Apex, processes or flows can't change type; for flows, deactivating isn't enough, and you must remove the reference, save a new version and delete the old one.[^s1][^s3]
- **Blocked types.** Formula fields can't be converted either way, encrypted fields can't change type, fields mapped for lead conversion are locked, and a unique text field can't become a picklist.[^s1][^s2]
- **External IDs.** Changing an external ID field to anything other than text, number or email removes its external ID behavior.[^s1]
- **Side effects of data loss.** When values are lost, list views filtered on the field are deleted, and assignment and escalation rules may be affected.[^s1]
- **Relationship fields.** Lookup to master-detail fails if any record has a blank value and sets the child's sharing to Controlled by Parent; master-detail can't become a lookup once a roll-up summary exists.[^s1]
- **Deployment scale.** A metadata `deploy()` or package upgrade can fail with a data type error once total value conversions exceed 85 million (records times converted fields).[^s1]
- **Auto Number length.** Text values longer than 30 characters must be shortened before a field can become an Auto Number.[^s1]

## Change Data Capture behavior

Downstream subscribers see conversions differently. Destructive conversions (Date or Date/Time, Checkbox, or
Multi-Select Picklist sources) null the field on all records and publish a single change event whose `recordIds`
header holds a wildcard of the object's key prefix plus an asterisk, such as `001*` for Account.[^s4] Lossless,
truncating and Picklist-to-Text or Text-to-Picklist conversions publish no change or gap events, so replicas must be
reconciled another way.[^s5]

## When to use it (and when not)

Conversion is appropriate early in a field's life, or for the widening and remapping paths above where data is kept.[^s1][^s5]
For a field with valuable data and a destructive path, a safer pattern is to create a new field of the target type,
migrate values with your own transformation, repoint automation and retire the old field, because the platform's
in-place conversion offers no preview or rollback.[^s1] Plan around flows and code first, since references block the
change outright.[^s3]

## Connections

Field type conversion is an operation on **custom fields** and interacts with specific types: **picklist value sets**
and **multi-select picklists** through value limits and remapping, **auto-number fields** through the Text round-trip,
**rich text area fields** through the one-way path to long text, and **external ID fields**, which lose their role
outside text, number or email.[^s1][^s2] It depends on the **lookup vs. master-detail** rules when relationship fields
change, contrasts with **formula fields**, which can't be converted, is applied at scale through **Metadata API**
deployments, and is visible to **Change Data Capture** subscribers only for destructive conversions.[^s1][^s4][^s5]

## Sources

[^s1]: Salesforce Help, "Considerations for Converting the Field Type of a Custom Field". https://help.salesforce.com/s/articleView?id=sf.notes_on_changing_custom_field_types.htm&language=en_US&type=5 (accessed 2026-11-24)
[^s2]: Salesforce Help, "Convert a Text Field to a Picklist Field". https://help.salesforce.com/s/articleView?id=platform.fields_converting_field_to_picklist.htm&language=en_US&type=5 (accessed 2026-11-24)
[^s3]: Salesforce Help, "Salesforce Error: 'Can't change the data type because it's referenced in the following Flows'". https://help.salesforce.com/s/articleView?id=000387461&language=en_US&type=1 (accessed 2026-11-24)
[^s4]: Salesforce Developers, "Conversions That Generate a Change Event". https://developer.salesforce.com/docs/platform/change-data-capture/guide/cdc-field-conversion-single-event.html (accessed 2026-11-24)
[^s5]: Salesforce Developers, "Conversions That Don't Generate Events". https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_field_conversion_no_events.htm (accessed 2026-11-24)
