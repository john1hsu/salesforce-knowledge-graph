---
id: kt:mulesoft-anypoint-platform
type: Product
title: MuleSoft Anypoint Platform
aliases: [Anypoint Platform, MuleSoft Anypoint, Anypoint]
domain: integration
summary: >-
  MuleSoft's platform for designing, building, deploying and managing APIs and integrations, made up of a control
  plane (Design Center, Exchange, API Manager, Runtime Manager) and a runtime plane in which the Mule runtime engine
  executes integration applications on MuleSoft-hosted or customer-managed infrastructure.
release: "Winter '27"
status: current
broader: [kt:data-integration]
related: [kt:event-driven-architecture, kt:rest-api, kt:salesforce-connect, kt:change-data-capture, kt:flow-orchestrator, kt:mulesoft-platform-architect-certification]
relations:
  - {predicate: implements, object: kt:api-led-connectivity}
  - {predicate: integratesWith, object: kt:salesforce-platform}
  - {predicate: hasPart, object: kt:mule-runtime-engine}
  - {predicate: coveredBy, object: kt:integration-architect-certification}
sources:
  - id: s1
    title: "Anypoint Platform Glossary"
    publisher: MuleSoft (Salesforce)
    url: https://docs.mulesoft.com/general/glossary
    type: official-docs
    accessed: 2026-11-04
  - id: s2
    title: "Mule Runtime Engine Overview"
    publisher: MuleSoft (Salesforce)
    url: https://docs.mulesoft.com/mule-runtime/latest/
    type: official-docs
    accessed: 2026-11-04
  - id: s3
    title: "Explore API-Led Connectivity (Application Networks and API-Led Connectivity in MuleSoft)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/application-networks-and-api-led-connectivity-in-mulesoft/explore-api-led-connectivity
    type: official-learning
    accessed: 2026-11-04
  - id: s4
    title: "Get Started with Integration Decision Guides"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/decision-guides/guide/get-started-integration-decision-guides.html
    type: official-docs
    accessed: 2026-11-04
  - id: s5
    title: "Application Networks and API-Led Connectivity in MuleSoft"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/application-networks-and-api-led-connectivity-in-mulesoft
    type: official-learning
    accessed: 2026-11-04
created: 2026-11-04
---

# MuleSoft Anypoint Platform

MuleSoft Anypoint Platform is MuleSoft's product for designing, building and managing APIs and integrations.[^s1] In the Salesforce ecosystem it is the enterprise integration layer that sits outside any single org: where native features such as Change Data Capture or Salesforce Connect move or expose data for one org, Anypoint is used to connect Salesforce with ERPs, databases, legacy systems and other Salesforce orgs through reusable, governed APIs.[^s4][^s3]

## How it works

The platform is split into a **control plane** and a **runtime plane**. MuleSoft's glossary places Design Center, Management Center and Exchange in the control plane, and the Mule runtime engine plus the runtime services that tools such as Runtime Fabric manage in the runtime plane.[^s1] The main control-plane components are:

- **Design Center** — a cloud-based environment for building Mule applications and API definitions.[^s1]
- **Anypoint Exchange** — a curated catalog of reusable assets such as APIs, policies, templates and connectors; many connectors, including one for Salesforce, are published there.[^s1]
- **API Manager** — the component that manages, governs and secures APIs.[^s1]
- **Runtime Manager** — the console for deploying and managing Mule applications in the cloud or on premises.[^s1]

Developers build integrations in Anypoint Studio, an IDE with visual and XML editors where connectors and components are dragged onto a canvas, and transform data with DataWeave, MuleSoft's query and transformation language.[^s1] The resulting Mule applications, along with shared domains and API policies, are written in an XML-based domain-specific language and executed by the Mule runtime engine, whose documentation lists Mule 4.13 as the latest version at the time of writing.[^s2]

## Deployment options

Mule runtimes can run in several places, which is a key architecture decision:

