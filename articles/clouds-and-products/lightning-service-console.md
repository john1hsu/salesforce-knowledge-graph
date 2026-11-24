---
id: kt:lightning-service-console
type: Feature
title: Lightning Service Console
aliases: [Service Console, Salesforce Service Console app, Lightning console app for service, agent workspace]
domain: clouds-and-products
summary: >-
  The standard Lightning console app in Service Cloud (Agentforce Service) that gives service reps one screen for cases,
  customers and knowledge, using workspace tabs, subtabs, split view and a utility bar.
release: "Winter '27"
status: current
broader: [kt:service-cloud]
related: [kt:salesforce-voice, kt:dispatcher-console, kt:workspace-api, kt:lightning-web-components]
relations:
  - {predicate: partOf, object: kt:service-cloud}
  - {predicate: integratesWith, object: kt:omni-channel}
  - {predicate: integratesWith, object: kt:knowledge-base}
  - {predicate: configuredVia, object: kt:lightning-app-builder}
sources:
  - id: s1
    title: "Explore the Service Console (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/service-cloud-agent-experience/explore-the-service-console
    type: official-learning
    accessed: 2026-11-24
  - id: s2
    title: "Set Up the Lightning Service Console (Trailhead project unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/content/learn/projects/set-up-the-service-console/set-up-the-lightning-service-console
    type: official-learning
    accessed: 2026-11-24
  - id: s3
    title: "Get to Know Lightning Console (Salesforce Console Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_console.meta/api_console/sforce_api_console_js_lex_intro.htm
    type: official-docs
    accessed: 2026-11-24
  - id: s4
    title: "Methods for Workspace Tabs and Subtabs in Lightning Experience"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_console.meta/api_console/sforce_api_console_methods_lightning_workspaceAPI.htm
    type: official-docs
    accessed: 2026-11-24
  - id: s5
    title: "Explore the New Service Tools (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lex_migration_whatsnew/lex_migration_whatsnew_service
    type: official-learning
    accessed: 2026-11-24
  - id: s6
    title: "Learn How to Use the Preconfigured Console (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/service-cloud-essentials-features/learn-how-to-use-the-preconfigured-console
    type: official-learning
    accessed: 2026-11-24
created: 2026-11-24
---

# Lightning Service Console

The Lightning Service Console is the standard Lightning console app that ships with Service Cloud (now marketed as Agentforce Service). It gathers case, customer and knowledge information onto a single screen so a service rep can work several cases without losing context.[^s5][^s1] Salesforce treats it as the rep's home base: case details, the case feed, related records and productivity tools all sit in one workspace.[^s6] Reps open it from the App Launcher, and admins often rename and rebrand it for their company.[^s1]

## How it works

A Lightning console app differs from a standard navigation app in how records open. Records open as **workspace tabs**, and related records open as **subtabs** under them, so an account and its contacts or a case and its child cases stay grouped. Tabs can be refreshed, pinned, customized or closed from the tab menu.[^s3] **Split view** adds a collapsible list panel on the left; opening a record from it creates a new workspace tab, which lets a rep move through a queue without returning to a list view.[^s3][^s5] The **utility bar** along the bottom holds tools such as History and Notes, and admins can add Macros, Omni-Channel and an Open CTI softphone.[^s5][^s1]

The preconfigured case page uses three columns. The first shows case and contact details plus related cases for the parent account. The middle column holds a highlights panel and a compact case feed. The third holds related lists and Knowledge articles relevant to the case.[^s5] The case feed is a timeline of emails, calls, social posts and internal notes on the case.[^s1] The console also works in the Salesforce mobile app and supports screen readers and speech recognition.[^s1]

## Setting it up

Admins create or edit console apps in **App Manager**: create a new Lightning app, choose Console Navigation as the navigation style, then add utility items, navigation items and profiles.[^s2] **Navigation rules** decide how each object opens. For example, Accounts can open as workspace tabs, Cases as subtabs of their parent case, and Contacts as subtabs of their account.[^s2] The standard Service Console app is assigned to all standard and custom profiles by default, and every property except its Developer Name can be changed.[^s5] Record pages inside the console are customized with Lightning page layouts and components.[^s2]

## Limits and gotchas

- Notes must be enabled in the org before the Notes utility works, and Lightning Knowledge must be on for the Knowledge component.[^s5]
- The Lightning Knowledge component replaces the Classic Knowledge One sidebar, and standard record types replace Classic article types.[^s5]
- Tab-control methods such as `openTab`, `openSubtab`, `focusTab` and `closeTab` only work inside Lightning console apps, and several Workspace API methods are not supported in Lightning Web Components.[^s4]
- A tab's highlight set with `setTabHighlighted` does not survive a page reload, and the first subtab shares its workspace tab's ID.[^s4]

## Extending it

Developers control tabs from Aura or Lightning Web Components with the **Workspace API**. It can open, focus, label, highlight and close workspace tabs and subtabs, and LWC gets wire adapters such as `IsConsoleNavigation` and `EnclosingTabId`.[^s4] Components that use it can run in the utility bar or on a page inside a console app.[^s3]

## When to use it (and when not)

Use the console for high-volume, multi-record work such as case handling, where reps switch between a case, its contact and its account dozens of times an hour.[^s5][^s6] Orgs on Agentforce Contact Center or Partner Contact Center can add the Phone utility for in-console call controls.[^s2] The underlying console navigation is not service-specific: the same workspace tabs, subtabs and utility bar are available to any Lightning app built with Console Navigation, so other teams with similar multi-record work can reuse the pattern.[^s2][^s3]

## Connections

The console is **part of** `kt:service-cloud`, the product it serves as the rep workspace.[^s5] It **integrates with** `kt:omni-channel`, whose utility delivers routed work and lets reps set presence, and with `kt:knowledge-base`, whose articles appear beside each case.[^s5] Its pages are **configured via** `kt:lightning-app-builder`, while the app itself is defined in App Manager.[^s2] It is related to `kt:salesforce-voice`, whose phone utility runs inside the console, and to `kt:dispatcher-console`, the Field Service counterpart for scheduling work.[^s2][^s5] Developers extend it through `kt:workspace-api` from `kt:lightning-web-components` or Aura components.[^s4]

## Sources
[^s1]: Trailhead, "Explore the Service Console". https://trailhead.salesforce.com/content/learn/modules/service-cloud-agent-experience/explore-the-service-console (accessed 2026-11-24)
[^s2]: Trailhead, "Set Up the Lightning Service Console". https://trailhead.salesforce.com/en/content/learn/projects/set-up-the-service-console/set-up-the-lightning-service-console (accessed 2026-11-24)
[^s3]: Salesforce Developers, "Get to Know Lightning Console". https://developer.salesforce.com/docs/atlas.en-us.api_console.meta/api_console/sforce_api_console_js_lex_intro.htm (accessed 2026-11-24)
[^s4]: Salesforce Developers, "Methods for Workspace Tabs and Subtabs in Lightning Experience". https://developer.salesforce.com/docs/atlas.en-us.api_console.meta/api_console/sforce_api_console_methods_lightning_workspaceAPI.htm (accessed 2026-11-24)
[^s5]: Trailhead, "Explore the New Service Tools". https://trailhead.salesforce.com/content/learn/modules/lex_migration_whatsnew/lex_migration_whatsnew_service (accessed 2026-11-24)
[^s6]: Trailhead, "Learn How to Use the Preconfigured Console". https://trailhead.salesforce.com/content/learn/modules/service-cloud-essentials-features/learn-how-to-use-the-preconfigured-console (accessed 2026-11-24)
