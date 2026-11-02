---
id: kt:knowledge-base
type: Feature
title: Salesforce Knowledge
aliases: [Lightning Knowledge, Knowledge base, Salesforce Knowledge base, Knowledge__kav]
domain: clouds-and-products
summary: >-
  Salesforce's built-in knowledge base: versioned, translatable articles stored in the Knowledge__kav object,
  structured by record types, classified and secured by data categories, and published to internal, customer,
  partner and public channels, where they also ground Agentforce and other generative AI answers.
release: "Winter '27"
status: current
broader: [kt:service-cloud]
related: [kt:experience-cloud, kt:einstein-trust-layer, kt:approval-processes, kt:record-types]
relations:
  - {predicate: dependsOn, object: kt:data-categories}
  - {predicate: integratesWith, object: kt:agentforce}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: configuredVia, object: kt:salesforce-go}
sources:
  - id: s1
    title: "Get Started with Knowledge (Knowledge Basics, Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lightning-knowledge-basics/get-started-with-lightning-knowledge
    type: official-learning
    accessed: 2026-11-02
  - id: s2
    title: "Prepare Your Salesforce Knowledge Base (Knowledge Basics, Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lightning-knowledge-basics/prepare-the-kb-for-success
    type: official-learning
    accessed: 2026-11-02
  - id: s3
    title: "Set Up a Simple Knowledge Base (Knowledge Basics, Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lightning-knowledge-basics/set-up-a-simple-knowledge-base
    type: official-learning
    accessed: 2026-11-02
  - id: s4
    title: "Lightning Knowledge Guide (PDF)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/lightning_knowledge_guide.pdf
    type: official-docs
    accessed: 2026-11-02
  - id: s5
    title: "SOAP API Developer Guide (Winter '27 docs): Salesforce Knowledge"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.api.meta/api/sforce_api_guidelines_knowledge.htm
    type: official-docs
    accessed: 2026-11-02
created: 2026-11-02
---

# Salesforce Knowledge

Salesforce Knowledge is the knowledge base built into the Salesforce platform. Articles capture answers about a company's products and processes, such as FAQs, step-by-step procedures and handling guidelines, so that service reps, customers on self-service sites and AI agents can all find them.[^s1] Because it lives in the org, admins manage its permissions, rules and tooling the same way as other Salesforce data.[^s1] Salesforce now positions Knowledge as the trusted data layer behind AI in service: articles ground Agentforce Service Agent, Einstein Service Replies and Einstein Search Answers.[^s1][^s2] The current implementation is **Lightning Knowledge**; the older Salesforce Classic implementation used a different data model.[^s5]

## How it works

**Data model.** In Lightning Knowledge every article lives in one pair of objects: `Knowledge__ka` (the article) and `Knowledge__kav` (its versions). Different kinds of article are modeled as **record types** on `Knowledge__kav`, each with its own page layouts. Classic Knowledge instead created a separate object pair per *article type*, such as `FAQ__kav`.[^s5] The generic `KnowledgeArticle` record keeps one ID across all versions and languages, while each `KnowledgeArticleVersion` has its own ID and carries the field values. An auto-assigned Article Number ties a primary-language article to its translations, so it is not unique per record.[^s5]

**Lifecycle.** A version moves from **Draft** to **Online** (published) to **Archived**; to change a published article you create a new draft version, which replaces the online one when it is published.[^s5] Out of the box, publishing has no approval step. Admins can add an approval process per record type for content such as safety or compliance material.[^s3][^s2] Each article can hold one draft, one published version and several archived versions at a time.[^s4]

**Classification and access.** Articles are tagged with **data categories**, arranged in hierarchical category groups (for example, Products or Regions). Users use them to filter and find articles; admins grant category visibility on profiles to restrict who sees what.[^s5][^s2] SOQL and SOSL support a `WITH DATA CATEGORY` clause, and Lightning categorization is stored in `Knowledge__DataCategorySelection`.[^s5] **Channels** decide the audience: Internal App, Customer, Partner and Public Knowledge Base. Customer and partner access runs through Experience Cloud sites and needs the matching community licenses.[^s5]

