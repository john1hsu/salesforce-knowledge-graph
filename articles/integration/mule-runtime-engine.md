---
id: kt:mule-runtime-engine
type: Product
title: Mule Runtime Engine
aliases: [Mule runtime, Mule 4 runtime, Mule ESB, Mule server]
domain: integration
summary: >-
  The lightweight integration engine at the heart of MuleSoft Anypoint Platform that executes Mule applications,
  shared domains and API policies, using a reactive, non-blocking execution model and deployable to CloudHub 2.0,
  CloudHub 1.0, Runtime Fabric or customer-managed servers.
release: "Winter '27"
status: current
broader: [kt:mulesoft-anypoint-platform]
related: [kt:api-led-connectivity, kt:integration-patterns, kt:event-driven-architecture, kt:data-integration, kt:mulesoft-platform-architect-certification]
relations:
  - {predicate: partOf, object: kt:mulesoft-anypoint-platform}
  - {predicate: integratesWith, object: kt:salesforce-platform}
  - {predicate: configuredVia, object: kt:anypoint-runtime-manager}
sources:
  - id: s1
    title: "Mule Runtime Engine Overview"
    publisher: MuleSoft (Salesforce)
    url: https://docs.mulesoft.com/mule-runtime/latest/
    type: official-docs
    accessed: 2026-11-18
  - id: s2
    title: "Edge and LTS Releases for Mule"
    publisher: MuleSoft (Salesforce)
    url: https://docs.mulesoft.com/release-notes/mule-runtime/lts-edge-release-cadence
    type: official-docs
    accessed: 2026-11-18
  - id: s3
    title: "Mule Runtime Execution Engine"
    publisher: MuleSoft (Salesforce)
    url: https://docs.mulesoft.com/mule-runtime/latest/execution-engine
    type: official-docs
    accessed: 2026-11-18
  - id: s4
    title: "Get to Know Anypoint Platform (Understanding Anypoint Platform for Integration Success)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/fr/content/learn/modules/anypoint-platform-basics/get-to-know-anypoint-platform
    type: official-learning
    accessed: 2026-11-18
created: 2026-11-18
---

# Mule Runtime Engine

Mule runtime engine (usually just "Mule") is MuleSoft's lightweight integration engine: it runs Mule applications and also hosts shared domains and API policies, all of which are written in an XML-based domain-specific language.[^s1] Trailhead describes it as the application server behind every MuleSoft application, the piece that actually moves data securely between systems.[^s4] Where Anypoint Platform's control plane is where integrations are designed, catalogued and managed, Mule is the runtime plane that executes them.[^s1][^s4]

## What it runs

Mule hosts three kinds of artifact.[^s1]

- **Mule applications** connect systems, services, APIs and devices, handling routing, data mapping, orchestration and reliability.[^s1]
- **Domains** share global configuration (error handlers, properties, scheduler pools, connector configs) across apps.[^s1]
- **Policies** enforce security and traffic rules on HTTP-based APIs through Mule's embedded API gateway.[^s1]

Applications are built in MuleSoft's IDEs; Trailhead now points developers to Anypoint Code Builder for designing, building and testing integrations, and connectors to databases, web services and SaaS apps (including Salesforce) come prebuilt from Anypoint Exchange or can be custom-built.[^s4] Policies can be applied automatically from API Manager or developed as custom policies.[^s1]

## How it works

Mule 4 uses a reactive execution engine designed for non-blocking, asynchronous work. Each operation in a flow is treated as a task carrying metadata about its workload, and Mule uses that metadata to tune itself, so developers rarely manage threads directly.[^s3] Operations are classified as CPU-Light (quick work or non-blocking I/O such as an HTTP request), Blocking I/O (for example a database select) or CPU Intensive (for example a DataWeave transform); CPU-Light is the default when a component declares nothing.[^s3]

Since Mule 4.3, all applications on a Mule instance share a single self-sizing thread pool, the UBER pool, which Mule sizes at startup from the available cores and memory.[^s3] A legacy DEDICATED strategy with separate pools still exists, and an individual app can declare its own pools, but MuleSoft recommends keeping defaults and load testing before changing them.[^s3] Inside an active transaction, thread switching is suspended so all participating processors run on one thread.[^s3]

