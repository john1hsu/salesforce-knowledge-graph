---
id: kt:enhanced-scheduling-and-optimization
type: Feature
title: Enhanced Scheduling and Optimization
aliases: [Enhanced S&O, ESO, Field Service Enhanced Scheduling and Optimization, Enhanced Optimization per Territory]
domain: clouds-and-products
summary: >-
  The current Field Service scheduling and optimization engine, which replaces the legacy optimization and the
  manual and semiautomatic scheduling services, runs on Hyperforce, is on by default for orgs created from
  Summer '23, and can be adopted org-wide or territory by territory.
release: "Winter '27"
status: current
broader: [kt:field-service]
related: [kt:scheduling-console, kt:field-service-scheduling-policies, kt:dispatcher-console, kt:service-appointments, kt:permission-sets]
relations:
  - {predicate: partOf, object: kt:field-service}
  - {predicate: dependsOn, object: kt:hyperforce}
  - {predicate: consumedBy, object: kt:scheduling-console}
  - {predicate: consumedBy, object: kt:dispatcher-console}
sources:
  - id: s1
    title: "Enable Enhanced Scheduling and Optimization"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.pfs_enhanced_setup_enable.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-26
  - id: s2
    title: "Set Up Enhanced Optimization for Field Service Territories"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.pfs_enhanced_optimization_per_territory.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-26
  - id: s3
    title: "Get Ready for Field Service Scheduling and Optimization"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=service.pfs_customization.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-26
  - id: s4
    title: "Configure Enhanced Optimization per Territory"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.pfs_enhanced_optimization_per_territory_configure.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-26
  - id: s5
    title: "Optimize Today's Field Service Schedule"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=service.pfs_in_day_optimization.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-26
  - id: s6
    title: "Understanding Optimization in Field Service Scheduling (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/field-service-lightning-optimization/explore-optimization
    type: official-learning
    accessed: 2026-11-26
created: 2026-11-26
---

# Enhanced Scheduling and Optimization

**Enhanced Scheduling and Optimization** (Enhanced S&O, often shortened to ESO) is the scheduling engine behind Field Service. Salesforce describes it as a more efficient architecture that improves scalability, performance and schedule quality for optimization and for the manual and semiautomatic scheduling services such as Get Candidates and Schedule.[^s1] Help states that it replaces the legacy optimization and scheduling services and runs on Hyperforce.[^s3] It is available in Enterprise, Unlimited and Developer Editions where Field Service is enabled, in both Lightning Experience and Salesforce Classic.[^s1]

## How it works

The engine applies the same scheduling model as before: a scheduling policy combines work rules, which filter out ineligible candidates, with weighted service objectives that rank the slots that remain.[^s3] Trailhead explains the optimizer's approach: it orders appointments by priority, filters candidates with work rules, grades every slot against the policy's objectives, then repeatedly unschedules and reschedules a random subset and keeps the new plan only if its overall grade improves, until the time budget ends.[^s6] That search space grows factorially; the unit's example of one worker and 11 appointments already yields 39,916,800 possible orders.[^s6]

Two practical differences stand out in the enhanced engine:

- It uses point-to-point predictive routing for travel time, whatever the routing preferences set in Field Service Settings say.[^s1]
- It authenticates as a Platform Integration User instead of the optimization user and profile that the legacy "Activate Field Service Schedule Optimization" step creates.[^s3]

Optimization comes in several scopes. Global optimization is the most thorough and can run for hours, while in-day optimization repairs today's schedule after late bookings or cancellations.[^s5] In-day runs are capped at 5 minutes with Enhanced S&O versus 10 minutes on the legacy engine, and they work best over the current day or at most 2 days.[^s5] Dispatchers start them from the dispatch console or schedule them as jobs several times a day, using a policy flagged as In-Day Optimization; Pin Criteria lists statuses that must not move, and an appointment that breaks a rule is pinned rather than optimized.[^s5]

## Setup and rollout

