---
id: kt:composite-api
type: API
title: Composite API
aliases: [REST API composite resources, Composite resource, Composite Batch, Composite Graph, sObject Tree, sObject Collections]
domain: integration
summary: >-
  The family of Salesforce REST API composite resources (Composite, Composite Batch, Composite Graph, sObject Tree
  and sObject Collections) that bundle several record operations or dependent subrequests into one HTTP call,
  cutting round trips and, for most of them, API-call consumption.
release: "Winter '27"
status: current
broader: [kt:rest-api]
related: [kt:bulk-api-2, kt:governor-limits, kt:external-id-fields]
relations:
  - {predicate: partOf, object: kt:rest-api}
  - {predicate: alternativeTo, object: kt:bulk-api-2}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: governedBy, object: kt:api-request-limits}
  - {predicate: coveredBy, object: kt:integration-architect-certification}
sources:
  - id: s1
    title: "Send Multiple Requests Using Composite (REST API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-rest/guide/resources-composite-composite-post.html
    type: official-docs
    accessed: 2026-11-03
  - id: s2
    title: "Composite Request Body (REST API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api/requests_composite.htm
    type: official-docs
    accessed: 2026-11-03
  - id: s3
    title: "Composite Batch (REST API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-rest/guide/resources-composite-batch.html
    type: official-docs
    accessed: 2026-11-03
  - id: s4
    title: "sObject Tree (REST API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-rest/guide/resources-composite-sobject-tree.html
    type: official-docs
    accessed: 2026-11-03
  - id: s5
    title: "Create Records Using sObject Collections (REST API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-rest/guide/resources-composite-sobjects-collections-create.html
    type: official-docs
    accessed: 2026-11-03
  - id: s6
    title: "Composite Graph Limits (REST API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-rest/guide/resources-composite-graph-limits.html
    type: official-docs
    accessed: 2026-11-03
created: 2026-11-03
---

# Composite API

"Composite API" is the practitioner's name for the composite resources of the Salesforce REST API. Each one lets a client pack several operations into a single HTTP request instead of making one call per record or per step. The flagship **Composite** resource (`POST /services/data/vXX.X/composite`) runs a series of REST subrequests in one call, lets later subrequests use the output of earlier ones, and returns every subrequest's status and body in a single response. All subrequests run as the same user.[^s1] Around it sit four siblings: **Composite Batch**, **Composite Graph**, **sObject Tree** and **sObject Collections**, each tuned for a different shape of work.[^s3][^s4][^s5][^s6]

## How it works

A Composite request body has a required `compositeRequest` array. Each subrequest gives a `method`, a `url` beginning with `/services/data/vXX.X/`, a case-sensitive `referenceId` and an optional `body`.[^s2] A later subrequest can pull a value from an earlier response with the `@{referenceId.field}` syntax, in either its URL or its body. A `[]` operator indexes into arrays, so you can create an Account and then a Contact pointing at `@{refAccount.id}` in one round trip.[^s1][^s2] Two optional flags shape execution. `allOrNone` decides whether any error rolls back the whole request or only skips the subrequests that depend on the failed one; the top-level HTTP status is 200 either way. `collateSubrequests` lets Salesforce bulkify unrelated subrequests, and it defaults to true from API version 49.0. Ordering is then guaranteed only where explicit dependencies exist.[^s2]

Supported subrequest targets include the sObject resources (among them upsert by external ID), Query and QueryAll, and sObject Collections from API 43.0. Resources that return binary data, such as sObject Blob Get, are excluded.[^s1] The whole Composite series counts as **one call** toward the org's API limits.[^s1]

The siblings differ mainly in dependency and transaction semantics:

