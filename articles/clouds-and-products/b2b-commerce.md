---
id: kt:b2b-commerce
type: Product
title: B2B Commerce
aliases: [Salesforce B2B Commerce, B2B Commerce on Lightning, B2B Commerce on Lightning Experience]
domain: clouds-and-products
summary: >-
  Salesforce's business-to-business ecommerce product, built natively on the Salesforce Platform so that stores use CRM
  accounts, contacts, products and price books directly, with buyer groups and entitlement policies controlling which
  business buyers see which products and prices.
release: "Winter '27"
status: current
broader: [kt:commerce-cloud]
related: [kt:sales-cloud, kt:service-cloud, kt:experience-cloud, kt:salesforce-dx, kt:salesforce-platform]
relations:
  - {predicate: partOf, object: kt:commerce-cloud}
  - {predicate: contrastsWith, object: kt:b2c-commerce}
  - {predicate: dependsOn, object: kt:price-books}
  - {predicate: configuredVia, object: kt:experience-builder}
  - {predicate: queriedWith, object: kt:connect-api}
  - {predicate: integratesWith, object: kt:salesforce-order-management}
sources:
  - id: s1
    title: "Get Started with B2B Commerce (B2B Commerce Basics, Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/b2b-commerce-basics/get-started-with-b2b-commerce
    type: official-learning
    accessed: 2026-11-28
  - id: s2
    title: "Understand How CRM Powers B2B Commerce (B2B Commerce Basics, Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/b2b-commerce-basics/understand-how-crm-powers-b2b-commerce
    type: official-learning
    accessed: 2026-11-28
  - id: s3
    title: "Organize How Customers Access Your Commerce Store (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/b2b-commerce-lightning-experience-data-model/organize-how-buyers-access-your-store
    type: official-learning
    accessed: 2026-11-28
  - id: s4
    title: "Get Started with B2B Commerce (B2B Commerce Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-comm-dev-guide.html
    type: official-docs
    accessed: 2026-11-28
  - id: s5
    title: "B2B Commerce Data Model (B2B Commerce Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-dev-data-model.html
    type: official-docs
    accessed: 2026-11-28
created: 2026-11-28
---

# B2B Commerce

B2B Commerce is the part of Salesforce's commerce family built for businesses that sell to other businesses online. Trailhead frames it around buying relationships that are more complex than consumer shopping: carts with hundreds of line items, orders worth large sums, pricing and terms negotiated per account, and orders that a sales rep or call-center agent often places on the buyer's behalf.[^s1] Unlike B2C Commerce, which runs on its own platform, B2B Commerce is built natively on the Salesforce Lightning Platform and works out of the box with Sales Cloud, Service Cloud and community sites.[^s1]

## What buyers get

Trailhead lists the buyer-facing capabilities that distinguish a B2B store from a consumer one.[^s1]

- **Personal catalogs and pricing**: buyers see exclusive items and prices set by contract or segment.[^s1]
- **Large orders and fast reorders**: carts can hold hundreds or thousands of SKUs, and repeat orders take a couple of clicks.[^s1]
- **Advanced shipping**: one order can be split across several delivery dates and locations.[^s1]
- **Payment choice**: invoices, ACH and credit cards, so buyers with credit can pay on terms (for example by purchase order) while others pay by card at checkout.[^s1][^s2]

Because the store shares the org with CRM, account and contact records are the backbone of the commerce data. A seller can see account health and next-best-action prompts while the buyer browses, and service agents can handle order status and invoice questions from the same record.[^s2] Trailhead groups the product into four areas: experience management (the branded storefront, quick order, search and merchandising), a commerce engine for products, prices and promotions by account or segment (including multi-currency and multi-language), account and order management (checkout, order history, tracking and invoices), and dashboards and reports that combine commerce with sales, service and marketing data.[^s2]

## How it works: the data model

