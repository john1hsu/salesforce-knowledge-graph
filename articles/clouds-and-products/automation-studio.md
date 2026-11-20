---
id: kt:automation-studio
type: Feature
title: Automation Studio
aliases: [Marketing Cloud Automation Studio, SFMC Automation Studio, Marketing Cloud Engagement Automation Studio]
domain: clouds-and-products
summary: >-
  The Marketing Cloud Engagement application for building multi-step batch automations (imports, SQL query
  activities, file transfers, scripts, sends, list refreshes and Journey Builder events) that run on a schedule,
  immediately, from an API trigger or when a file lands in a folder.
release: "Winter '27"
status: current
broader: [kt:marketing-cloud-engagement]
related: [kt:salesforce-marketing-solutions, kt:schedule-triggered-flow, kt:data-extensions]
relations:
  - {predicate: partOf, object: kt:marketing-cloud-engagement}
  - {predicate: integratesWith, object: kt:journey-builder}
  - {predicate: dependsOn, object: kt:contact-builder}
  - {predicate: queriedWith, object: kt:marketing-cloud-sql}
sources:
  - id: s1
    title: "Automate Marketing Cloud Engagement Tasks with Automation Studio (Automation Studio Activities)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/automation-studio-activities/automate-marketing-cloud-tasks
    type: official-learning
    accessed: 2026-11-20
  - id: s2
    title: "Run SQL Queries in Automation Studio (Automation Studio Activities)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/automation-studio-activities/run-sql-queries-in-automation-studio
    type: official-learning
    accessed: 2026-11-20
  - id: s3
    title: "Automation Studio and SQL in Marketing Cloud"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2023/02/automation-studio-and-sql-in-marketing-cloud
    type: official-blog
    accessed: 2026-11-20
  - id: s4
    title: "Query Data with SQL (Marketing Cloud Engagement Data Management)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-data-management/query-data-with-sql
    type: official-learning
    accessed: 2026-11-20
  - id: s5
    title: "Automation Studio for Marketing Cloud Engagement (module overview)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/automation-studio-activities
    type: official-learning
    accessed: 2026-11-20
created: 2026-11-20
---

# Automation Studio

Automation Studio is the part of Marketing Cloud Engagement that runs multi-step marketing and data tasks without someone clicking through them each time. An **automation** is a sequence of steps, each holding one or more **activities**, and it can run on an immediate, triggered or scheduled basis.[^s1][^s3] Where Journey Builder moves individual contacts through a customer journey, Automation Studio is the batch engine behind it: importing files, reshaping data extensions with SQL, refreshing lists and pushing audiences into journeys.[^s1] Trailhead classes the topic as intermediate developer material, covering activities, SQL queries, API-triggered runs and troubleshooting.[^s5]

## How it works

Each automation has a **starting source** that decides when it runs:[^s1]

- **Schedule**: run at a set date, time and recurrence.[^s1]
- **Run once**: start immediately, useful for one-off loads and tests.[^s1]
- **API event**: run when an external system calls the trigger (Trailhead's module has a unit on API-triggered automations).[^s1][^s5]
- **File drop**: start when a .zip file lands in a designated folder on the account's file location.[^s1]

Activities fall into a few families. Messaging activities send email, push or SMS. Data activities include **Data Copy or Import** (formerly Import File), **File Transfer** to or from FTP, the **SQL Query** activity, **Server-side JavaScript** and **Refresh** for email groups and mobile lists. Utility activities add a **Wait** and run **Reports**. Journey activities include **Fire Event** and **Journey Entry Audience**, which hand contacts to Journey Builder.[^s1]

Steps run in order, and activities within one step run together. A common chain is: a file drop imports to a data extension, a SQL query segments it, and a later step sends an email or fires a journey event.[^s1]

## The SQL Query activity

The SQL Query activity is the most heavily used. You give it a name, external key and folder, write the query, validate the syntax, choose a **target data extension**, and choose whether the results **append**, **update** or **overwrite** that target.[^s2] Queries can read data extensions and system **data views** such as `_Sent`, `_Open`, `_Click`, `_Bounce`, `_Subscribers` and `_Journey`, so engagement and journey history can be joined to your own profile data.[^s2][^s4] Shared data extensions in a parent business unit are reached with the `ent.` prefix.[^s4] Click and open data in the data views is stored in Central Standard Time, with no daylight saving adjustment.[^s4]

## Limits and gotchas

- **Timeout**: Trailhead states that queries time out after 30 minutes.[^s4]
- **Auto-deactivation**: a SQL Query activity is deactivated after 24 consecutive failures, and this behavior can't be turned off. Once inactive, an automation won't run again until it's fixed and reactivated.[^s3]
- **Same-step ordering**: an activity that reads a data extension must sit in a later step than the query that fills it. Putting both in one step returns no results.[^s1]
- **Silent mismatches**: if a selected column name doesn't match a target field, the query may not raise an error. It just leaves data missing, so always validate syntax and check the target.[^s2]
- **Scope and contention**: limit query date ranges to roughly six months.[^s2][^s3] Stagger hourly automations five to 15 minutes apart, and avoid running an import and a query against the same data extension at the same time.[^s3]
- **Performance**: filter, join and sort on indexed fields where possible. Use `SELECT *` sparingly and be careful with outer joins, which can return very large result sets.[^s3][^s4]

## When to use it (and when not)

Use Automation Studio for recurring, set-based data work inside Marketing Cloud Engagement: nightly imports, segmentation queries, suppression lists and scheduled batch sends.[^s1][^s3] Use Journey Builder when each contact needs an individual, multi-step path with waits and decision splits. Automation Studio often feeds those journeys through Fire Event or Journey Entry Audience.[^s1] For heavy data unification and segmentation across many sources, Salesforce's developer blog suggests a dedicated data platform instead of more SQL activities, pointing to a data warehouse or to Genie.[^s3] For record automation on the core CRM platform, the equivalent tools are Flow types such as schedule-triggered flows, not Automation Studio.

## Connections

Automation Studio is `partOf` **Marketing Cloud Engagement** and sits in the wider **Salesforce marketing solutions** family.[^s1] It `integratesWith` **Journey Builder** through its journey activities.[^s1] It `dependsOn` **Contact Builder**, the relational data model of data extensions and data views that its imports and queries read and write.[^s4] It is `queriedWith` **Marketing Cloud SQL**, the SQL dialect used by Query activities against data extensions and data views.[^s2][^s4] It relates to **data extensions** as its main input and output. It is also a conceptual counterpart of the core platform's **schedule-triggered flow**, since both run batch work on a schedule in different products.[^s1]

## Sources

[^s1]: Trailhead, "Automate Marketing Cloud Engagement Tasks with Automation Studio". https://trailhead.salesforce.com/content/learn/modules/automation-studio-activities/automate-marketing-cloud-tasks (accessed 2026-11-20)
[^s2]: Trailhead, "Run SQL Queries in Automation Studio". https://trailhead.salesforce.com/content/learn/modules/automation-studio-activities/run-sql-queries-in-automation-studio (accessed 2026-11-20)
[^s3]: Salesforce Developers Blog, "Automation Studio and SQL in Marketing Cloud" (2023-02-02). https://developer.salesforce.com/blogs/2023/02/automation-studio-and-sql-in-marketing-cloud (accessed 2026-11-20)
[^s4]: Trailhead, "Query Data with SQL". https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-data-management/query-data-with-sql (accessed 2026-11-20)
[^s5]: Trailhead, "Automation Studio for Marketing Cloud Engagement" (module). https://trailhead.salesforce.com/content/learn/modules/automation-studio-activities (accessed 2026-11-20)
