---
id: kt:prompt-builder
type: Tool
title: Prompt Builder
aliases: [Salesforce Prompt Builder, Einstein Prompt Builder, prompt templates, GenAiPromptTemplate]
domain: data-cloud-and-ai
summary: >-
  The Setup tool for building reusable, grounded prompt templates that merge Salesforce record data, related lists,
  Flow and Apex output into instructions for a large language model, then run them from record pages, Flow, Apex,
  the REST API or Agentforce actions.
release: "Winter '27"
status: current
broader: [kt:agentforce-studio]
related: [kt:agentforce, kt:flow-builder, kt:knowledge-base]
relations:
  - {predicate: dependsOn, object: kt:einstein-trust-layer}
  - {predicate: integratesWith, object: kt:apex}
  - {predicate: integratesWith, object: kt:data-cloud}
  - {predicate: configuredVia, object: kt:metadata-api}
sources:
  - id: s1
    title: "Prompt Template Types"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=ai.prompt_builder_standard_template_types.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-02
  - id: s2
    title: "Create and Ground Prompt Templates (Prompt Builder Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/prompt-builder-basics/create-and-ground-prompt-templates
    type: official-learning
    accessed: 2026-11-02
  - id: s3
    title: "Ground Your Prompt Templates with Data Using Flow or Apex"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/04/ground-your-prompt-templates-with-data-using-flow-or-apex
    type: official-blog
    accessed: 2026-11-02
  - id: s4
    title: "Resolve a Prompt Template (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/connectapi_examples_resolve_prompt_template.htm
    type: official-docs
    accessed: 2026-11-02
  - id: s5
    title: "Maximize Generative AI with Prompt Templates (Quick Start: Prompt Builder)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/quick-start-prompt-builder/get-started-with-prompt-builder
    type: official-learning
    accessed: 2026-11-02
  - id: s6
    title: "GenAiPromptTemplate (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_genaiprompttemplate.htm
    type: official-docs
    accessed: 2026-11-02
  - id: s7
    title: "Jen's Top Winter '27 Release Features For Admins"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2026/jens-top-winter-27-release-features-for-admins
    type: official-blog
    accessed: 2026-11-02
created: 2026-11-02
---

# Prompt Builder

Prompt Builder is the Salesforce tool for authoring **prompt templates**: reusable instructions for a large language model (LLM) that contain placeholders, which are filled with org data every time the template runs, so each prompt and its response are personalized to the record at hand.[^s5] Templates are managed from Setup, where an Explore page lists each template with its type, category and status.[^s2] Every request built from a template passes through the Einstein Trust Layer on its way to the model.[^s3]

## How it works

An author picks a **template type**, names the template, chooses its input objects, writes natural-language instructions, and inserts resources such as merge fields (for example `{!$Input:Sender.Name}` in a sales email).[^s2] The template is then previewed against a sample record, a model is selected from the available model types, and the template is activated before users can run it.[^s5] Salesforce's guidance is that a good template has a clear goal and is specific, which it describes as being grounded.[^s2]

Grounding pulls in data the model was not trained on. The built-in data providers are merge fields, related lists, Flow and Apex.[^s3] For Flow, an admin builds a *Template-Triggered Prompt Flow* bound to the template's capability and uses the **Add Prompt Instructions** element, which can be repeated, to append text to the prompt.[^s3] For Apex, a developer writes an `@InvocableMethod` that takes a `List<Request>` and returns a `List<Response>`, sets `capabilityType` to the matching template type (or `FlexTemplate://<API name>` for a Flex template), and references it as `{!$Apex:ClassName.Prompt}`.[^s3][^s2] Apex suits SOQL queries, external callouts, well-formatted JSON or programmatic filtering.[^s2]

## Template types

Salesforce ships many template types, each tied to where it runs. **Field Generation** fills a Lightning record field when a user clicks a button; **Sales Emails** drafts personalized emails from record data; **Record Summary** backs the Summarize Record invocable action and agent action; and **Flex** covers needs no other type fits, letting the author define the resources.[^s1] Other types are embedded in specific features, such as Case Summary and Work Summary for service, Knowledge Answers, Record Research (which uses the Einstein Search Web Retriever) and Journey Decisioning types for Marketing Cloud Engagement Journey Builder.[^s1] The 2024 developer blog notes that a Flex template accepts up to five objects, while Sales Email takes a contact or lead plus one optional object.[^s3]

