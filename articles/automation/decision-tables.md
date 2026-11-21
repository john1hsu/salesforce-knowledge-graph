---
id: kt:decision-tables
type: Feature
title: Decision Tables
aliases: [decision table, DecisionTable, BRE decision tables, Decision Table Builder]
domain: automation
summary: >-
  Business Rules Engine lookup tables that read their rows from Salesforce object or custom metadata type records
  (or a CSV upload), match multiple input conditions with operators, and return one or many output rows to Flow,
  expression sets or Connect REST callers.
release: "Winter '27"
status: current
broader: [kt:business-rules-engine]
related: [kt:custom-metadata-types, kt:custom-objects, kt:salesforce-pricing, kt:decision-matrices]
relations:
  - {predicate: consumedBy, object: kt:flow-builder}
  - {predicate: consumedBy, object: kt:loyalty-management}
  - {predicate: queriedWith, object: kt:connect-api}
  - {predicate: configuredVia, object: kt:tooling-api}
sources:
  - id: s1
    title: "Get Started with Decision Tables (Explore Lookup Tables in Business Rules Engine)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/deep-dive-into-lookup-tables-in-business-rules-engine/get-started-with-decision-tables
    type: official-learning
    accessed: 2026-11-21
  - id: s2
    title: "Explore Decision Tables (Explore Lookup Tables in Business Rules Engine)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/deep-dive-into-lookup-tables-in-business-rules-engine/explore-decision-tables
    type: official-learning
    accessed: 2026-11-21
  - id: s3
    title: "Decision Table (Public Sector Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.psc_api.meta/psc_api/decision_table.htm
    type: official-docs
    accessed: 2026-11-21
  - id: s4
    title: "DecisionTable (Tooling API object, Public Sector Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.psc_api.meta/psc_api/tooling_api_objects_decisiontable.htm
    type: official-docs
    accessed: 2026-11-21
  - id: s5
    title: "Decision Table Refresh Action (Public Sector Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.psc_api.meta/psc_api/dt_actions_refresh_decision_table.htm
    type: official-docs
    accessed: 2026-11-21
  - id: s6
    title: "Decision Table Invocation (POST) (Public Sector Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.psc_api.meta/psc_api/connect_resources_decisionTableId.htm
    type: official-docs
    accessed: 2026-11-21
  - id: s7
    title: "Build Decisions with Lookup Tables (Business Rules Engine module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/business-rules-engine/build-decisions-with-lookup-tables
    type: official-learning
    accessed: 2026-11-21
created: 2026-11-21
---

# Decision Tables

A decision table is a lookup table that returns outcomes for one or more fields based on business rules you define, where the rules themselves are rows stored in a standard object, a custom object or a custom metadata type.[^s3][^s1] You build it in Business Rules Engine, give it several input conditions and several result fields, and then call it from a flow or an expression set.[^s1] Because its rows are ordinary Salesforce records, administrators maintain the rules by editing data, not by redeploying automation.[^s7] The developer guide lists it for Lightning Experience in Enterprise, Unlimited and Performance Editions with Loyalty Management or Rebate Management.[^s3]

## How it works

Designing a table means choosing a source object, picking condition fields (inputs) and result fields (outputs), setting behaviours, previewing and saving, and then activating; activation runs asynchronously and can take a few seconds.[^s1] Conditions are required by default and can be marked optional, and the condition type can be All (AND), Any (OR) or custom logic such as `(1 AND 2) OR 3`.[^s1][^s4] Each condition can use an operator, so a row can mean "price greater than 1,000" rather than only an exact match.[^s7][^s6]

The underlying `DecisionTable` record (Tooling API, version 51.0 and later) exposes the design choices as fields.[^s4] The main ones are:

- **Status**: Draft, ActivationInProgress, Active or Inactive.[^s4]
- **DataSourceType**: SingleSobject (the default), MultipleSobjects, CsvUpload or ContextDefinition.[^s4]
- **Type**: volume and execution profiles such as LowVolume (the default), MediumVolume, Advanced and RealTime.[^s4]
- **FilterResultBy**: how matches are returned, for example FirstMatch, AnyValue or OutputOrder.[^s4]
- **UsageType**: Bre by default when Business Rules Engine is enabled, plus product qualification and record-alert uses.[^s4]

