---
id: kt:apex-callouts
type: Feature
title: Apex Callouts
aliases: [Apex HTTP callout, HTTP callouts from Apex, Apex web service callout, outbound Apex callout]
domain: development
summary: >-
  The Apex capability for calling external web services or sending HTTP requests from Salesforce, using the Http,
  HttpRequest and HttpResponse classes or WSDL-generated SOAP classes, subject to per-transaction callout and timeout limits.
release: "Winter '27"
status: current
broader: [kt:apex, kt:data-integration]
related: [kt:queueable-apex, kt:apex-testing, kt:integration-patterns, kt:outbound-messaging, kt:external-objects]
relations:
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: dependsOn, object: kt:named-credentials}
  - {predicate: configuredVia, object: kt:remote-site-settings}
  - {predicate: hasPart, object: kt:apex-continuations}
  - {predicate: alternativeTo, object: kt:external-services}
  - {predicate: coveredBy, object: kt:integration-architect-certification}
sources:
  - id: s1
    title: "Apex Developer Guide: Invoking Callouts Using Apex"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_callouts.htm
    type: official-docs
    accessed: 2026-11-04
  - id: s2
    title: "Apex Developer Guide: Callout Limits and Limitations"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_callouts_timeouts.htm
    type: official-docs
    accessed: 2026-11-04
  - id: s3
    title: "Apex Developer Guide: Testing HTTP Callouts by Implementing the HttpCalloutMock Interface"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_restful_http_testing_httpcalloutmock.htm
    type: official-docs
    accessed: 2026-11-04
  - id: s4
    title: "Trailhead: Apex REST Callouts (Apex Integration Services)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/content/learn/modules/apex_integration_services/apex_integration_rest_callouts
    type: official-learning
    accessed: 2026-11-04
created: 2026-11-04
---

# Apex Callouts

An Apex callout is outbound integration initiated from Apex code: the code either invokes an external web service or sends an HTTP request and processes the response.[^s1] Salesforce supports two styles. SOAP services described by a WSDL are called through Apex classes generated from that WSDL document, while RESTful and other HTTP services are called directly with HTTP classes.[^s1] For long-running requests started from a Visualforce page or Lightning component, an asynchronous continuation lets the request run while the response is handled later in a callback method.[^s1] The opposite direction, external systems invoking Apex, is handled by Apex web services rather than callouts.[^s1]

## How it works

An HTTP callout is built from three classes: `HttpRequest` carries the endpoint, method, headers and body; `Http.send()` dispatches it; and `HttpResponse` exposes the status code, headers and body.[^s4] JSON payloads are typically turned into Apex structures with `JSON.deserializeUntyped` or a `JSONParser`.[^s4] The call is synchronous, so the transaction blocks until the remote service answers or the timeout expires.[^s4]

Before any callout can reach an endpoint, the endpoint must be authorized. Registering the host in Remote Site Settings is the classic approach; without it the callout fails, and Salesforce also blocks calls to unauthorized network addresses.[^s1] If the callout uses a named credential as its endpoint, no remote site setting is needed: the named credential holds the URL and authentication parameters, and the platform handles authentication instead of the code.[^s1] That makes named credentials the cleaner choice whenever the target requires authentication, because secrets stay out of Apex.[^s1]

## Limits and gotchas

The figures below were checked against the Winter '27 (API 68.0) Apex Developer Guide.[^s2]

- **Count.** One Apex transaction can make at most 100 callouts, whether HTTP requests or API calls.[^s2]
- **Timeouts.** Each callout defaults to a 10-second timeout; a custom value can range from 1 millisecond to 120,000 milliseconds, and the timeouts of all callouts in a transaction together cannot exceed 120 seconds.[^s2]
- **Uncommitted work.** A callout cannot follow pending operations in the same transaction, including DML, enqueued future or batch jobs, scheduled Apex and sending email; callouts may run before them.[^s2] The usual design is callout first, then DML, or moving the callout into asynchronous Apex.
- **Long-running request limit.** Each org limits requests running more than 5 seconds, but the timer pauses while an HTTP callout is processing, so callout wait time does not count.[^s2]
- **Developer Edition concurrency.** Developer Edition orgs may run up to 20 concurrent callouts to endpoints outside the org's domain; this cap does not apply to other editions.[^s2]
- **Read-only mode.** Callouts still execute when an org is read-only, but record writes fail, so the guide suggests checking `System.getApplicationReadWriteMode()` and skipping callouts in that mode.[^s2]
- **Triggers.** Because a callout blocks, a trigger cannot call out synchronously; the work must move to a method annotated `@future(callout=true)` or to Queueable Apex.[^s4]

## Testing

Test methods do not support real callouts, and a test that attempts one fails, so coverage requires mocks.[^s4] `Test.setMock` tells the runtime to return a fake response: either a `StaticResourceCalloutMock` that serves a body stored in a static resource, or a class implementing `HttpCalloutMock` whose `respond` method builds an `HttpResponse` with the desired status, headers and body.[^s4][^s3] The `respond` method can also assert on the outgoing request, such as its endpoint or method, and marking the mock class `@IsTest` keeps it out of the org's code size limit.[^s3] Pending DML is allowed before a mock callout in a test, which differs from production behaviour.[^s2]

## When to use it (and when not)

Use Apex callouts when logic must shape the request or interpret the response, for example to transform data, branch on status codes, or orchestrate several calls in one transaction.[^s1][^s4] For request-reply integrations started from the UI with slow endpoints, prefer continuations so the user's request is not held open.[^s1] For declarative, schema-driven calls, External Services can replace hand-written HTTP code, and for one-way notifications without code, outbound messaging or event-based patterns may fit better than a trigger-plus-future callout.[^s1][^s4]

## Connections

`kt:apex-callouts` sits under `kt:apex` as a language capability and under `kt:data-integration` as the main code-based way Salesforce calls out to other systems.[^s1] It is `governedBy` `kt:governor-limits` (the 100-callout and 120-second cumulative caps), `dependsOn` `kt:named-credentials` for authenticated endpoints, and is `configuredVia` `kt:remote-site-settings` when no named credential is used.[^s2][^s1] `kt:apex-continuations` is its asynchronous variant for UI-initiated long requests, and `kt:external-services` is the declarative alternative.[^s1] From triggers it is commonly run through `kt:queueable-apex` or future methods, it is tested with the mocking tools in `kt:apex-testing`, and it appears as a solution option within `kt:integration-patterns`, alongside `kt:outbound-messaging` and `kt:external-objects`.[^s4][^s3] The edge to `kt:integration-architect-certification` reflects that callout limits and placement are core integration design concerns.[^s2]

## Sources
[^s1]: Salesforce Developers, "Apex Developer Guide: Invoking Callouts Using Apex". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_callouts.htm (accessed 2026-11-04)
[^s2]: Salesforce Developers, "Apex Developer Guide: Callout Limits and Limitations". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_callouts_timeouts.htm (accessed 2026-11-04)
[^s3]: Salesforce Developers, "Apex Developer Guide: Testing HTTP Callouts by Implementing the HttpCalloutMock Interface". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_restful_http_testing_httpcalloutmock.htm (accessed 2026-11-04)
[^s4]: Trailhead, "Apex REST Callouts" (Apex Integration Services module). https://trailhead.salesforce.com/en/content/learn/modules/apex_integration_services/apex_integration_rest_callouts (accessed 2026-11-04)
