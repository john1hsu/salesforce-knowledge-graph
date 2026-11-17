---
id: kt:salesforce-analytics
type: Concept
title: Salesforce Analytics
aliases: [Salesforce analytics portfolio, Analytics (Salesforce Help product area)]
domain: clouds-and-products
summary: >-
  The umbrella for Salesforce's analytics offerings: built-in Reports and Dashboards on the core platform,
  CRM Analytics, the Tableau family (including the Data 360-based Tableau Next) and Tableau Semantics. Choosing
  among these layers is a recurring architecture decision about data scope, licensing and where insights surface.
release: "Winter '27"
status: concept
broader: [kt:salesforce-platform]
related: [kt:data-cloud, kt:calculated-insights, kt:agentforce, kt:salesforce-sharing-model]
relations:
  - {predicate: hasPart, object: kt:reports-and-dashboards}
  - {predicate: hasPart, object: kt:crm-analytics}
  - {predicate: hasPart, object: kt:tableau}
  - {predicate: hasPart, object: kt:tableau-next}
  - {predicate: hasPart, object: kt:tableau-semantics}
sources:
  - id: s1
    title: "Analytics (Salesforce Help product page)"
    publisher: Salesforce
    url: https://help.salesforce.com/s/products/analytics
    type: official-docs
    accessed: 2026-11-17
  - id: s2
    title: "Analyze Your Data with Reports and Dashboards (Lightning Experience Productivity)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lightning-experience-productivity/analyze-your-data-with-reports-and-dashboards
    type: official-learning
    accessed: 2026-11-17
  - id: s3
    title: "Reports and Dashboards REST API: Requirements and Limitations"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_analytics.meta/api_analytics/sforce_analytics_rest_api_limits_limitations.htm
    type: official-docs
    accessed: 2026-11-17
  - id: s4
    title: "CRM Analytics (Salesforce Help)"
    publisher: Salesforce
    url: https://help.salesforce.com/HTViewHelpDoc?id=bi.htm
    type: official-docs
    accessed: 2026-11-17
  - id: s5
    title: "Tableau Next Features Overview"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/analytics/tableau-next-isv-dev/guide/tn-features-overview.html
    type: official-docs
    accessed: 2026-11-17
  - id: s6
    title: "All Analytics Products"
    publisher: Salesforce
    url: https://salesforce.com/analytics/all-products
    type: official-blog
    accessed: 2026-11-17
created: 2026-11-17
---

# Salesforce Analytics

"Salesforce Analytics" is not one product but the family of analytics capabilities Salesforce sells and documents together. The Analytics area of Salesforce Help currently groups six entries: Reports and Dashboards, CRM Analytics, Tableau Next, Tableau, Tableau Semantics and a CSI Score feature in beta.[^s1] Salesforce's marketing catalogue draws the circle wider, listing Tableau, Tableau Pulse, embedded analytics, Tableau Exchange, CRM Analytics, Revenue Intelligence, Data 360, Marketing Analytics and Sales Analytics, while treating reports and dashboards as a built-in platform feature rather than a separate product.[^s6] For a practitioner the useful view is a set of layers, each with a different data scope, license and place where insight appears.

## The layers

**Reports and Dashboards (included with the platform).** Reports answer operational questions such as pipeline or open cases. The report type chosen decides which objects and fields are available, and the builder supports filters, row and column groupings, bucket columns, formulas, subtotals and an embedded chart.[^s2] A dashboard is assembled from saved reports: each widget renders one source report as a table, chart or metric, and charts and metrics need a source report with at least one grouping.[^s2] Dashboards add dashboard-wide filters, "view as" settings, drill-through into filtered reports, feeds (once an admin enables feed tracking) and scheduled email subscriptions.[^s2]

**CRM Analytics (licensed add-on).** Help describes it as a cloud platform that connects data from several sources, builds interactive views and shares them in apps, with Einstein Discovery supplying statistical models and predictions.[^s4] It reaches back into the core layer, since datasets and trending dashboards can be built from Salesforce reports and Lightning reports can be queried directly on CRM Analytics dashboards. It also reaches outward: Tableau views can be published into it, and a Metadata Bridge helps carry its assets into Tableau Next semantic models.[^s4]

