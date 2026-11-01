---
id: kt:sales-cloud
type: Product
title: Sales Cloud
aliases: [Agentforce Sales, Salesforce Sales Cloud]
domain: clouds-and-products
summary: >-
  Salesforce's sales CRM product, now marketed as Agentforce Sales, built around the Lead, Account, Contact and
  Opportunity objects, with guided selling (Path, Kanban), pipeline reporting and forecasting on top of the core platform.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:service-cloud, kt:role-hierarchy, kt:flow-builder, kt:lead-conversion]
relations:
  - {predicate: hasPart, object: kt:collaborative-forecasts}
  - {predicate: hasPart, object: kt:opportunity-splits}
  - {predicate: integratesWith, object: kt:agentforce}
  - {predicate: integratesWith, object: kt:enterprise-territory-management}
  - {predicate: coveredBy, object: kt:sales-cloud-consultant-certification}
sources:
  - id: s1
    title: "Get to Know the Sales Cloud Platform (Sales Cloud Platform Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/sales-cloud-platform-quick-look/get-to-know-the-sales-cloud-platform
    type: official-learning
    accessed: 2026-11-01
  - id: s2
    title: "Create and Convert Leads as Potential Customers"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/leads_opportunities_lightning_experience/create-and-convert-leads-lightning
    type: official-learning
    accessed: 2026-11-01
  - id: s3
    title: "Work with Leads and Opportunities (Lightning Experience tour)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/lex_salesforce_tour/lex_salesforce_tour_sales
    type: official-learning
    accessed: 2026-11-01
  - id: s4
    title: "Review Your Collaborative Forecasts Setup (Revenue Intelligence Setup)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/zh-CN/content/learn/modules/revenue-intelligence-setup/review-your-collaborative-forecasts-setup
    type: official-learning
    accessed: 2026-11-01
  - id: s5
    title: "Forecasts (Salesforce Help PDF, latest release)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/forecasts.pdf
    type: official-docs
    accessed: 2026-11-01
  - id: s6
    title: "Manage Leads and Sales Pipelines (Sales for Small Business)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/fr/content/learn/modules/sales-for-small-business/manage-leads-and-sales-pipelines
    type: official-learning
    accessed: 2026-11-01
created: 2026-11-01
---

# Sales Cloud

Sales Cloud is Salesforce's CRM product for sales teams. Salesforce's own learning content now calls it **Agentforce Sales (formerly Sales Cloud)**, and notes that it is so widely used that people often say "Salesforce" when they mean this product.[^s1] Treat the two names as the same node. Salesforce positions it as one place for customer data, lead alerts, real-time reports, mobile deal work and built-in AI and automation, running the sales organization "from pipeline to paycheck".[^s1]

## How it works: the lead-to-opportunity model

The data model rests on four standard objects. A **Lead** is a person or company that has shown interest but is not yet qualified. Leads come from referrals, web forms (**Web-to-Lead**), partners, ads, events and imports.[^s2] Companies often route new leads automatically, by geography or territory, or drop them into a queue, using assignment logic the admin configures.[^s2]

When a lead qualifies, the rep **converts** it. Conversion creates a business **Account** from the company name, a **Contact** from the person's name, and an **Opportunity**. The rep can attach the lead to an existing account or contact instead of creating new ones.[^s2][^s3] An **Opportunity** is a real deal with an amount, stage, close date and probability.[^s2] Accounts are the companies you sell to and Contacts are the people at them; contact roles link those people to deals.[^s3]

## Guided selling and pipeline

Lightning record pages for leads and opportunities center on **Path**, which shows the stages of your sales process with coaching at each step, such as discovery questions at Needs Analysis or price-objection tips at Proposal.[^s3] A composer logs calls, meetings and tasks, and an activity timeline shows history and next steps.[^s3] **Kanban** views group opportunities by a field such as stage; dragging a card updates the record, and opportunity alerts flag deals with no recent activity.[^s3]

