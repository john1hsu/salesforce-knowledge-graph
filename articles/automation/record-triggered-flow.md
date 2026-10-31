---
id: kt:record-triggered-flow
type: Feature
title: Record-Triggered Flow
aliases: [record-triggered flows, before-save flow, after-save flow, fast field update flow, flow trigger]
domain: automation
summary: >-
  An autolaunched flow that runs in the background when a record is created, updated or deleted, with
  before-save (fast field update), after-save, asynchronous and scheduled paths; Salesforce's primary
  low-code alternative to Apex triggers.
release: "Winter '27"
status: current
broader: [kt:flow-builder, kt:process-automation]
related: [kt:order-of-execution, kt:flow-trigger-explorer, kt:screen-flow, kt:autolaunched-flow]
relations:
  - {predicate: alternativeTo, object: kt:apex-triggers}
  - {predicate: replaces, object: kt:workflow-rules}
  - {predicate: replaces, object: kt:process-builder}
  - {predicate: governedBy, object: kt:governor-limits}
sources:
  - id: s1
    title: "Record-Triggered Flows: Get Started with Triggered Flows"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/record-triggered-flows/get-started-with-triggered-flows
    type: official-learning
    accessed: 2026-10-31
  - id: s2
    title: "Record-Triggered Flow Considerations"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=platform.flow_considerations_trigger_record.htm
    type: official-docs
    accessed: 2026-10-31
  - id: s3
    title: "Architect's Guide to Record-Triggered Automation"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/decision-guides/trigger-automation
    type: official-docs
    accessed: 2026-10-31
  - id: s4
    title: "Automate This! Discover Tips and Best Practices for Record-Triggered Flows"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2022/automate-this-discover-tips-and-best-practices-for-record-triggered-flows
    type: official-blog
    accessed: 2026-10-31
created: 2026-10-31
---

# Record-Triggered Flow

A record-triggered flow is an automation built in Flow Builder that runs in the background whenever a record on a chosen object is saved or removed. Trailhead describes it as the most commonly used kind of automation, following an "if something happens, then do something else" shape: update related records, send notifications, start a process or keep data consistent.[^s1] The Start element defines the object and the trigger, which is one of: only when a record is created, when a record is updated, when a record is created or updated, or only when a record is deleted.[^s1]

## How it works

A single record-triggered flow can contain up to four kinds of path, each tied to a different point relative to the save that fired it:[^s1]

- **Fast field updates (before-save)** run during the save, before the change is committed. They are meant for setting fields on the triggering record or raising a custom error, and they touch the database least.[^s1]
- **Actions and related records (after-save)** run during the save, after the record is written, and can create, update or delete other records, call subflows, or invoke actions such as email alerts.[^s1]
- **Run asynchronously** executes right after the triggering transaction completes, so slow work such as calling an external system doesn't block the user's save.[^s1]
- **Scheduled paths** run later, offset from a date on the record (for example a Close Date), which suits reminders and follow-ups.[^s1]

Entry conditions on the Start element filter which saves launch the flow at all. Salesforce's architects note that tight entry conditions can greatly reduce performance cost and let a flow fire only when a record reaches a particular state, such as a status moving from open to closed.[^s3] Where several flows fire on the same object and event, a trigger order value sets their sequence; values need not be consecutive, ties run alphabetically, and the guide recommends gaps (10, 20, 30) so new flows can be slotted in later.[^s3] The Flow Trigger Explorer lists every flow that fires for a given object and action and is where admins review that order.[^s4]

## Limits and gotchas

- A before-save flow can only change fields on the triggering record; it supports just Assignment, Decision, Get Records and Loop elements, and cannot touch related records or run other actions.[^s2] The architect guide adds that it cannot call invocable Apex or subflows.[^s3]
- Synchronous paths fail if they reach external data, including Data Cloud objects, because callouts aren't allowed while a record is saving; such work belongs on an asynchronous path. Asynchronous paths in turn don't support the ISCHANGED operator.[^s2]
- Record-triggered flows run custom validation rules, and because of where they sit in the save order they can behave differently from an equivalent workflow rule.[^s2] Activating a triggered autolaunched flow requires the View All Data permission.[^s2]
- Updating the triggering record from an after-save path causes a recursive save that re-runs earlier steps of the order of execution; doing the same work before-save avoids that.[^s3]
- Flow bulkifies across records in a batch automatically, but DML or queries placed inside a Loop are not bulkified and can exhaust governor limits; the guide cites per-transaction ceilings of 150 DML statements and 10,000 processed DML rows.[^s3]
- Scheduled paths that wait a long time are fragile: the flow fails if the triggering user is deactivated before it resumes, waiting interviews count against a limit, and a lead tied to a paused interview can't be converted.[^s4]

## When to use it (and when not)

Salesforce positions Flow as the go-forward low-code tool and recommends using Workflow Rules and Process Builder only when unavoidable.[^s3] In Salesforce's own testing, before-save flows handled bulk same-record updates roughly 10–20 times faster than Workflow Rules or Process Builder, so the guide treats them as safe wherever a workflow field update was used.[^s3] Admins are advised to pick fast field updates whenever the flow qualifies, and to set fields on `$Record` with an Assignment element instead of an Update Records element.[^s4]

Apex triggers remain the better fit for complex list processing, heavy batch logic and fine-grained control over callouts and error handling; teams that are Apex-centric with mature CI/CD may reasonably keep logic in code, while invocable Apex can extend a flow where Flow alone struggles.[^s3] The old "one flow per object" rule from the Process Builder era no longer applies: splitting logic into several well-filtered flows organised by business function has little performance cost, while one catch-all flow that runs on every save hurts performance.[^s3][^s4]

## Connections

Record-triggered flow is one flow type built in **Flow Builder** and sits under the broader **process-automation** toolset, alongside **screen flows** and plain **autolaunched flows**.[^s1] It is the low-code **alternative to Apex triggers**, and it **replaces Workflow Rules and Process Builder** as the recommended home for save-time automation.[^s3] Its before-save and after-save paths occupy fixed slots in the **order of execution**, its ordering is managed in the **Flow Trigger Explorer**, and every path runs inside the same transaction budget as other code, so it is **governed by governor limits**.[^s3][^s4]

## Sources

[^s1]: Trailhead, "Record-Triggered Flows: Get Started with Triggered Flows". https://trailhead.salesforce.com/content/learn/modules/record-triggered-flows/get-started-with-triggered-flows (accessed 2026-10-31)
[^s2]: Salesforce Help, "Record-Triggered Flow Considerations". https://help.salesforce.com/apex/HTViewHelpDoc?id=platform.flow_considerations_trigger_record.htm (accessed 2026-10-31)
[^s3]: Salesforce Architects, "Architect's Guide to Record-Triggered Automation". https://architect.salesforce.com/decision-guides/trigger-automation (accessed 2026-10-31)
[^s4]: Salesforce Admins Blog, "Automate This! Discover Tips and Best Practices for Record-Triggered Flows". https://admin.salesforce.com/blog/2022/automate-this-discover-tips-and-best-practices-for-record-triggered-flows (accessed 2026-10-31)
