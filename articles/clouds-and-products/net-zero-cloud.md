---
id: kt:net-zero-cloud
type: Product
title: Agentforce Net Zero
aliases: [Net Zero Cloud, Salesforce Net Zero Cloud, Agentforce for Net Zero Cloud]
domain: clouds-and-products
summary: >-
  Salesforce's sustainability management product, formerly Net Zero Cloud, which records energy and activity data,
  calculates scope 1, 2 and 3 greenhouse-gas emissions with emissions factors, and supports targets, forecasting and
  ESG disclosure reporting on the Salesforce Platform.
release: "Winter '27"
status: current
broader: [kt:salesforce-industries]
related: [kt:agentforce, kt:salesforce-platform]
relations:
  - {predicate: implements, object: kt:greenhouse-gas-protocol}
  - {predicate: integratesWith, object: kt:data-cloud}
  - {predicate: integratesWith, object: kt:crm-analytics}
  - {predicate: dependsOn, object: kt:einstein-trust-layer}
sources:
  - id: s1
    title: "Introduction to Net Zero Cloud (Net Zero Cloud Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/industries/netzero-cloud-dev-guide/guide/netzero-cloud-std-objects-intro.html
    type: official-docs
    accessed: 2026-11-15
  - id: s2
    title: "Net Zero Cloud Calculations (Net Zero Cloud Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/industries/netzero-cloud-dev-guide/guide/netzero-cloud-calculations.html
    type: official-docs
    accessed: 2026-11-15
  - id: s3
    title: "Track Emissions with Net Zero Cloud (Net Zero Cloud Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/net-zero-cloud-basics/track-emissions-with-net-zero-cloud
    type: official-learning
    accessed: 2026-11-15
  - id: s4
    title: "Learn the Foundations of Carbon Accounting (Carbon Accounting for Assets with Net Zero Cloud)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/carbon-accounting-for-assets-with-net-zero-cloud/learn-the-foundations-carbon-accounting
    type: official-learning
    accessed: 2026-11-15
  - id: s5
    title: "Net Zero Cloud Guide"
    publisher: Salesforce
    url: https://www.salesforce.com/net-zero/cloud/guide/
    type: news
    accessed: 2026-11-15
  - id: s6
    title: "Agentforce for Net Zero Cloud announcement"
    publisher: Salesforce
    url: https://www.salesforce.com/news/stories/agentforce-for-net-zero-cloud-announcement/
    type: news
    accessed: 2026-11-15
created: 2026-11-15
---

# Agentforce Net Zero

Agentforce Net Zero is Salesforce's sustainability management product. It was sold as **Net Zero Cloud**, and Salesforce's own product guide and Trailhead now describe Net Zero Cloud as renamed to Agentforce Net Zero.[^s5][^s4] The developer documentation still uses the Net Zero Cloud name. It describes the product as a way to collect, analyze and report environmental, social and governance (ESG) data on the Salesforce Platform. It is available in Enterprise, Performance, Unlimited and Developer editions, in Lightning Experience only.[^s1]

## What it does

The core of the product is carbon accounting. Teams load energy-use and activity data from business operations and the product turns it into emissions using preloaded emissions factors. It then builds scope 1, 2 and 3 footprints and consolidates them across subsidiaries and partners, including apportionment for partial ownership.[^s1] Around that core it adds waste and water footprints, carbon-credit allocation, science-based target setting, emissions forecasting and what-if analysis, and supplier scorecards. It also offers quantitative social and governance disclosures and a Disclosure and Compliance Hub for frameworks such as CDP, GRI, SASB and ESRS.[^s1] Bulk data can be loaded through CSV templates into Received Documents.[^s1]

Trailhead frames the work as a yearly carbon-accounting cycle. Identify emissions sources, record activity data, load emissions factor datasets and review the calculated emissions. Then create carbon footprints, build the annual inventory and audit the result.[^s3] Inputs include utility bills, fuel receipts, travel records and supplier data. Procurement spend feeds scope 3, and auditors can review the data in the same system.[^s3]

## How the calculations work

The data model separates sources, activity and results:

- **Emissions sources**: Stationary Asset Environmental Source (buildings), Vehicle Asset Emissions Source and Scope 3 Emissions Source.[^s4]
- **Activity data**: Stationary Asset Energy Use and Vehicle Asset Energy Use records, one per period or event, such as a month of building consumption or one flight.[^s4][^s2]
- **Emissions factors**: Electricity, Refrigerant and Other Emissions Factor records, which can draw on reference datasets such as eGRID and EEIO.[^s4]
- **Carbon footprints**: per-asset footprints with line items per fuel type, plus Scope 3 Carbon Footprint records.[^s4]

