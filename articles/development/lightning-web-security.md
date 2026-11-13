---
id: kt:lightning-web-security
type: SecurityControl
title: Lightning Web Security
aliases: [LWS]
domain: development
summary: >-
  The current client-side security architecture for Lightning web components and Aura components, which isolates
  each namespace's JavaScript in its own virtualized sandbox and uses distortions of native APIs instead of secure wrappers.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:lightning-web-components, kt:aura-components]
relations:
  - {predicate: alternativeTo, object: kt:lightning-locker}
  - {predicate: configuredVia, object: kt:session-settings}
  - {predicate: mitigates, object: kt:cross-site-scripting}
  - {predicate: dependsOn, object: kt:content-security-policy}
sources:
  - id: s1
    title: "Lightning Components Security Guide: How Lightning Web Security Works"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lightning-components-security/guide/lws-architecture.html
    type: official-docs
    accessed: 2026-11-13
  - id: s2
    title: "Lightning Web Components Developer Guide: Lightning Web Security"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/security-lwsec-intro.html
    type: official-docs
    accessed: 2026-11-13
  - id: s3
    title: "Lightning Components Security Guide: Build Components to Work with Lightning Web Security"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lightning-components-security/guide/lws-build-components.html
    type: official-docs
    accessed: 2026-11-13
  - id: s4
    title: "Lightning Components Security Guide: Understand How LWS Architecture Affects Component Performance"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lightning-components-security/guide/lws-performance.html
    type: official-docs
    accessed: 2026-11-13
  - id: s5
    title: "Lightning Components Security Guide: Look Up Distortion Details in Lightning Web Security Distortion Viewer"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lightning-components-security/guide/lws-tools-distortion-viewer.html
    type: official-docs
    accessed: 2026-11-13
  - id: s6
    title: "Lightning Web Security Basics: Dig Deeper into Lightning Web Security"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lightning-web-security-basics/dig-deeper-into-lightning-web-security
    type: official-learning
    accessed: 2026-11-13
created: 2026-11-13
---

# Lightning Web Security

Lightning Web Security (LWS) is the security architecture that keeps Lightning components on the same page from interfering with each other or with platform code. A typical Lightning page mixes code from Salesforce, from the customer's own developers and from AppExchange packages, so isolating that code by namespace is the core job.[^s1] Salesforce describes LWS as modeled on current TC39 JavaScript standards and designed to let teams use third-party code without cross-site scripting (XSS) exposure.[^s2] It covers both Lightning web components and Aura components, is on by default in every org created in Winter '23 or later, and has been generally available for both component models since Summer '23.[^s2]

## How it works

LWS applies the industry approach of virtualization. The browser plays the host environment, LWS acts as the virtualization engine, and each namespace gets its own JavaScript sandbox as a virtual environment with limited, mediated access to host resources such as global objects, network access, cookies and local storage.[^s1][^s6] Code in one sandbox can't reach another sandbox's resources, so a malicious script is confined to the namespace it runs in.[^s1]

Cookies show the mechanism. A component in the `c` namespace that sets `foo=1` sees exactly that inside its sandbox, while LWS stores it in the host under a namespace-prefixed key, keeps the two in sync and hides the cookie from other namespaces. The prefix format is internal and can change, so code must never rely on it.[^s1]

Instead of handing code substitute objects, LWS applies **distortions**: targeted changes to the behavior of native JavaScript APIs inside a sandbox.[^s1][^s6] They fall into three categories:

- **Content filtering** limits `document.cookie`, `localStorage` and `sessionStorage` to the current sandbox's data.[^s1]
- **Sanitization** strips malicious code from values assigned to `innerHTML` and `outerHTML`.[^s1]
- **Property accessor modification** blocks reading or writing certain properties, such as `shadowRoot.mode`.[^s1]

