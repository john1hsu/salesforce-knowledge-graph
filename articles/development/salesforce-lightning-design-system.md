---
id: kt:salesforce-lightning-design-system
type: Tool
title: Salesforce Lightning Design System
aliases: [SLDS, SLDS 1, SLDS 2, Lightning Design System, Salesforce Cosmos theme]
domain: development
summary: >-
  Salesforce's CSS framework and design system that gives Lightning Experience its look and feel; SLDS 2,
  introduced in Spring '25, separates structure from visual design through global styling hooks and ships
  the Salesforce Cosmos theme.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:lightning-web-components, kt:aura-components, kt:section-508-accessibility, kt:static-resources, kt:slds-linter]
relations:
  - {predicate: consumedBy, object: kt:lightning-web-components}
  - {predicate: consumedBy, object: kt:aura-components}
  - {predicate: consumedBy, object: kt:visualforce}
  - {predicate: contrastsWith, object: kt:lightning-locker}
sources:
  - id: s1
    title: "LWC Developer Guide: Style Components with Lightning Design System"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/create-components-css-slds.html
    type: official-docs
    accessed: 2026-11-22
  - id: s2
    title: "LWC Developer Guide: Compare Salesforce Lightning Design System Versions"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/create-components-css-slds1-slds2.html
    type: official-docs
    accessed: 2026-11-22
  - id: s3
    title: "LWC Developer Guide: Style Components Using Lightning Design System Styling Hooks"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/create-components-css-custom-properties
    type: official-docs
    accessed: 2026-11-22
  - id: s4
    title: "Trailhead: Explore Salesforce Lightning Design System 2"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-lightning-design-system-2-for-developers/explore-salesforce-lightning-design-system-2
    type: official-learning
    accessed: 2026-11-22
created: 2026-11-22
---

# Salesforce Lightning Design System

The Salesforce Lightning Design System (SLDS) is the CSS framework behind the look and feel of Lightning Experience, covering styles, themes, branding and customization.[^s1] It publishes component blueprints: framework-agnostic HTML and CSS with no logic. Salesforce built the `lightning` namespace base components, such as `lightning-button`, `lightning-card` and `lightning-tree`, from those blueprints.[^s1] Custom components that run in Lightning Experience or the Salesforce mobile app can use SLDS classes without import statements or static resources.[^s1]

## SLDS 1 and SLDS 2

Salesforce introduced SLDS 2 in Spring '25, and the original framework is now called SLDS 1.[^s2] SLDS 2 is built on a new CSS framework that separates structure from visual design. Styling hooks, which are CSS custom properties, carry the visual design.[^s2] Trailhead calls it the latest design system for Lightning Platform products. Its main parts are the Lightning components, a semantic styling hook framework, the built-in Salesforce Cosmos theme, and tooling such as SLDS Linter and SLDS Validator.[^s4]

The main differences between the versions:[^s2]

- Default theme: SLDS 1 uses Lightning Blue; SLDS 2 uses Salesforce Cosmos, which an org opts in to by choosing that theme.[^s2]
- Documentation: SLDS 2 lives on lightningdesignsystem.com, while SLDS 1 moved to v1.lightningdesignsystem.com.[^s1]
- Design tokens: supported in SLDS 1 themes, but not supported in SLDS 2 themes or documented on the new site.[^s2]
- Global styling hooks: SLDS 2 adds semantic UI color hooks and recommends them over the original global color hooks.[^s2]
- Component styling hooks: SLDS 1 only; components that rely on `--slds-c-*` hooks should stay on SLDS 1 for now.[^s2]

Cosmos brings circular motifs, refreshed colors and improved typography, plus density controls and user personalization preferences.[^s4]

## How styling hooks work

