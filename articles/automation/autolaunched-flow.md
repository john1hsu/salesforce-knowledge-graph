---
id: kt:autolaunched-flow
type: Feature
title: Autolaunched Flow
aliases: [autolaunched flow (no trigger), no-trigger flow, headless flow]
domain: automation
summary: >-
  The Flow Builder flow type that has no trigger of its own and no screens: it runs in the background only when
  something else starts it, such as a parent flow's Subflow element, Apex, a custom button, an Agentforce action
  or a REST API call.
release: "Winter '27"
status: current
broader: [kt:flow-builder, kt:process-automation]
related: [kt:screen-flow, kt:record-triggered-flow, kt:flow-orchestrator, kt:schedule-triggered-flow, kt:platform-event-triggered-flow]
relations:
  - {predicate: integratesWith, object: kt:apex}
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: usedBy, object: kt:agentforce}
  - {predicate: queriedWith, object: kt:invocable-actions-api}
sources:
  - id: s1
    title: "Autolaunched and Scheduled Flows: Get Started with Autolaunched Flows"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/autolaunched-scheduled-flows/get-started-with-autolaunched-flows
    type: official-learning
    accessed: 2026-11-01
  - id: s2
    title: "Apex Reference Guide: Interview Class"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/flow_interview_class.htm
    type: official-docs
    accessed: 2026-11-01
  - id: s3
    title: "Actions Developer Guide: Flow Actions"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_action.meta/api_action/actions_obj_flow.htm
    type: official-docs
    accessed: 2026-11-01
  - id: s4
    title: "Per-Transaction Flow Limits"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=platform.flow_considerations_limit_transaction.htm
    type: official-docs
    accessed: 2026-11-01
  - id: s5
    title: "What Is a Subflow?"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2023/what-is-a-subflow
    type: official-blog
    accessed: 2026-11-01
created: 2026-11-01
---

# Autolaunched Flow

An autolaunched flow, labelled **Autolaunched Flow (No Trigger)** in Flow Builder, is a flow with no trigger defined inside it and no user interaction: it does nothing until something else starts it, which gives the caller full control over when it runs.[^s1] Trailhead draws a careful distinction. Lower-case "autolaunched" describes any flow that runs in the background, which also covers record-triggered, schedule-triggered and platform event-triggered flows; capital-A "Autolaunched" means only the no-trigger type this node describes.[^s1] It is the reusable, headless building block of Flow: the place to put logic that several flows, Apex classes, buttons, agents or external systems should share.

## How it is launched

Trailhead lists the main entry points:[^s1]

- **Another flow**, through a Subflow element in the parent.[^s1]
- **A custom button** on a page layout, optionally with visibility criteria. Actions look like buttons but can only call screen flows, so a screenless flow needs a custom button instead.[^s1]
- **Agentforce**, by wrapping the flow in an agent action and assigning it to the org's active agent.[^s1]
- **Other automation**: Apex, a Visualforce page, Flow Orchestration, or an API call from an external system.[^s1]

From **Apex**, developers instantiate the flow through the `Flow.Interview` class, either statically (`Flow.Interview.flowName`, which Salesforce recommends) or dynamically with `createInterview()`, passing a map of input-variable values. `start()` then runs it; this method works only with Autolaunched and User Provisioning flows. `getVariableValue()` reads output afterwards and returns null if the variable isn't found. A flow user runs the active version (or the latest, if none is active), while a flow admin always runs the latest version.[^s2]

From **outside Salesforce**, the Flow Actions REST resource invokes an active autolaunched flow at `/services/data/vXX.X/actions/custom/flow/<FlowApiName>` (API 32.0 or later). Inputs map to the flow's input variables, and the response returns the flow's output variables plus `Flow__InterviewStatus`.[^s3]

## Inputs, outputs and reuse as a subflow

Data crosses the flow boundary only through variables. Variables that receive data from a caller must be marked **Available for input**, and the parent passes values through the Subflow element's input and output assignments.[^s5] Both autolaunched and screen flows can be called as subflows, but record-triggered flows cannot be referenced from another flow. That is why shared logic such as error logging is usually factored into an autolaunched flow that many parents call.[^s5] The Admins blog sums up the benefit: change the subflow once, and the parents that use it don't need editing or redeploying.[^s5]

## Limits and gotchas

- **It shares the caller's transaction.** An autolaunched flow runs inside the transaction that launched it, such as an Apex call, and draws on the same governor limits.[^s4] Per transaction that means 100 SOQL queries, 50,000 records retrieved, 150 DML statements, 10,000 records processed by DML, and 10,000 ms of CPU time.[^s4]
- **Limit breaches roll back everything.** If an element exceeds a limit, the whole transaction rolls back, even when that element has a fault connector.[^s4]
- **Wait elements split transactions.** A flow that pauses ends its transaction. When it resumes, it runs in a batch transaction with other resumed interviews that share its user, execution time and flow version.[^s4]
- **Sharing from Apex.** To make a flow started from Apex enforce the running user's sharing rules, use API 62.0 or later and declare the class `with sharing`. Queries may then return fewer rows, and some operations can fail on permissions.[^s2]
- **Dynamic creation hides dependencies.** A flow referenced only through `createInterview()` must be added to a package by hand, and deleting the flow isn't checked against those references. A missing flow throws a `TypeException` at runtime.[^s2]
- **Spotting the type in Setup.** The All Flows list shows only the process type, so add the Trigger column. An Autolaunched Flow with a blank trigger is the no-trigger type.[^s1]

## When to use it (and when not)

Choose an autolaunched flow when logic must run without user input and the caller decides when it runs: reusable subflows, button-driven background jobs, agent actions, and admin-maintained logic that Apex or an integration invokes.[^s1][^s5] If a person must enter or confirm data, use a screen flow. If the logic should fire on a record change, a schedule or a platform event, use the matching triggered flow type, which has its trigger built in.[^s1]

## Connections

Autolaunched flow is a flow type built in **Flow Builder** and part of the broader **process-automation** toolset.[^s1] Its siblings are the **screen flow**, which adds user interaction, and the **record-triggered flow**, which owns its trigger. It is also one of the callers and callees in **Flow Orchestrator**.[^s1][^s5] It **integrates with Apex** through the `Flow.Interview` class.[^s2] External systems can start it through the **invocable actions** REST resource.[^s3] It is **governed by** the same per-transaction **governor limits** as the code that calls it.[^s4] **Agentforce** uses it as the implementation behind flow-based agent actions.[^s1]

## Sources

[^s1]: Trailhead, "Autolaunched and Scheduled Flows: Get Started with Autolaunched Flows". https://trailhead.salesforce.com/content/learn/modules/autolaunched-scheduled-flows/get-started-with-autolaunched-flows (accessed 2026-11-01)
[^s2]: Salesforce Developers, "Apex Reference Guide: Interview Class". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/flow_interview_class.htm (accessed 2026-11-01)
[^s3]: Salesforce Developers, "Actions Developer Guide: Flow Actions". https://developer.salesforce.com/docs/atlas.en-us.api_action.meta/api_action/actions_obj_flow.htm (accessed 2026-11-01)
[^s4]: Salesforce Help, "Per-Transaction Flow Limits". https://help.salesforce.com/apex/HTViewHelpDoc?id=platform.flow_considerations_limit_transaction.htm (accessed 2026-11-01)
[^s5]: Salesforce Admins Blog, "What Is a Subflow?". https://admin.salesforce.com/blog/2023/what-is-a-subflow (accessed 2026-11-01)
