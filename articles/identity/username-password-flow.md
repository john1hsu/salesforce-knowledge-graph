---
id: kt:username-password-flow
type: Feature
title: OAuth 2.0 Username-Password Flow
aliases: [username-password flow, username-password OAuth flow, resource owner password credentials grant, ROPC grant, grant_type=password, password grant]
domain: identity
summary: >-
  Salesforce's implementation of the OAuth 2.0 resource owner password credentials grant: a client posts a user's
  username and password (plus security token) with its consumer key and secret to the token endpoint and gets an
  access token with no browser login and no refresh token; it is a legacy flow, blocked by default in orgs created
  in Summer '23 or later.
release: "Winter '27"
status: current
broader: [kt:oauth-2-flows-in-salesforce]
related: [kt:login-history, kt:multi-factor-authentication]
relations:
  - {predicate: implements, object: kt:oauth-2-0}
  - {predicate: configuredVia, object: kt:connected-apps}
  - {predicate: alternativeTo, object: kt:client-credentials-flow}
  - {predicate: alternativeTo, object: kt:jwt-bearer-flow}
sources:
  - id: s1
    title: "RFC 6749: The OAuth 2.0 Authorization Framework"
    publisher: IETF
    url: https://datatracker.ietf.org/doc/html/rfc6749.html
    type: standards-body
    accessed: 2026-11-23
  - id: s2
    title: "RFC 9700: Best Current Practice for OAuth 2.0 Security"
    publisher: RFC Editor (IETF)
    url: https://www.rfc-editor.org/rfc/rfc9700.html
    type: standards-body
    accessed: 2026-11-23
  - id: s3
    title: "Understanding the Username-Password OAuth Authentication Flow (REST API Developer Guide, API 47.0)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.222.0.api_rest.meta/api/intro_understanding_username_password_oauth_flow.htm
    type: official-docs
    accessed: 2026-11-23
  - id: s4
    title: "Set Up Authorization with OAuth 2.0 (Streaming API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-streaming/guide/code-sample-auth-oauth.html
    type: official-docs
    accessed: 2026-11-23
  - id: s5
    title: "OauthOidcSettings (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_oauthoidcsettings.htm
    type: official-docs
    accessed: 2026-11-23
  - id: s6
    title: "Maintain Your Identity and Access Architect Certification for Winter '24"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-architect-certification-maintenance-winter-24/maintain-your-identity-and-access-architect-certification-for-winter-24
    type: official-learning
    accessed: 2026-11-23
created: 2026-11-23
---

# OAuth 2.0 Username-Password Flow

The **username-password flow** is the oldest and bluntest way to get a Salesforce access token: the client application already holds a user's username and password and sends them, together with the app's consumer key and secret, directly to the token endpoint.[^s3] Nobody is redirected to a Salesforce login page, so the user never sees or approves the request.[^s3] Salesforce's own documentation says to use it only when necessary and only when the app is handling its own credentials, and Salesforce now blocks it by default in new orgs.[^s3][^s4][^s6] The umbrella article on OAuth flows compares all the flows; this node covers the standard, the request, and why it has become a legacy option.

## The standard underneath

RFC 6749 section 4.3 defines it as the **resource owner password credentials grant**, meant for a client the user deeply trusts, such as a device operating system or a highly privileged application, and only when other flows are not viable.[^s1] The client sends `grant_type=password`, `username`, `password` and an optional `scope` to the token endpoint, authenticating itself if it is a confidential client, and it must discard the credentials once it has the token.[^s1] Section 10.7 calls the grant higher risk because it keeps the password anti-pattern OAuth was designed to remove, and says servers and clients should minimize its use.[^s1] The 2025 security best current practice, RFC 9700, goes further: section 2.4 says the grant must not be used.[^s2] Its reasons are that it exposes the user's credentials to the client, widens the attack surface, trains users to type passwords outside the authorization server, and doesn't fit multi-step or two-factor login or origin-bound cryptographic methods such as WebAuthn.[^s2]

## How it works in Salesforce

