---
id: kt:api-led-connectivity
type: Pattern
title: API-led Connectivity
aliases: [API-led integration, three-layer API architecture, System Process Experience APIs]
domain: integration
summary: >-
  MuleSoft's integration approach that connects data to applications through reusable, purpose-built APIs organized
  in three layers: System APIs that unlock systems of record, Process APIs that compose business logic, and
  Experience APIs that shape data for specific channels, replacing brittle point-to-point connections.
release: "Winter '27"
status: concept
broader: [kt:integration-patterns, kt:data-integration]
related: [kt:mulesoft-anypoint-platform, kt:salesforce-apis, kt:event-driven-architecture, kt:mulesoft-platform-architect-certification]
relations:
  - {predicate: contrastsWith, object: kt:point-to-point-integration}
  - {predicate: enables, object: kt:application-network}
sources:
  - id: s1
    title: "Explore API-Led Connectivity (Application Networks and API-Led Connectivity in MuleSoft)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/application-networks-and-api-led-connectivity-in-mulesoft/explore-api-led-connectivity
    type: official-learning
    accessed: 2026-11-13
  - id: s2
    title: "Discover Application Networks (Application Networks and API-Led Connectivity in MuleSoft)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/application-networks-and-api-led-connectivity-in-mulesoft/discover-application-networks
    type: official-learning
    accessed: 2026-11-13
  - id: s3
    title: "Explore the Application Network (MuleSoft Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/mulesoft-basics/app-network
    type: official-learning
    accessed: 2026-11-13
  - id: s4
    title: "What Is API-led Connectivity?"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/api-led-connectivity/?bc=OTH
    type: official-blog
    accessed: 2026-11-13
  - id: s5
    title: "Patterns to debunk API-led connectivity myths"
    publisher: MuleSoft (Salesforce)
    url: https://blogs.mulesoft.com/api-integration/patterns/patterns-to-debunk-api-led-connectivity-myths/
    type: official-blog
    accessed: 2026-11-13
  - id: s6
    title: "Get Started with Integration Decision Guides"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/decision-guides/guide/get-started-integration-decision-guides.html
    type: official-docs
    accessed: 2026-11-13
  - id: s7
    title: "Salesforce Certified MuleSoft Platform Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/credentials/mulesoftplatformarchitecti
    type: official-learning
    accessed: 2026-11-13
created: 2026-11-13
---

# API-led Connectivity

API-led connectivity is the integration approach MuleSoft (part of Salesforce) promotes for connecting data to applications through reusable, purposeful APIs rather than one-off connections between pairs of systems.[^s4] Instead of wiring each new application directly to each system it needs, teams expose capabilities as APIs that unlock data from systems, compose it into processes, or deliver it as experiences, so later projects can rewire existing building blocks instead of recreating them.[^s4][^s3] Trailhead frames it as organizing APIs into three distinct layers so that integrations become structured, reusable frameworks.[^s1]

## How it works: the three layers

**System APIs** sit at the foundation and connect directly to core systems such as databases, ERPs and CRMs. They unlock siloed data and insulate consumers from the complexity of, and changes to, those systems of record; a Salesforce System API, for example, can expose customer data to other applications without affecting the CRM itself.[^s1][^s3] The Salesforce blog describes them as the "nouns" of the business.[^s4]

**Process APIs** combine and reshape data from System APIs (and other Process APIs) into reusable business logic, handling transformation, aggregation and enrichment. They model business processes and break down technology silos, for example by merging Salesforce customer data with eCommerce orders into one reporting view.[^s1][^s3] In the blog's terms they are the "verbs", and they suit automation and bots.[^s4]

**Experience APIs** adapt Process API output for a specific user interface, device or channel, such as a mobile app showing real-time order status. They are designed for reuse and do not depend directly on the source systems, and they are often built by a different persona from the teams that own the lower layers.[^s1][^s3][^s4]

Together these layers form an application network: applications, data and devices connected through standardized, reusable APIs in a governed, scalable way, which Trailhead contrasts with rigid, costly point-to-point integrations that need constant maintenance and reinforce data silos.[^s2][^s3]

