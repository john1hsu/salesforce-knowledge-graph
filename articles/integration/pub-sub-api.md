---
id: kt:pub-sub-api
type: API
title: Pub/Sub API
aliases: [PubSub API, Salesforce Pub/Sub API, gRPC Pub/Sub API, ManagedSubscribe]
domain: integration
summary: >-
  Salesforce's gRPC-based API that gives external clients a single interface to publish platform events, subscribe to
  platform, change data capture and real-time event monitoring events, and retrieve event schemas, using binary
  Apache Avro payloads and client-controlled flow.
release: "Winter '27"
status: current
broader: [kt:event-driven-architecture]
related: [kt:platform-events, kt:change-data-capture, kt:bulk-api-2]
relations:
  - {predicate: integratesWith, object: kt:platform-events}
  - {predicate: integratesWith, object: kt:change-data-capture}
  - {predicate: alternativeTo, object: kt:streaming-api}
  - {predicate: governedBy, object: kt:platform-event-allocations}
  - {predicate: configuredVia, object: kt:managed-event-subscriptions}
sources:
  - id: s1
    title: "Get Started with Pub/Sub API (Pub/Sub API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pub-sub-api/guide/intro.html
    type: official-docs
    accessed: 2026-11-02
  - id: s2
    title: "Pub/Sub API Basics: Get to Know Pub/Sub API"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/pub-sub-api-basics/get-to-know-pubsub-api
    type: official-learning
    accessed: 2026-11-02
  - id: s3
    title: "Pub/Sub API and Event Allocations"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pub-sub-api/guide/allocations.html
    type: official-docs
    accessed: 2026-11-02
  - id: s4
    title: "Managed Event Subscriptions (Beta)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pub-sub-api/guide/managed-sub.html
    type: official-docs
    accessed: 2026-11-02
  - id: s5
    title: "Subscribe with Pub/Sub API (Change Data Capture Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_subscribe_pubsub_api.htm
    type: official-docs
    accessed: 2026-11-02
  - id: s6
    title: "Pub/Sub API: Building Event-Driven Integrations Just Got Even Easier"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2021/07/pub-sub-api-building-event-driven-integrations-just-got-even-easier
    type: official-blog
    accessed: 2026-11-02
created: 2026-11-02
---

# Pub/Sub API

Pub/Sub API is the Salesforce interface that external applications use to exchange real-time event messages with an org. One API covers publishing events, subscribing to them, and fetching their schemas. Supported event types are platform events, change data capture (CDC) events and real-time event monitoring events, plus some standard events.[^s1] It also consolidates work that used to be split across APIs. Before it, integrations published through SOAP, REST or Bulk and subscribed through the CometD-based Streaming API.[^s6] Salesforce announced a pilot in mid-2021, and an update to that announcement records general availability in July 2022.[^s6]

## How it works

The API runs on gRPC over HTTP/2 and sends binary event messages encoded with Apache Avro schemas. HTTP/2 compression and Avro's compact binary encoding keep payloads smaller and cheaper to process than JSON-based APIs.[^s1][^s2] The service is defined in a published `.proto` file, so clients can be generated for any gRPC-supported language. Salesforce cites eleven supported languages, including Java, Python, Node and C++.[^s1][^s5]

Its main RPC methods fall into two groups. `Subscribe`, `ManagedSubscribe` and `PublishStream` are bidirectional streaming calls, each with independent request and response streams. `Publish` is a unary call.[^s2] Because `PublishStream` doesn't wait for each response before sending the next batch, it reaches a higher publish rate than `Publish`. Every publish returns a final `PublishResult` per event showing whether the event was stored on the event bus. REST API and Apex publishing return only an intermediate queueing result.[^s2] Clients pass each event's schema ID to `GetSchema` to obtain the schema needed to decode the payload.[^s6]

Subscriptions are **pull-based**. The client sends a `FetchRequest` stating how many events it can handle, and the server answers with one or more full or partial batches until that number is reached. The client then asks for more.[^s2][^s5] This flow control keeps a slow consumer from being flooded during a publishing spike. Events arrive in replay-ID order. CDC subscribers use topic names such as `/data/OpportunityChangeEvent`, or `/data/ChangeEvents` for all change events, and these names are case-sensitive.[^s5]

