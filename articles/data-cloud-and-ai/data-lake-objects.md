---
id: kt:data-lake-objects
type: Feature
title: Data Lake Objects
aliases: [DLO, DLOs, data lake object, Data 360 data lake objects, Data Cloud data lake objects, __dlo objects]
domain: data-cloud-and-ai
summary: >-
  The storage layer of Data 360 (formerly Data Cloud): `__dlo` objects, usually created by deploying a data stream,
  that hold ingested or federated data in the source system's own schema until it is mapped to data model objects.
release: "Winter '27"
status: current
broader: [kt:data-cloud]
related: [kt:data-integration, kt:zero-copy-data-federation]
relations:
  - {predicate: enables, object: kt:data-model-objects}
  - {predicate: configuredVia, object: kt:data-streams}
  - {predicate: governedBy, object: kt:data-cloud-limits}
  - {predicate: contrastsWith, object: kt:big-objects}
  - {predicate: coveredBy, object: kt:data-cloud-consultant-certification}
sources:
  - id: s1
    title: "Salesforce Data Cloud Objects (Object Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_concepts_data_cloud_objects.htm
    type: official-docs
    accessed: 2026-11-08
  - id: s2
    title: "Model Data in Data 360"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-dmo-mapping/guide/c360dm-model-data.html
    type: official-docs
    accessed: 2026-11-08
  - id: s3
    title: "Create an Ingestion API Data Stream"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-create-ingestion-data-stream.html
    type: official-docs
    accessed: 2026-11-08
  - id: s4
    title: "Create an SFTP Data Stream"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-create-sftp-data-stream.html
    type: official-docs
    accessed: 2026-11-08
  - id: s5
    title: "Data Lake Object Naming Standards"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=data.c360_a_data_lake_object_naming.htm&language=fr&type=5
    type: official-docs
    accessed: 2026-11-08
  - id: s6
    title: "What Are the Data Stream Categories in Data Cloud?"
    publisher: Salesforce Ben
    url: https://www.salesforceben.com/what-are-the-data-stream-categories-in-data-cloud/
    type: community
    accessed: 2026-11-08
created: 2026-11-08
---

# Data Lake Objects

**Data lake objects (DLOs)** are where Data 360 (formerly Data Cloud) actually stores data. Data that
is ingested or federated into Data 360 is first held in a DLO, which captures the information in its initial, raw
state.[^s2] A DLO keeps the schema of the data stream that feeds it, so its fields look like the source system's
fields rather than like the Customer 360 Data Model.[^s1] DLO API names end in `__dlo`.[^s1]

## How it works

Most DLOs are created by deploying a **data stream**. While configuring a stream you either create a new DLO or
reuse an existing one, edit its fields, and enter a label, API name and object details; after you deploy, you map
the DLO to the data model.[^s4] The object details are where the important design choices sit:

- **Category** identifies the type of data: Profile, Engagement or Other.[^s3][^s4]
- **Primary key** is the field that uniquely identifies each record.[^s3][^s4]
- **Record modified field** (Profile and Other) tells Data 360 which version of a record is newest when data
  arrives out of order, so the record with the latest timestamp is loaded.[^s3][^s4]
- **Event time field** is required for Engagement data. It must record when the engagement happened and must not
  change over time.[^s3]
- **Organization unit identifier** selects the business unit used for a record's data lineage.[^s4]

You can add formula fields to a DLO, and DLOs are customizable.[^s1][^s4] The data itself is harmonized by mapping
DLO fields onto data model objects (DMOs). DMOs don't hold data; they point to the data in DLOs. Data prep and
transforms can also turn existing DLOs and DMOs into new DLOs.[^s1][^s2]

Two variants exist alongside standard DLOs. **Unstructured DLOs (UDLOs)** reference unstructured content in a blob
store. You create them manually, and they are mapped automatically to the unstructured DMO schema. The object reference also lists
**external DLOs** as a separate kind.[^s1]

## Choosing a category

In practitioner guidance, **Profile** (the default) is for demographic and contact-point data keyed by a unique ID,
such as a CRM record ID. **Engagement** is for time-stamped behaviour such as web visits or purchases, keyed to an
immutable DateTime that should include a time zone. **Other** is for data that fits neither, including engagement
data whose dates can change.[^s6] The same guidance warns that a stream's category can't be changed once selected,
so a wrong choice means rebuilding the stream.[^s6] The official Ingestion API guide makes the same point about
**Refresh Mode**: you set it when you create the data stream and cannot change it afterward.[^s3]

## Limits and gotchas

- **Naming.** Both the label and the API name are required and must be unique. The API name can be up to 40
  characters, uses only letters, digits and underscores, must start with a letter, can't end with an underscore,
  and can't contain two consecutive underscores.[^s5]
- **Latency.** For Ingestion API streams, Salesforce says to allow up to an hour before data appears.[^s3]
- **Packaging.** DLOs and the data streams that load them can be packaged with data kits. UDLOs can't be
  packaged, though the connections that ingest them can.[^s1]
- **Data spaces.** You choose a data space (or the default one) before you deploy a stream.[^s3]
- The pages used here give no numeric limits on DLO volume or field counts, so check the current Data 360 limits
  documentation rather than assuming a number.[^s1][^s4]

## When to use it (and when not)

Treat DLOs as the landing and staging layer. Keep the source shape there, choose the category and primary key
carefully at stream creation, and do your harmonization by mapping to standard DMOs. Segments, identity resolution
and insights all work on DMOs, not on raw DLOs.[^s1][^s2] Don't model DLOs as CRM sObjects. They are high-scale
Data 360 objects with their own suffix and access paths.[^s1]

## Connections

DLOs are the storage foundation of `kt:data-cloud`. They **enable** `kt:data-model-objects`, which only point at DLO
data, and are **configured via** `kt:data-streams`, whose deployment creates and loads them.[^s1][^s4] Federated
sources from `kt:zero-copy-data-federation` and inbound pipelines from `kt:data-integration` both land in this
layer.[^s2][^s3] Capacity questions are **governed by** `kt:data-cloud-limits`. DLOs **contrast with**
`kt:big-objects`, the CRM platform's own high-volume store, a separate mechanism that is easy to confuse with the lake.
Designing streams and DLOs is **covered by** `kt:data-cloud-consultant-certification`.[^s1]

## Sources

[^s1]: Salesforce Developers, "Salesforce Data Cloud Objects" (Object Reference). https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_concepts_data_cloud_objects.htm (accessed 2026-11-08)
[^s2]: Salesforce Developers, "Model Data in Data 360". https://developer.salesforce.com/docs/data/data-cloud-dmo-mapping/guide/c360dm-model-data.html (accessed 2026-11-08)
[^s3]: Salesforce Developers, "Create an Ingestion API Data Stream". https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-create-ingestion-data-stream.html (accessed 2026-11-08)
[^s4]: Salesforce Developers, "Create an SFTP Data Stream". https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-create-sftp-data-stream.html (accessed 2026-11-08)
[^s5]: Salesforce Help, "Data Lake Object Naming Standards". https://help.salesforce.com/s/articleView?id=data.c360_a_data_lake_object_naming.htm&language=fr&type=5 (accessed 2026-11-08)
[^s6]: Salesforce Ben, "What Are the Data Stream Categories in Data Cloud?". https://www.salesforceben.com/what-are-the-data-stream-categories-in-data-cloud/ (accessed 2026-11-08)
