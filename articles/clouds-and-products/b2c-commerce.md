---
id: kt:b2c-commerce
type: Product
title: B2C Commerce
aliases: [Salesforce B2C Commerce, B2C Commerce Cloud, Commerce Cloud Digital, B2C Commerce realm]
domain: clouds-and-products
summary: >-
  Salesforce's multi-tenant SaaS platform for consumer-facing digital storefronts, provisioned per customer as a realm of
  production, staging, development and sandbox instances and managed in Business Manager, with storefronts built on SFRA
  cartridges or the headless Composable Storefront (PWA Kit and Managed Runtime).
release: "Winter '27"
status: current
broader: [kt:commerce-cloud]
related: [kt:b2c-solution-architect-certification, kt:b2c-commerce-architect-certification, kt:passkeys, kt:continuous-integration-for-salesforce, kt:sandbox-types]
relations:
  - {predicate: partOf, object: kt:commerce-cloud}
  - {predicate: hasPart, object: kt:storefront-reference-architecture}
  - {predicate: hasPart, object: kt:composable-storefront}
  - {predicate: configuredVia, object: kt:business-manager}
  - {predicate: queriedWith, object: kt:salesforce-commerce-api}
  - {predicate: contrastsWith, object: kt:b2b-commerce}
sources:
  - id: s1
    title: "B2C Commerce Architecture"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/commerce/commerce-api/guide/get-started
    type: official-docs
    accessed: 2026-11-28
  - id: s2
    title: "Configuring B2C Commerce Sites (Architecture of B2C Commerce, Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/architecture-of-commerce-cloud-digital/cc-digital-configuration
    type: official-learning
    accessed: 2026-11-28
  - id: s3
    title: "Configure On-Demand Sandbox Roles and Settings Effectively (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/b2c-on-demand-sandbox/b2c-configure-on-demand-sandbox
    type: official-learning
    accessed: 2026-11-28
  - id: s4
    title: "SFRA Features and Components"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/commerce/sfra/guide/b2c-sfra-features-and-comps.html
    type: official-docs
    accessed: 2026-11-28
  - id: s5
    title: "Composable Storefront Overview"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/commerce/b2c-commerce/guide/getting-started.html
    type: official-docs
    accessed: 2026-11-28
  - id: s6
    title: "PWA Kit Overview"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/commerce/b2c-commerce/guide/pwa-kit-overview.html
    type: official-docs
    accessed: 2026-11-28
created: 2026-11-28
---

# B2C Commerce

B2C Commerce is the consumer-facing storefront platform within Salesforce's commerce family. It runs on its own dedicated infrastructure: each customer receives a **realm**, and the sites inside it are administered in Business Manager, with users managed in Account Manager.[^s1][^s2] A **site** is the application behind a storefront. One site can serve several storefronts, such as separate URLs for different brands, locales or channels. A site goes live when it is set to Online in Manage Sites in production Business Manager.[^s1]

## How it works: realms and instances

A realm is the top-level unit Salesforce provisions for a customer. It contains a primary instance group (PIG) and a secondary instance group (SIG).[^s2] The PIG has three instances. **Production** hosts the live sites. **Staging** is where merchandisers prepare catalogs, price books and promotions and preview the storefront. **Development** is where new custom code is tested against current staging data. Data moves from staging to development or production through replication.[^s1][^s2] The SIG holds sandboxes, with a minimum of 3 and a maximum of 47; Salesforce describes a typical realm as having about six instances.[^s1] Page caching is off on sandbox, staging and development, and on production it is enabled all the way to the browser. This matters when you compare performance across environments.[^s1]

On the infrastructure side, a realm sits behind a firewall and load balancer. Web servers and a web adapter handle page caching and spread load across app servers, and production runs at least two web servers and two app servers. Each instance has its own database schema and a shared file system that holds cartridges, images and logs.[^s2] Every instance runs its own Business Manager. The sites in an instance form an organization, and settings apply either to one site or to the whole organization.[^s2] Operational tasks such as starting instances are done in Control Center, and user accounts are managed in Account Manager.[^s1]

## On-demand sandboxes

