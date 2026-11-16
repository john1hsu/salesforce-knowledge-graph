---
id: kt:data-actions
type: Feature
title: Data Actions
aliases: [data action, Data 360 data actions, Data Cloud data actions, data action targets]
domain: data-cloud-and-ai
summary: >-
  Event-driven Data 360 (formerly Data Cloud) automations that watch a data model object, streaming insight or
  calculated insight for record changes, test optional conditions, and send an enriched event in near real time to a
  data action target: a Salesforce platform event, a webhook, or Marketing Cloud Engagement.
release: "Winter '27"
status: current
broader: [kt:data-cloud]
related: [kt:calculated-insights, kt:event-driven-architecture]
relations:
  - {predicate: dependsOn, object: kt:data-model-objects}
  - {predicate: dependsOn, object: kt:data-spaces}
  - {predicate: integratesWith, object: kt:platform-events}
  - {predicate: integratesWith, object: kt:marketing-cloud-engagement}
  - {predicate: contrastsWith, object: kt:data-cloud-activation}
  - {predicate: alternativeTo, object: kt:data-cloud-triggered-flows}
  - {predicate: governedBy, object: kt:data-cloud-limits}
sources:
  - id: s1
    title: "Use Insights in Data Cloud"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/customer-data-platform-insights/use-insights-in-customer-data-platform
    type: official-learning
    accessed: 2026-11-16
  - id: s2
    title: "Unleashing the Power of Data Actions Using a Webhook as a Target"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/01/unleashing-the-power-of-data-actions-using-a-webhook-as-a-target
    type: official-blog
    accessed: 2026-11-16
  - id: s3
    title: "Webhook Data Action Targets in Data 360"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/data/data-cloud-int/references/webhook-data-action-targets
    type: official-docs
    accessed: 2026-11-16
  - id: s4
    title: "Data 360 Integration Patterns and Practices"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/fundamentals/guide/data360_integration_patterns_and_practices
    type: official-docs
    accessed: 2026-11-16
  - id: s5
    title: "Trigger Flows from Data Cloud"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-cloud-in-flows/trigger-flows-from-data-cloud
    type: official-learning
    accessed: 2026-11-16
  - id: s6
    title: "Learn How to Act on Data"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/cert-prep-data-cloud-consultant/learn-how-to-act-on-data
    type: official-learning
    accessed: 2026-11-16
created: 2026-11-16
---

# Data Actions

**Data actions** are Data 360's (formerly Data Cloud's) mechanism for near-real-time, event-driven automation. A
data action watches a source object for changes and, when its conditions are met, sends an event to a configured
**data action target** so another system can update records, notify someone, call an external service or start a
business process.[^s2] Trailhead frames them as the way to put streaming insight results to work: each data action
delivers its results to a target.[^s1]

## How it works

Change detection builds on change data capture over the Lakehouse change data feed, which reports created, updated
and deleted records.[^s2] Setting up a data action takes two pieces of configuration:

1. **A data action target**, created on the Data Action Targets tab. You name it and pick a type, then configure that type: the connected org for Salesforce CRM, a generated key for a webhook, or Email or Journey for Marketing Cloud Engagement.[^s1]
2. **The data action itself**, created on the Data Actions tab. You select the target, a data space and a primary object, add optional rules and enrichment, then name it and choose Save and Publish.[^s1][^s2]

The primary object can be a data model object (which covers streaming insights and engagement objects) or a
calculated insight object.[^s2] An **event rule** decides which record changes trigger the action, and an **action
rule** then tests conditions on object attributes, combined with AND and OR.[^s2] Trailhead's example sends only
events whose product category is camping.[^s1] Before sending, you can enrich the event with one related object and
up to 10 related attributes, such as profile data.[^s1][^s2] Trailhead says a new target starts receiving events in
under 15 minutes.[^s1]

## Targets

