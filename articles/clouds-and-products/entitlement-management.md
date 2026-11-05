---
id: kt:entitlement-management
type: Feature
title: Entitlement Management
aliases: [Entitlements and Milestones, Salesforce Entitlements, SLA Policies]
domain: clouds-and-products
summary: >-
  Service Cloud feature that models what support a customer is owed (entitlements, service contracts) and enforces
  service-level timelines on cases and work orders through entitlement processes (SLA policies) made of timed milestones.
release: "Winter '27"
status: current
broader: [kt:service-cloud]
related: [kt:field-service, kt:omni-channel, kt:apex-triggers, kt:change-sets]
relations:
  - {predicate: partOf, object: kt:service-cloud}
  - {predicate: dependsOn, object: kt:business-hours}
  - {predicate: integratesWith, object: kt:field-service}
  - {predicate: configuredVia, object: kt:entitlement-process-metadata}
sources:
  - id: s1
    title: "Get Started with Entitlements (Entitlement Management for Lightning Experience)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/es/content/learn/modules/entitlement-management-for-lightning-experience/get-started-with-entitlements
    type: official-learning
    accessed: 2026-11-05
  - id: s2
    title: "Salesforce Entitlement Management Implementation Guide"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/242/latest/en-us/sfdc/pdf/salesforce_entitlements_implementation_guide.pdf
    type: official-docs
    accessed: 2026-11-05
  - id: s3
    title: "Use Entitlements in Customer Cases"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/entitlement-management-for-lightning-experience/use-entitlements-in-customer-cases
    type: official-learning
    accessed: 2026-11-05
  - id: s4
    title: "Use Entitlements with Work Orders"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/entitlement-management-for-lightning-experience/use-entitlements-with-work-orders
    type: official-learning
    accessed: 2026-11-05
  - id: s5
    title: "Get Started with SLA Policies"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/sla-and-entitlements-setup/get-started-with-sla-policies
    type: official-learning
    accessed: 2026-11-05
  - id: s6
    title: "Set Up Milestone Actions and Automate Policy Allotment"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/sla-and-entitlements-setup/set-up-milestone-actions-and-automate-policy-allotment
    type: official-learning
    accessed: 2026-11-05
created: 2026-11-05
---

# Entitlement Management

Entitlement management is the Service Cloud feature for tracking the support each customer is owed under a service level agreement (SLA) and timing whether reps deliver it. Salesforce calls entitlements units of customer support, such as phone support or web support. Reps can see a customer's entitlements on the account page and know what service applies.[^s1] Admins turn it on in Setup under **Entitlement Settings** by selecting **Enable Entitlement Management**.[^s1] The implementation guide lists it for Professional, Enterprise, Performance, Unlimited and Developer Editions with Service Cloud. Only users in Service Cloud orgs can enable, create or update entitlement items.[^s2]

## Building blocks

- **Entitlement**: a unit of support linked to an account, asset, contact or service contract, with start and end dates.[^s1][^s2]
- **Service contract** and **contract line item**: a service contract is a support agreement such as a warranty, subscription or SLA. Each contract line item is a product the contract covers and requires the Product object.[^s2]
- **Entitlement template**: predefined support terms attached to a product. When an asset is created from that product, the matching entitlement is added automatically.[^s1]
- **Entitlement process**: a timeline of milestones. A process is either a Case type or a Work Order type, and one process can serve many entitlements.[^s1][^s2]
- **Milestone**: a required step such as First Response or Resolution Time, with a time trigger in minutes, criteria, and optional business hours.[^s2]
- **Milestone action**: a time-based action of one of three kinds: success (on completion), warning (before a violation) and violation (after it). Actions can send email alerts, update fields or escalate.[^s2][^s6]

Milestones come in three recurrence types. *No Recurrence* fires once per record. *Independent* fires whenever its criteria are met. *Sequential* repeats in order each time its criteria are met.[^s2]

## How it works

An entitlement points to an entitlement process through a lookup. When a case is linked to that entitlement, the process starts and its milestones begin counting down. In Trailhead's example, a high-priority phone case created from the entitlement's Cases related list gets the entitlement automatically, and its Resolution Time milestone starts.[^s3] The Lightning **Milestones** component (the Milestone Tracker) shows time left before an active milestone's target, time elapsed on an overdue one, and upcoming and completed milestones. Admins add it to the case record page in Lightning App Builder.[^s3]

