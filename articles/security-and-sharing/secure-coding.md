---
id: kt:secure-coding
type: Concept
title: Secure Coding
aliases: [Secure Coding Guidelines, Salesforce Secure Coding Guide, secure development practices]
domain: security-and-sharing
summary: >-
  The practice of writing Apex, Visualforce, Lightning and integration code so it enforces the running user's
  access and resists common web attacks. Salesforce's Secure Coding Guidelines catalogue the issues it finds most
  often (injection, XSS, CSRF, broken access control, insecure secrets) and note where the platform already helps.
release: "Winter '27"
status: concept
broader: [kt:shared-responsibility-model, kt:salesforce-platform]
related: [kt:apex-user-mode, kt:apex-security-with-sharing, kt:appexchange-security-review]
relations:
  - {predicate: hasPart, object: kt:soql-injection}
  - {predicate: hasPart, object: kt:cross-site-scripting}
  - {predicate: mitigates, object: kt:data-breach-risk}
sources:
  - id: s1
    title: "Secure Coding Guidelines"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/secure-coding/guide/secure-coding-guidelines.html
    type: official-docs
    accessed: 2026-11-16
  - id: s2
    title: "Secure Server-Side Development: Write Secure Apex Controllers"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/secure-serverside-development/write-secure-apex-controllers
    type: official-learning
    accessed: 2026-11-16
  - id: s3
    title: "Secure Coding SQL Injection"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/secure-coding/guide/secure-coding-sql-injection.html
    type: official-docs
    accessed: 2026-11-16
  - id: s4
    title: "ISVforce Guide: Prevent Secure Coding Violations — Cross-Site Request Forgery"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/secure-code-violation-request-forgery.html
    type: official-docs
    accessed: 2026-11-16
  - id: s5
    title: "OWASP Secure Coding Practices - Quick Reference Guide: Overview"
    publisher: OWASP
    url: https://owasp.github.io/www-project-secure-coding-practices-quick-reference-guide/stable-en/03-appendices/03-overview.html
    type: community
    accessed: 2026-11-16
created: 2026-11-16
---

# Secure Coding

Secure coding is the discipline of writing software so that it preserves the confidentiality, integrity and availability of the data it handles, using technical controls that close off common classes of vulnerability.[^s5] OWASP stresses that developers design for what an application is supposed to do while attackers probe for what it can be made to do, so security requirements and abuse cases belong early in the lifecycle rather than after release.[^s5] On Salesforce, the platform secures the infrastructure and supplies safe defaults, but custom Apex, Visualforce, Lightning components and integrations are the customer's or partner's responsibility, and that code can undo platform protections if written carelessly.[^s1][^s2]

## Salesforce's Secure Coding Guidelines

Salesforce Developers publishes the Secure Coding Guidelines, a reference built from the security issues Salesforce most often finds when auditing applications built on or integrated with the platform.[^s1] It is deliberately a quick reference rather than a full treatment of web security, points readers to OWASP for depth, and flags where the platform already gives full or partial protection.[^s1] Its chapters cover flow design, session IDs, cross-site scripting, SQL (SOQL) injection, cross-site request forgery, secure communications, storing sensitive data, open redirects, clickjacking, authorization and access control, Lightning security, Marketing Cloud Engagement API integrations, PostMessage and WebSockets.[^s1]

## Core practices on the platform

**Enforce the user's access in Apex.** Apex runs in system mode by default, ignoring the running user's object permissions, field-level security and sharing, so code must opt in to enforcement.[^s2] Trailhead calls user mode the recommended way to avoid sharing, CRUD and FLS violations: `WITH USER_MODE` on SOQL, `as user` or `AccessLevel.USER_MODE` on DML and SOSL.[^s2] Older or more granular alternatives are `WITH SECURITY_ENFORCED` (which throws when a referenced field or object is inaccessible), Schema describe checks such as `isAccessible()` and `isUpdateable()`, and `Security.stripInaccessible`, which silently removes fields the user cannot see.[^s2]

**Declare sharing explicitly.** A class without a sharing keyword is insecure by default; use `with sharing` normally, `inherited sharing` for entry points such as controllers and REST services, and `without sharing` only where elevated access is intended.[^s2] The sharing setting of the class that defines a method applies, not the caller's.[^s2]

**Treat input as data, not code.** For queries, prefer static SOQL with bind variables, and validate dynamic object and field names against what exists and what the user may access.[^s3] Salesforce advises against relying on `String.escapeSingleQuotes()` alone, because it fails for unquoted input and does nothing about unauthorized access.[^s3] Even though SOQL is read-only, injection can still expose records and bypass CRUD and FLS checks.[^s3] Output encoding plays the same role in the browser against cross-site scripting.[^s1]

**Keep state changes behind user actions.** The platform protects form posts and user-triggered DML against CSRF, but logic that changes data when a page or component initialises bypasses that protection.[^s4] For Visualforce, set `confirmationTokenRequired` on pages that must change state on load; for Aura and LWC, move DML out of controller instantiation and into a user action such as a button click.[^s4]

## When it is enforced

Secure coding matters to every org with custom code, but ISV partners face formal enforcement: the ISVforce Guide files these issues under "Prevent Secure Coding Violations" within the security requirements for AppExchange and AgentExchange solutions.[^s4] Trailhead adds that `WITH SECURITY_ENFORCED` queries should use API version 48.0 or later for the security review.[^s2]

## Connections

Secure coding sits under the **shared responsibility model** because it is the customer- and partner-side half of protecting a **Salesforce Platform** org: Salesforce secures the service, while builders secure what they deploy.[^s1][^s5] It **has part** **SOQL injection** and **cross-site scripting**, two of the vulnerability classes the guidelines document in their own chapters.[^s1][^s3] **Apex user mode** and **Apex sharing keywords** are the main Apex mechanisms for honouring the running user's access.[^s2] The **AgentExchange (AppExchange) security review** is where partners' code is checked against these rules.[^s4] Practised consistently, secure coding **mitigates** data-breach risk by keeping code from exposing data that the user's permissions would otherwise hide.[^s2][^s3]

## Sources
[^s1]: Salesforce Developers, "Secure Coding Guidelines". https://developer.salesforce.com/docs/platform/secure-coding/guide/secure-coding-guidelines.html (accessed 2026-11-16)
[^s2]: Salesforce Trailhead, "Secure Server-Side Development: Write Secure Apex Controllers". https://trailhead.salesforce.com/content/learn/modules/secure-serverside-development/write-secure-apex-controllers (accessed 2026-11-16)
[^s3]: Salesforce Developers, "Secure Coding SQL Injection". https://developer.salesforce.com/docs/platform/secure-coding/guide/secure-coding-sql-injection.html (accessed 2026-11-16)
[^s4]: Salesforce Developers, "ISVforce Guide: Cross-Site Request Forgery". https://developer.salesforce.com/docs/platform/isvforce/guide/secure-code-violation-request-forgery.html (accessed 2026-11-16)
[^s5]: OWASP, "Secure Coding Practices - Quick Reference Guide: Overview". https://owasp.github.io/www-project-secure-coding-practices-quick-reference-guide/stable-en/03-appendices/03-overview.html (accessed 2026-11-16)
