---
id: kt:data-cloud-activation
type: Feature
title: Data 360 Activation
aliases: [Data Cloud activation, Data 360 activations, activation targets, segment activation, CdpActivation]
domain: data-cloud-and-ai
summary: >-
  The Data 360 (formerly Data Cloud) process that sends a published segment, with chosen contact points and
  attributes, to an activation target such as Marketing Cloud, an ad platform, cloud storage or Data 360 itself, so
  the audience can be used outside the segment definition.
release: "Winter '27"
status: current
broader: [kt:data-cloud]
related: [kt:identity-resolution, kt:data-spaces, kt:agentexchange, kt:zero-copy-data-sharing]
relations:
  - {predicate: dependsOn, object: kt:data-cloud-segmentation}
  - {predicate: integratesWith, object: kt:marketing-cloud-engagement}
  - {predicate: contrastsWith, object: kt:data-actions}
  - {predicate: queriedWith, object: kt:connect-api}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: governedBy, object: kt:data-cloud-limits}
sources:
  - id: s1
    title: "Create and Activate a Segment in Data Cloud (Quick Start)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/quick-start-create-a-data-cloud-segment/create-and-activate-a-segment-in-data-cloud
    type: official-learning
    accessed: 2026-11-16
  - id: s2
    title: "Get to Know the Data 360 Activation Toolkit"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-360-activation-toolkit-for-independent-software-vendors/get-to-know-the-data-360-activation-toolkit
    type: official-learning
    accessed: 2026-11-16
  - id: s3
    title: "Meta Activation Connector (Data 360 Integration Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-metaadaudiences-connector.html
    type: official-docs
    accessed: 2026-11-16
  - id: s4
    title: "CdpActivation Class (Apex Reference Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexcode/apex_ConnectAPI_CdpActivation_static_methods.htm
    type: official-docs
    accessed: 2026-11-16
  - id: s5
    title: "ActivationPlatform (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_activationplatform.htm
    type: official-docs
    accessed: 2026-11-16
  - id: s6
    title: "Data 360 Integration Patterns and Practices"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/fundamentals/guide/data360_integration_patterns_and_practices
    type: official-docs
    accessed: 2026-11-16
created: 2026-11-16
---

# Data 360 Activation

**Activation** is the outbound step of Data 360 (formerly Data Cloud): it moves an audience segment to an
**activation target**, which publishes that audience to the platform where it will actually be used, such as an
email tool or an ad network.[^s1] A segment on its own is only a definition; activation is what turns it into
something a campaign, an ad audience or a downstream system can consume.[^s2]

## How it works

Two objects are involved. An **activation target** holds the connection, authentication and authorization details
for one destination platform, and is created in the Activation Targets tab.[^s1] Supported targets include Marketing
Cloud, B2C Commerce, Amazon Ads and Google Audience Insights, and a **Data 360 target** writes segment results back into Data 360 when
there is no external system to send them to.[^s1][^s3] An **activation** then ties one segment to one target. In the
Activations tab the admin picks the segment, the target and the activation membership (for example Unified
Individual), selects the contact point to send (such as Email), and adds attributes.[^s1]

Attributes come in two kinds. **Direct attributes** hold a single value per member, like a first name or postal
code, while **related attributes** can carry several values for the same member.[^s1] Only the attributes placed on
the activation travel to the target, so the payload is shaped per destination rather than exporting whole
profiles.[^s1] When a segment is activated to a Data 360 target, the records land in an audience data model object
that can be inspected in Data Explorer or read through the Query API.[^s1]

Each activation has a refresh type. The quick-start defaults to **incremental refresh**, which sends only new and
changed members after the first load.[^s1] Ad connectors also offer a **full refresh** that reloads every record;
for Meta, running one periodically keeps an audience from expiring under the platform's retention rules.[^s3]

## Connectors and the ISV toolkit