- **CloudHub 2.0** — a managed, containerized iPaaS that MuleSoft operates across 12 global regions.[^s2]
- **CloudHub 1.0** — the earlier MuleSoft-managed cloud with built-in high availability and load balancing.[^s2]
- **Runtime Fabric** — a container service the customer runs in its own data center or in AWS or Azure; it is not supported on MuleSoft Government Cloud or Anypoint Platform PCE.[^s2]
- **Hybrid standalone runtimes** — Mule on customer servers, VMs or third-party clouds, still managed centrally from the control plane.[^s2]
- **Standalone runtimes** — isolated runtimes with no control-plane connection, where the customer owns high availability, failover and load balancing.[^s2]

Domains (shared configurations) can only be deployed on premises, which matters if a design relies on sharing connector configuration across apps.[^s2]

## API-led connectivity

Anypoint is the vehicle for MuleSoft's API-led connectivity approach, which arranges APIs into three layers. **System APIs** unlock data in core systems such as CRMs, ERPs and databases while shielding them from disruption; **Process APIs** combine and transform data from System APIs to carry business logic; and **Experience APIs** shape that data for a particular consumer such as a mobile app or dashboard.[^s3] The intended payoffs are reuse of existing APIs, faster delivery, developer self-service and central security and monitoring, building toward what MuleSoft calls an application network.[^s3][^s5]

## When to use it (and when not)

Salesforce's architect guidance lists Anypoint among the options for outbound integrations from Salesforce and for cross-org data sharing, alongside native choices such as Change Data Capture, External Services, Heroku Connect, native APIs and Salesforce Connect's cross-org adapter.[^s4] The same guidance frames the choice around the existing tool landscape (including established ESB or ETL tooling), timing and direction of data flow, complexity, maintainability, data volume and platform limits.[^s4]

In practice, Anypoint earns its cost when many systems must be connected, when the same data is consumed by several channels, or when orchestration and transformation logic should live outside Salesforce rather than in Apex or Flow. For a single point-to-point sync or read-only access to external data, a native feature is usually simpler. Because Mule apps still call Salesforce through its APIs, they remain subject to the org's API request allocations.[^s4]

## Connections

Anypoint sits under `kt:data-integration` as one of the principal tools in Salesforce's integration landscape, and the architect guidance positions it next to native options such as `kt:change-data-capture` and `kt:salesforce-connect`, which cover some outbound and cross-org cases without middleware.[^s4] It implements `kt:api-led-connectivity`, the three-layer System/Process/Experience model, and has `kt:mule-runtime-engine` as the part that actually executes integration code.[^s3][^s2] It integrates with `kt:salesforce-platform` through Salesforce connectors published in Exchange, which call platform APIs such as `kt:rest-api`.[^s1] Anypoint integrations often serve `kt:event-driven-architecture` designs and long-running processes coordinated by `kt:flow-orchestrator`, and choosing between middleware and native tools is examined in the `kt:integration-architect-certification`.[^s4][^s5]

## Sources
[^s1]: MuleSoft, "Anypoint Platform Glossary". https://docs.mulesoft.com/general/glossary (accessed 2026-11-04)
[^s2]: MuleSoft, "Mule Runtime Engine Overview". https://docs.mulesoft.com/mule-runtime/latest/ (accessed 2026-11-04)
[^s3]: Trailhead, "Explore API-Led Connectivity". https://trailhead.salesforce.com/content/learn/modules/application-networks-and-api-led-connectivity-in-mulesoft/explore-api-led-connectivity (accessed 2026-11-04)
[^s4]: Salesforce Architects, "Get Started with Integration Decision Guides". https://architect.salesforce.com/docs/architect/decision-guides/guide/get-started-integration-decision-guides.html (accessed 2026-11-04)
[^s5]: Trailhead, "Application Networks and API-Led Connectivity in MuleSoft". https://trailhead.salesforce.com/content/learn/modules/application-networks-and-api-led-connectivity-in-mulesoft (accessed 2026-11-04)
