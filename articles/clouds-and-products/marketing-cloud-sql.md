---
id: kt:marketing-cloud-sql
type: Language
title: Marketing Cloud SQL
aliases: [SFMC SQL, Marketing Cloud Engagement SQL, SQL Query activity language, Marketing Cloud query activity SQL]
domain: clouds-and-products
summary: >-
  The SQL used in Marketing Cloud Engagement to read data extensions and system data views and write the
  result set into a target data extension, usually through a SQL Query activity in Automation Studio, with an
  Append, Update or Overwrite data action and a 30-minute timeout per query.
release: "Winter '27"
status: current
broader: [kt:marketing-cloud-engagement]
related: [kt:data-extensions, kt:journey-builder, kt:contact-builder, kt:marketing-cloud-data-views, kt:query-studio]
relations:
  - {predicate: consumedBy, object: kt:automation-studio}
  - {predicate: dependsOn, object: kt:data-extensions}
  - {predicate: dependsOn, object: kt:marketing-cloud-data-views}
  - {predicate: contrastsWith, object: kt:soql}
sources:
  - id: s1
    title: "Query Data with SQL (Marketing Cloud Engagement Data Management)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-data-management/query-data-with-sql
    type: official-learning
    accessed: 2026-11-27
  - id: s2
    title: "Run SQL Queries in Automation Studio (Automation Studio Activities)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/automation-studio-activities/run-sql-queries-in-automation-studio
    type: official-learning
    accessed: 2026-11-27
  - id: s3
    title: "Automation Studio and SQL in Marketing Cloud"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2023/02/automation-studio-and-sql-in-marketing-cloud
    type: official-blog
    accessed: 2026-11-27
created: 2026-11-27
---

# Marketing Cloud SQL

Marketing Cloud SQL is the query language Marketing Cloud Engagement practitioners use to segment, join and reshape subscriber and tracking data. A query reads from data extensions and from read-only system data views, and its result set is written into a target data extension rather than returned to the caller.[^s1][^s2] It is not SOQL: it works on Marketing Cloud's own tables instead of core platform objects, and it is built around set-based joins and filters.[^s1][^s3]

## How it works

Queries run inside a SQL Query activity. In Automation Studio you add the activity to an automation, create a new query activity with a name, external key, folder and description, write the statement, validate it, pick the target data extension and choose a data action, then save.[^s1][^s2] The automation's starting source (a schedule or a file drop) decides when the query fires.[^s1]

The data action controls what happens to the target: **Append** adds the rows to what is already there, **Update** changes existing rows and appends new ones, and **Overwrite** replaces the whole contents with the new result.[^s1][^s2] Because Update matches on existing rows, the target's primary key (for example a ContactID or ContactKey field) decides what counts as the same record.[^s2]

The core syntax is familiar: SELECT, FROM, JOIN (inner, left, right and full outer) and WHERE, with table aliases, and the keywords are not case sensitive.[^s1] Names that contain spaces go in square brackets, and a data extension shared from the parent business unit is referenced with an `ent.` prefix.[^s1] Date logic in the official examples uses functions such as DATEADD and GETDATE to build rolling windows.[^s1][^s3]

System data views are prebuilt tables, named with a leading underscore, that expose send and engagement history: Trailhead's examples include `_Sent`, `_Open`, `_Click`, `_Bounce`, `_Complaint`, `_Journey`, `_JourneyActivity` and `_Subscribers`.[^s1][^s2] They cannot be modified, so a common pattern is to query them into a data extension for reporting or targeting.[^s1] Open and click times are recorded in Central Standard Time without daylight saving.[^s1] Data extensions usually lack a subscriber's status, so queries that need it join to a subscriber list such as All Subscribers.[^s3]

## Limits and gotchas

- **Timeout:** a query times out after 30 minutes, and larger scans are the likeliest to hit it.[^s1]
- **Auto-deactivation:** a SQL Query activity that fails 24 consecutive times is deactivated, in every account, and this cannot be switched off.[^s3]
- **Validation is partial:** Validate Syntax checks the statement's structure and that referenced sources exist, but it does not catch mismatches between selected columns and target fields.[^s2]
- **Date ranges:** Salesforce advises keeping requests to roughly the previous six months of data where possible.[^s2][^s3]
- **SELECT \*:** listing every column slows queries down, so name only the fields you need.[^s1]
- **Outer joins** can produce very large result sets, so use them with care.[^s1]

## Performance and practice

Narrow each query's scope, split queries that could produce a lot of data into segments, and put the fields used in JOIN, WHERE, GROUP BY and ORDER BY on indexed columns where you can.[^s2][^s3] Don't run an Import activity and a query against the same data extension at once. Stagger hourly automations 5 to 15 minutes apart, for example starting at 12:05 or 12:15 rather than on the hour.[^s3] Create the target data extension before you build the activity. To test a statement without creating a target, the developer blog suggests the free Query Studio app from Salesforce Labs.[^s3]

## When to use it (and when not)

Use Marketing Cloud SQL for scheduled segmentation, for shaping data before a send or journey entry, and for turning tracking data views into reportable tables.[^s2][^s3] For complex unification or segmentation of very large datasets, the developer blog points to a data warehouse or a customer data platform instead of chained queries.[^s3]

## Connections

Marketing Cloud SQL sits under `kt:marketing-cloud-engagement` and is **consumed by** `kt:automation-studio`, whose SQL Query activity runs it on a schedule or file drop.[^s1][^s2] It **depends on** `kt:data-extensions`, which are both its inputs and its required targets, and on `kt:marketing-cloud-data-views`, the system tables that hold send, open, click, bounce and journey history.[^s1][^s2] It reads journey history from `kt:journey-builder` through the `_Journey` and `_JourneyActivity` views, and shared data extensions in `kt:contact-builder` are reached with the `ent.` prefix.[^s1][^s2] `kt:query-studio` is the companion tool for testing queries.[^s3] It **contrasts with** `kt:soql`, the platform's object query language, since Marketing Cloud SQL writes result sets into tables instead of returning records to code.[^s1][^s3]

## Sources

[^s1]: Trailhead, "Query Data with SQL (Marketing Cloud Engagement Data Management)". https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-data-management/query-data-with-sql (accessed 2026-11-27)
[^s2]: Trailhead, "Run SQL Queries in Automation Studio (Automation Studio Activities)". https://trailhead.salesforce.com/content/learn/modules/automation-studio-activities/run-sql-queries-in-automation-studio (accessed 2026-11-27)
[^s3]: Salesforce Developers Blog, "Automation Studio and SQL in Marketing Cloud". https://developer.salesforce.com/blogs/2023/02/automation-studio-and-sql-in-marketing-cloud (accessed 2026-11-27)
