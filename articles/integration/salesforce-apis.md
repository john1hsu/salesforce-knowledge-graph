---
id: kt:salesforce-apis
type: Concept
title: Salesforce APIs
aliases: [Salesforce Platform APIs, Lightning Platform APIs, Salesforce API family, Salesforce API Library]
domain: integration
summary: >-
  The family of programmatic interfaces Salesforce exposes for its platform and products, spanning
  synchronous REST and SOAP data APIs, asynchronous Bulk and Metadata APIs, event streaming through
  Pub/Sub API, and UI, tooling and product-specific APIs; choosing among them is driven by data volume,
  protocol and whether the integration moves data, metadata, events or UI state.
release: "Winter '27"
status: concept
broader: [kt:data-integration, kt:salesforce-platform]
related: [kt:rest-api, kt:bulk-api-2, kt:pub-sub-api, kt:metadata-api, kt:graphql-api, kt:integration-patterns]
relations:
  - {predicate: hasPart, object: kt:soap-api}
  - {predicate: hasPart, object: kt:connect-api}
  - {predicate: hasPart, object: kt:tooling-api}
  - {predicate: hasPart, object: kt:user-interface-api}
  - {predicate: governedBy, object: kt:api-request-limits}
  - {predicate: dependsOn, object: kt:oauth-2-0}
sources:
  - id: s1
    title: "Get to Know the Salesforce Platform APIs (API Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/api_basics/api_basics_overview
    type: official-learning
    accessed: 2026-11-11
  - id: s2
    title: "Accessing Object Data with Salesforce Platform APIs"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/04/accessing-object-data-with-salesforce-platform-apis
    type: official-blog
    accessed: 2026-11-11
  - id: s3
    title: "API Request Limits and Allocations (Salesforce Developer Limits and Allocations Quick Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-app-limits-cheatsheet/guide/salesforce-app-limits-platform-api.html
    type: official-docs
    accessed: 2026-11-11
  - id: s4
    title: "Browse all APIs (API Library)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/apis
    type: official-docs
    accessed: 2026-11-11
  - id: s5
    title: "Get Started with Salesforce APIs — Thanks to Award-Winning Resources"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/05/get-started-with-salesforce-apis
    type: official-blog
    accessed: 2026-11-11
created: 2026-11-11
---

# Salesforce APIs

"Salesforce APIs" is the umbrella term for the many web-service interfaces through which external systems, tools and custom code read and change Salesforce data, metadata and events. The core Salesforce Platform alone offers a dozen general-purpose APIs, each tuned to a protocol, payload format and communication style, and every other product line (Commerce, Marketing, Data 360, MuleSoft, Tableau and the industry clouds) ships its own APIs on top.[^s1][^s5] The Salesforce Developers API Library lists more than fifty separately documented APIs, from REST, SOAP and Bulk API 2.0 to the Models API, Field Service, Loyalty Management and Public Sector REST APIs.[^s4]

## The core platform family

Trailhead's API Basics module groups the platform APIs by what they do and how they talk:[^s1]

- **Data APIs.** REST API (JSON or XML, synchronous) and SOAP API (WSDL contract, XML only, synchronous) handle record CRUD, query and search.[^s1]
- **Volume.** Bulk API is REST-based and asynchronous, built for loading, deleting or extracting large data sets in background jobs.[^s1]
- **Events.** Pub/Sub API streams platform events and Change Data Capture over gRPC and HTTP/2 with binary Avro payloads, so subscribers pull events instead of polling.[^s1]
- **Metadata and tools.** Metadata API (asynchronous SOAP) deploys and retrieves customizations; Tooling API (REST or SOAP) serves smaller metadata pieces to developer tools.[^s1]
- **UI and experience.** User Interface API returns data plus layout metadata for custom apps, GraphQL API returns only requested fields in one call, and Connect REST API covers Chatter, files, CMS, Experience Cloud and B2B Commerce.[^s1]
- **Custom endpoints.** Apex REST and Apex SOAP expose your own Apex classes as web services, subject to Apex governor limits.[^s1][^s2]

