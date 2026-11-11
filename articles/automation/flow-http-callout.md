---
id: kt:flow-http-callout
type: Feature
title: HTTP Callout in Flow
aliases: [Flow HTTP Callout, HTTP Callout action, Create HTTP Callout, declarative HTTP callout]
domain: automation
summary: >-
  A Flow Builder action that lets admins call an external JSON-based HTTP API without code: a guided wizard captures a
  named credential, method, path and sample payloads, then generates a reusable External Services registration,
  invocable action and Apex-defined types.
release: "Winter '27"
status: current
broader: [kt:flow-builder, kt:data-integration]
related: [kt:autolaunched-flow, kt:screen-flow, kt:record-triggered-flow, kt:flow-fault-handling, kt:flow-tests]
relations:
  - {predicate: dependsOn, object: kt:named-credentials}
  - {predicate: dependsOn, object: kt:external-services}
  - {predicate: alternativeTo, object: kt:apex-callouts}
  - {predicate: implements, object: kt:integration-patterns-request-reply-fire-and-forget}
  - {predicate: consumedBy, object: kt:invocable-actions-api}
sources:
  - id: s1
    title: "Connecting to an API Without a Connector Using HTTP Callout"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.flow_http_callout.htm&type=5
    type: official-docs
    accessed: 2026-11-11
  - id: s2
    title: "Configure an HTTP Callout Action"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.flow_http_callout_configure.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-11
  - id: s3
    title: "Callouts and Callbacks: Limits and Usage"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=external_services_schema_def_usage_considerations.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-11
  - id: s4
    title: "Easy Integrations with Flow HTTP Callouts"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2023/integrations-are-easier-than-ever-with-flow-http-callouts
    type: official-blog
    accessed: 2026-11-11
  - id: s5
    title: "Maintain Your Integration Architect Certification for Winter '24"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-architect-certification-maintenance-winter-24/maintain-your-integration-architect-certification-for-winter-24
    type: official-learning
    accessed: 2026-11-11
  - id: s6
    title: "Quick Start: Create HTTP Callouts with Flow Builder — Build the HTTP Callout Flow"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/quick-start-create-http-callouts-with-flow-builder/build-the-http-callout-flow
    type: official-learning
    accessed: 2026-11-11
created: 2026-11-11
---

# HTTP Callout in Flow

**HTTP Callout** is a Flow Builder action that connects a flow to an external HTTP-based API without Apex or middleware, so response data can drive later flow logic.[^s1] Behind the guided setup sits External Services: each HTTP Callout produces an external service registration with an invocable action, so the action can be reused in other flows and elsewhere in the org.[^s1] Unlike registering an external service from Setup, it needs no OpenAPI specification; Flow infers the schema from sample JSON.[^s4] Salesforce's example uses include address lookups from a map API in a screen flow, checking a payment processor's status by invoice number, and pushing leads to a marketing tool.[^s1]

## How it works

Authentication is set up first. The admin creates an external credential (the authentication protocol), a principal granted to users through a permission set, and a named credential holding the base URL.[^s4] Building the credentials and the action requires the Customize Application permission.[^s2]

In Flow Builder, the admin adds an Action element and clicks **Create HTTP Callout**.[^s2] The wizard then asks for:

- An external service name (letters and digits only, no spaces), a description and the named credential, from which the base URL is filled in.[^s2]
- An action label, the HTTP method, and an endpoint path that starts with a slash, has no question mark, and marks path variables in curly brackets.[^s2]
- Optional query parameter keys, each with a data type, a required flag and a description.[^s2]
- A sample JSON request body for POST, PUT, PATCH and DELETE, and a sample JSON response; Salesforce generates an Apex data structure from each, whose types can be corrected.[^s2]

Instead of pasting a response, the Trailhead quick start uses **Connect for Schema**, which calls the endpoint and derives the data structure from the live reply.[^s6] Saving creates the external service and the action, which appears in the flow's Actions list.[^s2] Generated classes follow a naming scheme such as `<Service>__<Label>_IN_body` for request bodies and `<Service>__<Label>_OUT_2XX` for success responses, and deleting the external service deletes those classes.[^s2]

