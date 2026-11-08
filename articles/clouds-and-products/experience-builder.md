---
id: kt:experience-builder
type: Tool
title: Experience Builder
aliases: [Community Builder, Salesforce Experience Builder, Experience Cloud site builder]
domain: clouds-and-products
summary: >-
  The drag-and-drop visual editor for Experience Cloud sites, where admins arrange pages and components, set
  themes and branding, preview by device and publish changes; developers extend it with Lightning web components
  and Aura components exposed through targets, interfaces and design properties.
release: "Winter '27"
status: current
broader: [kt:experience-cloud]
related: [kt:lightning-web-components, kt:aura-components, kt:experience-cloud-identity, kt:lightning-data-service]
relations:
  - {predicate: partOf, object: kt:experience-cloud}
  - {predicate: dependsOn, object: kt:lightning-web-components}
  - {predicate: contrastsWith, object: kt:lightning-app-builder}
  - {predicate: integratesWith, object: kt:screen-flow}
sources:
  - id: s1
    title: "Set Up a Community: Brand the Community (Trailhead project step)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/set-up-a-community/brand-the-community
    type: official-learning
    accessed: 2026-11-08
  - id: s2
    title: "Lightning Web Components Developer Guide: Configure a Component for Experience Builder"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/use-config-for-community-builder.html
    type: official-docs
    accessed: 2026-11-08
  - id: s3
    title: "LWR Sites for Experience Cloud: Create Components for LWR Sites"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/exp-cloud-lwr/guide/get-started-components.html
    type: official-docs
    accessed: 2026-11-08
  - id: s4
    title: "LWR Sites for Experience Cloud: Get Started"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.exp_cloud_lwr.meta/exp_cloud_lwr/get_started.htm
    type: official-docs
    accessed: 2026-11-08
  - id: s5
    title: "Lightning Aura Components Developer Guide: Configure Components for Experience Builder"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.lightning.meta/lightning/components_config_for_builder.htm
    type: official-docs
    accessed: 2026-11-08
  - id: s6
    title: "Experience Cloud Developer Guide: Before You Begin"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.communities_dev.meta/communities_dev/communities_dev_intro_before.htm
    type: official-docs
    accessed: 2026-11-08
created: 2026-11-08
---

# Experience Builder

Experience Builder is the point-and-click editor in which Experience Cloud sites are assembled. An admin opens it from the site's workspace menu, then works on a live canvas: the Page Structure view shows a page's regions (for example a content header, sidebar and content footer) and the components placed in each, and every component has its own property panel for labels, titles and behavior.[^s1] Sites built here start from an Experience Builder template or a Lightning Bolt solution, in an org with Digital Experiences enabled; Enterprise, Performance, Unlimited and Developer Editions and sandboxes all support building sites and components.[^s6]

## How it works

Branding lives in the Theme panel, where admins upload logos and header images and set the site's look, while the Settings area handles site-wide options such as featured topics.[^s1] A View Mode switch previews the page at desktop, tablet and phone widths, and the Preview button shows the published experience. Changes only reach visitors after **Publish**; activating the site, which also triggers member welcome emails, is a separate step in the Administration workspace.[^s1]

Templates fall into two runtimes. Aura-based templates host both Aura and Lightning web components, whereas LWR (Lightning Web Runtime) templates such as Build Your Own (LWR) and Microsite (LWR) are built entirely on Lightning web components, load fast and ship with only a few default pages, so you add the rest yourself.[^s4][^s6] The Aura guide notes that the LWC-based Marketing Website template cannot use Aura components at all.[^s5]

## Extending it with custom components

A Lightning web component appears in Experience Builder when its `js-meta.xml` sets `isExposed` to true and declares a target. `lightningCommunity__Page` puts it in the drag-and-drop Components panel; `lightningCommunity__Page_Layout` and `lightningCommunity__Theme_Layout` make it a page layout or theme layout for LWR sites; and `lightningCommunity__Default` carries the `targetConfigs` properties that admins edit in the property panel.[^s2][^s3] The LWR guide lists Integer, String, Boolean, Picklist and Color as the supported property types, and on enhanced LWR sites some properties can hold separate desktop, tablet and mobile values.[^s3] An optional SVG in the component folder supplies its icon.[^s2]

Aura components instead implement the `forceCommunity:availableForAllPageTypes` interface, are marked `access="global"` if they will be used outside the defining org, and include a design resource whose attributes become editable in the builder.[^s5]

## Limits and gotchas

- **Republish LWR sites after changes.** On LWR sites, after an org schema change or a component update you must publish again, or the site can break at runtime.[^s4]
- **Property changes can break placed components.** Once a component is used on a site or in a managed package, you cannot remove a property, add a new required property, make an existing property required, or tighten its `min`/`max`. For site-only components the workaround is to remove, change, redeploy and re-add it.[^s2]
- **Content Security Policy.** New sites default to strict CSP, so components that call third-party hosts need the security level adjusted and the hosts allowlisted.[^s2]
- **Guest user security.** Components on a site can bypass object and field-level security set on the guest user profile; Aura components with Apex controllers must enforce CRUD and FLS themselves, or rely on base components that use Lightning Data Service.[^s5]

## When to use it (and when not)

Use Experience Builder for any external-facing Experience Cloud site where admins should own layout and branding without deployments. Choose an LWR template when performance and a pure-LWC stack matter and your team can build missing pages and components; choose an Aura template when you need its larger set of default pages or existing Aura components.[^s4][^s5] Internal Lightning Experience record and app pages are edited in Lightning App Builder instead, which uses a parallel component-configuration model.[^s5]

## Connections

Experience Builder is the configuration surface of `kt:experience-cloud`, so it is modelled as part of that product. It depends on `kt:lightning-web-components` (the only component model for LWR sites) and still hosts `kt:aura-components` on Aura templates.[^s3][^s5] Its guest-user security guidance points to `kt:lightning-data-service` as the safe data path, and login and self-registration pages built here connect it to `kt:experience-cloud-identity`.[^s5] It contrasts with `kt:lightning-app-builder`, the internal-page editor whose design-resource setup it mirrors, and it can host `kt:screen-flow` components on site pages.[^s5][^s6]

## Sources
[^s1]: Trailhead, "Set Up a Community: Brand the Community". https://trailhead.salesforce.com/content/learn/projects/set-up-a-community/brand-the-community (accessed 2026-11-08)
[^s2]: Salesforce Developers, "Configure a Component for Experience Builder". https://developer.salesforce.com/docs/platform/lwc/guide/use-config-for-community-builder.html (accessed 2026-11-08)
[^s3]: Salesforce Developers, "Create Components for LWR Sites". https://developer.salesforce.com/docs/platform/exp-cloud-lwr/guide/get-started-components.html (accessed 2026-11-08)
[^s4]: Salesforce Developers, "LWR Sites for Experience Cloud: Get Started". https://developer.salesforce.com/docs/atlas.en-us.exp_cloud_lwr.meta/exp_cloud_lwr/get_started.htm (accessed 2026-11-08)
[^s5]: Salesforce Developers, "Configure Components for Experience Builder" (Aura). https://developer.salesforce.com/docs/atlas.en-us.264.0.lightning.meta/lightning/components_config_for_builder.htm (accessed 2026-11-08)
[^s6]: Salesforce Developers, "Experience Cloud Developer Guide: Before You Begin". https://developer.salesforce.com/docs/atlas.en-us.264.0.communities_dev.meta/communities_dev/communities_dev_intro_before.htm (accessed 2026-11-08)
