---
id: kt:identity-verification
type: SecurityControl
title: Identity Verification
aliases: [Salesforce identity verification, device activation, Identity Verification History, verification methods]
domain: identity
summary: >-
  Salesforce's framework for making a user prove they own an account — at login, when activating an unrecognized
  device or browser, or before a sensitive action — using a registered verification method such as a passkey,
  security key, Salesforce Authenticator, a TOTP app or (for external users) SMS or email codes. Every attempt is
  logged in Identity Verification History for six months.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity]
related: [kt:multi-factor-authentication, kt:session-security-levels, kt:login-ip-ranges-and-trusted-ip-ranges, kt:experience-cloud-identity, kt:login-flows]
relations:
  - {predicate: mitigates, object: kt:account-takeover}
  - {predicate: hasPart, object: kt:multi-factor-authentication}
  - {predicate: queriedWith, object: kt:soql}
sources:
  - id: s1
    title: "Identity Verification Overview"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.security_identity_verification_concept_overview.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-13
  - id: s2
    title: "Methods for Verifying Your Identity"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=activating_computer.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-13
  - id: s3
    title: "Configure the MFA Verification Methods Available to Your Users for Salesforce Orgs"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.mfa_config_available_verifiers.htm&amp=&type=5
    type: official-docs
    accessed: 2026-11-13
  - id: s4
    title: "VerificationHistory (Object Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_verificationhistory.htm
    type: official-docs
    accessed: 2026-11-13
  - id: s5
    title: "Create Identity Verification Reports and Dashboards (Identity for Mobile-Centric Customers)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/identity-for-mobile-centric-customers/identity_mfi_reports
    type: official-learning
    accessed: 2026-11-13
created: 2026-11-13
---

# Identity Verification

**Identity verification** is Salesforce's general mechanism for asking a user to present a registered verification method that proves they are the real owner of an account. It gates more than the login screen: Salesforce uses it when a user logs in, activates a new device, or reaches a resource that demands stronger proof.[^s1] Multi-factor authentication is the best-known use of the framework, but identity verification also covers device activation, step-up challenges, admin-issued temporary codes and the audit trail of every challenge.[^s1][^s4]

## When Salesforce challenges a user

Salesforce describes three main triggers:[^s1]

- **Multi-factor authentication** — required for direct and SSO logins and switched on automatically for direct logins to production orgs; a method is required at every login, recognized device or not.[^s1]
- **Device activation** — a challenge when a user logs in from a browser, app or IP address Salesforce doesn't recognize.[^s1][^s2]
- **Step-up authentication** — a challenge when a user tries something that needs a higher session security level, such as a High Assurance resource.[^s1]

Once MFA is enabled, device activation and step-up no longer fire separately: every login already demands a verifier and already yields a high-assurance session.[^s1]

The `VerificationHistory` object shows the full range of triggers. Its **Policy** (Triggered By) values include DeviceActivation, TwoFactorAuthentication, HighAssurance, ProfilePolicy, PageAccess, CustomApex, LightningLogin and PasswordlessLogin. Its **Activity** values show what the user was doing — logging in, opening a connected app or external client app, exporting or accessing reports, opening a list view, changing an email address, or registering a new verifier.[^s4]

## Verification methods and precedence

Salesforce prompts for the most secure method the user has registered, though the user can pick another. The order runs from most to least secure:[^s2]

1. **Built-in authenticator (passkey)** — a device biometric; it works only on the device where it was registered.[^s2]
2. **Security key** — a physical U2F or WebAuthn key.[^s1][^s2]
3. **Salesforce Authenticator** — push approval or offline one-time codes.[^s1][^s2]
4. **Third-party authenticator app** — TOTP codes from apps such as Google or Microsoft Authenticator.[^s2]
5. **SMS one-time password** — only for external users on customer or partner Experience Cloud sites, with a verified number.[^s2]
6. **Email one-time password** — also limited to external Experience Cloud users. The code is valid for 24 hours.[^s2]

An admin can also generate a **temporary verification code** for a user who has lost their device.[^s1] SMS verification needs the Identity Verification Credits add-on license.[^s4] Salesforce recommends that every user register at least two methods as a fallback.[^s2]

Admin control over methods depends on the org's age. In orgs created before Summer '25, an admin must turn on passkeys and security keys, while authenticator apps are available automatically. In newer orgs every method is allowed by default. Once MFA is enforced, passkeys and security keys are switched on for all employee users and the setting can't be turned off.[^s3] Salesforce steers privileged users toward these phishing-resistant methods.[^s3]

## Monitoring and reporting

Each attempt is written to **Identity Verification History** (`VerificationHistory`, API 36.0+), which keeps six months of records. Each record holds the user, the activity and the policy that triggered the challenge, along with the method used, the status, IP address, geolocation and related login history row.[^s4] Status values separate outcomes such as Succeeded, Denied, ReportedDenied, FailedInvalidCode and FailedTooManyAttempts, so failed and user-rejected challenges can be told apart.[^s4] The object needs the Manage Users permission and supports query and delete, so it can be read with SOQL as well as viewed in Setup.[^s4]

For dashboards, Trailhead builds a custom report type with Identity Verification History as its primary object, in the Administrative Reports category, and joins related Login History and user fields. The standard **Identity Verification Methods** report lists the verifiers each user has registered.[^s5]

## Gotchas

- Users with no registered method are sent to register one at their next login when MFA is on, so plan for it during rollouts.[^s2]
- A passkey works only on the device where it was registered, so users who move between machines need a second method.[^s2]
- Six months of history may fall short of audit retention needs, so export it if longer evidence is required.[^s4]

## Connections

Identity verification sits under **Salesforce Identity** and contains **multi-factor authentication** as its login-time use.[^s1] Its step-up path depends on **session security levels**, and device activation keys off unrecognized browsers and IP addresses, which links it to **login and trusted IP ranges**.[^s1][^s2] SMS and email codes are reserved for external users, which ties the feature to **Experience Cloud identity**.[^s2] By demanding a second proof at login, on new devices and before sensitive actions, it **mitigates account takeover**. History records are **queried with SOQL** or reported on for monitoring.[^s4][^s5] **Login flows** are a related, customizable way to add checks at login.

## Sources
[^s1]: Salesforce Help, "Identity Verification Overview". https://help.salesforce.com/s/articleView?id=sf.security_identity_verification_concept_overview.htm&language=en_US&type=5 (accessed 2026-11-13)
[^s2]: Salesforce Help, "Methods for Verifying Your Identity". https://help.salesforce.com/s/articleView?id=activating_computer.htm&language=en_US&type=5 (accessed 2026-11-13)
[^s3]: Salesforce Help, "Configure the MFA Verification Methods Available to Your Users for Salesforce Orgs". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.mfa_config_available_verifiers.htm&amp=&type=5 (accessed 2026-11-13)
[^s4]: Salesforce Developers, "VerificationHistory" (Object Reference). https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_verificationhistory.htm (accessed 2026-11-13)
[^s5]: Trailhead, "Identity for Mobile-Centric Customers" unit on identity verification reports. https://trailhead.salesforce.com/content/learn/modules/identity-for-mobile-centric-customers/identity_mfi_reports (accessed 2026-11-13)
