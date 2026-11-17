---
id: kt:unstructured-data-in-data-cloud
type: Feature
title: Unstructured Data in Data 360
aliases: [Unstructured Data in Data Cloud, unstructured data lake object, UDLO, unstructured data model object, UDMO, Enterprise Knowledge powered by Data Cloud, unstructured data connectors]
domain: data-cloud-and-ai
summary: >-
  The Data 360 capability that references documents, transcripts, web pages and other unstructured content in
  external stores through unstructured data lake objects (UDLOs) mapped to unstructured data model objects (UDMOs),
  so the content can be indexed and used to ground AI, automation and analytics.
release: "Winter '27"
status: current
broader: [kt:data-cloud]
related: [kt:data-lake-objects, kt:data-model-objects, kt:agentforce-data-library, kt:data-streams, kt:knowledge-base]
relations:
  - {predicate: consumedBy, object: kt:vector-search-in-data-cloud}
  - {predicate: consumedBy, object: kt:retrieval-augmented-generation-in-salesforce}
  - {predicate: dependsOn, object: kt:data-spaces}
  - {predicate: integratesWith, object: kt:document-ai}
sources:
  - id: s1
    title: "Get Started with Unstructured Data in Data Cloud (Unstructured Data in Data Cloud)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/unstructured-data-in-data-cloud/get-started-with-unstructured-data-in-data-cloud
    type: official-learning
    accessed: 2026-11-17
  - id: s2
    title: "Salesforce Data Cloud Objects (Object Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_concepts_data_cloud_objects.htm
    type: official-docs
    accessed: 2026-11-17
  - id: s3
    title: "Create a Microsoft SharePoint Unstructured (Documents) Data Lake Object"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-create-microsoftsharepoint-udlo.html
    type: official-docs
    accessed: 2026-11-17
  - id: s4
    title: "Microsoft SharePoint Unstructured (Documents) Limitations and Troubleshooting"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-microsoftsharepoint-unstructured-connector-limitations.html
    type: official-docs
    accessed: 2026-11-17
  - id: s5
    title: "Process Content for Use with AI (Data 360 content processing)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/de/content/learn/modules/data-cloud-process-content/process-content-for-use-with-ai
    type: official-learning
    accessed: 2026-11-17
  - id: s6
    title: "Salesforce Enterprise Knowledge: Data Cloud Unstructured Data"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/salesforce-enterprise-knowledge-data-cloud-unstructured-data/
    type: official-blog
    accessed: 2026-11-17
  - id: s7
    title: "Ingest Knowledge Article Data (Unstructured Data in Data Cloud)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/es/content/learn/projects/unstructured-data-in-data-cloud/ingest-knowledge-article-data
    type: official-learning
    accessed: 2026-11-17
created: 2026-11-17
---

# Unstructured Data in Data 360

Data 360 (formerly Data Cloud) can reference **unstructured data**: content with no consistent format that fits poorly in relational tables, such as chat transcripts, emails, legal documents, call recordings, video and long-form text.[^s1] Salesforce examples include Knowledge articles and sales call transcripts. Once referenced, the content feeds generative AI in Prompt Builder and Agentforce, automation in Flow Builder, and analytics in Tableau and CRM Analytics.[^s1] Salesforce's launch material cites an IDC estimate that nearly 90% of enterprise data is unstructured, which is why grounding agents on it matters.[^s6]

## How it works

The model mirrors structured ingestion but with two dedicated object kinds:[^s1][^s2]

- **Unstructured data lake object (UDLO)**: created manually for a connected source; it carries the `__dlo` suffix like other data lake objects.[^s2]
- **Unstructured data model object (UDMO)**: the target of the mapping, with the `__dlm` suffix. Because the schemas are identical, Data 360 builds the field mappings automatically.[^s1][^s2]
- **Cardinality**: each UDLO maps to at most one UDMO, but several UDLOs can map to one UDMO, e.g. recordings from two S3 buckets and a Google Cloud Storage bucket all landing in one CaseRecordings UDMO.[^s1]

A key design point: for blob-store sources, Data 360 does not import the files; the UDMO references them where they live.[^s1] A search index is then configured on the UDMO, and the indexing step generates chunk DMOs and vector-embedding DMOs used for retrieval-augmented generation (RAG).[^s2]

## Connectors and setup

The base path connects an external blob store (Amazon S3, Azure Blob Storage or Google Cloud Storage), creates a UDLO over it, and maps it to a UDMO.[^s1] Salesforce has since added prebuilt unstructured connectors, launching with Zendesk, Google Drive and SharePoint plus a sitemap connector and web crawler, with more rolling out from Summer '25.[^s6] Updates, changes and deletions in the source files sync to Data 360.[^s6]

