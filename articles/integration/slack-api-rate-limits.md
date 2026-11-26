---
id: kt:slack-api-rate-limits
type: Limit
title: Slack API Rate Limits
aliases: [Slack rate limits, Slack Web API rate limit tiers, Slack Events API delivery limit, app_rate_limited]
domain: integration
summary: >-
  The per-minute, per-method, per-workspace, per-app caps that Slack places on Web API calls (Tiers 1-4 plus
  special limits such as one posted message per second per channel), together with the hourly Events API delivery
  limit and the workflow trigger limits that constrain integrations between Salesforce and Slack.
release: "Winter '27"
status: current
broader: [kt:slack-platform]
related: [kt:block-kit, kt:slack-workflow-builder, kt:event-driven-architecture]
relations:
  - {predicate: contrastsWith, object: kt:api-request-limits}
sources:
  - id: s1
    title: "Rate limits"
    publisher: Slack (Salesforce)
    url: https://docs.slack.dev/apis/web-api/rate-limits
    type: official-docs
    accessed: 2026-11-26
  - id: s2
    title: "Rate limit changes for non-Marketplace apps"
    publisher: Slack (Salesforce)
    url: https://docs.slack.dev/changelog/2025/05/29/rate-limit-changes-for-non-marketplace-apps
    type: official-docs
    accessed: 2026-11-26
  - id: s3
    title: "Explore the Bolt Development Framework"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/slack-app-development-with-bolt/explore-the-bolt-development-framework
    type: official-learning
    accessed: 2026-11-26
  - id: s4
    title: "Considerations and Limitations (Apex SDK for Slack, Beta)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/known_issues.html
    type: official-docs
    accessed: 2026-11-26
created: 2026-11-26
---

# Slack API Rate Limits

**Slack API rate limits** are the throttles Slack applies to apps that call its APIs. Unlike Salesforce's org-wide daily API allocation, they are counted per API method, per workspace, per app, in windows of one minute, and every Slack plan gets the same limit for a given method.[^s1] Any integration that pushes Salesforce data into Slack or reads Slack conversations back has to be designed around them.

## How it works

Each Web API method is assigned to one tier, shown in the "Facts" section of the method's reference page.[^s1] The tiers are:

- **Tier 1**: 1+ requests per minute, for methods meant to be called rarely, with a little burst tolerated.[^s1]
- **Tier 2**: 20+ per minute (for example `conversations.list`); **Tier 3**: 50+ per minute, typical of paginated collections.[^s1]
- **Tier 4**: 100+ per minute with generous bursts; **Special** methods have their own documented rules.[^s1]

Slack does not publish exact burst limits; its guidance is to design for about one request per second per method and treat brief overshoots as tolerated, not guaranteed.[^s1] Cursor-paginated methods only get their published tier when the caller actually paginates; unpaginated calls face stricter limits.[^s1]

When a limit is exceeded on any HTTP-based API, including incoming webhooks, Slack answers **HTTP 429 Too Many Requests** with a `Retry-After` header giving the seconds to wait. The block applies only to that method for that workspace and token; other methods, and the same method in other workspaces, keep working.[^s1] Bolt's built-in Web API client includes rate limit handling and retry logic, which is one reason Trailhead steers custom app builders to it.[^s3]

## Specific limits worth knowing

Posting is a special case: an app may post no more than one message per second per channel, whether through `chat.postMessage`, an incoming webhook or another method, and `chat.postMessage` also carries a workspace-wide cap. Short bursts pass, but sustained excess is throttled.[^s1] The Events API delivers at most 30,000 events per workspace per app per 60 minutes; when a workspace goes over, Slack sends an `app_rate_limited` event carrying the team ID and the minute limiting began.[^s1] Profile writes through `users.profile.set` are capped at 10 updates per user per minute and 30 profiles per token per minute.[^s1]

Workflow automation has its own ceilings: 10,000 event triggers per hour and 10 webhook triggers per minute, plus per-team and per-workflow limits on the AI summary and AI Generate steps.[^s1]

## What changed in 2025

On May 29, 2025 Slack moved `conversations.history` and `conversations.replies` from Tier 3 to Tier 1 for commercially distributed apps not approved for the Slack Marketplace: one request per minute, with the maximum and default page size cut to 15 objects. The change applied at once to new unlisted apps and new installations; existing installations were not affected.[^s2] Marketplace apps and internal customer-built apps kept the higher limits, which the changelog gives as 50+ requests per minute and up to 1,000 objects per page. Slack suggested the Events API instead of polling channel history.[^s2]

## Limits and gotchas

- A record-triggered flow or trigger that posts one Slack message per record change can exceed one message per second per channel during a data load.[^s1]
- Retries must honour `Retry-After` per method and workspace; a single global backoff wastes capacity and a blind retry loop prolongs the block.[^s1]
- The Apex SDK for Slack is still in beta, and the SDK does not support some Web API families such as `admin.*` and `workflows.*`.[^s4]
- A partner app that reads channel history and is not Marketplace-listed may be held to 1 request per minute on new installs.[^s2]

## When to design for it

Batch or digest notifications instead of firing one message per event, route high-volume alerts to several channels, and subscribe to events rather than polling history.[^s1][^s2] When Salesforce is the caller, the Slack limits stack on top of the platform's own callout and transaction limits, so queue outbound posts asynchronously and let the queue absorb 429 responses.[^s1][^s3]

## Connections

This node is the `Limit` that `kt:slack-platform` is `governedBy`, and it sits under that product as its `broader` parent.[^s1] It `contrastsWith` `kt:api-request-limits`: Salesforce counts inbound calls per org per 24 hours, while Slack counts per method, per workspace, per app per minute.[^s1] Messages built with `kt:block-kit` and triggers in `kt:slack-workflow-builder` both consume these limits, and the Events API limit ties it to `kt:event-driven-architecture`, the recommended alternative to polling.[^s1][^s2][^s3]

## Sources
[^s1]: Slack (Salesforce), "Rate limits". https://docs.slack.dev/apis/web-api/rate-limits (accessed 2026-11-26)
[^s2]: Slack (Salesforce), "Rate limit changes for non-Marketplace apps" (2025-05-29). https://docs.slack.dev/changelog/2025/05/29/rate-limit-changes-for-non-marketplace-apps (accessed 2026-11-26)
[^s3]: Trailhead, "Explore the Bolt Development Framework". https://trailhead.salesforce.com/content/learn/modules/slack-app-development-with-bolt/explore-the-bolt-development-framework (accessed 2026-11-26)
[^s4]: Salesforce Developers, "Considerations and Limitations (Apex SDK for Slack, Beta)". https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/known_issues.html (accessed 2026-11-26)
