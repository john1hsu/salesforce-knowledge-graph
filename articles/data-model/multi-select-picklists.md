---
id: kt:multi-select-picklists
type: Feature
title: Multi-Select Picklists
aliases: [multi-select picklist, multiselect picklist, multi-picklist, MultiselectPicklist, MSP]
domain: data-model
summary: >-
  A custom field type that lets a user choose one or more values from a defined list, stored on the record as a
  single semicolon-separated string. Convenient for tagging, but harder to report on, automate and integrate than
  single-select picklists or related records.
release: "Winter '27"
status: current
broader: [kt:custom-fields]
related: [kt:picklist-value-sets, kt:field-dependencies, kt:junction-object, kt:formula-fields, kt:data-quality]
relations:
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: alternativeTo, object: kt:junction-object}
sources:
  - id: s1
    title: "Picklist Limitations"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.picklist_limitations.htm&type=5
    type: official-docs
    accessed: 2026-11-24
  - id: s2
    title: "SOQL and SOSL Reference: Query Multi-Select Picklists"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/api/sforce_api_calls_soql_querying_multiselect_picklists.htm
    type: official-docs
    accessed: 2026-11-24
  - id: s3
    title: "Picklist Administration: Get Started with Picklists"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/picklist_admin/picklist_admin_start
    type: official-learning
    accessed: 2026-11-24
  - id: s4
    title: "Alternatives to a Multi-Select Picklist"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2023/alternatives-to-a-multi-select-picklist
    type: official-blog
    accessed: 2026-11-24
  - id: s5
    title: "SOQL and SOSL Reference: Comparison Operators"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-comparisonoperators.html
    type: official-docs
    accessed: 2026-11-24
created: 2026-11-24
---

# Multi-Select Picklists

A multi-select picklist is one of the three picklist flavours in Salesforce, alongside standard picklists and custom single-select picklists. It lets a user pick one or more values from a defined list (one is still allowed), and the chosen values are displayed separated by semicolons.[^s3] In Lightning Experience users hold Ctrl (Windows) or Command (Mac) while clicking to add or remove values.[^s3] Like other custom picklists, a multi-select picklist can draw on its own values or on a global value set, can be restricted to its defined values, and can take part in dependent picklists.[^s3]

## How it works

Under the hood the field holds one delimited text value rather than a set of related rows. The Salesforce Admins blog illustrates this with a regions field stored as a single string such as "Midwest;Southwest;Northwest;West".[^s4] Everything that touches the field has to understand that format: Apex and Flow must split the string to work with individual values, and an import or API update must supply every value the record should keep, because the incoming string replaces what was there.[^s4]

SOQL has dedicated operators for this field type. `INCLUDES` and `EXCLUDES` apply only to multi-select picklists.[^s5] Within one quoted string, a semicolon means AND (both values selected), while comma-separated strings inside `INCLUDES` mean OR, so `INCLUDES ('AAA;BBB','CCC')` matches records with both AAA and BBB selected, or with CCC selected.[^s2] The `=` operator demands an exact match of the whole stored string, and from API version 39.0 onward queries filter on each value's API name, which can differ from its label.[^s2]

## Limits and gotchas

Salesforce Help lists these limits for custom multi-select picklists, verified for Winter '27:[^s1]

- Up to 500 values per field.[^s1]
- Up to 255 characters per value.[^s1]
- A user can select up to 100 values at a time on a single record.[^s1]

Practical gotchas go beyond the numbers. Reports group by each distinct combination of selections, so "A;B" and "A" land in separate buckets, and report filters should use "includes" or "contains" rather than "equals".[^s3] Only certain formula functions, such as `INCLUDES`, can reference the field, which limits roll-ups and validation logic.[^s3][^s4] The Admins blog adds that a Flow field update element cannot set a multi-select value directly, and that BACA Systems found two unrelated multi-select fields (equipment and manufacturer) impossible to correlate in reports.[^s4] Converting a multi-select picklist to a single-select picklist clears the field's data on existing records, so a later change of mind is costly.[^s3]

## When to use it (and when not)

A multi-select picklist suits light tagging: a short, stable list where users rarely pick many values and nobody needs per-value reporting or attributes. The Admins blog recommends asking first what the data will be used for.[^s4] When there is a small fixed number of choices, two single-select picklists sharing one global value set (for example primary and secondary referral source) often cover most needs.[^s4] When each selection needs its own attributes or reporting, model it as records: a child object with dependent picklists, or a junction object linking the record to a reference object, gives one row per value and clean reports.[^s4] Migrating existing multi-select data into such an object is easiest while the data is still clean.[^s4]

## Connections

Multi-select picklists are a field type within **custom fields**, and their values can come from shared **picklist value sets**.[^s3] They can act as dependent fields in **field dependencies**, which Trailhead lists among the capabilities they share with single-select picklists.[^s3] They are queried with **SOQL** through the `INCLUDES` and `EXCLUDES` operators.[^s2] Formula support is narrow, which is why **formula fields** that reference them rely on functions such as `INCLUDES`.[^s3] The main structural alternative is a **junction object**, which trades a quick field for proper many-to-many records, and that choice affects **data quality** because related records can be restricted and reported per value.[^s4]

## Sources
[^s1]: Salesforce Help, "Picklist Limitations". https://help.salesforce.com/s/articleView?language=en_US&id=platform.picklist_limitations.htm&type=5 (accessed 2026-11-24)
[^s2]: Salesforce Developers, "SOQL and SOSL Reference: Query Multi-Select Picklists". https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/api/sforce_api_calls_soql_querying_multiselect_picklists.htm (accessed 2026-11-24)
[^s3]: Trailhead, "Picklist Administration: Get Started with Picklists". https://trailhead.salesforce.com/content/learn/modules/picklist_admin/picklist_admin_start (accessed 2026-11-24)
[^s4]: Salesforce Admins Blog, Dianne Siebold, "Alternatives to a Multi-Select Picklist" (2023). https://admin.salesforce.com/blog/2023/alternatives-to-a-multi-select-picklist (accessed 2026-11-24)
[^s5]: Salesforce Developers, "SOQL and SOSL Reference: Comparison Operators". https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-comparisonoperators.html (accessed 2026-11-24)
