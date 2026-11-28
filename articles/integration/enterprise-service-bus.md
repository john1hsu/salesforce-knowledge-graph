---
id: kt:enterprise-service-bus
type: Pattern
title: Enterprise Service Bus
aliases: [ESB, enterprise service bus architecture, integration bus, centralized integration middleware]
domain: integration
summary: >-
  An integration architecture in which applications connect to a shared, centralized bus (an integration runtime
  plus messaging) that transforms, routes and mediates messages between them, instead of wiring each system to
  every other. A core building block of service-oriented architecture, it decouples endpoints but concentrates
  integration logic, governance and failure risk in one layer.
release: "Winter '27"
status: concept
broader: [kt:integration-patterns, kt:service-oriented-architecture]
related: [kt:mulesoft-anypoint-platform, kt:mule-runtime-engine, kt:process-integration, kt:data-integration, kt:outbound-messaging]
relations:
  - {predicate: alternativeTo, object: kt:point-to-point-integration}
  - {predicate: contrastsWith, object: kt:api-led-connectivity}
  - {predicate: contrastsWith, object: kt:microservices-architecture}
sources:
  - id: s1
    title: "What is an ESB?"
    publisher: MuleSoft (Salesforce)
    url: https://www.mulesoft.com/resources/esb/what-esb
    type: official-blog
    accessed: 2026-11-28
  - id: s2
    title: "Enterprise Service Bus (ESB): Connecting Enterprise Systems at Scale"
    publisher: Salesforce
    url: https://www.salesforce.com/ap/blog/what-is-esb/
    type: official-blog
    accessed: 2026-11-28
  - id: s3
    title: "Middleware Terms and Definitions (Integration Patterns and Practices)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.integration_patterns_and_practices.meta/integ/integ_pat_middleware_definitions.htm
    type: official-docs
    accessed: 2026-11-28
  - id: s4
    title: "Integration Architecture for the Salesforce Platform"
    publisher: Salesforce Developers Blog (Greg Cook)
    url: https://developer.salesforce.com/blogs/developer-relations/2014/11/salesforce-integration-architecture
    type: official-blog
    accessed: 2026-11-28
  - id: s5
    title: "What Is an Enterprise Service Bus (ESB)?"
    publisher: IBM
    url: https://www.ibm.com/think/topics/esb
    type: partner
    accessed: 2026-11-28
  - id: s6
    title: "ESB vs. Microservices: What's the Difference?"
    publisher: IBM
    url: https://www.ibm.com/think/topics/esb-vs-microservices
    type: partner
    accessed: 2026-11-28
created: 2026-11-28
---

# Enterprise Service Bus

An enterprise service bus (ESB) is an architecture for enterprise application integration: a set of rules and principles under which applications plug into a shared, bus-like infrastructure rather than into each other.[^s1] IBM frames it as an architectural pattern in which one centralized software component carries out the integrations between applications.[^s5] MuleSoft stresses that an ESB is an architecture, not merely a product bought off the shelf, and that products implement it in different ways.[^s1] Salesforce's own explainer adds the practical payoff: because each system talks only to the bus, changing one application does not break the rest of the integrations.[^s2]

## How it works

A typical ESB uses a messaging server (for example JMS or AMQP) as the bus itself, and data moves across it in a canonical format, traditionally XML.[^s1] Adapters sit between each application and the bus, translating to and from the canonical model; they can also take on routing, transactions, security, monitoring and error handling. ESB runtimes are generally stateless.[^s1][^s2] IBM lists the jobs the central component performs: transforming data models, handling connectivity, routing messages, converting protocols and, potentially, composing several requests into one, with the results exposed as reusable service interfaces.[^s5]

MuleSoft groups these capabilities as orchestration, transformation, transportation across protocols such as HTTP, JMS and JDBC, mediation (several interfaces for versioning or legacy callers), and consistent non-functional handling such as security, monitoring and scalability.[^s1] Salesforce's explainer names protocol mediation, message transformation, content-based routing and centralized security as the core functions, and notes the bus can also connect on-premises systems to SaaS applications in hybrid estates.[^s2]

## History

