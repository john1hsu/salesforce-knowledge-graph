---
id: kt:digital-wallet
type: Tool
title: Digital Wallet
aliases: [Salesforce Digital Wallet, Data Cloud credits and consumption, Data 360 credits and consumption, consumption cards, Data 360 credit consumption]
domain: data-cloud-and-ai
summary: >-
  Salesforce's free account-management tool for consumption-based products such as Data 360 and Agentforce,
  showing near real-time credit and capacity usage per consumption card, with alerts, tags and forecasting.
release: "Winter '27"
status: current
broader: [kt:salesforce-pricing, kt:data-cloud]
related: [kt:agentforce, kt:data-cloud-limits, kt:zero-copy-data-federation]
relations:
  - {predicate: configuredVia, object: kt:flow-builder}
  - {predicate: integratesWith, object: kt:tableau-next}
sources:
  - id: s1
    title: "Get to Know Salesforce Digital Wallet"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-digital-wallet-quick-look/get-to-know-salesforce-digital-wallet
    type: official-learning
    accessed: 2026-11-13
  - id: s2
    title: "Get Started with Data Cloud Credit Consumption"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/es/content/learn/modules/data-cloud-credit-consumption-quick-look/get-started-with-data-cloud-credit-consumption
    type: official-learning
    accessed: 2026-11-13
  - id: s3
    title: "Manage Costs and Optimize Consumption"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agentforce-model-switching-and-monetization/manage-costs-and-optimize-consumption
    type: official-learning
    accessed: 2026-11-13
  - id: s4
    title: "Flex Credits Rate Card (updated November 3, 2026)"
    publisher: Salesforce
    url: https://www.salesforce.com/en-us/wp-content/uploads/sites/4/assets/pdf/agentforce/Flex-Credits-Rate-Card-11.3.2026.pdf
    type: official-docs
    accessed: 2026-11-13
  - id: s5
    title: "Optimize Your Consumption with Digital Wallet"
    publisher: Salesforce
    url: https://www.salesforce.com/agentforce/digital-wallet/
    type: official-docs
    accessed: 2026-11-13
  - id: s6
    title: "TenantConsumptionAlert | Object Reference for the Salesforce Platform"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_tenantconsumptionalert.htm
    type: official-docs
    accessed: 2026-11-13
created: 2026-11-13
---

# Digital Wallet

**Digital Wallet** is Salesforce's account-management tool for consumption-based products: products billed by what an org uses rather than per user. The org buys either a pool of credits to spend over a contract period or a fixed capacity for stored data, and Digital Wallet shows near real-time usage against that entitlement.[^s1] It is free to use once an org has bought a Digital Wallet-enabled product.[^s5] It is the place where Data 360 credit consumption, Agentforce Flex Credit spend and similar meters become visible to admins and budget owners.

## How it works

The homepage is a set of **consumption cards**. A card groups related usage types with their **entitlement** (the credits, capacity or other currency purchased). Credits are deducted as metered features run; capacity applies to products that store data or files.[^s1] When the same SKU appears on several contracts, its entitlements are pooled onto one card, and usage draws first from the contract that expires soonest.[^s1] Opening a card leads to Consumption Insights, which charts usage by day or period and breaks it down into usage types, subtypes, multipliers and units consumed.[^s1]

For Agentforce, the Flex Credits card has a Consumption Overview tab (drivers and forecasting) and a Consumption Explorer tab (agents, actions and Data 360 sources). Users can filter by period, environment and usage type, and add custom tags to attribute spend to teams or individuals.[^s3] Salesforce markets tags for grouping consumption by environment, agent, feature or region, which supports internal chargeback, and says forecasting is powered by Tableau Next.[^s5]

Users reach the tool by searching "Digital Wallet" or "Consumption Cards" in the App Launcher, or through the Your Account app. They need the View Consumption Cards permission and an active contract for an enabled product.[^s1] The primary billing contact also gets a monthly account summary email on the 10th, one per contract; if it disagrees with an invoice, the invoice wins.[^s1]

## How credits are calculated

