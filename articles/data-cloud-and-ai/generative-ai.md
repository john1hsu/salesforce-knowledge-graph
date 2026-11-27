---
id: kt:generative-ai
type: ExternalConcept
title: Generative AI
aliases: [GenAI, GAI, generative artificial intelligence, generative foundation models]
domain: data-cloud-and-ai
summary: >-
  The class of AI models that learn the patterns of their training data and produce new text, images, audio or
  code from a prompt; built mostly on transformer-based foundation models such as large language models, it is
  the general technique underneath Agentforce, Prompt Builder and retrieval augmented generation in Salesforce.
release: "Winter '27"
status: concept
broader: [kt:artificial-intelligence, kt:computer-science]
related: [kt:retrieval-augmented-generation-in-salesforce, kt:einstein-trust-layer, kt:prompt-injection, kt:ai-models]
relations:
  - {predicate: hasPart, object: kt:large-language-models}
  - {predicate: consumedBy, object: kt:agentforce}
  - {predicate: consumedBy, object: kt:prompt-builder}
sources:
  - id: s1
    title: "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1)"
    publisher: National Institute of Standards and Technology
    url: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
    type: standards-body
    accessed: 2026-11-27
  - id: s2
    title: "Attention Is All You Need"
    publisher: arXiv:1706.03762, Ashish Vaswani et al.
    url: https://arxiv.org/abs/1706.03762
    type: peer-reviewed
    accessed: 2026-11-27
  - id: s3
    title: "Explore the Capabilities of Generative AI (Generative AI Basics)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/generative-ai-basics/explore-the-capabilities-of-generative-ai
    type: official-learning
    accessed: 2026-11-27
  - id: s4
    title: "Understand the Technology Ecosystem of Generative AI (Generative AI Basics)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/generative-ai-basics/understand-the-technology-ecosystem-of-generative-ai
    type: official-learning
    accessed: 2026-11-27
  - id: s5
    title: "Learn the Basics of Large Language Models (Large Language Models)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/large-language-models/learn-the-basics-of-large-language-models
    type: official-learning
    accessed: 2026-11-27
created: 2026-11-27
---

# Generative AI

**Generative AI** (GenAI, or GAI in NIST usage) is the branch of artificial intelligence whose models create new content rather than returning a single score or label. NIST's Generative AI Profile adopts the U.S. executive-order description of GAI as models that "emulate the structure and characteristics of input data", and notes that in practice the term mostly means generative foundation models.[^s1] Salesforce's own training draws the same line: a classic predictive model might output one number, such as an estimated house price, while a generative model produces text, images or sound it has never seen before.[^s3]

## How it works

Most current generative systems are built on the **transformer**, an architecture introduced in 2017 by Vaswani and seven co-authors. It relies entirely on attention mechanisms and drops the recurrence and convolution used by earlier sequence models; on WMT 2014 translation it reached 28.4 BLEU for English-to-German and 41.8 BLEU for English-to-French.[^s2] Because attention relates words across long distances and parallelises well, transformers made it practical to train on very large text corpora.[^s2][^s4]

Trailhead attributes the rapid progress of GenAI to three drivers: huge volumes of training data such as web pages, better training methods (the transformer), and abundant parallel compute.[^s4] A **large language model** trained this way learns statistical patterns of language and generates output one token at a time, each token being a prediction of what comes next; models commonly hold billions of learned parameters.[^s5] A pre-trained model can then be **fine-tuned** on a smaller, task-specific dataset, which needs far less data and compute than training from scratch.[^s5] Generated text is still a form of prediction, not evidence that the model thinks or holds opinions.[^s3]

Typical capabilities include summarisation, translation (including from natural language to code), error correction, question answering, guided image generation and text-to-speech.[^s3] The technology stack has several layers: some vendors specialise in training foundation models, others build applications on top of them or span multiple layers.[^s4]

## Risks and gotchas

NIST AI 600-1, published in July 2024 as a companion profile to the AI Risk Management Framework (AI RMF 1.0), lists twelve risks that are unique to or worsened by GAI. They include confabulation, data privacy, information integrity, information security, intellectual property, harmful bias or homogenization, human-AI configuration, environmental impacts, and value chain and component integration.[^s1] Trailhead names a similar practitioner set: hallucinations that diverge from facts, exposure of proprietary data during fine-tuning or prompting, plagiarism of training material, spoofed bot profiles, and the energy and water cost of large models.[^s4] The practical rule is to verify generated output and treat the model as a tool, not an infallible source of truth.[^s4][^s5]

## When it fits (and when not)

Use generative AI for open-ended language tasks: drafting replies, summarising records, answering questions over knowledge, or turning instructions into actions.[^s3] For a single numeric or categorical prediction, such as a churn score, a conventional predictive model is usually the simpler and more explainable choice, which is the distinction Trailhead draws between the two model families.[^s3] Where answers must reflect current, company-specific facts, ground the model in retrieved data rather than relying on training data alone, because incomplete or biased training data is one cause of hallucinations.[^s4]

## Connections

Generative AI is a subfield of `kt:artificial-intelligence` and, more broadly, of `kt:computer-science`, and **has part** `kt:large-language-models`, the transformer-based models that dominate the field.[^s2][^s5] On the Salesforce Platform it is **consumed by** `kt:agentforce` and `kt:prompt-builder`, and `kt:ai-models` is where customers connect or bring their own models. `kt:retrieval-augmented-generation-in-salesforce` is the Salesforce form of grounding generation in retrieved data. The data-exposure concern Trailhead raises is the one the `kt:einstein-trust-layer` is designed to address,[^s4] while `kt:prompt-injection` is a security risk specific to systems that act on model prompts, falling under NIST's information-security category.[^s1]

## Sources

[^s1]: National Institute of Standards and Technology, "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1)". https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf (accessed 2026-11-27)
[^s2]: Vaswani et al., "Attention Is All You Need", arXiv:1706.03762. https://arxiv.org/abs/1706.03762 (accessed 2026-11-27)
[^s3]: Salesforce Trailhead, "Explore the Capabilities of Generative AI". https://trailhead.salesforce.com/content/learn/modules/generative-ai-basics/explore-the-capabilities-of-generative-ai (accessed 2026-11-27)
[^s4]: Salesforce Trailhead, "Understand the Technology Ecosystem of Generative AI". https://trailhead.salesforce.com/content/learn/modules/generative-ai-basics/understand-the-technology-ecosystem-of-generative-ai (accessed 2026-11-27)
[^s5]: Salesforce Trailhead, "Learn the Basics of Large Language Models". https://trailhead.salesforce.com/content/learn/modules/large-language-models/learn-the-basics-of-large-language-models (accessed 2026-11-27)
