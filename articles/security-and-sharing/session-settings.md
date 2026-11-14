---
id: kt:session-settings
type: SecurityControl
title: Session Settings
aliases: [Session Settings page, session security settings, org-wide session settings, SessionSettings metadata]
domain: security-and-sharing
summary: >-
  The org-wide Setup page (stored as the sessionSettings part of SecuritySettings metadata) that controls how
  Salesforce UI sessions time out, are bound to IP and domain, protect cookies and caching, enforce browser security
  policies such as Stricter CSP and Lightning Web Security, and map login methods to session security levels.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity]
related: [kt:profiles, kt:login-ip-ranges-and-trusted-ip-ranges, kt:security-health-check, kt:experience-cloud]
relations:
  - {predicate: hasPart, object: kt:session-security-levels}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: mitigates, object: kt:account-takeover}
  - {predicate: integratesWith, object: kt:content-security-policy}
sources:
  - id: s1
    title: "Modify Session Security Settings"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.admin_sessions.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-14
  - id: s2
    title: "Edit Session Settings in Profiles"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=platform.users_profiles_session.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-14
  - id: s3
    title: "Metadata API Developer Guide: SecuritySettings"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_securitysettings.htm
    type: official-docs
    accessed: 2026-11-14
  - id: s4
    title: "Secure Your Salesforce Configuration: Enhance Salesforce Org Security"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/secure-salesforce-configuration/run-health-check
    type: official-learning
    accessed: 2026-11-14
created: 2026-11-14
---

# Session Settings

Session Settings is the Setup page where an admin decides how every browser session in the org behaves after login: how long it may sit idle, what it is bound to, which cookie and caching protections apply, and which browser-side security architecture runs on Lightning pages.[^s1] It is reached from Setup by searching for Session Settings, requires the Customize Application permission, and works in both Lightning Experience and Salesforce Classic.[^s1] In source-driven development the same values live in the `sessionSettings` element of the `Security.settings` file, part of the SecuritySettings metadata type.[^s3]

## How it works

The page groups its options into sections, and each one targets a different stage of a session's life.[^s1]

- **Timeout**: an inactivity limit, an optional warning popup 30 seconds before expiry, and an option to force a logout to the login page.[^s1]
- **Session binding**: lock sessions to the originating IP address or to the domain where they were first used, and end all of a user's sessions when an admin resets their password.[^s1]
- **Secure connections**: HttpOnly session cookies, POST for cross-domain session exchange, forced re-login after Login-As, and checking login IP ranges on every request rather than only at login.[^s1]
- **Caching**: login-page autocomplete, secure persistent browser caching, the user switcher, and a CDN for Lightning framework files.[^s1]
- **Browser security**: Stricter Content Security Policy, the Lightning Locker API version, the switch to Lightning Web Security, referrer policy and external-redirect blocking.[^s1]
- **Session security levels**: which login methods produce a Standard versus a High Assurance session, with MFA High Assurance by default.[^s1]

Profiles can override part of this. A profile's own timeout and its required session level at login take precedence over the org-wide values; profiles without those settings inherit the org defaults.[^s2] Customer and partner profiles add options such as device activation, and most community licenses cap sessions at 24 hours while External Identity licenses can go up to 7 days.[^s2]

## Limits and gotchas

The timeout picklist runs from 15 minutes to 24 hours; the metadata enumeration lists FifteenMinutes through TwentyFourHours, with NinetyMinutes added in API 58.0.[^s3] Salesforce records last activity only every 5 minutes, so a session can outlive the configured value, and sessions that use JWT-based access tokens ignore this setting; their timeout belongs to the connected app or external client app policy instead.[^s1]

Several hardening options break things. IP locking can disrupt some apps and mobile devices, HttpOnly breaks custom code that reads the session cookie from JavaScript, and POST-based cross-domain sessions can stop embedded images from loading.[^s1] Turning off secure browser caching slows Lightning Experience considerably, so the docs reserve that for strict policies or development orgs.[^s1] Stricter CSP should stay on because Lightning Locker and Lightning Web Security rely on it.[^s1] Demoting MFA to a Standard session level can lock out users whose profile requires High Assurance at login.[^s1] A change to the new-user link expiry (1, 7 or 180 days) also applies to welcome emails already sent.[^s1]

## When to use it (and when not)

Use Session Settings for org-wide defaults, and profile session settings when one population needs a shorter timeout or High Assurance at login.[^s2] Health Check scores the org against Salesforce's baseline and lets admins fix weak values in one click, and its recommendations include HttpOnly, HTTPS, clickjack protection and a short timeout for sensitive data.[^s4] Deploy the settings as metadata so sandboxes and production stay aligned rather than drifting through manual Setup edits.[^s3]

## Connections

The node is part of the session-management side of `kt:salesforce-identity`, and it `hasPart` `kt:session-security-levels`, whose login-method mapping lives on this page.[^s1] `kt:profiles` override its timeout and login session level, while `kt:login-ip-ranges-and-trusted-ip-ranges` interact with its "enforce on every request" option.[^s1][^s2] It `integratesWith` `kt:content-security-policy` through the Stricter CSP setting and is where admins choose between `kt:lightning-locker` and `kt:lightning-web-security`.[^s1] Its password-reset session termination and IP locking `mitigate` `kt:account-takeover`, and `kt:experience-cloud` sites inherit its domain-locking and employee-login options.[^s1] It is `configuredVia` `kt:metadata-api` as SecuritySettings, and `kt:security-health-check` audits it.[^s3][^s4]

## Sources
[^s1]: Salesforce Help, "Modify Session Security Settings". https://help.salesforce.com/s/articleView?id=sf.admin_sessions.htm&language=en_US&type=5 (accessed 2026-11-14)
[^s2]: Salesforce Help, "Edit Session Settings in Profiles". https://help.salesforce.com/s/articleView?id=platform.users_profiles_session.htm&language=en_US&type=5 (accessed 2026-11-14)
[^s3]: Salesforce Developers, "Metadata API Developer Guide: SecuritySettings". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_securitysettings.htm (accessed 2026-11-14)
[^s4]: Trailhead, "Secure Your Salesforce Configuration: Enhance Salesforce Org Security". https://trailhead.salesforce.com/content/learn/modules/secure-salesforce-configuration/run-health-check (accessed 2026-11-14)
