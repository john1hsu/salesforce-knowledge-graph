---
id: kt:web-server-flow
type: Feature
title: OAuth 2.0 Web Server Flow
aliases: [web server flow, web server OAuth authentication flow, Salesforce authorization code flow, OAuth 2.0 Web Server Flow for Web App Integration]
domain: identity
summary: >-
  Salesforce's implementation of the OAuth 2.0 authorization code grant: the user logs in and approves the app in a
  browser, Salesforce sends a short-lived authorization code to the app's callback URL, and the app's server exchanges
  that code (with its consumer secret and, increasingly, a PKCE code verifier) for access and refresh tokens.
release: "Winter '27"
status: current
broader: [kt:oauth-2-flows-in-salesforce]
related: [kt:refresh-token-policies, kt:openid-connect, kt:my-domain, kt:headless-identity, kt:appexchange-security-review]
relations:
  - {predicate: implements, object: kt:oauth-2-0}
  - {predicate: configuredVia, object: kt:external-client-apps}
  - {predicate: configuredVia, object: kt:connected-apps}
  - {predicate: alternativeTo, object: kt:device-flow}
  - {predicate: alternativeTo, object: kt:jwt-bearer-flow}
  - {predicate: alternativeTo, object: kt:client-credentials-flow}
sources:
  - id: s1
    title: "Implement the OAuth 2.0 Web Server Flow (Build Integrations with External Client Apps)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/build-integrations-with-external-client-apps/implement-the-oauth-20-web-server-flow
    type: official-learning
    accessed: 2026-11-19
  - id: s2
    title: "Web Server OAuth Authentication Flow (Connect REST API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.250.0.chatterapi.meta/chatterapi/intro_oauth_web_server_flow.htm
    type: official-docs
    accessed: 2026-11-19
  - id: s3
    title: "Secure Your Connected Apps and External Client Apps"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.packagingGuide.meta/packagingGuide/secure_code_ac_eca.htm
    type: official-docs
    accessed: 2026-11-19
  - id: s4
    title: "RFC 6749: The OAuth 2.0 Authorization Framework"
    publisher: IETF
    url: https://rfc-editor.org/rfc/rfc6749
    type: standards-body
    accessed: 2026-11-19
  - id: s5
    title: "RFC 7636: Proof Key for Code Exchange by OAuth Public Clients"
    publisher: IETF
    url: https://www.rfc-editor.org/rfc/rfc7636
    type: standards-body
    accessed: 2026-11-19
  - id: s6
    title: "RFC 9700: Best Current Practice for OAuth 2.0 Security"
    publisher: IETF
    url: https://www.rfc-editor.org/rfc/rfc9700.html?lang=en
    type: standards-body
    accessed: 2026-11-19
created: 2026-11-19
---

# OAuth 2.0 Web Server Flow

The **web server flow** is Salesforce's name for the OAuth 2.0 authorization code grant. A web application sends the user's browser to the Salesforce login page, the user signs in and approves the app, and Salesforce returns a temporary authorization code that the app's server trades for tokens.[^s1][^s2] The app never sees the user's password, and because the code exchange happens server to server, it is the standard choice for web apps that can keep a consumer secret confidential.[^s2] It is one of the OAuth 2.0 flows in Salesforce covered by the umbrella article; this node covers the request shape, PKCE and the security rules around it.

## The standard underneath

RFC 6749, published by the IETF in October 2012, defines the authorization code grant in five steps: the client redirects the browser to the authorization endpoint, the server authenticates the user, the server redirects back with a code and the client's `state`, the client presents the code to the token endpoint, and the server returns an access token and optionally a refresh token.[^s4] The redirect URI in the token request must match the one used in the authorization request, and a code is meant to be used only once.[^s4]

RFC 7636 (September 2015) added **Proof Key for Code Exchange (PKCE)** to stop an attacker who intercepts the code from redeeming it.[^s5] The client creates a random `code_verifier` of 43 to 128 characters, sends a derived `code_challenge` with the authorization request, and proves possession by sending the verifier at the token step; the `S256` method is mandatory for servers to implement and clients should use it whenever they can.[^s5]

## How it works in Salesforce

