---
id: kt:cutover-plan
type: Concept
title: Cutover Plan
aliases: [cutover, go-live cutover, cutover strategy, cutover runbook, mock cutover, cutover weekend]
domain: architecture-practice
summary: >-
  The sequenced, owner-assigned runbook for switching a business from its old system to a new Salesforce solution:
  freeze, final data loads, deployment, verification, a go/no-go decision and a tested rollback path.
release: "Winter '27"
status: concept
broader: [kt:release-management, kt:application-lifecycle-management]
related: [kt:data-migration-strategy, kt:hypercare, kt:user-acceptance-testing, kt:environment-strategy, kt:sharing-recalculation, kt:change-management-and-adoption]
relations:
  - {predicate: dependsOn, object: kt:rollback-plan}
  - {predicate: dependsOn, object: kt:go-live-readiness-assessment}
sources:
  - id: s1
    title: "Transition to new solutions successfully with the cutover process"
    publisher: Microsoft Learn (Dynamics 365 implementation guide)
    url: https://learn.microsoft.com/dynamics365/guidance/implementation-guide/prepare-go-live-cutover-strategy
    type: partner
    accessed: 2026-11-23
  - id: s2
    title: "Manage the Launch and Post-Launch Activities"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/cc-project-mgmt/cc-launch-and-post-launch
    type: official-learning
    accessed: 2026-11-23
  - id: s3
    title: "Deferred Sharing Calculations (Designing Record Access for Enterprise Scale)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/draes/guide/draes-tools-deferred-sharing-maintenance.html
    type: official-docs
    accessed: 2026-11-23
  - id: s4
    title: "Cutover stage (Best practices for cutting over network traffic to AWS)"
    publisher: AWS Prescriptive Guidance
    url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-migration-cutover/cutover-stage.html
    type: partner
    accessed: 2026-11-23
created: 2026-11-23
---

# Cutover Plan

A cutover is the moment a business stops working in its old system and starts working in the new one, and the cutover plan is the script for that moment. Microsoft's implementation guidance describes cutover as the last step before a new business application launches, a window (often a weekend of under 48 hours) in which neither the legacy nor the new system is fully usable.[^s1] On a Salesforce program the same idea covers the final metadata deployment, the last data loads, integration switch-over and user enablement. Salesforce's own delivery methodology calls the equivalent artifacts the rollout and rollback steps of a launch plan, written by a functional architect and run step by step on launch day.[^s2]

## What a cutover plan contains

A usable plan is a task list, not a narrative. Microsoft lists the elements every plan needs: the order and timing of each task, a named owner plus a backup owner, the instructions and tools for the task, how it is verified and signed off, and a rollback plan if something fails.[^s1] Trailhead's launch unit adds two companions. One is a communication plan naming who to contact in which order, with roles, availability, and who may declare the rollout a success or order a rollback. The other is a launch checklist in which every item has an owner.[^s2]

A typical Salesforce sequence runs: announce and start a change freeze; stop or drain legacy writes and integrations; take a final backup or extract; deploy and validate the release; run the final data loads in dependency order; recalculate sharing; switch integrations and single sign-on; smoke-test with business users; then go or roll back. AWS's guidance for cloud migrations uses the same skeleton (ingestion freeze, final backup, final data sync, routing changes, testing) and notes that the final backup doubles as the rollback source.[^s4]

## Rehearse it: the mock cutover

Plans fail on timing, so the plan has to be run before it is used. Microsoft recommends a mock cutover, a dress rehearsal in a test environment with the same data volumes, tools, people, steps and timings as the real event, repeated until it runs cleanly, with the plan updated after each run.[^s1] The Trailhead example likewise runs a launch dry run and separately tests the rollback procedure, which it calls the emergency brake.[^s2] For Salesforce the natural rehearsal target is a recently refreshed full sandbox, because only it reproduces production data volumes and therefore realistic load and sharing times.[^s3]

## Salesforce-specific gotchas

- **Sharing recalculation can blow the window.** Large role, group or sharing-rule changes can trigger long evaluations or timeouts.[^s3]
- **Defer calculations deliberately.** Deferred sharing calculation lets an admin suspend group-membership or sharing-rule processing, apply every change at once, resume, and then run a full recalculation.[^s3]
- **Not everything defers.** Some recalculations cannot be deferred for data-integrity reasons, and group membership locking can still occur while deferred.[^s3]
- **Pick the window around the business.** Avoid busy trading periods, month-end or year-end close, and holidays when key people are away; build in buffer time.[^s1]
- **Hard-coded endpoints bite.** AWS names hard-coded addresses as the main switch-over risk; on Salesforce the analogue is named credentials and remote endpoints still pointing at sandbox systems.[^s4]
- **Vendor lead times.** In the Trailhead example the go-live ticket goes to the vendor's support team about two weeks before launch.[^s2]

## Go/no-go and rollback

Before execution the plan should pass entrance criteria: approved data migration, testing, training, support and cutover plans; testing done with issues fixed or accepted; a working production environment.[^s1] A go/no-go meeting then applies criteria agreed in advance, such as how many open defects are tolerable and how they will be worked around.[^s1] During execution, AWS advises defining checkpoints at which predefined conditions trigger rollback, and naming one person who decides between fixing forward and rolling back.[^s4] Rolling back gets harder once users have written new data to the target, so the point of no return should be explicit in the plan.[^s4]

## When to use it

Every go-live that replaces a live process needs a cutover plan: a new org replacing a legacy CRM, an org merge, or a large realignment of roles and sharing in an existing org.[^s3] Small releases on an established org usually fold the same steps into routine release management instead. A phased cutover that shifts users or regions over time lowers risk and speeds rollback, at the cost of running both systems longer.[^s4]

## Connections

The cutover plan sits **broader** under release management and application lifecycle management, as the production-launch step of a release.[^s1] It **depends on** a rollback plan, the tested way back if a checkpoint fails,[^s2][^s4] and on a go-live readiness assessment, the entrance criteria and go/no-go decision that authorize execution.[^s1] It is **related** to data migration strategy, whose final loads run inside the cutover window,[^s4] and to sharing recalculation, whose duration often sets the window's length.[^s3] User acceptance testing and environment strategy supply the signed-off build and the full sandbox for mock cutovers;[^s1][^s3] change management and adoption owns the communication plan;[^s2] and hypercare begins the moment the cutover completes and support transitions.[^s1][^s2]

## Sources

[^s1]: Microsoft Learn, "Transition to new solutions successfully with the cutover process" (Dynamics 365 implementation guide). https://learn.microsoft.com/dynamics365/guidance/implementation-guide/prepare-go-live-cutover-strategy (accessed 2026-11-23)
[^s2]: Trailhead, "Manage the Launch and Post-Launch Activities". https://trailhead.salesforce.com/content/learn/modules/cc-project-mgmt/cc-launch-and-post-launch (accessed 2026-11-23)
[^s3]: Salesforce Developers, "Deferred Sharing Calculations" (Designing Record Access for Enterprise Scale). https://developer.salesforce.com/docs/platform/draes/guide/draes-tools-deferred-sharing-maintenance.html (accessed 2026-11-23)
[^s4]: AWS Prescriptive Guidance, "Cutover stage". https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-migration-cutover/cutover-stage.html (accessed 2026-11-23)
