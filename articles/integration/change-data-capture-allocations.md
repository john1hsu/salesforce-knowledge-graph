---
id: kt:change-data-capture-allocations
type: Limit
title: Change Data Capture Allocations
aliases: [CDC allocations, CDC limits, change event allocations, selected entities limit, Change Data Capture add-on license]
domain: integration
summary: >-
  The org-wide caps that govern Change Data Capture: how many objects can be selected for change events, how many
  custom channels exist, how many change events API-based subscribers may receive in a rolling 24 hours, and the
  concurrency and message-size ceilings shared with other streaming events, plus the add-on license that lifts them.
release: "Winter '27"
status: current
broader: [kt:governor-limits]
related: [kt:change-data-capture, kt:pub-sub-api, kt:streaming-api, kt:platform-event-channel-member, kt:orglimits-class]
relations:
  - {predicate: contrastsWith, object: kt:platform-event-allocations}
  - {predicate: contrastsWith, object: kt:api-request-limits}
sources:
  - id: s1
    title: "Change Data Capture Allocations (Change Data Capture Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/change-data-capture/guide/cdc-allocations.html
    type: official-docs
    accessed: 2026-11-17
  - id: s2
    title: "Change Data Capture Allocations: Default Allocations (Change Data Capture Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_allocations_default_allocations.htm
    type: official-docs
    accessed: 2026-11-17
  - id: s3
    title: "Filter Your Stream of Change Events with Channels"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/change-data-capture/guide/cdc-filter-section.html
    type: official-docs
    accessed: 2026-11-17
  - id: s4
    title: "Stream Events at Scale with Event Filters and Field Enrichment"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2023/01/stream-events-at-scale-with-event-filters-and-field-enrichment
    type: official-blog
    accessed: 2026-11-17
  - id: s5
    title: "Learn About Daily Rate Limits (App Development Without Limits)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/app-development-without-limits/app-development-without-limits-rate
    type: official-learning
    accessed: 2026-11-17
created: 2026-11-17
---

# Change Data Capture Allocations

Change Data Capture allocations are the org-level quotas that decide how far an org can scale
`kt:change-data-capture`. They are not per-transaction governor limits: they cap how many objects
generate change events, how many custom channels can carry them, how many events external subscribers
can pull in a rolling day, and how many streaming clients can be connected at once.[^s1] Salesforce
uses daily and fixed allocations like these to keep shared multitenant resources predictable for every
org.[^s5]

## The default allocations

Without an add-on license, the Winter '27 documentation lists these values:[^s2]

| Allocation | Performance / Unlimited | Enterprise | Developer |
|---|---|---|---|
| Selected entities across all channels | 5 | 5 | 5 |
| Custom channels | 100 | 100 | 100 |
| Event delivery, rolling 24 hours | 50,000 | 25,000 | 10,000 [^s2] |

**Selected entities.** An object chosen in several channels is counted only once. Selections that an
installed AppExchange released managed package makes in its own custom channel are exempt, while
selections from unmanaged or other managed packages count.[^s1] Because of that exemption, a Tooling
API count of distinct `SelectedEntity` values on `PlatformEventChannelMember` can legitimately exceed
five.[^s1] The custom-channel cap is tracked separately from the cap on custom platform event
channels.[^s2]

**Event delivery.** The delivery allocation meters only API-style subscribers: Pub/Sub API, CometD,
`empApi` Lightning components and event relays. Apex triggers and flows on change events don't
consume it.[^s1] It is one pool shared with high-volume platform events, and usage is summed per
subscribed client, so the same 20,000 events sent to two clients uses 40,000.[^s2] The window rolls:
Salesforce checks the last 24 hours each time a new event arrives rather than resetting at a fixed
time.[^s2][^s5] There is no publishing allocation for change events, because the platform itself
publishes them in response to record changes.[^s1]

## Common streaming ceilings

Two further limits are shared across event types.[^s1]

- **Concurrent CometD clients:** 2,000 (Performance/Unlimited), 1,000 (Enterprise), 20 (Developer).[^s1]
- **Message size:** 1 MB; a larger change event isn't delivered and a gap event replaces it.[^s1]