Data 360 is priced by consumption. Orgs hold either **Data Services credits**, which only Data 360 can spend across 21 usage types, or **Flex Credits**, which are interchangeable across Data 360, Agentforce and other features.[^s2] The basic formula is credits = (data processed ÷ unit) × multiplier, where the unit is 1 million rows for these usage types. Trailhead's example: a batch calculated insight over 20 million rows at a multiplier of 15 costs 300 credits.[^s2]

The Flex Credits rate card updated on November 3, 2026 lists volume tiers per usage type, reset on the first day of each calendar month.[^s4] For example, Data 360 Prep costs 40 credits per million rows at the base tier (up to 300k credits), falling to 32, 16 and 8 at higher tiers; sandboxes use a flat sandbox multiplier.[^s4] When a run crosses a tier boundary, the lower multiplier applies to the whole event.[^s2] On the Agentforce side, a standard or custom action costs 20 credits in production and 16 in a sandbox.[^s4] Flex Credits expire at the order end date and do not roll over.[^s4]

## Limits and gotchas

- **Near real-time is not billing.** Card data refreshes several times a day but can lag; the monthly statement is authoritative.[^s1]
- **One feature, several meters.** Previewing a data transform consumes Data Queries credits on top of transform credits, so check each feature's billing notes.[^s2]
- **Sandboxes still cost.** Sandbox and scratch-org usage consumes credits at sandbox multipliers.[^s4]
- **CRM ingestion is free.** Ingesting from Salesforce CRM and certain Agentforce connectors consumes no Data 360 credits.[^s2]
- **Switching credit types needs a contract.** An org with Data Services credits must re-contract to move to Flex Credits.[^s2]
- **Rates change.** Salesforce notes that multipliers and tiers may change over time, so recheck the current rate card.[^s4]

## Monitoring and optimization

Admins can set percentage thresholds, org-wide or per card, that notify by email, system notification or Slack; setup starts from the Consumption Threshold Alerts flow template in Flow Builder.[^s3] Since API version 67.0 (Summer '26), the `TenantConsumptionAlert` object logs each time a consumption signal is reached, with its type, resource and condition.[^s6] To reduce spend, Trailhead suggests batch instead of streaming where latency allows, deactivating stale segments, ingesting only relevant data and refreshing less often.[^s2]

## Connections

Digital Wallet is the operational face of `kt:salesforce-pricing` for metered products, and most of its meters come from `kt:data-cloud`.[^s1][^s2] It complements `kt:data-cloud-limits`: limits cap what an org may do, while credits price what it does.[^s2] `kt:agentforce` actions and prompts draw on the same Flex Credits pool.[^s4] `kt:zero-copy-data-federation` sharing-out is metered too.[^s4] Alerts are built in `kt:flow-builder`, and forecasting comes from `kt:tableau-next`.[^s3][^s5]

## Sources

[^s1]: Trailhead, "Get to Know Salesforce Digital Wallet". https://trailhead.salesforce.com/content/learn/modules/salesforce-digital-wallet-quick-look/get-to-know-salesforce-digital-wallet (accessed 2026-11-13)
[^s2]: Trailhead, "Get Started with Data Cloud Credit Consumption". https://trailhead.salesforce.com/es/content/learn/modules/data-cloud-credit-consumption-quick-look/get-started-with-data-cloud-credit-consumption (accessed 2026-11-13)
[^s3]: Trailhead, "Manage Costs and Optimize Consumption". https://trailhead.salesforce.com/content/learn/modules/agentforce-model-switching-and-monetization/manage-costs-and-optimize-consumption (accessed 2026-11-13)
[^s4]: Salesforce, "Flex Credits Rate Card (updated November 3, 2026)". https://www.salesforce.com/en-us/wp-content/uploads/sites/4/assets/pdf/agentforce/Flex-Credits-Rate-Card-11.3.2026.pdf (accessed 2026-11-13)
[^s5]: Salesforce, "Optimize Your Consumption with Digital Wallet". https://www.salesforce.com/agentforce/digital-wallet/ (accessed 2026-11-13)
[^s6]: Salesforce Developers, "TenantConsumptionAlert | Object Reference for the Salesforce Platform". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_tenantconsumptionalert.htm (accessed 2026-11-13)