A carbon footprint aggregates energy use records for an asset or activity, usually for a calendar or fiscal year. The Annual Emissions Inventory then totals scope 1, 2 and 3 in metric tonnes of CO2e.[^s2] Missing periods can be filled manually or with app-provided estimates through data gap filling. Building Energy Intensity records hold average intensity by fuel type, and Building Size Category records filter them by floor-area range.[^s2] Scope 2 can be reduced by allocating Energy Attribute Certificates, each representing 1 MWh of renewable electricity. Scope 3 also covers waste, both from operations and from end-of-life treatment of sold products.[^s2]

## Limits and gotchas

- **Calculation accuracy**: calculations target 99.99% accuracy, and deviations above 0.01% should go to Salesforce Support.[^s2]
- **Default factors are averages**: some defaults, such as refrigerant leakage rate, are industry averages that you can override.[^s2]
- **Analytics needs an add-on license**: the prebuilt Net Zero Analytics dashboards require the CRM Analytics for Net Zero Cloud add-on license.[^s1]
- **Defensible methodology**: footprints follow current GHG Protocol guidance, but your organization still owns the choice and review of factors and methods.[^s2]

## AI and data integration

Salesforce added Agentforce to the product so sustainability teams can ask questions about emissions and energy data in natural language. Agents can also draft disclosure responses for frameworks such as CSRD, SASB and CDP, and the work is grounded in company data through the Salesforce trust layer.[^s6] The same announcement describes a Data Cloud integration that unifies sustainability, energy and supplier data from finance, procurement and operations systems. It also describes a no-code builder for custom agents, for example one that watches water use for anomalies.[^s6] The product guide adds a Data Collection Agent for supply-chain data and a marketplace for emissions-factor datasets such as IPCC, USEEIO and IEA.[^s5]

## When to use it (and when not)

Use it when emissions data and disclosures need the same governance, sharing, audit and workflow tooling as other Salesforce data. It also fits when sustainability insight needs to appear inside sales, service, commerce or field service work.[^s5] A standalone carbon tool or a spreadsheet may suffice for an organization that only needs a simple scope 1 and 2 inventory and has no other Salesforce footprint. That is a trade-off to weigh rather than a documented limit.

## Connections

- **Broader**: the developer guide is published with the Salesforce Industries documentation. Like other industry products, it adds a specialized data model on the platform.[^s1]
- **Implements** the GHG Protocol, the accounting guidance its footprints follow.[^s2]
- **Integrates with** Data Cloud, for unifying sustainability data,[^s6] and with CRM Analytics, which powers the Net Zero Analytics dashboards.[^s1]
- **Depends on** the Einstein Trust Layer, which grounds its Agentforce features.[^s6]
- **Related** to Agentforce, which supplies the agent features behind the new name,[^s6] and to the Salesforce Platform it runs on.[^s1]

## Sources
[^s1]: Salesforce, "Introduction to Net Zero Cloud", Net Zero Cloud Developer Guide. https://developer.salesforce.com/docs/industries/netzero-cloud-dev-guide/guide/netzero-cloud-std-objects-intro.html (accessed 2026-11-15)
[^s2]: Salesforce, "Net Zero Cloud Calculations", Net Zero Cloud Developer Guide. https://developer.salesforce.com/docs/industries/netzero-cloud-dev-guide/guide/netzero-cloud-calculations.html (accessed 2026-11-15)
[^s3]: Trailhead, "Track Emissions with Net Zero Cloud". https://trailhead.salesforce.com/content/learn/modules/net-zero-cloud-basics/track-emissions-with-net-zero-cloud (accessed 2026-11-15)
[^s4]: Trailhead, "Learn the Foundations of Carbon Accounting". https://trailhead.salesforce.com/content/learn/modules/carbon-accounting-for-assets-with-net-zero-cloud/learn-the-foundations-carbon-accounting (accessed 2026-11-15)
[^s5]: Salesforce, "Net Zero Cloud Guide". https://www.salesforce.com/net-zero/cloud/guide/ (accessed 2026-11-15)
[^s6]: Salesforce, "Agentforce for Net Zero Cloud" announcement. https://www.salesforce.com/news/stories/agentforce-for-net-zero-cloud-announcement/ (accessed 2026-11-15)
