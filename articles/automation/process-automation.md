---
id: kt:process-automation
type: Concept
title: Process Automation
aliases: [Salesforce process automation, business process automation, Salesforce automation tools]
domain: automation
summary: >-
  The umbrella for the Salesforce tools that run business logic without manual steps: Flow (the main
  declarative tool), approval processes, orchestration, and Apex for code-based automation. Choosing
  between them depends on automation density.
release: "Winter '27"
status: concept
broader: [kt:salesforce-platform]
related: [kt:flow-builder, kt:flow-orchestrator, kt:apex-triggers, kt:order-of-execution]
relations:
  - {predicate: hasPart, object: kt:approval-processes}
  - {predicate: governedBy, object: kt:governor-limits}
sources:
  - id: s1
    title: "Record-Triggered Automation Decision Guide"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/decision-guides/guide/record-triggered
    type: official-docs
    accessed: 2026-11-01
  - id: s2
    title: "Record-Triggered Automation: Apex or Flow?"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/record-triggered-automation-apex-or-flow
    type: official-blog
    accessed: 2026-11-01
  - id: s3
    title: "Automate Business Processes (trail)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/trails/automate_business_processes
    type: official-learning
    accessed: 2026-11-01
  - id: s4
    title: "Business Process Automation: Customize How Records Get Approved"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/business_process_automation/approvals
    type: official-learning
    accessed: 2026-11-01
  - id: s5
    title: "Planning Your Switch to Flow Builder"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.flow_migrate_to_flow_best_practices.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-01
  - id: s6
    title: "Go with the Flow: What's Happening with Workflow Rules and Process Builder?"
    publisher: Salesforce Admins
    url: https://admin.salesforce.com/blog/2021/go-with-the-flow-whats-happening-with-workflow-rules-and-process-builder
    type: official-blog
    accessed: 2026-11-01
created: 2026-11-01
---

# Process Automation

Process automation in Salesforce is the family of platform features that carry out business logic on their own, such as updating fields, creating related records, routing work for approval, notifying people or calling other systems, so users do not have to do these steps by hand. Salesforce's own learning path for the topic covers four tools: Flow Builder, approval processes, Flow Orchestration (which coordinates multiple flows) and MuleSoft Composer for no-code app and data integration.[^s3] On the code side, Apex triggers and invocable Apex extend or replace declarative automation when an object's logic gets too heavy for Flow.[^s1]

## The toolset today

**Flow** is the centre of the toolset. Salesforce's architects call record-triggered flow the platform's premier declarative tool for record-triggered automation and the right default for most teams.[^s1] Salesforce Help says Workflow Rules and Process Builder are no longer the preferred tools and that Flow Builder is the recommended foundation, citing its extensibility, lifecycle management and faster performance.[^s5] Back in 2021 Salesforce said it was stopping active development on both legacy tools and consolidating triggered automation into Flow, while workflow *actions* such as email alerts were not being retired.[^s6]

**Approval processes** remain a separate tool. An approval process defines the approval steps, who approves at each step, and the actions taken on submission, final approval and final rejection. The default submission action locks the record so that only approvers and admins can edit it while the request is pending, and a flow can be launched as one of those actions.[^s4] In the same 2021 post, Salesforce said approval processes were not being retired soon, because Flow Orchestration could not yet replace all of their capabilities.[^s6]

**Apex** is the pro-code layer. The architect guidance names Apex triggers as the standard for high-density objects and recommends a hybrid where Flow handles entry criteria and orchestration and invocable Apex handles heavy computation.[^s1]

## Choosing a tool: automation density

Salesforce now frames the Flow-or-Apex decision around *automation density* rather than who builds the automation.[^s2] Density has three dimensions: how many automations fire on one save, how many records arrive at once (manual edits or bulk integrations), and how far one save cascades into other objects.[^s2] The decision guide's rough bands are: fewer than 15 automations with 0–1 downstream DML operations suits record-triggered flow; 15–30 with 2–4 downstream DML suits Flow plus invocable Apex; and more than 30, with batches of thousands of records and 5+ downstream DML, calls for an Apex trigger framework.[^s1] The guide also says to keep one entry point per object rather than mixing flows and Apex triggers on the same object.[^s1]

## Gotchas and good practice

- **Prefer before-save for same-record updates.** Before-save flows and before-context triggers save changes in the original transaction, avoiding a second DML and recursive saves.[^s1] Salesforce Help calls before-save (fast field update) flows the best-performing option because they are limited to the triggering record.[^s5]
- **Flow is not free.** It gives automatic bulkification, but the guide warns against using it for high-performance bulk processing. It lacks native Map and Set structures and cannot cache state across invocations in a transaction.[^s1] Bulk loads reach triggers in chunks of 200 records, so a 20,000-record load means about 100 trigger invocations.[^s1]
- **Some events are Apex-only.** Flow does not support after-undelete, so Apex is the only option there.[^s1]
- **Use precise entry conditions** to avoid needless runs, and move long operations such as callouts onto asynchronous paths.[^s5][^s2] Use scheduled paths instead of time-dependent workflow rules.[^s5]
- **Don't migrate one-to-one.** When moving off legacy tools, start with the object that has the fewest rules and remove redundant or recursive automations. Some logic is better as a formula field or a reusable subflow.[^s5]

## Connections

Process automation is a capability of the **Salesforce Platform** and is the parent concept for the graph's automation nodes. **Flow Builder** is its main declarative tool, and the record-triggered, screen and autolaunched flow types sit under it.[^s3][^s5] **Flow Orchestrator** coordinates multiple flows into longer, multi-user processes.[^s3] **Approval processes** are a separate part of the toolset that Orchestration may eventually overlap with.[^s4][^s6] **Apex triggers** are the code-based alternative for high-density objects.[^s1] Every automation that fires on a save takes a slot in the **order of execution**, and all of them share one transaction's **governor limits**, which is why density, rather than the number of tools, drives the design.[^s1][^s2]

## Sources

[^s1]: Salesforce Architects, "Record-Triggered Automation Decision Guide". https://architect.salesforce.com/docs/architect/decision-guides/guide/record-triggered (accessed 2026-11-01)
[^s2]: Salesforce, "Record-Triggered Automation: Apex or Flow?". https://www.salesforce.com/blog/record-triggered-automation-apex-or-flow (accessed 2026-11-01)
[^s3]: Trailhead, "Automate Business Processes" trail. https://trailhead.salesforce.com/trails/automate_business_processes (accessed 2026-11-01)
[^s4]: Trailhead, "Business Process Automation: Customize How Records Get Approved". https://trailhead.salesforce.com/content/learn/modules/business_process_automation/approvals (accessed 2026-11-01)
[^s5]: Salesforce Help, "Planning Your Switch to Flow Builder". https://help.salesforce.com/s/articleView?id=sf.flow_migrate_to_flow_best_practices.htm&language=en_US&type=5 (accessed 2026-11-01)
[^s6]: Salesforce Admins, "Go with the Flow: What's Happening with Workflow Rules and Process Builder?". https://admin.salesforce.com/blog/2021/go-with-the-flow-whats-happening-with-workflow-rules-and-process-builder (accessed 2026-11-01)
