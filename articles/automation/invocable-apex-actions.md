---
id: kt:invocable-apex-actions
type: Feature
title: Invocable Apex Actions
aliases: [custom invocable actions, InvocableMethod, "@InvocableMethod", InvocableVariable, Apex actions in Flow, invocable Apex methods]
domain: automation
summary: >-
  Apex methods marked with the @InvocableMethod annotation, with inputs and outputs exposed through
  @InvocableVariable members, so that flows, agents, Apex and the REST API can call custom code as a
  reusable, bulk-aware action.
release: "Winter '27"
status: current
broader: [kt:process-automation, kt:apex]
related: [kt:bulkification, kt:second-generation-managed-packages]
relations:
  - {predicate: consumedBy, object: kt:flow-builder}
  - {predicate: consumedBy, object: kt:agent-actions}
  - {predicate: consumedBy, object: kt:invocable-actions-api}
  - {predicate: dependsOn, object: kt:permission-sets}
  - {predicate: coveredBy, object: kt:platform-developer-certification}
sources:
  - id: s1
    title: "InvocableMethod Annotation (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_classes_annotation_InvocableMethod.htm
    type: official-docs
    accessed: 2026-11-14
  - id: s2
    title: "InvocableVariable Annotation (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_classes_annotation_InvocableVariable.htm
    type: official-docs
    accessed: 2026-11-14
  - id: s3
    title: "Get Ready to Create an Apex Action (Trailhead: Agent Customization with Apex)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agent-customization-with-apex/get-ready-to-create-an-apex-action
    type: official-learning
    accessed: 2026-11-14
  - id: s4
    title: "Get to Know Automation Comps (Trailhead Quick Start)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/quick-start-explore-the-automation-comps-sample-app/get-to-know-automation-comps
    type: official-learning
    accessed: 2026-11-14
  - id: s5
    title: "Salesforce Certified Platform Developer Exam Guide"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298965&type=1&language=en_US
    type: official-learning
    accessed: 2026-11-14
created: 2026-11-14
---

# Invocable Apex Actions

An **invocable Apex action** is an Apex method annotated with `@InvocableMethod`, which turns it into an action that flows, Apex, the REST API, Agentforce agents and bots can call. Its inputs and outputs are dynamic and can be discovered with describe calls.[^s1] It is the standard way for developers to put logic that is too complex for Flow Builder's declarative elements into a reusable building block that admins then drag onto the canvas like any other action.[^s4]

## How it works

The annotated method must be `static` and either `public` or `global`, and it must live in an outer class. Only one method per class may carry the annotation, and `Deprecated` is the only other annotation it can be combined with.[^s1] The method takes at most one parameter and may return nothing or a value of a supported type.[^s1] Supported input and output types are lists (or lists of lists) of primitives, of a specific sObject type, of the generic sObject, or of a user-defined Apex class; the generic `Object` type is not allowed.[^s1]

A user-defined request or response class exposes its fields through `@InvocableVariable`. Those members must be `public` or `global` instance variables; static, local, `final`, `private` and `protected` variables and properties cannot be invocable variables. The Apex variable name must match the name the flow uses, and the match is case-sensitive.[^s2] From API version 66.0, a class used for invocable parameters also needs a visible no-argument constructor.[^s2]

Optional modifiers shape how the action appears to admins. On the method, `label`, `description`, `category` and `iconName` control its name, help text, grouping and canvas icon in Flow Builder; `callout=true` declares that it calls an external system; `configurationEditor` registers a custom property editor; and `capabilityType` ties it to a capability such as a prompt template type.[^s1] On variables, `label`, `description`, `required`, `placeholderText` and `defaultValue` play the same role, and `required` cannot be combined with `defaultValue`.[^s2]

## Bulk behavior and error handling

An invocable method receives a list and must return a list of the same size and order: the i-th output answers the i-th input. This is what lets an Apex action run in bulk inside a record-triggered flow.[^s1] The method must return one result per input even when some fail, so the documented pattern is to wrap each result in an object that reports success or failure rather than throwing for the whole batch.[^s1]

## Agentforce and security

The same annotation exposes the method to Agentforce. Trailhead explains that the method's `label` and `description` become the agent action's label and instructions, and each variable's `description`, `required` flag and Apex type become its input or output instructions, required setting and data type, so clear descriptions directly affect how the agent plans.[^s3] Trailhead also recommends wrapping existing service logic in a separate invocable class rather than annotating the service itself.[^s3] The running user, or the agent's user, needs access to the Apex class through a profile or permission set; Trailhead names missing permissions as a main reason agent actions fail.[^s1][^s3]

## Limits and gotchas

- One annotated method per class, at most one input parameter, and no generic `Object` type.[^s1]
- `List<List<sObject>>` works only as a direct return type; as an invocable variable inside a class it causes a runtime error.[^s1]
- Once a package includes an invocable method, later package versions cannot remove it. Only `global` methods and variables are visible in Flow Builder in a subscriber org.[^s1][^s2]
- Input and output lists that differ in size or order break bulk execution, so never drop failed rows from the output.[^s1]

## Connections

Invocable Apex actions sit under **process automation** and **Apex**: they are the bridge that lets declarative automation call code. The Platform Developer exam guide asks candidates to combine declarative features with Apex and to use Apex with Flow, which is the scenario this feature serves, hence the `coveredBy` edge.[^s5] They are **consumed by Flow Builder** as Apex actions, by **agent actions** in Agentforce, and by the **Invocable Actions API**, which lets external REST clients call them. They **depend on permission sets** (or profiles) for Apex class access. Their list-in, list-out contract applies **bulkification** to flows, and their packaging rules matter when they ship in **second-generation managed packages**.

## Sources

[^s1]: Salesforce Developers, "InvocableMethod Annotation (Apex Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_classes_annotation_InvocableMethod.htm (accessed 2026-11-14)
[^s2]: Salesforce Developers, "InvocableVariable Annotation (Apex Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_classes_annotation_InvocableVariable.htm (accessed 2026-11-14)
[^s3]: Trailhead, "Get Ready to Create an Apex Action" (Agent Customization with Apex). https://trailhead.salesforce.com/content/learn/modules/agent-customization-with-apex/get-ready-to-create-an-apex-action (accessed 2026-11-14)
[^s4]: Trailhead, "Get to Know Automation Comps" (Quick Start). https://trailhead.salesforce.com/content/learn/projects/quick-start-explore-the-automation-comps-sample-app/get-to-know-automation-comps (accessed 2026-11-14)
[^s5]: Salesforce Help, "Salesforce Certified Platform Developer Exam Guide". https://help.salesforce.com/s/articleView?id=005298965&type=1&language=en_US (accessed 2026-11-14)
