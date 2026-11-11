---
id: kt:retrieval-augmented-generation-in-salesforce
type: Pattern
title: Retrieval Augmented Generation in Salesforce
aliases: [RAG in Salesforce, Salesforce RAG, Data 360 RAG, Data Cloud RAG, grounding with retrievers]
domain: data-cloud-and-ai
summary: >-
  The Salesforce implementation of retrieval-augmented generation: Data 360 chunks and vectorizes content into a
  search index, a retriever pulls the most relevant chunks at runtime, and Prompt Builder or Agentforce inserts
  them into the prompt so the LLM answers from the organization's own data.
release: "Winter '27"
status: current
broader: [kt:data-cloud, kt:generative-ai]
related: [kt:agentforce, kt:agent-actions, kt:knowledge-base, kt:data-model-objects, kt:einstein-trust-layer, kt:vector-search-in-data-cloud]
relations:
  - {predicate: dependsOn, object: kt:data-cloud}
  - {predicate: configuredVia, object: kt:prompt-builder}
  - {predicate: consumedBy, object: kt:atlas-reasoning-engine}
  - {predicate: hasPart, object: kt:agentforce-data-library}
sources:
  - id: s1
    title: "Augment Prompts with Relevant Knowledge (Retrieval Augmented Generation: Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/it/content/learn/modules/retrieval-augmented-generation-quick-look/augment-prompts-with-relevant-knowledge
    type: official-learning
    accessed: 2026-11-07
  - id: s2
    title: "Retrievers and Retriever Versions"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=data.c360_a_ai_retriever_version.htm
    type: official-docs
    accessed: 2026-11-07
  - id: s3
    title: "Create a Search Index, Retriever, and Prompt Template (Advanced RAG with Data 360 and Agentforce)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/advanced-rag-with-data-360-and-agentforce/create-a-search-index-retriever-and-prompt-template
    type: official-learning
    accessed: 2026-11-07
  - id: s4
    title: "Upgrade AI with Real-World Data (Agentforce Data Library Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agentforce-data-library-basics/upgrade-ai-with-real-world-data
    type: official-learning
    accessed: 2026-11-07
  - id: s5
    title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (NeurIPS 2020)"
    publisher: Advances in Neural Information Processing Systems 33
    url: https://papers.nips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-07
created: 2026-11-07
---

# Retrieval Augmented Generation in Salesforce

Retrieval-augmented generation (RAG) grounds a large language model's prompt in context it was never trained on. Generic LLMs learn from static public text, so Salesforce uses RAG to add domain knowledge and customer information, such as Knowledge articles, cases, call transcripts, RFP answers, emails and FAQs, to the prompt before the model responds.[^s1] The technique comes from research by Lewis et al., which paired a pre-trained generator (parametric memory) with a neural retriever over a dense vector index (non-parametric memory). That combination beat parametric-only models on open-domain question answering and produced more specific, factual text.[^s5]

## How it works

Salesforce splits RAG into an offline preparation stage and an online retrieval stage, both built on Data 360 (formerly Data Cloud).[^s1]

**Offline.** Content is ingested into Data 360, and a **search index** is built over it. The index splits text into chunks along natural passages such as sentences or paragraphs. Each chunk is then vectorized into a numeric embedding that captures semantic meaning.[^s1] Two index types are offered: **vector search**, and **hybrid search**, which combines semantic similarity with keyword matching.[^s1][^s3] Indexing a data model object creates companion objects, such as a chunk object and an index object for Case, that you can inspect in Data Explorer when answers look wrong.[^s3]

**Retrievers.** A retriever, managed in AI Models (formerly Einstein Studio), queries an index and returns the relevant content for one use case.[^s1][^s2] Salesforce offers three kinds:

- **Individual retrievers** point at one search index and set filters and return fields.[^s2]
- **Ensemble retrievers** combine several individual retrievers, merge their results, rerank them by relevance and return the best matches.[^s2]
- **Custom SQL retrievers** query Data 360 objects with a parameterized SQL statement and configured citations.[^s2]

