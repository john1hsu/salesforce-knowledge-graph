---
id: kt:invocable-actions-api
type: API
title: Invocable Actions API
aliases: [Invocable Actions resource, Actions REST resource, actions endpoint, Salesforce Actions API, invocable actions REST API]
domain: automation
summary: >-
  The REST API resource under /services/data/vXX.X/actions that lists, describes and runs standard and custom
  invocable actions, such as autolaunched flows, invocable Apex methods, quick actions, email alerts and Chatter
  posts, through one common endpoint and a shared JSON "inputs" request format.
release: "Winter '27"
status: current
broader: [kt:rest-api, kt:process-automation]
related: [kt:autolaunched-flow, kt:subflows, kt:apex, kt:bulkification, kt:prompt-builder, kt:agent-actions]
relations:
  - {predicate: alternativeTo, object: kt:subflows}
  - {predicate: dependsOn, object: kt:flow-versioning}
  - {predicate: consumedBy, object: kt:flow-builder}
sources:
  - id: s1
    title: "Invocable Actions (REST API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-rest/guide/resources-actions-invocable.html
    type: official-docs
    accessed: 2026-11-10
  - id: s2
    title: "Get Custom Invocable Actions (REST API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-rest/guide/resources-actions-invocable-custom-get.html
    type: official-docs
    accessed: 2026-11-10
  - id: s3
    title: "Get Standard Invocable Actions (REST API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.api_rest.meta/api_rest/resources_actions_invocable_standard_get.htm
    type: official-docs
    accessed: 2026-11-10
  - id: s4
    title: "Invoking Actions (Actions Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_action.meta/api_action/actions_intro_invoking.htm
    type: official-docs
    accessed: 2026-11-10
  - id: s5
    title: "Flow Actions (Actions Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.api_action.meta/api_action/actions_obj_flow.htm
    type: official-docs
    accessed: 2026-11-10
  - id: s6
    title: "InvocableMethod Annotation (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_classes_annotation_InvocableMethod.htm
    type: official-docs
    accessed: 2026-11-10
created: 2026-11-10
---

# Invocable Actions API

The **Invocable Actions API** is the part of the Salesforce REST API that exposes *invocable actions*: discrete units of work that applications can call to add behavior, such as posting to Chatter, sending an email, or running a custom process.[^s1] Salesforce splits them into **standard** actions, which exist in every org with predefined inputs and outputs, and **custom** actions, which you define yourself, for example with an Apex method or an autolaunched flow.[^s1][^s2] The resource has been available since REST API version 32.0 and supports GET and HEAD for discovery and POST for invocation.[^s1][^s2]

## How it works

Discovery starts at two collection URIs. `GET /services/data/vXX.X/actions/standard` lists the standard actions available to the caller, including `chatterPost`, `emailSimple`, `submit` (submit for approval) and `activateSessionPermSet`; the documentation warns that some actions require special access.[^s3] `GET /services/data/vXX.X/actions/custom` returns a map of custom action types to their URIs, among them `flow`, `apex`, `quickAction`, `emailAlert`, `sendNotification` and `generatePromptResponse`.[^s2] Each individual action can then be described to learn its inputs and outputs before it is called.[^s1][^s5]

Invocation is a POST to the action's URI, for example `/actions/standard/chatterPost` or `/actions/custom/flow/<FlowApiName>`.[^s4][^s5] Most actions share one body shape: a top-level `inputs` key whose value is an array, with one object of parameters per invocation, so a single request can carry several calls, such as two Chatter posts.[^s4] The response is a JSON array with one result per input, each containing `actionName`, `isSuccess`, `errors` and `outputValues`.[^s4] What `actionName` holds depends on the type: the flow name for a flow, the invocable method name for Apex, `<object>.<action>` for a quick action or email alert, and the prompt template's API name for Generate Prompt Response.[^s4]

## Custom action types in practice

