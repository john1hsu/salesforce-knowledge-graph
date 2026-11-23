---
id: kt:salesforce-mobile-app
type: Product
title: Salesforce Mobile App
aliases: [Salesforce1, Salesforce1 mobile app, Salesforce app for iOS and Android, Salesforce mobile web, Mobile Only app]
domain: platform-architecture
summary: >-
  Salesforce's own iOS and Android app (formerly Salesforce1) that renders an org's metadata-driven apps, records,
  actions and Lightning pages on phones, customized by admins through mobile navigation, compact layouts and quick actions.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform, kt:metadata-driven-architecture]
related: [kt:lightning-app-builder, kt:compact-layouts, kt:quick-actions, kt:dynamic-forms, kt:mobile-sdk]
relations:
  - {predicate: configuredVia, object: kt:lightning-app-builder}
  - {predicate: dependsOn, object: kt:compact-layouts}
  - {predicate: dependsOn, object: kt:quick-actions}
  - {predicate: enables, object: kt:briefcase-builder}
  - {predicate: alternativeTo, object: kt:mobile-sdk}
sources:
  - id: s1
    title: "Salesforce Mobile App Customization: Salesforce Mobile App Benefits & Features"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce1_mobile_app/salesforce1_mobile_app_intro
    type: official-learning
    accessed: 2026-11-23
  - id: s2
    title: "Salesforce Mobile App Customization: Customize Navigation Menu for Salesforce App"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/modules/salesforce1_mobile_app/units/salesforce1_mobile_app_navigation
    type: official-learning
    accessed: 2026-11-23
  - id: s3
    title: "Salesforce Mobile App Customization: Customize Compact Layouts"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce1_mobile_app/salesforce1_mobile_app_compact_layouts
    type: official-learning
    accessed: 2026-11-23
  - id: s4
    title: "Salesforce Mobile App Customization: Create Global Quick Actions"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/content/learn/modules/salesforce1_mobile_app/salesforce1_mobile_app_actions_global
    type: official-learning
    accessed: 2026-11-23
  - id: s5
    title: "Mobile and Offline Developer Guide: Build a Briefcase"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.mobile_offline.meta/mobile_offline/dx_onboard_wizard_briefcase.htm
    type: official-docs
    accessed: 2026-11-23
  - id: s6
    title: "Salesforce Mobile SDK Basics: Learn OAuth 2.0 for Secure Mobile App Authentication"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/mobile_sdk_introduction/mobilesdk_intro_security
    type: official-learning
    accessed: 2026-11-23
created: 2026-11-23
---

# Salesforce Mobile App

The Salesforce mobile app is Salesforce's own app for iOS and Android phones, originally branded Salesforce1. Users install it from the App Store or Google Play, and Trailhead describes it as included with every Salesforce license at no extra cost. It works alongside desktop Lightning Experience and includes offline capabilities.[^s1] Because it is built on the same metadata as the desktop UI, most of an org's customizations (objects, fields, apps, Lightning pages) appear in the app automatically, without a separate mobile build.[^s1]

## How it works

The app reads the org's metadata at runtime and renders it for a small screen. Admins shape the experience mainly through three tools: the mobile navigation of each Lightning app (and of the Mobile Only app), compact layouts, and quick actions.[^s1] Trailhead's example of why this matters is an opportunity page layout with more than 100 fields, which works on a desktop but is unwieldy on a phone.[^s1]

**Navigation.** A bar at the bottom of the screen plus a Menu list the objects, apps and items available to the user. Menu items mirror the desktop tabs of the active Lightning app; the default app is the first Lightning app in the App Launcher. Admins set the order in App Manager by editing the app, choosing the "Desktop and phone" form factor and reordering Navigation Items, and the top items become the icons in the bottom bar.[^s2] Users with permission can reorder items from the app itself, and changes made on desktop sync after a refresh.[^s2]

**Record headers.** Compact layouts decide which fields appear in a record's header on mobile. A compact layout holds up to 10 fields including Name and cannot contain text areas, long or rich text areas, or multi-select picklists.[^s3] Orgs that use Dynamic Highlights Panels on Lightning record pages can turn on the "Dynamic Forms and Dynamic Highlights Panel on Mobile" setting to drive mobile headers from the Lightning page instead.[^s3]

