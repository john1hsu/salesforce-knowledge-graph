---
id: kt:field-service
type: Product
title: Field Service
aliases: [Salesforce Field Service, Field Service Lightning, FSL, Field Service and Operations]
domain: clouds-and-products
summary: >-
  Salesforce's product for planning, scheduling and executing on-site work, built on work orders, service appointments,
  service resources and service territories, with a scheduling and optimization engine, a dispatcher console and a mobile app for technicians.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:service-cloud, kt:entitlement-management, kt:omni-channel, kt:my-domain]
relations:
  - {predicate: hasPart, object: kt:work-orders}
  - {predicate: hasPart, object: kt:service-appointments}
  - {predicate: hasPart, object: kt:field-service-scheduling-policies}
  - {predicate: hasPart, object: kt:dispatcher-console}
  - {predicate: hasPart, object: kt:field-service-mobile-app}
  - {predicate: integratesWith, object: kt:service-cloud}
sources:
  - id: s1
    title: "Field Service Basics: Enable Field Service and Create Service Territories (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/field_service_basics/field_service_basics_enable
    type: official-learning
    accessed: 2026-11-03
  - id: s2
    title: "Field Service Basics: Set Up Users, Service Resources and Dispatchers (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/field_service_basics/field_service_basics_set
    type: official-learning
    accessed: 2026-11-03
  - id: s3
    title: "Field Service Core Data Model (Field Service Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.field_service_dev.meta/field_service_dev/fsl_dev_soap_core.htm
    type: official-docs
    accessed: 2026-11-03
  - id: s4
    title: "Explore Scheduling (Field Service Scheduling Basics, Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/field-service-lightning-scheduling-basics/explore-scheduling
    type: official-learning
    accessed: 2026-11-03
  - id: s5
    title: "Explore Optimization (Field Service Optimization, Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/field-service-lightning-optimization/explore-optimization
    type: official-learning
    accessed: 2026-11-03
  - id: s6
    title: "Work from Anywhere (Field Service Mobile, Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/field-service-mobile/work-from-anywhere
    type: official-learning
    accessed: 2026-11-03
created: 2026-11-03
---

# Field Service

Field Service is Salesforce's product for managing a mobile workforce that performs work at customer sites: installing equipment, repairing assets, running inspections and similar jobs. Trailhead now frames it as part of "Field Service and Operations," built on three foundations: service territories that bound where work happens, operating hours that define when it can happen, and the mobile workers who do it.[^s1] It extends the case-centric service model of Service Cloud into scheduling, dispatch and on-site execution.

## How it works

**Enablement.** An admin turns the product on from Field Service Settings in Setup, which hands off to Salesforce Go, a guided launchpad that automates the main configuration steps. Turning it on activates both the core objects and the Field Service managed package, and unlocks work orders, service appointments and asset management.[^s1]

**Data model.** The core objects form a chain from "what needs doing" to "who does it, where and when":[^s3]

- A **work order** describes work for a customer and can link to an account, contact, asset, case, entitlement or service contract, and to one service territory. **Work order line items** split it into subtasks or billable pieces.[^s3]
- A **work type** is a reusable template that sets expected duration and required skills, and can auto-create a child service appointment.[^s3]
- A **service appointment** is the scheduled visit, with an arrival window, scheduled start and end and duration. Its parent is usually a work order or line item, but it can also hang off an account, asset, lead or opportunity.[^s3]
- A **service resource** is a technician (or, with the Crew resource type, a crew). **Assigned resource** records connect resources to appointments, and **service resource skills** record certifications and skill levels that work types require.[^s3]
- A **service territory** is a geographic or functional area; **service territory members** link resources to one or more territories. **Operating hours**, refined by time slots, can be set on accounts, territories and territory members. Resource capacity, absences and preferences (preferred, required or excluded) round out the model.[^s3]

Territories need not be geographic: Trailhead notes they can be functional, virtual (for remote work) or even mobile, such as a technician's van.[^s1] Each technician is a user linked to a service resource record that carries a territory lookup, and a separate dispatcher role grants access to the dispatcher console.[^s2]

