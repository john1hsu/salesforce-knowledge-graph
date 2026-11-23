---
id: kt:time-based-one-time-password
type: ExternalConcept
title: Time-Based One-Time Password
aliases: [TOTP, RFC 6238, TOTP authenticator app, third-party authenticator app, One-Time Password Authenticator]
domain: identity
summary: >-
  The IETF algorithm (RFC 6238) that derives a short, expiring code from a shared secret and the current time;
  in Salesforce it powers third-party authenticator apps such as Google Authenticator, Microsoft Authenticator and
  Authy, plus the offline codes in Salesforce Authenticator, as an MFA verification method that is strong but not
  phishing-resistant.
release: "Winter '27"
status: concept
broader: [kt:multi-factor-authentication]
related: [kt:salesforce-authenticator, kt:identity-verification, kt:session-security-levels, kt:salesforce-identity]
relations:
  - {predicate: dependsOn, object: kt:hmac-based-one-time-password}
  - {predicate: consumedBy, object: kt:salesforce-authenticator}
  - {predicate: mitigates, object: kt:account-takeover}
  - {predicate: dependsOn, object: kt:nist-digital-identity-guidelines}
  - {predicate: contrastsWith, object: kt:security-keys}
sources:
  - id: s1
    title: "RFC 6238: TOTP: Time-Based One-Time Password Algorithm"
    publisher: IETF / RFC Editor
    url: https://rfc-editor.org/rfc/rfc6238
    type: standards-body
    accessed: 2026-11-23
  - id: s2
    title: "NIST SP 800-63B-4: Authenticators"
    publisher: NIST
    url: https://pages.nist.gov/800-63-4/sp800-63b/authenticators
    type: standards-body
    accessed: 2026-11-23
  - id: s3
    title: "Multi-Factor Authentication for Salesforce"
    publisher: Salesforce Security
    url: https://security.salesforce.com/mfa
    type: official-docs
    accessed: 2026-11-23
  - id: s4
    title: "Enhance Security with MFA Verification (User Authentication module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/modules/identity_login/units/identity_login_2fa
    type: official-learning
    accessed: 2026-11-23
  - id: s5
    title: "Verify Your Identity with a TOTP Authenticator App (Salesforce Security Guide, Winter '21)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.228.0.securityImplGuide.meta/securityImplGuide/add_time-based_token.htm
    type: official-docs
    accessed: 2026-11-23
created: 2026-11-23
---

# Time-Based One-Time Password

A time-based one-time password (TOTP) is a short numeric code that an authenticator computes from a secret it shares with the verifier and the current time, so the code changes every few seconds and is useless once its window passes. The algorithm is RFC 6238, an Informational RFC published in May 2011 by authors from Verisign, Diversinet, Symantec and Portwise.[^s1] Salesforce lists third-party TOTP authenticator apps (Google Authenticator, Microsoft Authenticator and Authy are its examples) as one of the verification methods that satisfy its multi-factor authentication requirement, alongside Salesforce Authenticator push approvals, security keys and built-in biometric authenticators.[^s3][^s4]

## How it works

TOTP is a time-based variant of HOTP (RFC 4226): instead of an event counter, it feeds a time-step number into the same HMAC-and-truncate construction. The step number is the current Unix time minus a start time T0, divided by a step size X and rounded down; the defaults are T0 = 0 (the Unix epoch) and X = 30 seconds, and the RFC recommends 30 seconds as the default step.[^s1] HOTP is built on HMAC-SHA-1, and TOTP implementations may also use HMAC-SHA-256 or HMAC-SHA-512.[^s1] The RFC's own test vectors use 8-digit codes, while NIST allows OTP output to be truncated to as few as six decimal digits.[^s1][^s2]

Because the prover and verifier compute the code independently, both must hold the same per-user secret. The RFC says keys should be random (or derived with a key derivation function), should match the HMAC output length, and should be provisioned over a secure channel such as TLS.[^s1] Implementations must also handle time values beyond 32 bits so they keep working after 2038.[^s1]

