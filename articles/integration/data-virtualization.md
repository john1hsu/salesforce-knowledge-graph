---
id: kt:data-virtualization
type: Pattern
title: Data Virtualization
aliases: [data virtualization pattern, virtual integration pattern, zero-copy data access]
domain: integration
summary: >-
  The synchronous Salesforce integration pattern in which Salesforce reads external data in real time at the moment
  it is needed, typically through Salesforce Connect external objects, instead of copying it into the org and
  reconciling the copy.
release: "Winter '27"
status: concept
broader: [kt:integration-patterns]
related: [kt:salesforce-connect, kt:external-objects, kt:zero-copy-data-federation, kt:apex-callouts]
relations:
  - {predicate: partOf, object: kt:integration-patterns}
  - {predicate: dependsOn, object: kt:named-credentials}
  - {predicate: contrastsWith, object: kt:batch-data-synchronization}
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: coveredBy, object: kt:integration-architect-certification}
sources:
  - id: s1
    title: "Data Virtualization — Salesforce Architects"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/fundamentals/guide/data-virtualization
    type: official-docs
    accessed: 2026-11-05
  - id: s2
    title: "Integration Patterns Overview"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/integration-patterns
    type: official-docs
    accessed: 2026-11-05
  - id: s3
    title: "Pattern Selection Guide (Integration Patterns and Practices)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.integration_patterns_and_practices.meta/integ/integ_pat_selection_guide.htm
    type: official-docs
    accessed: 2026-11-05
  - id: s4
    title: "External Objects — Object Reference for the Salesforce Platform"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_external_objects.htm
    type: official-docs
    accessed: 2026-11-05
  - id: s5
    title: "Integrating with Salesforce Connect (Heroku Enterprise Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce_heroku_integration/integrating_with_salesforce_connect
    type: official-learning
    accessed: 2026-11-05
created: 2026-11-05
---

# Data Virtualization

Data Virtualization is the pattern in Salesforce's integration catalogue for the scenario in which Salesforce accesses external data in real time. Because nothing is persisted, there is no copy to reconcile between Salesforce and the external system.[^s2] The pattern selection guide places it under **virtual integration** with **synchronous** timing, as a separate category from process and data integration. Virtual integrations are always started by an event on the Salesforce side, such as a user action, a search or a record update.[^s3] Salesforce's architect guidance sums up the principle as data staying at its source, with the platform projecting a schema over it and querying it live.[^s1]

## The problem it solves

Copying external data into Salesforce with ETL creates three recurring costs. The copy is stale between loads, every copy widens compliance and governance scope, and pipelines need ongoing monitoring, failure handling and schema-drift management.[^s1] Virtualization trades those costs for a runtime dependency on the source: each query returns data as it is at execution time, so there is no replication lag.[^s1] The Trailhead treatment makes the same point. Salesforce Connect data stays in sync because it is fetched on request rather than stored, and its main use case is an external system whose data is useful inside the standard Salesforce UI.[^s5]

## How it works

The usual mechanism is **external objects** delivered by Salesforce Connect. They resemble custom objects, but their records live outside the org and are retrieved through web service callouts. API names end in `__x`.[^s4] Each external object belongs to an external data source definition. Salesforce Connect adapters include Cross-Org (using the REST API of another Salesforce org), OData 2.0 and 4.0, and custom adapters built with the Apex Connector Framework.[^s4] A custom adapter extends `DataSource.Connection`: `sync()` describes the table structure, `query()` fetches rows each time a user opens records, and `search()` handles searches.[^s5] Because external data usually lacks 18-character Salesforce IDs, relationships use external lookups and indirect lookups rather than standard lookups.[^s4]

The architect guide works through a Snowflake example. Salesforce translates SOQL into SQL and sends it over an authenticated HTTPS callout. Snowflake runs it on a virtual warehouse and returns only the result set. Credentials flow from the external data source through a named credential and external credential to an auth provider.[^s1] That SQL adapter needs its own add-on license on top of base Salesforce Connect.[^s1]

## Design choices

- **Identity model.** Named Principal is simpler but gives no per-user audit or fine-grained source access control. Per-User Principal supports row-level security and per-user audit trails at the cost of more token management, and is the recommended choice for regulated data and PII.[^s1]
- **Dual-layer security.** Source controls (row-level security, masking, roles) and Salesforce controls (profiles, permission sets, field-level security, sharing) both apply on every query. Tokens are kept in the encrypted credential store.[^s1]
- **Tiered approach.** Virtualize for live access, and keep a small replicated fallback for a few critical fields.[^s1]

## Limits and gotchas

The architect guide lists these constraints for the pattern:[^s1]

- 100 callouts per Apex transaction, a 120-second maximum callout timeout and the 50,000-row SOQL limit all apply.[^s1]
- Joins across external objects aren't supported, and in the Snowflake design the objects are read-only.[^s1]
- Zero copy does not mean zero transmission. Large result sets and frequent queries bring egress cost and latency, so high-volume workloads are a poor fit.[^s1]
- There is no cache. A source outage surfaces directly to users, and a cold warehouse can add 5–30 seconds to the first query. A role mismatch at the source can silently return zero rows.[^s1]

Recommended practices are to avoid querying external objects inside loops, push `WHERE` filters to the source, expose curated views with joins pre-materialized at the source, and validate licensing, limit exposure and OAuth setup in a sandbox first.[^s1]

## When to use it (and when not)

Virtualize when access is read-heavy and freshness matters, governance or residency rules discourage copying, and the external system is already the system of record.[^s1] Prefer replication when users need writes or multi-object joins, when access is high-frequency, or when Einstein and Agentforce features need the data as native records. For AI activation, the guide suggests Data 360 as a complement.[^s1]

## Connections

Data Virtualization is part of `kt:integration-patterns`, the catalogue's synchronous virtual-integration entry.[^s2][^s3] `kt:salesforce-connect` is its main implementation on the core platform, and it surfaces data as `kt:external-objects`.[^s4][^s5] `kt:zero-copy-data-federation` applies the same leave-it-in-place idea inside Data 360. The pattern **depends on** `kt:named-credentials` for authenticated callouts and is **governed by** `kt:governor-limits` such as callout and row caps, and custom adapters relate it to `kt:apex-callouts`.[^s1] It **contrasts with** `kt:batch-data-synchronization`, which copies data in bulk on a schedule.[^s2] The edge to `kt:integration-architect-certification` reflects that the integration patterns are that credential's shared design vocabulary.

## Sources
[^s1]: Salesforce Architects, "Data Virtualization". https://architect.salesforce.com/docs/architect/fundamentals/guide/data-virtualization (accessed 2026-11-05)
[^s2]: Salesforce Architects, "Integration Patterns Overview". https://architect.salesforce.com/fundamentals/integration-patterns (accessed 2026-11-05)
[^s3]: Salesforce Developers, "Pattern Selection Guide". https://developer.salesforce.com/docs/atlas.en-us.integration_patterns_and_practices.meta/integ/integ_pat_selection_guide.htm (accessed 2026-11-05)
[^s4]: Salesforce Developers, "External Objects". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_external_objects.htm (accessed 2026-11-05)
[^s5]: Trailhead, "Integrating with Salesforce Connect". https://trailhead.salesforce.com/content/learn/modules/salesforce_heroku_integration/integrating_with_salesforce_connect (accessed 2026-11-05)
