---
id: kt:integration-patterns-request-reply-fire-and-forget
type: Pattern
title: Remote Process Invocation (Request and Reply, Fire and Forget)
aliases: [Remote Process Invocation, Request and Reply pattern, Fire and Forget pattern, RPI request-reply, RPI fire-and-forget]
domain: integration
summary: >-
  The pair of outbound Salesforce integration patterns in which a Salesforce event starts a process in a remote system,
  either waiting synchronously for a reply (Request and Reply) or handing off without waiting (Fire and Forget).
release: "Winter '27"
status: concept
broader: [kt:integration-patterns]
related: [kt:event-driven-architecture, kt:outbound-messaging, kt:apex-continuations, kt:flow-fault-handling, kt:mulesoft-anypoint-platform]
relations:
  - {predicate: partOf, object: kt:integration-patterns}
  - {predicate: dependsOn, object: kt:apex-callouts}
  - {predicate: dependsOn, object: kt:named-credentials}
  - {predicate: dependsOn, object: kt:platform-events}
  - {predicate: contrastsWith, object: kt:remote-call-in}
  - {predicate: coveredBy, object: kt:integration-architect-certification}
sources:
  - id: s1
    title: "Integration Patterns Overview"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/integration-patterns
    type: official-docs
    accessed: 2026-11-09
  - id: s2
    title: "Pattern Selection Guide (Integration Patterns and Practices)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.integration_patterns_and_practices.meta/integ/integ_pat_selection_guide.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s3
    title: "Learn About Integration Patterns and Designs (Application Integration Patterns for Salesforce Lightning Platform)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/es/content/learn/modules/app-integration-patterns/app-integration-patterns-1
    type: official-learning
    accessed: 2026-11-09
  - id: s4
    title: "Callout Limits and Limitations (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_callouts_timeouts.htm
    type: official-docs
    accessed: 2026-11-09
created: 2026-11-09
---

# Remote Process Invocation (Request and Reply, Fire and Forget)

Remote Process Invocation is the family of patterns in Salesforce's integration catalogue for the case where something happens in Salesforce and a process must start in another system. It has two variants. In **Request and Reply**, Salesforce invokes the remote process and waits for its answer; in **Fire and Forget**, Salesforce invokes it and carries on without waiting for the process to finish.[^s3] The pattern selection guide places both under "Integrating Salesforce with Another System": Request and Reply is the synchronous option for process or data integration, and Fire and Forget is the asynchronous option for process integration.[^s2]

## Request and Reply

The problem is how to start a remote process from a Salesforce event, pass it data, receive a response and use that response to update Salesforce. The standard example is order handling: the remote system creates the order and replies synchronously with an order number and status, which Salesforce stores in the same transaction and later uses as a foreign key.[^s1] The deciding forces are whether Salesforce must wait, whether the response must be handled in the same transaction, message size, whether the trigger is a UI action or a DML event, and whether the endpoint can answer with low latency at peak load.[^s1]

Current architect guidance rates the options as follows:[^s1]

- **External Services** (best): declarative REST calls from a registered OpenAPI or YAML definition, invocable from Flow. Without a usable spec, fall back to Apex with Named Credentials.[^s1]
- **Lightning component or page calling synchronous Apex** (best): Apex REST or SOAP callouts via Named Credentials, using a continuation when the endpoint is slow.[^s1]
- **HTTP Callout action in Flow** (good): synchronous REST from Flow without Apex or a full service registration.[^s1]
- **Triggers or Batch Apex making callouts** (suboptimal): trigger-context calls must be asynchronous, so they really belong to Fire and Forget, and batch callouts are bounded per batch context.[^s1]

## Fire and Forget

Here Salesforce starts the remote process and does not wait for it; the remote system may update Salesforce later in a separate transaction. Extra forces include whether delivery must be guaranteed, whether the remote side can accept a contract defined by Salesforce, and whether declarative configuration is preferred.[^s1]