## Using TOTP with Salesforce

A user registers an app from their own settings: under Advanced User Details, the **App Registration: One-Time Password Authenticator** row has a Connect link; after re-authenticating, the user scans a QR code (or types the displayed key into the app) and confirms by entering the current code.[^s5] The Security Guide states that any app implementing RFC 6238 works, and Salesforce emails the user whenever a new verification method is added to the account, whether by the user or an admin.[^s5]

Salesforce Authenticator itself also shows TOTP codes, which users type in when push-based automation isn't available, for example without connectivity.[^s4] The Winter '21 edition of the Security Guide allowed up to two OTP-generating apps per user: Salesforce Authenticator plus one other app.[^s5] Admins turn MFA on for direct UI logins in Identity Verification settings, and MFA logins count as High Assurance in session security levels, which is what step-up checks for reports, dashboards and connected apps look for.[^s4]

## Limits and gotchas

- Clock drift: the RFC recommends allowing at most one time step for network delay and capping how far out of sync a validator will accept; two backward steps at 30 seconds tolerate about 89 seconds of drift.[^s1]
- Replay: a verifier must refuse a code that has already been accepted once, even inside its validity window, according to both RFC 6238 and NIST.[^s1][^s2]
- Brute force: NIST requires rate limiting when the OTP output is shorter than 64 bits, which covers every 6- or 8-digit TOTP code.[^s2]
- Phishing: NIST states plainly that OTP authentication is "not phishing-resistant", because a fake login page can relay a live code.[^s2]
- Secret strength: for single-factor OTP devices, the secret key and algorithm must give at least 112 bits of security strength, and a clock-based nonce must change at least once every two minutes.[^s2]

## When to use it (and when not)

TOTP apps are the most portable MFA option: they work offline, run on phones, desktops and browser extensions, and cost nothing, which makes them a good choice for users who can't or won't install Salesforce Authenticator.[^s3] They lack Salesforce Authenticator's push approvals and location-based automation, so every login means typing a code.[^s4] For admins and other privileged users, prefer security keys or built-in authenticators, since NIST rules out OTPs where phishing resistance is required.[^s2][^s3]

## Connections

TOTP sits under **multi-factor authentication** as one of its accepted verification methods, and it depends on the counter-based **HOTP** algorithm it extends.[^s1][^s3] **Salesforce Authenticator** consumes it to generate offline codes, while **security keys** are the contrasting, phishing-resistant choice.[^s2][^s4] NIST's **digital identity guidelines** (SP 800-63) set the requirements a TOTP verifier must meet, and a second factor of this kind is a main control against **account takeover**.[^s2][^s3] **Identity verification** and **session security levels** decide when Salesforce asks for the code and how much assurance a TOTP login grants.[^s4][^s5]

## Sources
[^s1]: IETF / RFC Editor, "RFC 6238: TOTP: Time-Based One-Time Password Algorithm". https://rfc-editor.org/rfc/rfc6238 (accessed 2026-11-23)
[^s2]: NIST, "SP 800-63B-4: Authenticators". https://pages.nist.gov/800-63-4/sp800-63b/authenticators (accessed 2026-11-23)
[^s3]: Salesforce Security, "Multi-Factor Authentication for Salesforce". https://security.salesforce.com/mfa (accessed 2026-11-23)
[^s4]: Trailhead, "Enhance Security with MFA Verification". https://trailhead.salesforce.com/en/modules/identity_login/units/identity_login_2fa (accessed 2026-11-23)
[^s5]: Salesforce Developers, "Verify Your Identity with a TOTP Authenticator App" (Security Guide, Winter '21). https://developer.salesforce.com/docs/atlas.en-us.228.0.securityImplGuide.meta/securityImplGuide/add_time-based_token.htm (accessed 2026-11-23)
