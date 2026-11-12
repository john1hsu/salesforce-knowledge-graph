---
id: kt:visualforce
type: Feature
title: Visualforce
aliases: [Visualforce pages, VF pages, apex:page markup, Visualforce framework]
domain: development
summary: >-
  Salesforce's original server-rendered UI framework: tag-based page markup bound to a standard controller,
  custom Apex controller or controller extension, still supported but superseded by Lightning Web Components
  for new custom UI.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:aura-components, kt:apex-continuations, kt:page-layouts, kt:experience-cloud]
relations:
  - {predicate: alternativeTo, object: kt:lightning-web-components}
  - {predicate: dependsOn, object: kt:apex}
  - {predicate: dependsOn, object: kt:salesforce-sharing-model}
  - {predicate: integratesWith, object: kt:lightning-message-service}
  - {predicate: integratesWith, object: kt:salesforce-lightning-design-system}
sources:
  - id: s1
    title: "Visualforce Developer Guide: What is Visualforce?"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-pages-developers-guide/guide/pages-intro-what-is-it.html
    type: official-docs
    accessed: 2026-11-12
  - id: s2
    title: "Visualforce Developer Guide: Optimize the View State"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.pages.meta/pages/pages_best_practices_perf_view_state.htm
    type: official-docs
    accessed: 2026-11-12
  - id: s3
    title: "Visualforce Basics: Use Standard Controllers"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/visualforce_fundamentals/visualforce_standard_controllers
    type: official-learning
    accessed: 2026-11-12
  - id: s4
    title: "Visualforce & Lightning Experience: Known Issues"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lex_dev_visualforce/lex_dev_visualforce_known_issues
    type: official-learning
    accessed: 2026-11-12
  - id: s5
    title: "Visualforce Developer Guide: Style Existing Visualforce Pages with Lightning Experience Stylesheets"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-pages-developers-guide/guide/vf-dev-best-practices-slds-lightningstylesheets.html
    type: official-docs
    accessed: 2026-11-12
  - id: s6
    title: "Platform Developer I Certification Prep: User Interfaces — Visualforce"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/platform-developer-i-certification-prep-user-interfaces/pd1-3-ui-visualforce
    type: official-learning
    accessed: 2026-11-12
created: 2026-11-12
---

# Visualforce

Visualforce is the framework Salesforce provides for building custom user interfaces hosted natively on the platform. A page is written in a tag-based markup language that resembles HTML, where each tag corresponds to a UI component such as a page section, a related list or a field, and everything sits inside a single `<apex:page>` tag that can also contain plain HTML and JavaScript.[^s1] Visualforce remains supported, but Salesforce now recommends Lightning Web Components for new custom functionality because they are lighter weight and perform better.[^s1]

## How it works

Every page is defined by two parts: its markup and a controller that supplies data and actions.[^s1] There are four controller options:

- **Standard controller**: reuses the logic of the standard record page, enforces the user's object access and runs in user mode.[^s1]
- **Standard list controller**: lets one page show or act on a set of records, as list views and mass-action pages do.[^s1]
- **Custom controller**: an Apex class that implements all page logic itself and runs in system mode, ignoring object and field permissions.[^s1]
- **Controller extension**: an Apex class that adds to or overrides a standard or custom controller's behaviour.[^s1]

Extending a standard controller keeps user-mode enforcement for the standard actions even though the extension itself runs in system mode, and custom controllers and extensions honour record sharing only when declared `with sharing`.[^s1] Most standard objects and all custom objects have a standard controller, which provides create, edit, save and delete without custom code; it reads the `id` URL parameter, loads that record and exposes it under the object's name.[^s3] Pages bind data with merge expressions of the form `{! Account.Name }`, and dot notation walks relationships, as in `{! Account.Owner.Name }`.[^s3]

