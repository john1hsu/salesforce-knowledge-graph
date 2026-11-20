---
id: kt:salesforce-authenticator
type: Product
title: Salesforce Authenticator
aliases: [Salesforce Authenticator app, Salesforce Authenticator mobile app, App Registration Salesforce Authenticator]
domain: identity
summary: >-
  Salesforce's free iOS and Android authenticator app, used as a second factor for multi-factor authentication:
  it approves logins by push notification, can auto-approve repeat requests that match a learned pattern
  (including location), and generates 6-digit TOTP codes for offline use and for non-Salesforce accounts.
release: "Winter '27"
status: current
broader: [kt:multi-factor-authentication]
related: [kt:identity-verification, kt:salesforce-identity, kt:login-ip-ranges-and-trusted-ip-ranges, kt:session-security-levels]
relations:
  - {predicate: mitigates, object: kt:account-takeover}
  - {predicate: implements, object: kt:time-based-one-time-password}
  - {predicate: consumedBy, object: kt:heroku}
  - {predicate: alternativeTo, object: kt:security-keys}
sources:
  - id: s1
    title: "Salesforce Authenticator for MFA"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=xcloud.mfa_supported_verification_methods_sfa.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-20
  - id: s2
    title: "Automate Multi-Factor Authentication with Salesforce Authenticator"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.salesforce_authenticator_automate_trusted_requests.htm&type=5
    type: official-docs
    accessed: 2026-11-20
  - id: s3
    title: "Use Salesforce Authenticator with Your Other Accounts"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.salesforce_authenticator_totp.htm&type=5
    type: official-docs
    accessed: 2026-11-20
  - id: s4
    title: "How to Set Up Salesforce Authenticator for MFA"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=002620371&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-20
  - id: s5
    title: "Secure Your Users' Identity (Enhance Security with MFA Verification)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/content/learn/modules/identity_login/identity_login_2fa
    type: official-learning
    accessed: 2026-11-20
  - id: s6
    title: "Salesforce Authenticator"
    publisher: Heroku Dev Center
    url: https://devcenter.heroku.com/articles/salesforceauthenticator
    type: official-docs
    accessed: 2026-11-20
created: 2026-11-20
---

# Salesforce Authenticator

Salesforce Authenticator is Salesforce's free mobile app for completing multi-factor authentication (MFA). After a user enters a username and password, the app receives a push notification; the user checks the request and taps to approve it.[^s1] It is available for every Salesforce product that offers MFA, installs from the Apple App Store or Google Play, and is registered per user as an identity verification method.[^s1][^s4] Besides push, the app generates time-based one-time passcodes (TOTP) that work without a mobile data connection.[^s1] Salesforce strongly recommends protecting the phone itself with a PIN or biometric lock.[^s1]

## How registration works

A user picks "Use the Salesforce Authenticator mobile app" at the verification-method prompt; the app then shows a two-word phrase, the user types it into the browser, and confirms the connection in the app.[^s4][^s5] The setup steps also ask users to allow notifications and to back up their accounts.[^s4] On the user record this appears as the **App Registration: Salesforce Authenticator** entry.[^s5] The same pairing pattern applies to Heroku, where the app sends a push on login and offers 6-digit codes when the device is offline.[^s6]

## Push, details and automation

Each push shows enough context to judge the request: the service, username, action, the client (browser, device or app) and an approximate location.[^s2][^s5] Users can also block unfamiliar activity instead of approving it.[^s6]

The app can automate approvals. Automation compares five factors of an incoming request (service, username, action, location and client) with earlier requests, and auto-approves a request whose factors all match one approved three times before.[^s2] It requires at least one connected Salesforce-ecosystem account, such as Salesforce, Heroku, MuleSoft, Marketing Cloud or Tableau, and an admin must allow it.[^s2] Admins can restrict automation to trusted IP addresses or switch it off in Identity Verification settings.[^s5] Users review and delete saved trusted requests from the account details in the app.[^s5] Salesforce says location data stays in the app, and automation works best with precise, always-on location and background access.[^s2]

## TOTP codes and other accounts

Every connected account gets its own 6-digit code that rotates every 30 seconds.[^s3] This is the fallback when push is unavailable or the phone has no data.[^s2] Because the codes follow the TOTP standard, the app also works as a generic authenticator for any outside service that supports TOTP MFA, often added by scanning the service's QR code.[^s3] Accounts that use only TOTP codes don't show the automation (Einstein) icon.[^s3]

## Gotchas

- **Back up before changing phones.** Without a backup and without the old device, the user cannot recover; an admin must disconnect the registration first.[^s4][^s5]
- **Users can't self-reset.** Disconnecting the app from a locked-out user's account is an admin step, so help-desk runbooks should cover it.[^s4]
- **Automation can degrade.** Private browsing, virtual desktops and switching browsers reduce match rates, and very high traffic can briefly delay push.[^s2]
- **Not phishing-resistant for admins.** From June 2026, privileged users need phishing-resistant MFA, and Salesforce recommends passkeys or security keys.[^s1]

## When to use it

For most standard users, the app is the lowest-friction way to meet the MFA requirement: it's free and, once trained, approves routine logins automatically.[^s1][^s2] For System Administrators and other privileged users, pair it with or replace it by a FIDO security key or passkey, since the June 2026 enforcement requires phishing-resistant MFA for them.[^s1] Third-party TOTP apps also satisfy MFA but lack push and automation.[^s5]

## Connections

The app is one verifier within **multi-factor authentication** and the broader **identity verification** framework of **Salesforce Identity**. Each verification attempt is recorded in Identity Verification History.[^s1][^s5] Its push-plus-context design helps defend against **account takeover** from stolen passwords, and its offline codes implement **TOTP**.[^s1][^s3] Admins can tie automation to **trusted IP ranges**, and MFA can be required as High Assurance via **session security levels**.[^s5] The same app secures **Heroku** logins.[^s6] For privileged users, **security keys** are the recommended alternative.[^s1]

## Sources
[^s1]: Salesforce Help, "Salesforce Authenticator for MFA". https://help.salesforce.com/s/articleView?id=xcloud.mfa_supported_verification_methods_sfa.htm&language=en_US&type=5 (accessed 2026-11-20)
[^s2]: Salesforce Help, "Automate Multi-Factor Authentication with Salesforce Authenticator". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.salesforce_authenticator_automate_trusted_requests.htm&type=5 (accessed 2026-11-20)
[^s3]: Salesforce Help, "Use Salesforce Authenticator with Your Other Accounts". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.salesforce_authenticator_totp.htm&type=5 (accessed 2026-11-20)
[^s4]: Salesforce Help, "How to Set Up Salesforce Authenticator for MFA". https://help.salesforce.com/s/articleView?id=002620371&language=en_US&type=1 (accessed 2026-11-20)
[^s5]: Trailhead, "Secure Your Users' Identity". https://trailhead.salesforce.com/en/content/learn/modules/identity_login/identity_login_2fa (accessed 2026-11-20)
[^s6]: Heroku Dev Center, "Salesforce Authenticator". https://devcenter.heroku.com/articles/salesforceauthenticator (accessed 2026-11-20)
