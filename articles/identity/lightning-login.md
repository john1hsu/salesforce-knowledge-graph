---
id: kt:lightning-login
type: Feature
title: Lightning Login
aliases: [Lightning Login for Password-Free Logins, password-free login, Salesforce passwordless login, Lightning Login User permission]
domain: identity
summary: >-
  Salesforce's password-free login method for internal users: an enrolled user enters only a username and
  approves the login in the Salesforce Authenticator app, which also counts toward Salesforce's MFA requirement.
release: "Winter '27"
status: current
broader: [kt:multi-factor-authentication, kt:salesforce-identity]
related: [kt:salesforce-authenticator, kt:session-security-levels, kt:identity-verification, kt:login-history, kt:password-policies]
relations:
  - {predicate: dependsOn, object: kt:salesforce-authenticator}
  - {predicate: configuredVia, object: kt:permission-sets}
  - {predicate: configuredVia, object: kt:profiles}
  - {predicate: mitigates, object: kt:account-takeover}
  - {predicate: alternativeTo, object: kt:single-sign-on-saml}
sources:
  - id: s1
    title: "Enable Lightning Login"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.security_ll_enable.htm&type=5
    type: official-docs
    accessed: 2026-11-21
  - id: s2
    title: "Enable Lightning Login Securely with the Authenticator App (MFA and SSO Settings Superbadge)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/es-MX/content/learn/superbadges/superbadge-mfa-sso-settings/superbadge-mfa-sso-settings_lightning-login
    type: official-learning
    accessed: 2026-11-21
  - id: s3
    title: "Demo Lightning Login for Your Company"
    publisher: Salesforce Admins
    url: https://admin.salesforce.com/blog/2017/demo-lightning-login-company
    type: official-blog
    accessed: 2026-11-21
  - id: s4
    title: "Identity | Salesforce Developer Center"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/developer-centers/identity
    type: official-docs
    accessed: 2026-11-21
created: 2026-11-21
---

# Lightning Login

Lightning Login is Salesforce's built-in, password-free way for internal users to log in to an org. Instead of typing a password, an enrolled user enters a username and then approves the login on a mobile device through the Salesforce Authenticator app. Salesforce positions it as giving users the speed, convenience and security of password-free logins, and lists it alongside single sign-on, MFA, login flows and password policies among the identity features of the platform.[^s1][^s4] The feature comes at no extra cost to Salesforce customers.[^s3]

## How it works

An admin turns the feature on, decides who may use it, and then each eligible user enrolls individually.[^s1] During enrollment the user connects Salesforce Authenticator to their Salesforce account and confirms the enrollment in the app; after that, logging in means entering the username, leaving the password blank, and approving the push request on the phone.[^s3] The Salesforce Admins walkthrough notes that the device itself also asks for a fingerprint or passcode, so the login combines something the user has (the registered phone) with something they know or are.[^s3] Registering a mobile number as a backup verification method is recommended for users who lose access to the app.[^s3]

Because the second factor is built into the approval, Salesforce states that Lightning Login satisfies its contractual requirement to use MFA for direct logins.[^s1] That makes it one of the few ways to meet the MFA requirement while removing the password entirely, rather than adding a step on top of it.

## Configuring it

Admin setup happens in a few places:[^s1]

- **Session Settings**: make sure **Allow Lightning Login** is selected. Clearing it later sends every user back to username-and-password login.[^s1]
- **Scope**: choose whether all users can use it or only users granted the **Lightning Login User** permission.[^s1]
- **Permission assignment**: grant Lightning Login User through a permission set, or through a cloned or custom profile (not a standard profile).[^s1]
- **Session level**: a Lightning Login session gets the Standard security level by default, the same as a password login; admins can raise it to High Assurance.[^s1]

Enabling the feature requires the Customize Application permission, and editing system permissions on profiles requires Manage Profiles and Permission Sets. Salesforce Help lists the feature in Salesforce Classic and Lightning Experience across editions from Essentials and Professional through Enterprise, Performance, Unlimited and Developer.[^s1] Trailhead's MFA and SSO superbadge uses exactly this pattern: it restricts Lightning Login to a permission set named Lightning Login User so a break-glass admin account can log in quickly and securely.[^s2]

## Limits and gotchas

- **Internal users only**: Salesforce Help states that Lightning Login isn't supported for external users, so Experience Cloud members need other methods.[^s1]
- **Transaction security policies**: if a transaction security policy requires MFA, Lightning Login is not supported and enrolled users fall back to username and password.[^s1]
- **Device activation**: when the org requires device activation, enrolled users are routed to username-and-password login and must complete identity verification.[^s1]
- **Login hints**: a lightning-bolt icon marks enrolled usernames on the login page only after "Remember me" was used; Safari may need a cookie setting changed for the hints to appear.[^s1]
- **Monitoring**: Lightning Login activity shows up in Login History and Identity Verification History.[^s1]

## When to use it (and when not)

Lightning Login suits orgs where users log in directly to Salesforce rather than through a corporate identity provider, and where admins want MFA compliance without password fatigue. It is also a practical option for a break-glass administrator who must reach the org when SSO is down.[^s2][^s1] Where an external identity provider already handles authentication, SAML or OpenID Connect single sign-on is usually the primary path instead, with MFA enforced at that provider.[^s4] For customers and partners on Experience Cloud sites, Lightning Login is not an option at all.[^s1]

## Connections

Lightning Login is a specialization of **multi-factor authentication** within **Salesforce Identity**: it meets the MFA requirement by making the authenticator approval the whole login.[^s1] It depends on **Salesforce Authenticator**, the app that receives and approves the push request.[^s3] Access is configured via **permission sets** or **profiles** that grant the Lightning Login User permission, and the resulting session level ties it to **session security levels**.[^s1] Its activity is audited in **Login History** and identity verification history, and device activation from **identity verification** can override it.[^s1] By removing reusable passwords it mitigates **account takeover**, and it is an alternative to **SAML single sign-on** for orgs without an external identity provider.[^s4][^s1] It sits next to **password policies**, since users who are not enrolled still log in with passwords governed by those policies.[^s1]

## Sources
[^s1]: Salesforce Help, "Enable Lightning Login". https://help.salesforce.com/s/articleView?language=en_US&id=sf.security_ll_enable.htm&type=5 (accessed 2026-11-21)
[^s2]: Trailhead, "Enable Lightning Login Securely with the Authenticator App". https://trailhead.salesforce.com/es-MX/content/learn/superbadges/superbadge-mfa-sso-settings/superbadge-mfa-sso-settings_lightning-login (accessed 2026-11-21)
[^s3]: Salesforce Admins, "Demo Lightning Login for Your Company". https://admin.salesforce.com/blog/2017/demo-lightning-login-company (accessed 2026-11-21)
[^s4]: Salesforce Developers, "Identity | Salesforce Developer Center". https://developer.salesforce.com/developer-centers/identity (accessed 2026-11-21)
