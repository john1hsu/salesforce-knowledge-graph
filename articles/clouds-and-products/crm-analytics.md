---
id: kt:crm-analytics
type: Product
title: CRM Analytics
aliases: [Tableau CRM, Einstein Analytics, Salesforce CRM Analytics]
domain: clouds-and-products
summary: >-
  Salesforce's platform-native analytics product (formerly Einstein Analytics, then Tableau CRM): it syncs Salesforce
  and external data into datasets via Data Sync, recipes and dataflows, queries them with SAQL, and surfaces lenses,
  dashboards, templated apps and Einstein Discovery predictions inside Salesforce workflows.
release: "Winter '27"
status: current
broader: [kt:salesforce-analytics]
related: [kt:event-monitoring, kt:sales-cloud, kt:service-cloud, kt:salesforce-sharing-model, kt:experience-cloud]
relations:
  - {predicate: hasPart, object: kt:einstein-discovery}
  - {predicate: queriedWith, object: kt:saql}
  - {predicate: alternativeTo, object: kt:tableau}
  - {predicate: integratesWith, object: kt:data-cloud}
  - {predicate: dependsOn, object: kt:salesforce-sharing-model}
sources:
  - id: s1
    title: "CRM Analytics (Salesforce Help)"
    publisher: Salesforce
    url: https://help.salesforce.com/HTViewHelpDoc?id=bi.htm
    type: official-docs
    accessed: 2026-11-07
  - id: s2
    title: "CRM Analytics Developer Center"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/developer-centers/crm-analytics
    type: official-docs
    accessed: 2026-11-07
  - id: s3
    title: "Set Up CRM Analytics App Licenses and Permissions"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/wave_apps_basics/wave_apps_setting_up_wave_app_licenses_and_permissions
    type: official-learning
    accessed: 2026-11-07
  - id: s4
    title: "SAQL Overview (SAQL Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/analytics/bi-dev-guide-saql/guide/bi-saql-intro.html
    type: official-docs
    accessed: 2026-11-07
  - id: s5
    title: "'CRM Analytics' Salesforce's new name for Tableau CRM"
    publisher: TechTarget
    url: https://www.techtarget.com/searchcustomerexperience/news/252515840/CRM-Analytics-Salesforces-new-name-for-Tableau-CRM
    type: news
    accessed: 2026-11-07
  - id: s6
    title: "CRM Analytics: Data Security to Control Access to Rows"
    publisher: Automation Champion
    url: https://automationchampion.com/2022/11/07/data-security-to-control-access-to-rows/
    type: community
    accessed: 2026-11-07
created: 2026-11-07
---

# CRM Analytics

CRM Analytics is Salesforce's cloud analytics platform for connecting data from several sources, building interactive views over it and sharing those views as apps, so that business users can act on insights as data changes.[^s1] Unlike an external BI tool, it runs inside the Salesforce org: dashboards embed in Lightning pages and Experience Cloud sites, and its prebuilt apps put analysis directly into sales and service workflows.[^s1][^s2]

The product has carried several names. It launched as Einstein Analytics, was rebranded Tableau CRM in late 2020, and became CRM Analytics in April 2022 alongside the Summer '22 release; Salesforce said the new name signals that it is built natively for CRM users, in line with naming products by function rather than by acquired brand.[^s5] Older docs, metadata and Trailhead URLs (including the original "Wave" module paths) still use the earlier names.[^s3][^s5]

## How it works

**Data layer.** Data reaches CRM Analytics through Data Sync (replication of Salesforce objects and external connections), data prep recipes, the older dataflows, and CSV or External Data API uploads; the output is a *dataset*, a compressed, query-optimized store separate from the transactional org.[^s1][^s2] The Recipe REST API exposes data prep programmatically and is shared with Data Cloud and Salesforce Data Pipelines.[^s2]

**Query and visualization layer.** Users explore a dataset in a *lens* for ad hoc questions, then assemble *dashboards* for ongoing monitoring and *collections* to organize insights.[^s1] Under the hood, every lens, dashboard and explorer action generates and runs a SAQL (Salesforce Analytics Query Language) query; developers can write SAQL directly in dashboard JSON, compare tables, the REST API and dataflow transformations.[^s4] A separate SQL for CRM Analytics dialect supports sharing inheritance and custom fiscal calendars.[^s2] Dashboards can be customized through the designer, dashboard JSON, extended metadata (XMD) for field formatting, and Lightning web components.[^s2]