- **Composite Batch** runs up to 25 independent subrequests serially. It isn't transactional: each success commits at once and isn't rolled back if a later one fails. Subrequests can't pass data to each other, and a batch that runs past 10 minutes times out, leaving the rest unexecuted.[^s3]
- **sObject Tree** creates nested parent-child hierarchies, each with a single root, in one all-or-nothing request. The whole request counts as one API call.[^s4]
- **sObject Collections** acts on a list of records in one request; its create operation can mix object types. Its own `allOrNone` defaults to false, so each record succeeds or fails on its own unless you ask for rollback. Results come back in input order.[^s5]
- **Composite Graph** organizes subrequests into graphs of nodes, and failures are counted per graph. Its node limits allow far larger payloads than the 25 subrequests of plain Composite.[^s1][^s6]

## Limits and gotchas

Limits verified against the Winter '27 REST API Developer Guide:

- **Composite:** at most 25 subrequests per call, and no more than 5 of them may be sObject Collections or query operations.[^s1][^s2] Subrequests can't set `Accept`, `Authorization` or `Content-Type` headers; they inherit these, and including them fails the whole request with HTTP 400.[^s2]
- **sObject Tree:** up to 200 records in total across all trees, no more than five object types, and trees at most five levels deep. A single failure fails the whole request, and the response returns only the failing record's reference ID and error.[^s4]
- **sObject Collections (create):** up to 200 records. Mixed types are split into chunks of consecutive same-type records, with at most 10 chunks per request, so interleaving types burns the chunk budget. A well-formed request returns 200 even when some records fail, so check each result's `success` flag.[^s5]
- **Composite Graph:** up to 75 graphs per payload, 500 nodes per graph and per payload, a maximum depth of 15, and 15 distinct nodes per payload. Processing halts after 14 graph failures, and the remaining graphs report `PROCESSING_HALTED`.[^s6]

A common trap is assuming a 200 response means success. Composite, Collections and Batch all report errors per subrequest or per record, so clients must inspect each item.[^s2][^s3][^s5]

## When to use it (and when not)

Use Composite when a UI or middleware step must chain a few dependent writes and reads with low latency. Use sObject Tree to seed a record hierarchy in one transaction, and sObject Collections to push up to 200 records synchronously.[^s1][^s4][^s5] Choose Composite Graph when one payload must carry many more operations than plain Composite allows, and Composite Batch only for genuinely independent calls where partial commits are acceptable.[^s3][^s6] For tens of thousands of records or more, these synchronous resources are the wrong fit; Bulk API 2.0 handles large asynchronous loads.

## Connections

The composite resources are **part of the REST API** (broader). They are a synchronous **alternative to Bulk API 2.0** for small-to-medium record sets. They are **queried with SOQL** through Query and QueryAll subrequests, and subrequests can address records by **external ID fields** through sObject Rows by External ID.[^s1] Each composite call is **governed by the org's API request limits**: one call for Composite and sObject Tree, though Batch subrequests each count against rate limits.[^s1][^s3][^s4] Inside Salesforce, the triggers and flows each request fires still run under **governor limits**. Choosing among the composite resources, Bulk API and event-driven options is core material for the **Integration Architect certification**.

## Sources

[^s1]: Salesforce Developers, "Send Multiple Requests Using Composite". https://developer.salesforce.com/docs/platform/api-rest/guide/resources-composite-composite-post.html (accessed 2026-11-03)
[^s2]: Salesforce Developers, "Composite Request Body". https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api/requests_composite.htm (accessed 2026-11-03)
[^s3]: Salesforce Developers, "Composite Batch". https://developer.salesforce.com/docs/platform/api-rest/guide/resources-composite-batch.html (accessed 2026-11-03)
[^s4]: Salesforce Developers, "sObject Tree". https://developer.salesforce.com/docs/platform/api-rest/guide/resources-composite-sobject-tree.html (accessed 2026-11-03)
[^s5]: Salesforce Developers, "Create Records Using sObject Collections". https://developer.salesforce.com/docs/platform/api-rest/guide/resources-composite-sobjects-collections-create.html (accessed 2026-11-03)
[^s6]: Salesforce Developers, "Composite Graph Limits". https://developer.salesforce.com/docs/platform/api-rest/guide/resources-composite-graph-limits.html (accessed 2026-11-03)
