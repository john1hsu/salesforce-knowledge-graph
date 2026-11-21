---
id: kt:customer-360
type: Product
title: Customer 360
aliases: [Salesforce Customer 360, Customer 360 Apps, Customer 360 Truth, Customer 360 business logic]
domain: clouds-and-products
summary: >-
  Salesforce's name for its full set of customer-facing applications (Sales, Service, Marketing, Commerce, Revenue,
  Field Service, Industries and related apps) sharing one platform and data model; in the Agentforce 360 architecture
  it is the business-logic layer that sits on Data 360 and that agents act through.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:slack-platform, kt:salesforce-industries]
relations:
  - {predicate: hasPart, object: kt:sales-cloud}
  - {predicate: hasPart, object: kt:service-cloud}
  - {predicate: hasPart, object: kt:salesforce-marketing-solutions}
  - {predicate: hasPart, object: kt:commerce-cloud}
  - {predicate: dependsOn, object: kt:data-cloud}
  - {predicate: integratesWith, object: kt:agentforce}
sources:
  - id: s1
    title: "Explore Customer 360 Business Logic (The Salesforce Agentic Enterprise Architecture)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/the-salesforce-agentic-enterprise-architecture/explore-the-customer-360-business-logic
    type: official-learning
    accessed: 2026-11-21
  - id: s2
    title: "Experience the Power of Unified Data (Unify Sales and Service Data with Data 360 Solutions)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-360-with-sales-and-service/experience-the-power-of-unified-data
    type: official-learning
    accessed: 2026-11-21
  - id: s3
    title: "Welcome to the Agentic Enterprise: With Agentforce 360, Salesforce Elevates Human Potential in the Age of AI"
    publisher: Salesforce
    url: https://www.salesforce.com/news/press-releases/2025/10/13/agentic-enterprise-announcement/
    type: news
    accessed: 2026-11-21
  - id: s4
    title: "Q&A: Inside Salesforce Customer 360"
    publisher: Salesforce
    url: https://www.salesforce.com/news/stories/qa-inside-salesforce-customer-360/
    type: news
    accessed: 2026-11-21
  - id: s5
    title: "Discover Salesforce (Salesforce Customer 360 module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-customer-360/discovers-salesforce-customer-360
    type: official-learning
    accessed: 2026-11-21
created: 2026-11-21
---

# Customer 360

**Customer 360** is the umbrella name Salesforce uses for its customer-facing application portfolio. Trailhead stresses that it is not a single app; it is the whole set of applications that already run a company's sales, service, marketing and commerce operations.[^s1] The common promise behind the name is that every employee works from one shared view of each customer on one integrated platform.[^s5]

## What it includes

Trailhead's agentic-architecture module lists the applications that make up Customer 360 and the job each one does:[^s1]

- **Sales Cloud** runs the pipeline from lead to close, and **Service Cloud** handles support across channels.[^s1]
- **Marketing Cloud** covers campaigns, personalization and journeys; **Commerce Cloud** runs storefronts and buying experiences.[^s1]
- **Revenue Cloud** handles quoting, billing and revenue operations; **Field Service** schedules and dispatches on-site work.[^s1]
- **IT & HR Service**, the **Industries** solutions (for example Financial Services, Health and Manufacturing) and **Tableau** analytics round out the set.[^s1]

The October 2025 Agentforce 360 announcement grouped the agent-enabled editions under a "Customer 360 Apps" heading, naming Agentforce Sales, Marketing, Service, Field Service, Revenue Management, Commerce, IT Service and 360 for Industries.[^s3]

## How it works

In the current architecture Salesforce describes four layers. The Agentforce 360 Platform is the foundation for building and running agents, Data 360 is the unified data layer that gives agents context, Customer 360 Apps supply the business logic and institutional memory, and Slack is the conversational interface where people and agents work together.[^s3]

The business-logic framing is the key idea. Approval chains, definitions such as what counts as a qualified lead, and the steps of a workflow already live inside these applications, and Trailhead presents them as decades of encoded process that agents can reuse rather than reinvent.[^s1] Business terms like revenue, churn or pipeline health are defined once and governed centrally, so humans, dashboards and agents agree on their meaning; the module also notes that this logic can be adjusted in plain language and that agents pick up the change.[^s1]

Data unification sits underneath. Data 360 ingests records from sales, service and other sources, harmonizes them into the Customer 360 Data Model (data model objects such as Account, Contact Point Email and Contact Point Phone), and links records about the same person or account into unified profiles through identity resolution.[^s2] Trailhead contrasts this "system of reference" with siloed systems of record.[^s2]

## History and naming

The name is older than the agent era. At Dreamforce 2019 Salesforce introduced **Customer 360 Truth**, built from four services: Customer 360 Data Manager, Salesforce Identity for Customers, Customer 360 Audiences (described as Salesforce's customer data platform) and Salesforce Privacy and Data Governance.[^s4] At the time Salesforce called Customer 360 its vision for helping customers transform, and said Truth was powered by the open-source Cloud Information Model.[^s4] In this graph those 2019 names survive as aliases: Customer 360 Audiences on `kt:data-cloud` (Data 360) and Customer 360 Identity on `kt:salesforce-identity`, while the data-unification role now belongs to Data 360 and its Customer 360 Data Model.[^s2][^s4]

## Gotchas

- Customer 360 names a portfolio of many apps, not one app, so check which specific cloud or edition a capability belongs to.[^s1][^s3]
- "Customer 360 Data Model" refers to the Data 360 data model, not to the Sales or Service object schema itself, though those objects map into it.[^s2]
- Marketing names drift: Salesforce product pages and announcements may say Customer 360, Agentforce 360 or a specific cloud for overlapping things, so check which layer a document means.[^s3]

## Connections

Customer 360 sits under `kt:salesforce-platform`, the Agentforce 360 Platform foundation that the announcement places beneath the apps.[^s3] It **has parts** `kt:sales-cloud`, `kt:service-cloud`, `kt:salesforce-marketing-solutions` and `kt:commerce-cloud`, and it relates to `kt:salesforce-industries` for vertical solutions.[^s1] It **depends on** `kt:data-cloud` (Data 360) for its unified data layer, **integrates with** `kt:agentforce`, whose agents act through Customer 360 business logic, and relates to `kt:slack-platform` as the conversational front end of the same architecture.[^s2][^s3]

## Sources
[^s1]: Trailhead, "Explore Customer 360 Business Logic". https://trailhead.salesforce.com/content/learn/modules/the-salesforce-agentic-enterprise-architecture/explore-the-customer-360-business-logic (accessed 2026-11-21)
[^s2]: Trailhead, "Experience the Power of Unified Data". https://trailhead.salesforce.com/content/learn/modules/data-360-with-sales-and-service/experience-the-power-of-unified-data (accessed 2026-11-21)
[^s3]: Salesforce, "Welcome to the Agentic Enterprise: With Agentforce 360, Salesforce Elevates Human Potential in the Age of AI" (13 Oct 2025). https://www.salesforce.com/news/press-releases/2025/10/13/agentic-enterprise-announcement/ (accessed 2026-11-21)
[^s4]: Salesforce, "Q&A: Inside Salesforce Customer 360" (19 Nov 2019). https://www.salesforce.com/news/stories/qa-inside-salesforce-customer-360/ (accessed 2026-11-21)
[^s5]: Trailhead, "Discover Salesforce". https://trailhead.salesforce.com/content/learn/modules/salesforce-customer-360/discovers-salesforce-customer-360 (accessed 2026-11-21)
