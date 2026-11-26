---
id: kt:data-dictionary
type: Concept
title: Data Dictionary
aliases: [Salesforce data dictionary, field dictionary, org data dictionary, metadata dictionary]
domain: architecture-practice
summary: >-
  A maintained catalog of an org's objects and fields that records, for each data element, its meaning, type,
  source, usage, owner, sensitivity and access rules, so admins, developers, analysts and AI agents share one
  definition of the data model.
release: "Winter '27"
status: concept
broader: [kt:data-architecture, kt:data-governance]
related: [kt:data-classification, kt:schema-builder, kt:custom-fields, kt:solution-design-document]
relations:
  - {predicate: queriedWith, object: kt:tooling-api}
  - {predicate: dependsOn, object: kt:metadata-api}
sources:
  - id: s1
    title: "Data Management Best Practices in Salesforce (Essential Habits for Salesforce Admins)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/essential-habits-for-salesforce-admins/delve-into-data-management
    type: official-learning
    accessed: 2026-11-26
  - id: s2
    title: "Understand Metadata for Reliable AI Performance (Data Reliability Risk Factors for AI)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/fr/content/learn/modules/data-reliability-risk-factors-for-ai/know-your-metadata
    type: official-learning
    accessed: 2026-11-26
  - id: s3
    title: "CustomField (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/customfield.htm
    type: official-docs
    accessed: 2026-11-26
  - id: s4
    title: "FieldDefinition (Tooling API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/tooling_api_objects_fielddefinition.htm
    type: official-docs
    accessed: 2026-11-26
  - id: s5
    title: "How to Document Inside Your Salesforce Instance"
    publisher: Salesforce Blog
    url: https://www.salesforce.com/blog/how-to-document-inside-your-salesforce-instance/
    type: official-blog
    accessed: 2026-11-26
  - id: s6
    title: "Data Dictionaries"
    publisher: U.S. Geological Survey
    url: https://usgs.gov/data-management/data-dictionaries
    type: government
    accessed: 2026-11-26
created: 2026-11-26
---

# Data Dictionary

A data dictionary is the reference document, or living repository, that describes every data element in a system: what it is called, what it means, how it is stored and how it may be used. The U.S. Geological Survey describes it as the place where metadata about a database or application is stored and communicated, listing data objects with their definitions alongside element properties such as type, size and nullability, reference values, and the business rules that govern data quality.[^s6] In a Salesforce context, Trailhead frames it as a central repository of the org's data structure, covering objects and their fields, that acts as one source of truth for admins, developers, analysts and IT.[^s1]

## What it contains

Trailhead's admin guidance suggests a Salesforce data dictionary record more than the schema alone does:[^s1]

- **Structure:** object, field label and API name, and data type, plus sample values that show what good data looks like.[^s1]
- **Origin and flow:** whether the value is entered manually, set by automation or written by an integration, and how it moves to and from external systems.[^s1]
- **Usage:** where the field appears on page layouts and in Apex, Visualforce and automation, which is how unused fields are found.[^s1]
- **Control:** field-level security and access, whether field history is tracked, and a notes or open-questions column for follow-up.[^s1]

Beyond those columns, a mature dictionary also records an owner and a sensitivity rating for each field. Salesforce supports this natively: the CustomField metadata type carries a description, field-level help text, a business owner (user or group), a business status of Active, DeprecateCandidate or Hidden, compliance groups such as GDPR, HIPAA, PCI and PII, and a security classification from Public through Internal, Confidential and Restricted to MissionCritical.[^s3]

## How it is built and maintained

Most of the raw content can be extracted rather than typed. The Tooling API's FieldDefinition object exposes each field's label, qualified API name, UI-style data type, description, business owner, business status, compliance group, security classification and whether it is indexed or history-tracked.[^s4] Queries against it must filter on the parent object, for example by `EntityDefinition.QualifiedApiName`, so a full-org extract iterates object by object.[^s4] Because these values live in metadata, they also travel with the Metadata API and source control, which keeps the dictionary close to what is actually deployed.[^s3]

