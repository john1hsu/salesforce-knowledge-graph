---
id: kt:mutual-tls-authentication
type: SecurityControl
title: Mutual TLS Authentication
aliases: [mTLS, mutual TLS, two-way SSL, 2-way SSL, mutual authentication, Enforce SSL/TLS Mutual Authentication]
domain: identity
summary: >-
  A TLS handshake in which both sides present X.509 certificates, so the server also authenticates the client.
  In Salesforce it secures inbound API calls (port 8443, a trusted Mutual Authentication certificate and the
  Enforce SSL/TLS Mutual Authentication permission) and outbound callouts that present an org client certificate.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity]
related: [kt:zero-trust-architecture, kt:login-ip-ranges-and-trusted-ip-ranges, kt:mulesoft-anypoint-platform, kt:oauth-2-0]
relations:
  - {predicate: dependsOn, object: kt:certificate-and-key-management}
  - {predicate: consumedBy, object: kt:named-credentials}
  - {predicate: consumedBy, object: kt:apex-callouts}
  - {predicate: integratesWith, object: kt:jwt-bearer-flow}
  - {predicate: configuredVia, object: kt:external-client-apps}
sources:
  - id: s1
    title: "Enhance Integration Security with mTLS for Salesforce and MuleSoft"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2025/10/enhance-integration-security-with-mtls-for-salesforce-and-mulesoft
    type: official-blog
    accessed: 2026-11-17
  - id: s2
    title: "From Manual to Automated: A Taxonomy to Secure Your Salesforce Environment in the Short-Lived Certificate Era"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/from-manual-to-automated-a-taxonomy-to-secure-your-salesforce-environment-in-the-short-lived-certificate-era/
    type: official-blog
    accessed: 2026-11-17
  - id: s3
    title: "Certificate requirements for two-way SSL (Salesforce Help knowledge article 000007225)"
    publisher: Salesforce
    url: https://help.salesforce.com/HTViewSolution?id=000007225
    type: official-docs
    accessed: 2026-11-17
  - id: s4
    title: "RFC 8705: OAuth 2.0 Mutual-TLS Client Authentication and Certificate-Bound Access Tokens"
    publisher: IETF
    url: https://www.rfc-editor.org/rfc/rfc8705.html
    type: standards-body
    accessed: 2026-11-17
  - id: s5
    title: "Salesforce Setup Guide: Mutual Authentication (mTLS)"
    publisher: Fivetran
    url: https://fivetran.com/docs/connectors/applications/salesforce/setup-guide/mtls
    type: partner
    accessed: 2026-11-17
created: 2026-11-17
---

# Mutual TLS Authentication

Ordinary (one-way) TLS proves only the server's identity to the caller. Mutual TLS, often called two-way SSL, adds a second step: the client also presents an X.509 certificate during the handshake, and the server refuses the connection unless that certificate chains to a root it trusts and maps to a known client.[^s4] Salesforce's security team groups its certificate flows into inbound one-way TLS, inbound user mTLS (browser login), inbound API mTLS, and outbound Apex mTLS, and treats the last three as places where the customer owns the client certificate.[^s2]

## How it works in Salesforce

**Inbound API mTLS (Salesforce as server).** An integration that calls an org's APIs over mTLS needs three pieces on the Salesforce side. First, a CA-signed client certificate is uploaded to the Mutual Authentication Certificates list in Certificate and Key Management. Second, the integration user gets a permission set holding both the Enforce SSL/TLS Mutual Authentication and API Only User permissions. Third, the client connects on port 8443 rather than the default 443, typically after obtaining a token through an external client app configured for the JWT bearer flow.[^s1] The certificate must carry the Client Authentication extended key usage, chain to a root listed on the instance's trusted CA page, and be sent with its full chain.[^s2]

**Inbound user mTLS.** Browser login can also require a client certificate, but the user's certificate must be mapped to their account. A partner's setup guide warns that once the enforcement permission applies to a user, that user can no longer sign in through the UI, which is why the permission belongs on a dedicated API-only integration user.[^s2][^s5]

