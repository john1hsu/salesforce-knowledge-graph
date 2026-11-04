---
id: kt:data-integration
type: Concept
title: Data Integration
aliases: [Salesforce data integration, data-level integration]
domain: integration
summary: >-
  The integration category concerned with moving and synchronising the information applications use, between
  Salesforce and external systems or between Salesforce orgs, as distinct from process integration (shared
  business flows) and virtual integration (accessing external data in place without copying it).
release: "Winter '27"
status: concept
broader: [kt:data-architecture]
related: [kt:rest-api, kt:bulk-api-2, kt:change-data-capture, kt:external-id-fields, kt:external-objects, kt:event-driven-architecture]
relations:
  - {predicate: contrastsWith, object: kt:process-integration}
  - {predicate: alternativeTo, object: kt:salesforce-connect}
  - {predicate: hasPart, object: kt:batch-data-synchronization}
  - {predicate: integratesWith, object: kt:mulesoft-anypoint-platform}
  - {predicate: governedBy, object: kt:api-request-limits}
  - {predicate: coveredBy, object: kt:integration-architect-certification}
sources:
  - id: s1
    title: "Data Integration with Salesforce (Architect Decision Guide)"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/decision-guides/guide/data-integration
    type: official-docs
    accessed: 2026-11-04
  - id: s2
    title: "Pattern Selection Guide (Integration Patterns and Practices)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.integration_patterns_and_practices.meta/integ/integ_pat_selection_guide.htm
    type: official-docs
    accessed: 2026-11-04
  - id: s3
    title: "Integration Patterns Overview"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/integration-patterns
    type: official-docs
    accessed: 2026-11-04
  - id: s4
    title: "Pattern Summary (Integration Patterns and Practices)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.integration_patterns_and_practices.meta/integ/integ_pat_pat_summary.htm
    type: official-docs
    accessed: 2026-11-04
  - id: s5
    title: "Get Started with Integration Decision Guides"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/decision-guides/guide/get-started-integration-decision-guides.html
    type: official-docs
    accessed: 2026-11-04
created: 2026-11-04
---

# Data Integration

Data integration is the part of integration design that keeps the information used by applications consistent across systems. Salesforce's integration patterns guide defines it as integrating the information applications use, and notes that it ranges from a simple insert or upsert to complex updates that need referential integrity and data translation.[^s2] The Architects overview calls it often the simplest integration type, but stresses that it still needs information management disciplines such as master data management, data governance and de-duplication.[^s3]

## How it differs from process and virtual integration

Salesforce classifies integrations along two axes, type and timing.[^s2] Alongside data integration, **process integration** connects the functional flow of a business process across two or more applications and carries harder problems such as long-running transactions and rollback, while **virtual integration** lets users view, search and modify external data in real time without replicating it into Salesforce.[^s2][^s3] Timing is either synchronous (blocking request/response, result returned immediately) or asynchronous (non-blocking, queue- or message-based, one-way).[^s2]

Mapping data integration onto the pattern catalogue gives four patterns. Outbound from Salesforce, the synchronous case is Remote Process Invocation—Request and Reply and the asynchronous case is UI Update Based on Data Changes; inbound to Salesforce, the synchronous case is Remote Call-In and the asynchronous case is Batch Data Synchronization.[^s2] Batch Data Synchronization covers bulk refreshes in either direction, and Remote Call-In covers an external system creating, reading, updating or deleting Salesforce records.[^s4]

## Tools and directions

The Architects decision guide scopes data-level integration in three directions: Salesforce to external systems, external systems to Salesforce, and org to org.[^s1] It also helps teams avoid needless replication and reuse existing ESB and ETL investments.[^s5] Its tool landscape includes the native REST, SOAP, Bulk, GraphQL and gRPC APIs; Change Data Capture and Platform Events; Outbound Messaging; External Services, Apex actions and custom Apex web services; Heroku Connect; OmniStudio Integration Procedures; Salesforce Connect and external objects; Data 360; and MuleSoft Anypoint.[^s1] Data Loader, the Data Import Wizard, Flow and the Salesforce CLI are classed as supporting tools for data stewardship rather than integration platforms.[^s1]

For inbound work the guide frames a key choice between **replication** (copying data into Salesforce or Data 360, for example with Heroku Connect, Platform Events, MuleSoft or the native APIs) and **virtualization** (leaving data in the source and surfacing it through Salesforce Connect, or zero-copy access in Data 360 for some platforms).[^s1] For cross-org integration it notes that Salesforce-to-Salesforce has reached end of life and points to Heroku Connect, MuleSoft, the native APIs, Change Data Capture, the Salesforce Connect cross-org adapter or Data 360 instead, while advising against Platform Events and custom Apex for that purpose.[^s1]

## Design guidance and gotchas

- **Name the source of truth and minimise copies.** The guide asks architects to settle which system owns each record before choosing a pattern, and to prefer Salesforce Connect or the APIs over replicating data that does not need to live in the org.[^s1]
- **Reuse the existing landscape.** If an ESB or ETL tool already exists, use it; otherwise consider MuleSoft for governance and reuse.[^s1] The overview adds that Salesforce cannot join distributed transactions or convert protocols natively, so multi-system rollback and translation belong in middleware or at the endpoint.[^s3]
- **Respect platform limits and volume.** Native APIs consume API request limits and allocations, Bulk API 2.0 suits extracts of thousands of records, and high-volume Change Data Capture and Platform Events need add-on licences.[^s1] The decision framework also weighs timing, directionality, coupling, exception handling, data volume and bulk initial loads.[^s1]
- **Authenticate deliberately.** The guide recommends an API Only integration user and External Client Applications rather than connected apps or SOAP login.[^s1]
- **Treat legacy channels with care.** Outbound Messaging is supported but not receiving further investment, and queued messages are dropped after 24 hours.[^s1]

## Connections

Data integration sits under `kt:data-architecture`, which decides where data lives before integration decides how it moves.[^s1] It contrasts with `kt:process-integration`, and its virtual counterpart is `kt:salesforce-connect`, the alternative when data need not be copied.[^s2][^s1] It has `kt:batch-data-synchronization` as a core pattern, is carried by `kt:rest-api` and `kt:bulk-api-2` and made idempotent by `kt:external-id-fields`, while `kt:change-data-capture` and `kt:event-driven-architecture` provide its asynchronous outbound path.[^s1][^s2] `kt:external-objects` implement the virtualization branch, `kt:mulesoft-anypoint-platform` is the recommended middleware when none exists, throughput is governed by `kt:api-request-limits`, and the topic is covered by the `kt:integration-architect-certification`.[^s1][^s3]

## Sources
[^s1]: Salesforce Architects, "Data Integration with Salesforce". https://architect.salesforce.com/docs/architect/decision-guides/guide/data-integration (accessed 2026-11-04)
[^s2]: Salesforce Developers, "Pattern Selection Guide". https://developer.salesforce.com/docs/atlas.en-us.integration_patterns_and_practices.meta/integ/integ_pat_selection_guide.htm (accessed 2026-11-04)
[^s3]: Salesforce Architects, "Integration Patterns Overview". https://architect.salesforce.com/fundamentals/integration-patterns (accessed 2026-11-04)
[^s4]: Salesforce Developers, "Pattern Summary". https://developer.salesforce.com/docs/atlas.en-us.integration_patterns_and_practices.meta/integ/integ_pat_pat_summary.htm (accessed 2026-11-04)
[^s5]: Salesforce Architects, "Get Started with Integration Decision Guides". https://architect.salesforce.com/docs/architect/decision-guides/guide/get-started-integration-decision-guides.html (accessed 2026-11-04)
