---
id: kt:context-service
type: Feature
title: Context Service
aliases: [Industries Context Service, context definitions, Context Definition Designer]
domain: clouds-and-products
summary: >-
  A common Salesforce Industries capability that assembles the data a business process needs into one logical,
  in-memory model (a context instance built from a context definition of nodes, attributes, tags and mappings),
  so engines like Business Rules Engine and Salesforce Pricing can read and update it without repeated queries.
release: "Winter '27"
status: current
broader: [kt:salesforce-industries]
related: [kt:data-model-objects, kt:revenue-cloud]
relations:
  - {predicate: usedBy, object: kt:business-rules-engine}
  - {predicate: usedBy, object: kt:salesforce-pricing}
  - {predicate: queriedWith, object: kt:connect-api}
  - {predicate: configuredVia, object: kt:tooling-api}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: integratesWith, object: kt:platform-events}
sources:
  - id: s1
    title: "Context Service Overview (Industries Common Resources Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.industries_reference.meta/industries_reference/context_service_overview.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s2
    title: "Explore Context Service Components and Processes (Context Service Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/context-service-basics/explore-context-service-components-and-processes
    type: official-learning
    accessed: 2026-11-09
  - id: s3
    title: "Get to Know Context Service (Context Service Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/es/content/learn/modules/context-service-basics/get-to-know-context-service
    type: official-learning
    accessed: 2026-11-09
  - id: s4
    title: "Context Service Tooling API Objects (Industries Common Resources Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/context_service_tooling_api_parent.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s5
    title: "Context Definition (GET, POST) (Industries Common Resources Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_context_definition.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s6
    title: "Fetch Opportunity Data (Automated Compliance with Business Rules Engine and Context Service)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/automated-compliance-with-business-rules-engine-and-context-service/fetch-opportunity-data
    type: official-learning
    accessed: 2026-11-09
created: 2026-11-09
---

# Context Service

Context Service is a generic module shared by Salesforce's industry clouds. It sits as a layer between applications and the procedures they run, so business data can be shared and reused across process steps.[^s1] It hides where the underlying data lives behind one logical data model. Developers then stop writing point-to-point integration code, and steps stop issuing their own database calls, which cuts latency.[^s3] Trailhead's example is a loan application. The process needs the applicant's job, income, credit history, collateral and guarantors, which live in different objects but are presented as one context.[^s2]

## How it works

**Design time.** An admin builds a *context definition* in the Context Definition Designer (Setup → Context Definitions). The definition describes all the information a process needs.[^s3][^s6] It has four parts:

- **Nodes**: hierarchical containers.
- **Attributes**: individual typed values that live inside nodes.
- **Context tags**: short aliases that consuming applications use to query nodes and attributes directly.
- **Context mappings**: links from nodes to Salesforce objects or Data Model Objects, and from attributes to fields.[^s2]

The design-time sequence is: create the definition, add the structure, tag it, then map it.[^s2] In the Business Rules Engine Trailhead project, a custom `SalesTransaction` definition has an Opportunity node whose attributes are marked INPUT or INPUT OUTPUT. A default mapping (`ContextMap`) binds those attributes to Opportunity fields, reaching Account.Rating through the AccountId lookup. The definition must be **activated** before Business Rules Engine can use it.[^s6]

**Run time.** An application calls the Build APIs to create a *context instance*. The instance loads data through the mappings and is held in temporary, transient stores, so later steps read from it instead of querying the database again.[^s2] The Apex API offers four operations:

- **Build**: create the instance.
- **Query**: read records and tags.
- **Update**: change or add data.
- **Persist**: write context data back to the database.[^s3]

A Business Object Transformation capability converts one business object into another, such as a quote into an order, and can persist the result.[^s3] A definition can use one mapping to read data and a different mapping to write it to other objects.[^s2] When a persistence run finishes, the `ContextPersistence` platform event notifies subscribers.[^s1]

## Standard, extended and cloned definitions

