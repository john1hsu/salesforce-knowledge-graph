---
id: kt:login-history
type: SecurityControl
title: Login History
aliases: [LoginHistory object, LoginHistory, Login History page, Monitor Login History, user login history]
domain: identity
summary: >-
  Salesforce's built-in record of login attempts to an org and its Experience Cloud sites, shown on the Setup
  Login History page and exposed through the LoginHistory object, with six months of data available to view
  or download without an add-on licence.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity]
related: [kt:login-ip-ranges-and-trusted-ip-ranges, kt:multi-factor-authentication, kt:account-takeover, kt:oauth-2-flows-in-salesforce]
relations:
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: instanceOf, object: kt:standard-objects}
  - {predicate: alternativeTo, object: kt:event-monitoring}
  - {predicate: contrastsWith, object: kt:field-audit-trail}
  - {predicate: mitigates, object: kt:account-takeover}
sources:
  - id: s1
    title: "Monitor Login History"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.users_login_history.htm&type=5
    type: official-docs
    accessed: 2026-11-18
  - id: s2
    title: "LoginHistory | Object Reference for the Salesforce Platform"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_loginhistory.htm
    type: official-docs
    accessed: 2026-11-18
  - id: s3
    title: "LoginEvent | Platform Events Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/sforce_api_objects_loginevent.htm
    type: official-docs
    accessed: 2026-11-18
  - id: s4
    title: "Get to Know Real-Time Events and Transaction Security"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/realtime-event-monitoring/get-to-know-realtime-events-and-transaction-security
    type: official-learning
    accessed: 2026-11-18
  - id: s5
    title: "Monitor and Audit Security in Salesforce"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.security_audit.htm&type=5
    type: official-docs
    accessed: 2026-11-18
  - id: s6
    title: "Admin Security Workshop: Audit Trail"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/workshops/admin-security-workshop/monitoring-and-response/1-audit-trail
    type: official-learning
    accessed: 2026-11-18
created: 2026-11-18
---

# Login History

Login History is the standard audit record of every attempt to log in to a Salesforce org and to its Experience Cloud sites, including API logins.[^s1] Admins reach it in Setup under Users → Login History, where it sits alongside Setup Audit Trail and Field History Tracking as one of the platform's no-cost audit tools.[^s5][^s6] Each row tells you who tried to log in, when, from which IP address and browser, through which login mechanism, and whether the attempt succeeded or why it failed.[^s1][^s2] It is the first place to look when a user is locked out, when SSO breaks, or when you suspect a credential is being abused.

## How it works

The Login History page lists up to 20,000 login records from the past six months; custom list views have the same ceiling.[^s1][^s5] Beyond that, you download the full six months as a CSV file or as a compressed GZIP file (the faster option), and the "All Logins" download also includes API access logins.[^s1] List views can filter on Application, Authentication Method Reference, Login Subtype, Login Time, Login Type, Login URL, TLS Protocol and TLS Cipher Suite, and show up to 15 fields.[^s1] Viewing it requires the Monitor Login History or Manage Users permission, and it is available in every edition from Contact Manager through Unlimited and Developer.[^s1]

Programmatically, the same data lives in the **LoginHistory** object (API 21.0 and later), which supports `describeSObjects()`, `query()`, `retrieve()` and `delete()`.[^s2] Only users with Manage Users or Monitor Login History can query it, except that since API 37.0 every user can retrieve their own login records.[^s2] Useful fields include:[^s2]

- **Status**: success, or the reason a login failed.
- **LoginType** and **LoginSubType**: the mechanism, such as SAML, partner or other API, and (from API 57.0) the flow, such as OAuth web server.[^s2]
- **SourceIp**, **CountryIso** and the **LoginGeo** relationship for location (LoginGeo needs Manage Users).[^s2]
- **TlsProtocol** and **CipherSuite** for transport security, plus **AuthenticationServiceId** for the SSO configuration used.[^s2]
- **AuthMethodReference**: the authentication method reported by an OpenID Connect provider (API 51.0+).[^s2]