Orgs created from Summer '23 have Enhanced S&O enabled for all service territories by default; older orgs opt in.[^s1] Enabling it needs Field Service turned on, the latest Field Service managed package, and the Customize Application permission; the admin selects the Field Service Enhanced Scheduling and Optimization checkbox in Field Service Settings, which also turns on Field Service Integration.[^s1] Help says the engine is backward compatible, so existing implementations remain after enablement.[^s1]

Enhanced Optimization per Territory allows a gradual cutover: simpler territories move first while complex ones stay on the legacy engine.[^s2] An admin can choose the org-wide option under Scheduling > General Logic, or add the "Use enhanced scheduling and optimization" field to the service territory layout and tick it on each territory in the Field Service Admin app.[^s2][^s4] A separate setting decides which engine serves appointments and resources that have no territory.[^s2]

## Limits and gotchas

- One optimization request, bulk schedule action or batch must not mix engines: every appointment and resource territory involved has to use the same one, and the UI warns when they differ.[^s2]
- The engine is chosen by the appointment's territory for drag-and-drop, Get Candidates, Schedule, Unschedule and Check Rules; by the selected territory for global optimization; and by the resource's territory membership for absence changes.[^s2]
- The two engines can produce different schedules. Salesforce advises pinning the next day's appointments, unscheduling everything after that, and re-optimizing with the enhanced engine during off-hours to avoid double-booking.[^s4]
- All Enhanced S&O limits and limitations apply to territory-level adoption as well; Help keeps them on a dedicated limits page that should be reviewed before go-live.[^s2]
- Configuring scheduling policies needs the FSL Admin permission set, and running in-day optimization needs FSL Admin or FSL Dispatcher.[^s5]

## When to use it

For new orgs there is no choice to make: Enhanced S&O is already the engine.[^s1] Older orgs on the legacy engine should plan the move territory by territory, because Help positions the enhanced engine as the replacement for the legacy services.[^s3][^s2] Keep a complex territory on the legacy engine only while its rules and objectives are retested against the enhanced engine's behaviour.[^s2][^s4]

## Connections

Enhanced S&O is **part of** `kt:field-service` and **depends on** `kt:hyperforce`, where the service runs.[^s3] It evaluates the work rules and objectives of `kt:field-service-scheduling-policies` to place `kt:service-appointments`.[^s3][^s6] It is **consumed by** the classic `kt:dispatcher-console`, from which in-day optimization is launched.[^s5] The newer `kt:scheduling-console` is the other dispatcher workspace that consumes it; its own node covers that dependency. Access for dispatchers and admins is granted through `kt:permission-sets` such as FSL Admin, FSL Dispatcher and Field Service Integration.[^s3][^s5]

## Sources

[^s1]: Salesforce Help, "Enable Enhanced Scheduling and Optimization". https://help.salesforce.com/s/articleView?id=sf.pfs_enhanced_setup_enable.htm&language=en_US&type=5 (accessed 2026-11-26)
[^s2]: Salesforce Help, "Set Up Enhanced Optimization for Field Service Territories". https://help.salesforce.com/s/articleView?id=sf.pfs_enhanced_optimization_per_territory.htm&language=en_US&type=5 (accessed 2026-11-26)
[^s3]: Salesforce Help, "Get Ready for Field Service Scheduling and Optimization". https://help.salesforce.com/s/articleView?id=service.pfs_customization.htm&language=en_US&type=5 (accessed 2026-11-26)
[^s4]: Salesforce Help, "Configure Enhanced Optimization per Territory". https://help.salesforce.com/s/articleView?id=sf.pfs_enhanced_optimization_per_territory_configure.htm&language=en_US&type=5 (accessed 2026-11-26)
[^s5]: Salesforce Help, "Optimize Today's Field Service Schedule". https://help.salesforce.com/s/articleView?id=service.pfs_in_day_optimization.htm&language=en_US&type=5 (accessed 2026-11-26)
[^s6]: Trailhead, "Understanding Optimization in Field Service Scheduling". https://trailhead.salesforce.com/content/learn/modules/field-service-lightning-optimization/explore-optimization (accessed 2026-11-26)
