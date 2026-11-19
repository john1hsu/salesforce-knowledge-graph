---
id: kt:data-cloud-triggered-flows
type: Feature
title: Data Cloud-Triggered Flow
aliases: [Data Cloud-triggered flows, Data 360-triggered flow, Data 360-triggered flows, flows triggered by Data 360 data]
domain: data-cloud-and-ai
summary: >-
  A Flow Builder flow type that starts when a new or changed record in a Data 360 (formerly Data Cloud) data model
  object, calculated insight object or accelerated external object meets the conditions set in its Start element,
  letting admins act on unified customer data inside the Salesforce org without code.
release: "Winter '27"
status: current
broader: [kt:data-cloud, kt:flow-builder]
related: [kt:record-triggered-flow, kt:platform-event-triggered-flow]
relations:
  - {predicate: dependsOn, object: kt:data-model-objects}
  - {predicate: dependsOn, object: kt:calculated-insights}
  - {predicate: dependsOn, object: kt:data-actions}
  - {predicate: integratesWith, object: kt:zero-copy-data-federation}
sources:
  - id: s1
    title: "Trigger Flows with Data 360 Data"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.flow_concepts_trigger_data_cloud.htm&amp=&type=5
    type: official-docs
    accessed: 2026-11-19
  - id: s2
    title: "Data 360: Data Cloud Triggered Flow Fails to Trigger for All Records"
    publisher: Salesforce Help (Knowledge Article)
    url: https://help.salesforce.com/s/articleView?id=005314323&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-19
  - id: s3
    title: "Trigger Flows from Data Cloud"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-cloud-in-flows/trigger-flows-from-data-cloud
    type: official-learning
    accessed: 2026-11-19
  - id: s4
    title: "Access Data Cloud from Flows"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-cloud-in-flows/access-data-cloud-from-flows
    type: official-learning
    accessed: 2026-11-19
  - id: s5
    title: "Power Automation with Flows and Agents (Data 360: Act on Data)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-cloud-act-on-data/power-automation-with-flows-and-agents
    type: official-learning
    accessed: 2026-11-19
  - id: s6
    title: "Automate Your Workflow with Data Cloud-Triggered Flows and Invocable Actions"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/08/automate-your-workflow-with-data-cloud-triggered-flows-and-invocable-actions
    type: official-blog
    accessed: 2026-11-19
created: 2026-11-19
---

# Data Cloud-Triggered Flow

A **Data Cloud-triggered flow** is a flow type in Flow Builder that runs when Data 360 (formerly Data Cloud) data
changes. Salesforce Help documents it under the heading "Trigger Flows with Data 360 Data" and still lists the flow
type as Data Cloud-Triggered Flow.[^s1] Trailhead draws the line simply: record-triggered flows react to changes in
Salesforce CRM records, and Data Cloud-triggered flows react to changes in Data 360 objects.[^s3] The developer blog
describes the pattern as event-driven, reacting to near-real-time changes that streaming ingestion brings in rather
than running on a schedule.[^s6]

## How it works

You create one from the Flows list: choose New Flow, start from scratch, pick Data Cloud-Triggered Flow, then use
the Start element to choose the object and conditions.[^s1] Trailhead's walkthrough also selects a data space (for
example `default`), the trigger event, and the condition logic.[^s3]

The flow can start from three kinds of object:[^s1]

- **Data model objects (DMOs)**, but only a DMO that is mapped as part of a data stream.[^s1]
- **Calculated insight objects (CIOs)**, which fire when a recalculation produces a new or changed output row.[^s1][^s3]
- **Accelerated external objects**, including Bring Your Own Lake objects; a non-accelerated BYOL object has no trigger path.[^s1]

Raw data lake objects are not available to flows; you work with DMOs and calculated insight results.[^s5]

The trigger is the qualifying record change, not the job that caused it. Data stream refreshes, connectors, the
Ingestion API, data transforms and calculated insight runs start a flow only when they produce a qualifying new or
changed record. A refresh that changes nothing starts nothing, and activating a flow doesn't process records that
already exist.[^s1] For updates, the option "Only when a record is updated to meet the condition requirements" fires
only on the transition from not meeting the conditions to meeting them.[^s1]

