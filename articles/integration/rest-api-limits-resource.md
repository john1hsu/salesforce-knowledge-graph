---
id: kt:rest-api-limits-resource
type: Feature
title: REST API Limits Resource
aliases: [Limits resource, /limits resource, List Org Limits, REST limits endpoint]
domain: integration
summary: >-
  The Salesforce REST API resource at /services/data/vXX.X/limits/ that returns, for each org-wide allocation
  (daily API requests, Bulk API batches, async Apex executions, platform-event deliveries, storage and more),
  its maximum and remaining value, so integrations and monitoring tools can check headroom before they act.
release: "Winter '27"
status: current
broader: [kt:rest-api]
related: [kt:api-request-limits, kt:platform-event-allocations, kt:event-monitoring]
relations:
  - {predicate: alternativeTo, object: kt:orglimits-class}
  - {predicate: consumedBy, object: kt:salesforce-cli}
  - {predicate: contrastsWith, object: kt:limits-class}
sources:
  - id: s1
    title: "REST API Developer Guide: Limits"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_limits.htm
    type: official-docs
    accessed: 2026-11-21
  - id: s2
    title: "REST API Developer Guide: Record Count"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-rest/guide/resources-record-count.html
    type: official-docs
    accessed: 2026-11-21
  - id: s3
    title: "REST API Developer Guide: Limit Info Header"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-rest/guide/headers-api-usage.html
    type: official-docs
    accessed: 2026-11-21
  - id: s4
    title: "Salesforce CLI Command Reference: org list limits"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_org_list_limits.html
    type: official-docs
    accessed: 2026-11-21
  - id: s5
    title: "API Limits and Monitoring Your API Usage"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/11/api-limits-and-monitoring-your-api-usage
    type: official-blog
    accessed: 2026-11-21
created: 2026-11-21
---

# REST API Limits Resource

The Limits resource is a read-only REST endpoint, `GET /services/data/vXX.X/limits/`, that lists the org's platform allocations and, for each one, the maximum allowed and the amount still remaining. It returns JSON or XML, takes a standard OAuth bearer token, and has been available since REST API version 29.0 to users who hold the View Setup and Configuration permission.[^s1] It is the main programmatic way for an external system to ask "how much budget does this org have left?" rather than discovering the answer through a failed call.[^s1][^s5]

## What it returns

Each entry in the response is keyed by a limit name and carries `Max` and `Remaining` values; Salesforce's API blog shows `DailyApiRequests` returned in exactly that shape.[^s5] The documented names span far more than API calls. Grouped roughly as the reference page groups them:[^s1]

- **API and async:** `DailyApiRequests`, `DailyBulkApiBatches`, `DailyBulkV2QueryJobs`, `DailyBulkV2QueryFileStorageMB`, `DailyAsyncApexExecutions`, `DailyAsyncApexTests`.[^s1]
- **Events and streaming:** `HourlyPublishedPlatformEvents`, `DailyDeliveredPlatformEvents`, `MonthlyPlatformEventsUsageEntitlement`, and the durable streaming event and client counts.[^s1]
- **Org and developer experience:** `DataStorageMB`, `FileStorageMB`, `SingleEmail`, `MassEmail`, `ActiveScratchOrgs`, `DailyScratchOrgs`, `Package2VersionCreates`, `PermissionSets`.[^s1]
- **Analytics, Flow and connectors:** report and dashboard run counts, `ScheduledFlowRunLimit`, `HourlyODataCallout` for Salesforce Connect, and External Services registration counts.[^s1]

Many names are version-gated. For example, `DailyBulkApiBatches` replaced `DailyBulkApiRequests` from version 49.0, `MonthlyPlatformEventsUsageEntitlement` replaced `MonthlyPlatformEvents` from version 48.0, and `DailyMetadataRetrievesWithDependencies` appears only from version 64.0, so the version segment in the URI changes which keys come back.[^s1] Some keys also depend on what the org has: the storage keys additionally require the Manage Users permission, and platform-event values differ for orgs with an event add-on license.[^s1]

A sibling resource, `/limits/recordCount`, returns approximate record counts per object (optionally filtered with an `sObjects` list) from REST API 40.0 onward.[^s2] Its counts are a cached snapshot refreshed on no fixed schedule and exclude recycle-bin and archived records, so Salesforce points to a SOQL `count()` query when an exact figure is needed.[^s2]

## Limits and gotchas

- **Not real time.** Salesforce states the tabulated values are accurate within five minutes of consumption and advises against concurrent or rapid requests if you want consistent results.[^s1]
- **No per-client breakdown.** The resource reports org totals only; attributing usage to a connected app or external client app requires the API Total Usage event log or Event Monitoring fields such as `CONNECTED_APP_ID`.[^s5]
- **Cheaper signal on every call.** Each REST response already carries an `Sforce-Limit-Info` header of the form `api-usage=<used>/<limit>`, so a client that only cares about daily API calls can read the header instead of polling the resource.[^s3]
- **Soft daily cap.** The blog describes the daily API request allocation as a soft limit, with hard system-protection blocks returning HTTP 403 `REQUEST_LIMIT_EXCEEDED`; the resource shows how close an org is, not which ceiling will stop it.[^s5]

## When to use it

Use the Limits resource in integration middleware that schedules bulk loads or event replays, in monitoring dashboards, and in pre-flight checks that throttle work when `Remaining` drops below a threshold.[^s1][^s5] Developers can call it without writing HTTP code through `sf org list limits` (formerly `force:limits:api:display`), which prints each limit's maximum and remaining allocation for a target org and supports `--json` output.[^s4]

## Connections

The resource is part of the **REST API** and is the canonical read-out for **API request limits**, alongside the header and Setup pages that report the same daily counter.[^s1][^s3][^s5] It also exposes **platform event allocations**, which makes it a monitoring point for event-driven integrations.[^s1] **Event Monitoring** complements it with per-caller attribution it cannot provide.[^s5] In the graph it is paired with the Apex **OrgLimits class** as the in-Apex alternative and contrasted with the Apex **Limits class**, which tracks per-transaction governor limits rather than org allocations; the **Salesforce CLI** consumes the same data through `sf org list limits`.[^s4]

## Sources

[^s1]: Salesforce Developers, "Limits | REST API Developer Guide". https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_limits.htm (accessed 2026-11-21)
[^s2]: Salesforce Developers, "Record Count | REST API Developer Guide". https://developer.salesforce.com/docs/platform/api-rest/guide/resources-record-count.html (accessed 2026-11-21)
[^s3]: Salesforce Developers, "Limit Info Header | REST API Developer Guide". https://developer.salesforce.com/docs/platform/api-rest/guide/headers-api-usage.html (accessed 2026-11-21)
[^s4]: Salesforce Developers, "org list limits | Salesforce CLI Command Reference". https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_org_list_limits.html (accessed 2026-11-21)
[^s5]: Jeremy Westerman, "API Limits and Monitoring Your API Usage", Salesforce Developers Blog, 2024-11-19. https://developer.salesforce.com/blogs/2024/11/api-limits-and-monitoring-your-api-usage (accessed 2026-11-21)
