---
id: kt:agentforce-data-library
type: Feature
title: Agentforce Data Library
aliases: [ADL, Agentforce Data Libraries, data library for Agentforce, ADL API, Data Libraries Connect API]
domain: data-cloud-and-ai
summary: >-
  A Setup-managed container of grounding content (Knowledge articles, uploaded files, web content or an existing
  retriever) that automatically provisions the Data 360 data streams, objects, search index and retriever an
  Agentforce agent or prompt needs to answer from an organization's own content.
release: "Winter '27"
status: current
broader: [kt:retrieval-augmented-generation-in-salesforce, kt:agentforce]
related: [kt:knowledge-base, kt:vector-search-in-data-cloud, kt:prompt-builder, kt:data-streams, kt:data-model-objects, kt:unstructured-data-in-data-cloud]
relations:
  - {predicate: dependsOn, object: kt:data-cloud}
  - {predicate: configuredVia, object: kt:agentforce-studio}
  - {predicate: queriedWith, object: kt:connect-api}
  - {predicate: consumedBy, object: kt:agentforce}
  - {predicate: coveredBy, object: kt:agentforce-specialist-certification}
sources:
  - id: s1
    title: "Upgrade AI with Real-World Data (Agentforce Data Library Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agentforce-data-library-basics/upgrade-ai-with-real-world-data
    type: official-learning
    accessed: 2026-11-13
  - id: s2
    title: "Build a File-Based Data Library for an Agent (Agentforce Data Library Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agentforce-data-library-basics/build-a-file-based-data-library-for-an-agent
    type: official-learning
    accessed: 2026-11-13
  - id: s3
    title: "Agentforce Data Libraries resources (Connect REST API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/connect_resources_adl.htm
    type: official-docs
    accessed: 2026-11-13
  - id: s4
    title: "Use Knowledge in Agentforce for Service"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agentforce-service-agent-quick-look/use-knowledge-in-agentforce-for-service
    type: official-learning
    accessed: 2026-11-13
  - id: s5
    title: "Get Started with Salesforce Agentforce Specialist Certification Prep"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/cert-prep-agentforce-specialist/get-started-with-salesforce-agentforce-specialist-certification-prep
    type: official-learning
    accessed: 2026-11-13
  - id: s6
    title: "Manage Data Libraries with the ADL API (Agentforce Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/adl.html
    type: official-docs
    accessed: 2026-11-13
created: 2026-11-13
---

# Agentforce Data Library

An **Agentforce Data Library** (ADL) is the admin-facing wrapper Salesforce puts around grounding. Instead of hand-building ingestion, mapping, indexing and retrieval in Data 360 and Prompt Builder, an admin creates a library, points it at content, and the platform provisions the rest.[^s1] Salesforce positions it as the way to turn large volumes of unstructured or semi-structured content into something an AI feature can search.[^s1][^s6]

## What a library can hold

Each library has one source, chosen at creation. Trailhead stresses that the source choice is permanent and cannot be changed later.[^s2] Trailhead modules name these sources:

- **Knowledge articles**, using selected article fields and attachments.[^s1][^s4]
- **Uploaded files**: Trailhead gives 4 MB per text or HTML file and 100 MB per PDF.[^s2]
- **Web content and transcripts**, plus custom retrievers built in Data 360.[^s1][^s4]

The Connect REST API names the same choices as source types. `SFDRIVE` is a file library, `KNOWLEDGE` an article library, and `RETRIEVER` wraps an existing active custom retriever. A `SITEMAP` type appears only among the fields an update can change.[^s3]

## What gets provisioned

Saving a library starts a chain of setup steps. A data stream lands the content in Data 360. Data lake and data model objects are created and mapped. The content is chunked into a search index, and a retriever is created on top of it.[^s1][^s2] Each library gets its own retriever, though two libraries can share one search index.[^s1] Chunking time grows with the number, size and complexity of the files or articles, and with the number of Knowledge fields you chunk.[^s1]

Data 360 must be turned on before you can set up a library.[^s4] Admins also need permission to work with Agentforce Data Library, and Trailhead advises building in a sandbox first.[^s2]

