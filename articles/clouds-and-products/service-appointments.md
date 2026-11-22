---
id: kt:service-appointments
type: StandardObject
title: Service Appointments
aliases: [service appointment, ServiceAppointment, ServiceAppointment object, SA record]
domain: clouds-and-products
summary: >-
  The ServiceAppointment standard object records when, where and by whom a piece of customer work is done; it is
  the schedulable unit that Field Service dispatches to mobile workers and that Salesforce Scheduler books for
  customer meetings.
release: "Winter '27"
status: current
broader: [kt:field-service, kt:standard-objects]
related: [kt:work-orders, kt:dispatcher-console, kt:field-service-mobile-app, kt:service-cloud]
relations:
  - {predicate: partOf, object: kt:field-service}
  - {predicate: consumedBy, object: kt:salesforce-scheduler}
  - {predicate: dependsOn, object: kt:work-orders}
  - {predicate: configuredVia, object: kt:field-service-scheduling-policies}
sources:
  - id: s1
    title: "ServiceAppointment | Object Reference for the Salesforce Platform"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_serviceappointment.htm
    type: official-docs
    accessed: 2026-11-22
  - id: s2
    title: "ServiceAppointment Custom Fields | Field Service Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.field_service_dev.meta/field_service_dev/fsl_custom_fields_object_serviceappointment.htm
    type: official-docs
    accessed: 2026-11-22
  - id: s3
    title: "ServiceAppointment | Salesforce Scheduler Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/service/salesforce-scheduler-dev-guide/guide/sforce-api-objects-serviceappointment.html
    type: official-docs
    accessed: 2026-11-22
  - id: s4
    title: "Get Started with Field Service and Operations (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/field_service_basics/field_service_basics_intro
    type: official-learning
    accessed: 2026-11-22
  - id: s5
    title: "Track Field Service (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/field_service_center/field_service_center_track
    type: official-learning
    accessed: 2026-11-22
created: 2026-11-22
---

# Service Appointments

A **service appointment** (API name `ServiceAppointment`) is the standard object that says when a job happens, where, and who does it. It has been available since API version 38.0, and one object serves several products: Field Service, Salesforce Scheduler (formerly Lightning Scheduler), Intelligent Appointment Management and Virtual Care.[^s1] In Field Service it is the unit that dispatchers schedule and optimize, and that mobile workers complete in the field.[^s4]

## How it works

Field Service separates the *request* from the *visit*. A work order is the request for field work, a work type is a reusable template for common jobs such as a cable installation, and a service appointment is the scheduled visit that delivers the work.[^s4] In the standard flow, agents create work orders, dispatchers schedule and optimize the appointments by skills, parts and location, and mobile workers complete the appointments and close out the work orders.[^s4] Appointments are carried out by service resources (individual mobile employees) or service crews (teams assigned as one unit), within service territories, the regions where the work happens.[^s4]

Every appointment has a parent record, held in `ParentRecordId`.[^s3] The time fields fall into three groups.[^s3]

- **Customer window:** `EarliestStartTime` and `DueDate` bound when the work may happen, and `ArrivalWindowStartTime`/`ArrivalWindowEndTime` hold the window promised to the customer.[^s3]
- **Plan:** `SchedStartTime` and `SchedEndTime` are set by scheduling; `Duration` is measured in the unit chosen in `DurationType` (Hours or Minutes, default Hours).[^s3]
- **Actuals:** `ActualStartTime`, `ActualEndTime` and `ActualDuration` record what really happened, for comparison with the plan.[^s3]

`ServiceTerritoryId` and `WorkTypeId` link the appointment to its territory and template, and `AppointmentNumber` is an auto-number.[^s3]

## Status lifecycle

