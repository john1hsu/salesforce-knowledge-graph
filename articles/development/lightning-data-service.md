---
id: kt:lightning-data-service
type: Feature
title: Lightning Data Service
aliases: [LDS, force:recordData, lightning/ui*Api data layer]
domain: development
summary: >-
  The client-side data layer for Lightning components that loads, caches and shares Salesforce record data and
  metadata through User Interface API, enforcing CRUD, field-level security and sharing without Apex.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:lightning-web-components, kt:aura-components, kt:salesforce-sharing-model, kt:api-request-limits]
relations:
  - {predicate: dependsOn, object: kt:user-interface-api}
  - {predicate: queriedWith, object: kt:graphql-api}
  - {predicate: alternativeTo, object: kt:apex}
  - {predicate: coveredBy, object: kt:platform-developer-certification}
sources:
  - id: s1
    title: "Lightning Web Components Developer Guide: Lightning Data Service"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/data-ui-api.html
    type: official-docs
    accessed: 2026-11-05
  - id: s2
    title: "Lightning Web Components Developer Guide: Data Guidelines"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/data-guidelines.html
    type: official-docs
    accessed: 2026-11-05
  - id: s3
    title: "Lightning Web Components Developer Guide: Client-Side Caching of Apex Method Results"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/apex-result-caching.html
    type: official-docs
    accessed: 2026-11-05
  - id: s4
    title: "Lightning Web Components for Aura Developers: Work with Salesforce Data"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lightning-web-components-for-aura-developers/work-with-salesforce-data
    type: official-learning
    accessed: 2026-11-05
  - id: s5
    title: "GraphQL API Developer Guide: GraphQL Wire Adapter for LWC"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/graphql/guide/graphql-wire-lwc.html
    type: official-docs
    accessed: 2026-11-05
created: 2026-11-05
---

# Lightning Data Service

Lightning Data Service (LDS) is the data layer that Lightning web components use to read and write Salesforce records. Records it loads are cached on the client and shared, so every component on a page that shows the same record shows the same version of it, and the record is loaded only once no matter how many components ask for it.[^s1] Developers reach LDS through three surfaces: the record form base components (`lightning-record-form`, `lightning-record-edit-form`, `lightning-record-view-form`), the wire adapters and functions in the `lightning/ui*Api` modules, and the GraphQL wire adapter.[^s1] In Aura, the equivalent entry points are `lightning:recordForm` and the `<force:recordData>` tag for custom markup.[^s4]

## How it works

LDS sits on top of User Interface API, the same public API that Lightning Experience and the Salesforce mobile apps use. UI API returns data and metadata together in one response and reflects admin layout changes, so a field removed from a layout drops out of layout-based responses.[^s1] Because every response respects CRUD permissions, field-level security and sharing, a component built on LDS shows a user only the records and fields that user can access, with no extra security code.[^s1]

Record data obtained through a wire adapter is cached client-side and re-requested after an unspecified lifetime that Salesforce says may change; object and layout metadata live in a separate durable store with its own timeout, which relies on secure browser caching (on by default).[^s1] LDS also loads record data progressively, invalidates cache entries when dependent data or metadata changes, and bulkifies and de-duplicates server calls.[^s1] When a component mutates a record through LDS, or a cache entry expires and a wire re-reads it, every component with a relevant `@wire` receives the new value.[^s1]

Reads are reactive: a `@wire` with an adapter such as `getRecord` re-provisions data when a `$`-prefixed parameter changes, and the adapter, not the component, decides when data arrives. Writes use the imperative `createRecord`, `updateRecord` and `deleteRecord` functions, which return Promises; Trailhead warns against using `@wire` for mutations.[^s4] The GraphQL wire adapter is also LDS-managed, so it inherits the shared cache and permission checks while letting one query span several objects, filter, sort, paginate and mutate.[^s2][^s5]

## Limits and gotchas

- **Supported objects.** All custom objects and the standard objects that UI API supports; custom metadata types are not supported.[^s1] Objects outside UI API, such as Task and Event, need Apex.[^s2]
- **No API consumption, but platform limits still apply.** LDS calls don't count against API usage, though general limits such as the number of records returned still do.[^s2]
- **Not transactional.** Each adapter or function call is its own transaction, so multi-record operations aren't atomic; use Apex when a failure must roll everything back.[^s2]
- **Over-fetching.** `getRecord` returns child relationships and layout types beyond the requested fields, so pick the adapter that returns the least data.[^s2]
- **Stale layouts.** Metadata changes may not appear until the durable cache times out and the page reloads; logging out and back in shows them immediately.[^s1]
- **Separate caches for Apex.** Apex results, even `cacheable=true` ones, aren't managed by LDS. Refresh wired Apex with `refreshApex()`, and after imperative Apex that changes records call `notifyRecordUpdateAvailable(recordIds)` so LDS refetches them. Using `refreshApex` to refresh non-Apex adapters is deprecated.[^s2][^s3] Mixing Apex fetches with GraphQL searches can yield null values for records Apex returned, so stay with one approach.[^s2]

## When to use it (and when not)

Salesforce recommends an order: start with the LDS record form components, move to `lightning/ui*Api` adapters and functions when you need a custom UI or business logic, use the GraphQL adapter when one request must cover several queries or related objects, and fall back to Apex only when none of those fit, for example criteria-based record loads, unsupported objects or all-or-nothing transactions.[^s2] Data still flows one way, from parent to child, and objects passed into a component are read-only, so copy them before changing them.[^s2]

## Connections

LDS is the data foundation of **Lightning Web Components** and also backs the Aura record forms and `force:recordData` in **Aura components**.[^s4] It depends on **User Interface API** for data, metadata and security enforcement, which is why it inherits the **sharing model** automatically.[^s1] The GraphQL wire adapter extends it with **GraphQL API** queries.[^s5] **Apex** is the alternative when LDS can't express an operation, at the cost of managing cache refresh yourself.[^s2][^s3] Because LDS calls aren't counted as API usage, it doesn't draw down the org's **API request limits**.[^s2] It is linked to the **Platform Developer certification**, since deciding between record forms, wire adapters and Apex is everyday developer work.[^s4]

## Sources

[^s1]: Salesforce Developers, "Lightning Web Components Developer Guide: Lightning Data Service". https://developer.salesforce.com/docs/platform/lwc/guide/data-ui-api.html (accessed 2026-11-05)
[^s2]: Salesforce Developers, "Lightning Web Components Developer Guide: Data Guidelines". https://developer.salesforce.com/docs/platform/lwc/guide/data-guidelines.html (accessed 2026-11-05)
[^s3]: Salesforce Developers, "Lightning Web Components Developer Guide: Client-Side Caching of Apex Method Results". https://developer.salesforce.com/docs/platform/lwc/guide/apex-result-caching.html (accessed 2026-11-05)
[^s4]: Trailhead, "Lightning Web Components for Aura Developers: Work with Salesforce Data". https://trailhead.salesforce.com/content/learn/modules/lightning-web-components-for-aura-developers/work-with-salesforce-data (accessed 2026-11-05)
[^s5]: Salesforce Developers, "GraphQL API Developer Guide: GraphQL Wire Adapter for LWC". https://developer.salesforce.com/docs/platform/graphql/guide/graphql-wire-lwc.html (accessed 2026-11-05)
