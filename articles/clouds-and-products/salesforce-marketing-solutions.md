---
id: kt:salesforce-marketing-solutions
type: Product
title: Salesforce Marketing Solutions
aliases: [Marketing Cloud portfolio, Salesforce marketing products, Marketing Cloud product family]
domain: clouds-and-products
summary: >-
  The family of Salesforce marketing products sold under the Marketing Cloud brand: Marketing Cloud Next on the
  core platform, the older Marketing Cloud Engagement (B2C) and Account Engagement (B2B) stacks, and add-ons for
  personalization, marketing intelligence and loyalty, with Data 360 as the shared data foundation.
release: "Winter '27"
status: current
broader: [kt:customer-360]
related: [kt:commerce-cloud, kt:sales-cloud, kt:journey-builder]
relations:
  - {predicate: hasPart, object: kt:marketing-cloud-next}
  - {predicate: hasPart, object: kt:marketing-cloud-engagement}
  - {predicate: hasPart, object: kt:marketing-cloud-account-engagement}
  - {predicate: hasPart, object: kt:loyalty-management}
  - {predicate: dependsOn, object: kt:data-cloud}
  - {predicate: integratesWith, object: kt:agentforce}
sources:
  - id: s1
    title: "Discover Salesforce Marketing Solutions (Salesforce Marketing Cloud Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-marketing-cloud-quick-look/discover-salesforce-marketing-solutions
    type: official-learning
    accessed: 2026-11-19
  - id: s2
    title: "Marketing products (Salesforce Help product index)"
    publisher: Salesforce
    url: https://help.salesforce.com/s/products/marketing
    type: official-docs
    accessed: 2026-11-19
  - id: s3
    title: "Marketing Cloud: the agentic marketing platform"
    publisher: Salesforce
    url: https://www.salesforce.com/marketing/
    type: official-docs
    accessed: 2026-11-19
  - id: s4
    title: "Meet Interaction Studio (Marketing Cloud Personalization Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/interaction-studio-basics/meet-interaction-studio
    type: official-learning
    accessed: 2026-11-19
created: 2026-11-19
---

# Salesforce Marketing Solutions

**Salesforce Marketing Solutions** is the umbrella for the marketing products Salesforce sells, marketed together under the Marketing Cloud brand. Trailhead's quick-look unit uses the phrase for the whole range and frames the practitioner's job as matching a business need to the right product in it.[^s1] Salesforce's marketing site positions the family as an agentic marketing platform, with Marketing Cloud Next as the flagship and Data 360 as the shared customer data foundation.[^s3] The family is a portfolio, not a single installable product: its members run on different technology stacks, use different people objects and automation tools, and are documented separately in Salesforce Help.[^s1][^s2]

## The products in the family

The portfolio has three main marketing applications, plus add-ons that layer on top of them.[^s1]

- **Marketing Cloud Next** runs natively on the core platform and is powered by Data 360, using Flow Builder, Data 360 segments and Experience Builder editors.[^s1]
- **Marketing Cloud Engagement** (formerly ExactTarget) is the B2C stack built around Journey Builder, Automation Studio, subscribers and data extensions.[^s1]
- **Marketing Cloud Account Engagement** (formerly Pardot) is B2B marketing automation built around Engagement Studio, prospects and lists.[^s1]
- **Personalization**: Marketing Cloud Personalization (formerly Interaction Studio) handles real-time interaction management, and Salesforce Personalization is the Data 360-based option for Next.[^s1][^s2]
- **Marketing intelligence**: Marketing Cloud Intelligence (formerly Datorama) unifies and visualizes marketing performance data; Next has its own Marketing Intelligence add-on.[^s1][^s2]
- **Loyalty Management** is a cross-industry add-on for rewards and recognition programs that Trailhead lists alongside Next.[^s1][^s2]

Salesforce Help's marketing product index lists more than twenty entries in this space. Besides the main products, it lists Engagement's studios and builders (Email Studio, Mobile Studio, Content Builder, Contact Builder), Marketing Cloud Connect, Unified Messaging, advertising, referral marketing and real-time offer management.[^s2] Marketing Cloud Personalization combines behavioral tracking, affinity modeling, segmentation and automated recommendations across web, email and mobile.[^s4]

## How to choose within the portfolio

The main split is architectural. Next keeps data, automation and content on the core Salesforce platform, so admins work with familiar tools such as Flow and unified individuals, leads and contacts.[^s1] Engagement and Account Engagement are older stacks with their own data structures (data extensions in Engagement, prospects and lists in Account Engagement) and their own automation builders.[^s1] Salesforce's marketing site says existing Engagement and Account Engagement customers can use Next's AI capabilities without switching platforms.[^s3] So choosing a product is usually about where the data and the team already live, not just about features.

Watch the naming. Several products have been renamed, and the same capability can appear twice under different brands. Trailhead's unit lists both Salesforce Personalization and Marketing Cloud Personalization, and Help separates Marketing Intelligence in Next from Marketing Cloud Intelligence.[^s1][^s2] When you read documentation, a requirement or a license, confirm which product a name refers to before you design against it.

## Connections

The portfolio sits under `kt:customer-360`, with which Marketing Cloud Next integrates natively.[^s1] In this graph it is a sibling of the other product families, `kt:commerce-cloud` and `kt:sales-cloud`. It **has parts** `kt:marketing-cloud-next`, `kt:marketing-cloud-engagement`, `kt:marketing-cloud-account-engagement` and `kt:loyalty-management`, the products Trailhead groups under the umbrella.[^s1] It **depends on** `kt:data-cloud` (Data 360) as its data foundation and **integrates with** `kt:agentforce` for its agentic features.[^s3] It relates to `kt:journey-builder`, the visual automation tool at the heart of Engagement.[^s1][^s2]

## Sources
[^s1]: Trailhead, "Discover Salesforce Marketing Solutions". https://trailhead.salesforce.com/content/learn/modules/salesforce-marketing-cloud-quick-look/discover-salesforce-marketing-solutions (accessed 2026-11-19)
[^s2]: Salesforce Help, marketing products index. https://help.salesforce.com/s/products/marketing (accessed 2026-11-19)
[^s3]: Salesforce, "Marketing Cloud". https://www.salesforce.com/marketing/ (accessed 2026-11-19)
[^s4]: Trailhead, "Meet Interaction Studio". https://trailhead.salesforce.com/content/learn/modules/interaction-studio-basics/meet-interaction-studio (accessed 2026-11-19)
