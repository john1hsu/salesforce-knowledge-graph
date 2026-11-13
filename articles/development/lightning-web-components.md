---
id: kt:lightning-web-components
type: Feature
title: Lightning Web Components
aliases: [LWC, Lightning web component, LWC framework, LWC programming model]
domain: development
summary: >-
  Salesforce's standards-based UI programming model for building Lightning components from custom elements,
  Shadow DOM, templates and modern JavaScript, with a thin layer of Salesforce services for data and security.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:apex, kt:screen-flow, kt:experience-cloud, kt:lightning-data-service, kt:lightning-message-service, kt:wire-service]
relations:
  - {predicate: alternativeTo, object: kt:aura-components}
  - {predicate: dependsOn, object: kt:lightning-web-security}
  - {predicate: integratesWith, object: kt:apex}
  - {predicate: dependsOn, object: kt:lightning-data-service}
sources:
  - id: s1
    title: "Introducing Lightning Web Components"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2018/12/introducing-lightning-web-components
    type: official-blog
    accessed: 2026-11-03
  - id: s2
    title: "Lightning Web Components Developer Guide: Lightning Web Components: Open Source"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/get-started-oss
    type: official-docs
    accessed: 2026-11-03
  - id: s3
    title: "Lightning Web Components Developer Guide: Lightning Web Security"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/component-library/documentation/en/lwc/security_lwsec_intro?
    type: official-docs
    accessed: 2026-11-03
  - id: s4
    title: "Lightning Aura Components Developer Guide (264.0): Lightning Locker"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.lightning.meta/lightning/security_code.htm
    type: official-docs
    accessed: 2026-11-03
  - id: s5
    title: "Lightning Web Components for Aura Developers: Work with Salesforce Data"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/es-MX/content/learn/modules/lightning-web-components-for-aura-developers/work-with-salesforce-data
    type: official-learning
    accessed: 2026-11-03
  - id: s6
    title: "Lightning Web Components Developer Guide: Call Apex Methods Imperatively"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/component-library/documentation/en/lwc/lwc.apex_call_imperative
    type: official-docs
    accessed: 2026-11-03
created: 2026-11-03
---

# Lightning Web Components

Lightning Web Components (LWC) is the programming model Salesforce recommends for building user-interface components on the Lightning Platform. Salesforce announced it in December 2018 as a lightweight framework built on web standards, adding only a thin layer of platform services on top.[^s1] Components are written as HTML templates plus modern JavaScript classes, and the same engine is also published as open source for use outside Salesforce.[^s1][^s2]

## Why it exists

When Salesforce launched the Lightning Component framework and the Aura programming model in 2014, browsers offered little beyond a rendering engine, basic elements and ECMAScript 5, so Aura had to supply its own component and module model.[^s1] Over the following years the standards bodies delivered custom elements, templates with slots, Shadow DOM, ES modules, classes and promises. LWC was rebuilt on those native features, so developers learn transferable web skills, components interoperate more easily, and browsers execute more of the work natively for better performance.[^s1] Salesforce-specific behaviour is expressed through decorators such as `@api` (public properties) and `@track`, plus `@wire` for reactive data.[^s1][^s5]

## How it works

The LWC engine is open source, and the same engine runs on and off the platform; what differs is how Salesforce configures the compiler and runtime.[^s2] Open-source LWC is usually released weekly, while the platform ships three times a year, so the on-platform version typically trails open source by three to six months.[^s2] On the platform, `@salesforce/*` imports are validated against org metadata at compile time, and dynamic `import()` and access to Aura globals such as `$A` are prohibited.[^s2] At run time, platform components use the `@lwc/synthetic-shadow` polyfill rather than native Shadow DOM, which means page-level styles loaded with `loadStyle` can leak into components.[^s2]

Data access follows a preference order. For standard record view, edit and create screens, the base components `lightning-record-form`, `lightning-record-view-form` and `lightning-record-edit-form` need no Apex at all.[^s5] Beneath them sits Lightning Data Service (LDS), built on the User Interface API, which caches records and shares updates across components on the page.[^s5] Custom reads use `@wire` adapters from the `lightning/ui*Api` modules (for example `getRecord`); writes use the promise-based `createRecord`, `updateRecord` and `deleteRecord` functions, not `@wire`. Developers cannot write their own wire adapters.[^s5]

