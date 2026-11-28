---
id: kt:saql
type: Language
title: SAQL
aliases: [Salesforce Analytics Query Language, SAQL query, SAQL queries, CRM Analytics query language]
domain: development
summary: >-
  Salesforce Analytics Query Language, the stream-based query language that CRM Analytics generates behind every
  lens, dashboard and explorer action and that developers write directly in dashboards, compare tables and the
  Analytics REST Query API to read CRM Analytics datasets.
release: "Winter '27"
status: current
broader: [kt:crm-analytics]
related: [kt:soql, kt:salesforce-analytics, kt:rest-api]
relations:
  - {predicate: alternativeTo, object: kt:sql-for-crm-analytics}
  - {predicate: contrastsWith, object: kt:soql}
  - {predicate: consumedBy, object: kt:lightning-web-components}
sources:
  - id: s1
    title: "Analytics SAQL Developer Guide: Overview"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.bi_dev_guide_saql.meta/bi_dev_guide_saql/bi_saql_intro.htm
    type: official-docs
    accessed: 2026-11-28
  - id: s2
    title: "Analytics SAQL Developer Guide: SAQL Statements"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.bi_dev_guide_saql.meta/bi_dev_guide_saql/bi_saql_statements_concept.htm
    type: official-docs
    accessed: 2026-11-28
  - id: s3
    title: "Analytics SAQL Developer Guide: Write Your First Query"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/analytics/bi-dev-guide-saql/guide/bi-saql-first-query.html
    type: official-docs
    accessed: 2026-11-28
  - id: s4
    title: "Analytics SAQL Developer Guide: Query Performance"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.bi_dev_guide_saql.meta/bi_dev_guide_saql/bi_saql_performance.htm
    type: official-docs
    accessed: 2026-11-28
  - id: s5
    title: "SQL for Analytics Developer Guide: SQL vs SAQL"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/analytics/bi-dev-guide-sql/guide/bi-sql-vs-saql.html
    type: official-docs
    accessed: 2026-11-28
  - id: s6
    title: "CRM Analytics REST API Developer Guide: Query CRM Analytics Data with the Query API"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.bi_dev_guide_rest.meta/bi_dev_guide_rest/bi_rest_api_query_data.htm
    type: official-docs
    accessed: 2026-11-28
created: 2026-11-28
---

# SAQL

**SAQL (Salesforce Analytics Query Language)** is the language used to read data from CRM Analytics datasets. It is the engine under the point-and-click experience: every lens, dashboard and explorer action generates and runs a SAQL query. Developers can also write SAQL directly through the CRM Analytics REST API, in dashboard JSON, in compare-table calculations that add a new column, and for transformations during data flows.[^s1] SAQL runs against CRM Analytics datasets, not against Salesforce objects, which is the key difference from SOQL.

## How it works

A SAQL query is a sequence of statements. Each statement takes an input stream, applies one operation, and produces an output stream, which is conventionally assigned back to a variable such as `q` so the next statement can use it.[^s2] Every query starts with `load`, which opens a dataset.[^s2] A minimal query that counts rows loads the `DTC_Opportunity_SAMPLE` dataset into `q`, then runs `q = group q by all;`, `q = foreach q generate count() as 'count';` and `q = limit q 2000;`.[^s3]

`group ... by all` aggregates the whole dataset as one group; grouping by a field (for example an account ID) gives one row per value instead. `foreach ... generate` is the projection step that outputs columns and aggregates.[^s3]

The main statements are:[^s2]

- **Shaping rows:** `filter` keeps rows that match a predicate, `foreach` projects expressions per row, and `group by` buckets rows for aggregates such as `count()` and `sum()`.[^s2]
- **Rollups:** `group by rollup` produces subtotal aggregations whose output depends on column order.[^s2]
- **Ordering and paging:** `order` sorts on one or more fields, while `limit` and `offset` cap and page results.[^s2]
- **Combining streams:** `cogroup` blends streams sharing a common field, `union` stacks identically shaped results, and semi/anti joins filter by presence.[^s2]
- **Sampling and gaps:** `sample` takes a random Bernoulli sample, and `fill` inserts null rows for missing date periods.[^s2]
- **Forecasting:** `timeseries` and `arimax` predict future data points and must follow a projection statement.[^s2]

