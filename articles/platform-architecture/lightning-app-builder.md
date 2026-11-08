---
id: kt:lightning-app-builder
type: Tool
title: Lightning App Builder
aliases: [Lightning pages, Lightning page, FlexiPage, FlexiPage metadata type, component visibility rules, Lightning record page]
domain: platform-architecture
summary: >-
  Salesforce's point-and-click page editor for building app, Home and record pages (Lightning pages, stored as
  FlexiPage metadata) from standard, custom and third-party components for Lightning Experience and the mobile app.
release: "Winter '27"
status: current
broader: [kt:metadata-driven-architecture, kt:salesforce-platform]
related: [kt:page-layouts, kt:dynamic-forms, kt:record-types, kt:profiles, kt:experience-builder, kt:aura-components]
relations:
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: integratesWith, object: kt:lightning-web-components}
  - {predicate: coveredBy, object: kt:platform-app-builder-certification}
sources:
  - id: s1
    title: "Lightning App Builder: Get Started with the Lightning App Builder"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lightning_app_builder/lightning_app_builder_intro
    type: official-learning
    accessed: 2026-11-08
  - id: s2
    title: "Lightning App Builder: Build a Custom Record Page for Lightning Experience and Salesforce Mobile App"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lightning_app_builder/lightning_app_builder_recordpage
    type: official-learning
    accessed: 2026-11-08
  - id: s3
    title: "Lightning App Builder: Add Visibility Rules for Dynamic Pages"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lightning_app_builder/add-visibility-rules-for-dynamic-pages-lab
    type: official-learning
    accessed: 2026-11-08
  - id: s4
    title: "Metadata API Developer Guide: FlexiPage"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_flexipage.htm
    type: official-docs
    accessed: 2026-11-08
  - id: s5
    title: "Lightning Web Components Developer Guide: Configure a Component for Lightning App Builder"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/use-config-for-app-builder.html
    type: official-docs
    accessed: 2026-11-08
  - id: s6
    title: "Lightning Web Components Developer Guide: Dynamic Interactions"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/use-config-for-app-builder-dynamic-interactions.html
    type: official-docs
    accessed: 2026-11-08
created: 2026-11-08
---

# Lightning App Builder

Lightning App Builder is the declarative, drag-and-drop tool admins use to assemble custom pages for Lightning Experience and the Salesforce mobile app. When opened from App Manager it also edits an app's branding, navigation items and assigned pages. The pages it produces are called Lightning pages and are made of regions that hold Lightning components; components can be standard (built by Salesforce), custom (built in-house and configured for the builder) or third-party packages from the marketplace.[^s1]

## How it works

Every Lightning page starts from a template, which defines the regions and how the layout adapts per device. The builder has a component palette (with a Fields tab on record pages), a canvas for arranging components, and a properties pane for page- or component-level settings.[^s1] The three page types admins meet most are app pages (a home page for an app, available in desktop and mobile navigation), Home pages (Lightning Experience only) and record pages, which customize an object's record view on both desktop and mobile.[^s1]

Under the hood a Lightning page is a `FlexiPage` metadata component (suffix `.flexipage`, folder `flexipages`). Its required `type` field covers far more than the three common types: `UtilityBar`, `RecordPreview`, `MailAppAppPage`, `ForecastingPage`, a beta `QuickAction` type in API 68.0, and many `Comm*` types used by Experience Builder sites. Each region has a name and a list of item instances, and a single region holds up to 100 components. The associated object is null for app and Home pages and can't be changed once set.[^s4]

## Activation and assignment

Saving a page doesn't show it to anyone; it must be activated. A record page can be made the org default for its object, the default for specific Lightning apps, or assigned to a combination of app, record type and profile, and it can be targeted at a form factor so phone and desktop users see different pages.[^s2] This layered assignment model is why the same object can look different to sales and service users without separate objects or code.[^s2]

