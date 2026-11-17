---
id: kt:marketing-cloud-account-engagement
type: Product
title: Marketing Cloud Account Engagement
aliases: [Pardot, Salesforce Pardot, Account Engagement, MCAE]
domain: clouds-and-products
summary: >-
  Salesforce's B2B marketing automation product (formerly Pardot), built around prospects, scoring and
  grading, lists, automation rules and Engagement Studio programs, and synced to Sales Cloud leads,
  contacts and campaigns through the Salesforce connector and per-business-unit configuration.
release: "Winter '27"
status: current
broader: [kt:salesforce-marketing-solutions]
related: [kt:marketing-cloud-next, kt:lead-conversion]
relations:
  - {predicate: alternativeTo, object: kt:marketing-cloud-engagement}
  - {predicate: integratesWith, object: kt:sales-cloud}
  - {predicate: hasPart, object: kt:engagement-studio}
  - {predicate: dependsOn, object: kt:connected-apps}
sources:
  - id: s1
    title: "Discover Salesforce Marketing Solutions (Salesforce Marketing Cloud Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-marketing-cloud-quick-look/discover-salesforce-marketing-solutions
    type: official-learning
    accessed: 2026-11-17
  - id: s2
    title: "Get Started with Account Engagement Lightning (Account Engagement Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/pardot-basics-lightning/get-started-with-pardot-lightning
    type: official-learning
    accessed: 2026-11-17
  - id: s3
    title: "Plan Your Integration (Account Engagement and Salesforce Integration)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/pardot-salesforce-integration-for-lightning-app/plan-your-integration
    type: official-learning
    accessed: 2026-11-17
  - id: s4
    title: "Get Started with Lead Scoring (Lead Scoring and Grading in Account Engagement)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lead-scoring-and-grading-in-account-engagement/get-started-with-lead-scoring
    type: official-learning
    accessed: 2026-11-17
  - id: s5
    title: "Get Started with Lead Grading (Lead Scoring and Grading in Account Engagement)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lead-scoring-and-grading-in-account-engagement/get-started-with-lead-grading
    type: official-learning
    accessed: 2026-11-17
  - id: s6
    title: "Create an Engagement Studio Program (Engagement Studio)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/pardot-engagement-studio-lightning/create-an-engagement-studio-program-lightning
    type: official-learning
    accessed: 2026-11-17
  - id: s7
    title: "Marketing Cloud Account Engagement Pricing"
    publisher: Salesforce
    url: https://www.salesforce.com/in/editions-pricing/marketing-cloud/account-engagement/
    type: official-docs
    accessed: 2026-11-17
  - id: s8
    title: "Pardot Renamed Marketing Cloud Account Engagement"
    publisher: Salesforce Ben
    url: https://www.salesforceben.com/the-drip/pardot-renamed-marketing-cloud-account-engagement/
    type: community
    accessed: 2026-11-17
created: 2026-11-17
---

# Marketing Cloud Account Engagement

Marketing Cloud Account Engagement is Salesforce's B2B marketing automation product, known until 2022 as **Pardot**.[^s1][^s8] Salesforce announced the rename at World Tour Sydney in April 2022 as part of an effort to make Marketing Cloud product names more consistent; the product had earlier moved between the Marketing Cloud and Sales Cloud organizations.[^s8] It is aimed at companies whose marketing and sales teams work together to build pipeline, and it is built on the Salesforce platform so marketers and sellers can work in the same place rather than switching between systems.[^s2]

## How it works

The core record is the **prospect**. An anonymous website visitor becomes a prospect once they submit contact details through a form or landing page, and a prospect is broadly comparable to a Sales Cloud lead.[^s2] Account Engagement tracks prospect activity across websites, emails and forms, and uses it for lead nurturing, qualification and automatic assignment to sales reps.[^s2] Compared with its sibling products, it keeps prospects alongside CRM leads and contacts, segments with **lists**, and automates with **Engagement Studio**, **automation rules** and **completion actions**, where Marketing Cloud Engagement uses data extensions, Journey Builder and Automation Studio.[^s1]

Qualification combines two separate measures:

- **Score** measures implicit interest. Baseline scoring rules add preset points for actions such as email opens, form submissions or webinar attendance.[^s4]
- Only the point values of baseline rules can be edited; automation rules and completion actions add or subtract points on top, and scoring categories score per product line via content folders.[^s4]
- **Grade** measures explicit fit with the ideal customer profile, from F (worst) to A+ (best). Every prospect starts at D.[^s5]
- The default grading profile weighs company size, industry, location, job title and department, each adjusted in thirds of a letter grade; custom profiles can be assigned by automation rules.[^s5]

