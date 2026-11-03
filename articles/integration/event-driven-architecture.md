---
id: kt:event-driven-architecture
type: Pattern
title: Event-Driven Architecture
aliases: [EDA, event-driven integration, event-based architecture, publish-subscribe architecture]
domain: integration
summary: >-
  An architectural style in which producers publish events describing state changes to a channel or bus and any
  number of decoupled consumers react to them asynchronously; on Salesforce it is realized mainly through the event
  bus, platform events, Change Data Capture and the Pub/Sub API.
release: "Winter '27"
status: concept
broader: [kt:integration-patterns]
related: [kt:platform-events, kt:change-data-capture, kt:pub-sub-api, kt:outbound-messaging, kt:well-architected-framework]
relations:
  - {predicate: contrastsWith, object: kt:integration-patterns-request-reply-fire-and-forget}
  - {predicate: integratesWith, object: kt:mulesoft-anypoint-platform}
  - {predicate: coveredBy, object: kt:integration-architect-certification}
sources:
  - id: s1
    title: "Using the Right Tools and Patterns for Event-Driven Architectures"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/decision-guides/event-driven
    type: official-docs
    accessed: 2026-11-03
  - id: s2
    title: "Event-Driven Software Architecture (Platform Events Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_intro_architecture.htm
    type: official-docs
    accessed: 2026-11-03
  - id: s3
    title: "Platform Events Basics: Understand Event-Driven Software Architecture"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/content/learn/modules/platform_events_basics/platform_events_architecture
    type: official-learning
    accessed: 2026-11-03
  - id: s4
    title: "Integration Patterns Overview"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/integration-patterns
    type: official-docs
    accessed: 2026-11-03
  - id: s5
    title: "Create an Event Relay"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=platform.ev_relay_create_ui.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-03
created: 2026-11-03
---

# Event-Driven Architecture

Event-driven architecture (EDA) is a way of connecting systems in which components produce and consume *events*, messages that announce a change in system or application state, instead of calling each other directly. Salesforce's architecture guidance presents it as a route to loosely coupled systems and near real-time updates, and recommends it for processes that do not need a synchronous answer. It is a poor fit when a person is waiting on a response, or when source data changes so rarely that a batch job would be simpler.[^s1]

## Core vocabulary

Salesforce's developer documentation and Trailhead use the same set of terms.[^s2][^s3] An **event** is a business-relevant change of state, such as an order being placed. An **event message** (or event notification) carries the data about that event. An **event producer** publishes messages, and an **event consumer** subscribes to a **channel**, the stream that producers write to and consumers read from. The Salesforce **event bus** is a multitenant, multicloud publish-subscribe storage and delivery service. It keeps a time-ordered log, so messages are delivered in the order Salesforce received them and can be read again at any point within the retention window.[^s2]

The key difference from request-response integration is who depends on whom. In request-response, a client must connect to a service and query it for current state, so the client relies on that service being available. In an event model, consumers are notified when something happens, producers do not know who is listening, and any number of consumers can react to one event. The only contract they share is what the message content means.[^s2][^s3] Trailhead compares it to radio broadcasting: messages go out asynchronously and receivers do not acknowledge them.[^s3]

## Patterns

The Salesforce decision guide separates five event patterns and compares them on delivery guarantees, per-subscriber copies and transformation:[^s1]

- **Publish/subscribe**: fire-and-forget messages to a bus, with a unique copy for each subscriber.[^s1]
- **Fanout**: all subscribers read the same message from a single queue. This is efficient for mass notifications, but it is harder to confirm that a particular subscriber received a message.[^s1]
- **Passed messages**: separate components route, transform (for example, field mappings and object relationships) and write messages, for high volumes and complex mapping.[^s1]
- **Streaming**: ordered event streams. Ordering needs extra logic when events come from several sources.[^s1]
- **Queuing**: producers write to queues that subscribers drain later, typically in FIFO order. This suits offline mobile clients and IoT. Queues have storage limits, so unread or oversized queues should be purged or disabled.[^s1]