## Choosing an API

For record-level integrations that are not UI-driven, Salesforce product management frames the choice by volume: REST sObject resources for single records, Composite resources for tens to thousands of records in fewer round trips, the Query resource for retrieval, and Bulk API 2.0 once a job generally exceeds 2,000 records.[^s2] The same guidance notes that SOAP API and the original Bulk API remain supported but are no longer enhanced, so new development should favour REST and Bulk API 2.0.[^s2] Composite variants differ in transaction semantics: Composite chains up to 25 subrequests, Composite Graph runs up to 500 subrequests in all-or-nothing graphs, and sObject Collections writes up to 200 records as a single call.[^s2] For UI work the recommendation is User Interface API or GraphQL API, and Pub/Sub API replaces polling when the need is near-real-time change notification.[^s1][^s2]

## Access, authentication and limits

API access requires an edition that includes it (Enterprise, Unlimited, Developer and Performance, or Professional with an add-on) and a user with the API Enabled permission; every call except the SOAP `login()` call must be authenticated, normally with an OAuth flow.[^s1] Salesforce also recommends giving each external application its own dedicated integration user for access control and auditability.[^s2]

Usage is metered three ways. Total requests are allocated per rolling 24 hours; in Enterprise Edition the allocation is 100,000 plus a per-license amount (1,000 for each Salesforce or Salesforce Platform license) plus purchased add-ons, while Developer Edition gets 15,000.[^s3] REST, SOAP, Bulk API, Bulk API 2.0, most Connect REST APIs and calls from installed managed packages all count toward it.[^s3] Long-running requests (20 seconds or more) are capped at 25 concurrent in production and sandboxes and 5 in Developer Edition and trial orgs, and REST and SOAP calls other than queries time out after 10 minutes.[^s3] Remaining capacity shows on the System Overview page, in the `Sforce-Limit-Info` REST response header and in the `/limits` REST resource.[^s1]

## Gotchas

- **Per-request cost differs.** sObject Collections counts as one call while each Composite Batch subrequest counts separately.[^s2]
- **Bulk is not free for small jobs.** Bulk API 2.0 carries job overhead and has no completion SLA, so it suits large, not small, workloads.[^s2]
- **Product APIs have their own rules.** Commerce, Marketing Cloud, Data 360 and MuleSoft APIs are documented and authenticated separately from the platform APIs.[^s4][^s5]

## Connections

Salesforce APIs sit under data integration and the Salesforce Platform as the toolbox that integration patterns are built from.[^s1] Its best-known members (REST API, Bulk API 2.0, Pub/Sub API, Metadata API and GraphQL API) have their own nodes, and SOAP API, Connect REST API, Tooling API and User Interface API are parts of the family.[^s1][^s4] The whole family is governed by the org's API request limits and depends on OAuth 2.0 for authenticated access.[^s1][^s3]

## Sources

[^s1]: Trailhead, "Get to Know the Salesforce Platform APIs". https://trailhead.salesforce.com/content/learn/modules/api_basics/api_basics_overview (accessed 2026-11-11)
[^s2]: Salesforce Developers Blog, "Accessing Object Data with Salesforce Platform APIs". https://developer.salesforce.com/blogs/2024/04/accessing-object-data-with-salesforce-platform-apis (accessed 2026-11-11)
[^s3]: Salesforce Developers, "API Request Limits and Allocations". https://developer.salesforce.com/docs/platform/salesforce-app-limits-cheatsheet/guide/salesforce-app-limits-platform-api.html (accessed 2026-11-11)
[^s4]: Salesforce Developers, "Browse all APIs". https://developer.salesforce.com/docs/apis (accessed 2026-11-11)
[^s5]: Salesforce Developers Blog, "Get Started with Salesforce APIs — Thanks to Award-Winning Resources". https://developer.salesforce.com/blogs/2024/05/get-started-with-salesforce-apis (accessed 2026-11-11)