A styling hook is a placeholder in the SLDS stylesheet that a component can set, for example `var(--slds-c-badge--color-background, #ecebea)`.[^s3] Hooks prefixed `--slds-c-` change one component, such as `--slds-c-button-brand-color-background`. Hooks prefixed `--slds-g-` are global and apply across the app.[^s3] In SLDS 2, global hook names follow a pattern of namespace, scope, category, property, pairing, role, attribute, state and range. Only the namespace, scope, category and range are required, and `--slds` is the official namespace.[^s4] To refactor a hard-coded value, replace it with a hook and keep the original value as the fallback, as in `var(--slds-g-radius-border-4, 1rem)`.[^s4] Salesforce also recommends an SLDS 1 fallback inside each SLDS 2 hook, such as `var(--slds-g-spacing-4, var(--lwc-spacingMedium, 1rem))`.[^s1]

## Limits and gotchas

- Salesforce doesn't support overriding base component styling except through documented styling hooks.[^s1]
- Don't target SLDS classes such as `.slds-button` or `.slds-input` in your own CSS. SLDS classes and base component internals can change in future releases.[^s3]
- Avoid overloaded selectors and `!important`; create your own classes and set global hooks instead.[^s1]
- Component styling hooks are available only in SLDS 1 as of Summer '25, and SLDS 2 doesn't support them yet.[^s3]
- Some components ignore styling hooks. `lightning/platformShowToastEvent` ignores toast hooks, though `lightning/toast` supports them, and `lightning-helptext` ignores tooltip hooks.[^s3]
- Link styling and form elements such as `lightning-input` and `lightning-textarea` don't support styling through custom properties.[^s3]
- When you set colors with global hooks, align them with WCAG 2.1 contrast guidance for text and non-text elements.[^s3]

## When to use it (and when not)

Base components already implement SLDS, so they are the preferred starting point. Use custom markup with SLDS utility classes, such as `slds-m-left_medium`, only when no base component fits.[^s1][^s4] Before you move an org to Cosmos, run SLDS Linter or SLDS Validator. They find design tokens and replace them with global styling hooks.[^s2] Salesforce recommends SLDS Linter, the newer tool, which can apply fixes in bulk. SLDS Validator still covers both versions in VS Code through the Salesforce Extension Pack.[^s1][^s4] Teams with heavy component-hook customizations should weigh staying on SLDS 1 until SLDS 2 supports component hooks.[^s2]

## Connections

SLDS is a styling layer consumed by Lightning Web Components (`kt:lightning-web-components`) and by Aura components (`kt:aura-components`). Custom components in Lightning Experience get SLDS without imports or static resources (`kt:static-resources`).[^s1] Visualforce (`kt:visualforce`) is the older UI framework that also consumes SLDS styling. Hooks are kept as fallbacks so code works under both versions, so one component library can serve SLDS 1 and SLDS 2 orgs during a migration.[^s1] SLDS's WCAG 2.1 contrast guidance supports accessibility obligations such as Section 508 (`kt:section-508-accessibility`).[^s3] It is often confused with Lightning Locker (`kt:lightning-locker`), which is a security boundary rather than a styling layer. With SLDS, the rule is to depend only on documented hooks and never on base component internals.[^s3] SLDS Linter (`kt:slds-linter`) is the migration tool Salesforce recommends for SLDS 2.[^s4]

## Sources
[^s1]: Salesforce Developers, "Style Components with Lightning Design System". https://developer.salesforce.com/docs/platform/lwc/guide/create-components-css-slds.html (accessed 2026-11-22)
[^s2]: Salesforce Developers, "Compare Salesforce Lightning Design System Versions". https://developer.salesforce.com/docs/platform/lwc/guide/create-components-css-slds1-slds2.html (accessed 2026-11-22)
[^s3]: Salesforce Developers, "Style Components Using Lightning Design System Styling Hooks". https://developer.salesforce.com/docs/platform/lwc/guide/create-components-css-custom-properties (accessed 2026-11-22)
[^s4]: Trailhead, "Explore Salesforce Lightning Design System 2". https://trailhead.salesforce.com/content/learn/modules/salesforce-lightning-design-system-2-for-developers/explore-salesforce-lightning-design-system-2 (accessed 2026-11-22)
