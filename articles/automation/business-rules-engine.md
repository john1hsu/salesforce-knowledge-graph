---
id: kt:business-rules-engine
type: Feature
title: Business Rules Engine
aliases: [BRE, Salesforce Business Rules Engine, expression sets, Expression Set Builder, decision matrices]
domain: automation
summary: >-
  A Salesforce suite of services, components and objects for no-code decisioning: expression sets chain
  conditions, calculations, aggregations and lookups against decision matrices and decision tables, and return
  JSON results to Flow, Omniscripts or callers of its Connect REST resources.
release: "Winter '27"
status: current
broader: [kt:process-automation, kt:salesforce-industries]
related: [kt:flow-builder, kt:product-configurator, kt:public-sector-solutions, kt:context-service]
relations:
  - {predicate: queriedWith, object: kt:connect-api}
  - {predicate: integratesWith, object: kt:omnistudio}
sources:
  - id: s1
    title: "Get to Know Business Rules Engine (Business Rules Engine module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/business-rules-engine/get-to-know-business-rules-engine
    type: official-learning
    accessed: 2026-11-09
  - id: s2
    title: "Orchestrate Rules with Expression Sets (Business Rules Engine module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/business-rules-engine/orchestrate-rules-with-expression-sets
    type: official-learning
    accessed: 2026-11-09
  - id: s3
    title: "Build Decisions with Lookup Tables (Business Rules Engine module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/business-rules-engine/build-decisions-with-lookup-tables
    type: official-learning
    accessed: 2026-11-09
  - id: s4
    title: "Business Rules Engine (Industries Common Resources Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s5
    title: "Expression Set Invocation (POST) (Public Sector Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.262.0.psc_api.meta/psc_api/connect_resources_bre_expression_set.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s6
    title: "Flow for Expression Set (Public Sector Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.psc_api.meta/psc_api/expression_set_flow_metadata_api.htm
    type: official-docs
    accessed: 2026-11-09
created: 2026-11-09
---

# Business Rules Engine

Business Rules Engine (BRE) is Salesforce's decisioning layer: a suite of services, components and objects for building rules that perform complex lookups and calculations.[^s4] Its three core building blocks are expression sets, decision matrices and decision tables, all designed in visual builders so business users can maintain eligibility, pricing, fee and discount logic without writing code.[^s1][^s4] The developer guide lists it for Lightning Experience in Enterprise, Professional, Unlimited and Developer Editions; in practice it ships with industry solutions, and practicing on Trailhead requires a special Developer Edition org rather than a standard playground.[^s4][^s1]

## How it works

**Expression sets** are the calculation engine. An expression set takes JSON input, runs an ordered sequence of elements, and returns JSON that a guided process can consume.[^s2] Element types include Condition (later steps run only if true), Conditional Group, Branch (prioritized paths, up to six including the default), Calculation (math or functions producing one result), Lookup Table (calls a decision matrix or table), Aggregate and Aggregate Group (sum, average, max or min across repeated runs), Sub Expression (calls a child expression set), and industry-specific Business Elements.[^s2] Variables and constants live in a Resource Manager, and a built-in simulator lets you enter test inputs and inspect each step's input and output JSON before activation.[^s2]

**Decision matrices** are lookup tables with user-defined input and output columns. Data is typed in or imported from a .csv file, with header type (input or output) and data type assigned on import.[^s3] A matrix returns the single row that matches its inputs. Grouped matrices additionally organize rows by keys such as region or product code.[^s3]

**Decision tables** read their rows from Salesforce records (or values you specify), so they refresh automatically when the underlying data changes, support per-field operators such as less-than and greater-than, and can return multiple matching outcome sets.[^s3][^s1]

A companion **Decision Explainer** stores step results and explainability messages so you can later report why a rule produced a given outcome.[^s1][^s4]

## Versioning and invocation

Expression sets and decision matrices are both versioned. Each version carries start and end dates and a rank (priority), and at runtime the engine picks the version whose dates and priority apply, which lets teams schedule rate or rule changes in advance.[^s2][^s3] An active matrix version can't be edited; changes go into a new, copied version.[^s3]

There are three common entry points. From Flow, a FlowActionCall with actionType `runExpressionSet` runs an active expression set (API version 55.0 and later).[^s6] From OmniStudio, an Omniscript step embeds the expression set in a guided experience.[^s1][^s2] From code or external systems, the Connect REST resource `/connect/business-rules/expressionSet/{expressionSetName}` accepts a POST with an `inputs` array and optional `options` such as an effective date, also available since API version 55.0.[^s5]

## Limits and gotchas

- Only **active** decision matrices and tables can be referenced from an expression set, and only active expression sets can be invoked from Flow.[^s1][^s6]
- A decision matrix returns one output row even if several rows match; if you need several results or comparison operators, use a decision table.[^s3]
- Version selection is date- and rank-driven; overlapping versions with careless priorities are a common source of "wrong rate" bugs, so simulate with several inputs before going live.[^s2][^s3]
- None of the sources opened for this article publish numeric caps on matrix rows, versions or payload size; check your industry cloud's documentation before sizing very large tables.[^s3][^s5]

## When to use it (and when not)

Reach for BRE when rules are table-shaped and owned by the business: fee schedules, rating tables, discounts, eligibility criteria, or anything already maintained in spreadsheets.[^s3][^s2] A single decision-table lookup can replace long chains of Decision elements in a flow.[^s3] For simple branching on one record, plain Flow logic is lighter and avoids an extra versioned asset to activate and maintain.[^s3][^s6]

## Connections

BRE sits under `kt:process-automation` and is delivered as common capability of `kt:salesforce-industries`.[^s4] It is **related** to `kt:flow-builder`, which invokes expression sets as actions, and **integrates with** `kt:omnistudio`, whose Omniscripts embed them in guided experiences.[^s6][^s1] External callers **query** it through `kt:connect-api` business-rules resources.[^s5] Its typical use cases, such as permit and application fees, benefit eligibility and volume discounts, make it **related** to industry features like `kt:public-sector-solutions` and `kt:product-configurator`, whose own articles describe how they consume BRE rules.[^s2] Expression set inputs can also reference context definitions, linking it to `kt:context-service`.[^s5]

## Sources
[^s1]: Trailhead, "Get to Know Business Rules Engine". https://trailhead.salesforce.com/content/learn/modules/business-rules-engine/get-to-know-business-rules-engine (accessed 2026-11-09)
[^s2]: Trailhead, "Orchestrate Rules with Expression Sets". https://trailhead.salesforce.com/content/learn/modules/business-rules-engine/orchestrate-rules-with-expression-sets (accessed 2026-11-09)
[^s3]: Trailhead, "Build Decisions with Lookup Tables". https://trailhead.salesforce.com/content/learn/modules/business-rules-engine/build-decisions-with-lookup-tables (accessed 2026-11-09)
[^s4]: Salesforce, "Business Rules Engine", Industries Common Resources Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/business_rules_engine.htm (accessed 2026-11-09)
[^s5]: Salesforce, "Expression Set Invocation (POST)", Public Sector Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.262.0.psc_api.meta/psc_api/connect_resources_bre_expression_set.htm (accessed 2026-11-09)
[^s6]: Salesforce, "Flow for Expression Set", Public Sector Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.psc_api.meta/psc_api/expression_set_flow_metadata_api.htm (accessed 2026-11-09)
