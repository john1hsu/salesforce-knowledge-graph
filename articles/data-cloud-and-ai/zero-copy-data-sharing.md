---
id: kt:zero-copy-data-sharing
type: Feature
title: Zero Copy Data Sharing
aliases: [Data 360 data sharing, Data Cloud data sharing, Data Shares, Data Share Targets, Zero Copy data out]
domain: data-cloud-and-ai
summary: >-
  The outbound half of Data 360 zero copy: an admin bundles data lake objects, data model objects and calculated
  insight objects into a data share and links it to a data share target, so external platforms such as Snowflake,
  Databricks or another Data 360 org can read the data in place without an ETL copy.
release: "Winter '27"
status: current
broader: [kt:data-cloud]
related: [kt:zero-copy-data-federation, kt:data-cloud-activation, kt:data-model-objects, kt:calculated-insights]
relations:
  - {predicate: implements, object: kt:data-virtualization}
  - {predicate: dependsOn, object: kt:data-spaces}
  - {predicate: dependsOn, object: kt:data-lake-objects}
  - {predicate: alternativeTo, object: kt:data-cloud-activation}
sources:
  - id: s1
    title: "Get Started with Zero Copy Data Sharing (Data 360 with Zero Copy)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-cloud-with-zero-copy/get-started-with-zero-copy-data-sharing
    type: official-learning
    accessed: 2026-11-18
  - id: s2
    title: "Create a Data Share Target to Connect with Databricks"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=data.c360_a_create_data_share_target_databricks.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-18
  - id: s3
    title: "Create Data Share Target to Connect with a Data 360 Org"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=data.c360_a_create_data_share_target_datacloud.htm&type=5
    type: official-docs
    accessed: 2026-11-18
  - id: s4
    title: "Share Your Data from Salesforce Data Cloud to Snowflake"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/08/share-your-data-from-salesforce-data-cloud-to-snowflake
    type: official-blog
    accessed: 2026-11-18
  - id: s5
    title: "Migrate from the legacy Snowflake data share target"
    publisher: Snowflake Documentation
    url: https://docs.snowflake.com/en/user-guide/data-integration/zero-copy/salesforce/migrate-legacy-share
    type: partner
    accessed: 2026-11-18
  - id: s6
    title: "Salesforce Data 360 File Sharing"
    publisher: Microsoft Learn (Azure Databricks documentation)
    url: https://learn.microsoft.com/hi-in/azure/databricks/query-federation/salesforce-data-cloud-file-sharing
    type: partner
    accessed: 2026-11-18
created: 2026-11-18
---

# Zero Copy Data Sharing

Zero Copy Data Sharing is the Data 360 (formerly Data Cloud) capability that exposes selected Data 360 data to an
external platform without loading a copy of it there. It is the mirror image of `kt:zero-copy-data-federation`:
federation brings external data into Data 360, while sharing lets an external system such as Snowflake, a
Databricks lakehouse or an enterprise warehouse read Data 360 data in place, with near real-time access to the
current values.[^s1] Typical uses are giving data science teams harmonized customer profiles for model training,
or joining Salesforce engagement data with warehouse data for analytics, without building and maintaining export
pipelines.[^s1]

## What can be shared

A share can include three kinds of Data 360 object.[^s1]

- **Data lake objects (DLOs):** ingested data stored in Data 360 after it has been cleansed and transformed.[^s1]
- **Data model objects (DMOs):** the harmonized, standard or custom objects built from streams, insights and DLOs.[^s1]
- **Calculated insight objects (CIOs):** the objects produced when a calculated insight runs, holding its measures and dimensions.[^s1]

## How it works

Sharing uses two Setup objects that are created separately and then linked.[^s1]

1. **Data share.** An admin gives the share a unique name, picks a data space and adds the objects. Saving it makes the share active. The data space scopes what can be selected to that space's data.[^s1]
2. **Data share target.** This holds the connection and credentials for one external account. Once an active share is linked to a target, its objects appear in the external system.[^s1]

Each target type has its own handshake.

