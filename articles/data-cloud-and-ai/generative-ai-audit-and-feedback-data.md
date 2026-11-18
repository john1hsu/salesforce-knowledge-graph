---
id: kt:generative-ai-audit-and-feedback-data
type: Feature
title: Generative AI Audit and Feedback Data
aliases: [Einstein Generative AI Audit and Feedback Data, Einstein audit and feedback data model, GenAI audit trail, Einstein Generative AI Data Collection]
domain: data-cloud-and-ai
summary: >-
  The opt-in data collection that stores a record of every Einstein generative AI and Agentforce LLM call
  (prompts, masked prompts, responses, safety scores, tags and user feedback) as standard GenAI data model
  objects in Data 360, where admins report on, query and alert on it.
release: "Winter '27"
status: current
broader: [kt:data-model-objects]
related: [kt:agentforce, kt:prompt-builder, kt:data-lake-objects]
relations:
  - {predicate: partOf, object: kt:einstein-trust-layer}
  - {predicate: dependsOn, object: kt:data-cloud}
  - {predicate: consumedBy, object: kt:calculated-insights}
  - {predicate: integratesWith, object: kt:data-cloud-triggered-flows}
  - {predicate: queriedWith, object: kt:soql}
sources:
  - id: s1
    title: "Generative AI Audit & Feedback Data Model"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/data-models/guide/generative-ai-audit-feedback-dmos.html
    type: official-docs
    accessed: 2026-11-18
  - id: s2
    title: "The Einstein Audit and Feedback Data Model in Data Cloud"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/07/the-einstein-audit-and-feedback-data-model-in-data-cloud
    type: official-blog
    accessed: 2026-11-18
  - id: s3
    title: "Discover Insights from Einstein Generative AI Audit and Feedback Data"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/search-analytics-for-ai-generated-search-answers/discover-insights-from-einstein-generative-ai-audit-and-feedback-data
    type: official-learning
    accessed: 2026-11-18
  - id: s4
    title: "How to Create a Continuous Optimization Loop with Salesforce Einstein and Data Cloud"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2024/how-to-create-a-continuous-optimization-loop-with-salesforce-einstein-and-data-cloud
    type: official-blog
    accessed: 2026-11-18
  - id: s5
    title: "Enable Trusted Agents with Data Cloud"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-cloud-powered-agentforce/enable-trusted-agents-with-data-cloud
    type: official-learning
    accessed: 2026-11-18
created: 2026-11-18
---

# Generative AI Audit and Feedback Data

Generative AI audit and feedback data is the record Salesforce keeps of what happens when an Einstein generative AI feature or an Agentforce agent calls a large language model. It captures the prompt (raw and with PII masked), request parameters, the model used, request tags, the generated output, safety scores and what the user did with the result, and stores all of it in Data 360 (formerly Data Cloud).[^s2][^s5] Salesforce positions it, alongside the Einstein Trust Layer, as one of the two Data 360-powered guardrails for agents: the Trust Layer protects each call, and the audit trail lets you inspect calls after the fact.[^s5]

## Turning it on

Collection is opt-in. Einstein must be enabled and Data 360 fully provisioned; an admin then switches on **Einstein Generative AI Data Collection** in Einstein Setup, which also records consent to storing the data in Data 360.[^s4][^s3] Records flow into data lake objects and are mapped to the standard data model objects automatically, and the first data can take up to 24 hours to appear.[^s4] Switching collection off pauses the stream, so the paused period is simply missing from later reports.[^s4]

## The data model

Salesforce publishes the schema as a Data 360 data model with nine entities: GenAI Gateway Request, GenAI Request Tag, GenAI Gateway Response, GenAI Generation, GenAI Content Quality, GenAI Content Category, GenAI Feedback, GenAI Feedback Detail and GenAI App Generation.[^s1] In queries the objects carry the `__dlm` suffix (for example `GenAIGatewayRequest__dlm`) and custom fields end in `__c`.[^s2][^s3] They fall into three groups:[^s2]

- **Request and response**: the gateway request, its tags, the gateway response and the individual generations.[^s2]
- **Content quality**: a summary safety verdict per generation, plus per-category scores from 0.0 to 1.0.[^s2]
- **Feedback**: explicit and implicit feedback, edit details, and app-level transformed outputs.[^s2]

