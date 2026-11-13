---
id: kt:lightning-locker
type: SecurityControl
title: Lightning Locker
aliases: [Locker Service, LockerService, Lightning LockerService, Salesforce Locker]
domain: development
summary: >-
  The original client-side security architecture for Lightning components, which wraps JavaScript globals and DOM
  objects in secure wrappers so a component can only reach what it created; the predecessor to Lightning Web Security.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:aura-components, kt:lightning-web-components, kt:experience-cloud]
relations:
  - {predicate: alternativeTo, object: kt:lightning-web-security}
  - {predicate: configuredVia, object: kt:session-settings}
  - {predicate: dependsOn, object: kt:content-security-policy}
  - {predicate: consumedBy, object: kt:lightning-out}
sources:
  - id: s1
    title: "Lightning Components Security Guide: How Lightning Web Security Compares to Lightning Locker"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lightning-components-security/guide/get-started-compare-lws-locker.html
    type: official-docs
    accessed: 2026-11-13
  - id: s2
    title: "Lightning Aura Components Developer Guide (264.0): Get Started with Security for Lightning Components"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.lightning.meta/lightning/security_intro.htm
    type: official-docs
    accessed: 2026-11-13
  - id: s3
    title: "Lightning Components Security Guide: Disable Lightning Locker for an Aura Component"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lightning-components-security/guide/locker-disable.html
    type: official-docs
    accessed: 2026-11-13
  - id: s4
    title: "Lightning Components Security Guide: Enable Lightning Web Security in an Org"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lightning-components-security/guide/lws-enable.html
    type: official-docs
    accessed: 2026-11-13
  - id: s5
    title: "Lightning Components Security Guide: When to Enable Lightning Web Security"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lightning-components-security/guide/lws-when.html
    type: official-docs
    accessed: 2026-11-13
  - id: s6
    title: "Experience Cloud LWR Sites Developer Guide: Lightning Web Security in LWR Sites"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/exp-cloud-lwr/guide/template-differences-locker.html
    type: official-docs
    accessed: 2026-11-13
created: 2026-11-13
---

# Lightning Locker

Lightning Locker is the client-side security architecture that Salesforce first used to isolate custom Lightning components, both Aura components and Lightning web components, running on the same page. Salesforce now describes it as the predecessor to Lightning Web Security (LWS), which was introduced in Spring '22, and an org runs one of the two architectures for its Lightning components.[^s2] Whichever is active, components also run in JavaScript strict mode and under Content Security Policy (CSP) rules.[^s2]

## How it works

Locker's core technique is wrapping. Rather than handing component code the real browser objects, it substitutes more secure versions, so every interaction goes through a wrapper that blocks unsafe behavior.[^s1] The wrapped globals are `window`, `document` and `element` (for example `SecureWindow`), and the wrappers deliberately leave out some APIs.[^s1][^s3] The resulting rules are the ones developers run into day to day:

- **DOM containment.** A component can only reach DOM elements it created itself, and for LWC Locker preserves Shadow DOM encapsulation and stops code changing `shadowRoot` properties.[^s1]
- **Blocked or narrowed APIs.** Locker blocks `customElements` and access to iframe content, confines `eval()` to the global scope, and allows only a listed set of MIME types in `Blob` objects.[^s1]
- **Version pinning.** An org can be set to an earlier version of the Locker rules through its Locker API version setting, which has no effect when LWS is on.[^s1]

For Aura, enforcement is decided per component by its own API version. Components at API version 40.0 (Summer '17) or later run under Locker; a component pinned to 39.0 or earlier runs without it, regardless of the org's Locker API version setting.[^s3] Neither the extension hierarchy nor the containment hierarchy changes this: a 39.0 child inside a 40.0 parent still runs with Locker disabled, and it can't see a `window` property the parent added, because that property lives in the parent's wrapper.[^s3]

## Limits and gotchas

- **Third-party libraries break.** Libraries that depend on APIs the secure wrappers hide often fail under Locker.[^s1]
- **Array performance.** Locker filters arrays passed to child components, which can cause performance problems with large data sets.[^s1]
- **Disabling is Aura-only and fragile.** You can't turn Locker off for individual Lightning web components, and you can't pin an Aura component to 39.0 if it uses a base component with a later minimum version, such as `lightning:map` (44.0 or later).[^s3]
- **Mixed versions are hard to debug.** Salesforce recommends one API version for all custom components in an app or hierarchy, since mixing Locker-enabled and Locker-disabled components complicates troubleshooting.[^s3]
- **Lightning Out needs Locker.** Lightning Out requires Locker and isn't supported when LWS is enabled.[^s1]

## When to use it (and when not)

New orgs have LWS enabled by default, and orgs created from a template inherit the template's setting, so Locker mainly survives in older orgs that never switched.[^s4][^s5] Admins move an org to LWS by selecting "Use Lightning Web Security for Lightning web components and Aura components" in Session Settings and then clearing the browser cache; the same checkbox covers both component models.[^s4] Salesforce strongly recommends enabling LWS in a sandbox staging environment first, especially for orgs with packaged components or Experience Cloud sites, and an org that hits problems can go back to Locker by deselecting the setting.[^s5] Compared with Locker, LWS runs each namespace in its own sandbox with direct access to globals, permits cross-namespace imports, custom elements and iframe access, and is faster because it has no wrappers.[^s1] The main reason to stay on Locker is a dependency on Lightning Out.[^s1] Once LWS is on, an Aura component's API version no longer affects enforcement.[^s3]

## Connections

Lightning Locker is part of the `kt:salesforce-platform` UI runtime and sandboxes both `kt:aura-components` and `kt:lightning-web-components`.[^s2] It is the older `alternativeTo` `kt:lightning-web-security`, and the choice between them is `configuredVia` `kt:session-settings`.[^s4] Both architectures sit on top of `kt:content-security-policy`, which still applies whichever one is active.[^s2] `kt:lightning-out` consumes Locker, since it can't run under LWS.[^s1] In `kt:experience-cloud`, LWR sites always use their own LWS instance instead of Locker, controlled by a site-level setting in Experience Builder rather than the org's Session Settings.[^s6]

## Sources

[^s1]: Salesforce Developers, "How Lightning Web Security Compares to Lightning Locker" (Lightning Components Security Guide). https://developer.salesforce.com/docs/platform/lightning-components-security/guide/get-started-compare-lws-locker.html (accessed 2026-11-13)
[^s2]: Salesforce Developers, "Get Started with Security for Lightning Components" (Aura Components Developer Guide 264.0). https://developer.salesforce.com/docs/atlas.en-us.264.0.lightning.meta/lightning/security_intro.htm (accessed 2026-11-13)
[^s3]: Salesforce Developers, "Disable Lightning Locker for an Aura Component" (Lightning Components Security Guide). https://developer.salesforce.com/docs/platform/lightning-components-security/guide/locker-disable.html (accessed 2026-11-13)
[^s4]: Salesforce Developers, "Enable Lightning Web Security in an Org" (Lightning Components Security Guide). https://developer.salesforce.com/docs/platform/lightning-components-security/guide/lws-enable.html (accessed 2026-11-13)
[^s5]: Salesforce Developers, "When to Enable Lightning Web Security" (Lightning Components Security Guide). https://developer.salesforce.com/docs/platform/lightning-components-security/guide/lws-when.html (accessed 2026-11-13)
[^s6]: Salesforce Developers, "Lightning Web Security in LWR Sites" (Experience Cloud LWR Sites Developer Guide). https://developer.salesforce.com/docs/platform/exp-cloud-lwr/guide/template-differences-locker.html (accessed 2026-11-13)