Industry clouds ship *standard* definitions, and you can't modify their components. You have three options instead:

- **Extend** a standard definition. It inherits the standard nodes, attributes and mappings as read-only and receives Industry Cloud updates automatically. If an automatic update fails, you update it manually.
- **Clone** a standard or custom definition into a fully editable copy.
- **Build** a custom definition from scratch.[^s2]

*Transposable* child nodes store data as key–value pairs, such as a product attribute Color = Blue. They are available only in custom definitions or on custom nodes.[^s2]

## Developer surface and limits

Definitions are exposed as Metadata API types, Tooling API objects, standard invocable actions, an Apex class and Business REST APIs. The REST APIs follow Connect REST API conventions.[^s1] The Tooling API model includes these objects:

- `ContextDefinition` and `ContextDefinitionVersion` (only one version can be active at a time)[^s4]
- `ContextNode` and `ContextAttribute`
- `ContextNodeMapping`, `ContextMapping` and `ContextAttributeMapping`
- `ContextTag`[^s4]

Most of these objects arrived in API 59.0. Later objects include `ContextDefinitionReference` (60.0), `ContextMappingIntent` (61.0) and `ContextDefinitionSync` (62.0).[^s4]

The `/connect/context-definitions` resource has been available since API 59.0. Its GET lists definitions. Its POST can create a definition, clone one, extend a standard file-based definition, or save a whole definition as a JSON `payload`. Optional fields include `startDate`/`endDate` validity and a `contextTtl` time-to-live.[^s5]

Gotchas:

- Persistence is an explicit step. Changes to an instance are not saved automatically.[^s2]
- Standard components are read-only.[^s2]
- The overview documentation publishes no numeric quotas.[^s1]

## When to use it

Use Context Service when an Industries engine needs a curated, cached slice of related records, for example pricing a quote, evaluating eligibility rules or transforming a quote into an order. Don't hand-build SOQL inside every step. For one-off record logic outside the Industries engines, ordinary Flow or Apex queries remain simpler.[^s3][^s2]

## Connections

Context Service is a common capability of `kt:salesforce-industries` (its **broader** node) and is **related** to `kt:revenue-cloud` through the pricing engine described below; it serves industry clouds generally.[^s1][^s3] It is **used by** `kt:business-rules-engine`, whose expression sets consume activated definitions.[^s6] It is also **used by** `kt:salesforce-pricing`; like any consuming application, pricing reads context data through tags rather than raw object fields.[^s2] Its Business REST resources are **queried with** `kt:connect-api` conventions.[^s5][^s1] Definitions are **configured via** `kt:tooling-api` objects and `kt:metadata-api` types.[^s4][^s1] Context mappings can target `kt:data-model-objects` as well as standard objects.[^s2] It **integrates with** `kt:platform-events` through the `ContextPersistence` event.[^s1]

## Sources
[^s1]: Salesforce, "Context Service Overview", Industries Common Resources Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.264.0.industries_reference.meta/industries_reference/context_service_overview.htm (accessed 2026-11-09)
[^s2]: Trailhead, "Explore Context Service Components and Processes". https://trailhead.salesforce.com/content/learn/modules/context-service-basics/explore-context-service-components-and-processes (accessed 2026-11-09)
[^s3]: Trailhead, "Get to Know Context Service". https://trailhead.salesforce.com/es/content/learn/modules/context-service-basics/get-to-know-context-service (accessed 2026-11-09)
[^s4]: Salesforce, "Context Service Tooling API Objects", Industries Common Resources Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/context_service_tooling_api_parent.htm (accessed 2026-11-09)
[^s5]: Salesforce, "Context Definition (GET, POST)", Industries Common Resources Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/connect_resources_context_definition.htm (accessed 2026-11-09)
[^s6]: Trailhead, "Fetch Opportunity Data". https://trailhead.salesforce.com/content/learn/modules/automated-compliance-with-business-rules-engine-and-context-service/fetch-opportunity-data (accessed 2026-11-09)
