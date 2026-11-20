---
id: kt:pushtopic-streaming-allocations
type: Limit
title: PushTopic Streaming Allocations
aliases: [PushTopic allocations, PushTopic limits, generic streaming allocations, legacy Streaming API allocations, DailyDurableStreamingApiEvents]
domain: integration
summary: >-
  The org-wide caps on Salesforce's legacy PushTopic and generic Streaming API events: how many PushTopic records and
  streaming channels an org can define, how many CometD clients can subscribe at once, and how many notifications
  can be delivered in a rolling 24 hours, by edition.
release: "Winter '27"
status: current
broader: [kt:governor-limits]
related: [kt:streaming-api, kt:orglimits-class, kt:environment-hub, kt:soql]
relations:
  - {predicate: contrastsWith, object: kt:platform-event-allocations}
  - {predicate: contrastsWith, object: kt:change-data-capture-allocations}
  - {predicate: contrastsWith, object: kt:api-request-limits}
sources:
  - id: s1
    title: "PushTopic Streaming Allocations (Streaming API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.api_streaming.meta/api_streaming/limits.htm
    type: official-docs
    accessed: 2026-11-20
  - id: s2
    title: "Generic Streaming Allocations (Streaming API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/limits_generic.htm
    type: official-docs
    accessed: 2026-11-20
  - id: s3
    title: "Monitoring Event Usage (Streaming API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/using_streaming_api_monitoring_events_usage.htm
    type: official-docs
    accessed: 2026-11-20
  - id: s4
    title: "Monitor PushTopic and Generic Event Usage with the REST API"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.262.0.api_streaming.meta/api_streaming/using_streaming_api_monitoring_events_usage_api.htm
    type: official-docs
    accessed: 2026-11-20
  - id: s5
    title: "Considerations for Multiple Notifications in the Same Transaction"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/using_streaming_api_multiple_notifications.htm
    type: official-docs
    accessed: 2026-11-20
created: 2026-11-20
---

# PushTopic Streaming Allocations

PushTopic streaming allocations are the default quotas Salesforce applies to the legacy PushTopic
events of `kt:streaming-api`. They are org-level allocations rather than per-transaction governor
limits, and the Streaming API guide states that they apply to PushTopic consumers in every API
version.[^s1] A sibling table, the generic streaming allocations, governs the other legacy event type,
generic events pushed through StreamingChannel records; both are summarized here because they share
clients, error behaviour and monitoring.[^s1][^s2]

## The PushTopic allocations

The Winter '27 (release 264) documentation lists these values:[^s1]

| Allocation | Performance / Unlimited | Enterprise | All other editions |
|---|---|---|---|
| PushTopic records per org | 100 | 50 | 40 |
| Concurrent CometD clients, all channels and event types | 2,000 | 1,000 | 20 |
| Delivered notifications in 24 hours, shared by all CometD clients | 1,000,000 | 200,000 | 50,000 [^s1] |

Free orgs get only 10,000 delivered notifications in 24 hours. Salesforce counts Developer Edition
orgs and trial orgs of any edition as free orgs, including partner test and demo orgs spun up through
`kt:environment-hub`.[^s1] Sandboxes inherit the allocations of the production org they belong to.[^s1]

Several fixed ceilings apply in every edition:[^s1]

- The `Query` field of a PushTopic holds a SOQL statement of at most 1,300 characters.[^s1]
- A PushTopic name can be at most 25 characters long.[^s1]
- The CometD socket times out after 110 seconds during a connection, and a client must reconnect within 40 seconds after a successful connect.[^s1]

## The generic streaming allocations

Generic events have their own channel cap and delivery pool. Every paid edition can define 1,000
streaming channels and free orgs 200.[^s2] With durable generic streaming (API version 37.0 and
later), the 24-hour delivery allocation is 1,000,000 for Performance and Unlimited, 200,000 for
Enterprise, 100,000 for Professional and 10,000 for free orgs.[^s2] Clients on API version 36.0 or
earlier get the older non-durable figures of 100,000 for paid editions and 10,000 for free orgs, so
an outdated client version shrinks the usable pool as well as losing replay.[^s2]

