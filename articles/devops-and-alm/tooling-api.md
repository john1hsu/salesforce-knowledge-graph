---
id: kt:tooling-api
type: API
title: Tooling API
aliases: [Salesforce Tooling API, Force.com Tooling API, /services/data/tooling]
domain: devops-and-alm
summary: >-
  The Salesforce API, with REST and SOAP interfaces, that exposes development metadata such as Apex classes,
  debug logs, test runs and code coverage as queryable objects, giving developer tools fine-grained access to org metadata.
release: "Winter '27"
status: current
broader: [kt:application-lifecycle-management]
related: [kt:source-tracking, kt:apex-testing, kt:apex, kt:rest-api]
relations:
  - {predicate: contrastsWith, object: kt:metadata-api}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: queriedWith, object: kt:salesforce-cli}
  - {predicate: governedBy, object: kt:api-request-limits}
sources:
  - id: s1
    title: "Introducing Tooling API (Tooling API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling
    type: official-docs
    accessed: 2026-11-06
  - id: s2
    title: "When to Use Tooling API (Tooling API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/intro_tasks.htm
    type: official-docs
    accessed: 2026-11-06
  - id: s3
    title: "REST Resources (Tooling API Developer Guide, Winter '27)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.api_tooling.meta/api_tooling/intro_rest_resources.htm
    type: official-docs
    accessed: 2026-11-06
  - id: s4
    title: "SOQL Operation Limitations (Tooling API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/reference_objects_soql_limits.htm
    type: official-docs
    accessed: 2026-11-06
  - id: s5
    title: "ApexCodeCoverageAggregate (Tooling API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/tooling_api_objects_apexcodecoverageaggregate.htm
    type: official-docs
    accessed: 2026-11-06
  - id: s6
    title: "data query (Salesforce CLI Command Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_data_query.html
    type: official-docs
    accessed: 2026-11-06
  - id: s7
    title: "SourceMember (Tooling API Developer Guide, Summer '23)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.244.0.api_tooling.meta/api_tooling/tooling_api_objects_sourcemember.htm
    type: official-docs
    accessed: 2026-11-06
created: 2026-11-06
---

# Tooling API

The Tooling API is the Salesforce API intended for people who build development tools: IDE extensions, CI utilities, code-quality scanners and admin scripts. Salesforce positions it for adding features to existing platform tools, embedding development modules in enterprise integration tools, and building specialised tools for one application or service. It offers both SOAP and REST interfaces, and the documentation suggests REST when the client language is not strongly typed, such as JavaScript.[^s1] In Winter '27 the guide is at API version 68.0.[^s3]

## How it works

Where most APIs expose business records, the Tooling API exposes development metadata as sObject-like records that can be described, queried and, for many types, created or updated. Its core advantage is granularity: SOQL support for many metadata types lets a tool fetch small pieces of metadata, which performs better and suits interactive applications, and a single element inside a complex type can be changed on its own.[^s1][^s2] Salesforce groups its uses by task:[^s2]

- **Object and field definitions** through `EntityDefinition`, `FieldDefinition`, `CustomField`, `ValidationRule` and `WorkflowRule`.[^s2]
- **Source code working copies** of Apex classes, triggers and Visualforce through `ApexClassMember`, `ApexTriggerMember` and related member objects held in a `MetadataContainer`, with `ContainerAsyncRequest` used to check them for errors and commit them to the org.[^s2]
- **Debugging**: `TraceFlag` sets logging for yourself or other users, `ApexLog` holds the logs, and `ApexExecutionOverlayAction` sets heap-dump markers whose output is read from `ApexExecutionOverlayResult`.[^s2]
- **Tests and coverage**: `ApexTestQueueItem` and `ApexTestResult` run and record tests, while `ApexCodeCoverage`, `ApexOrgWideCoverage` and `ApexCodeCoverageAggregate` report coverage.[^s2]

`ApexCodeCoverageAggregate`, for example, holds aggregate coverage results per Apex class or trigger and has been available since version 29.0.[^s5]

