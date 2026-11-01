---
id: kt:einstein-trust-layer
type: SecurityControl
title: Einstein Trust Layer
aliases: [Trust Layer, Salesforce Trust Layer, Agentforce Trust Layer, Einstein GPT Trust Layer]
domain: data-cloud-and-ai
summary: >-
  The secure AI architecture built into the Salesforce platform that wraps every generative AI request with
  permission-aware grounding, data masking, prompt defense, zero data retention at third-party LLMs, toxicity
  scoring and an audit trail stored in Data Cloud.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:agentforce, kt:prompt-builder, kt:salesforce-sharing-model]
relations:
  - {predicate: dependsOn, object: kt:data-cloud}
  - {predicate: mitigates, object: kt:prompt-injection}
  - {predicate: integratesWith, object: kt:tableau}
sources:
  - id: s1
    title: "Trust Layer (Agentforce Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/trust.html
    type: official-docs
    accessed: 2026-11-01
  - id: s2
    title: "Follow the Prompt Journey (The Einstein Trust Layer)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/the-einstein-trust-layer/follow-the-prompt-journey
    type: official-learning
    accessed: 2026-11-01
  - id: s3
    title: "Follow the Response Journey (The Einstein Trust Layer)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/the-einstein-trust-layer/follow-the-response-journey
    type: official-learning
    accessed: 2026-11-01
  - id: s4
    title: "The Einstein Audit and Feedback Data Model in Data Cloud"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/07/the-einstein-audit-and-feedback-data-model-in-data-cloud
    type: official-blog
    accessed: 2026-11-01
  - id: s5
    title: "AI in Tableau and the Einstein Trust Layer"
    publisher: Tableau (Salesforce)
    url: https://help.tableau.com/current/tableau/en-us/tableau_gai_einstein_trust_layer.htm
    type: official-docs
    accessed: 2026-11-01
created: 2026-11-01
---

# Einstein Trust Layer

The Einstein Trust Layer is the set of controls Salesforce places between its generative AI features and the large language models (LLMs) they call. It combines contractual agreements with model providers, security technology, and data and privacy controls, and products such as Agentforce and AI in Tableau inherit it rather than reimplementing their own safeguards.[^s5] Salesforce frames the protections as grounding in CRM data, masking of sensitive values, toxicity detection, an audit trail with feedback, and zero data retention at third-party providers.[^s1]

## How it works: the prompt journey

A request passes through several stages before it reaches a model. **Secure data retrieval** pulls the record and org data the prompt needs while honouring the running user's existing permissions, so the model only sees what that user is entitled to see.[^s2] **Dynamic grounding** then fills placeholders in a prompt template with page context, merge fields and relevant knowledge articles, which lets one template be reused across an org; **semantic search** can add relevant passages from other sources such as knowledge or customer history.[^s2]

Next, **data masking** tokenizes sensitive values such as names, addresses and card numbers, replacing each with a typed placeholder (for example `<NAME_1>`) so the LLM keeps context without seeing real values.[^s2] Tableau describes this masking as pattern-based and supporting multiple regions and languages.[^s5] **Prompt defense** appends guardrail instructions that tell the model how to behave, for instance not answering when it lacks data, which reduces harmful output and helps resist prompt injection.[^s2] The prompt then crosses a secure LLM gateway; Salesforce's agreements with providers such as OpenAI include **zero data retention** commitments, so third-party providers should not keep customer data.[^s1][^s2] Tableau adds that this data is not used for model training and is not viewed by humans.[^s5]

## The response journey

On the way back, ML models score the prompt and response for **toxicity** across several categories and roll the results into a single score between 0 and 1, where higher is more toxic; the score is returned to the calling app.[^s3] **Demasking** uses the saved token map to restore the real values so users see a personalized reply.[^s3] A **feedback framework** captures whether the user accepted, edited or ignored the output, plus thumbs up or down with a reason.[^s3] Finally, an **audit trail** logs every step as timestamped metadata, including the prompt, the original unfiltered response, toxicity scores and feedback.[^s3]

That audit and feedback data is stored in Data Cloud, where it can be queried with Data Cloud tools such as the Query Editor.[^s4] It lands in data model objects including `GenAIGatewayRequest`, `GenAIGatewayResponse`, `GenAIGeneration`, `GenAIContentQuality`, `GenAIContentCategory`, `GenAIFeedback` and `GenAIFeedbackDetail`, and content-quality checks record 0.0–1.0 scores in eight categories: toxicity, hate, identity, violence, physical, sexual, profanity and bias.[^s4]

## Limits and gotchas

- **Masking is not universal.** Admins can enable masking for embedded features such as Service Replies and Work Summaries, but it is disabled for agents, so agent designs must rely on permissions and grounding scope instead.[^s2]
- **Audit needs Data Cloud.** Because audit data lives in Data Cloud data model objects, analysing it means working in Data Cloud; in Tableau the audit control is available with Tableau+ only.[^s4][^s5]
- **Humans stay accountable.** Salesforce recommends that a person check model responses before sharing them for most use cases, and the customer remains responsible for what is sent.[^s1]
- Prompt-defense policies can vary by feature and use case, so behaviour is not identical across every AI surface.[^s5]

## When to rely on it

Treat the Trust Layer as the platform baseline for any Salesforce-native generative AI: it enforces record-level access, keeps data out of provider retention, and gives compliance teams an auditable record.[^s2][^s3] It does not replace good data security design; if a user can over-see data through sharing, grounding will faithfully over-share it too, because retrieval follows the user's permissions.[^s2]

## Connections

The Trust Layer sits **broader** under the Salesforce platform because it is shared infrastructure for every AI feature rather than a product of its own.[^s5] **Agentforce** and **Prompt Builder** templates depend on it for grounding, masking and gateway calls, and its secure retrieval inherits the **Salesforce sharing model**, which is why those nodes are related.[^s2] It **depends on Data Cloud** for its audit and feedback store,[^s4] it **mitigates prompt injection** through prompt defense,[^s2] and it **integrates with Tableau**, whose AI features are built on the same layer.[^s5]

## Sources
[^s1]: Salesforce Developers, "Trust Layer (Agentforce Developer Guide)". https://developer.salesforce.com/docs/ai/agentforce/guide/trust.html (accessed 2026-11-01)
[^s2]: Trailhead, "Follow the Prompt Journey (The Einstein Trust Layer)". https://trailhead.salesforce.com/content/learn/modules/the-einstein-trust-layer/follow-the-prompt-journey (accessed 2026-11-01)
[^s3]: Trailhead, "Follow the Response Journey (The Einstein Trust Layer)". https://trailhead.salesforce.com/content/learn/modules/the-einstein-trust-layer/follow-the-response-journey (accessed 2026-11-01)
[^s4]: Salesforce Developers Blog, "The Einstein Audit and Feedback Data Model in Data Cloud". https://developer.salesforce.com/blogs/2024/07/the-einstein-audit-and-feedback-data-model-in-data-cloud (accessed 2026-11-01)
[^s5]: Tableau, "AI in Tableau and the Einstein Trust Layer". https://help.tableau.com/current/tableau/en-us/tableau_gai_einstein_trust_layer.htm (accessed 2026-11-01)
