---
id: kt:salesforce-cpq
type: Product
title: Salesforce CPQ
aliases: [CPQ, Salesforce Configure Price Quote, SBQQ]
domain: clouds-and-products
summary: >-
  Salesforce's original configure-price-quote product, which adds product rules, price rules, a layered price
  waterfall and quote documents to opportunities; it is end of sale (not end of life) and its strategic successor is
  Revenue Cloud Advanced in Agentforce Revenue Management.
release: "Winter '27"
status: deprecated
broader: [kt:sales-cloud]
related: [kt:product-configurator, kt:salesforce-pricing]
relations:
  - {predicate: replacedBy, object: kt:revenue-cloud}
  - {predicate: dependsOn, object: kt:price-books}
  - {predicate: integratesWith, object: kt:heroku}
  - {predicate: contrastsWith, object: kt:salesforce-pricing}
sources:
  - id: s1
    title: "Product and Price Rules (Salesforce CPQ Features)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-cpq-features/product-and-price-rules
    type: official-learning
    accessed: 2026-11-09
  - id: s2
    title: "Identify Exceptions to Standard Pricing (Pricing Methods for Salesforce CPQ)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/pricing-methods-for-salesforce-cpq/identify-exceptions-to-standard-pricing
    type: official-learning
    accessed: 2026-11-09
  - id: s3
    title: "Use Salesforce CPQ for Discounting (Discounting Tools in Salesforce CPQ)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/discounting-tools-in-salesforce-cpq/use-salesforce-cpq-for-discounting
    type: official-learning
    accessed: 2026-11-09
  - id: s4
    title: "Javascript Quote Calculator Plugin (CPQ Plugins Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/revenue/cpq-plugins/guide/cpq-dev-jsqcp-parent.html
    type: official-docs
    accessed: 2026-11-09
  - id: s5
    title: "Quote Calculator Plugin Guidelines (CPQ Plugins Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/revenue/cpq-plugins/guide/cpq-dev-jsqcp-guidelines.html
    type: official-docs
    accessed: 2026-11-09
  - id: s6
    title: "Navigating the Future of Salesforce CPQ: Product End of Sale (Not End of Life)"
    publisher: Salesforce
    url: https://www.salesforce.com/sales/cpq/end-of-life/
    type: official-blog
    accessed: 2026-11-09
created: 2026-11-09
---

# Salesforce CPQ

Salesforce CPQ (configure, price, quote) is the quoting product that many Salesforce orgs still run on top of their opportunities. Reps pick products from guided bundles, a rules engine works out the price, and the result goes onto a quote with lines that roll up to the opportunity.[^s1][^s2] Salesforce now calls it **end of sale, not end of life**. New customers can't buy it, but existing customers keep using it. It sits in a maintenance phase with support and critical fixes and no new features.[^s6] So architects meet it mostly in existing orgs and in migration planning, not in greenfield designs.

## How it works

**Configure.** CPQ has four kinds of **product rules**. *Validation* rules check that product combinations or quote line values meet conditions. *Selection* rules add, remove, hide, enable or disable bundle options. *Filter* rules narrow which products can go into a bundle. *Alert* rules show guidance messages during configuration or pricing.[^s1] Bundles use these rules to keep incompatible products apart and to add required companions automatically.[^s1]

**Price.** A **price rule** writes a static value, another field's value or a summary variable into a quote or quote line field. It can target either the configurator or the calculator in the quote line editor, and it runs when the rep clicks Save or Calculate.[^s1] Pricing builds on standard price books. A product can be quoted only when the quote's price book has an entry for it, and a $0 entry is a common placeholder for a price CPQ will replace.[^s2] Pricing methods change the starting price before any discounts apply. They include block pricing (a flat price for a quantity range), percent of total, option price overrides inside bundles, cost-plus markup and account-specific contracted pricing.[^s2]

**The price waterfall.** Every quote line carries a chain of price fields, and each one feeds the next:[^s2][^s3]