**Actions.** Quick actions appear in the action bar and action menu. Object-specific actions run in the context of a record and can update it, while global actions create records with no relationship to others and cannot update a record. The global publisher layout's "Salesforce Mobile and Lightning Experience Actions" section sets which global actions appear in the feed and Chatter groups, and in what order.[^s4]

## Offline access

Offline data is driven by Briefcase Builder in Setup, which defines which records are primed onto the device for offline use. Salesforce advises grouping users by role when designing briefcases, and every record on a user's offline Landing Page must also be in their briefcase, because the Landing Page relies on it for record details.[^s5]

## Limits and gotchas

- One compact layout per object applies to every user; it can't vary by profile, only by record type through Record Type Overrides.[^s3]
- Mobile navigation can't be configured differently per user type; Visualforce pages, Lightning pages and components need a tab and must be enabled for mobile to show in the menu.[^s2]
- Quick action layouts should stay short: Trailhead recommends fewer than five fields and never more than eight.[^s4]
- The app logs in to production by default; test customizations in a sandbox, Developer Edition or Trailhead Playground. Some desktop features aren't available in the app.[^s1]
- New actions may not appear until the user refreshes, or logs out and back in.[^s4]

## When to use it (and when not)

Use the Salesforce mobile app when users need the same org, data and declarative customizations on a phone; it costs nothing extra and inherits the metadata of the desktop org.[^s1] When a team needs a fully custom native experience, the Mobile SDK is the alternative: SDK apps authenticate with OAuth 2.0 through an external client app (or a connected app for multi-org distribution) and can enforce an optional screen lock with biometric or passcode unlock.[^s6] For heavy offline use, plan briefcases by user role so each group gets only the records it needs.[^s5]

## Connections

The app is a consumer of `kt:salesforce-platform` metadata and so sits under `kt:metadata-driven-architecture`.[^s1] Its record pages are built in `kt:lightning-app-builder`, with headers from `kt:compact-layouts` or `kt:dynamic-forms`-era Dynamic Highlights Panels, and its action bar depends on `kt:quick-actions`.[^s3][^s4] Offline behavior is enabled by `kt:briefcase-builder`, which primes the records each user group can open offline.[^s5] For custom native apps the contrasting option is `kt:mobile-sdk`, which connects through `kt:external-client-apps` or `kt:connected-apps`.[^s6]

## Sources

[^s1]: Trailhead, "Salesforce Mobile App Customization: Salesforce Mobile App Benefits & Features". https://trailhead.salesforce.com/content/learn/modules/salesforce1_mobile_app/salesforce1_mobile_app_intro (accessed 2026-11-23)
[^s2]: Trailhead, "Salesforce Mobile App Customization: Customize Navigation Menu for Salesforce App". https://trailhead.salesforce.com/modules/salesforce1_mobile_app/units/salesforce1_mobile_app_navigation (accessed 2026-11-23)
[^s3]: Trailhead, "Salesforce Mobile App Customization: Customize Compact Layouts". https://trailhead.salesforce.com/content/learn/modules/salesforce1_mobile_app/salesforce1_mobile_app_compact_layouts (accessed 2026-11-23)
[^s4]: Trailhead, "Salesforce Mobile App Customization: Create Global Quick Actions". https://trailhead.salesforce.com/en/content/learn/modules/salesforce1_mobile_app/salesforce1_mobile_app_actions_global (accessed 2026-11-23)
[^s5]: Salesforce Developers, "Mobile and Offline Developer Guide: Build a Briefcase". https://developer.salesforce.com/docs/atlas.en-us.264.0.mobile_offline.meta/mobile_offline/dx_onboard_wizard_briefcase.htm (accessed 2026-11-23)
[^s6]: Trailhead, "Salesforce Mobile SDK Basics: Learn OAuth 2.0 for Secure Mobile App Authentication". https://trailhead.salesforce.com/content/learn/modules/mobile_sdk_introduction/mobilesdk_intro_security (accessed 2026-11-23)
