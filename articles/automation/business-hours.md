---
id: kt:business-hours
type: Feature
title: Business Hours
aliases: [BusinessHours, support hours, BusinessHours object, BusinessHours class]
domain: automation
summary: >-
  Named, time-zoned weekly schedules (with optional holidays) that tell Salesforce when a support team is
  working, so escalation rules, entitlement milestones and Apex time calculations count only working time.
release: "Winter '27"
status: current
broader: [kt:process-automation, kt:service-cloud]
related: [kt:change-sets, kt:field-service]
relations:
  - {predicate: integratesWith, object: kt:escalation-rules}
  - {predicate: integratesWith, object: kt:entitlement-management}
  - {predicate: integratesWith, object: kt:apex}
  - {predicate: hasPart, object: kt:holidays}
sources:
  - id: s1
    title: "Set Business Hours"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=service.customize_supporthours.htm&type=5
    type: official-docs
    accessed: 2026-11-07
  - id: s2
    title: "BusinessHours (SOAP API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_objects_businesshours.htm
    type: official-docs
    accessed: 2026-11-07
  - id: s3
    title: "Holiday (Object Reference for the Salesforce Platform)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_holiday.htm
    type: official-docs
    accessed: 2026-11-07
  - id: s4
    title: "BusinessHours Class (Apex Reference Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_classes_businesshours.htm
    type: official-docs
    accessed: 2026-11-07
  - id: s5
    title: "How Business Hours Work in Entitlement Management"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=entitlements_business_hours.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-07
  - id: s6
    title: "Entitlement Management Limits and Limitations"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=entitlements_best_practices.htm&type=5
    type: official-docs
    accessed: 2026-11-07
created: 2026-11-07
---

# Business Hours

Business Hours are setup records that describe when a support organization is open: a name, a time zone, and an open and close time for each day of the week. Salesforce uses them to make time-based service automation count working time rather than wall-clock time, which makes case escalations and service-level milestones more accurate.[^s1] Each set is stored as a `BusinessHours` record with fields such as `Name`, `TimeZoneSidKey`, `IsActive` and `IsDefault`, plus per-day start and end times.[^s2]

## How it works

Admins with the Manage Business Hours permission create a set in Setup, choose a time zone, and enter hours per day; a day can be marked 24 hours, or left with blank times to mean the team is unavailable that day. A set must be marked Active before it can be associated with cases, escalation rules, milestones or entitlement processes, and one set can be flagged as the default that is applied to new cases.[^s1] If nothing is configured, an org's business hours run around the clock in the default time zone from the organization profile; in the API, a 24-hour day is represented by midnight-to-midnight open and close times.[^s1][^s2]

Holidays are separate `Holiday` records linked to business hours. While a linked holiday is in effect, those business hours, and the escalation rules that use them, are suspended. Holidays can be all-day or time-bounded (start and end times are stored in minutes), and can repeat on a pattern defined by recurrence type, interval, day-of-week and month/day fields; whether a holiday recurs can be set only when it is created.[^s3]

## Where it is used

- **Escalation rules** run only during the business hours associated with them, so a case does not age toward escalation overnight or on weekends unless the hours say the team is working.[^s2] A rule entry can also override a case's own business hours when the case matches its criteria.[^s1]
- **Entitlement processes and milestones** count milestone time in business hours. Salesforce uses the most specific level that is set: milestone hours first, then entitlement process hours, then the business hours on the case or work order.[^s5] When an entitlement belongs to a process, Salesforce recommends leaving the entitlement's own business hours blank so records follow the process.[^s5]
- **Apex** exposes a `BusinessHours` class with static methods: `add` and `addGmt` move a datetime forward by an interval of business time, `diff` returns the business-time milliseconds between two datetimes, `isWithin` tests whether a moment is inside business hours (holidays included), and `nextStartDate` returns the next opening time. Precision below one minute is ignored by `add`.[^s4] This lets custom SLA logic, routing or scheduled automation reuse the same calendar as the standard features.

## Limits and gotchas

- Business hours on entitlement processes aren't supported in change sets; Salesforce suggests recreating the process in the target org, using another deployment method, or removing the hours before adding the process to a change set.[^s6]
- In Lightning Experience the Business Hours field isn't available on the Case Milestones related list.[^s6]
- Because milestone-level hours win over process-level hours, a milestone with its own hours ignores later edits to the process's hours. Changing hours on an active process requires entitlement versioning: create a new version, edit its hours, then add an update rule on the original version pointing at the new one.[^s5]
- All users can read business hours and holidays through the API even without View Setup and Configuration; Customer Portal users can't access holidays.[^s2][^s3]
- `add` and `nextStartDate` return local-time datetimes while `addGmt` returns GMT, so mixing them without care produces off-by-time-zone errors.[^s4]

## When to use it

Create one set per staffed location or shift pattern (naming it after the location or time zone, as Salesforce suggests) and attach it wherever time is measured against a customer promise.[^s1] Use process-level hours when cases with different schedules share one entitlement process, and milestone-level hours when one milestone, such as an after-hours customer update, needs a different calendar.[^s5]

## Connections

Business Hours are a building block of **process automation** in **Service Cloud**: **Escalation rules** and **Entitlement Management** both depend on them to measure elapsed working time.[^s1][^s2] **Apex** reads the same records through the `BusinessHours` class.[^s4] Their `Holiday` records (**holidays**) suspend the schedule on given dates, and the recurring-holiday `NextStartDate` field is tied to **Field Service**.[^s3] The change-set limitation makes **change sets** a poor fit for moving entitlement processes that carry business hours.[^s6]

## Sources

[^s1]: Salesforce Help, "Set Business Hours". https://help.salesforce.com/s/articleView?language=en_US&id=service.customize_supporthours.htm&type=5 (accessed 2026-11-07)
[^s2]: Salesforce Developers, "BusinessHours", SOAP API Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_objects_businesshours.htm (accessed 2026-11-07)
[^s3]: Salesforce Developers, "Holiday", Object Reference for the Salesforce Platform. https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_holiday.htm (accessed 2026-11-07)
[^s4]: Salesforce Developers, "BusinessHours Class", Apex Reference Guide. https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_classes_businesshours.htm (accessed 2026-11-07)
[^s5]: Salesforce Help, "How Business Hours Work in Entitlement Management". https://help.salesforce.com/s/articleView?id=entitlements_business_hours.htm&language=en_US&type=5 (accessed 2026-11-07)
[^s6]: Salesforce Help, "Entitlement Management Limits and Limitations". https://help.salesforce.com/s/articleView?language=en_US&id=entitlements_best_practices.htm&type=5 (accessed 2026-11-07)