Target dates follow business hours in a set order. Hours on the milestone override hours on the entitlement process. If neither is set, the case or work order's own hours apply.[^s2]

Salesforce has also added a **Simplified SLA Setup** option in Entitlement Settings. It brings milestones, entitlements and *SLA policies* together in one setup view, and also models operational level agreements (OLAs) between internal teams.[^s5] In that view, activating an SLA policy can create a linked entitlement, and **Application Rules** with an order, criteria and target entitlement assign the entitlement, and its SLA policy, to matching cases. Trailhead's example assigns it by Case Origin.[^s6]

## Limits and gotchas

The implementation guide gives these limits: 1,000 entitlement processes per org, 10 milestones per entitlement process, up to 10 actions and 10 time triggers per milestone action type, and 10,000 service contracts and 10,000 contract line items per hierarchy.[^s2] That guide edition predates Winter '27, so check current values before designing near them.

- Without Application Rules, entitlements are **not** applied automatically to cases from Web-to-Case, Email-to-Case or experience sites. Salesforce provides a sample Apex trigger that looks up an active entitlement on the contact, then the account.[^s2][^s6]
- Milestones do **not** complete on their own. Closing a case leaves Resolution Time open unless an Apex trigger completes it or a rep clicks Mark Completed.[^s2][^s3]
- After activation you can change little about a process. To keep several versions, turn on **entitlement versioning**. You can then add milestones to a new version and move entitlements and cases to it, but every version must be the same type.[^s2][^s3]
- A Case-type process won't run on work orders. Field Service work orders need their own Work Order-type process, and Trailhead advises leaving it inactive until its milestones are added.[^s4]
- Time-triggered actions run only during org business hours. Business hours on entitlement processes aren't supported in change sets.[^s2]

## When to use it

Use entitlement management when contracts promise response or resolution times that must be timed, escalated and reported. Examples include tiered support plans, warranties tied to assets, and on-site service windows on work orders.[^s1][^s4] For simple aging alerts on cases with no contractual terms, record-triggered automation may be enough. Entitlements add data and configuration work for every account and product.

## Connections

Entitlement management is **part of** `kt:service-cloud`, which uses it to model SLAs.[^s1] Its milestone timers **depend on** `kt:business-hours`.[^s2] It **integrates with** `kt:field-service`, because work orders run their own entitlement processes.[^s4] Processes are deployed as the `EntitlementProcess` Metadata API type, so it is **configured via** `kt:entitlement-process-metadata`. Because change sets don't carry entitlement-process business hours, it is related to `kt:change-sets`.[^s2] It is related to `kt:apex-triggers`, the usual way to auto-attach entitlements and complete milestones, and to `kt:omni-channel`, which routes the cases whose SLA clocks it runs.[^s2]

## Sources

[^s1]: Trailhead, "Get Started with Entitlements (Entitlement Management for Lightning Experience)". https://trailhead.salesforce.com/es/content/learn/modules/entitlement-management-for-lightning-experience/get-started-with-entitlements (accessed 2026-11-05)
[^s2]: Salesforce, "Salesforce Entitlement Management Implementation Guide". https://resources.docs.salesforce.com/242/latest/en-us/sfdc/pdf/salesforce_entitlements_implementation_guide.pdf (accessed 2026-11-05)
[^s3]: Trailhead, "Use Entitlements in Customer Cases". https://trailhead.salesforce.com/content/learn/modules/entitlement-management-for-lightning-experience/use-entitlements-in-customer-cases (accessed 2026-11-05)
[^s4]: Trailhead, "Use Entitlements with Work Orders". https://trailhead.salesforce.com/content/learn/modules/entitlement-management-for-lightning-experience/use-entitlements-with-work-orders (accessed 2026-11-05)
[^s5]: Trailhead, "Get Started with SLA Policies". https://trailhead.salesforce.com/content/learn/modules/sla-and-entitlements-setup/get-started-with-sla-policies (accessed 2026-11-05)
[^s6]: Trailhead, "Set Up Milestone Actions and Automate Policy Allotment". https://trailhead.salesforce.com/content/learn/modules/sla-and-entitlements-setup/set-up-milestone-actions-and-automate-policy-allotment (accessed 2026-11-05)
