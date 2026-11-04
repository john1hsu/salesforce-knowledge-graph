---
id: kt:integration-patterns
type: Concept
title: Integration Patterns
aliases: [Salesforce integration patterns, Integration Patterns and Practices, integration pattern catalogue]
domain: integration
summary: >-
  Salesforce's published catalogue of reusable integration designs (Request and Reply, Fire and Forget, Batch Data
  Synchronization, Remote Call-In, UI Update Based on Data Changes and Data Virtualization), each documented with a
  standard template and fit-rated solution options, used by architects to choose how Salesforce connects to other systems.
release: "Winter '27"
status: concept
broader: [kt:salesforce-architecture-center]
related: [kt:data-integration, kt:event-driven-architecture, kt:composite-api, kt:pub-sub-api, kt:apex-callouts]
relations:
  - {predicate: hasPart, object: kt:integration-patterns-request-reply-fire-and-forget}
  - {predicate: hasPart, object: kt:batch-data-synchronization}
  - {predicate: hasPart, object: kt:remote-call-in}
  - {predicate: hasPart, object: kt:data-virtualization}
  - {predicate: integratesWith, object: kt:mulesoft-anypoint-platform}
  - {predicate: coveredBy, object: kt:integration-architect-certification}
sources:
  - id: s1
    title: "Integration Patterns Overview"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/integration-patterns
    type: official-docs
    accessed: 2026-11-04
  - id: s2
    title: "Pattern Summary (Integration Patterns and Practices)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.integration_patterns_and_practices.meta/integ/integ_pat_pat_summary.htm
    type: official-docs
    accessed: 2026-11-04
  - id: s3
    title: "Purpose and Scope (Integration Patterns and Practices)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.integration_patterns_and_practices.meta/integ/integ_pat_purpose_scope.htm
    type: official-docs
    accessed: 2026-11-04
  - id: s4
    title: "Learn About Integration Patterns and Designs (Application Integration Patterns for Salesforce Lightning Platform)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/zh-CN/content/learn/modules/app-integration-patterns/app-integration-patterns-1
    type: official-learning
    accessed: 2026-11-04
created: 2026-11-04
---

# Integration Patterns

Salesforce's integration patterns are a catalogue of reusable design strategies for the recurring situations in which Salesforce must exchange data or trigger work with other applications. They describe approaches rather than code, and are aimed at architects and designers.[^s1] Salesforce says the guidance distils many successful implementations by its own architects and partners, and that its consulting architects use the patterns as reference points during architecture reviews.[^s3] Trailhead frames them the same way: a tested starting point for weighing options, not an implementation guide, with each pattern recommending specific connectors or services.[^s4]

## The catalogue

The Integration Patterns and Practices guide contains six patterns:[^s2][^s1]

- **Remote Process Invocation—Request and Reply**: Salesforce calls a remote process, waits for it to complete and tracks state from the response.[^s2]
- **Remote Process Invocation—Fire and Forget**: Salesforce starts a remote process and continues once the remote system acknowledges receipt.[^s2]
- **Batch Data Synchronization**: data is refreshed in batches in either direction between Salesforce and an external system.[^s2]
- **Remote Call-In**: an external system creates, reads, updates or deletes Salesforce data.[^s2]
- **UI Update Based on Data Changes**: the Salesforce user interface refreshes automatically when underlying data changes.[^s2]
- **Data Virtualization**: Salesforce reads external data in real time instead of storing and reconciling a copy.[^s2]

The Trailhead module groups a slightly different set of seven, adding High-Frequency Data Replication and Publish/Subscribe alongside the core patterns, and scopes itself to Lightning Platform integration, excluding Heroku, MuleSoft and UI mashups.[^s4] The guide likewise says the patterns cover most but not all scenarios and puts UI integration such as mashups out of scope.[^s3]

## How patterns are organised and chosen

Each pattern follows a fixed template: name, context, problem, forces, solution, a UML sequence sketch, results, sidebars and an example.[^s1] Patterns are classified by integration type (data, process or virtual) and by timing, where synchronous calls block until a response arrives and asynchronous calls are one-way and non-blocking; a selection matrix maps direction and timing to the recommended pattern.[^s1] Salesforce advises anyone planning large-scale adoption to read the pattern summary and selection matrix first.[^s3]

Within a pattern, candidate solutions are rated for fit. For Request and Reply, External Services calling a REST API and Lightning components calling Apex (with asynchronous continuation for slow endpoints) are rated best, while Batch Apex making synchronous callouts is suboptimal.[^s1] For Fire and Forget, Flow-driven platform events, the Pub/Sub API and Change Data Capture are rated best, and outbound messaging or trigger-driven asynchronous callouts are suboptimal.[^s1] For Remote Call-In, the Composite, REST, Bulk API 2.0, GraphQL and Pub/Sub APIs are rated best, and SOAP API and custom Apex web services suboptimal.[^s1]

## Cross-cutting considerations and gotchas

- **Put complexity in middleware.** Complex orchestration, transformation and multi-system transactions belong in a middleware layer; Salesforce is transactional internally but cannot join distributed transactions, so rollback and compensation live outside it.[^s1]
- **Manage state and idempotency.** Systems correlate records by storing either the remote key in Salesforce or the Salesforce ID remotely; receivers should de-duplicate on unique message IDs and prefer upserts, because event replay can redeliver messages.[^s1]
- **Respect timeouts and volume.** Apex callouts can wait up to 120 seconds, and the guide suggests short external timeouts to avoid exhausting the limit on long-running transactions; Bulk API 2.0 is recommended above 2,000 records, and a Composite API call bundles up to 25 subrequests.[^s1]
- **Plan for delivery guarantees.** Apex callouts have no native reliable messaging, so retries must be built; high-volume platform event messages are retained for 72 hours.[^s1]
- **Secure the channel.** Recommended controls include TLS, Named Credentials and OAuth 2.0, and Trailhead points to Shield Platform Encryption for outbound patterns.[^s1][^s4]

## Connections

The catalogue is published through `kt:salesforce-architecture-center`.[^s1] It has `kt:integration-patterns-request-reply-fire-and-forget`, `kt:batch-data-synchronization`, `kt:remote-call-in` and `kt:data-virtualization` as parts; `kt:data-integration` is one of its three integration types, and `kt:event-driven-architecture` underlies its asynchronous options.[^s2][^s1] Solutions it rates highly include `kt:composite-api`, `kt:pub-sub-api` and `kt:apex-callouts`, and it recommends middleware such as `kt:mulesoft-anypoint-platform` for orchestration.[^s1] The edge to `kt:integration-architect-certification` reflects that the patterns are the shared vocabulary Salesforce architects use as reference points in architecture reviews.[^s3]

## Sources
[^s1]: Salesforce Architects, "Integration Patterns Overview". https://architect.salesforce.com/fundamentals/integration-patterns (accessed 2026-11-04)
[^s2]: Salesforce Developers, "Pattern Summary". https://developer.salesforce.com/docs/atlas.en-us.integration_patterns_and_practices.meta/integ/integ_pat_pat_summary.htm (accessed 2026-11-04)
[^s3]: Salesforce Developers, "Purpose and Scope". https://developer.salesforce.com/docs/atlas.en-us.integration_patterns_and_practices.meta/integ/integ_pat_purpose_scope.htm (accessed 2026-11-04)
[^s4]: Trailhead, "Learn About Integration Patterns and Designs". https://trailhead.salesforce.com/zh-CN/content/learn/modules/app-integration-patterns/app-integration-patterns-1 (accessed 2026-11-04)
