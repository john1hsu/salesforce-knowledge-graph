---
id: kt:wire-service
type: Feature
title: Wire Service
aliases: [LWC wire service, "@wire decorator", wire adapters]
domain: development
summary: >-
  The reactive read mechanism of Lightning Web Components: the @wire decorator binds a property or function to a
  wire adapter or cacheable Apex method and receives an immutable stream of data that the framework provisions.
release: "Winter '27"
status: current
broader: [kt:lightning-web-components]
related: [kt:lightning-data-service, kt:user-interface-api, kt:graphql-api, kt:apex]
relations:
  - {predicate: dependsOn, object: kt:lightning-data-service}
  - {predicate: partOf, object: kt:lightning-web-components}
  - {predicate: integratesWith, object: kt:apex}
  - {predicate: queriedWith, object: kt:graphql-api}
sources:
  - id: s1
    title: "Lightning Web Components Developer Guide: Understand the Wire Service"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/data-wire-service-about.html
    type: official-docs
    accessed: 2026-11-12
  - id: s2
    title: "Lightning Web Components Developer Guide: Wire Apex Methods to Lightning Web Components"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/apex-wire-method.html
    type: official-docs
    accessed: 2026-11-12
  - id: s3
    title: "Lightning Web Components Developer Guide: Client-Side Caching of Apex Method Results"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/apex-result-caching.html
    type: official-docs
    accessed: 2026-11-12
  - id: s4
    title: "Lightning Web Components Basics: Add Styles and Data to a Lightning Web Component"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lightning-web-components-basics/add-styles-and-data-to-a-lightning-web-component
    type: official-learning
    accessed: 2026-11-12
  - id: s5
    title: "Lightning Web Components Developer Guide: Decorators"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/reference-decorators.html
    type: official-docs
    accessed: 2026-11-12
created: 2026-11-12
---

# Wire Service

The wire service is how a Lightning web component reads Salesforce data declaratively. A component decorates a property or function with `@wire`, naming either a wire adapter or an Apex method, and the component re-renders whenever the service delivers new data.[^s5] Salesforce describes what the component receives as an immutable stream: each value is a newer version of the previous one.[^s1] Trailhead introduces it as a reactive service built on Lightning Data Service, through which the platform feeds a continuous stream of data to the app.[^s4]

The design splits reads from writes. Reads are handed to the LWC engine via `@wire`, while creating, updating and deleting records use imperative JavaScript functions, so the developer stays in control of every mutation.[^s1]

## How it works

A component imports an adapter by name from a module in the `lightning/ui*Api` family (for example `getRecord` from `lightning/uiRecordApi`) and applies `@wire(adapter, config)`. Config values can be plain strings or field and object references imported from `@salesforce/schema`; importing references is recommended because Salesforce then validates them, blocks deletion of referenced fields and cascades renames.[^s1] Trailhead's starter example wires `getRecord` with `recordId: '$userId'` and reads the name with `getFieldValue`.[^s4]

Prefixing a top-level config value with `$` turns it into a reactive reference to a component property, such as `$recordId`. When that property changes, the service provisions fresh data and the template re-renders. Private fields, getter/setter properties and `@api` properties can all be reactive, but a `$` string inside an array is just a literal.[^s1]

The decorated target determines how results arrive:

- **Wired property**: the value is an object with `data` and `error`; use it when the template consumes the data as-is.[^s1]
- **Wired function**: it receives `{ data, error }` and suits logic that must run on each new value, which can happen before or after the component connects or renders.[^s1]

Until something arrives, the value is `{ data: undefined, error: undefined }`, so it is safe to read in any lifecycle hook. On success `data` is set and `error` is undefined; on failure the reverse. The GraphQL adapter reports `errors` (plural) instead.[^s1] One wire's output can feed another's input (for example `$record.data.fieldName`), which is also the documented way to run wires in sequence.[^s1][^s2]

