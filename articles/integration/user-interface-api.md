---
id: kt:user-interface-api
type: API
title: User Interface API
aliases: [UI API, Salesforce UI API, ui-api, User Interface REST API]
domain: integration
summary: >-
  A Salesforce REST API under /services/data/vXX.X/ui-api that returns record data together with the metadata
  needed to render it (layouts, object info, picklists, actions, list views), already shaped by the running
  user's permissions and locale; it is the API that Lightning Experience and Lightning Data Service build on.
release: "Winter '27"
status: current
broader: [kt:salesforce-apis]
related: [kt:rest-api, kt:page-layouts, kt:external-objects, kt:wire-service, kt:duplicate-management]
relations:
  - {predicate: consumedBy, object: kt:lightning-data-service}
  - {predicate: consumedBy, object: kt:graphql-api}
  - {predicate: governedBy, object: kt:api-request-limits}
  - {predicate: dependsOn, object: kt:field-level-security}
  - {predicate: dependsOn, object: kt:oauth-2-0}
  - {predicate: integratesWith, object: kt:connect-api}
sources:
  - id: s1
    title: "Get Started with User Interface API (User Interface API Developer Guide, v68.0)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.uiapi.meta/uiapi/ui_api_get_started_intro.htm
    type: official-docs
    accessed: 2026-11-12
  - id: s2
    title: "Supported Objects (User Interface API Developer Guide, v68.0)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.uiapi.meta/uiapi/ui_api_get_started_supported_objects.htm
    type: official-docs
    accessed: 2026-11-12
  - id: s3
    title: "Records (User Interface API Developer Guide, v68.0)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.uiapi.meta/uiapi/ui_api_resources_record.htm
    type: official-docs
    accessed: 2026-11-12
  - id: s4
    title: "User Interface API Resources (User Interface API Developer Guide, v68.0)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.uiapi.meta/uiapi/ui_api_resources_overview.htm
    type: official-docs
    accessed: 2026-11-12
  - id: s5
    title: "Work with Records (User Interface API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.uiapi.meta/uiapi/ui_api_features_records.htm
    type: official-docs
    accessed: 2026-11-12
  - id: s6
    title: "Introduction to the Salesforce UI API"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2018/01/introduction-salesforce-ui-api
    type: official-blog
    accessed: 2026-11-12
created: 2026-11-12
---

# User Interface API

User Interface API (UI API) is the Salesforce REST API for building user interfaces. Its resources supply both the data and the metadata a client needs to draw Salesforce screens: records, object information, layouts, actions, list views, favorites, apps and the org's theme.[^s4] Salesforce built it because admins can change layouts, permissions and rules at any time, and a custom UI that hard-codes them goes stale. Instead of combining a Metadata API or `describe/layout` call with separate data queries, a UI API response returns the layout and the data together, already filtered by field-level security and sharing and formatted for the user's locale.[^s6] Lightning Experience itself reads and writes data this way through Lightning Data Service.[^s6]

## How it works

Requests go to a versioned path such as `https://MyDomainName.my.salesforce.com/services/data/v68.0/ui-api`; v68.0 is the Winter '27 version. Authentication is OAuth 2.0, as with the other Salesforce REST APIs, and OAuth settings are configured in an external client app.[^s1] The resources fall into a few families:[^s4]

- **Records**: record data with layout and object metadata, object info, picklist values, child records, create, clone, update and delete.[^s3]
- **Actions, Lists, Favorites and Apps**: metadata for buttons and quick actions, list views and related lists, user favorites, and app navigation.[^s4]
- **Utility resources**: the org's active theme and the session's cross-site request forgery (CSRF) token.[^s4]

The `/ui-api/object-info` directory lists the supported objects the context user can access, with one `/ui-api/object-info/{objectApiName}` resource per object. `/ui-api/record-ui/{recordIds}` returns record data and layout metadata in one call.[^s2] Responses include display values formatted for the user's locale, default values for new or cloned records, and layouts tailored to large, medium or small form factors.[^s6] Lightweight default-value resources skip layout information and return only the fields you request.[^s3]

