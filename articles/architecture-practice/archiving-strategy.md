---
id: kt:archiving-strategy
type: Concept
title: Archiving Strategy
aliases: [Salesforce data archiving strategy, data archiving policy, data retention strategy, data archival]
domain: architecture-practice
summary: >-
  The architectural plan for moving inactive or historical Salesforce records out of the live object set into
  cheaper long-term storage, governed by retention, purge and access rules, so the org stays fast, within
  storage limits and compliant.
release: "Winter '27"
status: concept
broader: [kt:data-architecture]
related: [kt:data-migration-strategy, kt:large-data-volumes, kt:data-skew, kt:environment-strategy]
relations:
  - {predicate: dependsOn, object: kt:big-objects}
  - {predicate: dependsOn, object: kt:salesforce-archive}
  - {predicate: contrastsWith, object: kt:backup-and-recover}
sources:
  - id: s1
    title: "What Is Data Archiving? (Guide to Data Archiving)"
    publisher: Salesforce
    url: https://www.salesforce.com/platform/data-archiving-solutions/guide/
    type: official-blog
    accessed: 2026-11-01
  - id: s2
    title: "Optimize Data with Archive (Archive Basics)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/archive-basics/optimize-data-with-archive
    type: official-learning
    accessed: 2026-11-01
  - id: s3
    title: "Big Objects (Big Objects Implementation Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/big-object-impl-guide/guide/big-object.html
    type: official-docs
    accessed: 2026-11-01
  - id: s4
    title: "Best Practices (Best Practices for Deployments with Large Data Volumes)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-best-practices.html
    type: official-docs
    accessed: 2026-11-01
  - id: s5
    title: "ArchivePolicyDefinition (Object Reference for the Salesforce Platform)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_archivepolicydefinition.htm
    type: official-docs
    accessed: 2026-11-01
created: 2026-11-01
---

# Archiving Strategy

An archiving strategy is the plan that decides which Salesforce records stop living in the active org, where they go, how long they are kept, and who may still reach them. Salesforce defines archiving as keeping inactive or historical data for long-term retention, in storage that balances cost, accessibility and security, and it frames the payoff in three ways: faster queries and searches, lower storage spend, and defensible compliance with rules such as GDPR and CCPA.[^s1] For architects it is the steady-state counterpart of a data migration: migration decides what comes in, archiving decides what goes out.[^s4]

## Why it matters on the platform

Salesforce's large-data-volume guidance says performance tuning comes down to reducing the number of records the platform must process, and it names keeping less data active as one of the two main levers alongside selective queries.[^s4] It warns that performance degrades as volume grows and recommends archiving or discarding data at the rate it arrives, so the active set stays roughly constant.[^s4] An archiving strategy is how that rate is made explicit and enforceable rather than left to periodic clean-ups.

## Archiving is not backup

Backup and archive solve different problems and a strategy needs both. Backup is short-term protection against failure, outage or accidental deletion; it copies everything and is rarely touched. Archiving keeps selected records for years and is queried for audits, reporting and legal requests.[^s1] Trailhead's Archive module repeats the point: archived records leave production, so a separate backup remains necessary for disaster recovery.[^s2]

## Building the strategy

Salesforce's guidance lays out a policy-first sequence.[^s1][^s2]

1. **Classify and set policy.** Decide what to archive, retain or delete based on business need and legal timelines, and group data by type, sensitivity and retention period. Typical candidates include closed cases, completed or lost opportunities, inactive leads and contacts, expired contracts and old logs.[^s1]
2. **Involve the right people.** Identify who sets policy (often administrators), who knows which data is inactive, and who can point to high-volume objects; Storage Analyzer helps by showing top objects by storage and usage history.[^s2]
3. **Preserve relationships.** Archive parents with their children so the data stays usable; in Salesforce Archive, master-detail children follow their parent automatically and lookup children can be included by configuration.[^s2]
4. **Schedule and automate.** Run archive jobs on a fixed cadence and off-peak so they do not compete with production workloads.[^s2]
5. **Govern access and deletion.** Apply least privilege to viewing and un-archiving, keep audit trails, set retention periods that expire records automatically, and use purge policies for cases such as right-to-be-forgotten requests, remembering that purged data cannot be recovered.[^s2]
6. **Measure.** Track storage reduction, performance gains, retrieval speed for audits and policy adherence.[^s1]

## Target options

- **Salesforce Archive.** The native product applies policies that select records by age, status or custom rules, moves them with related records and attachments into its own secure store outside the org, and exposes them through Lightning widgets for search and restore. Trailhead says it can process tens of millions of records a day by running jobs in parallel.[^s2] Its policies are represented in the API by the `ArchivePolicyDefinition` object, available from API version 65.0, which captures each policy's scope, frequency and rules for archiving or purging records from a root entity such as Contact or Lead.[^s5]
- **Big objects.** Custom big objects keep historical archives on-platform without slowing core apps, scaling to billions of records with consistent performance.[^s3] The trade-offs are significant: only object and field permissions apply (no sharing rules), triggers and flows are not supported, REST API is not supported, and writes are idempotent. The edition note lists Enterprise, Performance, Unlimited and Developer Editions for up to 1 million records, so larger volumes require additional capacity.[^s3]
- **External or third-party stores.** Flow or Apex jobs can automate movement, and AppExchange tools offer external cloud storage and tiered-storage policies.[^s1]

## When to use it (and when not)

Any org with steady record growth, storage overage risk, or regulatory retention duties needs a written archiving strategy, ideally designed before go-live together with the migration plan.[^s1][^s4] It is not a substitute for selective queries or skinny design: archiving reduces volume, but badly filtered queries still scan what remains.[^s4] Data that users must edit, share by rule or drive automation from is a poor fit for big objects and better kept active or moved to a searchable archive that supports restore.[^s3][^s2]

## Connections

Archiving strategy sits under **data architecture** and is the outbound mirror of **data migration strategy**; deciding what not to migrate often feeds the first archive policy.[^s4] It is a primary mitigation in **large data volumes** guidance and indirectly eases **data skew** by shrinking the child and ownership counts that accumulate over time.[^s4] It **depends on** a target such as **big objects** or **Salesforce Archive**, and it **contrasts with** backup and recovery, which protects against loss rather than managing retention.[^s1][^s3][^s2] Archive jobs should be rehearsed in sandboxes as part of the wider **environment strategy**, since Salesforce recommends piloting archiving in a test or staging environment first.[^s1]

## Sources
[^s1]: Salesforce, "What Is Data Archiving?", Guide to Data Archiving. https://www.salesforce.com/platform/data-archiving-solutions/guide/ (accessed 2026-11-01)
[^s2]: Salesforce Trailhead, "Optimize Data with Archive", Archive Basics. https://trailhead.salesforce.com/content/learn/modules/archive-basics/optimize-data-with-archive (accessed 2026-11-01)
[^s3]: Salesforce, "Big Objects", Big Objects Implementation Guide. https://developer.salesforce.com/docs/platform/big-object-impl-guide/guide/big-object.html (accessed 2026-11-01)
[^s4]: Salesforce, "Best Practices", Best Practices for Deployments with Large Data Volumes. https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-best-practices.html (accessed 2026-11-01)
[^s5]: Salesforce, "ArchivePolicyDefinition", Object Reference for the Salesforce Platform. https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_archivepolicydefinition.htm (accessed 2026-11-01)