Pages can override standard buttons and tab pages, back custom tabs, be embedded in detail page layouts, act as dashboard components or console sidebar components, and appear as actions in the Salesforce mobile app.[^s1] Pages embedded in object page layouts, used as object-specific custom actions or shown as mobile cards must use the standard controller of that object.[^s3]

## Limits and gotchas

- **View state**: component state, field values and the controller are serialized into an encrypted hidden form field capped at 170 KB.[^s2]
- **Shrinking view state**: mark request-only variables `transient`, narrow SOQL queries, paginate, and show read-only data with output components.[^s2]
- **JavaScript remoting** skips view-state transmission but does not shrink the state, and it gives up `reRender` handling.[^s2]

In Lightning Experience each page renders inside its own iframe, so the Lightning header cannot be hidden and the `showHeader` and `sidebar` attributes have no effect.[^s4] Code that sets `window.location` directly must be rewritten, `sforce.one` exists in both Lightning Experience and the mobile app so it cannot detect mobile, and a list-view action override is unreachable there.[^s4] Adding `lightningStylesheets` to `<apex:page>` gives a page the Lightning look in Lightning Experience and the mobile app, but it is not supported in Experience Cloud sites, does not apply to PDF rendering, and is suppressed when `standardStylesheets` is false.[^s5]

## When to use it (and when not)

Choose Lightning Web Components for new UI; keep Visualforce for maintaining existing pages, PDF output via `renderAs="pdf"` (which Lightning stylesheets do not style), and places that still require a page, such as a standard-controller page in a page layout.[^s1][^s5] Because custom controllers run in system mode, developers must enforce object, field and sharing access themselves; Trailhead's Platform Developer prep content groups Visualforce with UI and data-access security vulnerabilities in its user-interface material.[^s1][^s6]

## Connections

Visualforce sits on the `kt:salesforce-platform` UI layer and is an `alternativeTo` `kt:lightning-web-components`, the recommended successor, and a sibling of `kt:aura-components`.[^s1] Its controllers `dependsOn` `kt:apex`, and they must opt into `kt:salesforce-sharing-model` with `with sharing`.[^s1] Pages can be embedded in `kt:page-layouts` with a standard controller, can call `kt:apex-continuations` for long-running callouts, and `integratesWith` `kt:lightning-message-service` to talk to Lightning components.[^s3][^s1] `lightningStylesheets` applies `kt:salesforce-lightning-design-system` styling, with exclusions for `kt:experience-cloud` sites.[^s5]

## Sources
[^s1]: Salesforce Developers, "Visualforce Developer Guide: What is Visualforce?". https://developer.salesforce.com/docs/platform/salesforce-pages-developers-guide/guide/pages-intro-what-is-it.html (accessed 2026-11-12)
[^s2]: Salesforce Developers, "Visualforce Developer Guide: Optimize the View State". https://developer.salesforce.com/docs/atlas.en-us.pages.meta/pages/pages_best_practices_perf_view_state.htm (accessed 2026-11-12)
[^s3]: Trailhead, "Visualforce Basics: Use Standard Controllers". https://trailhead.salesforce.com/content/learn/modules/visualforce_fundamentals/visualforce_standard_controllers (accessed 2026-11-12)
[^s4]: Trailhead, "Visualforce & Lightning Experience: Known Issues". https://trailhead.salesforce.com/content/learn/modules/lex_dev_visualforce/lex_dev_visualforce_known_issues (accessed 2026-11-12)
[^s5]: Salesforce Developers, "Style Existing Visualforce Pages with Lightning Experience Stylesheets". https://developer.salesforce.com/docs/platform/salesforce-pages-developers-guide/guide/vf-dev-best-practices-slds-lightningstylesheets.html (accessed 2026-11-12)
[^s6]: Trailhead, "Platform Developer I Certification Prep: User Interfaces — Visualforce". https://trailhead.salesforce.com/content/learn/modules/platform-developer-i-certification-prep-user-interfaces/pd1-3-ui-visualforce (accessed 2026-11-12)