## Scheduling and optimization

The scheduling engine takes a job's required skills, location and window (earliest start to due date), finds qualified, available resources and then picks the slot and worker that best fit business priorities.[^s4] What "best" means is set by a **scheduling policy**, made of two building blocks: **work rules**, pass/fail filters (skills, availability, territory) that remove ineligible candidates, and **service objectives**, which rank the survivors, for example by minimizing travel.[^s4]

Each objective grades every candidate-and-slot pair; the optimizer multiplies grades by the objective's weight and adds the appointment's priority value to get a score. Priority comes from work order, line item or appointment priority fields, on a default 1–10 scale where 1 is highest (a 1–100 scale is also available).[^s5] Global optimization exists because brute force is hopeless: one worker with 11 appointments already has 39,916,800 possible orderings, so the optimizer builds a graded schedule and then repeatedly unschedules and reschedules random appointments, keeping changes only when the overall grade improves until its time budget runs out.[^s5] Trailhead names in-day optimization, resource schedule optimization and Enhanced Scheduling and Optimization as further options, documented separately.[^s5]

Dispatchers work in the **dispatcher console**, whose four elements are the appointment list, scheduling actions, a mobile worker availability chart and an interactive map, with a Gantt timeline of every appointment. The classic console is now accompanied by a newer Scheduling Console.[^s4]

## Mobile execution

Technicians use the Field Service mobile app for iOS and Android, logging in through the org's My Domain. It shows the day's schedule, a calendar, a map with driving directions and quick actions; work order detail is split into overview, details, related and feed panes, and workers can check inventory, review asset service history, attach before-and-after photos and complete the job from the device.[^s6]

## When to use it (and gotchas)

Use Field Service when the unit of work is a visit that must be matched to a qualified person, a place and a time window; for routing inbound cases or chats to agents at desks, Omni-Channel is the fit instead.[^s4][^s3] Scheduling quality depends on clean master data: inaccurate skills, territory memberships, operating hours or absences directly shrink or distort the candidate pool that work rules produce.[^s4][^s5] Because part of the product ships as a managed package, plan for package-level configuration alongside standard objects.[^s1]

## Connections

Field Service sits on the **Salesforce Platform** (broader) and **integrates with Service Cloud**, since work orders reference cases, accounts, assets and entitlements.[^s3] Entitlements can carry operating hours that define when a customer may be served, linking it to **entitlement management**.[^s3] It **has parts** for work orders, service appointments, scheduling policies, the dispatcher console and the mobile app,[^s4][^s6] and the mobile login relies on **My Domain**.[^s6] It is related to **Omni-Channel** as the desk-side counterpart for routing work to people.

## Sources
[^s1]: Trailhead, "Field Service Basics: Enable Field Service and Create Service Territories". https://trailhead.salesforce.com/content/learn/modules/field_service_basics/field_service_basics_enable (accessed 2026-11-03)
[^s2]: Trailhead, "Field Service Basics: Set Up Users, Service Resources and Dispatchers". https://trailhead.salesforce.com/content/learn/modules/field_service_basics/field_service_basics_set (accessed 2026-11-03)
[^s3]: Salesforce, "Field Service Core Data Model". https://developer.salesforce.com/docs/atlas.en-us.field_service_dev.meta/field_service_dev/fsl_dev_soap_core.htm (accessed 2026-11-03)
[^s4]: Trailhead, "Explore Scheduling". https://trailhead.salesforce.com/content/learn/modules/field-service-lightning-scheduling-basics/explore-scheduling (accessed 2026-11-03)
[^s5]: Trailhead, "Explore Optimization". https://trailhead.salesforce.com/content/learn/modules/field-service-lightning-optimization/explore-optimization (accessed 2026-11-03)
[^s6]: Trailhead, "Work from Anywhere (Field Service Mobile)". https://trailhead.salesforce.com/content/learn/modules/field-service-mobile/work-from-anywhere (accessed 2026-11-03)