**Apps and prediction.** Intelligent analytics apps are curated, purpose-built sets of dashboards for specific business areas, and templates let a team package an app built on one org's data so others can recreate it on theirs.[^s1][^s2] Einstein Discovery adds statistical modeling and machine learning that predicts outcomes and recommends improvements; deployed models can be embedded through the Einstein Discovery REST API.[^s1][^s2]

**Tooling.** Builders work in Analytics Studio and Data Manager, and source-driven teams use the Analytics CLI plugin for Salesforce DX with VS Code.[^s2]

## Licensing and security gotchas

No CRM Analytics permission set can be assigned until the org buys a license, either CRM Analytics Growth or CRM Analytics Plus.[^s3] The Plus license ships User and Admin permission sets; the Admin set adds permissions such as Manage CRM Analytics, Manage Einstein Discovery, Download CRM Analytics Data and Edit Dataset Recipes.[^s3] Einstein Discovery specifically requires CRM Analytics Plus or an Einstein Predictions license.[^s1] App access is granted separately (Viewer, Editor or Manager) by sharing the app in Analytics Studio.[^s3]

The biggest architectural gotcha is that datasets do not automatically honor org record access. By default, anyone who can open a dataset sees all of its rows and fields, so row-level security must be added per dataset.[^s6] Two mechanisms exist: *security predicates*, filter expressions (by owner, role hierarchy, territory, team or a custom user field) evaluated whenever a user queries the dataset, and *sharing inheritance*, which applies a source object's Salesforce sharing to the dataset and is supported for Accounts, Cases, Contacts, Leads and Opportunities.[^s6] The Integration User that syncs data has view-all access by default, so sensitive objects or fields must be removed from its profile.[^s6]

## When to use it (and when not)

Choose CRM Analytics when the analysis is mainly Salesforce data, users live in Salesforce, and you need embedded dashboards, prebuilt Sales or Service apps, or Einstein Discovery predictions in the flow of work.[^s1][^s3] When the data and audiences extend well beyond the CRM, the separately branded Tableau portfolio is the usual comparison point, a distinction Salesforce drew deliberately when it dropped the Tableau name from this product.[^s5] Because datasets are copies, plan refresh schedules and row-level security as first-class design decisions rather than afterthoughts.[^s6]

## Connections

CRM Analytics sits under the Salesforce analytics portfolio and is the native **alternative to Tableau**.[^s5] It **has part** Einstein Discovery and is **queried with** SAQL.[^s1][^s4] Its Recipe REST API is shared with **Data Cloud**, so data prep skills and integrations carry across.[^s2] It is **related** to Event Monitoring; that node describes how its daily log files load into an analytics app. Row-level access is **governed by** the Salesforce sharing model through predicates and sharing inheritance.[^s6] Its prebuilt apps target **Sales Cloud** and **Service Cloud**, and dashboards embed in **Experience Cloud** sites.[^s1][^s3]

## Sources

[^s1]: Salesforce, "CRM Analytics (Salesforce Help)". https://help.salesforce.com/HTViewHelpDoc?id=bi.htm (accessed 2026-11-07)
[^s2]: Salesforce Developers, "CRM Analytics Developer Center". https://developer.salesforce.com/developer-centers/crm-analytics (accessed 2026-11-07)
[^s3]: Trailhead, "Set Up CRM Analytics App Licenses and Permissions". https://trailhead.salesforce.com/content/learn/modules/wave_apps_basics/wave_apps_setting_up_wave_app_licenses_and_permissions (accessed 2026-11-07)
[^s4]: Salesforce Developers, "SAQL Overview (SAQL Developer Guide)". https://developer.salesforce.com/docs/analytics/bi-dev-guide-saql/guide/bi-saql-intro.html (accessed 2026-11-07)
[^s5]: TechTarget, "'CRM Analytics' Salesforce's new name for Tableau CRM". https://www.techtarget.com/searchcustomerexperience/news/252515840/CRM-Analytics-Salesforces-new-name-for-Tableau-CRM (accessed 2026-11-07)
[^s6]: Automation Champion, "CRM Analytics: Data Security to Control Access to Rows". https://automationchampion.com/2022/11/07/data-security-to-control-access-to-rows/ (accessed 2026-11-07)
