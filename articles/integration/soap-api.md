---
id: kt:soap-api
type: API
title: SOAP API
aliases: [Salesforce SOAP API, Lightning Platform SOAP API, Force.com Web Services API, Enterprise WSDL, Partner WSDL]
domain: integration
summary: >-
  Salesforce's synchronous, WSDL-described web services interface for creating, reading, updating,
  deleting and querying org records over SOAP 1.1 and XML; a formal-contract alternative to the REST API,
  typed per org (enterprise WSDL) or generically (partner WSDL).
release: "Winter '27"
status: current
broader: [kt:salesforce-apis, kt:data-integration]
related: [kt:metadata-api, kt:tooling-api, kt:external-id-fields, kt:remote-call-in]
relations:
  - {predicate: contrastsWith, object: kt:rest-api}
  - {predicate: alternativeTo, object: kt:bulk-api-2}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: queriedWith, object: kt:sosl}
  - {predicate: dependsOn, object: kt:oauth-2-0}
  - {predicate: governedBy, object: kt:api-request-limits}
sources:
  - id: s1
    title: "About SOAP API (SOAP API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/
    type: official-docs
    accessed: 2026-11-12
  - id: s2
    title: "API Call Basics (SOAP API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/calls.htm
    type: official-docs
    accessed: 2026-11-12
  - id: s3
    title: "SOAP API Call Limits (Salesforce Developer Limits and Allocations Quick Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-app-limits-cheatsheet/guide/salesforce-app-limits-platform-apicalls.html
    type: official-docs
    accessed: 2026-11-12
  - id: s4
    title: "SOAP API End-of-Life Policy"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api/guide/api-eol-soap.html
    type: official-docs
    accessed: 2026-11-12
  - id: s5
    title: "login() (SOAP API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/workdotcom_dev/sforce_api_calls_login.htm
    type: official-docs
    accessed: 2026-11-12
  - id: s6
    title: "Get to Know the Salesforce Platform APIs (Trailhead, API Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/api_basics/api_basics_overview
    type: official-learning
    accessed: 2026-11-12
created: 2026-11-12
---

# SOAP API

SOAP API is the Salesforce web services interface that gives client applications programmatic access to the records in an org, built around Salesforce objects.[^s1] It is one of the oldest platform APIs and still a common choice for server-to-server integrations with ERP, finance and other back-office systems, because its WSDL acts as a formal contract between Salesforce and the consumer.[^s6] Requests and responses use XML only, whereas the REST API accepts JSON or XML.[^s6]

## How it works

The API follows SOAP 1.1, WSDL 1.1 and the WS-I Basic Profile 1.1, so any language with a SOAP toolkit can generate a client stub from the WSDL; Salesforce's own samples use Java (the open-source WSC library) and C#/.NET.[^s1] You download one of two WSDLs from the org and import it into your development platform.[^s1]

The **enterprise WSDL** is strongly typed and mirrors one org's schema, so it changes when custom objects or fields are added, renamed or removed, and you must regenerate it to see them; it is aimed at customers integrating their own org.[^s1] The **partner WSDL** is loosely typed and works against any org's object model, which is why ISVs and partners building multi-org tools use it.[^s1]

Calls are synchronous: the client waits for the response, and asynchronous calls are not supported in this API.[^s2] Writes commit automatically, and in a multi-record create, update or delete each record is its own transaction, so some records can succeed while others fail; from API version 20.0 the `AllOrNoneHeader` makes create, update, upsert, delete and undelete roll back unless every record succeeds.[^s2] Calls fall into three groups: core calls for data work such as `login`, `query`, `search`, `create`, `update` and `delete`; describe calls such as `describeGlobal` and `describeSObject` for metadata about the data model; and utility calls for tasks like fetching the server time or changing passwords.[^s2]

Each Salesforce release ships a new SOAP API version (Winter '24 was 59.0 and Spring '24 was 60.0), and Salesforce does not guarantee an integration built on one version keeps working unchanged on later ones.[^s1] Using the API requires Enterprise, Performance, Unlimited or Developer Edition (some Professional Edition orgs have API access enabled) and the **API Enabled** user permission; the Salesforce Integration user license grants API-only access for system-to-system work.[^s1]

