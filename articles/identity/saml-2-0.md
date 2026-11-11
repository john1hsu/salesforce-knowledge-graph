---
id: kt:saml-2-0
type: ExternalConcept
title: SAML 2.0
aliases: [Security Assertion Markup Language 2.0, SAML V2.0, SAML2, OASIS SAML]
domain: identity
summary: >-
  The OASIS XML standard (approved March 2005) for exchanging authentication, attribute and authorization statements
  between an identity provider and a service provider, built from assertions, protocols, bindings and profiles; its Web
  Browser SSO and Single Logout profiles underpin Salesforce's SAML single sign-on as both service provider and
  identity provider.
release: "Winter '27"
status: concept
broader: [kt:integration-security]
related: [kt:salesforce-identity, kt:my-domain, kt:multi-factor-authentication, kt:just-in-time-provisioning]
relations:
  - {predicate: consumedBy, object: kt:single-sign-on-saml}
  - {predicate: consumedBy, object: kt:single-logout}
  - {predicate: contrastsWith, object: kt:openid-connect}
  - {predicate: contrastsWith, object: kt:oauth-2-0}
sources:
  - id: s1
    title: "Security Assertion Markup Language (SAML) V2.0 Technical Overview (Committee Draft 02)"
    publisher: OASIS Security Services TC
    url: https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html
    type: standards-body
    accessed: 2026-11-11
  - id: s2
    title: "Assertions and Protocols for the OASIS Security Assertion Markup Language (SAML) V2.0 (saml-core-2.0-os)"
    publisher: OASIS
    url: https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf
    type: standards-body
    accessed: 2026-11-11
  - id: s3
    title: "Security and Privacy Considerations for the OASIS SAML V2.0 (saml-sec-consider-2.0-os)"
    publisher: OASIS
    url: https://docs.oasis-open.org/security/saml/v2.0/saml-sec-consider-2.0-os.pdf
    type: standards-body
    accessed: 2026-11-11
  - id: s4
    title: "SAML v2.0 Approved as OASIS Standard (press release)"
    publisher: OASIS
    url: https://www.oasis-open.org/?p=3715
    type: standards-body
    accessed: 2026-11-11
  - id: s5
    title: "Set Up Single Sign-On for Your Internal Users (Identity Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/identity_login/identity_login_sso
    type: official-learning
    accessed: 2026-11-11
created: 2026-11-11
---

# SAML 2.0

Security Assertion Markup Language (SAML) 2.0 is an XML-based framework, maintained by the OASIS Security Services Technical Committee, for exchanging security information between online business partners. Its headline uses are cross-domain web single sign-on and identity federation.[^s1] OASIS members approved version 2.0 as an OASIS Standard in March 2005. It merged three earlier efforts — SAML 1.x, the Liberty Alliance Identity Federation Framework (ID-FF) and Internet2's Shibboleth — and added federation management, attribute profiles, a metadata specification, encryption, pseudonyms and user consent.[^s4] This node describes the standard itself; Salesforce's configuration of it lives under SAML Single Sign-On.

## Roles and trust

SAML separates the **asserting party** (a SAML authority) from the **relying party** that consumes its statements. In web SSO the asserting party is the **identity provider (IdP)** and the relying party is the **service provider (SP)**; an attribute authority may also answer attribute queries. Everything rests on a trust relationship established in advance, typically backed by a PKI, which SAML recommends but does not require.[^s1]

## Building blocks

The specification is layered into four pieces:[^s1]

- **Assertions** carry statements about a subject: authentication, attribute and authorization-decision statements.[^s1]
- **Protocols** define request/response messages such as Authentication Request, Single Logout, Artifact Resolution and Name Identifier Management.[^s1]
- **Bindings** map those messages onto transports: HTTP Redirect, HTTP POST, HTTP Artifact, SAML SOAP, Reverse SOAP (PAOS) and SAML URI.[^s1]
- **Profiles** combine the three for a use case, most importantly Web Browser SSO, plus Single Logout, ECP and IdP Discovery.[^s1]