**Flow actions** run an active autolaunched flow in the org, from API version 32.0. Inputs are the flow's input variables, and outputs are its output variables plus `Flow__InterviewStatus`, which reports whether the interview was Created, Started, Finished, in Error or Waiting.[^s5] Invocable Process Builder processes can be called from API version 38.0, but they need an sObject or sObject ID input matching the process's object and return no outputs.[^s5]

**Apex actions** come from methods annotated with `@InvocableMethod`. Only one method per class can carry the annotation; it must be static, public or global, in an outer class, and take at most one parameter, typically a list.[^s6] The same methods are callable natively from REST, Apex, flows, Agentforce agents and bots.[^s6] For Apex inputs sent over REST, the supported primitive types are Blob, Boolean, Date, Datetime, Decimal, Double, ID, Integer, Long, String and Time.[^s2]

## Limits and gotchas

- **Version resolution.** A flow user invoking an autolaunched flow runs its active version, or the latest version if none is active; a flow admin always runs the latest version.[^s2]
- **Access checks.** Describing or invoking an Apex action respects the caller's access to the Apex class and returns an error without it.[^s2][^s6]
- **Email limits.** Email sent through the `emailAlert` action counts against the org's daily workflow email limit.[^s2]
- **Packaging.** Components that actions reference, such as an email alert's template, are not added to a package automatically.[^s2]
- **Bulk contract.** An invocable Apex method must return outputs in the same size and order as its inputs, and should return one result per input even when some fail.[^s6]
- **Removal breaks callers.** Removing `@InvocableMethod` from a class used by a flow causes runtime failures, and in managed packages the method cannot be removed in later versions.[^s2][^s6]
- **Order Management actions.** These should be invoked through the matching Connect REST API resources or ConnectApi methods instead of the generic endpoint.[^s4]

## When to use it (and when not)

Use the Invocable Actions API when an external system needs to trigger business logic that already exists as a flow or invocable Apex, rather than re-implementing that logic in the client or writing a dedicated Apex REST service: admins keep ownership of the flow while integrators get one stable endpoint and a uniform request shape.[^s1][^s5] Inside Salesforce, a flow that wants to reuse another flow normally calls it as a subflow, and Apex can call the same invocable logic directly, so the REST route matters mainly for callers outside the platform.[^s5][^s6] For plain record create, read, update and delete, the REST API's ordinary sObject resources are usually the simpler fit, since no action wrapper is needed.

## Connections

The resource is part of the **REST API** and a mechanism of **process automation**, since its main payloads are **autolaunched flows** and invocable **Apex**.[^s1][^s5][^s6] It is the outside-the-platform alternative to **subflows**, which reach the same autolaunched logic from inside **Flow Builder**, and it depends on **flow versioning** because the version that runs depends on who calls.[^s2] The input/output ordering rule ties it to **bulkification**.[^s6] Because Apex invocable methods also power **Agentforce agent actions** and the `generatePromptResponse` action runs **Prompt Builder** templates, the same building blocks serve AI features.[^s2][^s6]

## Sources

[^s1]: Salesforce Developers, "Invocable Actions (REST API Developer Guide)". https://developer.salesforce.com/docs/platform/api-rest/guide/resources-actions-invocable.html (accessed 2026-11-10)
[^s2]: Salesforce Developers, "Get Custom Invocable Actions (REST API Developer Guide)". https://developer.salesforce.com/docs/platform/api-rest/guide/resources-actions-invocable-custom-get.html (accessed 2026-11-10)
[^s3]: Salesforce Developers, "Get Standard Invocable Actions (REST API Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.264.0.api_rest.meta/api_rest/resources_actions_invocable_standard_get.htm (accessed 2026-11-10)
[^s4]: Salesforce Developers, "Invoking Actions (Actions Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.api_action.meta/api_action/actions_intro_invoking.htm (accessed 2026-11-10)
[^s5]: Salesforce Developers, "Flow Actions (Actions Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.264.0.api_action.meta/api_action/actions_obj_flow.htm (accessed 2026-11-10)
[^s6]: Salesforce Developers, "InvocableMethod Annotation (Apex Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_classes_annotation_InvocableMethod.htm (accessed 2026-11-10)
