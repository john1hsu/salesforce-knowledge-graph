---
id: kt:apex-continuations
type: Feature
title: Apex Continuations
aliases: [Continuation class, asynchronous Apex callouts from the UI, long-running callouts with continuations, System.Continuation]
domain: development
summary: >-
  The Apex Continuation class, which lets a Visualforce, Aura or Lightning Web Component action make up to three
  parallel (or three chained) long-running HTTP callouts that suspend the request and resume in a callback method.
release: "Winter '27"
status: current
broader: [kt:apex-callouts]
related: [kt:lightning-web-components, kt:aura-components, kt:visualforce, kt:apex-testing, kt:integration-patterns-request-reply-fire-and-forget]
relations:
  - {predicate: partOf, object: kt:apex-callouts}
  - {predicate: dependsOn, object: kt:named-credentials}
  - {predicate: configuredVia, object: kt:remote-site-settings}
  - {predicate: alternativeTo, object: kt:queueable-apex}
sources:
  - id: s1
    title: "Apex Developer Guide: Make Long-Running Callouts with Continuations"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_continuation_overview.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s2
    title: "Apex Developer Guide: Asynchronous Callout Limits"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_continuation_limits.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s3
    title: "Apex Reference Guide: Continuation Class"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_class_System_Continuation.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s4
    title: "Lightning Web Components Developer Guide: Make Long-Running Callouts with Continuations"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/apex-continuations.html
    type: official-docs
    accessed: 2026-11-09
  - id: s5
    title: "Lightning Web Components Developer Guide: Work with a Continuation in an Apex Class"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/apex-continuations-apex.html
    type: official-docs
    accessed: 2026-11-09
  - id: s6
    title: "Apex Continuations: Implementation and Testing in Aura & LWC"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2020/05/apex-continuations-implementation-and-testing-in-aura-lwc
    type: official-blog
    accessed: 2026-11-09
created: 2026-11-09
---

# Apex Continuations

A continuation is an asynchronous callout started from a user-facing action: the Apex action builds a `Continuation` object holding one or more `HttpRequest`s, returns it, and the platform suspends the request while the external service works; when the responses arrive, a named callback method runs and returns the result to the page or component.[^s1] The Apex guide documents them for Visualforce controllers (API version 30.0 or later) and are also used from Aura components and Lightning Web Components.[^s1][^s4] They also work with WSDL-generated SOAP stubs, not only raw HTTP requests.[^s1]

## How it works

The action method creates `new Continuation(timeoutInSeconds)`, sets `continuationMethod` to the callback's name, and calls `addHttpRequest`, which returns a label identifying that request; any value placed in the `state` property is handed back to the callback.[^s3] For Aura and LWC, the starting method must be `static` and annotated `@AuraEnabled(continuation=true)` (the Salesforce examples also mark it `cacheable=true`), the callback must live in the same Apex class, and its recommended signature is `(List<String> labels, Object state)`.[^s5][^s6] The component imports the method from the `@salesforce/apexContinuation` module rather than the usual `@salesforce/apex` module.[^s6] Inside the callback, the static `Continuation.getResponse(label)` returns each `HttpResponse`.[^s3]

The response is processed in a new Apex transaction, so ordinary governor limits, including callout limits, start fresh there; continuation-specific limits apply only to the suspended part.[^s1] In Lightning, the framework treats continuations as background actions that are not batched ("boxcar'ed") with other server calls, so they don't hold up the component's other requests.[^s4]

## Limits and gotchas

As documented for Winter '27:[^s2][^s3]

- Up to **3** parallel callouts per continuation, and up to **3** chained callouts (each issued after the previous response).[^s2]
- Maximum timeout of **120 seconds** per continuation; timeouts set on individual `HttpRequest` objects or SOAP stubs are ignored.[^s2][^s3]
- Maximum HTTP response size of **1 MB**; Visualforce controller state is capped at **80 KB**.[^s2]
- Non-200 status codes signal continuation errors: 2000 timeout, 2001 connection failure, 2002 exception, 2003 response not yet arrived, 2004 response over 1 MB.[^s3]

Each endpoint needs a remote site setting unless it is called through a named credential.[^s5] Asynchronous callouts, including those via named credentials, are not supported over Private Connect, and a continuation action can't be invoked outside its UI context, for example from the Developer Console.[^s1] Tests cannot make real callouts: use `Test.setContinuationResponse` to supply mocks. `Test.invokeContinuationMethod` needs a controller instance, so the static Aura/LWC methods require a workaround such as `@TestVisible` fields.[^s6]

## When to use it (and when not)

The original selling point was that continuation callouts did not count toward the org limit on concurrent synchronous requests running longer than five seconds. Since Winter '20 all callouts are excluded from that limit, so the remaining benefit is user experience: non-blocking, parallel callouts and a longer timeout for a user who is waiting on the answer.[^s4][^s6] When the user doesn't need to wait for the result, a fire-and-forget job such as Queueable Apex is the better fit.[^s6] Use chaining only when calls depend on each other or ordering matters; otherwise run them in parallel.[^s1]

## Connections

`kt:apex-continuations` is `partOf` `kt:apex-callouts` and sits under it as the asynchronous, UI-initiated variant.[^s1] It `dependsOn` `kt:named-credentials` or is `configuredVia` `kt:remote-site-settings` to authorize endpoints.[^s5] It is invoked from `kt:visualforce`, `kt:aura-components` and `kt:lightning-web-components`.[^s1][^s4] It is an `alternativeTo` `kt:queueable-apex` when choosing between a user-awaited and a background callout, and is tested with the mocking tools in `kt:apex-testing`.[^s6] It suits the user-awaited, request-and-reply style of integration against slow endpoints (`kt:integration-patterns-request-reply-fire-and-forget`).[^s1]

## Sources
[^s1]: Salesforce Developers, "Apex Developer Guide: Make Long-Running Callouts with Continuations". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_continuation_overview.htm (accessed 2026-11-09)
[^s2]: Salesforce Developers, "Apex Developer Guide: Asynchronous Callout Limits". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_continuation_limits.htm (accessed 2026-11-09)
[^s3]: Salesforce Developers, "Apex Reference Guide: Continuation Class". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_class_System_Continuation.htm (accessed 2026-11-09)
[^s4]: Salesforce Developers, "Lightning Web Components Developer Guide: Make Long-Running Callouts with Continuations". https://developer.salesforce.com/docs/platform/lwc/guide/apex-continuations.html (accessed 2026-11-09)
[^s5]: Salesforce Developers, "Lightning Web Components Developer Guide: Work with a Continuation in an Apex Class". https://developer.salesforce.com/docs/platform/lwc/guide/apex-continuations-apex.html (accessed 2026-11-09)
[^s6]: Salesforce Developers Blog, "Apex Continuations: Implementation and Testing in Aura & LWC". https://developer.salesforce.com/blogs/2020/05/apex-continuations-implementation-and-testing-in-aura-lwc (accessed 2026-11-09)
