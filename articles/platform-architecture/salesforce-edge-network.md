---
id: kt:salesforce-edge-network
type: Feature
title: Salesforce Edge Network
aliases: [Edge Network, Salesforce Edge, Salesforce EDGE, Hyperforce Edge Networking, Use Salesforce Edge Network]
domain: platform-architecture
summary: >-
  Salesforce's own edge layer, which routes My Domain traffic to the nearest Salesforce edge location for TLS
  termination, caching of cacheable static content, intelligent routing and TCP optimizations before forwarding
  requests to the org's data center over Salesforce's backbone.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:hyperforce, kt:custom-domains, kt:login-ip-ranges-and-trusted-ip-ranges, kt:content-delivery-network]
relations:
  - {predicate: dependsOn, object: kt:my-domain}
  - {predicate: integratesWith, object: kt:hyperforce}
  - {predicate: contrastsWith, object: kt:custom-domains}
  - {predicate: contrastsWith, object: kt:government-cloud}
sources:
  - id: s1
    title: "What Is Salesforce Edge Network?"
    publisher: Salesforce Developers (Identity Implementation Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/domain_name_edge_network_what_is.htm
    type: official-docs
    accessed: 2026-11-13
  - id: s2
    title: "Considerations for Salesforce Edge Network"
    publisher: Salesforce Developers (Identity Implementation Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/domain_name_edge_network_considerations.htm
    type: official-docs
    accessed: 2026-11-13
  - id: s3
    title: "Route My Domain Through Salesforce Edge Network"
    publisher: Salesforce Developers (Identity Implementation Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/domain_name_edge_network_route_my_domain.htm
    type: official-docs
    accessed: 2026-11-13
  - id: s4
    title: "Enhanced Domains"
    publisher: Salesforce Developers (Identity Implementation Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/domain_name_enhanced.htm
    type: official-docs
    accessed: 2026-11-13
  - id: s5
    title: "Optimizing Global Performance for the World's Most Trusted Enterprise Cloud"
    publisher: Salesforce Engineering
    url: https://engineering.salesforce.com/optimizing-global-performance-for-the-worlds-most-trusted-enterprise-cloud-58979125c9b6/
    type: official-blog
    accessed: 2026-11-13
  - id: s6
    title: "How Hyperforce Edge Networking Scales to Handle 20 Million Domains on Just 30GB of RAM"
    publisher: Salesforce Engineering
    url: https://engineering.salesforce.com/how-hyperforce-edge-networking-scales-to-handle-20-million-domains-on-just-30gb-of-ram/
    type: official-blog
    accessed: 2026-11-13
created: 2026-11-13
---

# Salesforce Edge Network

**Salesforce Edge Network** is a networking layer that Salesforce runs itself to make org pages load faster for users far from the org's data center. Rather than travelling the whole way to the data center, a request goes to the closest Salesforce edge location. There the connection is terminated and optimized, and the request is then carried to the data center over Salesforce's own high-bandwidth links. Traffic stays on Salesforce infrastructure the whole time.[^s1] Admins turn it on for an org through the **Routing** section of the My Domain Setup page.[^s3]

## How it works

The edge location provides four services:[^s1]

- **TLS termination.** The secure connection is set up at the edge, with persistent TLS connections that cut handshake time.[^s1]
- **Static content caching.** Only content that Salesforce or a customer integration marks as cacheable is cached, such as public JavaScript and CSS files.[^s1]
- **Intelligent routing.** Users are sent to the best-performing point of presence based on Salesforce's network measurements.[^s1]
- **TCP optimizations.** These make data transfer between the edge and the data center faster and more efficient.[^s1]

The latency case is easiest to see with numbers from Salesforce Engineering's early write-up, when the service was branded Salesforce EDGE (formerly Twin Prime). A Tokyo user reaching a UK data center at 125 ms round-trip time needs three round trips to open a TLS connection, roughly 375 ms. With an edge hop in Tokyo, that drops to roughly 75 ms.[^s5] The same post described route optimization based on measured latency and topology, and peering with large network providers to shorten paths.[^s5]

On Hyperforce, Salesforce Engineering describes the edge as acting as an internal CDN across Salesforce clouds. Its data centers span more than 20 regions, and it has grown to serve over 20 million domains.[^s6] The proxy layer keeps TLS certificates and secrets encrypted with AWS KMS. It respects web application firewalls and uses blue-green deployments.[^s6]

## Enabling it

1. Deploy My Domain first; it is a prerequisite.[^s3]
2. In Setup, open **My Domain**, edit **Routing**, select **Use Salesforce Edge Network**, and save. This takes the Customize Application permission.[^s3]

The feature is listed for Group, Essentials, Professional, Enterprise, Performance, Unlimited and Developer editions, in Lightning Experience and Salesforce Classic.[^s2][^s3]

## Limits and gotchas

- **One-way switch.** After an org moves to Edge Network, only Salesforce Customer Support can reverse it.[^s2][^s3]
- **Exclusions.** Public Cloud, Government Cloud, Customer 360 Data Manager and some individual orgs are excluded.[^s2][^s3]
- **IP allowlists.** Firewalls that allowlist Salesforce IP ranges by region must include the current ranges for every region where you have users.[^s2]
- **Certificate pinning.** Edge Network uses certificates specific to each data center. Pin the intermediate certificate, not the leaf certificate.[^s2][^s3]
- **Partial coverage.** Most My Domain URLs are routed. Turning on enhanced domains afterwards routes more URLs, because they then carry the My Domain name instead of the instance name.[^s2]
- **URLs not routed.** URLs with an instance name are not routed. Neither are custom domains for Sites and Experience Cloud sites, or `.force.com` site domains.[^s2]
- **More unrouted URLs.** Live Agent chat hosts, untrusted content domains and orgs in Government Isolated Architecture data centers are also not routed.[^s2]

## When to use it (and when not)

Turn it on when users are geographically far from the org's data center, especially for Lightning pages heavy with static assets. Those users gain the most from shorter handshakes and edge caching.[^s1][^s5] Before switching, check firewalls, proxies and integration clients that pin certificates or allowlist IPs, since the change can't be undone by an admin.[^s2] It does not replace a general-purpose CDN for public site content on custom domains, which are outside its routing.[^s2]

## Connections

Edge Network is part of the **Salesforce Platform** (`kt:salesforce-platform`) delivery infrastructure. It **depends on My Domain** (`kt:my-domain`), because routing is configured on the My Domain page and needs a deployed domain.[^s3] Enhanced domains, documented under My Domain, are available in orgs routed through the edge as well as in Hyperforce orgs.[^s4] It **integrates with Hyperforce** (`kt:hyperforce`), where the edge layer runs as an internal CDN across Salesforce clouds.[^s6] It **contrasts with custom domains** (`kt:custom-domains`), whose URLs are excluded from Edge Network routing.[^s2] It also **contrasts with Government Cloud** (`kt:government-cloud`), which is excluded from routing.[^s2] IP allowlisting ties it to **login IP ranges and trusted IP ranges** (`kt:login-ip-ranges-and-trusted-ip-ranges`), and its caching role relates it to a generic **content delivery network** (`kt:content-delivery-network`).[^s2][^s6]

## Sources
[^s1]: Salesforce Developers, "What Is Salesforce Edge Network?". https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/domain_name_edge_network_what_is.htm (accessed 2026-11-13)
[^s2]: Salesforce Developers, "Considerations for Salesforce Edge Network". https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/domain_name_edge_network_considerations.htm (accessed 2026-11-13)
[^s3]: Salesforce Developers, "Route My Domain Through Salesforce Edge Network". https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/domain_name_edge_network_route_my_domain.htm (accessed 2026-11-13)
[^s4]: Salesforce Developers, "Enhanced Domains". https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/domain_name_enhanced.htm (accessed 2026-11-13)
[^s5]: Salesforce Engineering, "Optimizing Global Performance for the World's Most Trusted Enterprise Cloud". https://engineering.salesforce.com/optimizing-global-performance-for-the-worlds-most-trusted-enterprise-cloud-58979125c9b6/ (accessed 2026-11-13)
[^s6]: Salesforce Engineering, "How Hyperforce Edge Networking Scales to Handle 20 Million Domains on Just 30GB of RAM". https://engineering.salesforce.com/how-hyperforce-edge-networking-scales-to-handle-20-million-domains-on-just-30gb-of-ram/ (accessed 2026-11-13)
