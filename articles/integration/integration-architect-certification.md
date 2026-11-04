---
id: kt:integration-architect-certification
type: Certification
title: Integration Architect Certification
aliases: [Salesforce Certified Platform Integration Architect, Platform Integration Architect certification]
domain: integration
summary: >-
  Salesforce's domain architect credential for assessing an integration landscape and designing scalable, end-to-end
  integration solutions on the Salesforce Platform; it is one of the four certifications that together grant the
  System Architect credential on the path to Certified Technical Architect.
release: "Winter '27"
status: current
broader: [kt:salesforce-architect]
related: [kt:integration-patterns, kt:data-integration, kt:event-driven-architecture, kt:platform-events, kt:named-credentials, kt:mulesoft-anypoint-platform]
relations:
  - {predicate: partOf, object: kt:system-architect-certification}
  - {predicate: contrastsWith, object: kt:identity-and-access-management-architect-certification}
sources:
  - id: s1
    title: "Certification - Salesforce Certified Platform Integration Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/pt-BR/credentials/platformintegrationarchitect
    type: official-learning
    accessed: 2026-11-04
  - id: s2
    title: "Certification - Salesforce Certified System Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/es/credentials/systemarchitect
    type: official-learning
    accessed: 2026-11-04
  - id: s3
    title: "Integration Patterns Overview"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/integration-patterns
    type: official-docs
    accessed: 2026-11-04
  - id: s4
    title: "Integration Patterns and Practices: Pattern Summary"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.integration_patterns_and_practices.meta/integ/integ_pat_pat_summary.htm
    type: official-docs
    accessed: 2026-11-04
created: 2026-11-04
---

# Integration Architect Certification

The Salesforce Certified Platform Integration Architect is the architect-level credential for people who assess an organization's architecture environment and requirements and then design scalable Salesforce Platform solutions that meet end-to-end integration needs.[^s1] Trailhead lists it next to the other domain architect credentials — Identity and Access Management, Development Lifecycle and Deployment, and the MuleSoft Platform Integration Architect — and recommends the "Architect Journey: Integration Architecture" Trailmix as preparation.[^s1]

## Where it sits in the architect path

Like the other domain exams, it is mainly a building block. Salesforce grants the **System Architect** credential once a candidate holds four prerequisites: Platform Developer, Platform Development Lifecycle and Deployment Architect, Platform Identity and Access Management Architect, and Platform Integration Architect; there is no separate System Architect exam.[^s2] Trailhead describes System Architects as focused on off-platform systems, integration and securing access between systems, plus governance and testing of change.[^s1][^s2] The Certified Technical Architect sits above it as a related, higher credential covering secure, high-performance integrated solutions within a customer's wider architectural landscape.[^s2]

## What it tests (at a practitioner level)

The exam is about choosing and justifying an integration approach, not memorizing API syntax. Salesforce's architecture guidance frames the territory in three categories: data integration (keeping records in sync across systems, which depends on master data management and de-duplication), process integration (a business process spanning applications, via orchestration or choreography), and virtual integration (working with external data in real time without copying it).[^s3] It then names six canonical patterns: Remote Process Invocation—Request and Reply, Remote Process Invocation—Fire and Forget, Batch Data Synchronization, Remote Call-In, UI Update Based on Data Changes, and Data Virtualization.[^s4] Request and Reply and Data Virtualization are synchronous; Fire and Forget, Batch Data Synchronization and UI updates are asynchronous; Remote Call-In can be either.[^s3]

Candidates are expected to map requirements onto those patterns using the forces Salesforce lists: whether Salesforce must wait for an answer, message size, whether a UI action or DML triggers the call, latency tolerance, guaranteed delivery, and whether a declarative tool is preferable to Apex.[^s3] The same guidance supplies the kind of numbers and rules scenario questions hinge on: Apex callout timeouts are configurable up to 120 seconds, synchronous governor limits argue for short callouts or continuations, platform events are published without Salesforce-side retry and can't be rolled back with the transaction, and high-volume event messages are retained for 72 hours for replay.[^s3]

## Gotchas

- **Middleware is a design decision, not an afterthought.** Salesforce does not take part in distributed transactions, so heavy orchestration, transformation and cross-system transactional integrity belong in middleware such as MuleSoft.[^s3]
- **Legacy tools are discouraged for new designs.** The guidance rates outbound messaging and CometD-based Streaming API below Pub/Sub API, platform events and Change Data Capture for fire-and-forget work.[^s3]
- **Security choices are tested too.** Prefer Named Credentials and OAuth 2.0 over custom authentication code, and note that WS-Security is not natively supported.[^s3]
- **Idempotency matters.** Unique message IDs and upsert-style writes prevent duplicates when messages are redelivered.[^s3]
- **Exam logistics change.** The credential page links out to a separate registration experience; confirm question count, timing and fee there rather than in third-party summaries.[^s1]

## When to pursue it

Pursue it if you design how Salesforce exchanges data and events with ERPs, data warehouses, middleware or custom apps, or if you are aiming for System Architect or CTA.[^s2] If your integration work is mostly building MuleSoft APIs rather than designing the Salesforce side, the separate MuleSoft Platform Integration Architect credential is the closer match.[^s1]

## Connections

- **broader → `kt:salesforce-architect`**: one rung of the Salesforce architect credential ladder.[^s1]
- **partOf → `kt:system-architect-certification`**: one of the four certifications that roll up into System Architect.[^s2]
- **contrastsWith → `kt:identity-and-access-management-architect-certification`**: a sibling System Architect prerequisite; IAM covers how users and systems authenticate, this exam how systems exchange data and processes.[^s2]
- **related → `kt:integration-patterns`, `kt:data-integration`, `kt:event-driven-architecture`**: the pattern catalogue and integration styles the exam is built around.[^s3][^s4]
- **related → `kt:platform-events`, `kt:named-credentials`**: the event bus and callout-authentication features the guidance recommends.[^s3]
- **related → `kt:mulesoft-anypoint-platform`**: the middleware Salesforce points to for orchestration and transformation.[^s3]

## Sources
[^s1]: Trailhead, "Certification - Salesforce Certified Platform Integration Architect". https://trailhead.salesforce.com/pt-BR/credentials/platformintegrationarchitect (accessed 2026-11-04)
[^s2]: Trailhead, "Certification - Salesforce Certified System Architect". https://trailhead.salesforce.com/es/credentials/systemarchitect (accessed 2026-11-04)
[^s3]: Salesforce Architects, "Integration Patterns Overview". https://architect.salesforce.com/fundamentals/integration-patterns (accessed 2026-11-04)
[^s4]: Salesforce Developers, "Integration Patterns and Practices: Pattern Summary". https://developer.salesforce.com/docs/atlas.en-us.integration_patterns_and_practices.meta/integ/integ_pat_pat_summary.htm (accessed 2026-11-04)
