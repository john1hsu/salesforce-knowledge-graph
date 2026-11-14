---
id: kt:workflow-rules
type: Feature
title: Workflow Rules
aliases: [workflow rule, Salesforce Workflow, time-based workflow, workflow actions, time-dependent workflow actions]
domain: automation
summary: >-
  Salesforce's original declarative "if criteria, then actions" automation, which fires field updates, email
  alerts, tasks and outbound messages when a record is saved; new rules can no longer be created and the feature
  has been out of support since December 31, 2025, with record-triggered flows as the migration path.
release: "Winter '27"
status: deprecated
broader: [kt:process-automation]
related: [kt:process-builder, kt:approval-processes, kt:outbound-messaging, kt:order-of-execution, kt:technical-debt-in-salesforce, kt:migrate-to-flow-tool]
relations:
  - {predicate: replacedBy, object: kt:record-triggered-flow}
  - {predicate: configuredVia, object: kt:flow-builder}
  - {predicate: contrastsWith, object: kt:approval-processes}
sources:
  - id: s1
    title: "Salesforce Workflow Rules & Process Builder End of Support"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&amp=&id=001096524&amp=&type=1
    type: official-docs
    accessed: 2026-11-03
  - id: s2
    title: "Workflow: Automating the Process (cheat sheet)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.salesforce_workflow_cheatsheet.meta/salesforce_workflow_cheatsheet/workflow_cheatsheet.htm
    type: official-docs
    accessed: 2026-11-03
  - id: s3
    title: "Migrate Workflows and Processes to Flows: Understand Automation Changes"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/migrate-workflows-and-processes-to-flows/understand-automation-changes
    type: official-learning
    accessed: 2026-11-03
  - id: s4
    title: "Go with the Flow: What's Happening with Workflow Rules and Process Builder?"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2021/go-with-the-flow-whats-happening-with-workflow-rules-and-process-builder
    type: official-blog
    accessed: 2026-11-03
created: 2026-11-03
---

# Workflow Rules

Workflow rules are the oldest of Salesforce's declarative automation tools: a rule on one object evaluates records as they are saved and, when a record meets the rule's criteria, runs one or more workflow actions. Any change that makes a record match, including a change to a field the user cannot see, can fire a rule, and a single save can fire several rules.[^s2] Salesforce has stopped active development of the feature and blocked the creation of new rules, and as of December 31, 2025 it no longer supports workflow rules at all; existing active rules keep executing, but Salesforce provides neither customer support nor bug fixes for them.[^s1][^s4] For a practitioner today, workflow rules matter mainly as legacy automation to inventory, understand and migrate.

## How it works

Each rule combines evaluation criteria, rule criteria and actions. Actions come in two flavours. Immediate actions run as soon as the record meets the criteria; time-dependent actions are queued against a time trigger and run on a schedule counted from the moment the record matched. A time trigger can only be added while the rule is inactive, has no pending actions in the queue, and is not set to evaluate on create and every edit.[^s2] Admins monitor and cancel queued actions from the Time-Based Workflow page in Setup.[^s2]

Four reusable action types do the work. A field update changes a value on the record (read-only fields such as formulas and auto-numbers cannot be targets, and formula-based updates are not supported for checkbox or picklist fields). An email alert sends a templated email to users or non-users, and emails every member when the recipient is a role. A task assigns an activity to a user, role or owner on an object of the same type. An outbound message posts a configurable XML payload to an external listener as a designated user.[^s2] Because these actions are defined independently of any single rule, the same action can be reused across rules and approval processes; before configuring rules, Salesforce recommends setting the default workflow user in Process Automation Settings.[^s2]

## Limits and gotchas

Workflow rules are effectively frozen: active development ended, new rules cannot be created, and since the end-of-support date issues will not be fixed, so any defect found in a legacy rule must be worked around by migrating it.[^s1][^s4] Salesforce's guidance is to find active rules by sorting the Active column on the Workflow Rules page under Setup > Process Automation and migrate them as soon as possible, because migration and testing take real time.[^s1]

## Migrating off workflow rules

Salesforce's Migrate to Flow tool, first released in Spring '22 for workflow rules, converts eligible rules into record-triggered flows; rules whose only actions are same-record field updates become fast field update (before-save) flows.[^s4][^s3] The tool has gaps: it does not migrate task actions, criteria that use related-record or global-variable fields or record types, operators such as Does Not Contain, Includes, Excludes or Within, relative date values, multiple currencies, or formulas using functions like ISCLONE, TIMENOW or $RecordType, so those rules must be rebuilt by hand.[^s3] Time-dependent actions map to scheduled paths in a record-triggered flow, ideally with entry conditions so they only run when needed, and Salesforce encourages reviewing and pruning unused automation before migrating rather than converting it one-for-one.[^s4] Workflow actions themselves, such as email alerts, and approval processes were explicitly not part of the retirement plan.[^s4]

## When to use it (and when not)

Do not build new automation with workflow rules; Flow is Salesforce's consolidated home for triggered automation and offers better performance, easier maintenance and execution ordering through Flow Trigger Explorer.[^s3][^s4] The only reason to touch a workflow rule now is to read it as a specification for its replacement, or to deactivate it once the replacement flow has been tested.

## Connections

Workflow rules sit under the broader **process-automation** toolset and are **replaced by record-triggered flows**, which are built in **Flow Builder**; **Process Builder** is the sibling legacy tool that reached end of support on the same date.[^s1][^s3] They **contrast with approval processes**, which run only when a user submits a record rather than firing automatically, although both draw on the same reusable action library.[^s2] Their outbound message action is the declarative entry point to **outbound messaging**, their rule evaluation is one of the legacy steps an architect must account for in the save **order of execution** until rules are migrated, and active unmigrated rules are a common item on any **technical debt** register because they no longer receive fixes.[^s2][^s1]

## Sources
[^s1]: Salesforce Help, "Salesforce Workflow Rules & Process Builder End of Support". https://help.salesforce.com/s/articleView?language=en_US&amp=&id=001096524&amp=&type=1 (accessed 2026-11-03)
[^s2]: Salesforce Developers, "Workflow: Automating the Process". https://developer.salesforce.com/docs/atlas.en-us.salesforce_workflow_cheatsheet.meta/salesforce_workflow_cheatsheet/workflow_cheatsheet.htm (accessed 2026-11-03)
[^s3]: Trailhead, "Migrate Workflows and Processes to Flows: Understand Automation Changes". https://trailhead.salesforce.com/content/learn/projects/migrate-workflows-and-processes-to-flows/understand-automation-changes (accessed 2026-11-03)
[^s4]: Salesforce Admins Blog, "Go with the Flow: What's Happening with Workflow Rules and Process Builder?". https://admin.salesforce.com/blog/2021/go-with-the-flow-whats-happening-with-workflow-rules-and-process-builder (accessed 2026-11-03)
