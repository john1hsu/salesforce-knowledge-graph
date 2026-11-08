---
id: kt:login-ip-ranges-and-trusted-ip-ranges
type: SecurityControl
title: Login IP Ranges and Trusted IP Ranges
aliases: [trusted IP ranges, login IP ranges, Network Access, profile login IP ranges, Restrict Login IP Addresses in Profiles, IP allowlisting in Salesforce, Enforce login IP ranges on every request, Continuous IP Enforcement]
domain: identity
summary: >-
  Salesforce's two IP-based login controls: org-wide trusted IP ranges (Network Access), which let users log in
  without an identity verification challenge, and per-profile login IP ranges, which deny any login from outside
  the allowed addresses.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity]
related: [kt:multi-factor-authentication, kt:session-security-levels, kt:login-flows, kt:integration-security, kt:hyperforce]
relations:
  - {predicate: configuredVia, object: kt:profiles}
  - {predicate: integratesWith, object: kt:connected-apps}
  - {predicate: alternativeTo, object: kt:mutual-tls-authentication}
  - {predicate: mitigates, object: kt:account-takeover}
  - {predicate: coveredBy, object: kt:identity-and-access-management-architect-certification}
sources:
  - id: s1
    title: "Set Trusted IP Ranges for Your Org"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.security_networkaccess.htm&type=5
    type: official-docs
    accessed: 2026-11-08
  - id: s2
    title: "Restrict Login IP Addresses in Profiles"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=xcloud.login_ip_ranges.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-08
  - id: s3
    title: "Connected App IP Relaxation and Continuous IP Enforcement"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.connected_app_continuous_ip.htm&type=5
    type: official-docs
    accessed: 2026-11-08
  - id: s4
    title: "Security and the API (SOAP API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api/guide/sforce-api-concepts-security.html
    type: official-docs
    accessed: 2026-11-08
  - id: s5
    title: "Data Security: Control Access to the Org"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data_security/data_security_org
    type: official-learning
    accessed: 2026-11-08
created: 2026-11-08
---

# Login IP Ranges and Trusted IP Ranges

Salesforce has two IP-address controls on login that are easy to confuse. **Trusted IP ranges**, set org-wide on the Network Access setup page, list addresses from which users can log in without being challenged to verify their identity; a login from elsewhere still succeeds once the user passes the challenge.[^s1] **Login IP ranges**, set on a profile, are a hard allowlist: once a profile has at least one range, a login by its users from any other address is denied, with no verification fallback.[^s2][^s5] Trailhead frames the difference simply: outside a trusted range the user verifies and continues, while outside a profile range the user is turned away.[^s5]

## How it works

Both controls take a start and end address (inclusive); entering the same value twice allows a single IP, and a description is optional.[^s1][^s2] Trusted ranges are managed in Setup → Network Access by users with Manage IP Addresses, and are available in all editions.[^s1] Profile ranges need View Setup and Configuration to view and Manage Profiles and Permission Sets to edit; Professional Edition needs the profiles add-on for them, otherwise only org-level trusted ranges are available.[^s2]

When someone logs in, Salesforce first checks the profile's login hours, then any profile IP restrictions; only if the profile has no IP restrictions does it fall back to the trusted IP list or a recognised browser and device, and if neither matches the user must verify identity.[^s4] The challenge uses the user's strongest registered method, from built-in authenticators and security keys down to Salesforce Authenticator, TOTP apps, SMS and finally email codes.[^s1] For API logins outside the trusted list, users without MFA for API logins append their security token to the password; inside the trusted list the password alone works.[^s4]

By default profile ranges are evaluated only at login. The session setting **Enforce login IP ranges on every request** applies them to every page request, including requests from client applications, but only for profiles that have ranges.[^s2][^s4]

## Limits and gotchas

- **Range size caps (since Winter '26):** 16,777,216 IPv4 addresses and 2^99 IPv6 addresses; IPv4-mapped IPv6 counts against the IPv4 cap, and the same caps apply to profile ranges. Addresses in 10.0.0.0–10.255.255.255 aren't counted when added as their own entry.[^s1][^s2]
- **Oversized legacy ranges:** orgs that exceeded the cap before the limit took effect may see device activation challenges even for users inside their ranges.[^s1][^s2]
- **Removing every trusted range** sends every user with org access through device activation.[^s1]
- **IPv6** is supported only for the Salesforce CDN on Experience Cloud sites; a profile with only IPv6 ranges blocks its users until support arrives, so pair them with IPv4 ranges.[^s2]
- **One address type per range:** IPv4, IPv4-mapped IPv6 or IPv6, never mixed.[^s1]
- **Exceptions:** profile restrictions don't apply to sites on Experience Delivery, and cached static resources on restricted guest profiles can take up to 45 days to expire.[^s2]
- **Partner User profiles** are limited to five IP addresses unless Support raises the limit.[^s2]

## Connected apps and integrations

A connected app's IP relaxation policy decides how profile IP restrictions apply to its OAuth users: fully enforced, relaxed only for refresh tokens, relaxed for activated devices, or fully relaxed.[^s3] With continuous enforcement on, relaxed users still can't change passwords, register verification methods or reach login flow pages.[^s3] SAML bearer assertion and JWT bearer flows always enforce IP restrictions regardless of the app's policy, which matters for server-to-server integrations whose egress IPs change.[^s3]

## When to use it (and when not)

Use trusted ranges to reduce verification friction on corporate networks, and profile login IP ranges where a population must only ever connect from known networks, such as integration users or a call centre also bound by login hours.[^s5][^s2] IP allowlisting is brittle for cloud and serverless clients, and on Hyperforce Salesforce points customers to alternatives such as mTLS or domain allowlisting instead.[^s1][^s2]

## Connections

Both controls sit under **Salesforce Identity** and are configured partly through **profiles**.[^s2] They complement **multi-factor authentication** and the **session security levels** model, and they interact with **login flows** and **connected apps** via continuous enforcement and IP relaxation.[^s3] Restricting where credentials work helps mitigate **account takeover**, and **mutual TLS** is the alternative Salesforce suggests on **Hyperforce**; for integration users the controls are one layer of **integration security**.[^s1][^s4]

## Sources
[^s1]: Salesforce Help, "Set Trusted IP Ranges for Your Org". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.security_networkaccess.htm&type=5 (accessed 2026-11-08)
[^s2]: Salesforce Help, "Restrict Login IP Addresses in Profiles". https://help.salesforce.com/s/articleView?id=xcloud.login_ip_ranges.htm&language=en_US&type=5 (accessed 2026-11-08)
[^s3]: Salesforce Help, "Connected App IP Relaxation and Continuous IP Enforcement". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.connected_app_continuous_ip.htm&type=5 (accessed 2026-11-08)
[^s4]: Salesforce Developers, "Security and the API". https://developer.salesforce.com/docs/platform/api/guide/sforce-api-concepts-security.html (accessed 2026-11-08)
[^s5]: Trailhead, "Data Security: Control Access to the Org". https://trailhead.salesforce.com/content/learn/modules/data_security/data_security_org (accessed 2026-11-08)
