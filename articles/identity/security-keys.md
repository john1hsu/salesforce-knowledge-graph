---
id: kt:security-keys
type: Feature
title: Security Keys
aliases: [Security Keys (Passkeys), physical passkeys, U2F security key, WebAuthn security key, FIDO security key, hardware security key]
domain: identity
summary: >-
  Physical USB-A, USB-C, Lightning or NFC authenticators that support WebAuthn (FIDO2) or FIDO U2F and serve as a
  phishing-resistant verification method for Salesforce multi-factor authentication and identity verification;
  Salesforce also calls them physical passkeys.
release: "Winter '27"
status: current
broader: [kt:multi-factor-authentication, kt:identity-verification]
related: [kt:salesforce-identity, kt:certificate-and-key-management, kt:passkeys, kt:single-sign-on-saml]
relations:
  - {predicate: implements, object: kt:webauthn}
  - {predicate: mitigates, object: kt:account-takeover}
  - {predicate: alternativeTo, object: kt:salesforce-authenticator}
sources:
  - id: s1
    title: "Security Keys (Passkeys) for MFA"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.mfa_supported_verification_methods_securitykey.htm&type=5
    type: official-docs
    accessed: 2026-11-22
  - id: s2
    title: "Register a Security Key as an Identity Verification Method for Salesforce Orgs"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.security_u2f_register_security_key.htm&type=5
    type: official-docs
    accessed: 2026-11-22
  - id: s3
    title: "Prepare for Phishing-Resistant MFA Enforcement for Privileged Users including Admins"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005321563&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-22
  - id: s4
    title: "Enable Passkeys for Identity Verification in Salesforce Orgs"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.security_enable_builtin_authenticator.htm&type=5
    type: official-docs
    accessed: 2026-11-22
  - id: s5
    title: "Web Authentication: An API for accessing Public Key Credentials Level 3 is now a W3C Recommendation"
    publisher: W3C
    url: https://www.w3.org/news/2026/web-authentication-an-api-for-accessing-public-key-credentials-level-3-is-now-a-w3c-recommendation/
    type: standards-body
    accessed: 2026-11-22
  - id: s6
    title: "Web Authentication: An API for accessing Public Key Credentials - Level 3"
    publisher: W3C
    url: https://www.w3.org/TR/webauthn-3/
    type: standards-body
    accessed: 2026-11-22
created: 2026-11-22
---

# Security Keys

A **security key** is a small physical device (USB-A, USB-C, Lightning or NFC) that a user plugs in or taps to prove who they are. In Salesforce it is one of the supported verification methods for multi-factor authentication (MFA) and identity verification, and Salesforce Help now labels it a "physical passkey". Any key compatible with WebAuthn (FIDO2) or the older FIDO Universal Second Factor (U2F) standard works; Salesforce names the YubiKey and Google Titan Security Key as examples and suggests looking for the FIDO logo.[^s1] Unlike a phone app, a key holds no biometric data, even if it has a touch button.[^s1]

## How it works

WebAuthn, the W3C standard behind modern keys, has an authenticator create a public-key credential for a specific relying party, only with the user's consent. That credential can then be used only by origins that belong to the same relying party.[^s6] The standard calls off-device authenticators reached over USB, Bluetooth or NFC **roaming authenticators**, as opposed to **platform authenticators** built into the device, such as Touch ID or Windows Hello.[^s6] Level 3 of the specification became a W3C Recommendation on 25 August 2026.[^s5] Because the credential is scoped to the real Salesforce origin, a look-alike phishing site cannot obtain a usable response. That is why Salesforce counts security keys as phishing-resistant, unlike push-approval or one-time-code apps.[^s3][^s6]

To register a key, the user opens their personal settings (Advanced User Details), clicks **Register** next to the Security Key (U2F or WebAuthn) field, logs in again, inserts the key and touches it if prompted. Registration can time out, so users should have the key ready before they start.[^s2] Users can self-provision keys with no admin pre-registration, though Salesforce recommends that companies buy, distribute and keep spare keys.[^s1] At later logins, after entering their username and password, the user connects the key and presses its button, and the browser passes the generated credential to Salesforce.[^s1] One key can be registered with several orgs and with other service providers.[^s1]

