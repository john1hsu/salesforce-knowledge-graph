---
id: kt:dispatcher-console
type: Feature
title: Dispatcher Console
aliases: [Field Service Dispatcher Console, Classic Dispatch Console, dispatch console, Field Service Gantt, dispatcher Gantt]
domain: clouds-and-products
summary: >-
  The Field Service managed package's dispatching workspace: an appointment list, a resource Gantt and a map
  in one tab, where dispatchers schedule, dispatch and optimize service appointments; Trailhead now labels it the
  Classic Dispatch Console alongside the newer Scheduling Console.
release: "Winter '27"
status: current
broader: [kt:field-service]
related: [kt:service-appointments, kt:field-service-scheduling-policies, kt:scheduling-console, kt:field-sets, kt:custom-permissions]
relations:
  - {predicate: partOf, object: kt:field-service}
  - {predicate: dependsOn, object: kt:service-appointments}
  - {predicate: configuredVia, object: kt:field-sets}
  - {predicate: alternativeTo, object: kt:scheduling-console}
  - {predicate: dependsOn, object: kt:field-service-scheduling-policies}
sources:
  - id: s1
    title: "Explore the Dispatcher Console (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/field-service-dispatcher-console-for-dispatchers/explore-the-dispatcher-console
    type: official-learning
    accessed: 2026-11-22
  - id: s2
    title: "Set Up the Dispatcher Console (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/dispatcher-console-for-admins/set-up-the-dispatcher-console
    type: official-learning
    accessed: 2026-11-22
  - id: s3
    title: "Customize Dispatcher Console Settings (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/content/learn/modules/dispatcher-console-for-admins/customize-dispatcher-console-settings
    type: official-learning
    accessed: 2026-11-22
  - id: s4
    title: "Customize Your View (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/field-service-dispatcher-console-for-dispatchers/customize-your-view
    type: official-learning
    accessed: 2026-11-22
  - id: s5
    title: "Code Examples: Dispatcher Console Custom Actions | Field Service Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/service/field-service-dev/guide/fsl-dev-code-samples-dispatcher.html
    type: official-docs
    accessed: 2026-11-22
  - id: s6
    title: "Get to Know the Scheduling Console (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/scheduling-console-basics/get-to-know-the-scheduling-console
    type: official-learning
    accessed: 2026-11-22
  - id: s7
    title: "Add a Custom Action (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/dispatcher-console-for-admins/add-a-custom-action
    type: official-learning
    accessed: 2026-11-22
created: 2026-11-22
---

# Dispatcher Console

The **Dispatcher Console** is the dispatcher's workspace in Field Service. It combines a filterable list of service appointments, a Gantt chart of mobile workers' schedules and an embedded map, so a dispatcher can schedule, dispatch, flag and optimize work from one tab.[^s1] It ships with the Field Service managed package: admins enable Field Service and install the package before they can set the console up.[^s2] In current Trailhead content dispatchers reach it from the Field Service app, on a tab now labelled **Classic Dispatch Console**, which can take a few minutes to load.[^s1]

## How it works

The left-hand **appointment list** is driven by a handful of controls.[^s1]

- **Policy** picks the scheduling policy used when scheduling from the console; Customer First is the default, and a dispatcher can switch it, for example during an emergency.[^s1]
- **Territories** chooses which service territories to show, and can also show appointments that have no territory.[^s1]
- **Time frame** and **filters** decide which appointments appear: all by default, or subsets such as unscheduled work, plus admin-defined custom filters.[^s1]
- **Bulk actions** apply schedule, dispatch, flag, unflag or optimize to the selected appointments.[^s1]

The **Gantt** shows one row per mobile worker, grouped by territory, with appointments, absences, breaks, travel time and crew assignments on the timeline.[^s1] A KPI bar above it totals scheduled time, average travel time per appointment and the number of appointments in jeopardy.[^s1] Its filter panel narrows workers by skill or resource type and offers visible hours, colour schemes, and long-term and utilization views.[^s1] The **map** view plots appointments, resources and territories on Google Maps, with an optional traffic layer.[^s1]

Dispatchers can tune their own view. A scheduling window length and a Horizon setting (due date, scheduled start or scheduled end) set which appointments the list shows.[^s4] The Gantt opens on the current day; arrows and a date picker move through time, and more visible days widen the view.[^s4] Colour palettes recolour Gantt appointments by a field such as Due Date, but reloading the Gantt or changing the list resets to the default palette.[^s4]

