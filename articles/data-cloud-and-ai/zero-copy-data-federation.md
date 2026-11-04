---
id: kt:zero-copy-data-federation
type: Feature
title: Zero Copy Data Federation
aliases: [Zero Copy, Zero Copy Integration, Data 360 query federation, Data 360 file federation]
domain: data-cloud-and-ai
summary: >-
  The Data 360 capability that reads data where it lives in external warehouses and lakehouses (Snowflake,
  Databricks, BigQuery, Redshift and others) through query federation or file federation, instead of copying it
  into Data 360 with ETL pipelines.
release: "Winter '27"
status: current
broader: [kt:data-cloud]
related: [kt:zero-copy-data-sharing, kt:external-objects, kt:data-integration, kt:data-model-objects]
relations:
  - {predicate: implements, object: kt:data-virtualization}
  - {predicate: alternativeTo, object: kt:salesforce-connect}
  - {predicate: dependsOn, object: kt:data-lake-objects}
  - {predicate: coveredBy, object: kt:data-cloud-consultant-certification}
sources:
  - id: s1
    title: "Get Started with Zero Copy Data Federation (Data 360 with Zero Copy)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-cloud-with-zero-copy/get-started-with-zero-copy-data-federation
    type: official-learning
    accessed: 2026-11-04
  - id: s2
    title: "Get Started with Zero Copy Data Sharing (Data 360 with Zero Copy)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/it/content/learn/modules/data-cloud-with-zero-copy/get-started-with-zero-copy-data-sharing
    type: official-learning
    accessed: 2026-11-04
  - id: s3
    title: "Data Stream Settings and Refresh Modes"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=data.c360_a_data_stream_edit_settings.htm
    type: official-docs
    accessed: 2026-11-04
  - id: s4
    title: "Zero Copy Data Federation with Snowflake and Salesforce Data Cloud"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/08/zero-copy-data-federation-with-snowflake-and-salesforce-data-cloud
    type: official-blog
    accessed: 2026-11-04
  - id: s5
    title: "Zero Copy"
    publisher: Salesforce
    url: https://www.salesforce.com/data/connectivity/zero-copy/
    type: official-blog
    accessed: 2026-11-04
  - id: s6
    title: "Set up Salesforce Data Cloud for Zero-Copy"
    publisher: Snowflake Documentation
    url: https://docs.snowflake.com/en/user-guide/data-integration/zero-copy/salesforce/setup-salesforce
    type: partner
    accessed: 2026-11-04
created: 2026-11-04
---

# Zero Copy Data Federation

Zero Copy Data Federation is the Data 360 (formerly Data Cloud) capability that lets the platform use data held in
an external data warehouse or lakehouse without duplicating it. Salesforce describes zero copy as a bidirectional
connection with two halves: **data federation**, in which Data 360 reads external data, and **data sharing**, in
which an external system reads Data 360 data.[^s1] This node covers the federation (inbound) half. Salesforce
positions it as a way to give applications and AI agents current data without building ETL pipelines that replicate
it.[^s5]

## How it works

Federation runs through a zero-copy connector of one of two kinds.[^s1]

- **Query federation:** Data 360 sends queries to the external system's query engine over JDBC and fetches only what
  it needs. The results are processed in memory and discarded, so nothing is persisted in Data 360.[^s5] Every
  compatible system supports this mode, but you may pay the external platform's compute fees for each query.[^s1]
- **File federation:** Data 360 reads the files directly from the external storage layer with its own compute,
  bypassing the warehouse's compute layer. It suits large datasets in open table formats such as Apache Iceberg,
  avoids external compute fees, and is the recommended option where the external system supports it.[^s1] The
  Salesforce product page still labels file federation as beta.[^s5]

Out of the box, Salesforce lists Snowflake, Databricks, Amazon Redshift and Google BigQuery as federation sources,
and its Zero Copy Partner Network includes AWS, Databricks, Google Cloud, Snowflake, Microsoft and IBM.[^s5]
Systems outside the partner network can also be compatible, but not every system supports file federation.[^s1]

