---
id: kt:external-objects
type: Feature
title: External Objects
aliases: [external object, __x object, __x objects, virtual objects]
domain: data-model
summary: >-
  Salesforce object definitions, suffixed __x, whose records live in an external system and are read on demand through
  an external data source (Salesforce Connect or Files Connect) instead of being stored in the org.
release: "Winter '27"
status: current
broader: [kt:data-architecture, kt:salesforce-connect]
related: [kt:object-relationships, kt:external-id-fields, kt:big-objects, kt:zero-copy-data-federation, kt:data-integration]
relations:
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: queriedWith, object: kt:sosl}
  - {predicate: dependsOn, object: kt:apex-callouts}
  - {predicate: configuredVia, object: kt:named-credentials}
  - {predicate: requiresLicense, object: kt:salesforce-connect}
  - {predicate: coveredBy, object: kt:platform-data-architect-certification}
sources:
  - id: s1
    title: "External Objects — Object Reference for the Salesforce Platform"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_external_objects.htm
    type: official-docs
    accessed: 2026-11-04
  - id: s2
    title: "More Features Supported by Salesforce Connect"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=platform.platform_connect_general_considerations.htm
    type: official-docs
    accessed: 2026-11-04
  - id: s3
    title: "General Limits for Salesforce Connect—OData 2.0, 4.0, and 4.01 Adapters"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=odata_general_limits.htm&language=en_US
    type: official-docs
    accessed: 2026-11-04
  - id: s4
    title: "Considerations for Salesforce Connect OData Adapters"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=platform.odata_considerations.htm
    type: official-docs
    accessed: 2026-11-04
  - id: s5
    title: "Data Virtualization — Salesforce Architects"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/fundamentals/guide/data-virtualization
    type: official-docs
    accessed: 2026-11-04
  - id: s6
    title: "Quick Start: Salesforce Connect — Create an Indirect Lookup Relationship"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/quickstart-lightning-connect/quickstart-lightning-connect3
    type: official-learning
    accessed: 2026-11-04
  - id: s7
    title: "GitHub Custom Adapter for Salesforce Connect — Apex Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_connector_example_github.htm
    type: official-docs
    accessed: 2026-11-04
created: 2026-11-04
---

# External Objects

An external object is a Salesforce object definition whose records are not stored in the org. Each one is bound to an external data source definition that tells Salesforce how to reach the remote system, and records are fetched on demand, so users always see the current external data rather than a synced copy. External objects are available from API version 32.0 through Salesforce Connect and Files Connect, and their API names end in two underscores and a lowercase x (for example `ExtraLogInfo__x`); the name must still be unique across standard, custom and external objects in the org.[^s1] Salesforce positions them for large datasets you don't want to copy into the org when only a small slice is needed at any one time.[^s1]

## How it works

An administrator defines an external data source (adapter, endpoint, authentication) and then runs **Validate and Sync**, which reads the remote schema and generates external objects and fields. At runtime, list views, detail pages, SOQL and SOSL against the object are translated into callouts to the source.[^s1] The adapters include Cross-Org (another Salesforce org via its REST API), OData 2.0, 4.0 and 4.01, custom adapters written with the Apex Connector Framework, Amazon DynamoDB, SQL adapters for Amazon Athena and Snowflake, a GraphQL adapter, and Files Connect adapters for content repositories; which ones an org can use depends on its add-on license.[^s1][^s2] In a custom adapter, a `DataSource.Provider` class declares capabilities and authentication, and a `DataSource.Connection` class implements `sync()`, `query()` and `search()`, mapping a remote key into the standard `ExternalId` field and a link into `DisplayUrl`.[^s7]

Most platform features that support custom objects also support external objects, including the APIs, SOQL, SOSL and search, packaging, the Metadata API (where they appear as `CustomObject`) and change sets.[^s1][^s2] Salesforce Connect is included in Developer Edition but is an extra-cost add-on in Enterprise, Performance and Unlimited Editions.[^s2]

## Relationships

