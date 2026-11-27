---
id: kt:passkeys
type: Feature
title: Passkeys
aliases: [built-in authenticators, built-in authenticator (passkey), platform authenticator passkeys, passwordless login with passkeys]
domain: identity
summary: >-
  FIDO public-key credentials unlocked with a device's own screen lock (Touch ID, Face ID, Windows Hello, a device
  PIN or a password manager); in Salesforce they serve as a phishing-resistant MFA and identity verification method,
  the default registration choice for employee users, and the basis of passwordless shopper login in B2C Commerce.
release: "Winter '27"
status: current
broader: [kt:multi-factor-authentication, kt:identity-verification]
related: [kt:security-keys, kt:lightning-login, kt:single-sign-on-saml, kt:salesforce-authenticator]
relations:
  - {predicate: implements, object: kt:webauthn}
  - {predicate: mitigates, object: kt:account-takeover}
  - {predicate: consumedBy, object: kt:b2c-commerce}
sources:
  - id: s1
    title: "Enable Passkeys for Identity Verification in Salesforce Orgs"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.security_enable_builtin_authenticator.htm&type=5
    type: official-docs
    accessed: 2026-11-27
  - id: s2
    title: "Recognize Passkey Creation Prompt Behavior"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=xcloud.mfa_passkeys_prompts_understand.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-27
  - id: s3
    title: "Resolve Passkey Login Issues in Salesforce"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005390721&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-27
  - id: s4
    title: "MFA and Phishing-Resistant MFA Post-Enforcement Passkey Prompts and Extension Behavior"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=005388907&type=1
    type: official-docs
    accessed: 2026-11-27
  - id: s5
    title: "Passkeys"
    publisher: FIDO Alliance
    url: https://fidoalliance.org/passkeys/
    type: standards-body
    accessed: 2026-11-27
  - id: s6
    title: "Passwordless Login with Passkeys (B2C Commerce SLAS)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/commerce/commerce-api/guide/slas-passwordless-login-passkey.html
    type: official-docs
    accessed: 2026-11-27
created: 2026-11-27
---

# Passkeys

A **passkey** is a FIDO authentication credential bound to a user's account and kept on a phone, a computer or a hardware key; the user unlocks it with the same biometric, PIN or pattern that unlocks the device.[^s5] The FIDO Alliance uses "passkey" as a cross-platform, general term and describes the underlying FIDO2 standard as built on public-key cryptography, which is what makes passkeys phishing-resistant.[^s5] Salesforce Help calls the on-device kind **built-in authenticators (passkeys)**: users log in and satisfy MFA with Touch ID, Face ID, Windows Hello, a device password or a password manager.[^s1] Physical USB or NFC keys are covered separately as security keys.

## How it works

Passkeys come in two flavours. **Synced passkeys** are copied between a user's devices by a passkey provider with end-to-end encryption, while **device-bound passkeys** never leave one device; hardware security keys are the classic device-bound example.[^s5] In Salesforce that difference matters: a synced passkey in a password manager follows the user to a new laptop, whereas a device-bound one needs a fresh registration on each device, usually after an admin issues a temporary verification code.[^s3] Users can also scan a QR code to use a passkey stored on their phone.[^s3]

An admin turns passkeys on in Setup under **Identity Verification** by selecting the built-in authenticator option; this needs both Customize Application and Manage Users, and the setting exists in all editions in Lightning and Classic.[^s1] Once MFA enforcement reaches an org, Salesforce enables passkeys for every employee user automatically and the setting can no longer be switched off; before that, admins can enable it to test.[^s1] Creating a passkey needs Chrome, Edge, Firefox or Safari plus a device unlock method such as Face ID, Touch ID, a Windows Hello PIN or fingerprint.[^s3]

## Passkey-first MFA and enforcement

Salesforce now defaults every employee user to a passkey-first MFA registration flow.[^s2] Privileged users, who must use phishing-resistant MFA, get the passkey prompt on direct login and on SSO logins where the identity provider doesn't meet Salesforce's MFA requirements, and they can't pick another method. Other users see the passkey prompt first but may choose Salesforce Authenticator or a third-party authenticator app instead.[^s2] Passkeys fully meet the phishing-resistant requirement for privileged users.[^s1]

