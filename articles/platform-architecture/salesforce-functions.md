---
id: kt:salesforce-functions
type: Product
title: Salesforce Functions
aliases: [Salesforce Elastic Services, Elastic Services, Salesforce Functions retirement, functions namespace]
domain: platform-architecture
summary: >-
  Salesforce's retired functions-as-a-service offering (sold as Salesforce Elastic Services) that ran Java and
  JavaScript/TypeScript code in Salesforce-managed, Heroku-powered compute environments, preauthenticated to an org
  and invoked from Apex; no longer sold or renewed, with Heroku AppLink as the recommended successor.
release: "Winter '27"
status: retired
broader: [kt:salesforce-platform]
related: [kt:asynchronous-apex, kt:salesforce-dx, kt:apex-callouts]
relations:
  - {predicate: replacedBy, object: kt:heroku-applink}
  - {predicate: dependsOn, object: kt:heroku}
  - {predicate: configuredVia, object: kt:salesforce-cli}
  - {predicate: integratesWith, object: kt:apex}
  - {predicate: mitigates, object: kt:governor-limits}
sources:
  - id: s1
    title: "Salesforce Functions Retirement"
    publisher: Heroku Dev Center (Salesforce)
    url: https://devcenter.heroku.com/articles/salesforce-functions-retirement
    type: official-docs
    accessed: 2026-11-25
  - id: s2
    title: "Overview and Architecture (Salesforce Functions Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/functions/guide/overview.html
    type: official-docs
    accessed: 2026-11-25
  - id: s3
    title: "Invoke Functions with Apex (Salesforce Functions Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/functions/guide/invoke-apex.html
    type: official-docs
    accessed: 2026-11-25
  - id: s4
    title: "Manage Compute Environments (Salesforce Functions Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/functions/guide/manage-envs.html
    type: official-docs
    accessed: 2026-11-25
  - id: s5
    title: "Function Class (Apex Reference Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_class_functions_Function.htm
    type: official-docs
    accessed: 2026-11-25
  - id: s6
    title: "Deliver Scalable Experiences Without Limits Using Functions"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2021/06/functions-announcement
    type: official-blog
    accessed: 2026-11-25
created: 2026-11-25
---

# Salesforce Functions

**Salesforce Functions**, sold as **Salesforce Elastic Services**, was Salesforce's functions-as-a-service product: developers wrote code in standard languages, deployed it to Salesforce-managed compute outside the org, and called it from Apex. Salesforce has retired it. The last day to buy a new Elastic Services subscription was October 31, 2023, and the last day to renew one was January 31, 2024; customers were told to put an alternative in place before their current order term ran out.[^s1] The recommended replacement is **Heroku AppLink**, and the retirement notice points out that Heroku was the technology underneath Functions all along.[^s1] It matters to architects today mainly when reviewing older orgs that still carry `functions` Apex code, and as context for why AppLink looks the way it does.

## How it worked

Functions ran on Salesforce-managed infrastructure kept apart from the org's own multitenant runtime. Code was never deployed into the org; instead, each Salesforce DX project mapped to one dedicated **compute environment**.[^s2] At runtime a function was automatically authenticated to the org that invoked it, its compute did not count against the org's request limits, and it scaled elastically. Supported regions were Virginia, Oregon, Dublin, Frankfurt, Tokyo and Sydney, and the runtime stayed on the latest version of its Heroku stack.[^s2] Enabling Functions for an org required a Salesforce Functions license.[^s2]

The developer loop lived in the Salesforce CLI. A compute environment had to exist before a function could be deployed or invoked, each one was tied to a single org, and teams typically created one per scratch org or sandbox plus one for production, using commands such as `sf env create compute`.[^s4] The 2021 beta announcement showed Java and Node.js functions that received an invocation event and a context object giving access to the authenticated org; it announced a Summer '21 beta with general availability planned for Winter '22.[^s6]

## Invoking from Apex

Apex reached functions through the `functions` namespace. `functions.Function.get()` returned a reference by project and function name, and `invoke()` called it either synchronously with a JSON string payload or asynchronously with a `functions.FunctionCallback` whose `handleResponse()` method received the result.[^s5] Asynchronous calls were queued through asynchronous Apex, the callback ran as the invoking user in system mode, and those calls did not count against Queueable limits.[^s3] Request status could be tracked by querying the FunctionInvocationRequest object.[^s3]

## Limits and gotchas

A synchronous invocation was capped at two minutes, and exceeding it raised a `CalloutException`, as did pending uncommitted DML, invoking from a trigger, or a 404 or 5xx response.[^s5] Apex triggers had to call functions asynchronously.[^s3] Functions could not be invoked from Apex tests, so test code needed mocks, and an asynchronous call was not queued if its transaction did not commit.[^s5]

## Migration and alternatives

Because the product is no longer sold or renewed, new designs should not use it. Salesforce directs customers to Heroku AppLink, which adds connections to multiple orgs and enforces Salesforce user permissions when a Heroku app works with org data.[^s1] Migrating generally means moving function code into a Heroku app and replacing `functions.Function` calls with calls to the services AppLink exposes, including the test mocks that wrapped them.[^s1][^s3] For lighter elastic needs that fit inside the platform, asynchronous Apex remains the in-org option, since Functions were themselves invoked through it.[^s3]

## Connections

Functions belonged to the broader **Salesforce Platform** as its off-org compute tier, and they **depended on Heroku**, which powered the runtime.[^s1] They were **configured via the Salesforce CLI** and the Salesforce DX project model, with one compute environment per org.[^s4] They **integrated with Apex**, through the `functions` namespace, and leaned on **asynchronous Apex** for queued calls.[^s3] Their purpose was to **mitigate governor limits** by moving heavy processing to elastic compute that did not consume org limits, an alternative to plain **Apex callouts** to self-managed services.[^s2] They are **replaced by Heroku AppLink**.[^s1]

## Sources

[^s1]: Heroku Dev Center (Salesforce), "Salesforce Functions Retirement". https://devcenter.heroku.com/articles/salesforce-functions-retirement (accessed 2026-11-25)
[^s2]: Salesforce, "Overview and Architecture (Salesforce Functions Developer Guide)". https://developer.salesforce.com/docs/platform/functions/guide/overview.html (accessed 2026-11-25)
[^s3]: Salesforce, "Invoke Functions with Apex (Salesforce Functions Developer Guide)". https://developer.salesforce.com/docs/platform/functions/guide/invoke-apex.html (accessed 2026-11-25)
[^s4]: Salesforce, "Manage Compute Environments (Salesforce Functions Developer Guide)". https://developer.salesforce.com/docs/platform/functions/guide/manage-envs.html (accessed 2026-11-25)
[^s5]: Salesforce, "Function Class (Apex Reference Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_class_functions_Function.htm (accessed 2026-11-25)
[^s6]: Salesforce Developers Blog, "Deliver Scalable Experiences Without Limits Using Functions". https://developer.salesforce.com/blogs/2021/06/functions-announcement (accessed 2026-11-25)