When every thread is busy or a flow exceeds its `maxConcurrency`, Mule applies **back-pressure**: it logs that the flow cannot accept new events and tells the source, which reacts in its own way; an HTTP listener may answer 503, while a broker listener may wait or drop the message.[^s3]

## Deployment options

The same runtime can run in several places, and the choice drives operations and compliance.[^s1]

- **CloudHub 2.0**: fully managed, containerized iPaaS across 12 regions, with shared or single tenancy.[^s1]
- **CloudHub 1.0**: MuleSoft-managed with built-in high availability, clustering, failover and load balancing.[^s1]
- **Runtime Fabric**: a Docker/Kubernetes-based service in your data center or AWS/Azure; not on Government Cloud or PCE.[^s1]
- **Hybrid standalone**: Mule on your own servers or VMs, still managed centrally from the cloud control plane.[^s1]
- **Standalone**: isolated runtimes without control-plane access, where you own HA, clustering and failover.[^s1]

Domains can only be deployed when Mule runs on premises, so designs that rely on sharing connector configuration across apps don't carry over to CloudHub.[^s1]

## Versions, limits and gotchas

Mule ships on two channels. **Edge** releases arrive up to three times a year with new features and short support windows; from 4.9 onward, an Edge version keeps Standard Support until one month after the next Edge ships, plus three months of Extended Support.[^s2] **LTS** releases come each February and receive at least 18 months of Standard Support and at least 6 months of Extended Support (4.6 and later).[^s2] Edge versions are not FedRAMP approved, which matters for public-sector workloads.[^s2]

As of this release, MuleSoft's documentation lists 4.13 as the latest version, released as an Edge version in October 2026 with Standard Support ending March 2027; 4.9 LTS is supported until August 2027 (Extended Support to February 2028).[^s1][^s2] Versions from 4.9 run on Java 17 only, while 4.6 LTS still supported Java 8, 11 and 17, so upgrades from older runtimes usually include a Java move.[^s2]

## When to use it (and when not)

Choose Mule-based integration when logic should live outside Salesforce: many systems to connect, transformations and orchestration reused across channels, or API policies to enforce centrally.[^s1][^s4] Pick the deployment target by operational model: CloudHub 2.0 when MuleSoft should run the infrastructure, Runtime Fabric or hybrid when data must stay in your network, and standalone only for disconnected environments.[^s1] Prefer an LTS version for long-lived production estates and Edge only when you need a new feature and can upgrade frequently.[^s2]

## Connections

Mule is `partOf` `kt:mulesoft-anypoint-platform`, its runtime plane, and is deployed and monitored through `kt:anypoint-runtime-manager`.[^s1][^s4] Mule applications are the building blocks of `kt:api-led-connectivity` and implement classic `kt:integration-patterns` and `kt:event-driven-architecture` designs within the broader `kt:data-integration` landscape.[^s1] It `integratesWith` the `kt:salesforce-platform` through prebuilt connectors published in Anypoint Exchange.[^s4] Runtime deployment choices are core material for architects working toward the `kt:mulesoft-platform-architect-certification`.[^s1]

## Sources
[^s1]: MuleSoft, "Mule Runtime Engine Overview". https://docs.mulesoft.com/mule-runtime/latest/ (accessed 2026-11-18)
[^s2]: MuleSoft, "Edge and LTS Releases for Mule". https://docs.mulesoft.com/release-notes/mule-runtime/lts-edge-release-cadence (accessed 2026-11-18)
[^s3]: MuleSoft, "Mule Runtime Execution Engine". https://docs.mulesoft.com/mule-runtime/latest/execution-engine (accessed 2026-11-18)
[^s4]: Trailhead, "Get to Know Anypoint Platform". https://trailhead.salesforce.com/fr/content/learn/modules/anypoint-platform-basics/get-to-know-anypoint-platform (accessed 2026-11-18)
