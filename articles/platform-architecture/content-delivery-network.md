---
id: kt:content-delivery-network
type: Concept
title: Content Delivery Network
aliases: [CDN, Salesforce CDN, Lightning CDN, content delivery networks in Salesforce]
domain: platform-architecture
summary: >-
  A distributed set of caching servers that delivers publicly cacheable content from locations close to users; in
  Salesforce it appears as the partner-run Salesforce CDN for Experience Cloud and custom domains, the option to front a
  custom domain with a third-party CDN, and the Lightning CDN that serves framework JavaScript and CSS.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform, kt:distributed-computing]
related: [kt:salesforce-edge-network, kt:custom-domains, kt:experience-cloud, kt:platform-cache, kt:session-settings]
relations:
  - {predicate: consumedBy, object: kt:experience-cloud}
  - {predicate: dependsOn, object: kt:custom-domains}
  - {predicate: contrastsWith, object: kt:salesforce-edge-network}
  - {predicate: configuredVia, object: kt:session-settings}
sources:
  - id: s1
    title: "Content Delivery Networks (CDNs) and Salesforce"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=platform.community_builder_cdn_overview.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-16
  - id: s2
    title: "Considerations for the Salesforce CDN"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.community_builder_cdn_considerations.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-16
  - id: s3
    title: "Options to Serve a Custom Domain"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.domain_mgmt_domain_config_options.htm&type=5
    type: official-docs
    accessed: 2026-11-16
  - id: s4
    title: "Enable CDN to Load Applications Faster"
    publisher: Salesforce Developers (Lightning Web Components Developer Guide)
    url: https://developer.salesforce.com/docs/platform/lwc/guide/perf-cdn.html
    type: official-docs
    accessed: 2026-11-16
  - id: s5
    title: "Which Performance Tools Do I Need Based on My Experience Cloud Site?"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.exp_cloud_site_use_cases.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-16
  - id: s6
    title: "RFC 9111: HTTP Caching"
    publisher: IETF (RFC Editor)
    url: https://www.rfc-editor.org/rfc/rfc9111
    type: standards-body
    accessed: 2026-11-16
created: 2026-11-16
---

# Content Delivery Network

A **content delivery network (CDN)** is a fleet of caching servers spread across many locations. It serves publicly cacheable content from a server near the user instead of from the origin. Pages load faster, and the origin carries less traffic.[^s1] In HTTP terms, a CDN node is a **shared cache**: it stores a response so many users can reuse it. A **private cache**, such as a browser's, serves only one user.[^s6]

In Salesforce, "CDN" names three related things. One is the **Salesforce CDN**, run by a Salesforce CDN partner, for Experience Cloud sites and custom domains. Another is a **third-party CDN** placed in front of a custom domain. The third is the **Lightning CDN** for framework assets.[^s1][^s4]

## How it works in Salesforce

- **Default site domain.** Experience Cloud sites get a system-managed `*.my.site.com` domain that already uses the Salesforce CDN. Government Cloud Plus orgs can opt out.[^s1][^s2]
- **Custom domain on the Salesforce CDN.** Salesforce recommends this option for Digital Experiences sites. It serves only subdomains such as `www.example.com`, not registrable domains like `example.com`, and isn't available for Salesforce Sites.[^s1][^s3]
- **Custom domain behind a third-party CDN.** The domain points to the external service, which forwards requests. Salesforce identifies the site from the forwarded Host header.[^s3] This is the only CDN option for registrable domains and Salesforce Sites.[^s1]
- **Lightning CDN.** It serves static Lightning Component framework JavaScript and CSS through Akamai, and doesn't distribute Salesforce data or metadata.[^s4] You enable it in Session Settings with the "Enable Content Delivery Network (CDN) for Lightning Component framework" checkbox.[^s4]

What gets cached depends on the site framework. Aura sites cache mostly static assets such as CMS content, images, JavaScript, CSS and fonts.[^s2] LWR sites also cache base page documents and public data from Salesforce API calls and internal Apex methods.[^s2] An Apex method's result is cached only if it is annotated `@AuraEnabled(cacheable=true scope='global')`, and it should return public data only.[^s2] This follows the general HTTP rule that a response marked `private` must not be stored by a shared cache.[^s6]

## Limits and gotchas