Inside the flow you can query both Salesforce objects and Data 360 objects, send email, create records and build
text from templates.[^s3] Trailhead's examples email a guest whose loyalty tier changes to Diamond, and open a
high-priority case for a queue once an abandoned-cart insight reaches three or more abandons.[^s3] For heavier work,
the developer blog has the flow check consent, create a lead and publish a platform event. A platform event-triggered
flow then calls invocable Apex that performs a credit-check callout through a named credential.[^s6]

## Limits and gotchas

- Under the hood each qualifying record is delivered to the org as a data change event by a background data action.[^s2]
- That event has a record-level limit of 128k characters (125,000 for payload values) summed across all columns.[^s2]
- Records over the limit are skipped with no error on the flow; monitor the Data Actions Activity tab in Data 360.[^s2]
- To stay under it, unmap large text fields the routing logic doesn't need and pass a reference ID instead.[^s2]
- Data volume, flow complexity and the data stream refresh schedule can delay when the flow runs.[^s1]
- Users need Manage Flow, View Setup, View All Data and Data Cloud User access, or the legacy Data Cloud Marketing Admin permission.[^s1]
- When you only need to read Data 360 data from a CRM record-triggered flow, use Get Records on an asynchronous or scheduled path.[^s4]

Salesforce Help gives no per-org count or execution quota for these flows, so this article states none.[^s1]

## When to use it (and when not)

Use a Data Cloud-triggered flow when a Data 360 signal, such as a tier change on a unified profile or an insight
crossing a threshold, should create or update CRM records or notify people inside the same org.[^s3][^s5] Use a
record-triggered flow when the change happens on a CRM record and Data 360 only supplies lookup data.[^s4] When the
trigger is a streaming insight or another insight type, Trailhead routes you to **data actions** instead.[^s3] When the flow needs
callouts or complex logic, hand off to a platform event and invocable Apex, as the developer blog's example does.[^s6]

## Connections

The flow type sits **broader** under `kt:data-cloud` and `kt:flow-builder`, where it appears alongside other
triggered flow types.[^s1] It is **related** to `kt:record-triggered-flow`, its CRM-side counterpart, and to
`kt:platform-event-triggered-flow`, which it often hands work to.[^s3][^s6] It **depends on**
`kt:data-model-objects` and `kt:calculated-insights` as trigger sources, and on `kt:data-actions` as the delivery
mechanism behind each trigger.[^s1][^s2] It **integrates with** `kt:zero-copy-data-federation` through accelerated
Bring Your Own Lake objects.[^s1]

## Sources

[^s1]: Salesforce Help, "Trigger Flows with Data 360 Data". https://help.salesforce.com/s/articleView?language=en_US&id=sf.flow_concepts_trigger_data_cloud.htm&amp=&type=5 (accessed 2026-11-19)
[^s2]: Salesforce Help, "Data 360: Data Cloud Triggered Flow Fails to Trigger for All Records". https://help.salesforce.com/s/articleView?id=005314323&language=en_US&type=1 (accessed 2026-11-19)
[^s3]: Trailhead, "Trigger Flows from Data Cloud". https://trailhead.salesforce.com/content/learn/modules/data-cloud-in-flows/trigger-flows-from-data-cloud (accessed 2026-11-19)
[^s4]: Trailhead, "Access Data Cloud from Flows". https://trailhead.salesforce.com/content/learn/modules/data-cloud-in-flows/access-data-cloud-from-flows (accessed 2026-11-19)
[^s5]: Trailhead, "Power Automation with Flows and Agents". https://trailhead.salesforce.com/content/learn/modules/data-cloud-act-on-data/power-automation-with-flows-and-agents (accessed 2026-11-19)
[^s6]: Salesforce Developers Blog, "Automate Your Workflow with Data Cloud-Triggered Flows and Invocable Actions". https://developer.salesforce.com/blogs/2024/08/automate-your-workflow-with-data-cloud-triggered-flows-and-invocable-actions (accessed 2026-11-19)
