---
id: kt:data-migration-strategy
type: Concept
title: Data Migration Strategy
aliases: [Salesforce data migration, data migration plan, data load strategy, initial data load]
domain: architecture-practice
summary: >-
  The architectural plan for moving legacy data into a Salesforce org: what gets loaded, in which order, with
  which API and keys, and how the org is temporarily configured so the load is fast, lock-free and recoverable.
release: "Winter '27"
status: concept
broader: [kt:data-architecture]
related: [kt:large-data-volumes, kt:environment-strategy, kt:data-skew, kt:archiving-strategy]
relations:
  - {predicate: queriedWith, object: kt:bulk-api-2}
  - {predicate: dependsOn, object: kt:external-id-fields}
  - {predicate: mitigates, object: kt:record-locking}
  - {predicate: dependsOn, object: kt:sandbox-types}
sources:
  - id: s1
    title: "Loading Data from the API (Best Practices for Deployments with Large Data Volumes)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-best-practices-api-loading-data.html
    type: official-docs
    accessed: 2026-11-01
  - id: s2
    title: "General Best Practices (Best Practices for Deployments with Large Data Volumes)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-best-practices-general.md
    type: official-docs
    accessed: 2026-11-01
  - id: s3
    title: "Extreme Force.com Data Loading, Part 4: Sequencing Load Operations"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2013/06/extreme-force-com-data-loading-part-4-sequencing-load-operations
    type: official-blog
    accessed: 2026-11-01
  - id: s4
    title: "Step 5: Bulk Upsert (Bulk API 2.0 and Bulk API Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_bulk_v2/walkthrough_upsert.htm
    type: official-docs
    accessed: 2026-11-01
created: 2026-11-01
---

# Data Migration Strategy

A data migration strategy is the plan an architect writes before any record is moved from a legacy system into Salesforce. It decides the scope of data to bring over, the order in which objects are loaded, the API and keys used to stitch records together, and the temporary org configuration that keeps a large load fast and free of lock contention. Salesforce's own large-data-volume guidance treats loading as a discipline in its own right, with its own trade-offs between speed, correctness and sharing overhead.[^s1][^s3]

## How it works

Salesforce's long-standing sequencing guidance splits a migration into four phases.[^s3]

1. **Configure the org for loading.** Build the role hierarchy, load users into their roles, and set organization-wide defaults on the target objects to Public Read/Write so that no sharing rows have to be computed while data streams in. Ask Salesforce Support about enabling parallel sharing recalculation and deferred sharing calculation.[^s3]
2. **Prepare the data.** Cleanse it, paying particular attention to foreign-key references, because errors push parallel loads into slow single-row processing. Suspend automation that fires on insert, and use a sandbox to find the largest batch size that does not time out.[^s3][^s1]
3. **Execute the load.** Load parents before their master-detail children, capture the new parent IDs for the child files, and group child rows by parent so concurrent batches do not contend for the same parent record. When grouping is impossible, run the Bulk API in serial mode.[^s3][^s1]
4. **Configure the org for production.** Tighten the defaults to Private or Public Read Only, create public groups and queues, add sharing rules, and re-enable the automation that was switched off.[^s3]

## Choosing the API and operation

The official guidance recommends Bulk API 2.0 for operations above 2,000 records and bulkified synchronous calls, such as REST Composite or SOAP, below that threshold.[^s1] Operation choice matters too: insert is the fastest, then update, then upsert, so where possible a migration should split upserts into separate create and update passes and send only changed fields on updates (delta loads).[^s1] Long transfers benefit from authenticating once per load rather than per record, and from GZIP compression with HTTP keep-alive.[^s1]

Upsert still earns its place for reruns and incremental waves because it is idempotent against a key. In Bulk API 2.0, the job names an `externalIdFieldName`, and the platform uses that field to decide whether each CSV row updates an existing record or creates a new one; the success file returns `sf__Id` and `sf__Created` for each row, which is what a migration uses to build its legacy-to-Salesforce cross-reference.[^s4] Carrying the legacy primary key into a custom External ID field on every migrated object is therefore a standard design choice.

## Limits and gotchas

- **Sharing overhead.** Adding sharing rules after the data is in triggers recalculation. Add them one at a time and let each finish, or use the defer-sharing-calculation permission to postpone the work until the load is complete.[^s1][^s3]
- **Automation.** Apex triggers, workflow and validation rules multiply the cost of every save. The guidance suggests disabling them during the load and running any needed enrichment afterwards with batch Apex.[^s1]
- **Skew.** Avoid letting one user own more than 10,000 records, and keep each parent under 10,000 children. If thousands of contacts arrive without accounts, spread them across several placeholder accounts instead of one.[^s2]
- **Dirty data costs time.** Batch errors force single-row reprocessing and degrade throughput, which is why cleansing happens before, not during, the load.[^s1]

## When to use it (and when not)

Every go-live that inherits historical records needs an explicit migration strategy, and the same plan should be rehearsed end to end in a sandbox before the production cutover.[^s3] Not all data needs to move, though. The guidance points out that some coupled integrations can use a mashup instead of copying records into Salesforce, and that data can be tiered across objects or external stores and loaded on demand.[^s1][^s2] Deciding what stays behind is part of the strategy, and it often feeds a parallel archiving decision.

## Connections

Data migration strategy sits under **data architecture** and draws directly on **large data volumes** guidance, since the same skew and sharing limits apply to loads as to steady-state orgs.[^s2] It depends on **Bulk API 2.0** and **External ID fields** for idempotent, key-based loads.[^s4] Grouping children by parent and serial mode **mitigate record locking**, and the ownership and child-count limits link it to **data skew**.[^s1][^s2] Rehearsals run in a full or partial-copy sandbox, which ties the plan to **sandbox types** and the wider **environment strategy**, and the choice of what not to migrate connects it to **archiving strategy**.[^s3]

## Sources
[^s1]: Salesforce, "Loading Data from the API", Best Practices for Deployments with Large Data Volumes. https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-best-practices-api-loading-data.html (accessed 2026-11-01)
[^s2]: Salesforce, "General Best Practices", Best Practices for Deployments with Large Data Volumes. https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-best-practices-general.md (accessed 2026-11-01)
[^s3]: Salesforce Developers Blog, "Extreme Force.com Data Loading, Part 4: Sequencing Load Operations". https://developer.salesforce.com/blogs/2013/06/extreme-force-com-data-loading-part-4-sequencing-load-operations (accessed 2026-11-01)
[^s4]: Salesforce, "Step 5: Bulk Upsert", Bulk API 2.0 and Bulk API Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_bulk_v2/walkthrough_upsert.htm (accessed 2026-11-01)
