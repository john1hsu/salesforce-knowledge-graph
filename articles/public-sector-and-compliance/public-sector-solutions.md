---
id: kt:public-sector-solutions
type: Product
title: Public Sector Solutions
aliases: [Agentforce Public Sector, PSS, Salesforce Public Sector Solutions, Agentforce for Public Sector Solutions]
domain: public-sector-and-compliance
summary: >-
  Salesforce's industry product for government agencies (now branded Agentforce Public Sector): a government data
  model, the Industries common layer and prebuilt apps for licensing, permitting, inspections, benefits, grants and
  case management, layered on Service, Sales and Experience Cloud.
release: "Winter '27"
status: current
broader: [kt:salesforce-industries]
related: [kt:service-cloud, kt:experience-cloud, kt:person-accounts]
relations:
  - {predicate: dependsOn, object: kt:omnistudio}
  - {predicate: integratesWith, object: kt:agentforce}
  - {predicate: configuredVia, object: kt:business-rules-engine}
sources:
  - id: s1
    title: "Explore the Components of Public Sector Solutions"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/public-sector-solutions-design/explore-the-components-of-public-sector-solutions
    type: official-learning
    accessed: 2026-10-31
  - id: s2
    title: "Discover Public Sector Solutions"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/public-sector-solutions-quick-look/discover-public-sector-solutions
    type: official-learning
    accessed: 2026-10-31
  - id: s3
    title: "Get Started with Public Sector Cloud (Licensing, Permitting, and Inspections with Public Sector Solutions)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/licensing-permitting-and-inspections-with-public-sector-solutions/get-started-with-public-sector-cloud
    type: official-learning
    accessed: 2026-10-31
  - id: s4
    title: "Prepare the Org (Admin Essentials for Public Sector Solutions)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/admin-essentials-for-public-sector-solutions/prepare-the-org
    type: official-learning
    accessed: 2026-10-31
  - id: s5
    title: "Learn About Agentforce for Public Sector Solutions"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agentforce-for-public-sector-solutions/learn-about-agentforce-for-public-sector-solutions
    type: official-learning
    accessed: 2026-10-31
  - id: s6
    title: "Public Sector Solutions Documentation (PDF)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/admin_public_sector_cloud.pdf
    type: official-docs
    accessed: 2026-10-31
created: 2026-10-31
---

# Public Sector Solutions

Public Sector Solutions (PSS) is Salesforce's industry product for government agencies at every level, from municipal to national. It bundles a government-specific data model, low-code tooling and prebuilt apps for work such as licensing and permitting, benefits, grants and regulatory enforcement.[^s2] Current Trailhead content brands it **Agentforce Public Sector (formerly Public Sector Solutions)**, so both names refer to the same product and this node carries the new name as an alias.[^s3][^s5]

## How it works

Trailhead describes PSS as a stack of layers. The foundation is the Salesforce Platform plus Service Cloud (constituent relationship and case management), Sales Cloud (accounts and service-request objects) and Experience Cloud (public portals where constituents apply for benefits, renew permits or file complaints). On top sits a public-sector data model, then the Industries common layer, then the prebuilt apps.[^s1]

The data model adds purpose-built objects to standard ones. Examples include regulatory authorities, authorization types and regulatory codes for licensing; programs, benefits and care-plan goals for social programs; and complaints, visits, inspections and investigations for enforcement.[^s1] Trailhead notes that these objects line up closely with Data 360 objects, which eases use with Agentforce.[^s1] The admin documentation adds that individuals are modelled as person accounts and many-to-many links use junction objects.[^s6]

The **Industries common layer** supplies shared building blocks. OmniStudio provides guided forms and flows. Action Plans provide task checklists for inspections or eligibility reviews. Document tooling covers checklist items, Intelligent Document Automation and OmniStudio Document Generation. The Business Rules Engine, with Decision Explainer, automates eligibility and fee decisions through expression sets and decision matrices and shows why a rule fired. Further pieces include identity verification, audit trails and the Actionable Relationship Center for household and case relationships.[^s1]

