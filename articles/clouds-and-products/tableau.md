---
id: kt:tableau
type: Product
title: Tableau
aliases: [Tableau Software, Tableau by Tableau]
domain: clouds-and-products
summary: >-
  Salesforce's analytics and visualization brand, acquired in 2019, spanning the original "Tableau by Tableau"
  portfolio (Desktop, Cloud, Server, Prep, Pulse) and the Salesforce-native Tableau Next platform built on
  Data 360 with the Tableau Semantics layer and Agentforce skills.
release: "Winter '27"
status: current
broader: [kt:salesforce-analytics]
related: [kt:data-cloud, kt:agentforce, kt:sales-cloud, kt:service-cloud]
relations:
  - {predicate: hasPart, object: kt:tableau-next}
  - {predicate: hasPart, object: kt:tableau-pulse}
  - {predicate: hasPart, object: kt:tableau-semantics}
  - {predicate: integratesWith, object: kt:einstein-trust-layer}
  - {predicate: alternativeTo, object: kt:crm-analytics}
  - {predicate: acquiredBy, object: kt:salesforce-inc}
sources:
  - id: s1
    title: "Tableau's Products and Features"
    publisher: Tableau (Salesforce)
    url: https://help.tableau.com/current/online/en-us/tableau_next_tableau_product_overview.htm
    type: official-docs
    accessed: 2026-11-04
  - id: s2
    title: "Tableau Next Features Overview"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/analytics/tableau-next-isv-dev/guide/tn-features-overview.html
    type: official-docs
    accessed: 2026-11-04
  - id: s3
    title: "Redefine Data Analytics with Tableau Next (Tableau Next Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/tableau-next-quick-look/redefine-data-analytics-with-tableau-next
    type: official-learning
    accessed: 2026-11-04
  - id: s4
    title: "Technical Considerations for Migrating from Tableau Server to Tableau Cloud"
    publisher: Tableau (Salesforce)
    url: https://help.tableau.com/current/server/en-us/migrate_server_to_cloud_overview.htm
    type: official-docs
    accessed: 2026-11-04
  - id: s5
    title: "Salesforce Completes Exchange Offer for Tableau Common Stock"
    publisher: Salesforce Investor Relations
    url: https://investor.salesforce.com/news/news-details/2019/Salesforce-Completes-Exchange-Offer-for-Tableau-Common-Stock/default.aspx
    type: news
    accessed: 2026-11-04
created: 2026-11-04
---

# Tableau

Tableau is the analytics and data-visualization brand inside the Salesforce portfolio. Salesforce completed its acquisition of Tableau Software on August 1, 2019, when a second-step merger made Tableau a wholly owned subsidiary.[^s5] Today the name covers two distinct product lines: the original portfolio, which Tableau's own documentation now calls "Tableau by Tableau", and the Salesforce-native Tableau Next platform. They are separate products with separate licenses, so an architect must always clarify which one a requirement means.[^s1]

## The two product lines

**Tableau by Tableau.** Tableau Desktop is the original authoring tool and can publish workbooks and data sources to Tableau Cloud (hosted, browser-based authoring and sharing) or Tableau Server (the self-managed, on-premises counterpart). Tableau Prep Builder creates data-preparation flows, and Prep Conductor schedules published flows on Cloud or Server. Around these sit Tableau Pulse (metrics delivered into tools such as Slack and email, now bundled with Cloud), Tableau Agent (an AI assistant for building and interpreting visualizations), Tableau Catalog (lineage and data-quality warnings) and Tableau Bridge (connectivity from Cloud to non-cloud data). Users are licensed as Viewer, Explorer or Creator.[^s1]

**Tableau Next.** Tableau Next is an agentic analytics platform built on the Salesforce code base. It runs on Data 360 (Data Cloud), includes the Tableau Semantics layer, adds Agentforce analysis skills such as Concierge, Data Pro and Inspector, and is licensed separately as Creator or Consumer. The Tableau+ bundle (Cloud only) packages Viewer/Explorer/Creator licenses with Data 360 credits and Tableau Next.[^s1] Its building blocks are workspaces, which hold data connections, a semantic model builder, a metric creator and visualization tools; semantic models, which are first-class Salesforce metadata that map data to business terms; visualizations; and dashboards that can be templated and distributed through Marketplace.[^s2] Trailhead frames it as an API-first, composable platform whose semantic layer lets both people and AI agents understand the same business data.[^s3]

## Limits and gotchas

Hosting choice matters for Tableau by Tableau. On Tableau Cloud, Tableau runs the environment on AWS in a region you choose and MFA is required for all users; direct Active Directory, LDAP and Kerberos authentication are not supported, so you integrate through SAML or OIDC instead. On-premises or private-network data reaches Cloud only through Bridge, which cannot hold live connections to files, run Prep Conductor flows, or serve analytics extensions. Cube data sources, Connector SDK custom connectors, guest users and server-level REST administration are also unavailable in Cloud, and site capacity limits cover storage and tasks.[^s4] Tableau's migration guidance also warns that embedded extracts that run past roughly ten minutes risk timeouts, and recommends publishing and refreshing data sources separately.[^s4] Tableau Public and Tableau Reader have no governance, so they are unsuitable for sensitive data.[^s1]

## When to use it (and when not)

Choose Tableau by Tableau for broad, multi-source enterprise BI, especially where much of the data lives outside Salesforce or where Server-based deployment is required.[^s1][^s4] Consider Tableau Next when analytics should sit inside Salesforce workflows, share a governed semantic model with Data 360, and feed Agentforce agents with business context; it requires Data 360 and a separate license.[^s1][^s3] Standard Salesforce reports and dashboards remain the lighter option for simple operational reporting on CRM records.

## Connections

Tableau sits under `kt:salesforce-analytics` and was brought in by acquisition (`acquiredBy kt:salesforce-inc`).[^s5] It `hasPart` Tableau Next, Tableau Pulse and Tableau Semantics, the Salesforce-native layers described above.[^s1] Tableau Next depends on `kt:data-cloud` (Data 360) and adds `kt:agentforce` analysis skills; the `kt:einstein-trust-layer` node covers how AI in Tableau is governed from the trust side.[^s1][^s3] It is commonly weighed against `kt:crm-analytics`, whose capabilities the product overview says were combined into Tableau Next.[^s1] Pulse for Salesforce surfaces metrics inside `kt:sales-cloud` and `kt:service-cloud` CRM workflows.[^s1]

## Sources
[^s1]: Tableau (Salesforce), "Tableau's Products and Features". https://help.tableau.com/current/online/en-us/tableau_next_tableau_product_overview.htm (accessed 2026-11-04)
[^s2]: Salesforce Developers, "Tableau Next Features Overview". https://developer.salesforce.com/docs/analytics/tableau-next-isv-dev/guide/tn-features-overview.html (accessed 2026-11-04)
[^s3]: Trailhead, "Redefine Data Analytics with Tableau Next". https://trailhead.salesforce.com/content/learn/modules/tableau-next-quick-look/redefine-data-analytics-with-tableau-next (accessed 2026-11-04)
[^s4]: Tableau (Salesforce), "Technical Considerations for Migrating from Tableau Server to Tableau Cloud". https://help.tableau.com/current/server/en-us/migrate_server_to_cloud_overview.htm (accessed 2026-11-04)
[^s5]: Salesforce Investor Relations, "Salesforce Completes Exchange Offer for Tableau Common Stock" (2019). https://investor.salesforce.com/news/news-details/2019/Salesforce-Completes-Exchange-Offer-for-Tableau-Common-Stock/default.aspx (accessed 2026-11-04)