## Enablement and the phishing-resistant mandate

Security keys are switched on automatically for privileged users and can't be disabled for them; for everyone else an admin must enable the method in Identity Verification settings.[^s1] Once an admin enables security keys or built-in passkeys, all users in the org can use them. Admins can't limit them to admins only.[^s3]

From July 2026 Salesforce began enforcing phishing-resistant MFA for privileged users in paid production and sandbox orgs. Sandboxes started on July 10 and production on July 20, rolling out by release group into September.[^s3] "Privileged" covers the System Administrator profile and anyone granted Modify All Data, View All Data, Customize Application or Author Apex, for both direct UI and SSO logins.[^s3] These users must register a security key or a built-in authenticator, because Salesforce Authenticator and TOTP apps no longer satisfy their MFA requirement.[^s3] Passkeys on the device (Touch ID, Face ID, Windows Hello or a password manager) meet the same requirement, and Salesforce turns them on automatically for employee users under enforcement.[^s4]

## Limits and gotchas

- **Browsers.** WebAuthn keys work in Chrome, Edge Chromium, Firefox and Safari; U2F keys only in Chrome 41+ or Edge Chromium.[^s1]
- **NFC and Data Loader.** NFC keys aren't supported in products built on the Salesforce Platform, and Data Loader OAuth logins can't use security keys.[^s1]
- **Custom domains.** Orgs using domains other than salesforce.com and force.com don't support U2F keys.[^s1]
- **Legacy U2F registrations.** Keys registered before Summer '22 are encrypted with a master key on the Certificate and Key Management page; deleting it locks those users out.[^s1]
- **Sandbox refreshes.** Registered verifiers don't carry over, and SAML SSO settings are disabled after a refresh, so keep at least one admin with a hardware key.[^s3]
- **Lockout recovery.** Another admin can issue a temporary verification code and reset verifiers; with no other admin, Salesforce Support must help.[^s3]

## When to use it (and when not)

Hardware keys are the strongest choice for admins, shared break-glass accounts and sandbox access. They work across devices and don't depend on a phone.[^s1][^s3] Built-in passkeys are more convenient for everyday users on a single trusted laptop or phone.[^s4] Salesforce Authenticator remains acceptable for non-privileged users who want push approvals.[^s3]

## Connections

Security keys are a method within **multi-factor authentication** and the wider **identity verification** framework, and they implement the **WebAuthn** standard.[^s1][^s6] They are a phishing-resistant **alternative to Salesforce Authenticator** and so help **mitigate account takeover**.[^s3] They sit beside **passkeys**, the built-in authenticators that Salesforce Help groups under the same name.[^s4] They also depend on **certificate and key management** for legacy U2F registrations, and they interact with **SAML single sign-on**, where the identity provider must pass a phishing-resistant signal for privileged users.[^s1][^s3]

## Sources
[^s1]: Salesforce Help, "Security Keys (Passkeys) for MFA". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.mfa_supported_verification_methods_securitykey.htm&type=5 (accessed 2026-11-22)
[^s2]: Salesforce Help, "Register a Security Key as an Identity Verification Method for Salesforce Orgs". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.security_u2f_register_security_key.htm&type=5 (accessed 2026-11-22)
[^s3]: Salesforce Help, "Prepare for Phishing-Resistant MFA Enforcement for Privileged Users including Admins". https://help.salesforce.com/s/articleView?id=005321563&language=en_US&type=1 (accessed 2026-11-22)
[^s4]: Salesforce Help, "Enable Passkeys for Identity Verification in Salesforce Orgs". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.security_enable_builtin_authenticator.htm&type=5 (accessed 2026-11-22)
[^s5]: W3C, "Web Authentication: An API for accessing Public Key Credentials Level 3 is now a W3C Recommendation". https://www.w3.org/news/2026/web-authentication-an-api-for-accessing-public-key-credentials-level-3-is-now-a-w3c-recommendation/ (accessed 2026-11-22)
[^s6]: W3C, "Web Authentication: An API for accessing Public Key Credentials - Level 3". https://www.w3.org/TR/webauthn-3/ (accessed 2026-11-22)