Setup is point-and-click. In Salesforce's Snowflake walkthrough, an admin creates a warehouse and an integration user
in Snowflake, registers that user's RSA public key for key-pair authentication, then creates a Snowflake connection
in Data 360 Setup with the account URL, username and private key. A data stream is then created from the Snowflake
connector by choosing the connection, database and schema.[^s4] The federated tables become external data lake
objects that can be mapped to data model objects like ingested data.[^s6]

## Limits and gotchas

- **Trigger-based features need caching.** Under query federation, features that react to changes, such as data
  actions, work only when caching is enabled. File federation can detect changes in the external system without
  it.[^s1]
- **Cost moves rather than disappears.** Zero copy consumes Data 360 credits, and query federation can add
  external compute charges.[^s1]
- **Incremental refresh has a deletion gap.** Incremental refresh works with zero-copy federation, but it doesn't
  delete records during incremental runs. Refresh schedules are set in UTC.[^s3]
- **Key handling.** Data 360 doesn't accept encrypted keys for the Snowflake connection, and the sample integration
  user was granted broad privileges. Salesforce calls the walkthrough a general example, not a complete set of
  best practices.[^s4]
- **Federated data can't be re-shared.** An external data lake object, or a DMO mapped to one, can't be included in a
  zero-copy data share.[^s6]

## When to use it (and when not)

Use federation when the warehouse or lakehouse is already the governed system of record for large or fast-changing
data, such as transactions, telemetry or model scores. Federation avoids pipeline maintenance, keeps data current
without waiting for syncs, and reduces the number of persistent copies to secure.[^s1] Prefer file federation for
very large Iceberg-format tables. Use query federation where file federation isn't supported, or where you need
broad compatibility.[^s1] Ingest the data instead when Data 360 features must react to every change and you can't
enable caching, or when repeated queries would make external compute cost unpredictable.[^s1]

## Connections

Zero copy federation is a feature of `kt:data-cloud` and **implements** `kt:data-virtualization`, leaving data in
the source system.[^s5] Its counterpart `kt:zero-copy-data-sharing` works in the opposite direction, sharing DLOs,
DMOs and calculated insight objects with platforms such as Snowflake or Databricks without copying them.[^s2] It
**depends on** `kt:data-lake-objects`, because federated tables surface as external DLOs that are mapped to
`kt:data-model-objects`.[^s6] It is an **alternative to** `kt:salesforce-connect` and its `kt:external-objects`:
Connect virtualizes external tables inside the CRM org, while zero copy brings them into Data 360's harmonized
model. Both are inbound options in `kt:data-integration` design.[^s1][^s5] Zero-copy connectors are **covered by**
`kt:data-cloud-consultant-certification`.

## Sources

[^s1]: Trailhead, "Get Started with Zero Copy Data Federation". https://trailhead.salesforce.com/content/learn/modules/data-cloud-with-zero-copy/get-started-with-zero-copy-data-federation (accessed 2026-11-04)
[^s2]: Trailhead, "Get Started with Zero Copy Data Sharing". https://trailhead.salesforce.com/it/content/learn/modules/data-cloud-with-zero-copy/get-started-with-zero-copy-data-sharing (accessed 2026-11-04)
[^s3]: Salesforce Help, "Data Stream Settings and Refresh Modes". https://help.salesforce.com/apex/HTViewHelpDoc?id=data.c360_a_data_stream_edit_settings.htm (accessed 2026-11-04)
[^s4]: Salesforce Developers Blog, "Zero Copy Data Federation with Snowflake and Salesforce Data Cloud" (2024). https://developer.salesforce.com/blogs/2024/08/zero-copy-data-federation-with-snowflake-and-salesforce-data-cloud (accessed 2026-11-04)
[^s5]: Salesforce, "Zero Copy". https://www.salesforce.com/data/connectivity/zero-copy/ (accessed 2026-11-04)
[^s6]: Snowflake Documentation, "Set up Salesforce Data Cloud for Zero-Copy". https://docs.snowflake.com/en/user-guide/data-integration/zero-copy/salesforce/setup-salesforce (accessed 2026-11-04)
