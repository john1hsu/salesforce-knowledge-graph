---
id: kt:managed-event-subscriptions
type: Feature
title: Managed Event Subscriptions
aliases: [Managed Subscriptions, ManagedEventSubscription, Pub/Sub API managed subscriptions, server-side replay tracking]
domain: integration
summary: >-
  A beta Pub/Sub API capability in which Salesforce stores a subscriber's committed replay ID on the server, so an
  external client defined by a ManagedEventSubscription metadata record can disconnect and resume from its last
  processed event without keeping its own replay store.
release: "Winter '27"
status: beta
broader: [kt:pub-sub-api]
related: [kt:platform-events, kt:change-data-capture, kt:event-driven-architecture, kt:platform-event-channel-member]
relations:
  - {predicate: partOf, object: kt:pub-sub-api}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: configuredVia, object: kt:tooling-api}
  - {predicate: integratesWith, object: kt:change-data-capture}
  - {predicate: governedBy, object: kt:platform-event-allocations}
sources:
  - id: s1
    title: "Managed Event Subscriptions (Beta) (Pub/Sub API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pub-sub-api/guide/managed-sub.html
    type: official-docs
    accessed: 2026-11-19
  - id: s2
    title: "ManagedEventSubscription (Beta) (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_managedeventsubscription.htm
    type: official-docs
    accessed: 2026-11-19
  - id: s3
    title: "Pub/Sub API Basics: Subscribe to Events Using Managed Subscriptions (Beta)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/pub-sub-api-basics/subscribe-to-events-using-managed-subscriptions-beta
    type: official-learning
    accessed: 2026-11-19
  - id: s4
    title: "Pub/Sub API and Event Allocations"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pub-sub-api/guide/allocations.html
    type: official-docs
    accessed: 2026-11-19
  - id: s5
    title: "Pub/Sub API Made Easy via Managed Subscriptions"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/05/pub-sub-api-made-easy-via-managed-subscriptions
    type: official-blog
    accessed: 2026-11-19
created: 2026-11-19
---

# Managed Event Subscriptions

Managed event subscriptions let an external Pub/Sub API subscriber hand replay bookkeeping to Salesforce. Normally a client that wants durable, gap-free delivery must persist the replay ID of the last event it handled and pass that ID back when it reconnects. With a managed subscription, the client commits that ID to the server, and Salesforce resumes delivery after it on the next connection.[^s1][^s3] Salesforce introduced the capability as an open beta in Summer '24, pitching it as a way for clients to run statelessly instead of building their own replay store.[^s5] The current Pub/Sub API and Metadata API documentation still labels it a Beta Service governed by the Beta Services Terms.[^s1][^s2]

## How it works

Each subscription is defined once as a `ManagedEventSubscription` record, created through the Tooling API or deployed as Metadata API source. The Metadata API type has been available since API version 60.0. Its files use the `.managedEventSubscription` suffix in a `managedEventSubscriptions` folder, and deploying or retrieving them requires the Customize Application permission.[^s2] The record names a `topicName` and sets three behaviours. `defaultReplay` sets where delivery starts when no replay ID is stored. `errorRecoveryReplay` sets where it restarts if the committed ID has become invalid. `state` controls whether the subscription may run.[^s1][^s2] Valid topics include a single platform event (`/event/Name__e`), a custom platform event channel, the standard `/data/ChangeEvents` channel, a single object's change event, or a custom change event channel.[^s2]

At run time the client opens the bidirectional `ManagedSubscribe` RPC, identifying the subscription by developer name or record ID. It then sends `ManagedFetchRequest` messages stating how many events it can take, and receives batches in `ManagedFetchResponse` messages.[^s1][^s3] After processing a batch, it embeds a `CommitReplayRequest` carrying the last processed replay ID in its next fetch request. The server answers with a `CommitReplayResponse` reporting whether the commit succeeded.[^s1][^s5] Trailhead also advises committing after an empty batch, using the `latest_replay_id` the response returns. That value can run ahead of the last delivered event because the event bus interleaves streams from many orgs, and committing it saves the server a long seek on resume.[^s3] When events are pending but nothing new has arrived, the server sends keepalives; otherwise the client must keep sending fetch or commit requests to hold the stream open.[^s3]

## Limits and gotchas

- An org can create at most **200** unique managed subscriptions, and a single `ManagedSubscribe` call can request up to **100** events in total across its fetch requests.[^s4]
- Managed subscriptions consume the same event delivery allocations as ordinary `Subscribe` calls, so they don't add delivery capacity.[^s1][^s4]
- Both replay presets accept `LATEST` (the default) or `EARLIEST`. `EARLIEST` reaches back about 72 hours and can slow delivery and drain allocations if overused.[^s2]
- Setting `state` to `STOP` disconnects the client and deletes the committed replay ID, so a later run restarts from `defaultReplay`. Wait at least five minutes before switching back to `RUN`; `PAUSE` is reserved for internal use.[^s1][^s2]
- A subscription belongs to exactly one client and can't be shared. Record changes can take a few minutes to reach Pub/Sub API, and a deleted record's developer name shouldn't be reused.[^s1]
- Resuming only works inside the event bus's three-day retention window; an older committed ID triggers `errorRecoveryReplay` instead.[^s1][^s5]

## When to use it (and when not)

Use a managed subscription when a Pub/Sub API consumer needs at-least-once processing across restarts but you'd rather not run a database or cache just to remember replay IDs, for example a containerised or serverless worker.[^s5] Clients must use the updated Pub/Sub API proto file that defines `ManagedSubscribe`.[^s5] Keep the classic `Subscribe` RPC with client-stored replay IDs when you need several consumers to read the same topic independently, since managed subscriptions can't be shared, or when beta terms are unacceptable for a production integration.[^s1][^s2] Because stopping wipes the stored position, operational runbooks should treat `STOP` as a reset rather than a pause.[^s1]

## Connections

Managed event subscriptions are **part of** (and narrower than) **Pub/Sub API**, adding the `ManagedSubscribe` RPC alongside its standard methods.[^s3] They are **configured via** the **Metadata API** and **Tooling API**, which carry the `ManagedEventSubscription` type.[^s2] Their topics are **platform events** and **change data capture** events or channels, and custom channels assembled with **platform event channel members** can be targeted as one topic.[^s2] Delivery is **governed by** the same **platform event allocations** as other subscriptions.[^s4] The feature serves the broader **event-driven architecture** pattern by making durable consumers simpler to build.[^s5]

## Sources

[^s1]: Salesforce Developers, "Managed Event Subscriptions (Beta)". https://developer.salesforce.com/docs/platform/pub-sub-api/guide/managed-sub.html (accessed 2026-11-19)
[^s2]: Salesforce Developers, "ManagedEventSubscription (Beta)". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_managedeventsubscription.htm (accessed 2026-11-19)
[^s3]: Trailhead, "Pub/Sub API Basics: Subscribe to Events Using Managed Subscriptions (Beta)". https://trailhead.salesforce.com/content/learn/modules/pub-sub-api-basics/subscribe-to-events-using-managed-subscriptions-beta (accessed 2026-11-19)
[^s4]: Salesforce Developers, "Pub/Sub API and Event Allocations". https://developer.salesforce.com/docs/platform/pub-sub-api/guide/allocations.html (accessed 2026-11-19)
[^s5]: Salesforce Developers Blog, "Pub/Sub API Made Easy via Managed Subscriptions". https://developer.salesforce.com/blogs/2024/05/pub-sub-api-made-easy-via-managed-subscriptions (accessed 2026-11-19)
