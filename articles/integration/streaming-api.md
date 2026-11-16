---
id: kt:streaming-api
type: API
title: Streaming API
aliases: [Salesforce Streaming API, CometD Streaming API, Bayeux Streaming API]
domain: integration
summary: >-
  Salesforce's original push-style event API: clients use CometD over the Bayeux protocol (HTTP long polling) to
  subscribe to channels for platform events, change data capture events and the legacy PushTopic and generic events,
  receiving notifications in near real time instead of polling for changes.
release: "Winter '27"
status: current
broader: [kt:salesforce-apis, kt:event-driven-architecture]
related: [kt:platform-events, kt:change-data-capture, kt:pub-sub-api, kt:heroku-connect]
relations:
  - {predicate: alternativeTo, object: kt:pub-sub-api}
  - {predicate: integratesWith, object: kt:platform-events}
  - {predicate: integratesWith, object: kt:change-data-capture}
  - {predicate: governedBy, object: kt:pushtopic-streaming-allocations}
  - {predicate: dependsOn, object: kt:salesforce-sharing-model}
sources:
  - id: s1
    title: "Getting Started with Streaming API (Streaming API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-streaming/guide/intro-stream.html
    type: official-docs
    accessed: 2026-11-16
  - id: s2
    title: "PushTopic Events (Legacy)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/pushtopic_events_intro.htm
    type: official-docs
    accessed: 2026-11-16
  - id: s3
    title: "PushTopic Streaming Allocations"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/limits.htm
    type: official-docs
    accessed: 2026-11-16
  - id: s4
    title: "Generic Events (Legacy)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/generic_streaming_intro.htm
    type: official-docs
    accessed: 2026-11-16
  - id: s5
    title: "Streaming Event Features"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/event_comparison.htm
    type: official-docs
    accessed: 2026-11-16
  - id: s6
    title: "Subscribe to Platform Event Notifications with CometD (Platform Events Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_subscribe_cometd.htm
    type: official-docs
    accessed: 2026-11-16
created: 2026-11-16
---

# Streaming API

Streaming API is Salesforce's push-based event delivery API. Instead of an app repeatedly querying for changed records, a client subscribes to a channel and Salesforce sends it notifications in near real time, which cuts out wasted API calls from frequent polling.[^s1] It is the older of Salesforce's two external subscription APIs: transport runs on the Bayeux protocol, implemented with CometD, using HTTP/1.1 long polling.[^s1] Salesforce now recommends the gRPC-based Pub/Sub API for new apps that publish or subscribe to platform events and change data capture events.[^s1][^s6]

## Event types

Streaming API carries four kinds of event:[^s1][^s5]

- **Platform events**: custom, strongly typed messages that Apex, APIs and Flow can publish.[^s5]
- **Change data capture (CDC) events**: auto-published record-change events with a fixed payload.[^s5]
- **PushTopic events (legacy)**: record-change notifications defined by a SOQL query on a PushTopic record.[^s2]
- **Generic events (legacy)**: arbitrary payloads sent to a StreamingChannel through a REST resource.[^s4]

PushTopic and generic events are labelled legacy: Salesforce no longer adds features to them and offers only limited support.[^s2][^s4] Its feature comparison points PushTopic users to Change Data Capture and generic-event users to platform events.[^s5] The two legacy types can only be consumed through CometD, whereas platform and CDC events can also be received by Pub/Sub API and Apex triggers.[^s5]

## How it works

A client opens a CometD session against the org's endpoint (the path ends in `/cometd/` plus an API version) and subscribes to a channel; platform event channels take the form `/event/Event_Name__e`, and subscribing to one works the same way as subscribing to a PushTopic or generic channel apart from the channel name.[^s6] Events arrive in order of replay ID, sometimes several in one batch, and each message carries the schema ID, payload and event metadata, including the replay ID.[^s6] Salesforce advises giving the client a receive buffer of at least 10 MB.[^s6] Salesforce recommends using the org's My Domain login URL in the endpoint so subscriptions survive instance refreshes and migrations.[^s1]

