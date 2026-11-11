---
id: kt:connect-api
type: API
title: Connect REST API
aliases: [Connect API, Connect in Apex, ConnectApi namespace, ConnectApi classes]
domain: integration
summary: >-
  Salesforce's presentation-oriented REST API (with an Apex twin, Connect in Apex / the ConnectApi namespace) for
  Chatter feeds, files, notifications, Experience Cloud sites, CMS, Commerce and other feature resources, returning
  localized, display-ready JSON or XML rather than raw sObject records.
release: "Winter '27"
status: current
broader: [kt:salesforce-apis]
related: [kt:rest-api, kt:experience-cloud, kt:graphql-api, kt:data-cloud-segmentation, kt:salesforce-industries, kt:apex-testing]
relations:
  - {predicate: dependsOn, object: kt:oauth-2-0}
  - {predicate: governedBy, object: kt:api-request-limits}
  - {predicate: contrastsWith, object: kt:rest-api}
  - {predicate: consumedBy, object: kt:apex}
sources:
  - id: s1
    title: "Connect REST API Introduction (Connect REST API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/connect-rest-api/guide/intro_working_with_chatter_connect.html
    type: official-docs
    accessed: 2026-11-11
  - id: s2
    title: "What Is Connect REST API? (Connect REST API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/connect-rest-api/guide/intro_what_is_chatter_connect
    type: official-docs
    accessed: 2026-11-11
  - id: s3
    title: "Build the Resource URL (Connect REST API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/connect-rest-api/guide/intro_building_url.html
    type: official-docs
    accessed: 2026-11-11
  - id: s4
    title: "Understanding Limits for ConnectApi Classes (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_connect_api_limits.htm
    type: official-docs
    accessed: 2026-11-11
  - id: s5
    title: "Testing ConnectApi Code (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/connectAPI_TestingApex.htm
    type: official-docs
    accessed: 2026-11-11
  - id: s6
    title: "Connect in Apex Features (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/connectapi_features.htm
    type: official-docs
    accessed: 2026-11-11
created: 2026-11-11
---

# Connect REST API

Connect REST API is a versioned Salesforce HTTP API for building client applications that work with feature
resources rather than raw records. Salesforce describes it as giving programmatic access to B2B Commerce, CMS
managed content, Experience Cloud sites, files, notifications, topics and more, grouped into API families such as
Agentforce, Chatter, Chatter Feeds, CMS, Commerce, Experience Cloud, Files and Folders, and Personalization.[^s2]
Chatter REST API resources are a subset of Connect REST API resources.[^s1] The same capabilities are exposed
inside the platform as **Connect in Apex**, the `ConnectApi` namespace, which Salesforce recommends for building
custom experiences within Salesforce and which is available in every org and edition where Apex is enabled.[^s2][^s6]

## How it works

Clients authenticate with OAuth and exchange JSON or XML over standard HTTP methods; response bodies are minimally
HTML entity-encoded by default, and filter parameters let a client ask for a smaller response size group or include
or exclude named properties.[^s1] Unlike record-centric APIs, responses are localized and structured for
presentation, so a mobile app or intranet page can render a feed, user or group without assembling it from
several objects.[^s2]

Resource URLs follow the org's instance and API version. Org-level resources sit under the version path, for
example `/services/data/v67.0/chatter/feeds/news/me/feed-elements`.[^s3] To scope a call to an Experience Cloud
site, `/connect/communities/{communityId}` goes between the version and the resource; the literal `internal` can
stand in for the default site even when digital experiences aren't enabled, and site requests can also go through
the site's own `my.site.com` domain and path.[^s3] Objects such as groups that exist both in the org and in sites
return site-specific results when requested through the site.[^s3]

In Apex, `ConnectApi` classes mirror these resources. For example, `ConnectApi.FeedElement` is the abstract parent
of `FeedItem` (posts) and `GenericFeedElement` (bundles and recommendations), many methods operate in the context
of a single Experience Cloud site, and unauthenticated site guests can call a subset of methods for data they can
access.[^s6]

