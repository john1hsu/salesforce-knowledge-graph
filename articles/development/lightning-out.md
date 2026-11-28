---
id: kt:lightning-out
type: Feature
title: Lightning Out
aliases: [Lightning Out 2.0, Lightning Out (Beta), Lightning Out beta, lightning-out-application, Lightning Out 2.0 app]
domain: development
summary: >-
  Salesforce's mechanism for running Lightning components inside external, non-Salesforce web apps. Lightning Out 2.0
  (GA since Winter '26) embeds custom LWCs in isolated iframes on Lightning Web Runtime; the older Lightning Out (Beta)
  injects Aura-based apps directly into the host page.
release: "Winter '27"
status: current
broader: [kt:lightning-web-components]
related: [kt:aura-components, kt:lightning-locker]
relations:
  - {predicate: dependsOn, object: kt:lightning-web-security}
  - {predicate: dependsOn, object: kt:frontdoor-jsp-session-bridging}
  - {predicate: dependsOn, object: kt:content-security-policy}
  - {predicate: dependsOn, object: kt:lightning-web-runtime}
sources:
  - id: s1
    title: "Lightning Web Components Developer Guide: Understand Lightning Out 2.0 Architecture"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/lightning-out-architecture.html
    type: official-docs
    accessed: 2026-11-28
  - id: s2
    title: "Lightning Web Components Developer Guide: How Lightning Out 2.0 Compares to Lightning Out (Beta)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/lightning-out-compare.html
    type: official-docs
    accessed: 2026-11-28
  - id: s3
    title: "Lightning Web Components Developer Guide: Lightning Out 2.0 Limitations"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/lightning-out-limitations.html
    type: official-docs
    accessed: 2026-11-28
  - id: s4
    title: "Lightning Out 2.0 Is Now Generally Available in Winter '26"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2025/10/lightning-out-2-0-is-now-generally-available-in-winter-26
    type: official-blog
    accessed: 2026-11-28
  - id: s5
    title: "Lightning Web Components Developer Guide: Use Components Outside Salesforce with Lightning Out (Beta)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/lightning-out.html
    type: official-docs
    accessed: 2026-11-28
  - id: s6
    title: "Lightning Web Components Developer Guide: Lightning Out (Beta) Requirements"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/lightning-out-requirements.html
    type: official-docs
    accessed: 2026-11-28
created: 2026-11-28
---

# Lightning Out

Lightning Out lets a team reuse Salesforce UI components in a web application that Salesforce does not host, such as a portal, an intranet or a React, Angular or Vue front end. There are two generations. Lightning Out 2.0 became generally available in Winter '26 and is now the approach Salesforce recommends for running Lightning web components outside the platform.[^s4] The original Lightning Out (Beta) still exists but remains a Beta Service under the Beta Services Terms, and its documentation points readers to 2.0 instead.[^s5] Salesforce describes 2.0 as a complete replacement rather than an extension of the beta, so the two share a name but not an architecture.[^s2]

## How Lightning Out 2.0 works

An admin creates a Lightning Out 2.0 app in Setup, adds the custom LWCs it may expose, and copies the generated markup into the external page. The host page loads a JavaScript library from the org's My Domain and declares a `<lightning-out-application>` element. That element has no UI and is configured with three attributes: a `frontdoor-url` that starts the Salesforce session and must be set at runtime, the 18-digit `app-id` from the Lightning Out 2.0 App Manager (apps created before Spring '26 can omit it), and a comma-separated `components` list such as `c-my-component`.[^s1]

Each listed component appears on the host page as a mirror web component. Inside it sits an iframe that is the root of a closed shadow DOM, so host scripts can't read or change what is rendered, while the LWC itself executes in the Salesforce context.[^s1] Startup follows a fixed sequence. The host exchanges a valid access token or session ID for a frontdoor URL through the UI Bridge API (starting the OAuth authorization flow if the user isn't signed in), sets `frontdoor-url`, and the library establishes the session. The mirror components then create their iframes and render the LWCs.[^s1]

