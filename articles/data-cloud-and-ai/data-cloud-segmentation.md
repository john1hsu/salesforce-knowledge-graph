---
id: kt:data-cloud-segmentation
type: Feature
title: Data 360 Segmentation
aliases: [Data Cloud segmentation, Data 360 segments, Data Cloud segments, segment canvas, waterfall segments, rapid publish segments, real-time segments]
domain: data-cloud-and-ai
summary: >-
  The Data 360 (formerly Data Cloud) feature for building audiences: filtered sets of profiles, such as unified
  individuals or accounts, defined with attributes and container logic on a segment canvas and published on a schedule
  or on demand to activation targets like Marketing Cloud Engagement.
release: "Winter '27"
status: current
broader: [kt:data-cloud]
related: [kt:calculated-insights, kt:identity-resolution, kt:data-graphs]
relations:
  - {predicate: dependsOn, object: kt:data-model-objects}
  - {predicate: enables, object: kt:data-cloud-activation}
  - {predicate: integratesWith, object: kt:marketing-cloud-engagement}
  - {predicate: governedBy, object: kt:data-cloud-limits}
  - {predicate: queriedWith, object: kt:connect-api}
  - {predicate: coveredBy, object: kt:data-cloud-consultant-certification}
sources:
  - id: s1
    title: "Match Segment Types to Your Use Case (Advanced Segmentation in Data 360)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/advanced-segmentation-in-data-360/match-segment-types-to-your-use-case
    type: official-learning
    accessed: 2026-11-08
  - id: s2
    title: "Manage Segment Lookback, Schedules, and Publish (Advanced Segmentation in Data 360)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/advanced-segmentation-in-data-360/manage-segment-lookback-schedules-and-publish
    type: official-learning
    accessed: 2026-11-08
  - id: s3
    title: "Navigate Data Cloud Segmentation"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/customer-360-audiences-segmentation/navigate-customer-360-audiences-segmentation-
    type: official-learning
    accessed: 2026-11-08
  - id: s4
    title: "CdpSegment Class (Apex Reference Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_ConnectAPI_CdpSegment_static_methods.htm
    type: official-docs
    accessed: 2026-11-08
  - id: s5
    title: "Run Queries and Personalize Engagement with Segmentation"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-cloud-query-and-segment/run-queries-and-personalize-engagement-with-segmentation
    type: official-learning
    accessed: 2026-11-08
created: 2026-11-08
---

# Data 360 Segmentation

**Segmentation** in Data 360 (named Data Cloud until October 2025) is how marketers and admins carve harmonized,
unified customer data into **segments**: filtered audiences used to understand, target and analyze customers. Segments
are built in the Segments tab and published to activation targets such as Marketing Cloud Engagement.[^s3] Combined
with insights, a segment stays dynamic instead of being a static list, for example loyal customers whose engagement
score is high over the past 30 days.[^s5]

## How it works

Every segment starts with a **Segment On** entity, the object whose records become members. Common choices are
Unified Individual (which requires identity resolution), Individual (used without identity resolution, at the risk of
duplicate or skipped people), Unified Household, Account and Unified Account for B2B, or another profile or engagement
DMO.[^s1] That choice decides which attributes appear in the **Attribute Library** on the segment canvas. Only fields
that are mapped in the data model and enabled for segmentation show up there.[^s3]

Attributes come in two kinds. **Direct attributes** have one value per record, such as postal code. **Related
attributes** can have many values per person, such as purchases or email opens.[^s3] You drag attributes into
**containers**. Criteria inside one container must match on the same related record, while separate containers are
evaluated independently. So "scarf AND yellow" in one container finds buyers of a yellow scarf, but split across two
containers it finds anyone who bought any scarf and also any yellow item. Filter values are not case-sensitive. The
canvas shows a **population** count, which refreshes after a publish or an on-demand count.[^s3]

Standard segments also have a **lookback window** that filters on the event timestamp mapped from the data stream.
It defaults to 90 days and can be extended up to 2 years, or 360 days depending on org settings. A narrower window set
on a container overrides the segment's window for that criterion.[^s2]

## Segment types

