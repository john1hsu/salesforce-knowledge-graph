---
id: kt:models-api
type: API
title: Models API
aliases: [Einstein Models API, Agentforce Models API, aiplatform.ModelsAPI, Einstein Platform Models API]
domain: data-cloud-and-ai
summary: >-
  Salesforce's REST endpoints and Apex classes (aiplatform.ModelsAPI) for calling configured large language models
  directly to generate text, chat responses and embeddings and to submit feedback, with every request routed through
  the Einstein Trust Layer.
release: "Winter '27"
status: current
broader: [kt:salesforce-apis]
related: [kt:ai-models, kt:generative-ai-audit-and-feedback-data]
relations:
  - {predicate: dependsOn, object: kt:einstein-trust-layer}
  - {predicate: dependsOn, object: kt:einstein-generative-ai-setup}
  - {predicate: configuredVia, object: kt:external-client-apps}
  - {predicate: alternativeTo, object: kt:prompt-builder}
sources:
  - id: s1
    title: "Learn the Basics of the Models API (Get Started with the Models API)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/get-started-with-einstein-models-api/learn-the-basics-of-models-api
    type: official-learning
    accessed: 2026-11-25
  - id: s2
    title: "Access Models API with REST (Agentforce Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/access-models-api-with-rest.html
    type: official-docs
    accessed: 2026-11-25
  - id: s3
    title: "Access Models API with Apex (Agentforce Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/access-models-api-with-apex.html
    type: official-docs
    accessed: 2026-11-25
  - id: s4
    title: "Rate Limits for Models API (Agentforce Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/models-api-rate-limits.html
    type: official-docs
    accessed: 2026-11-25
  - id: s5
    title: "Model API Names (Agentforce Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/models-api-names.html
    type: official-docs
    accessed: 2026-11-25
created: 2026-11-25
---

# Models API

The Models API is the developer-facing way to call large language models (LLMs) from Salesforce code without going through a prompt template or an agent. It exposes REST endpoints and matching Apex classes that connect an application to models from Salesforce's partners, such as Anthropic, Google and OpenAI, and to any model that can be configured in AI Models (formerly Einstein Studio).[^s1] Trailhead positions it beside Prompt Builder and Agentforce: those are faster for managed prompts and interactive chat, while the Models API adds embeddings and multi-turn chat with history for teams building their own AI features.[^s1]

## Capabilities

The API offers four operations, each available over REST and in Apex.[^s1][^s3]

- **Generate text**: send a single prompt and receive generated text with content-quality (toxicity) scores.[^s1][^s2]
- **Generate chat**: send a list of messages so the model can answer with conversation history in context.[^s1]
- **Generate embeddings**: turn text into vectors for retrieval-augmented generation and semantic search.[^s1]
- **Submit feedback**: record user feedback on a generation; Salesforce stores it in Data 360.[^s1][^s2]

## How it works

Over REST, requests go to the base URL `https://api.salesforce.com/einstein/platform/v1`, with `POST /models/{modelName}/generations`, `/chat-generations` and `/embeddings`, plus `POST /feedback`, which takes no model name.[^s2] Authentication uses an External Client App with OAuth and JWT-based access tokens: the app needs the `api`, `refresh_token`/`offline_access` and `sfap_api` scopes, the client credentials flow enabled, and a Run As user. The caller exchanges its client ID and secret at the org's My Domain token endpoint and sends the token as a Bearer header along with two reserved context headers, `x-sfdc-app-context` and `x-client-feature-id`.[^s2]

In Apex, the `aiplatform.ModelsAPI` class provides `createGenerations`, `createChatGenerations`, `createEmbeddings` and `submitFeedback`, each taking a typed request object and returning a typed response; failures surface as a method-specific `ResponseException` that carries the response code.[^s3] Salesforce generates these classes from the REST specification with External Services, so the Apex methods are subject to Apex callout limits and limitations, and tests follow the External Services testing guidance.[^s3]

Models are addressed by API name. A Salesforce-managed name combines the `sfdc_ai` namespace, a configuration name, a provider and a model, for example `sfdc_ai__DefaultOpenAIGPT4OmniMini`; bring-your-own and custom-configured models have their own names, found in Setup on the AI Models page under the Generative tab.[^s5] Bring-your-own models run inference on the customer's provider instance but still pass through the Models API and the Trust Layer.[^s1]

## Trust Layer behaviour

Every Models API call goes through the Einstein Trust Layer. Generation requests get automatic data masking and toxicity scoring, and the response includes a toxicity flag and category scores that are stored in Data 360 with masking and feedback data.[^s1] Salesforce's agreements with LLM providers such as OpenAI include zero data retention commitments, but Trailhead stresses that the Trust Layer does not replace human review of model output.[^s1]

## Limits and gotchas

- Production orgs: 10,000 generation requests per minute per org per endpoint (or Apex method); per-model values can be lower.[^s4]
- Embeddings and feedback: 1,000 requests per minute per org each.[^s4]
- Free and trial orgs default to 150 generation requests per hour and token caps of 100,000 per minute and 750,000 per hour.[^s4]
- Apex calls from sandboxes are limited to 500 requests per hour; sandbox REST calls use the production limits.[^s4]
- Exceeding a limit returns HTTP 429; increases go through the account executive, and all calls are billed at Salesforce usage rates.[^s4]
- A 401 or 404 on REST usually means missing scopes or app settings, and an `invalid_grant` error usually means the wrong My Domain was used for the token request.[^s2]

## When to use it (and when not)

Use the Models API when code needs direct control over the model call: custom chat experiences, embedding pipelines for search, or batch generation from Apex. For admin-managed prompts grounded in record data, a Prompt Builder template is simpler; for conversational automation with actions, use Agentforce.[^s1] Because Apex calls count as callouts, bulk work should be designed around callout and rate limits rather than invoked per record in a trigger.[^s3][^s4]

## Connections

The API sits under Salesforce's broader API family (`kt:salesforce-apis`) and is the programmatic counterpart to AI Models (`kt:ai-models`), where the models it calls are configured.[^s1][^s5] It depends on the Einstein Trust Layer (`kt:einstein-trust-layer`) for masking and toxicity scoring, and on Einstein generative AI being set up in the org (`kt:einstein-generative-ai-setup`).[^s1] REST access is configured through an External Client App (`kt:external-client-apps`) using the client credentials flow.[^s2] It is an alternative to Prompt Builder (`kt:prompt-builder`) when developers need raw model access, and its feedback and toxicity records join the generative AI audit data in Data 360 (`kt:generative-ai-audit-and-feedback-data`).[^s1]

## Sources
[^s1]: Trailhead, "Learn the Basics of the Models API". https://trailhead.salesforce.com/content/learn/modules/get-started-with-einstein-models-api/learn-the-basics-of-models-api (accessed 2026-11-25)
[^s2]: Salesforce, "Access Models API with REST". https://developer.salesforce.com/docs/ai/agentforce/guide/access-models-api-with-rest.html (accessed 2026-11-25)
[^s3]: Salesforce, "Access Models API with Apex". https://developer.salesforce.com/docs/ai/agentforce/guide/access-models-api-with-apex.html (accessed 2026-11-25)
[^s4]: Salesforce, "Rate Limits for Models API". https://developer.salesforce.com/docs/ai/agentforce/guide/models-api-rate-limits.html (accessed 2026-11-25)
[^s5]: Salesforce, "Model API Names". https://developer.salesforce.com/docs/ai/agentforce/guide/models-api-names.html (accessed 2026-11-25)