When logic or queries go beyond what LDS covers, a component calls Apex. Non-mutating methods annotated `@AuraEnabled(cacheable=true)` can be wired; methods that change data, that aren't cacheable, or that touch objects UI API doesn't support (such as Task and Event) must be called imperatively, returning a promise.[^s5][^s6]

## Limits and gotchas

- **Cache staleness.** Cached Apex results flow through the LDS cache, which doesn't manage Apex-provided data, so after changes a component should call `notifyRecordUpdateAvailable(recordIds)`; the older `getRecordNotifyChange` is deprecated.[^s6]
- **Parameter shape.** Apex arguments are passed as an object whose property names match the Apex parameter names, and JavaScript `Map` values are not serialized, so use plain objects or arrays.[^s6]
- **Security sandboxing.** Components run under Lightning Locker or Lightning Web Security (LWS). Under these, some DOM access is restricted; for instance a child's `shadowRoot` returns `null`.[^s2] LWS isolates each namespace in its own JavaScript environment, is the default for orgs created in Winter '23 or later, and has been generally available for LWC and Aura in all orgs since Summer '23.[^s3][^s4] Older orgs still default to Locker unless LWS is enabled, and Salesforce recommends switching after sandbox testing.[^s4]
- **External calls.** Calling third-party endpoints requires registering them as CSP Trusted Sites, and third-party libraries must be uploaded as static resources.[^s5]

## When to use it (and when not)

Salesforce recommends LWC for all new component work and suggests migrating Aura components over time, starting with those that would gain the most performance.[^s1] Aura and LWC coexist: both can sit on the same page, Aura components can include Lightning web components, and both share the base Lightning components and services such as LDS.[^s1] Before writing a component at all, check whether a base record form or declarative tooling covers the need, because those require no Apex or JavaScript to maintain.[^s5] To use LWC outside Salesforce with Salesforce data, the documented route is Lightning Out 2.0; components that need no Salesforce features can run on open-source LWC on any host.[^s2]

## Connections

LWC is the UI layer of `kt:salesforce-platform`, and is the modern `alternativeTo` `kt:aura-components`, which it can interoperate with on the same page.[^s1] It `dependsOn` `kt:lightning-data-service` for cached record access, and `integratesWith` `kt:apex` through `@AuraEnabled` methods called by wire or imperatively.[^s5][^s6] Its runtime `dependsOn` `kt:lightning-web-security` (or the older Lightning Locker).[^s3][^s4] In the wider graph, `kt:screen-flow` and `kt:experience-cloud` both point here as consumers of custom components, and the Aura-to-LWC data guidance links LWC back to the platform's shared UI services.[^s1][^s5]

## Sources

[^s1]: Salesforce Developers Blog, "Introducing Lightning Web Components". https://developer.salesforce.com/blogs/2018/12/introducing-lightning-web-components (accessed 2026-11-03)
[^s2]: Salesforce Developers, "Lightning Web Components: Open Source". https://developer.salesforce.com/docs/platform/lwc/guide/get-started-oss (accessed 2026-11-03)
[^s3]: Salesforce Developers, "Lightning Web Security". https://developer.salesforce.com/docs/component-library/documentation/en/lwc/security_lwsec_intro? (accessed 2026-11-03)
[^s4]: Salesforce Developers, "Lightning Locker" (Aura Components Developer Guide 264.0). https://developer.salesforce.com/docs/atlas.en-us.264.0.lightning.meta/lightning/security_code.htm (accessed 2026-11-03)
[^s5]: Trailhead, "Lightning Web Components for Aura Developers: Work with Salesforce Data". https://trailhead.salesforce.com/es-MX/content/learn/modules/lightning-web-components-for-aura-developers/work-with-salesforce-data (accessed 2026-11-03)
[^s6]: Salesforce Developers, "Call Apex Methods Imperatively". https://developer.salesforce.com/docs/component-library/documentation/en/lwc/lwc.apex_call_imperative (accessed 2026-11-03)
