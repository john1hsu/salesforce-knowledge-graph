---
id: kt:collaborative-forecasts
type: Feature
title: Collaborative Forecasts
aliases: [Salesforce Forecasting, Sales Forecasting, Forecasts (Sales Cloud)]
domain: clouds-and-products
summary: >-
  Sales Cloud feature that rolls opportunity, product, split or schedule amounts up a role- or territory-based forecast
  hierarchy by forecast category and period, with quotas, owner and manager adjustments, and a Forecasts page for review.
release: "Winter '27"
status: current
broader: [kt:sales-cloud]
related: [kt:role-hierarchy, kt:opportunity-splits, kt:revenue-intelligence]
relations:
  - {predicate: partOf, object: kt:sales-cloud}
  - {predicate: dependsOn, object: kt:role-hierarchy}
  - {predicate: integratesWith, object: kt:enterprise-territory-management}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: coveredBy, object: kt:sales-cloud-consultant-certification}
sources:
  - id: s1
    title: "Collaborative Forecasts (Salesforce help PDF)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/242/latest/en-us/sfdc/pdf/forecasts.pdf
    type: official-docs
    accessed: 2026-11-05
  - id: s2
    title: "Configure Sales Forecasting in Salesforce"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/sales-forecasting/configure-sales-forecasting-in-salesforce
    type: official-learning
    accessed: 2026-11-05
  - id: s3
    title: "View and Set Sales Forecasts"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/it/content/learn/modules/sales-forecasting/view-and-set-sales-forecasts
    type: official-learning
    accessed: 2026-11-05
  - id: s4
    title: "Adjust Sales Projections in Collaborative Forecasts"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/introduction-to-revenue-intelligence-for-sales-cloud/adjust-forecasts
    type: official-learning
    accessed: 2026-11-05
  - id: s5
    title: "ForecastingItem (Object Reference)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.248.0.object_reference.meta/object_reference/sforce_api_objects_forecastingitem.htm
    type: official-docs
    accessed: 2026-11-05
  - id: s6
    title: "ForecastingSettings (Metadata API Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_forecastingsettings.htm
    type: official-docs
    accessed: 2026-11-05
created: 2026-11-05
---

# Collaborative Forecasts

Collaborative Forecasts is the Sales Cloud forecasting feature, shown in the app as **Forecasts**. It helps sales teams project revenue or quantity from pipeline through closed business. A forecast is a set of totals and subtotals of opportunities grouped by forecast category, rolled up through a forecast hierarchy for each forecast period.[^s1] Managers use it to review their team's numbers, make adjustments and present one collective forecast to leadership.[^s4]

## How it works

**Forecast types** decide what is measured. Each type sets a source object, revenue or quantity, a date measure, and a role or territory hierarchy. Filters can narrow a type, for example to separate new business from renewals. The default type forecasts opportunity amount by close date.[^s2] The guide lists four source objects. *Opportunity* can forecast amount, quantity, or a custom currency or number field. *Opportunity Product* forecasts total price or quantity by product family. *Opportunity Split* needs team selling and a revenue, overlay or custom split type. *Line Item Schedule* forecasts revenue or quantity by schedule date.[^s1] Up to **4** forecast types can be active at once.[^s1]

**The forecast hierarchy** is generated from the role hierarchy, but admins still choose which users forecast and who manages each level. Each user needs **Allow Forecasting** enabled on the user record, and each level has only one forecast manager.[^s1][^s2] Managers see and adjust the forecasts of the people one level below them.[^s2] A territory-based hierarchy is also available. It requires Enterprise Territory Management, uses only the active territory model, and rolls each opportunity into one territory forecast.[^s1]

**Forecast categories** come from opportunity stages. The categories are Pipeline, Best Case, Commit, Closed and Omitted, which is excluded from forecasts. Lightning adds an optional Most Likely category between Commit and Best Case. Admins can rename categories and change stage mappings.[^s1][^s2] The default **single-category** rollup totals each category separately. **Cumulative** rollups add later categories in, so Commit Forecast covers Commit plus Closed.[^s1][^s2]

**Quotas** are monthly or quarterly goals for a user or territory, by revenue, quantity or a custom measure. Admins enter them in Setup or load them with Data Loader or the API. Manager quotas don't roll up automatically.[^s1] With quota attainment turned on, the Forecasts page shows red, yellow and green progress bars per category.[^s3]