Out of the box an appointment moves through None (unscheduled, the default), Scheduled, Dispatched (the resource is on the way), In Progress, and finally Completed, Cannot Complete or Canceled.[^s5] Work orders have their own, separate list: New, In Progress, On Hold, Completed, Closed, Cannot Complete and Canceled. Completing an appointment therefore doesn't close its work order. Admins can add, remove or relabel values, and the Trailhead example completes the appointment first and the work order second.[^s5] Each custom status value maps to a `StatusCategory`, which holds the same values as the default statuses, so automation can rely on the category even when labels change.[^s3]

## Field Service package fields

When the Field Service managed package is installed, it adds `FSL__` fields that drive the scheduling engine and the dispatcher Gantt.[^s2]

- `FSL__Pinned__c` locks an appointment in place, so it can't be dragged or moved by automatic scheduling or optimization.[^s2]
- `FSL__Scheduling_Policy_Used__c` looks up a scheduling policy; setting it overrides the default policy in Field Service Settings.[^s2]
- `FSL__InJeopardy__c` flags at-risk work, and `FSL__InJeopardyReason__c` gives the reason: Delayed Start, Delayed Finish, Due Date Approaching, No Response or Rejected by Contractor.[^s2]
- `FSL__Emergency__c` is set by the Emergency Wizard, and `FSL__IsMultiDay__c` marks appointments that span several days.[^s2]
- `FSL__Schedule_Mode__c` records how the appointment was scheduled (for example Automatic, Manual or Optimization). The system sets it, and the docs say not to edit it.[^s2]

## Gotchas

- `FSL__Duration_In_Minutes__c` is calculated from the scheduled start and end, and it is 0 while `SchedStartTime` is blank, so reports built on it ignore unscheduled work.[^s2]
- Fill-In Schedule only picks an appointment if its own `FSL__IsFillInCandidate__c` flag is true and, when the parent is a work order or work order line item, the parent's flag is also true.[^s2]
- Under Salesforce Scheduler, `ParentRecordId` can't be changed after the record is created. The parent can be an account, case, lead or opportunity.[^s3]
- Scheduler adds a CheckedIn status that has no matching status category, plus fields for group appointments (`AppointmentMode`, `AttendeeLimit`) and anonymous booking (`IsAnonymousBooking`).[^s3]

## Connections

The object is **part of** `kt:field-service` and belongs among the platform's `kt:standard-objects`.[^s1] It **depends on** `kt:work-orders` in the usual Field Service design, where the work order defines the job and its appointments schedule it.[^s4] Scheduling is **configured via** `kt:field-service-scheduling-policies`, which an appointment can override one record at a time.[^s2] Dispatchers manage appointments on the `kt:dispatcher-console` Gantt, and technicians complete them in the `kt:field-service-mobile-app`.[^s2][^s4] The same object is **consumed by** `kt:salesforce-scheduler` for booking customer meetings, with the differences noted above.[^s3] Field Service and Scheduler both build on `kt:service-cloud` case and account data.[^s3]

## Sources
[^s1]: Salesforce Developers, "ServiceAppointment | Object Reference for the Salesforce Platform". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_serviceappointment.htm (accessed 2026-11-22)
[^s2]: Salesforce Developers, "ServiceAppointment Custom Fields | Field Service Developer Guide". https://developer.salesforce.com/docs/atlas.en-us.field_service_dev.meta/field_service_dev/fsl_custom_fields_object_serviceappointment.htm (accessed 2026-11-22)
[^s3]: Salesforce Developers, "ServiceAppointment | Salesforce Scheduler Developer Guide". https://developer.salesforce.com/docs/service/salesforce-scheduler-dev-guide/guide/sforce-api-objects-serviceappointment.html (accessed 2026-11-22)
[^s4]: Trailhead, "Get Started with Field Service and Operations". https://trailhead.salesforce.com/content/learn/modules/field_service_basics/field_service_basics_intro (accessed 2026-11-22)
[^s5]: Trailhead, "Track Field Service". https://trailhead.salesforce.com/content/learn/modules/field_service_center/field_service_center_track (accessed 2026-11-22)
