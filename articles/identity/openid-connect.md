---
id: kt:openid-connect
type: ExternalConcept
title: OpenID Connect
aliases: [OIDC, OpenID Connect 1.0, OpenID Connect Core]
domain: identity
summary: >-
  The OpenID Foundation standard that adds an identity layer on top of OAuth 2.0: an OpenID Provider authenticates
  the end-user and returns a signed JWT ID token (plus a UserInfo endpoint) so a relying party can verify who signed
  in; Salesforce acts both as an OpenID Provider and, through authentication providers, as a relying party.
release: "Winter '27"
status: concept
broader: [kt:oauth-2-0]
related: [kt:salesforce-identity, kt:connected-apps, kt:external-client-apps, kt:oauth-2-flows-in-salesforce, kt:experience-cloud-identity]
relations:
  - {predicate: contrastsWith, object: kt:single-sign-on-saml}
  - {predicate: consumedBy, object: kt:openid-connect-authentication-providers}
  - {predicate: dependsOn, object: kt:json-web-token}
sources:
  - id: s1
    title: "OpenID Connect Core 1.0 incorporating errata set 2"
    publisher: OpenID Foundation
    url: https://openid.net/specs/openid-connect-core-1_0.html
    type: standards-body
    accessed: 2026-11-10
  - id: s2
    title: "OpenID Connect Discovery 1.0 incorporating errata set 2"
    publisher: OpenID Foundation
    url: https://openid.net/specs/openid-connect-discovery-1_0.html
    type: standards-body
    accessed: 2026-11-10
  - id: s3
    title: "Salesforce OpenID Provider Configuration (login.salesforce.com discovery document)"
    publisher: Salesforce
    url: https://login.salesforce.com/.well-known/openid-configuration
    type: official-docs
    accessed: 2026-11-10
  - id: s4
    title: "Integrate Service Providers with Salesforce (Connected App Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/ko/content/learn/modules/connected-app-basics/connected-app-basics-sso
    type: official-learning
    accessed: 2026-11-10
  - id: s5
    title: "Using OpenID Tokens to Access External Services (Mobile SDK Development Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/mobile-sdk/guide/auth-openid-tokens.html
    type: official-docs
    accessed: 2026-11-10
  - id: s6
    title: "Configure an Authentication Provider Using OpenID Connect (Mobile SDK Development Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.mobile_sdk.meta/mobile_sdk/sso_provider_openid_connect.htm
    type: official-docs
    accessed: 2026-11-10
created: 2026-11-10
---

# OpenID Connect

OpenID Connect (OIDC) is an OpenID Foundation standard that describes itself as a simple identity layer on top of OAuth 2.0. It lets a client verify the identity of an end-user from an authentication performed by an authorization server, and obtain basic profile information about that user. The current text of the core specification is OpenID Connect Core 1.0 incorporating errata set 2, dated December 15, 2023.[^s1] Like OAuth 2.0 it is a protocol, not a Salesforce feature: this node covers the standard, while the Salesforce relying-party configuration is described under OpenID Connect Authentication Providers.

## Core model

OIDC renames the OAuth roles for authentication: the authorization server acts as the **OpenID Provider (OP)** and the client acts as the **Relying Party (RP)**. A request becomes an OpenID Connect request only when its scope includes the value `openid`; without it, the exchange is plain OAuth.[^s1]

