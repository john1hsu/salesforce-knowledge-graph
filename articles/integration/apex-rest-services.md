---
id: kt:apex-rest-services
type: Feature
title: Apex REST Services
aliases: [Apex REST, Apex REST web services, custom Apex REST API, RestResource, services/apexrest]
domain: integration
summary: >-
  The Apex capability for exposing a global class as a custom REST endpoint under /services/apexrest/, using the
  @RestResource class annotation and @HttpGet, @HttpPost, @HttpPut, @HttpPatch and @HttpDelete method annotations.
release: "Winter '27"
status: current
broader: [kt:apex, kt:salesforce-apis]
related: [kt:remote-call-in, kt:rest-api, kt:apex-callouts, kt:apex-testing, kt:apex-security-with-sharing]
relations:
  - {predicate: alternativeTo, object: kt:rest-api}
  - {predicate: alternativeTo, object: kt:apex-soap-web-services}
  - {predicate: governedBy, object: kt:api-request-limits}
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: dependsOn, object: kt:apex-user-mode}
  - {predicate: dependsOn, object: kt:oauth-2-flows-in-salesforce}
sources:
  - id: s1
    title: "Introduction to Apex REST (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_rest_intro.htm
    type: official-docs
    accessed: 2026-11-22
  - id: s2
    title: "RestResource Annotation (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_classes_annotation_rest_resource.htm
    type: official-docs
    accessed: 2026-11-22
  - id: s3
    title: "Apex REST Methods (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_rest_methods.htm
    type: official-docs
    accessed: 2026-11-22
  - id: s4
    title: "Exposing Data with Apex REST Web Service Methods (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_rest_exposing_data.htm
    type: official-docs
    accessed: 2026-11-22
  - id: s5
    title: "Apex Web Services (Apex Integration Services)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/content/learn/modules/apex_integration_services/apex_integration_webservices
    type: official-learning
    accessed: 2026-11-22
created: 2026-11-22
---

# Apex REST Services

Apex REST lets a developer publish a custom REST endpoint whose behaviour is written in Apex. A class becomes a REST resource through the class-level `@RestResource` annotation, and individual methods are bound to HTTP verbs with annotations such as `@HttpGet`.[^s1] The full annotation set is `@RestResource(urlMapping=...)`, `@HttpGet`, `@HttpPost`, `@HttpPut`, `@HttpPatch` and `@HttpDelete`, plus `@ReadOnly`, which can be applied to any of the HTTP methods.[^s3] Callers authenticate with OAuth 2.0 or a session ID, the same as for the standard REST API.[^s1]

## How it works

The annotated class must be `global`, and its URL mapping is appended to `/services/apexrest/` on the org's domain.[^s2] Trailhead's walkthrough uses global static methods and maps the verbs to CRUD semantics: GET reads, POST creates, DELETE deletes, PUT upserts and PATCH updates only the fields sent.[^s5] That PUT/PATCH difference matters in practice: in the Trailhead example a PUT that leaves out a field clears it.[^s5]

URL mapping rules are strict:

- The mapping must start with `/`, may be up to 255 characters, is case-sensitive and can contain a `*` wildcard.[^s2]
- A wildcard must follow a `/`, and unless it is the final character it must also be followed by one.[^s2]
- An exact match wins; otherwise the longest matching wildcard pattern is used, and no match returns HTTP 404.[^s2]
- In a managed package the namespace becomes part of the path, and a namespaced class wins a URL collision.[^s2]

Request bodies can be JSON (the default, chosen by the Content-Type header) or XML.[^s3] If a method declares parameters, the body is deserialized into them by name, in any order; if it declares none, the raw body is placed in `RestRequest.requestBody`.[^s3] A non-void return value is serialized into the response body, and `RestContext.request` and `RestContext.response` give direct access to headers, parameters and status codes.[^s3] `@HttpGet` and `@HttpDelete` methods must take no parameters, and one class cannot contain two methods with the same HTTP annotation.[^s3] Supported types are primitives, sObjects, lists or String-keyed maps of those, and user-defined types built from them.[^s3]

## Limits and gotchas

Calls to Apex REST classes count against the org's API request limits, and every normal Apex governor limit applies. The maximum request or response size is 6 MB for synchronous Apex and 12 MB for asynchronous Apex.[^s1] Other behaviours to plan for:

- `multipart/form-data` is not supported, and XML cannot carry maps, lists of lists or Connect in Apex objects.[^s3]
- Duplicate parameter names in a request return HTTP 400, as do cyclic user-defined types at run time.[^s3]
- Running out of heap while serializing returns HTTP 200 with an error fragment appended to partial JSON, so large payloads need explicit handling.[^s3]
- Unhandled Apex exceptions surface as HTTP 500; a verb with no matching method returns 405.[^s3]

Security defaults have changed by API version. For classes at API 67.0 and later, custom Apex REST methods run in user mode, so object permissions, field-level security and sharing are enforced, and a class with no sharing keyword runs with sharing; at API 66.0 and earlier the defaults were system mode and without sharing.[^s4] Bypassing these checks now takes an explicit `WITH SYSTEM_MODE` clause or a `without sharing` class.[^s4] Older tutorials that describe Apex web services as running with system privileges predate this change, so check the class's API version.

Testing does not need a real HTTP call: a test builds a `RestRequest`, sets its URI, method, headers and body, assigns it to `RestContext.request` and then calls the method directly.[^s5] Workbench's REST Explorer can exercise a deployed endpoint by its relative `/services/apexrest/...` URI.[^s5]

## When to use it (and when not)

A custom endpoint is worth building when the logic should be hidden from the client, or when one call should replace several round trips through standard APIs.[^s5] Trailhead suggests versioning the URL mapping (for example `/Cases/v1/*`) so the contract can change without breaking callers.[^s5] When the client only needs record CRUD or queries, the standard REST API avoids custom code to maintain and test. SOAP-based Apex web services are the counterpart for clients that need a WSDL contract.[^s5]

## Connections

Apex REST is part of `kt:apex` and one of the inbound entry points among `kt:salesforce-apis`.[^s1] It is the custom-code option within `kt:remote-call-in`, and an `alternativeTo` both the standard `kt:rest-api` and `kt:apex-soap-web-services`.[^s5] It is `governedBy` `kt:api-request-limits` and `kt:governor-limits`.[^s1] It `dependsOn` `kt:apex-user-mode` and the sharing keywords in `kt:apex-security-with-sharing` for its data access, and on `kt:oauth-2-flows-in-salesforce` for authentication.[^s1][^s4] It is the inbound mirror of `kt:apex-callouts`, and its endpoints are covered by `kt:apex-testing` through `RestContext`.[^s5]

## Sources

[^s1]: Salesforce Developers, "Introduction to Apex REST (Apex Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_rest_intro.htm (accessed 2026-11-22)
[^s2]: Salesforce Developers, "RestResource Annotation (Apex Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_classes_annotation_rest_resource.htm (accessed 2026-11-22)
[^s3]: Salesforce Developers, "Apex REST Methods (Apex Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_rest_methods.htm (accessed 2026-11-22)
[^s4]: Salesforce Developers, "Exposing Data with Apex REST Web Service Methods (Apex Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_rest_exposing_data.htm (accessed 2026-11-22)
[^s5]: Trailhead, "Apex Web Services (Apex Integration Services)". https://trailhead.salesforce.com/en/content/learn/modules/apex_integration_services/apex_integration_webservices (accessed 2026-11-22)
