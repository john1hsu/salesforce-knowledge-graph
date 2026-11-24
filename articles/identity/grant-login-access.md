---
id: kt:grant-login-access
type: Feature
title: Grant Login Access
aliases: [Log In As, Login As another user, Grant Account Login Access, Login Access Policies, Administrators Can Log in as Any User]
domain: identity
summary: >-
  The Salesforce mechanism that lets an administrator, Salesforce support or a managed-package publisher sign in
  as a specific user to troubleshoot, either because that user granted login access or because the org lets
  administrators log in as any user.
release: "Winter '27"
status: current
broader: [kt:user-management, kt:salesforce-identity]
related: [kt:setup-audit-trail, kt:multi-factor-authentication, kt:login-flows, kt:profiles]
relations:
  - {predicate: dependsOn, object: kt:session-security-levels}
  - {predicate: consumedBy, object: kt:license-management-app}
  - {predicate: consumedBy, object: kt:first-generation-managed-packages}
  - {predicate: contrastsWith, object: kt:salesforce-as-identity-provider}
sources:
  - id: s1
    title: "Login Access"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.identity_login_access.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-24
  - id: s2
    title: "Control Login Access Policies"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.controlling_login_access.htm&amp=&type=5
    type: official-docs
    accessed: 2026-11-24
  - id: s3
    title: "Enable the 'Administrators Can Log in as Any User' Feature"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000386710&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-24
  - id: s4
    title: "How to Log In as Another User in Salesforce (Admin Login Access)"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=004333094&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-24
  - id: s5
    title: "Request Login Access from Subscribers"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg1-dev/guide/lma-requesting-login-access.html
    type: official-docs
    accessed: 2026-11-24
  - id: s6
    title: "Collaborate Effectively with Your Salesforce Admin"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lex_salesforce_basics/lex_salesforce_basics_your_admin
    type: official-learning
    accessed: 2026-11-24
created: 2026-11-24
---

# Grant Login Access

Grant Login Access is the Salesforce feature set that lets someone other than a user sign in *as* that user — an internal administrator, Salesforce support, a partner's support team, or the publisher of a managed package the user is licensed for — usually to reproduce a problem exactly as the user sees it.[^s1][^s6] Admins decide whether users must explicitly grant that access first and which outside parties users may grant it to; the governing settings live on the **Login Access Policies** page in Setup.[^s1][^s2] The admin-side action is commonly called **Log In As** (or "Login As").[^s4]

## How it works

There are two models for an internal administrator:

- **User-granted access.** The user opens their personal Settings and uses *Grant Account Login Access* to give an admin or support party access for a chosen duration.[^s6]
- **Administrators Can Log in as Any User.** With this org setting on, system administrators can log in as any user without first asking the user to grant access.[^s2][^s3]

Either way, the admin goes to Setup > Users and clicks the **Login** link beside the user's name; the link only appears when the user has granted access or the org allows admins to log in as anyone.[^s4] The admin needs the Modify All Data permission, and turning on the any-user setting is documented as needing Modify All Data and Manage Users.[^s3][^s4] To return to their own account, the admin chooses the logout entry labelled with the impersonated user's name.[^s4]

The any-user setting is offered in Enterprise, Performance, Unlimited and Developer Editions and cannot be activated on Professional Edition or lower; if the checkbox is missing in an eligible org, it has to be provisioned through Salesforce.[^s3] Removing the option once enabled also requires contacting Salesforce, after which users must grant access before an admin can troubleshoot their account.[^s2]

## Publishers and support organizations

For ISVs, the License Management App flow depends on the subscriber granting login access to the publisher before the publisher can log in to the subscriber org.[^s5] When a publisher does not appear in a user's grant list, typical reasons are that the admin disabled non-admin grants, the user lacks a package licence, or the package is licensed to the whole org — in which case only an admin with Manage Users can grant access.[^s2][^s5] On the Login Access Policies page an admin can mark a publisher as *Available to Administrators Only* so that ordinary users can no longer grant it access, for example for regulatory or privacy reasons; the Support Organization column names the License Management Org that owns each package.[^s2] Some managed packages don't support login access at all.[^s2]

## Limits and gotchas

- With the any-user setting off, a granted login access lasts a limited time and the subscriber can revoke it at any time.[^s5]
- An admin can't log in as an inactive user, and can't start a second Log In As while already logged in as someone.[^s3]
- The any-user setting does not apply to Experience Cloud site users.[^s3]
- Logging out of the impersonated session can also end the admin's own session, forcing a fresh login.[^s3]
- Login flows on either profile don't run during Log In As, and it isn't supported when Salesforce is the SAML identity provider for an SSO service provider.[^s4]
- While logged in as a user, support users and subscribers can't authorize OAuth data access for that user or switch usernames.[^s1]
- MFA during Log In As applies only when a separate setting is enabled; a High Assurance requirement can still prompt a challenge.[^s1][^s2]

## Auditing

Changes a publisher makes while logged in as a subscriber are recorded in the subscriber org's audit trail, so impersonated activity remains attributable.[^s5] The trade-off between the two models is consent: with the any-user setting off, each user decides who may sign in as them and for how long, and can revoke that grant, whereas with it on, admins skip that step entirely.[^s3][^s5]

## Connections

Grant Login Access sits under `kt:user-management` and the wider `kt:salesforce-identity` stack, since it is configured alongside users, profiles and login policies.[^s4] Its interaction with `kt:multi-factor-authentication` and `kt:session-security-levels` decides whether an impersonating admin is challenged, and it deliberately bypasses `kt:login-flows`.[^s1][^s2][^s4] Publishers reach it through the `kt:license-management-app` for `kt:first-generation-managed-packages`, and their changes land in the `kt:setup-audit-trail`.[^s5] It contrasts with `kt:salesforce-as-identity-provider`, where Log In As is not supported for downstream SSO.[^s4]

## Sources
[^s1]: Salesforce Help, "Login Access". https://help.salesforce.com/s/articleView?id=sf.identity_login_access.htm&language=en_US&type=5 (accessed 2026-11-24)
[^s2]: Salesforce Help, "Control Login Access Policies". https://help.salesforce.com/s/articleView?language=en_US&id=sf.controlling_login_access.htm&amp=&type=5 (accessed 2026-11-24)
[^s3]: Salesforce Help, "Enable the 'Administrators Can Log in as Any User' Feature". https://help.salesforce.com/s/articleView?id=000386710&language=en_US&type=1 (accessed 2026-11-24)
[^s4]: Salesforce Help, "How to Log In as Another User in Salesforce (Admin Login Access)". https://help.salesforce.com/s/articleView?id=004333094&language=en_US&type=1 (accessed 2026-11-24)
[^s5]: Salesforce Developers, "Request Login Access from Subscribers". https://developer.salesforce.com/docs/platform/pkg1-dev/guide/lma-requesting-login-access.html (accessed 2026-11-24)
[^s6]: Trailhead, "Collaborate Effectively with Your Salesforce Admin". https://trailhead.salesforce.com/content/learn/modules/lex_salesforce_basics/lex_salesforce_basics_your_admin (accessed 2026-11-24)
