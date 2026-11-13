---
id: kt:commerce-cloud
type: Product
title: Commerce Cloud
aliases: [Agentforce Commerce, Salesforce Commerce Cloud, SFCC, Demandware]
domain: clouds-and-products
summary: >-
  Salesforce's commerce product family, now taught on Trailhead under the umbrella name Agentforce Commerce, spanning
  B2C Commerce storefronts, B2B and D2C Commerce stores on the core platform, Order Management, Payments and point of sale.
release: "Winter '27"
status: current
broader: [kt:customer-360]
related: [kt:experience-cloud, kt:lightning-web-components, kt:marketing-cloud-engagement, kt:service-cloud, kt:connect-api]
relations:
  - {predicate: hasPart, object: kt:b2c-commerce}
  - {predicate: hasPart, object: kt:b2b-commerce}
  - {predicate: hasPart, object: kt:salesforce-order-management}
  - {predicate: integratesWith, object: kt:data-cloud}
  - {predicate: integratesWith, object: kt:agentforce}
  - {predicate: configuredVia, object: kt:experience-builder}
sources:
  - id: s1
    title: "Discover Commerce Cloud (Commerce Cloud Quick Look, Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/commerce-cloud-quick-look/discover-commerce-cloud
    type: official-learning
    accessed: 2026-11-13
  - id: s2
    title: "Get to Know the Agentforce Commerce Products (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agentforce-commerce-and-the-unified-commerce-platform/get-to-know-the-agentforce-commerce-products
    type: official-learning
    accessed: 2026-11-13
  - id: s3
    title: "B2C Commerce Storefront Options"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/commerce/sfra/guide/which-product.html
    type: official-docs
    accessed: 2026-11-13
  - id: s4
    title: "B2B Commerce Developer Guide: Get Started"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide
    type: official-docs
    accessed: 2026-11-13
created: 2026-11-13
---

# Commerce Cloud

Commerce Cloud is Salesforce's ecommerce software for companies that sell business-to-business (B2B), business-to-consumer (B2C) or direct-to-consumer (D2C, sometimes called B2B2C).[^s1] Current Trailhead content presents the family under the umbrella name Agentforce Commerce, while page titles and module names still use Commerce Cloud, so practitioners will meet both names for the same product.[^s1][^s2] Trailhead describes it as a unified platform that brings ecommerce, order management and point-of-sale tools together.[^s2]

## Where it came from

The family was assembled through acquisitions. Demandware joined Salesforce in 2016 and became the B2C product, CloudCraze added B2B capabilities, and a D2C product followed later.[^s1] That history explains the most important architectural fact about Commerce Cloud: it is not one codebase. B2C Commerce runs on its own platform with its own APIs and storefront frameworks, while B2B Commerce runs on the Salesforce Lightning Platform alongside CRM data.[^s1][^s3][^s4]

## The product family

- **B2C Commerce**: scalable, localized storefronts with geo-specific sites, multiple languages and privacy tools for GDPR and CCPA.[^s2]
- **B2B Commerce**: stores for known business buyers, with large carts, quick reorders, per-account themes and complex multi-location shipping.[^s1]
- **D2C Commerce**: lets B2B merchants sell straight to consumers, with guided setup and drag-and-drop storefronts.[^s1]
- **Order Management**: the order lifecycle from capture through fulfillment, payment capture, invoicing and service, in one multichannel order repository.[^s2]
- **Salesforce Payments**: cards, digital wallets, direct debit and local methods, plus Pay Now links that can be shared or embedded in records.[^s2]
- **Point of sale**: a POS app that connects to Order Management, Omnichannel Inventory and B2C Commerce, including buy-online-pickup-in-store.[^s2]

## How the two main platforms are built

