---
id: kt:salesforce-pricing
type: Feature
title: Salesforce Pricing
aliases: [Revenue Cloud pricing engine, pricing procedures, Agentforce Revenue Management pricing]
domain: clouds-and-products
summary: >-
  The pricing engine of Agentforce Revenue Management that calculates line-item prices by running ordered pricing
  procedures of pricing elements over a context definition, with price adjustment methods, decision-table lookups
  and a price waterfall that explains each step.
release: "Winter '27"
status: current
broader: [kt:revenue-cloud]
related: [kt:product-configurator, kt:sales-cloud]
relations:
  - {predicate: dependsOn, object: kt:price-books}
  - {predicate: dependsOn, object: kt:decision-tables}
  - {predicate: dependsOn, object: kt:context-service}
  - {predicate: queriedWith, object: kt:connect-api}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: contrastsWith, object: kt:salesforce-cpq}
sources:
  - id: s1
    title: "Salesforce Pricing (Revenue Management Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/pricing_overview.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s2
    title: "Salesforce Pricing Business APIs (Revenue Management Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/pricing_business_apis.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s3
    title: "Create a Pricing Procedure with the List Price Element (Price Management with Agentforce Revenue Management)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/price-management-with-revenue-cloud/create-a-pricing-procedure-with-the-list-price-element
    type: official-learning
    accessed: 2026-11-09
  - id: s4
    title: "Configure Contract-Based Pricing (Advanced Price Management with Agentforce Revenue Management)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/advanced-price-management-with-revenue-cloud/configure-contract-based-pricing
    type: official-learning
    accessed: 2026-11-09
created: 2026-11-09
---

# Salesforce Pricing

Salesforce Pricing is the price-calculation feature inside Agentforce Revenue Management (formerly Revenue Cloud). Admins use it to define **price adjustment methods**, which decide the discounts applied to products and services, and **pricing procedures**, which make the calculation visible step by step.[^s1] It runs in Lightning Experience in Enterprise, Unlimited and Developer Editions of Revenue Management where the feature is enabled. Pricing-specific fields on standard objects only appear once it is turned on.[^s1]

## How it works

A **pricing procedure** is an ordered, editable chain of **pricing elements**. Each element is one step, and its rank sets when it runs. A procedure has a usage type (Pricing) and points at a **context definition**, the data shape the calculation reads from and writes back to. Trailhead's examples use *RevSalesTransactionContext*, an extension of the shipped *SalesTransactionContext*, which ties the calculation to quotes, orders and assets.[^s3] Elements do not read records directly. Their input and output variables map to **context tags**, which carry values between steps and back to the transaction a rep sees.[^s3]

The building blocks a practitioner meets first:

- **Pricing Setting** maps shared inputs such as the line item, and outputs such as net unit price, subtotal and the price waterfall.[^s3]
- **List Price** looks up the price book entry using product, price book and product selling model, then returns list price and subtotal.[^s3]
- **Volume Discount** applies tiered discounts by quantity.[^s4]
- **List Group** wraps elements that should run only when a condition holds.[^s4]
- **Stop Pricing** ends processing early.[^s4]

Each element has an *Include in Output* flag that controls whether its result reaches the final output.[^s3] The **price waterfall** records every adjustment that produced the final price. In the Pricing Procedure Builder, *Simulate* shows the waterfall for test inputs, entered either as fields or as JSON.[^s3] On a quote, hovering over Net Unit Price shows the same waterfall.[^s4]

Pricing data is served from lookup tables, so record changes are not live straight away. In the contract-pricing exercise, admins refresh the *Contract Pricing Entries* and *Contract Pricing Volume Tiers* decision tables after editing contract prices. Otherwise the latest data is not used.[^s4] The active procedure is chosen in **Revenue Settings** under *Set Up Salesforce Pricing*. A new procedure has no effect until it is activated and selected there.[^s4]

## Contract-based pricing as an example

Negotiated terms live on an activated contract. They are stored as a Contract Item Price, with a selling model, a date range and an adjustment method, plus optional Contract Item Price Adjustment Tiers for volume discounts.[^s4] The procedure then runs two branches. Standard List Price and Volume Discount elements handle uncontracted lines. Copies with *Use contract-based pricing* checked handle contracted lines and output an `IsContracted` flag. That flag gates a List Group ending in Stop Pricing, so a contracted line skips the standard discounts.[^s4] Common gotchas are leaving that checkbox unchecked, using an inactive contract, out-of-range dates, and tier boundaries: a lower bound of 101 means exactly 100 units get no discount.[^s4]

## APIs and automation

The engine is exposed through Connect REST business APIs under `/connect/core-pricing/`. They let you price a context instance by ID, or create and price a context in one call that returns per-line prices and errors. They can also sync pricing data into lookup tables, list, clone and map pricing recipes to decision tables, and read or create waterfall logs and execution details.[^s2] A second resource family manages procedure plan definitions and their versions.[^s2] The feature also ships standard invocable actions for Flow, Apex classes, and Metadata API and Tooling API types for its configuration.[^s1]

## When to use it (and when not)

Use Salesforce Pricing for new quote-to-cash builds on Agentforce Revenue Management. Use it especially where pricing has to stay explainable and reusable across quotes, orders and contracts, because the waterfall and execution logs show why a price came out as it did.[^s2][^s3] It only exists in Revenue Management editions where Salesforce Pricing is enabled, so an org on another quoting tool does not get it automatically.[^s1] It also adds operational steps that simple price-book pricing lacks: you build procedures, activate one in Revenue Settings, and keep the lookup tables refreshed. For a catalog that needs only list prices from price books, that overhead may not pay off.[^s3][^s4]

## Connections

Salesforce Pricing is a part of `kt:revenue-cloud` (its **broader** node) and sits beside `kt:product-configurator` in the quote flow that extends `kt:sales-cloud`.[^s1][^s3] It **depends on** `kt:price-books`, because the List Price element reads price book entries. It also depends on `kt:decision-tables`, the lookup tables that pricing data syncs into, and on `kt:context-service`, whose context definitions and tags carry data between elements.[^s3][^s4][^s2] It is **queried with** `kt:connect-api` business resources and **configured via** `kt:metadata-api` types.[^s2][^s1] It **contrasts with** `kt:salesforce-cpq`, whose price rules solve the same problem in a different, managed-package model.[^s1]

## Sources
[^s1]: Salesforce, "Salesforce Pricing (Revenue Management Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/pricing_overview.htm (accessed 2026-11-09)
[^s2]: Salesforce, "Salesforce Pricing Business APIs". https://developer.salesforce.com/docs/atlas.en-us.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/pricing_business_apis.htm (accessed 2026-11-09)
[^s3]: Trailhead, "Create a Pricing Procedure with the List Price Element". https://trailhead.salesforce.com/content/learn/modules/price-management-with-revenue-cloud/create-a-pricing-procedure-with-the-list-price-element (accessed 2026-11-09)
[^s4]: Trailhead, "Configure Contract-Based Pricing". https://trailhead.salesforce.com/content/learn/modules/advanced-price-management-with-revenue-cloud/configure-contract-based-pricing (accessed 2026-11-09)