The harder part is the human meaning. A Salesforce blog on in-org documentation recommends writing help text that tells users what a field is for, and using the longer description to explain how the field works, which teams rely on it, how it drives automation and, for integration-fed fields, where its values come from.[^s5] The same article suggests marking retired fields in their label (for example a "DNU_" prefix) so that people stop using them before they are deleted.[^s5]

Maintenance cadence should follow the org's rate of change; Trailhead notes that a fast-moving org may need weekly updates so that new fields and integration changes are reflected quickly.[^s1] USGS adds that a dictionary should be planned at the start of a project and updated whenever structures change, and warns that a stale dictionary signals weak data stewardship.[^s6]

## Why it matters now

The dictionary used to be mostly an onboarding and audit aid, reducing entry errors, rework and integration mistakes.[^s1] With generative AI it has become an operational input. Trailhead's module on AI data reliability explains that agents interpret data through field names, descriptions and classifications, and that missing or misleading metadata can lead an agent to misread a field or surface data a user should not see.[^s2] It names three risks: unclear labels and descriptions, missing sensitivity classifications such as PII or PCI, and metadata drift when field usage changes without oversight, and it recommends that every new or changed field carry a description, help text, an owner and, where relevant, a classification.[^s2]

## Gotchas

- **Treat the org as the source.** Keep descriptions and classifications in field metadata and export them, rather than maintaining a spreadsheet that silently drifts from the deployed schema.[^s3][^s4]
- **DataType is display text.** FieldDefinition returns UI-style types such as `Text(40)`, not API type names, so mapping documents built from it may need translation.[^s4]
- **Do not cache DurableId.** Salesforce warns that FieldDefinition's DurableId is not guaranteed to stay stable between releases, so key the dictionary on qualified API names instead.[^s4]
- **Some values need features turned on.** The PersonalInfo compliance group only appears when Enhanced Personal Information Management and Digital Experiences are enabled.[^s4]

## Connections

A data dictionary sits **broader** under data architecture, as the documented form of the data model, and under data governance, because ownership, business status and classification are governance decisions recorded per field.[^s1][^s3] It is closely **related** to data classification, which supplies the sensitivity and compliance values; to Schema Builder, which visualizes the same objects and relationships the dictionary describes in words; to custom fields, whose description and help text are its primary content; and to the solution design document, which references it for data definitions.[^s3][^s5] It is **queried with** the Tooling API's FieldDefinition object and **depends on** the Metadata API, where descriptions and classifications are stored and deployed.[^s3][^s4] Its reach beyond Salesforce follows general data-management practice, where dictionaries support shared vocabulary, integration mapping and decision making.[^s6]

## Sources

[^s1]: Trailhead, "Data Management Best Practices in Salesforce". https://trailhead.salesforce.com/content/learn/modules/essential-habits-for-salesforce-admins/delve-into-data-management (accessed 2026-11-26)
[^s2]: Trailhead, "Understand Metadata for Reliable AI Performance". https://trailhead.salesforce.com/fr/content/learn/modules/data-reliability-risk-factors-for-ai/know-your-metadata (accessed 2026-11-26)
[^s3]: Salesforce Developers, "CustomField". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/customfield.htm (accessed 2026-11-26)
[^s4]: Salesforce Developers, "FieldDefinition". https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/tooling_api_objects_fielddefinition.htm (accessed 2026-11-26)
[^s5]: Salesforce Blog, "How to Document Inside Your Salesforce Instance". https://www.salesforce.com/blog/how-to-document-inside-your-salesforce-instance/ (accessed 2026-11-26)
[^s6]: U.S. Geological Survey, "Data Dictionaries". https://usgs.gov/data-management/data-dictionaries (accessed 2026-11-26)