A store is a **WebStore** record, the site where buyers transact, which declares the currencies, languages and price books it supports.[^s5] Products (Product2) are organized into a **ProductCatalog** of categories that provisions the store, and prices come from standard price books, with PricebookEntry joining a price book to a product.[^s5]

Access is controlled by three objects that matter most to an architect:[^s3][^s5]

- **Buyer accounts**: a standard Account is enabled as a buyer account, then its contacts are enabled as buyers; only buyers and buyer managers can purchase.[^s3]
- **Buyer groups**: connect buyer accounts to a store and carry shared settings, so a store can serve several groups with different products, prices and entitlements.[^s3][^s5]
- **Entitlement policies**: CommerceEntitlementPolicy links buyer groups to products, with CanViewProduct and CanViewPrice fields controlling visibility.[^s5]

The BuyerAccount object also carries the buyer's financial details such as credit and order limits.[^s5] Carts are WebCart records holding product, shipping and tax totals, and the data model supports Salesforce Order Management downstream of checkout.[^s5] The data model is available in Enterprise, Unlimited and Developer editions.[^s5]

## Building and extending stores

Stores are built from the Commerce template in Experience Builder.[^s4] The developer guide distinguishes LWR-template stores from older Aura-template stores: on LWR, predefined flows simplify tax, shipping and payment integrations, while Aura stores set up those integrations differently.[^s4] Custom storefront components are Lightning Web Components added to an LWR store, and Salesforce recommends Salesforce DX for building them.[^s4] Programmatic access goes through the Connect Commerce API, which manages catalogs, inventory, carts and order processing, and extension points support integrations with ERP systems and payment gateways; the guide also documents headless storefronts.[^s4]

## When to use it (and gotchas)

Choose B2B Commerce when the buyer is a known business account whose pricing, catalog and terms already live in CRM; choose B2C Commerce for high-traffic anonymous consumer storefronts on a separate platform.[^s1][^s4] The same template and APIs also power D2C stores, which differ mainly in access: a D2C store uses a single buyer group so every shopper sees the same products and prices, whereas a B2B store segments buyers into many groups.[^s3][^s4] The common gotcha is visibility: a product a buyer cannot see is usually missing from the buyer group's entitlement policy or price book rather than broken in the catalog.[^s3][^s5]

## Connections

B2B Commerce is **part of** `kt:commerce-cloud` and **contrasts with** `kt:b2c-commerce`, which uses a different platform, APIs and skill set.[^s1][^s4] It **depends on** `kt:price-books` for pricing, is **configured via** `kt:experience-builder` templates, and is **queried with** the `kt:connect-api` Commerce resources.[^s4][^s5] Orders flow into Salesforce Order Management.[^s5] It is related to `kt:sales-cloud` and `kt:service-cloud`, whose reps and agents work the same accounts and orders, to `kt:experience-cloud` sites, and to `kt:salesforce-dx` for component development.[^s1][^s2][^s4]

## Sources

[^s1]: Trailhead, "Get Started with B2B Commerce". https://trailhead.salesforce.com/content/learn/modules/b2b-commerce-basics/get-started-with-b2b-commerce (accessed 2026-11-28)
[^s2]: Trailhead, "Understand How CRM Powers B2B Commerce". https://trailhead.salesforce.com/content/learn/modules/b2b-commerce-basics/understand-how-crm-powers-b2b-commerce (accessed 2026-11-28)
[^s3]: Trailhead, "Organize How Customers Access Your Commerce Store". https://trailhead.salesforce.com/content/learn/modules/b2b-commerce-lightning-experience-data-model/organize-how-buyers-access-your-store (accessed 2026-11-28)
[^s4]: Salesforce Developers, "Get Started with B2B Commerce", B2B Commerce Developer Guide. https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-comm-dev-guide.html (accessed 2026-11-28)
[^s5]: Salesforce Developers, "B2B Commerce Data Model", B2B Commerce Developer Guide. https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-dev-data-model.html (accessed 2026-11-28)
