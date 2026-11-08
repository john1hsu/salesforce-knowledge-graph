---
id: kt:graphql-api
type: API
title: GraphQL API
aliases: [Salesforce GraphQL API, UI API GraphQL, graphql endpoint, GraphQL wire adapter API]
domain: integration
summary: >-
  Salesforce's implementation of the GraphQL specification, exposed at a single /graphql endpoint, that lets a
  client ask for exactly the fields it needs across related UI API-enabled objects in one request and, from API
  v66.0, create, update and delete records through mutations.
release: "Winter '27"
status: current
broader: [kt:salesforce-apis]
related: [kt:rest-api, kt:composite-api, kt:lightning-data-service, kt:soql, kt:polymorphic-relationships]
relations:
  - {predicate: dependsOn, object: kt:user-interface-api}
  - {predicate: alternativeTo, object: kt:rest-api}
  - {predicate: usedBy, object: kt:lightning-web-components}
  - {predicate: governedBy, object: kt:api-request-limits}
  - {predicate: governedBy, object: kt:field-level-security}
  - {predicate: coveredBy, object: kt:integration-architect-certification}
sources:
  - id: s1
    title: "What is GraphQL API? (GraphQL API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/graphql/guide/intro-graphql-api.html
    type: official-docs
    accessed: 2026-11-08
  - id: s2
    title: "GraphQL Request and Response Structure (GraphQL API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/graphql/guide/requests-and-responses.html
    type: official-docs
    accessed: 2026-11-08
  - id: s3
    title: "Query Limits (GraphQL API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/graphql/guide/query-limits.html
    type: official-docs
    accessed: 2026-11-08
  - id: s4
    title: "Mutations (GraphQL API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/graphql/guide/mutations-intro.html
    type: official-docs
    accessed: 2026-11-08
  - id: s5
    title: "GraphQL Mutations Now Available in LWC: Create, Update and Delete Records"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2026/05/graphql-mutations-now-available-in-lwc-create-update-and-delete-records
    type: official-blog
    accessed: 2026-11-08
created: 2026-11-08
---

# GraphQL API

The Salesforce GraphQL API is the platform's implementation of the open GraphQL specification (it conforms to the June 2018 version of the spec). It gives clients a GraphQL representation of the sObjects that User Interface API supports, and it is available in Enterprise, Performance, Unlimited and Developer Editions.[^s1] Its selling points are the classic GraphQL ones: the client declares exactly which fields it wants, so payloads stay small; one query can walk related records, so several REST round trips collapse into one; and the schema can be introspected, so tools discover types, fields and relationships at run time.[^s1]

## How it works

Every operation is an HTTP POST to `https://{MyDomainName}.my.salesforce.com/services/data/v{version}/graphql`, authenticated with an OAuth bearer token. The JSON body carries a required `query` string plus optional `operationName`, `variables` and `extensions`.[^s2] Queries are nested under the `uiapi` namespace, then `query`, then the object name, for example `uiapi { query { Account(where: …) { edges { node { Name { value } } } } } }`. Records arrive as `edges` that each wrap a `node`, scalar fields are read through a `value` sub-field, and `Id` is selected directly.[^s2] Paged results follow the Relay Connection Specification.[^s1]

The response always has the same three parts: `data`, `errors` and `extensions`. A failed request returns empty `data` and an `errors` array whose entries give the error type, the line and column, a message and the path, so a client has to inspect `errors` rather than rely only on the HTTP status.[^s2]

Because the schema is built from UI API, the API applies the running user's object- and field-level security, so two users can see different schemas from the same org. From API v68.0, admins can control unauthenticated guest-user access under API Access Controls in Setup; object and field security still apply to guests.[^s1]

Mutations create, update and delete records through the `Mutation` operation type. They were beta from v59.0 to v65.0 and are generally available from v66.0.[^s4] In Lightning Web Components, `executeMutation` from `lightning/graphql` takes the same `query`, `variables` and `operationName` properties as the GraphQL wire adapter. Lightning Data Service keeps the cache consistent: deleted records drop out of wired results, updated fields can flow to overlapping wires, but new records appear in an existing query only after it is refreshed.[^s5]

## Limits and gotchas

The query limits page lists these limits (checked for Winter '27):[^s3]

- Up to 10 subqueries per query; **each subquery counts as one request** against API rate limits, so a "single" GraphQL call can consume several API calls.[^s3]
- Each subquery returns at most 2,000 records, and only 10 are returned by default; use pagination for more.[^s3]
- Up to 55 child-to-parent relationships, 5 levels deep from v58.0 (2 levels in v57.0 and earlier); up to 20 parent-to-child relationships, only 1 level deep.[^s3]
- Semi-joins and anti-joins allow at most 2 `nin`/`ninq` operators per `where`, can't be nested, and can't be combined with `or` or `orderBy`.[^s3]
- Only UI API-supported objects can be queried, and some fields can't be used in `where`. Note bodies and textarea, blob and S-control content can't be filtered.[^s3]
- External objects: a subquery fetches up to 1,000 rows, a query allows up to 4 joins across external and other objects, and each join is a separate trip to the external system.[^s3]

Event and Task support was beta from v59.0 to v65.0 and became GA in v66.0, so check the API version you pin in the endpoint URL.[^s3]

## When to use it (and when not)

Choose GraphQL when a UI or mobile client needs a precise slice of data from several related objects in one round trip, or when LWC code should read and write across objects without custom Apex.[^s1][^s5] It is not a bulk tool: the 2,000-record subquery ceiling, the 10-record default page and per-subquery rate counting all point large extracts and loads toward Bulk API 2.0.[^s3] And because only UI API-supported objects are reachable, integrations that touch other objects still need the REST or Composite API.[^s3]

## Connections

GraphQL API sits within the family of **Salesforce APIs** as an **alternative to the REST API**: it shares the same `/services/data` base path and OAuth model but replaces fixed resources with client-shaped queries.[^s2] It **depends on User Interface API**, which defines both the objects it can reach and the security it enforces, so it is **governed by field-level security** and object permissions.[^s1] Its subquery accounting ties it to **API request limits**.[^s3] In the UI tier it is **used by Lightning Web Components** through the GraphQL wire adapter and `executeMutation`, both managed by **Lightning Data Service**.[^s5] Its filtering and relationship traversal mirror **SOQL**, including traversing **polymorphic relationships**, and its scope overlaps with the **Composite API** for multi-object requests.[^s3] Choosing between these APIs is examined in the **Integration Architect certification**.[^s1]

## Sources

[^s1]: Salesforce Developers, "What is GraphQL API? (GraphQL API Developer Guide)". https://developer.salesforce.com/docs/platform/graphql/guide/intro-graphql-api.html (accessed 2026-11-08)
[^s2]: Salesforce Developers, "GraphQL Request and Response Structure (GraphQL API Developer Guide)". https://developer.salesforce.com/docs/platform/graphql/guide/requests-and-responses.html (accessed 2026-11-08)
[^s3]: Salesforce Developers, "Query Limits (GraphQL API Developer Guide)". https://developer.salesforce.com/docs/platform/graphql/guide/query-limits.html (accessed 2026-11-08)
[^s4]: Salesforce Developers, "Mutations (GraphQL API Developer Guide)". https://developer.salesforce.com/docs/platform/graphql/guide/mutations-intro.html (accessed 2026-11-08)
[^s5]: Salesforce Developers Blog, "GraphQL Mutations Now Available in LWC: Create, Update and Delete Records". https://developer.salesforce.com/blogs/2026/05/graphql-mutations-now-available-in-lwc-create-update-and-delete-records (accessed 2026-11-08)
