---
id: kt:content-security-policy
type: SecurityControl
title: Content Security Policy
aliases: [CSP, Lightning CSP, CSP Trusted Sites, Trusted URLs, CspTrustedSite]
domain: security-and-sharing
summary: >-
  The W3C browser standard, applied by Salesforce to Lightning pages, Experience Builder sites and opted-in Visualforce
  pages, that limits which origins a page may load scripts, styles, images, fonts, frames and connections from; admins
  widen it per host with Trusted URLs (formerly CSP Trusted Sites).
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:lightning-web-security, kt:lightning-locker, kt:experience-builder, kt:remote-site-settings, kt:visualforce]
relations:
  - {predicate: mitigates, object: kt:cross-site-scripting}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: contrastsWith, object: kt:remote-site-settings}
sources:
  - id: s1
    title: "Lightning Components Security Guide: Content Security Policy Overview"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lightning-components-security/guide/content-security-policy-intro.html
    type: official-docs
    accessed: 2026-11-14
  - id: s2
    title: "Lightning Web Components Developer Guide: Content Security Policy Overview"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/security-csp.html
    type: official-docs
    accessed: 2026-11-14
  - id: s3
    title: "Metadata API Developer Guide: CspTrustedSite"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_csptrustedsite.htm
    type: official-docs
    accessed: 2026-11-14
  - id: s4
    title: "Experience Cloud Developer Guide: Develop Secure Sites: CSP, LWS, and Lightning Locker"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/communities-dev/guide/communities-dev-security-locker-csp.html
    type: official-docs
    accessed: 2026-11-14
  - id: s5
    title: "Content Security Policy Level 3 (W3C Working Draft)"
    publisher: W3C Web Application Security Working Group
    url: https://www.w3.org/TR/CSP3/Overview.html
    type: standards-body
    accessed: 2026-11-14
created: 2026-11-14
---

# Content Security Policy

Content Security Policy (CSP) is a W3C specification that lets a site tell the browser which sources a page may fetch or execute resources from. It is delivered mainly as a `Content-Security-Policy` HTTP response header made of semicolon-separated directives such as `default-src`, `script-src`, `connect-src`, `frame-src`, `img-src` and `style-src`.[^s5] The specification positions CSP as defense in depth against content injection such as cross-site scripting (XSS): it limits the damage of an injection but does not replace input validation and output encoding.[^s5] CSP Level 3 is still a Working Draft on the W3C Recommendation track.[^s5]

## How Salesforce applies it

The Lightning Component framework sends CSP headers that the browser enforces for every component and library on a page, with the stated main goal of preventing XSS and other code injection.[^s1] By default `script-src` is `'self'`, so third-party JavaScript libraries must be uploaded to the org as static resources rather than loaded from a CDN.[^s1][^s2] The `font-src`, `img-src`, `media-src`, `frame-src`, `style-src` and `connect-src` directives are also `'self'`, so those resources must live in the org unless an admin trusts another host.[^s1]

Inline script is blocked: `unsafe-inline` is not allowed for `script-src`, so `<script>` tags cannot carry inline code and attributes like `onclick="doSomething()"` do not run.[^s2] External fonts, images, frames and CSS must be served over HTTPS, and a trusted host cannot be downgraded to HTTP.[^s1][^s2]

## Trusted URLs

To let components reach a third-party host, admins add a **Trusted URL**, which Salesforce previously called a CSP Trusted Site.[^s1] Under the hood each entry is a `CspTrustedSite` metadata component (available since API 39.0), deployable with Metadata API from a `cspTrustedSites` folder.[^s3] Each entry has an `endpointUrl` (domain, optional port, `*` wildcards such as `*.example.com`) and boolean flags that add the host to individual directives: `isApplicableToConnectSrc`, `FontSrc`, `FrameSrc`, `ImgSrc`, `MediaSrc` and `StyleSrc`.[^s3] A `context` value scopes the entry to all contexts, Lightning Experience only, Experience Builder sites only, Field Service mobile extensions, or custom Visualforce pages; Visualforce pages are only restricted when their `cspHeader` attribute is true.[^s3] Since API 59.0 an entry can also grant camera or microphone access through the Permissions-Policy header; in API 58.0 and earlier the entries held only CSP directives and were called CSP Trusted Sites.[^s3]

## Experience Builder sites

CSP rules in a site apply page-wide, including third-party components and custom code in head markup.[^s4] Experience Builder offers per-site script security levels: **Strict CSP** is the default for new sites and keeps Lightning Locker or LWS on, while **Relaxed CSP** is required before the Lightning Locker setting can be changed in the site.[^s4]

## Limits and gotchas

- Keep the generated CSP header under 12 KB; customers have reported problems as headers approach 16 KB, and intermediaries may add to it.[^s3]
- Since API 59.0 every Trusted URL needs at least one directive or permission flag set to true; older API versions silently defaulted flags (to img-src only in API 50.0–58.0).[^s3]
- Malformed URLs saved before February 2025 are excluded from generated headers, and placeholders like `{subdomain}` are invalid.[^s3]
- WebSocket endpoints must use `wss://`, third-party APIs `https://`, and Chrome extension URIs cannot use wildcards.[^s3]
- Not every browser enforces CSP; violations appear in the browser developer console and can be ignored if the app behaves correctly.[^s1]

## When to use it (and when not)

Add a Trusted URL when browser-side code (a Lightning component's `fetch`, an embedded iframe, a remote image or font) must load from an external origin, and scope it to the narrowest context and directives that work.[^s3] Prefer uploading scripts as static resources over trying to trust a script CDN, since `script-src` stays locked to the org.[^s1] CSP governs only what the browser fetches for the page, so server-side Apex callouts are outside its scope and need their own allowlisting.[^s5]

## Connections

CSP is a browser-enforced control that complements the component isolation of `kt:lightning-web-security` and its predecessor `kt:lightning-locker`; together they `mitigate` `kt:cross-site-scripting`.[^s1][^s4] `kt:experience-builder` exposes per-site CSP levels that interact with those settings.[^s4] Trusted URLs are deployed as metadata through `kt:metadata-api` and can scope rules to `kt:visualforce` pages.[^s3] The node `contrastsWith` `kt:remote-site-settings`, which allowlists server-side callouts, whereas CSP is enforced by the browser on what the page loads.[^s5]

## Sources
[^s1]: Salesforce Developers, "Lightning Components Security Guide: Content Security Policy Overview". https://developer.salesforce.com/docs/platform/lightning-components-security/guide/content-security-policy-intro.html (accessed 2026-11-14)
[^s2]: Salesforce Developers, "Lightning Web Components Developer Guide: Content Security Policy Overview". https://developer.salesforce.com/docs/platform/lwc/guide/security-csp.html (accessed 2026-11-14)
[^s3]: Salesforce Developers, "Metadata API Developer Guide: CspTrustedSite". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_csptrustedsite.htm (accessed 2026-11-14)
[^s4]: Salesforce Developers, "Experience Cloud Developer Guide: Develop Secure Sites: CSP, LWS, and Lightning Locker". https://developer.salesforce.com/docs/platform/communities-dev/guide/communities-dev-security-locker-csp.html (accessed 2026-11-14)
[^s5]: W3C, "Content Security Policy Level 3". https://www.w3.org/TR/CSP3/Overview.html (accessed 2026-11-14)
