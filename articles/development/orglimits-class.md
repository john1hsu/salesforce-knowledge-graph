---
id: kt:orglimits-class
type: Feature
title: OrgLimits Class
aliases: [System.OrgLimits, OrgLimit class, System.OrgLimit, Apex org limits]
domain: development
summary: >-
  The Apex System.OrgLimits class and its companion System.OrgLimit: static methods that return the org's
  Salesforce API and platform allocations (such as daily API requests or Bulk API batches) with current usage
  and maximum, so Apex code can check org-wide headroom without calling the REST limits resource.
release: "Winter '27"
status: current
broader: [kt:apex]
related: [kt:api-request-limits, kt:rest-api, kt:bulk-api-allocations, kt:platform-event-allocations, kt:event-monitoring, kt:scheduled-apex]
relations:
  - {predicate: contrastsWith, object: kt:limits-class}
  - {predicate: mitigates, object: kt:api-request-limits}
  - {predicate: alternativeTo, object: kt:rest-api-limits-resource}
sources:
  - id: s1
    title: "Apex Reference Guide: OrgLimits Class"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexcode/apex_class_System_OrgLimits.htm
    type: official-docs
    accessed: 2026-11-16
  - id: s2
    title: "Apex Reference Guide: OrgLimit Class"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexcode/apex_class_System_OrgLimit.htm
    type: official-docs
    accessed: 2026-11-16
  - id: s3
    title: "REST API Developer Guide: Limits"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_limits.htm
    type: official-docs
    accessed: 2026-11-16
  - id: s4
    title: "API Limits and Monitoring Your API Usage"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/11/api-limits-and-monitoring-your-api-usage
    type: official-blog
    accessed: 2026-11-16
created: 2026-11-16
---

# OrgLimits Class

`OrgLimits` is a class in the Apex `System` namespace that returns every org limit as a collection of `System.OrgLimit` objects. The Winter '27 reference (API 68.0) gives SOAP API requests, Bulk API requests and Streaming API limits as examples of what it covers.[^s1] Each `OrgLimit` carries a limit's name, its maximum and its current value, which makes the pair the in-Apex view of the same org-wide allocations that the REST API `limits` resource exposes.[^s2][^s3]

## How it works

`OrgLimits` has two static methods. `getAll()` returns a `List<System.OrgLimit>`, and `getMap()` returns a `Map<String, System.OrgLimit>` keyed by limit name, so code can fetch one limit such as `DailyApiRequests` directly.[^s1] On each `OrgLimit`, `getName()` returns the name, `getValue()` the current usage as an `Integer`, `getLimit()` the maximum as an `Integer`, and `toString()` a summary such as how many Bulk API batches were consumed out of how many allowed.[^s2]

The limit names match those of the REST `limits` resource, which groups them into areas such as API requests (`DailyApiRequests`), asynchronous Apex (`DailyAsyncApexExecutions`), Bulk API (`DailyBulkApiBatches`), platform events, scratch orgs, email and data and file storage.[^s3] Salesforce states that the values are refreshed asynchronously in near real time rather than at the instant you read them.[^s1][^s2]

## Limits and gotchas

- `getValue()` reports usage consumed, while the REST resource reports `Remaining`; compute headroom as `getLimit() - getValue()`.[^s2][^s3]
- Values lag actual consumption: the REST guide says its figures are accurate within five minutes, so treat them as estimates.[^s1][^s3]
- Avoid rapid or concurrent polling for the same reason; the REST guide recommends against it to get consistent values.[^s3]
- Some names changed over versions: `DailyBulkApiBatches` was `DailyBulkApiRequests` in API 48.0 and earlier, so check names in a map before relying on them.[^s3]
- The daily API request limit it reports is soft: Salesforce lets an org exceed it until a protection limit blocks calls with HTTP 403 `REQUEST_LIMIT_EXCEEDED`.[^s4]

## When to use it (and when not)

Use `OrgLimits` when Apex itself must decide whether to proceed, for example a scheduled job that checks `DailyApiRequests` or `DailyAsyncApexExecutions` before enqueueing more work, or an admin utility that logs org consumption without an authenticated callout to the org's own REST endpoint.[^s1][^s3] External monitoring tools are better served by the REST `limits` resource, which needs the View Setup and Configuration permission, or by the `Sforce-Limit-Info` response header, which reports API usage on each REST call.[^s3][^s4] To find which integration is consuming requests, rather than how many remain, use Event Monitoring's API Total Usage logs and API usage notifications.[^s4]

Do not use it for per-transaction governors such as SOQL queries, CPU time or heap: both reference pages state that it returns Salesforce API limits, and that the `Limits` class covers Apex governor limits instead.[^s1][^s2]

## Connections

**Apex** is the parent: `OrgLimits` and `OrgLimit` are built-in system classes.[^s1] The class `contrastsWith` the **Limits class**, which reports the running transaction's governors, while this one reports org-wide allocations.[^s2] It `mitigates` **API request limits** by letting code back off before the daily allocation runs out; the same data also covers **Bulk API allocations**, **platform event allocations** and asynchronous Apex executions.[^s3][^s4] It is an `alternativeTo` the **REST API limits resource**, which returns identically named limits to external callers.[^s1][^s3] **Event Monitoring** complements it with per-client attribution,[^s4] and **Scheduled Apex** is a natural host for periodic checks.

## Sources
[^s1]: Salesforce Developers, "Apex Reference Guide: OrgLimits Class" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexcode/apex_class_System_OrgLimits.htm (accessed 2026-11-16)
[^s2]: Salesforce Developers, "Apex Reference Guide: OrgLimit Class" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexcode/apex_class_System_OrgLimit.htm (accessed 2026-11-16)
[^s3]: Salesforce Developers, "REST API Developer Guide: Limits". https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_limits.htm (accessed 2026-11-16)
[^s4]: Jeremy Westerman, "API Limits and Monitoring Your API Usage", Salesforce Developers Blog, 2024-11-19. https://developer.salesforce.com/blogs/2024/11/api-limits-and-monitoring-your-api-usage (accessed 2026-11-16)
