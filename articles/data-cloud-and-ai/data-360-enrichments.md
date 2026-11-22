---
id: kt:data-360-enrichments
type: Feature
title: Data 360 Enrichments
aliases: [Data Cloud enrichments, Data 360 related lists, Data 360 copy fields, copy field enrichment, related list enrichment, direct-DMO related list enrichment, Data Cloud copy fields]
domain: data-cloud-and-ai
summary: >-
  Data 360 (formerly Data Cloud) features that surface Data 360 data on Salesforce CRM records, either as related
  lists queried live from data model objects or as copy fields that sync Data 360 values into standard and custom
  CRM fields through batch jobs.
release: "Winter '27"
status: current
broader: [kt:data-cloud]
related: [kt:calculated-insights, kt:identity-resolution, kt:lightning-app-builder, kt:person-accounts]
relations:
  - {predicate: dependsOn, object: kt:data-model-objects}
  - {predicate: dependsOn, object: kt:data-spaces}
  - {predicate: dependsOn, object: kt:data-actions}
  - {predicate: contrastsWith, object: kt:data-cloud-activation}
  - {predicate: governedBy, object: kt:data-cloud-limits}
sources:
  - id: s1
    title: "Enrichment Considerations"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=data.c360_a_enrichment_considerations.htm&type=5
    type: official-docs
    accessed: 2026-11-22
  - id: s2
    title: "Enrich Your Org with 360 Data and Insights"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=data.c360_a_enrich_your_org_with_data_and_insights.htm&type=5
    type: official-docs
    accessed: 2026-11-22
  - id: s3
    title: "Create a Direct-DMO Related List Enrichment"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=data.c360_a_create_a_related_list_direct_dmo_enrichment.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-22
  - id: s4
    title: "Create and Verify Your Copy Field Enrichment (Data 360 Enrichments module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-cloud-enrichments/create-and-verify-your-copy-field-enrichment
    type: official-learning
    accessed: 2026-11-22
  - id: s5
    title: "A Visual Guide to Salesforce Data Cloud Capabilities"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/10/a-visual-guide-to-salesforce-data-cloud-capabilities
    type: official-blog
    accessed: 2026-11-22
created: 2026-11-22
---

# Data 360 Enrichments

**Data 360 enrichments** bring data that lives in Data 360 (formerly Data Cloud) back onto Salesforce CRM records, so
users see unified profiles, engagement history and calculated insights inside standard record pages instead of
switching tools.[^s2][^s5] There are three flavors: **related list enrichments**, **direct-DMO related list
enrichments**, and **copy field enrichments**. They are available in all editions that support Data 360.[^s2][^s3]

## How each type works

**Related lists** display data model object (DMO) records that have a one-to-many relationship with a Data 360
Individual or Unified Individual, such as the many email engagement events tied to one contact.[^s2] The records are
not copied: the list queries Data 360 when the user opens it, so it shows near-real-time data.[^s1] These lists target
Account, Contact and Lead, and draw on engagement, profile or other DMOs related to the Individual, Unified Individual,
Account or Unified Account DMOs.[^s1]

**Direct-DMO related lists** link a DMO to a CRM object directly through an ID or string field, with no identity
resolution required. The Help example shows Vehicle Telematics Event records on a Vehicle in Automotive Cloud.[^s2][^s3]
You create the relationship from the DMO's Relationships tab with N:1 cardinality and a CRM related object, then add a
dynamic related list in Lightning App Builder; 1:1 cardinality isn't supported.[^s3] Targets include Account, Asset,
Case, Contact, Opportunity, Order, Product, Vehicle, Work Order and custom objects, and Person Account fields can be
matched starting in Winter '26.[^s3]

**Copy fields** copy values from objects with a one-to-one relationship to an Individual, Unified Individual, Account
or Unified Account DMO into CRM fields through a batch job.[^s1][^s2] Calculated insight objects qualify when they
have a single Individual ID as their dimension or are multi-dimensional aggregatable insights.[^s2] Supported field
types include Number, Text, Date, DateTime, Email, Phone, Url, Percent, Boolean and Currency.[^s1]