**Engagement Studio** programs send targeted emails based on prospect behavior. A program draws from a recipient list (minus a suppression list) and is built from actions, triggers and rules, each with yes and no branches, plus end steps. Programs have their own business-hours settings, can be tested in a simulator before launch, and must be paused before they are edited.[^s6]

## Salesforce integration

The connection to CRM runs through the **Salesforce connector**, which syncs prospect data with Salesforce leads and contacts. The connector is created paused, and an Account Engagement admin must configure and unpause it before anything syncs.[^s3] It runs as a connector user that needs system permissions such as API Enabled, plus object permissions on leads, contacts, accounts, opportunities, campaigns and campaign members (for example, View All and Modify All on leads and contacts).[^s3] Users reach the product through a Lightning app, which requires access to the Account Engagement connected app and the Sales Cloud User or CRM User permission set.[^s3]

**Business units** let one company run several Account Engagement setups, and each one needs its own Account Engagement admin. A Salesforce admin enables business units and assigns those admins, who don't need Salesforce admin rights.[^s3]

## Editions, limits and gotchas

Salesforce currently sells four editions, Growth+, Plus+, Advanced+ and Premium+, priced per org per month. Growth+ caps forms and landing pages at 50 each and automation rules at 50; higher editions add AI-powered scoring, B2B Marketing Analytics, business units and a dedicated IP address. Growth+, Plus+ and Advanced+ each list a Marketing Cloud Next edition, and Premium+ is described as including all capabilities.[^s7]

- Leads and contacts that exist only in Salesforce don't sync automatically; import them to establish the sync.[^s3]
- To limit which records sync, choose an appropriately permissioned connector user or set up Marketing Data Sharing before unpausing the connector.[^s3]
- Prospect scores can be edited by hand, but scoring-category scores cannot, and score resets are best used sparingly.[^s4]

## Connections

Account Engagement belongs to the **Salesforce marketing solutions** family.[^s1] It is the B2B **alternative to** Marketing Cloud Engagement, which runs on a separate platform, and is related to **Marketing Cloud Next**, which Salesforce now bundles into Account Engagement editions.[^s1][^s7] It **integrates with** Sales Cloud through the connector, **depends on** a connected app for user access, and **has part** Engagement Studio.[^s3][^s6] Its scoring and grading feed the qualification that precedes **lead conversion** in Sales Cloud.[^s2][^s4]

## Sources
[^s1]: Trailhead, "Discover Salesforce Marketing Solutions". https://trailhead.salesforce.com/content/learn/modules/salesforce-marketing-cloud-quick-look/discover-salesforce-marketing-solutions (accessed 2026-11-17)
[^s2]: Trailhead, "Get Started with Account Engagement Lightning". https://trailhead.salesforce.com/content/learn/modules/pardot-basics-lightning/get-started-with-pardot-lightning (accessed 2026-11-17)
[^s3]: Trailhead, "Plan Your Integration". https://trailhead.salesforce.com/content/learn/modules/pardot-salesforce-integration-for-lightning-app/plan-your-integration (accessed 2026-11-17)
[^s4]: Trailhead, "Get Started with Lead Scoring". https://trailhead.salesforce.com/content/learn/modules/lead-scoring-and-grading-in-account-engagement/get-started-with-lead-scoring (accessed 2026-11-17)
[^s5]: Trailhead, "Get Started with Lead Grading". https://trailhead.salesforce.com/content/learn/modules/lead-scoring-and-grading-in-account-engagement/get-started-with-lead-grading (accessed 2026-11-17)
[^s6]: Trailhead, "Create an Engagement Studio Program". https://trailhead.salesforce.com/content/learn/modules/pardot-engagement-studio-lightning/create-an-engagement-studio-program-lightning (accessed 2026-11-17)
[^s7]: Salesforce, "Marketing Cloud Account Engagement Pricing". https://www.salesforce.com/in/editions-pricing/marketing-cloud/account-engagement/ (accessed 2026-11-17)
[^s8]: Salesforce Ben, "Pardot Renamed Marketing Cloud Account Engagement". https://www.salesforceben.com/the-drip/pardot-renamed-marketing-cloud-account-engagement/ (accessed 2026-11-17)
