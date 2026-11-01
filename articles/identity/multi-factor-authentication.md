---
id: kt:multi-factor-authentication
type: SecurityControl
title: Multi-Factor Authentication
aliases: [MFA, Salesforce MFA, two-factor authentication, 2FA, MFA requirement, phishing-resistant MFA]
domain: identity
summary: >-
  Salesforce's requirement and built-in capability that users prove their identity with two or more factors at
  login — a password plus an authenticator app, security key or built-in biometric. Required for UI logins since
  2022, enforced for all users from June 2026, with phishing-resistant methods required for privileged users.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity]
related: [kt:single-sign-on-saml, kt:connected-apps, kt:external-client-apps, kt:my-domain, kt:experience-cloud-identity]
relations:
  - {predicate: mitigates, object: kt:account-takeover}
  - {predicate: implements, object: kt:nist-digital-identity-guidelines}
  - {predicate: configuredVia, object: kt:session-security-levels}
  - {predicate: coveredBy, object: kt:identity-and-access-management-architect-certification}
sources:
  - id: s1
    title: "Check That Your Implementation Satisfies the MFA Requirement"
    publisher: Salesforce Security
    url: https://security.salesforce.com/mfa-requirement-check
    type: official-docs
    accessed: 2026-11-01
  - id: s2
    title: "Prepare Your Org for Salesforce MFA Enforcement"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2026/prepare-your-org-for-salesforce-mfa-enforcement
    type: official-blog
    accessed: 2026-11-01
  - id: s3
    title: "Secure Your Users' Identity (User Authentication module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/identity_login/identity_login_2fa
    type: official-learning
    accessed: 2026-11-01
  - id: s4
    title: "Multi-Factor Authentication (Security Implementation Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.232.0.securityImplGuide.meta/securityImplGuide/security_overview_2fa.htm
    type: official-docs
    accessed: 2026-11-01
  - id: s5
    title: "NIST SP 800-63B-4: Authentication Assurance Levels"
    publisher: NIST
    url: https://pages.nist.gov/800-63-4/sp800-63b/aal
    type: standards-body
    accessed: 2026-11-01
created: 2026-11-01
---

# Multi-Factor Authentication

Multi-factor authentication (MFA) in Salesforce means a user must present two or more independent pieces of evidence to log in: typically something they know (username and password) plus something they possess, such as a phone running an authenticator app or a physical security key.[^s1][^s3] Salesforce treats the older term two-factor authentication (2FA) as a subset of MFA and uses the two interchangeably.[^s3][^s4] Because a stolen password alone no longer opens the org, MFA is the platform's primary defence against phishing-driven account takeover.[^s4]

## Requirement and enforcement timeline

Salesforce has contractually required MFA for direct logins to the Salesforce UI since February 1, 2022, and MFA is on by default for production orgs.[^s1][^s4] For several years admins could still toggle the org-wide setting or grant an exemption permission to specific users. Starting June 26, 2026, MFA is enforced for all users: the setting "Require multi-factor authentication (MFA) for all direct UI logins" can no longer be changed, and the "Waive Multi-Factor Authentication for Exempt Users" option is removed, so formerly exempt users are prompted to enroll at their next login.[^s2]

The same change requires **phishing-resistant MFA** for privileged users — System Administrators and anyone holding Modify All Data, View All Data, Customize Application or Author Apex.[^s2] Other Salesforce products (Heroku, Marketing Cloud, MuleSoft Anypoint Platform, Tableau Cloud, B2C Commerce) have their own MFA implementations described on the Salesforce security site.[^s1]

## Verification methods

Salesforce accepts four families of verifiers for direct logins:[^s1][^s3]

- **Salesforce Authenticator** — a free mobile app that approves logins via push notification.[^s1][^s3]
- **Third-party TOTP apps** — apps such as Google Authenticator, Microsoft Authenticator or Authy that generate time-based one-time codes.[^s1][^s3]
- **Security keys** — USB, Lightning or NFC tokens that support FIDO U2F or WebAuthn, such as YubiKey or Google Titan.[^s1][^s3]
- **Built-in authenticators** — platform biometrics or screen locks such as Windows Hello, Touch ID and Face ID.[^s1][^s3]

For phishing-resistant MFA, Salesforce points admins to the last two (FIDO-based keys and built-in authenticators); passkeys can additionally be enabled for passwordless login.[^s2] Admins switch these on under Setup > Identity Verification, and users register devices in their advanced user details.[^s2] Salesforce recommends each user register more than one method, and that privileged users hold two phishing-resistant factors.[^s2][^s4]

## How it works with SSO

If users reach Salesforce through single sign-on, MFA must still happen somewhere: either at the identity provider or with Salesforce's own free MFA.[^s1] Salesforce reads the authentication-method (AMR) or authentication-context (ACR) signals the IdP passes; when they show MFA already occurred, users are not prompted again, otherwise they are asked to set up a Salesforce verification method. For privileged users, the IdP must pass a claim showing a phishing-resistant (FIDO2) method was used.[^s2]

## Beyond the login: step-up and API

Admins can also demand MFA in further situations — API access, specific connected apps, sensitive reports or dashboards, and custom login flows — by placing MFA in the High Assurance session security level (Setup > Session Settings) and requiring that level where needed.[^s3] Login results are reviewable in Identity Verification History.[^s3]

## Gotchas

- Plan a **break-glass** recovery: an admin can issue a Temporary Verification Code to a locked-out user after verifying their identity.[^s2]
- Test-automation and other accounts that relied on the exemption permission (a documented use case for it) must now enroll or be redesigned, since the waiver no longer exempts anyone.[^s2][^s3]
- An IdP that does not emit AMR/ACR claims will cause duplicate prompts after SSO.[^s2]

## Connections

MFA is a control within **Salesforce Identity** and interacts closely with **single sign-on (SAML)**, because the IdP's assertion determines whether Salesforce re-prompts.[^s1][^s2] Integrations authenticate through **connected apps** or **external client apps** rather than interactive MFA, while high-assurance step-up is configured through session security levels.[^s3] Salesforce's split between ordinary and phishing-resistant MFA mirrors NIST SP 800-63B, where AAL2 requires two factors and a phishing-resistant option, and AAL3 requires phishing-resistant cryptographic authentication.[^s5] Org login URLs from **My Domain** and external-user logins in **Experience Cloud identity** are related surfaces where identity verification is configured.[^s3]

## Sources
[^s1]: Salesforce Security, "Check That Your Implementation Satisfies the MFA Requirement". https://security.salesforce.com/mfa-requirement-check (accessed 2026-11-01)
[^s2]: Salesforce Admins Blog, "Prepare Your Org for Salesforce MFA Enforcement". https://admin.salesforce.com/blog/2026/prepare-your-org-for-salesforce-mfa-enforcement (accessed 2026-11-01)
[^s3]: Trailhead, "Secure Your Users' Identity". https://trailhead.salesforce.com/content/learn/modules/identity_login/identity_login_2fa (accessed 2026-11-01)
[^s4]: Salesforce Developers, "Multi-Factor Authentication" (Security Implementation Guide). https://developer.salesforce.com/docs/atlas.en-us.232.0.securityImplGuide.meta/securityImplGuide/security_overview_2fa.htm (accessed 2026-11-01)
[^s5]: NIST, "SP 800-63B-4: Authentication Assurance Levels". https://pages.nist.gov/800-63-4/sp800-63b/aal (accessed 2026-11-01)