**Managed event subscriptions** (beta) move replay tracking to the server. An admin or developer defines a `ManagedEventSubscription` through Metadata or Tooling API, with a topic, a default replay position (`LATEST` or `EARLIEST`), an error-recovery replay position and a `RUN`/`STOP` state. The client calls `ManagedSubscribe` and periodically commits the last processed replay ID. After a disconnect, the subscription resumes after that committed ID, as long as it is still inside the event bus retention window.[^s4]

## Limits and gotchas

Limits verified this run against the Pub/Sub API Developer Guide:[^s3]

- A subscribe call can request at most **100 events** in total across its fetch requests. Larger requests are treated as 100.[^s3]
- A single event can be at most **1 MB**. gRPC caps a publish request at **4 MB**, and the server fails the call and closes the stream above that. Salesforce recommends keeping batches at or below 3 MB and about 200 events per request.[^s3]
- One gRPC channel supports up to **1,000 concurrent streams** on its HTTP/2 connection. Extra RPCs queue on the client, and heavy sharing of one channel can reduce throughput.[^s3]
- An org can create at most **200** unique managed subscriptions. These count against the same delivery allocations as ordinary `Subscribe` calls.[^s3]

Publishing and delivery also consume the separate platform event, CDC and event monitoring allocations.[^s3] With managed subscriptions, stopping one through the API deletes its stored replay ID, so it restarts from the default replay position. A subscription also can't be shared between clients. Configuration changes can take a few minutes to take effect.[^s4] For CDC, decoded fields may need post-processing; `CreatedDate`, for example, arrives in epoch time. Schema IDs also change when the event schema changes, so clients should cache schemas by ID rather than by topic.[^s5]

## When to use it (and when not)

Choose Pub/Sub API for new external subscribers or high-volume publishers that need efficient binary transport, explicit flow control and final publish acknowledgments. Salesforce positions it as the replacement for Streaming API subscriptions and for publishing events through SOAP, REST or Bulk.[^s1][^s6] It assumes a client that can speak gRPC over HTTP/2.[^s1] It also doesn't help with in-org processing, where Apex triggers or flows on platform or change events are simpler. For bulk record loads rather than event streams, Bulk API 2.0 remains the right tool.[^s1]

## Connections

Pub/Sub API is a transport within Salesforce's **event-driven architecture** (broader). It carries the messages defined by **platform events** and generated by **change data capture**, so it integrates with both. It is the modern **alternative to the Streaming API**, whose CometD client it replaces for subscriptions.[^s6] Its throughput is governed by **platform event allocations** and by its own limits.[^s3] Server-side replay is **configured via managed event subscriptions**.[^s4] **Bulk API 2.0** is related as the batch-oriented counterpart for moving record data instead of events.

## Sources

[^s1]: Salesforce Developers, "Get Started with Pub/Sub API". https://developer.salesforce.com/docs/platform/pub-sub-api/guide/intro.html (accessed 2026-11-02)
[^s2]: Trailhead, "Pub/Sub API Basics: Get to Know Pub/Sub API". https://trailhead.salesforce.com/content/learn/modules/pub-sub-api-basics/get-to-know-pubsub-api (accessed 2026-11-02)
[^s3]: Salesforce Developers, "Pub/Sub API and Event Allocations". https://developer.salesforce.com/docs/platform/pub-sub-api/guide/allocations.html (accessed 2026-11-02)
[^s4]: Salesforce Developers, "Managed Event Subscriptions (Beta)". https://developer.salesforce.com/docs/platform/pub-sub-api/guide/managed-sub.html (accessed 2026-11-02)
[^s5]: Salesforce Developers, "Subscribe with Pub/Sub API". https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_subscribe_pubsub_api.htm (accessed 2026-11-02)
[^s6]: Salesforce Developers Blog, "Pub/Sub API: Building Event-Driven Integrations Just Got Even Easier". https://developer.salesforce.com/blogs/2021/07/pub-sub-api-building-event-driven-integrations-just-got-even-easier (accessed 2026-11-02)