The ESB grew out of the need to escape point-to-point integration, which MuleSoft describes as spaghetti code that does not scale.[^s1] IBM places it as an essential component of service-oriented architecture (SOA), which emerged in the late 1990s.[^s5] In theory a central bus delivered standardization, shared cost, one specialist integration team and reuse; in practice, IBM notes, changes could destabilize unrelated integrations, every update needed heavy regression testing, requests queued up behind the central team and high-availability costs rose, so the bus often delayed the productivity gains it promised.[^s5]

## Salesforce perspective

Salesforce's integration guidance leaves several middleware jobs to a layer outside the org. The Winter '27 Integration Patterns and Practices guide says Salesforce doesn't convert protocols natively, can't take part in distributed transactions, and recommends putting complex orchestrations in middleware because of timeouts and governor limits; it also discourages doing heavy transformation in Apex for maintenance and performance reasons.[^s3] Salesforce's only explicit queuing capability is outbound messaging, so durable buffering usually belongs in middleware as well.[^s3]

A 2014 Salesforce Developers blog on integration architecture describes the classic enterprise layout: outbound messages from Salesforce usually land on an ESB and a durable queue, the ESB handles transformation, mediation and orchestration, and it should also own real-time calls from on-premises systems into Salesforce instead of each application calling the org directly.[^s4] The same author warns against making Salesforce itself the integration hub, and against routing cloud-to-cloud traffic through an on-premises ESB when that adds cost and ties the cloud solution to legacy infrastructure.[^s4]

## When to use it (and when not)

IBM argues microservices won't simply replace ESBs: a centralized bus still suits large on-premises-to-SaaS integration estates and benefits from central governance and easier troubleshooting, but without fault tolerance it is a single point of failure.[^s6] Microservices, by contrast, are a cloud-native way to build applications from independently deployable services and fit streaming, IoT and fast-changing features, at the price of more distributed complexity.[^s6] Salesforce's explainer positions centralized middleware for heavy legacy, complex orchestration and strict governance, while API management, microservices and iPaaS suit external-facing, distributed or low-code needs.[^s2] IBM also describes "agile integration", which breaks the ESB into fine-grained, decentralized integration components.[^s5]

## Connections

An ESB is one of the **integration patterns** and a building block of **service-oriented architecture**.[^s5] It is the classic **alternative to point-to-point integration**, replacing a mesh of direct links with one hub.[^s1] It **contrasts with API-led connectivity** and **microservices architecture**, which decentralize integration logic into reusable APIs or independent services.[^s2][^s6] MuleSoft's **Mule runtime engine** on the **MuleSoft Anypoint Platform** is Salesforce's own implementation of the idea.[^s2] Within Salesforce design work, the ESB is the usual home for the orchestration and transactionality concerns of **process integration**, the movement concerns of **data integration**, and the durable queuing that **outbound messaging** only partly provides.[^s3][^s4]

## Sources

[^s1]: MuleSoft, "What is an ESB?". https://www.mulesoft.com/resources/esb/what-esb (accessed 2026-11-28)
[^s2]: Salesforce, "Enterprise Service Bus (ESB): Connecting Enterprise Systems at Scale". https://www.salesforce.com/ap/blog/what-is-esb/ (accessed 2026-11-28)
[^s3]: Salesforce Developers, "Middleware Terms and Definitions" (Integration Patterns and Practices, Winter '27). https://developer.salesforce.com/docs/atlas.en-us.integration_patterns_and_practices.meta/integ/integ_pat_middleware_definitions.htm (accessed 2026-11-28)
[^s4]: Salesforce Developers Blog (Greg Cook), "Integration Architecture for the Salesforce Platform" (2014). https://developer.salesforce.com/blogs/developer-relations/2014/11/salesforce-integration-architecture (accessed 2026-11-28)
[^s5]: IBM, "What Is an Enterprise Service Bus (ESB)?". https://www.ibm.com/think/topics/esb (accessed 2026-11-28)
[^s6]: IBM, "ESB vs. Microservices: What's the Difference?". https://www.ibm.com/think/topics/esb-vs-microservices (accessed 2026-11-28)
