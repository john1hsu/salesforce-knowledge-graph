---
id: kt:data-cloud-limits
type: Limit
title: Data 360 Limits and Guidelines
aliases: [Data Cloud limits, Data Cloud limits and guidelines, Data 360 limits, Customer Data Platform limits and guidelines, Data 360 usage limits]
domain: data-cloud-and-ai
summary: >-
  The published per-org caps on Data 360 (formerly Data Cloud) objects, ingestion, identity resolution,
  segmentation, activation, insights and APIs, which vary by license and change frequently between releases.
release: "Winter '27"
status: current
broader: [kt:data-cloud, kt:governor-limits]
related: [kt:data-lake-objects, kt:data-model-objects, kt:identity-resolution, kt:calculated-insights, kt:data-cloud-segmentation]
relations:
  - {predicate: contrastsWith, object: kt:api-request-limits}
  - {predicate: coveredBy, object: kt:data-cloud-consultant-certification}
sources:
  - id: s1
    title: "Customer Data Platform Limits and Guidelines"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.c360_a_limits_and_guidelines_cdp.htm&type=5
    type: official-docs
    accessed: 2026-11-08
  - id: s2
    title: "Data 360 Usage and Access Changes"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.c360_a_changelog_usage_and_access.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-08
  - id: s3
    title: "Get Started with Ingestion API"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-ref/guide/c360a-api-get-started.html
    type: official-docs
    accessed: 2026-11-08
  - id: s4
    title: "Query Data 360 Data using Query API"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-query-guide/references/data-cloud-query-api-reference/c360a-api-queryservices-overview.html
    type: official-docs
    accessed: 2026-11-08
created: 2026-11-08
---

# Data 360 Limits and Guidelines

**Data 360 limits and guidelines** are the published caps on what one Data 360 (formerly Data Cloud) org can
hold and process: how many data streams and objects it has, how large ingested files can be, how identity
resolution and segmentation are scheduled, and how often its APIs can be called. Salesforce publishes them in
Salesforce Help as a set of license-specific tables, and points API users to that limits page for usage
caps.[^s1][^s4] Unlike core platform governor limits, these are org-level capacity and scheduling ceilings rather
than per-transaction limits, and they change often enough that Salesforce keeps a dated changelog of them.[^s2]

## How the limits are organized

The tables are grouped by capability: general, activation, AI models, calculated insights, data actions, data
federation, data graphs, ingestion (general, bulk, local file and SFTP), data model objects, data shares, data
transforms, identity resolution, segmentation, streaming insights and APIs. Values differ by license, and the
page used here describes the legacy **Customer Data Platform** license, with separate values for Developer
orgs.[^s1] Treat the numbers below as that license's values, verified for Winter '27; check your own license's
table before designing to a ceiling.

## Key limits (Customer Data Platform license)

- **Objects and streams.** Up to 5,000 data streams, 5,000 data lake objects and 7,500 data model objects. A data
  stream or DMO can have 1,050 fields in total, with at most 800 of any single field type, and a DMO can have 25
  custom relationships.[^s1]
- **Bulk file ingestion (S3, GCS, Azure).** Up to 1,000 files per scheduled run; a compressed CSV can be up to
  250 MB, an uncompressed CSV up to 200 GB, and one cell up to 70,000 characters. SFTP files are capped at 2 GB
  each and 30 GB per stream run.[^s1]
- **Identity resolution.** Two rulesets per primary DMO per data space, up to 10 match rules per ruleset with 10
  criteria each, scheduled at most once a day and run at most 4 times in 24 hours. One unified profile can merge
  up to 50,000 source profiles.[^s1]
- **Segmentation.** 9,950 active segments, 100 filters per segment (up to 50 each in Include and Exclude), 50
  standard concurrent publishes, and at most 2 scheduled publishes per standard segment per day. Standard segments
  query 24 months of events; rapid segments query 7 days and can publish up to 24 times a day.[^s1]
- **Calculated insights.** 300 per tenant, 10 dimensions and 50 measures each, nesting up to 4 deep, a 2-hour
  maximum execution time and 30 manual runs per insight per 24 hours.[^s1]
- **Activation.** 300 activation targets, 100 attributes, and a scheduled publish frequency between 12 and 24
  hours. Activations can use up to 300 related attributes across no more than 4 DMOs.[^s1]
- **Data graphs and shares.** 2 data graphs per org on this license, with up to 25 objects each; 20 data shares,
  5 share targets and 250 objects per share.[^s1]

## API limits

The Ingestion API's streaming mode accepts request bodies up to 200 KB, deletes up to 200 records per request,
and allows 250 requests per second across all object endpoints; data is processed asynchronously about every 3
minutes. Bulk mode allows 100 files per job, 150 MB CSVs, 20 jobs per hour and 5 concurrent jobs, and deletes
open jobs older than 7 days.[^s3] For querying, the limits table gives a 5-minute timeout and 1,000 Query and
Insights API queries per day on Corporate and Enterprise editions; Profile API daily quotas are 10,000 (Corporate)
and 50,000 (Enterprise).[^s1] The Query API guide adds that results from a query can be re-read for 24 hours
without further consumption charges, so paging through stored rows is cheaper than re-running a query.[^s4]

## Gotchas

- **Limits move.** The changelog records frequent changes in 2026: data graphs per org rose from 10 to 25 (April),
  search indexes per instance from 25 to 100 (May), and data shares per org from 10 to 20 while share targets
  fell from 20 to 5 (August).[^s2] A design note citing an old number can be wrong in either direction.
- **License matters.** The changelog says connected CRM orgs no longer have a limit as of April 28, 2026, while the
  Customer Data Platform table still lists 5 connected CRM orgs, which shows how values differ between license
  tables.[^s1][^s2]
- **Throttling.** An HTTP 429 from the Ingestion API means back off and retry later; Salesforce gives no fixed
  retry interval.[^s3]

## Connections

These limits sit **under** `kt:data-cloud` and are the Data 360 counterpart of the platform's
`kt:governor-limits`. They **govern** `kt:data-lake-objects` and `kt:data-model-objects` (object and field
counts), `kt:identity-resolution` (ruleset counts and schedules), `kt:calculated-insights` (dimensions, measures,
runtime) and `kt:data-cloud-segmentation` (segment counts and publish schedules).[^s1] They **contrast with**
`kt:api-request-limits`, the rolling 24-hour core API allocation, because Data 360 APIs carry their own quotas.[^s1][^s3]
Knowing where these ceilings sit is part of the `kt:data-cloud-consultant-certification`.[^s1]

## Sources

[^s1]: Salesforce Help, "Customer Data Platform Limits and Guidelines". https://help.salesforce.com/s/articleView?language=en_US&id=sf.c360_a_limits_and_guidelines_cdp.htm&type=5 (accessed 2026-11-08)
[^s2]: Salesforce Help, "Data 360 Usage and Access Changes". https://help.salesforce.com/s/articleView?id=sf.c360_a_changelog_usage_and_access.htm&language=en_US&type=5 (accessed 2026-11-08)
[^s3]: Salesforce Developers, "Get Started with Ingestion API". https://developer.salesforce.com/docs/data/data-cloud-ref/guide/c360a-api-get-started.html (accessed 2026-11-08)
[^s4]: Salesforce Developers, "Query Data 360 Data using Query API". https://developer.salesforce.com/docs/data/data-cloud-query-guide/references/data-cloud-query-api-reference/c360a-api-queryservices-overview.html (accessed 2026-11-08)