Because external records rarely carry 18-character Salesforce IDs, external objects add two relationship types beyond the standard lookup: the external lookup and the indirect lookup.[^s1][^s2] An indirect lookup links a child external object to a parent standard or custom object by matching a remote column against a unique external ID field on the parent. Salesforce's GitHub adapter example joins a remote `login` to a Contact field, and the Trailhead quick start joins an external Order's customer ID to an Account field, which surfaces an Orders related list on the Account page.[^s6][^s7]

## Limits and gotchas

For the OData adapters, Salesforce documents an 8 MB limit on HTTP requests and responses, a 16 MB result-set limit per OData query, and 1,000 rows per OData subquery. OData 2.0 and 4.0 also cap new external record IDs at 100k per hour for both long-term and short-term ID mapping; the ID-mapping limits were lifted for OData 4.01 on Hyperforce starting in Spring '25.[^s3] Orgs that hit rate limits can enable **High Data Volume** on the data source, which bypasses most rate limits but changes behaviour: for example, Lightning Experience requires High Data Volume to be off for OData sources (the Cross-Org adapter is exempt).[^s2][^s4] In Salesforce Classic, search results for an external object show only the top 25 rows.[^s2]

Salesforce's architecture guidance adds design gotchas: SOQL joins across multiple external objects aren't supported, so pre-join in the source; every query moves its result set over the network, so latency and egress matter at scale; there is no built-in fallback if the source is down; and callouts are subject to Apex governor limits, so avoid querying in loops and push filters to the source.[^s5]

## When to use it (and when not)

Use external objects when data must stay in its system of record (for regulatory or contractual reasons), when freshness matters more than speed, and when access is read-heavy and selective. Prefer replication when you need heavy reporting, high-frequency or high-volume access, offline resilience, or AI grounding: the architecture guide notes that external objects don't support grounding Agentforce or Einstein features and points to Data 360 as the complement in that case.[^s5] For the authentication choice, a per-user principal gives row-level security and per-user audit at the cost of token management, whereas a named principal is simpler but shared.[^s5]

## Connections

External objects are the object-level surface of **Salesforce Connect** (which also gates them by license), and they extend **object relationships** with the external and indirect lookup types, the latter keyed on **external ID fields**.[^s1][^s6] They are queried with **SOQL** and **SOSL** and depend on **Apex callouts**, with endpoints and credentials typically managed through **named credentials**.[^s2][^s5][^s7] Architecturally they are a virtualization option within **data integration**, contrasted with in-org archival stores such as **big objects** and with **zero copy data federation** into Data Cloud.[^s5]

## Sources
[^s1]: Salesforce Developers, "External Objects — Object Reference for the Salesforce Platform". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_external_objects.htm (accessed 2026-11-04)
[^s2]: Salesforce Help, "More Features Supported by Salesforce Connect". https://help.salesforce.com/apex/HTViewHelpDoc?id=platform.platform_connect_general_considerations.htm (accessed 2026-11-04)
[^s3]: Salesforce Help, "General Limits for Salesforce Connect—OData 2.0, 4.0, and 4.01 Adapters". https://help.salesforce.com/apex/HTViewHelpDoc?id=odata_general_limits.htm&language=en_US (accessed 2026-11-04)
[^s4]: Salesforce Help, "Considerations for Salesforce Connect OData Adapters". https://help.salesforce.com/apex/HTViewHelpDoc?id=platform.odata_considerations.htm (accessed 2026-11-04)
[^s5]: Salesforce Architects, "Data Virtualization". https://architect.salesforce.com/docs/architect/fundamentals/guide/data-virtualization (accessed 2026-11-04)
[^s6]: Trailhead, "Quick Start: Salesforce Connect — Create an Indirect Lookup Relationship". https://trailhead.salesforce.com/content/learn/projects/quickstart-lightning-connect/quickstart-lightning-connect3 (accessed 2026-11-04)
[^s7]: Salesforce Developers, "GitHub Custom Adapter for Salesforce Connect — Apex Developer Guide". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_connector_example_github.htm (accessed 2026-11-04)
