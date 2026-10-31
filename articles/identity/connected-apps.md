---
id: kt:connected-apps
type: Feature
title: Connected Apps
aliases: [connected app, ConnectedApp, connected app framework]
domain: identity
summary: >-
  The long-standing Salesforce framework that registers an external application so it can authenticate and call
  Salesforce APIs over OAuth 2.0, SAML or OpenID Connect, with admin-controlled access policies. Creation of new
  connected apps has been restricted since Spring '26 in favour of external client apps.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity]
related: [kt:oauth-2-flows-in-salesforce, kt:single-sign-on-saml, kt:external-client-apps, kt:metadata-api]
relations:
  - {predicate: replacedBy, object: kt:external-client-apps}
  - {predicate: implements, object: kt:oauth-2-0}
  - {predicate: configuredVia, object: kt:metadata-api}
sources:
  - id: s1
    title: "Create a Connected App"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.connected_app_create.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-10-31
  - id: s2
    title: "Manage OAuth Access Policies for a Connected App"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=xcloud.connected_app_manage_oauth.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-10-31
  - id: s3
    title: "External Client Apps and Connected Apps (Mobile SDK Development Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/mobile-sdk/guide/connected-apps.html
    type: official-docs
    accessed: 2026-10-31
  - id: s4
    title: "Connected Apps (First-Generation Managed Packaging Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg1-dev/guide/connected-apps.html
    type: official-docs
    accessed: 2026-10-31
  - id: s5
    title: "RFC 6749: The OAuth 2.0 Authorization Framework"
    publisher: IETF / RFC Editor
    url: https://rfc-editor.org/rfc/rfc6749
    type: standards-body
    accessed: 2026-10-31
created: 2026-10-31
---

# Connected Apps

A connected app is the Salesforce record that lets an external application integrate with the platform through its APIs using standard protocols — SAML, OAuth and OpenID Connect — for authentication, authorization and single sign-on. The external application can live anywhere: another cloud platform, a device, or a SaaS product; the Salesforce mobile app is itself an example. The connected app stores metadata about the client (which protocol it uses, where it runs), and Salesforce uses that record to grant data access, attach access policies such as token expiry, and audit usage.[^s4]

In OAuth terms (RFC 6749), the connected app is the client registration: a client must register with the authorization server before the protocol starts, supplying its type and redirection URIs, and receives a client identifier in return. RFC 6749 distinguishes confidential clients, which can keep a secret on a secure server, from public clients such as native or browser apps that cannot.[^s5] Salesforce plays the authorization server and resource server; the connected app's consumer key and consumer secret are the issued client credentials.[^s1]

## How it works

When creating a connected app, an admin first decides how it will be used and enables the matching settings. Every app needs basic settings (name, logo, contact details). Beyond that, the app can be configured for OAuth API integration (an external app requests data on a user's behalf), the OAuth 2.0 client credentials flow (the app trades its consumer key and secret for an access token without a user), SAML 2.0 where Salesforce is the identity provider for a service provider (SP- and IdP-initiated SSO), mobile integration with or without the Mobile SDK, a custom Apex connected app handler, or a canvas app surfaced inside Salesforce.[^s1] Connected apps can be created in Group, Essentials, Professional, Enterprise, Performance, Unlimited and Developer editions and installed in all editions.[^s1]

Once the app exists, admins govern it from Manage Connected Apps. The OAuth policies are the heart of it:[^s2]

- **Permitted Users** — either *All users may self-authorize* (the default; each user approves on first use) or *Admin approved users are pre-authorized*, where access is granted only through profiles or permission sets.[^s2]
- **IP Relaxation** — enforce the org's IP restrictions (default), enforce them but relax for refresh tokens, relax for activated devices, or relax entirely.[^s2]
- **Refresh Token Policy** — valid until revoked (default), immediately expire, expire after a period of inactivity, or expire after a fixed period.[^s2]
- **Single Logout** — optionally log users out of the app when they log out of Salesforce, using an absolute https URL.[^s2]

## Limits and gotchas

- **Creation is restricted.** As of Spring '26, new connected apps can no longer be created by default; existing apps continue to work during and after that release, and teams that truly need a new one must contact Salesforce Support. Salesforce recommends external client apps for new integrations.[^s1][^s3]
- **The Use Any API Client permission** lets a user reach any connected app, even one set to admin-approved, so audit who holds it.[^s2]
- **Switching to admin-approved** immediately cuts off users without a profile or permission set grant.[^s2]
- **IP relaxation has edges:** JWT bearer and SAML bearer flows always enforce IP restrictions regardless of policy, IP restrictions only apply if set on the user's profile, and apps from managed packages use the default Permitted Users and IP settings.[^s2]
- **Refresh token policy** is evaluated only when a refresh token is used; tightening it does not end an active session.[^s2]
- **Canvas apps using signed requests** require admin-approved users, immediately expiring refresh tokens and profile or permission set access.[^s2]

## When to use it (and when not)

For anything new, start with external client apps, which Salesforce positions as the next generation designed to improve security and fix the packaging and distribution problems of connected apps.[^s3] Connected apps remain relevant because most production orgs already run integrations, managed packages and SSO configurations on them; architects need to understand their policies to secure, audit and eventually migrate those integrations.[^s3][^s4] Prefer admin-approved access, the narrowest IP relaxation that works, and a finite refresh token policy for integration users.[^s2]

## Connections

Connected apps sit under **Salesforce Identity** as the mechanism that registers clients and service providers.[^s4] They are the configuration point for every flow described in **OAuth 2.0 flows in Salesforce** and implement the client-registration model of the **OAuth 2.0** standard.[^s5] With SAML settings they back **single sign-on (SAML)** where Salesforce is the identity provider.[^s1] They are being superseded by **external client apps**, the recommended migration path.[^s3] As metadata, they are deployed with the `ConnectedApp` type through the **Metadata API** and can ship in packages.[^s4]

## Sources
[^s1]: Salesforce Help, "Create a Connected App". https://help.salesforce.com/s/articleView?id=sf.connected_app_create.htm&language=en_US&type=5 (accessed 2026-10-31)
[^s2]: Salesforce Help, "Manage OAuth Access Policies for a Connected App". https://help.salesforce.com/s/articleView?id=xcloud.connected_app_manage_oauth.htm&language=en_US&type=5 (accessed 2026-10-31)
[^s3]: Salesforce Developers, "External Client Apps and Connected Apps" (Mobile SDK Development Guide). https://developer.salesforce.com/docs/platform/mobile-sdk/guide/connected-apps.html (accessed 2026-10-31)
[^s4]: Salesforce Developers, "Connected Apps" (First-Generation Managed Packaging Developer Guide). https://developer.salesforce.com/docs/platform/pkg1-dev/guide/connected-apps.html (accessed 2026-10-31)
[^s5]: IETF / RFC Editor, "RFC 6749: The OAuth 2.0 Authorization Framework" (October 2012). https://rfc-editor.org/rfc/rfc6749 (accessed 2026-10-31)