1. **Authorize.** The app redirects the browser to `/services/oauth2/authorize` on the org's My Domain with `response_type=code`, the consumer key as `client_id` and the callback URL as `redirect_uri`; optional `state`, `immediate` and `display` parameters control round-trip data, silent re-approval and the login page layout.[^s2][^s1]
2. **Log in and allow.** The user signs in and approves the app; this step is skipped if the user already authorized it.[^s2]
3. **Callback.** Salesforce redirects to the callback URL with a `code` query parameter (plus `state` if sent), and the app's server must host that page.[^s2]
4. **Exchange.** The server POSTs to `/services/oauth2/token` with `grant_type=authorization_code`, the `code`, `client_id`, `client_secret` and the identical `redirect_uri`.[^s1][^s2]
5. **Use the tokens.** The JSON response carries `access_token`, `token_type` of `Bearer`, `instance_url`, the identity URL in `id`, `issued_at` and a `signature`, which is an HMAC-SHA256 over the id and issue time keyed with the consumer secret.[^s2] The docs also list a `refresh_token` for getting new access tokens later, and Trailhead's example with the `openid` scope returns an `id_token` too.[^s2][^s1]

On an external client app, the **Require Secret for Web Server Flow** setting makes Salesforce refuse to issue a token unless a valid consumer secret is sent.[^s1] Developer docs add that if an app does not require a secret but one is sent anyway, Salesforce still tries to validate it.[^s2]

## Security requirements and gotchas

- **PKCE for everyone.** Salesforce now requires partner-built connected apps and external client apps used by more than two customer production orgs to enable PKCE for both public and confidential clients, and the setting cannot be turned off once on.[^s3] Public clients send only the `code_verifier`, while confidential clients send it together with the `client_secret`.[^s3]
- **The 2025 BCP agrees.** RFC 9700 says public clients must use PKCE, recommends it for confidential clients, and requires exact string matching of redirect URIs.[^s6] It also requires clients to prevent CSRF, either through PKCE or a one-time `state` value bound to the browser.[^s6]
- **Treat tokens as secrets.** The access token acts like a session ID and the refresh token should be protected like a password.[^s2] Partner apps must also turn on refresh token rotation and a 30-day idle refresh-token lifetime, and enable a refresh-token IP allowlist, which Salesforce describes as meant for web server flow apps.[^s3]
- **Callback hygiene.** Host the callback on a secure server and keep the consumer secret server-side, sending it only in the POST body.[^s1]

## When to use it (and when not)

Use the web server flow whenever a person is present and the app runs in or can open a browser: web apps with a confidential server, and, with PKCE, public clients that cannot keep a secret.[^s6][^s3] RFC 9700 says the implicit grant should give way to the code flow and that the password grant must not be used, which leaves this flow as the default interactive login.[^s6] Because it depends on a user approving in a browser and an app able to protect its secret, it suits neither input-constrained devices nor unattended integrations, which the device, JWT bearer and client credentials flows cover instead.[^s2]

## Connections

The flow is one of the **OAuth 2.0 flows in Salesforce** and **implements** the **OAuth 2.0** authorization code grant.[^s4][^s2] It is **configured via** an **external client app** or a **connected app**, where secret, PKCE and refresh-token settings live, and those refresh-token settings tie it to **refresh token policies**.[^s1][^s3] Adding the `openid` scope layers **OpenID Connect** on top, the authorize URL lives on **My Domain**, and **Headless Identity** wires native single sign-on through it.[^s1][^s2] The partner requirements tie it to the **AppExchange security review**, and it is an **alternative to** the **device**, **JWT bearer** and **client credentials** flows.[^s3][^s2]

## Sources

[^s1]: Trailhead, "Implement the OAuth 2.0 Web Server Flow". https://trailhead.salesforce.com/content/learn/projects/build-integrations-with-external-client-apps/implement-the-oauth-20-web-server-flow (accessed 2026-11-19)
[^s2]: Salesforce Developers, "Web Server OAuth Authentication Flow". https://developer.salesforce.com/docs/atlas.en-us.250.0.chatterapi.meta/chatterapi/intro_oauth_web_server_flow.htm (accessed 2026-11-19)
[^s3]: Salesforce Developers, "Secure Your Connected Apps and External Client Apps". https://developer.salesforce.com/docs/atlas.en-us.packagingGuide.meta/packagingGuide/secure_code_ac_eca.htm (accessed 2026-11-19)
[^s4]: IETF, "RFC 6749: The OAuth 2.0 Authorization Framework". https://rfc-editor.org/rfc/rfc6749 (accessed 2026-11-19)
[^s5]: IETF, "RFC 7636: Proof Key for Code Exchange by OAuth Public Clients". https://www.rfc-editor.org/rfc/rfc7636 (accessed 2026-11-19)
[^s6]: IETF, "RFC 9700: Best Current Practice for OAuth 2.0 Security". https://www.rfc-editor.org/rfc/rfc9700.html?lang=en (accessed 2026-11-19)
