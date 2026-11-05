---
id: kt:platform-data-architect-certification
type: Certification
title: Platform Data Architect Certification
aliases: [Salesforce Certified Platform Data Architect, Data Architect certification]
domain: data-model
summary: >-
  Salesforce's domain architect credential for designing sound, scalable, high-performing data solutions on the
  Salesforce Platform for enterprise data management; it is one of the four certifications that together grant the
  Application Architect credential on the path to Certified Technical Architect.
release: "Winter '27"
status: current
broader: [kt:salesforce-architect]
related: [kt:data-architecture, kt:large-data-volumes, kt:data-skew, kt:query-optimizer-selectivity, kt:bulk-api-2, kt:data-migration-strategy]
relations:
  - {predicate: partOf, object: kt:application-architect-certification}
  - {predicate: contrastsWith, object: kt:sharing-and-visibility-architect-certification}
sources:
  - id: s1
    title: "Certification - Salesforce Certified Platform Data Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/platformdataarchitect
    type: official-learning
    accessed: 2026-11-05
  - id: s2
    title: "Certification - Salesforce Certified Application Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/applicationarchitect
    type: official-learning
    accessed: 2026-11-05
  - id: s3
    title: "Architect Certifications Overview"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/architectoverview
    type: official-learning
    accessed: 2026-11-05
  - id: s4
    title: "Best Practices for Deployments with Large Data Volumes: General"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-best-practices-general.md
    type: official-docs
    accessed: 2026-11-05
  - id: s5
    title: "Best Practices for Deployments with Large Data Volumes: Loading Data from the API"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-best-practices-api-loading-data.html
    type: official-docs
    accessed: 2026-11-05
  - id: s6
    title: "Best Practices for Deployments with Large Data Volumes"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-best-practices.html
    type: official-docs
    accessed: 2026-11-05
created: 2026-11-05
---

# Platform Data Architect Certification

The Salesforce Certified Platform Data Architect is the architect-level credential for people who design sound, scalable and high-performing solutions on the Salesforce Platform with enterprise data management in mind.[^s1] Trailhead lists it among the domain architect credentials alongside Sharing and Visibility, Identity and Access Management, Integration and Development Lifecycle and Deployment, and points candidates to the "Architect Journey: Data Architecture and Management" Trailmix as preparation.[^s1][^s3]

## Where it sits in the architect path

The exam is mainly a building block. Salesforce grants the **Application Architect** credential automatically once a candidate holds four certifications: Platform App Builder, Platform Data Architect, Platform Developer, and Platform Sharing and Visibility Architect; there is no separate Application Architect exam.[^s2] Trailhead describes Application Architects as having deep knowledge of native Salesforce features and as experts at modeling role hierarchies, data and the right sharing mechanisms.[^s2] Its counterpart, the System Architect, focuses instead on off-platform systems, integration and securing access between systems.[^s1][^s2] The Certified Technical Architect sits above both as the credential for secure, high-performance, integrated solutions within a customer's wider landscape.[^s1]

## What it tests (at a practitioner level)

The emphasis is on reasoning about data at scale rather than clicking through setup. Salesforce's large-data-volume guidance frames the central idea: performance improves when the platform has fewer records to process, so architects write narrow, selective queries and keep the active data set small by archiving or discarding records at roughly the rate new ones arrive.[^s6] The same guidance supplies the concrete rules scenario questions tend to hinge on. To avoid ownership skew, keep any single user's owned records under 10,000, and to avoid parent-child skew, keep each parent under 10,000 child records, spreading children across several placeholder parents when no natural parent exists.[^s4] Data tiering — spreading data across objects and pulling it on demand from another object or an external store — is the recommended performance lever, and sandbox copies go faster when unnecessary field history is excluded.[^s4]

Loading and migrating data is the other recurring theme. Salesforce recommends Bulk API 2.0 for operations over 2,000 records and bulkified synchronous REST Composite or SOAP calls below that.[^s5] Insert is the fastest operation, followed by update and then upsert, so splitting an upsert into separate creates and updates can pay off; only changed fields should be sent on updates.[^s5] For initial loads the guidance is to use Public Read/Write defaults during the load, create roles before sharing rules, place users in roles before loading records, add sharing rules one at a time, and use the defer sharing calculation permission until the data is in.[^s5] Grouping child records by parent within a batch reduces lock contention, and triggers, workflow and validations can be disabled during a load and their work replayed afterwards with batch Apex.[^s5]

## Gotchas

- **Field history and sandboxes.** Large orgs refresh full sandboxes faster when field history is left out and big data changes are avoided during the copy.[^s4]
- **Clean data before bulk loads.** In Bulk API 2.0, batch errors push processing into single-row mode, which sharply slows the job.[^s5]
- **Not loading is an option.** The guidance suggests mashups or coupled integrations instead of copying data into Salesforce when the data needn't live there.[^s5]
- **Exam logistics change.** The credential page links out to Trailhead Academy for registration; confirm question count, timing, passing score and fee there rather than in third-party summaries.[^s1]

## When to pursue it

Pursue it if you design object models, plan migrations or archive strategies, or troubleshoot performance in orgs with millions of records, or if you are working toward Application Architect or CTA.[^s2] If your work is mainly about who can see which records, the Sharing and Visibility Architect exam — its sibling prerequisite — is the closer fit.[^s2]

## Connections

- **broader → `kt:salesforce-architect`**: one rung of the Salesforce architect credential ladder.[^s3]
- **partOf → `kt:application-architect-certification`**: one of the four certifications that roll up into Application Architect.[^s2]
- **contrastsWith → `kt:sharing-and-visibility-architect-certification`**: the sibling Application Architect prerequisite; this exam covers how data is shaped and scaled, that one who can see it.[^s2]
- **related → `kt:data-architecture`, `kt:data-migration-strategy`**: the discipline and migration practice the credential certifies.[^s1][^s5]
- **related → `kt:large-data-volumes`, `kt:data-skew`, `kt:query-optimizer-selectivity`**: the performance topics behind the 10,000-record skew rules and selective-query advice.[^s4][^s6]
- **related → `kt:bulk-api-2`**: the recommended API for loads above 2,000 records.[^s5]

## Sources
[^s1]: Trailhead, "Certification - Salesforce Certified Platform Data Architect". https://trailhead.salesforce.com/credentials/platformdataarchitect (accessed 2026-11-05)
[^s2]: Trailhead, "Certification - Salesforce Certified Application Architect". https://trailhead.salesforce.com/credentials/applicationarchitect (accessed 2026-11-05)
[^s3]: Trailhead, "Architect Certifications Overview". https://trailhead.salesforce.com/credentials/architectoverview (accessed 2026-11-05)
[^s4]: Salesforce Developers, "Best Practices for Deployments with Large Data Volumes: General". https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-best-practices-general.md (accessed 2026-11-05)
[^s5]: Salesforce Developers, "Best Practices for Deployments with Large Data Volumes: Loading Data from the API". https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-best-practices-api-loading-data.html (accessed 2026-11-05)
[^s6]: Salesforce Developers, "Best Practices for Deployments with Large Data Volumes". https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-best-practices.html (accessed 2026-11-05)