- **Original Price**: the price book price.[^s2]
- **List Price**: after block, percent-of-total or option overrides.
- **Special Price**: after cost-plus, contracted or option discounts.
- **Regular Price**: after automatic volume discounts.
- **Customer Price**: after the rep's manual discounts.
- **Partner Price**: after the partner discount.
- **Net Price**: after the distributor discount.[^s3]

Net Price is what the customer pays, and it syncs to the opportunity product.[^s2][^s3] Because each discount type lands in its own field, partner and distributor margins stay visible instead of disappearing into one number.[^s3]

**Subscriptions.** Multi-dimensional quoting (MDQ) splits a subscription into time segments such as years or months. Each segment gets its own quantity and discount, without adding separate products.[^s1]

## Extending it with code

The **JavaScript Quote Calculator Plugin (QCP)** puts custom JavaScript into the quote line editor's calculation. The code is stored in CPQ as custom scripts, and it can change line calculations or control field visibility.[^s4] The plugin is an ES6 module that must run in both the browser and Node, so browser globals such as `window` may not exist. Asynchronous work has to return Promises so the calculation steps stay in order.[^s5] Quote calculations call Heroku to run asynchronously.[^s4]

## Limits and gotchas

- QCP can't call non-Salesforce endpoints during asynchronous calculation, and the character limit for a custom script can't be raised.[^s5]
- Fields from related records, such as the account or opportunity, aren't loaded into the calculator by default. Pull them in with quote formula fields or reference them in price actions.[^s5]
- Dates arrive in the plugin as `YYYY-MM-DD` strings and must be written back in that format.[^s5]
- CPQ objects, custom fields, price rules and scripts don't map one-to-one to Revenue Cloud Advanced. Migrating is a data transformation that Salesforce says typically takes 3–6 months.[^s6]

## When to use it (and when not)

Existing CPQ customers can stay. They can renew, add users and receive support, and Salesforce has announced no retirement date and no forced migration.[^s6] New quote-to-cash projects, and orgs that need capabilities CPQ will no longer get, should look at **Revenue Cloud Advanced**, which Salesforce names as the successor.[^s6] Plan a move like a reimplementation. Inventory price rules, product rules and QCP logic first, because none of it carries over automatically.[^s5][^s6]

## Connections

CPQ extends `kt:sales-cloud` opportunities with quotes and quote lines and depends on standard `kt:price-books`.[^s2] It is **replaced by** `kt:revenue-cloud` (Agentforce Revenue Management), whose Revenue Cloud Advanced is the stated successor.[^s6] The two products cover the same ground differently, so its rules engine and waterfall **contrast with** `kt:salesforce-pricing` procedures, and its bundle rules relate to `kt:product-configurator`. Neither maps directly, which is why migration is a transformation.[^s6] Its calculator **integrates with** `kt:heroku` for asynchronous calculation, and its partner and distributor discounts keep channel margins visible on each line.[^s4][^s3]

## Sources

[^s1]: Trailhead, "Product and Price Rules". https://trailhead.salesforce.com/content/learn/modules/salesforce-cpq-features/product-and-price-rules (accessed 2026-11-09)
[^s2]: Trailhead, "Identify Exceptions to Standard Pricing". https://trailhead.salesforce.com/content/learn/modules/pricing-methods-for-salesforce-cpq/identify-exceptions-to-standard-pricing (accessed 2026-11-09)
[^s3]: Trailhead, "Use Salesforce CPQ for Discounting". https://trailhead.salesforce.com/content/learn/modules/discounting-tools-in-salesforce-cpq/use-salesforce-cpq-for-discounting (accessed 2026-11-09)
[^s4]: Salesforce, "Javascript Quote Calculator Plugin". https://developer.salesforce.com/docs/revenue/cpq-plugins/guide/cpq-dev-jsqcp-parent.html (accessed 2026-11-09)
[^s5]: Salesforce, "Quote Calculator Plugin Guidelines". https://developer.salesforce.com/docs/revenue/cpq-plugins/guide/cpq-dev-jsqcp-guidelines.html (accessed 2026-11-09)
[^s6]: Salesforce, "Navigating the Future of Salesforce CPQ: Product End of Sale (Not End of Life)". https://www.salesforce.com/sales/cpq/end-of-life/ (accessed 2026-11-09)
