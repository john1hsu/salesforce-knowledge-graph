---
id: kt:skinny-tables
type: Feature
title: Skinny Tables
aliases: [skinny table, Salesforce skinny tables, skinny indexes]
domain: platform-architecture
summary: >-
  Support-enabled, platform-maintained database tables that hold a chosen subset of an object's standard and custom
  fields in one place, letting read-only reports, list views and SOQL on very large objects skip joins and soft-deleted rows.
release: "Winter '27"
status: current
broader: [kt:large-data-volumes]
related: [kt:query-optimizer-selectivity, kt:soql, kt:sandbox-types, kt:data-skew, kt:big-objects]
relations:
  - {predicate: partOf, object: kt:large-data-volumes}
  - {predicate: alternativeTo, object: kt:custom-indexes}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: coveredBy, object: kt:platform-data-architect-certification}
sources:
  - id: s1
    title: "Best Practices for Deployments with Large Data Volumes: Skinny Tables"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-infrastructure-skinny-tables.html
    type: official-docs
    accessed: 2026-11-06
  - id: s2
    title: "Large Data Volumes: Conduct Data Queries and Searches"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/modules/large-data-volumes/units/conduct-data-queries-and-searches
    type: official-learning
    accessed: 2026-11-06
  - id: s3
    title: "Long- and Short-Term Approaches for Tuning Force.com Performance"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/engineering/2013/03/long-and-short-term-approaches-for-tuning-force-com-performance
    type: official-blog
    accessed: 2026-11-06
created: 2026-11-06
---

# Skinny Tables

A skinny table is a database table that Salesforce builds and maintains on an org's behalf, holding a hand-picked subset of fields from one standard or custom object. It exists for one reason: making read-heavy operations such as reports, list views and SOQL queries faster on objects with millions of records.[^s1][^s2] Customers never see or query a skinny table directly; the platform decides at query time whether a skinny table can serve a request, so reports, Apex and API calls need no changes.[^s3]

## How it works

Under the multitenant data model, an object's standard fields and custom fields live in separate underlying tables, so a query that touches both kinds of field needs a join. A skinny table stores the selected standard and custom fields side by side, removing that join for queries that reference only fields it contains.[^s1] Its rows are also narrower than the base table's, so the database scans less data and returns more rows per fetch, which raises throughput on large objects.[^s3]

Two further effects help. Skinny tables leave out soft-deleted records (rows in the Recycle Bin), which can shrink the volume scanned, and they replicate the base object's custom indexes, which then often perform better because fewer joins are involved.[^s2][^s3] The platform keeps the skinny table synchronized with its source automatically whenever the base records change.[^s1][^s3]

## Enabling and maintaining one

There is no setup page. An org asks Salesforce Customer Support to create a skinny table, and once it exists Salesforce uses it automatically where appropriate; customers cannot create, access or modify it themselves.[^s1] The definition is fixed to the fields chosen at creation, so adding a field to the report, list view or query that motivated it means going back to Support to update or re-create it.[^s1][^s2] Changing the data type of an included field invalidates the skinny table and likewise needs a Support request.[^s2]

## Limits and gotchas

Verified against the current Large Data Volumes guide for Winter '27:[^s1]

- **Objects:** custom objects plus Account, Contact, Opportunity, Lead and Case.
- **Columns:** a maximum of 200. Older guidance from 2013 cited 100 fields, so check the current guide rather than older blog posts.[^s3]
- **Field types:** checkbox, currency, date, date/time, email, number, percent, phone, multi-select picklist, text, text area, long text area and URL. Skinny tables and skinny indexes can hold encrypted data.
- **No cross-object fields:** a skinny table can't include fields from other objects. The 2013 engineering guidance also excluded formula fields and lookup-derived values.[^s3]
- **Sandboxes:** skinny tables are copied to Full sandboxes only; for other sandbox types, Support must activate them. This differs from the 2013 guidance, which said they were not copied to sandboxes at all.[^s1][^s3]
- **Overhead:** keeping a second copy of live data has a cost, and using a skinny table in the wrong context can make performance worse.[^s1]

## When to use it (and when not)

Salesforce frames skinny tables as a later step. First tune queries and add well-placed custom indexes so filters are selective. Ask for a skinny table only when reports, dashboards or SOQL on a very large object still time out after that work.[^s2][^s3] They suit stable, read-only workloads whose field set changes rarely, such as standard operational reports. They are a poor fit when the query's fields change often, because every change needs Support.[^s2] The guide also suggests designing the skinny table to avoid repeated computation. For example, filter on a stored year field instead of recalculating a date range for every annual report.[^s1]

## Connections

Skinny tables are one of the main tools in **large data volumes** work, alongside index design and the selectivity rules described in **query optimizer selectivity**; they are an alternative to, and often follow, adding custom indexes.[^s2] They accelerate **SOQL**, reports and list views without code changes.[^s3] Their copy behavior matters for **sandbox types** planning, because only Full sandboxes receive them automatically.[^s1] They don't fix lock contention from **data skew**, and for data you only need to keep rather than report on, archiving into **big objects** is the more appropriate tool. Skinny tables sit in the large-data-volume material that the **Platform Data Architect certification** targets, which is why the node links to it.

## Sources

[^s1]: Salesforce Developers, "Best Practices for Deployments with Large Data Volumes: Skinny Tables". https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-infrastructure-skinny-tables.html (accessed 2026-11-06)
[^s2]: Trailhead, "Large Data Volumes: Conduct Data Queries and Searches". https://trailhead.salesforce.com/modules/large-data-volumes/units/conduct-data-queries-and-searches (accessed 2026-11-06)
[^s3]: Salesforce Developers Blog, "Long- and Short-Term Approaches for Tuning Force.com Performance" (2013). https://developer.salesforce.com/blogs/engineering/2013/03/long-and-short-term-approaches-for-tuning-force-com-performance (accessed 2026-11-06)
