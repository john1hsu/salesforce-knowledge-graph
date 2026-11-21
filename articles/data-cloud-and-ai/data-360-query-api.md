---
id: kt:data-360-query-api
type: API
title: Data 360 Query API
aliases: [Data Cloud Query API, Query API V3, Data 360 Query Services, query-sql endpoint, CDP Query API, sfsqlquery]
domain: data-cloud-and-ai
summary: >-
  The SQL interface for reading Data 360 (formerly Data Cloud) data lake and data model objects from outside the
  platform or from Apex, exposed through Connect REST query-sql resources, the direct /api/v3/query endpoints and
  the sfsqlquery Apex namespace, with the V1 and V2 query endpoints kept as legacy.
release: "Winter '27"
status: current
broader: [kt:data-cloud]
related: [kt:data-model-objects, kt:data-lake-objects, kt:calculated-insights, kt:data-graphs]
relations:
  - {predicate: governedBy, object: kt:data-cloud-limits}
  - {predicate: dependsOn, object: kt:external-client-apps}
  - {predicate: dependsOn, object: kt:client-credentials-flow}
  - {predicate: consumedBy, object: kt:queueable-apex}
  - {predicate: contrastsWith, object: kt:ingestion-api}
sources:
  - id: s1
    title: "Query Data using Query API (Data 360 REST API Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-query-guide/references/data-cloud-query-api-reference/c360a-api-queryservices-overview.html
    type: official-docs
    accessed: 2026-11-21
  - id: s2
    title: "Data 360 SQL Query APIs"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-query-guide/guide/dc-sql-query-apis.html
    type: official-docs
    accessed: 2026-11-21
  - id: s3
    title: "Submit SQL Query (POST /api/v3/query)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-query-guide/references/data-cloud-query-api-reference/query-api-v3-post.html
    type: official-docs
    accessed: 2026-11-21
  - id: s4
    title: "Legacy Query Services API (Query V1 and V2 API)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-query-guide/references/data-cloud-query-api-reference/c360a-api-queryservices-legacy.html
    type: official-docs
    accessed: 2026-11-21
  - id: s5
    title: "Query Data 360 Data with Apex"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-query-guide/guide/dc-apex-query.html
    type: official-docs
    accessed: 2026-11-21
  - id: s6
    title: "Query Data in Data 360 (Get Started)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-query-guide/guide/query-guide-get-started.html
    type: official-docs
    accessed: 2026-11-21
created: 2026-11-21
---

# Data 360 Query API

The Data 360 Query API is how code reads harmonized customer data out of Data 360 with SQL. Salesforce positions it
for custom queries that no object-specific API or language library already covers: joins, aggregations and
transformations across data model objects (DMOs) and data lake objects (DLOs), and large extracts.[^s2] Data Cloud
was rebranded Data 360 on October 14, 2025, so older material calls this the Data Cloud or CDP Query API.[^s6] The
SQL it accepts is Data 360 SQL; the guide warns that calculated insights and data transforms are authored in a
different dialect, so a statement that works in one place may not work in the other.[^s6]

## Three ways in

- **Connect REST API.** Recommended for most integrations: POST `/services/data/vXX.X/ssot/query-sql` submits a statement, and companion GET, rows and DELETE resources return status, page through results and cancel.[^s1]
- **Direct Data 360 REST API (V3).** POST `/api/v3/query` on the tenant's separate Data 360 instance URL, with status, rows, chunks, metadata and cancel resources; Salesforce calls it the interface for new integrations.[^s1][^s3]
- **Apex.** The `sfsqlquery` namespace (SqlStatement, SqlRowIterator, Row, QueryHandle, SqlQueueable) is the recommended path for new Apex code; `ConnectApi.CdpQuery` remains as a lower-level option.[^s5]

REST callers authenticate with an OAuth 2.0 bearer token, typically from a client-credentials integration, while
Apex runs with the current user's session and Data 360 permissions.[^s1][^s5] Setup starts with an external client
app and OAuth, and the Metadata API is the suggested way to discover which objects exist before writing SQL.[^s6]

## How execution works

Queries can come back synchronously or asynchronously, and the documentation tells clients to handle both.[^s1] On
the V3 endpoint the `transferMode` field picks the behaviour. ADAPTIVE, the default, returns rows inline if the
query finishes within an adaptive timeout and otherwise falls back to an asynchronous response. ASYNC always returns
only metadata and zero rows, and the client polls the status resource until the query completes.[^s3] The query ID
and progress come back in an `x-hyperdb-status` response header, and large result sets are best read through the
chunk resource rather than offset paging.[^s1][^s3]

