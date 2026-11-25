---
id: kt:workspace-api
type: API
title: Workspace API
aliases: [Lightning Console Workspace API, lightning/platformWorkspaceApi, lightning:workspaceAPI, Platform Workspace API]
domain: development
summary: >-
  The Lightning Console JavaScript API library that lets Aura and Lightning web components open, focus, label,
  refresh and close workspace tabs and subtabs in Lightning console apps; LWC uses the lightning/platformWorkspaceApi
  module, Aura the legacy lightning:workspaceAPI component.
release: "Winter '27"
status: current
created: 2026-11-25
broader: [kt:salesforce-apis]
related: [kt:lightning-message-service, kt:lwc-jest-testing, kt:content-security-policy]
relations:
  - {predicate: integratesWith, object: kt:lightning-service-console}
  - {predicate: consumedBy, object: kt:lightning-web-components}
  - {predicate: consumedBy, object: kt:aura-components}
sources:
  - id: s1
    title: "Salesforce Console Developer Guide: Lightning Console API"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.api_console.meta/api_console/sforce_api_console_lex_getting_started.htm
    type: official-docs
    accessed: 2026-11-25
  - id: s2
    title: "Lightning Component Reference: Platform Workspace API"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-platform-workspace-api.html
    type: official-docs
    accessed: 2026-11-25
  - id: s3
    title: "Salesforce Console Developer Guide: openTab() for Lightning Experience"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/service/api-console/guide/sforce-api-console-lightning-opentab.html
    type: official-docs
    accessed: 2026-11-25
  - id: s4
    title: "Lightning Component Reference: Workspace API (Legacy Components)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/aura-workspace-api.html
    type: official-docs
    accessed: 2026-11-25
  - id: s5
    title: "Navigate Console Apps from Lightning Web Components with the Workspace API"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/06/navigate-console-apps-from-lightning-web-components-with-the-workspace-api
    type: official-blog
    accessed: 2026-11-25
---

# Workspace API

The **Workspace API** is the part of the Lightning Console JavaScript API that gives custom components programmatic control over the workspace tabs and subtabs of a Lightning console app. The console API is split into three libraries: the navigation item API (Aura only, which drives the console's navigation menu), the utility bar API (Aura and LWC, usable in standard or console navigation), and the workspace API (Aura and LWC, console apps only).[^s1] It is available in Lightning Experience across Essentials, Professional, Enterprise, Performance, Unlimited and Developer editions.[^s1]

## Two entry points: LWC and Aura

In Lightning web components the API is the `lightning/platformWorkspaceApi` module, which requires API version 59.0 or later.[^s2] Salesforce's developer blog describes its general availability in Spring '24 as closing the gap that previously forced LWC developers to wrap the Aura component, and positions the module as the replacement for that legacy component.[^s5] Salesforce recommends LWC over Aura for new console work.[^s1]

The module exposes individual functions such as `openTab`, `openSubtab`, `focusTab`, `closeTab`, `refreshTab`, `getFocusedTabInfo`, `getTabInfo`, `getAllTabInfo`, `setTabLabel`, `setTabIcon`, `setTabHighlighted` and `disableTabClose`, plus the `IsConsoleNavigation` and `EnclosingTabId` wire adapters.[^s2] Every function returns a promise; required parameters are passed as separate arguments and optional ones in an object as the last argument.[^s2] Console events that Aura receives as application events are consumed in LWC by subscribing to Lightning message channels.[^s2]

In Aura, a component declares `<lightning:workspaceAPI aura:id="workspace"/>`, looks it up with `component.find`, and calls methods that mostly take a single JSON argument.[^s4] The Aura reference lists some methods that the LWC module's import list does not show, including `getTabURL`, `isSubtab`, `generateConsoleURL`, `openConsoleURL` and the browser-title queue methods, so check both references before porting a component.[^s4][^s2]

## How opening a tab works

`openTab()` opens a new workspace tab, or focuses it if it is already open, and resolves to the new tab's ID.[^s3] Its optional inputs are a `pageReference`, a `recordId` or a `url`, plus `focus` (open in the foreground or background) and `overrideNavRules`; LWC additionally accepts `label`, `icon` and `iconAlt`.[^s3] When more than one target is passed, `pageReference` wins over `recordId`, which wins over `url`, and the lower-priority values are ignored.[^s3] `openSubtab` opens a subtab under a parent workspace tab, whose ID a component can read through the `EnclosingTabId` wire adapter or tab-info functions.[^s2]

## Limits and gotchas

- **Console apps only.** The workspace API does nothing useful in standard navigation apps; guard calls with the `IsConsoleNavigation` wire adapter.[^s1][^s2]
- **External URLs need a trusted site.** A third-party domain passed to `openTab` must be added as a CSP Trusted Site first.[^s3]
- **Placement matters.** An LWC must include the `lightning__AppPage` target in its configuration to be used in a console app.[^s3]
- **Nav rules.** `overrideNavRules` has no effect on records without navigation rules or on URLs that don't point to a record.[^s3]
- **No navigation item API in LWC.** Only the utility bar and workspace libraries are supported for Lightning web components today.[^s1]
- **Testing.** Jest can't load Lightning Experience, so unit tests stub the module's functions instead of opening real tabs.[^s5]

## When to use it

Use the Workspace API when a component must behave like part of the console: opening related records as subtabs of the current case, renaming or highlighting a tab when work is waiting, or refreshing a tab after a background update.[^s2][^s3] Because the library is limited to console apps, components that must also run in standard navigation apps need a fallback path, and footer utilities are handled by the separate utility bar API rather than this one.[^s1]

## Connections

The Workspace API is one of the `kt:salesforce-apis`, a client-side JavaScript API rather than a data API.[^s1] It **integrates with** `kt:lightning-service-console`, a standard console app whose tabs it controls, and is **consumed by** `kt:lightning-web-components` through `lightning/platformWorkspaceApi` and by `kt:aura-components` through `lightning:workspaceAPI`.[^s2][^s4] It is related to `kt:lightning-message-service`, the channel LWC uses for console events, to `kt:lwc-jest-testing`, where its functions are stubbed, and to `kt:content-security-policy`, because external tab URLs must be trusted sites.[^s2][^s5][^s3]

## Sources
[^s1]: Salesforce, "Salesforce Console Developer Guide: Lightning Console API". https://developer.salesforce.com/docs/atlas.en-us.api_console.meta/api_console/sforce_api_console_lex_getting_started.htm (accessed 2026-11-25)
[^s2]: Salesforce, "Lightning Component Reference: Platform Workspace API". https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-platform-workspace-api.html (accessed 2026-11-25)
[^s3]: Salesforce, "Salesforce Console Developer Guide: openTab() for Lightning Experience". https://developer.salesforce.com/docs/service/api-console/guide/sforce-api-console-lightning-opentab.html (accessed 2026-11-25)
[^s4]: Salesforce, "Lightning Component Reference: Workspace API (Legacy Components)". https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/aura-workspace-api.html (accessed 2026-11-25)
[^s5]: Salesforce Developers Blog, "Navigate Console Apps from Lightning Web Components with the Workspace API". https://developer.salesforce.com/blogs/2024/06/navigate-console-apps-from-lightning-web-components-with-the-workspace-api (accessed 2026-11-25)
