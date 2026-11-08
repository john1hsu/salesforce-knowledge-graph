---
id: kt:orchestration-work-guide
type: Feature
title: Orchestration Work Guide
aliases: [Flow Orchestration Work Guide, Work Guide component, orchestration work items component]
domain: automation
summary: >-
  The Lightning page component in which users assigned to an interactive orchestration or flow approval step
  see their open work items on a record page and complete them by running the step's screen flow.
release: "Winter '27"
status: current
broader: [kt:flow-orchestrator]
related: [kt:approval-processes, kt:queues, kt:omni-channel, kt:experience-builder]
relations:
  - {predicate: partOf, object: kt:flow-orchestrator}
  - {predicate: dependsOn, object: kt:screen-flow}
  - {predicate: configuredVia, object: kt:lightning-app-builder}
  - {predicate: integratesWith, object: kt:experience-cloud}
sources:
  - id: s1
    title: "Make Assigned Work Items Accessible on a Record Page"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.orchestrator_build_add_work_guide.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-08
  - id: s2
    title: "Flow Orchestration Work Items"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.orchestrator_concepts_work_items.htm&type=5
    type: official-docs
    accessed: 2026-11-08
  - id: s3
    title: "Orchestration Work Guide (Experience Builder component)"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=experience.rss_flow_orchestration_work_guide_component.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-08
  - id: s4
    title: "Approval Work Items and Orchestration Work Items"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.automate_automated_approvals_concepts_work_items.htm&type=5
    type: official-docs
    accessed: 2026-11-08
  - id: s5
    title: "Flow Orchestration Basics: Flow Orchestration Stages & Types"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/orchestrator-basics/get-to-know-orchestrator
    type: official-learning
    accessed: 2026-11-08
  - id: s6
    title: "FlowOrchestrationWorkItem (Object Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_floworchestrationworkitem.htm
    type: official-docs
    accessed: 2026-11-08
created: 2026-11-08
---

# Orchestration Work Guide

The **Orchestration Work Guide** is the record-page component through which people take part in an orchestration. When an interactive step of a Flow Orchestrator run starts, it creates a work item and assigns it to a user, group or queue; assignees open the related record and finish the work inside the Work Guide, which runs the step's screen flow there so they don't have to switch tools.[^s2][^s5] Each of those items is stored as a `FlowOrchestrationWorkItem` record, an object available from API version 54.0 that represents the runtime instance of an interactive step.[^s6]

## How it works

An admin adds the component to the Lightning record page for the object that the interactive steps point at, using Lightning App Builder (which needs the Customize Application permission), saves and activates the page, and only then activates the orchestration.[^s1] Optional settings control the runtime title, the default sort order, whether each item shows its orchestration run, stage or step name, whether the component hides itself when the user has nothing assigned, and whether finishing one item automatically opens the next item from the same run; without that last option the component simply refreshes its list.[^s1]

Assignees usually arrive from a notification email that links to the record page. Internal users can also reach items through the Flow Orchestration Work Items list view or their To Do List, but the Work Guide still has to be on the page layout for them to do the work in context.[^s2] An evaluation flow can mark an interactive step complete without anyone using the guide, and supervisors follow progress from the Orchestration Runs list.[^s5]

## Limits and gotchas

- **Groups and queues race.** For work assigned to a group or queue, the first member to finish the screen flow completes the item; a simultaneous second submission gets an error, and the item disappears for everyone else.[^s2][^s4]
- **Email links are internal.** Links to internal record pages don't work for Experience Cloud visitors, and email delivery requires both domain- and user-level email verification.[^s2]
- **Ownership varies.** Items assigned to a user are owned by that user; group items, and queue items whose queue isn't tied to the Orchestration Work Item object, are owned by the automated process user.[^s2]
- **Reassignment restarts the item.** Reassigning an open item treats it as newly created; unanimous-approval child items can't be reassigned.[^s2][^s4]
- **Statuses are coarse.** Orchestration work items move through Assigned, Completed and Error, with history milestones recording start, end (with Completed By and Duration) and reassignment.[^s2][^s4]

## Experience Cloud sites

A separate Experience Builder version of the component lets credentialed site visitors complete their work items on an object detail page. It is listed for Enterprise, Performance, Unlimited and Developer editions, needs the Run Flows permission, sets its Record ID automatically (Salesforce advises leaving it alone), and its configuration changes don't show in the Builder preview, only on the live site.[^s3] Site visitors can also use an Orchestration Work Item list page that admins add to Aura and LWR sites.[^s2]

## Use with flow approval processes

Flow Approval Processes reuse the same machinery: every approval work item has a linked orchestration work item, and approvers can act in the Work Guide, where the step's screen flow runs. They can also use the Approval Work Items list view, whose standard screen flow can't be replaced, or reply by email when both email settings are enabled. Salesforce says to add the Work Guide before users start submitting approvals.[^s4]

## Connections

The Work Guide is **part of Flow Orchestrator**: it is the user-facing surface for that feature's interactive steps.[^s5] It **depends on screen flows**, because each interactive step runs one inside the component.[^s5] It is **configured via Lightning App Builder** on internal record pages and through **Experience Builder** on **Experience Cloud** sites.[^s1][^s3] Work can be routed to **queues**, and queues tied to the Orchestration Work Item object also receive **Omni-Channel** routing notifications.[^s2] It is shared with **approval processes** built in Flow, which surface approver tasks in the same component.[^s4]

## Sources
[^s1]: Salesforce Help, "Make Assigned Work Items Accessible on a Record Page". https://help.salesforce.com/s/articleView?id=sf.orchestrator_build_add_work_guide.htm&language=en_US&type=5 (accessed 2026-11-08)
[^s2]: Salesforce Help, "Flow Orchestration Work Items". https://help.salesforce.com/s/articleView?language=en_US&id=platform.orchestrator_concepts_work_items.htm&type=5 (accessed 2026-11-08)
[^s3]: Salesforce Help, "Orchestration Work Guide (Experience Builder component)". https://help.salesforce.com/s/articleView?id=experience.rss_flow_orchestration_work_guide_component.htm&language=en_US&type=5 (accessed 2026-11-08)
[^s4]: Salesforce Help, "Approval Work Items and Orchestration Work Items". https://help.salesforce.com/s/articleView?language=en_US&id=platform.automate_automated_approvals_concepts_work_items.htm&type=5 (accessed 2026-11-08)
[^s5]: Trailhead, "Flow Orchestration Basics: Flow Orchestration Stages & Types". https://trailhead.salesforce.com/content/learn/modules/orchestrator-basics/get-to-know-orchestrator (accessed 2026-11-08)
[^s6]: Salesforce Developers, "FlowOrchestrationWorkItem". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_floworchestrationworkitem.htm (accessed 2026-11-08)
