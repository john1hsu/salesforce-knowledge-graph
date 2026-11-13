---
id: kt:aura-components
type: Feature
title: Aura Components
aliases: [Lightning Aura Components, Aura component framework, Lightning Component framework, Aura]
domain: development
summary: >-
  Salesforce's original Lightning UI programming model, in which reusable components are built from .cmp markup bundles,
  JavaScript client-side controllers and Apex server-side controllers that communicate through framework events.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:lightning-web-components, kt:lightning-data-service, kt:lightning-message-service, kt:lightning-locker]
relations:
  - {predicate: alternativeTo, object: kt:lightning-web-components}
  - {predicate: integratesWith, object: kt:apex}
sources:
  - id: s1
    title: "Lightning Aura Components Developer Guide: Components"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/light/components_overview.htm
    type: official-docs
    accessed: 2026-11-06
  - id: s2
    title: "Aura Components Developer Guide: Communicating with Events"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/aura-platform/guide/events-intro.html
    type: official-docs
    accessed: 2026-11-06
  - id: s3
    title: "Lightning Aura Components Developer Guide: Calling a Server-Side Action"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/controllers_server_intro.htm
    type: official-docs
    accessed: 2026-11-06
  - id: s4
    title: "Lightning Web Components Developer Guide: How to Choose Lightning Web Components or Aura"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/get-started-lwc-or-aura.html
    type: official-docs
    accessed: 2026-11-06
  - id: s5
    title: "Lightning Web Components Developer Guide: Supported Salesforce Targets and Tools"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/get-started-supported-experiences.html
    type: official-docs
    accessed: 2026-11-06
  - id: s6
    title: "Lightning Web Components for Aura Developers: Understand How Lightning Web Components Work with Aura Components"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/fr/content/learn/modules/lightning-web-components-for-aura-developers/understand-how-lightning-web-components-work-with-aura-components
    type: official-learning
    accessed: 2026-11-06
created: 2026-11-06
---

# Aura Components

Aura components are the building blocks of Salesforce's first Lightning Component framework. Each component wraps a modular, potentially reusable slice of user interface, anywhere from a single line of text to an entire application.[^s1] Although Lightning Web Components (LWC) is now the default model for new UI work, Aura remains a supported, current technology: much of Lightning Experience and many existing org customizations still run on it, and some surfaces still require it.[^s4][^s5]

## How it works

A component's markup lives in a file with a `.cmp` suffix and can reference other components. The markup, its JavaScript and its related resources are grouped into a **component bundle**.[^s1] Components declare typed **attributes**, which behave much like member variables on an Apex class, and **expressions** in markup read those attributes or pass values down to child components.[^s1] Larger components are composed from smaller ones through the `body` attribute and through *facets*, which are attributes typed as arrays of components. The framework also brings inheritance and encapsulation to the presentation layer, and an `access` system attribute decides whether a resource can be used outside its namespace.[^s1]

Behaviour is event-driven. Events are declared with `aura:event` in a `.evt` resource, fired from JavaScript controller actions, and can carry attributes that the handler reads.[^s2] There are two kinds:

- **Component events** are fired by a component instance and handled by that component or by a component above it in the containment hierarchy.[^s2]
- **Application events** follow publish-subscribe: every component that registers a handler is notified, which suits parts of the app with no containment relationship.[^s2]

Salesforce's guidance is to prefer component events and keep application events for app-wide concerns such as navigating to a record.[^s2]

Server work goes through Apex. A client-side controller action can call a server-side action on an Apex controller whose methods are exposed with `@AuraEnabled`. The client registers a callback that runs when the round trip completes, and the server can return any JSON-serializable data.[^s3] The framework queues server actions and sends them to the server in batches to cut network traffic. Actions can be marked *storable*, so cached data renders immediately while fresh data is fetched if the cache is stale. They can also be marked *abortable*, so a queued action is dropped if its component has been unrendered.[^s3]

## Limits and gotchas

- **Security is enforced in Apex, not the component.** A user can only invoke an `@AuraEnabled` method if their profile or a permission set grants access to the Apex class. The developer guide says that from API version 67.0, Apex runs in user mode by default, enforcing the user's permissions and field-level security unless an operation is explicitly set to system mode. Sharing is enforced by default unless the class is declared `without sharing`.[^s3]
- **Apex data is not cached for you.** Unlike Lightning Data Service, data returned from Apex isn't managed by the framework, so the component must handle refreshing it.[^s3]
- **Cached pages and stale handlers.** Event handlers that stay active on cached pages can misbehave. For cross-DOM communication within a Lightning page, the guide points to Lightning message service, whose default scope publishes only to active components.[^s2]
- **Edition availability.** Creating Aura components isn't supported in Starter and Pro Suite editions.[^s1]

## When to use it (and when not)

Salesforce's own decision guide says to choose LWC unless you need something LWC doesn't support, noting that LWC performs better and is simpler to build.[^s4] Aura is still the right tool in two cases. The first is an experience, feature or interface that LWC doesn't support: build the logic in LWC and wrap it in a thin Aura component. The second is a base component with no LWC equivalent, which may mean building most of the component in Aura.[^s4] The supported-targets page lists Chatter extensions, global actions, list view actions, related list view actions and standard action overrides as tools that don't take an LWC directly and need an Aura wrapper.[^s5]

The two models coexist. An Aura component can contain Lightning web components, but an LWC cannot contain Aura components. Both can talk through events, and both can share code through ES6 modules.[^s6] Migration is optional and incremental. Trailhead recommends treating it as a redesign rather than a line-by-line port, starting with simple UI-only or performance-critical components, and migrating whole component trees for the biggest gains.[^s6]

## Connections

Aura is an `alternativeTo` `kt:lightning-web-components`: the newer, standards-based model that Salesforce now recommends for new work, while Aura covers the gaps and hosts LWCs as a wrapper.[^s4][^s6] It `integratesWith` `kt:apex` through `@AuraEnabled` server-side controllers, which is where its data security is enforced.[^s3] It is related to `kt:lightning-data-service`, the managed data layer that Apex calls don't get, and to `kt:lightning-message-service`, the recommended channel for cross-DOM messaging on Lightning pages.[^s2][^s3] Its broader context is the `kt:salesforce-platform` UI layer.[^s1]

## Sources

[^s1]: Salesforce Developers, "Lightning Aura Components Developer Guide: Components". https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/light/components_overview.htm (accessed 2026-11-06)
[^s2]: Salesforce Developers, "Aura Components Developer Guide: Communicating with Events". https://developer.salesforce.com/docs/platform/aura-platform/guide/events-intro.html (accessed 2026-11-06)
[^s3]: Salesforce Developers, "Lightning Aura Components Developer Guide: Calling a Server-Side Action". https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/controllers_server_intro.htm (accessed 2026-11-06)
[^s4]: Salesforce Developers, "How to Choose Lightning Web Components or Aura". https://developer.salesforce.com/docs/platform/lwc/guide/get-started-lwc-or-aura.html (accessed 2026-11-06)
[^s5]: Salesforce Developers, "Supported Salesforce Targets and Tools". https://developer.salesforce.com/docs/platform/lwc/guide/get-started-supported-experiences.html (accessed 2026-11-06)
[^s6]: Trailhead, "Understand How Lightning Web Components Work with Aura Components". https://trailhead.salesforce.com/fr/content/learn/modules/lightning-web-components-for-aura-developers/understand-how-lightning-web-components-work-with-aura-components (accessed 2026-11-06)
