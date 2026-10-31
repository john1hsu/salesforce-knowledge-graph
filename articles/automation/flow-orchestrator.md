---
id: kt:flow-orchestrator
type: Feature
title: Flow Orchestrator
aliases: [Flow Orchestration, Salesforce Orchestrator, Orchestration flow type]
domain: automation
summary: >-
  A Flow type that coordinates multi-user, multi-step business processes by running existing screen and
  autolaunched flows as steps grouped into sequential stages, with work items surfaced to assignees in the
  Orchestration Work Guide.
release: "Winter '27"
status: current
broader: [kt:flow-builder, kt:process-automation]
related: [kt:screen-flow, kt:record-triggered-flow, kt:autolaunched-flow]
relations:
  - {predicate: alternativeTo, object: kt:approval-processes}
  - {predicate: integratesWith, object: kt:mulesoft-anypoint-platform}
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: hasPart, object: kt:orchestration-work-guide}
sources:
  - id: s1
    title: "Flow Orchestration Basics: Flow Orchestration Stages & Types"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/orchestrator-basics/get-to-know-orchestrator
    type: official-learning
    accessed: 2026-10-31
  - id: s2
    title: "Build a Flow Orchestration: Identify Your Steps and Build Your Flows"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/build-a-flow-orchestration/identify-your-steps-and-build-your-flows
    type: official-learning
    accessed: 2026-10-31
  - id: s3
    title: "Orchestration Steps"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=orchestrator_concepts_steps.htm&type=5&language=en_US
    type: official-docs
    accessed: 2026-10-31
  - id: s4
    title: "Considerations for Orchestrations"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=platform.orchestrator_considerations_orchestrations.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-10-31
  - id: s5
    title: "General Flow Orchestration Limits"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=platform.orchestrator_considerations_limit.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-10-31
  - id: s6
    title: "Flow Orchestration is Now a Standard Flow Type"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2026/flow-orchestration-is-now-a-standard-flow-type
    type: official-blog
    accessed: 2026-10-31
  - id: s7
    title: "Introducing Flow Orchestrator: Unify Your Complex Business Processes Without Code"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2021/introducing-flow-orchestrator-unify-your-complex-business-processes-without-code
    type: official-blog
    accessed: 2026-10-31
created: 2026-10-31
---

# Flow Orchestrator

Flow Orchestrator (documented in Salesforce Help as **Flow Orchestration**, and often just "Orchestrator") is a Flow type for business processes that span several people, teams and days. Instead of one flow doing everything, an orchestration strings together existing screen and autolaunched flows, decides who works on each piece and when, and tracks the whole process as a single run.[^s7] Salesforce introduced it on the Admins blog in 2021 as a declarative way to build multi-user, multi-step processes.[^s7] It was a paid add-on until February 18, 2026, when Salesforce made it a standard Flow type for all customers, subject to the edition-based Flow limits.[^s6]

## How it works

An orchestration is either **record-triggered** (it starts when a record of a given object is created or updated) or **autolaunched** (no trigger, invoked from Apex, REST and similar callers). Both are created from the New Flow dialog in Setup.[^s1] It is built from three blocks:

- **Stages** group related steps into phases. Stages run in sequence, and only one stage per orchestration can be in progress at a time. Each stage has its own completion conditions, and Decision elements between stages add branching.[^s1][^s7]
- **Steps** sit inside a stage and can run one after another or at the same time.[^s1] An *interactive step* runs an active screen flow, creates an orchestration work item, and is assigned to a user, group or queue. A *background step* runs an active autolaunched flow, synchronously or asynchronously, with no user involvement. A *MuleSoft step* asynchronously runs an operation imported from a MuleSoft API.[^s3]
- **Evaluation flows** supply custom logic for when a step may start, or when an interactive step counts as complete.[^s1]

Steps move through the statuses Not Started, In Progress, Completed, Discontinued and Error. A step is *Discontinued* if it was still running when its stage completed or the orchestration failed.[^s3] Output variables from a called flow become available to the orchestration only after that step completes, and only if they are marked "Available for output" in the called flow.[^s3]

