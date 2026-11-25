---
id: kt:work-orders
type: StandardObject
title: Work Orders
aliases: [work order, WorkOrder, WorkOrder object, work order line items, WorkOrderLineItem]
domain: clouds-and-products
summary: >-
  The WorkOrder standard object represents field service work to be performed for a customer; it holds the
  request, its asset, case and SLA context, and is the usual parent of the line items and service appointments
  that Field Service schedules and completes.
release: "Winter '27"
status: current
broader: [kt:field-service, kt:standard-objects]
related: [kt:service-appointments, kt:entitlement-management, kt:field-service-mobile-app, kt:service-cloud, kt:field-service-scheduling-policies]
relations:
  - {predicate: partOf, object: kt:field-service}
  - {predicate: dependsOn, object: kt:entitlement-management}
  - {predicate: consumedBy, object: kt:field-service-mobile-app}
sources:
  - id: s1
    title: "WorkOrder | Object Reference for the Salesforce Platform"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_objects_workorder.htm
    type: official-docs
    accessed: 2026-11-25
  - id: s2
    title: "WorkOrderLineItem | Object Reference for the Salesforce Platform"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_workorderlineitem.htm
    type: official-docs
    accessed: 2026-11-25
  - id: s3
    title: "Field Service Core Data Model | Field Service Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/service/field-service-dev/guide/fsl-dev-soap-core.html
    type: official-docs
    accessed: 2026-11-25
  - id: s4
    title: "WorkOrder Custom Fields | Field Service Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/service/field-service-dev/guide/fsl-custom-fields-object-workorder.html
    type: official-docs
    accessed: 2026-11-25
  - id: s5
    title: "Initiate Field Service Jobs (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/field_service_center/field_service_center_workorders
    type: official-learning
    accessed: 2026-11-25
  - id: s6
    title: "Customizing Work Orders in Salesforce (Trailhead project step)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/modify-the-field-service-center/customize-work-orders
    type: official-learning
    accessed: 2026-11-25
created: 2026-11-25
---

# Work Orders

A **work order** (API name `WorkOrder`) is the standard object that represents field service work to be performed for a customer. It was introduced in API version 36.0 and requires work orders or Field Service to be enabled in the org.[^s1] Trailhead frames it as a specific customer request for field service, and it is the record that the rest of the Field Service data model hangs from.[^s5][^s3]

## How it works

The Field Service data model separates the *request* from the *visit*. The work order captures the job, work order line items break it into subtasks, work types act as templates, and service appointments are the scheduled visits that carry the work out.[^s3] A work order can link to an asset (the equipment being serviced), a case (when the work is part of a customer issue), an account and contact (the customer), and an entitlement or service contract (the service level owed).[^s3][^s1] It can sit in one service territory, and a `LocationId` lookup ties it to a work site.[^s3][^s1]

A **work type** is optional but useful: it is a reusable template, such as a cable install, that defines duration and skill requirements and can auto-create a child service appointment on records that use it.[^s3][^s5] When a work order gets a work type, it inherits the work type's duration, duration type and required skills; a blank `Duration` falls back to the work type's value.[^s1] Admins usually add the Work Type field and the Products Required and Products Consumed related lists to the work order page layout, so parts planning and usage are tracked on the job.[^s6]

**Work order line items** (`WorkOrderLineItem`, API 36.0 and later) represent subtasks on a work order.[^s2] They are child records used to split work for billing or to track smaller tasks, and each one can carry its own work type, for example drilling cable holes as part of an installation.[^s3][^s6] A service appointment's parent is typically a work order or a work order line item, and one work order can have several appointments, such as a job that needs two visits.[^s3]

## Key fields

- **Hierarchy:** `ParentWorkOrderId` points to a parent work order, and read-only `RootWorkOrderId` identifies the top of the tree; children show in the Child Work Orders related list.[^s1]
- **Status:** default values are New, In Progress, On Hold, Completed, Cannot Complete, Closed and Canceled; all are customizable.[^s1]
- **StatusCategory:** a restricted picklist with eight defaults (the seven statuses plus None), and every custom status must map to a category.[^s1]
- **Priority:** Low, Medium, High and Critical by default; `IsClosed` records whether the work order is closed.[^s1]
- **Pricing:** `Pricebook2Id` (only when products are enabled), plus read-only `Subtotal`, `TotalPrice`, `Discount` and `LineItemCount` rolled up from the line items.[^s1]
- **Maintenance:** `MaintenancePlanId` and `SuggestedMaintenanceDate` are filled in when a maintenance plan generates the work order.[^s1]
- **Identity:** `WorkOrderNumber` is an eight-digit auto-generated number, and the compound `Address` gives the place where work is done.[^s1]

## Field Service package fields

The Field Service managed package adds a few `FSL__` fields to the object.[^s4]

- `FSL__Scheduling_Priority__c` is calculated from Priority (Critical 1, High 2, Medium 3, Low 4); a lower value means higher priority.[^s4]
- `FSL__VisitingHours__c` looks up operating hours that limit when the work order's appointments can be scheduled.[^s4]
- Visiting hours are enforced only when the scheduling policy includes the Visiting Hours work rule.[^s4]
- `FSL__IsFillInCandidate__c` (default true) must be true for the work order's appointments to be picked by Fill-In Schedule.[^s4]

## Limits and gotchas

Changing a work order's status doesn't change its line items or its service appointments, so close-out automation has to update each level itself.[^s1] `Duration` on the work order is independent of the line items' durations and is not a sum of them.[^s1] `Discount`, `GrandTotal`, `IsGeneratedFromMaintenancePlan` and `RootWorkOrderId` can't be edited regardless of field-level security.[^s1] The object reference shows no documented depth limit for the parent-child hierarchy; report on child work orders with a custom report type, as the docs suggest.[^s1] Work orders publish change events (`WorkOrderChangeEvent`, API 48.0), and the object supports sharing rules and field history.[^s1]

## Connections

The object is **part of** `kt:field-service` and is one of the platform's `kt:standard-objects`.[^s1][^s3] It is the usual parent of `kt:service-appointments`, which Field Service schedules under `kt:field-service-scheduling-policies` and technicians complete in the `kt:field-service-mobile-app`.[^s3][^s4] Its entitlement and service contract links make it **depend on** `kt:entitlement-management` for SLA tracking, and its case link ties field work back to `kt:service-cloud` customer issues.[^s1][^s3]

## Sources
[^s1]: Salesforce Developers, "WorkOrder | Object Reference for the Salesforce Platform". https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_objects_workorder.htm (accessed 2026-11-25)
[^s2]: Salesforce Developers, "WorkOrderLineItem | Object Reference for the Salesforce Platform". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_workorderlineitem.htm (accessed 2026-11-25)
[^s3]: Salesforce Developers, "Field Service Core Data Model | Field Service Developer Guide". https://developer.salesforce.com/docs/service/field-service-dev/guide/fsl-dev-soap-core.html (accessed 2026-11-25)
[^s4]: Salesforce Developers, "WorkOrder Custom Fields | Field Service Developer Guide". https://developer.salesforce.com/docs/service/field-service-dev/guide/fsl-custom-fields-object-workorder.html (accessed 2026-11-25)
[^s5]: Trailhead, "Initiate Field Service Jobs". https://trailhead.salesforce.com/content/learn/modules/field_service_center/field_service_center_workorders (accessed 2026-11-25)
[^s6]: Trailhead, "Customizing Work Orders in Salesforce". https://trailhead.salesforce.com/content/learn/projects/modify-the-field-service-center/customize-work-orders (accessed 2026-11-25)