- **Standard:** built on a DMO with include and exclude criteria and the full set of refinements. Publishes manually
  or on a daily, weekly or monthly schedule, for example every 12 or 24 hours, to any supported target. Standard
  segments can overlap, so one customer can land in several of them.[^s1][^s2]
- **Rapid publish:** refreshes every 1 or 4 hours, looks only at the past 7 days of engagement data, and activates
  only to Marketing Cloud Engagement and cloud file storage. Up to 20 rapid segments are allowed, and a standard segment
  can't be switched to rapid after creation.[^s2]
- **Waterfall:** an ordered list of up to 20 active segments that share the same Segment On entity. Each person is
  placed in the first segment they match, which makes the buckets mutually exclusive. Waterfalls can't contain nested
  segments and use standard publish only.[^s1]
- **Dynamic:** uses standard filters with parameterized values that an external service supplies through the API at
  request time. It has no stored membership and no UI schedule.[^s1]
- **Real-time:** evaluated in milliseconds against a real-time data graph, with no exclusions, no nested batch
  segments, no counts and no manual publish.[^s1][^s5]

## Publishing and gotchas

Publishing writes membership to a segment membership DMO and sends each activation target only the attributes chosen
for that activation. The first publish to a target is a full refresh, and later ones can be incremental. A **Skipped**
or **Deferred** status means simultaneous-publish limits delayed the run and it usually clears on its own. An
**Error** needs investigation followed by Publish Now. Longer lookbacks and more frequent schedules raise processing
cost, while short ones can leave audiences stale.[^s2] Tenant-wide quotas such as active-segment counts are covered in
`kt:data-cloud-limits`.

Segments can also be managed in code. The Apex `ConnectApi.CdpSegment` class can create, update, deactivate, delete,
list (in pages of 1 to 200) and ad hoc publish segments, optionally scoped to a data space.[^s4]

## When to use which

Choose standard segments for scheduled batch campaigns and waterfalls when each customer must receive only one offer,
such as the best discount they qualify for. Use rapid publish for short-lived engagement triggers, dynamic segments
for API-driven lookups, and real-time segments for in-session decisions like next-best-action on a website.[^s1][^s2]

## Connections

Segmentation is a feature of `kt:data-cloud`. It **depends on** `kt:data-model-objects` for its Segment On entities
and attributes, and usually on `kt:identity-resolution` for unified profiles.[^s1][^s3] `kt:calculated-insights`
supply aggregated attributes, and real-time segments run on `kt:data-graphs`.[^s5] Segments **enable**
`kt:data-cloud-activation`, most often **integrating with** `kt:marketing-cloud-engagement`.[^s2][^s3] They are
**governed by** `kt:data-cloud-limits` and can be **accessed with** the `kt:connect-api` (Apex `ConnectApi`)
classes.[^s4] Segmentation is **covered by** `kt:data-cloud-consultant-certification`.

## Sources

[^s1]: Trailhead, "Match Segment Types to Your Use Case (Advanced Segmentation in Data 360)". https://trailhead.salesforce.com/content/learn/modules/advanced-segmentation-in-data-360/match-segment-types-to-your-use-case (accessed 2026-11-08)
[^s2]: Trailhead, "Manage Segment Lookback, Schedules, and Publish (Advanced Segmentation in Data 360)". https://trailhead.salesforce.com/content/learn/modules/advanced-segmentation-in-data-360/manage-segment-lookback-schedules-and-publish (accessed 2026-11-08)
[^s3]: Trailhead, "Navigate Data Cloud Segmentation". https://trailhead.salesforce.com/content/learn/modules/customer-360-audiences-segmentation/navigate-customer-360-audiences-segmentation- (accessed 2026-11-08)
[^s4]: Salesforce Developers, "CdpSegment Class (Apex Reference Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_ConnectAPI_CdpSegment_static_methods.htm (accessed 2026-11-08)
[^s5]: Trailhead, "Run Queries and Personalize Engagement with Segmentation". https://trailhead.salesforce.com/content/learn/modules/data-cloud-query-and-segment/run-queries-and-personalize-engagement-with-segmentation (accessed 2026-11-08)