- **Editions.** The site CDN options are documented for Enterprise, Performance and Unlimited Editions.[^s1][^s2]
- **Request and upload limits.** Maximum URI size is 16 KB. Uploads are capped at 128 MB per file on `*.my.site.com` and 500 MB per file on custom domains.[^s2]
- **Annual allowances.** With an Experience Cloud license, a third-party CDN setup gets 10 single-certificate domains and 48 TB of traffic per year.[^s2] Orgs without that license get 5 domains and 5 TB.[^s2]
- **Provisioning time.** Salesforce CDN provisioning usually finishes within 12 hours and can take up to 24. Activation can take up to 20 minutes to propagate.[^s2]
- **Switch-over blips.** Moving an existing domain to the Salesforce CDN can cause connection resets or DNS errors for up to 5 minutes, so activate during quiet periods.[^s2]
- **DNS discipline.** Keep the CNAME shown on the Domains Setup page and leave the `_acme-challenge` record alone. If you use Cloudflare DNS, set the records to DNS only, not proxied.[^s2]
- **IPv6 and allowlists.** The Salesforce CDN supports IPv6, so IPv4-only login IP ranges, including the guest profile's, can block users.[^s2]
- **Lightning CDN domain.** Add `https://static.lightning.force.com` to firewall allowlists, and don't filter that domain by IP address, because its IPs are dynamic.[^s4]
- **Regional and product limits.** The Salesforce CDN isn't recommended for sites with users in China. Commerce LWR sites can't use a CDN outside Salesforce.[^s2][^s1]
- **Security extras.** Single-certificate domains on the Salesforce CDN include a web application firewall and rate limiting. Admins can turn these enhanced security services off if valid requests are blocked.[^s2]

## When to use it (and when not)

Salesforce lists its CDN as a recommended tool for every high-traffic Experience Cloud pattern. That covers guest-heavy help centers, authenticated portals, transaction-heavy business flows and B2B partner sites.[^s5] For guest and portal traffic it pairs the CDN with LWR and Apex caching on the CDN.[^s5] Choose a third-party CDN when you need an apex domain, serve Salesforce Sites, or already run a corporate CDN or WAF.[^s1][^s3] Never cache personalized data in a shared cache. Keep anything user-specific out of globally scoped cacheable Apex.[^s2][^s6]

## Connections

The CDN is part of the **Salesforce Platform** (`kt:salesforce-platform`) delivery layer and an applied case of **distributed computing** (`kt:distributed-computing`), pushing copies of content to the network edge.[^s1] Its main consumer is **Experience Cloud** (`kt:experience-cloud`), whose sites use it by default.[^s1] It **depends on custom domains** (`kt:custom-domains`) for branded hosting, since the serving option is chosen per domain.[^s3] It **contrasts with Salesforce Edge Network** (`kt:salesforce-edge-network`), which routes My Domain traffic rather than serving site domains.[^s3] The Lightning CDN is **configured via Session Settings** (`kt:session-settings`).[^s4] It complements **Platform Cache** (`kt:platform-cache`): the CDN caches public responses at the edge, while Platform Cache holds data inside the org.[^s2][^s6]

## Sources
[^s1]: Salesforce Help, "Content Delivery Networks (CDNs) and Salesforce". https://help.salesforce.com/s/articleView?id=platform.community_builder_cdn_overview.htm&language=en_US&type=5 (accessed 2026-11-16)
[^s2]: Salesforce Help, "Considerations for the Salesforce CDN". https://help.salesforce.com/s/articleView?id=sf.community_builder_cdn_considerations.htm&language=en_US&type=5 (accessed 2026-11-16)
[^s3]: Salesforce Help, "Options to Serve a Custom Domain". https://help.salesforce.com/s/articleView?language=en_US&id=platform.domain_mgmt_domain_config_options.htm&type=5 (accessed 2026-11-16)
[^s4]: Salesforce Developers, "Enable CDN to Load Applications Faster". https://developer.salesforce.com/docs/platform/lwc/guide/perf-cdn.html (accessed 2026-11-16)
[^s5]: Salesforce Help, "Which Performance Tools Do I Need Based on My Experience Cloud Site?". https://help.salesforce.com/s/articleView?id=sf.exp_cloud_site_use_cases.htm&language=en_US&type=5 (accessed 2026-11-16)
[^s6]: IETF, "RFC 9111: HTTP Caching". https://www.rfc-editor.org/rfc/rfc9111 (accessed 2026-11-16)
