---
id: kt:platform-events
type: Feature
title: Platform Events
aliases: [platform event, high-volume platform events, __e object, custom platform event]
domain: integration
summary: >-
  Salesforce's publish/subscribe messaging feature: custom event definitions with an __e suffix whose messages are
  published to the event bus from Apex, Flow or APIs and consumed in near real time by triggers, flows and external
  clients.
release: "Winter '27"
status: current
broader: [kt:event-driven-architecture]
related: [kt:change-data-capture, kt:apex-triggers, kt:flow-builder, kt:platform-event-triggered-flow]
relations:
  - {predicate: queriedWith, object: kt:pub-sub-api}
  - {predicate: governedBy, object: kt:platform-event-allocations}
  - {predicate: alternativeTo, object: kt:outbound-messaging}
sources:
  - id: s1
    title: "Platform Events Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/platform-events/guide/platform-events-intro.html
    type: official-docs
    accessed: 2026-10-31
  - id: s2
    title: "Platform Events Basics: Define and Publish Platform Events"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/fr/content/learn/modules/platform_events_basics/platform_events_define_publish
    type: official-learning
    accessed: 2026-10-31
  - id: s3
    title: "Common Platform Event Allocations"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/platform-events/guide/platform-events-limits-common.html
    type: official-docs
    accessed: 2026-10-31
  - id: s4
    title: "Configure the User and Batch Size for Your Platform Event Trigger with PlatformEventSubscriberConfig"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_trigger_config.htm
    type: official-docs
    accessed: 2026-10-31
  - id: s5
    title: "Using the Right Tools and Patterns for Event-Driven Architectures"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/decision-guides/event-driven
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

# Platform Events

Platform events are Salesforce's built-in publish/subscribe messages. A publisher sends an event message carrying custom data, and any number of subscribers receive it in near real time, without the publisher knowing who is listening. They connect business processes inside one org and between Salesforce and external applications, and are available in Performance, Unlimited, Enterprise and Developer editions.[^s1] You define an event much like a custom object, in Setup, with custom fields of type Checkbox, Date, Date/Time, Number, Text or Long Text Area. Salesforce appends `__e` to the API name, so an event labelled "Cloud News" becomes `Cloud_News__e`.[^s2]

## How it works

**Publishing.** Inside Salesforce, Apex passes event instances to `EventBus.publish()`, and Flow uses a Create Records element on the event object. External systems publish through the Pub/Sub API or through the SOAP, REST and Bulk data APIs, where publishing looks like inserting an sObject.[^s1][^s2] Publishing is asynchronous: a successful `Database.SaveResult` (or a REST response with status `OPERATION ENQUEUED`) only means the message was queued. Failed Apex publishes return errors in the result rather than throwing exceptions, and a list publish can partially succeed, so code should inspect every result. For final confirmation, Salesforce points to Apex publish callbacks.[^s2][^s6]

**Publish behavior.** Each event definition chooses one of two behaviors. *Publish Immediately*, the default, sends the message when the publish call runs, whether or not the surrounding transaction later succeeds, so a subscriber can see it before the data is committed. *Publish After Commit* sends only if the transaction commits, which suits subscribers that need to read the committed records.[^s2]

**Subscribing.** Subscribers can be Apex triggers on the `__e` object, flows and processes, Pub/Sub API clients and CometD clients.[^s1] Event Apex triggers run as the Automated Process user by default and receive up to 2,000 messages per execution. The PlatformEventSubscriberConfig metadata (deployed with Tooling or Metadata API) can change the running user and set a batch size from 1 to 2,000, though Salesforce warns that very small batches slow processing.[^s4]

**Retention and replay.** New events are high-volume by default, and standard-volume events can no longer be defined. High-volume messages stay on the event bus for 72 hours, compared with 24 hours for legacy standard-volume events defined before Spring '19. Each delivered message carries a `ReplayId`, which subscribers should store and reuse (values are not guaranteed contiguous) to resume from a known position. Stored events cannot be queried with SOQL or SOSL, or used in reports or list views.[^s2]

## Limits and gotchas

Allocations verified against the Winter '27 documentation:[^s3]

- Event definitions per org: 100 in Performance and Unlimited, 50 in Enterprise, 5 in Developer and Professional (with API add-on). Events from installed managed packages share this allocation.
- Concurrent CometD clients: 2,000 (Performance/Unlimited), 1,000 (Enterprise), 20 (Developer/Professional). Apex triggers and flows do not count against it.
- Maximum event message size: 1 MB in every edition.
- In Apex, Publish After Commit calls count against the DML statement limit, while Publish Immediately calls have a separate cap of 150 `EventBus.publish()` calls per transaction.[^s2]

Common traps: a trigger that publishes the same event it subscribes to creates an infinite loop, and Publish Immediately messages are not rolled back when the transaction fails.[^s5] Bulk jobs, data loads and batch Apex can generate enough events to exhaust delivery allocations, so filter before publishing (flow entry criteria or trigger conditions) rather than only filtering on the subscriber side.[^s6] Usage can be monitored by querying the PlatformEventUsageMetric object.[^s1]

## When to use it (and when not)

Salesforce's event-driven decision guide lists platform events and Change Data Capture as the preferred ways to publish changes for other systems. Platform events fit when you need a custom, business-meaningful payload, and CDC fits when subscribers need record create, update, delete and undelete changes in a fixed structure. Outbound messages remain supported but receive no new investment, and PushTopic and generic streaming events are not recommended for new work.[^s5] Do not use events to chain internal automation steps. The guide recommends subflows or Flow Orchestrator for that.[^s5]

## Connections

Platform events are Salesforce's main implementation of `kt:event-driven-architecture`, and they are **related to** `kt:change-data-capture`, the sibling event type that shares the bus, replay window and 1 MB limit but has a predefined payload.[^s5] External clients **access** them through `kt:pub-sub-api`, the gRPC-based API that Salesforce recommends over the older Streaming API.[^s5][^s6] They are **an alternative to** `kt:outbound-messaging` for notifying external endpoints.[^s5] Inside the org they are consumed by `kt:apex-triggers` and published or consumed by `kt:flow-builder` flows.[^s2] Their capacity is **governed by** `kt:platform-event-allocations`, the per-edition limits on definitions, clients, publishing and delivery.[^s3]

## Sources

[^s1]: Salesforce Developers, "Platform Events Developer Guide". https://developer.salesforce.com/docs/platform/platform-events/guide/platform-events-intro.html (accessed 2026-10-31)
[^s2]: Trailhead, "Platform Events Basics: Define and Publish Platform Events". https://trailhead.salesforce.com/fr/content/learn/modules/platform_events_basics/platform_events_define_publish (accessed 2026-10-31)
[^s3]: Salesforce Developers, "Common Platform Event Allocations". https://developer.salesforce.com/docs/platform/platform-events/guide/platform-events-limits-common.html (accessed 2026-10-31)
[^s4]: Salesforce Developers, "Configure the User and Batch Size for Your Platform Event Trigger with PlatformEventSubscriberConfig". https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_trigger_config.htm (accessed 2026-10-31)
[^s5]: Salesforce Architects, "Using the Right Tools and Patterns for Event-Driven Architectures". https://architect.salesforce.com/decision-guides/event-driven (accessed 2026-10-31)
[^s6]: Michael Norton, Salesforce Developers Blog, "Design Considerations for Change Data Capture and Platform Events" (2022). https://developer.salesforce.com/blogs/2022/10/design-considerations-for-change-data-capture-and-platform-events (accessed 2026-10-31)