The host can follow progress through four custom events: `lo.application.ready`, `lo.application.error`, `lo.component.ready` and `lo.component.error`; the error events carry a message and the original error.[^s1] Under the hood, events crossing the iframe boundary are wrapped in `window.postMessage()`, yet developers still work with the standard EventTarget and CustomEvent APIs.[^s4] Properties set on a mirror element pass through only when the LWC exposes them; unsupported attributes fail silently rather than throwing.[^s1] Styling can cross the boundary through CSS custom properties and SLDS styling hooks configured in the app.[^s2]

## Lightning Out 2.0 vs. the beta

The comparison Salesforce publishes highlights these differences:[^s2]

- Runtime: 2.0 builds on Web Components standards and Lightning Web Runtime; the beta is a standalone Aura application.[^s2]
- Placement: 2.0 isolates each LWC in an iframe, with a CSP directive limiting which external apps may load it; the beta injects components straight into the host DOM.[^s2]
- Components: 2.0 embeds only custom LWCs; the beta also takes custom Aura components and some base components.[^s2]
- Security: 2.0 always applies Lightning Web Security and doesn't support Lightning Locker; the beta requires Locker and doesn't run with LWS.[^s2]
- Users and events: 2.0 serves authenticated users only and supports events; the beta allows guest access (with Digital Experiences enabled) but not events.[^s2]

The beta also shifts more work onto the team: you host the Aura app on your own origin server, register a connected app for it, add the server to the CORS allowlist, and handle authentication yourself.[^s5][^s6]

## Limits and gotchas

- Wrap standard components: only custom LWCs embed, so put a standard LWC inside a custom one, and expect it may not be fully styled; Aura isn't supported.[^s3]
- Cookies: users' browsers must allow third-party cookies, and the org must enable cross-domain session cookies.[^s3]
- Load the library from the host page, not from an LWC, because LWS blocks script insertion; navigation and `lightning/navigation` don't work.[^s3]
- No guest users and no client credentials flow, since that flow carries no user context.[^s3]

Unauthenticated access through Experience Cloud and Aura compatibility were described as post-GA roadmap items, not shipped features.[^s4]

## When to use it

Choose 2.0 for new work whenever the components are LWCs and every viewer has a Salesforce login; its iframe isolation avoids the CSS and script clashes the beta suffered on busy host pages.[^s4] Keep the beta only where you still need Aura components or guest users and can accept beta terms and Locker.[^s2][^s6] For OmniStudio components, Salesforce points to Omni Out rather than Lightning Out.[^s4]

## Connections

Lightning Out is a delivery channel for `kt:lightning-web-components`, its broader node. Version 2.0 `dependsOn` `kt:lightning-web-runtime` and `kt:lightning-web-security`, and on `kt:content-security-policy` to restrict which hosts may frame it.[^s2] Its session start relies on the frontdoor URL issued through the UI Bridge API, covered in `kt:frontdoor-jsp-session-bridging`.[^s1] The beta ties it to `kt:aura-components` and to `kt:lightning-locker`, which it requires.[^s2][^s6]

## Sources
[^s1]: Salesforce Developers, "Understand Lightning Out 2.0 Architecture". https://developer.salesforce.com/docs/platform/lwc/guide/lightning-out-architecture.html (accessed 2026-11-28)
[^s2]: Salesforce Developers, "How Lightning Out 2.0 Compares to Lightning Out (Beta)". https://developer.salesforce.com/docs/platform/lwc/guide/lightning-out-compare.html (accessed 2026-11-28)
[^s3]: Salesforce Developers, "Lightning Out 2.0 Limitations". https://developer.salesforce.com/docs/platform/lwc/guide/lightning-out-limitations.html (accessed 2026-11-28)
[^s4]: Salesforce Developers Blog, "Lightning Out 2.0 Is Now Generally Available in Winter '26". https://developer.salesforce.com/blogs/2025/10/lightning-out-2-0-is-now-generally-available-in-winter-26 (accessed 2026-11-28)
[^s5]: Salesforce Developers, "Use Components Outside Salesforce with Lightning Out (Beta)". https://developer.salesforce.com/docs/platform/lwc/guide/lightning-out.html (accessed 2026-11-28)
[^s6]: Salesforce Developers, "Lightning Out (Beta) Requirements". https://developer.salesforce.com/docs/platform/lwc/guide/lightning-out-requirements.html (accessed 2026-11-28)