## Authentication and the login() retirement

Historically a client called `login()` with a username and password, received a session ID, the user ID and the endpoint URL to use for later calls, and put the session ID in the SOAP header of each subsequent request.[^s5] Those calls count toward a login rate limit of 3,600 calls per user per hour.[^s5] The `login()` call is now disabled by default in new orgs, is available only up to API version 64.0, and from version 67.0 any user who calls it after it is enabled also needs the Use Any API Auth permission.[^s5] Salesforce has scheduled `login()` for retirement in Summer '27, with versions 62.0 to 64.0 supported for at least two years after their release.[^s4] New integrations should therefore obtain a session through OAuth 2.0 with a connected app or external client app, a path the developer guide documents alongside the API.[^s1]

## Limits and gotchas

The following per-call limits were taken from the Salesforce Developer Limits and Allocations quick reference.[^s3]

- `create()` and `update()` accept at most 200 records per call; a larger request fails entirely.[^s3]
- `query()` and `queryMore()` return batches of up to 2,000 records, a suggested maximum only, capped at 200 if two or more long text fields are selected.[^s3]
- `merge()` takes up to 200 merge requests per call with three records per merge, master included.[^s3]
- `describeSObjects()` returns at most 100 objects, and the `login()` request is limited to 10 KB.[^s3]
- `getDeleted()` throws `EXCEEDED_ID_LIMIT` if more than 600,000 records would be returned.[^s3]

Calls also draw on the org's rolling 24-hour API request allocation and are subject to timeout and concurrent long-running request limits; the remaining allocation is reported in the response under the API REQUESTS element.[^s6] Version retirement is a recurring gotcha: versions 31.0 to 40.0 become unsupported in Summer '27 and are retired in Summer '28, and calls to a retired version fail with `500:UNSUPPORTED_API_VERSION`.[^s4] The API Total Usage event type in event log files identifies which integrations still call old versions.[^s4] Salesforce supports each version for at least three years and gives at least one year's notice before ending support.[^s4]

## When to use it (and when not)

Most SOAP functionality is also exposed by the REST API, so the choice is mainly about the standard that suits the consumer.[^s6] SOAP API fits middleware and enterprise stacks that already generate typed clients from WSDLs and value a strict contract, while REST is lighter for web and mobile clients.[^s6] Because writes are capped at 200 records per synchronous call, very large loads are usually better served by `kt:bulk-api-2`.[^s3]

## Connections

SOAP API is one member of the `kt:salesforce-apis` family and a building block of `kt:data-integration`; it is most often compared with the `kt:rest-api`, which offers mostly the same operations with JSON payloads, and is an `alternativeTo` `kt:bulk-api-2` for record loads.[^s6] Its core `query` and `search` calls are where `kt:soql` and `kt:sosl` statements run, and its `upsert` call is one of the write operations that `kt:external-id-fields` support.[^s2] Authentication is moving to `kt:oauth-2-0` as `login()` retires, and every call counts against `kt:api-request-limits`.[^s4] The `kt:metadata-api` and `kt:tooling-api` reuse the same SOAP style for metadata and developer tooling, and an external system calling into Salesforce through SOAP API is one way to implement the `kt:remote-call-in` pattern.[^s1]

## Sources

[^s1]: Salesforce Developers, "About SOAP API (SOAP API Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/ (accessed 2026-11-12)
[^s2]: Salesforce Developers, "API Call Basics (SOAP API Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/calls.htm (accessed 2026-11-12)
[^s3]: Salesforce Developers, "SOAP API Call Limits". https://developer.salesforce.com/docs/platform/salesforce-app-limits-cheatsheet/guide/salesforce-app-limits-platform-apicalls.html (accessed 2026-11-12)
[^s4]: Salesforce Developers, "SOAP API End-of-Life Policy". https://developer.salesforce.com/docs/platform/api/guide/api-eol-soap.html (accessed 2026-11-12)
[^s5]: Salesforce Developers, "login() (SOAP API Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.api.meta/workdotcom_dev/sforce_api_calls_login.htm (accessed 2026-11-12)
[^s6]: Trailhead, "Get to Know the Salesforce Platform APIs". https://trailhead.salesforce.com/api_basics/api_basics_overview (accessed 2026-11-12)
