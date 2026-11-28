---
id: kt:webauthn
type: ExternalConcept
title: WebAuthn
aliases: [Web Authentication API, W3C Web Authentication, Web Authentication Level 3, navigator.credentials WebAuthn API]
domain: identity
summary: >-
  The W3C Web Authentication standard: a browser API that lets a site register and verify origin-scoped public-key
  credentials held by authenticators; together with the FIDO Alliance's CTAP it forms FIDO2, and it underpins the
  security keys and passkeys that Salesforce accepts as phishing-resistant MFA.
release: "Winter '27"
status: concept
broader: [kt:multi-factor-authentication]
related: [kt:identity-verification, kt:salesforce-identity, kt:session-security-levels, kt:nist-digital-identity-guidelines]
relations:
  - {predicate: consumedBy, object: kt:security-keys}
  - {predicate: consumedBy, object: kt:passkeys}
  - {predicate: mitigates, object: kt:account-takeover}
  - {predicate: contrastsWith, object: kt:time-based-one-time-password}
  - {predicate: integratesWith, object: kt:client-to-authenticator-protocol}
sources:
  - id: s1
    title: "Web Authentication: An API for accessing Public Key Credentials Level 3"
    publisher: W3C
    url: https://www.w3.org/TR/webauthn-3/
    type: standards-body
    accessed: 2026-11-28
  - id: s2
    title: "Web Authentication: An API for accessing Public Key Credentials Level 3 is now a W3C Recommendation"
    publisher: W3C
    url: https://www.w3.org/news/2026/web-authentication-an-api-for-accessing-public-key-credentials-level-3-is-now-a-w3c-recommendation/
    type: standards-body
    accessed: 2026-11-28
  - id: s3
    title: "User Authentication Specifications Overview"
    publisher: FIDO Alliance
    url: https://fidoalliance.org/specifications/
    type: standards-body
    accessed: 2026-11-28
  - id: s4
    title: "Prepare for Phishing-Resistant MFA Enforcement for Privileged Users including Admins"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005321563&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-28
  - id: s5
    title: "Enable Passkeys for Identity Verification in Salesforce Orgs"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.security_enable_builtin_authenticator.htm&type=5
    type: official-docs
    accessed: 2026-11-28
created: 2026-11-28
---

# WebAuthn

WebAuthn (Web Authentication) is a W3C specification that defines a browser API for creating and using strong, attested, public-key credentials to authenticate users. Each credential is scoped to one Relying Party (the website or service), is bound to an authenticator, and can be used only by origins that belong to that Relying Party; a Relying Party cannot even detect credentials that belong to another site.[^s1] Level 3 of the specification, produced by the Web Authentication Working Group, became a W3C Recommendation on 25 August 2026 as the successor to Level 2, with further features planned for Level 4.[^s2] In the Salesforce ecosystem WebAuthn is the standard behind security keys and passkeys, the verification methods that count as phishing-resistant MFA.[^s4]

## How it works

WebAuthn has two ceremonies. In registration, the site calls `navigator.credentials.create()` and the authenticator generates a new key pair scoped to the Relying Party and the user's account; the private key stays with the authenticator and the site stores the public key, optionally with attestation about the authenticator. In authentication, the site calls `navigator.credentials.get()` and the authenticator returns a signed assertion that proves the user was present and consented.[^s1] The user agent mediates every call to protect privacy, and the specification requires authenticators to perform no operation without user consent.[^s1]

The specification distinguishes platform authenticators, built into the user's device, from roaming authenticators reached over USB, Bluetooth Low Energy or NFC.[^s1] Roaming authenticators talk to the client through the FIDO Alliance's Client to Authenticator Protocol (CTAP); the Alliance describes WebAuthn plus CTAP together as FIDO2, and it renamed the older U2F protocol CTAP1 so that existing U2F keys keep working as second factors.[^s3] The Level 3 document also defines client capability discovery, JSON parsing helpers for creation and request options, signal methods for keeping credential lists in sync, and Related Origins for credentials shared across a set of domains.[^s1]

## Why it resists phishing

Because each credential is bound to the Relying Party's origin and the browser enforces that binding, a look-alike site cannot obtain a usable assertion, and no shared secret or code is typed that an attacker could relay.[^s1] The FIDO Alliance likewise describes every passkey as unique and bound to the domain of the service that created it, which is why it presents FIDO standards as phishing-resistant authentication.[^s3] This is the key contrast with one-time-password methods, where a user can be tricked into entering a valid code on an attacker's page.

## WebAuthn in Salesforce

Salesforce's phishing-resistant MFA tier lists Security Keys (WebAuthn) and built-in authenticators such as Touch ID and Windows Hello, while Salesforce Authenticator push and TOTP apps fall in the standard MFA tier that does not satisfy the requirement.[^s4] That requirement applies to privileged users, such as those with the System Administrator profile or permissions like Modify All Data, View All Data, Customize Application or Author Apex, for direct and SSO logins; production enforcement began on 20 July 2026 and was rolled out by release group through September 2026.[^s4] Passkeys, which Salesforce also calls built-in authenticators, let users verify with Touch ID, Face ID, Windows Hello, a device password or a password manager; admins turn them on in Identity Verification settings, and under MFA enforcement Salesforce enables them for all employee users and the setting can't be switched off.[^s5]

## Connections

WebAuthn sits under **multi-factor authentication** as one family of verification methods, and it is consumed by two Salesforce features: **security keys** (roaming authenticators) and **passkeys** (platform and synced credentials).[^s4][^s5] It mitigates **account takeover** through origin binding, and it contrasts with **TOTP**, which is strong but phishable.[^s1][^s4] It works with **Client to Authenticator Protocol (CTAP)**, the FIDO2 half that reaches external authenticators.[^s3] Admins switch passkeys on in **identity verification** settings; **session security levels**, **Salesforce Identity** and NIST's **digital identity guidelines** are linked as related nodes for the wider assurance picture.[^s5]

## Sources

[^s1]: W3C, "Web Authentication: An API for accessing Public Key Credentials Level 3". https://www.w3.org/TR/webauthn-3/ (accessed 2026-11-28)
[^s2]: W3C, "Web Authentication: An API for accessing Public Key Credentials Level 3 is now a W3C Recommendation". https://www.w3.org/news/2026/web-authentication-an-api-for-accessing-public-key-credentials-level-3-is-now-a-w3c-recommendation/ (accessed 2026-11-28)
[^s3]: FIDO Alliance, "User Authentication Specifications Overview". https://fidoalliance.org/specifications/ (accessed 2026-11-28)
[^s4]: Salesforce Help, "Prepare for Phishing-Resistant MFA Enforcement for Privileged Users including Admins". https://help.salesforce.com/s/articleView?id=005321563&language=en_US&type=1 (accessed 2026-11-28)
[^s5]: Salesforce Help, "Enable Passkeys for Identity Verification in Salesforce Orgs". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.security_enable_builtin_authenticator.htm&type=5 (accessed 2026-11-28)
