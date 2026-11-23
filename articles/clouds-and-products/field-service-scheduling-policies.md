---
id: kt:field-service-scheduling-policies
type: Feature
title: Field Service Scheduling Policies
aliases: [scheduling policy, scheduling policies, Field Service scheduling policy, work rules and service objectives, FSL scheduling policy]
domain: clouds-and-products
summary: >-
  The configurable rule sets that tell the Field Service scheduling engine how to place service appointments:
  pass/fail work rules filter out ineligible mobile workers, and weighted service objectives rank the remaining
  candidates and time slots.
release: "Winter '27"
status: current
broader: [kt:field-service]
related: [kt:dispatcher-console, kt:service-appointments, kt:scheduling-console, kt:enhanced-scheduling-and-optimization, kt:public-sector-solutions, kt:batch-apex]
relations:
  - {predicate: partOf, object: kt:field-service}
  - {predicate: consumedBy, object: kt:dispatcher-console}
  - {predicate: consumedBy, object: kt:public-sector-solutions}
  - {predicate: dependsOn, object: kt:enhanced-scheduling-and-optimization}
sources:
  - id: s1
    title: "Examine Scheduling Policies (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/field-service-lightning-scheduling-basics/examine-scheduling-policies
    type: official-learning
    accessed: 2026-11-23
  - id: s2
    title: "Customize a Scheduling Policy (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/field-service-lightning-scheduling-basics/customize-a-scheduling-policy
    type: official-learning
    accessed: 2026-11-23
  - id: s3
    title: "ScheduleService Class | Field Service Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/service/field-service-dev/guide/apex-class-fsl-scheduleservice.html
    type: official-docs
    accessed: 2026-11-23
  - id: s4
    title: "Discover the Workforce Scheduling Architecture (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/fr/content/learn/modules/workforce-scheduling-for-field-service-and-operations/discover-the-workforce-scheduling-architecture
    type: official-learning
    accessed: 2026-11-23
created: 2026-11-23
---

# Field Service Scheduling Policies

A **scheduling policy** is the instruction set the Field Service scheduling engine follows when it decides who should do a job and when. Each policy combines two kinds of building blocks: **work rules**, which are pass/fail filters that remove mobile workers who can't take the job, and **service objectives**, which rank the workers and slots that survive the filters.[^s1] Dispatchers choose which policy to apply and can change it during the day, and Apex scheduling calls take a policy id, so the policy is where an organization encodes its trade-off between customer preference, speed and travel cost.[^s2][^s3]

## How it works

**Work rules** are evaluated one at a time, for example territory first and then skills, and any candidate who fails a rule drops out.[^s1] Rules named in Trailhead include Match Skills, Required Resource, Excluded Resource and Service Appointment Visiting Hours.[^s1] Three rules are described as mandatory for a working policy: Service Resource Availability, Earliest Start Permitted and Due Date Match Time.[^s1] Variants of a rule type can carry their own settings; Trailhead's example adds a lunch-break availability rule with a 12:00 start and a 45-minute duration.[^s1]

**Service objectives** then rank the remaining options. Each objective in a policy has a weight, and a higher weight makes the engine favour that goal more strongly; admins set weights with sliders, and a pie chart shows each objective's relative share.[^s2] Trailhead lists ten objectives: ASAP, Group Nearby Service Appointments, Minimize Gaps, Minimize Overtime, Minimize Travel, Preferred Resource, Resource Priority, Same Site, Skill Level and Skill Preference.[^s1] Four of them (Group Nearby, Minimize Gaps, Same Site and Skill Preference) need Enhanced Scheduling and Optimization, which Trailhead says is on by default in orgs created after Summer '23.[^s1] With that engine, candidates collect penalty points and the lowest penalty wins; the legacy engine instead awards points and picks the highest reward.[^s1]

## Out-of-the-box policies

Orgs ship with several ready-made policies, which Trailhead summarizes as follows.[^s2]

- **Customer First** ranks by the customer's preferred worker, then ASAP, then travel; it suits an ordinary day.[^s2]
- **High Intensity** puts minimal travel and grouped appointments ahead of ASAP to maximize completed jobs, for example during a storm.[^s2]
- **Soft Boundaries** behaves like Customer First but lets workers cover neighbouring territories, which helps small urban territories.[^s2]
- **Emergency** works with the Emergency Chatter action to dispatch urgent jobs, such as a person trapped in an elevator.[^s2]

Dispatchers can switch policy during the day, and the recommended way to customize is to clone Customer First in the Field Service Admin app's guided setup (Customize Scheduling Policies) and edit the copy, which leaves the original untouched.[^s2] In the clone, rules are moved in or out of a Selected Rules list; Trailhead swaps a lunch-aware availability rule in for the standard one rather than keeping both.[^s2]

## Using policies from code

The `FSL.ScheduleService` Apex class takes a policy record id as an argument. `schedule(policyId, serviceAppointmentId)` books one appointment into the best-scoring slot and does nothing if no slot is available; for many appointments the docs recommend an Apex batch class that schedules one appointment per batch.[^s3] `scheduleExtended` handles complex work chains, and `scheduleHere` books a chosen slot and resource but fails unless Enhanced Scheduling and Optimization is on.[^s3] The guide advises avoiding DML earlier in the same transaction, since scheduling can trigger a callout.[^s3] The running user needs a Field Service Admin, Dispatcher, Call Center or Self-Service permission set; event-triggered scheduling runs as the Automated Process user by default, which lacks them.[^s3]

## Gotchas

- Drag-and-drop on the Gantt can break work rules, flagged with a yellow triangle, while automatic scheduling always honours them.[^s1]
- Objectives pull against each other: ASAP can add travel time, so weights need deliberate tuning.[^s1]
- Test weight changes in a sandbox before production, because small shifts can change which worker wins.[^s2]
- Duplicating overlapping rules, such as two availability rules, can conflict; replace rather than add.[^s2]

## Connections

Scheduling policies are **part of** `kt:field-service` and are **consumed by** `kt:dispatcher-console`, the dispatcher's workspace where policies are switched during the day; the newer `kt:scheduling-console` is a related dispatch workspace.[^s2] They decide where `kt:service-appointments` land, and several objectives **depend on** `kt:enhanced-scheduling-and-optimization`.[^s1] `kt:public-sector-solutions` reuses the same model in Workforce Scheduling, where policies define eligibility rules and objectives for field and on-site work, either separately or in one shared policy.[^s4] Bulk scheduling from code pairs `FSL.ScheduleService` with `kt:batch-apex`.[^s3]

## Sources
[^s1]: Trailhead, "Examine Scheduling Policies". https://trailhead.salesforce.com/content/learn/modules/field-service-lightning-scheduling-basics/examine-scheduling-policies (accessed 2026-11-23)
[^s2]: Trailhead, "Customize a Scheduling Policy". https://trailhead.salesforce.com/content/learn/modules/field-service-lightning-scheduling-basics/customize-a-scheduling-policy (accessed 2026-11-23)
[^s3]: Salesforce Developers, "ScheduleService Class". https://developer.salesforce.com/docs/service/field-service-dev/guide/apex-class-fsl-scheduleservice.html (accessed 2026-11-23)
[^s4]: Trailhead, "Workforce Scheduling: Architecture, Objects, and Roles". https://trailhead.salesforce.com/fr/content/learn/modules/workforce-scheduling-for-field-service-and-operations/discover-the-workforce-scheduling-architecture (accessed 2026-11-23)
