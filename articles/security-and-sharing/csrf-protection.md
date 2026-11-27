---
id: kt:csrf-protection
type: SecurityControl
title: CSRF Protection
aliases: [cross-site request forgery protection, anti-CSRF token, XSRF protection, Salesforce CSRF defenses]
domain: security-and-sharing
summary: >-
  The platform and coding defenses that stop a forged request from riding a logged-in user's Salesforce session:
  an anti-CSRF token checked on standard controller form posts, plus the developer rule that state changes must
  happen only in response to explicit user actions, never on page load or component initialization.
release: "Winter '27"
status: current
broader: [kt:secure-coding]
related: [kt:clickjack-protection, kt:cross-site-scripting, kt:visualforce, kt:aura-components, kt:lightning-web-components, kt:session-settings]
relations:
  - {predicate: mitigates, object: kt:data-breach-risk}
  - {predicate: contrastsWith, object: kt:cross-site-scripting}
sources:
  - id: s1
    title: "Secure Coding Guide: Secure Coding Cross Site Request Forgery"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/secure-coding/guide/secure-coding-cross-site-req-forgery.html
    type: official-docs
    accessed: 2026-11-27
  - id: s2
    title: "Secure Coding Guide: Protect Your Application from CSRF Vulnerabilities"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/secure-coding/guide/security-protect-application-from-csrf-vulnerabilities.html
    type: official-docs
    accessed: 2026-11-27
  - id: s3
    title: "Apex Developer Guide: Cross-Site Request Forgery (CSRF)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/pages_security_tips_csrf.htm
    type: official-docs
    accessed: 2026-11-27
  - id: s4
    title: "Cross-Site Request Forgery Prevention Cheat Sheet"
    publisher: OWASP Cheat Sheet Series
    url: https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html
    type: community
    accessed: 2026-11-27
created: 2026-11-27
---

# CSRF Protection

Cross-site request forgery (CSRF) tricks a user who is already logged in into sending a request they never intended, so the attacker borrows that authenticated session to change records, alter settings or fire business logic.[^s1] Salesforce's Apex guide frames it less as a coding bug than as a missing defense: a page on another site only needs something like an image tag pointing at a Salesforce URL, and the browser sends the request with the victim's cookies attached.[^s3] CSRF protection is the combination of what the platform does automatically and what developers must do so that their own code doesn't reopen the hole.[^s1][^s2]

## How the platform protects

The Lightning Platform includes an anti-CSRF token: each page carries a random value in a hidden form field, and the platform checks it when the next request arrives.[^s3] This covers standard controllers and their methods, so insert, update, delete and upsert operations triggered by a user interaction, such as clicking a button or submitting a form, are protected without extra code.[^s2][^s3] The Secure Coding Guide states that components built with Apex and Visualforce get this protection automatically, and tells developers using other frameworks to confirm their own protection is switched on.[^s1]

## Where developers break it

The token only helps when something checks it. CSRF protection does not apply to state-changing logic that runs automatically while a page or component loads.[^s2]

- **Visualforce page load.** A method named in the `action` attribute of `<apex:page>`, or DML in a controller constructor, runs before the user does anything and bypasses the token check.[^s2][^s3]
- **The classic exploit.** An `init` action reads an `id` URL parameter and deletes that record; the token is never validated, so an attacker can supply any id.[^s3]
- **Aura and LWC initialization.** Calling an update from `doInit`, `connectedCallback`, `renderedCallback` or a constructor has the same flaw; lifecycle hooks should only read data.[^s2]
- **JavaScript-triggered actions.** Invoking `apex:actionFunction` methods from events such as `onload` turns a load into a write and should be avoided.[^s2]

The fix is structural: move the state change behind an explicit user action, for example an `<apex:commandButton>` inside `<apex:form>`, or a click handler in a Lightning component.[^s2] Where DML on page load can't be avoided, the guide points to enabling the "Require CSRF protection on GET requests" setting.[^s2] For a custom endpoint that the platform token doesn't cover, the Apex guide admits there is no built-in defense and suggests an intermediate confirmation page, a shorter idle session timeout, and training users to log out and avoid browsing other sites while signed in.[^s3] For calls to third-party APIs, Salesforce suggests sending a custom anti-CSRF token in a request header set with `setRequestHeader()`.[^s2]

## General principles

OWASP's guidance lines up with Salesforce's. Use the framework's built-in protection before writing your own, and never use GET requests for operations that change state.[^s4] The synchronizer token pattern, which Salesforce's hidden-field token follows, needs tokens that are secret, unpredictable and unique per session, kept out of URLs and logs.[^s4][^s3] SameSite cookie attributes and Fetch Metadata headers such as `Sec-Fetch-Site` are useful layers, but OWASP treats SameSite as defense in depth rather than a full defense.[^s4] It also warns that cross-site scripting can defeat every CSRF mitigation, since injected script runs same-origin and can read the token.[^s4]

## Gotchas

- With several Salesforce login pages open, users can hit an error saying the submitted page was invalid for their session; refreshing and retrying resolves it.[^s3]
- Code review should look past standard controllers: custom Visualforce pages, Lightning components, Apex endpoints and Flows are all in scope.[^s1]
- A confirmation page or short session timeout reduces risk but isn't a token check; prefer redesigning so writes only happen after a user's explicit action.[^s2][^s3]

## Connections

CSRF protection is a practice within `kt:secure-coding` and `mitigates` `kt:data-breach-risk`, since a forged request can modify or expose data under the victim's identity.[^s1] It `contrastsWith` `kt:cross-site-scripting`: XSS runs attacker script inside the page, while CSRF sends a request from outside it, and a working XSS defeats CSRF defenses.[^s4] It sits beside `kt:clickjack-protection` as a defense against actions the user didn't mean to take. Most of the developer rules concern `kt:visualforce`, `kt:aura-components` and `kt:lightning-web-components`, where page-load and lifecycle code can bypass the token.[^s2] It relates to `kt:session-settings` because a shorter idle session timeout is one of the fallback mitigations Salesforce suggests.[^s3]

## Sources
[^s1]: Salesforce Developers, "Secure Coding Guide: Secure Coding Cross Site Request Forgery". https://developer.salesforce.com/docs/platform/secure-coding/guide/secure-coding-cross-site-req-forgery.html (accessed 2026-11-27)
[^s2]: Salesforce Developers, "Secure Coding Guide: Protect Your Application from CSRF Vulnerabilities". https://developer.salesforce.com/docs/platform/secure-coding/guide/security-protect-application-from-csrf-vulnerabilities.html (accessed 2026-11-27)
[^s3]: Salesforce Developers, "Apex Developer Guide: Cross-Site Request Forgery (CSRF)", Winter '27 (API version 68.0). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/pages_security_tips_csrf.htm (accessed 2026-11-27)
[^s4]: OWASP, "Cross-Site Request Forgery Prevention Cheat Sheet". https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html (accessed 2026-11-27)
