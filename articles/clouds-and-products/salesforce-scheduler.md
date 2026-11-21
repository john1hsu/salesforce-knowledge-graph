---
id: kt:salesforce-scheduler
type: Product
title: Salesforce Scheduler
aliases: [Lightning Scheduler, Scheduler, LxScheduler]
domain: clouds-and-products
summary: >-
  Salesforce's extra-cost appointment-booking product that matches customers with the right service resource,
  location, topic and time slot, built on service territories, work type groups, work types and service appointments.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:field-service, kt:financial-services-cloud, kt:apex]
relations:
  - {predicate: integratesWith, object: kt:field-service}
  - {predicate: dependsOn, object: kt:service-appointments}
  - {predicate: dependsOn, object: kt:operating-hours}
  - {predicate: queriedWith, object: kt:connect-api}
  - {predicate: integratesWith, object: kt:platform-events}
sources:
  - id: s1
    title: "Introduction to Salesforce Scheduler"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/service/salesforce-scheduler-dev-guide/guide/salesforce-scheduler-intro.html
    type: official-docs
    accessed: 2026-11-21
  - id: s2
    title: "Salesforce Scheduler Standard Objects"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/service/salesforce-scheduler-dev-guide/guide/salesforce-scheduler-objects-overview.html
    type: official-docs
    accessed: 2026-11-21
  - id: s3
    title: "Get Started with Salesforce Scheduler"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/set-up-salesforce-scheduler/salesforce-scheduler-get-started
    type: official-learning
    accessed: 2026-11-21
  - id: s4
    title: "Explore Appointment Topics and Templates"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lightning-scheduler-data-model/explore-appointment-topics-and-templates
    type: official-learning
    accessed: 2026-11-21
  - id: s5
    title: "LxScheduler Namespace"
    publisher: Salesforce Developers (Apex Reference Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_namespace_lxscheduler.htm
    type: official-docs
    accessed: 2026-11-21
  - id: s6
    title: "WorkTypeGroup"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/service/salesforce-scheduler-dev-guide/guide/sforce-api-objects-worktypegroup.html
    type: official-docs
    accessed: 2026-11-21
created: 2026-11-21
---

# Salesforce Scheduler

Salesforce Scheduler, which Salesforce previously called Lightning Scheduler, is the platform's product for booking customer appointments with the right person, at the right place and time, whether the meeting happens in person, by phone or by video.[^s1] It is sold as an extra-cost add-on in Lightning Experience and is available in Enterprise, Unlimited, Performance and Developer editions.[^s2] Trailhead positions it for embedding appointment booking into everyday CRM work such as leads and referrals, opportunities and accounts, and distinguishes inbound scheduling (customers booking with an organization's agents) from outbound scheduling (agents booking with customers).[^s3]

## How it works

Scheduler models an appointment as the intersection of who, where, what and when. The developer guide lays out setup as a sequence: create service resources (the attendees) with their skills, locations and availability; define service territories for the branches or offices where they meet customers; create work type groups as appointment topics such as a home loan or an investment review; create work types as templates that tie topics to locations and set duration, buffers and availability; and finally book appointments.[^s1]

The work type is the template that does most of the configuration. It defines the skills an advisor needs for a topic (with a minimum skill level), links topics to territories so you can see which branches handle a topic, and sets appointment duration, the range of bookable slots, and preparation and wrap-up buffers. Junction objects carry those links: Work Type Group Member joins a template to a topic, Service Territory Work Type joins it to a location, and Skill Requirement attaches a required skill or certification.[^s4] Operating hours and time slots can optionally narrow when the specialists for a topic are available during the day or week.[^s4]

The data model is shared with Field Service, and those standard objects make up Scheduler's core features.[^s2] Key objects include:

