---
id: kt:change-data-capture
type: Feature
title: Change Data Capture
aliases: [CDC, change events, ChangeEvent object, change event trigger]
domain: integration
summary: >-
  Salesforce feature that publishes a change event to the event bus whenever a record of a selected object is created,
  updated, deleted or undeleted, so external systems and asynchronous Apex can replicate or react to data changes in
  near real time without polling.
release: "Winter '27"
status: current
broader: [kt:event-driven-architecture]
related: [kt:platform-events, kt:apex-triggers, kt:asynchronous-apex]
relations:
  - {predicate: queriedWith, object: kt:pub-sub-api}
  - {predicate: governedBy, object: kt:change-data-capture-allocations}
  - {predicate: configuredVia, object: kt:platform-event-channel-member}
  - {predicate: alternativeTo, object: kt:outbound-messaging}
sources:
  - id: s1
    title: "What Is Change Data Capture? (Change Data Capture Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_what.htm
    type: official-docs
    accessed: 2026-10-31
  - id: s2
    title: "Change Data Capture: Learn Change Data Capture Characteristics"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/change-data-capture/learn-change-data-capture-characteristics
    type: official-learning
    accessed: 2026-10-31
  - id: s3
    title: "Change Data Capture Allocations"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/change-data-capture/guide/cdc-allocations.html
    type: official-docs
    accessed: 2026-10-31
  - id: s4
    title: "Change Event Triggers"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_trigger_intro.htm
    type: official-docs
    accessed: 2026-10-31
  - id: s5
    title: "Subscribe to Change Events (Change Data Capture Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_subscribe.htm
    type: official-docs
    accessed: 2026-10-31
  - id: s6
    title: "Design Considerations for Change Data Capture and Platform Events"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2022/10/design-considerations-for-change-data-capture-and-platform-events
    type: official-blog
    accessed: 2026-10-31
created: 2026-10-31
---

# Change Data Capture

Change Data Capture (CDC) keeps an external system's copy of Salesforce data current by pushing change notifications
instead of relying on scheduled exports, imports or repeated API polling. Salesforce positions it as the mechanism for
near-real-time replication of Salesforce records into other systems.[^s1] Change events are available for every custom
object and for a subset of standard objects; you choose which ones publish on the Change Data Capture page in Setup, or
programmatically through the `PlatformEventChannelMember` metadata type, which also binds objects to custom
channels.[^s1]

## How it works

Each enabled object gets its own change event object: `Account` publishes `AccountChangeEvent`, and a custom
`Shipment__c` publishes `Shipment__ChangeEvent`.[^s6] An event fires for four change types: `CREATE`, `UPDATE`,
`DELETE` and `UNDELETE`.[^s2] Every message carries a `ChangeEventHeader` with fields such as `entityName`,
`recordIds`, `changeType`, `changeOrigin`, `transactionKey`, `sequenceNumber`, `commitTimestamp`, `commitUser`,
`nulledFields`, `diffFields` and `changedFields`.[^s2] The `transactionKey` and `sequenceNumber` let a subscriber
reassemble all changes from one Salesforce transaction, and Trailhead recommends replaying a transaction's changes as a
single commit on the target side.[^s2] When identical changes hit several records of the same object within one second,
Salesforce may merge them into one event that lists all affected IDs in `recordIds`.[^s2]

Events are delivered in the order of their committed transactions on standard or custom channels, and channel names are
case-sensitive.[^s5] External clients typically subscribe with the Pub/Sub API, a gRPC/HTTP/2 interface that returns
binary Avro-encoded messages and lets the client request only as many events as it can process; CometD (Streaming API)
and event relays are also supported subscription paths.[^s5] Pub/Sub API subscribers can also request *enrichment*:
extra fields that are always included in the event even when they did not change, which is useful for carrying an
external ID needed for matching.[^s2]

