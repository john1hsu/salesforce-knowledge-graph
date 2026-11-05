---
id: kt:platform-event-allocations
type: Limit
title: Platform Event Allocations
aliases: [platform event limits, event delivery allocation, event publishing allocation, DailyDeliveredPlatformEvents, HourlyPublishedPlatformEvents, platform events add-on license]
domain: integration
summary: >-
  The org-wide caps on how many platform event and change event messages can be published per hour and delivered
  to API-based subscribers per 24 hours, plus the usage-based monthly entitlement that a platform events add-on
  license adds on top.
release: "Winter '27"
status: current
broader: [kt:governor-limits]
related: [kt:platform-events, kt:change-data-capture, kt:pub-sub-api]
relations:
  - {predicate: contrastsWith, object: kt:api-request-limits}
  - {predicate: coveredBy, object: kt:integration-architect-certification}
sources:
  - id: s1
    title: "Default Platform Event Allocations for Event Publishing and Delivery"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/platform-events/guide/platform-events-limits-default.html
    type: official-docs
    accessed: 2026-11-05
  - id: s2
    title: "Increase Your Event Delivery and Publishing Allocations with a Platform Event Add-On License"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/platform-events/guide/platform-events-limits-entitlement.html
    type: official-docs
    accessed: 2026-11-05
  - id: s3
    title: "Which Type of Platform Events Do Allocations Apply to?"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/platform-events/guide/platform-events-limits-which-events.html
    type: official-docs
    accessed: 2026-11-05
  - id: s4
    title: "Monitor Event Usage Against Your Allocations"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/platform-events/guide/platform-events-limits-monitor.html
    type: official-docs
    accessed: 2026-11-05
  - id: s5
    title: "Standard-Volume Platform Event Allocations"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_limits_svpe.htm
    type: official-docs
    accessed: 2026-11-05
  - id: s6
    title: "Stream Events at Scale with Event Filters and Field Enrichment"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2023/01/stream-events-at-scale-with-event-filters-and-field-enrichment
    type: official-blog
    accessed: 2026-11-05
created: 2026-11-05
---

# Platform Event Allocations

Platform event allocations are the org-level quotas that Salesforce enforces on the event bus. There are two that matter most in practice: a **publishing** allocation, counted over a rolling hour, and a **delivery** allocation, counted over a rolling 24 hours. Salesforce enforces the default figures to share the multitenant service fairly, and they cannot be exceeded without an add-on license.[^s1] They sit alongside the "common" allocations (event definitions, concurrent CometD clients, maximum message size) that are described with the feature itself, and they are separate from the daily API request allocation.[^s1]

## How it works