At run time, an Assignment element fills an Apex-defined request variable before the call, and a Transform element can map between Salesforce records and the external shape.[^s2] Outputs are grouped by response code; the Salesforce Admins team suggests a Decision element that checks for a 2XX result before using the data.[^s4]

## Evolution

GET reached general availability in Summer '23, with POST in beta at the time.[^s4] In Winter '24 the declarative editor gained POST, PUT, PATCH and DELETE, which previously required hand-editing the generated API specification.[^s5] Current help documentation lists all five methods as options in the wizard.[^s2]

## Limits and gotchas

- **JSON only.** The feature supports APIs that answer with JSON, and request and response shapes come from the samples you supply.[^s4]
- **Sample quality matters.** A sample that omits a decimal can make a number look like an integer; check inferred types against the API docs.[^s4]
- **Timeout.** External Services callouts time out after 120 seconds.[^s3]
- **No uncommitted work.** A callout cannot run while uncommitted changes are pending; in Flow, Salesforce advises ending the transaction with a Pause element first.[^s3]
- **No async callbacks in Flow.** External Services callback operations work from Apex, not from Flow.[^s3]
- **Shared limits.** API requests and external service registrations count toward org-wide limits.[^s4]
- **Editions.** It is a Lightning Experience feature in Enterprise, Performance, Unlimited and Developer editions.[^s5]

## When to use it (and when not)

Use HTTP Callout when an admin needs a few REST/JSON operations from a well-documented API and wants the result to be reusable across flows.[^s1] Salesforce stresses picking a well-documented API, because inaccurate field definitions make debugging slow.[^s2] When the provider publishes an OpenAPI spec, registering it through External Services captures many operations at once.[^s4] Choose Apex callouts when the integration needs callbacks, custom parsing, or non-JSON payloads, since those fall outside what Flow supports.[^s3][^s4]

## Connections

HTTP Callout is a guided extension of **Flow Builder** and a no-code route to **data integration**.[^s1] It depends on **Named Credentials** for the endpoint and authentication, and on **External Services**, which it generates; the result is exposed as an invocable action like those in the **Invocable Actions API**.[^s1][^s4] It typically implements the synchronous **request-reply** integration pattern and is the declarative **alternative to Apex callouts**, which remain the route for callbacks and non-JSON payloads.[^s3][^s4] It is added to **autolaunched** and **screen flows** like any other action, and in **record-triggered flows** it must respect the rule against callouts with uncommitted work.[^s3][^s6] Because outputs are grouped by response code, the flow itself decides how to treat non-2XX replies, alongside the usual **fault handling** and **Flow Tests** that apply to any flow action.[^s4]

## Sources

[^s1]: Salesforce Help, "Connecting to an API Without a Connector Using HTTP Callout". https://help.salesforce.com/s/articleView?language=en_US&id=platform.flow_http_callout.htm&type=5 (accessed 2026-11-11)
[^s2]: Salesforce Help, "Configure an HTTP Callout Action". https://help.salesforce.com/s/articleView?id=sf.flow_http_callout_configure.htm&language=en_US&type=5 (accessed 2026-11-11)
[^s3]: Salesforce Help, "Callouts and Callbacks: Limits and Usage". https://help.salesforce.com/s/articleView?id=external_services_schema_def_usage_considerations.htm&language=en_US&type=5 (accessed 2026-11-11)
[^s4]: Salesforce Admins Blog, "Easy Integrations with Flow HTTP Callouts". https://admin.salesforce.com/blog/2023/integrations-are-easier-than-ever-with-flow-http-callouts (accessed 2026-11-11)
[^s5]: Trailhead, "Maintain Your Integration Architect Certification for Winter '24". https://trailhead.salesforce.com/content/learn/modules/salesforce-architect-certification-maintenance-winter-24/maintain-your-integration-architect-certification-for-winter-24 (accessed 2026-11-11)
[^s6]: Trailhead, "Quick Start: Create HTTP Callouts with Flow Builder — Build the HTTP Callout Flow". https://trailhead.salesforce.com/content/learn/projects/quick-start-create-http-callouts-with-flow-builder/build-the-http-callout-flow (accessed 2026-11-11)
