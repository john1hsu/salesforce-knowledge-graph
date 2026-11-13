---
id: kt:delegated-authentication
type: Feature
title: Delegated Authentication
aliases: [delegated authentication SSO, delegated SSO, Delegated Gateway URL]
domain: identity
summary: >-
  A Salesforce single sign-on method in which Salesforce validates a user's password by calling a customer-hosted
  SOAP web service (often wrapping LDAP) that answers true or false, so passwords and their policies live in the
  external system rather than in Salesforce.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity]
related: [kt:password-policies, kt:multi-factor-authentication, kt:login-ip-ranges-and-trusted-ip-ranges]
relations:
  - {predicate: alternativeTo, object: kt:single-sign-on-saml}
  - {predicate: alternativeTo, object: kt:openid-connect-authentication-providers}
  - {predicate: integratesWith, object: kt:ldap}
sources:
  - id: s1
    title: "Delegated Authentication"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.sso_delauthentication.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-13
  - id: s2
    title: "Configure Salesforce for Delegated Authentication"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.sso_delauthentication_configuring.htm&type=5
    type: official-docs
    accessed: 2026-11-13
  - id: s3
    title: "Single Sign-On and Password Management FAQ for Salesforce Delegated Authentication"
    publisher: Salesforce Help (Knowledge Article 000385305)
    url: https://help.salesforce.com/s/articleView?id=000385305&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-13
  - id: s4
    title: "Multi-Factor Authentication (MFA)"
    publisher: Salesforce Security
    url: https://security.salesforce.com/mfa
    type: official-docs
    accessed: 2026-11-13
created: 2026-11-13
---

# Delegated Authentication

Delegated authentication is a way of letting another system decide whether a Salesforce login is valid. When a user who is enabled for it types a username and password on the Salesforce login page, Salesforce does not check the password itself; it passes the credentials to a web service that the customer hosts, and that service answers yes or no. Salesforce describes it as similar to single sign-on, with the difference that users still sign in to each application separately rather than reusing one session.[^s1] It is available in Professional, Enterprise, Performance, Unlimited, Developer and Database.com editions, in both Lightning Experience and Salesforce Classic.[^s1]

## How it works

The customer wraps an existing authentication method, the classic example being an LDAP directory, in a SOAP web service that Salesforce can call. At login, Salesforce first checks the username and the user's access settings. If the user has the **Is Single Sign-On Enabled** permission, Salesforce sends the username, password and source IP address to that service, which returns true or false. True lets the login proceed; false produces the usual invalid-username-or-password error. Salesforce discards the password immediately and does not store, log or display it, and the same flow applies to API logins as well as browser logins.[^s1]

Because the permission is granted through profiles or permission sets, an org can run a mix: some users authenticate through the delegated service while others keep Salesforce-managed passwords.[^s1] The endpoint only ever receives what is in the password field, so instead of a real corporate password the service can accept a token such as a Kerberos ticket that an internal portal posts to the Salesforce login page on the user's behalf.[^s2]

## Configuration

The setup process in Salesforce Help has these main steps:[^s2]

1. Enable delegated authentication for the org.[^s2]
2. In Setup, open **API** and download the **Delegated Authentication WSDL**, then generate a server-side stub from it (for example with WSDL2Java or .NET tools) and add the authentication logic.[^s2]
3. In **Single Sign-On Settings**, enter the **Delegated Gateway URL**, the endpoint Salesforce will call.[^s2]
4. Grant **Is Single Sign-On Enabled** to the users who should authenticate this way.[^s2]
5. Optionally select **Force Delegated Authentication Callout**, which calls the endpoint on every login attempt, including attempts Salesforce would already reject because of a restriction.[^s2]

For security, Salesforce only posts to the gateway on port 80 (HTTP only), 443 (HTTPS only), or ports 1024 and higher (HTTP or HTTPS).[^s2] Viewing the settings needs View Setup and Configuration; editing needs Customize Application and Modify All Data.[^s2]

## Limits and gotchas

- **Password policy moves out of Salesforce.** Expiration, minimum length and lockout after failed attempts are not enforced by Salesforce for these users; the endpoint has to enforce them.[^s1][^s3]
- **No password resets in Salesforce.** A reset requested from the login page leads to a fixed page telling SSO users to contact their admin, and an admin's Reset Password action sends nothing.[^s3]
- **Misleading error text.** A wrong password produces a message suggesting the company's authentication service is down, which can confuse users and help desks.[^s3]
- **IP restrictions still apply.** API and desktop clients can log in through the service unless they come from outside a restricted IP range for the user.[^s2]
- **Turning it off.** When the feature is disabled, users fall back to the Salesforce password they had before, so Salesforce recommends sending them all a password reset.[^s3]
- **Welcome emails.** New delegated users get a welcome email with their username and a login link but no password, and the wording cannot be customized.[^s3]

## MFA and when to use it

Salesforce's MFA guidance for orgs that use single sign-on is to make sure every Salesforce user is covered by MFA, either through the SSO provider's own MFA service or through the free MFA built into Salesforce.[^s4] With delegated authentication, Salesforce only sees a true or false result from the endpoint, so any second factor checked there is invisible to Salesforce; that makes Salesforce's native MFA the simpler way to show coverage.[^s1][^s4]

Delegated authentication suits organizations that must keep password checking against an on-premises directory and cannot run a federation identity provider. Where an identity provider is available, federated options such as SAML single sign-on or an OpenID Connect authentication provider avoid sending passwords to Salesforce at all and give users one session across applications.[^s1]

## Connections

Delegated authentication is part of **Salesforce Identity** (`broader`). It is an `alternativeTo` **SAML single sign-on** and **OpenID Connect authentication providers**, the federated sign-in options that use an external identity provider instead of a password check.[^s1] It `integratesWith` **LDAP**, the directory Salesforce uses as its example back end.[^s1] It is related to **password policies**, which no longer apply to delegated users; to **multi-factor authentication**, which still has to be met for them; and to **login IP ranges**, which continue to restrict where they can log in from.[^s3][^s4][^s2]

## Sources

[^s1]: Salesforce Help, "Delegated Authentication". https://help.salesforce.com/s/articleView?id=sf.sso_delauthentication.htm&language=en_US&type=5 (accessed 2026-11-13)
[^s2]: Salesforce Help, "Configure Salesforce for Delegated Authentication". https://help.salesforce.com/s/articleView?language=en_US&id=sf.sso_delauthentication_configuring.htm&type=5 (accessed 2026-11-13)
[^s3]: Salesforce Help, "Single Sign-On and Password Management FAQ for Salesforce Delegated Authentication" (Knowledge Article 000385305). https://help.salesforce.com/s/articleView?id=000385305&language=en_US&type=1 (accessed 2026-11-13)
[^s4]: Salesforce Security, "Multi-Factor Authentication (MFA)". https://security.salesforce.com/mfa (accessed 2026-11-13)