For a PushTopic, you write a SOQL query that defines the channel. When a record is created, updated, deleted or undeleted, Salesforce evaluates the change against that query and notifies subscribers if it matches.[^s2] Notifications respect sharing, so a user only hears about records they can see, and subscription filters can narrow the stream further.[^s2] Generic events instead need a StreamingChannel record; you push messages through the Streaming Channel Push REST resource and can target specific users, teams or the whole org.[^s4]

Since API version 37.0, durable streaming lets clients replay events that were stored while they were disconnected; clients on 36.0 or earlier can miss messages.[^s1] PushTopic and generic events are kept for 24 hours, while high-volume platform events and CDC events are kept for 72 hours.[^s1][^s5]

## Limits and gotchas

PushTopic allocations depend on edition (verified for Winter '27):[^s3]

- **Topics per org**: 100 in Performance and Unlimited, 50 in Enterprise, 40 in other supported editions.[^s3]
- **Concurrent clients across all channels and event types**: 2,000, 1,000 and 20 respectively.[^s3]
- **Event deliveries per 24 hours, shared by all CometD clients**: 1,000,000, 200,000 and 50,000 (10,000 for free orgs).[^s3]

A PushTopic query can be at most 1,300 characters and its name at most 25 characters.[^s3] The CometD socket times out after 110 seconds, and a client must reconnect within 40 seconds after a successful connection.[^s3] Exceeding the daily delivery allocation returns a `403::Organization total events daily limit exceeded` error on the `/meta/connect` channel, but events produced afterwards stay on the event bus for the 24-hour retention window.[^s3] Sandboxes get the same allocations as their production org.[^s3]

Generic events reach clients only while their Salesforce session is active, unless durable generic streaming is used, and StreamingChannel is not available to Experience Cloud users or legacy Customer Portals.[^s4] Standard-volume platform events are no longer available; only those defined before Spring '19 remain.[^s1]

## When to use it (and when not)

Streaming API still works with any org where the API is enabled, so existing CometD subscribers to platform or CDC channels can stay on it.[^s1][^s6] For new external integrations, Pub/Sub API is the recommended route: it uses gRPC and HTTP/2, sends binary messages and supports many languages.[^s1] Avoid building new solutions on PushTopic or generic events; use CDC for record changes and platform events for custom messages.[^s5]

## Connections

Streaming API sits under `kt:salesforce-apis` and is one of the delivery mechanisms of `kt:event-driven-architecture`.[^s1] It is an `alternativeTo` `kt:pub-sub-api`, which Salesforce recommends for new work, and it `integratesWith` `kt:platform-events` and `kt:change-data-capture`, both of which it can subscribe to.[^s1][^s5] Its PushTopic allocations form the `kt:pushtopic-streaming-allocations` limit node.[^s3] Because PushTopic notifications honour record visibility, it `dependsOn` `kt:salesforce-sharing-model`.[^s2] The `kt:heroku-connect` article links here as an integration neighbour.

## Sources

[^s1]: Salesforce Developers, "Getting Started with Streaming API". https://developer.salesforce.com/docs/platform/api-streaming/guide/intro-stream.html (accessed 2026-11-16)
[^s2]: Salesforce Developers, "PushTopic Events (Legacy)". https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/pushtopic_events_intro.htm (accessed 2026-11-16)
[^s3]: Salesforce Developers, "PushTopic Streaming Allocations". https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/limits.htm (accessed 2026-11-16)
[^s4]: Salesforce Developers, "Generic Events (Legacy)". https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/generic_streaming_intro.htm (accessed 2026-11-16)
[^s5]: Salesforce Developers, "Streaming Event Features". https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/event_comparison.htm (accessed 2026-11-16)
[^s6]: Salesforce Developers, "Subscribe to Platform Event Notifications with CometD". https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_subscribe_cometd.htm (accessed 2026-11-16)