**Outbound mTLS (Salesforce as client).** For callouts, the org holds a certificate and private key and presents it to the remote server. Apex can name the certificate explicitly with `setClientCertificateName`, or a named credential can carry it as its client certificate; the target server must already trust it, and a self-signed certificate works only if the server has it in its keystore.[^s1][^s3] Outbound messages, delegated authentication and SAML use the certificate selected as the org's API client certificate.[^s3]

**Relationship to OAuth.** The IETF standard RFC 8705 lets an OAuth client authenticate to the authorization server with its TLS certificate and lets the server bind access tokens to that certificate's SHA-256 thumbprint, so a stolen token is useless without the private key.[^s4] Salesforce's documented pattern is different: mTLS protects the transport on port 8443 while a separate OAuth JWT bearer token, signed with its own certificate, authenticates the user.[^s1]

## Limits and gotchas

- **Port 8443 is mandatory inbound.** A named credential pointing at an mTLS-protected org must state port 8443 in its URL explicitly.[^s1]
- **Two certificates, two jobs.** The JWT signing certificate can be self-signed; the mTLS certificate must be CA-signed. Mixing them up is the common setup failure.[^s1]
- **Intermediates are not added for you.** Salesforce will not put intermediate certificates on its trust list, so the client must send the complete chain; a root outside the supported list needs a support request first.[^s3]
- **Public CAs are dropping client authentication.** Public TLS certificates are being limited to server authentication, so Salesforce advises using a private PKI for mTLS client certificates; a partner guide adds that certificates requested from March 15, 2027 should come from a CA's dedicated client-authentication hierarchy.[^s2][^s5]
- **Rotation is yours.** Salesforce rotates its server certificate for inbound flows unless you bring your own, but never the client certificate; for outbound Apex mTLS it rotates neither. With validity periods heading toward 47 days, Salesforce recommends automating renewal and rehearsing it in a sandbox.[^s2]

## When to use it (and when not)

Use mTLS when policy demands that only known machines can even open a connection to the org, for example in zero-trust designs or regulated system-to-system integrations, or when a partner API requires a client certificate from Salesforce callouts.[^s1][^s2] It adds certificate lifecycle work and a dedicated port, so for most integrations an OAuth flow with IP restrictions is lighter; mTLS is a transport control layered under OAuth, not a replacement for it.[^s1][^s4]

## Connections

Mutual TLS sits under **Salesforce Identity** and `dependsOn` **Certificate and Key Management**, where both the trusted client certificates and the org's own client certificates live.[^s1][^s3] Outbound, it is consumed by **named credentials** and **Apex callouts**; inbound, it is paired with the **JWT bearer flow** configured through an **external client app**.[^s1] It complements the network-level checks of **login and trusted IP ranges**, supports **zero-trust architecture**, extends the **OAuth 2.0** model per RFC 8705, and is set up on the client side of **MuleSoft Anypoint Platform** through a keystore in the Salesforce connector.[^s1][^s2][^s4]

## Sources

[^s1]: Salesforce Developers Blog, "Enhance Integration Security with mTLS for Salesforce and MuleSoft" (2025-10-09). https://developer.salesforce.com/blogs/2025/10/enhance-integration-security-with-mtls-for-salesforce-and-mulesoft (accessed 2026-11-17)
[^s2]: Salesforce, "From Manual to Automated: A Taxonomy to Secure Your Salesforce Environment in the Short-Lived Certificate Era". https://www.salesforce.com/blog/from-manual-to-automated-a-taxonomy-to-secure-your-salesforce-environment-in-the-short-lived-certificate-era/ (accessed 2026-11-17)
[^s3]: Salesforce Help, knowledge article 000007225 on certificates for two-way SSL. https://help.salesforce.com/HTViewSolution?id=000007225 (accessed 2026-11-17)
[^s4]: IETF, "RFC 8705: OAuth 2.0 Mutual-TLS Client Authentication and Certificate-Bound Access Tokens" (February 2020). https://www.rfc-editor.org/rfc/rfc8705.html (accessed 2026-11-17)
[^s5]: Fivetran, "Salesforce Setup Guide: Mutual Authentication (mTLS)". https://fivetran.com/docs/connectors/applications/salesforce/setup-guide/mtls (accessed 2026-11-17)
