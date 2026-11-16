---
id: kt:certificate-and-key-management
type: Feature
title: Certificate and Key Management
aliases: [Certificates and Keys, Certificate and Key Management page, Salesforce certificates, self-signed certificate, CA-signed certificate, Import from Keystore]
domain: identity
summary: >-
  The Setup page and Certificate metadata type where an org creates, imports, renews and stores the X.509
  certificates and key pairs it uses to sign SAML and JWT assertions, present a client certificate on mutual-TLS
  callouts, and trust inbound mutual-authentication clients.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity]
related: [kt:custom-domains, kt:mutual-tls-authentication, kt:salesforce-as-identity-provider, kt:mulesoft-anypoint-platform]
relations:
  - {predicate: consumedBy, object: kt:single-sign-on-saml}
  - {predicate: consumedBy, object: kt:jwt-bearer-flow}
  - {predicate: consumedBy, object: kt:named-credentials}
  - {predicate: consumedBy, object: kt:apex-callouts}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: enables, object: kt:mutual-tls-authentication}
sources:
  - id: s1
    title: "Certificate (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_certificate.htm
    type: official-docs
    accessed: 2026-11-16
  - id: s2
    title: "Generate a Salesforce Compatible JKS From PFX or P12 (Knowledge Article 000381987)"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000381987&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-16
  - id: s3
    title: "Resolving 'Keystore contains an entry whose alias is not acceptable for import' Error (Knowledge Article 000387657)"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000387657&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-16
  - id: s4
    title: "\"Data Not Available\" Error When Importing Keystore Certificate (Knowledge Article 005228563)"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005228563&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-16
  - id: s5
    title: "Enhance Integration Security with mTLS for Salesforce and MuleSoft"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2025/10/enhance-integration-security-with-mtls-for-salesforce-and-mulesoft
    type: official-blog
    accessed: 2026-11-16
  - id: s6
    title: "From Manual to Automated: A Taxonomy to Secure Your Salesforce Environment in the Short-Lived Certificate Era"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/?p=138659
    type: official-blog
    accessed: 2026-11-16
created: 2026-11-16
---

# Certificate and Key Management

Certificate and Key Management is the Setup page (under Security) where a Salesforce org keeps the X.509 certificates and key pairs it uses to prove its own identity. The same records are exposed to deployment tooling as the `Certificate` metadata type, which Salesforce describes as the certificate behind digital signatures that show a request came from your org, for example when it signs single sign-on assertions or acts as an identity provider.[^s1] The page also holds a separate list of mutual-authentication certificates that the org trusts for inbound mutual-TLS clients.[^s5]

## How it works

An admin creates one of two kinds of certificate. A **self-signed** certificate is generated and signed by Salesforce on save. A **CA-signed** certificate starts as a certificate signing request (CSR): you download the CSR, have a certificate authority sign it, and upload the signed chain, after which the record's expiration date updates to match the signed certificate.[^s1] Key size is 2048 or 4096 bits, defaulting to 2048; for self-signed certificates the expiry is set automatically to one year for a 2048-bit key and two years for a 4096-bit key, and the larger key is slower to use but lasts longer.[^s1]

Other metadata fields record whether the certificate is CA-signed, its label (up to 64 characters), whether the private key is exportable (true by default) and whether it is encrypted with Platform Encryption. Files use the `.crt` suffix in a `certs` folder, the type has existed since API version 36.0, and `package.xml` accepts the `*` wildcard for it.[^s1]

Certificates that already exist outside Salesforce arrive through **Import from Keystore**, which takes a Java keystore. A PFX or P12 file returned by a CA is not accepted as-is: Salesforce's support guidance rebuilds it with OpenSSL (converting the private key to PKCS8) and Java `keytool` into a JKS, then imports that file on the Certificate and Key Management page.[^s2]

## Limits and gotchas

