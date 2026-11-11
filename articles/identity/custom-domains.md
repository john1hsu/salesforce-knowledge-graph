---
id: kt:custom-domains
type: Feature
title: Custom Domains
aliases: [custom domain, custom URLs, branded site domain, Salesforce custom domain]
domain: identity
summary: >-
  A domain the customer owns (for example www.example.com) that is added on the Domains Setup page and mapped, via
  custom URL records, to Experience Cloud sites and Salesforce Sites so external users reach them on a branded address
  instead of a Salesforce-managed host.
release: "Winter '27"
status: current
broader: [kt:experience-cloud]
related: [kt:my-domain, kt:salesforce-edge-network, kt:experience-builder, kt:experience-cloud-identity, kt:hyperforce]
relations:
  - {predicate: contrastsWith, object: kt:my-domain}
  - {predicate: consumedBy, object: kt:salesforce-sites}
  - {predicate: dependsOn, object: kt:certificate-and-key-management}
sources:
  - id: s1
    title: "Custom Domains in Salesforce"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.domain_mgmt_overview.htm&amp=&type=5
    type: official-docs
    accessed: 2026-11-11
  - id: s2
    title: "Set Up a Custom Domain That Uses Your HTTPS Certificate"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=domain_mgmt_cert_setup.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-11
  - id: s3
    title: "Brand Your Salesforce Org's Domains"
    publisher: Salesforce Developers (Identity Implementation Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/domain_name_brand_your_org.htm
    type: official-docs
    accessed: 2026-11-11
  - id: s4
    title: "Include SNI Extension for Custom Domains Using Salesforce Cloud Option with Salesforce Edge Network"
    publisher: Salesforce Help (Knowledge Article 000389364)
    url: https://help.salesforce.com/s/articleView?id=000389364&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-11
  - id: s5
    title: "Considerations for Salesforce Edge Network"
    publisher: Salesforce Developers (Identity Implementation Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/domain_name_edge_network_considerations.htm
    type: official-docs
    accessed: 2026-11-11
  - id: s6
    title: "Experience Cloud (Salesforce Help PDF)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/communities.pdf
    type: official-docs
    accessed: 2026-11-11
created: 2026-11-11
---

# Custom Domains

A custom domain is a domain that the customer already owns, such as `www.example.com`, used to serve an org's Experience Cloud sites or Salesforce Sites so that external visitors see a branded address rather than a Salesforce-managed host.[^s1][^s3] The content still comes from the org; only the hostname changes.[^s3] Salesforce's own site domains (ending in `*.my.site.com`, `*.my.salesforce-sites.com` or `*.force.com`) and the `MyDomainName.my.salesforce.com` login domain are managed by Salesforce and cannot be edited, whereas custom domains are added by an admin on the **Domains** Setup page.[^s1] The feature is available in Enterprise, Performance and Unlimited Editions and applies to Salesforce Sites and to LWR, Aura and Visualforce sites.[^s1][^s6]

## Why use one

Salesforce lists four benefits: a branded experience for external users, the ability for several sites to share a domain (or one site to answer on several brand domains), simpler domain and network allowlist management, and a stable address when the Salesforce-hosted site URL changes after a My Domain rename.[^s1] The Experience Cloud guide adds that setting the domain up while the site is still being built means visitors use the branded address from day one, which helps search ranking and avoids updating hard-coded links later.[^s6]

## Domains, custom URLs and paths

A domain on its own serves nothing. Each **custom URL** record ties a domain, a site and an optional path together, so domains and sites form a many-to-many relationship: one domain can serve `/shop`, `/help` and `/apply` from different sites.[^s1][^s6] The documented ceilings are 200 sites per domain and 500 domains per site; because an Experience Cloud site counts as two sites, a domain serving only Experience Cloud sites tops out at 100.[^s1]

## HTTPS options

Salesforce describes three ways to serve a custom domain over HTTPS: with the customer's own certificate on Salesforce servers, through the Salesforce content delivery network (CDN) partner, or through a third-party CDN, web application firewall or other host.[^s1][^s2] The certificate option is set up roughly as follows:[^s2]

1. Add the domain on the Domains page and choose to serve it with your HTTPS certificate on Salesforce servers, selecting a certificate from Certificate and Key Management.[^s2]
2. Create a DNS CNAME record pointing the domain at the target host name the page displays, which embeds the 18-character org ID.[^s2]
3. Save (status **Awaiting Custom URL**), add the first custom URL to start provisioning, then click **Activate** once the status reads **Awaiting Activation**.[^s2]

The current configuration then shows as **Salesforce Cloud**.[^s2] Domains on this cloud option are being moved onto Salesforce Edge Network, which relies on the client sending the TLS Server Name Indication (SNI) extension; without SNI, Edge Network returns a default certificate that only covers `.my.salesforce.com` hostnames and the handshake fails with a name mismatch.[^s4]

## Limits and gotchas

- Timing: DNS changes can take up to 20 hours worldwide, provisioning takes 4–14 hours after the first custom URL, and activation can take the site offline for 5–10 minutes.[^s2]
- Until it is activated, a new custom domain is served over HTTP rather than HTTPS, so plan go-live around activation.[^s2]
- Sandbox custom domains are added in the production org that owns the sandbox, using the Associated Org field, which is editable only from production.[^s2]
- Permissions: editing or deleting a domain needs Manage Custom Domains; adding domains or custom URLs also needs Create and Set Up Experiences or a Site.com Publisher license.[^s2]
- SNI failures typically come from API clients or upstream CDNs that do not send or forward the original hostname, not from browsers.[^s4]
- Custom-domain URLs are excluded from the Edge Network routing that applies to My Domain URLs, so My Domain routing settings do not govern them.[^s5]
- In a Professional Edition org using Marketing Cloud Account Engagement, the custom domain must use the Salesforce CDN.[^s6]

## Connections

Custom domains sit under **Experience Cloud**, whose sites (built in **Experience Builder**) are their main consumers, alongside **Salesforce Sites**.[^s1][^s6] They **contrast with My Domain**: My Domain gives the org a Salesforce-suffixed subdomain for login and application URLs, while a custom domain is a domain the company owns and covers only Sites and Experience Cloud sites.[^s3] The certificate option **depends on Certificate and Key Management** for the HTTPS certificate, and the cloud option is being migrated onto the **Salesforce Edge Network**.[^s2][^s4] It is listed as related to **Hyperforce** because both affect how org traffic is routed and which hostnames integrations must trust.[^s5] Because an Experience Cloud site's external users reach it on this address, the custom domain is also the visible host for the sign-in pages designed under **Experience Cloud identity**.[^s1][^s6]

## Sources

[^s1]: Salesforce Help, "Custom Domains in Salesforce". https://help.salesforce.com/s/articleView?language=en_US&id=sf.domain_mgmt_overview.htm&amp=&type=5 (accessed 2026-11-11)
[^s2]: Salesforce Help, "Set Up a Custom Domain That Uses Your HTTPS Certificate". https://help.salesforce.com/s/articleView?id=domain_mgmt_cert_setup.htm&language=en_US&type=5 (accessed 2026-11-11)
[^s3]: Salesforce Developers, "Brand Your Salesforce Org's Domains". https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/domain_name_brand_your_org.htm (accessed 2026-11-11)
[^s4]: Salesforce Help, "Include SNI Extension for Custom Domains Using Salesforce Cloud Option with Salesforce Edge Network" (000389364). https://help.salesforce.com/s/articleView?id=000389364&language=en_US&type=1 (accessed 2026-11-11)
[^s5]: Salesforce Developers, "Considerations for Salesforce Edge Network". https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/domain_name_edge_network_considerations.htm (accessed 2026-11-11)
[^s6]: Salesforce, Experience Cloud guide (PDF), "Configure a Custom Domain for Your Experience Cloud Site". https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/communities.pdf (accessed 2026-11-11)
