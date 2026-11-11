---
id: kt:lightning-message-service
type: Feature
title: Lightning Message Service
aliases: [LMS, lightning/messageService, message channel, LightningMessageChannel]
domain: development
summary: >-
  A client-side publish/subscribe service that lets unrelated Lightning web components, Aura components and
  Visualforce pages on the same Lightning page exchange JSON messages over metadata-defined message channels.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:lightning-web-components, kt:aura-components, kt:lightning-data-service, kt:lightning-app-builder]
relations:
  - {predicate: integratesWith, object: kt:visualforce}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: contrastsWith, object: kt:platform-events}
  - {predicate: integratesWith, object: kt:experience-builder}
sources:
  - id: s1
    title: "LWC Developer Guide: Communicate Across the DOM with Lightning Message Service"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/use-message-channel
    type: official-docs
    accessed: 2026-11-11
  - id: s2
    title: "LWC Developer Guide: Lightning Message Service Limitations"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/use-message-channel-considerations.html
    type: official-docs
    accessed: 2026-11-11
  - id: s3
    title: "LWC Developer Guide: Define the Scope of the Message Service"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/use-message-channel-scope.html
    type: official-docs
    accessed: 2026-11-11
  - id: s4
    title: "Component Reference: lightning/messageService"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-message-service.html
    type: official-docs
    accessed: 2026-11-11
  - id: s5
    title: "Metadata API Developer Guide: LightningMessageChannel"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_lightningmessagechannel.htm
    type: official-docs
    accessed: 2026-11-11
  - id: s6
    title: "Visualforce Developer Guide: Communicating Across the DOM with Lightning Message Service"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-pages-developers-guide/guide/message-channel-intro.html
    type: official-docs
    accessed: 2026-11-11
  - id: s7
    title: "Communicate Between Unrelated Components"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/communicate-between-lightning-web-components/communicate-between-unrelated-components
    type: official-learning
    accessed: 2026-11-11
  - id: s8
    title: "Learn MOAR: Lightning Message Service Generally Available in Summer '20"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2020/06/learn-moar-lightning-message-service-generally-available-in-summer-20
    type: official-blog
    accessed: 2026-11-11
created: 2026-11-11
---

# Lightning Message Service

Lightning Message Service (LMS) is the supported way for components that do not share a DOM tree to talk to each other on a Lightning page. It is a publish/subscribe bus that works across Lightning web components, Aura components and Visualforce pages, including components in the utility bar and pop-out utilities, and Open CTI softphones.[^s1] It was introduced as a developer preview in Winter '20 and became generally available in Summer '20, when message scopes were added.[^s8] Because all three UI technologies can share one channel, LMS is also a migration aid: new LWCs can coordinate with legacy Visualforce or Aura pieces during a move from Classic to Lightning Experience.[^s1]

## How it works

A **message channel** is metadata of type `LightningMessageChannel`, stored as `<Name>.messageChannel-meta.xml` in the `messageChannels` folder and available from API version 47.0.[^s5] Its fields are a required `masterLabel`, a `description`, a list of `lightningMessageFields` describing the payload, and `isExposed`, which controls whether components in other namespaces may use the channel.[^s5] The API name takes a `__c` suffix (for example `Record_Selected__c`), which does not make it a custom object; channels from a managed package are referenced with that package's namespace.[^s1][^s4] The declared fields aid tooling and reference checks, but they are not enforced at runtime, so a publisher can send any serializable object.[^s8]

In LWC, a component imports the channel from `@salesforce/messageChannel/...` and the functions `publish`, `subscribe`, `unsubscribe` and `MessageContext` from `lightning/messageService`.[^s4] It gets a context with `@wire(MessageContext)`, publishes with `publish(context, channel, payload)`, and subscribes with a listener, typically in `connectedCallback`.[^s3][^s7] The wired context cleans up its subscriptions when the component is destroyed; service modules that are not `LightningElement`s instead call `createMessageContext()` and must call `releaseMessageContext()` themselves.[^s4] Visualforce pages reach a channel through the `$MessageChannel` global variable and publish or subscribe with `sforce.one.publish()`, `sforce.one.subscribe()` and `sforce.one.unsubscribe()`.[^s6]