The client makes an out-of-band POST to `/services/oauth2/token` on the login host with five values: `grant_type=password`, `client_id` (the consumer key), `client_secret`, `username`, and `password`.[^s3][^s4] The password field carries the user's password with the user's **security token** appended, for example `mypassword` followed by the token characters.[^s3] The client secret can be omitted only if the app's "Require Secret for Web Server Flow" setting is turned off.[^s3] A successful response returns `access_token`, `instance_url`, the identity URL `id`, `issued_at` and a `signature`, an HMAC-SHA256 over the ID and issue time keyed with the client secret.[^s3][^s4] The access token acts as a session ID, so Salesforce says to protect it as carefully as the credentials themselves.[^s3] The Streaming API guide still ships a Java sample built on this flow, which then calls the identity URL to read the user's details.[^s4]

## Limits and gotchas

- **No refresh token.** Because the user never logs in through Salesforce, the flow can't issue refresh tokens; apps that need them should use another flow.[^s3]
- **Blocked by default in newer orgs.** Orgs created in Summer '23 or later block the flow by default; an admin can re-enable it with **Allow OAuth Username-Password Flows** in OAuth and OpenID Connect Settings.[^s6]
- **Blocking can break things.** Salesforce warns that turning the block on can break mobile apps, including its own, and managed packages.[^s6]
- **Settings as metadata.** The `OauthOidcSettings` type (API 56.0+) exposes the block as the boolean `blockOAuthUnPwFlow`, next to `blockOAuthUsrAgtFlow` for the user-agent flow.[^s5]
- **Finding remaining users.** Add the Login Subtype field to a Login History view to see which connected apps still log in this way.[^s6]

## When to use it (and when not)

Treat it as a legacy and migration path, not a design choice for new integrations.[^s1][^s2] Salesforce recommends the client credentials flow as the replacement for server-to-server work, since it authenticates the app without handling any user's password.[^s6] The JWT bearer flow, covered in its own article, is the other back-end option in this graph. Interactive apps acting for a user belong in a redirect-based flow such as the web server flow, which can also issue refresh tokens.[^s3] If an old integration still depends on this flow, keep its credentials on a dedicated, least-privileged user and plan its migration before blocking the flow org-wide.[^s1][^s6]

## Connections

It is one of the **OAuth 2.0 flows in Salesforce** and **implements** the password grant from **OAuth 2.0** (RFC 6749).[^s1][^s3] It is **configured via** a **connected app**, whose consumer key and secret go in the request.[^s3] The **client credentials flow** is Salesforce's recommended **alternative** for unattended integrations,[^s6] and the **JWT bearer flow** is linked as a second alternative. Its use shows up in **Login History** under the Login Subtype field, and because the grant can't run a multi-step login, it sits poorly with **multi-factor authentication**.[^s2][^s6]

## Sources

[^s1]: IETF, "RFC 6749: The OAuth 2.0 Authorization Framework". https://datatracker.ietf.org/doc/html/rfc6749.html (accessed 2026-11-23)
[^s2]: RFC Editor, "RFC 9700: Best Current Practice for OAuth 2.0 Security". https://www.rfc-editor.org/rfc/rfc9700.html (accessed 2026-11-23)
[^s3]: Salesforce Developers, "Understanding the Username-Password OAuth Authentication Flow". https://developer.salesforce.com/docs/atlas.en-us.222.0.api_rest.meta/api/intro_understanding_username_password_oauth_flow.htm (accessed 2026-11-23)
[^s4]: Salesforce Developers, "Set Up Authorization with OAuth 2.0". https://developer.salesforce.com/docs/platform/api-streaming/guide/code-sample-auth-oauth.html (accessed 2026-11-23)
[^s5]: Salesforce Developers, "OauthOidcSettings". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_oauthoidcsettings.htm (accessed 2026-11-23)
[^s6]: Trailhead, "Maintain Your Identity and Access Architect Certification for Winter '24". https://trailhead.salesforce.com/content/learn/modules/salesforce-architect-certification-maintenance-winter-24/maintain-your-identity-and-access-architect-certification-for-winter-24 (accessed 2026-11-23)