**Tableau and Tableau Next.** Salesforce calls Tableau its flagship analytics platform for enterprise-wide exploration and frames Tableau and CRM Analytics as complementary: Tableau for broad analysis, CRM Analytics for insight inside CRM workflows.[^s6] Tableau Next is the newer, API-first layer built on the Data 360 semantic layer. Analysts work in workspaces that hold data connections, a semantic model builder, a metric creator and visualization tools, and it integrates with Agentforce AI.[^s5] Tableau Semantics, which maps data to shared business terms, is listed as its own Help product because those models are reusable across Data 360.[^s1][^s5]

## Limits and gotchas

The built-in layer has firm ceilings that shape design. Through the Reports and Dashboards REST API a report run returns at most 2,000 rows and 100 columns, with no more than 20 custom field filters.[^s3] Orgs get 500 synchronous runs per hour (20 at a time) and 1,200 asynchronous run requests per hour, and async results are kept for a rolling 24 hours.[^s3] Dashboard refreshes are capped at 200 per hour per org, and each user may hold at most 5 report subscriptions.[^s3] Cross filters, standard report filters and row-limit filters cannot be set through the API, and historical tracking reports work only in matrix format and cannot be subscribed to.[^s3] On the UI side, changes made while reading a report are lost unless saved, and missing groupings silently block charts.[^s2]

The higher layers trade those ceilings for licensing and data movement. CRM Analytics and Tableau Next each need their own licenses, and Tableau Next depends on Data 360 as its data foundation.[^s4][^s5] Because names have shifted over the years, check which product a requirement means: "Tableau" alone may refer to the original Desktop/Cloud/Server line or to Tableau Next.

## When to use which

Start with Reports and Dashboards when the question is about CRM records in one org, the row counts are modest and users live in Lightning pages.[^s2][^s3] Move to CRM Analytics when you need blended datasets, predictions or analytics embedded in CRM workflows at volumes that standard reports cannot handle.[^s4][^s6] Choose Tableau for enterprise-wide analysis across many non-Salesforce sources, and Tableau Next when a governed semantic model in Data 360 should serve both people and Agentforce agents.[^s5][^s6] Salesforce says it is building more interoperability between Tableau and CRM Analytics, so mixed estates are common and the layers are not mutually exclusive.[^s6]

## Connections

This node sits under `kt:salesforce-platform` and `hasPart` each layer: `kt:reports-and-dashboards`, `kt:crm-analytics`, `kt:tableau`, `kt:tableau-next` and `kt:tableau-semantics`.[^s1] It is `related` to `kt:data-cloud` (Data 360), whose semantic layer underpins Tableau Next, and to `kt:calculated-insights`, the Data 360 way of computing metrics before they reach a dashboard.[^s5] `kt:agentforce` appears because Tableau Next integrates Agentforce AI.[^s5] `kt:salesforce-sharing-model` is listed as a design input, since deciding who should see which numbers is part of choosing a layer; dashboards expose this directly through their "view as" setting.[^s2]

## Sources
[^s1]: Salesforce, "Analytics (Salesforce Help product page)". https://help.salesforce.com/s/products/analytics (accessed 2026-11-17)
[^s2]: Trailhead, "Analyze Your Data with Reports and Dashboards". https://trailhead.salesforce.com/content/learn/modules/lightning-experience-productivity/analyze-your-data-with-reports-and-dashboards (accessed 2026-11-17)
[^s3]: Salesforce Developers, "Reports and Dashboards REST API: Requirements and Limitations". https://developer.salesforce.com/docs/atlas.en-us.api_analytics.meta/api_analytics/sforce_analytics_rest_api_limits_limitations.htm (accessed 2026-11-17)
[^s4]: Salesforce, "CRM Analytics (Salesforce Help)". https://help.salesforce.com/HTViewHelpDoc?id=bi.htm (accessed 2026-11-17)
[^s5]: Salesforce Developers, "Tableau Next Features Overview". https://developer.salesforce.com/docs/analytics/tableau-next-isv-dev/guide/tn-features-overview.html (accessed 2026-11-17)
[^s6]: Salesforce, "All Analytics Products". https://salesforce.com/analytics/all-products (accessed 2026-11-17)
