---
id: kt:vector-search-in-data-cloud
type: Feature
title: Vector Search in Data 360
aliases: [Vector Search in Data Cloud, Data 360 search index, Data Cloud search index, hybrid search in Data 360, enriched search index, semantic search in Data 360]
domain: data-cloud-and-ai
summary: >-
  The Data 360 search index feature that chunks text from data model objects, embeds each chunk as a vector,
  and serves semantic (vector), hybrid (vector plus keyword) or enriched retrieval to retrievers, Agentforce,
  Prompt Builder, Flow and Tableau.
release: "Winter '27"
status: current
broader: [kt:data-cloud]
related: [kt:retrieval-augmented-generation-in-salesforce, kt:ai-models, kt:data-lake-objects, kt:unstructured-data-in-data-cloud]
relations:
  - {predicate: dependsOn, object: kt:data-model-objects}
  - {predicate: consumedBy, object: kt:retrieval-augmented-generation-in-salesforce}
  - {predicate: consumedBy, object: kt:agentforce}
  - {predicate: configuredVia, object: kt:data-cloud-code-extension}
  - {predicate: contrastsWith, object: kt:sosl}
sources:
  - id: s1
    title: "Get to Know Search Index Types in Data Cloud (Search Index Types in Data Cloud: Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/search-index-types-data-cloud-quick-look/get-to-know-search-index-types-in-data-cloud
    type: official-learning
    accessed: 2026-11-11
  - id: s2
    title: "Create a Search Index Configuration (Unstructured Data in Data Cloud)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/unstructured-data-in-data-cloud/create-a-search-index-configuration
    type: official-learning
    accessed: 2026-11-11
  - id: s3
    title: "Step 3: Create Search Index and Retriever (Ground Agentforce on Website Content)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/ai/ground-agentforce-on-website/guide/aes-create-search-index-and-retriever.html
    type: official-docs
    accessed: 2026-11-11
  - id: s4
    title: "Use a Custom Chunking Function in a Search Index"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-code-ext/guide/use-chunking-in-search-index.html
    type: official-docs
    accessed: 2026-11-11
  - id: s5
    title: "How Data Cloud Hybrid Search Combines Keyword and Vector Retrieval to Elevate the Search Experience"
    publisher: Salesforce Engineering
    url: https://engineering.salesforce.com/how-data-cloud-hybrid-search-combines-keyword-and-vector-retrieval-to-elevate-the-search-experience/
    type: official-blog
    accessed: 2026-11-11
  - id: s6
    title: "Pro-Code Chunking of Data 360 Search Indexes for Agentforce"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2026/09/pro-code-chunking-of-data-360-search-indexes-for-agentforce
    type: official-blog
    accessed: 2026-11-11
created: 2026-11-11
---

# Vector Search in Data 360

Vector search in Data 360 (formerly Data Cloud) is delivered through **search indexes**. A search index splits text from unstructured, semi-structured or structured data into chunks, turns each chunk into a vector embedding, and lets applications find the chunks closest in meaning to a query.[^s1] It is the retrieval layer that grounds generative AI in Agentforce, Prompt Builder, Flow Builder and Tableau on an organization's own content.[^s1][^s2]

## Index types

Data 360 offers three kinds of search index:[^s1]

- **Vector search** returns chunks whose embeddings are semantically close to the query. It suits long, general questions; Trailhead's rule of thumb is that queries over about five words do well with vector search alone.[^s1]
- **Hybrid search** runs vector search and keyword search together, merges the two result sets with a fusion ranker, and returns a hybrid score plus separate keyword and vector scores. It helps when queries mix general meaning with exact, domain-specific terms.[^s1]
- **Enriched indexes** add LLM-generated metadata (keywords, entities, summaries) and generated questions to a vector or hybrid index. Each source chunk becomes three chunks (plain, metadata and question), and generating them consumes Flex Credits.[^s1]

There is no keyword-only index type; keyword matching exists as half of hybrid search.[^s1]

## How an index is built

In Advanced Setup you pick the search type, choose the source data model object (DMO) or unstructured DMO, and select the text fields to chunk with Manage Fields.[^s2][^s4] You then choose a chunking strategy. Options named in Salesforce material include semantic-based passage extraction (splits at headings, lists and bold subheadings), window-based passage extraction (splits at block elements or line breaks, or by sentence for plain text) and section-aware chunking.[^s2][^s3][^s6] Next comes the vectorization strategy, meaning the embedding model, plus optional filter fields and the index name.[^s2][^s4]