**Online.** A prompt template in Prompt Builder embeds a retriever as a resource and passes it a dynamic query. Retrieved chunks are merged into the prompt, and the augmented prompt goes to the LLM. Queries and the index use the same embedding model.[^s1] In Agentforce, the *Answer Questions with Knowledge* action runs the same loop through a prompt template that calls the retriever.[^s1] An **Agentforce Data Library** packages this setup. From Knowledge articles, uploaded files, websites or transcripts, it creates the data streams, data model objects, chunked search index and a dedicated retriever.[^s4]

## Limits and gotchas

- **Permission-aware results.** Retrievers follow data governance policies. A record that the running user or agent can't access is left out of the results.[^s2]
- **Versioning.** Each saved edit to a custom retriever creates a new version. Only one version can be active at a time, and you can't delete a version while a prompt template depends on it. Only individual retrievers can be edited.[^s2]
- **Indexing takes time.** In the Trailhead walkthrough, learners wait about 20 minutes for an index to reach *Ready*.[^s3] Data Library setup time grows with the number and size of articles or files and with how many fields are chunked.[^s4]
- **Tune result counts.** The walkthrough retriever defaults to 20 results, while its prompt template asks for 5. More chunks mean more tokens and more noise in the prompt.[^s3]
- **Constrain the model.** The same template tells the LLM to answer only from retrieved chunks, cite a source ID, and return a fixed apology when nothing matches. Salesforce presents this as a way to avoid hallucinations.[^s3]

## When to use it (and when not)

Use RAG when answers depend on large or changing bodies of unstructured text that won't fit in a prompt, such as policies, manuals or past cases.[^s1][^s4] Index chunking exists because LLMs have token limits.[^s4] For a single record's fields, a direct merge field or flow resource in a prompt template is simpler than an index. For exact matches against structured data, a custom SQL retriever avoids semantic search altogether.[^s2]

## Connections

RAG is **part of** the `kt:data-cloud` (Data 360) platform and **depends on** its ingestion, `kt:data-model-objects` and search indexes.[^s1][^s3] It is **configured via** `kt:prompt-builder`, where retrievers are added to templates as resources.[^s3] `kt:agentforce` uses it through `kt:agent-actions` such as *Answer Questions with Knowledge*.[^s1] The `kt:atlas-reasoning-engine` **uses** RAG as one of its grounding techniques, as documented on that node. A `kt:agentforce-data-library` is the packaged, low-configuration form, often fed by `kt:knowledge-base` articles.[^s4] Retrievers enforce record access on their results,[^s2] which complements the prompt-level safeguards of the `kt:einstein-trust-layer`. The pattern itself is the Salesforce form of the general `kt:generative-ai` technique introduced by Lewis et al.[^s5]

## Sources

[^s1]: Trailhead, "Augment Prompts with Relevant Knowledge". https://trailhead.salesforce.com/it/content/learn/modules/retrieval-augmented-generation-quick-look/augment-prompts-with-relevant-knowledge (accessed 2026-11-07)
[^s2]: Salesforce Help, "Retrievers and Retriever Versions". https://help.salesforce.com/apex/HTViewHelpDoc?id=data.c360_a_ai_retriever_version.htm (accessed 2026-11-07)
[^s3]: Trailhead, "Create a Search Index, Retriever, and Prompt Template". https://trailhead.salesforce.com/content/learn/modules/advanced-rag-with-data-360-and-agentforce/create-a-search-index-retriever-and-prompt-template (accessed 2026-11-07)
[^s4]: Trailhead, "Upgrade AI with Real-World Data". https://trailhead.salesforce.com/content/learn/modules/agentforce-data-library-basics/upgrade-ai-with-real-world-data (accessed 2026-11-07)
[^s5]: Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks", NeurIPS 2020. https://papers.nips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html (accessed 2026-11-07)
