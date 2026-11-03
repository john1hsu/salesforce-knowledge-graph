---
id: kt:revenue-cloud
type: Product
title: Agentforce Revenue Management
aliases: [Revenue Cloud, Revenue Management, Revenue Lifecycle Management, Salesforce Revenue Cloud]
domain: clouds-and-products
summary: >-
  Salesforce's product-to-cash suite (formerly Revenue Cloud) that covers product catalog, pricing, configuration,
  quotes and orders, asset lifecycle, order orchestration, contracts, usage rating and billing on the core platform.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:sales-cloud, kt:metadata-api]
relations:
  - {predicate: replaces, object: kt:salesforce-cpq}
  - {predicate: hasPart, object: kt:salesforce-pricing}
  - {predicate: hasPart, object: kt:product-configurator}
  - {predicate: hasPart, object: kt:dynamic-revenue-orchestrator}
  - {predicate: integratesWith, object: kt:agentforce}
  - {predicate: coveredBy, object: kt:revenue-management-consultant-certification}
sources:
  - id: s1
    title: "Meet Revenue Lifecycle Management (Revenue Lifecycle Management Foundations)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/revenue-lifecycle-management-foundations/meet-revenue-lifecycle-management
    type: official-learning
    accessed: 2026-11-03
  - id: s2
    title: "Explore Revenue Lifecycle Management (Revenue Lifecycle Management Foundations)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/revenue-lifecycle-management-foundations/explore-revenue-lifecycle-management
    type: official-learning
    accessed: 2026-11-03
  - id: s3
    title: "Get Started with Revenue Management Developer Resources (Revenue Management Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/rlm_get_started.htm
    type: official-docs
    accessed: 2026-11-03
  - id: s4
    title: "Configure Pricing for Products (Revenue Cloud Design)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/revenue-cloud-design/configure-pricing-for-products
    type: official-learning
    accessed: 2026-11-03
  - id: s5
    title: "Set Up Your Product Offerings (Revenue Cloud Design)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/revenue-cloud-design/set-up-your-product-offerings
    type: official-learning
    accessed: 2026-11-03
  - id: s6
    title: "Navigating the Future of Salesforce CPQ: Product End of Sale (Not End of Life)"
    publisher: Salesforce
    url: https://www.salesforce.com/sales/cpq/end-of-life/
    type: official-blog
    accessed: 2026-11-03
created: 2026-11-03
---

# Agentforce Revenue Management

Agentforce Revenue Management is Salesforce's product-to-cash suite for selling and buying across channels. Trailhead states plainly that **Revenue Cloud is now Agentforce Revenue Management**, and warns that the old name still shows up in the app and in documentation.[^s1][^s5] The developer documentation shortens it to **Revenue Management**.[^s3] Treat all of these names, plus the "revenue lifecycle management" label used in URLs and guide names, as one node. The suite is aimed at subscription, usage-based and multiproduct businesses that need renewals, amendments, proration, bundling and large quotes handled in one model.[^s1]

## How it works: the component map

Trailhead groups the suite into five areas.[^s2]

- **Product catalog and pricing.** *Product Catalog Management* is the central product model and the single source of product data. *Salesforce Pricing* applies prices, discounts and taxes consistently to quotes, orders and sales agreements. *Rate Management* prices consumption with tiers and volume, using rating procedures and a rating waterfall. *Product Configurator* guides reps through bundles, options and attributes for complex products.[^s2]
- **Transaction management.** Quote creation and order capture across channels, including a spreadsheet-style CPQ grid for large deals, and *Asset Lifecycle Management*, which tracks the install base through amendments, renewals and cancellations.[^s2]
- **Order-to-cash.** *Dynamic Revenue Orchestrator* splits each placed order into fulfillment tasks and routes them through automated and human steps.[^s2]
- **Contract lifecycle management.** *Salesforce Contracts* creates contracts from quotes and orders, supports external redlining and uses AI to extract clauses and entities.[^s2]
- **Billing.** Invoices are generated from billing schedules that orders trigger, with tax across legal entities, payment terms, credit memos and accounting periods.[^s2]

The intended flow is catalog, then pricing and promotions, then configurator templates, then quote, order, contract, fulfillment and invoice.[^s2] Because it exposes composable APIs, other clouds can reuse its product and pricing data.[^s1][^s2]

## Building the catalog and pricing