The LWS Distortion Viewer, listed under Tools in the DX and LWC Developer Centers, documents each distorted API by object, with the vulnerability it addresses and the changed behavior; any API it doesn't list behaves natively.[^s5] Because each namespace is isolated rather than walled off, a component can still import components and modules from other namespaces, something that fails with a cross-namespace error when LWS is off.[^s2][^s6]

## Limits and gotchas

Most components written for Lightning Locker run under LWS without refactoring, but several patterns need attention.[^s2][^s3]

- **Third-party scripts.** Libraries that attach themselves to `window` or explicitly set `"use strict"` can break, and analytics scripts can't see code outside the sandboxes.[^s3]
- **Proxied data.** Objects passed between components are proxied and mutations don't propagate outside the sandbox; pass JSON strings or shallow clones instead.[^s3]
- **Blocked endpoints and globals.** LWS blocks URLs containing `/aura` or `/webruntime`, and Lightning web components can't use `$A`, `Aura`, `Sfdc` or `sforce`.[^s3]
- **Script, iframe and Blob handling.** Script tags become fetches evaluated in the sandbox, iframe content is reachable only when same-origin, and a Blob needs an explicit MIME type.[^s3]
- **Proxy overhead.** A few thousand proxies cost little, but tens of thousands become observable; building a `Set` from a 100,000-entry array is very noticeable.[^s4]
- **Host-owned data and DOM size.** Data from Apex or Lightning Data Service lives in the host, so every access crosses a proxy; clone it into the sandbox or process it server-side, and expect large DOMs to slow down sooner.[^s4]

For large collections, Salesforce recommends plain JavaScript objects over `Set`, `Map` and typed arrays, because those globals are host-owned and proxied.[^s4] Code already near its performance limits can get slower under LWS even if it was fine under Locker.[^s4] Setting changes can take 10 to 15 minutes to show up because of caching.[^s6]

## Connections

LWS is part of the `kt:salesforce-platform` UI runtime and secures both `kt:lightning-web-components` and `kt:aura-components`.[^s2] It is the newer `alternativeTo` `kt:lightning-locker`: it replaces secure wrappers with distortions and namespace sandboxes.[^s1] Admins turn it on through a checkbox in `kt:session-settings`.[^s6] Its stated purpose is to let pages run third-party code while it `mitigates` `kt:cross-site-scripting`, with sanitization of HTML assignments as one of the direct controls.[^s1][^s2] It works alongside the platform's `kt:content-security-policy` rules rather than replacing them; for example, it restricts iframe and object URLs to `http` and `https` schemes.[^s3]

## Sources

[^s1]: Salesforce Developers, "How Lightning Web Security Works" (Lightning Components Security Guide). https://developer.salesforce.com/docs/platform/lightning-components-security/guide/lws-architecture.html (accessed 2026-11-13)
[^s2]: Salesforce Developers, "Lightning Web Security" (Lightning Web Components Developer Guide). https://developer.salesforce.com/docs/platform/lwc/guide/security-lwsec-intro.html (accessed 2026-11-13)
[^s3]: Salesforce Developers, "Build Components to Work with Lightning Web Security" (Lightning Components Security Guide). https://developer.salesforce.com/docs/platform/lightning-components-security/guide/lws-build-components.html (accessed 2026-11-13)
[^s4]: Salesforce Developers, "Understand How LWS Architecture Affects Component Performance" (Lightning Components Security Guide). https://developer.salesforce.com/docs/platform/lightning-components-security/guide/lws-performance.html (accessed 2026-11-13)
[^s5]: Salesforce Developers, "Look Up Distortion Details in Lightning Web Security Distortion Viewer" (Lightning Components Security Guide). https://developer.salesforce.com/docs/platform/lightning-components-security/guide/lws-tools-distortion-viewer.html (accessed 2026-11-13)
[^s6]: Trailhead, "Dig Deeper into Lightning Web Security" (Lightning Web Security Basics). https://trailhead.salesforce.com/content/learn/modules/lightning-web-security-basics/dig-deeper-into-lightning-web-security (accessed 2026-11-13)
