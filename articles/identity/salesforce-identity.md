---
id: kt:salesforce-identity
type: Product
title: Salesforce Identity
aliases: [Salesforce IAM, Identity for Salesforce, Customer Identity, Customer 360 Identity, Salesforce Identity and Access Management]
domain: identity
summary: >-
  Salesforce's identity and access management (IAM) service: a cloud user directory plus authentication, single
  sign-on, multi-factor authentication, app access and provisioning features that connect org users, customers and
  partners to Salesforce and external apps using SAML, OAuth 2.0 and OpenID Connect.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:experience-cloud, kt:experience-cloud-identity, kt:identity-connect, kt:salesforce-scim]
relations:
  - {predicate: hasPart, object: kt:single-sign-on-saml}
  - {predicate: hasPart, object: kt:multi-factor-authentication}
  - {predicate: hasPart, object: kt:my-domain}
  - {predicate: hasPart, object: kt:connected-apps}
  - {predicate: hasPart, object: kt:external-client-apps}
  - {predicate: implements, object: kt:oauth-2-0}
  - {predicate: implements, object: kt:openid-connect-authentication-providers}
  - {predicate: hasPart, object: kt:headless-identity}
  - {predicate: coveredBy, object: kt:identity-and-access-management-architect-certification}
sources:
  - id: s1
    title: "What Is Salesforce Identity?"
    publisher: Salesforce Developers (Identity Implementation Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/identity_overview.htm
    type: official-docs
    accessed: 2026-11-02
  - id: s2
    title: "Get to Know Salesforce Identity (Identity Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/identity_basics/identity_basics_product
    type: official-learning
    accessed: 2026-11-02
  - id: s3
    title: "Identity | Salesforce Developer Center"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/developer-centers/identity
    type: official-docs
    accessed: 2026-11-02
  - id: s4
    title: "External Identity License Details"
    publisher: Salesforce Developers (Identity Implementation Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/users_license_types_external_identity.htm
    type: official-docs
    accessed: 2026-11-02
  - id: s5
    title: "What Is Headless Identity?"
    publisher: Salesforce Developers (Headless Identity Implementation Guide)
    url: https://developer.salesforce.com/docs/platform/headless-identity-impl-guide/guide/headless-identity-what-is-it.html
    type: official-docs
    accessed: 2026-11-02
  - id: s6
    title: "Single Sign-On from an External Identity Provider"
    publisher: Salesforce Developers (Identity Implementation Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/identity_sso_id_provider.htm
    type: official-docs
    accessed: 2026-11-02
created: 2026-11-02
---

# Salesforce Identity

Salesforce Identity is the identity and access management (IAM) layer of the Salesforce Platform. It ties the users of an org to external apps and services, and gives admins tools to monitor, maintain and report on which apps users can reach and how they are authorised.[^s1] Trailhead frames it as a set of features that control access to Salesforce orgs and to apps running on the platform, on premises, in other clouds or on mobile devices, with the aim of stronger security and less login friction: sign in once, reach every authorised app.[^s2] It is the umbrella for most nodes in this graph's identity domain.

## What it includes

The Identity Implementation Guide groups the service into a handful of capabilities: a cloud user directory that other services can draw on; authentication controls such as multi-factor authentication, app restrictions and session login frequency; app access and authorisation for third-party apps; bulk provisioning and de-provisioning of app access; a management API; identity event logs that feed reports on SSO and connected-app usage; and **Identity Connect**, which synchronises Microsoft Active Directory users with Salesforce users and can provide SSO into Salesforce.[^s1] Trailhead's shorter list of seven core features is single sign-on, external client apps, social sign-on, MFA, My Domain, centralised user account management (grant or revoke access, freeze users, apply login policies) and the App Launcher.[^s2]

MFA is required for every user who logs in directly to the Salesforce UI and is switched on by default in production orgs; supported factors include authenticator apps, security keys and Salesforce Authenticator push notifications.[^s2] The Developer Center also lists single logout, Lightning Login for password-free sign-in, certificate-based authentication, custom login flows, password policies, API Access Control and login monitoring as identity features.[^s3]

## How it works: standards and roles

Salesforce Identity is built on open standards rather than proprietary protocols. SAML carries assertions for browser SSO from a corporate portal or identity provider; OAuth 2.0 authorises apps to call Salesforce APIs through several flows; and OpenID Connect adds an authentication layer on OAuth so users can sign in with another service.[^s1] The Developer Center adds SCIM for provisioning and managing user identities across systems.[^s3] Integrations are registered as connected apps (and, more recently, external client apps), which carry the SAML, OAuth or OpenID Connect configuration.[^s1][^s2]

An org can play either side of a federation. In **inbound SSO** an external identity provider authenticates the user and Salesforce acts as the service provider that trusts its SAML assertion; in **outbound SSO** a user already signed in to Salesforce reaches third-party apps without logging in again, with Salesforce as the identity provider.[^s6][^s1] The App Launcher then presents Salesforce, on-premises and third-party apps as tiles; Lightning Experience users get it by default, whereas Classic users need the Use Identity Features permission.[^s1]

## Workforce vs. customer identity and licensing

For employees, Identity features come with standard user licenses, and Identity Only licenses exist for people who need SSO and related features without a Sales Cloud or Service Cloud licence.[^s2] The overview page lists the service for Enterprise, Performance, Unlimited and Developer Editions.[^s1]

For external users, the **External Identity** license is sold in blocks of active users for customers, partners, patients, dealers and similar audiences, who can self-register, log in and manage profiles through an Experience Cloud site. It is included at no extra cost with paid Community licenses in Enterprise, Performance and Unlimited Editions, and each Developer Edition org gets five such licences.[^s4] Gotchas from the licence page: usernames must be unique within the site's org, Salesforce recommends staying at or below 10 million unique logins per month per site before contacting your account team, and the default profile allows ten custom objects (managed-package objects excluded).[^s4] Social sign-on with providers such as Google, LinkedIn or Facebook is especially useful for these external users.[^s2]

When a brand wants its own native UI, **Headless Identity** exposes login, registration and forgot-password APIs built on OAuth 2.0 (the Authorization Code and Credentials flow), so an off-platform or mobile app can use Salesforce customer identity behind the scenes; an Experience Cloud site is still required to store accounts and contacts and manage app access.[^s5]

## When to use it (and when not)

Use Salesforce Identity when Salesforce should be the identity provider or central directory, for example for customer and partner portals on Experience Cloud, or to give employees one launcher across apps. Where an enterprise IdP already exists, the common pattern is the reverse: keep the corporate IdP as source of truth and configure Salesforce as a SAML or OpenID Connect service provider, using Identity Connect or SCIM for provisioning where needed.[^s6][^s1][^s3] Either way, the org needs a My Domain, which is a prerequisite for SSO with external identity vendors and for social sign-on.[^s2]

## Connections

Salesforce Identity sits on the **Salesforce Platform** and **has as parts** **SAML single sign-on**, **multi-factor authentication**, **My Domain**, **connected apps**, **external client apps** and **Headless Identity**.[^s1][^s2][^s5] It **implements OAuth 2.0** and OpenID Connect, the basis for **OpenID Connect authentication providers** used in social sign-on.[^s1] Its customer side is realised through **Experience Cloud** sites and **Experience Cloud identity**, licensed via External Identity.[^s4] **Identity Connect** links it to Active Directory.[^s1] The product is examined in the **Identity and Access Management Architect** certification.

## Sources

[^s1]: Salesforce Developers, "What Is Salesforce Identity?" (Identity Implementation Guide). https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/identity_overview.htm (accessed 2026-11-02)
[^s2]: Trailhead, "Get to Know Salesforce Identity" (Identity Basics). https://trailhead.salesforce.com/content/learn/modules/identity_basics/identity_basics_product (accessed 2026-11-02)
[^s3]: Salesforce Developers, "Identity | Salesforce Developer Center". https://developer.salesforce.com/developer-centers/identity (accessed 2026-11-02)
[^s4]: Salesforce Developers, "External Identity License Details". https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/users_license_types_external_identity.htm (accessed 2026-11-02)
[^s5]: Salesforce Developers, "What Is Headless Identity?". https://developer.salesforce.com/docs/platform/headless-identity-impl-guide/guide/headless-identity-what-is-it.html (accessed 2026-11-02)
[^s6]: Salesforce Developers, "Single Sign-On from an External Identity Provider". https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/identity_sso_id_provider.htm (accessed 2026-11-02)