## Limits and gotchas

- **Shared allocation.** Most Connect REST API requests share the rate limits of other Salesforce APIs.[^s1]
- **Chatter rate limit.** Chatter REST API resources also carry a per-user, per-application, hourly limit.[^s1]
- **Over the limit.** Exceeding the REST limit returns `503 Service Unavailable`.[^s1]
- **ConnectApi DML.** In Apex, every `ConnectApi` write operation costs one DML statement against governor limits.[^s4]
- **ConnectApi API calls.** Most `ConnectApi` calls also count toward the org's total API request allocation.[^s4]
- **Apex Chatter limit.** Methods that need Chatter have a per-user, per-namespace, hourly limit and throw `ConnectApi.RateLimitException` when it is exceeded.[^s4]
- **Version support.** Each version is supported for at least three years from first release; older versions can be retired.[^s1]

Testing is the most common surprise. `ConnectApi` methods run as the context user and don't support `runAs`;
most need org data and fail unless the test is annotated `@IsTest(SeeAllData=true)`.[^s5] Some methods, such as
`getFeedElementsFromFeed`, can't read org data in tests at all: you register canned output with a matching
`setTest…` method first, and the regular method throws if no data was registered for that parameter
combination.[^s5] `Test.startTest` begins a fresh Chatter rate-limit count and `Test.stopTest` restores the earlier
count.[^s4]

## When to use it (and when not)

Use Connect REST API when an external app, mobile client or intranet needs Chatter feeds, users, groups, files or
site content in a display-ready shape; Salesforce singles out mobile feed display as a typical case.[^s2] Use
Connect in Apex when the same features are needed server-side in a custom Lightning or site experience.[^s2] For
plain record create, read, update and delete, or for SOQL queries, the general REST API or GraphQL API is the better
fit, because Connect resources are organized around features, not sObjects.[^s2][^s1]

## Connections

Connect REST API sits under the family of `kt:salesforce-apis` (its **broader** node) and **contrasts with**
`kt:rest-api`: both are REST and versioned, but REST API returns sObject data while Connect returns
presentation-shaped feature resources.[^s1][^s2] It is **related** to `kt:graphql-api`, another option for
UI-oriented reads. It **depends on** `kt:oauth-2-0` for authentication and is **governed by**
`kt:api-request-limits`, since most calls consume the shared allocation.[^s1][^s4] Its `/connect/communities`
scoping ties it to `kt:experience-cloud`.[^s3] Through the `ConnectApi` namespace it is **consumed by** `kt:apex`,
and it is **related** to `kt:apex-testing` practices such as `SeeAllData` and `setTest` registration.[^s5][^s6] The
namespace also carries Data Cloud segment input classes, which is why `kt:data-cloud-segmentation` links here, while
the `kt:salesforce-industries` articles in this graph link here for their business API resources.[^s6]

## Sources
[^s1]: Salesforce Developers, "Connect REST API Introduction". https://developer.salesforce.com/docs/platform/connect-rest-api/guide/intro_working_with_chatter_connect.html (accessed 2026-11-11)
[^s2]: Salesforce Developers, "What Is Connect REST API?". https://developer.salesforce.com/docs/platform/connect-rest-api/guide/intro_what_is_chatter_connect (accessed 2026-11-11)
[^s3]: Salesforce Developers, "Build the Resource URL". https://developer.salesforce.com/docs/platform/connect-rest-api/guide/intro_building_url.html (accessed 2026-11-11)
[^s4]: Salesforce Developers, "Understanding Limits for ConnectApi Classes". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_connect_api_limits.htm (accessed 2026-11-11)
[^s5]: Salesforce Developers, "Testing ConnectApi Code". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/connectAPI_TestingApex.htm (accessed 2026-11-11)
[^s6]: Salesforce Developers, "Connect in Apex Features". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/connectapi_features.htm (accessed 2026-11-11)
