---
id: kt:jwt-bearer-flow
type: Feature
title: OAuth 2.0 JWT Bearer Flow
aliases: [JWT bearer flow, JWT bearer token flow, JWT bearer grant, RFC 7523 bearer grant, sf org login jwt]
domain: identity
summary: >-
  Salesforce's implementation of the RFC 7523 JWT bearer authorization grant: a server signs a short-lived JWT
  with a certificate's private key and exchanges it at the token endpoint for an access token for a pre-approved
  user, with no browser login and no refresh token. Salesforce also acts as the client side of the same grant
  through Apex and JWT-based external credentials.
release: "Winter '27"
status: current
broader: [kt:oauth-2-flows-in-salesforce]
related: [kt:continuous-integration-for-salesforce, kt:session-security-levels, kt:scratch-orgs]
relations:
  - {predicate: implements, object: kt:oauth-2-0}
  - {predicate: configuredVia, object: kt:external-client-apps}
  - {predicate: configuredVia, object: kt:connected-apps}
  - {predicate: alternativeTo, object: kt:client-credentials-flow}
  - {predicate: consumedBy, object: kt:salesforce-cli}
  - {predicate: consumedBy, object: kt:named-credentials}
sources:
  - id: s1
    title: "OAuth 2.0 JWT Bearer Flow for Server-to-Server Integration"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.remoteaccess_oauth_jwt_flow.htm&type=5
    type: official-docs
    accessed: 2026-11-14
  - id: s2
    title: "RFC 7523: JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants"
    publisher: IETF / RFC Editor
    url: https://www.rfc-editor.org/rfc/rfc7523
    type: standards-body
    accessed: 2026-11-14
  - id: s3
    title: "Authorize an Org Using the JWT Flow"
    publisher: Salesforce Developers (Salesforce DX Developer Guide)
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-auth-jwt-flow.html
    type: official-docs
    accessed: 2026-11-14
  - id: s4
    title: "JWTBearerTokenExchange Class"
    publisher: Salesforce Developers (Apex Reference Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_class_Auth_JWTBearerTokenExchange.htm
    type: official-docs
    accessed: 2026-11-14
  - id: s5
    title: "Create or Edit an OAuth External Credential with the JWT Bearer Flow"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.nc_create_edit_oath_jwt_bearer_ext_cred.htm&type=5
    type: official-docs
    accessed: 2026-11-14
created: 2026-11-14
---

# OAuth 2.0 JWT Bearer Flow

The **JWT bearer flow** lets a back-end system get a Salesforce access token without any interactive login. The client builds a JSON Web Token naming the app and the user, signs it with the private key behind a certificate registered on the app, and posts it to the token endpoint; Salesforce validates it and returns an access token if the user has already been approved for the app.[^s1] It is Salesforce's implementation of the authorization-grant half of RFC 7523, a May 2015 IETF Standards Track profile whose co-authors include a Salesforce engineer.[^s2] The umbrella article on OAuth flows compares it with its siblings; this node covers the mechanics, the setup on both sides of the exchange, and the operational gotchas.

## The standard underneath

RFC 7523 defines two uses of a JWT at an OAuth token endpoint: as an **authorization grant**, sent as `assertion` with grant type `urn:ietf:params:oauth:grant-type:jwt-bearer`, and as a **client authentication** credential, sent as `client_assertion`.[^s2] For grants it requires the `iss`, `sub`, `aud` and `exp` claims; `nbf`, `iat` and `jti` are optional. The JWT must be signed or MACed, RS256 is mandatory to implement, the server must reject a token whose audience doesn't name it or that has expired (allowing for clock skew), and a bad grant JWT yields an `invalid_grant` error.[^s2] Client authentication is optional for the grant, which is why Salesforce needs no client secret here.[^s2][^s1]

## How it works in Salesforce

The client signs with RSA SHA-256 using the private key of an X.509 certificate uploaded to the external client app or connected app; the certificate can't exceed 4 KB, and a DER-encoded file is the suggested fix if it does.[^s1] The claims map as follows: `iss` is the app's consumer key, `aud` is `https://login.salesforce.com`, `https://test.salesforce.com` or an Experience Cloud site URL, `sub` is the username (the legacy `prn` claim is still accepted), and `exp` is in epoch seconds with a three-minute skew allowance.[^s1] Including `jti` makes Salesforce reject a token it has seen before, giving replay protection.[^s1]

The token request is a form-encoded POST to `/services/oauth2/token` carrying `grant_type` and `assertion`. A successful response holds `access_token`, `token_type` Bearer, `scope`, `instance_url` and the identity URL `id`, plus `sfdc_site_url` and `sfdc_site_id` when the user belongs to an Experience Cloud site.[^s1]

## Limits and gotchas

- **No refresh token, ever.** The client mints a fresh JWT whenever it needs a new access token.[^s1]
- **Approval must already exist.** With "Admin approved users are pre-authorized", access is granted through profiles and permission sets; with self-authorization, the user must previously have approved the app with a grant that issued a refresh token. Otherwise the request fails as unauthorized.[^s1]
- **Scopes can't be requested.** They come from prior approvals, the app's assigned scopes, or API Access Control allowlisting, depending on configuration.[^s1]
- **High assurance blocks it.** If the org demands stepped-up authentication, the identity-verification prompt stops a headless JWT login.[^s3]
- **Use My Domain URLs.** For CLI logins, point at the `my.salesforce.com` My Domain (or sandbox) URL rather than a Lightning URL; My Domain URLs survive org migrations.[^s3]

## Common uses

**CI/CD.** `sf org login jwt` takes `--client-id`, `--jwt-key-file`, `--username` and optionally `--instance-url` and `--alias`, so a pipeline can authenticate from a stored key without a browser.[^s3] The DX guide recommends an external client app, but a connected app when the Dev Hub will create scratch orgs or sandboxes; a scratch org can then be authorized with its Dev Hub's consumer key and key file, using the scratch org admin's username and instance URL (a "user isn't approved" error usually means replication hasn't finished).[^s3]

**Salesforce as the client.** In Apex, `Auth.JWTBearerTokenExchange` POSTs a signed `Auth.JWS` to another provider's token endpoint and returns the `access_token` (or the full `HttpResponse`); its default grant type is the RFC 7523 URN, and callouts can be mocked with `Auth.HttpCalloutMockUtil`.[^s4] Declaratively, an OAuth 2.0 external credential with the JWT Bearer flow type does the same: it names the identity provider URL, a signing certificate from Certificate and Key Management, RS256 or RS512, optional scopes and custom JWT claims, and named or per-user principals, and is then linked to a named credential.[^s5]

## When to use it (and when not)

Choose it for unattended server-to-server integrations that must run as a specific user and can protect a private key, and for CI pipelines. When managing certificates is harder than managing a shared secret and a single integration user is fine, the client credentials flow is the lighter alternative; for anything a human drives interactively, use a flow with a login step.[^s1][^s3]

## Connections

It is one of the **OAuth 2.0 flows in Salesforce** and **implements** the **OAuth 2.0** framework's JWT profile.[^s1][^s2] It is **configured via** an **external client app** or **connected app**, is **consumed by** the **Salesforce CLI** for headless org logins in **continuous integration** and with **scratch orgs**, and is **consumed by** **named credentials** through JWT-based external credentials.[^s3][^s5] It is an **alternative to** the **client credentials flow**, and because it has no approval step it collides with **session security levels** that require high assurance.[^s1][^s3]

## Sources

[^s1]: Salesforce Help, "OAuth 2.0 JWT Bearer Flow for Server-to-Server Integration". https://help.salesforce.com/s/articleView?language=en_US&id=sf.remoteaccess_oauth_jwt_flow.htm&type=5 (accessed 2026-11-14)
[^s2]: IETF / RFC Editor, "RFC 7523: JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants". https://www.rfc-editor.org/rfc/rfc7523 (accessed 2026-11-14)
[^s3]: Salesforce Developers, "Authorize an Org Using the JWT Flow". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-auth-jwt-flow.html (accessed 2026-11-14)
[^s4]: Salesforce Developers, "JWTBearerTokenExchange Class". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_class_Auth_JWTBearerTokenExchange.htm (accessed 2026-11-14)
[^s5]: Salesforce Help, "Create or Edit an OAuth External Credential with the JWT Bearer Flow". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.nc_create_edit_oath_jwt_bearer_ext_cred.htm&type=5 (accessed 2026-11-14)
