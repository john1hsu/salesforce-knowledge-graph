---
id: kt:remote-call-in
type: Pattern
title: Remote Call-In
aliases: [Remote Call-In pattern, inbound integration pattern, remote call in]
domain: integration
summary: >-
  The inbound Salesforce integration pattern in which a remote system connects and authenticates to Salesforce to
  notify it of external events or to create, retrieve, update or delete Salesforce records, typically through the
  REST, Composite, GraphQL, Bulk 2.0 or Pub/Sub APIs.
release: "Winter '27"
status: concept
broader: [kt:integration-patterns]
related: [kt:bulk-api-2, kt:pub-sub-api, kt:graphql-api, kt:external-id-fields, kt:apex-rest-services]
relations:
  - {predicate: partOf, object: kt:integration-patterns}
  - {predicate: contrastsWith, object: kt:integration-patterns-request-reply-fire-and-forget}
  - {predicate: dependsOn, object: kt:rest-api}
  - {predicate: dependsOn, object: kt:composite-api}
  - {predicate: dependsOn, object: kt:platform-events}
  - {predicate: governedBy, object: kt:api-request-limits}
  - {predicate: coveredBy, object: kt:integration-architect-certification}
sources:
  - id: s1
    title: "Integration Patterns Overview"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/integration-patterns
    type: official-docs
    accessed: 2026-11-09
  - id: s2
    title: "Send Multiple Requests Using Composite (REST API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-rest/guide/resources-composite-composite-post.html
    type: official-docs
    accessed: 2026-11-09
  - id: s3
    title: "Apex Web Services (Apex Integration Services)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/apex_integration_services/apex_integration_webservices
    type: official-learning
    accessed: 2026-11-09
created: 2026-11-09
---

# Remote Call-In

Remote Call-In is the inbound pattern in Salesforce's integration catalogue: data stored in Salesforce is created, retrieved, updated or deleted by a remote system, or the remote system tells Salesforce that something happened outside it.[^s1] The catalogue's selection matrix makes it the key pattern when another system integrates with Salesforce for process integration (synchronous or asynchronous) and for synchronous data integration; asynchronous data integration in that direction points to Batch Data Synchronization instead.[^s1]

## Problem and forces

The question the pattern answers is how an external system connects and authenticates to Salesforce to signal events and maintain records. The forces an architect weighs are: whether the call is an event notification (decoupled producer and consumer) or a CRUD operation on specific records; whether the caller needs a reply; whether one object or several related objects change per transaction; SOAP versus REST; message size; whether the remote side accepts a contract dictated by Salesforce; whether transactional processing is needed; and how much Salesforce-side customization is acceptable.[^s1] Calls into the platform are always synchronous request-reply at the transport level, though a caller can ignore the response to behave asynchronously.[^s1]

## Solution options

The architect guidance rates these options:

- **Best:** REST API for simple, lightweight record operations, event publishing and queries; Composite API to bundle several dependent requests; Composite Graph API for larger related-record graphs; GraphQL API for multi-object reads that select specific fields; Pub/Sub API (gRPC) as the recommended way for external publishers to send platform events; and platform events published through REST, SOAP or Bulk APIs.[^s1]
- **Best for bulk operations:** Bulk API 2.0, the asynchronous option once an operation exceeds roughly 2,000 records.[^s1]
- **Suboptimal:** SOAP API, which needs deep object-model and SOAP knowledge; and custom Apex SOAP or Apex REST services, justified only when full transactional control or custom pre-commit logic is required.[^s1]

The composite resource accepts up to 25 subrequests per call, of which at most 5 can be query or sObject Collections operations; later subrequests can reference earlier results by reference ID, and the whole series counts as one call against API limits.[^s2] By default composite allows partial success, so a 200 response can still hide a failed, rolled-back subrequest, and callers must inspect the body.[^s1][^s2]

Custom Apex REST services are global classes annotated with `@RestResource`, exposed under `/services/apexrest/`, and they accept OAuth 2.0 or session authentication. They suit hiding complex logic behind one endpoint, while the standard APIs remain the choice for plain create, update and delete.[^s3]

## Limits and gotchas

- **Volumes.** Synchronous SOAP or REST create, update and delete calls handle up to 200 records per request. Query batches default to 500 rows with a maximum of 2,000, and each SOQL query times out at 120 seconds.[^s1]
- **Events.** An event message can be at most 1 MB, and publishing consumes standard API limits. The guidance cites 100,000 events per hour for standard volume and 250,000 per hour for high-volume usage-based events.[^s1]
- **Query cursors.** A user can hold up to 10 open query cursors, and the oldest is released when that is exceeded, so shared integration users should run queries serially or be split per application.[^s1]
- **API allocation.** Daily API requests depend on edition and licenses; the guidance's example is 5,000 requests per Salesforce Platform license per 24 hours in Unlimited Edition.[^s1]
- **Security.** Calls run with the authenticated user's profile, permission sets and sharing, and profile IP ranges can restrict API access. SOAP requires TLS 1.2 or later; REST and custom services rely on an OAuth trust, and tokens should be cached and reused rather than requested per call.[^s1] Apex web service methods run in system context and ignore the user's object and field permissions unless the code enforces them, so declare `with sharing` and add access checks.[^s3]
- **Errors and idempotency.** The remote system or middleware owns timeouts, retries and reliable messaging, because the SOAP and REST APIs do not implement protocols such as WS-ReliableMessaging. Calls must be idempotent to avoid duplicate inserts and unintended trigger or flow executions on retry.[^s1]

## When to use it (and when not)

Use Remote Call-In when the external system is the initiator: pushing an order status, upserting reference data keyed on an external ID, or publishing a business event that flows and triggers react to. If Salesforce is the master, the remote system stores the Salesforce ID; if the remote system is master, Salesforce stores its key in an external ID field in the same transaction.[^s1] Move to Batch Data Synchronization for large asynchronous loads, and to middleware when aggregation, orchestration or transformation is needed, which the guidance prefers over custom Apex services.[^s1]

## Connections

Remote Call-In is part of `kt:integration-patterns` and contrasts with `kt:integration-patterns-request-reply-fire-and-forget`, where Salesforce initiates the call.[^s1] It depends on `kt:rest-api`, `kt:composite-api` and `kt:platform-events`, and draws on `kt:bulk-api-2`, `kt:pub-sub-api` and `kt:graphql-api` for bulk, streaming and read-heavy variants.[^s1][^s2] Cross-system keys rely on `kt:external-id-fields`, custom endpoints are `kt:apex-rest-services`, and volume is governed by `kt:api-request-limits`.[^s1][^s3] The pattern is core vocabulary for the `kt:integration-architect-certification`.

## Sources
[^s1]: Salesforce Architects, "Integration Patterns Overview". https://architect.salesforce.com/fundamentals/integration-patterns (accessed 2026-11-09)
[^s2]: Salesforce Developers, "Send Multiple Requests Using Composite". https://developer.salesforce.com/docs/platform/api-rest/guide/resources-composite-composite-post.html (accessed 2026-11-09)
[^s3]: Trailhead, "Apex Web Services". https://trailhead.salesforce.com/content/learn/modules/apex_integration_services/apex_integration_webservices (accessed 2026-11-09)
