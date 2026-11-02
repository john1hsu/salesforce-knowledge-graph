---
id: kt:oauth-2-0
type: ExternalConcept
title: OAuth 2.0
aliases: [OAuth 2.0 Authorization Framework, RFC 6749, OAuth2]
domain: identity
summary: >-
  The IETF authorization framework (RFC 6749, with bearer-token usage in RFC 6750) that lets a client application
  obtain limited, scoped access tokens to a protected resource on behalf of a resource owner or itself, without
  handling the owner's password; it underpins Salesforce API authorization, and its security guidance is now
  consolidated in RFC 9700 and the in-progress OAuth 2.1 draft.
release: "Winter '27"
status: concept
broader: [kt:integration-security]
related: [kt:oauth-2-flows-in-salesforce, kt:connected-apps, kt:external-client-apps, kt:openid-connect-authentication-providers, kt:named-credentials]
relations:
  - {predicate: contrastsWith, object: kt:single-sign-on-saml}
  - {predicate: coveredBy, object: kt:identity-and-access-management-architect-certification}
sources:
  - id: s1
    title: "RFC 6749: The OAuth 2.0 Authorization Framework"
    publisher: IETF / RFC Editor
    url: https://rfc-editor.org/rfc/rfc6749.html
    type: standards-body
    accessed: 2026-11-02
  - id: s2
    title: "RFC 6750: The OAuth 2.0 Authorization Framework: Bearer Token Usage"
    publisher: IETF Datatracker
    url: https://datatracker.ietf.org/doc/rfc6750
    type: standards-body
    accessed: 2026-11-02
  - id: s3
    title: "RFC 9700: Best Current Practice for OAuth 2.0 Security"
    publisher: IETF / RFC Editor
    url: https://rfc-editor.org/rfc/rfc9700.html
    type: standards-body
    accessed: 2026-11-02
  - id: s4
    title: "The OAuth 2.1 Authorization Framework (draft-ietf-oauth-v2-1-16)"
    publisher: IETF
    url: https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-16.html
    type: standards-body
    accessed: 2026-11-02
  - id: s5
    title: "Authorization Through Connected Apps and OAuth 2.0 (REST API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_oauth_and_connected_apps.htm
    type: official-docs
    accessed: 2026-11-02
  - id: s6
    title: "Connected App Basics: API Integration"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/connected-app-basics/connected-app-basics-api-integration
    type: official-learning
    accessed: 2026-11-02
created: 2026-11-02
---

# OAuth 2.0

OAuth 2.0 is the IETF authorization framework published as RFC 6749 in October 2012. It lets a third-party application obtain limited access to an HTTP service, either on behalf of a resource owner or on its own behalf, by exchanging tokens rather than sharing the owner's credentials. It obsoleted OAuth 1.0 (RFC 5849) and is deliberately not backward compatible with it.[^s1] It is a standard, not a Salesforce feature: this node describes the protocol itself, while the Salesforce-specific grant types live under OAuth 2.0 Flows in Salesforce.

## Core model

The framework defines four roles. The **resource owner** can grant access (an end-user when it is a person); the **resource server** hosts protected data and accepts access tokens; the **client** is the application requesting access; and the **authorization server** authenticates the owner and issues tokens.[^s1] Clients are either **confidential**, able to keep a secret (a server-side app), or **public**, unable to do so (a native or browser-based app). Each client registers with the authorization server in advance, declaring its type and redirection URIs; the registration process itself is out of scope for the spec.[^s1]

Three endpoints carry the protocol: the authorization endpoint (user-agent redirection to obtain a grant), the token endpoint (exchanging a grant or refresh token for an access token, always by POST), and the client's redirection endpoint. The authorization and token endpoints require TLS.[^s1] **Scope** is a space-delimited list of strings defined by the authorization server, which may grant less than was requested but must then tell the client.[^s1]

## Grants and tokens

