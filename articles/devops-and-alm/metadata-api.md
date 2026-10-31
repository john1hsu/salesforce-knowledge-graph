---
id: kt:metadata-api
type: API
title: Metadata API
aliases: [MDAPI, Salesforce Metadata API, mdapi deploy]
domain: devops-and-alm
summary: >-
  The Salesforce API for retrieving, deploying, creating, updating and deleting org customizations (metadata) rather
  than records, through asynchronous file-based deploy/retrieve of .zip packages and synchronous CRUD-based calls.
release: "Winter '27"
status: current
broader: [kt:application-lifecycle-management]
related: [kt:change-sets, kt:connected-apps, kt:apex-testing]
relations:
  - {predicate: queriedWith, object: kt:salesforce-cli}
  - {predicate: dependsOn, object: kt:apex-testing}
  - {predicate: hasPart, object: kt:package-xml-manifest}
sources:
  - id: s1
    title: "Deploying and Retrieving Metadata (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/file_based.htm
    type: official-docs
    accessed: 2026-10-31
  - id: s2
    title: "Salesforce Developer Limits and Allocations Quick Reference: Platform Metadata"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-app-limits-cheatsheet/guide/salesforce-app-limits-platform-metadata.html
    type: official-docs
    accessed: 2026-10-31
  - id: s3
    title: "Deploy Metadata with Apex Testing Using REST"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_rest_deploy.htm
    type: official-docs
    accessed: 2026-10-31
  - id: s4
    title: "CRUD-Based Calls (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_crud_based_calls_intro.htm
    type: official-docs
    accessed: 2026-10-31
  - id: s5
    title: "Deploy Metadata Using the Manifest"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/package-xml/package-xml-deploy
    type: official-learning
    accessed: 2026-10-31
created: 2026-10-31
---

# Metadata API

The Metadata API is the Salesforce API that works on an org's *configuration* instead of its business records. Custom objects and fields, permission sets, flows, Apex classes and many other component types are represented as XML files, which the API can pull out of one org and push into another.[^s1] Retrieved files can be put under version control, compared, and later deployed to a different org. The typical path is building in a sandbox or Developer Edition org and promoting the result to production, or packaging an app for AppExchange.[^s1] The Winter '27 documentation corresponds to API version 68.0.[^s1][^s4]

## How it works

The API offers two families of operations. **File-based calls**, `deploy()` and `retrieve()`, move a .zip archive containing a `package.xml` manifest and folders of component files.[^s1][^s3] **CRUD-based calls** (`createMetadata()`, `readMetadata()`, `updateMetadata()`, `upsertMetadata()`, `deleteMetadata()` and `renameMetadata()`) act on individual components synchronously, much like the synchronous calls of the enterprise WSDL. The older asynchronous `create()`, `update()` and `delete()` calls were removed in API version 31.0.[^s4] XML values use the English (United States) locale, so dates and numbers stay consistent between orgs set to different languages.[^s1]

The manifest lists components by metadata type. Each `types` block names a type, such as `PermissionSet`, and its `members` by API name, and a `version` element pins the API version.[^s5] In day-to-day work most teams call the API through the Salesforce CLI. For example, `sf project deploy start -x ./package.xml -o <org>` deploys only what the manifest names, and `sf project retrieve start` pulls changes back into a local project.[^s5]

Deployments are asynchronous. In the REST form, a POST to `/services/data/vXX.0/metadata/deployRequest` with a multipart body (JSON `deployOptions` plus the .zip) returns HTTP 201 with a deployment id and a `Pending` status. The caller then polls for progress, which runs through statuses such as `InProgress`, `Succeeded`, `SucceededPartial` and `Failed`.[^s3]

## Deploy options that matter

- **`checkOnly`**: validates the deployment and runs tests without saving anything. A successful validation can later be deployed without rerunning tests.[^s3]
- **`testLevel`**: `NoTestRun`, `RunSpecifiedTests`, `RunRelevantTests` (beta), `RunLocalTests` or `RunAllTestsInOrg`. `RunLocalTests`, which skips tests from installed managed and unlocked packages, is the default for production deployments that contain Apex.[^s3]
- **`rollbackOnError`**: defaults to `false` in the options object but must be `true` for production, so a single failure rolls back the whole deployment.[^s3]
- **`runTests`**: the test class names to use with `RunSpecifiedTests`. In that mode each class and trigger needs at least 75% coverage individually, not only on aggregate.[^s3]
- `allowMissingFiles` and `ignoreWarnings` should not be used against production, and `purgeOnDelete` only works in Developer Edition and sandbox orgs.[^s3]

## Limits and gotchas

Limits as published for Winter '27 (Salesforce notes they can change without notice):[^s2]

- Up to 10,000 files per deploy or retrieve. Inbound and outbound change sets have the same 10,000-file cap.[^s2]
- A maximum of 39 MB for the compressed .zip and 600 MB for the uncompressed folder. Base-64 encoding inflates the payload toward the 50 MB SOAP message limit, which is why the compressed size is capped lower.[^s2]
- Retrieves using `rootTypesWithDependencies` are limited to 25 requests per day and 100 components per request.[^s2]
- A single deployment can contain at most 45,000 custom fields, counted from both the CustomObject and CustomField sections of the manifest. A retrieve can return more than that, but you then need several deployments to put it back.[^s1]
- A big object can be retrieved only if its index is defined.[^s2]
- Some Data Cloud setup objects, including data stream definitions and data lake objects, must not be moved with file-based deployment. Doing so leaves orphaned records that block later deployments.[^s1]
- Apex tests in a deployment run synchronously and one after another, so large test suites lengthen every production release.[^s3][^s5]

## When to use it (and when not)

Use the Metadata API, usually through the CLI or a CI pipeline, for repeatable, source-controlled promotion of configuration between orgs. Manifest-driven deploys suit quick, targeted changes. For moving whole apps or large swaths of an org, Trailhead points teams toward package development instead.[^s5] Use the synchronous CRUD calls for small programmatic changes, such as a setup tool that creates one field, where shipping a .zip would be overkill.[^s4]

## Connections

The Metadata API sits **under** `kt:application-lifecycle-management`: it is the transport that moves changes between environments, and sandbox-to-production promotion is its core use case.[^s1] It is **accessed with** `kt:salesforce-cli`, whose `sf project deploy` and `sf project retrieve` commands wrap it, and it **has part** `kt:package-xml-manifest`, the file that scopes each deploy or retrieve.[^s5] It **depends on** `kt:apex-testing`, because production deployments that contain Apex must pass tests at the chosen test level.[^s3] It is **related** to `kt:change-sets`, which share its file limits, and to `kt:connected-apps`, whose article in this graph lists the Metadata API as its configuration route.[^s2]

## Sources

[^s1]: Salesforce Developers, "Deploying and Retrieving Metadata". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/file_based.htm (accessed 2026-10-31)
[^s2]: Salesforce Developers, "Salesforce Developer Limits and Allocations Quick Reference: Platform Metadata". https://developer.salesforce.com/docs/platform/salesforce-app-limits-cheatsheet/guide/salesforce-app-limits-platform-metadata.html (accessed 2026-10-31)
[^s3]: Salesforce Developers, "Deploy Metadata with Apex Testing Using REST". https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_rest_deploy.htm (accessed 2026-10-31)
[^s4]: Salesforce Developers, "CRUD-Based Calls". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_crud_based_calls_intro.htm (accessed 2026-10-31)
[^s5]: Trailhead, "Deploy Metadata Using the Manifest". https://trailhead.salesforce.com/content/learn/modules/package-xml/package-xml-deploy (accessed 2026-10-31)
