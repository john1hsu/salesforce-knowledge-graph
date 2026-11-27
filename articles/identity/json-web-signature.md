---
id: kt:json-web-signature
type: ExternalConcept
title: JSON Web Signature
aliases: [JWS, RFC 7515, JWS Compact Serialization]
domain: identity
summary: >-
  The IETF standard (RFC 7515) for protecting arbitrary content with a digital signature or MAC using JSON-based
  structures; it is the signing layer beneath signed JWTs, and in Salesforce Apex the Auth.JWS class produces a
  JWS compact serialization signed with a certificate from Certificate and Key Management.
release: "Winter '27"
status: concept
broader: [kt:integration-security]
related: [kt:json-web-token, kt:jwt-bearer-flow, kt:openid-connect, kt:token-exchange-flow]
relations:
  - {predicate: dependsOn, object: kt:certificate-and-key-management}
  - {predicate: consumedBy, object: kt:jwt-bearer-flow}
  - {predicate: consumedBy, object: kt:json-web-token}
  - {predicate: contrastsWith, object: kt:saml-2-0}
sources:
  - id: s1
    title: "RFC 7515: JSON Web Signature (JWS)"
    publisher: IETF / RFC Editor
    url: https://rfc-editor.org/rfc/rfc7515.html
    type: standards-body
    accessed: 2026-11-27
  - id: s2
    title: "RFC 7518: JSON Web Algorithms (JWA)"
    publisher: IETF / RFC Editor
    url: https://www.rfc-editor.org/rfc/rfc7518
    type: standards-body
    accessed: 2026-11-27
  - id: s3
    title: "RFC 8725: JSON Web Token Best Current Practices"
    publisher: IETF / RFC Editor
    url: https://rfc-editor.org/rfc/rfc8725.html
    type: standards-body
    accessed: 2026-11-27
  - id: s4
    title: "Apex Reference Guide: JWS Class"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_class_Auth_JWS.htm
    type: official-docs
    accessed: 2026-11-27
  - id: s5
    title: "Apex Reference Guide: Auth Namespace"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_namespace_Auth.htm
    type: official-docs
    accessed: 2026-11-27
created: 2026-11-27
---

# JSON Web Signature

JSON Web Signature (JWS) is the IETF format for attaching integrity protection to content: a payload is secured either with a digital signature or with a message authentication code (MAC), and the result is described with JSON data structures. RFC 7515, a Standards Track document by Jones, Bradley and Sakimura, was published in May 2015.[^s1] JWS deliberately leaves the cryptography to a companion specification, JSON Web Algorithms (RFC 7518), and leaves encryption to JSON Web Encryption (JWE); keys can be expressed as JSON Web Keys (RFC 7517).[^s1][^s2] For Salesforce practitioners, JWS is what makes a JWT trustworthy: the signed tokens posted in the JWT bearer flow are JWS objects, and Apex builds them with the `Auth.JWS` class.[^s4]

## How it works

A JWS has three logical parts: a JOSE header that describes how the content is protected, the payload (any octet sequence, not necessarily JSON), and the signature or MAC value. What gets signed is the **JWS Signing Input**: the base64url-encoded protected header, a period, and the base64url-encoded payload. Because the header is inside the signing input, changing the declared algorithm or key hint breaks the signature.[^s1]

RFC 7515 defines two serializations. The **compact serialization** is the familiar three dot-separated base64url segments (header, payload, signature); it is URL-safe, carries one signature, and has no unprotected header. The **JSON serialization** is an object with `payload` plus one or more signatures, each with a `protected` header, an optional unprotected `header` and a `signature`; it can carry several signatures over the same payload, and a flattened variant puts a single signature's members at the top level.[^s1] Values in an unprotected header are not covered by the signature, and a name must not appear in both the protected and unprotected sets.[^s1] Appendix F also describes **detached content**: the payload segment is emptied before transmission and the recipient reinserts it before validating.[^s1]

## Header parameters

`alg` is the one mandatory header parameter; it names the algorithm and must be understood by the recipient.[^s1] The other registered parameters are optional key and type hints:[^s1]

