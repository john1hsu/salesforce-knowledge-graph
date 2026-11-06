---
id: kt:login-flows
type: Feature
title: Login Flows
aliases: [login flow, custom login flows, custom login flow, post-authentication flow]
domain: identity
summary: >-
  A screen flow or Visualforce page that Salesforce runs after a user authenticates and before they reach the
  org or an Experience Cloud site, assigned per profile, used to add steps such as custom verification,
  terms acceptance or data collection, and able to force a logout.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity]
related: [kt:screen-flow, kt:multi-factor-authentication, kt:experience-cloud-identity, kt:single-sign-on-saml]
relations:
  - {predicate: dependsOn, object: kt:flow-builder}
  - {predicate: configuredVia, object: kt:profiles}
  - {predicate: integratesWith, object: kt:session-security-levels}
  - {predicate: coveredBy, object: kt:identity-and-access-management-architect-certification}
sources:
  - id: s1
    title: "Custom Login Flows"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.security_login_flow.htm&type=5
    type: official-docs
    accessed: 2026-11-06
  - id: s2
    title: "Login Flow Examples"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=security_login_flow_examples.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-06
  - id: s3
    title: "Create a Login Flow with Flow Builder"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.security_login_flow_cloud_designer.htm&type=5
    type: official-docs
    accessed: 2026-11-06
  - id: s4
    title: "Assign the Login Flow and Test It in Your Portal (Self-Registration in a Portal)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/selfregistration-in-a-portal/assign-the-login-flow-and-test-it-in-your-portal
    type: official-learning
    accessed: 2026-11-06
created: 2026-11-06
---

# Login Flows

A login flow is a custom process that Salesforce inserts into the login sequence: it runs after the platform has authenticated the user and before that user lands in the org or an Experience Cloud site.[^s1] It does not replace authentication — the user must already have passed the password, delegated authentication, SAML single sign-on or third-party auth provider step — but it adds business logic on top of it.[^s1] A user who completes the flow is redirected into the org or site; a flow can also log the user out on the spot.[^s1][^s2]

## How it works

Admins build a login flow in one of two ways: declaratively as a **screen flow** in Flow Builder, or in code as a **Visualforce page with an Apex controller** when they need full control over the page's look and behaviour.[^s1][^s3] The flow is then registered in Setup under **Login Flows**, where it is marked as a login flow and tied to a user license and profile, so only users with that profile see it.[^s3][^s4] Different profiles can get different flows — for example one for sales reps and another for service agents.[^s1] Building one requires the Manage Flow permission.[^s3]

Once assigned, the flow fires on every login for those users, including logins from the Salesforce mobile app and from OAuth-enabled client apps.[^s1] While the flow is running, the user can reach only the flow itself and cannot skip past it into the application.[^s1]

### Context variables

Salesforce passes the login context into the flow through text variables that follow a `LoginFlow_` naming convention: `LoginFlow_LoginType`, `LoginFlow_LoginSubType`, `LoginFlow_IpAddress`, `LoginFlow_UserAgent`, `LoginFlow_Platform`, `LoginFlow_Application`, `LoginFlow_Community`, `LoginFlow_SessionLevel` and `LoginFlow_UserId`.[^s2] The user ID lets the flow query the User record. Two output variables steer the outcome: `LoginFlow_FinishLocation` (text) sets where the user goes when the flow ends, and `LoginFlow_ForceLogout` (Boolean) logs the user out immediately when set to true.[^s2]

## Typical uses

Salesforce lists a broad set of use cases: branding the login experience, collecting or confirming user data such as phone numbers or addresses, requiring acceptance of terms of service or a survey, verifying the user against an external identity or geo-fencing service, adding custom or third-party strong authentication, asking a secret question, raising alerts for logins outside working hours, and limiting concurrent sessions per user.[^s1] The documented examples include a flow that reads `Phone` and `MobilePhone` with Get Records and lets the user update them, a TOTP registration-and-verification flow built on a legacy Apex action, and pointers to third-party factors such as YubiKey or SMS providers; an unmanaged samples package bundles email confirmation, conditional MFA that skips trusted IPs, device activation and terms-of-service flows.[^s2] On Experience Cloud, Trailhead's self-registration module uses a login flow assigned to a Customer Community license and portal profile to capture a new member's privacy preferences.[^s4]

## Limits and gotchas

- **Not for API logins.** Login flows don't run for API logins, nor for sessions handed to the UI through `frontdoor.jsp` from a non-UI login.[^s1]
- **Outlook via SSO.** For Outlook integration through SSO, custom login flows aren't invoked; they rerun only after the user manually logs out.[^s1]
- **Admin lockout.** Don't attach an untested flow to the administrator profile — if it fails, admins can't log in. Test with a dedicated user and profile first.[^s2]
- **Lightning runtime.** With *Render Flow in Lightning Runtime* enabled, users can reach Salesforce before finishing the flow; Salesforce calls this a security risk and advises keeping it off when the flow enforces security.[^s2]
- **Keep it login-only.** Unrelated record updates inside the flow can cause side effects and block services; put them in separate flows.[^s1]
- **No external redirects.** Sending users outside the org from a login flow creates an open-redirect vulnerability and breaks start-URL services such as password reset.[^s1]

## When to use it (and when not)

Use a login flow when a requirement must be enforced at the moment of login for an interactive user and the platform's standard controls don't cover it — a custom verification step, a consent gate, or conditional logic based on IP, platform or application.[^s1][^s2] Prefer Salesforce's built-in multi-factor authentication and identity verification for ordinary MFA, since the custom TOTP example relies on a legacy action and adds code you must maintain.[^s2] Because API sessions bypass login flows, controls that must cover integrations need to live elsewhere, such as connected-app policies.[^s1]

## Connections

Login flows are a feature of **Salesforce Identity** and are built with **Flow Builder** as a specialised use of the **screen flow** type.[^s1][^s3] They are assigned through **profiles**, and the `LoginFlow_SessionLevel` input exposes the current session's level, tying them to **session security levels**.[^s2] They extend, rather than replace, **multi-factor authentication** and **SAML single sign-on**, since they run after either has completed.[^s1] For external users, they are one of the tools of **Experience Cloud identity**, as Trailhead's portal self-registration example shows.[^s4]

## Sources
[^s1]: Salesforce Help, "Custom Login Flows". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.security_login_flow.htm&type=5 (accessed 2026-11-06)
[^s2]: Salesforce Help, "Login Flow Examples". https://help.salesforce.com/s/articleView?id=security_login_flow_examples.htm&language=en_US&type=5 (accessed 2026-11-06)
[^s3]: Salesforce Help, "Create a Login Flow with Flow Builder". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.security_login_flow_cloud_designer.htm&type=5 (accessed 2026-11-06)
[^s4]: Trailhead, "Assign the Login Flow and Test It in Your Portal". https://trailhead.salesforce.com/content/learn/modules/selfregistration-in-a-portal/assign-the-login-flow-and-test-it-in-your-portal (accessed 2026-11-06)
