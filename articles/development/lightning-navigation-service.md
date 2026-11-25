---
id: kt:lightning-navigation-service
type: Feature
title: Lightning Navigation Service
aliases: [lightning/navigation, NavigationMixin, LWC navigation service, PageReference navigation]
domain: development
summary: >-
  The lightning/navigation module that lets Lightning web components navigate to, and generate URLs for,
  Salesforce pages described by PageReference objects instead of hard-coded URLs, and read the current page
  reference through the CurrentPageReference wire adapter.
release: "Winter '27"
status: current
broader: [kt:lightning-web-components]
related: [kt:lightning-message-service, kt:workspace-api, kt:wire-service, kt:visualforce, kt:salesforce-mobile-app]
relations:
  - {predicate: integratesWith, object: kt:experience-builder}
  - {predicate: integratesWith, object: kt:screen-flow}
  - {predicate: integratesWith, object: kt:quick-actions}
sources:
  - id: s1
    title: "LWC Developer Guide: Basic Navigation"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/use-navigate-basic.html
    type: official-docs
    accessed: 2026-11-25
  - id: s2
    title: "Lightning Component Reference: Navigation (lightning/navigation)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-navigation.html
    type: official-docs
    accessed: 2026-11-25
  - id: s3
    title: "LWC Developer Guide: PageReference Types"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/reference-page-reference-type
    type: official-docs
    accessed: 2026-11-25
  - id: s4
    title: "LWC Developer Guide: Navigate to Different Page Types"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/use-navigate-page-types.html
    type: official-docs
    accessed: 2026-11-25
  - id: s5
    title: "LWC Developer Guide: Navigate From a Modal"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/use-navigate-modal.html
    type: official-docs
    accessed: 2026-11-25
  - id: s6
    title: "Use the Navigation Service and Reuse Visualforce"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/ja/content/learn/modules/lwc-for-visualforce-developers/use-the-navigation-service-and-reuse-visualforce
    type: official-learning
    accessed: 2026-11-25
  - id: s7
    title: "LWR Sites for Experience Cloud: Lightning Navigation"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/exp-cloud-lwr/guide/get-started-comp-navigation.html
    type: official-docs
    accessed: 2026-11-25
created: 2026-11-25
---

# Lightning Navigation Service

The Lightning Navigation Service is the `lightning/navigation` module that Lightning web components use to move between pages and to build links. Instead of concatenating URLs, a component describes its destination as a **PageReference**, a JavaScript object with a required `type`, required `attributes` and optional `state`, and the service resolves it to the right URL for the container it runs in.[^s1] The module is documented for Lightning Experience, Experience Builder sites, the Salesforce mobile app and Mobile Offline.[^s2] It is also the Lightning replacement for Visualforce habits such as `URLFOR` links and Apex methods that return a `PageReference`.[^s6]

## How it works

A component imports `NavigationMixin` from `lightning/navigation` and applies it to its base class, as in `class MyCmp extends NavigationMixin(LightningElement)`.[^s1] The mixin adds two functions. `this[NavigationMixin.Navigate](pageReference, replace)` navigates; the optional `replace` boolean defaults to false and, when true, replaces the current entry in the browser history instead of adding one.[^s1][^s4] `this[NavigationMixin.GenerateUrl](pageReference)` returns a promise that resolves to a URL, which suits an anchor's `href` or a call to `window.open()`.[^s1][^s4] Calling either function before the component is connected to the DOM can produce unexpected results.[^s2]

To read where the user is, a component wires `CurrentPageReference`, imported from the same module. Its `state` key-value pairs are serialized into URL query parameters, which is how components support bookmarkable deep links.[^s2] State values are strings, and non-standard state keys must carry a namespace prefix such as `c__`.[^s1][^s3]

### PageReference types