The V3 body also supports bind parameters in three placeholder styles, session settings such as time zone, date
style and a query timeout, and a `queryRowLimit` that acts like an implicit LIMIT. Setting it to zero returns
only the result schema.[^s3] Responses default to JSON, but an Apache Arrow stream can be requested on the submit,
rows, chunk and metadata resources for faster columnar transfer.[^s1]

In Apex, the three workflows are: run a new statement and iterate rows, reopen earlier results through a
QueryHandle, and process large datasets asynchronously by extending SqlQueueable, which chains Queueable jobs per
data chunk.[^s5]

## Limits and gotchas

- In ADAPTIVE mode, the `resultRange.byteLimit` that caps the inline result is 20 MB by default and at most.[^s3]
- Connect REST query results can be re-read for 24 hours without more consumption, so page through stored rows instead of resubmitting.[^s1]
- Bind parameter values are always JSON strings, and their types use SQL names such as varchar or bigint.[^s3]
- Without an explicit `date_style`, a literal such as 01/08/1999 is ambiguous; set the style in the session settings.[^s3]
- Fields without configured key qualifiers come back null; join on them null-safely with IS NOT DISTINCT FROM.[^s1]
- Errors return HTTP 400, 401, 408, 429 or 500 with a SQLSTATE code and, for syntax errors, a character position.[^s3]

Selecting every column is discouraged: filter with WHERE and bound the result with LIMIT.[^s1] Row and rate
allocations are published in the Data 360 limits documentation rather than in the API reference.[^s1] In Apex,
Salesforce advises asynchronous patterns and polling so that long queries don't run into governor limits.[^s5]

## Legacy V1 and V2

Query API V1 (POST `/api/v1/query`) is synchronous only. V2 (POST `/api/v2/query`, then GET with a `nextBatchId`)
accepts ANSI SQL over data stream, profile, engagement and unified objects and pages results in batches.[^s4] Both
are documented as legacy, and the reference points new work to the Connect REST query services and offers a
migration guide to V3.[^s4][^s3] No retirement date was published on the pages checked for Winter '27.[^s4]

## When to use it (and when not)

Use it when an external app, a warehouse job or Apex logic needs set-based SQL over unified data. For a single
object-oriented read, the object-specific Connect REST or Data Cloud REST APIs are simpler, and for BI or desktop
SQL clients the JDBC and Python libraries or integrated apps such as Query Editor avoid hand-rolled polling.[^s6]
Calculated insights or data transforms are the better home for logic that should run inside Data 360 on a
schedule, since they use their own SQL dialect and persist results there.[^s6]

## Connections

The API sits under [[kt:data-cloud]] and queries [[kt:data-model-objects]] and [[kt:data-lake-objects]], including
the outputs of [[kt:calculated-insights]] and [[kt:data-graphs]].[^s1][^s2] Its allocations are part of
[[kt:data-cloud-limits]], its REST callers depend on [[kt:external-client-apps]] and the
[[kt:client-credentials-flow]] for tokens, and the Apex SqlQueueable class builds on [[kt:queueable-apex]].[^s1][^s5]
It is the read-side counterpart of the [[kt:ingestion-api]]: the query guide covers extraction, while loading
records into Data 360 is documented separately.[^s2]

## Sources
[^s1]: Salesforce Developers, "Query Data using Query API". https://developer.salesforce.com/docs/data/data-cloud-query-guide/references/data-cloud-query-api-reference/c360a-api-queryservices-overview.html (accessed 2026-11-21)
[^s2]: Salesforce Developers, "Data 360 SQL Query APIs". https://developer.salesforce.com/docs/data/data-cloud-query-guide/guide/dc-sql-query-apis.html (accessed 2026-11-21)
[^s3]: Salesforce Developers, "Submit SQL Query". https://developer.salesforce.com/docs/data/data-cloud-query-guide/references/data-cloud-query-api-reference/query-api-v3-post.html (accessed 2026-11-21)
[^s4]: Salesforce Developers, "Legacy Query Services API". https://developer.salesforce.com/docs/data/data-cloud-query-guide/references/data-cloud-query-api-reference/c360a-api-queryservices-legacy.html (accessed 2026-11-21)
[^s5]: Salesforce Developers, "Query Data 360 Data with Apex". https://developer.salesforce.com/docs/data/data-cloud-query-guide/guide/dc-apex-query.html (accessed 2026-11-21)
[^s6]: Salesforce Developers, "Query Data in Data 360". https://developer.salesforce.com/docs/data/data-cloud-query-guide/guide/query-guide-get-started.html (accessed 2026-11-21)