**Working with articles.** In the Service Console the Knowledge component suggests articles by relevance and lets reps search, filter by language and status, create, attach to a case or insert into an email, depending on permissions.[^s1] Admins can tune search with synonyms, which also improves AI grounding.[^s2]

## Setup, licensing and limits

- **Knowledge User license.** All internal users can read articles by default, but creating and editing requires the Knowledge User license, enabled with a checkbox on the user record.[^s3][^s4] Salesforce Go can turn on Knowledge, assign author licenses and create the first category groups in one flow.[^s3]
- **One-way switch.** Once Lightning Knowledge is enabled it cannot be disabled, so try it in a sandbox first.[^s3][^s4]
- **Record types.** Lightning Knowledge is subject to the per-object record type limit of 200; Classic allowed up to 100 article types.[^s4]
- **Default volume limits** (Lightning Knowledge Guide, Spring '26 edition): 500 articles and 1 language on Essentials and Professional; 50,000 articles and 5 languages on Enterprise and Developer; 150,000 articles and 10 languages on Unlimited; 10 retained versions per article on every edition. Salesforce Support can raise them.[^s4]
- **Version display.** For articles with more than 30 versions, the extra versions show in Classic but not in Lightning Experience.[^s4]
- **Migration.** Classic Knowledge moves over with the Lightning Knowledge Migration Tool, which Salesforce Support must enable; test it in a freshly refreshed full-copy sandbox, because the move needs manual steps and some data may not transfer.[^s4] Content from another knowledge base comes in through the Knowledge import tool.[^s2]
- **Reporting gap.** Data categories don't appear in Knowledge list views; filter by category in reports instead.[^s4]

## When to use it (and when not)

Use Knowledge when the same answers are reused across reps, self-service and AI agents, and you need versioning, translation, approval and audience control in one governed store. The Trailhead guidance favours few, clearly named category groups and record types per content kind.[^s2] Content that already lives in systems such as SharePoint, Confluence or Google Drive can feed AI grounding through other connectors rather than being copied into articles.[^s2] For a handful of static help pages, a plain Experience Cloud page may be simpler than standing up a governed knowledge base.

## Connections

Knowledge sits under `kt:service-cloud`, where it powers the console's suggested articles.[^s1] It **depends on** `kt:data-categories` for classification and visibility and is **queried with** `kt:soql` through `WITH DATA CATEGORY`.[^s5] It **integrates with** `kt:agentforce`, whose service agents ground answers in published articles, and is related to `kt:einstein-trust-layer`, the layer that handles that grounding.[^s1][^s2] It is **configured via** `kt:salesforce-go`.[^s3] It is related to `kt:experience-cloud`, which delivers the customer, partner and public channels, to `kt:approval-processes` for review before publishing, and to `kt:record-types`, which replaced Classic article types.[^s5][^s3][^s4]

## Sources

[^s1]: Trailhead, "Get Started with Knowledge". https://trailhead.salesforce.com/content/learn/modules/lightning-knowledge-basics/get-started-with-lightning-knowledge (accessed 2026-11-02)
[^s2]: Trailhead, "Prepare Your Salesforce Knowledge Base". https://trailhead.salesforce.com/content/learn/modules/lightning-knowledge-basics/prepare-the-kb-for-success (accessed 2026-11-02)
[^s3]: Trailhead, "Set Up a Simple Knowledge Base". https://trailhead.salesforce.com/content/learn/modules/lightning-knowledge-basics/set-up-a-simple-knowledge-base (accessed 2026-11-02)
[^s4]: Salesforce, "Lightning Knowledge Guide" (Spring '26 edition). https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/lightning_knowledge_guide.pdf (accessed 2026-11-02)
[^s5]: Salesforce Developers, "SOAP API Developer Guide: Salesforce Knowledge". https://developer.salesforce.com/docs/atlas.en-us.264.0.api.meta/api/sforce_api_guidelines_knowledge.htm (accessed 2026-11-02)
