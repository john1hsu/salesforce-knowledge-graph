---
id: kt:refresh-token-policies
type: SecurityControl
title: OAuth Refresh Token Policies
aliases: [Refresh Token Policy, refresh token expiration policy, Refresh Token Idle TTL, refresh token rotation]
domain: identity
summary: >-
  The per-app OAuth policies that decide how long a Salesforce refresh token stays usable — valid until revoked,
  immediately expired, expired after an inactivity window, or expired after a fixed lifetime — plus the newer
  hardening controls for connected and external client apps: a 30-day idle time-to-live, refresh token rotation
  and a refresh token IP allowlist.
release: "Winter '27"
status: current
broader: [kt:oauth-2-flows-in-salesforce, kt:integration-security]
related: [kt:connected-apps, kt:external-client-apps, kt:login-ip-ranges-and-trusted-ip-ranges, kt:salesforce-cli, kt:appexchange-security-review]
relations:
  - {predicate: configuredVia, object: kt:connected-apps}
  - {predicate: configuredVia, object: kt:external-client-apps}
  - {predicate: implements, object: kt:oauth-2-0}
  - {predicate: mitigates, object: kt:account-takeover}
sources:
  - id: s1
    title: "Manage OAuth Access Policies for a Connected App"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.connected_app_manage_oauth.htm&type=5
    type: official-docs
    accessed: 2026-11-12
  - id: s2
    title: "Limit the Idle Refresh Token TTL in Connected Apps"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=xcloud.connected_app_limit_idle_ttl.htm&amp=&language=en_US&amp=&type=5
    type: official-docs
    accessed: 2026-11-12
  - id: s3
    title: "Secure Your Connected Apps and External Client Apps"
    publisher: Salesforce Developers (ISVforce Guide)
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/secure-code-ac-eca.html
    type: official-docs
    accessed: 2026-11-12
  - id: s4
    title: "ExtlClntAppOauthConfigurablePolicies"
    publisher: Salesforce Developers (Metadata API Developer Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_extlclntappoauthconfigurablepolicies.htm
    type: official-docs
    accessed: 2026-11-12
  - id: s5
    title: "Use the Default Connected App Securely"
    publisher: Salesforce Developers (Salesforce DX Developer Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_default_conn_app.htm
    type: official-docs
    accessed: 2026-11-12
  - id: s6
    title: "RFC 9700: Best Current Practice for OAuth 2.0 Security"
    publisher: IETF Datatracker
    url: https://datatracker.ietf.org/doc/rfc9700/
    type: standards-body
    accessed: 2026-11-12
  - id: s7
    title: "OAuth 2.0 Refresh Token Flow"
    publisher: Salesforce Developers (Mobile SDK Development Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.mobile_sdk.meta/pages/oauth_refresh_token_flow.htm
    type: official-docs
    accessed: 2026-11-12
created: 2026-11-12
---

# OAuth Refresh Token Policies

A refresh token lets an OAuth client get a new access token after the current session expires, without sending the user back through login. In Salesforce, how long that token stays usable is not fixed by the platform: each connected app or external client app carries a **Refresh Token Policy**, and newer controls (an idle time-to-live, rotation and an IP allowlist) tighten it further. Because a refresh token is effectively a long-lived credential, these settings are one of the main levers for limiting the damage of a leaked integration token.[^s1][^s3]

## The four policy options

The policy is checked only when a refresh token is presented; it doesn't cut short a session that is already running.[^s1]

- **Refresh token is valid until revoked** (the default) — the token works indefinitely until a user or admin revokes it.[^s1]
- **Immediately expire refresh token** — the current access token runs until it expires, but no new session can be obtained.[^s1]
- **Expire refresh token if not used for _n_** — a sliding inactivity window; each successful exchange renews the token and resets the clock.[^s1]
- **Expire refresh token after _n_** — a fixed lifetime counted from issuance, regardless of how often the token is used.[^s1]

In metadata for external client apps, the same choices appear as `refreshTokenPolicyType` values `Infinite`, `Zero`, `SpecificInactivity` and `SpecificLifetime`, with `refreshTokenValidityPeriod` and a unit of hours, days or months for the two timed options.[^s4]

## Hardening controls

**Idle TTL of 30 days.** The "Limit Idle Refresh Token Time-to-Live (TTL) to 30 Days" setting caps how long any refresh token may sit unused. Turning it on immediately expires tokens idle for 30 days or more, along with their access tokens; for flows without refresh tokens, access tokens expire 30 days after the user's last login. Salesforce is enforcing this control for connected apps, after which the setting can't be edited.[^s2]

The cap interacts with the policy options. "Valid until revoked" is hidden and behaves as a 30-day inactivity policy, but it isn't updated in metadata automatically, so it should be set to `specific_inactivity:30:DAYS`. An inactivity window can't exceed 30 days. A fixed lifetime longer than 30 days still applies, but a token idle for 30 days expires first.[^s2]

**Refresh token rotation.** With rotation on, every refresh issues a new refresh token and invalidates the old one, so a stolen token dies at the next legitimate refresh. Once enabled it can't be turned off. Clients must store the new token from each response, treat a rejected refresh as a possible compromise, and guard against parallel requests racing to use the same token.[^s3] This follows the IETF's OAuth security best practice, which requires public clients' refresh tokens to be either sender-constrained or rotated, and recommends expiring tokens that go unused.[^s6]

**Refresh token IP allowlist.** For apps using the web server flow, an allowlist blocks refresh requests from outside the listed ranges, with at most 256 IP addresses across all ranges. It isn't suitable for callbacks to localhost or custom URL schemes.[^s3] It is separate from the app's IP Relaxation policy, whose options include enforcing org IP restrictions but relaxing them for refresh tokens.[^s1]

## Requirements for AppExchange partners

For partner apps used by more than two customer production orgs, Salesforce requires PKCE, rotation, the 30-day idle TTL and the IP allowlist, with a May 11, 2026 deadline. Partners self-attest through Review Controls, which locks the controls on. Non-compliance can lead to de-listing or suspension of the app's access.[^s3]

## Gotchas and guidance

Shorter is safer. Salesforce's guidance for the default "Salesforce CLI" connected app, whose tokens never expire by default, is to set refresh tokens to expire in 90 days or less and the session timeout to 15 minutes; an expired token then forces a fresh `org login`.[^s5] In mobile apps built with the Mobile SDK, an expired or revoked refresh token resets app state and purges SmartStore data, so very short policies have user-facing costs.[^s7] Canvas apps that use signed requests should use the "immediately expire" policy with admin-approved users.[^s1]

## Connections

The policy governs the refresh token step of the **OAuth 2.0 flows in Salesforce** and is Salesforce's implementation of refresh token guidance in **OAuth 2.0**.[^s1][^s6] It is configured on **connected apps** and on their successor, **external client apps**.[^s1][^s4] The IP allowlist complements **login IP ranges and trusted IP ranges**, and the partner requirements feed into the **AppExchange security review** process.[^s1][^s3] Short lifetimes and rotation mitigate **account takeover** through stolen integration tokens, including tokens issued to the **Salesforce CLI**.[^s3][^s5] The controls are part of broader **integration security**.

## Sources
[^s1]: Salesforce Help, "Manage OAuth Access Policies for a Connected App". https://help.salesforce.com/s/articleView?language=en_US&id=sf.connected_app_manage_oauth.htm&type=5 (accessed 2026-11-12)
[^s2]: Salesforce Help, "Limit the Idle Refresh Token TTL in Connected Apps". https://help.salesforce.com/s/articleView?id=xcloud.connected_app_limit_idle_ttl.htm&amp=&language=en_US&amp=&type=5 (accessed 2026-11-12)
[^s3]: Salesforce Developers, ISVforce Guide, "Secure Your Connected Apps and External Client Apps". https://developer.salesforce.com/docs/platform/isvforce/guide/secure-code-ac-eca.html (accessed 2026-11-12)
[^s4]: Salesforce Developers, Metadata API Developer Guide, "ExtlClntAppOauthConfigurablePolicies". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_extlclntappoauthconfigurablepolicies.htm (accessed 2026-11-12)
[^s5]: Salesforce Developers, Salesforce DX Developer Guide, "Use the Default Connected App Securely". https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_default_conn_app.htm (accessed 2026-11-12)
[^s6]: IETF, "RFC 9700: Best Current Practice for OAuth 2.0 Security" (January 2025). https://datatracker.ietf.org/doc/rfc9700/ (accessed 2026-11-12)
[^s7]: Salesforce Developers, Mobile SDK Development Guide, "OAuth 2.0 Refresh Token Flow". https://developer.salesforce.com/docs/atlas.en-us.mobile_sdk.meta/pages/oauth_refresh_token_flow.htm (accessed 2026-11-12)
