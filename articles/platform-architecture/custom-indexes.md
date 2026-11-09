---
id: kt:custom-indexes
type: Feature
title: Custom Indexes
aliases: [custom index, Salesforce custom indexes, indexed fields, standard indexes, two-column indexes, CustomIndex]
domain: platform-architecture
summary: >-
  Database indexes that Salesforce maintains on selected fields beyond the platform's default indexed fields, created
  through Salesforce Customer Support (or deployed as CustomIndex metadata) so selective filters on large objects can
  avoid full table scans.
release: "Winter '27"
status: current
broader: [kt:large-data-volumes, kt:multitenancy]
related: [kt:query-optimizer-selectivity, kt:skinny-tables, kt:external-id-fields, kt:soql, kt:data-skew]
relations:
  - {predicate: partOf, object: kt:large-data-volumes}
  - {predicate: alternativeTo, object: kt:skinny-tables}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: governedBy, object: kt:custom-index-limits}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: coveredBy, object: kt:platform-data-architect-certification}
sources:
  - id: s1
    title: "Best Practices for Deployments with Large Data Volumes: Indexes"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-infrastructure-indexes.html
    type: official-docs
    accessed: 2026-11-09
  - id: s2
    title: "Metadata API Developer Guide: CustomIndex"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_customindex.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s3
    title: "Database Basics for .NET Developers: Write Efficient Queries"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/database_basics_dotnet/writing_efficient_queries
    type: official-learning
    accessed: 2026-11-09
  - id: s4
    title: "Force.com SOQL Best Practices: Nulls and Formula Fields"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/engineering/2013/02/force-com-soql-best-practices-nulls-and-formula-fields
    type: official-blog
    accessed: 2026-11-09
  - id: s5
    title: "Know Thy Salesforce Field Indexes for Fast Reports, List Views, and SOQL"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/engineering/2015/06/know-thy-salesforce-field-indexes-fast-reports-list-views-soql
    type: official-blog
    accessed: 2026-11-09
created: 2026-11-09
---

# Custom Indexes

A **custom index** is an index that Salesforce builds on a field the platform does not index by default, so that
reports, list views and SOQL queries filtering on that field can locate rows without scanning the whole object.
Because Salesforce stores custom field values in shared multitenant tables that are not suited to direct indexing,
the platform keeps a separate index table (a copy of the field data with type information) and builds an ordinary
database index on top of it.[^s1] Custom indexes are a core tuning lever for large data volume (LDV) orgs, alongside
skinny tables and selective query design.

## Default indexes versus custom indexes

Most objects already carry platform-maintained indexes on the record Id, Name, RecordTypeId, Division, CreatedDate,
Systemmodstamp (LastModifiedDate), lookup and master-detail foreign keys, and Email on Contact and Lead.[^s1] Trailhead
adds OwnerId to this list and notes that fields flagged as unique or as External IDs are indexed automatically, which is
why it recommends filtering incremental extracts on SystemModStamp rather than LastModifiedDate.[^s3] Marking a field
as an External ID is therefore the one self-service way to index it, but it is allowed only on Auto Number, Email,
Number and Text fields.[^s1]

Everything else, including indexes on most standard fields, is created on request. Admins open a case with Salesforce
Customer Support and include the SOQL query that would use the index; Support then evaluates it.[^s3] Salesforce also
runs an auto-indexer that analyses candidate fields and adds an index itself when it would noticeably speed up one or
more queries.[^s5] Indexes are represented in the Metadata API by the `CustomIndex` type (API 50.0 and later, files with
the `.indx-meta` suffix in a `customindex` folder). Its `allowNullValues` flag defaults to false and, from API 61.0,
`booleanIndexedValue` controls boolean indexing; creating one still requires special access arranged through
Support.[^s2] Indexes Support creates in production are copied into sandboxes later created from that org.[^s1]

## What can and cannot be indexed

Custom fields are eligible except long text area, rich text area, encrypted text and non-deterministic formula
fields.[^s1] A formula is non-deterministic, and so unindexable, if it reaches other objects through lookups, uses
TODAY or NOW, references owner, auto-number, division or most audit fields (CreatedDate and CreatedById are the
exceptions), or touches multi-select picklists, multicurrency currency fields, binary fields, or standard fields with
special behaviour such as Opportunity Amount and IsClosed, Case ClosedDate or Lead Status.[^s4] Changing an indexed
formula causes its index to be rebuilt. A common workaround is to filter with cross-object notation directly on an
indexed field of the related record instead of wrapping it in a formula.[^s1]

## Nulls and two-column indexes

By default an index omits rows where the field is empty, so a filter such as `Field__c = null` forces a full scan.[^s1]
Support can enable null rows on a custom index, but an existing index has to be explicitly enabled and rebuilt; the
option is not available for picklists, external IDs or foreign keys.[^s4] For those, a **two-column (compound) index**
is the alternative, because its second column may hold nulls. Two-column indexes also help when two fields are routinely
combined, for example a list view that filters on State and sorts by City; otherwise they follow the same rules as
single-column indexes.[^s1][^s4]

## Limits and gotchas

An index is only a candidate: the query optimizer still checks whether the filter is selective enough, and custom
indexes face stricter thresholds than standard ones (see **query optimizer selectivity**).[^s1] Salesforce stresses
that even a correctly built index is not guaranteed to be used.[^s4] The filter must also use optimizable operators;
an indexed field alone is not enough.[^s5] To check the plan, enable **Query Plan** under Help > Preferences in the
Developer Console and compare the cost of each candidate path, where a table scan signals trouble.[^s3] The field list on an object's detail
page has an Indexed column showing which fields carry an index.[^s5]

## When to use it

Request a custom index when a frequently run report, list view or SOQL filter on a large object targets a narrow slice
of rows through an unindexed field. When queries instead read many columns from a wide object, or join an object with
its soft-deleted rows, skinny tables may be the better tool, and the two can be combined.[^s1][^s5]

## Connections

Custom indexes are part of the **large data volumes** toolkit and exist because of the shared-table design of
**multitenancy**.[^s1] They feed the decisions described in **query optimizer selectivity** and are an alternative or
complement to **skinny tables**. **External ID fields** are the self-service route to an index, and the
`CustomIndex` type ties indexes to the **Metadata API**.[^s1][^s2] Index design is examined in the
**Platform Data Architect certification**.[^s3]

## Sources
[^s1]: Salesforce Developers, "Best Practices for Deployments with Large Data Volumes: Indexes". https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-infrastructure-indexes.html (accessed 2026-11-09)
[^s2]: Salesforce Developers, "Metadata API Developer Guide: CustomIndex". https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_customindex.htm (accessed 2026-11-09)
[^s3]: Trailhead, "Database Basics for .NET Developers: Write Efficient Queries". https://trailhead.salesforce.com/content/learn/modules/database_basics_dotnet/writing_efficient_queries (accessed 2026-11-09)
[^s4]: Salesforce Developers Blog, "Force.com SOQL Best Practices: Nulls and Formula Fields". https://developer.salesforce.com/blogs/engineering/2013/02/force-com-soql-best-practices-nulls-and-formula-fields (accessed 2026-11-09)
[^s5]: Salesforce Developers Blog, "Know Thy Salesforce Field Indexes for Fast Reports, List Views, and SOQL". https://developer.salesforce.com/blogs/engineering/2015/06/know-thy-salesforce-field-indexes-fast-reports-list-views-soql (accessed 2026-11-09)
