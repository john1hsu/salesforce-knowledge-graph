---
id: kt:certificate-based-authentication
type: Feature
title: Certificate-Based Authentication
aliases: [CBA, Salesforce certificate-based authentication, user authentication certificates, certificate-based login, smart card login, PIV/CAC login]
domain: identity
summary: >-
  A Salesforce login method in which individual users authenticate to the org with an X.509 client certificate
  (uploaded as a user authentication certificate) instead of, or in addition to, a password. Enabled in Identity
  Verification settings and exposed as a Certificate-Based Login button on the My Domain login page.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity, kt:multi-factor-authentication]
related: [kt:mutual-tls-authentication, kt:security-keys, kt:lightning-login, kt:fedramp-high, kt:zero-trust-architecture]
relations:
  - {predicate: configuredVia, object: kt:identity-verification}
  - {predicate: configuredVia, object: kt:my-domain}
  - {predicate: dependsOn, object: kt:certificate-and-key-management}
  - {predicate: implements, object: kt:nist-digital-identity-guidelines}
  - {predicate: mitigates, object: kt:account-takeover}
sources:
  - id: s1
    title: "Enable Certificate-Based Authentication"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.security_certificate_based_auth_enable.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-22
  - id: s2
    title: "Add Certificate-Based Authentication to Your My Domain Login Page"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=security_certificate_based_auth_login.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-22
  - id: s3
    title: "Certificate-Based Authentication (Mobile Device Management)"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=xcloud.mobile_security_mdm_cert.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-22
  - id: s4
    title: "Prepare for Phishing-Resistant MFA Enforcement for Privileged Users including Admins"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005321563&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-22
  - id: s5
    title: "UserAuthCertificate | Metadata API Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_userauthcertificate.htm
    type: official-docs
    accessed: 2026-11-22
  - id: s6
    title: "FIPS 201: Personal Identity Verification (PIV) of Federal Employees and Contractors, Section 6 PIV Cardholder Authentication"
    publisher: NIST
    url: https://pages.nist.gov/FIPS201/authentication
    type: standards-body
    accessed: 2026-11-22
created: 2026-11-22
---

# Certificate-Based Authentication

Certificate-based authentication (CBA) lets an org authenticate individual users with digital certificates rather than relying only on a username and password. Salesforce describes the uploaded user certificate as a PEM-encoded X.509 certificate that is associated with a specific user and used to authenticate that user.[^s1][^s5] Once it is set up, the org's My Domain login page shows a **Certificate-Based Login** button next to (or instead of) the normal login form.[^s2] It is the Salesforce counterpart of the smart-card logins common in government and regulated industries, where the certificate lives on a PIV or CAC card or in a device's secure hardware.[^s4][^s6]

## How it works

CBA is a user login method, not an integration method. The client presents its certificate during a mutual TLS handshake, and Salesforce's phishing-resistant MFA guidance notes that the private key is normally held in secure hardware such as a TPM or secure enclave, with a corporate certificate installed on the device.[^s4] Because there is no typed secret and the key stays in hardware, Salesforce counts this among the phishing-resistant forms of MFA.[^s4]

The certificate itself is represented in metadata as **UserAuthCertificate**. Each record carries a label and developer name, the certificate's serial number, its expiration date and the user it belongs to, and Salesforce documents these certificates as externally uploaded.[^s5] In other words, the org does not issue user certificates; an enterprise certificate authority or PIV issuer does, and admins upload or deploy the public certificate for each user.[^s5][^s1]

NIST's PIV standard describes the same pattern at the card level. In its PKI-AUTH mechanism the relying system validates the PIV Authentication certificate (path, expiry and revocation), the cardholder unlocks the card with a PIN, and the card signs a challenge with its private key.[^s6] NIST rates PKI-AUTH at authenticator assurance level AAL3 for remote access and notes that it needs certificate status checking infrastructure to block revoked cards.[^s6]

## Configuring it

Setup is a two-step process in Setup:

- **Enable the feature**: in **Identity Verification**, select *Let users authenticate with a certificate*. This needs the Manage Internal Users permission and is available in all editions, in Classic and Lightning Experience.[^s1]
- **Upload user certificates**: add a user authentication certificate for each user who logs in this way, before exposing the login option.[^s2][^s5]
- **Expose it on the login page**: in **My Domain**, edit Authentication Configuration and select **Certificate** as an authentication service. This needs Customize Application and adds the Certificate-Based Login button.[^s2]