## Setting up a copy field

The Trailhead walkthrough shows the typical flow: create target fields on Account, grant the **Customer 360 Data
Platform Integration** permission set read and edit access to them, then go to Setup > Copy Field > New, choose a data
space, a source object (a calculated insight of open and total cases per account), the target object and an ID
matching method, map fields, and click Save and Start Sync.[^s4] Sync History on the enrichment shows whether the job
completed.[^s4] Help notes that the integration permission set only appears once at least one data action and data
action target exist, and that it needs Read, Edit, Delete, View All and Modify All on most target objects.[^s2]

## Limits and gotchas

- **Related list ceiling.** An org can have up to 10,000 related list enrichments, tied to the lookup relationship maximum.[^s1]
- **Engagement window.** Engagement related lists return the last 7 days by default; a dynamic list filter only overrides this if it covers every Event-Time-mapped field.[^s1]
- **Full syncs are heavy.** A full copy-field sync can run up to 24 hours and process 60–100 million records; later syncs update only changed records.[^s1]
- **License consumption.** Each copy field enrichment consumes one data action and one data target from the org's Data 360 license, and enrichment usage affects credit consumption.[^s1][^s2]
- **Overwrites.** Scheduled ingestion can overwrite edits users made to copy-field target fields; Help recommends dedicated Data 360-only fields.[^s1]
- **Unsupported fields.** Person Account fields with a Person prefix or `_pc` suffix can't be copy-field targets, and multi-currency orgs aren't supported.[^s1]
- **Visibility.** Users need access to the parent object and the data space; otherwise the related list renders blank.[^s1][^s3]
- **Companion orgs.** CRM-to-DMO relationships don't sync from a home org to companion orgs, so create them in the companion org directly.[^s3]

## When to use which

Use a **related list** when users need fresh, many-row engagement history and don't need to report or automate on it in
core CRM.[^s1][^s2] Use a **copy field** when a single value, such as lifetime value or an open-case count, must live on
the record for list views, reports, flows or formulas, accepting batch latency and license consumption.[^s1][^s4] Use a
**direct-DMO related list** when external records already carry a CRM ID and identity resolution would add nothing.[^s3]

## Connections

Enrichments sit **broader** under **Data 360**.[^s5] They **depend on data model objects** as their source and on
**data spaces** for access scoping, and copy fields **depend on data actions**, since each one consumes a data action
and target.[^s1][^s2] They draw heavily on **calculated insights** and **identity resolution** for unified
profiles.[^s2][^s4] Related lists are placed with **Lightning App Builder**, and Person Account support links them to
**Person Accounts**.[^s3] They **contrast with activation**: enrichments land Data 360 data on CRM records themselves, and they are
**governed by Data 360 limits** such as the related list ceiling and sync capacity.[^s1][^s2]

## Sources

[^s1]: Salesforce Help, "Enrichment Considerations". https://help.salesforce.com/s/articleView?language=en_US&id=data.c360_a_enrichment_considerations.htm&type=5 (accessed 2026-11-22)
[^s2]: Salesforce Help, "Enrich Your Org with 360 Data and Insights". https://help.salesforce.com/s/articleView?language=en_US&id=data.c360_a_enrich_your_org_with_data_and_insights.htm&type=5 (accessed 2026-11-22)
[^s3]: Salesforce Help, "Create a Direct-DMO Related List Enrichment". https://help.salesforce.com/s/articleView?id=data.c360_a_create_a_related_list_direct_dmo_enrichment.htm&language=en_US&type=5 (accessed 2026-11-22)
[^s4]: Trailhead, "Create and Verify Your Copy Field Enrichment (Data 360 Enrichments module)". https://trailhead.salesforce.com/content/learn/modules/data-cloud-enrichments/create-and-verify-your-copy-field-enrichment (accessed 2026-11-22)
[^s5]: Salesforce Developers Blog, "A Visual Guide to Salesforce Data Cloud Capabilities". https://developer.salesforce.com/blogs/2024/10/a-visual-guide-to-salesforce-data-cloud-capabilities (accessed 2026-11-22)
