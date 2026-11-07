---
id: kt:architect-decision-guides
type: Tool
title: Architect Decision Guides
aliases: [Salesforce Decision Guides, Platform Decision Guides, Salesforce Architects decision guides]
domain: architecture-practice
summary: >-
  A set of Salesforce-authored guides on architect.salesforce.com that compare overlapping platform tools for one problem
  area (forms, record-triggered automation, async processing, eventing, data integration, agentic vs. traditional
  automation) and give a decision framework, recommendations and anti-patterns; first published in June 2020.
release: "Winter '27"
status: current
broader: [kt:solution-design-tradeoffs]
related: [kt:record-triggered-flow, kt:apex-triggers, kt:asynchronous-apex, kt:event-driven-architecture, kt:data-integration, kt:screen-flow]
relations:
  - {predicate: partOf, object: kt:salesforce-architecture-center}
  - {predicate: usedBy, object: kt:salesforce-architect}
sources:
  - id: s1
    title: "Get Started with Platform Decision Guides"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/decision-guides/guide/get-started-platform-decision-guides.html
    type: official-docs
    accessed: 2026-11-07
  - id: s2
    title: "Introducing the Architect Decision Guides"
    publisher: Salesforce Architects (Medium)
    url: https://medium.com/salesforce-architects/introducing-architect-decision-guides-609ae5d7b5da
    type: official-blog
    accessed: 2026-11-07
  - id: s3
    title: "Record-Triggered Automation Decision Guide"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/decision-guides/guide/record-triggered
    type: official-docs
    accessed: 2026-11-07
  - id: s4
    title: "Using the Right Tools and Patterns for Event-Driven Architectures"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/decision-guides/event-driven
    type: official-docs
    accessed: 2026-11-07
  - id: s5
    title: "Decision Guide Updates for January 2024"
    publisher: Salesforce Architects (Medium)
    url: https://medium.com/salesforce-architects/decision-guide-updates-for-january-2025-11a66dc69605
    type: official-blog
    accessed: 2026-11-07
created: 2026-11-07
---

# Architect Decision Guides

Architect Decision Guides are Salesforce-authored documents that help a team choose between platform tools that overlap. Each guide takes one problem area, compares the tools or approaches available for it, lists the factors to weigh, and closes with best practices and pitfalls to avoid.[^s1] They are written for solution and enterprise architects, but admins and developers use them to settle "Flow or Apex?"-style debates with the product teams' own recommendations rather than opinion.[^s1][^s2]

## Origin and maintenance

Salesforce Architects launched the guides on June 25, 2020 with two titles: an Architect's Guide to Building Forms and an Architect's Guide to Building Record-Triggered Automation.[^s2] Both used the same two-step method. First, narrow the field to tools that meet the functional, performance and scalability requirements. Then pick the one that best fits the team's skills now and later, weighing specialized skills, who will deliver the work, and long-term ownership.[^s2] The launch post was explicit that the guides are not a signal to refactor existing implementations, and that the first iteration left troubleshooting, maintenance and governance out of scope.[^s2]

The guides are living documents. Salesforce Architects say they review them regularly with product team members and other subject-matter experts. A January 2024 update, for example, changed the Data Integration guide to recommend Data Cloud or MuleSoft for multi-org approaches and added AWS Event Relays and new anti-patterns to the Event-Driven Architecture guide.[^s5] Most guide pages show no publication or last-updated date, so check the change announcements before relying on a detail in a design document.[^s1][^s3]

## What the catalogue covers

As of Winter '27 the platform index lists guides for asynchronous processing, building forms, agentic versus traditional workflow automation, event-driven architecture and record-triggered automation, plus a step-based async framework that sits under the site's fundamentals section.[^s1]

- **Asynchronous Processing** compares Queueable Apex, Scheduled Apex, platform event triggers, Change Data Capture, and the scheduled and asynchronous paths of record-triggered flows, with server- and client-side patterns and anti-patterns.[^s1]
- **Building Forms** compares Dynamic Forms, Screen Flow, OmniStudio, Screen Flow with LWC and plain LWC, including skills and licensing, against factors such as object impact, navigation, location (app, mobile, web) and test automation.[^s1]
- **Agentic and Traditional Workflow Automation** introduces an "Orchestration Density" framework that scores execution path, goal complexity and modality mix, then maps low, medium and high density to tools ranging from Flow and Apex to Agentforce and MuleSoft.[^s1]
- **Event-Driven Architecture** compares Platform Events, Change Data Capture, Pub/Sub API, Outbound Messages, Event Relays, Kafka on Heroku and MuleSoft connectors across the publish/subscribe, fanout, passed-messages, streaming and queueing patterns.[^s4]

## Example: record-triggered automation

The record-triggered guide shows the typical shape. It sets three principles: match the tool to automation density, use caution with async processing, and keep one automation entry point per object.[^s3] Its density matrix recommends record-triggered Flow for low density (fewer than 15 automations on an object), a hybrid of Flow orchestrating invocable Apex for medium density (15 to 30), and Apex triggers, ideally on a metadata-driven framework, above 30.[^s3] It also steers same-record field updates to before-save context, warns that async limits are org-wide, and recommends Change Data Capture for high-volume asynchronous work, noting that CDC payloads lack prior values.[^s3]

## Gotchas

The guides give recommendations, not platform rules, so a design still has to be checked against the org's actual limits and licences.[^s1][^s2] Some guidance is a product-investment signal rather than a technical limit. The event-driven guide, for instance, says Salesforce will keep supporting PushTopic and generic events without investing further, and recommends moving to Pub/Sub API where feasible.[^s4] Finally, guides cross-reference each other. Eventing and async choices often need the Asynchronous Processing, Event-Driven Architecture and Data Integration guides read together.[^s1][^s4]

## Connections

The guides are **part of** the `kt:salesforce-architecture-center` and are a concrete, documented form of `kt:solution-design-tradeoffs`, which is their broader practice.[^s1] The record-triggered guide is the canonical comparison of `kt:record-triggered-flow` and `kt:apex-triggers`.[^s3] The async guide covers `kt:asynchronous-apex` tools, the forms guide weighs `kt:screen-flow` against code, and the eventing and integration guides frame choices in `kt:event-driven-architecture` and `kt:data-integration`.[^s1][^s4][^s5] They are **used by** the `kt:salesforce-architect` role to justify tool choices with published rationale.[^s1][^s2]

## Sources

[^s1]: Salesforce Architects, "Get Started with Platform Decision Guides". https://architect.salesforce.com/docs/architect/decision-guides/guide/get-started-platform-decision-guides.html (accessed 2026-11-07)
[^s2]: Salesforce Architects, "Introducing the Architect Decision Guides" (2020-06-25). https://medium.com/salesforce-architects/introducing-architect-decision-guides-609ae5d7b5da (accessed 2026-11-07)
[^s3]: Salesforce Architects, "Record-Triggered Automation Decision Guide". https://architect.salesforce.com/docs/architect/decision-guides/guide/record-triggered (accessed 2026-11-07)
[^s4]: Salesforce Architects, "Using the Right Tools and Patterns for Event-Driven Architectures". https://architect.salesforce.com/decision-guides/event-driven (accessed 2026-11-07)
[^s5]: Salesforce Architects, "Decision Guide Updates for January 2024" (2024-01-16). https://medium.com/salesforce-architects/decision-guide-updates-for-january-2025-11a66dc69605 (accessed 2026-11-07)
