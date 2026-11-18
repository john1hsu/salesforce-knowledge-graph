---
id: kt:json-web-token
type: ExternalConcept
title: JSON Web Token
aliases: [JWT, RFC 7519, JWT claims set]
domain: identity
summary: >-
  The IETF standard (RFC 7519) for a compact, URL-safe token that carries a JSON set of claims, protected by a
  JSON Web Signature or JSON Web Encryption; Salesforce uses JWTs as bearer assertions in the JWT bearer flow, as
  OpenID Connect ID tokens, and optionally as self-contained RS256-signed access tokens.
release: "Winter '27"
status: concept
broader: [kt:integration-security]
related: [kt:oauth-2-0, kt:salesforce-identity, kt:certificate-and-key-management, kt:external-client-apps]
relations:
  - {predicate: consumedBy, object: kt:jwt-bearer-flow}
  - {predicate: consumedBy, object: kt:openid-connect}
  - {predicate: consumedBy, object: kt:named-credentials}
  - {predicate: consumedBy, object: kt:salesforce-cli}
  - {predicate: dependsOn, object: kt:json-web-signature}
  - {predicate: contrastsWith, object: kt:saml-2-0}
sources:
  - id: s1
    title: "RFC 7519: JSON Web Token (JWT)"
    publisher: IETF / RFC Editor
    url: https://rfc-editor.org/rfc/rfc7519
    type: standards-body
    accessed: 2026-11-18
  - id: s2
    title: "RFC 8725: JSON Web Token Best Current Practices"
    publisher: IETF / RFC Editor
    url: https://rfc-editor.org/rfc/rfc8725.html
    type: standards-body
    accessed: 2026-11-18
  - id: s3
    title: "JWT-Based Access Tokens"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.jwt_access_tokens.htm&amp=&type=5
    type: official-docs
    accessed: 2026-11-18
  - id: s4
    title: "Apex Reference: Auth.JWT Class"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_class_Auth_JWT.htm
    type: official-docs
    accessed: 2026-11-18
  - id: s5
    title: "Apex Reference: Auth.JWS Class"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_class_Auth_JWS.htm
    type: official-docs
    accessed: 2026-11-18
  - id: s6
    title: "Named Credentials Reference: JWT Bearer Flow Claims"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/named-credentials/references/named-credentials-reference/jwt-claims.html
    type: official-docs
    accessed: 2026-11-18
  - id: s7
    title: "Authorize an Org Using the JWT Flow (Salesforce DX Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-auth-jwt-flow.html
    type: official-docs
    accessed: 2026-11-18
created: 2026-11-18
---

# JSON Web Token

A JSON Web Token (JWT, suggested pronunciation "jot") is a compact way to pass a set of claims between two parties. RFC 7519, a Proposed Standard published in May 2015, defines the format; the claims are a JSON object that becomes the payload of a JSON Web Signature (JWS) or the plaintext of a JSON Web Encryption (JWE), always in the compact serialization.[^s1] In Salesforce, JWTs show up wherever an identity or authorization assertion has to be verifiable without a round trip: signed assertions in the OAuth 2.0 JWT bearer flow, OpenID Connect ID tokens, and optional JWT-based access tokens.[^s3][^s4]

## How it works

A signed JWT is three base64url-encoded parts joined by periods: a JOSE header naming the algorithm, the claims set, and the signature.[^s1][^s5] RFC 7519 sorts claim names into registered, public (collision-resistant) and private names agreed between the parties, and every registered claim is optional at the format level:[^s1]

- `iss` (issuer), `sub` (subject) and `aud` (audience); a recipient that isn't in `aud` must reject the token.[^s1]
- `exp` (expiry), `nbf` (not before) and `iat` (issued at) bound the token's lifetime in NumericDate seconds.[^s1]
- `jti` gives the token a unique identifier, which recipients can use to detect replays.[^s1]

The header may carry `typ` (usually "JWT") and, for a JWT nested inside another, `cty`. The spec also allows an unsecured JWT using the `none` algorithm with an empty signature; its claims then have no integrity protection.[^s1]

## In Salesforce

