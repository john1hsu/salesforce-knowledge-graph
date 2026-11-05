---
id: kt:api-request-limits
type: Limit
title: API Request Limits
aliases: [API request allocations, daily API request limit, DailyApiRequests, total API request allocation, concurrent API request limit]
domain: integration
summary: >-
  The org-wide allocations that cap how many inbound Salesforce Platform API calls (REST, SOAP, Bulk and most
  Connect REST) an org can make per 24-hour period, plus the separate limits on concurrent long-running requests
  and API call timeouts.
release: "Winter '27"
status: current
broader: [kt:governor-limits]
related: [kt:rest-api, kt:bulk-api-2, kt:composite-api, kt:connected-apps, kt:multitenancy]
relations:
  - {predicate: contrastsWith, object: kt:platform-event-allocations}
  - {predicate: queriedWith, object: kt:rest-api}
  - {predicate: coveredBy, object: kt:integration-architect-certification}
sources:
  - id: s1
    title: "API Request Limits and Allocations (Salesforce Developer Limits and Allocations Quick Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-app-limits-cheatsheet/guide/salesforce-app-limits-platform-api.html
    type: official-docs
    accessed: 2026-11-05
  - id: s2
    title: "API Limits and Monitoring Your API Usage"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/11/api-limits-and-monitoring-your-api-usage
    type: official-blog
    accessed: 2026-11-05
  - id: s3
    title: "Learn About Daily Rate Limits (App Development Without Limits)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/app-development-without-limits/app-development-without-limits-rate
    type: official-learning
    accessed: 2026-11-05
created: 2026-11-05
---

# API Request Limits

API request limits are the allocations Salesforce applies to inbound calls against the Salesforce Platform SOAP and REST APIs and the APIs built on them. They are enforced on the aggregate of every call made to the org in a 24-hour period, not per user, so one noisy integration can exhaust capacity for every other client.[^s1] Salesforce explains these allocations as a consequence of its shared, multitenant infrastructure: they keep pooled resources predictable for every tenant.[^s3]

## How the allocation is calculated

For Enterprise, Professional (with API access), Unlimited and Performance editions, the daily total is 100,000 requests plus the number of licenses multiplied by a per-license-type amount, plus any purchased API call add-ons. Developer Edition orgs get a flat 15,000, and a Full sandbox not created from a template gets 5,000,000.[^s1] Per-license amounts differ by edition: a full Salesforce or Salesforce Platform license adds 1,000 calls in Enterprise and Professional but 5,000 in Unlimited and Performance, while Customer Community licenses add nothing and Customer Community Plus Login and Partner Community Login licenses add 10 each.[^s1] The Salesforce Developers Blog notes that extra capacity can be bought in daily increments.[^s2]

Usage is also aggregated into 30-day periods from the contract start date and shown as the "API Request Limit per Month" entitlement; that monthly figure is tracked rather than enforced.[^s1][^s2]

## What counts

Calls to the Lightning Platform REST API, SOAP API, Bulk API, Bulk API 2.0 and most Connect REST APIs count against the allocation, and so do calls from installed managed packages. Calls from certain Salesforce-owned connected apps, such as the Salesforce mobile app, do not. Requests sent with the DebuggingHeader have their own limit of 1,000 per 24 hours.[^s1]

## Soft limit, hard cap and concurrency

The daily limit is soft: in paid, active orgs Salesforce generally lets calls continue past it during spikes, but a hard cap protects the platform, and the grace does not apply to trials, Developer Edition orgs or sandboxes.[^s1] Once the protection limit is hit, calls fail with HTTP 403 and `REQUEST_LIMIT_EXCEEDED`, and they resume when usage over the preceding 24 hours falls back under the limit.[^s2]

A separate limit governs concurrent long-running requests, meaning inbound calls lasting 20 seconds or more: 25 in production orgs and sandboxes, 5 in Developer Edition and trial orgs. Shorter calls have no concurrency cap. REST and SOAP calls also time out after 10 minutes (queries follow SOQL limits), and for composite resources the timeout covers the whole composite request.[^s1]

## Monitoring

Admins can see 24-hour usage in Setup on the System Overview and Company Information pages, and set API Usage Notifications that email a user when usage crosses a percentage threshold.[^s1] Programmatically, every REST response carries an `Sforce-Limit-Info` header, SOAP responses include limit info in the body, and the REST `/limits` resource returns `DailyApiRequests` with `Max` and `Remaining` values.[^s1][^s2] Every org can download the daily API Total Usage event log; orgs with Event Monitoring get per-API event types with fields such as connected app ID and client name to identify the caller.[^s2]

## Gotchas and practices

- Don't design normal workloads around the overage grace; it is meant for occasional spikes.[^s1][^s2]
- Give each integration its own user and its own connected app or external client app, and set a client name in the `Sforce-Call-Options` header so usage can be attributed.[^s2]
- Remove the API Enabled permission from profiles that don't need it, and have clients poll the limits resource before bursts of calls.[^s3]
- Batch work: composite resources cut round trips, and the Bulk APIs suit large volumes.[^s1]

## Connections

API request limits are a narrower case of **governor limits**, the family of caps that exist because of **multitenancy**.[^s3] They apply to **REST API** and **Bulk API 2.0** traffic and can be read through the REST `/limits` resource.[^s1] The **Composite API** mitigates them by bundling subrequests into one call.[^s1] Clients authenticate through **connected apps**, which is how usage is attributed.[^s2] They contrast with **platform event allocations**, which Trailhead describes as a rolling allocation where excess events are queued rather than rejected.[^s3] Sizing integrations against these limits is core material for the **Integration Architect certification**.

## Sources
[^s1]: Salesforce Developers, "API Request Limits and Allocations" (Developer Limits and Allocations Quick Reference). https://developer.salesforce.com/docs/platform/salesforce-app-limits-cheatsheet/guide/salesforce-app-limits-platform-api.html (accessed 2026-11-05)
[^s2]: Jeremy Westerman, "API Limits and Monitoring Your API Usage", Salesforce Developers Blog, 2024-11-19. https://developer.salesforce.com/blogs/2024/11/api-limits-and-monitoring-your-api-usage (accessed 2026-11-05)
[^s3]: Trailhead, "Learn About Daily Rate Limits" (App Development Without Limits). https://trailhead.salesforce.com/content/learn/modules/app-development-without-limits/app-development-without-limits-rate (accessed 2026-11-05)