The guidance rates flow-published platform events, Pub/Sub API, Change Data Capture and Event Relay (for Amazon EventBridge) as best fits. OmniStudio Integration Procedures and Apex-published platform events are good. Flow-driven outbound messaging is suboptimal and described as legacy, though it retries until acknowledged. Asynchronous Apex callouts from components, triggers or batch jobs are also suboptimal because they need custom delivery and retry logic.[^s1] In the reference sketch, the remote system subscribes to a platform event, a flow publishes the event when a record changes, and the remote listener queues it for processing, with an optional callback into Salesforce.[^s1]

## Limits and gotchas

- **Callout limits.** An Apex transaction can make 100 callouts. Each callout defaults to a 10-second timeout and can be set from 1 millisecond to 120 seconds, but the total across the transaction is also capped at 120 seconds.[^s4]
- **Pending work.** A callout cannot be made after uncommitted DML, asynchronous Apex, scheduled Apex or email sends in the same transaction; call out first.[^s4]
- **Long-running requests.** The architect guidance warns against more than 50 synchronous transactions each running over five seconds, and suggests a five-second callout timeout or continuations for slow services.[^s1]
- **Payload size.** Request and Reply is for small, real-time payloads, not batch transfer.[^s1]
- **Error handling.** In Request and Reply the caller handles errors and Salesforce commits nothing until it receives success. In Fire and Forget, Salesforce only sees the initial handoff; failed flows email the last modifier unless fault paths are added, and platform events cannot be rolled back.[^s1]
- **Idempotency.** Remote operations must be idempotent. Send unique message IDs and upsert on stable keys. Event subscribers can detect duplicates by replay ID, and high-volume events stay retrievable for 72 hours.[^s1]
- **Security and reachability.** Use Named Credentials rather than custom authentication, and consider OAuth 2.0. One-way SSL is the default and two-way SSL is supported. WS-Security headers must be built manually. Endpoints must be reachable from the internet unless Private Connect is used.[^s1]

## When to use it (and when not)

Choose Request and Reply when a user or process needs the remote result immediately, such as a payment authorisation or an account number to store. Choose Fire and Forget when the remote work can finish later, especially for DML-triggered events. For bulk movement of records, use Batch Data Synchronization instead. When the other system initiates the change, use Remote Call-In. Orchestration across several systems, heavy transformation or cross-system transactions belong in middleware.[^s1][^s2]

## Connections

Both variants are part of `kt:integration-patterns` and contrast with `kt:remote-call-in`, its inbound mirror image.[^s2] Request and Reply depends on `kt:apex-callouts` secured through `kt:named-credentials`, and uses `kt:apex-continuations` for slow endpoints.[^s1][^s4] Fire and Forget depends on `kt:platform-events` and is the event-based case of `kt:event-driven-architecture`. `kt:outbound-messaging` is its legacy option, and `kt:flow-fault-handling` covers its Flow error paths.[^s1] `kt:mulesoft-anypoint-platform` fits where middleware orchestration is needed.[^s1] The edge to `kt:integration-architect-certification` reflects that the catalogue's patterns are shared vocabulary for that credential.

## Sources
[^s1]: Salesforce Architects, "Integration Patterns Overview". https://architect.salesforce.com/fundamentals/integration-patterns (accessed 2026-11-09)
[^s2]: Salesforce Developers, "Pattern Selection Guide (Integration Patterns and Practices)". https://developer.salesforce.com/docs/atlas.en-us.integration_patterns_and_practices.meta/integ/integ_pat_selection_guide.htm (accessed 2026-11-09)
[^s3]: Trailhead, "Learn About Integration Patterns and Designs". https://trailhead.salesforce.com/es/content/learn/modules/app-integration-patterns/app-integration-patterns-1 (accessed 2026-11-09)
[^s4]: Salesforce Developers, "Callout Limits and Limitations". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_callouts_timeouts.htm (accessed 2026-11-09)
