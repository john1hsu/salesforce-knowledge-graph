---
id: kt:openid-connect-authentication-providers
type: Feature
title: OpenID Connect Authentication Providers
aliases: [OpenID Connect auth provider, OIDC authentication provider, OIDC auth provider, Auth. Provider (OpenID Connect), social sign-on via OpenID Connect]
domain: identity
summary: >-
  A Salesforce authentication provider (Auth. Provider) of type OpenID Connect, which makes an org or Experience
  Cloud site a relying party that signs users in through any external OpenID provider and creates or links Salesforce
  users through an Apex registration handler.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity]
related: [kt:experience-cloud-identity, kt:my-domain, kt:oauth-2-flows-in-salesforce, kt:multi-factor-authentication, kt:apex]
relations:
  - {predicate: implements, object: kt:openid-connect}
  - {predicate: dependsOn, object: kt:oauth-2-0}
  - {predicate: alternativeTo, object: kt:single-sign-on-saml}
  - {predicate: coveredBy, object: kt:identity-and-access-management-architect-certification}
sources:
  - id: s1
    title: "Configure an Authentication Provider Using OpenID Connect (Mobile SDK Development Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/mobile-sdk/guide/sso-provider-openid-connect.html
    type: official-docs
    accessed: 2026-11-02
  - id: s2
    title: "RegistrationHandler Interface (Apex Reference Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_auth_plugin.htm
    type: official-docs
    accessed: 2026-11-02
  - id: s3
    title: "Set Up Social Sign-On (External Identity module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/content/learn/modules/identity_external/identity_external_social
    type: official-learning
    accessed: 2026-11-02
  - id: s4
    title: "OpenID Connect Core 1.0 incorporating errata set 2"
    publisher: OpenID Foundation
    url: https://openid.net/specs/openid-connect-core-1_0.html
    type: standards-body
    accessed: 2026-11-02
created: 2026-11-02
---

# OpenID Connect Authentication Providers

An OpenID Connect authentication provider is an **Auth. Provider** definition in Setup whose provider type is OpenID Connect. It turns a Salesforce org or Experience Cloud site into a relying party: users click a login button, are redirected to an external OpenID provider, and are signed in to Salesforce once that provider authenticates them. Salesforce ships built-in provider types for services such as Facebook, Google and Amazon, but the OpenID Connect type works with any provider that implements the server side of the protocol, and a fully custom provider can be written in Apex when neither fits.[^s1][^s3]

## The protocol underneath

OpenID Connect Core 1.0 describes itself as a simple identity layer on top of OAuth 2.0. A request becomes an OIDC request by including the `openid` scope, and the provider returns an **ID token** — a JWT whose required claims are the issuer (`iss`), subject (`sub`), audience (`aud`, which must contain the client ID), expiry (`exp`) and issue time (`iat`). Profile attributes come from the **UserInfo endpoint**, a protected resource called with the access token. The spec defines authorization code, implicit and hybrid flows; the current text is the final version incorporating errata set 2, dated December 2023.[^s4]

## How it is configured

An admin with Customize Application and Manage Auth. Providers first registers a web app with the external provider, then creates the Auth. Provider in Salesforce. Required values are a name, a URL suffix, the consumer key and secret, and the authorize, token and user-info endpoint URLs; the user-info URL can be omitted when the provider is used only for API access rather than login. Optional settings include a token issuer, default scopes, a PKCE checkbox, sending the access token or client credentials in headers instead of the query string or body, custom error and logout URLs, and an icon for Experience Cloud login pages. The feature is available in Enterprise, Performance, Unlimited and Developer editions.[^s1]

After saving, Salesforce generates a callback URL that must be copied back into the provider's app registration, plus client configuration URLs: a Test-Only Initialization URL for checking the handshake and an SSO initialization URL of the form `/services/auth/sso/<suffix>` on the My Domain or site URL. The generated Auth. Provider ID is what Apex uses with `Auth.AuthToken` to retrieve the stored third-party access token.[^s1]

## Registration handler

Just-in-time user handling is done by an Apex class implementing `Auth.RegistrationHandler`, and Salesforce will not generate the SSO initialization URL without one. `createUser` runs on a user's first login and returns either a new User (which Salesforce inserts) or an existing one to link; `updateUser` runs on subsequent logins to refresh attributes.[^s1][^s2] Both receive an `Auth.UserData` object carrying the raw provider attributes, the encoded and decoded ID token and the user-info JSON. The class runs as the **Execute Registration As** user, who needs Manage Users; Trailhead advises a dedicated service account in production so registration does not break when an admin leaves.[^s1][^s2][^s3]

## Limits and gotchas

- **ID token signatures are not validated.** Salesforce checks the ID token against the configured token issuer and the user-info response but does not verify its signature; validate it yourself with `Auth.JWTUtil` in the handler if that matters.[^s1][^s2]
- **Audience must be the consumer key only**; adding other audience values breaks validation. The authorization code flow requires an ID token in the token response.[^s1]
- **Secrets are masked in metadata.** Since November 2022 the consumer secret is replaced with a placeholder in Metadata API retrievals, so deployments must restore it or have it re-entered in Setup.[^s1]
- **MFA ownership.** The "Use Salesforce MFA for this SSO provider" option applies Salesforce MFA instead of the provider's, but only to users with the MFA requirement assigned directly.[^s1]
- **Don't rely on Salesforce-managed apps in production.** Leaving key and secret blank on built-in types uses Salesforce-managed apps, which Trailhead warns can have downtime.[^s3]

## When to use it

Choose an OIDC provider for consumer and partner social sign-on, for modern cloud identity providers that speak OIDC natively, and when an integration also needs the third-party access token. Choose SAML single sign-on when the enterprise IdP is SAML-first or assertion-based attribute mapping is required. Enable PKCE when the provider supports it.[^s1][^s4]

## Connections

This node is part of **Salesforce Identity** and **implements** the **OpenID Connect** standard, which **depends on** **OAuth 2.0**; the Salesforce-side grants it relies on are described under **OAuth 2.0 Flows in Salesforce**.[^s4] It is the usual **alternative to SAML single sign-on** for inbound federation, and its SSO URLs live on **My Domain** and on the sites covered by **Experience Cloud identity**.[^s1][^s3] It interacts with **multi-factor authentication** through the Salesforce-MFA option, extends through **Apex** registration handlers, and is examined in the **Identity and Access Management Architect** certification.[^s1][^s2]

## Sources
[^s1]: Salesforce Developers, "Configure an Authentication Provider Using OpenID Connect", Mobile SDK Development Guide. https://developer.salesforce.com/docs/platform/mobile-sdk/guide/sso-provider-openid-connect.html (accessed 2026-11-02)
[^s2]: Salesforce Developers, "RegistrationHandler Interface", Apex Reference Guide. https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_auth_plugin.htm (accessed 2026-11-02)
[^s3]: Trailhead, "Set Up Social Sign-On", External Identity module. https://trailhead.salesforce.com/en/content/learn/modules/identity_external/identity_external_social (accessed 2026-11-02)
[^s4]: OpenID Foundation, "OpenID Connect Core 1.0 incorporating errata set 2" (December 2023). https://openid.net/specs/openid-connect-core-1_0.html (accessed 2026-11-02)
