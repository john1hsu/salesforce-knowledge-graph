---
id: kt:ai-models
type: Feature
title: AI Models
aliases: [Model Builder, Einstein Studio, Einstein 1 Studio Model Builder, Data 360 AI Models, bring your own model, BYOM, bring your own LLM, BYOLLM]
domain: data-cloud-and-ai
summary: >-
  The Data 360 (Data Cloud) workspace, formerly Einstein Studio and its Model Builder, where teams build no-code
  predictive models on harmonized data, connect externally hosted predictive models (BYOM) and large language
  models (BYOLLM), and configure, test and manage the models that predictions, prompts and agents use.
release: "Winter '27"
status: current
broader: [kt:data-cloud]
related: [kt:agentforce-studio, kt:retrieval-augmented-generation-in-salesforce]
relations:
  - {predicate: dependsOn, object: kt:data-model-objects}
  - {predicate: dependsOn, object: kt:einstein-trust-layer}
  - {predicate: consumedBy, object: kt:prompt-builder}
  - {predicate: integratesWith, object: kt:flow-builder}
  - {predicate: enables, object: kt:data-cloud-segmentation}
  - {predicate: queriedWith, object: kt:models-api}
sources:
  - id: s1
    title: "Get to Know Einstein Studio (Build AI Models in Einstein Studio)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/build-ai-models-in-einstein-studio/get-to-know-einstein-studio
    type: official-learning
    accessed: 2026-11-10
  - id: s2
    title: "Bring Your Own Large Language Model in Einstein 1 Studio"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/03/bring-your-own-large-language-model-in-einstein-1-studio
    type: official-blog
    accessed: 2026-11-10
  - id: s3
    title: "Get Started with AI Models (Agentforce Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/get-started-einstein-studio.html
    type: official-docs
    accessed: 2026-11-10
  - id: s4
    title: "Supported Models (Agentforce Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/supported-models.html
    type: official-docs
    accessed: 2026-11-10
  - id: s5
    title: "How to Build a Predictive AI Model in Data Cloud"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/07/how-to-build-a-predictive-ai-model-in-data-cloud
    type: official-blog
    accessed: 2026-11-10
  - id: s6
    title: "Use Model Builder to Integrate Databricks Models with Salesforce"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/03/use-model-builder-to-integrate-databricks-models-with-salesforce
    type: official-blog
    accessed: 2026-11-10
created: 2026-11-10
---

# AI Models

**AI Models** is the tab in Data 360 (formerly Data Cloud) that acts as the central place to create, connect,
manage and monitor an org's predictive and generative models, without requiring code or data-science skills.[^s1]
It was formerly called **Einstein Studio**, and older material calls it "Einstein 1 Studio" and its builder
**Model Builder**.[^s1][^s3][^s2][^s6] Because models are built on data already harmonized in Data 360, predictions
can flow into the same unified records that segments and activations use.[^s1][^s6]

## How it works

AI Models supports three ways to bring a model into Salesforce:[^s1]

- **Build from scratch**: a business user trains a predictive model with clicks on Data 360 data.[^s1][^s5]
- **Bring your own model (BYOM)**: connect a predictive model hosted on Amazon SageMaker, Google Vertex AI or Databricks; it stays on that platform and is called through an API.[^s1][^s6]
- **Bring your own LLM (BYOLLM)**: connect a foundation model from an external provider such as OpenAI, Azure OpenAI, Anthropic or Gemini models.[^s1][^s2]

**Predictive models.** The builder walks through choosing a data model object as the training source, optionally
filtering the training records, picking the outcome field and goal (maximize or minimize a value), and choosing
predictor attributes; it can choose the algorithm automatically, as when it picked XGBoost for a binary
classification example.[^s5] Supported capabilities are regression, which predicts a number, and binary
classification, which predicts one of two outcomes.[^s1] After training, the model shows a performance rating, an
AUC score for binary models or R-squared for regression, an ROC curve and top predictors; only an **active** model
can be used in flows or batch transforms.[^s1][^s5] Each model is labelled Custom, Connected or
Salesforce-Enabled by origin.[^s1]

