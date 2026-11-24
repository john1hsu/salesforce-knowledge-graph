---
id: kt:rough-order-of-magnitude-estimate
type: Concept
title: Rough Order of Magnitude Estimate
aliases: [ROM, ROM estimate, rough order of magnitude, ballpark estimate]
domain: architecture-practice
summary: >-
  A quick, early, range-based estimate of the services, people and cost a Salesforce implementation is likely to
  need, produced after discovery and before a proposal or statement of work. It sets expectations and supports go/no-go
  and option comparisons, but it is never a budget-quality or contractual figure.
release: "Winter '27"
status: concept
broader: [kt:project-estimation]
related: [kt:statement-of-work, kt:requirements-gathering, kt:total-cost-of-ownership, kt:proof-of-concept, kt:risk-and-assumption-logs]
relations:
  - {predicate: dependsOn, object: kt:requirements-gathering}
  - {predicate: enables, object: kt:build-vs-buy-decisions}
  - {predicate: contrastsWith, object: kt:life-cycle-cost-estimate}
sources:
  - id: s1
    title: "Understand Statements of Work (Statement of Work Best Practices)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/sow-best-practices/understand-a-sow
    type: official-learning
    accessed: 2026-11-24
  - id: s2
    title: "Cost Estimating and Assessment Guide: Types of Cost Estimates (GAO-20-195G)"
    publisher: U.S. Government Accountability Office
    url: https://gaoinnovations.gov/cost-guide/types-of-cost-estimates.html
    type: government
    accessed: 2026-11-24
  - id: s3
    title: "Define a Feasible Scope for Your Pro Bono Project (Pro Bono Project Management)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/pro-bono-project-management/define-a-feasible-scope-for-your-pro-bono-project
    type: official-learning
    accessed: 2026-11-24
created: 2026-11-24
---

# Rough Order of Magnitude Estimate

A rough order of magnitude (ROM) estimate is the first priced view of a Salesforce implementation: a deliberately coarse answer to "roughly what will this take, and roughly what will it cost?" In Salesforce's partner training it is the second of four phases in the implementation sales process, after discovery and before the proposal and the statement of work.[^s1] The consultant uses what discovery revealed about the customer's business and the value of the project to name the likely services, the personnel required and a range of costs, with the stated aim of setting the customer's expectations and deciding what happens next.[^s1] The term is general estimating language rather than a Salesforce product, and the U.S. Government Accountability Office (GAO) defines it in much the same way.[^s2]

## What a ROM is (and is not)

GAO's cost guide treats the ROM as a quick estimate built when few details are available. It is usually derived from historical information and can be produced by one person or a small group in hours, days or weeks.[^s2] It may cover only part of the life cycle cost, and it is useful for what-if analysis and for checking whether high-level alternatives are feasible.[^s2] GAO is explicit about its main limit: a ROM "should never be considered a budget-quality cost estimate."[^s2] GAO likens it to the conceptual estimate in OMB terminology, and contrasts it with a full program office estimate, which needs a large team, can take many months and becomes the basis of the budget.[^s2]

The same pattern holds in a Salesforce sales cycle. A ROM is a range, not a price. The proposal that follows carries a more precise cost estimate, and only the statement of work commits to activities, timelines, costs and deliverables.[^s1]

## How it is produced in practice

The inputs are the outputs of discovery: business goals, the rough scope of clouds and features, and known integrations, data and change-management needs.[^s1] Where requirements are already written as user stories, Trailhead's volunteer project guidance has the team estimate time requirement by requirement, admits the exercise is closer to art than science, and advises leaning conservative.[^s3] Requirements that do not fit the available effort are then split into in-scope work and work deferred to a later phase.[^s3] A ROM applies that thinking at a coarser grain. It sizes groups of capabilities, and typically leans on historical data from similar past projects rather than detailed design.[^s2]

## Gotchas

Treating a ROM as a commitment is the classic failure. GAO stresses that a ROM is built from few details and is not budget quality, so it should not be read as a price.[^s2] Trailhead's worked example shows how the number shifts even at the SOW stage. A first SOW of US$300,000 met a customer budget of US$275,000. The gap closed by dropping one of three initiatives and moving some work in-house.[^s1] Since the ROM's stated job is to set expectations, an early figure that anchors the customer too low makes those later conversations harder.[^s1]

## When to use it

Use a ROM early, when a customer or internal sponsor needs to know whether a project is worth pursuing, or when several solution options need to be compared quickly before investing in detailed design.[^s2] Move to a detailed, bottom-up estimate once scope is stable enough to commit to, because proposals and SOWs carry contractual weight that a ROM cannot bear.[^s1]

## Connections

A ROM **depends on** `kt:requirements-gathering`, since discovery supplies everything it sizes.[^s1] It feeds the `kt:statement-of-work`, which replaces its range with committed costs and deliverables.[^s1] Its feasibility checks across high-level alternatives **enable** `kt:build-vs-buy-decisions`, and a `kt:proof-of-concept` is one way to test an option before its estimate is firmed up.[^s2] Because it may cover only part of the life cycle, it is a narrower figure than `kt:total-cost-of-ownership`, and it **contrasts with** the full `kt:life-cycle-cost-estimate` that GAO treats as the budget baseline.[^s2] The assumptions behind its range are natural entries for the project's `kt:risk-and-assumption-logs`.[^s2] It sits under `kt:project-estimation` as the earliest and least precise estimate in that discipline.[^s2]

## Sources
[^s1]: Salesforce Trailhead, "Understand Statements of Work", Statement of Work Best Practices. https://trailhead.salesforce.com/content/learn/modules/sow-best-practices/understand-a-sow (accessed 2026-11-24)
[^s2]: U.S. Government Accountability Office, "Types of Cost Estimates", Cost Estimating and Assessment Guide (GAO-20-195G). https://gaoinnovations.gov/cost-guide/types-of-cost-estimates.html (accessed 2026-11-24)
[^s3]: Salesforce Trailhead, "Define a Feasible Scope for Your Pro Bono Project", Pro Bono Project Management. https://trailhead.salesforce.com/content/learn/modules/pro-bono-project-management/define-a-feasible-scope-for-your-pro-bono-project (accessed 2026-11-24)