Inside Salesforce, a **change event trigger** (for example on `AccountChangeEvent`) subscribes from Apex. These triggers
support only `after insert`, run asynchronously outside the originating transaction, receive batches of up to 2,000
messages by default, and run as the Automated Process entity unless overridden with `PlatformEventSubscriberConfig`.[^s4]

## Limits and gotchas

Verified against the Winter '27 documentation: without an add-on, an org may select at most **5 entities** across all
channels, and the 24-hour event delivery allocation is **50,000** (Performance and Unlimited), **25,000** (Enterprise)
and **10,000** (Developer Edition); orgs can create up to 100 custom channels.[^s3] Events are retained for **72 hours**
and can be replayed by Replay ID from Pub/Sub API or CometD after a subscriber reconnects.[^s3] The CDC add-on removes
the entity cap and adds 100,000 delivered events per day (3 million per month) plus a grace allocation.[^s3]

- **Gap and overflow events.** When Salesforce cannot generate a normal event, it sends a gap event with the record ID
  but no field data; very large change volumes produce overflow events, also without record data. Subscribers must
  re-query the source record in both cases.[^s2]
- **Null semantics in Apex.** Unchanged fields arrive as null in change event triggers, so use `nulledFields` to tell
  "set to null" from "unchanged"; large text fields can arrive as a diff flagged in `diffFields`.[^s4]
- **Security model.** Field-level security limits which fields a subscriber sees, but sharing settings are not
  applied.[^s2]
- **Debugging.** Trigger logs belong to Automated Process, so you need a trace flag on that entity; audit fields on
  records the trigger writes also reference Automated Process.[^s4]
- **Bulk loads.** Batch Apex, ETL jobs and data loads publish every changed record and can exhaust delivery allocations;
  channel filters reduce what subscribers receive but not what is published.[^s6]

## When to use it (and when not)

Use CDC when the goal is replicating or reacting to record-level changes with no custom publishing code — Salesforce's
developer blog calls it the quickest way to start publishing events.[^s6] Prefer a custom platform event when you need a
business-level message, a curated payload, or to publish only records that meet criteria, accepting the upkeep of the
flow or Apex that publishes it.[^s6] Inside the platform, put transaction-critical logic in ordinary object triggers and
resource-heavy follow-up work in change event triggers.[^s5]

## Connections

CDC is a specialised form of `kt:platform-events` within an `kt:event-driven-architecture`: change events are
platform event objects generated by Salesforce rather than defined by you.[^s6] It is consumed through
`kt:pub-sub-api` and CometD, governed by its own delivery and entity allocations
(`kt:change-data-capture-allocations`), and configured through `PlatformEventChannelMember`
(`kt:platform-event-channel-member`).[^s1][^s3][^s5] Change event triggers relate to `kt:apex-triggers` and
`kt:asynchronous-apex` because they run after commit in a separate transaction.[^s4] As a push-based replication
option that removes the need for polling or scheduled exports, it is an alternative to `kt:outbound-messaging`.[^s1]

## Sources

[^s1]: Salesforce Developers, "What Is Change Data Capture?". https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_what.htm (accessed 2026-10-31)
[^s2]: Trailhead, "Change Data Capture: Learn Change Data Capture Characteristics". https://trailhead.salesforce.com/content/learn/modules/change-data-capture/learn-change-data-capture-characteristics (accessed 2026-10-31)
[^s3]: Salesforce Developers, "Change Data Capture Allocations". https://developer.salesforce.com/docs/platform/change-data-capture/guide/cdc-allocations.html (accessed 2026-10-31)
[^s4]: Salesforce Developers, "Change Event Triggers". https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_trigger_intro.htm (accessed 2026-10-31)
[^s5]: Salesforce Developers, "Subscribe to Change Events". https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_subscribe.htm (accessed 2026-10-31)
[^s6]: Salesforce Developers Blog, "Design Considerations for Change Data Capture and Platform Events". https://developer.salesforce.com/blogs/2022/10/design-considerations-for-change-data-capture-and-platform-events (accessed 2026-10-31)
