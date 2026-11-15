---
id: kt:data-classification
type: Feature
title: Data Classification
aliases: [data classification metadata, field data classification, Data Sensitivity Level, Compliance Categorization, Data Classification Settings]
domain: public-sector-and-compliance
summary: >-
  The practice of labelling data by sensitivity and applicable regulation, and the built-in Salesforce field metadata
  (Data Owner, Field Usage, Data Sensitivity Level, Compliance Categorization) that records those labels on every field
  so that access, encryption, monitoring and compliance decisions can be driven from one inventory.
release: "Winter '27"
status: current
broader: [kt:data-governance]
related: [kt:nist-sp-800-60, kt:fips-199, kt:salesforce-shield, kt:field-level-security]
relations:
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: queriedWith, object: kt:tooling-api}
  - {predicate: integratesWith, object: kt:data-detect}
  - {predicate: integratesWith, object: kt:data-cloud}
sources:
  - id: s1
    title: "Data Classification Metadata Fields"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=platform.data_classification_metadata_fields.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-15
  - id: s2
    title: "Set Up Data Classification Metadata"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.data_classification_set_up.htm&amp=&type=5
    type: official-docs
    accessed: 2026-11-15
  - id: s3
    title: "FieldDefinition — Tooling API Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/tooling_api_objects_fielddefinition.htm
    type: official-docs
    accessed: 2026-11-15
  - id: s4
    title: "Design Your Governance Strategy (Data 360 Data Governance Strategies)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-cloud-data-governance-strategies/design-your-governance-strategy
    type: official-learning
    accessed: 2026-11-15
  - id: s5
    title: "ITL Bulletin March 2004: Federal Information Processing Standard (FIPS) 199"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/files/pubs/shared/itlb/itlbul2004-03.pdf
    type: standards-body
    accessed: 2026-11-15
  - id: s6
    title: "Guide to Data Classification: Types and Examples"
    publisher: Salesforce
    url: https://www.salesforce.com/platform/data-security/data-classification/
    type: official-blog
    accessed: 2026-11-15
  - id: s7
    title: "Know Your Metadata (Data Reliability and Risk Factors for AI)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-reliability-risk-factors-for-ai/know-your-metadata
    type: official-learning
    accessed: 2026-11-15
created: 2026-11-15
---

# Data Classification

Data classification sorts information into categories by how sensitive it is, which rules apply to it and how valuable it is to the business, so that the organization can decide who may see it and how it must be protected.[^s6] Salesforce builds this into the platform as four metadata attributes on each field, available in every edition and switched on automatically in all orgs, which makes the org itself the system of record for "which fields hold what kind of data".[^s1][^s2]

## The four classification fields

Each field in Object Manager carries the same set of attributes, and each maps to a column on the Tooling API `FieldDefinition` object.[^s1][^s3]

- **Data Owner** (`BusinessOwnerId`): the user or group accountable for the field, who may set its minimum sensitivity level.[^s1][^s3]
- **Field Usage** (`BusinessStatus`): Active, DeprecateCandidate or Hidden; changing it does not hide or expose the field to anyone.[^s1]
- **Data Sensitivity Level** (`SecurityClassification`): Public, Internal, Confidential, Restricted or MissionCritical by default.[^s1][^s3]
- **Compliance Categorization** (`ComplianceGroup`): a multi-select of regimes such as PII, HIPAA, GDPR, PCI, COPPA and CCPA.[^s1][^s3]

A seventh compliance value, PersonalInfo, appears only when Enhanced Personal Information Management and Digital Experiences are both enabled.[^s1] The fields are informational: they record a decision, and other controls have to act on it.[^s1]

## How to set and manage it

Editing classification requires the Customize Application or Modify Data Classification permission.[^s1][^s2] Admins classify one field at a time from Fields & Relationships, or in bulk with the Data Classification Upload tool or the CustomField Metadata API.[^s2] The **Data Classification Settings** page lets you add, rename, delete, reorder and describe Data Sensitivity Level and Compliance Categorization values, flag a sensitivity value as high risk, and toggle default sensitivity so that fields such as email arrive pre-labelled.[^s2] Field Usage values can be changed only through the Metadata API's standard value sets.[^s1]

