---
id: kt:government-cloud-plus
type: Product
title: Government Cloud Plus
aliases: [Salesforce Government Cloud Plus, GovCloud Plus, Gov Cloud Plus]
domain: public-sector-and-compliance
summary: >-
  Salesforce's dedicated, isolated instance of its SaaS and PaaS services for eligible US government customers,
  carrying a FedRAMP High authorization (FedRAMP ID FR2003061248), with a separate Defense variant for DoD Impact
  Level 5 data.
release: "Winter '27"
status: current
broader: [kt:hyperforce]
related: [kt:public-sector-solutions, kt:multitenancy, kt:agentforce, kt:mulesoft-anypoint-platform]
relations:
  - {predicate: implements, object: kt:fedramp-high}
  - {predicate: hasPart, object: kt:il4-and-il5}
  - {predicate: contrastsWith, object: kt:government-cloud}
sources:
  - id: s1
    title: "Government Cloud Plus (Compliance services page)"
    publisher: Salesforce
    url: https://compliance.salesforce.com/services/salesforce-government-cloud-plus-hyperforce
    type: official-docs
    accessed: 2026-10-31
  - id: s2
    title: "FedRAMP Marketplace: Salesforce Government Cloud Plus (FR2003061248)"
    publisher: FedRAMP (GSA)
    url: https://www.fedramp.gov/marketplace/products/FR2003061248/
    type: government
    accessed: 2026-10-31
  - id: s3
    title: "Salesforce Launches Government Cloud Plus, Achieves FedRAMP Provisional Authority to Operate at the High Security Impact Level"
    publisher: Salesforce Investor Relations
    url: https://investor.salesforce.com/news/news-details/2020/Salesforce-Launches-Government-Cloud-Plus-Achieves-FedRAMP-Provisional-Authority-to-Operate-at-the-High-Security-Impact-Level/default.aspx
    type: news
    accessed: 2026-10-31
  - id: s4
    title: "Government Cloud Plus - Defense (Compliance services page)"
    publisher: Salesforce
    url: https://compliance.salesforce.com/services/salesforce-government-cloud-plus-defense
    type: official-docs
    accessed: 2026-10-31
  - id: s5
    title: "MuleSoft Government Cloud Plus"
    publisher: MuleSoft (Salesforce)
    url: https://docs.mulesoft.com/govcloud-plus/
    type: official-docs
    accessed: 2026-10-31
  - id: s6
    title: "Use Agentforce Vibes with Government Cloud Orgs"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/agentforcevibes/guide/afv-government-cloud.html
    type: official-docs
    accessed: 2026-10-31
created: 2026-10-31
---

# Government Cloud Plus

Government Cloud Plus is a dedicated instance of Salesforce's PaaS and SaaS applications that runs on an authorized government cloud and is sold under its own name; Salesforce's compliance statements for it apply only to the environment branded that way.[^s1] It is aimed at US public-sector buyers who need a FedRAMP High authorization rather than the controls of the commercial multitenant service. At launch Salesforce listed eligible customers as US federal, state and local government bodies, government contractors, and federally funded research and development centers.[^s3]

## History and authorization

Salesforce announced Government Cloud Plus on June 18, 2020, alongside a FedRAMP Provisional Authority to Operate at the High security impact level granted through the Joint Authorization Board (JAB), which then provided continuous monitoring of the system's security posture.[^s3] The launch announcement described it as a dedicated, isolated instance built on AWS GovCloud (US).[^s3] Today the FedRAMP Marketplace lists "Salesforce Government Cloud Plus" (ID FR2003061248) at the High impact level on the JAB path, Rev5, with a status of FedRAMP Certified in the ongoing-certification phase, certified since May 27, 2020; at the time of access it showed 67 agency ATO/ATU letters issued against the package.[^s2]

Salesforce's compliance portal lists the same FedRAMP ID, a Government Community Cloud deployment model, SaaS and PaaS service models, and Coalfire Systems as the independent assessor. Beyond FedRAMP High it lists DoD IL2, CJIS, TX-RAMP, SOC 1 and HIPAA-related material, and its document table tags some authorization artifacts as AWS and others as Hyperforce, reflecting the move of the environment onto Salesforce's Hyperforce architecture.[^s1]