**Connected (BYOM) models.** For an external model, you register its endpoint URL, authentication header and
input/output schema, activate it, then create a prediction job that maps Data 360 fields to the model's
predictors.[^s6] Results land in a prediction data model object related to the scored object; the job can run
on streaming updates when predictor values change or on a batch schedule.[^s6]

**Generative models.** AI Models lists Salesforce-managed model configurations and lets you add BYOLLM foundation
models, save tuned hyperparameters as named configured models and try prompts in Model Playground before
use.[^s2][^s3][^s4] In a Prompt Builder template, switching the model type from Standard to Custom selects a
configured model.[^s2]
BYOLLM providers are Amazon Bedrock, Azure OpenAI, OpenAI and Vertex AI, and the LLM Open Connector extends BYOLLM
to any other language model, including custom-built ones.[^s3][^s4] BYOLLM inference runs at the provider, but
requests still pass through the Models API and Trust Layer features still apply.[^s4]

## Limits and gotchas

- The no-code builder offers regression and binary classification only; other problem types need an external model.[^s1]
- An AUC that is "too high" can indicate data leakage or overfitting, so check predictors before activation.[^s1]
- Predictor field data types for a prediction job must match the fields in the scoring data model object.[^s6]
- Beta models show as disabled until enabled, and Salesforce advises enabling them only in sandbox or dev orgs.[^s4]
- Deprecated LLMs stay usable until their shutdown date, after which requests are rerouted to a replacement.[^s4]
- BYOLLM calls consume 30% fewer Einstein Requests than other models, which matters for consumption budgets.[^s4]

## When to use it (and when not)

Use the from-scratch builder when the outcome is a number or a yes/no and the training data already lives in
Data 360, such as lead conversion or attrition likelihood.[^s1][^s5] Choose BYOM when a data-science team already
trains models in SageMaker, Vertex AI or Databricks and only needs the scores in Salesforce.[^s1][^s6] Choose
BYOLLM when contracts, fine-tuning or data residency require a specific LLM provider; otherwise the
Salesforce-managed models need no provider account.[^s4]

## Connections

AI Models is part of `kt:data-cloud` and trains on, and writes predictions to, `kt:data-model-objects`.[^s5][^s6]
Prediction objects feed calculated insights and `kt:data-cloud-segmentation`, and a Data Cloud-triggered flow in
`kt:flow-builder` can act when a prediction changes.[^s6] Configured LLMs are **consumed by** `kt:prompt-builder`
templates.[^s2] Generative calls depend on the `kt:einstein-trust-layer` and are queried through the
`kt:models-api` from REST, Apex, Lightning web components and flows.[^s2][^s3][^s4] The models configured here
are the ones that grounded generation in `kt:retrieval-augmented-generation-in-salesforce` and agents built in
`kt:agentforce-studio` call, including the managed model mix Agentforce uses by default.[^s4]

## Sources

[^s1]: Trailhead, "Get to Know Einstein Studio (Build AI Models in Einstein Studio)". https://trailhead.salesforce.com/content/learn/modules/build-ai-models-in-einstein-studio/get-to-know-einstein-studio (accessed 2026-11-10)
[^s2]: Salesforce Developers Blog, "Bring Your Own Large Language Model in Einstein 1 Studio". https://developer.salesforce.com/blogs/2024/03/bring-your-own-large-language-model-in-einstein-1-studio (accessed 2026-11-10)
[^s3]: Salesforce Developers, "Get Started with AI Models (Agentforce Developer Guide)". https://developer.salesforce.com/docs/ai/agentforce/guide/get-started-einstein-studio.html (accessed 2026-11-10)
[^s4]: Salesforce Developers, "Supported Models (Agentforce Developer Guide)". https://developer.salesforce.com/docs/ai/agentforce/guide/supported-models.html (accessed 2026-11-10)
[^s5]: Salesforce Developers Blog, "How to Build a Predictive AI Model in Data Cloud". https://developer.salesforce.com/blogs/2024/07/how-to-build-a-predictive-ai-model-in-data-cloud (accessed 2026-11-10)
[^s6]: Salesforce Developers Blog, "Use Model Builder to Integrate Databricks Models with Salesforce". https://developer.salesforce.com/blogs/2024/03/use-model-builder-to-integrate-databricks-models-with-salesforce (accessed 2026-11-10)