Two further pieces make deployments workable. **Metadata** lets each party publish its endpoints, supported bindings, roles and signing and encryption keys, and **authentication context** describes how the user authenticated, so an SP can ask for a stronger method such as multi-factor.[^s1]

An assertion must carry a version, ID, issue instant and an `Issuer`; it may add an XML signature, a `Subject`, and `Conditions` such as NotBefore/NotOnOrAfter, AudienceRestriction and OneTimeUse. The subject's `NameID` can use formats including unspecified, email address, X.509 subject name, persistent and transient.[^s2] **Persistent** identifiers stay linked to an SP account until removed, while **transient** ones are one-time values discarded at session end, giving the user anonymity at the SP.[^s1]

## Web Browser SSO flows

In the common **SP-initiated** flow, the user requests a protected resource, the SP redirects the browser to the IdP with an authentication request, and the IdP returns an assertion that the SP uses to grant or deny access. In the **IdP-initiated** flow, a user already signed in at the IdP follows a link and the IdP posts an unsolicited assertion to the SP's assertion consumer service.[^s1] When a response travels through the browser on the POST binding it must be digitally signed with XML Signature.[^s1]

## Security considerations

OASIS's non-normative security guide lists the main defences. Correlate each response to its request with `InResponseTo` and require origin authentication, protect integrity with XML Signature or TLS (encryption alone is not enough), and keep assertion validity to a few minutes with roughly synchronised clocks.[^s3] Assertions sent over the browser POST profile should carry OneTimeUse and the SP must refuse to reuse them; artifacts are likewise single-use and short-lived.[^s3] Signatures are only as strong as key management, so private keys need restricted access and certificate validity and revocation must be checked.[^s3]

## SAML 2.0 in Salesforce

Trailhead describes SAML as the protocol Salesforce Identity uses for SSO. In the classic inbound case a third-party IdP authenticates the user, Salesforce acts as the SP, and each side is configured with the other's details: the IdP's issuer and certificate go into Salesforce, while Salesforce supplies its Entity ID (the org's My Domain URL) and Login URL to the IdP.[^s5] Salesforce matches the asserted identity to a user, commonly through the **Federation ID**, a value that must be unique within an org but may repeat across orgs for the same person.[^s5]

## Connections

SAML 2.0 is the standard that **SAML Single Sign-On** and **Single Logout** consume, through its Web Browser SSO and Single Logout profiles.[^s1] It is part of the **Salesforce Identity** toolkit, and its endpoints and Entity ID hang off **My Domain**.[^s5] Its authentication-context mechanism is how an SP signals a need for **multi-factor authentication**, and attribute statements can carry user data that **just-in-time provisioning** relies on.[^s1] It is often confused with token-based standards: it contrasts with **OAuth 2.0**, which delegates API authorization rather than browser login, and with **OpenID Connect**, the JSON/JWT identity layer that serves the same SSO purpose. Its signing, TLS and replay protections make it part of the wider **integration security** picture.[^s3]

## Sources
[^s1]: OASIS Security Services TC, "Security Assertion Markup Language (SAML) V2.0 Technical Overview", Committee Draft 02 (25 March 2008). https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html (accessed 2026-11-11)
[^s2]: OASIS, "Assertions and Protocols for the OASIS Security Assertion Markup Language (SAML) V2.0", OASIS Standard (15 March 2005). https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf (accessed 2026-11-11)
[^s3]: OASIS, "Security and Privacy Considerations for the OASIS Security Assertion Markup Language (SAML) V2.0", OASIS Standard (15 March 2005). https://docs.oasis-open.org/security/saml/v2.0/saml-sec-consider-2.0-os.pdf (accessed 2026-11-11)
[^s4]: OASIS, "SAML v2.0 Approved as OASIS Standard" (March 2005). https://www.oasis-open.org/?p=3715 (accessed 2026-11-11)
[^s5]: Trailhead, "Set Up Single Sign-On for Your Internal Users", Identity Basics module. https://trailhead.salesforce.com/content/learn/modules/identity_login/identity_login_sso (accessed 2026-11-11)
