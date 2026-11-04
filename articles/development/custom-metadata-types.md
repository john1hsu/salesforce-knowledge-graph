---
id: kt:custom-metadata-types
type: MetadataType
title: Custom Metadata Types
aliases: [custom metadata, __mdt, CMT, CMDT, custom metadata records]
domain: development
summary: >-
  Customizable, deployable application configuration on the Salesforce Platform: a type with the __mdt suffix
  defines the shape of configuration, and its records are themselves metadata, so they travel with packages,
  change sets and the Metadata API instead of being reloaded as data.
release: "Winter '27"
status: current
broader: [kt:metadata-driven-architecture]
related: [kt:apex, kt:metadata-api, kt:change-sets, kt:second-generation-managed-packages, kt:flow-builder]
relations:
  - {predicate: alternativeTo, object: kt:custom-settings}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: governedBy, object: kt:governor-limits}
sources:
  - id: s1
    title: "Custom Metadata Types: Get Started with Custom Metadata Types"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/custom_metadata_types_dec/cmt_overview
    type: official-learning
    accessed: 2026-11-04
  - id: s2
    title: "Custom Metadata Types (overview)"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.custommetadatatypes_overview.htm&type=5&language=en_US
    type: official-docs
    accessed: 2026-11-04
  - id: s3
    title: "Custom Metadata Allocations and Usage Calculations"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.custommetadatatypes_limits.htm&type=5
    type: official-docs
    accessed: 2026-11-04
  - id: s4
    title: "Custom Metadata Types Limitations"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=platform.custommetadatatypes_limitations.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-04
  - id: s5
    title: "Protection and Privacy Options for Custom Metadata Types"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.custommetadatatypes_protection.htm&type=5
    type: official-docs
    accessed: 2026-11-04
  - id: s6
    title: "Custom Metadata Types: Use Custom Metadata Types in Formulas, Default Values, and Validation Rules"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/custom_metadata_types_dec/cmt_formulas
    type: official-learning
    accessed: 2026-11-04
created: 2026-11-04
---

# Custom Metadata Types

A custom metadata type is an object-like definition, identified by the `__mdt` suffix, that describes the structure of application configuration rather than business data. Both its fields and its records are metadata, so a team can model things like tax rates, routing tables or feature switches once and have them move between orgs as part of the application.[^s1] Salesforce positions the feature as the basis for declarative developer frameworks: you define the type, then write reusable logic whose behaviour is driven by its records.[^s2]

## How it works

Types and records can be created and edited in Setup, through the Metadata API, or with Salesforce CLI commands, and they can be shipped in unmanaged packages, managed packages and package extensions, or moved from sandbox to production with change sets.[^s2] Because records are metadata, they install with the package; custom objects and custom settings deploy only their definitions, leaving records to be loaded separately.[^s1]

Supported field types include metadata relationships, checkbox, date and date/time, email, phone, number, percent, picklist, text, text area and URL.[^s1] Metadata relationship fields can target another custom metadata type, an entity definition (an object) or a field definition, so one record can say which object and field a rule applies to.[^s3]

Records are read with SOQL and, declaratively, referenced in advanced formula fields, field default values and validation rules with the `$CustomMetadata.Type__mdt.Record.Field__c` form; editing the record then changes every rule or formula that uses it.[^s6] Apex can create, read and update records but cannot delete them, and modifying records from Apex goes through the `Metadata` namespace rather than DML.[^s1][^s4]

## Limits and gotchas (Winter '27)

Salesforce's allocations page lists unlimited SOQL queries against custom metadata per Apex transaction, but queries issued from flows and queries that include long text area fields still count toward governor limits. An org gets 10 million characters of custom metadata, 100 fields per type and 200 types; beyond 200, up to 150 more can come only from certified managed packages, for 350 in total. A transaction can return at most 50,000 records.[^s3]

Usage is charged by each field's maximum size, not the characters stored, so a text area adds 255 characters per record even when nearly empty; picklists and checkboxes count as 10 characters, and relationship fields 10 or 15. Records from installed certified managed packages don't consume the org's allotment, but records a developer removes from a package linger and count until deleted.[^s3]

Other gotchas from the limitations list: no Tooling API or Developer Console support; no Shield Platform Encryption on these fields; global picklists aren't allowed; formulas can't traverse metadata relationships; an object's validation rules can reference at most 15 distinct types; deployments lock records and can cause row-lock errors; and records are cached per type, so an in-flight request may see stale values during an update. In Flow, a Get Records element filtering with an AND on values that vary across a bulk transaction loses bulkification and can hit governor limits.[^s4]

## Protection and packaging

Visibility is public, protected or PackageProtected. Protected types restrict Apex access to the package namespace, and PackageProtected to the same second-generation managed package; subscribers can't add records to installed protected types. Protection only applies inside a managed package, since protected types in an unmanaged package behave as public, so secrets belong in protected types of a managed package.[^s5][^s4]

## When to use it (and when not)

Choose custom metadata for configuration that should be versioned and deployed with the app: mappings, thresholds, rule tables and switches. Custom settings remain the option when you need user-, profile- or org-level hierarchy values or full CRUD from Apex, since custom metadata offers list-style records only and no Apex delete.[^s1] Frequently changing transactional data belongs in custom objects, given deployment locking and caching behaviour.[^s4]

## Connections

Custom metadata types are a concrete expression of Salesforce's metadata-driven architecture, and they are an alternative to custom settings for app configuration.[^s1] They are queried with SOQL under special governor-limit treatment, managed through the Metadata API, deployed with change sets, and protected through managed packaging, which links them to second-generation managed packages.[^s2][^s3][^s5] Apex and Flow are their main consumers, with the bulkification caveat above.[^s4]

## Sources

[^s1]: Trailhead, "Custom Metadata Types: Get Started with Custom Metadata Types". https://trailhead.salesforce.com/content/learn/modules/custom_metadata_types_dec/cmt_overview (accessed 2026-11-04)
[^s2]: Salesforce Help, "Custom Metadata Types". https://help.salesforce.com/s/articleView?id=sf.custommetadatatypes_overview.htm&type=5&language=en_US (accessed 2026-11-04)
[^s3]: Salesforce Help, "Custom Metadata Allocations and Usage Calculations". https://help.salesforce.com/s/articleView?language=en_US&id=sf.custommetadatatypes_limits.htm&type=5 (accessed 2026-11-04)
[^s4]: Salesforce Help, "Custom Metadata Types Limitations". https://help.salesforce.com/s/articleView?id=platform.custommetadatatypes_limitations.htm&language=en_US&type=5 (accessed 2026-11-04)
[^s5]: Salesforce Help, "Protection and Privacy Options for Custom Metadata Types". https://help.salesforce.com/s/articleView?language=en_US&id=platform.custommetadatatypes_protection.htm&type=5 (accessed 2026-11-04)
[^s6]: Trailhead, "Custom Metadata Types: Use Custom Metadata Types in Formulas, Default Values, and Validation Rules". https://trailhead.salesforce.com/content/learn/modules/custom_metadata_types_dec/cmt_formulas (accessed 2026-11-04)
