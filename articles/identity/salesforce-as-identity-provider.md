---
id: kt:salesforce-as-identity-provider
type: Feature
title: Salesforce as Identity Provider
aliases: [Salesforce as IdP, Salesforce identity provider, Salesforce SAML identity provider, Salesforce IdP, Enable Identity Provider]
domain: identity
summary: >-
  The Salesforce capability that lets an org (or its Experience Cloud sites) act as the SAML 2.0 identity provider
  for external service providers, so users who authenticate to Salesforce get single sign-on into other apps that
  are registered as SAML- or OpenID Connect-enabled connected apps.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity, kt:single-sign-on-saml]
related: [kt:single-logout, kt:my-domain, kt:experience-cloud-identity]
relations:
  - {predicate: implements, object: kt:saml-2-0}
  - {predicate: implements, object: kt:openid-connect}
  - {predicate: configuredVia, object: kt:connected-apps}
  - {predicate: dependsOn, object: kt:certificate-and-key-management}
  - {predicate: coveredBy, object: kt:identity-and-access-management-architect-certification}
sources:
  - id: s1
    title: "Enable Salesforce as a SAML Identity Provider"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.identity_provider_enable.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-20
  - id: s2
    title: "Complete Prerequisites for SAML Service Provider Integration"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.service_provider_prerequisites.htm&type=5
    type: official-docs
    accessed: 2026-11-20
  - id: s3
    title: "Integrate Service Providers with Salesforce (Connected App Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/connected-app-basics/connected-app-basics-sso
    type: official-learning
    accessed: 2026-11-20
  - id: s4
    title: "Learn the Language of Identity (Identity Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/identity_basics/identity_basics_protocols
    type: official-learning
    accessed: 2026-11-20
  - id: s5
    title: "Security Assertion Markup Language (SAML) V2.0 Technical Overview"
    publisher: OASIS
    url: https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html
    type: standards-body
    accessed: 2026-11-20
  - id: s6
    title: "Salesforce Certified Platform Identity and Access Management Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/platformidentityandaccessmanagementarchitect
    type: official-learning
    accessed: 2026-11-20
created: 2026-11-20
---

# Salesforce as Identity Provider

Salesforce can sit on either side of a federated login. As a **service provider** it trusts an external identity provider such as ADFS, PingFederate or Shibboleth; as an **identity provider (IdP)** it is the system that authenticates the user, and identities flow outward from Salesforce into other applications.[^s4] Turning on the IdP role lets users who are already signed in to Salesforce reach third-party apps without a second password, with each external app registered in the org as a connected app.[^s3]

## How it works

The feature is available in Developer, Enterprise, Performance, Unlimited and Database.com editions, in both Lightning Experience and Salesforce Classic, and defining identity and service providers needs the Customize Application permission.[^s1] An admin picks a signing certificate, searches Setup for **Identity Provider**, clicks **Enable Identity Provider**, selects the certificate and saves.[^s1] By default the IdP signs with a self-signed SHA-256 certificate; a different self-signed certificate or one signed by a certificate authority can be chosen instead.[^s1]

The Identity Provider page then shows the **Issuer** (the IdP's unique identifier) and offers **Download Certificate** and **Download Metadata** (an XML file) to hand to service providers.[^s1] Its SAML metadata discovery endpoints list one metadata URL for the org's custom domain and one for each Experience Cloud site, so a site can act as an IdP for its own external users.[^s1]

Before integrating a service provider, the admin exchanges details in both directions: Salesforce supplies its metadata or certificate, and the service provider supplies its Assertion Consumer Service (ACS) URL, its Entity ID, the subject type it expects (the assertion subject or a custom attribute), and a certificate if it initiates login and signs its requests.[^s2] The service provider is then created as a SAML 2.0 connected app; because Salesforce is already the IdP, the app only needs to validate Salesforce's signature on the response.[^s3] For apps that prefer OpenID Connect, the connected app instead enables OAuth settings with the `openid` scope and an ID token configuration.[^s3]

SAML 2.0 defines both directions of browser single sign-on: SP-initiated, where the user starts at the app and is redirected to the IdP with an authentication request, and IdP-initiated, where the user signs in at the IdP first and is sent to the app with an unsolicited assertion.[^s5] Salesforce, acting as IdP, participates in both.[^s4]

## Limits and gotchas

- Assertions are valid for 5 minutes after issue, with a 30-second clock-skew buffer; service providers must honor that window.[^s1][^s2]
- Changing the IdP certificate can break access until every external app trusts the new one.[^s1]
- Disabling the identity provider removes users' SSO access to all external apps at once.[^s1]
- If a service provider sends `ForceAuthn`, Salesforce makes the user re-enter credentials even with a live session; no extra org setup is needed.[^s2]

Plan certificate rotation (with overlap and partner coordination) and clock synchronization before go-live; both failure modes surface as sudden login errors at the partner, not in Salesforce.[^s1][^s2]

## When to use it (and when not)

Use Salesforce as the IdP when Salesforce is the system of record for a population, typically partners or customers on Experience Cloud sites, and you want them to reach companion apps with one login.[^s1][^s4] When the enterprise already runs a corporate IdP for employees, it is usually cleaner for Salesforce to be a service provider of that IdP instead of introducing a second identity hub.[^s4] Designing which system holds the IdP role is a core single sign-on decision assessed by the identity and access management architect credential.[^s6]

## Connections

This feature is the outbound half of `kt:single-sign-on-saml` and one of the capabilities of `kt:salesforce-identity`; it implements the IdP role of `kt:saml-2-0` and, through the `openid` scope, `kt:openid-connect`.[^s3][^s4][^s5] Each service provider is configured via `kt:connected-apps`, and the signing certificate comes from `kt:certificate-and-key-management`.[^s1][^s3] Metadata endpoints hang off `kt:my-domain` and per-site endpoints tie it to `kt:experience-cloud-identity`.[^s1] Logout propagation to partners is handled by `kt:single-logout`, and the topic is covered by `kt:identity-and-access-management-architect-certification`.[^s6]

## Sources

[^s1]: Salesforce Help, "Enable Salesforce as a SAML Identity Provider". https://help.salesforce.com/s/articleView?id=sf.identity_provider_enable.htm&language=en_US&type=5 (accessed 2026-11-20)
[^s2]: Salesforce Help, "Complete Prerequisites for SAML Service Provider Integration". https://help.salesforce.com/s/articleView?language=en_US&id=sf.service_provider_prerequisites.htm&type=5 (accessed 2026-11-20)
[^s3]: Trailhead, "Integrate Service Providers with Salesforce" (Connected App Basics). https://trailhead.salesforce.com/content/learn/modules/connected-app-basics/connected-app-basics-sso (accessed 2026-11-20)
[^s4]: Trailhead, "Learn the Language of Identity" (Identity Basics). https://trailhead.salesforce.com/content/learn/modules/identity_basics/identity_basics_protocols (accessed 2026-11-20)
[^s5]: OASIS, "Security Assertion Markup Language (SAML) V2.0 Technical Overview". https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html (accessed 2026-11-20)
[^s6]: Trailhead, "Salesforce Certified Platform Identity and Access Management Architect". https://trailhead.salesforce.com/credentials/platformidentityandaccessmanagementarchitect (accessed 2026-11-20)
