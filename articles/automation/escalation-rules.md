---
id: kt:escalation-rules
type: Feature
title: Escalation Rules
aliases: [Case Escalation Rules, case escalation rule, escalation rule]
domain: automation
summary: >-
  Declarative case rules that reassign a case and send notifications when it stays open past a set age,
  measured against business hours, using ordered rule entries and up to five timed escalation actions each.
release: "Winter '27"
status: current
broader: [kt:process-automation, kt:service-cloud]
related: [kt:order-of-execution, kt:workflow-rules, kt:schedule-triggered-flow]
relations:
  - {predicate: integratesWith, object: kt:queues}
  - {predicate: dependsOn, object: kt:business-hours}
  - {predicate: contrastsWith, object: kt:assignment-rules}
  - {predicate: contrastsWith, object: kt:entitlement-management}
  - {predicate: configuredVia, object: kt:metadata-api}
sources:
  - id: s1
    title: "Set Up Escalation Rules"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.rules_escalation_create.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-07
  - id: s2
    title: "Escalation Rule Entries"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=service.rules_escalation_rule_entry.htm&type=5
    type: official-docs
    accessed: 2026-11-07
  - id: s3
    title: "EscalationRules"
    publisher: Salesforce Developers (Metadata API Developer Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_escalationrules.htm
    type: official-docs
    accessed: 2026-11-07
  - id: s4
    title: "Triggers and Order of Execution"
    publisher: Salesforce Developers (Apex Developer Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm
    type: official-docs
    accessed: 2026-11-07
  - id: s5
    title: "Create a Process for Managing Support Cases: Create an Escalation Rule"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/content/learn/projects/create-a-process-for-managing-support-cases/create-an-escalation-rule
    type: official-learning
    accessed: 2026-11-07
  - id: s6
    title: "Case Management Implementation Guide (PDF)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/242/latest/en-us/sfdc/pdf/salesforce_case_implementation_guide.pdf
    type: official-docs
    accessed: 2026-11-07
created: 2026-11-07
---

# Escalation Rules

Escalation rules are Salesforce's built-in, time-based automation for **cases**. When a case that matches a rule entry stays open longer than a configured age, the platform runs escalation actions: it can reassign the case to a user or queue and email the people who need to know.[^s1][^s6] A typical example is moving unresolved Product Support cases to a Tier 2 queue after four hours and notifying the support manager.[^s5] Rules live in Setup under **Escalation Rules**, and creating or editing them requires the Customize Application permission.[^s1]

## How it works

An org can hold several escalation rules, but only one can be active at a time, so the usual design is one rule with many entries.[^s1] Entries are evaluated in sort order and evaluation stops at the first match, so Salesforce advises placing complex entries first and ending with a catch-all entry that has no criteria.[^s2] An entry's condition is either field criteria (combined with AND by default, or with custom filter logic) or a formula that returns true.[^s2]

Each entry also decides two timing questions:

- **Business hours**: ignore them, use the business hours on the case, or set a specific business hours record. Escalation only happens inside the chosen hours.[^s2]
- **Start of the clock**: when the case is created; when it is created but disabled once the case is first modified; or based on the last modification time, which restarts the clock on every edit.[^s2]

Each entry can have up to five **escalation actions** that fire over increasing periods.[^s1] An action's **Age Over** value is whole hours plus 0 or 30 minutes; the case escalates if it is still not closed once that age is reached.[^s1] An action can reassign the case to a user or queue with a notice template, notify a named user, notify the case owner, and email up to five additional addresses.[^s1][^s6] After saving a test case, admins can open **Case Escalations** in Setup and search to see the **Escalate At** time computed for it.[^s5]

## In the save and in metadata

Escalation rules are evaluated at step 12 of the order of execution, after workflow rules and before Salesforce Flow automations at step 13. If a workflow field update re-runs triggers, escalation rules aren't evaluated again, and during a recursive save Salesforce skips steps 9 through 17 entirely.[^s4] Entitlement rules are separate and run later, at step 15.[^s4]

In the Metadata API, rules are stored per object in a file such as `Case.escalationRules`. Each `RuleEntry` carries `businessHoursSource` (`None`, `Case` or `Static`), `escalationStartTime` (`CaseCreation` or `CaseLastModified`), `disableEscalationWhenModified`, and either `formula` or `criteriaItems`, never both. Each `EscalationAction` stores its delay in `minutesToEscalation`.[^s3] Salesforce recommends Classic email templates in escalation actions because Lightning email templates aren't packageable.[^s3]

## Limits and gotchas

- **One active rule.** Only one escalation rule can be active at a time, so variations belong in entries of that rule rather than in separate rules.[^s1]
- **Entry caps.** Salesforce's case implementation guide lists up to 3,000 rule entries per rule, of which up to 300 can be formula entries.[^s6]
- **First match wins.** A broad entry placed too early silently swallows cases meant for later entries.[^s2]
- **Modification-based clocks.** With "disable after first modified" any edit, even a trivial one, permanently stops escalation for that case.[^s6]
- **Business hours shift the deadline.** Because escalation only happens inside the selected business hours, the actual escalation time can fall well after the raw Age Over; check the Escalate At column when testing.[^s2][^s5]

## When to use it (and when not)

Use escalation rules for simple "open too long" safety nets: reroute stale cases to a senior queue and alert a manager.[^s5] When customers have contracted service levels, with timers per entitlement, success and violation actions, and milestone tracking on the case, **Entitlement Management** is the purpose-built tool and runs at a different point in the save.[^s4] Requirements beyond reassign-and-notify, such as updating fields or acting on other objects, usually move to scheduled paths in record-triggered flows or schedule-triggered flows.

## Connections

Escalation rules are part of Salesforce's **process automation** toolkit and a core **Service Cloud** feature.[^s6] They fire at a fixed point in the **order of execution**, right after **workflow rules**.[^s4] Their reassignment target is commonly a **queue**, and their timing depends on **business hours**.[^s1][^s2] They are often confused with **assignment rules**, which set a case's first owner at save time, while escalation rules act later based on age.[^s4] **Entitlement Management** contrasts with them as the SLA-driven alternative, **schedule-triggered flows** offer a programmable alternative, and the rules deploy through the **Metadata API** as the `EscalationRules` type.[^s3]

## Sources
[^s1]: Salesforce Help, "Set Up Escalation Rules". https://help.salesforce.com/s/articleView?id=sf.rules_escalation_create.htm&language=en_US&type=5 (accessed 2026-11-07)
[^s2]: Salesforce Help, "Escalation Rule Entries". https://help.salesforce.com/s/articleView?language=en_US&id=service.rules_escalation_rule_entry.htm&type=5 (accessed 2026-11-07)
[^s3]: Salesforce Developers, "EscalationRules", Metadata API Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_escalationrules.htm (accessed 2026-11-07)
[^s4]: Salesforce Developers, "Triggers and Order of Execution", Apex Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm (accessed 2026-11-07)
[^s5]: Trailhead, "Create a Process for Managing Support Cases: Create an Escalation Rule". https://trailhead.salesforce.com/en/content/learn/projects/create-a-process-for-managing-support-cases/create-an-escalation-rule (accessed 2026-11-07)
[^s6]: Salesforce, "Case Management Implementation Guide" (PDF). https://resources.docs.salesforce.com/242/latest/en-us/sfdc/pdf/salesforce_case_implementation_guide.pdf (accessed 2026-11-07)