**Adjustments** let managers, owners or both override a total without editing opportunities. They need the Override Forecasts permission, and each forecast type keeps its own adjustments.[^s1][^s2] Trailhead says to use them for things like a rep's habitual over- or under-estimate or a market shift. If a deal's scope changes, update the opportunity instead.[^s3] Optional extras include forecast submissions, manager judgments, custom columns such as commit coverage, and custom Forecasts pages built in Lightning App Builder.[^s2]

## Limits and gotchas

- Periods are monthly or quarterly. The default range is 3 months, and the maximum is 15 months, 15 fiscal periods or 8 quarters.[^s1]
- Changing the period type or the standard fiscal year purges all quotas and adjustments. Creating the first custom fiscal year deletes them for that year and later years.[^s1]
- Switching between single-category and cumulative rollups deletes adjustments for every active forecast type. Deactivating a forecast type deletes its forecast data.[^s1]
- The product-family grid shows at most 2,000 rows.[^s1]
- A role's reporting line does not set someone's forecast manager. Update the forecast hierarchy whenever roles change.[^s1][^s2]
- These limits come from an older help PDF edition. Confirm them in current Help before designing close to them.[^s1]

## Data and reporting

Forecast data is held in objects such as **ForecastingItem**. It is a read-only object, available since API version 26.0, that exposes amounts with and without adjustments: ForecastAmount, AmountWithoutAdjustments, AmountWithoutManagerAdjustment and OwnerOnlyAmount, plus quantity equivalents.[^s5] Custom report types can be built on forecasting items and forecasting quotas.[^s1] Forecast settings are deployed as the `ForecastingSettings` metadata type.[^s6] With Historical Trending on, arrows show how values changed over the last seven days.[^s3]

## When to use it

Use Collaborative Forecasts when a sales organization commits numbers up a management chain and needs category rollups, quota attainment and an audit of adjustments. Einstein Forecasting adds AI predictions to the same page. It needs Unlimited Edition or the Sales Cloud Einstein add-on.[^s3] Revenue Intelligence comes before it in the workflow: teams inspect the pipeline first, then finalise numbers in Forecasts.[^s4]

## Connections

Collaborative Forecasts is **part of** `kt:sales-cloud`.[^s1] Its default hierarchy **depends on** `kt:role-hierarchy`, and territory forecasts **integrate with** `kt:enterprise-territory-management`.[^s1][^s2] It is related to `kt:opportunity-splits`, which split forecast types rely on.[^s1] It is also related to `kt:revenue-intelligence`, whose pipeline inspection leads into forecast adjustment.[^s4] Settings are **configured via** `kt:metadata-api` as ForecastingSettings,[^s6] and forecast data is **queried with** `kt:soql` against objects such as ForecastingItem.[^s5] The topic is **covered by** `kt:sales-cloud-consultant-certification`.

## Sources

[^s1]: Salesforce, "Collaborative Forecasts (Salesforce help PDF)". https://resources.docs.salesforce.com/242/latest/en-us/sfdc/pdf/forecasts.pdf (accessed 2026-11-05)
[^s2]: Trailhead, "Configure Sales Forecasting in Salesforce". https://trailhead.salesforce.com/content/learn/modules/sales-forecasting/configure-sales-forecasting-in-salesforce (accessed 2026-11-05)
[^s3]: Trailhead, "View and Set Sales Forecasts". https://trailhead.salesforce.com/it/content/learn/modules/sales-forecasting/view-and-set-sales-forecasts (accessed 2026-11-05)
[^s4]: Trailhead, "Adjust Sales Projections in Collaborative Forecasts". https://trailhead.salesforce.com/content/learn/modules/introduction-to-revenue-intelligence-for-sales-cloud/adjust-forecasts (accessed 2026-11-05)
[^s5]: Salesforce, "ForecastingItem (Object Reference)". https://developer.salesforce.com/docs/atlas.en-us.248.0.object_reference.meta/object_reference/sforce_api_objects_forecastingitem.htm (accessed 2026-11-05)
[^s6]: Salesforce, "ForecastingSettings (Metadata API Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_forecastingsettings.htm (accessed 2026-11-05)