Stages such as prospecting, qualification, proposal and negotiation make up the **pipeline**. Prebuilt reports and dashboards show deal size, win rate, cycle length and conversion counts.[^s6] In the small-business editions, forecasting is not included in Starter; Pro Suite adds a forecast dashboard that projects revenue from deal movement.[^s6]

## Forecasting

Full forecasting is **Collaborative Forecasts**, which newer Help content calls pipeline forecasting. Forecasts are totals of opportunities by **forecast category** (Pipeline, Best Case, Commit, Omitted, Closed), rolled up by hierarchy and period. Managers and reps can apply adjustments without changing the underlying records.[^s5] A **forecast type** combines an object, a measure (such as Amount), a date field and a hierarchy, with optional filters such as renewals only.[^s4] Types can be built on Opportunity, Opportunity Product, Opportunity Split or Line Item Schedule.[^s5] The forecast hierarchy comes from the role hierarchy, or from the territory hierarchy for territory forecasts.[^s5]

## Limits and gotchas

- Only **four forecast types** can be active at a time; more require a request to Salesforce Customer Support.[^s5][^s4]
- Users must be **enabled in the forecast hierarchy** even if they already sit in the role hierarchy, and each level needs a forecast manager.[^s4][^s5]
- Changing the rollup setting **deletes existing adjustments** for all active forecast types, and changing the date range can delete data.[^s4]
- Territory forecasts work only for the **active territory model**.[^s5]
- With person accounts enabled, a lead with no company name converts to a **person account**, not a business account.[^s2]
- Conversion appends the account name to the opportunity name; Trailhead shows using Flow Builder to standardize names.[^s2]
- Split forecasts need team selling and opportunity splits enabled; overlay splits need not total 100%.[^s5]

## When to use it (and when not)

Use Sales Cloud when the business runs a qualified-lead and deal pipeline that managers must forecast against quota. For small teams, the Starter and Pro suites give leads, pipeline reports and (in Pro) a forecast dashboard with less setup.[^s6] Teams whose main work is support cases belong in Service Cloud; the two share Accounts and Contacts on the same platform.[^s3]

## Connections

Sales Cloud sits under `kt:salesforce-platform` and is a sibling of `kt:service-cloud`, sharing the account and contact model.[^s3] It **has parts** `kt:collaborative-forecasts` and `kt:opportunity-splits`.[^s4][^s5] Forecast rollups depend on `kt:role-hierarchy`, and territory forecasts **integrate with** `kt:enterprise-territory-management`.[^s5] It is related to `kt:lead-conversion`, its key data transition, and to `kt:flow-builder`, used to automate steps such as opportunity naming.[^s2] It **integrates with** `kt:agentforce`, whose built-in AI the product is now named after.[^s1] Practitioner skills are **covered by** `kt:sales-cloud-consultant-certification`.

## Sources

[^s1]: Trailhead, "Get to Know the Sales Cloud Platform". https://trailhead.salesforce.com/content/learn/modules/sales-cloud-platform-quick-look/get-to-know-the-sales-cloud-platform (accessed 2026-11-01)
[^s2]: Trailhead, "Create and Convert Leads as Potential Customers". https://trailhead.salesforce.com/content/learn/modules/leads_opportunities_lightning_experience/create-and-convert-leads-lightning (accessed 2026-11-01)
[^s3]: Trailhead, "Work with Leads and Opportunities". https://trailhead.salesforce.com/lex_salesforce_tour/lex_salesforce_tour_sales (accessed 2026-11-01)
[^s4]: Trailhead, "Review Your Collaborative Forecasts Setup". https://trailhead.salesforce.com/zh-CN/content/learn/modules/revenue-intelligence-setup/review-your-collaborative-forecasts-setup (accessed 2026-11-01)
[^s5]: Salesforce, "Forecasts" (Help PDF). https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/forecasts.pdf (accessed 2026-11-01)
[^s6]: Trailhead, "Manage Leads and Sales Pipelines". https://trailhead.salesforce.com/fr/content/learn/modules/sales-for-small-business/manage-leads-and-sales-pipelines (accessed 2026-11-01)
