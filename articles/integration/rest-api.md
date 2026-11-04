---
id: kt:rest-api
type: API
title: REST API
aliases: [Salesforce REST API, Lightning Platform REST API, Force.com REST API, sObject REST API]
domain: integration
summary: >-
  Salesforce's synchronous, resource-oriented HTTP interface for org data and metadata, reached under
  /services/data/vXX.X/ with OAuth 2.0 bearer tokens and JSON or XML payloads; the default API for web,
  mobile and record-at-a-time integrations.
release: "Winter '27"
status: current
broader: [kt:data-integration]
related: [kt:connected-apps, kt:external-client-apps, kt:pub-sub-api, kt:metadata-api]
relations:
  - {predicate: hasPart, object: kt:composite-api}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: dependsOn, object: kt:oauth-2-0}
  - {predicate: alternativeTo, object: kt:bulk-api-2}
  - {predicate: contrastsWith, object: kt:soap-api}
  - {predicate: governedBy, object: kt:api-request-limits}
sources:
  - id: s1
    title: "REST Resources and Requests (REST API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-rest/guide/intro-rest-resources.html
    type: official-docs
    accessed: 2026-11-04
  - id: s2
    title: "Quick Start (REST API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/quickstart.htm
    type: official-docs
    accessed: 2026-11-04
  - id: s3
    title: "Limits (REST API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-rest/guide/resources-limits.md
    type: official-docs
    accessed: 2026-11-04
  - id: s4
    title: "Which API Do I Use?"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=integrate_what_is_api.htm&language=en_US
    type: official-docs
    accessed: 2026-11-04
  - id: s5
    title: "Get to Know the Salesforce Platform APIs (API Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/modules/api_basics/units/api_basics_overview
    type: official-learning
    accessed: 2026-11-04
  - id: s6
    title: "Use REST API (API Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/api_basics/api_basics_rest
    type: official-learning
    accessed: 2026-11-04
created: 2026-11-04
---

# REST API

The Salesforce REST API is the platform's general-purpose, synchronous web-service interface. It exposes org functionality as resources, each addressed by a URI and manipulated with standard HTTP methods, and it accepts and returns either JSON or XML.[^s1][^s5] Salesforce positions it as the default choice for web and mobile projects because its lightweight request/response model is easy to integrate with from almost any language or HTTP client.[^s4][^s5]

## How it works

Every call targets a URI of the form `https://MyDomainName.my.salesforce.com/services/data/vXX.X/resource/`, where the My Domain subdomain identifies the org and `vXX.X` pins the API version. A `latest` alias resolves to the most recently released version, and a Versions resource lists all available ones.[^s1] Pinning an explicit version is the safer habit for production integrations, since behaviour is tied to the version an integration was built and tested against.[^s1]

A request has four parts: the resource URI, an HTTP method, headers, and an optional body.[^s6] The API supports HEAD, GET, POST, PATCH, PUT and DELETE, and what each verb does depends on the resource. The `Accept` header chooses JSON or XML for the response (JSON if absent or malformed), `Content-Type` declares the body format, and `Authorization` carries an OAuth 2.0 access token as a Bearer token. Optional headers enable compression and conditional requests. Record IDs in URIs are case-sensitive, while object and field names are not.[^s1]

Typical resources cover the everyday data lifecycle: listing API versions, describing an object and its fields (for example `/sobjects/Account/describe`), creating, updating and deleting records, and running SOQL through the query resource's `q` parameter.[^s6] The Limits resource (`/services/data/vXX.X/limits/`, available since version 29.0) returns each org allocation with its maximum and remaining value, including `DailyApiRequests`, Bulk API batches, asynchronous Apex executions and platform-event deliveries; it requires the View Setup and Configuration permission.[^s3] Salesforce also publishes an OpenAPI 3.0 description of the sObjects REST API as a beta.[^s2]

## Authentication

Callers must first obtain an access token. The Quick Start uses Salesforce CLI, which is already registered as a connected app, but a production integration normally registers its own connected app (or external client app) and uses an appropriate OAuth 2.0 flow.[^s2][^s1]

## Limits and gotchas

- **API allocations.** REST calls count against the org's rolling 24-hour API request total, which varies by edition and licenses; separate concurrency limits cap long-running calls, and timeout limits bound a single call.[^s5]
- **Monitoring usage.** Remaining calls are visible on the System Overview page, in the `Sforce-Limit-Info` response header on REST calls, or through the Limits resource.[^s5][^s3] Limits values are tabulated within about five minutes of consumption, so rapid polling will not give perfectly consistent numbers.[^s3]
- **Record-at-a-time cost.** Each request is synchronous and usually touches one record or one query, so chatty clients burn allocations fast; composite resources or Bulk API are better for volume.[^s4][^s5]

## When to use it (and when not)

Use REST API for mobile and web apps, middleware doing transactional CRUD, and any integration that wants simple HTTP plus JSON.[^s4][^s5] Salesforce's guidance steers large jobs elsewhere: Bulk API 2.0 is the asynchronous option, recommended for jobs of more than 2,000 records, while smaller jobs suit synchronous REST (such as Composite) or SOAP.[^s4] SOAP API offers a formal WSDL contract and XML only, suited to server-to-server integrations, though most of its functionality is also available in REST.[^s5] For UI rendering, User Interface API is the better fit; Connect REST API serves Chatter, Experience Cloud and B2B Commerce; Pub/Sub API replaces polling with real-time event streams; and Metadata API handles customizations rather than data.[^s4][^s5]

## Connections

REST API sits under the broader practice of data integration and is the parent of the Composite API family, whose resources batch several REST subrequests into one call.[^s4] It queries data with SOQL through the query resource and depends on OAuth 2.0 access tokens issued to a connected app or external client app.[^s1][^s2][^s6] Bulk API 2.0 is its high-volume alternative and SOAP API its contract-first counterpart, while Pub/Sub API and Metadata API cover event streaming and metadata respectively.[^s4][^s5] Its consumption is governed by the org's API request limits, which the Limits resource itself exposes.[^s3][^s5]

## Sources

[^s1]: Salesforce Developers, "REST Resources and Requests". https://developer.salesforce.com/docs/platform/api-rest/guide/intro-rest-resources.html (accessed 2026-11-04)
[^s2]: Salesforce Developers, "Quick Start". https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/quickstart.htm (accessed 2026-11-04)
[^s3]: Salesforce Developers, "Limits". https://developer.salesforce.com/docs/platform/api-rest/guide/resources-limits.md (accessed 2026-11-04)
[^s4]: Salesforce Help, "Which API Do I Use?". https://help.salesforce.com/apex/HTViewHelpDoc?id=integrate_what_is_api.htm&language=en_US (accessed 2026-11-04)
[^s5]: Trailhead, "Get to Know the Salesforce Platform APIs". https://trailhead.salesforce.com/en/modules/api_basics/units/api_basics_overview (accessed 2026-11-04)
[^s6]: Trailhead, "Use REST API". https://trailhead.salesforce.com/content/learn/modules/api_basics/api_basics_rest (accessed 2026-11-04)
