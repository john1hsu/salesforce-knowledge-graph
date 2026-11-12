---
id: kt:financial-services-cloud
type: Product
title: Financial Services Cloud
aliases: [Agentforce Financial Services, Salesforce Financial Services Cloud, FSC]
domain: clouds-and-products
summary: >-
  Salesforce's industry cloud for banks, wealth managers, lenders and insurers, now also branded Agentforce Financial
  Services, which adds financial-account, household, onboarding/KYC and compliance data models and tools on top of
  Sales Cloud and Service Cloud.
release: "Winter '27"
status: current
broader: [kt:salesforce-industries]
related: [kt:sales-cloud, kt:service-cloud, kt:omnistudio, kt:experience-cloud, kt:health-cloud]
relations:
  - {predicate: dependsOn, object: kt:person-accounts}
  - {predicate: hasPart, object: kt:compliant-data-sharing}
  - {predicate: hasPart, object: kt:actionable-relationship-center}
  - {predicate: integratesWith, object: kt:data-cloud}
  - {predicate: integratesWith, object: kt:agentforce}
sources:
  - id: s1
    title: "Meet Financial Services Cloud (Financial Services Cloud Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/financial-services-cloud-basics/meet-financial-services-cloud
    type: official-learning
    accessed: 2026-11-12
  - id: s2
    title: "Explore Financial Services Cloud Sectors (Financial Services Cloud Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/financial-services-cloud-basics/explore-financial-services-cloud-sectors
    type: official-learning
    accessed: 2026-11-12
  - id: s3
    title: "Dive into Financial Services Cloud Solutions (Financial Services Cloud Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/financial-services-cloud-basics/dive-into-financial-services-cloud-solutions
    type: official-learning
    accessed: 2026-11-12
  - id: s4
    title: "Build Households and Groups (Client Management in Financial Services Cloud)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/client-management-in-financial-services-cloud/build-households-and-groups
    type: official-learning
    accessed: 2026-11-12
  - id: s5
    title: "Financial Services Cloud Developer Guide (Winter '27, API 68.0)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.financial_services_cloud_object_reference.meta/fsc_business_apis.htm
    type: official-docs
    accessed: 2026-11-12
  - id: s6
    title: "Financial Services Cloud — Product Overview"
    publisher: Salesforce
    url: https://www.salesforce.com/financial-services/cloud/
    type: news
    accessed: 2026-11-12
created: 2026-11-12
---

# Financial Services Cloud

Financial Services Cloud (FSC) is Salesforce's industry cloud for financial institutions. Trailhead describes it as a set of features, components and data models built for banks, wealth-management firms, lenders and insurers, running on the Salesforce Platform and extending the sales and service products with financial-industry functionality.[^s1] Trailhead now states that the product has been renamed **Agentforce Financial Services**, in line with the Agentforce Sales and Agentforce Service branding, while the developer guide and the product page still use the Financial Services Cloud name.[^s1][^s5][^s6] It belongs to the Salesforce Industries family of vertical clouds alongside Health Cloud and Public Sector Solutions.

## Sectors and capabilities

The product is organized by line of business, each with its own data model and prebuilt experiences:[^s2]

- **Retail banking.** Bankers see financial accounts, households and branches; a Branch Manager dashboard tracks team performance.[^s2]
- **Wealth management.** Advisor client views, planning and notes, goal alerts, a Run My Day briefing and an AI-generated Client Pulse.[^s2]
- **Commercial banking.** A Commercial Banking Console, deal tracking, Business Relationship Plans, and KYC/KYB onboarding models.[^s2]
- **Insurance.** Policy, quote, commission and claims data models, with optional Digital and Brokerage add-ons.[^s2]
- **Lending.** A loan application data model, a borrower Experience Cloud site, disclosures and consent, and Omnistudio-modeled loan processes.[^s2]