Prebuilt apps cover licensing and permitting with inspections, social program and benefit management, regulatory investigations, grants, emergency programs, talent recruitment and tax and revenue management. Agencies can deploy them modularly.[^s2][^s6] The licensing app follows an authorization lifecycle of outreach and intake, application review, inspection or assessment, issuance and renewal.[^s3] An Agentforce for Public Sector add-on supplies role-based agent templates, for example for complaint resolution and compliance work. Their actions call flows, Apex, prompt templates and APIs, and the Einstein Trust Layer keeps LLMs from retaining constituent data.[^s5]

## Limits and gotchas

- **Person accounts are one-way.** They cannot be disabled once enabled, they are excluded from account hierarchies, and they should be turned on before OmniStudio is installed.[^s4]
- **Trial orgs are limited.** Some setup tasks, including installing OmniStudio, are not available in trial orgs such as a standard Trailhead Playground.[^s4]
- **Licensing varies by purchase.** The licenses and permission set licenses an org sees depend on which apps were bought; check them under Company Information in Setup.[^s4] Users need both the permission set and its permission set license, and the shipped "Designer" permission sets are meant for builders, so clone them with read access for ordinary users.[^s6]
- **OmniStudio is a hard dependency** for Document Generation, the Business Rules Engine and Decision Explainer.[^s6]
- **Usage-based pricing mapping matters.** The admin guide warns that application record types left unmapped default to License and Permit Management, which can inflate usage counts.[^s6]

## When to use it (and when not)

Choose PSS when an agency's processes match its prebuilt apps, such as permits, benefits or inspections. You then inherit a tested data model, portal templates and rules tooling instead of building custom objects on plain Service Cloud.[^s1][^s2] For a single, simple intake process, plain Service Cloud with Experience Cloud may be enough, because PSS brings OmniStudio, person accounts and per-app licensing that must be designed around.[^s4][^s6]

## Connections

PSS sits under `kt:salesforce-industries`, the family of industry clouds that share the common layer.[^s1] It is **related** to `kt:service-cloud` and `kt:experience-cloud`, which form its foundation, and to `kt:person-accounts`, its model for constituents.[^s1][^s6] It **depends on** `kt:omnistudio` for forms and document generation, its eligibility and fee logic is **configured via** `kt:business-rules-engine`, and it **integrates with** `kt:agentforce` through public-sector agent templates.[^s1][^s5][^s6]

## Sources

[^s1]: Trailhead, "Explore the Components of Public Sector Solutions". https://trailhead.salesforce.com/content/learn/modules/public-sector-solutions-design/explore-the-components-of-public-sector-solutions (accessed 2026-10-31)
[^s2]: Trailhead, "Discover Public Sector Solutions". https://trailhead.salesforce.com/content/learn/modules/public-sector-solutions-quick-look/discover-public-sector-solutions (accessed 2026-10-31)
[^s3]: Trailhead, "Get Started with Public Sector Cloud". https://trailhead.salesforce.com/content/learn/modules/licensing-permitting-and-inspections-with-public-sector-solutions/get-started-with-public-sector-cloud (accessed 2026-10-31)
[^s4]: Trailhead, "Prepare the Org". https://trailhead.salesforce.com/content/learn/modules/admin-essentials-for-public-sector-solutions/prepare-the-org (accessed 2026-10-31)
[^s5]: Trailhead, "Learn About Agentforce for Public Sector Solutions". https://trailhead.salesforce.com/content/learn/modules/agentforce-for-public-sector-solutions/learn-about-agentforce-for-public-sector-solutions (accessed 2026-10-31)
[^s6]: Salesforce, "Public Sector Solutions Documentation" (admin guide PDF). https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/admin_public_sector_cloud.pdf (accessed 2026-10-31)