The **product catalog** is the container for every other object, so admins create it first. Then they define product attributes, product classifications (templates for product variations), categories, and products or bundles. Pricing and configurator rules come last.[^s5] Which products a user can see is decided separately by **qualification rules**. These rules combine decision tables, a qualification rule procedure and a context definition, and admins must pick the right context in Product Discovery settings.[^s5]

Pricing is procedural. A **pricing procedure** is an ordered chain of pricing elements, such as list price, volume discount, attribute discount, manual discount and aggregate price. Each element reads from a **context definition** and passes its result to the next. The shipped *SalesTransactionContext* links the calculation to quotes, orders and assets.[^s4] Elements read their data from **decision tables**, not straight from records. Admins set a default pricing procedure and price recipe in org settings, then run **Sync Pricing Data**. Until that sync runs, edits to pricing data do not take effect.[^s4] Procedures can be simulated, and the result is a price waterfall showing each step.[^s4]

## Developer surface

The developer guide lists business (Connect) APIs, built-in Apex classes, invocable actions (for example, creating orders from quotes), standard objects, Tooling API objects and Metadata API types for each feature area. It also names a `RevenueManagementSettings` metadata type.[^s3] Product Configurator rules are written in **Constraint Modeling Language (CML)**. The guide also points to the Business Rules Engine and Context Service as related platform services.[^s3] It lists availability in Lightning Experience for Enterprise, Unlimited and Developer Editions.[^s3]

## Limits and gotchas

- The product has been renamed, so expect Revenue Cloud, Revenue Management and Agentforce Revenue Management in different screens and docs.[^s1][^s3]
- Pricing changes need a **Sync Pricing Data** run before they take effect.[^s4]
- Visibility comes from qualification rules, which must be simulated and activated. Products don't control their own visibility.[^s5]
- Migrating from the managed-package **Salesforce CPQ** is a data transformation, not a mapping. CPQ objects, fields, price rules and scripts don't carry over directly. Salesforce gives a typical timeline of 3–6 months.[^s6]

## When to use it (and when not)

Use it for new quote-to-cash builds and for subscription, usage or complex-bundle selling where catalog, pricing, assets and billing should share one data model.[^s1][^s2] Salesforce CPQ is **end of sale, not end of life**. Existing customers can renew, add users and get support and critical fixes, but no new features. There is no forced migration, and Salesforce has not announced a retirement date.[^s6] Revenue Cloud Advanced, part of this suite, is the stated successor. Salesforce suggests assessing where CPQ limits you before setting a migration date.[^s6]

## Connections

Agentforce Revenue Management runs on `kt:salesforce-platform` and extends the deal work in `kt:sales-cloud` into quoting, ordering and billing.[^s2] It **replaces** `kt:salesforce-cpq` as the strategic quoting product.[^s6] It **has parts** `kt:salesforce-pricing`, `kt:product-configurator` and `kt:dynamic-revenue-orchestrator`.[^s2] Its setup ships as metadata types, which ties it to `kt:metadata-api`.[^s3] It **integrates with** `kt:agentforce`, which its new name reflects, and with Einstein analytics for revenue insights.[^s1][^s2] Practitioner skills are **covered by** `kt:revenue-management-consultant-certification`, the certification Trailhead's preparation trail targets.

## Sources

[^s1]: Trailhead, "Meet Revenue Lifecycle Management". https://trailhead.salesforce.com/content/learn/modules/revenue-lifecycle-management-foundations/meet-revenue-lifecycle-management (accessed 2026-11-03)
[^s2]: Trailhead, "Explore Revenue Lifecycle Management". https://trailhead.salesforce.com/content/learn/modules/revenue-lifecycle-management-foundations/explore-revenue-lifecycle-management (accessed 2026-11-03)
[^s3]: Salesforce, "Get Started with Revenue Management Developer Resources". https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/rlm_get_started.htm (accessed 2026-11-03)
[^s4]: Trailhead, "Configure Pricing for Products". https://trailhead.salesforce.com/content/learn/modules/revenue-cloud-design/configure-pricing-for-products (accessed 2026-11-03)
[^s5]: Trailhead, "Set Up Your Product Offerings". https://trailhead.salesforce.com/content/learn/modules/revenue-cloud-design/set-up-your-product-offerings (accessed 2026-11-03)
[^s6]: Salesforce, "Navigating the Future of Salesforce CPQ: Product End of Sale (Not End of Life)". https://www.salesforce.com/sales/cpq/end-of-life/ (accessed 2026-11-03)