## Dynamic pages and component interactions

Component visibility rules show or hide a component (standard, custom or third-party) based on filters such as record field values, the device form factor, or the user's profile or permissions; a component with no filter always displays. On Dynamic Forms field-level rules are evaluated as the user edits, while field section rules are only evaluated after the record is saved.[^s3] Dynamic Interactions let an admin wire an event fired by one component to actions on other components on an app page. Only Lightning web components can act as sources, though Aura or LWC components can be targets, and event schema properties are limited to String, Integer and Boolean.[^s6]

## Making custom components available

A Lightning web component appears in the palette only when its `js-meta.xml` sets `isExposed` to true and lists targets such as `lightning__RecordPage`, `lightning__AppPage` and `lightning__HomePage`. A `targetConfig` per target can expose different admin-editable properties and, for record pages, restrict the component to specific objects; external objects are not supported in that restriction. If a property's type differs between the JavaScript and the configuration file, the configuration file wins.[^s5]

## Limits and gotchas

- Up to 100 components per region; Home pages don't render in the mobile app.[^s4][^s1]
- Hidden components can leave a region looking empty, so test visibility rules on all components that share a tab, accordion or column.[^s3]
- Some standard components are desktop-only; palette icons indicate supported form factors.[^s2]
- `EmailContentPage` and `EmailTemplatePage` FlexiPages store builder markup and can't be retrieved or deployed.[^s4]

## When to use it (and when not)

Use Lightning App Builder whenever a page arrangement, conditional display or component wiring can be done declaratively; it keeps UI in metadata that deploys like any other component.[^s4] Reach for a custom Lightning web component when no standard component fits, then expose it to the builder so admins still control placement and properties.[^s5] For public-facing sites, Experience Builder edits the `Comm*` page types instead.[^s4]

## Connections

Lightning pages are FlexiPage metadata, so the tool sits under `kt:metadata-driven-architecture` and is deployed through `kt:metadata-api`.[^s4] Record pages sit on top of `kt:page-layouts` and can replace layout-driven field sections with `kt:dynamic-forms`; assignment combines apps with `kt:record-types` and `kt:profiles`.[^s2][^s3] Custom building blocks come from `kt:lightning-web-components` and legacy `kt:aura-components`, the latter able to be Dynamic Interaction targets.[^s5][^s6] `kt:experience-builder` is the sibling builder for Experience Cloud pages, and the tool is core material for the `kt:platform-app-builder-certification`.[^s4][^s1]

## Sources

[^s1]: Trailhead, "Lightning App Builder: Get Started with the Lightning App Builder". https://trailhead.salesforce.com/content/learn/modules/lightning_app_builder/lightning_app_builder_intro (accessed 2026-11-08)
[^s2]: Trailhead, "Lightning App Builder: Build a Custom Record Page for Lightning Experience and Salesforce Mobile App". https://trailhead.salesforce.com/content/learn/modules/lightning_app_builder/lightning_app_builder_recordpage (accessed 2026-11-08)
[^s3]: Trailhead, "Lightning App Builder: Add Visibility Rules for Dynamic Pages". https://trailhead.salesforce.com/content/learn/modules/lightning_app_builder/add-visibility-rules-for-dynamic-pages-lab (accessed 2026-11-08)
[^s4]: Salesforce Developers, "Metadata API Developer Guide: FlexiPage". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_flexipage.htm (accessed 2026-11-08)
[^s5]: Salesforce Developers, "Lightning Web Components Developer Guide: Configure a Component for Lightning App Builder". https://developer.salesforce.com/docs/platform/lwc/guide/use-config-for-app-builder.html (accessed 2026-11-08)
[^s6]: Salesforce Developers, "Lightning Web Components Developer Guide: Dynamic Interactions". https://developer.salesforce.com/docs/platform/lwc/guide/use-config-for-app-builder-dynamic-interactions.html (accessed 2026-11-08)
