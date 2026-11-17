---
id: kt:platform-event-channel-member
type: MetadataType
title: Platform Event Channel Member
aliases: [PlatformEventChannelMember, channel member, event channel member, custom channel member]
domain: integration
summary: >-
  The metadata component that places one event entity on a streaming channel: it selects a change event on the
  standard ChangeEvents channel or a custom channel, or a platform event on a custom channel, and can carry a
  SOQL-like filter expression and enriched fields that shape what subscribers receive.
release: "Winter '27"
status: current
broader: [kt:metadata-api, kt:event-driven-architecture]
related: [kt:change-data-capture, kt:platform-events, kt:platform-event-allocations]
relations:
  - {predicate: configuredVia, object: kt:tooling-api}
  - {predicate: consumedBy, object: kt:pub-sub-api}
  - {predicate: consumedBy, object: kt:streaming-api}
  - {predicate: mitigates, object: kt:change-data-capture-allocations}
sources:
  - id: s1
    title: "PlatformEventChannelMember (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_platformeventchannelmember.htm
    type: official-docs
    accessed: 2026-11-17
  - id: s2
    title: "Group Platform Events into One Stream with a Custom Channel (Platform Events Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_subscribe_custom_channels.htm
    type: official-docs
    accessed: 2026-11-17
  - id: s3
    title: "Create a Custom Channel and Add Platform Events with Tooling API (Platform Events Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_custom_channel_tooling_api.htm
    type: official-docs
    accessed: 2026-11-17
  - id: s4
    title: "Filter Your Stream of Change Events with Channels (Change Data Capture Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/change-data-capture/guide/cdc-filter-section.html
    type: official-docs
    accessed: 2026-11-17
  - id: s5
    title: "Stream Events at Scale with Event Filters and Field Enrichment"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2023/01/stream-events-at-scale-with-event-filters-and-field-enrichment
    type: official-blog
    accessed: 2026-11-17
  - id: s6
    title: "Add the Order Event and the Filter Expression to a Channel Member (Filter Your Platform Event Stream project)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/filter-your-platform-event-stream/add-the-order-event-and-the-filter-expression-to-a-channel-member
    type: official-learning
    accessed: 2026-11-17
created: 2026-11-17
---

# Platform Event Channel Member

`PlatformEventChannelMember` is the Metadata API and Tooling API type that puts a single event entity onto a
streaming channel. It represents either an object selected for Change Data Capture on the standard `ChangeEvents`
channel or a custom channel, or a platform event selected on a custom channel. It has existed since API version
47.0, and deploying or retrieving it requires the Customize Application permission.[^s1] Its companion type,
`PlatformEventChannel`, defines the custom channel itself; the member is what links an event to that channel.[^s2]

## How it works

A member has two required fields and two optional ones:[^s1]

- `eventChannel`: the channel name, either `ChangeEvents` or a custom channel such as `SalesEvents__chn`.[^s1]
- `selectedEntity`: the event to stream, such as `AccountChangeEvent`, `MyObject__ChangeEvent` or a platform event `Order__e`.[^s1][^s3]
- `enrichedFields` (API 51.0+): change event fields always sent on update and delete events, even when unchanged.[^s1]
- `filterExpression` (API 56.0+): a SOQL-based expression so only matching events are delivered to subscribers.[^s1]

Every selected entity is its own component, so a channel carrying five events has five members. Member full names
follow `ChannelName_EventName`, and because a double underscore is only allowed as a suffix or namespace prefix,
a custom channel's `__chn` collapses to `_chn` inside the member name (for example
`SalesEvents_chn_AccountChangeEvent`).[^s1] To retrieve a channel together with its members, list both
`PlatformEventChannel` and `PlatformEventChannelMember` in `package.xml`; the member type supports the `*`
wildcard.[^s1]

For platform events, the usual flow is to create a `PlatformEventChannel` with `channelType` set to `event`, then
POST one member per event to the Tooling API `sobjects/PlatformEventChannelMember` resource.[^s3] Subscribers then
listen on `/event/ChannelName__chn` and receive a single interleaved stream from all member events, for example
regional order events feeding one order-management client.[^s2] Change event channels use the
`/data/ChannelName__chn` path instead.[^s4] Salesforce moved channel and member creation to the Tooling and
Metadata APIs as of Spring '23.[^s5]