Salesforce's website-grounding guide shows hybrid search with section-aware chunking at 1,200 max tokens, zero overlap tokens, the title prepended to every chunk, and the Salesforce Embedding V2 Small model, which supports 1,200-token chunks. The guide warns that a smaller chunk size such as 512 tokens needs an embedding model with a matching sequence length.[^s3]

Saving the configuration produces a chunk DMO holding the text chunks and index DMOs holding the embeddings. The run moves from Submitted to In Progress to Ready, which can take several minutes, and Process History shows records processed and chunks created.[^s2] Chunks can be inspected as data lake objects in Data Explorer.[^s3] In SQL, the `vector_search()` and `hybrid_search()` table functions return scores that you join back to the chunk object.[^s1]

## Hybrid ranking under the hood

Keyword and vector similarity scores come from different distributions, so Salesforce Engineering normalizes them before fusing them. The transforms it describes are a query max scaler and a reciprocal rank transform. Fusion then uses either reciprocal rank fusion, with a decay of 60 and customizable index weights, or an optimized linear fusion ranker with trained weights. Popularity and recency can act as tie-breakers. In Salesforce's evaluations, hybrid beat keyword-only and vector-only retrieval on passage ranking and RAG-style question answering.[^s5]

## Custom chunking with Code Extension

When native chunking mangles complex PDFs, dense tables or multi-speaker transcripts, you can write a chunking function in Python with the Data Custom Code SDK. Functions run sandboxed and stateless inside the Salesforce trust boundary and are deployed with the Salesforce CLI or the UI.[^s6] Once a function shows Deployed, you select **Code Extension** as a field's chunking strategy and pick the function by name. This requires the Data Cloud Architect permission set and is offered in Developer, Enterprise, Performance and Unlimited editions.[^s4] Salesforce presents Code Extension as an escalation path, not a replacement for native chunking.[^s6]

## Gotchas

- **Chunk size must fit the model.** Max tokens and the embedding model's sequence length are coupled; change one and check the other.[^s3]
- **No content, no chunks.** Only content already ingested into the selected DMO is chunked, so failed uploads silently yield nothing.[^s4]
- **Enrichment costs credits.** Weigh the retrieval gain from an enriched index against the extra LLM cost.[^s1]
- **Pick by query style.** Short, term-heavy queries favor hybrid search; long natural-language questions often do fine with vector search alone.[^s1]

## Connections

A search index is a feature of `kt:data-cloud` and **depends on** `kt:data-model-objects` (or unstructured DMOs, see `kt:unstructured-data-in-data-cloud`) for its source text. Its chunks and embeddings are stored as `kt:data-lake-objects`.[^s2][^s3] Retrievers managed in `kt:ai-models` query the index, which is how `kt:retrieval-augmented-generation-in-salesforce` and `kt:agentforce` **consume** it.[^s1][^s3] Custom chunking is **configured via** `kt:data-cloud-code-extension`.[^s4] Its semantic matching **contrasts with** the keyword-only full-text search of `kt:sosl` on core CRM records; hybrid search combines both ideas inside Data 360.[^s5]

## Sources

[^s1]: Trailhead, "Get to Know Search Index Types in Data Cloud". https://trailhead.salesforce.com/content/learn/modules/search-index-types-data-cloud-quick-look/get-to-know-search-index-types-in-data-cloud (accessed 2026-11-11)
[^s2]: Trailhead, "Create a Search Index Configuration". https://trailhead.salesforce.com/content/learn/projects/unstructured-data-in-data-cloud/create-a-search-index-configuration (accessed 2026-11-11)
[^s3]: Salesforce Developers, "Step 3: Create Search Index and Retriever". https://developer.salesforce.com/docs/ai/ground-agentforce-on-website/guide/aes-create-search-index-and-retriever.html (accessed 2026-11-11)
[^s4]: Salesforce Developers, "Use a Custom Chunking Function in a Search Index". https://developer.salesforce.com/docs/data/data-cloud-code-ext/guide/use-chunking-in-search-index.html (accessed 2026-11-11)
[^s5]: Salesforce Engineering, "How Data Cloud Hybrid Search Combines Keyword and Vector Retrieval". https://engineering.salesforce.com/how-data-cloud-hybrid-search-combines-keyword-and-vector-retrieval-to-elevate-the-search-experience/ (accessed 2026-11-11)
[^s6]: Salesforce Developers Blog, "Pro-Code Chunking of Data 360 Search Indexes for Agentforce". https://developer.salesforce.com/blogs/2026/09/pro-code-chunking-of-data-360-search-indexes-for-agentforce (accessed 2026-11-11)