Assignees get an email linking to the record page. They do the work in the **Orchestration Work Guide**, a component added to the page in Lightning App Builder, and can see all their tasks in the Orchestration Work Items list. Admins watch the Orchestration Runs list and can cancel or debug a run that is in progress.[^s1] Trailhead's hiring example shows the usual design approach: break the process into interactive and background steps, build and activate each flow first, and make generic, reusable flows (for example one email-alert flow driven by input variables) before assembling the orchestration.[^s2]

## Limits and gotchas

- **Org caps.** Help lists 50 versions per orchestration, 2,000 active orchestrations per org and 4,000 total orchestrations per org for Enterprise, Unlimited, Performance and Developer Editions.[^s5]
- **Input size.** If a step's flow receives more than 32,768 combined characters of input, the orchestration fails. Passing whole records is the usual cause, so pass a record ID and query it inside the flow with Get Records.[^s4]
- **Shared governor limits.** Steps that run at the same time are batched by user context and flow version and run in one transaction. SOQL, DML and CPU time add up across the batch, together with any record-triggered flows and Apex triggers those step flows set off. Salesforce warns that staggering start times does not reliably shrink these batches. Its advice: keep queries, DML and callouts out of loops; use collection-based invocable Apex; separate callouts and DML into different steps; and add a Wait element to force a background flow to run asynchronously.[^s4]
- **Record-change evaluations.** The referenced record's object must support change events. Formula fields, fields from related records, IsDeleted and SystemModeStamp cannot trigger an evaluation. In record-triggered orchestrations, `$Record` is the only global variable that can be the referenced record.[^s4]
- **Double alerts.** A failed step flow that fails the orchestration sends two emails, one flow error and one orchestration error.[^s4]

## When to use it (and when not)

Orchestrator is a good fit when work passes between people or departments, waits days or weeks for a human decision, or needs several people working in parallel. Examples include onboarding, contract renewals and Sales-to-Finance-to-Operations handoffs.[^s6][^s7] For a single user's task or fully automated record logic, a plain screen flow or record-triggered flow is simpler. Approval-style processes can be built either way: Salesforce's Flow-based approvals share the same 32,768-character input limit for called flows.[^s4]

## Connections

Orchestrator is a Flow type built in **Flow Builder** and is part of the wider **process automation** toolset.[^s1] Its steps run **screen flows** (interactive) and **autolaunched flows** (background), and an orchestration can be started like a **record-triggered flow**.[^s1][^s3] Its MuleSoft steps tie it to the **MuleSoft Anypoint Platform**.[^s3] Concurrent steps share **governor limits** in one transaction.[^s4] The **Orchestration Work Guide** is the component users work in.[^s1] For human sign-off it overlaps with **approval processes**, which is why it is linked here as an alternative to them.[^s6]

## Sources
[^s1]: Trailhead, "Flow Orchestration Basics: Flow Orchestration Stages & Types". https://trailhead.salesforce.com/content/learn/modules/orchestrator-basics/get-to-know-orchestrator (accessed 2026-10-31)
[^s2]: Trailhead, "Build a Flow Orchestration: Identify Your Steps and Build Your Flows". https://trailhead.salesforce.com/content/learn/modules/build-a-flow-orchestration/identify-your-steps-and-build-your-flows (accessed 2026-10-31)
[^s3]: Salesforce Help, "Orchestration Steps". https://help.salesforce.com/s/articleView?id=orchestrator_concepts_steps.htm&type=5&language=en_US (accessed 2026-10-31)
[^s4]: Salesforce Help, "Considerations for Orchestrations". https://help.salesforce.com/s/articleView?id=platform.orchestrator_considerations_orchestrations.htm&language=en_US&type=5 (accessed 2026-10-31)
[^s5]: Salesforce Help, "General Flow Orchestration Limits". https://help.salesforce.com/s/articleView?id=platform.orchestrator_considerations_limit.htm&language=en_US&type=5 (accessed 2026-10-31)
[^s6]: Salesforce Admins Blog, "Flow Orchestration is Now a Standard Flow Type" (2026-02-18). https://admin.salesforce.com/blog/2026/flow-orchestration-is-now-a-standard-flow-type (accessed 2026-10-31)
[^s7]: Salesforce Admins Blog, "Introducing Flow Orchestrator: Unify Your Complex Business Processes Without Code" (2021). https://admin.salesforce.com/blog/2021/introducing-flow-orchestrator-unify-your-complex-business-processes-without-code (accessed 2026-10-31)