Filters are written like a SOQL `WHERE` clause, for example `City__c='San Francisco' AND Amount__c<1000`, and support
only a subset of SOQL operators and field types.[^s6] For change events, expressions can reference record fields and
`ChangeEventHeader` fields such as the change type, and fields used in a filter are added to the change event
automatically.[^s4][^s5] The developer blog that introduced the pattern described enrichment as supporting up to ten
fields, which is useful for always sending an immutable external ID to a downstream system.[^s5]

## Limits and gotchas

- **No create or delete calls.** `createMetadata()` and `deleteMetadata()` aren't supported; remove a member by deploying `destructiveChanges.xml`.[^s1]
- **One event product per channel.** A channel holds platform events or change events, never both, and its `ChannelType` and `EventType` are fixed once created.[^s2][^s5]
- **Event type restrictions.** Custom platform event channels accept high-volume custom platform events and Real-Time Event Monitoring events, not standard or legacy standard-volume platform events.[^s2]
- **Some members are Metadata-only.** `ApiEventStream` and `ReportEventStream` can be added through the Metadata API but not the Tooling API.[^s2]
- **Deleting a channel deletes its members.**[^s2]
- **Apex triggers don't use channels.** Custom channels and filters serve Pub/Sub API clients, CometD clients and event relays; Apex triggers subscribe without them.[^s2][^s4]
- **Government Cloud.** Orgs created there before January 14, 2022 must ask Salesforce to enable channel filtering.[^s4]

Channel and member counts have their own allocations, which differ by event type; the CDC and platform event
allocation pages hold the numbers.[^s2]

## When to use it (and when not)

Use a custom channel with filtered members when an external subscriber needs only a slice of a high-volume stream,
or when one client should consume several related events as one stream.[^s2][^s4] Server-side filtering means
unwanted events are never sent, which lowers delivered-event consumption compared with discarding them in the
client.[^s4][^s5] Keep filtered streams on a custom channel rather than the standard `ChangeEvents` channel so they
are isolated from unfiltered subscribers.[^s4] For in-org processing with Apex triggers, channels add nothing,
since triggers subscribe directly to the event.[^s2]

## Connections

- **Broader:** `kt:metadata-api` is where the type is defined and deployed, and `kt:event-driven-architecture` is the pattern channels serve.[^s1][^s2]
- **Related:** `kt:change-data-capture` and `kt:platform-events` are the two event products a member can select.[^s1][^s2]
- **Configured via:** `kt:tooling-api`, the usual REST surface for creating channels and members.[^s3][^s6]
- **Consumed by:** `kt:pub-sub-api` and `kt:streaming-api` (CometD) subscribers, the clients that receive channel streams.[^s2][^s4]
- **Mitigates / related:** filtering reduces pressure on `kt:change-data-capture-allocations` and `kt:platform-event-allocations` delivery quotas.[^s4][^s5]

## Sources

[^s1]: Salesforce Developers, "PlatformEventChannelMember (Metadata API Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_platformeventchannelmember.htm (accessed 2026-11-17)
[^s2]: Salesforce Developers, "Group Platform Events into One Stream with a Custom Channel". https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_subscribe_custom_channels.htm (accessed 2026-11-17)
[^s3]: Salesforce Developers, "Create a Custom Channel and Add Platform Events with Tooling API". https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_custom_channel_tooling_api.htm (accessed 2026-11-17)
[^s4]: Salesforce Developers, "Filter Your Stream of Change Events with Channels". https://developer.salesforce.com/docs/platform/change-data-capture/guide/cdc-filter-section.html (accessed 2026-11-17)
[^s5]: Salesforce Developers Blog, "Stream Events at Scale with Event Filters and Field Enrichment". https://developer.salesforce.com/blogs/2023/01/stream-events-at-scale-with-event-filters-and-field-enrichment (accessed 2026-11-17)
[^s6]: Trailhead, "Add the Order Event and the Filter Expression to a Channel Member". https://trailhead.salesforce.com/content/learn/projects/filter-your-platform-event-stream/add-the-order-event-and-the-filter-expression-to-a-channel-member (accessed 2026-11-17)