- `kid` is a case-sensitive key identifier, while `jwk` embeds the public key and `jku` points to a JWK Set URL fetched over TLS.[^s1]
- `x5c` carries the X.509 chain inline, `x5u` points to it by URL, and `x5t` / `x5t#S256` give SHA-1 or SHA-256 certificate thumbprints.[^s1]
- `typ` declares the media type of the whole object, `cty` the payload's type, and `crit` lists extensions that must be understood or the JWS rejected.[^s1]

## Algorithms

RFC 7518 registers the `alg` values and their implementation requirements. HMAC with SHA-256 (`HS256`) is Required, RSASSA-PKCS1-v1_5 with SHA-256 (`RS256`) is Recommended, and ECDSA with P-256 and SHA-256 (`ES256`) is Recommended+, meaning its requirement level is expected to rise; the PSS and larger-hash variants and `none` are Optional.[^s2] RSA keys must be 2048 bits or larger, and an HMAC key must be at least as long as the hash output, so 256 bits for `HS256`.[^s2] An unsecured JWS (`alg` set to `none`) has an empty signature, and implementations must not accept such objects by default.[^s2]

## Limits and gotchas

Most real-world JWS failures are validation mistakes, which RFC 8725 catalogues. Attackers have relabelled tokens as `none`, or switched an RS256 token to HS256 so that a naive library verifies the MAC using the RSA public key as the secret.[^s3] The countermeasure is algorithm verification: the caller fixes the allowed algorithm set, each key is bound to exactly one algorithm, and anything else is rejected.[^s3] HMAC keys must never be human-memorable passwords, because a captured token permits offline guessing.[^s3] Header values such as `kid`, `jku` and `x5u` are attacker-controlled input, so they should be sanitized and URLs fetched only from an allowlist.[^s3] A valid signature also proves only who signed, not who the token was meant for, so recipients must still check issuer and audience.[^s3]

## In Salesforce

The Apex `Auth.JWS` class applies a digital signature to a JWT. Its two constructors take either an `Auth.JWT` instance or a payload string, plus the unique name of a certificate in Certificate and Key Management; `getCompactSerialization()` returns the dot-separated header, payload and signature.[^s4] The Auth namespace pairs it with `Auth.JWT`, which builds the claims set, `Auth.JWTBearerTokenExchange`, which posts the signed token to a token endpoint for an access token, and `Auth.JWTUtil`, which validates an incoming JWT inside a token exchange handler.[^s5]

## Connections

JWS sits under **integration security** and is consumed by the **JSON Web Token** format, which uses it for signed tokens, and by the **JWT bearer flow**, whose assertions are JWS compact serializations.[^s1][^s4] Signing in Apex depends on **Certificate and Key Management**, which holds the private key named in the `Auth.JWS` constructor.[^s4] On the inbound side, `Auth.JWTUtil` supports the **token exchange flow** and RFC 8725's issuer and key-binding checks apply equally to **OpenID Connect** tokens.[^s3][^s5] It contrasts with **SAML 2.0**, the XML-based assertion format that serves similar federation roles.

## Sources

[^s1]: IETF / RFC Editor, "RFC 7515: JSON Web Signature (JWS)". https://rfc-editor.org/rfc/rfc7515.html (accessed 2026-11-27)
[^s2]: IETF / RFC Editor, "RFC 7518: JSON Web Algorithms (JWA)". https://www.rfc-editor.org/rfc/rfc7518 (accessed 2026-11-27)
[^s3]: IETF / RFC Editor, "RFC 8725: JSON Web Token Best Current Practices". https://rfc-editor.org/rfc/rfc8725.html (accessed 2026-11-27)
[^s4]: Salesforce Developers, "Apex Reference Guide: JWS Class". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_class_Auth_JWS.htm (accessed 2026-11-27)
[^s5]: Salesforce Developers, "Apex Reference Guide: Auth Namespace". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_namespace_Auth.htm (accessed 2026-11-27)