One request can produce one or many generations, and each generation can have zero or many feedback records; tags hang off the request, content quality hangs off a generation, and content categories hang off content quality.[^s2] The eight scored safety categories are toxicity, hate, identity, violence, physical, sexual, profanity and biased, with higher scores meaning the category is more likely present.[^s2] Feedback covers thumbs up or down with optional reason text, and implicit signals such as accepting, regenerating, editing or ignoring a response, including the edited text that was finally used.[^s5][^s2] GenAI App Generation records cases where an app transforms the model output before display, such as translating it or splitting it into several outputs.[^s2]

## Reporting and analysis

Salesforce ships a reports package and a Data 360 dashboard, the Einstein Generative AI and Feedback Data Dashboard, showing weekly users, request volume, thumbs up and down, and tokens used.[^s4] Agentforce Analytics adds prebuilt dashboards on masking, toxicity, user trends and acceptance rates, also processed in Data 360.[^s5] For ad hoc work, the Data 360 Query Editor runs ANSI SQL over the DMOs, for example to join prompts, responses and feedback or to find generations above a violence-score threshold.[^s2] Calculated insights can aggregate the data, such as feedback counts per interaction or prompt text by day, and feed custom Analytics Studio dashboards.[^s3] Pairing a scheduled calculated insight with a Data 360-triggered flow lets you alert, for example when negative feedback passes a threshold.[^s4]

## Gotchas

- **Fan-out in joins.** Because requests have many generations and generations many feedback rows, joins repeat request IDs; deduplicate before counting.[^s2]
- **Tags drift.** Tag keys and values are free-form, can change as features evolve, and dictionary values are stored as JSON strings, so saved queries need maintenance.[^s2]
- **Scores and masking are probabilistic.** Safety scores are likelihoods, not verdicts, and PII detection runs with a confidence score and can miss or over-mask.[^s2]
- **Implicit feedback is ambiguous.** An ignored response might be a rejection, or the user might simply not have needed it.[^s2]
- **Data 360 is mandatory.** Without a provisioned Data 360 org there is nowhere to store the data, so plan Data 360 setup before go-live.[^s3][^s4]

## When to use it

Turn collection on before an AI rollout reaches users, so you have a baseline. Use it to tune prompt templates by comparing feedback per template tag, to show compliance teams which prompts carried masked data, and to watch toxicity trends over time.[^s2][^s4] Its scope is the AI interaction itself: what the model was sent, what it returned, how safe the output scored and whether people accepted it.[^s5][^s2]

## Connections

The data model sits **broader** under **data model objects**, since it is a set of standard Data 360 DMOs fed from **data lake objects**.[^s1][^s4] It is **part of** the **Einstein Trust Layer**, whose audit and feedback guardrail it implements, and it **depends on Data 360** for storage.[^s5] **Agentforce** agents and **Prompt Builder** templates generate the records it holds, and template tags are a key filter dimension.[^s2][^s5] **Calculated insights** consume it for aggregations, **Data 360-triggered flows** integrate with it for alerting, and the DMOs can also be **queried with SOQL** as well as SQL.[^s3][^s4][^s2]

## Sources
[^s1]: Salesforce Developers, "Generative AI Audit & Feedback Data Model". https://developer.salesforce.com/docs/platform/data-models/guide/generative-ai-audit-feedback-dmos.html (accessed 2026-11-18)
[^s2]: Salesforce Developers Blog, "The Einstein Audit and Feedback Data Model in Data Cloud". https://developer.salesforce.com/blogs/2024/07/the-einstein-audit-and-feedback-data-model-in-data-cloud (accessed 2026-11-18)
[^s3]: Trailhead, "Discover Insights from Einstein Generative AI Audit and Feedback Data". https://trailhead.salesforce.com/content/learn/modules/search-analytics-for-ai-generated-search-answers/discover-insights-from-einstein-generative-ai-audit-and-feedback-data (accessed 2026-11-18)
[^s4]: Salesforce Admins Blog, "How to Create a Continuous Optimization Loop with Salesforce Einstein and Data Cloud". https://admin.salesforce.com/blog/2024/how-to-create-a-continuous-optimization-loop-with-salesforce-einstein-and-data-cloud (accessed 2026-11-18)
[^s5]: Trailhead, "Enable Trusted Agents with Data Cloud". https://trailhead.salesforce.com/content/learn/modules/data-cloud-powered-agentforce/enable-trusted-agents-with-data-cloud (accessed 2026-11-18)
