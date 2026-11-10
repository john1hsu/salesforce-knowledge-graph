---
id: kt:data-spaces
type: Feature
title: Data Spaces
aliases: [data space, Data 360 data spaces, Data Cloud data spaces, dataspace, default data space]
domain: data-cloud-and-ai
summary: >-
  Logical partitions inside a single Data 360 (formerly Data Cloud) instance that segregate data, metadata and
  processes by brand, region or department, with access granted through permission sets tied to each data space.
release: "Winter '27"
status: current
broader: [kt:data-cloud]
related: [kt:data-lake-objects, kt:data-model-objects, kt:identity-resolution, kt:data-cloud-segmentation]
relations:
  - {predicate: dependsOn, object: kt:permission-sets}
  - {predicate: contrastsWith, object: kt:data-residency}
  - {predicate: consumedBy, object: kt:data-streams}
  - {predicate: coveredBy, object: kt:data-cloud-consultant-certification}
sources:
  - id: s1
    title: "About Data Spaces"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=data.c360_a_data_spaces.htm&type=5
    type: official-docs
    accessed: 2026-11-10
  - id: s2
    title: "Explore Data Space Functionality (Data Spaces in Data 360: Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-spaces-in-data-cloud-quick-look/explore-data-space-functionality
    type: official-learning
    accessed: 2026-11-10
  - id: s3
    title: "Data 360 Architecture"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/fundamentals/guide/data-360-architecture.html
    type: official-docs
    accessed: 2026-11-10
  - id: s4
    title: "Data 360: Impact of Data Space Filters on Data Stream Counts"
    publisher: Salesforce Help (Knowledge Article)
    url: https://help.salesforce.com/s/articleView?id=002721752&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-10
  - id: s5
    title: "Review Data Cloud Setup and Administration (Data Cloud Consultant Certification Prep)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/cert-prep-data-cloud-consultant/review-data-cloud-setup-and-administration
    type: official-learning
    accessed: 2026-11-10
created: 2026-11-10
---

# Data Spaces

A **data space** is a logical partition of a Data 360 (formerly Data Cloud) instance. It lets one org keep data,
metadata and processes for profile unification, insights and marketing separate by category such as brand, region
or department.[^s1] Salesforce's architecture guidance describes the data space as the basic logical container for all
data and metadata in Data 360, giving an isolated environment for processing and modeling and a form of internal
multitenancy between business units, regions or brands.[^s3]

## How it works

Every Data 360 org starts with a **default data space**. Until other data spaces are created, all Data 360 objects map
to it, and it can never be deleted; its display name can be changed.[^s1][^s2] A data space's name and description are
editable, but its prefix cannot be modified after creation, so choose it carefully.[^s1]

Once data spaces are in use, Data 360 runs user and system data services in the context of a data space, which shapes
how calculated insights, segmentation and activation behave.[^s2] Inside a data space a user can build object mappings,
identity resolution rulesets, insights, data actions, segments and activation targets.[^s2] The architecture guide adds
that each DLO or DMO belongs to a single data space, and that queries, transformations and mappings don't cross data
space boundaries unless explicitly authorized.[^s3]

Data enters a data space through its data lake objects. When data is brought in, a DLO can be associated with a data
space with or without filters, and the same DLO can be added to more than one data space.[^s1] Only standard data
bundles, such as the Salesforce CRM or Marketing Cloud Engagement bundles, can be deployed to a non-default data space.[^s1]

## Access control

Access to data-space-aware objects and features is granted through object and feature permissions in permission sets.
By default, users with the standard Data 360 permission sets reach only the default data space; admins create custom
permission sets and choose the data spaces each one covers.[^s1] Users with the Data Cloud Architect permission set and
a System Administrator profile can create, edit and delete data spaces, and a user viewing data sees only what is
assigned to their data space.[^s2] Architects treat data spaces as the coarse-grained access boundary, with
attribute-based policies providing finer control over objects, fields and rows within one data space.[^s3]

## Limits and gotchas

- **Filters don't reduce ingestion.** A data space filter on a DLO only limits which records are visible in that data space; the DLO and the stream's Total Records still count every ingested record.[^s4]
- **No CRM pre-filtering.** You currently can't pre-filter Salesforce CRM records so that only matching rows are ingested; the filter is applied after ingestion.[^s4]
- **Not everything is data space aware.** Salesforce notes that some objects and features ignore data spaces, so check each feature before relying on the partition for isolation.[^s1]
- **Only mapped data is usable.** Segmentation and activation can use only mapped fields and objects that have relationships.[^s1]

## When to use it (and when not)

Data spaces fit an org that runs one Data 360 instance for several brands, regions or departments and wants each
team to see and work only on its own data.[^s2] They are a poor fit when the main goal is unifying and targeting
customers across brands, and they do not solve data residency: data spaces partition data logically, not by
geographic location.[^s2] For sandbox work, a local data kit deployment can replicate Data 360 metadata and process
definitions across several data spaces in the same sandbox.[^s1]

## Connections

Data spaces are a feature of `kt:data-cloud` and partition its storage and model layers: `kt:data-lake-objects`
are associated with one or more data spaces, optionally filtered, and the `kt:data-model-objects` mapped from them
belong to a single space.[^s1][^s3] `kt:data-streams` deploy into a chosen data space, and processes such as
`kt:identity-resolution` rulesets, `kt:data-cloud-segmentation` and activation run in a data space's context.[^s2]
Access depends on `kt:permission-sets` tied to each space.[^s1] Data spaces contrast with
`kt:data-residency`, which they explicitly do not address.[^s2] The Data Cloud Consultant certification prep lists
identifying data space use cases and creating data spaces under Data Cloud Setup and Administration, 12% of the
exam (`kt:data-cloud-consultant-certification`).[^s5]

## Sources
[^s1]: Salesforce Help, "About Data Spaces". https://help.salesforce.com/s/articleView?language=en_US&id=data.c360_a_data_spaces.htm&type=5 (accessed 2026-11-10)
[^s2]: Trailhead, "Explore Data Space Functionality". https://trailhead.salesforce.com/content/learn/modules/data-spaces-in-data-cloud-quick-look/explore-data-space-functionality (accessed 2026-11-10)
[^s3]: Salesforce Architects, "Data 360 Architecture". https://architect.salesforce.com/docs/architect/fundamentals/guide/data-360-architecture.html (accessed 2026-11-10)
[^s4]: Salesforce Help, "Data 360: Impact of Data Space Filters on Data Stream Counts". https://help.salesforce.com/s/articleView?id=002721752&language=en_US&type=1 (accessed 2026-11-10)
[^s5]: Trailhead, "Review Data Cloud Setup and Administration". https://trailhead.salesforce.com/content/learn/modules/cert-prep-data-cloud-consultant/review-data-cloud-setup-and-administration (accessed 2026-11-10)
