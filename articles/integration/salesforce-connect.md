---
id: kt:salesforce-connect
type: Product
title: Salesforce Connect
aliases: [Salesforce Connect add-on, Salesforce Connect adapters]
domain: integration
summary: >-
  Salesforce's add-on for data virtualization: it defines external data sources (OData, Cross-Org, custom Apex,
  Amazon, Snowflake, GraphQL and other adapters) and surfaces their records as external objects queried live at
  runtime, so users and automation can work with outside data without copying it into the org.
release: "Winter '27"
status: current
broader: [kt:data-integration]
related: [kt:zero-copy-data-federation, kt:change-data-capture, kt:mulesoft-anypoint-platform]
relations:
  - {predicate: hasPart, object: kt:external-objects}
  - {predicate: implements, object: kt:data-virtualization}
  - {predicate: dependsOn, object: kt:named-credentials}
  - {predicate: contrastsWith, object: kt:batch-data-synchronization}
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: coveredBy, object: kt:integration-architect-certification}
sources:
  - id: s1
    title: "Salesforce Connect — Access External Data with the OData 2.0, 4.0, or 4.01 Adapter"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=platform.salesforce_connect_odata.htm
    type: official-docs
    accessed: 2026-11-04
  - id: s2
    title: "Get Started with the Apex Connector Framework — Apex Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connector_start.htm
    type: official-docs
    accessed: 2026-11-04
  - id: s3
    title: "Writable External Objects Considerations for Salesforce Connect"
    publisher: Salesforce Help
    url: https://help.salesforce.com/HTViewHelpDoc?id=platform_connect_considerations_writable_external_objects.htm
    type: official-docs
    accessed: 2026-11-04
  - id: s4
    title: "Track Data Changes for Salesforce Connect External Objects (External Change Data Capture)"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=platform.external_object_change_tracking_intro.htm
    type: official-docs
    accessed: 2026-11-04
  - id: s5
    title: "Data Virtualization — Salesforce Architects"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/fundamentals/guide/data-virtualization
    type: official-docs
    accessed: 2026-11-04
  - id: s6
    title: "Learn MOAR in Winter '23 with the Salesforce Connect Adapter for Amazon Athena"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2022/09/learn-moar-in-winter-23-with-the-salesforce-connect-adapter-for-amazon-athena
    type: official-blog
    accessed: 2026-11-04
created: 2026-11-04
---

# Salesforce Connect

Salesforce Connect is the Salesforce add-on that lets users and processes work with data held outside the org without importing it. An administrator registers an external data source, Salesforce reads its schema, and the remote tables appear as external objects that are fetched on demand whenever someone opens a list view, runs a query or triggers automation.[^s1] Salesforce's architecture guidance classifies this as data virtualization, a zero-copy pattern in which no ETL pipeline writes rows into the org and the external system stays the system of record.[^s5] Typical use cases are back-office data such as ERP orders or invoices that users need to see next to CRM records.[^s1]

## How it works

Every connection starts with an **external data source** that picks an adapter. The current adapter family covers OData 2.0, 4.0 and 4.01; a Cross-Org adapter for another Salesforce org; custom adapters written with the Apex Connector Framework; Amazon DynamoDB; SQL adapters for Amazon Athena and Snowflake; a GraphQL adapter; and adapters for Privacy Center and the Salesforce archive data store.[^s1] After **Validate and Sync**, Salesforce generates external objects, and queries against them are translated into callouts to the source, with filters, sort order and limits pushed down so that only the result set travels back.[^s1][^s5] Large result sets are paged either by the client or by the server.[^s1]

Credentials are not stored on the data source itself. The trust chain runs from the external data source to a named credential, then an external credential and an auth provider, and users need profile or permission-set access to the external credential or queries fail.[^s5] With a **named principal**, one service identity serves everyone, which is simple but loses per-user audit; with a **per-user principal**, each user authenticates with their own token, enabling source-side row-level security at the cost of token management.[^s5]