A Field Generation template only reaches users after the record page is updated: Dynamic Forms must be enabled, the template selected on the field, and the page assigned.[^s5] Users then click the Einstein icon, review the suggested value, and accept, refine or edit it.[^s5]

## Invoking templates from code and metadata

Templates can be run from Flow, Apex, the REST API and agent actions in addition to their UI entry points.[^s3] In Apex, `ConnectApi.EinsteinLLM.generateMessagesForPromptTemplate` takes the template identifier and an `EinsteinPromptTemplateGenerationsInput` whose `inputParams` map wraps record IDs or strings under keys like `Input:Account`; the result exposes the resolved prompt and the generated text.[^s4] Templates are deployable as the `GenAiPromptTemplate` metadata type, which represents a template definition with its related objects and fields, alongside a separate `GenAiPromptTemplateActv` type.[^s6]

## Limits and gotchas

- **Licensing.** Prompt templates run in Lightning Experience on Enterprise, Performance and Unlimited editions with an Einstein or Agentforce add-on or Agentforce Foundations; some types need further add-ons, such as Revenue Cloud for Extract Product Mentions.[^s1]
- **Data reach.** In the 2024 guidance, merge fields and related lists could not reach external data and used Data Cloud data only for contacts and leads via enrichment, while Flow and Apex could reach CRM, Data Cloud and external data.[^s3]
- **Model changes alter output.** Salesforce rerouted Gemini 2.5 requests to Gemini 3.5 models on October 20, 2026, and advised admins to retest prompts in Prompt Builder because responses may change.[^s7]
- **Grounding Apex must be deployed** and match the capability type before it appears as a resource.[^s3]

## When to use it

Use a standard type when a feature already consumes it (summaries, sales emails, knowledge drafting), a Field Generation template for in-record assistance, and a Flex template when inputs or the output destination are custom.[^s1] Reach for Flow grounding when admins own the logic and Apex when queries or callouts get complex.[^s3] In Winter '27, admins can also build custom Knowledge Generation templates to draft knowledge articles.[^s7]

## Connections

Prompt Builder sits **broader** under Agentforce Studio, which must be turned on before building templates.[^s5] Its templates surface as **Agentforce** agent actions and as **Flow** resources, and Knowledge Answers and Knowledge Generation templates tie it to **Salesforce Knowledge**.[^s1][^s7] It **depends on the Einstein Trust Layer** for every model call,[^s3] **integrates with Apex** for grounding and invocation,[^s3][^s4] **integrates with Data Cloud** through Flow, Apex and enrichment,[^s3] and is **configured via the Metadata API** as `GenAiPromptTemplate`.[^s6]

## Sources
[^s1]: Salesforce Help, "Prompt Template Types". https://help.salesforce.com/s/articleView?id=ai.prompt_builder_standard_template_types.htm&language=en_US&type=5 (accessed 2026-11-02)
[^s2]: Trailhead, "Create and Ground Prompt Templates (Prompt Builder Basics)". https://trailhead.salesforce.com/content/learn/modules/prompt-builder-basics/create-and-ground-prompt-templates (accessed 2026-11-02)
[^s3]: Salesforce Developers Blog, "Ground Your Prompt Templates with Data Using Flow or Apex". https://developer.salesforce.com/blogs/2024/04/ground-your-prompt-templates-with-data-using-flow-or-apex (accessed 2026-11-02)
[^s4]: Salesforce Developers, "Resolve a Prompt Template (Apex Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/connectapi_examples_resolve_prompt_template.htm (accessed 2026-11-02)
[^s5]: Trailhead, "Maximize Generative AI with Prompt Templates (Quick Start: Prompt Builder)". https://trailhead.salesforce.com/content/learn/projects/quick-start-prompt-builder/get-started-with-prompt-builder (accessed 2026-11-02)
[^s6]: Salesforce Developers, "GenAiPromptTemplate (Metadata API Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_genaiprompttemplate.htm (accessed 2026-11-02)
[^s7]: Salesforce Admins Blog, "Jen's Top Winter '27 Release Features For Admins". https://admin.salesforce.com/blog/2026/jens-top-winter-27-release-features-for-admins (accessed 2026-11-02)