## What runs in it

The in-scope service list is broad: Sales Cloud, Service Cloud, Lightning Platform, Experience Cloud, Data Cloud, Agentforce, CRM Analytics, Shield, Public Sector Solutions, MuleSoft Anypoint Platform and Salesforce Mobile are among the certified services.[^s1] Inclusion in the boundary does not mean feature parity with commercial orgs, so practitioners must check each product's government documentation. For example, MuleSoft Government Cloud Plus is a separate US control plane on Hyperforce that only allows CloudHub 2.0 Private Spaces, Runtime Fabric and hybrid standalone deployments, disables outbound internet access from Private Spaces by default, and only permits connectors tagged as FIPS 140-3 verified; it is also distinct from the older MuleSoft Government Cloud.[^s5] Similarly, AI tooling for Government Cloud orgs routes requests to a dedicated government endpoint with LLMs hosted inside Government Cloud, uses a narrower model list, and omits some features such as hosted MCP servers.[^s6]

## Defense variant

Government Cloud Plus - Defense is a physically isolated, dedicated instance intended for the US Department of Defense and its contractors and designed to store and process Impact Level 5 data; its DoD IL5 documentation is tagged Hyperforce.[^s4] Federal staff request the FedRAMP and DoD packages via the FedRAMP Marketplace, while other eligible organizations go through their Salesforce account team.[^s4]

## Limits and gotchas

- **Eligibility is restricted.** Only qualifying government entities and their contractors can buy it, and pricing at launch was set as a 15% uplift on net spend for products hosted in the dedicated instance.[^s3]
- **The authorization covers the boundary, not your org.** Agencies still issue their own ATO against the package; the 67 letters on the Marketplace are individual agency decisions.[^s2]
- **Feature lag.** Products inside the boundary can have reduced or delayed functionality (see the MuleSoft and AI examples above), so validate every required feature before committing an architecture.[^s5][^s6]
- **Documentation access is gated.** Detailed security documentation lives in a public-sector documentation portal and trust center rather than public help pages.[^s1]

## Connections

Government Cloud Plus is a deployment of Salesforce's platform on Hyperforce (its `broader` node), isolating eligible customers from the general multitenant population described in `kt:multitenancy`.[^s1][^s3] It `implements` the FedRAMP High baseline (`kt:fedramp-high`), and its Defense variant is the route to DoD IL5 workloads (`kt:il4-and-il5`).[^s2][^s4] It `contrastsWith` the older Government Cloud offering; MuleSoft, for instance, documents its Government Cloud Plus control plane as a separate platform with its own authorization boundary, infrastructure and feature set.[^s5] Public Sector Solutions, Agentforce and the MuleSoft Anypoint Platform are among the products certified to run inside the boundary, each with its own government-specific constraints.[^s1][^s5][^s6]

## Sources

[^s1]: Salesforce, "Government Cloud Plus" compliance services page. https://compliance.salesforce.com/services/salesforce-government-cloud-plus-hyperforce (accessed 2026-10-31)
[^s2]: FedRAMP (GSA), "Salesforce Government Cloud Plus" Marketplace listing FR2003061248. https://www.fedramp.gov/marketplace/products/FR2003061248/ (accessed 2026-10-31)
[^s3]: Salesforce, "Salesforce Launches Government Cloud Plus, Achieves FedRAMP Provisional Authority to Operate at the High Security Impact Level" (June 18, 2020). https://investor.salesforce.com/news/news-details/2020/Salesforce-Launches-Government-Cloud-Plus-Achieves-FedRAMP-Provisional-Authority-to-Operate-at-the-High-Security-Impact-Level/default.aspx (accessed 2026-10-31)
[^s4]: Salesforce, "Government Cloud Plus - Defense" compliance services page. https://compliance.salesforce.com/services/salesforce-government-cloud-plus-defense (accessed 2026-10-31)
[^s5]: MuleSoft, "MuleSoft Government Cloud Plus". https://docs.mulesoft.com/govcloud-plus/ (accessed 2026-10-31)
[^s6]: Salesforce Developers, "Use Agentforce Vibes with Government Cloud Orgs". https://developer.salesforce.com/docs/platform/agentforcevibes/guide/afv-government-cloud.html (accessed 2026-10-31)