Each `type` has its own attributes and supported containers.[^s3] The common ones in Lightning Experience and mobile are `standard__recordPage` (a record with `actionName` view, edit or clone), `standard__objectPage` (an object's home, list or new page, with `filterName` and `defaultFieldValues` state), `standard__recordRelationshipPage` (a related list), `standard__navItemPage` (a custom tab), `standard__namedPage` (pages such as home or chatter), `standard__component` (a URL-addressable component) and `standard__webPage` (an external URL).[^s3][^s4] Some types exist only in Lightning Experience, such as `standard__quickAction` and `standard__flow`, which passes flow input variables as `flow__`-prefixed state and does not accept record, Apex-defined or collection variables.[^s3] Experience Builder sites use `comm__` types such as `comm__namedPage` and `comm__loginPage`.[^s3]

## Limits and gotchas

- Salesforce advises against `window.location`, which behaves inconsistently across browsers, containers and iframes and can open security holes.[^s2]
- PageReference is not supported in Lightning Out, and Experience Builder support is limited per type; for example, sites do not support the clone or edit actions on record pages.[^s3]
- LWR sites use `comm__namedPage` instead of `standard__namedPage`, do not support `comm__loginPage`, and require `objectApiName` on record and record-relationship page references.[^s7]
- For standalone LWR apps outside Salesforce containers, the reference points to `lwr/navigation` instead of this module.[^s2]
- A class that extends `LightningModal` cannot use `NavigationMixin`; the modal's content dispatches an event that the opening component handles by navigating.[^s5]
- Component URLs are case-sensitive, and a component reached through `standard__component` must declare a URL-addressable target in its configuration file.[^s1][^s3]

## When to use it (and when not)

Use the service for any in-app navigation or generated link so the same code works across desktop, mobile and sites, and so Experience Cloud pages get crawlable `href` values for SEO.[^s7][^s2] It changes the page; it does not pass messages. For components that need to communicate rather than navigate, the Trailhead migration path points to Lightning Message Service.[^s6]

## Connections

The service is a module of `kt:lightning-web-components` and is read through the `kt:wire-service` via the `CurrentPageReference` adapter.[^s1][^s2] It sits beside `kt:lightning-message-service`, which the Trailhead migration module pairs with navigation for Visualforce-to-Lightning moves, and it supersedes `kt:visualforce` URL-building patterns.[^s6] It runs in the `kt:salesforce-mobile-app` as well as Lightning Experience, and is related to `kt:workspace-api`, the separate API console apps use to manage their tabs.[^s2] It `integratesWith` `kt:experience-builder` sites through `comm__` page types, with `kt:screen-flow` through `standard__flow`, and with `kt:quick-actions` through `standard__quickAction`.[^s3][^s7]

## Sources
[^s1]: Salesforce Developers, "LWC Developer Guide: Basic Navigation". https://developer.salesforce.com/docs/platform/lwc/guide/use-navigate-basic.html (accessed 2026-11-25)
[^s2]: Salesforce Developers, "Lightning Component Reference: Navigation (lightning/navigation)". https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-navigation.html (accessed 2026-11-25)
[^s3]: Salesforce Developers, "LWC Developer Guide: PageReference Types". https://developer.salesforce.com/docs/platform/lwc/guide/reference-page-reference-type (accessed 2026-11-25)
[^s4]: Salesforce Developers, "LWC Developer Guide: Navigate to Different Page Types". https://developer.salesforce.com/docs/platform/lwc/guide/use-navigate-page-types.html (accessed 2026-11-25)
[^s5]: Salesforce Developers, "LWC Developer Guide: Navigate From a Modal". https://developer.salesforce.com/docs/platform/lwc/guide/use-navigate-modal.html (accessed 2026-11-25)
[^s6]: Trailhead, "Use the Navigation Service and Reuse Visualforce". https://trailhead.salesforce.com/ja/content/learn/modules/lwc-for-visualforce-developers/use-the-navigation-service-and-reuse-visualforce (accessed 2026-11-25)
[^s7]: Salesforce Developers, "LWR Sites for Experience Cloud: Lightning Navigation". https://developer.salesforce.com/docs/platform/exp-cloud-lwr/guide/get-started-comp-navigation.html (accessed 2026-11-25)