The central addition is the **ID token**, a JSON Web Token carrying claims about the authentication event. It must contain `iss` (issuer), `sub` (subject identifier), `aud` (audience, which includes the RP's client ID), `exp` and `iat`. A `nonce` sent in the request must be echoed back, binding the token to the client session and blocking replay; `auth_time` is required when the RP asks for a maximum authentication age. ID tokens must be signed with JWS, with RS256 as the default algorithm, and may additionally be encrypted.[^s1]

Before trusting an ID token, the RP checks that the issuer matches exactly, that its client ID is in the audience, that the signature is valid, that the token has not expired and was issued recently, and that the nonce matches.[^s1] The specification stresses that only the combination of `iss` and `sub` reliably identifies a user; claims such as `email` or `preferred_username` must not be used as unique keys.[^s1]

## Flows, scopes and the UserInfo endpoint

The `response_type` selects the flow. The **authorization code flow** (`code`) returns every token from the token endpoint; the **implicit flow** (`id_token` or `id_token token`) returns tokens directly from the authorization endpoint; the **hybrid flow** combines both, for example `code id_token`.[^s1]

The **UserInfo endpoint** is an OAuth-protected resource called with the access token as a bearer token over TLS. Its response must include a `sub` that exactly matches the ID token, or the RP must discard it. The standard scopes `profile`, `email`, `address` and `phone` request groups of claims, such as `email` and `email_verified`; an optional `claims` parameter can request individual claims.[^s1]

**Discovery** lets an RP configure itself automatically. It fetches the issuer URL with `/.well-known/openid-configuration` appended and receives a JSON document listing endpoints, the JWKS signing-key URL, and supported response types, subject types and signing algorithms (which must include RS256). The `issuer` value in that document must equal both the requested URL and the `iss` claim in ID tokens. WebFinger can optionally locate the issuer from a user identifier.[^s2]

## OpenID Connect in Salesforce

**Salesforce as OpenID Provider.** Salesforce publishes a discovery document at login.salesforce.com. It names the authorize, token, userinfo, revocation and introspection endpoints under `/services/oauth2/`, publishes keys at `/id/keys`, and advertises the `openid`, `profile`, `email`, `address` and `phone` scopes among many Salesforce-specific ones. It lists `code`, `token` and `token id_token` response types, RS256 ID-token signing, public subject identifiers, and `S256` as its only PKCE method.[^s3] To sign users into an external service provider, an admin adds the `openid` scope to a connected app and configures its ID token. The service provider must be able to accept OIDC tokens. Trailhead suggests OIDC when the provider supports it and SAML when an org already uses SAML.[^s4] Mobile SDK apps can also request a short-lived OpenID token and exchange it with external services that don't accept Salesforce access tokens.[^s5]

**Salesforce as relying party.** An authentication provider of the OpenID Connect type takes the external provider's client ID and secret and its authorize, token and user info endpoints. It can enable PKCE and record a token issuer. Salesforce checks the ID token against that issuer and the user info endpoint, but doesn't validate the ID token's signature. A required Apex registration handler creates or links the Salesforce user.[^s6]

## Connections

OpenID Connect sits under **OAuth 2.0** because it reuses OAuth's endpoints, grants and bearer tokens and only adds identity semantics.[^s1] Its ID tokens are **JSON Web Tokens**, and it is the main alternative to **SAML single sign-on** for federated login.[^s1][^s4] Inside the platform it is consumed by **OpenID Connect authentication providers** on the relying-party side, and issued through **connected apps** and **external client apps** on the provider side. Those OAuth endpoints and scopes are the same ones that **OAuth 2.0 flows in Salesforce** use.[^s3][^s4][^s6] It is a building block of **Salesforce Identity**, including social and enterprise sign-on for **Experience Cloud identity**.[^s4]

## Sources
[^s1]: OpenID Foundation, "OpenID Connect Core 1.0 incorporating errata set 2" (December 15, 2023). https://openid.net/specs/openid-connect-core-1_0.html (accessed 2026-11-10)
[^s2]: OpenID Foundation, "OpenID Connect Discovery 1.0 incorporating errata set 2" (December 15, 2023). https://openid.net/specs/openid-connect-discovery-1_0.html (accessed 2026-11-10)
[^s3]: Salesforce, OpenID Provider configuration for login.salesforce.com. https://login.salesforce.com/.well-known/openid-configuration (accessed 2026-11-10)
[^s4]: Trailhead, "Integrate Service Providers with Salesforce", Connected App Basics. https://trailhead.salesforce.com/ko/content/learn/modules/connected-app-basics/connected-app-basics-sso (accessed 2026-11-10)
[^s5]: Salesforce Developers, "Using OpenID Tokens to Access External Services", Mobile SDK Development Guide. https://developer.salesforce.com/docs/platform/mobile-sdk/guide/auth-openid-tokens.html (accessed 2026-11-10)
[^s6]: Salesforce Developers, "Configure an Authentication Provider Using OpenID Connect", Mobile SDK Development Guide. https://developer.salesforce.com/docs/atlas.en-us.mobile_sdk.meta/mobile_sdk/sso_provider_openid_connect.htm (accessed 2026-11-10)