For SSO, Salesforce reads the AMR/ACR values the identity provider sends. An accepted signal lets the user straight in; without one, privileged users are told their account needs a passkey.[^s4] SAML AMR values are matched case-insensitively, but OIDC AMR values are case-sensitive, a frequent cause of unexpected prompts.[^s4]

## Limits and gotchas

- **Lockout recovery.** Temporary codes last 1 to 24 hours, one active per user, and up to six per user per hour.[^s3]
- **Keep two admins.** Keep at least two users with the permission to manage MFA in the UI; a sole admin who is locked out must contact Support.[^s3]
- **Sandbox refreshes.** Refreshed sandboxes don't inherit all verification settings, so users are asked to create a new passkey and SAML SSO must be re-enabled.[^s2]
- **Removed bypass permission.** After enforcement, code that references the MFA-waiver permission field can fail to compile and block package installs or upgrades.[^s2]
- **External users.** From August 2026, Experience Cloud and Chatter external users no longer see the create-a-passkey prompt, and orgs using passwordless passkey login should review that setting.[^s3]
- **High Assurance.** MFA enforcement alone doesn't make a session High Assurance; at least one method must be assigned to that category in Session Settings.[^s4]
- **Integrations.** Web-server, user-agent and username-password OAuth flows and SOAP login() still involve UI login and MFA, so Salesforce points integrations to JWT bearer or client credentials.[^s3]

## Passwordless shopper login in B2C Commerce

The Shopper Login and API Access Service (SLAS) lets B2C Commerce shoppers sign in with FIDO2 passkeys on platform or hardware authenticators.[^s6] The SLAS client is configured with a WebAuthn relying party ID and allowed origins, the shopper's identity is first verified (for example by an emailed one-time password), and registration and login each run a start call, the browser WebAuthn ceremony and a finish call, after which SLAS issues a shopper JWT.[^s6] Shoppers can keep their passwords and add passkeys, so stores can migrate gradually.[^s6]

## When to use it (and when not)

Passkeys are the convenient everyday phishing-resistant choice for users who work on trusted devices, especially when synced through a password manager.[^s1][^s3] Hardware security keys suit break-glass admins and users who move between many machines, and Salesforce Authenticator remains an option only for non-privileged users.[^s2][^s3]

## Connections

Passkeys are a method within **multi-factor authentication** and **identity verification**, implementing **WebAuthn**, the browser half of FIDO2.[^s1][^s5] They sit beside **security keys**, the device-bound hardware form, and are the phishing-resistant **alternative to Salesforce Authenticator** that helps **mitigate account takeover**.[^s2][^s5] They interact with **SAML single sign-on** through AMR/ACR signals, and **Lightning Login** can conflict with them at login.[^s3][^s4] **B2C Commerce** consumes them for passwordless shopper login.[^s6]

## Sources
[^s1]: Salesforce Help, "Enable Passkeys for Identity Verification in Salesforce Orgs". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.security_enable_builtin_authenticator.htm&type=5 (accessed 2026-11-27)
[^s2]: Salesforce Help, "Recognize Passkey Creation Prompt Behavior". https://help.salesforce.com/s/articleView?id=xcloud.mfa_passkeys_prompts_understand.htm&language=en_US&type=5 (accessed 2026-11-27)
[^s3]: Salesforce Help, "Resolve Passkey Login Issues in Salesforce". https://help.salesforce.com/s/articleView?id=005390721&language=en_US&type=1 (accessed 2026-11-27)
[^s4]: Salesforce Help, "MFA and Phishing-Resistant MFA Post-Enforcement Passkey Prompts and Extension Behavior". https://help.salesforce.com/s/articleView?language=en_US&id=005388907&type=1 (accessed 2026-11-27)
[^s5]: FIDO Alliance, "Passkeys". https://fidoalliance.org/passkeys/ (accessed 2026-11-27)
[^s6]: Salesforce Developers, "Passwordless Login with Passkeys (B2C Commerce SLAS)". https://developer.salesforce.com/docs/commerce/commerce-api/guide/slas-passwordless-login-passkey.html (accessed 2026-11-27)