To report on the inventory, query `FieldDefinition` with SOQL through the Tooling API, filtering on `EntityDefinitionId` and selecting the classification columns, or read the same data through other Salesforce APIs and Apex.[^s1][^s3]

## Limits and gotchas

- The CSV upload accepts at most 10,000 rows, each naming an object, a field and a sensitivity level.[^s2]
- The download includes only fields that have a sensitivity value, is capped at 5 MB, and holds the first 2,000 records per sensitivity value.[^s2]
- Person Account `__pc` fields return no compliance categorization in queries, because the metadata lives on Contact; query Contact instead.[^s1]
- User object fields do not show the classification attributes in Object Manager, so they must be set through the Metadata API or the upload tool.[^s1]

Classification on the core platform describes the field, not its contents. It will not notice a Description field that users have filled with card numbers; finding sensitive values in actual data is the job of Shield's Data Detect, which ties sensitivity levels and categories to what is really stored.[^s6]

## Data 360 tags and policies

Data 360 (Data Cloud) has its own governance layer built on tags arranged in a hierarchical taxonomy, where assigning a child tag also applies its parent so that policies written for a category reach every tagged field.[^s4] Its Suggest Tags feature uses a large language model over object and field names and descriptions, never the data itself, and an administrator must approve each suggestion; tags can then propagate to downstream objects such as unified profiles.[^s4] Trailhead advises starting with data that affects privacy, compliance or critical decisions rather than tagging everything.[^s4]

## Mapping to federal categorization

Public-sector programs categorize information under FIPS 199, which rates the potential impact of a loss of confidentiality, integrity or availability as low, moderate or high.[^s5] A system takes the highest rating of any information type it handles for each objective, the high-water mark, so one high-impact field type can raise the whole org's baseline.[^s5] Salesforce field classification is the natural place to record which fields carry those information types, which turns a categorization worksheet into queryable metadata.[^s1][^s5]

## Connections

Data classification is a **part of data governance**, its broader node, which supplies the ownership and stewardship model the Data Owner field encodes.[^s1] On the compliance side it feeds **NIST SP 800-60** and **FIPS 199** categorization, which assign impact levels to information types.[^s5] It is **configured via the Metadata API** and **queried with the Tooling API**.[^s2][^s3] It **integrates with Data Detect** in **Salesforce Shield**, which checks real field contents against the labels, and it informs which fields need **field-level security** restrictions.[^s6][^s7] For data held in **Data Cloud** (Data 360), tags and policies play the same role and can be extended to non-CRM sources.[^s4][^s7]

## Sources

[^s1]: Salesforce Help, "Data Classification Metadata Fields". https://help.salesforce.com/s/articleView?id=platform.data_classification_metadata_fields.htm&language=en_US&type=5 (accessed 2026-11-15)
[^s2]: Salesforce Help, "Set Up Data Classification Metadata". https://help.salesforce.com/s/articleView?language=en_US&id=sf.data_classification_set_up.htm&amp=&type=5 (accessed 2026-11-15)
[^s3]: Salesforce Developers, "FieldDefinition — Tooling API Developer Guide". https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/tooling_api_objects_fielddefinition.htm (accessed 2026-11-15)
[^s4]: Trailhead, "Design Your Governance Strategy". https://trailhead.salesforce.com/content/learn/modules/data-cloud-data-governance-strategies/design-your-governance-strategy (accessed 2026-11-15)
[^s5]: NIST CSRC, "ITL Bulletin March 2004: FIPS 199". https://csrc.nist.gov/files/pubs/shared/itlb/itlbul2004-03.pdf (accessed 2026-11-15)
[^s6]: Salesforce, "Guide to Data Classification: Types and Examples". https://www.salesforce.com/platform/data-security/data-classification/ (accessed 2026-11-15)
[^s7]: Trailhead, "Know Your Metadata". https://trailhead.salesforce.com/content/learn/modules/data-reliability-risk-factors-for-ai/know-your-metadata (accessed 2026-11-15)
