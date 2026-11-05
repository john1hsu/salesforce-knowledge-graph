---
id: kt:batch-data-synchronization
type: Pattern
title: Batch Data Synchronization
aliases: [batch data sync pattern, batch synchronization integration pattern, ETL batch sync]
domain: integration
summary: >-
  The asynchronous Salesforce integration pattern in which records are created or refreshed in bulk to mirror an external
  system, and Salesforce changes are sent back out, typically by ETL tooling or Change Data Capture within a batch window.
release: "Winter '27"
status: concept
broader: [kt:integration-patterns, kt:data-integration]
related: [kt:large-data-volumes, kt:record-locking, kt:data-migration-strategy, kt:external-id-fields]
relations:
  - {predicate: partOf, object: kt:integration-patterns}
  - {predicate: dependsOn, object: kt:bulk-api-2}
  - {predicate: dependsOn, object: kt:change-data-capture}
  - {predicate: contrastsWith, object: kt:salesforce-connect}
  - {predicate: alternativeTo, object: kt:remote-call-in}
  - {predicate: coveredBy, object: kt:integration-architect-certification}
sources:
  - id: s1
    title: "Integration Patterns Overview"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/integration-patterns
    type: official-docs
    accessed: 2026-11-05
  - id: s2
    title: "Pattern Summary (Integration Patterns and Practices)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.integration_patterns_and_practices.meta/integ/integ_pat_pat_summary.htm
    type: official-docs
    accessed: 2026-11-05
  - id: s3
    title: "Subscribing to Change Events (Change Data Capture Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_subscribe.htm
    type: official-docs
    accessed: 2026-11-05
  - id: s4
    title: "Bulk API and Bulk API 2.0 Limits and Allocations"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-app-limits-cheatsheet/guide/salesforce-app-limits-platform-bulkapi.html
    type: official-docs
    accessed: 2026-11-05
created: 2026-11-05
---

# Batch Data Synchronization

Batch Data Synchronization is one of the six patterns in Salesforce's integration catalogue. Records in Salesforce are created or refreshed to reflect changes in an external system, Salesforce changes flow back to that system, and updates in either direction move in batches rather than one transaction at a time.[^s2] Salesforce's architecture guidance classifies it as asynchronous data integration, which sets it apart from Remote Call-In, the synchronous way for another system to change Salesforce data.[^s1]

## The problem it solves

The pattern addresses a recurring question: how to import and export large volumes of data without disrupting users during business hours. The canonical scenarios are an initial load from a legacy CRM, a recurring load of billing data from a back-office system, and a periodic export of customer activity to a data warehouse.[^s1] Before choosing it, Salesforce asks architects to weigh whether the data needs to live in Salesforce at all, whether refreshes are event-driven or scheduled, and whether core business processes, reporting or analytics depend on the copy.[^s1] If the answer to the first question is no, a virtual approach that leaves the data in place may fit better.[^s1]

## Solution options

The current architect guidance rates the options by which system is the data master:[^s1]

- **Third-party ETL with change capture on the source** (remote system as master): rated best. The tool detects source changes, transforms them and writes to Salesforce through Bulk API, with REST suitable for smaller volumes.[^s1]
- **Third-party ETL querying Salesforce** (Salesforce as master): rated good. Changed rows are found with time or status fields and extracted through Bulk API 2.0 or REST.[^s1]
- **Data 360 actions, activations and Connect APIs via MuleSoft**: rated best for moving data between orgs or into Marketing Cloud.[^s1]
- **Composite Graph API**: rated best when Salesforce is master; the guidance gives limits of 75 graphs per payload and 500 nodes per graph.[^s1]
- **Data Import Wizard and Data Loader**: suited to data stewardship, not as the basis of an integration.[^s1]
- **Remote Call-In and Remote Process Invocation**: rated suboptimal, because pushing every change as it happens creates continuous traffic, locking risk and performance impact on users.[^s1]