Sandboxes in the SIG are on-demand. They run on public cloud and are created through the self-service B2C Commerce Developer Sandbox REST API, using a configured API client ID and the four-character realm ID.[^s2][^s3] They are paid for with purchased credits. A running medium sandbox (1 CPU, 10 GB) uses 1 credit per minute, larger profiles use more, and a stopped sandbox still uses 0.3 credits per minute until it is deleted.[^s3] Each sandbox has a time to live that defaults to 24 hours, and the realm maximum can be set up to 2,160 hours. A TTL of 0 turns automatic deletion off. You can also schedule start and stop times at realm level to keep idle environments from consuming credits.[^s3]

## Storefront options

- **Storefront Reference Architecture (SFRA)**: an MVC storefront built from cartridges. The cartridge path set in Business Manager decides the order, which runs from custom cartridges through LINK and plug-in cartridges down to `app_storefront_base`.[^s4]
- **SFRA customization rule**: overlay `app_storefront_base` and the `server` module from custom cartridges placed further left on the path. Never edit them directly, or upgrades will need manual merges.[^s4]
- **Composable Storefront**: a headless option that pairs PWA Kit, a server-side-rendered React framework, with Managed Runtime hosting. It reaches the platform through the B2C Commerce API (SCAPI) and OCAPI.[^s5][^s6]

On the cartridge path, the first controller with a given name wins. That is how the cartridges to the left override behavior from the base.[^s4] Each Managed Runtime deployment fully replaces the previous one. Salesforce reports a historical uptime of 99.99% for the service.[^s5] Each PWA Kit major version gets security patches for at least 24 months after its GA. Because the docs also track Node.js end-of-life dates, projects need to keep upgrading their runtime.[^s6]

## When to use it (and when not)

B2C Commerce fits high-traffic, merchandiser-driven consumer storefronts that need catalog sharing across brands and locales. Sites in the same realm can share a catalog. Sites in different realms cannot, except by importing the data, so the realm boundary is a key early design decision.[^s1] Choose SFRA when you want server-rendered cartridges that can reuse LINK integrations. Choose Composable Storefront when you want a React front end with headless APIs and separate hosting.[^s4][^s5]

## Connections

- **partOf → `kt:commerce-cloud`**: B2C Commerce is documented as one product line within Salesforce's Commerce Cloud developer documentation.[^s1][^s5]
- **hasPart → `kt:storefront-reference-architecture`, `kt:composable-storefront`**: the two main storefront approaches described above.[^s4][^s5]
- **configuredVia → `kt:business-manager`**: each instance has its own Business Manager, which handles site configuration and the cartridge path.[^s2][^s4]
- **queriedWith → `kt:salesforce-commerce-api`**: headless storefronts reach shopper and admin data through SCAPI.[^s5][^s6]
- **contrastsWith → `kt:b2b-commerce`**: the sibling commerce product for business buyers, commonly confused with B2C Commerce; B2C Commerce's realm, instance-group and replication model is specific to it.[^s1]
- **related**: its on-demand sandboxes are provisioned and billed differently from core `kt:sandbox-types`, they serve continuous-integration testing (`kt:continuous-integration-for-salesforce`), and the node links to passkey login and the B2C architect certifications.[^s2][^s3]

## Sources
[^s1]: Salesforce Developers, "B2C Commerce Architecture". https://developer.salesforce.com/docs/commerce/commerce-api/guide/get-started (accessed 2026-11-28)
[^s2]: Trailhead, "Configuring B2C Commerce Sites". https://trailhead.salesforce.com/content/learn/modules/architecture-of-commerce-cloud-digital/cc-digital-configuration (accessed 2026-11-28)
[^s3]: Trailhead, "Configure On-Demand Sandbox Roles and Settings Effectively". https://trailhead.salesforce.com/content/learn/modules/b2c-on-demand-sandbox/b2c-configure-on-demand-sandbox (accessed 2026-11-28)
[^s4]: Salesforce Developers, "SFRA Features and Components". https://developer.salesforce.com/docs/commerce/sfra/guide/b2c-sfra-features-and-comps.html (accessed 2026-11-28)
[^s5]: Salesforce Developers, "Composable Storefront Overview". https://developer.salesforce.com/docs/commerce/b2c-commerce/guide/getting-started.html (accessed 2026-11-28)
[^s6]: Salesforce Developers, "PWA Kit Overview". https://developer.salesforce.com/docs/commerce/b2c-commerce/guide/pwa-kit-overview.html (accessed 2026-11-28)