Across sectors, Trailhead groups the tools into relationships, onboarding, service, engagement, automation and compliance. Relationship tools include householding, the Actionable Relationship Center (ARC), financial accounts and financial goals. Onboarding includes the Discovery Framework, the Know Your Customer data model and Intelligent Document Automation. Service Process Studio extends the Case object with prebuilt processes such as fee reversal and transaction disputes.[^s3] For compliance, field tracking and change auditing sit beside **Compliant Data Sharing**, which lets admins configure stricter, role-aware data-sharing rules without code.[^s3] The product page adds prebuilt Agentforce agents for banking, wealth and insurance work and zero-copy access to external data through Data 360 (formerly Data Cloud).[^s6]

## Data model: households and relationships

Individual clients are usually modeled as person accounts. Households and other groups exist for wealth-style work where one advisor serves a family. In the standard model, a household is a business account tied to a party relationship group of type Household, with members linked through account-contact relationship records.[^s4] A person account can belong to several groups but has only one primary group, and relationships between people must be created reciprocally so they read correctly from both sides.[^s4] Financial summary rollups (investments, liabilities, deposits) are computed by eight predefined Data Processing Engine definitions and stored in the Account Financial Summary object.[^s4] ARC's Relationship Graph visualizes these connections on Lightning record pages.[^s4]

## Gotchas: managed package vs. core

FSC exists in two forms. Older orgs run the **managed package**, whose objects and fields carry the `FinServ` namespace, such as the custom object `FinServ__FinancialAccount__c`.[^s5] Newer capabilities ship as standard objects in core. The developer guide warns that package components are one API version behind core Salesforce, while standard FSC objects share the core API version.[^s5] Trailhead also notes that households work differently in the managed package, so instructions written for the standard model may not apply to a package org.[^s4] Check which model an org uses before designing integrations or copying setup steps.

## When to use it

Choose FSC when a firm needs financial accounts, households, KYC onboarding, regulated data sharing and sector templates rather than building them from generic Sales Cloud and Service Cloud objects.[^s1][^s3] Salesforce sells editions such as Sales Core, Service Core, Sales & Service Core and the Max tiers, with Max adding the Agentforce industry suite and Data 360 connectivity; list prices are published and subject to change.[^s6] For firms that only need basic contact and opportunity management, standard Sales Cloud may be enough, and Trailhead notes that person accounts alone can serve individual-focused work without households.[^s4]

## Connections

FSC has the **broader** node `kt:salesforce-industries`, the vertical-cloud family it belongs to. It is **related** to `kt:sales-cloud` and `kt:service-cloud`, which it extends, to `kt:omnistudio`, used for Discovery Framework, Service Process Studio and lending processes, and to `kt:experience-cloud`, which hosts borrower portals.[^s1][^s2][^s3] It is a sibling of `kt:health-cloud`. It **depends on** `kt:person-accounts` for individual clients and **has part** `kt:actionable-relationship-center` and `kt:compliant-data-sharing`.[^s3][^s4] It **integrates with** `kt:data-cloud` for calculated insights and zero-copy data and with `kt:agentforce` for prebuilt financial-services agents.[^s3][^s6]

## Sources
[^s1]: Trailhead, "Meet Financial Services Cloud". https://trailhead.salesforce.com/content/learn/modules/financial-services-cloud-basics/meet-financial-services-cloud (accessed 2026-11-12)
[^s2]: Trailhead, "Explore Financial Services Cloud Sectors". https://trailhead.salesforce.com/content/learn/modules/financial-services-cloud-basics/explore-financial-services-cloud-sectors (accessed 2026-11-12)
[^s3]: Trailhead, "Dive into Financial Services Cloud Solutions". https://trailhead.salesforce.com/content/learn/modules/financial-services-cloud-basics/dive-into-financial-services-cloud-solutions (accessed 2026-11-12)
[^s4]: Trailhead, "Build Households and Groups". https://trailhead.salesforce.com/content/learn/modules/client-management-in-financial-services-cloud/build-households-and-groups (accessed 2026-11-12)
[^s5]: Salesforce, "Financial Services Cloud Developer Guide" (Winter '27). https://developer.salesforce.com/docs/atlas.en-us.financial_services_cloud_object_reference.meta/fsc_business_apis.htm (accessed 2026-11-12)
[^s6]: Salesforce, "Financial Services Cloud — Product Overview". https://www.salesforce.com/financial-services/cloud/ (accessed 2026-11-12)
