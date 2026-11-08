---
id: kt:subflows
type: Feature
title: Subflows
aliases: [subflow, Subflow element, child flow, referenced flow, flow within a flow]
domain: automation
summary: >-
  The Flow Builder mechanism, exposed as the Subflow element, by which a parent flow launches another active
  autolaunched or screen flow at runtime, passing data in and out through variables marked available for input
  and output, so shared logic lives in one reusable child flow.
release: "Winter '27"
status: current
broader: [kt:flow-builder, kt:process-automation]
related: [kt:autolaunched-flow, kt:screen-flow, kt:record-triggered-flow, kt:flow-fault-handling, kt:custom-metadata-types, kt:prompt-builder]
relations:
  - {predicate: dependsOn, object: kt:flow-versioning}
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: alternativeTo, object: kt:invocable-actions-api}
sources:
  - id: s1
    title: "Flow Element: Subflow"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_subflow.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-08
  - id: s2
    title: "Build Flows with Logic: Run a Flow Within a Flow"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/flow-build-logic/run-flow-within-flow
    type: official-learning
    accessed: 2026-11-08
  - id: s3
    title: "What Is a Subflow?"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2023/what-is-a-subflow
    type: official-blog
    accessed: 2026-11-08
  - id: s4
    title: "Per-Transaction Flow Limits"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=platform.flow_considerations_limit_transaction.htm
    type: official-docs
    accessed: 2026-11-08
  - id: s5
    title: "Considerations for Record-Triggered Flows"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=platform.flow_considerations_trigger_record.htm
    type: official-docs
    accessed: 2026-11-08
created: 2026-11-08
---

# Subflows

A **subflow** is a flow that another flow, the *parent*, calls at runtime through a **Subflow** element. Salesforce Help calls the flow being launched the *referenced flow*; it must be an active flow in the same org.[^s1] The point is reuse: logic that several automations need, such as assigning a task, adjusting permission set membership or sending a failure notice, is built once in a child flow and referenced from every parent instead of being copied into each.[^s2][^s3]

## How it works

The child flow's variables define its interface. A variable marked **Available for input** can receive a value from the parent, and one marked **Available for output** hands a value back when the child finishes. In the parent, the Subflow element shows a *Set Input Values* section only if the child declares inputs, and *Store Output Values* maps outputs into the parent's own variables.[^s2][^s1] Inputs are assigned at the moment of the call and outputs when the referenced flow completes. The child cannot see the parent's triggering record, so the parent must pass anything the child needs, typically a record ID or the record itself.[^s1][^s2]

Which flows can be referenced depends on the caller. Trailhead describes the Subflow element as referencing autolaunched flows and screen flows.[^s2] An autolaunched flow, however, cannot reference a screen flow, since nobody is there to see the screens.[^s1][^s5] Prompt flows gained the Subflow element at API version 62.0 and can call autolaunched flows from API version 63.0.[^s1] A flow that contains a Wait element cannot be referenced at all.[^s1]

## Versions

A Subflow element points at a flow, not at a fixed version. For API version 61.0 and later, screen flows and record-triggered flows call the referenced flow's active version, falling back to its latest version when none is active; screen flows on earlier API versions call the latest version by default.[^s1] Calling a flow with no active version works only for flow admins; for other users the call fails at runtime.[^s1][^s2] While debugging, you can force parents to run the latest version of every referenced flow with a debug option or by adding `?latestSub=true` to the parent's Flow Builder URL.[^s1]

Because parents resolve the child at runtime, a change to an activated child takes effect in every parent without editing or redeploying them. That is the maintenance win, and also the risk: one careless change ripples everywhere, so test the child thoroughly before activating a new version.[^s3]

## Limits and gotchas

- A subflow is not a separate transaction. Autolaunched flows run inside the transaction that launched them and share its limits: 100 SOQL queries, 150 DML statements, 10,000 records processed by DML and 10,000 ms of CPU time. If any limit is exceeded, the entire transaction rolls back, even when a fault connector is present.[^s4]
- Before-save record-triggered flows support only Assignment, Decision, Get Records and Loop elements, so they cannot call subflows; put that logic in an after-save flow.[^s5]
- Input and output variable API names longer than 40 characters cause a save error in the calling flow, and a null passed into a non-collection text, picklist or multi-select picklist input arrives as an empty string.[^s1]
- Flow Builder doesn't show variable descriptions in the Subflow element, so document the child's contract elsewhere.[^s1]

## When to use it (and when not)

Use a subflow for small, generic, reusable steps: Salesforce suggests utility flows such as address handling or payment authorization.[^s1] A common pattern is an error-handling subflow called from the fault connectors of Get, Create and Update Records elements, with configuration such as the alert address kept in a custom metadata type rather than hard-coded.[^s3] Avoid using subflows simply to hide a very large flow's complexity across many layers, and don't treat them as a way around governor limits, because the work still counts against the caller's transaction.[^s4]

## Connections

Subflows are a building block of **Flow Builder** and of **process automation** generally. The callable children are usually **autolaunched flows**, sometimes **screen flows**, and parents are often **record-triggered flows** in after-save mode.[^s1][^s5] Error-handling subflows pair with **flow fault handling** and **custom metadata types**.[^s3] Prompt flows in **Prompt Builder** can also call them.[^s1] Version resolution ties subflows to flow versioning, and shared transactions put them under **governor limits**.[^s1][^s4] For callers outside Flow, such as Apex or integrations, the invocable actions route is the alternative way to reach the same autolaunched logic.

## Sources

[^s1]: Salesforce Help, "Flow Element: Subflow". https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_subflow.htm&language=en_US&type=5 (accessed 2026-11-08)
[^s2]: Trailhead, "Build Flows with Logic: Run a Flow Within a Flow". https://trailhead.salesforce.com/content/learn/modules/flow-build-logic/run-flow-within-flow (accessed 2026-11-08)
[^s3]: Salesforce Admins Blog, "What Is a Subflow?". https://admin.salesforce.com/blog/2023/what-is-a-subflow (accessed 2026-11-08)
[^s4]: Salesforce Help, "Per-Transaction Flow Limits". https://help.salesforce.com/apex/HTViewHelpDoc?id=platform.flow_considerations_limit_transaction.htm (accessed 2026-11-08)
[^s5]: Salesforce Help, "Considerations for Record-Triggered Flows". https://help.salesforce.com/apex/HTViewHelpDoc?id=platform.flow_considerations_trigger_record.htm (accessed 2026-11-08)