## Running SAQL from code

The Query API endpoint is `wave/query`, called with a POST body whose only required attribute is `query`. An optional `queryLanguage` value of `SAQL` (the default) or `SQL` selects the language.[^s6] SAQL sent through the REST API must load the dataset by **dataset ID and dataset version ID**; loading by dataset name returns an error, unlike SQL requests, which accept the name.[^s6] The response contains column metadata, records, the response time and any warnings. In Lightning Web Components, the `lightning/analyticsWaveApi` module's `executeQuery` runs the same queries without a server-side proxy.[^s6]

## Limits and gotchas

- If a query sets no `limit`, it returns at most **10,000 rows**.[^s2]
- Do heavy transformations in the dataflow or recipe rather than at query time, and place `group` and `filter` on simple fields before `foreach` instead of after.[^s4]
- Multivalue fields perform poorly and have undefined behavior in `group by` and `foreach`; reference them only in filters where possible.[^s4]
- `unique()` is expensive on large datasets, which the guide describes as over 100 million rows with more than one million unique values.[^s4]
- Dashboard bindings and faceting can inject redundant filters, so inspect the generated SAQL when tuning a slow dashboard.[^s4]
- On an empty dataset, a count in SAQL returns an empty response rather than 0, and grouped nulls behave differently than in SQL.[^s5]

## SAQL vs SQL for CRM Analytics

CRM Analytics also accepts SQL for datasets. SAQL keeps capabilities the SQL dialect lacks: random sampling, cogrouping, type casting with `string_to_number()` and `toString()`, relative date filters such as a range from two years ago to one day ago, and date functions like `date_diff()` and `now()`.[^s5] SQL is the more familiar syntax for analysts. When a values query mixes aggregated and unaggregated columns without grouping, SQL raises an error, whereas SAQL returns each row's value.[^s5] Teams therefore often prototype in SQL and fall back to SAQL for sampling, cogroup blends, date math and forecasting statements.

## Connections

- **Broader:** `kt:crm-analytics` is the product whose datasets SAQL queries and whose UI generates it.[^s1]
- **Related:** `kt:soql` is a different language for Salesforce object records and is commonly confused with SAQL. `kt:salesforce-analytics` is the umbrella analytics portfolio. `kt:rest-api` is the family of HTTP APIs to which the Analytics Query API belongs.[^s6]
- **alternativeTo** `kt:sql-for-crm-analytics`: both query the same datasets, with the trade-offs above.[^s5]
- **consumedBy** `kt:lightning-web-components` through `executeQuery` in `lightning/analyticsWaveApi`.[^s6]

## Sources

[^s1]: Salesforce Developers, "Analytics SAQL Developer Guide: Overview". https://developer.salesforce.com/docs/atlas.en-us.264.0.bi_dev_guide_saql.meta/bi_dev_guide_saql/bi_saql_intro.htm (accessed 2026-11-28)
[^s2]: Salesforce Developers, "Analytics SAQL Developer Guide: SAQL Statements". https://developer.salesforce.com/docs/atlas.en-us.264.0.bi_dev_guide_saql.meta/bi_dev_guide_saql/bi_saql_statements_concept.htm (accessed 2026-11-28)
[^s3]: Salesforce Developers, "Analytics SAQL Developer Guide: Write Your First Query". https://developer.salesforce.com/docs/analytics/bi-dev-guide-saql/guide/bi-saql-first-query.html (accessed 2026-11-28)
[^s4]: Salesforce Developers, "Analytics SAQL Developer Guide: Query Performance". https://developer.salesforce.com/docs/atlas.en-us.264.0.bi_dev_guide_saql.meta/bi_dev_guide_saql/bi_saql_performance.htm (accessed 2026-11-28)
[^s5]: Salesforce Developers, "SQL for Analytics Developer Guide: SQL vs SAQL". https://developer.salesforce.com/docs/analytics/bi-dev-guide-sql/guide/bi-sql-vs-saql.html (accessed 2026-11-28)
[^s6]: Salesforce Developers, "CRM Analytics REST API Developer Guide: Query CRM Analytics Data with the Query API". https://developer.salesforce.com/docs/atlas.en-us.bi_dev_guide_rest.meta/bi_dev_guide_rest/bi_rest_api_query_data.htm (accessed 2026-11-28)