- **Private keys stay put through the API.** The Metadata API cannot import or export private keys, and uploading an existing certificate to renew it copies its X.509 parameters but generates a new key pair.[^s1]
- **CSR availability.** Once the signed chain is uploaded, the CSR can no longer be retrieved through the API, although the UI still shows it.[^s1]
- **Keystore aliases are strict.** Aliases may use only letters, digits and underscores, must start with a letter, cannot end with an underscore or contain two underscores in a row; one bad alias blocks the whole import.[^s3]
- **Identity Provider must be on.** Import from Keystore fails with a vague "Data Not Available" error when Identity Provider is not enabled in the org; enabling it first resolves the error.[^s4]
- **Shorter certificate lifetimes.** Public TLS certificates are moving from roughly a year toward lifetimes as short as 45 or 47 days, and public CAs are dropping the Client Authentication usage that client certificates need.[^s6]

## Who rotates what

Salesforce's own guidance splits responsibility by flow. Salesforce rotates the server certificate for inbound TLS unless you bring your own; for outbound Apex mutual TLS and for SAML or OIDC/JWT single sign-on, rotation is the customer's job.[^s6] For signing SSO and JWT assertions, Salesforce suggests a long-lived self-signed certificate so partners don't need frequent metadata updates, while mutual-TLS client certificates should come from a private PKI as public CAs drop client authentication.[^s6]

## When to use it (and when not)

Use a self-signed certificate when only the relying party needs to trust a signature you control, as with SAML assertion signing or the JWT bearer flow; use a CA-signed one when the other side validates the chain, as in mutual TLS. In a Salesforce-to-Salesforce mutual-TLS setup, the server org uploads a CA-signed certificate as a mutual authentication certificate, the client org stores the CA-signed mTLS certificate plus an OAuth signing certificate, and the integration user receives the Enforce SSL/TLS Mutual Authentication and API Only User permissions.[^s5] Outbound, a named credential points at port 8443 with a CA-signed client certificate, or Apex sets it with `setClientCertificateName`.[^s5]

## Connections

The page sits under **Salesforce Identity** because signing keys underpin identity flows. **SAML single sign-on** and **JWT bearer flow** consume its certificates to sign assertions, and **Salesforce as an identity provider** must be enabled before keystore import works.[^s1][^s4] **Named credentials** and **Apex callouts** present its client certificates, which enables **mutual TLS authentication**; MuleSoft apps on **MuleSoft Anypoint Platform** hold the matching keys in their own keystores.[^s5] The **Metadata API** `Certificate` type moves certificates between orgs without their private keys.[^s1] **Custom domains** link here as a dependency because their own-certificate option relies on a certificate kept on this page; it is listed as related rather than restated.

## Sources
[^s1]: Salesforce Developers, "Certificate (Metadata API Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_certificate.htm (accessed 2026-11-16)
[^s2]: Salesforce Help, "Generate a Salesforce Compatible JKS From PFX or P12". https://help.salesforce.com/s/articleView?id=000381987&language=en_US&type=1 (accessed 2026-11-16)
[^s3]: Salesforce Help, "Resolving 'Keystore contains an entry whose alias is not acceptable for import' Error". https://help.salesforce.com/s/articleView?id=000387657&language=en_US&type=1 (accessed 2026-11-16)
[^s4]: Salesforce Help, "\"Data Not Available\" Error When Importing Keystore Certificate". https://help.salesforce.com/s/articleView?id=005228563&language=en_US&type=1 (accessed 2026-11-16)
[^s5]: Salesforce Developers Blog, "Enhance Integration Security with mTLS for Salesforce and MuleSoft" (2025-10-09). https://developer.salesforce.com/blogs/2025/10/enhance-integration-security-with-mtls-for-salesforce-and-mulesoft (accessed 2026-11-16)
[^s6]: Salesforce, "From Manual to Automated: A Taxonomy to Secure Your Salesforce Environment in the Short-Lived Certificate Era". https://www.salesforce.com/blog/?p=138659 (accessed 2026-11-16)