## What happens when you run out

When the daily delivery allocation is exhausted, the subscriber receives
`403::Organization total events daily limit exceeded` on the Bayeux `/meta/connect` channel, either
when it first connects or on an open connection.[^s1][^s2] Notifications produced after the cap stay
on the event bus and can still be retrieved within the 24-hour retention window, so a client that
tracks its replay ID can catch up once usage falls.[^s1][^s2] The only way to raise these limits is
to contact Salesforce.[^s1][^s2]

Volume can also surprise you through transaction behaviour. From API version 37.0, a field update
that triggers further changes on the same record can produce extra notifications, even for untracked
fields and regardless of whether the values match the PushTopic query.[^s5] When one record generates
several notifications in a single transaction, the last ones are delivered first.[^s5]

## Monitoring usage

The REST API limits resource reports streaming usage. For durable streaming (API version 37.0 and
later) the keys are `DailyDurableStreamingApiEvents` for PushTopic events,
`DailyDurableGenericStreamingApiEvents` for generic events and `DurableStreamingApiConcurrentClients`
for connected subscribers.[^s4] Older clients map to `DailyStreamingApiEvents`,
`DailyGenericStreamingApiEvents` and `StreamingApiConcurrentClients`.[^s4] Only the pre-37.0 PushTopic
count also appears in Setup, on the Company Information page; full PushTopic and generic usage needs
the API.[^s3]

## When it matters

These allocations matter mostly for maintaining existing integrations, because PushTopic and generic
events are legacy features. The concurrent-client cap counts subscribers across all channels and all event types,
so a CometD estate shares one connection budget with any platform-event or change-event clients.[^s1][^s2] For new
designs, `kt:change-data-capture` and `kt:platform-events` have their own allocation models and
delivery options; sizing a migration means comparing those quotas with the counters above.

## Connections

- **Broader:** `kt:governor-limits`, the umbrella for platform quotas; this node is the legacy-streaming slice.[^s1]
- **Related:** governs the PushTopic and generic channels of `kt:streaming-api`, and the `kt:soql` query that defines each PushTopic is capped at 1,300 characters.[^s1]
- **Related:** `kt:environment-hub` partner test and demo orgs fall under the free-org allocation.[^s1]
- **Related:** `kt:orglimits-class` is the Apex-side view of org limits, complementing the REST limits resource that reports these counters.[^s4]
- **Contrasts with:** `kt:platform-event-allocations` and `kt:change-data-capture-allocations`, the quota models for the recommended event types, which share the concurrent-client ceiling.[^s1]
- **Contrasts with:** `kt:api-request-limits`, a separate daily allocation also surfaced by the REST limits resource.[^s4]

## Sources

[^s1]: Salesforce Developers, "PushTopic Streaming Allocations". https://developer.salesforce.com/docs/atlas.en-us.264.0.api_streaming.meta/api_streaming/limits.htm (accessed 2026-11-20)
[^s2]: Salesforce Developers, "Generic Streaming Allocations". https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/limits_generic.htm (accessed 2026-11-20)
[^s3]: Salesforce Developers, "Monitoring Event Usage". https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/using_streaming_api_monitoring_events_usage.htm (accessed 2026-11-20)
[^s4]: Salesforce Developers, "Monitor PushTopic and Generic Event Usage with the REST API". https://developer.salesforce.com/docs/atlas.en-us.262.0.api_streaming.meta/api_streaming/using_streaming_api_monitoring_events_usage_api.htm (accessed 2026-11-20)
[^s5]: Salesforce Developers, "Considerations for Multiple Notifications in the Same Transaction". https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/using_streaming_api_multiple_notifications.htm (accessed 2026-11-20)
