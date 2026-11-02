---
id: kt:single-sign-on-saml
type: Feature
title: SAML Single Sign-On
aliases: [single sign-on (SAML), SAML SSO, SAML single sign-on settings, federated authentication, inbound SAML SSO]
domain: identity
summary: >-
  Salesforce's implementation of the SAML 2.0 Web Browser SSO profile, letting an org or Experience Cloud site act as
  a service provider that trusts assertions from an external identity provider, or as an identity provider for other
  SAML-enabled apps.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity]
related: [kt:my-domain, kt:multi-factor-authentication, kt:connected-apps, kt:external-client-apps, kt:experience-cloud-identity, kt:oauth-2-flows-in-salesforce]
relations:
  - {predicate: implements, object: kt:saml-2-0}
  - {predicate: dependsOn, object: kt:my-domain}
  - {predicate: alternativeTo, object: kt:openid-connect-authentication-providers}
  - {predicate: coveredBy, object: kt:identity-and-access-management-architect-certification}
sources:
  - id: s1
    title: "Step 2: Create a SAML Single Sign-On Setting in Salesforce"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.sso_service_provider_configuration.htm&type=5
    type: official-docs
    accessed: 2026-11-02
  - id: s2
    title: "Salesforce as a Service Provider"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=xcloud.sso_sfdc_sp_rp_parent.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-02
  - id: s3
    title: "Salesforce as a SAML Identity Provider"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.sso_sfdc_idp_saml_parent.htm&type=5
    type: official-docs
    accessed: 2026-11-02
  - id: s4
    title: "Set Up Inbound SSO for Internal Users (Identity Login module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/identity_login/identity_login_sso
    type: official-learning
    accessed: 2026-11-02
  - id: s5
    title: "Security Assertion Markup Language (SAML) V2.0 Technical Overview"
    publisher: OASIS
    url: https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html
    type: standards-body
    accessed: 2026-11-02
created: 2026-11-02
---

# SAML Single Sign-On

SAML single sign-on lets users reach Salesforce without a separate Salesforce password: an external identity provider (IdP) authenticates them and sends a signed assertion that the org trusts. In Salesforce's terminology the org is then the **service provider** (SP), and SAML sits alongside authentication providers (predefined, OpenID Connect or custom Apex) as one of the inbound SSO options. SAML can also drive just-in-time (JIT) user provisioning on first login.[^s2] The reverse direction is supported too: an org or Experience Cloud site can act as a SAML IdP so its users sign in to external apps with Salesforce credentials.[^s3]

## How the protocol works

SAML 2.0, standardised by OASIS, separates an asserting party (the IdP) from a relying party (the SP). An assertion carries statements about a subject: authentication, attributes or authorization decisions. Messages travel over bindings such as HTTP Redirect, HTTP POST and HTTP Artifact, and the Web Browser SSO profile defines two flows. In **SP-initiated** login the user hits the SP first and is redirected to the IdP with an authentication request; in **IdP-initiated** login the user is already signed in at the IdP and is sent to the SP with an unsolicited assertion. Partners exchange metadata describing endpoints, bindings and keys, and the profile also defines single logout.[^s5]

## Configuring Salesforce as the service provider

An admin enables SAML under Single Sign-On Settings and creates a configuration manually or from an IdP metadata file or URL. Key fields:[^s1]

- **Issuer** must match the `Issuer` element in the IdP's assertion; **Entity ID** identifies the org (normally the My Domain URL) and must match an `Audience` value.[^s1]
- **Identity Provider Certificate** validates assertion signatures; a **Request Signing Certificate** and **Request Signature Method** (RSA-SHA1 or RSA-SHA256) sign SP-initiated requests. An **Assertion Decryption Certificate** is used when the IdP encrypts assertions.[^s1]
- **SAML Identity Type** chooses how the user is matched: Salesforce username, Federation ID, or User ID. **SAML Identity Location** is either the Subject's NameIdentifier or a named attribute (with a Name ID format such as unspecified, emailAddress or persistent).[^s1]
- **Service Provider Initiated Request Binding** is HTTP POST or HTTP Redirect, per the IdP's requirement; optional login, logout and error URLs control where users land.[^s1]

After saving, Salesforce generates SAML endpoints for the org and its Experience Cloud sites. Editing a configuration requires Customize Application and Modify All Data.[^s1]

## Gotchas

- **Federation ID hygiene.** The Federation ID on the user record must be unique within an org; a user present in several orgs should carry the same value in each, and bulk loading via Data Loader is the usual approach. Case-insensitive Federation ID matching is on by default and Salesforce recommends leaving it on.[^s4][^s1]
- **My Domain is the anchor.** Trailhead's setup uses the My Domain URL (with https) as the Entity ID and the Login URL from the Endpoints section as the IdP's recipient URL. Appending `?login` to the My Domain URL gives admins a fallback to standard login if the IdP fails.[^s4][^s1]
- **MFA still applies.** SSO users must satisfy MFA, either through Salesforce's MFA for SSO or the IdP's own MFA service.[^s4]
- **Digest algorithm drift.** For configurations created before Spring '22 the digest defaults to SHA1 unless the admin opts to derive it from the request signature method; newer configurations follow the chosen method automatically.[^s1]
- **New IdP-side apps.** When Salesforce is the IdP, each SP is set up as a SAML-enabled external client app or connected app; new connected apps can no longer be created as of Spring '26, so external client apps are the forward path.[^s3]

## When to use it (and when not)

Choose SAML when the enterprise IdP already federates other SaaS apps over SAML and the goal is interactive browser login for employees or site users. Choose an authentication provider instead when the IdP speaks OpenID Connect or when the integration also needs delegated access to third-party data, which authentication providers support and SAML does not.[^s2] Where Salesforce must be the hub that other apps trust, configure it as the SAML IdP instead, which supports both IdP-initiated and SP-initiated login, including forced authentication requests.[^s3]

## Connections

SAML SSO is a core capability of **Salesforce Identity** and **implements** the OASIS **SAML 2.0** standard.[^s2][^s5] It **depends on My Domain**, whose URL serves as the entity ID and login endpoint.[^s4] It is the main **alternative to OpenID Connect authentication providers** for inbound federation.[^s2] When Salesforce acts as the IdP, service providers are registered as **external client apps** or legacy **connected apps**, which also host **OAuth 2.0 flows** for API access.[^s3] It interacts with **multi-factor authentication** because SSO logins must still meet the MFA requirement, and the same endpoints extend to **Experience Cloud identity** for customer and partner sites.[^s4][^s1] The topic is examined in the **Identity and Access Management Architect** certification.

## Sources
[^s1]: Salesforce Help, "Step 2: Create a SAML Single Sign-On Setting in Salesforce". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.sso_service_provider_configuration.htm&type=5 (accessed 2026-11-02)
[^s2]: Salesforce Help, "Salesforce as a Service Provider". https://help.salesforce.com/s/articleView?id=xcloud.sso_sfdc_sp_rp_parent.htm&language=en_US&type=5 (accessed 2026-11-02)
[^s3]: Salesforce Help, "Salesforce as a SAML Identity Provider". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.sso_sfdc_idp_saml_parent.htm&type=5 (accessed 2026-11-02)
[^s4]: Trailhead, "Set Up Inbound SSO for Internal Users". https://trailhead.salesforce.com/content/learn/modules/identity_login/identity_login_sso (accessed 2026-11-02)
[^s5]: OASIS, "Security Assertion Markup Language (SAML) V2.0 Technical Overview". https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html (accessed 2026-11-02)
