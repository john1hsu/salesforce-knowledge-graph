---
id: kt:api-version-lifecycle
type: Concept
title: API Version Lifecycle
aliases: [API end-of-life policy, API version retirement, legacy API version retirement, Salesforce API versioning, API EOL policy]
domain: platform-architecture
summary: >-
  How Salesforce numbers, supports, deprecates and retires versions of its Platform APIs and versioned code: every
  release adds a new API version, each version is supported for at least three years, and retired versions are
  rejected with version errors.
release: "Winter '27"
status: concept
broader: [kt:salesforce-apis, kt:salesforce-seasonal-releases]
related: [kt:rest-api, kt:soap-api, kt:metadata-api, kt:release-updates, kt:apex-user-mode]
relations:
  - {predicate: dependsOn, object: kt:salesforce-seasonal-releases}
  - {predicate: consumedBy, object: kt:apex}
  - {predicate: mitigates, object: kt:technical-debt-in-salesforce}
  - {predicate: configuredVia, object: kt:event-monitoring}
sources:
  - id: s1
    title: "API End-of-Life Policy (REST API Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/api_rest_eol.htm
    type: official-docs
    accessed: 2026-11-22
  - id: s2
    title: "API End-of-Life Policy (Metadata API Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_api_eol.htm
    type: official-docs
    accessed: 2026-11-22
  - id: s3
    title: "New Tools to Help Prepare for API Version Retirement"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/10/new-tools-to-help-prepare-for-api-version-retirement
    type: official-blog
    accessed: 2026-11-22
  - id: s4
    title: "Apex Versioned Behavior Changes (Apex Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/versioned_behavior_changes.htm
    type: official-docs
    accessed: 2026-11-22
created: 2026-11-22
---

# API Version Lifecycle

Salesforce versions its Platform APIs (REST, SOAP, Bulk, Metadata and others) with a numbered API version that advances with each seasonal release, and publishes an end-of-life (EOL) policy that governs how long each version keeps working. The policy commits Salesforce to support every API version for at least three years after it first ships, and to notify customers who use a version at least one year before support for it ends.[^s1][^s2] The same version number also pins the behavior of saved code: an Apex class or trigger runs with the semantics of the API version it was saved against, so the lifecycle reaches beyond integrations into the org's own codebase.[^s4]

## How it works

A version passes through three states in the policy tables. **Supported** versions work normally. **Deprecated** versions still answer calls but are flagged as unsupported, with a published retirement date. **Retired** versions are switched off, and requests that name them are refused.[^s1][^s2] As verified for Winter '27, the Metadata API guide lists 41.0 through 68.0 as supported; 31.0 through 40.0 as deprecated and unsupported from Summer '27, with retirement scheduled for Summer '28; 21.0 through 30.0 as retired since Summer '25; and 7.0 through 20.0 as retired since Summer '22.[^s2] The REST API guide carries the same deprecation and retirement schedule, though its supported range was listed only up to 67.0 when checked.[^s1]

Calls to a retired version fail with version-specific errors rather than silently falling back. REST returns HTTP 410 GONE and SOAP returns 500 UNSUPPORTED_API_VERSION;[^s2] Salesforce's retirement guidance adds that Bulk API returns 400 InvalidVersion.[^s3]

## Finding and fixing legacy calls

Ahead of the Summer '25 retirement of versions 21.0 through 30.0, Salesforce shipped two aids that remain the standard playbook for any retirement wave.[^s3]

- **API Total Usage event log files**: free logs covering SOAP, REST and Bulk API requests, viewable in the Event Log Browser under Event Monitoring setup. Without an Event Monitoring license you get daily files covering the last 24 hours; with it, hourly and daily files for 30 days.[^s3]
- **Retirement enforcement test run**: a Release Update that, once you enable its test run, makes the org reject retired versions early so integrations break in a controlled window instead of on release weekend.[^s3]

The log fields that matter most are the connected app ID, the optional client name, the user ID and the client IP, which together identify which integration is still pinned to an old endpoint.[^s3] Salesforce therefore recommends routing each integration through its own connected app, sending a client name in the call-options header, and giving each app a dedicated integration user, so legacy traffic can be traced to an owner.[^s3]

## Versioned code behavior

Apex is versioned too: when Salesforce changes language semantics, classes saved at older API versions keep the original behavior, and only code saved at the new version picks up the change.[^s4] Recent examples include version 67.0 running Apex in user mode by default (66.0 and earlier default to system mode) and dropping support for WITH SECURITY_ENFORCED in SOQL in favor of WITH USER_MODE.[^s4] Older examples include 61.0 stopping subclass methods from overriding private methods, and 54.0 throwing a StringException when an invalid ID string is assigned.[^s4] Salesforce strongly recommends saving code at the latest available API version, while noting that its list of versioned changes is not exhaustive.[^s4]

## Gotchas

Bumping a class's API version is a behavior change, not a cosmetic edit: moving a class to 67.0 or later can change which records and fields it sees because of the new user-mode default, so version bumps need regression tests.[^s4] Conversely, leaving integrations on old endpoints accumulates risk, because each retirement wave (31.0 through 40.0 is next) turns those calls into hard failures on a fixed release date.[^s1][^s3]

## Connections

The lifecycle is a facet of the **Salesforce APIs** and is paced by **seasonal releases**, since each release mints a new version and the deprecation and retirement milestones are expressed as release names.[^s1][^s2] It applies to **REST API**, **SOAP API** and **Metadata API** alike, with the errors described above.[^s2][^s3] Enforcement is previewed through **release updates**, and legacy traffic is found with the API Total Usage logs of **Event Monitoring**.[^s3] For code, the version setting determines **Apex** semantics such as the **Apex user mode** default introduced at 67.0.[^s4] Keeping versions current is one way to limit **technical debt**.[^s3]

## Sources
[^s1]: Salesforce, "API End-of-Life Policy (REST API Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/api_rest_eol.htm (accessed 2026-11-22)
[^s2]: Salesforce, "API End-of-Life Policy (Metadata API Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_api_eol.htm (accessed 2026-11-22)
[^s3]: Salesforce Developers Blog, "New Tools to Help Prepare for API Version Retirement". https://developer.salesforce.com/blogs/2024/10/new-tools-to-help-prepare-for-api-version-retirement (accessed 2026-11-22)
[^s4]: Salesforce, "Apex Versioned Behavior Changes (Apex Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/versioned_behavior_changes.htm (accessed 2026-11-22)
