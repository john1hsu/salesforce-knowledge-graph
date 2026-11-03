---
id: kt:approval-processes
type: Feature
title: Approval Processes
aliases: [approval process, Classic Approval Processes, Flow Approval Processes, flow approval process, approval orchestration, Submit for Approval]
domain: automation
summary: >-
  Salesforce automation that routes a record through one or more approval steps, locking it while it is
  reviewed and running actions on submission, approval, rejection or recall; built either as a classic
  approval process or as a Flow Approval Process on the orchestration engine.
release: "Winter '27"
status: current
broader: [kt:process-automation]
related: [kt:record-locking, kt:record-triggered-flow, kt:autolaunched-flow, kt:queues]
relations:
  - {predicate: configuredVia, object: kt:flow-builder}
  - {predicate: alternativeTo, object: kt:flow-orchestrator}
  - {predicate: hasPart, object: kt:orchestration-work-guide}
  - {predicate: governedBy, object: kt:governor-limits}
sources:
  - id: s1
    title: "Guide to Salesforce Record Approval Processes"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/business_process_automation/approvals
    type: official-learning
    accessed: 2026-11-03
  - id: s2
    title: "Considerations for Managing Classic Approval Processes"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.approvals_considerations_manage.htm&type=5
    type: official-docs
    accessed: 2026-11-03
  - id: s3
    title: "Automate Your Approvals with Flow Approval Processes"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.automate_automated_approvals.htm&type=5
    type: official-docs
    accessed: 2026-11-03
  - id: s4
    title: "Flow Approval Processes Concepts"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=platform.automate_automated_approvals_concepts.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-03
  - id: s5
    title: "Considerations for Migrating from Approval Processes"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=platform.automate_automated_approvals_considerations_migrating_from_legacy_approval_processes.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-03
  - id: s6
    title: "Flow Approval Processes Limits and Considerations"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.automate_automated_approvals_considerations.htm&type=5
    type: official-docs
    accessed: 2026-11-03
created: 2026-11-03
---

# Approval Processes

An approval process automates how a Salesforce record gets approved: it defines the chain of approval steps, who approves at each step, and what happens when the record is submitted, approved or rejected.[^s1] Typical uses are a new-position request that goes first to the submitter's manager and then to the CEO, a time-off request, or an opportunity whose discount exceeds a threshold and therefore needs a manager's sign-off.[^s1] Salesforce now offers two implementations: **classic approval processes**, configured in Setup per object, and **Flow Approval Processes**, which are built in Flow Builder and run on the orchestration engine.[^s2][^s3]

## How classic approval processes work

A classic process is a sequence of approval steps with actions attached to each outcome. Initial submission actions run when the record is first submitted; by default they lock the record so that only approvers and administrators can edit it while it is pending, and they can also send email alerts, update fields, create tasks, send outbound messages or launch flows.[^s1] Final rejection actions run when an approver rejects (for example, setting a status field to Rejected), while final approval actions fire only when the record is approved with no further steps left, typically setting the status, unlocking the record and notifying the requester.[^s1]

Classic processes are available in Salesforce Classic and Lightning Experience in Enterprise, Performance, Unlimited and Developer Editions.[^s2] Users with Modify All on the object, or Modify All Data, act as approval admins: they can approve or reject pending requests without being named in the process and can edit records that are locked for approval.[^s2]

## How Flow Approval Processes work

A Flow Approval Process is a sequence of **stages**, each holding one or more **steps**. Approval steps create work items assigned to a user, group or queue; background steps run actions with no human interaction; and Decision elements choose the path based on conditions.[^s3] Each submission has its own orchestration run, and each approval work item is linked to an orchestration work item.[^s4] A process is either **autolaunched**, created in the Approvals app and started manually such as from a custom button, or **record-triggered**, starting when a record is created or updated that meets the Start element's conditions; both default to running as the Automated Process user in system context.[^s4]

Approvers and their delegates are emailed a link to the record, and can act in the Orchestration Work Guide component, from the Approval Work Items list view, or by replying to the email with a keyword.[^s3][^s4] Admins must add the Orchestration Work Guide to the record page before activating a process for an object.[^s3] Fault paths on stages let a submission end as approved or rejected instead of failing outright, and record locking depends on whether a stage's approval steps run consecutively or concurrently.[^s4]

## Limits and gotchas

- A classic process needs at least one step before activation. Once it has been activated you can no longer add, delete or reorder steps or change reject and skip behaviour, even after deactivating it, so test in a sandbox first.[^s2]
- Deleting a classic process requires it to be inactive and every request and submitted record tied to it to be removed (including from the Recycle Bin); a failed delete can be retried after 2 days.[^s2]
- Deactivate and delete approval processes before deleting their custom object; an orphaned process can stop Metadata API tools from listing or retrieving approval process metadata.[^s2]
- Migration is not one-to-one. Classic processes rely on the Submit for Approval button and an email template; flow approvals use record triggers, a custom button or the Request an Approval action, default notifications and text templates. Recall is modelled as a recall path on the Start element, and letting submitters pick any user as approver at submission time is not supported, so the approver must be resolved in the process, for example from a variable.[^s5]

## When to use which

Classic approval processes remain a declarative option for simple, object-bound routing, but Salesforce notes they support conditions only in limited ways, whereas Flow Approval Processes support dynamic routing.[^s2] Choose flow approvals for new multi-stage work that mixes human approvals with system actions, conditional branches or group and queue assignment, and review the known feature gaps before replacing a classic process.[^s3][^s5]

## Connections

Approval processes are a branch of **process automation**. Flow Approval Processes are authored in **Flow Builder** and are a specialised form of **Flow Orchestrator** runs, an alternative for approval-centric processes, with work surfaced through the **Orchestration Work Guide**.[^s3][^s4] They start from **record-triggered** or **autolaunched flows**, assign work to **queues** and groups, and depend on **record locking** to freeze a record during review; and Salesforce tells designers to keep flow approval limits, flow limits and Apex **governor limits** in mind.[^s1][^s4][^s6]

## Sources
[^s1]: Trailhead, "Guide to Salesforce Record Approval Processes". https://trailhead.salesforce.com/content/learn/modules/business_process_automation/approvals (accessed 2026-11-03)
[^s2]: Salesforce Help, "Considerations for Managing Classic Approval Processes". https://help.salesforce.com/s/articleView?language=en_US&id=platform.approvals_considerations_manage.htm&type=5 (accessed 2026-11-03)
[^s3]: Salesforce Help, "Automate Your Approvals with Flow Approval Processes". https://help.salesforce.com/s/articleView?language=en_US&id=platform.automate_automated_approvals.htm&type=5 (accessed 2026-11-03)
[^s4]: Salesforce Help, "Flow Approval Processes Concepts". https://help.salesforce.com/s/articleView?id=platform.automate_automated_approvals_concepts.htm&language=en_US&type=5 (accessed 2026-11-03)
[^s5]: Salesforce Help, "Considerations for Migrating from Approval Processes". https://help.salesforce.com/s/articleView?id=platform.automate_automated_approvals_considerations_migrating_from_legacy_approval_processes.htm&language=en_US&type=5 (accessed 2026-11-03)
[^s6]: Salesforce Help, "Flow Approval Processes Limits and Considerations". https://help.salesforce.com/s/articleView?language=en_US&id=platform.automate_automated_approvals_considerations.htm&type=5 (accessed 2026-11-03)
