---
id: kt:org-strategy
type: Concept
title: Org Strategy
aliases: [Salesforce org strategy, single-org vs multi-org, multi-org strategy, single-org architecture, multi-org architecture]
domain: platform-architecture
summary: >-
  The enterprise architecture decision about how many production Salesforce orgs a company runs (one shared org
  or several) and how those orgs are governed, integrated and reported across.
release: "Winter '27"
status: concept
broader: [kt:solution-design-tradeoffs]
related: [kt:environment-strategy, kt:data-residency, kt:data-cloud, kt:single-sign-on-saml]
relations:
  - {predicate: dependsOn, object: kt:integration-patterns}
  - {predicate: mitigates, object: kt:data-skew}
sources:
  - id: s1
    title: "Data Cloud Provisioning (Salesforce Architects decision guide)"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/decision-guides/data-cloud-provisioning
    type: official-docs
    accessed: 2026-11-06
  - id: s2
    title: "Single Org Architecture (Salesforce Architects reference diagram)"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/reference-diagrams/guide/single-org-architecture
    type: official-docs
    accessed: 2026-11-06
  - id: s3
    title: "Enterprise Architecture with Force.com: Multi-Org Strategy"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/developer-relations/2014/10/enterprise-architecture-multi-org-strategy
    type: official-blog
    accessed: 2026-11-06
  - id: s4
    title: "Four Factors to Consider for a Successful Salesforce Org Strategy"
    publisher: Salesforce Architects (Medium)
    url: https://medium.com/salesforce-architects/four-factors-to-consider-for-a-successful-salesforce-org-strategy-2295da39c55e
    type: official-blog
    accessed: 2026-11-06
  - id: s5
    title: "Single- or Multi-Org Architecture? Six Factors to Consider"
    publisher: Salesforce Architects (Medium)
    url: https://medium.com/salesforce-architects/single-or-multi-org-architecture-six-factors-to-consider-849d7f2d9b7a
    type: official-blog
    accessed: 2026-11-06
created: 2026-11-06
---

# Org Strategy

An **org strategy** decides whether a company runs one Salesforce production org for all of its business units or several orgs, and how those orgs relate to each other. Salesforce's architects describe it as a foundational choice that shapes staffing, governance, budget and functionality, and one that is expensive to reverse once implementation is under way.[^s4] Because every later design (data model, sharing, release management, integration) is built inside the chosen org boundaries, it is treated as an enterprise architecture decision rather than a project-level one.[^s3]

## The two basic shapes

A **single-org** strategy puts multiple business units, sometimes global ones, on one shared org; Salesforce's reference diagram shows one org serving several units, each consuming shared products or capabilities such as lead or case management.[^s2] Its benefits are integrated processes and data, one set of governance, fewer integrations and lower licensing and environment overhead, and an easier single customer view. The price is complexity inside the org: harder security and sharing design, stricter naming standards, more disciplined Apex, more contention between business units for change capacity, and limits shared by everyone.[^s3]

A **multi-org** strategy gives regions, brands or business units their own orgs. It buys isolation (for regulation or divergent processes), independent release cycles and governance, and separate limits, at the cost of extra licences, duplicated data and processes, cross-org integration work and the need for single sign-on so users are not juggling logins.[^s3]

## Decision factors

Salesforce Architects frame the decision across four dimensions rather than technology alone: **business** (how units go to market and whether processes should be common), **technology** (data model, security, integration and data volumes), **governance and culture** (appetite for central control and readiness for change) and **operations** (shared versus per-org support desks and release management).[^s4] An older but still useful framework maps the choice to the company's operating model: highly standardized and integrated businesses favour as few orgs as possible, while diversified businesses with little shared process will likely keep several orgs permanently.[^s3] The same guidance warns that a growing number of business units is not, by itself, a sound reason to split, and that apparent limit problems should be raised with the account team before they drive an org split.[^s3]

A worked example from a regulated global company shows the factors pulling in different directions. Although back-office ERP had been consolidated, sales, service and marketing rules differed by region, so the team plotted each factor on a spectrum from "clearly shared" to "clearly separate" and chose regional orgs. Global roll-up reporting moved to an external analytics tool, which also reduced per-org data volumes, the risk of data skew and the need for complex sharing; support teams specialized by region; and middleware absorbed the extra integration load.[^s5]

## Multi-org patterns and gotchas

Common multi-org patterns include a central org distributing packaged functionality to replicated units, a **hub-and-spoke** design in which a hub org holds master data shared to spokes, and a separate reporting or collaboration hub for consolidated visibility. Without such a pattern, point-to-point org links tend to become brittle "spaghetti" integrations.[^s3] Each org also needs its own governance (a change committee, architecture review and tiered administration), with a centre of excellence owning shared standards across all of them.[^s3]

Data Cloud adds a newer lever. Many enterprises run multiple orgs because of acquisitions, regions or history, and Salesforce's provisioning guide recommends a single **Home Org** hosting Data Cloud with other orgs attached as companion orgs, reserving multiple independent Data Cloud instances for strict autonomy, residency or compliance needs.[^s1] It also advises making such provisioning choices through an enterprise architecture or governance council rather than org by org.[^s1]

## Connections

Org strategy sits **under** `kt:solution-design-tradeoffs`, because it is a classic balance of integration value against isolation.[^s4] It is distinct from `kt:environment-strategy`, which plans the sandboxes and scratch orgs that feed each production org once their number is set.[^s3] A multi-org design **depends on** `kt:integration-patterns` for cross-org data flow,[^s3] and splitting data across orgs can **mitigate** `kt:data-skew` and heavy sharing loads.[^s5] It is **related** to `kt:data-residency`, a common reason for separate orgs or separate Data Cloud instances,[^s1] to `kt:data-cloud`, whose Home Org model unifies customer data across orgs,[^s1] and to `kt:single-sign-on-saml`, which keeps a multi-org landscape usable for people who work in more than one org.[^s3]

## Sources
[^s1]: Salesforce Architects, "Data Cloud Provisioning" decision guide. https://architect.salesforce.com/decision-guides/data-cloud-provisioning (accessed 2026-11-06)
[^s2]: Salesforce Architects, "Single Org Architecture" reference diagram. https://architect.salesforce.com/docs/architect/reference-diagrams/guide/single-org-architecture (accessed 2026-11-06)
[^s3]: Greg Cook, "Enterprise Architecture with Force.com: Multi-Org Strategy", Salesforce Developers Blog, 2014. https://developer.salesforce.com/blogs/developer-relations/2014/10/enterprise-architecture-multi-org-strategy (accessed 2026-11-06)
[^s4]: Divya Alavarthi, Martin Griffiths and Pierre Couppey, "Four Factors to Consider for a Successful Salesforce Org Strategy", Salesforce Architects, 2021. https://medium.com/salesforce-architects/four-factors-to-consider-for-a-successful-salesforce-org-strategy-2295da39c55e (accessed 2026-11-06)
[^s5]: Tom Leddy, "Single- or Multi-Org Architecture? Six Factors to Consider", Salesforce Architects, 2023. https://medium.com/salesforce-architects/single-or-multi-org-architecture-six-factors-to-consider-849d7f2d9b7a (accessed 2026-11-06)
