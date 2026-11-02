---
id: kt:large-data-volumes
type: Concept
title: Large Data Volumes
aliases: [LDV, large data volume, Salesforce LDV, LDV deployments]
domain: platform-architecture
summary: >-
  The architectural concern of running Salesforce orgs with very high user counts, record counts or storage (roughly
  tens of millions of records), where query selectivity, sharing calculation, data loading and deletion must be
  designed deliberately to keep the multitenant platform performant.
release: "Winter '27"
status: concept
broader: [kt:data-architecture]
related: [kt:data-skew, kt:archiving-strategy, kt:multitenancy]
relations:
  - {predicate: hasPart, object: kt:query-optimizer-selectivity}
  - {predicate: hasPart, object: kt:skinny-tables}
  - {predicate: queriedWith, object: kt:bulk-api-2}
sources:
  - id: s1
    title: "Best Practices for Deployments with Large Data Volumes: Introduction"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-introduction.html
    type: official-docs
    accessed: 2026-11-02
  - id: s2
    title: "Best Practices for Deployments with Large Data Volumes (PDF)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/256/latest/en-us/sfdc/pdf/salesforce_large_data_volumes_bp.pdf
    type: official-docs
    accessed: 2026-11-02
  - id: s3
    title: "Large Data Volumes Best Practices: General"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-best-practices-general.html
    type: official-docs
    accessed: 2026-11-02
  - id: s4
    title: "Large Data Volumes Best Practices: Loading Data from the API"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-best-practices-api-loading-data.html
    type: official-docs
    accessed: 2026-11-02
  - id: s5
    title: "Large Data Volumes: Conduct Data Queries and Searches"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/large-data-volumes/conduct-data-queries-and-searches
    type: official-learning
    accessed: 2026-11-02
created: 2026-11-02
---

# Large Data Volumes

**Large data volumes (LDV)** is Salesforce's umbrella term for orgs whose scale makes ordinary design choices
break down. Salesforce's own guide calls it an imprecise, elastic term and gives rough markers: tens of thousands of
users, tens of millions of records, or hundreds of gigabytes of record storage. The guidance targets experienced
architects, and the pressure points it names are bulk loading and updating, extracting data through reports, queries
and views, and the need to defer or bypass business-rule and sharing processing.[^s1]

## Why scale behaves differently on Salesforce

Salesforce runs one application for all tenants and stores customer data in large shared tables that are partitioned
by org; virtual tables are assembled at runtime from metadata. Because customers cannot tune the SQL the platform
generates, classic database tuning is not available, and performance comes instead from how the data model, filters
and processing are designed.[^s2] Salesforce's query optimizer chooses indexes, driving tables and join order for the
queries behind reports, list views and SOQL, using statistics about data distribution and pre-queries to decide whether
an index will help.[^s5] Those statistics are gathered nightly, so after a large API load they may lag reality until
they are refreshed.[^s2]

## Core techniques

**Selective queries and indexes.** The platform indexes fields such as record ID, Name, CreatedDate, SystemModstamp,
RecordTypeId, Division and foreign keys. The guide publishes the thresholds the optimizer uses: a standard index is
considered when a filter matches under 30% of the first million records and under 15% of the remainder, capped at one
million records; a custom index when it matches under 10% of records, capped at 333,333. Custom indexes cannot be
built on multi-select picklists, long or rich text areas, non-deterministic formulas or encrypted text, and filtering
on null in picklist or lookup fields tends to bypass indexes.[^s2]

**Skinny tables.** Salesforce Support can create a skinny table holding a subset of an object's commonly used fields,
which avoids joins and excludes soft-deleted rows. They are supported on custom objects plus Account, Contact,
Opportunity, Lead and Case, are limited to 200 columns, cannot contain fields from other objects, and are copied only to
Full sandboxes automatically.[^s2] Adding a field or changing a field's type means Support must rebuild the table.[^s5]

**Avoid unnecessary data.** Options include mashups that leave data in an external system and fetch it on demand,
data tiering across objects or external stores, and divisions to partition very large objects.[^s2][^s3] Deleted
records sit in the Recycle Bin and still affect performance, so for a million or more records the guide recommends the
hard-delete option of Bulk API or Bulk API 2.0, deleting children before parents.[^s2]

**Loading data.** Salesforce suggests Bulk API 2.0 for operations above 2,000 records; insert is faster than update,
which is faster than upsert. During initial loads it recommends Public Read/Write defaults, disabling triggers,
workflow and validations, sending only changed fields, grouping child records by parent ID within a batch to reduce
lock contention, and using the defer sharing calculation permission until loading finishes.[^s4]

## Gotchas and thresholds

Two numbers recur in design reviews: avoid any single user owning more than 10,000 records, and avoid any parent having
more than 10,000 child records, for example by spreading orphaned contacts across several placeholder accounts.[^s3]
Search runs on separate indexing servers, so text changes can take about 15 minutes or longer to become searchable,
and very large changes take longer to index.[^s2] For queries, Batch Apex can process up to 50 million records, and
Bulk API query results are delivered as files up to 15 GB in total.[^s5] The PDF edition of the guide cited here is
an earlier release build; verify thresholds against the current online guide before quoting them in a design.[^s2]

## When it matters

Treat LDV as a design input, not a tuning exercise: decide record ownership, parent distribution, indexing,
archiving and load sequencing before data arrives. Retrofitting skinny tables or custom indexes needs Support
involvement, and the guide recommends batching large sharing configuration changes and letting the deferred
recalculation run in a maintenance window.[^s2][^s3]

## Connections

LDV sits under **data architecture** as one of its main constraints.[^s1] **Data skew** is the most common LDV
anti-pattern, arising when too many records concentrate on one owner or parent.[^s3] An **archiving strategy** is the
long-term remedy for growth, complementing hard deletes and data tiering.[^s2][^s3] LDV behaviour follows from
**multitenancy**, which is why the platform offers selectivity rules and skinny tables rather than raw database
tuning.[^s2] **Query optimizer selectivity** and **skinny tables** are its key query-side techniques, and **Bulk API
2.0** is the recommended channel for loading and deleting at scale.[^s2][^s4]

## Sources

[^s1]: Salesforce Developers, "Best Practices for Deployments with Large Data Volumes: Introduction". https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-introduction.html (accessed 2026-11-02)
[^s2]: Salesforce, "Best Practices for Deployments with Large Data Volumes" (PDF). https://resources.docs.salesforce.com/256/latest/en-us/sfdc/pdf/salesforce_large_data_volumes_bp.pdf (accessed 2026-11-02)
[^s3]: Salesforce Developers, "Large Data Volumes Best Practices: General". https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-best-practices-general.html (accessed 2026-11-02)
[^s4]: Salesforce Developers, "Large Data Volumes Best Practices: Loading Data from the API". https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-best-practices-api-loading-data.html (accessed 2026-11-02)
[^s5]: Trailhead, "Large Data Volumes: Conduct Data Queries and Searches". https://trailhead.salesforce.com/content/learn/modules/large-data-volumes/conduct-data-queries-and-searches (accessed 2026-11-02)
