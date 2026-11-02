---
id: kt:oauth-2-flows-in-salesforce
type: Feature
title: OAuth 2.0 Flows in Salesforce
aliases: [Salesforce OAuth flows, OAuth authorization flows, Salesforce OAuth grant types]
domain: identity
summary: >-
  The set of OAuth 2.0 and OpenID Connect authorization flows Salesforce supports for apps to obtain access
  tokens — web server (authorization code, with PKCE), JWT bearer, client credentials, device, refresh token,
  hybrid, asset token and the discouraged user-agent and username-password flows — each suited to a different
  client type and trust model.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity, kt:oauth-2-0]
related: [kt:connected-apps, kt:external-client-apps, kt:named-credentials, kt:my-domain, kt:openid-connect-authentication-providers]
relations:
  - {predicate: implements, object: kt:oauth-2-0}
  - {predicate: configuredVia, object: kt:external-client-apps}
  - {predicate: configuredVia, object: kt:connected-apps}
  - {predicate: coveredBy, object: kt:identity-and-access-management-architect-certification}
sources:
  - id: s1
    title: "OAuth Authorization Flows"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_oauth_flows_ca.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-02
  - id: s2
    title: "OAuth 2.0 JWT Bearer Flow for Server-to-Server Integration"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_jwt_flow.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-02
  - id: s3
    title: "Proof Key for Code Exchange (PKCE) Extension"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_pkce.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-02
  - id: s4
    title: "Using the Client Credentials Flow for Easier API Authentication"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2023/03/using-the-client-credentials-flow-for-easier-api-authentication
    type: official-blog
    accessed: 2026-11-02
  - id: s5
    title: "RFC 7636: Proof Key for Code Exchange by OAuth Public Clients"
    publisher: IETF / RFC Editor
    url: https://www.rfc-editor.org/info/rfc7636
    type: standards-body
    accessed: 2026-11-02
  - id: s6
    title: "Winter '27 Release Highlights"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/winter-27-release-highlights/
    type: official-learning
    accessed: 2026-11-02
created: 2026-11-02
---

# OAuth 2.0 Flows in Salesforce

An OAuth flow (grant type) is the sequence of requests an application uses to obtain an access token from Salesforce acting as the authorization server. Salesforce supports a family of flows, each matched to a kind of client: a server-hosted web app, a mobile or desktop app, a back-end service with no user present, or an input-constrained device. Apart from the SAML assertion flow, every flow requires a registered client app — a connected app or, for new work, an external client app.[^s1] This article was checked against the Winter '27 (264) documentation.[^s1][^s6]

## The flows

- **Web server flow** — the authorization code grant for apps hosted on a secure server, which must protect the client ID and secret. It is the default choice for web apps calling Salesforce APIs on a user's behalf.[^s1]
- **User-agent flow** — the implicit grant for browser, desktop or mobile apps. Salesforce recommends avoiding it because it exposes credentials in transit.[^s1]
- **Refresh token flow** — exchanges a refresh token from the web server or user-agent flow for a new access token without re-prompting the user.[^s1]
- **Hybrid app flows** — bind access and refresh tokens to the web session so hybrid apps don't have to track session expiry and re-bridge manually.[^s1]
- **JWT bearer flow** — a server signs a JWT with a certificate's private key and receives an access token with no interactive login; the client app must already be approved.[^s1][^s2]
- **Client credentials flow** — a service exchanges the consumer key and secret for an access token, running as a designated integration user.[^s1][^s4]
- **Device flow** — for smart TVs, appliances and command-line tools that can't easily take input; the user authorizes on another device's browser.[^s1]
- **Asset token flow** — issues JWT-based asset tokens to secure requests from connected IoT devices.[^s1]
- **Username-password flow** — the client sends stored user credentials directly. It is for narrow, high-trust, first-party cases only.[^s1]
- **OpenID Connect dynamic client registration** — lets Salesforce act as an independent authorization server for resources on an external API gateway; Salesforce notes it is not a typical authorization flow.[^s1]

## How the key server-to-server flows work