RFC 6749 defines four grant types — authorization code, implicit, resource owner password credentials and client credentials — plus an extension mechanism for new grants. An **access token** represents a specific scope and lifetime and is usually opaque to the client; an optional **refresh token** is presented only to the authorization server to obtain fresh access tokens, never to resource servers.[^s1]

RFC 6750 specifies how **bearer tokens** are presented: whoever holds the token can use it, with no proof of possession. Clients should send it in the `Authorization: Bearer` header; form-body and URI-query parameters are discouraged, and URLs in particular are often logged. TLS is mandatory, tokens should be short-lived (one hour or less) and audience-restricted, and resource servers signal failures with `invalid_request` (400), `invalid_token` (401) or `insufficient_scope` (403).[^s2]

## Modern security guidance

The 2012 text has been substantially tightened. RFC 9700 (BCP 240, January 2025) updates RFCs 6749 and 6750: the password grant must not be used, the implicit grant should not be, public clients must use PKCE with the `S256` method, authorization servers must match redirect URIs exactly, and public-client refresh tokens must be rotated or sender-constrained. It also recommends least-privilege, audience-restricted access tokens and sender-constraining via mutual TLS or DPoP.[^s3]

OAuth 2.1, still an IETF Internet-Draft (revision 16, September 2026), folds those practices into one document intended to replace RFCs 6749 and 6750. It makes PKCE mandatory, forbids the `plain` PKCE method, requires exact redirect matching, and drops the implicit and password grants entirely.[^s4]

## OAuth 2.0 in Salesforce

Salesforce's REST API requires a client app to be authorized through an OAuth 2.0 flow, using an external client app or a connected app. Salesforce restricted creation of new connected apps in Spring '26 and recommends external client apps for new integrations.[^s5] In practice Salesforce issues tokens from its token endpoint, validates authorization codes, JWTs and scopes on each request, and returns refresh tokens so integrations can renew access without user intervention.[^s6] Architects should read Salesforce's flow choices through the RFC 9700 lens: prefer authorization code with PKCE and server-to-server grants, and treat the implicit-style user-agent and username-password flows as legacy.[^s3][^s6]

## Connections

OAuth 2.0 is the standard that **OAuth 2.0 Flows in Salesforce** implement, and the client registrations it assumes are realised as **connected apps** and **external client apps**.[^s1][^s5] Because it governs delegated authorization rather than login, it is often contrasted with **SAML single sign-on**, and it is the base on which **OpenID Connect authentication providers** build. Outbound callouts reuse the same grants through **named credentials**. Its security practices — PKCE, exact redirect matching, least-privilege and sender-constrained tokens — make it a building block of **integration security** and a staple of the **Identity and Access Management Architect** certification.[^s3]

## Sources
[^s1]: IETF / RFC Editor, "RFC 6749: The OAuth 2.0 Authorization Framework" (October 2012). https://rfc-editor.org/rfc/rfc6749.html (accessed 2026-11-02)
[^s2]: IETF Datatracker, "RFC 6750: The OAuth 2.0 Authorization Framework: Bearer Token Usage" (October 2012). https://datatracker.ietf.org/doc/rfc6750 (accessed 2026-11-02)
[^s3]: IETF / RFC Editor, "RFC 9700: Best Current Practice for OAuth 2.0 Security" (January 2025). https://rfc-editor.org/rfc/rfc9700.html (accessed 2026-11-02)
[^s4]: IETF, "The OAuth 2.1 Authorization Framework", draft-ietf-oauth-v2-1-16 (September 2026). https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-16.html (accessed 2026-11-02)
[^s5]: Salesforce Developers, "Authorization Through Connected Apps and OAuth 2.0", REST API Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_oauth_and_connected_apps.htm (accessed 2026-11-02)
[^s6]: Trailhead, "Connected App Basics: API Integration". https://trailhead.salesforce.com/content/learn/modules/connected-app-basics/connected-app-basics-api-integration (accessed 2026-11-02)