### Scope

By default a subscriber hears messages only from the **active area**: the selected navigation tab or item, console workspace tab or subtab, and utility items, which are always active.[^s3] Passing `{ scope: APPLICATION_SCOPE }` as the fourth argument to `subscribe()` delivers messages anywhere in the app, which matters most in console apps where background tabs would otherwise miss updates.[^s3][^s8] For LWC, scoping only works when the context comes from `@wire(MessageContext)`.[^s2]

## Limits and gotchas

Payloads must be serializable JSON; functions and symbols cannot be sent.[^s4][^s6] LMS is supported in standard and console navigation in Lightning Experience, in the Salesforce mobile app for Aura and LWC (but not Visualforce), and for Lightning components in Aura and LWR Experience Builder sites.[^s2] It does not work in Salesforce Tabs + Visualforce sites or for Visualforce pages in Experience Builder sites.[^s2] Messages stop at iframe boundaries unless you bridge them with `sforce.one.subscribe()`.[^s2]

`isExposed` defaults to false and, once set to true on a channel that is packaged or referenced, cannot be set back.[^s5] Visualforce can only use exposed channels, yet AppExchange security review expects `isExposed` to be false, so a managed package that uses a channel from Visualforce cannot pass review.[^s5] Message channels can ship in both first- and second-generation packages.[^s2]

## When to use it (and when not)

When you own both components and a common parent, plain DOM events are more efficient; LMS fits components dropped into separate Lightning App Builder regions where you control no parent.[^s7] Salesforce recommends LMS over the old `pubsub` module, which is confined to one page, needs manual unregistering, and is not officially supported; keep pubsub only for containers without LMS support.[^s2]

## Connections

LMS sits on the `kt:salesforce-platform` UI layer and is the cross-DOM channel for `kt:lightning-web-components` and `kt:aura-components`, and it `integratesWith` `kt:visualforce` through `$MessageChannel`.[^s1][^s6] Channels are metadata, so they are `configuredVia` the `kt:metadata-api` and deployed like other source.[^s5] It is related to `kt:lightning-data-service`, which shares record data between components while LMS shares arbitrary UI events, and to `kt:lightning-app-builder`, whose independent page regions are the typical use case.[^s4][^s7] It `contrastsWith` `kt:platform-events`: LMS messages stay in the browser on one page, while platform events travel through the server-side event bus.[^s1] It `integratesWith` `kt:experience-builder` sites for Lightning components, with the Visualforce exclusions above.[^s2]

## Sources
[^s1]: Salesforce Developers, "LWC Developer Guide: Communicate Across the DOM with Lightning Message Service". https://developer.salesforce.com/docs/platform/lwc/guide/use-message-channel (accessed 2026-11-11)
[^s2]: Salesforce Developers, "LWC Developer Guide: Lightning Message Service Limitations". https://developer.salesforce.com/docs/platform/lwc/guide/use-message-channel-considerations.html (accessed 2026-11-11)
[^s3]: Salesforce Developers, "LWC Developer Guide: Define the Scope of the Message Service". https://developer.salesforce.com/docs/platform/lwc/guide/use-message-channel-scope.html (accessed 2026-11-11)
[^s4]: Salesforce Developers, "Component Reference: lightning/messageService". https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-message-service.html (accessed 2026-11-11)
[^s5]: Salesforce Developers, "Metadata API Developer Guide: LightningMessageChannel". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_lightningmessagechannel.htm (accessed 2026-11-11)
[^s6]: Salesforce Developers, "Visualforce Developer Guide: Communicating Across the DOM with Lightning Message Service". https://developer.salesforce.com/docs/platform/salesforce-pages-developers-guide/guide/message-channel-intro.html (accessed 2026-11-11)
[^s7]: Trailhead, "Communicate Between Unrelated Components". https://trailhead.salesforce.com/content/learn/projects/communicate-between-lightning-web-components/communicate-between-unrelated-components (accessed 2026-11-11)
[^s8]: Salesforce Developers Blog, "Learn MOAR: Lightning Message Service Generally Available in Summer '20". https://developer.salesforce.com/blogs/2020/06/learn-moar-lightning-message-service-generally-available-in-summer-20 (accessed 2026-11-11)
