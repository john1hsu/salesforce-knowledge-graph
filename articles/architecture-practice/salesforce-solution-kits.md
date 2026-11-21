---
id: kt:salesforce-solution-kits
type: Tool
title: Salesforce Solution Kits
aliases: [Solution Kits, CRM Solution Kits, Salesforce solution kit, cross-cloud solution kits]
domain: architecture-practice
summary: >-
  Salesforce-vetted reference packages for architects and solution engineers that start from a common cross-cloud use
  case (such as abandoned cart or unified customer identity) and bundle the required products, a workflow, the connecting
  technology, configuration steps, design considerations and a solution architecture diagram.
release: "Winter '27"
status: current
broader: [kt:reference-architectures]
related: [kt:customer-360, kt:salesforce-diagrams, kt:architect-decision-guides, kt:commerce-cloud, kt:marketing-cloud-engagement, kt:experience-cloud-identity]
relations:
  - {predicate: usedBy, object: kt:salesforce-architect}
  - {predicate: enables, object: kt:cross-cloud-integration}
sources:
  - id: s1
    title: "Salesforce Solution Kits: Quick Look — Deliver Connected Customer Experiences with Solution Kits"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-solution-kits-quick-look/c360-sk1
    type: official-learning
    accessed: 2026-11-21
  - id: s2
    title: "Our Guides for Connecting Commerce, Marketing, and Service"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/?p=3076
    type: official-blog
    accessed: 2026-11-21
  - id: s3
    title: "Implement B2C Cross-Cloud Solutions (trail)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/en/content/learn/trails/implement-b2c-crosscloud-solutions
    type: official-learning
    accessed: 2026-11-21
  - id: s4
    title: "Cross-Cloud Customer Identity and Data Management for Salesforce B2C Commerce — Enable Unified Customer Identity"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/customer-identity-and-data-management-for-b2c-commerce/enable-unified-customer-identity
    type: official-learning
    accessed: 2026-11-21
created: 2026-11-21
---

# Salesforce Solution Kits

**Salesforce Solution Kits** are packaged reference materials that Salesforce publishes to help architects and solution engineers make the technical decisions involved in connecting several Salesforce clouds. Each kit begins with a use case that solves a common cross-cloud challenge, and Salesforce describes the guidance as vetted with its own experts, so a team can start from an approved pattern instead of designing the connection from scratch.[^s1] Trailhead now markets them as "CRM Solution Kits", while the body text calls them Salesforce solution kits; both names refer to the same resource.[^s1]

## What a kit contains

Every kit follows the same structure, which makes kits easy to compare and reuse:[^s1]

- **Required products**: the clouds and add-ons the use case needs before anything can be built.[^s1]
- **Workflow**: a visual overview of how users and systems interact across the clouds in the scenario.[^s1]
- **Connecting technology**: the connectors or APIs that move data or identity between the products.[^s1]
- **Configurations**: the setup work to do in each product involved.[^s1]
- **Design considerations**: limits and performance guardrails to plan for, such as data set import limits.[^s1]
- **Resources**: supporting documentation and links to related kits.[^s1]

Each kit also ships with a solution architecture diagram that shows the data flow between the products.[^s1]

## History and examples

Salesforce introduced the kits in 2019 as a set of guides with best practices, considerations and materials for building continuous customer experiences across Commerce, Marketing and Service.[^s2] The first set covered six use cases: abandoned shopping cart, coupon redemption, order on behalf of a customer, personalized marketing recommendations, transactional email, and viewing order history and cancelling orders.[^s2] Those early kits were published as downloadable Salesforce Help articles.[^s2]

The Abandoned Cart kit is still the standard teaching example. It helps a retailer nudge shoppers to complete purchases left in a digital cart. To do that it connects Agentforce Commerce with Agentforce Marketing Engagement, and its design considerations call out data set import limits.[^s1]

Kits have since grown beyond marketing and commerce. The Trailhead trail *Implement B2C Cross-Cloud Solutions* is aimed at architects and uses B2C solution kits across Commerce Cloud, Experience Cloud and the Salesforce Platform.[^s3] Its customer-identity module walks through a kit for giving each shopper one login across a B2C Commerce storefront and an Experience Cloud site.[^s4] That design needs Experience Cloud, Salesforce Identity and B2C Commerce. Experience Cloud is the system of record for profile data and credentials, and B2C Commerce keeps shopping data such as address books and wish lists.[^s4] Salesforce Identity acts as an OAuth 2.0 provider for B2C Commerce, and External Identity Embedded Login handles the branded sign-in. The design uses person accounts, because the B2C Commerce connector to the service side supports them out of the box.[^s4]

## When to use them (and gotchas)

Use a solution kit early in design, when a requirement matches a kit's use case. The kit gives you a starting product list, an integration approach and a set of known guardrails, which shortens discovery and lowers the risk of an unsupported pattern. Custom requirements can be layered on top of the kit's baseline.[^s1] Kits are narrow by design: each one covers a single scenario. For choosing between overlapping platform tools in general, the decision guides are a better fit.

Check the kit's age and product names before relying on it. The original kits date from 2019, and products have been renamed since then; current Trailhead material refers to Agentforce Commerce and Agentforce Marketing Engagement.[^s2][^s1] Also confirm any limit a kit lists against the current release documentation, because the kit only points to the guardrail and the actual value can change between releases.[^s1]

## Connections

Solution kits are a specialized kind of **reference architecture** (`broader: kt:reference-architectures`). Each kit pairs a use-case narrative with an architecture diagram and configuration steps, where a reference diagram alone shows only the structure.[^s1] Their diagrams fit alongside **Salesforce Diagrams**, and **Architect Decision Guides** cover the complementary job of choosing between tools.[^s1] The kits exist to stitch together **Customer 360** clouds such as **Commerce Cloud**, **Marketing Cloud Engagement** and Service, so they enable **cross-cloud integration** (`kt:cross-cloud-integration`).[^s2] The identity kit is a worked example of **Experience Cloud identity** used together with B2C Commerce.[^s4] The primary audience is the **Salesforce Architect** role, along with solution engineers.[^s1][^s3]

## Sources
[^s1]: Salesforce Trailhead, "Salesforce Solution Kits: Quick Look — Deliver Connected Customer Experiences with Solution Kits". https://trailhead.salesforce.com/content/learn/modules/salesforce-solution-kits-quick-look/c360-sk1 (accessed 2026-11-21)
[^s2]: Salesforce (Ron Pereira), "Our Guides for Connecting Commerce, Marketing, and Service", 2019. https://www.salesforce.com/blog/?p=3076 (accessed 2026-11-21)
[^s3]: Salesforce Trailhead, "Implement B2C Cross-Cloud Solutions" trail. https://trailhead.salesforce.com/en/content/learn/trails/implement-b2c-crosscloud-solutions (accessed 2026-11-21)
[^s4]: Salesforce Trailhead, "Enable Unified Customer Identity" (Cross-Cloud Customer Identity and Data Management for Salesforce B2C Commerce). https://trailhead.salesforce.com/content/learn/modules/customer-identity-and-data-management-for-b2c-commerce/enable-unified-customer-identity (accessed 2026-11-21)