- **Salesforce CRM (platform event):** publishes to the core event bus, so flows or Apex subscribers can react to Data 360 signals.[^s1][^s2]
- **Webhook:** pushes to an external HTTP endpoint and is event-driven, not request-driven; Salesforce signs each payload.[^s3]
- **Marketing Cloud Engagement:** triggers an email send or a journey entry from eligible objects.[^s1]

A webhook payload uses the `DataObjectDataChgEvent` format: a creation timestamp, an event count, an array of
schemas, and an array of events.[^s3] Signatures use HMAC-SHA256 with a secret key you generate in Data 360. If no
key exists, the target gets no payload and the call is logged as "Signing Key Not Found."[^s3]

## Limits and gotchas

- Rotate the webhook secret key at least every 12 months; a new key can take up to 15 minutes to take effect.[^s3]
- Update the key on the receiving system right after regenerating it, or signature validation there fails.[^s3]
- The developer blog says action events are retained for four days and webhook replay wasn't yet available, so build durable consumers.[^s2]
- Creating data actions needs the feature enabled, data already ingested and mapped, and the Data Aware Specialist role.[^s2]
- Per-org counts and throughput are on the Data 360 limits page, which Trailhead links but doesn't restate.[^s1]

## When to use it (and when not)

Use a data action when a Data 360 signal must leave the platform, or reach the Salesforce event bus, within minutes.
Examples include alerting a webhook on a churn-risk threshold or entering a contact into a Marketing Cloud
journey.[^s1][^s4] For logic that stays inside Salesforce and starts from a data model object or calculated insight
change, a **Data Cloud-triggered flow** is simpler: you build it directly in Flow Builder with Start-element
conditions. Trailhead points to data actions when the trigger is another insight type, such as a streaming
insight.[^s5] Salesforce's architecture guidance keeps lightweight choreography in flows and sends complex,
stateful orchestration to middleware.[^s4] For scheduled, audience-sized exports to ad or messaging platforms, use
segmentation and activation instead.[^s4][^s6]

## Connections

Data actions are a feature of `kt:data-cloud`. They **depend on** `kt:data-model-objects` as primary sources and run
within `kt:data-spaces`.[^s2] They are fed by streaming insights and `kt:calculated-insights`.[^s1][^s2] They
**integrate with** `kt:platform-events` through the CRM target and with `kt:marketing-cloud-engagement` through its
target.[^s1] They follow `kt:event-driven-architecture`, which **contrasts with** batch `kt:data-cloud-activation`.
They are an **alternative to** `kt:data-cloud-triggered-flows` for in-org automation.[^s4][^s5] The Data 360
Consultant prep material treats data actions and activations as separate topics in its Act on Data section.[^s6]
They are **governed by** `kt:data-cloud-limits`.[^s1]

## Sources

[^s1]: Trailhead, "Use Insights in Data Cloud". https://trailhead.salesforce.com/content/learn/modules/customer-data-platform-insights/use-insights-in-customer-data-platform (accessed 2026-11-16)
[^s2]: Salesforce Developers Blog, "Unleashing the Power of Data Actions Using a Webhook as a Target". https://developer.salesforce.com/blogs/2024/01/unleashing-the-power-of-data-actions-using-a-webhook-as-a-target (accessed 2026-11-16)
[^s3]: Salesforce, "Webhook Data Action Targets in Data 360". https://developer.salesforce.com/docs/data/data-cloud-int/references/webhook-data-action-targets (accessed 2026-11-16)
[^s4]: Salesforce Architects, "Data 360 Integration Patterns and Practices". https://architect.salesforce.com/docs/architect/fundamentals/guide/data360_integration_patterns_and_practices (accessed 2026-11-16)
[^s5]: Trailhead, "Trigger Flows from Data Cloud". https://trailhead.salesforce.com/content/learn/modules/data-cloud-in-flows/trigger-flows-from-data-cloud (accessed 2026-11-16)
[^s6]: Trailhead, "Learn How to Act on Data". https://trailhead.salesforce.com/content/learn/modules/cert-prep-data-cloud-consultant/learn-how-to-act-on-data (accessed 2026-11-16)