## Salesforce tooling

For publishing record and field changes, the decision guide prefers platform events (custom payloads) and Change Data Capture (fixed create, update, delete and undelete payloads). Both have a 3-day replay period and a 1 MB message limit. It names the Pub/Sub API as the mechanism for all new publish/subscribe work and suggests moving Streaming API or custom Apex-based messaging to it where feasible.[^s1] Outbound messages, PushTopic and generic streaming events remain supported but receive no further investment.[^s1] For Amazon Web Services targets, an **event relay** links a channel on the event bus to Amazon EventBridge through a named credential. The relay is created in a stopped state and is started after the partner event source is activated in EventBridge.[^s5] For broader enterprise use, the guide points to MuleSoft Anypoint (with connectors for Kafka, JMS, Solace, Anypoint MQ and others) or an existing enterprise service bus.[^s1]

In Salesforce's integration pattern catalogue, the *Remote Process Invocation: Fire and Forget* pattern is the main event-driven pattern. It is asynchronous and triggered by DML events. Flow-driven platform events, Pub/Sub API, Change Data Capture and Event Relay are listed as its best fits, and outbound messaging and Apex callouts from triggers or batch jobs are rated suboptimal.[^s4]

## Trade-offs and anti-patterns

Publishers usually cannot see whether subscribers are online, so a critical message published while every subscriber is down can be lost. Replay and redundant subscribers on separate servers mitigate this risk.[^s1] Once external subscribers depend on a message format, changing it is costly. Versioned channels or a schema registry help, and so does governance by skilled staff. Legacy systems may not be able to consume events, and the bus itself can become a bottleneck. The guide recommends migrating to EDA incrementally, starting with the most business-critical applications.[^s1]

Anti-patterns the guide calls out include:[^s1]

- triggers that publish the event they subscribe to, which causes an infinite loop;[^s1]
- two systems that each publish in response to the other's events;[^s1]
- publishing before the DML transaction commits;[^s1]
- using events to orchestrate internal Flow automation instead of subflows or Flow Orchestrator;[^s1]
- events that create runtime dependencies between packages;[^s1]
- oversized payloads.[^s1]

## Connections

EDA sits under `kt:integration-patterns`, the catalogue of Salesforce integration approaches, and it **contrasts with** the synchronous request-and-reply style covered by `kt:integration-patterns-request-reply-fire-and-forget`.[^s4] Its main Salesforce implementations are `kt:platform-events` and `kt:change-data-capture`, consumed externally through `kt:pub-sub-api`. `kt:outbound-messaging` is the legacy low-code option that the decision guide no longer invests in.[^s1] At enterprise scale it **integrates with** `kt:mulesoft-anypoint-platform`.[^s1] The graph also links it to `kt:integration-architect-certification` as a study topic and to `kt:well-architected-framework`, whose architecture guidance hosts the decision guide.[^s1]

## Sources

[^s1]: Salesforce Architects, "Using the Right Tools and Patterns for Event-Driven Architectures". https://architect.salesforce.com/decision-guides/event-driven (accessed 2026-11-03)
[^s2]: Salesforce Developers, "Event-Driven Software Architecture", Platform Events Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_intro_architecture.htm (accessed 2026-11-03)
[^s3]: Trailhead, "Platform Events Basics: Understand Event-Driven Software Architecture". https://trailhead.salesforce.com/en/content/learn/modules/platform_events_basics/platform_events_architecture (accessed 2026-11-03)
[^s4]: Salesforce Architects, "Integration Patterns Overview". https://architect.salesforce.com/fundamentals/integration-patterns (accessed 2026-11-03)
[^s5]: Salesforce Help, "Create an Event Relay". https://help.salesforce.com/s/articleView?id=platform.ev_relay_create_ui.htm&language=en_US&type=5 (accessed 2026-11-03)