## Configuration

Admins customize the console in the Field Service Admin app under Field Service Settings.[^s3] The settings cover the appointment lifecycle, global actions, scheduling and optimization policies, the Gantt time zone, refresh frequency and whether absences show.[^s2] Field sets choose which fields appear in list columns, Gantt hover cards, the resource lightbox and Gantt filters.[^s3] Setting the Gantt chart time zone to Territory Timezone shows each territory's work in its local time.[^s3]

**Drip-feed dispatching**, under the Dispatch settings, releases a set number of appointments at a time, so a worker gets the next job only after finishing the current one.[^s3] The Number of Services to Drip Feed field on a service territory overrides the org-wide value for that territory.[^s3]

## Custom actions

Custom actions add menu items that call an Apex class or open a Visualforce page.[^s2] They can run on one or several appointments, on a service resource, on a resource absence, or on the appointments inside a map polygon.[^s7] The Apex classes implement global interfaces in the `FSL` namespace:

- `FSL.CustomGanttServiceAppointmentAction` receives a list of appointment ids plus the visible Gantt dates, so it must handle bulk selections.[^s5]
- `FSL.CustomGanttServiceResourceAction` receives a resource id and its territory membership id.[^s5]
- `FSL.CustomGanttResourceAbsenceAction` receives an absence id and a type of `na` or `break`.[^s5]

Each method returns a string, and a non-empty value is shown as a Gantt notification.[^s5] Visualforce actions receive ids and dates as GET parameters, and a custom action can't open a Visualforce page that belongs to a managed package.[^s5] An action can require a custom permission, so only users with a matching permission set see it.[^s7]

## Gotchas and alternatives

- The console is a managed-package UI, so its settings live in Field Service Settings rather than in standard Lightning page layouts.[^s3]
- Palette choices and some view tweaks are not sticky: reloading the Gantt resets the palette.[^s4]
- Salesforce now also offers the **Scheduling Console**, built on Lightning Web Components and GraphQL, with server-side filtering and lazy loading for large volumes.[^s6] Its setup includes a step to migrate dispatchers to it, which creates a permission set granting access.[^s6] The custom-action docs above describe only the classic console.[^s5]

## Connections

The console is **part of** `kt:field-service` and **depends on** `kt:service-appointments`, the records it lists, schedules and pins on the Gantt.[^s1] Which slot an appointment lands in **depends on** the `kt:field-service-scheduling-policies` chosen in the list.[^s1] Its columns, tooltips and filters are **configured via** `kt:field-sets`, and custom actions can be gated with `kt:custom-permissions`.[^s3][^s7] The newer `kt:scheduling-console` is an **alternative** dispatch workspace with Gantt, list and map views of its own.[^s6]

## Sources
[^s1]: Trailhead, "Explore the Dispatcher Console". https://trailhead.salesforce.com/content/learn/modules/field-service-dispatcher-console-for-dispatchers/explore-the-dispatcher-console (accessed 2026-11-22)
[^s2]: Trailhead, "Set Up the Dispatcher Console". https://trailhead.salesforce.com/content/learn/modules/dispatcher-console-for-admins/set-up-the-dispatcher-console (accessed 2026-11-22)
[^s3]: Trailhead, "Customize Dispatcher Console Settings". https://trailhead.salesforce.com/en/content/learn/modules/dispatcher-console-for-admins/customize-dispatcher-console-settings (accessed 2026-11-22)
[^s4]: Trailhead, "Customize Your View". https://trailhead.salesforce.com/content/learn/modules/field-service-dispatcher-console-for-dispatchers/customize-your-view (accessed 2026-11-22)
[^s5]: Salesforce Developers, "Code Examples: Dispatcher Console Custom Actions". https://developer.salesforce.com/docs/service/field-service-dev/guide/fsl-dev-code-samples-dispatcher.html (accessed 2026-11-22)
[^s6]: Trailhead, "Get to Know the Scheduling Console". https://trailhead.salesforce.com/content/learn/modules/scheduling-console-basics/get-to-know-the-scheduling-console (accessed 2026-11-22)
[^s7]: Trailhead, "Add a Custom Action". https://trailhead.salesforce.com/content/learn/modules/dispatcher-console-for-admins/add-a-custom-action (accessed 2026-11-22)