The REST interface lives under `/services/data/vXX.X/tooling/` on the org's My Domain. Its resources include `/query/` for SOQL, `/search/` for SOSL, `/sobjects/` for describe and CRUD, `/executeAnonymous/` for anonymous Apex, `/runTestsAsynchronous/` and `/runTestsSynchronous/` for Apex and automated flow tests, `/completions` for Apex and Visualforce code completion, and `/sobjects/ApexLog/{id}/Body/` for raw debug logs. Winter '27 adds `/apexCompileResults/` (API 68.0) and a beta `/symbols` resource for Apex type metadata.[^s3]

## Limits and gotchas

- **Restricted SOQL on catalog objects.** Queries against Metadata Catalog entities such as `EntityDefinition`, `FieldDefinition`, `EntityParticle` and `UserFieldAccess` (and custom metadata types) do not support `COUNT()`, `GROUP BY`, `LIMIT`, `OFFSET`, `OR`, `NOT` or `INCLUDES`. Most raise an error, but `LIMIT` and `OFFSET` are silently ignored, so a tool can get wrong results without any warning.[^s4]
- **Synchronous test runs** must keep all test methods in one class, and since API 40.0 posting to `/runTestsSynchronous/` needs the View Setup permission.[^s3]
- **Anonymous Apex** requests from components in managed packages are blocked.[^s3]
- **API consumption.** Calls count against the org's API limits; the composite resource (API 40.0 and later) can bundle several Tooling API requests into one call that counts once.[^s3]
- Required permissions differ by endpoint and object, so check each resource before you build on it.[^s3]

## When to use it (and when not)

Use the Tooling API for interactive, fine-grained work: reading one class body, checking coverage, tailing debug logs, running a test class, or querying field definitions for a documentation or org-analysis tool. Salesforce also lists source control integration, continuous integration and deploying individual Apex classes or triggers as fits.[^s2] For moving whole sets of components between orgs as packaged deployments, the file-based Metadata API remains the standard route. From the command line, `sf data query --use-tooling-api` runs SOQL against Tooling API objects, for example to list Apex triggers.[^s6]

## Connections

The Tooling API **contrasts with** the **Metadata API**: both work on metadata, but the Tooling API trades bulk deploy and retrieve for small, queryable units.[^s2] It is **queried with SOQL** and reached from the **Salesforce CLI** through the tooling flag.[^s4][^s6] It shares REST conventions with the **REST API**, and its usage is **governed by API request limits**.[^s3] Its test-run and coverage objects make it the programmatic face of **Apex testing**, its code objects serve **Apex** development, and **source tracking** records each tracked change as a `SourceMember` Tooling API object, present in every scratch org and in source-tracked sandboxes.[^s2][^s5][^s7] As a tool-building API, it sits under **application lifecycle management**.[^s1]

## Sources

[^s1]: Salesforce, "Introducing Tooling API", Tooling API Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling (accessed 2026-11-06)
[^s2]: Salesforce, "When to Use Tooling API", Tooling API Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/intro_tasks.htm (accessed 2026-11-06)
[^s3]: Salesforce, "REST Resources", Tooling API Developer Guide (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.264.0.api_tooling.meta/api_tooling/intro_rest_resources.htm (accessed 2026-11-06)
[^s4]: Salesforce, "SOQL Operation Limitations", Tooling API Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/reference_objects_soql_limits.htm (accessed 2026-11-06)
[^s5]: Salesforce, "ApexCodeCoverageAggregate", Tooling API Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/tooling_api_objects_apexcodecoverageaggregate.htm (accessed 2026-11-06)
[^s6]: Salesforce, "data query", Salesforce CLI Command Reference. https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_data_query.html (accessed 2026-11-06)
[^s7]: Salesforce, "SourceMember", Tooling API Developer Guide (Summer '23). https://developer.salesforce.com/docs/atlas.en-us.244.0.api_tooling.meta/api_tooling/tooling_api_objects_sourcemember.htm (accessed 2026-11-06)
