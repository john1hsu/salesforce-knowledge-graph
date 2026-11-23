---
id: kt:point-to-point-integration
type: Pattern
title: Point-to-Point Integration
aliases: [point to point integration, P2P integration, direct integration, spaghetti integration]
domain: integration
summary: >-
  An integration topology in which each system is wired directly to every system it exchanges data with through
  custom, purpose-built connections. Quick to build for two or three systems, it becomes tightly coupled, brittle
  and costly to maintain as the number of endpoints grows, which is why Salesforce guidance steers larger
  estates toward middleware, API-led connectivity or an event bus.
release: "Winter '27"
status: concept
broader: [kt:integration-patterns]
related: [kt:application-network, kt:mulesoft-anypoint-platform, kt:apex-callouts, kt:platform-events]
relations:
  - {predicate: contrastsWith, object: kt:api-led-connectivity}
  - {predicate: contrastsWith, object: kt:event-driven-architecture}
  - {predicate: alternativeTo, object: kt:enterprise-service-bus}
  - {predicate: causes, object: kt:technical-debt-in-salesforce}
sources:
  - id: s1
    title: "Explore the Application Network (MuleSoft Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/mulesoft-basics/app-network
    type: official-learning
    accessed: 2026-11-23
  - id: s2
    title: "Using the Right Tools and Patterns for Event-Driven Architectures (Platform Decision Guides)"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/decision-guides/event-driven
    type: official-docs
    accessed: 2026-11-23
  - id: s3
    title: "Event-Driven Software Architecture (Platform Events Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_intro_architecture.htm
    type: official-docs
    accessed: 2026-11-23
  - id: s4
    title: "Integration Architecture for the Salesforce Platform"
    publisher: Salesforce Developers Blog (Greg Cook)
    url: https://developer.salesforce.com/blogs/developer-relations/2014/11/salesforce-integration-architecture
    type: official-blog
    accessed: 2026-11-23
  - id: s5
    title: "Eliminating point to point integration pain with Mule ESB"
    publisher: MuleSoft (Salesforce)
    url: https://www.mulesoft.com/integration/point-to-point-integration
    type: official-blog
    accessed: 2026-11-23
  - id: s6
    title: "Enterprise Service Bus (ESB): Connecting Enterprise Systems at Scale"
    publisher: Salesforce
    url: https://www.salesforce.com/ap/blog/what-is-esb/
    type: official-blog
    accessed: 2026-11-23
created: 2026-11-23
---

# Point-to-Point Integration

Point-to-point integration connects each system directly to each other system it needs to talk to, usually with a
custom piece of code per connection.[^s1] Trailhead's MuleSoft Basics module uses it as the baseline that
API-led connectivity is designed to replace: the connections are tightly coupled, so even a small change in one
system can force a rewrite of the code on the other side, and over time the estate becomes hard to maintain and
slows the business down.[^s1] Salesforce's ESB explainer describes the end state as a tangled web of dependencies
that grows fragile, expensive and hard to manage as a company adds applications.[^s6]

## How it works

In a Salesforce org the typical building blocks are custom code, such as Apex calling out to another system,
with each link carrying its own logic for that one pair of systems.[^s1][^s4] The 2014 Salesforce Developers Blog guide to
integration architecture notes that the platform makes this style of integration easy to build, but warns that
the more Salesforce acts as the hub for these links, the more time a team spends building, maintaining and
troubleshooting them; it advises against making Apex the primary integration technology.[^s4]

The cost is structural. Because every pair of systems that exchanges data needs its own link, the number of
connections grows much faster than the number of systems. MuleSoft illustrates this with three systems needing
three connections, five needing ten, and ten or more needing at least 45, which is the n(n−1)/2 count of a fully
connected mesh.[^s5]

## Limits and gotchas

- **Tight coupling.** A change to one endpoint's schema, API version or security settings ripples into every system wired to it.[^s1][^s5]
- **Single points of failure.** MuleSoft cites failures that cascade because there is no central place to reroute or queue traffic, plus poor documentation of who calls what.[^s5]
- **One-to-many fan-out.** The event-driven decision guide calls custom connections to every dependent system burdensome, a source of technical debt, and a limit on scaling.[^s2]
- **Scattered cross-cutting concerns.** Logging, monitoring, transformation and credential management are re-implemented per link rather than handled once in middleware.[^s4][^s6]

## When to use it (and when not)

Point-to-point is a reasonable choice when only a handful of systems are involved and no growth is expected:
MuleSoft's own guidance treats three or fewer systems as the range where it stays manageable.[^s5] It is also the
natural shape of a synchronous request-reply call where a user is waiting on an answer, a case the event-driven
decision guide says asynchronous event architectures cannot serve well because they cannot guarantee response
time.[^s2]

Beyond that, the alternatives decouple systems. An enterprise service bus puts a central hub between applications
so that changing one does not break the others.[^s6] An event bus lets a source publish once while any number of
subscribers consume; the decision guide recommends adding a new subscriber to the bus instead of building another
custom point-to-point link.[^s2] The Platform Events guide states the underlying benefit: producers do not know
which consumers receive their events, so the only shared dependency is the meaning of the message.[^s3] For
request-driven APIs, API-led connectivity organizes reusable System, Process and Experience APIs into an
application network.[^s1]

## Connections

Point-to-point integration is the simplest topology among the `kt:integration-patterns` and the one most
Salesforce guidance positions as the starting point to grow out of.[^s2][^s4] It contrasts with
`kt:api-led-connectivity`, which Trailhead defines as its opposite, and with the `kt:application-network` of
reusable APIs that API-led connectivity produces, typically on `kt:mulesoft-anypoint-platform`.[^s1] It also
contrasts with `kt:event-driven-architecture`, where `kt:platform-events` and an event bus replace one-to-one
links with publish/subscribe.[^s2][^s3] A central `kt:enterprise-service-bus` is the classic alternative
topology.[^s6] In Salesforce, `kt:apex-callouts` are the usual way such links are built, and an accumulation of
them is a common cause of `kt:technical-debt-in-salesforce`.[^s2][^s4]

## Sources

[^s1]: Trailhead, "Explore the Application Network (MuleSoft Basics)". https://trailhead.salesforce.com/content/learn/modules/mulesoft-basics/app-network (accessed 2026-11-23)
[^s2]: Salesforce Architects, "Using the Right Tools and Patterns for Event-Driven Architectures". https://architect.salesforce.com/decision-guides/event-driven (accessed 2026-11-23)
[^s3]: Salesforce, "Event-Driven Software Architecture", Platform Events Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_intro_architecture.htm (accessed 2026-11-23)
[^s4]: Greg Cook, "Integration Architecture for the Salesforce Platform", Salesforce Developers Blog, 2014. https://developer.salesforce.com/blogs/developer-relations/2014/11/salesforce-integration-architecture (accessed 2026-11-23)
[^s5]: MuleSoft, "Eliminating point to point integration pain with Mule ESB". https://www.mulesoft.com/integration/point-to-point-integration (accessed 2026-11-23)
[^s6]: Salesforce, "Enterprise Service Bus (ESB): Connecting Enterprise Systems at Scale". https://www.salesforce.com/ap/blog/what-is-esb/ (accessed 2026-11-23)