When Salesforce is the source, Change Data Capture publishes change events that an external client consumes. Pub/Sub API serves external subscribers over gRPC and HTTP/2, while Apex triggers are the on-platform option. Events are kept for a retention window during which subscribers can retrieve them.[^s3] The architect guidance gives that window as 72 hours and recommends resuming from the last processed event with replay IDs.[^s1]

## How a typical ETL job runs

A well-behaved job reads a control table for its last run time, uses it to filter the source query, validates and enriches the rows, transforms them, and writes them to Salesforce objects. On success it updates the control values; on failure it records restart information and exits. Control tables should live where the ETL tool can still reach them when Salesforce is unavailable, so the ETL infrastructure acts as the hub and Salesforce as a spoke.[^s1] Recommended practices include chaining and sequencing jobs, matching records on keys from both systems, extracting only changed data, grouping child records by parent key to avoid locking, and keeping post-load trigger logic selective.[^s1]

## Limits and gotchas

- **Batch windows.** Timeliness matters less than in request-reply patterns, but jobs must finish within their window. Loading during business hours causes contention that can fail either user edits or the batch. Global orgs can segment data by record type or filter when no single window fits.[^s1]
- **Bulk API 2.0 behaviour.** It processes batches in parallel without a serial mode, so ordering is not guaranteed and each batch commits independently; parallelism can also raise lock contention.[^s1]
- **Throughput caps.** Bulk API 2.0 allows 150,000,000 ingested records per rolling 24 hours and 150 MB of base64-encoded data per job upload, and an ingest job can stay open for at most 24 hours.[^s4]
- **Error handling.** CDC hand-offs cannot be rolled back, so the subscriber owns retries. For writes, use the per-record IDs, statuses and errors that the API returns to drive retries, and consider a delayed restart so bad data can be triaged.[^s1]
- **Security.** The integration user needs a Lightning Platform license with at least API-only permissions, stored credentials must be encrypted, and every call must use HTTPS.[^s1]

## Middleware

ETL tooling such as Informatica or MuleSoft is the core technology and must support Bulk API. Mandatory capabilities include transformation, queuing and buffering, process choreography and ETL. Long polling is required for CDC, and gRPC support is required for Pub/Sub API.[^s1]

## Connections

The pattern is part of `kt:integration-patterns` and is the asynchronous inbound case of `kt:data-integration`.[^s2][^s1] It depends on `kt:bulk-api-2` for volume and on `kt:change-data-capture` when Salesforce is master, whose external subscribers use `kt:pub-sub-api`.[^s3][^s4] It contrasts with `kt:salesforce-connect` and Data Virtualization, which read external data in real time without persisting it, and is the batch alternative to `kt:remote-call-in`.[^s1] Its locking and volume concerns tie it to `kt:record-locking` and `kt:large-data-volumes`. Its matching on keys from both systems relies on `kt:external-id-fields`, and an initial load is usually planned under `kt:data-migration-strategy`.[^s1] The edge to `kt:integration-architect-certification` reflects that the six patterns form that credential's shared design vocabulary.

## Sources
[^s1]: Salesforce Architects, "Integration Patterns Overview". https://architect.salesforce.com/fundamentals/integration-patterns (accessed 2026-11-05)
[^s2]: Salesforce Developers, "Pattern Summary (Integration Patterns and Practices)". https://developer.salesforce.com/docs/atlas.en-us.integration_patterns_and_practices.meta/integ/integ_pat_pat_summary.htm (accessed 2026-11-05)
[^s3]: Salesforce Developers, "Subscribing to Change Events". https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_subscribe.htm (accessed 2026-11-05)
[^s4]: Salesforce Developers, "Bulk API and Bulk API 2.0 Limits and Allocations". https://developer.salesforce.com/docs/platform/salesforce-app-limits-cheatsheet/guide/salesforce-app-limits-platform-bulkapi.html (accessed 2026-11-05)
