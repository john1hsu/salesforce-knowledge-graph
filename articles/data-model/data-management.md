---
id: kt:data-management
type: Concept
title: Data Management
aliases: [Salesforce data management, enterprise data management, data lifecycle management, DAMA data management]
domain: data-model
summary: >-
  The umbrella discipline of planning, executing and supervising the policies, programs and practices that deliver,
  control, protect and enhance the value of data across its lifecycle; in Salesforce terms it spans governance,
  quality, architecture, application development, integration, security and day-to-day data operations.
release: "Winter '27"
status: concept
broader: [kt:information-management]
related: [kt:identity-resolution, kt:archiving-strategy, kt:data-migration-strategy, kt:data-classification, kt:salesforce-center-of-excellence]
relations:
  - {predicate: hasPart, object: kt:data-governance}
  - {predicate: hasPart, object: kt:data-quality}
  - {predicate: hasPart, object: kt:data-architecture}
  - {predicate: hasPart, object: kt:data-integration}
  - {predicate: hasPart, object: kt:data-stewardship}
sources:
  - id: s1
    title: "Describe Data Management (Data Management Fundamentals)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-management-fundamentals/describe-data-management
    type: official-learning
    accessed: 2026-11-22
  - id: s2
    title: "Review Data Management Concepts (Data Management Fundamentals)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-management-fundamentals/review-data-management-concepts
    type: official-learning
    accessed: 2026-11-22
  - id: s3
    title: "AI Guide for Government, Chapter 5: Data governance and management"
    publisher: U.S. General Services Administration, IT Modernization Centers of Excellence
    url: https://coe.gsa.gov/coe/ai-guide-for-government/data-governance-management/
    type: government
    accessed: 2026-11-22
created: 2026-11-22
---

# Data Management

Data management is the overall discipline that keeps an organization's data usable, trustworthy and valuable from the moment it is captured to the moment it is disposed of. Salesforce's Trailhead material adopts the definition from DAMA International's Data Management Body of Knowledge (DAMA-DMBOK): developing, executing and supervising the plans, policies, programs and practices that deliver, control, protect and enhance the value of data and information assets across their lifecycle.[^s1] The U.S. General Services Administration uses the same DAMA-DMBOK wording for lifecycle data management and treats the field as multidisciplinary.[^s3] The practical consequence for a Salesforce team is that data is managed as a business asset tied to organizational goals, not as a by-product of whichever app happened to create it.[^s1]

## The functions it covers

Trailhead breaks data management into seven functions, each of which has its own node or frontier entry in this graph:[^s1]

- **Data governance**: policies, standards, procedures, compliance and clear accountability for data.[^s1]
- **Data quality management**: assessing, improving and monitoring whether data is accurate, complete and fit for purpose.[^s1]
- **Data architecture**: designing how data is structured, stored, integrated and flows between systems.[^s1]
- **Application development**: building the apps that collect and deliver data, including choosing the system of record.[^s1]
- **Data integration**: combining data from different sources so systems can interoperate.[^s1]
- **Data security**: protecting data from unauthorized access and breaches with access controls and encryption.[^s1]
- **Data operations**: running day-to-day data activities and watching usage, performance and availability.[^s1]

## Planning, delivery and maintenance

A second Trailhead unit groups the working vocabulary into three stages.[^s2] **Planning** covers data strategy (how data will be collected, managed, analyzed and used to meet business goals), governance and architecture. **Delivery** covers how applications handle data: the system of record holds the authoritative version where data is usually created; a system of reference is the trusted access point when several systems of record disagree; systems of intelligence apply analytics and AI; and systems of engagement are the screens customers and employees touch.[^s2] Delivery also includes transformation, standardization, integration, enrichment and validation, with identity resolution treated as the part of validation that matches and reconciles duplicate records.[^s2] **Maintenance** covers data operations, data quality, cleansing (also called scrubbing), retention policies and monitoring data trends for anomalies.[^s2]

Retention is where the lifecycle becomes concrete. Trailhead's worked example sets different horizons for different purposes: purchase history kept for seven years for legal reasons, order detail older than three years archived because it no longer matters for warranty claims, and order detail older than seven years purged.[^s2]

## Who does the work

Data management depends on business and technology roles working together under clearly assigned responsibilities.[^s1] Data stewards monitor quality in systems of record and reference, look for suspicious values such as placeholder email addresses, and remove invalid data with transformation or cleansing tools.[^s2] In the U.S. federal government the structure is formalized: the Evidence Act of 2018 requires every executive agency to appoint a Chief Data Officer, and OMB guidance has the CDO chair a data governance body; GSA recommends a tiered model of steering committee, advisory group and working groups so routine decisions are not escalated.[^s3]

## Why it matters on Salesforce

Trailhead's scenario describes the familiar failure mode of a fast-growing org: data silos, inconsistent quality and analysts who spend days reconciling conflicting reports, which erodes trust in the system and in turn hurts user adoption.[^s2] A shared data management vocabulary gives admins, developers and architects a common language for deciding which system owns a record, how it is validated and how long it is kept.[^s2] GSA adds the lifecycle steps that are easy to skip: describing each dataset with metadata at ingestion, cataloging it so consumers can find it, basing access controls on that metadata, and archiving according to the owner's handling rules.[^s3]

## Connections

Data management is the parent discipline of several written nodes. `kt:data-governance` is its policy and accountability function, `kt:data-quality` its quality function, `kt:data-architecture` its design function and `kt:data-integration` its interoperability function, all listed as components in the DAMA-based Trailhead breakdown; `kt:data-stewardship` is the hands-on role that carries out quality and governance work day to day.[^s1][^s2] It is related to `kt:identity-resolution`, which Trailhead places under data validation, and to `kt:archiving-strategy` and `kt:data-migration-strategy`, which implement retention and delivery decisions in a Salesforce program.[^s2] GSA ties access controls to the metadata recorded for each dataset, which is the role `kt:data-classification` plays in an org, and it describes tiered governance bodies of the kind a `kt:salesforce-center-of-excellence` hosts.[^s3] Its broader node, `kt:information-management`, is the wider practice of managing all information assets, of which data is one.

## Sources

[^s1]: Trailhead, "Describe Data Management". https://trailhead.salesforce.com/content/learn/modules/data-management-fundamentals/describe-data-management (accessed 2026-11-22)
[^s2]: Trailhead, "Review Data Management Concepts". https://trailhead.salesforce.com/content/learn/modules/data-management-fundamentals/review-data-management-concepts (accessed 2026-11-22)
[^s3]: U.S. General Services Administration, "AI Guide for Government: Data governance and management". https://coe.gsa.gov/coe/ai-guide-for-government/data-governance-management/ (accessed 2026-11-22)
