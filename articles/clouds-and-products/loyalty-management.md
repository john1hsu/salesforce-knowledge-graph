---
id: kt:loyalty-management
type: Product
title: Loyalty Management
aliases: [Salesforce Loyalty Management, Loyalty Management Cloud]
domain: clouds-and-products
summary: >-
  Salesforce product, now part of Marketing Cloud Next, for running B2C and B2B loyalty programs on the core
  platform: members earn and spend qualifying and non-qualifying currencies, move through tiers that carry
  benefits, and redeem vouchers, with activity recorded as transaction journals and processed by promotions.
release: "Winter '27"
status: current
broader: [kt:marketing-cloud-next]
related: [kt:data-cloud, kt:marketing-cloud-engagement, kt:experience-cloud, kt:crm-analytics]
relations:
  - {predicate: partOf, object: kt:marketing-cloud-next}
  - {predicate: dependsOn, object: kt:decision-tables}
  - {predicate: dependsOn, object: kt:data-processing-engine}
  - {predicate: configuredVia, object: kt:flow-builder}
  - {predicate: integratesWith, object: kt:data-cloud}
  - {predicate: integratesWith, object: kt:journey-builder}
sources:
  - id: s1
    title: "Get Started with Loyalty Management (Loyalty Management Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/loyalty-management-basics/get-started-loyalty-management
    type: official-learning
    accessed: 2026-11-16
  - id: s2
    title: "Set Up a Loyalty Program (Loyalty Management Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/loyalty-management-basics/set-up-loyalty-program
    type: official-learning
    accessed: 2026-11-16
  - id: s3
    title: "Explore Actions and Processes (Loyalty Management Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/loyalty-management-basics/explore-actions-processes
    type: official-learning
    accessed: 2026-11-16
  - id: s4
    title: "Loyalty Management Standard Objects"
    publisher: Salesforce Developers (Loyalty Management Developer Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.loyalty.meta/loyalty/loyalty_api_overview.htm
    type: official-docs
    accessed: 2026-11-16
  - id: s5
    title: "TransactionJournal"
    publisher: Salesforce Developers (Loyalty Management Developer Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.loyalty.meta/loyalty/sforce_api_objects_transactionjournal.htm
    type: official-docs
    accessed: 2026-11-16
  - id: s6
    title: "Loyalty Management Pricing"
    publisher: Salesforce
    url: https://www.salesforce.com/marketing/loyalty/pricing/
    type: official-docs
    accessed: 2026-11-16
created: 2026-11-16
---

# Loyalty Management

Loyalty Management is Salesforce's product for designing and running loyalty programs on the Salesforce Platform. Trailhead now places it inside Marketing Cloud Next and positions it for cross-industry programs in both B2C and B2B settings, with the aim of raising engagement and customer lifetime value through personalized rewards.[^s1] Because it runs on the core platform, loyalty data sits beside the Contacts, Accounts and orders that sales and service teams already use.[^s1][^s3]

## How it works

A program is built from a few connected building blocks, each a standard object linked to the `LoyaltyProgram` record.[^s4]

- **Currencies.** Non-qualifying currencies are points members redeem; qualifying currencies have no cash value and drive tier status.[^s2][^s4]
- **Tier groups and tiers.** A tier group sets the tier model, qualifying period and tier duration, and holds an ordered set of tiers.[^s2][^s4]
- **Benefits.** Perks are grouped by benefit type, ranked by priority, and assigned automatically when a member reaches a tier.[^s1][^s2]
- **Members.** Individual members link to a Contact; corporate members link to an Account. Members can pool non-qualifying points in groups.[^s3]
- **Partners.** An accrual partner lets members earn on its products, a redemption partner lets them spend there, or both.[^s3]
- **Vouchers and badges.** Vouchers give a discount or a free item and are issued from a `VoucherDefinition` template.[^s1][^s4]

Member activity is recorded as `TransactionJournal` records. Each journal has a journal type and subtype, a required activity date, a lookup to the member, and a restricted status picklist (Pending, Processed, Error, Cancelled). Point movements that result are written to `LoyaltyLedger`.[^s5][^s4] Accrual activities (a purchase, a review, an enrollment) credit points either in real time or in batches; redemptions are deducted in real time.[^s2]

Rules are configured in Promotion Setup, which credits and debits points, changes tiers and updates records. Trailhead lists Flows, Decision Tables, Batch Management and the Data Processing Engine as the other automation pieces behind a running program.[^s2][^s3]

## Limits and gotchas

- Point expiry is either **fixed** (each accrual expires after a set period) or **activity-based** (the whole balance expires after a period with no activity).[^s2]
- **Escrow** holds points for a set number of days to absorb returns; with escrow on, balances can't go negative, so it can't be combined with negative points.[^s2]
- A qualifying currency belongs to exactly one tier group, although a tier group can use several qualifying currencies.[^s2]
- The Experience Cloud Loyalty Member Portal template can be tied to only one loyalty program per site.[^s3]
- `TransactionJournal` is available from API version 51.0, accepts up to 50 custom fields, and indexes only a limited set of fields, so filter queries on member, program, activity date or external transaction number.[^s5]
- Editions cap volume. The pricing page lists Starter, Growth and Advanced at 1 million, 15 million and 50 million loyalty events a year, and only Advanced runs multiple programs.[^s6]

Users need the Loyalty Management permission set (or equivalent object permissions and sharing) to manage programs.[^s1]

## When to use it (and when not)

Choose Loyalty Management when points, tiers and partner earning must live next to CRM data and feed segmentation and journeys. Trailhead describes targeting promotions with Data 360 segments and delivering them through Journey Builder or Marketing Cloud Engagement.[^s1] A simple one-off reward, such as a discount code, may not justify the licence: edition prices on the official pricing page are quoted per org per month.[^s6]

## Connections

Loyalty Management is **part of** `kt:marketing-cloud-next`, its broader node.[^s1] It **integrates with** `kt:data-cloud` for segmentation and with `kt:journey-builder` for delivery, and relates to `kt:marketing-cloud-engagement`, which can send loyalty promotions.[^s1] It **depends on** `kt:decision-tables` and `kt:data-processing-engine`, and is **configured via** `kt:flow-builder` alongside Promotion Setup.[^s3] Its member portal is an `kt:experience-cloud` template.[^s3] Each edition includes CRM Analytics for Loyalty Management licences, which ties it to `kt:crm-analytics`.[^s6]

## Sources
[^s1]: Trailhead, "Get Started with Loyalty Management". https://trailhead.salesforce.com/content/learn/modules/loyalty-management-basics/get-started-loyalty-management (accessed 2026-11-16)
[^s2]: Trailhead, "Set Up a Loyalty Program". https://trailhead.salesforce.com/content/learn/modules/loyalty-management-basics/set-up-loyalty-program (accessed 2026-11-16)
[^s3]: Trailhead, "Explore Actions and Processes". https://trailhead.salesforce.com/content/learn/modules/loyalty-management-basics/explore-actions-processes (accessed 2026-11-16)
[^s4]: Salesforce Developers, "Loyalty Management Standard Objects". https://developer.salesforce.com/docs/atlas.en-us.loyalty.meta/loyalty/loyalty_api_overview.htm (accessed 2026-11-16)
[^s5]: Salesforce Developers, "TransactionJournal". https://developer.salesforce.com/docs/atlas.en-us.loyalty.meta/loyalty/sforce_api_objects_transactionjournal.htm (accessed 2026-11-16)
[^s6]: Salesforce, "Loyalty Management Pricing". https://www.salesforce.com/marketing/loyalty/pricing/ (accessed 2026-11-16)