UI API supports HTTP caching. Record responses carry a `weakEtag`, and responses include an ETag header that a client sends back in `If-None-Match`. If its copy is still current, the server answers 304 Not Modified with headers only.[^s1] Other write helpers include idempotent record writes to avoid duplicates when a network call is retried, Base64 binary upload during create or update, and file and file-version upload.[^s5] There are also resources for lookup suggestions and duplicate checks.[^s3]

## Limits and gotchas

Checked against the Winter '27 (v68.0) guide:

- UI API counts against Salesforce API limits and Connect REST API limits. Over the rate limit, every UI API resource returns 503 Service Unavailable.[^s1]
- Batch object-info requests accept up to 2,000 objects, and batch create, update and delete accept up to 200 records per request.[^s3]
- All custom and external objects are supported, but only *many* standard objects. List views and MRU list views cover only a subset of those, and not every resource supports every object. Check `/ui-api/object-info` instead of assuming.[^s2]
- Child-record responses can get large and slow. Request only the relationships you need and set a page size.[^s5]
- Parts of the API are case-sensitive. Dates use ISO 8601, and integers of 2^31 or more must be sent as quoted strings.[^s1]
- Experience Cloud users with Customer Community or Partner Community licenses can call UI API. Components such as `lightning-record-view-form` on site pages run as the site user and can consume API limits even without the API Enabled permission.[^s1]

## When to use it (and when not)

Use UI API when a custom web, mobile or desktop client should look and behave like Salesforce. In that case it should respect the admin's current layouts, required fields, picklist dependencies, permissions and locale without hard-coding them.[^s6] Because its responses depend on the user and context, it is not meant for data extraction or bulk loads; use Bulk API 2.0 or the REST API for those. For design-time org configuration, use the Metadata API.[^s6] Inside Lightning components, developers usually don't call UI API endpoints directly. They use Lightning Data Service, which calls UI API for them and caches the results.[^s6]

## Connections

UI API is one of the **Salesforce APIs** and shares the REST API's `/services/data` base path, OAuth 2.0 authentication and versioning. It differs from the **REST API** by returning presentation-ready metadata (**page layouts**, display values and actions) alongside the data.[^s1][^s6] It is **consumed by Lightning Data Service**, so the **wire service** adapters in Lightning Web Components rest on it. The **GraphQL API** builds on UI API's set of supported objects as well.[^s6][^s2] Because responses enforce the user's **field-level security** and sharing, the API **depends on** those controls.[^s6] It **integrates with the Connect REST API**, whose rate limits it shares, and it is **governed by API request limits**.[^s1] It supports **external objects** as fully as custom objects, and its duplicate-check resources reflect the org's **duplicate management** configuration.[^s2][^s3]

## Sources

[^s1]: Salesforce Developers, "Get Started with User Interface API (User Interface API Developer Guide, v68.0)". https://developer.salesforce.com/docs/atlas.en-us.264.0.uiapi.meta/uiapi/ui_api_get_started_intro.htm (accessed 2026-11-12)
[^s2]: Salesforce Developers, "Supported Objects (User Interface API Developer Guide, v68.0)". https://developer.salesforce.com/docs/atlas.en-us.264.0.uiapi.meta/uiapi/ui_api_get_started_supported_objects.htm (accessed 2026-11-12)
[^s3]: Salesforce Developers, "Records (User Interface API Developer Guide, v68.0)". https://developer.salesforce.com/docs/atlas.en-us.264.0.uiapi.meta/uiapi/ui_api_resources_record.htm (accessed 2026-11-12)
[^s4]: Salesforce Developers, "User Interface API Resources (User Interface API Developer Guide, v68.0)". https://developer.salesforce.com/docs/atlas.en-us.264.0.uiapi.meta/uiapi/ui_api_resources_overview.htm (accessed 2026-11-12)
[^s5]: Salesforce Developers, "Work with Records (User Interface API Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.uiapi.meta/uiapi/ui_api_features_records.htm (accessed 2026-11-12)
[^s6]: Salesforce Developers Blog, "Introduction to the Salesforce UI API". https://developer.salesforce.com/blogs/2018/01/introduction-salesforce-ui-api (accessed 2026-11-12)