## Attaching it to an agent

In Agentforce Builder, the agent's **Knowledge** tab lets you pick an existing library or create a new one. After that you save and reactivate the agent.[^s2] Before testing, check that both the search index and the library show as ready, and restart the preview conversation so it uses the new content.[^s2] At runtime the user's question goes into a prompt template that references the library's retriever. The most relevant chunks are added to the prompt, the LLM answers, and the response is checked against the prompt's instructions before the user sees it.[^s1]

For service teams, this replaces Einstein Bot article answers. Those needed NLP training, field mapping and a build that could take 30 minutes or more. A data library needs no field mapping or retraining, and articles don't have to be refreshed by hand.[^s4]

## Programmatic management and limits

The ADL Connect API lets you create, list, update and delete libraries. For file libraries it can also request presigned upload URLs, add or remove files, start indexing and poll status.[^s3][^s6] Limits documented in the resource reference:[^s3]

- One add-files request can include at most 1,000 files, and file names must be unique within that batch.[^s3]
- Only the default data space is supported; other data space IDs return HTTP 400.[^s3]
- The primary index fields of a Knowledge library cannot be changed after creation.[^s3]
- A library that an agent is using cannot be deleted.[^s3]

Indexing calls apply only to file libraries; Knowledge libraries start provisioning automatically when created.[^s3]

## When to use it (and when not)

Use a data library when the goal is "answer from these documents or articles" and the default chunking and retrieval are good enough. It is the fastest path to grounded answers.[^s1][^s4] When you need retrieval tuned beyond the defaults, build a custom retriever in Data 360 yourself. A `RETRIEVER` library can then expose it to agents with no upload step.[^s3][^s4] Because files must sit in the default data space, orgs that split data across data spaces should plan for that limit.[^s3]

## Connections

The library is a packaged form of `kt:retrieval-augmented-generation-in-salesforce` for `kt:agentforce`, which is why both are listed as broader nodes.[^s1] It **depends on** `kt:data-cloud` and generates `kt:data-streams`, `kt:data-model-objects` and a `kt:vector-search-in-data-cloud` index, much of it built from `kt:unstructured-data-in-data-cloud`.[^s1][^s4] Its retriever is used through prompt templates in `kt:prompt-builder`.[^s1] It often sits on a `kt:knowledge-base`.[^s4] It is **configured via** Agentforce Builder in `kt:agentforce-studio` and **queried with** the `kt:connect-api`.[^s2][^s3] The Agentforce Specialist exam's Data Cloud for Agentforce section (20%) covers using data libraries to improve answer accuracy, so the node is **covered by** `kt:agentforce-specialist-certification`.[^s5]

## Sources

[^s1]: Trailhead, "Upgrade AI with Real-World Data". https://trailhead.salesforce.com/content/learn/modules/agentforce-data-library-basics/upgrade-ai-with-real-world-data (accessed 2026-11-13)
[^s2]: Trailhead, "Build a File-Based Data Library for an Agent". https://trailhead.salesforce.com/content/learn/modules/agentforce-data-library-basics/build-a-file-based-data-library-for-an-agent (accessed 2026-11-13)
[^s3]: Salesforce Developers, "Agentforce Data Libraries resources", Connect REST API Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/connect_resources_adl.htm (accessed 2026-11-13)
[^s4]: Trailhead, "Use Knowledge in Agentforce for Service". https://trailhead.salesforce.com/content/learn/modules/agentforce-service-agent-quick-look/use-knowledge-in-agentforce-for-service (accessed 2026-11-13)
[^s5]: Trailhead, "Get Started with Salesforce Agentforce Specialist Certification Prep". https://trailhead.salesforce.com/content/learn/modules/cert-prep-agentforce-specialist/get-started-with-salesforce-agentforce-specialist-certification-prep (accessed 2026-11-13)
[^s6]: Salesforce Developers, "Manage Data Libraries with the ADL API", Agentforce Developer Guide. https://developer.salesforce.com/docs/ai/agentforce/guide/adl.html (accessed 2026-11-13)