- **ServiceAppointment, AssignedResource and ServiceAppointmentAttendee**: the booking, the resources assigned to it, and the leads, contacts or person accounts on a group appointment.[^s2]
- **ServiceResource, ServiceTerritory and ServiceTerritoryMember**: the technician or asset, the region where work happens, and the resource's membership in that region.[^s2]
- **OperatingHours and TimeSlot**: availability windows for territories, resources or accounts, where operating hours are built from one or more weekday time slots.[^s2]
- **ResourceAbsence and Holiday**: periods when a resource can't work or can't be scheduled.[^s2]
- **AppointmentInvitation, Waitlist and WaitlistParticipant**: invitation links customers use to book, and queues for walk-in customers without an appointment.[^s2]

WorkTypeGroup itself was added in API version 45.0, can only be used once Scheduler is enabled, and has an IsActive flag that controls whether the group can be used for scheduling.[^s6]

## Extending it

For developers, Scheduler exposes REST APIs, Connect REST APIs, platform events and Apex classes.[^s1] The Apex `LxScheduler` namespace provides input builders for finding appointment candidates and time slots for a work type group and territories, plus the `ServiceResourceScheduleHandler` interface, which lets an implementing class check external calendar events so that slots already booked elsewhere are treated as unavailable. Unavailable slots are returned in UTC even when operating hours span time zones.[^s5]

## Limits and gotchas

- **One work type per group per territory**: an admin can map only one work type from a given work type group to any one service territory.[^s4]
- **Shared objects with Field Service**: Scheduler reuses Field Service's standard objects, so plan customizations on them with both products in mind.[^s2]
- **Licensing**: Scheduler costs extra, so a plain Service or Sales Cloud org doesn't include it.[^s2]
- **Hands-on practice**: the Trailhead setup project needs a special Developer Edition org that ships with Scheduler and sample data.[^s3]

## When to use it

Pick Scheduler when customers or reps need to book time with a qualified person at a branch or over video. The docs' own examples are branch advisors handling topics such as home loans or investments, and waitlists for walk-in customers.[^s1][^s2] When the problem is dispatching mobile workers to customer sites, use Field Service, which shares the same territory, resource and appointment objects but adds dispatch and mobile execution.[^s2]

## Connections

Scheduler sits on the `kt:salesforce-platform` as a separately licensed product. It **integrates with** `kt:field-service` through the shared appointment, resource and territory objects.[^s2] It **depends on** `kt:service-appointments` as the record each booking creates, and on `kt:operating-hours` to define when resources and territories are available.[^s2] Developers **query it with** the `kt:connect-api` and react to it through `kt:platform-events`.[^s1] `kt:apex` adds external-calendar availability checks via the LxScheduler namespace.[^s5] Its branch, home-loan and investment examples are banking scenarios, which relates it to `kt:financial-services-cloud`.[^s4]

## Sources
[^s1]: Salesforce Developers, "Introduction to Salesforce Scheduler". https://developer.salesforce.com/docs/service/salesforce-scheduler-dev-guide/guide/salesforce-scheduler-intro.html (accessed 2026-11-21)
[^s2]: Salesforce Developers, "Salesforce Scheduler Standard Objects". https://developer.salesforce.com/docs/service/salesforce-scheduler-dev-guide/guide/salesforce-scheduler-objects-overview.html (accessed 2026-11-21)
[^s3]: Trailhead, "Get Started with Salesforce Scheduler". https://trailhead.salesforce.com/content/learn/projects/set-up-salesforce-scheduler/salesforce-scheduler-get-started (accessed 2026-11-21)
[^s4]: Trailhead, "Explore Appointment Topics and Templates". https://trailhead.salesforce.com/content/learn/modules/lightning-scheduler-data-model/explore-appointment-topics-and-templates (accessed 2026-11-21)
[^s5]: Salesforce Developers, "LxScheduler Namespace" (Apex Reference Guide). https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_namespace_lxscheduler.htm (accessed 2026-11-21)
[^s6]: Salesforce Developers, "WorkTypeGroup". https://developer.salesforce.com/docs/service/salesforce-scheduler-dev-guide/guide/sforce-api-objects-worktypegroup.html (accessed 2026-11-21)