When no packaged adapter fits, developers write a custom one: a class extending `DataSource.Connection` describes the schema and answers queries and searches, and a class extending `DataSource.Provider` declares its capabilities; the adapter then appears in Setup as a new data source type.[^s2] Amazon adapters were added over time; the Athena adapter, for example, arrived in Winter '23 so admins could reach data in Amazon S3 and Redshift without copying it.[^s6]

## Licensing, writes and change tracking

Salesforce Connect is not included in every edition, and the Snowflake SQL adapter needs its own add-on license beyond the base entitlement.[^s5] The `DataSource.Connection` class used by custom adapters likewise requires a Salesforce Connect add-on license.[^s2] Writable external objects are available in Developer Edition and at extra cost in Enterprise, Performance and Unlimited Editions.[^s3]

External objects are read-only by default. Writes can be switched on per data source, but the remote system executes them and resolves conflicts, Salesforce can't guarantee that every write lands, and saving external and regular object changes in one transaction throws an error. Apex writes go through an asynchronous background queue, while UI and flow writes run synchronously. Writes are not available for high-data-volume external objects or Amazon Athena sources.[^s3]

**External Change Data Capture** lets automation react to changes in the remote system. It works only with the OData 4.0 and 4.01 adapters, must be enabled on the data source and on each tracked object, and polls the source every 30 minutes by default, or as often as every 5 minutes. Changes are published to a change event channel that Streaming API clients or Apex triggers can subscribe to.[^s4]

## Limits and gotchas

Because every access is a callout, Apex governor limits shape the design: the architecture guide cites 100 callouts per transaction and a 120-second callout timeout, and it warns against querying external objects inside loops.[^s5] It also notes that there is no cache or fallback when the source is down, that zero-copy still means paying for network egress, and that Snowflake warehouses which auto-suspend can add several seconds to the first query.[^s5] Einstein and Agentforce features don't use external objects for grounding or actions, so Salesforce points to Data 360 for AI scenarios.[^s5]

## When to use it (and when not)

Choose Salesforce Connect when access is read-heavy and selective, freshness matters, or residency or governance rules forbid copying the data. Prefer replication when you need multi-object joins, heavy reporting, high-frequency or high-volume access, or native objects for automation and AI.[^s5]

## Connections

Salesforce Connect sits under **data integration** as its virtual branch and **implements data virtualization**, in **contrast to batch data synchronization**.[^s5] Its object-level surface is **external objects**, and it **depends on named credentials** for callout authentication.[^s1][^s5] Callouts are **governed by governor limits**.[^s5] External Change Data Capture extends the platform's **change data capture** model to remote data.[^s4] **Zero copy data federation** in Data 360 is the complementary path for analytics and AI, **MuleSoft Anypoint Platform** is the option when data must be orchestrated or transformed rather than viewed in place, and the topic is covered by the **Integration Architect certification**.[^s5]

## Sources
[^s1]: Salesforce Help, "Salesforce Connect — Access External Data with the OData 2.0, 4.0, or 4.01 Adapter". https://help.salesforce.com/apex/HTViewHelpDoc?id=platform.salesforce_connect_odata.htm (accessed 2026-11-04)
[^s2]: Salesforce Developers, "Get Started with the Apex Connector Framework — Apex Developer Guide". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connector_start.htm (accessed 2026-11-04)
[^s3]: Salesforce Help, "Writable External Objects Considerations for Salesforce Connect". https://help.salesforce.com/HTViewHelpDoc?id=platform_connect_considerations_writable_external_objects.htm (accessed 2026-11-04)
[^s4]: Salesforce Help, "Track Data Changes for Salesforce Connect External Objects (External Change Data Capture)". https://help.salesforce.com/apex/HTViewHelpDoc?id=platform.external_object_change_tracking_intro.htm (accessed 2026-11-04)
[^s5]: Salesforce Architects, "Data Virtualization". https://architect.salesforce.com/docs/architect/fundamentals/guide/data-virtualization (accessed 2026-11-04)
[^s6]: Salesforce Developers Blog, "Learn MOAR in Winter '23 with the Salesforce Connect Adapter for Amazon Athena". https://developer.salesforce.com/blogs/2022/09/learn-moar-in-winter-23-with-the-salesforce-connect-adapter-for-amazon-athena (accessed 2026-11-04)
