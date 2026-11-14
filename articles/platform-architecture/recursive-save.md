---
id: kt:recursive-save
type: Concept
title: Recursive Save
aliases: [recursive save cycle, save recursion, same-record update recursion, re-entering the save order]
domain: platform-architecture
summary: >-
  The platform behaviour in which automation that updates a record after it was saved sends that record through the
  save order of execution again in the same transaction, re-running early steps such as triggers while skipping others.
release: "Winter '27"
status: current
broader: [kt:order-of-execution]
related: [kt:record-triggered-flow, kt:apex-triggers, kt:trigger-framework-pattern, kt:workflow-rules, kt:process-builder, kt:roll-up-summary-field, kt:transaction-control]
relations:
  - {predicate: governedBy, object: kt:governor-limits}
sources:
  - id: s1
    title: "Apex Developer Guide: Triggers and Order of Execution"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm
    type: official-docs
    accessed: 2026-11-14
  - id: s2
    title: "Record-Triggered Automation Decision Guide"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/decision-guides/trigger-automation
    type: official-docs
    accessed: 2026-11-14
  - id: s3
    title: "Platform Decision Guides: Record-Triggered Automation"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/decision-guides/guide/record-triggered
    type: official-docs
    accessed: 2026-11-14
  - id: s4
    title: "Apex Developer Guide: Static and Instance Methods, Variables, and Initialization Code"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_static.htm
    type: official-docs
    accessed: 2026-11-14
created: 2026-11-14
---

# Recursive Save

A **recursive save** happens when automation that runs after a record has been written to the database changes a record again, so that record re-enters the save procedure inside the same transaction. The Apex Developer Guide (Winter '27, API version 68.0) ties it to three mechanisms: workflow field updates, which update the record again; processes and flows that perform DML, which send the affected record through the save procedure; and roll-up summary fields, which send the parent and possibly the grandparent record through it.[^s1] It is not a feature you switch on but a consequence of how the order of execution is built, and it is the main reason after-save same-record updates are expensive.[^s2]

## How it works

The order of execution is a numbered list of steps. During a recursive save, Salesforce skips steps 9 through 17: assignment rules, auto-response rules, workflow rules, escalation rules, processes and workflow-launched flows, after-save record-triggered flows, entitlement rules and the parent and grandparent roll-up summary updates.[^s1] Everything else runs again, including loading the record, before-save flows, before triggers, system and custom validation, duplicate rules, the database save and after triggers.[^s1] Criteria-based sharing evaluation, the commit and post-commit logic (emails, enqueued asynchronous jobs) still happen once at the end of the outer transaction.[^s1]

Workflow field updates are a special case. After the field update, before update and after update triggers fire one more time, and only once more, whether the original operation was an insert or an update.[^s1] Inside that extra trigger run, `Trigger.old` holds the values from before the user's original update, not the values the workflow set. Salesforce's example is a field changed from 1 to 10 and incremented to 11 by workflow, where `Trigger.old` still shows 1.[^s1]

Flow triggers get recursion control for the skipped middle of the save order but not for the early and late steps. An after-save flow that updates its own triggering record therefore re-runs the early validation, before-trigger and after-trigger stages.[^s2] The architects' guide also states that a flow trigger never causes itself to fire again on the same record, although the same flow can legitimately run twice on a record in one transaction if another save, not its own, caused the second run.[^s2]

## Cost and gotchas

- **Performance.** Salesforce measured bulk same-record updates as roughly 10–20 times faster in before-save flow triggers than in Workflow Rules or Process Builder, which run after the save and cause recursive saves.[^s2]
- **Scale of the problem.** In April 2020 about 100 billion of roughly 150 billion automation actions were same-record field updates, which the guide equates to 100 billion recursive saves in a month.[^s2]
- **Infinite loops in Apex.** An after-update trigger that updates the same object can fire itself again and loop until a governor limit exception ends the transaction.[^s3]
- **Dense automation compounds it.** The record-triggered decision guide flags recursion risk as automation density grows, and triangular recursion loops at high density.[^s3]
- **Static state survives.** Static variables keep their values across repeated trigger firings in one transaction and are not reset between invocations within one Bulk API request.[^s4]

## Avoiding it

The primary fix is to move same-record field updates into before-save logic: a before-save record-triggered flow or a before trigger changes the record in memory, so no second DML and no recursive save are needed.[^s3] Invocable Apex cannot run before save, so it is not an option for same-record updates.[^s3] Merging several Update Records elements into one also trims redundant passes through the save order.[^s2]

When a recursive pass cannot be avoided, make the logic idempotent. Static Boolean flags or sets of processed record IDs are the traditional guard, and the Apex guide shows a class-level static that stops a trigger after its first run.[^s4][^s3] Salesforce now prefers comparing new and old values (`Trigger.new` against `Trigger.oldMap`, or `$Record` against `$Record__Prior` in flow entry criteria) and running only when the relevant field actually changed.[^s3]

## Connections

Recursive save is a behaviour of the save **order of execution** (`kt:order-of-execution`), its broader node, and it is what that article warns same-record after-save updates cause.[^s1] Every recursive pass stays in the same transaction (`kt:transaction-control`) and is **governed by** `kt:governor-limits`, which is what finally stops runaway recursion.[^s3] The legacy tools that generate the most recursive saves are **workflow rules** (`kt:workflow-rules`) and **Process Builder** (`kt:process-builder`), while before-save **record-triggered flows** (`kt:record-triggered-flow`) and before **Apex triggers** (`kt:apex-triggers`) avoid them.[^s2] Parent re-saves link it to **roll-up summary fields** (`kt:roll-up-summary-field`).[^s1] The recursion guards and old-versus-new checks are part of the **trigger framework pattern** (`kt:trigger-framework-pattern`).[^s3][^s4]

## Sources

[^s1]: Salesforce Developers, "Apex Developer Guide: Triggers and Order of Execution". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm (accessed 2026-11-14)
[^s2]: Salesforce Architects, "Record-Triggered Automation Decision Guide". https://architect.salesforce.com/decision-guides/trigger-automation (accessed 2026-11-14)
[^s3]: Salesforce Architects, "Platform Decision Guides: Record-Triggered Automation". https://architect.salesforce.com/docs/architect/decision-guides/guide/record-triggered (accessed 2026-11-14)
[^s4]: Salesforce Developers, "Apex Developer Guide: Static and Instance Methods, Variables, and Initialization Code". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_static.htm (accessed 2026-11-14)