**B2C Commerce.** Developers choose among four storefront approaches.[^s3] Storefront Next is the recommended option for new sites; it is built on React and React Router, runs on Managed Runtime, and supports server-side rendering.[^s3] The Storefront Reference Architecture (SFRA) uses server-side HTML and JavaScript with the Script API and suits teams reusing existing SFRA code and connectors.[^s3] A hybrid path lets an SFRA site move to Storefront Next gradually, and a build-your-own option uses the B2C Commerce API (SCAPI) with any front-end stack.[^s3] The documentation positions SCAPI as the main API for customization, ahead of the older OCAPI.[^s3]

**B2B and D2C Commerce.** Stores are built from a Commerce template in Experience Builder; custom components are Lightning Web Components on the Lightning Web Runtime (LWR) template, with Salesforce DX recommended.[^s4] The Connect Commerce API handles catalogs, inventory, carts and order processing, and a headless path supports guest cart and checkout using JWT.[^s4] The Store object is the hub for transactional configuration, and buyer groups, buyer accounts and entitlement policies control who sees which products and prices.[^s2] LWR stores ship with predefined flows for tax, shipping and payment provider integrations.[^s4]

## AI and agents

Agentforce Guided Shopping gives B2C shoppers real-time assistance, visual product search and in-chat checkout with Apple Pay and Google Pay, while Agentforce Guided Buying helps B2B buyers find products, reorder and check order status.[^s2] Storefront Next also supports a Shopper Agent for AI-assisted shopping.[^s3] B2C Commerce uses Data 360 for a unified customer view and Einstein AI for personalization and product recommendations.[^s2]

## Gotchas and when to use what

- **Pick the platform before the features.** B2C and B2B Commerce differ in hosting, data model, APIs and skill sets, so a B2C developer's SFRA experience does not transfer to an LWR store.[^s1][^s3][^s4]
- **B2B fits known accounts.** Use it when buyers are existing CRM accounts with negotiated entitlements and recurring orders; use B2C for anonymous, high-volume consumer traffic.[^s1]
- **Aura and LWR stores differ.** The B2B developer guide notes that integrations work differently in older Aura stores, so check the template before reusing code.[^s4]
- **New B2C storefronts default to Storefront Next.** SFRA remains supported for existing sites, with the hybrid path for gradual migration.[^s3]

## Connections

- **broader → `kt:customer-360`**: Commerce sits beside sales, service and marketing in Salesforce's customer platform; D2C Commerce shares a data model spanning B2B, B2C, Order Management, CMS, Sales and Service.[^s1]
- **hasPart → `kt:b2c-commerce`, `kt:b2b-commerce`, `kt:salesforce-order-management`**: the major product lines described above.[^s1][^s2]
- **integratesWith → `kt:data-cloud`**: B2C Commerce and B2B analytics draw on Data 360.[^s2]
- **integratesWith → `kt:agentforce`**: Guided Shopping and Guided Buying agents.[^s2]
- **configuredVia → `kt:experience-builder`**: B2B and D2C stores start from a Commerce Experience Builder template.[^s4]
- **related → `kt:experience-cloud`, `kt:lightning-web-components`, `kt:connect-api`**: the site, component and API layers B2B stores are built from.[^s4]
- **related → `kt:service-cloud`, `kt:marketing-cloud-engagement`**: B2C Commerce is pitched as integrating ecommerce with marketing and service, and D2C's unified model includes Service.[^s1]

## Sources
[^s1]: Trailhead, "Discover Commerce Cloud". https://trailhead.salesforce.com/content/learn/modules/commerce-cloud-quick-look/discover-commerce-cloud (accessed 2026-11-13)
[^s2]: Trailhead, "Get to Know the Agentforce Commerce Products". https://trailhead.salesforce.com/content/learn/modules/agentforce-commerce-and-the-unified-commerce-platform/get-to-know-the-agentforce-commerce-products (accessed 2026-11-13)
[^s3]: Salesforce Developers, "B2C Commerce Storefront Options". https://developer.salesforce.com/docs/commerce/sfra/guide/which-product.html (accessed 2026-11-13)
[^s4]: Salesforce Developers, "B2B Commerce Developer Guide: Get Started". https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide (accessed 2026-11-13)