Taking SharePoint as an example, you open Data Lake Objects, choose **New → From External Files**, pick the connector tile and connection, enter the site ID, name the UDLO, select a data space, and map it to a new or existing UDMO.[^s3] The wizard can enable semantic search with system defaults, which picks text fields and a chunking strategy automatically, or you can build the search index later.[^s3] Optional **content harmonization** converts formats into a consistent one; enabling it turns off AI enrichments (summary and Q&A) by default.[^s3][^s6] Connecting unstructured data requires the Data Cloud Architect permission, and ingestion takes minutes depending on the number and size of assets.[^s3]

Knowledge articles are a special case: they mix structured and unstructured content in custom text fields and are ingested through the Salesforce CRM connector's Knowledge data bundle (part of the Service Cloud bundle), after which a search index is built over the Knowledge object.[^s7]

## Limits and gotchas

Limits are set per connector, so check each connector's limitations page. For the SharePoint Unstructured (Documents) connector, verified for Winter '27:[^s4]

- **File size**: 100 MB for PDF, CSV and similar; 20 MB for images; 4 MB for other supported formats.[^s4]
- **Scope**: only the default Documents library of the given site; no subsites, other libraries or folder-level filtering.[^s4]
- **Volume and age**: up to 300 GB per site or library per ingestion job; jobs over 24 hours may time out; files last modified more than 2 years before sync are skipped.[^s4]
- **Silent skips**: unsupported file types are skipped, and a job that finds no supported files completes with zero records and no UI error.[^s4]

Other gotchas: UDLOs cannot be packaged, though the connections behind them can, and data kits are the recommended way to move UDMOs.[^s2]

## When to use it (and when not)

Use unstructured ingestion when agents, prompts or flows must answer from documents, transcripts or web content that lives outside CRM records.[^s1][^s5] For the common case of grounding an agent, see `kt:agentforce-data-library`, which wraps these steps; the underlying objects are the same UDLOs, UDMOs and search indexes.[^s2] When the goal is extracting specific fields (names, dates, amounts) from invoices or contracts into structured records, Document AI is the better fit; it stores extracted values in data lake objects with a defined schema.[^s5]

## Connections

This capability is part of `kt:data-cloud` and extends `kt:data-lake-objects` and `kt:data-model-objects` with unstructured variants; connections are set up much like `kt:data-streams`, and each UDLO is assigned to one of the `kt:data-spaces`.[^s2][^s3] Its UDMOs are **consumed by** `kt:vector-search-in-data-cloud`, which chunks and embeds them, and through that by `kt:retrieval-augmented-generation-in-salesforce`.[^s2] `kt:agentforce-data-library` automates the same pipeline for agents, and `kt:knowledge-base` content is a common source.[^s1][^s7] It **integrates with** `kt:document-ai`, which turns semi-structured documents into structured data.[^s5]

## Sources

[^s1]: Trailhead, "Get Started with Unstructured Data in Data Cloud". https://trailhead.salesforce.com/content/learn/projects/unstructured-data-in-data-cloud/get-started-with-unstructured-data-in-data-cloud (accessed 2026-11-17)
[^s2]: Salesforce Developers, "Salesforce Data Cloud Objects". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_concepts_data_cloud_objects.htm (accessed 2026-11-17)
[^s3]: Salesforce Developers, "Create a Microsoft SharePoint Unstructured (Documents) Data Lake Object". https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-create-microsoftsharepoint-udlo.html (accessed 2026-11-17)
[^s4]: Salesforce Developers, "Microsoft SharePoint Unstructured (Documents) Limitations and Troubleshooting". https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-microsoftsharepoint-unstructured-connector-limitations.html (accessed 2026-11-17)
[^s5]: Trailhead, "Process Content for Use with AI". https://trailhead.salesforce.com/de/content/learn/modules/data-cloud-process-content/process-content-for-use-with-ai (accessed 2026-11-17)
[^s6]: Salesforce, "Salesforce Enterprise Knowledge: Data Cloud Unstructured Data". https://www.salesforce.com/blog/salesforce-enterprise-knowledge-data-cloud-unstructured-data/ (accessed 2026-11-17)
[^s7]: Trailhead, "Ingest Knowledge Article Data". https://trailhead.salesforce.com/es/content/learn/projects/unstructured-data-in-data-cloud/ingest-knowledge-article-data (accessed 2026-11-17)
