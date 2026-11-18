---
id: kt:process-integration
type: Concept
title: Process Integration
aliases: [process-based integration, business process integration, Salesforce process integration]
domain: integration
summary: >-
  The integration category in which a single business process spans Salesforce and one or more other applications,
  so one system invokes processing in another; implemented with the Remote Process Invocation and Remote Call-In
  patterns and coordinated by orchestration or choreography, as distinct from data and virtual integration.
release: "Winter '27"
status: concept
broader: [kt:integration-patterns]
related: [kt:event-driven-architecture, kt:apex-callouts, kt:platform-events, kt:flow-orchestrator, kt:transaction-control]
relations:
  - {predicate: contrastsWith, object: kt:data-integration}
  - {predicate: contrastsWith, object: kt:data-virtualization}
  - {predicate: hasPart, object: kt:integration-patterns-request-reply-fire-and-forget}
  - {predicate: hasPart, object: kt:remote-call-in}
  - {predicate: integratesWith, object: kt:mulesoft-anypoint-platform}
  - {predicate: governedBy, object: kt:governor-limits}
sources:
  - id: s1
    title: "Integration Patterns Overview"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/integration-patterns
    type: official-docs
    accessed: 2026-11-18
  - id: s2
    title: "Pattern Selection Guide (Integration Patterns and Practices)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.integration_patterns_and_practices.meta/integ/integ_pat_selection_guide.htm
    type: official-docs
    accessed: 2026-11-18
  - id: s3
    title: "Learn About Integration Patterns and Designs (Application Integration Patterns for Salesforce Lightning Platform)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/app-integration-patterns/app-integration-patterns-1
    type: official-learning
    accessed: 2026-11-18
  - id: s4
    title: "Identify Business Uses for Flow Orchestration (Build a Flow Orchestration)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/fr/content/learn/modules/build-a-flow-orchestration/identify-business-uses-for-flow-orchestration
    type: official-learning
    accessed: 2026-11-18
created: 2026-11-18
---

# Process Integration

Process integration is the integration category used when a business process cannot finish inside one application: the triggering system reaches across process boundaries and invokes work in two or more systems. Salesforce's architecture guidance warns that these integrations usually demand complex design, testing and exception handling, and that they load the participating systems more heavily because they tend to run long transactions and must track or report process state.[^s1] The Integration Patterns and Practices guide frames it as integrating the functional flow of processing across applications, and notes that it typically brings more abstraction and complexity than data integration, particularly around transactionality and rollback.[^s2] Trailhead summarises the category as extending business processes and services across systems, for example an event in one system that triggers activity in another, or a transaction that runs between two systems.[^s3]

## How it differs from data and virtual integration

Salesforce groups integrations into three types. Data integration keeps the information applications use synchronised; virtual integration lets users view, search and change external data in real time without copying it; process integration coordinates the *work* itself.[^s1][^s2] The distinction matters because it changes the design questions: a data sync is judged on consistency, volume and freshness, whereas a process integration is judged on who controls each step, how long the process lives, and what happens when one participant fails halfway through.[^s1]

## Patterns used

The pattern selection guide maps process integration onto three patterns by direction and timing. When Salesforce calls another system and waits for an answer, use Remote Process Invocation: Request and Reply; when it hands off work without waiting, use Remote Process Invocation: Fire and Forget; when another system invokes processing in Salesforce, use Remote Call-In, which can be synchronous or asynchronous.[^s2][^s1] Synchronous means the caller blocks for an immediate result, and asynchronous means it continues without waiting.[^s2]

## Orchestration versus choreography

There are two coordination styles. In orchestration a central controller directs each service and the orchestration describes the whole behaviour; in choreography the participating processes act autonomously, with no central authority, reacting to one another.[^s1] Inside Salesforce, Flow Orchestration can run long-running, multi-step processes without middleware, and parts of a choreography can be built with Flow Orchestration, flows or Apex.[^s1] Flow Orchestration groups flows into stages and steps, runs only one stage at a time, and mixes background steps (autolaunched flows) with interactive steps that create work items for users, groups or queues, which suits processes that hand off between teams such as mortgage approval or a lead-to-fulfilment sales cycle.[^s4]

## Limits and gotchas

The central constraint is transactionality. Salesforce is transactional within itself, but it cannot join a distributed transaction or one started outside Salesforce, so multi-system transactions and their rollback or compensation logic belong in a middleware layer.[^s1] The architects' guidance recommends placing complex cross-system orchestration in middleware to avoid Salesforce timeouts and governor limits, and notes that Apex callouts have a configurable timeout of up to 120 seconds.[^s1] Apex callouts alone cannot preserve integrity across several systems, and guaranteed delivery from callouts must be built as a customisation.[^s1] Because an asynchronous hand-off finishes after the original transaction, the remote system usually has to call back with the Salesforce record ID to record its result.[^s1] For inbound calls, the remote caller or middleware must cope with duplicate requests after errors or timeouts, so idempotent design is the caller's job.[^s1] An integration can therefore require an external middleware or Enterprise Service Bus, depending on the requirements of the scenario.[^s2]

## When to use it (and when not)

Choose process integration when the requirement is a business outcome that spans systems, such as submitting an order to ERP or running a credit check during approval, rather than simply having the same data in two places. Keep simple, short, single-callout steps inside Salesforce; move long-running, multi-system or transaction-critical coordination, message transformation and result aggregation to middleware or a composite service.[^s1]

## Connections

Process integration sits under `kt:integration-patterns` and is realised by two of its pattern families, `kt:integration-patterns-request-reply-fire-and-forget` and `kt:remote-call-in`.[^s2] It contrasts with `kt:data-integration` and `kt:data-virtualization`, the other two integration categories.[^s1] Asynchronous choreographies lean on `kt:event-driven-architecture` and `kt:platform-events`, outbound steps on `kt:apex-callouts`, and in-platform orchestration on `kt:flow-orchestrator`.[^s1][^s4] Because Salesforce cannot take part in distributed transactions, designs must respect `kt:transaction-control` and `kt:governor-limits`, and complex orchestration commonly moves to middleware such as `kt:mulesoft-anypoint-platform`.[^s1]

## Sources

[^s1]: Salesforce Architects, "Integration Patterns Overview". https://architect.salesforce.com/fundamentals/integration-patterns (accessed 2026-11-18)
[^s2]: Salesforce Developers, "Pattern Selection Guide (Integration Patterns and Practices)". https://developer.salesforce.com/docs/atlas.en-us.integration_patterns_and_practices.meta/integ/integ_pat_selection_guide.htm (accessed 2026-11-18)
[^s3]: Trailhead, "Learn About Integration Patterns and Designs". https://trailhead.salesforce.com/content/learn/modules/app-integration-patterns/app-integration-patterns-1 (accessed 2026-11-18)
[^s4]: Trailhead, "Identify Business Uses for Flow Orchestration". https://trailhead.salesforce.com/fr/content/learn/modules/build-a-flow-orchestration/identify-business-uses-for-flow-orchestration (accessed 2026-11-18)