## What it captures

Beyond plain username-and-password logins, Login History records My Domain login URLs, SAML SSO logins, OAuth flows used by connected apps (client credentials, user-agent, username-password and web server), and password resets as a login subtype.[^s1] For OpenID Connect logins it surfaces the provider's Authentication Method References, so you can see whether the identity provider applied MFA.[^s1] It records both Source IP (the first client address to reach Salesforce) and a Forwarded-for IP taken from the X-Forwarded-For header, although the latter isn't populated for OAuth and SSO logins.[^s1] Failed logins carry status codes in the Login History report, for example an invalid password, a lockout in effect, an inactive user or an SSO service error.[^s1]

## Limits and gotchas

- **Six-month window.** Data older than six months is gone, so compliance programs needing longer retention must export it on a schedule.[^s1]
- **20,000-row UI cap.** Busy orgs exceed this quickly; use the download or a SOQL query against LoginHistory instead of the page.[^s1][^s2]
- **Filtering limits.** Only some fields are filterable in SOQL (for example UserId, LoginTime, LoginType, LoginUrl and CountryIso), and SourceIp doesn't support LIKE.[^s2]
- **Geolocation is approximate.** Country, city and postal code can be inaccurate.[^s1]

## When to use it (and when not)

Use Login History for day-to-day troubleshooting and periodic login reviews: diagnosing failed SSO, spotting logins from unexpected countries, finding users still on deprecated OAuth flows, and confirming that MFA is applied.[^s1] Salesforce recommends blocking the user-agent and username-password OAuth flows, and Login History shows who still relies on them.[^s1] When you need real-time detection, longer history or automatic blocking, move to Event Monitoring: its LoginEvent object (API 36.0+) stores login activity as a big object and can drive Transaction Security policies, but it requires the Shield or Event Monitoring add-on.[^s3][^s4] LoginEvent even carries a LoginHistoryId that ties each event back to its Login History row.[^s3]

## Connections

Login History is part of `kt:salesforce-identity` and is the free counterpart to `kt:event-monitoring`, whose real-time LoginEvent offers richer, longer-lived data under licence.[^s3][^s4] It is queried with `kt:soql` as the standard LoginHistory object.[^s2] It provides the evidence for reviewing `kt:login-ip-ranges-and-trusted-ip-ranges`, `kt:multi-factor-authentication` and `kt:oauth-2-flows-in-salesforce` in practice, and supports detecting `kt:account-takeover`.[^s1] It contrasts with `kt:field-audit-trail`, which audits data changes rather than authentication, just as Setup Audit Trail covers configuration changes.[^s5][^s6]

## Sources
[^s1]: Salesforce Help, "Monitor Login History". https://help.salesforce.com/s/articleView?language=en_US&id=sf.users_login_history.htm&type=5 (accessed 2026-11-18)
[^s2]: Salesforce Developers, "LoginHistory | Object Reference for the Salesforce Platform". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_loginhistory.htm (accessed 2026-11-18)
[^s3]: Salesforce Developers, "LoginEvent | Platform Events Developer Guide". https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/sforce_api_objects_loginevent.htm (accessed 2026-11-18)
[^s4]: Trailhead, "Get to Know Real-Time Events and Transaction Security". https://trailhead.salesforce.com/content/learn/modules/realtime-event-monitoring/get-to-know-realtime-events-and-transaction-security (accessed 2026-11-18)
[^s5]: Salesforce Help, "Monitor and Audit Security in Salesforce". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.security_audit.htm&type=5 (accessed 2026-11-18)
[^s6]: Salesforce Developers, "Admin Security Workshop: Audit Trail". https://developer.salesforce.com/workshops/admin-security-workshop/monitoring-and-response/1-audit-trail (accessed 2026-11-18)
