---
id: kt:action-plans
type: Feature
title: Action Plans
aliases: [action plan, action plan templates, action plan template, Industries action plans]
domain: automation
summary: >-
  A Salesforce Industries feature that turns a repeatable business process into a published template of tasks
  and document checklist items, then stamps out action plans whose items are assigned and dated automatically
  from the plan's start date on a target record.
release: "Winter '27"
status: current
broader: [kt:process-automation, kt:salesforce-industries]
related: [kt:activity-data-model, kt:queues, kt:opportunity-teams, kt:experience-cloud]
relations:
  - {predicate: dependsOn, object: kt:business-hours}
  - {predicate: integratesWith, object: kt:flow-orchestrator}
  - {predicate: consumedBy, object: kt:financial-services-cloud}
  - {predicate: hasPart, object: kt:document-checklist-items}
sources:
  - id: s1
    title: "Action Plans for Industries: Get Started with Action Plans"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/action-plans-for-industries/get-started-with-action-plans
    type: official-learning
    accessed: 2026-11-23
  - id: s2
    title: "Action Plans for Industries: Create Action Plan Templates and Configure Tasks"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/action-plans-for-industries/create-action-plan-templates-and-tasks
    type: official-learning
    accessed: 2026-11-23
  - id: s3
    title: "Action Plans in Financial Services Cloud: Learn About Action Plans"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/action-plans-in-financial-services-cloud/learn-about-action-plans
    type: official-learning
    accessed: 2026-11-23
  - id: s4
    title: "Action Plans for Financial Advisors in Financial Services Cloud: Configure Action Plans"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/action-plans-for-financial-advisors-in-financial-services-cloud/configure-action-plans
    type: official-learning
    accessed: 2026-11-23
created: 2026-11-23
---

# Action Plans

Action Plans let an admin define a recurring business process once, as an **action plan template**, and then launch it repeatedly against individual records. The template holds an ordered set of items — tasks and document checklist items — and each **action plan** created from it is a run-time instance tied to one target record of the template's object type.[^s1] Trailhead compares the relationship to a reusable document template: the template is set up once, and every plan created from it starts from the same structure.[^s3] The feature ships with Salesforce Industries products and is used in financial services, healthcare, automotive, consumer goods, manufacturing, public sector and nonprofit social services.[^s1]

## How it works

A template needs a name, an action plan type (Industries by default) and a target object that has Activities enabled. Supported targets include Account, Case, Contact, Lead and Opportunity, the standard objects of Industries products, and custom objects with Activities turned on.[^s1][^s2] In Financial Services Cloud (now branded Agentforce Financial Services) the list also covers objects such as Financial Account, Financial Goal, Insurance Policy and Residential Loan Application, subject to configuration and licenses.[^s3]

Each task item carries a subject, a priority, a number of days to complete and an assignee; it can be flagged as required and can send the assignee a reminder at a set time on the due date.[^s2][^s4] Assignees can be a named user, the plan creator, a queue, or a role when account, opportunity or case team roles are enabled.[^s2] Document checklist items represent paperwork the process needs, such as a contract, proof of insurance or identity verification.[^s1] An admin can also let users add their own items to a running plan.[^s2]

Tasks can depend on up to three prerequisite tasks. Only tasks without prerequisites are created when the plan starts; dependent tasks appear once their prerequisites are completed, which lets a template model a simple sequence such as schedule meeting, then prepare a report, then review it.[^s2][^s4] A template must be published before plans can be created from it.[^s2][^s4]

Users launch a plan from the Action Plans component on the target record by choosing a name, start date, template and status. Due dates are computed as the start date plus each item's day offset, and the creator chooses calendar days or working days; the "Skip Nonwork Days for Tasks" option pushes deadlines past weekends and holidays.[^s3][^s4] Working-day calculation uses the org's business hours and nonrecurring holidays.[^s2] A preview step shows the calculated deadlines and resolved owners before saving, after which tasks appear in owners' task lists and on the record's activity timeline.[^s3][^s4]

## Limits and gotchas

- Items with no resolvable user, or assigned to a role held by two or more users, fall back to the plan creator.[^s3]
- A template built in the UI makes the creator the plan owner; one built through the API can name a different owner.[^s3]
- Plan status doesn't follow task progress by itself: admins clone and activate the "Update Action Plan Status" flow template to keep it in sync.[^s2]
- The feature must be enabled and permissions assigned, and it isn't available in a standard Trailhead Playground.[^s2][^s4]

## When to use it (and when not)

Use Action Plans when the process is a checklist of human tasks and documents with relative deadlines — onboarding a client, collecting loan or claim documents, or a case-handling playbook — and you want every instance to look the same.[^s1][^s3] Tasks can also go to Experience Cloud site users, given a community user profile and permission set, which suits processes where customers or partners supply documents.[^s1] For multi-step, multi-user work with branching logic and background steps, Flow Orchestrator is the stronger tool; Salesforce itself pairs the two by using an orchestration flow to run recurring action plans.[^s1]

## Connections

Action Plans sit under **process automation** as a template-driven way to generate activity records, and under **Salesforce Industries** because they ship with Industries clouds such as **Financial Services Cloud**.[^s1][^s3] They write standard Task records, so they extend the **activity data model**, and they route work to **queues** or team roles such as **opportunity teams**.[^s2] Deadline maths depends on **business hours** and holidays.[^s2] Recurring schedules integrate with **Flow Orchestrator**, external assignees reach plans through **Experience Cloud**, and document checklist items are the other building block of each template.[^s1]

## Sources

[^s1]: Trailhead, "Action Plans for Industries: Get Started with Action Plans". https://trailhead.salesforce.com/content/learn/modules/action-plans-for-industries/get-started-with-action-plans (accessed 2026-11-23)
[^s2]: Trailhead, "Action Plans for Industries: Create Action Plan Templates and Configure Tasks". https://trailhead.salesforce.com/content/learn/modules/action-plans-for-industries/create-action-plan-templates-and-tasks (accessed 2026-11-23)
[^s3]: Trailhead, "Action Plans in Financial Services Cloud: Learn About Action Plans". https://trailhead.salesforce.com/content/learn/modules/action-plans-in-financial-services-cloud/learn-about-action-plans (accessed 2026-11-23)
[^s4]: Trailhead, "Action Plans for Financial Advisors in Financial Services Cloud: Configure Action Plans". https://trailhead.salesforce.com/content/learn/modules/action-plans-for-financial-advisors-in-financial-services-cloud/configure-action-plans (accessed 2026-11-23)
