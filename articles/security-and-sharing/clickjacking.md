---
id: kt:clickjacking
type: Concept
title: Clickjacking
aliases: [clickjacking attack, UI redress attack, iframe overlay attack, CSS overlay clickjacking]
domain: security-and-sharing
summary: >-
  A web attack in which a decoy page hides or overlays a trusted page, usually inside an invisible iframe, so the
  victim's clicks land on the trusted page's controls. On Salesforce it matters both for framed pages and for
  Lightning components whose CSS can float over other content.
release: "Winter '27"
status: concept
broader: [kt:secure-coding]
related: [kt:clickjack-protection, kt:content-security-policy, kt:lightning-web-components, kt:visualforce, kt:csrf-protection]
relations:
  - {predicate: contrastsWith, object: kt:cross-site-scripting}
  - {predicate: causes, object: kt:data-breach-risk}
sources:
  - id: s1
    title: "Understand Clickjacking (Secure Coding Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/secure-coding/guide/security-clickjacking.html
    type: official-docs
    accessed: 2026-11-28
  - id: s2
    title: "RFC 7034: HTTP Header Field X-Frame-Options"
    publisher: IETF
    url: https://www.rfc-editor.org/rfc/rfc7034.html
    type: standards-body
    accessed: 2026-11-28
  - id: s3
    title: "Clickjacking Defense Cheat Sheet"
    publisher: OWASP Cheat Sheet Series
    url: https://cheatsheetseries.owasp.org/cheatsheets/Clickjacking_Defense_Cheat_Sheet.html
    type: community
    accessed: 2026-11-28
  - id: s4
    title: "Clickjacking (Web Security attacks)"
    publisher: MDN Web Docs
    url: https://developer.mozilla.org/en-US/docs/Glossary/Clickjacking
    type: community
    accessed: 2026-11-28
  - id: s5
    title: "Mitigate clickjacking with XFO or CSP (Lighthouse)"
    publisher: Chrome for Developers
    url: https://developer.chrome.com/docs/lighthouse/best-practices/clickjacking-mitigation
    type: community
    accessed: 2026-11-28
created: 2026-11-28
---

# Clickjacking

**Clickjacking** is an attack in which the victim believes they are clicking something harmless while the click is actually delivered to a different, trusted page. Salesforce's Secure Coding Guide describes it as an invisible iframe or layer laid over visible secure content, and lists data intrusion, unauthorized emails and changed credentials among the possible results.[^s1] Browser vendors describe the same mechanism: the trusted site is embedded, in whole or in part, in a malicious page, usually through an `<iframe>`.[^s5]

## How the attack works

The classic form uses a decoy page that loads the target site in a frame, makes that frame transparent with CSS, and positions an enticing fake button exactly over a sensitive control on the target. MDN's worked example places a "free kitten" button above a bank's transfer button; the click reaches the real button, and because the browser sends the user's session cookies with the framed request, the action runs as the logged-in victim.[^s4] The attacker never reads the victim's data directly, which is why clickjacking is a UI deception attack rather than an injection flaw.[^s4][^s3]

Variants keep appearing. OWASP's cheat sheet singles out **DoubleClickjacking**, which abuses a second window during a double-click; frame-blocking headers do not stop it, so OWASP recommends server-side authorization for high-risk transactions.[^s3]

## The Salesforce angle: overlays from component CSS

Salesforce adds a platform-specific risk that needs no iframe at all. In Lightning Web Components and Aura, a reusable component's CSS can let it float over buttons, links or forms on pages it doesn't own; the guide files this under "CSS outside of component".[^s1] Its guidance for externally exposed or shared components is to avoid `position: absolute` and `position: fixed` unless the component stays inside its own namespace or appears only on pages that namespace owns, to keep styles inside the component's styling scope, and to leave positioning, z-index and overlays to app-level layout.[^s1] When reviewing components, the guide says to look for fixed or absolute positioning, very high z-index values, and large negative margins or padding offsets.[^s1]

For framing, the guide points administrators to Salesforce's clickjack protection settings, which secure a site by controlling whether browsers allow frames that point to its pages.[^s1]

## Defenses

Defenses fall into three independent families, and OWASP recommends layering more than one:[^s3]

- **Frame-blocking headers.** `X-Frame-Options` takes `DENY`, `SAMEORIGIN` or `ALLOW-FROM` with an origin; RFC 7034 (October 2013, Informational) defined it.[^s2] The CSP `frame-ancestors` directive is the finer-grained successor, and browsers that support it ignore `X-Frame-Options` when both are present.[^s4][^s3]
- **SameSite cookies.** Setting session cookies to `Lax` or `Strict` keeps them off cross-site framed requests, so the framed page loads logged out; MDN and OWASP both call this a partial mitigation.[^s4][^s3]
- **Frame-busting scripts.** OWASP no longer recommends the simple top-window check, because double framing, sandboxed frames and other tricks defeat it.[^s3]

Both headers must be sent as HTTP response headers on the document itself; declaring them in a `<meta>` tag has no effect.[^s2][^s5] RFC 7034 also warns that the header alone is not sufficient, since browsers do not check every ancestor in a chain of nested frames.[^s2] Chrome's Lighthouse audit passes a page only when `X-Frame-Options` is `DENY` or `SAMEORIGIN`, or `frame-ancestors` is set.[^s5]

## Gotchas

- `ALLOW-FROM` is obsolete, and OWASP warns that it fails open in browsers that don't support it, so allowlists belong in `frame-ancestors`.[^s3]
- Proxies can strip security headers, and per-page header configuration is easy to get wrong, which is why OWASP stresses layering defenses.[^s3]
- A component that passes header checks can still overlay other UI through CSS, so code review must cover both risks.[^s1]

## Connections

Clickjacking sits under `kt:secure-coding` as one of the browser-side threats Salesforce developers must design against.[^s1] It is the threat that `kt:clickjack-protection` controls, and it is enforced through the same `frame-ancestors` mechanism discussed under `kt:content-security-policy`.[^s1][^s3] The CSS overlay variant concerns `kt:lightning-web-components` (and Aura), while framed-page risk historically centres on `kt:visualforce` and other pages that can be embedded.[^s1] It **contrasts with** `kt:cross-site-scripting`: both hijack the user's session, but clickjacking tricks the user's clicks instead of running injected script.[^s4] It is often discussed alongside `kt:csrf-protection`, because SameSite cookies blunt both attacks, and a successful attack can **cause** `kt:data-breach-risk`.[^s3][^s1]

## Sources

[^s1]: Salesforce Developers, "Understand Clickjacking", Secure Coding Guide. https://developer.salesforce.com/docs/platform/secure-coding/guide/security-clickjacking.html (accessed 2026-11-28)
[^s2]: IETF, "RFC 7034: HTTP Header Field X-Frame-Options". https://www.rfc-editor.org/rfc/rfc7034.html (accessed 2026-11-28)
[^s3]: OWASP Cheat Sheet Series, "Clickjacking Defense Cheat Sheet". https://cheatsheetseries.owasp.org/cheatsheets/Clickjacking_Defense_Cheat_Sheet.html (accessed 2026-11-28)
[^s4]: MDN Web Docs, "Clickjacking". https://developer.mozilla.org/en-US/docs/Glossary/Clickjacking (accessed 2026-11-28)
[^s5]: Chrome for Developers, "Mitigate clickjacking with XFO or CSP". https://developer.chrome.com/docs/lighthouse/best-practices/clickjacking-mitigation (accessed 2026-11-28)