## Benefits

Trailhead attributes several properties to the approach: reuse of existing APIs to cut duplication, agility from modular building blocks, self-service discovery that reduces dependence on central IT, and security and governance because each API can be secured and monitored.[^s1] The MuleSoft Basics unit adds clear contracts, discoverability, visibility, and availability and resiliency.[^s3] Salesforce also argues the approach narrows the IT delivery gap and turns build-vs-buy into a "create vs. integrate" decision; its productivity figures are vendor-reported and should be treated as such.[^s4]

## Limits and gotchas

The three layers are a starting point, not a mandate. MuleSoft's own architects state that API-led connectivity "is not strictly restricted to three layers" and show valid designs that omit the Experience layer, or that use a single System API when there is no business logic to orchestrate.[^s5] Adding layers by reflex raises implementation, operations and maintenance costs, adds SLA overhead from extra hops, and can expose more data elements to consumers than they should receive.[^s5] Add an Experience API only when consumers need a different contract, or when the Process API definition is expected to change, and weigh performance, SLAs, security, topology and expected change for each use case.[^s5]

## When to use it (and when not)

API-led connectivity pays off when many consumers need the same systems of record and reuse can be realized; it is an architecture for an organization's integration estate, not a single feature. For Salesforce-centred work, the Architects' integration decision guides list MuleSoft Anypoint alongside native options such as Change Data Capture, Salesforce Connect and the platform APIs, and weigh existing middleware, data flow requirements, complexity, maintainability, volume and platform limits when choosing.[^s6] A simple one-way feed may be better served by a native tool than by a layered API stack.[^s6][^s5]

## Connections

API-led connectivity is one of the `kt:integration-patterns` and a strategy for `kt:data-integration`.[^s1][^s6] It is the model that `kt:mulesoft-anypoint-platform` is built to implement, with Salesforce typically reached through System APIs that wrap `kt:salesforce-apis`.[^s1][^s3] It deliberately contrasts with `kt:point-to-point-integration`, and its layered APIs are what make up an `kt:application-network`.[^s2][^s3] It complements `kt:event-driven-architecture`: the layering governs request-driven APIs, while events cover asynchronous change propagation, and both options appear in the integration decision guides.[^s6] Defining an organization's Anypoint Platform strategy, the remit validated by the `kt:mulesoft-platform-architect-certification`, is where this layered model is applied across the whole integration estate.[^s7][^s1]

## Sources

[^s1]: Trailhead, "Explore API-Led Connectivity". https://trailhead.salesforce.com/content/learn/modules/application-networks-and-api-led-connectivity-in-mulesoft/explore-api-led-connectivity (accessed 2026-11-13)
[^s2]: Trailhead, "Discover Application Networks". https://trailhead.salesforce.com/content/learn/modules/application-networks-and-api-led-connectivity-in-mulesoft/discover-application-networks (accessed 2026-11-13)
[^s3]: Trailhead, "Explore the Application Network" (MuleSoft Basics). https://trailhead.salesforce.com/content/learn/modules/mulesoft-basics/app-network (accessed 2026-11-13)
[^s4]: Salesforce, "What Is API-led Connectivity?". https://www.salesforce.com/blog/api-led-connectivity/?bc=OTH (accessed 2026-11-13)
[^s5]: MuleSoft Blog, "Patterns to debunk API-led connectivity myths". https://blogs.mulesoft.com/api-integration/patterns/patterns-to-debunk-api-led-connectivity-myths/ (accessed 2026-11-13)
[^s6]: Salesforce Architects, "Get Started with Integration Decision Guides". https://architect.salesforce.com/docs/architect/decision-guides/guide/get-started-integration-decision-guides.html (accessed 2026-11-13)
[^s7]: Trailhead, "Salesforce Certified MuleSoft Platform Architect". https://trailhead.salesforce.com/en/credentials/mulesoftplatformarchitecti (accessed 2026-11-13)