Salesforce Help also groups companion tasks under the feature, including validating the revocation status of user authentication certificates and reviewing certificate login errors, which matter for the same reason NIST stresses status checking.[^s1][^s6]

### Mobile apps through MDM

For Salesforce mobile apps, CBA is turned on through a mobile device management (MDM) suite rather than Setup. Salesforce says certificates can remove usernames and passwords from mobile provisioning, either authenticating the user outright or acting as a second factor.[^s3] Two managed key-value pairs control it:

- **RequireCertAuth** (Boolean, Android and iOS): starts the certificate flow. Android uses the device's user certificate inside a webview; iOS sends authentication requests to Safari.[^s3]
- **ManagedAppCertAlias** (String, Android only): the alias of the on-device certificate the app should present.[^s3]

## CBA and phishing-resistant MFA

Salesforce's 2026 enforcement of phishing-resistant MFA for privileged users (System Administrator profile, or permissions such as Modify All Data, View All Data, Customize Application and Author Apex) lists certificate-based authentication among the supported phishing-resistant methods.[^s4] For SSO, the same article treats identity-provider assertions whose AMR or ACR values signal certificate or smart-card login (for example x509, pki or smartcard) as phishing-resistant.[^s4] Read the direct-login table in that article carefully, though: it names security keys, built-in authenticators and temporary codes for direct logins, so teams should confirm in their own org how a CBA login is classified before relying on it to meet the requirement.[^s4]

## Gotchas and when to use it

- **Certificate lifecycle is yours**: every uploaded certificate has an expiration date, so plan renewals and re-uploads as part of user management.[^s5]
- **Revocation**: a lost card or device is only blocked if revocation status is checked; configure validation rather than relying on deletion alone.[^s1][^s6]
- **Not API mTLS**: certificates for API clients use a separate Mutual Authentication certificate setup, covered under certificate and key management.[^s1]

CBA fits public-sector and defense workloads that already issue PIV or CAC cards, and enterprises with managed devices and an internal PKI.[^s6][^s3] Where users already sign in to a corporate identity provider with smart cards, SAML or OpenID Connect SSO that passes certificate-based AMR values is often simpler; for orgs without a PKI, security keys give similar phishing resistance with less infrastructure.[^s4]

## Connections

CBA is part of **Salesforce Identity** and a phishing-resistant form of **multi-factor authentication**.[^s4] It is configured via **identity verification** settings and the **My Domain** login page, and depends on **certificate and key management** practices for uploading, renewing and revoking certificates.[^s1][^s2] It shares the TLS client-certificate mechanism with **mutual TLS authentication**, which applies it to API traffic instead of user logins.[^s4][^s1] It implements the certificate-based authenticator model of the **NIST digital identity guidelines** and PIV standards, which matters for **FedRAMP High** and **zero trust** programs.[^s6] Like **security keys** and **Lightning Login**, it removes reusable passwords from the login and so mitigates **account takeover**.[^s4]

## Sources
[^s1]: Salesforce Help, "Enable Certificate-Based Authentication". https://help.salesforce.com/s/articleView?id=sf.security_certificate_based_auth_enable.htm&language=en_US&type=5 (accessed 2026-11-22)
[^s2]: Salesforce Help, "Add Certificate-Based Authentication to Your My Domain Login Page". https://help.salesforce.com/s/articleView?id=security_certificate_based_auth_login.htm&language=en_US&type=5 (accessed 2026-11-22)
[^s3]: Salesforce Help, "Certificate-Based Authentication" (Mobile Device Management). https://help.salesforce.com/s/articleView?id=xcloud.mobile_security_mdm_cert.htm&language=en_US&type=5 (accessed 2026-11-22)
[^s4]: Salesforce Help, "Prepare for Phishing-Resistant MFA Enforcement for Privileged Users including Admins". https://help.salesforce.com/s/articleView?id=005321563&language=en_US&type=1 (accessed 2026-11-22)
[^s5]: Salesforce Developers, "UserAuthCertificate", Metadata API Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_userauthcertificate.htm (accessed 2026-11-22)
[^s6]: NIST, FIPS 201, "PIV Cardholder Authentication". https://pages.nist.gov/FIPS201/authentication (accessed 2026-11-22)