The client cap covers CometD subscribers to platform events, change events, PushTopic and generic
events. Each logged-in `empApi` user counts as one client, and several browser tabs share a single
connection.[^s1]

## What happens when you run out

When the delivery allocation is spent, the subscription is disconnected. CometD clients receive a 403
"Organization total events daily limit exceeded" error, and Pub/Sub API clients receive the error code
`sfdc.platform.eventbus.grpc.subscription.limit.exceeded`.[^s1] Change events are retained for 72 hours,
so a subscriber can resume from its last replay ID once rolling usage falls back under the cap.[^s2]
A design that can't tolerate that gap should be sized with headroom rather than run near the cap.

## The add-on license

A Change Data Capture add-on removes the selected-entity limit and adds a usage-based entitlement of
100,000 delivered events per day, or 3 million per month, plus a grace allocation that Salesforce may
adjust.[^s1] The entitlement resets monthly from the contract start date and applies only to
production orgs, not sandboxes or trials.[^s1] With the add-on, the 24-hour figure shown is 150,000 for
Performance and Unlimited and 125,000 for Enterprise, and monthly overage is assessed against the daily
allocation multiplied by 30.[^s1]

## Monitoring and reducing usage

Setup's Platform Events page shows an Event Allocations section; the REST `limits` resource and Apex
`System.OrgLimit` expose `DailyDeliveredPlatformEvents`, and API version 48.0 and later report
monthly add-on use as `MonthlyPlatformEventsUsageEntitlement`.[^s1] For trends by event, client and
usage type, query `PlatformEventUsageMetric`; for near-real-time tracking, poll the daily value
hourly.[^s1] Monitoring proactively, rather than waiting for a failure, is the general guidance for
every daily allocation.[^s5]

The main levers for staying under the delivery cap are reducing what each subscriber receives:

- **Custom channels with filters**, so a subscriber gets only matching events rather than the whole `ChangeEvents` stream.[^s1][^s3]
- **Fewer subscribers**, since every additional client multiplies delivered-event usage.[^s1]
- **Server-side filtering instead of client-side discarding**, which otherwise still consumes allocation.[^s4]

Filter expressions use a SOQL-like subset over record fields and `ChangeEventHeader` fields, and a
channel holds either change events or platform events, never both.[^s3][^s4]

## Connections

- **Broader:** `kt:governor-limits` is the umbrella for platform quotas; this node is the CDC-specific slice.[^s1]
- **Related:** it governs `kt:change-data-capture` and is consumed by subscribers on `kt:pub-sub-api` and `kt:streaming-api`.[^s1]
- **Related:** `kt:platform-event-channel-member` is where entity selections and filters live, so it drives the entity count.[^s1][^s3]
- **Related:** `kt:orglimits-class` reads `DailyDeliveredPlatformEvents` from Apex for in-org monitoring.[^s1]
- **Contrasts with:** `kt:platform-event-allocations`, which shares the delivery pool but also caps publishing; CDC has no publishing cap.[^s1][^s2]
- **Contrasts with:** `kt:api-request-limits`, a different daily allocation that is often confused with event delivery; both surface through the REST `limits` resource.[^s1][^s5]

## Sources

[^s1]: Salesforce Developers, "Change Data Capture Allocations". https://developer.salesforce.com/docs/platform/change-data-capture/guide/cdc-allocations.html (accessed 2026-11-17)
[^s2]: Salesforce Developers, "Change Data Capture Allocations: Default Allocations". https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_allocations_default_allocations.htm (accessed 2026-11-17)
[^s3]: Salesforce Developers, "Filter Your Stream of Change Events with Channels". https://developer.salesforce.com/docs/platform/change-data-capture/guide/cdc-filter-section.html (accessed 2026-11-17)
[^s4]: Salesforce Developers Blog, "Stream Events at Scale with Event Filters and Field Enrichment". https://developer.salesforce.com/blogs/2023/01/stream-events-at-scale-with-event-filters-and-field-enrichment (accessed 2026-11-17)
[^s5]: Trailhead, "Learn About Daily Rate Limits". https://trailhead.salesforce.com/content/learn/modules/app-development-without-limits/app-development-without-limits-rate (accessed 2026-11-17)