Ad-platform targets are Data Out connectors. The Meta connector, for example, needs the Ad Audiences add-on license,
hashes identifiers such as email and phone with SHA-256 before sending, and matches on email as the required
key.[^s3] Meta will not use an audience for targeting until it has at least 100 matched users, and audiences left
unused in live ads for over two years are flagged and deleted 90 days later.[^s3]

For destinations without a native connector, the **Data 360 Activation Toolkit** lets an ISV describe its platform
as packaged metadata (connection steps, target schema, frequency, data thresholds and file specs) and distribute it
through AgentExchange, so subscribers install it and start activating without a custom integration.[^s2] That
configuration is the `ActivationPlatform` Metadata API type, which defines the platform type, the output format
(CSV, JSON or Parquet), grouping, refresh mode (full or incremental) and an S3 data connector.[^s5]

## Automating activations in code

Apex can manage activations through `ConnectApi.CdpActivation`, available since API version 60.0, with methods to
list, page through, create, read, update and delete them.[^s4] Paginated reads accept a batch size from 1 to 200
(default 20) and can filter by segment, target, refresh type or status.[^s4] The reference warns that deleting an
activation stops Data 360 from sending data to every downstream system tied to it, so check the target first.[^s4]

## Limits and gotchas

- Activation is a scheduled batch push, not an event stream; latency is acceptable only for campaign-style use.[^s6]
- Target platforms add their own rules, such as Meta's audience minimum, hashing and consent requirements.[^s3]
- Deleting an activation silently cuts off its consumers; look up the linked target before you remove it.[^s4]

## When to use it (and when not)

Salesforce's integration guidance puts batch activation alongside three other outbound options: on-demand API
access (Connect API or Data Graph API), real-time data actions, and zero-copy sharing.[^s6] Use activation when a
curated audience must reach a marketing or advertising platform or be exported to cloud storage on a schedule.[^s6]
Choose data actions when a single record change must trigger work immediately, APIs when an app needs a profile
on request, and zero copy when an external platform such as Databricks should read data in place.[^s6]

## Connections

Activation sits under `kt:data-cloud` and **depends on** `kt:data-cloud-segmentation`, since every activation sends
a published segment; membership is usually the unified profile produced by `kt:identity-resolution`, scoped to a
`kt:data-spaces` data space.[^s1] It **integrates with** `kt:marketing-cloud-engagement` and ad platforms, and
**contrasts with** the event-driven `kt:data-actions`.[^s1][^s6] It is **queried with** `kt:connect-api` through
`ConnectApi.CdpActivation`, **configured via** `kt:metadata-api` through `ActivationPlatform`, and is **governed by**
`kt:data-cloud-limits`.[^s4][^s5] ISV destinations ship through `kt:agentexchange`, and
`kt:zero-copy-data-sharing` is the no-movement alternative for warehouses and lakehouses.[^s2][^s6]

## Sources
[^s1]: Trailhead, "Create and Activate a Segment in Data Cloud (Quick Start)". https://trailhead.salesforce.com/content/learn/projects/quick-start-create-a-data-cloud-segment/create-and-activate-a-segment-in-data-cloud (accessed 2026-11-16)
[^s2]: Trailhead, "Get to Know the Data 360 Activation Toolkit". https://trailhead.salesforce.com/content/learn/modules/data-360-activation-toolkit-for-independent-software-vendors/get-to-know-the-data-360-activation-toolkit (accessed 2026-11-16)
[^s3]: Salesforce Developers, "Meta Activation Connector (Data 360 Integration Guide)". https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-metaadaudiences-connector.html (accessed 2026-11-16)
[^s4]: Salesforce Developers, "CdpActivation Class (Apex Reference Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexcode/apex_ConnectAPI_CdpActivation_static_methods.htm (accessed 2026-11-16)
[^s5]: Salesforce Developers, "ActivationPlatform (Metadata API Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_activationplatform.htm (accessed 2026-11-16)
[^s6]: Salesforce Architects, "Data 360 Integration Patterns and Practices". https://architect.salesforce.com/docs/architect/fundamentals/guide/data360_integration_patterns_and_practices (accessed 2026-11-16)