**Publishing.** The hourly publishing allocation covers every way of publishing: Apex, Pub/Sub API, REST, SOAP, Bulk API, flows and processes. Default values (Winter '27 documentation) are 250,000 events per hour in Performance, Unlimited, Enterprise and Professional (with API add-on) editions, and 50,000 in Developer Edition.[^s1] Publishing through REST, SOAP or Bulk API also consumes the org's daily API requests, while publishing from Pub/Sub API, Apex, flows and processes does not.[^s1] Usage is checked at publish time against the last hour.[^s1]

**Delivery.** The 24-hour delivery allocation applies only to API-based subscribers: Pub/Sub API clients, CometD clients, the `empApi` Lightning component and event relays. Apex triggers, flows and processes that subscribe to an event do not consume it.[^s1] Defaults are 50,000 delivered messages in Performance and Unlimited, 25,000 in Enterprise and Professional (with API add-on), and 10,000 in Developer Edition. The pool is shared by high-volume platform events and Change Data Capture events.[^s1] Each subscriber is counted separately, so two clients each receiving the same 20,000 events use 40,000 of the allocation.[^s1] This is why the publishing number is much higher than the delivery number: an Apex publish consumed by an Apex trigger uses only publishing, while the same publish read by a Pub/Sub API client uses both.[^s1]

**Which events count.** Custom platform events count against both allocations. Salesforce-defined standard events do not count toward publishing, and whether their delivery counts is stated per event in its reference page. Real-Time Event Monitoring events count toward neither; system protection limits apply instead.[^s3]

## Add-on license

A platform events add-on, bought through the account team, raises the hourly publishing allocation by 25,000 (to 275,000 in Performance, Unlimited, Enterprise and Professional) and adds 100,000 deliveries per day. Delivery then moves to a monthly usage-based entitlement calculated as the daily figure times 30: one add-on gives 4.5 million per month in Performance and Unlimited and 3.75 million in Enterprise and Professional.[^s2] The daily delivery figure is enforced less strictly under an add-on, with an unpublished grace allocation that absorbs spikes; Salesforce may adjust that grace at any time, and contacts customers who exceed the monthly entitlement. Entitlement usage is computed only in production orgs, not sandboxes or trials.[^s2]

## Limits and gotchas

- **Exceeding publishing** makes the publish call fail with `LIMIT_EXCEEDED`. The event is neither published nor queued, so the publisher must retry later.[^s1]
- **Exceeding delivery** disconnects the subscriber. CometD clients receive `403::Organization total events daily limit exceeded`; Pub/Sub API clients receive `sfdc.platform.eventbus.grpc.subscription.limit.exceeded`. Because events are retained for 72 hours, a client can reconnect after usage drops and resume from its stored Replay ID.[^s1]
- **Legacy standard-volume events** (defined in API version 44.0 and earlier) have their own allocations, for example 50,000 deliveries per day and 100,000 publishes per hour in Unlimited Edition. They can no longer be created and are scheduled for retirement in Summer '27.[^s5]
- **Extra subscribers multiply cost.** Removing unneeded subscribers and filtering streams are the first remedies Salesforce recommends before buying an add-on.[^s1]

## Monitoring and design

Usage appears in Setup on the Platform Events page (Event Allocations section) and, for add-on orgs, in the Usage-based Entitlements list on Company Information. The REST `limits` resource returns `HourlyPublishedPlatformEvents`, `DailyDeliveredPlatformEvents` and, for add-on orgs, `MonthlyPlatformEventsUsageEntitlement`; Apex can read the same values through `System.OrgLimit`.[^s4] For finer breakdowns by event, client or usage type, the PlatformEventUsageMetric object can be queried with SOQL.[^s1][^s4]

The most effective design lever is server-side filtering. Custom channels let a channel member carry a filter expression, based on a subset of SOQL, so the bus delivers only matching events instead of every event being sent and then discarded by the client, which reduces the org's limit consumption.[^s6]

## Connections

These allocations **govern** `kt:platform-events` and `kt:pub-sub-api`, and they share a delivery pool with `kt:change-data-capture`, so capacity planning has to treat all three together.[^s1] They are a specialised member of the wider family of `kt:governor-limits`. They **contrast with** `kt:api-request-limits`: the two are often confused, yet only REST, SOAP and Bulk publishes touch both, while Pub/Sub API traffic is measured only here.[^s1] Sizing event volumes against these numbers is part of the integration design scope tested by the `kt:integration-architect-certification`.[^s1][^s2]

## Sources

[^s1]: Salesforce Developers, "Default Platform Event Allocations for Event Publishing and Delivery". https://developer.salesforce.com/docs/platform/platform-events/guide/platform-events-limits-default.html (accessed 2026-11-05)
[^s2]: Salesforce Developers, "Increase Your Event Delivery and Publishing Allocations with a Platform Event Add-On License". https://developer.salesforce.com/docs/platform/platform-events/guide/platform-events-limits-entitlement.html (accessed 2026-11-05)
[^s3]: Salesforce Developers, "Which Type of Platform Events Do Allocations Apply to?". https://developer.salesforce.com/docs/platform/platform-events/guide/platform-events-limits-which-events.html (accessed 2026-11-05)
[^s4]: Salesforce Developers, "Monitor Event Usage Against Your Allocations". https://developer.salesforce.com/docs/platform/platform-events/guide/platform-events-limits-monitor.html (accessed 2026-11-05)
[^s5]: Salesforce Developers, "Standard-Volume Platform Event Allocations". https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_limits_svpe.htm (accessed 2026-11-05)
[^s6]: Philippe Ozil, Salesforce Developers Blog, "Stream Events at Scale with Event Filters and Field Enrichment" (2023). https://developer.salesforce.com/blogs/2023/01/stream-events-at-scale-with-event-filters-and-field-enrichment (accessed 2026-11-05)
