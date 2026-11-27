---
id: kt:clickjack-protection
type: SecurityControl
title: Clickjack Protection
aliases: [clickjacking protection, Visualforce clickjack protection, Trusted Domains for Inline Frames, IframeWhiteListUrl]
domain: security-and-sharing
summary: >-
  Salesforce's framing controls that stop its pages from being loaded in iframes on untrusted sites, set in Session
  Settings (plus per-site settings for Experience Cloud and Site.com) and relaxed per domain through Trusted Domains
  for Inline Frames, enforced in the browser with Content-Security-Policy frame-ancestors headers.
release: "Winter '27"
status: current
broader: [kt:session-settings, kt:secure-coding]
related: [kt:visualforce, kt:experience-cloud, kt:csrf-protection, kt:my-domain]
relations:
  - {predicate: mitigates, object: kt:clickjacking}
  - {predicate: integratesWith, object: kt:content-security-policy}
  - {predicate: configuredVia, object: kt:metadata-api}
sources:
  - id: s1
    title: "Visualforce Developer Guide: Put Visualforce Pages on External Domains"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-pages-developers-guide/guide/pages-quick-start-external-iframe.html
    type: official-docs
    accessed: 2026-11-27
  - id: s2
    title: "Secure Coding Guide: Platform Security FAQs"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/secure-coding/guide/secure-coding-platform-securityfaqs.html
    type: official-docs
    accessed: 2026-11-27
  - id: s3
    title: "Object Reference for the Salesforce Platform: IframeWhiteListUrl"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_iframewhitelisturl.htm
    type: official-docs
    accessed: 2026-11-27
  - id: s4
    title: "Clickjacking Defense Cheat Sheet"
    publisher: OWASP Cheat Sheet Series
    url: https://cheatsheetseries.owasp.org/cheatsheets/Clickjacking_Defense_Cheat_Sheet.html
    type: standards-body
    accessed: 2026-11-27
created: 2026-11-27
---

# Clickjack Protection

Clickjacking, also called a UI redress attack, hides or disguises a legitimate page inside a frame on an attacker's site so that the victim clicks something they never meant to click.[^s4] In Salesforce terms, that stray click sends a real HTTP request in the user's session, which can expose data, send email or change credentials.[^s2] Clickjack protection is the set of platform settings that decide which sites, if any, may load Salesforce pages in an inline frame (iframe).[^s2]

## How it works

Most Salesforce-served pages can be framed only by a page on the same domain.[^s2] The platform enforces this with the `frame-ancestors` directive of the Content-Security-Policy response header, which tells the browser which origins may embed the page; Salesforce describes that directive as the replacement for the obsolete `X-Frame-Options` header.[^s2] OWASP's guidance agrees: under the CSP specification an enforced `frame-ancestors` policy causes browsers to ignore `X-Frame-Options`, whose `ALLOW-FROM` value no longer works in modern browsers.[^s4]

Visualforce is the main exception. By default Visualforce pages can be framed, and pages that set their own headers omit `frame-ancestors`, so Salesforce strongly recommends turning clickjack protection on for them.[^s2] In Setup, the **Clickjack Protection** section of Session Settings has separate checkboxes for customer Visualforce pages with headers disabled and with standard headers; the Visualforce guide says to select both.[^s1] The same switches exist in the `SecuritySettings` Metadata API type as `enableClickjackNonsetupUser` and `enableClickjackNonsetupUserHeaderless`.[^s3]

## Allowing trusted framers

When a page legitimately has to appear inside another site, keep protection on and list the framing domains under **Trusted Domains for Inline Frames**, choosing the iframe type (for example Visualforce Pages).[^s1] Salesforce then sends `X-Frame-Options` and Content-Security-Policy headers that permit those domains.[^s1] Each entry is an `IframeWhiteListUrl` record, available since API version 45.0, that covers Embedded Service, Surveys and Visualforce content.[^s3] Its `Context` picklist accepts `VisualforcePages`, `Surveys` and `DisclosureAndComplianceHubConnector`, and its `Url` field takes forms such as `example.com`, `*example.com` or `https://example.com`.[^s3]

Experience Cloud sites carry two more framing settings, one on the Salesforce site detail page and one in the Site.com configuration; Salesforce recommends setting both to the same value.[^s2]

## Limits and gotchas

- Session Settings accepts up to 512 trusted external framing domains.[^s1]
- Every trusted domain lengthens the CSP header: keep it under 12 KB, as problems have been reported near 16 KB.[^s1]
- Authenticated pages need the session cookie, which browsers block in third-party frames; serve them from a subdomain or the same domain as the framer.[^s1]
- If no custom domain works, Lightning Out (beta) with token authentication is the fallback; otherwise open the page in a new tab.[^s1]
- Framing headers must be real HTTP response headers; meta-tag versions of `X-Frame-Options` and `frame-ancestors` are ignored.[^s4]
- Frame headers do not stop DoubleClickjacking, which uses a top-level window; protect risky actions with server-side authorization.[^s4]

## When to use it (and when not)

Leave protection on for every page type and add the narrowest trusted domains when a partner portal or intranet must embed content.[^s1] OWASP recommends refusing all framing unless a page needs it, and treating `SameSite` cookies and frame-busting scripts as extra layers, not substitutes.[^s4] Turning protection off to fix an embedding problem trades a configuration fix for an open clickjacking path.[^s2]

## Connections

Clickjack protection lives inside `kt:session-settings` and is one practice in `kt:secure-coding`; it `mitigates` `kt:clickjacking`.[^s2] It `integratesWith` `kt:content-security-policy`, since both trusted framers and Trusted URLs end up in the CSP header and share its size budget.[^s1] It matters most for `kt:visualforce`, which is frameable by default, and for `kt:experience-cloud` sites with their own framing settings.[^s2] The settings are `configuredVia` `kt:metadata-api` through `SecuritySettings`.[^s3] Authenticated framing works best on a custom domain, which links it to `kt:my-domain`.[^s1] It sits beside `kt:csrf-protection` as a defense against requests the user did not intend.[^s2]

## Sources
[^s1]: Salesforce Developers, "Visualforce Developer Guide: Put Visualforce Pages on External Domains". https://developer.salesforce.com/docs/platform/salesforce-pages-developers-guide/guide/pages-quick-start-external-iframe.html (accessed 2026-11-27)
[^s2]: Salesforce Developers, "Secure Coding Guide: Platform Security FAQs". https://developer.salesforce.com/docs/platform/secure-coding/guide/secure-coding-platform-securityfaqs.html (accessed 2026-11-27)
[^s3]: Salesforce Developers, "Object Reference for the Salesforce Platform: IframeWhiteListUrl". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_iframewhitelisturl.htm (accessed 2026-11-27)
[^s4]: OWASP, "Clickjacking Defense Cheat Sheet". https://cheatsheetseries.owasp.org/cheatsheets/Clickjacking_Defense_Cheat_Sheet.html (accessed 2026-11-27)