Apex builds and signs JWTs natively. `Auth.JWT` produces the claims set (setters for issuer, subject, audience, validity length in seconds that drives `exp`, plus additional custom claims), and its `toJSONString()` output feeds `Auth.JWS`.[^s4] `Auth.JWS` signs that payload with a certificate referenced by its unique name in Certificate and Key Management and returns the compact serialization.[^s5]

External credentials that use the JWT bearer flow let admins edit `iss`, `sub` and `aud`; if no expiration is set, `exp` defaults to two minutes ahead, and `alg` is fixed to RS256.[^s6] Salesforce CLI's `sf org login jwt` signs its request with a private key whose matching certificate is uploaded to an external client app (or a connected app for Dev Hub scratch-org work), so CI can authorize without a browser.[^s7]

On the issuing side, Salesforce can mint JWT-based access tokens instead of opaque ones. They let off-platform services validate the token locally rather than calling Salesforce, they are signed with RS256 (the only algorithm Salesforce supports for them), and they carry claims such as `aud`, `exp`, `iss`, `nbf`, `sub` and `scp`.[^s3]

## Limits and gotchas

- JWT-based access tokens can be used only against Salesforce REST APIs, and they behave differently from opaque tokens.[^s3]
- A JWT is signed, not encrypted, by default: anyone holding it can decode the claims, so keep sensitive data out or use encryption plus TLS.[^s1]
- If the org requires high-assurance sessions, identity verification blocks headless JWT logins from Salesforce CLI.[^s7]

RFC 8725 (BCP 225, February 2020) lists the classic failures. Validators should accept only an allow-listed set of algorithms and bind each key to one algorithm, which defeats `none` tokens and RS256-to-HS256 key-confusion attacks.[^s2] They should check that signing keys belong to the stated `iss`, require and validate `aud` when an issuer serves several relying parties, use explicit `typ` values to avoid confusing one kind of JWT for another, and never use human-memorable passwords as HMAC keys.[^s2]

## When to use it (and when not)

Use a JWT when a party needs a self-describing, signed assertion it can verify offline: server-to-server OAuth without stored secrets, federated sign-in through OpenID Connect, or downstream services validating Salesforce-issued tokens.[^s3][^s6] Prefer opaque tokens when a consumer must call SOAP or other non-REST Salesforce APIs.[^s3]

## Connections

JWT is the token format beneath several identity nodes: the **JWT bearer flow** posts a signed JWT assertion for an access token, **OpenID Connect** ID tokens are JWTs, **named credentials** build JWT claims for outbound calls, and **Salesforce CLI** relies on the JWT flow for CI.[^s6][^s7] Its signing depends on JSON Web Signature and on certificates held in **Certificate and Key Management**.[^s5] It sits under **integration security** alongside **OAuth 2.0**, and contrasts with the XML assertions of **SAML 2.0**; JWT-based access tokens are enabled per **external client app** or connected app.[^s3]

## Sources
[^s1]: IETF, "RFC 7519: JSON Web Token (JWT)". https://rfc-editor.org/rfc/rfc7519 (accessed 2026-11-18)
[^s2]: IETF, "RFC 8725: JSON Web Token Best Current Practices". https://rfc-editor.org/rfc/rfc8725.html (accessed 2026-11-18)
[^s3]: Salesforce Help, "JWT-Based Access Tokens". https://help.salesforce.com/s/articleView?language=en_US&id=sf.jwt_access_tokens.htm&amp=&type=5 (accessed 2026-11-18)
[^s4]: Salesforce Developers, "Apex Reference: Auth.JWT Class". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_class_Auth_JWT.htm (accessed 2026-11-18)
[^s5]: Salesforce Developers, "Apex Reference: Auth.JWS Class". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_class_Auth_JWS.htm (accessed 2026-11-18)
[^s6]: Salesforce Developers, "Named Credentials Reference: JWT Bearer Flow Claims". https://developer.salesforce.com/docs/platform/named-credentials/references/named-credentials-reference/jwt-claims.html (accessed 2026-11-18)
[^s7]: Salesforce Developers, "Authorize an Org Using the JWT Flow". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-auth-jwt-flow.html (accessed 2026-11-18)