In the **JWT bearer flow**, the client builds a token whose `iss` is the app's client ID, `aud` is the authorization server (for example login or test, or an Experience Cloud site URL), `sub` is the username and `exp` is an expiry in epoch seconds; Salesforce allows a three-minute clock-skew buffer. An optional `jti` claim enables replay detection. The JWT is signed RS256 with the private key of an X.509 certificate uploaded to the app, and the certificate can't exceed 4 KB. No refresh token is ever issued, scopes cannot be requested in the assertion, and the request fails as unauthorized unless the user is pre-authorized (admin-approved policy) or has previously approved the app with a grant that included a refresh token.[^s2]

The **client credentials flow** is enabled on the app, which is given a run-as user; every token carries that user's permissions. Salesforce's guidance is to create a dedicated integration user and restrict it with permission sets rather than running as a system administrator.[^s4]

## Securing user-facing flows with PKCE

Proof Key for Code Exchange (RFC 7636) defends public clients against interception of the authorization code: the client sends a hashed `code_challenge` with the authorization request and the original `code_verifier` with the token request.[^s5] Salesforce supports PKCE on the web server flow, the hybrid web server flow and every variant of the Authorization Code and Credentials Flow (headless registration, passwordless login and guest flows), in all editions. Admins can require PKCE per app or org-wide; the org-wide setting automatically blocks any authorization code variant that doesn't use it. Salesforce recommends PKCE for all public clients, and PKCE plus the consumer secret for confidential ones.[^s3]

## Limits and gotchas

- **Block the legacy flows.** Salesforce strongly recommends blocking the user-agent and username-password flows; the username-password flow is blocked by default in orgs created in Summer '23 or later, though it can be re-enabled.[^s1]
- **Connected app creation is restricted** as of Spring '26; existing apps keep working, but new integrations should use external client apps.[^s1]
- **JWT scopes come from policy,** not the request — from the Permitted Users configuration or org-level API Access Control.[^s2]
- **Keep secrets out of URLs**; send them in the POST body or a header.[^s2]
- **Client credentials tokens are only as narrow as the run-as user.**[^s4]

## When to use which

For a web app acting for a user, use the web server flow with PKCE. For back-end integrations, choose JWT bearer when you can manage a certificate and want a specific user context, or client credentials when a shared secret and a fixed integration user suffice; both replace the username-password flow.[^s1][^s2][^s4] Use the device flow for CLIs and constrained hardware, and the refresh token flow to keep long-lived user sessions alive.[^s1]

## Connections

These flows are Salesforce's implementation of the **OAuth 2.0** framework and sit under **Salesforce Identity**.[^s1] Every flow except SAML assertion is configured through a client registration — legacy **connected apps** or their successor, **external client apps**.[^s1] Hardening with PKCE follows the IETF extension.[^s5] Callouts from Salesforce to other systems use the same grants through **named credentials**, and user-facing flows depend on **My Domain** login URLs and **OpenID Connect authentication providers**, which also support PKCE.[^s3] The topic is core to the **Identity and Access Management Architect** certification.

## Sources
[^s1]: Salesforce Help, "OAuth Authorization Flows". https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_oauth_flows_ca.htm&language=en_US&type=5 (accessed 2026-11-02)
[^s2]: Salesforce Help, "OAuth 2.0 JWT Bearer Flow for Server-to-Server Integration". https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_jwt_flow.htm&language=en_US&type=5 (accessed 2026-11-02)
[^s3]: Salesforce Help, "Proof Key for Code Exchange (PKCE) Extension". https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_pkce.htm&language=en_US&type=5 (accessed 2026-11-02)
[^s4]: Salesforce Developers Blog, "Using the Client Credentials Flow for Easier API Authentication" (March 2023). https://developer.salesforce.com/blogs/2023/03/using-the-client-credentials-flow-for-easier-api-authentication (accessed 2026-11-02)
[^s5]: IETF / RFC Editor, "RFC 7636: Proof Key for Code Exchange by OAuth Public Clients" (September 2015). https://www.rfc-editor.org/info/rfc7636 (accessed 2026-11-02)
[^s6]: Trailhead, "Winter '27 Release Highlights". https://trailhead.salesforce.com/content/learn/modules/winter-27-release-highlights/ (accessed 2026-11-02)
