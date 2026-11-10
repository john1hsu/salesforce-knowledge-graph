---
id: kt:flow-trigger-explorer
type: Tool
title: Flow Trigger Explorer
aliases: [Flow Trigger Explorer tool, flow trigger order explorer]
domain: automation
summary: >-
  A Setup tool that lists every record-triggered flow (and record-triggered orchestration) that runs for a chosen
  object and trigger event, grouped by when it runs, and lets admins inspect versions, activate or deactivate them
  and drag-and-drop the run order of before-save and after-save flows.
release: "Winter '27"
status: current
broader: [kt:flow-builder]
related: [kt:record-triggered-flow, kt:order-of-execution, kt:flow-orchestrator, kt:workflow-rules, kt:process-builder]
relations:
  - {predicate: dependsOn, object: kt:order-of-execution}
  - {predicate: partOf, object: kt:process-automation}
sources:
  - id: s1
    title: "Meet Flow Trigger Explorer (Record-Triggered Flows module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/record-triggered-flows/meet-flow-trigger-explorer
    type: official-learning
    accessed: 2026-11-05
  - id: s2
    title: "Define the Run Order of Record-Triggered Flows for an Object"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=platform.flow_task_trigger_run_order.htm
    type: official-docs
    accessed: 2026-11-05
  - id: s3
    title: "Introducing Flow Trigger Explorer: View All Your Triggered Automation in One Place"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2022/introducing-flow-trigger-explorer-view-all-your-triggered-automation-in-one-place
    type: official-blog
    accessed: 2026-11-05
  - id: s4
    title: "Use Flow Trigger Explorer to Easily View All of Your Record-Triggered Flows"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2022/use-flow-trigger-explorer-to-easily-view-all-of-your-record-triggered-flows
    type: official-blog
    accessed: 2026-11-05
created: 2026-11-05
---

# Flow Trigger Explorer

Flow Trigger Explorer is a visual, interactive Setup tool for managing record-triggered automation on one object at a time. Pick an object and a trigger event, and it shows every flow that will run when a record is created, updated or deleted. You can review those flows, open their versions, and change the order in which they run.[^s1] It also lists record-triggered orchestrations alongside flows.[^s1][^s3] Salesforce introduced it in the Spring '22 release. The Flow product team described it as a bird's-eye view of an object's triggered automation, a counterpart to the per-flow view inside Flow Builder.[^s3]

## How it works

There are three ways to open the explorer. Inside a record-triggered flow, use the link at the bottom of the Start element, which opens the explorer for that flow's object. In Object Manager, open the object's Flow Triggers page. Or use the Flow Trigger Explorer button next to New Flow on the Flows setup page.[^s1] The screen has three areas:[^s1]

- **Object and trigger selector.** Choose the object and the event (Created, Updated or Deleted). You can filter the list by criteria such as status and process type.[^s1]
- **Categorized flows.** Flows are grouped by when they execute: before save, after save, asynchronously, or on a scheduled path. Within each group they appear in run order.[^s1]
- **Status and details panel.** Opened from a flow's dropdown, it shows the flow's details (name, description, version, status, last modified by, process type and trigger). It also lists every version, each with buttons to open it in Flow Builder or to activate or deactivate it.[^s1]

To reorder, click **Edit Order** in a section, drag flows into place by their handles, and click **Update**. Moved flows are highlighted, and you don't need to open each flow. Keyboard users can pick up a flow with the spacebar, move it with the arrow keys, drop it with the spacebar again, and cancel with Esc.[^s1] The explorer and the per-flow setting edit the same thing: each flow's **Trigger Order** property, which admins can also set in the flow's advanced or version properties.[^s2][^s3]

## Limits and gotchas

The trigger order the explorer manages follows rules set in Salesforce Help:[^s2]

- Values range from 1 to 2,000 and apply only to before-save and after-save flows. Flows numbered 1–1,000 run first in ascending order. Flows with no value run next, ordered by activation date. Flows numbered 1,001–2,000 run last. Flows that share a value run alphabetically by API name.
- Ordering only compares flows on the same object with the same trigger type. It can't override the order of execution: an after-save flow will never run ahead of a before-save flow or an Apex trigger, whatever its number.
- Order values have no effect on asynchronous or scheduled paths. Trailhead adds that flows in the Run Asynchronously group can't be guaranteed to run in the listed order.[^s2][^s1]
- Activating, deactivating or reordering one flow can automatically shift the order of others, so review the whole section after any change.[^s2]
- Flows created in Winter '22 or earlier have no order value until you assign one, so they fall into the activation-date band.[^s2]
- The explorer doesn't show individual pending runs of scheduled paths. Use the Time-Based Automations setup page to see and delete those queued instances.[^s1]

Help recommends leaving gaps between values (10, 20, 30, or 100, 200, 300) so new flows can go in later without renumbering.[^s2]

## When to use it (and when not)

Use the explorer when an object has several record-triggered flows and you need to know what will fire, and in what sequence, before you add or change automation. It is the quickest way to audit an object during a migration from workflow rules or Process Builder. It is also where you set run order without merging separate automations into one large flow. Salesforce gave that as the reason for shipping trigger ordering and the explorer together.[^s3][^s4] When a sequencing problem crosses the boundary between flows and code, the explorer alone is not enough. Its ordering sits inside the platform's order of execution, so reason about Apex triggers and other save-time steps with that sequence instead.[^s2]

## Connections

Flow Trigger Explorer is a management surface around **Flow Builder** and exists to manage **record-triggered flows**. It shows their before-save, after-save, asynchronous and scheduled paths, and it also lists **Flow Orchestrator** record-triggered orchestrations.[^s1][^s3] The order values it edits are **governed by the order of execution**, which fixes where each category of flow runs relative to Apex triggers and other save steps.[^s2] Teams retiring **workflow rules** and **Process Builder** use it to see the flows that replace them in one place. The Admins blog positioned it as part of that consolidation onto Flow, inside the broader **process-automation** toolset.[^s3][^s4]

## Sources

[^s1]: Trailhead, "Meet Flow Trigger Explorer (Record-Triggered Flows module)". https://trailhead.salesforce.com/content/learn/modules/record-triggered-flows/meet-flow-trigger-explorer (accessed 2026-11-05)
[^s2]: Salesforce Help, "Define the Run Order of Record-Triggered Flows for an Object". https://help.salesforce.com/apex/HTViewHelpDoc?id=platform.flow_task_trigger_run_order.htm (accessed 2026-11-05)
[^s3]: Salesforce Admins Blog, "Introducing Flow Trigger Explorer: View All Your Triggered Automation in One Place". https://admin.salesforce.com/blog/2022/introducing-flow-trigger-explorer-view-all-your-triggered-automation-in-one-place (accessed 2026-11-05)
[^s4]: Salesforce Admins Blog, "Use Flow Trigger Explorer to Easily View All of Your Record-Triggered Flows". https://admin.salesforce.com/blog/2022/use-flow-trigger-explorer-to-easily-view-all-of-your-record-triggered-flows (accessed 2026-11-05)
