---
id: kt:external-services
type: Feature
title: External Services
aliases: [External Service, External Service Registration, ExternalServiceRegistration, External Service actions]
domain: integration
summary: >-
  A declarative integration feature that imports an OpenAPI specification for a REST API, authenticated through a
  named credential, and turns its selected operations into invocable actions for Flow and Agentforce and into
  strongly typed Apex classes in the ExternalService namespace.
release: "Winter '27"
status: current
broader: [kt:data-integration]
related: [kt:flow-builder, kt:mulesoft-anypoint-platform, kt:heroku]
relations:
  - {predicate: dependsOn, object: kt:named-credentials}
  - {predicate: alternativeTo, object: kt:apex-callouts}
  - {predicate: consumedBy, object: kt:flow-http-callout}
  - {predicate: consumedBy, object: kt:agent-actions}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: implements, object: kt:integration-patterns-request-reply-fire-and-forget}
sources:
  - id: s1
    title: "ExternalServiceRegistration — Metadata API Developer Guide (Winter '27, API 68.0)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_externalserviceregistration.htm
    type: official-docs
    accessed: 2026-11-13
  - id: s2
    title: "External Services — Apex Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_external_services.htm
    type: official-docs
    accessed: 2026-11-13
  - id: s3
    title: "Use External Services with a Flow — Register an External Service"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/use-external-services-with-a-flow/register-external-service
    type: official-learning
    accessed: 2026-11-13
  - id: s4
    title: "External Services — Define an API Specification for an External Service"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/content/learn/modules/external-services/define-a-schema-for-an-external-service
    type: official-learning
    accessed: 2026-11-13
  - id: s5
    title: "Call Third-Party APIs from an Agent with External Service Actions"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2025/05/call-third-party-apis-from-an-agent-with-external-service-actions
    type: official-blog
    accessed: 2026-11-13
  - id: s6
    title: "External Services, API Updates & Learn MOAR in Spring '23"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2023/01/external-services-api-updates-learn-moar-spring-23
    type: official-blog
    accessed: 2026-11-13
created: 2026-11-13
---

# External Services

External Services is Salesforce's declarative way to connect an org to an outside REST API. An admin or developer registers the API by supplying a machine-readable OpenAPI description of it; Salesforce reads the paths, operations, inputs and responses from that document and exposes each selected operation as an action that Flow and other tools can call, with no hand-written HTTP or JSON code.[^s4][^s3] The same registration also produces type-safe Apex, so code and clicks share one integration definition.[^s2]

## How it works

Registration has three moving parts. First, a named credential holds the endpoint and authentication, so secrets never live in the spec or in flows.[^s3][^s5] Second, the API specification supplies the contract: inputs and outputs, endpoint information, authentication parameters and the operations available on each path, each with parameters and status-code-specific responses.[^s4] Third, the admin selects which operations to activate.[^s3]

In Setup, **Add an External Service** starts a wizard: pick **From API Specification**, name the service, choose the named credential, and point to the schema. A relative URL is appended to the named credential's endpoint to locate the spec; uploading a file or giving an absolute URL are the other recorded options.[^s3][^s1] After selecting operations, the wizard lists the generated actions; for example, a `getAccount` operation becomes an action with an `accountName` input and outputs keyed by response code such as 200.[^s3]

Those actions then appear in the Flow Builder toolbox and can be dropped into screen, autolaunched or record-triggered flows.[^s3] In Apex, objects and operations from the registered spec become classes and methods in the `ExternalService` namespace, and schema types map to strongly typed Apex types, so the compiler catches many mismatches and developers skip the `Http` class and manual JSON parsing.[^s2]

Since Spring '25 the same registrations back **API** agent actions in Agentforce: set up the credential, import the spec (or a MuleSoft service), then create an action of the API type and attach it to topics. Descriptions written in the spec carry over into the action setup.[^s5]

## Metadata and deployment

A registration is stored as the `ExternalServiceRegistration` metadata type (introduced in API 39.0), so it moves between orgs with the rest of the source.[^s1] Key fields include the `schema` itself (OpenAPI 2.0.x or 3.0.x content in JSON or YAML), the `namedCredentialReference`, the list of active `operations`, and a `serviceBinding` that maps unsupported media types to supported ones.[^s1] Since API 66.0, `registrationProviderType` records where the spec came from, with values such as Custom, MuleSoft, Heroku, ApexRest and AgentToAgent.[^s1]

## Limits and gotchas

- A spec must be valid OpenAPI and also meet External Services' own schema rules; an unsupported structure fails to import.[^s4]
- Registration can also fail when the spec exceeds the file-size limit or the cap on total objects or actions, so trim large public APIs to needed operations.[^s4][^s5]
- The 2025 developer blog cites a 10 MB maximum upload size when it advises trimming large specs such as GitHub's.[^s5]
- Spring '23 expanded the limits so large specs register and all operations fit in one registration, and added a Setup page with usage gauges.[^s6]
- The read-only `systemVersion` (currently 9) cannot be upgraded in place; recreate the service from the same spec and repoint references.[^s1]

## When to use it (and when not)

Use External Services when the target API has, or can be given, an OpenAPI description and the consumers are flows, agents or Apex that benefit from typed inputs and outputs.[^s2][^s5] If no spec exists and the payloads are simple JSON, the Flow **HTTP Callout** action generates the external service registration, invocable action and Apex-defined types for you.[^s6] Hand-written Apex callouts with the `Http` class remain the route when you would rather build and parse requests yourself than maintain a spec.[^s2]

## Connections

`kt:external-services` sits under `kt:data-integration` as the declarative, spec-driven path for outbound REST calls.[^s4] It `dependsOn` `kt:named-credentials` for endpoint and authentication.[^s3] It is the low-code `alternativeTo` `kt:apex-callouts`, while its generated Apex keeps code-based callers in sync.[^s2] It is `consumedBy` `kt:flow-http-callout`, whose wizard produces an external service registration, and by `kt:agent-actions` through the API action type.[^s6][^s5] It is `configuredVia` `kt:metadata-api` as `ExternalServiceRegistration`, and its provider types tie it to `kt:mulesoft-anypoint-platform` and `kt:heroku`.[^s1] Its synchronous calls `implements` `kt:integration-patterns-request-reply-fire-and-forget`, and the actions run inside `kt:flow-builder`.[^s3]

## Sources

[^s1]: Salesforce Developers, "ExternalServiceRegistration — Metadata API Developer Guide (Winter '27, API 68.0)". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_externalserviceregistration.htm (accessed 2026-11-13)
[^s2]: Salesforce Developers, "External Services — Apex Developer Guide". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_external_services.htm (accessed 2026-11-13)
[^s3]: Trailhead, "Use External Services with a Flow — Register an External Service". https://trailhead.salesforce.com/content/learn/projects/use-external-services-with-a-flow/register-external-service (accessed 2026-11-13)
[^s4]: Trailhead, "External Services — Define an API Specification for an External Service". https://trailhead.salesforce.com/en/content/learn/modules/external-services/define-a-schema-for-an-external-service (accessed 2026-11-13)
[^s5]: Salesforce Developers Blog, "Call Third-Party APIs from an Agent with External Service Actions" (2025-05-01). https://developer.salesforce.com/blogs/2025/05/call-third-party-apis-from-an-agent-with-external-service-actions (accessed 2026-11-13)
[^s6]: Salesforce Developers Blog, "External Services, API Updates & Learn MOAR in Spring '23" (2023-01-17). https://developer.salesforce.com/blogs/2023/01/external-services-api-updates-learn-moar-spring-23 (accessed 2026-11-13)