## Wiring Apex

A component can wire a custom Apex method when built-in adapters are not enough. The method must be `static`, `public` or `global`, and annotated `@AuraEnabled(cacheable=true)`; parameters are passed as an object whose keys match the Apex parameter names, even when there is only one.[^s2] Cacheable methods may only read data, never mutate it, so writes go through imperative calls instead.[^s3] A `null` parameter still invokes the method, but an `undefined` one does not, and Salesforce warns against overloading `@AuraEnabled` methods because the overload that runs is effectively random.[^s2]

## Caching and refresh

When the requested data is already in the Lightning Data Service cache, no network request is made; otherwise wire evaluation triggers one.[^s1] Because LDS does not manage Apex results, stale wired Apex data is refreshed by passing the previously emitted wire value to `refreshApex()`, which returns a promise; GraphQL wires use `refreshGraphQL()`.[^s1][^s3] After imperative Apex changes records, call `notifyRecordUpdateAvailable()` with the record IDs so LDS refetches them.[^s3] Salesforce advises refreshing once after a mutation rather than polling with timers.[^s1]

## Limits and gotchas

- **Incomplete config**: an adapter runs only when every dynamic parameter has a value; an undefined one means nothing is provisioned.[^s1]
- **No timing guarantees**: the framework decides when, how often and from where data is fetched, and response order isn't guaranteed.[^s1]
- **Background changes**: asynchronous changes made by an Apex trigger or autolaunched flow do not re-evaluate the wire.[^s1]
- **Read-only data**: provisioned objects are immutable; shallow-copy before editing, and never change config properties in `renderedCallback()`, which risks an infinite loop.[^s1]
- **Unsupported shapes**: maps aren't supported for wired or imperative Apex calls, and Decimals with more than 15 digits of precision are returned as JSON strings.[^s2]
- **Security**: adapters respect object CRUD, field-level security and sharing, so inaccessible fields are simply absent from the response.[^s1]

## When to use it (and when not)

Use `@wire` for reactive, read-only data that should stay in step with component state and the shared LDS cache. Use imperative calls for writes, for non-cacheable Apex, or when the call must happen at a precise moment, such as a button click, because wire timing is controlled by the service, not the component.[^s1][^s3]

## Connections

The wire service is `partOf` `kt:lightning-web-components`, exposed through the `@wire` decorator alongside `@api` and `@track`.[^s5] It `dependsOn` `kt:lightning-data-service`, whose cache it reads first, and its built-in adapters come from the `lightning/ui*Api` modules backed by `kt:user-interface-api`.[^s1][^s4] It `integratesWith` `kt:apex` through cacheable `@AuraEnabled` methods, and it is `queriedWith` `kt:graphql-api` via the GraphQL adapter and its own refresh function.[^s1][^s2]

## Sources
[^s1]: Salesforce Developers, "Lightning Web Components Developer Guide: Understand the Wire Service". https://developer.salesforce.com/docs/platform/lwc/guide/data-wire-service-about.html (accessed 2026-11-12)
[^s2]: Salesforce Developers, "Wire Apex Methods to Lightning Web Components". https://developer.salesforce.com/docs/platform/lwc/guide/apex-wire-method.html (accessed 2026-11-12)
[^s3]: Salesforce Developers, "Client-Side Caching of Apex Method Results". https://developer.salesforce.com/docs/platform/lwc/guide/apex-result-caching.html (accessed 2026-11-12)
[^s4]: Trailhead, "Add Styles and Data to a Lightning Web Component". https://trailhead.salesforce.com/content/learn/modules/lightning-web-components-basics/add-styles-and-data-to-a-lightning-web-component (accessed 2026-11-12)
[^s5]: Salesforce Developers, "Lightning Web Components Developer Guide: Decorators". https://developer.salesforce.com/docs/platform/lwc/guide/reference-decorators.html (accessed 2026-11-12)