Trailhead's walkthrough explains the three common result filters: First Match returns one output from the first matching row; Any Value returns one output only if every matching row agrees, otherwise an empty response; and Output Order, the default, returns all matching rows.[^s2] A Sort By field orders outcomes, and a group key splits a Standard-type table into groups at design time.[^s1]

## Multiple sources and aggregation

A table can draw on a primary source object plus up to four objects related to it, which lets one lookup return, say, a price from the source and a discount from a related offer object.[^s2] The Table tab is not available for multi-object tables.[^s2] For speed, condition fields can be aggregated at save time: the fields must be input conditions, combined with at least one AND, and use the Equals operator, after which grouped fields are treated as one lookup key.[^s2]

## Refreshing the data

Source records are synced into the table, and each sync is tracked on the definition record.[^s4] The `refreshDecisionTable` standard invocable action (API 51.0 and later) queues a refresh of an active table and reports Queued or Failed.[^s5] An incremental refresh syncs only recent changes, but the first refresh must be full, and if changes exceed 2,000 records the incremental refresh fails and a full refresh is required.[^s5] Full refreshes update `LastSyncDate`, while incremental ones update only `LastIncrementalSyncDate`; `RefreshStatus` and `RefreshFailureReason` on the record help troubleshoot.[^s5][^s4]

## Limits and gotchas

- Trailhead states that a decision table can read up to 1 million rows.[^s1]
- Up to four related objects can be added to a primary source object.[^s2]
- Incremental refresh fails above 2,000 changed records; schedule full refreshes after bulk loads.[^s5]
- The refresh action accepts only an active table, and null column values are left out of lookups unless `DoesConsiderNullValue` is true.[^s5][^s4]

## Invocation

Beyond Flow and expression sets, external code can POST to `/connect/business-rules/decision-table/lookup/{decisionTableId}` (API 58.0) with a list of condition groups and receive a bulk outcome; conditions can carry operators such as Matches or GreaterThan.[^s6]

## When to use it (and when not)

Choose a decision table over a decision matrix when rules already live in Salesforce records, when you need comparison operators, or when one lookup should return several matching rows; a matrix is typed in or imported from CSV, is versioned by dates and priority, and returns a single matching row.[^s7] For a handful of static branches, ordinary Flow decision logic avoids the refresh and activation overhead.[^s7][^s5]

## Connections

Decision tables are a component of `kt:business-rules-engine`, their broader node, and an **alternative to** its other lookup type, `kt:decision-matrices`.[^s7] They read rules from `kt:custom-objects`, standard objects or `kt:custom-metadata-types`.[^s3] They are **consumed by** `kt:flow-builder` flows and by `kt:loyalty-management`, whose sample refresh request refreshes a points-redemption table, and they relate to `kt:salesforce-pricing`.[^s1][^s5][^s3] External callers **query** them through `kt:connect-api` business-rules resources, and their definitions are **configured via** `kt:tooling-api` `DecisionTable` records.[^s6][^s4]

## Sources
[^s1]: Trailhead, "Get Started with Decision Tables". https://trailhead.salesforce.com/content/learn/modules/deep-dive-into-lookup-tables-in-business-rules-engine/get-started-with-decision-tables (accessed 2026-11-21)
[^s2]: Trailhead, "Explore Decision Tables". https://trailhead.salesforce.com/content/learn/modules/deep-dive-into-lookup-tables-in-business-rules-engine/explore-decision-tables (accessed 2026-11-21)
[^s3]: Salesforce, "Decision Table", Public Sector Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.264.0.psc_api.meta/psc_api/decision_table.htm (accessed 2026-11-21)
[^s4]: Salesforce, "DecisionTable" Tooling API object, Public Sector Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.psc_api.meta/psc_api/tooling_api_objects_decisiontable.htm (accessed 2026-11-21)
[^s5]: Salesforce, "Decision Table Refresh Action", Public Sector Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.psc_api.meta/psc_api/dt_actions_refresh_decision_table.htm (accessed 2026-11-21)
[^s6]: Salesforce, "Decision Table Invocation (POST)", Public Sector Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.psc_api.meta/psc_api/connect_resources_decisionTableId.htm (accessed 2026-11-21)
[^s7]: Trailhead, "Build Decisions with Lookup Tables". https://trailhead.salesforce.com/content/learn/modules/business-rules-engine/build-decisions-with-lookup-tables (accessed 2026-11-21)
