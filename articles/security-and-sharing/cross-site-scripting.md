---
id: kt:cross-site-scripting
type: Concept
title: Cross-Site Scripting
aliases: [XSS, cross site scripting, stored XSS, reflected XSS, DOM-based XSS, script injection]
domain: security-and-sharing
summary: >-
  A web injection vulnerability in which untrusted data reaches a page in a form the browser executes as script,
  letting an attacker act with the viewing user's session. On Salesforce it arises mainly from unescaped Visualforce
  output and formulas and from manual DOM manipulation in Lightning components.
release: "Winter '27"
status: concept
broader: [kt:secure-coding]
related: [kt:visualforce, kt:lightning-web-components, kt:lightning-web-security, kt:content-security-policy, kt:soql-injection, kt:static-resources]
relations:
  - {predicate: causes, object: kt:data-breach-risk}
  - {predicate: contrastsWith, object: kt:soql-injection}
sources:
  - id: s1
    title: "Secure Client-Side Development: Mitigate Cross-Site Scripting"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/secure-clientside-development/mitigate-crosssite-scripting
    type: official-learning
    accessed: 2026-11-14
  - id: s2
    title: "Visualforce Developer Guide: Cross Site Scripting (XSS) — Unescaped Output and Formulas"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-pages-developers-guide/guide/pages-security-tips-scontrols.html
    type: official-docs
    accessed: 2026-11-14
  - id: s3
    title: "Lightning Components Security Guide: Lightning Web Security Sanitization"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lightning-components-security/guide/lws-sanitize.html
    type: official-docs
    accessed: 2026-11-14
  - id: s4
    title: "Security Anti-Patterns in Lightning Web Components"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2026/06/security-anti-patterns-in-lightning-web-components
    type: official-blog
    accessed: 2026-11-14
  - id: s5
    title: "Cross Site Scripting Prevention Cheat Sheet"
    publisher: OWASP Cheat Sheet Series
    url: https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
    type: community
    accessed: 2026-11-14
created: 2026-11-14
---

# Cross-Site Scripting

Cross-site scripting (XSS) is an injection flaw: an attacker gets JavaScript, or other active content such as HTML or VBScript, into a page that other people load, and the browser runs it as if the application had sent it.[^s1] Because that script executes with the victim's session, it can hijack the session, submit transactions the user never intended, log keystrokes, push fake download prompts or quietly exfiltrate data shown on the page.[^s1] OWASP frames the root cause as untrusted data being placed into a page where the browser interprets it as code rather than displaying it as text.[^s5]

## Types

Trailhead's secure client-side development module distinguishes three forms.[^s1]

- **Stored**: the payload is saved server-side (a record field, a post, a profile) and served to later viewers.[^s1]
- **Reflected**: the payload rides in a request, such as a crafted link or search box, and is echoed back in the response.[^s1]
- **DOM-based**: a client-side *source* such as `window.location.hash` flows into an executing *sink*; it is the hardest to spot and can slip past client-side sanitizers.[^s1]

## Where it appears on Salesforce

**Visualforce.** Standard components escape their output, but setting `escape="false"` on a component turns filtering off, so the developer must validate that output.[^s2] Formula expressions placed outside components are rendered on the server without escaping, and client-side script cannot repair that afterwards.[^s2] The classic example is writing a URL parameter such as `retURL` straight into a JavaScript string; wrapping the merge field in `JSENCODE` makes it safe for that context.[^s2] Salesforce also warns that data already inside the org is not trustworthy: a low-privilege user can plant script that runs when an administrator views the record, subverting the role hierarchy and audit trail.[^s2]

**Lightning Web Components.** LWC templates render data safely, so the main guidance is to let the framework own the DOM: use data binding and directives like `for:each` and `lwc:if` rather than building markup in JavaScript, and avoid `lwc:dom="manual"`, which hands DOM control back to the developer.[^s1][^s4] Setting `innerHTML` from user-supplied values is the typical mistake; for trusted rich text, use `lightning-formatted-rich-text`.[^s4] `eval()` and `Function()` still run inside the sandbox and become injection vectors when fed user input.[^s4] Some unsafe APIs, such as `document.write()` and `Element.setHTMLUnsafe()`, throw at runtime.[^s4]

## Defences

The primary control is context-aware output encoding: encode differently for HTML bodies, attributes, URLs, JavaScript and CSS, and prefer text-only sinks such as `textContent` over `innerHTML`.[^s5] Where users must author HTML, run it through a maintained sanitizer.[^s5] For input handling, Trailhead recommends output encoding over filtering, and allowlisting over blocklisting, because a complete blocklist is impossible to maintain.[^s1]

Platform layers add depth but are not substitutes. Lightning Web Security sanitizes HTML and SVG strings that components insert into the DOM via properties such as `innerHTML`, keeping only allowlisted elements and attributes, but it does not sanitize input text.[^s3] Salesforce's own developer blog cautions that this sanitization applies to shared page elements rather than inside a component's shadow DOM, so relying on it is fragile.[^s4] OWASP likewise treats Content Security Policy as an extra layer of defence, not the primary control.[^s5]

## Connections

XSS sits under **secure coding** as one of the core vulnerability classes, and it **causes** data-breach risk because the injected script reads whatever the victim can see.[^s1] It **contrasts with** SOQL injection: both come from treating untrusted input as code, but SOQL injection alters a server-side query while XSS executes in the victim's browser.[^s1] It is closely related to **Visualforce**, where escaping is on by default but easy to switch off, and to **Lightning Web Components**, whose template system is the main safeguard.[^s2][^s4] **Lightning Web Security** and **Content Security Policy** mitigate it as defence-in-depth layers.[^s3][^s5] **Static resources** matter because loading third-party libraries from an external CDN violates Salesforce's CSP, so libraries should be uploaded as static resources and loaded with `lightning/platformResourceLoader`.[^s4]

## Sources
[^s1]: Salesforce Trailhead, "Secure Client-Side Development: Mitigate Cross-Site Scripting". https://trailhead.salesforce.com/content/learn/modules/secure-clientside-development/mitigate-crosssite-scripting (accessed 2026-11-14)
[^s2]: Salesforce Developers, "Visualforce Developer Guide: Cross Site Scripting (XSS)". https://developer.salesforce.com/docs/platform/salesforce-pages-developers-guide/guide/pages-security-tips-scontrols.html (accessed 2026-11-14)
[^s3]: Salesforce Developers, "Lightning Web Security Sanitization". https://developer.salesforce.com/docs/platform/lightning-components-security/guide/lws-sanitize.html (accessed 2026-11-14)
[^s4]: Tim Dionne, "Security Anti-Patterns in Lightning Web Components", Salesforce Developers Blog, 2026-06-05. https://developer.salesforce.com/blogs/2026/06/security-anti-patterns-in-lightning-web-components (accessed 2026-11-14)
[^s5]: OWASP, "Cross Site Scripting Prevention Cheat Sheet". https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html (accessed 2026-11-14)
