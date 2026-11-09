---
id: kt:product-configurator
type: Feature
title: Product Configurator
aliases: [Revenue Cloud Product Configurator, Agentforce Revenue Management configurator, configurator flows]
domain: clouds-and-products
summary: >-
  The configuration feature of Agentforce Revenue Management that lets reps and buyers customize a product's or
  bundle's attributes and components at runtime, enforcing compatibility through configuration rules (Business
  Rules Engine) or constraint models (Constraint Rules Engine) and handing the result to pricing and the quote or order.
release: "Winter '27"
status: current
broader: [kt:revenue-cloud]
related: [kt:salesforce-pricing, kt:constraint-modeling-language, kt:business-rules-engine]
relations:
  - {predicate: dependsOn, object: kt:product-catalog-management}
  - {predicate: configuredVia, object: kt:flow-builder}
  - {predicate: queriedWith, object: kt:connect-api}
  - {predicate: contrastsWith, object: kt:salesforce-cpq}
sources:
  - id: s1
    title: "Product Configurator (Revenue Management Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.258.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/prod_config_overview.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s2
    title: "Get Started with Product Configurator (Product Configuration with Agentforce Revenue Management)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/product-configuration-with-revenue-cloud/get-started-with-product-configurator
    type: official-learning
    accessed: 2026-11-09
  - id: s3
    title: "Use Product Configurator with Business Rules Engine"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/product-configuration-with-revenue-cloud/use-product-configurator-with-business-rules-engine
    type: official-learning
    accessed: 2026-11-09
  - id: s4
    title: "Explore Product Configurator with Constraint Rules Engine"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/product-configuration-with-revenue-cloud/explore-product-configurator-with-constraint-rules-engine
    type: official-learning
    accessed: 2026-11-09
  - id: s5
    title: "Define Your Product Configuration Experience (Agentforce Revenue Management Design)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/revenue-cloud-design/define-your-product-configuration-experience
    type: official-learning
    accessed: 2026-11-09
created: 2026-11-09
---

# Product Configurator

Product Configurator is the "configure" step of the configure-price-quote pillar in Agentforce Revenue Management (formerly Revenue Cloud). It lets sales reps tailor complex products, bundles and assets for quotes and orders.[^s2] Salesforce's developer guide describes it as customizing a product's components and attributes to fit specific business requirements. It runs in Lightning Experience in Enterprise, Unlimited and Developer Editions of Revenue Management where the feature is enabled.[^s1]

## How it works

The base product data (products, bundles, attributes, classifications) lives in Product Catalog Management. Configuration layers runtime choices on top, such as adding accessories or warranties, or picking a hardware option like the number of USB ports.[^s5] A rep can open the configurator during product discovery, or from the action menu on a quote or order line item. For a bundle, each component has its own Configure button. A summary panel shows the bundle's specifications and price, and *Save & Exit* writes the configured product back to the quote or order.[^s2] Toggles for **Product Validation** and **Instant Pricing** control whether each selection is checked and priced as it is made. Reps can also save a configuration and reuse it later.[^s2]

**Configurator flows** control presentation. Salesforce ships default flow templates for each aspect of configuration, for example a product attribute template where you set the column count and display style. Admins assign a flow to a product, or to a product classification so many products share it.[^s5] The interfaces are built from composable templates using tools such as Flow Builder.[^s2] For fully custom front ends or digital commerce, headless configurator APIs and third-party configurator integration are supported.[^s2][^s5] The developer guide lists Product Configurator Business APIs, standard invocable actions, a dedicated data model, and Metadata API types for the feature's settings.[^s1]

## Two rule engines

Every catalog product is purchasable by default, so compatibility has to be enforced by rules.[^s5] Product Configurator supports two engines.[^s3]

- **Business Rules Engine.** Point-and-click **Product Configuration Rules**, each with a scope, a condition and an action. The scope is a single product's attributes, a bundle's children, or the whole transaction (every line on the quote or order).[^s3][^s5] Rule types are validation, exclusion and requirement. Actions include setting attribute values or quantities and hiding attributes or values.[^s3][^s5] Messages are Information, Warning or Error, and only an Error blocks submission.[^s5] Before rules run, you activate the shipped *Configuration Rules* rule library version and enable configuration rules in **Revenue Settings**. Each rule also needs an Active status and a valid start date.[^s3]
- **Constraint Rules Engine.** This is the newer option. It evaluates the possible combinations of selections and allows only valid ones. Logic is written in **Constraint Modeling Language (CML)**, either directly in the CML Editor or through the no-code Visual Builder, which generates CML.[^s4][^s1] A **constraint model** groups the products, attributes and constraint rules. You create it in the Constraint Models app, enable the constraints-engine setting in Revenue Settings, and activate the model before the configurator uses it.[^s4] Trailhead says this engine includes all the Business Rules Engine rule types and adds more powerful ones.[^s4]

## Limits and gotchas

- Neither engine does anything until its Revenue Settings option is turned on and the rule library or constraint model is activated.[^s3][^s4]
- Explicit if-then rules need manual upkeep with every product change and get hard to scale when they overlap. Trailhead positions constraint-based modeling for interdependent attributes and large option sets.[^s4]
- Visual Builder suits simple logic, and complex logic needs the CML Editor.[^s4]
- Configuration errors flow downstream as order fallout. Configured data feeds order management, billing, contracts and revenue recognition.[^s5][^s2]

## When to use it (and when not)

Use Product Configurator for new quote-to-cash builds on Agentforce Revenue Management where products have attributes, nested bundles or regional compatibility rules. Pick the Business Rules Engine for simple-to-moderate products with fixed logic, and the Constraint Rules Engine for large or highly interdependent catalogs.[^s4][^s3] Use a third-party configurator when you need a custom UI, unusual workflow or external integration. Salesforce still handles pricing, product data and quoting in that case.[^s4]

## Connections

Product Configurator is part of `kt:revenue-cloud` (its **broader** node). It **depends on** `kt:product-catalog-management` for products, bundles and classifications.[^s5] It is **configured via** `kt:flow-builder` configurator flows and can be **queried with** its headless business APIs on `kt:connect-api`.[^s2][^s1] Its rules run on `kt:business-rules-engine` or are written in `kt:constraint-modeling-language`.[^s3][^s4] Selections pass to `kt:salesforce-pricing` for real-time prices.[^s2] It **contrasts with** `kt:salesforce-cpq`, a separate quoting product with its own configuration model. The two are easy to confuse because Product Configurator also sits in a configure-price-quote pillar.[^s2]

## Sources
[^s1]: Salesforce, "Product Configurator (Revenue Management Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.258.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/prod_config_overview.htm (accessed 2026-11-09)
[^s2]: Trailhead, "Get Started with Product Configurator". https://trailhead.salesforce.com/content/learn/modules/product-configuration-with-revenue-cloud/get-started-with-product-configurator (accessed 2026-11-09)
[^s3]: Trailhead, "Use Product Configurator with Business Rules Engine". https://trailhead.salesforce.com/content/learn/modules/product-configuration-with-revenue-cloud/use-product-configurator-with-business-rules-engine (accessed 2026-11-09)
[^s4]: Trailhead, "Explore Product Configurator with Constraint Rules Engine". https://trailhead.salesforce.com/content/learn/modules/product-configuration-with-revenue-cloud/explore-product-configurator-with-constraint-rules-engine (accessed 2026-11-09)
[^s5]: Trailhead, "Define Your Product Configuration Experience". https://trailhead.salesforce.com/content/learn/modules/revenue-cloud-design/define-your-product-configuration-experience (accessed 2026-11-09)