- **Snowflake:** the Developers Blog walkthrough creates a Snowflake integration user and a custom OAuth security integration, then authenticates the target from Data 360 until it shows Active and Successful.[^s4] The share then appears under Private Sharing as a direct share, which a Snowflake admin mounts as a database.[^s4]
- **Databricks:** Data 360 provides a Core Tenant ID and Tenant Endpoint. The Databricks admin uses them to create a connection, which yields an Account URL and Connection URL to enter on the target.[^s2] Databricks then exposes the share as a Unity Catalog foreign catalog governed by Unity Catalog privileges.[^s6]
- **Another Data 360 org:** the target takes the receiving org's My Domain URL and Org ID. The receiving admin must accept the request, and the source org can resend the invite if the notification doesn't arrive.[^s3]

Data share targets are available in every edition that supports Data 360.[^s2][^s3]

## Limits and gotchas

- **Order matters.** A share must be active before it can be linked to a target.[^s1]
- **Snowflake integration roles.** Snowflake blocks the Account Admin, Org Admin and Security Admin roles as integration users by default, so use another role or a custom one.[^s4]
- **Snowflake V2 migration.** Shares linked to the legacy Snowflake target must be moved to the Snowflake V2 target, which mounts a catalog-linked database through the Zerocopy Connector. The migration is not automatic.[^s5] Link the V2 target before unlinking the legacy one. Snowflake supplies a function that swaps database names so downstream references keep working.[^s5]
- **Databricks compute requirements.** Databricks reads the shared files from cloud object storage on its own compute. It needs a Unity Catalog workspace, Runtime 16.3 or later in standard access mode or a Pro or Serverless SQL warehouse, and it doesn't work on single-user clusters.[^s6]
- **Consumer compute is still billed.** Reads run on the consuming platform's compute, so its charges apply to every query against the shared data.[^s6]

## When to use it (and when not)

Use sharing when a warehouse, lakehouse or ML platform needs Data 360's unified profiles, engagement data or
insights as current, query-ready tables. A share replaces a scheduled export with a governed, near real-time view,
while keeping Data 360's security and governance
standards.[^s1] Use `kt:data-cloud-activation` instead when the goal is to push segment
members to a marketing or advertising destination for action, not to give analysts tables to query. Use
federation, the inbound direction, when the warehouse is the system of record and Data 360 needs to read it.[^s1]

## Connections

Zero Copy Data Sharing is a feature of `kt:data-cloud` and, like federation, **implements**
`kt:data-virtualization`: consumers query data where it lives rather than receiving a replicated copy.[^s1][^s6]
Its inbound counterpart is `kt:zero-copy-data-federation`.[^s1] It **depends on** `kt:data-spaces`, because every share
is scoped to one data space, and on `kt:data-lake-objects`, which together with `kt:data-model-objects` and
`kt:calculated-insights` output are the objects a share can carry.[^s1] It is an **alternative to**
`kt:data-cloud-activation` for getting Data 360 data out: activation publishes segments to destinations, while
sharing exposes whole objects for querying.[^s1][^s4]

## Sources

[^s1]: Trailhead, "Get Started with Zero Copy Data Sharing". https://trailhead.salesforce.com/content/learn/modules/data-cloud-with-zero-copy/get-started-with-zero-copy-data-sharing (accessed 2026-11-18)
[^s2]: Salesforce Help, "Create a Data Share Target to Connect with Databricks". https://help.salesforce.com/s/articleView?id=data.c360_a_create_data_share_target_databricks.htm&language=en_US&type=5 (accessed 2026-11-18)
[^s3]: Salesforce Help, "Create Data Share Target to Connect with a Data 360 Org". https://help.salesforce.com/s/articleView?language=en_US&id=data.c360_a_create_data_share_target_datacloud.htm&type=5 (accessed 2026-11-18)
[^s4]: Salesforce Developers Blog, "Share Your Data from Salesforce Data Cloud to Snowflake" (2024). https://developer.salesforce.com/blogs/2024/08/share-your-data-from-salesforce-data-cloud-to-snowflake (accessed 2026-11-18)
[^s5]: Snowflake Documentation, "Migrate from the legacy Snowflake data share target". https://docs.snowflake.com/en/user-guide/data-integration/zero-copy/salesforce/migrate-legacy-share (accessed 2026-11-18)
[^s6]: Microsoft Learn, "Salesforce Data 360 File Sharing" (Azure Databricks). https://learn.microsoft.com/hi-in/azure/databricks/query-federation/salesforce-data-cloud-file-sharing (accessed 2026-11-18)
