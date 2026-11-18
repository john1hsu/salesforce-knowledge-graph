---
id: kt:flow-limits
type: Limit
title: Flow Limits
aliases: [flow limits and considerations, flow limits per org, per-transaction flow limits, general flow limits]
domain: automation
summary: >-
  The limits that apply to Salesforce Flow: per-transaction governor limits that flows share with Apex (SOQL, DML,
  CPU time), plus org-level allocations such as versions per flow, active flows per flow type, interview size and
  schedule-triggered interviews per 24 hours.
release: "Winter '27"
status: current
broader: [kt:governor-limits, kt:flow-builder]
related: [kt:flow-bulkification, kt:flow-transaction-boundaries, kt:schedule-triggered-flow, kt:flow-fault-handling, kt:flow-versioning, kt:workflow-rules]
relations:
  - {predicate: partOf, object: kt:governor-limits}
  - {predicate: causes, object: kt:limit-exception}
sources:
  - id: s1
    title: "Per-Transaction Flow Limits (Salesforce Help)"
    publisher: Salesforce
    url: https://help.salesforce.com/s/articleView?id=platform.flow_considerations_limit_transaction.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-18
  - id: s2
    title: "Flow Limits per Org (Salesforce Help)"
    publisher: Salesforce
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.flow_considerations_limit.htm&type=5
    type: official-docs
    accessed: 2026-11-18
  - id: s3
    title: "Schedule-Triggered Flow Limits and Considerations (Salesforce Help)"
    publisher: Salesforce
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.flow_considerations_trigger_schedule.htm&type=5
    type: official-docs
    accessed: 2026-11-18
  - id: s4
    title: "Paused Flow Interview Considerations (Salesforce Help)"
    publisher: Salesforce
    url: https://help.salesforce.com/s/articleView?id=platform.flow_considerations_design_pause.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-18
  - id: s5
    title: "Trailhead: Avoid Flow Limits (Flow Implementation I)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/flow-implementation-1/avoid-flow-limits
    type: official-learning
    accessed: 2026-11-18
  - id: s6
    title: "Flow Limits and Considerations (Salesforce Help)"
    publisher: Salesforce
    url: https://help.salesforce.com/s/articleView?id=flow_considerations.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-18
created: 2026-11-18
---

# Flow Limits

**Flow limits** are the ceilings Salesforce places on what flows can do. They come in two layers. The first is the set of **per-transaction limits**, which Apex enforces and which flows share with any Apex code in the same transaction. The second is a set of **org-level allocations** that cap how many flows, versions and interviews an org can have.[^s6][^s1][^s2] Salesforce documents them together under Flow Limits and Considerations, alongside design, packaging and debugging considerations.[^s6]

## Per-transaction limits

Flow elements are translated into the same SOQL queries, DML statements and CPU time that Apex consumes. The documented ceilings per transaction are:[^s1][^s5]

- **SOQL queries: 100.** Get Records counts, as do Update or Delete Records that use filter conditions.[^s1]
- **Records retrieved by SOQL: 50,000**, and **DML statements: 150** (Create, Update and Delete Records).[^s1]
- **Records processed by DML: 10,000**, and **CPU time: 10,000 milliseconds** on Salesforce servers.[^s1]
- **Duplicate updates in one batch: 12.**[^s1]

When an element pushes the transaction past a limit, the whole transaction rolls back, and a fault connector on that element does not prevent the rollback.[^s1][^s6] An autolaunched flow started by Apex or another automation runs inside the caller's transaction and spends from the same budget. Trailhead's example is an Apex class using 9 seconds of CPU that calls a flow using 2 seconds: both fail.[^s5][^s1]

## Org-level allocations

The per-org page lists limits by edition. For Enterprise, Unlimited, Performance and Developer editions, an org can have **2,000 active flows** and **4,000 total flows per flow type**; Essentials and Professional are limited to 5 of each.[^s2] Every edition allows **50 versions per flow**, and a flow interview can be roughly **1 MB**; larger interviews can't be saved or paused.[^s2] The old cap of 2,000 executed elements per interview applied only to API version 56.0 and earlier, and API 57.0 removed it.[^s2] Total heap per flow interview is 215 MB at API 61.0 and later.[^s2] Marketing flow types have their own, higher active and total flow counts that vary by marketing edition.[^s2]

## Scheduled and paused interviews

**Schedule-triggered flows** create one interview per record the start query returns. An org can run **250,000 interviews per 24 hours**, or 200 times its user licences if that is greater, and a single flow is capped at 250,000.[^s3][^s2] The batch size defaults to 200 and can be set from 1 to 200. Hitting the limit sends a flow error email.[^s3]

**Paused interviews** (Wait elements) end their transaction. On resume, interviews from the same user, time and flow version run together as one batch transaction, so the batch can exceed SOQL or DML limits.[^s1][^s4] An org processes up to 1,000 time-based resume events per hour and defers the rest to the next hour. A paused interview over 1 MB fails to save.[^s4]

## Avoiding the limits

Trailhead's guidance mirrors Apex bulkification. Filter Get Records and record-triggered start conditions so the flow touches only the records it needs. Put Get Records before loops and Create, Update and Delete after them, collecting records into a collection variable for one DML statement.[^s5] A schedule-triggered flow that updates every contact fails once the object exceeds 10,000 contacts, unless it is filtered.[^s5] Where usage cannot be reduced, a Wait element starts a new transaction with fresh limits.[^s5] For resumed batches, Salesforce suggests fault paths that loop back to a Wait element when a too-many-queries or too-many-DML error occurs.[^s4]

## Connections

Flow limits are **part of** the platform's **governor limits** and sit under **Flow Builder**, because Apex enforces the same per-transaction budget for both.[^s6][^s1] **Flow bulkification** and **flow transaction boundaries** explain how interviews share or split that budget; **schedule-triggered flows** carry their own interview allocation, and **flow versioning** is bounded by the 50-version ceiling.[^s3][^s2] Exceeding a per-transaction limit **causes** a **LimitException**-style failure that **flow fault handling** cannot catch, because the transaction rolls back regardless.[^s1] Flow resume events also draw on a combined org total of 20,000 time-based automations that they share with scheduled actions in processes and time triggers in legacy **workflow rules**.[^s2]

## Sources
[^s1]: Salesforce, "Per-Transaction Flow Limits". https://help.salesforce.com/s/articleView?id=platform.flow_considerations_limit_transaction.htm&language=en_US&type=5 (accessed 2026-11-18)
[^s2]: Salesforce, "Flow Limits per Org". https://help.salesforce.com/s/articleView?language=en_US&id=sf.flow_considerations_limit.htm&type=5 (accessed 2026-11-18)
[^s3]: Salesforce, "Schedule-Triggered Flow Limits and Considerations". https://help.salesforce.com/s/articleView?language=en_US&id=platform.flow_considerations_trigger_schedule.htm&type=5 (accessed 2026-11-18)
[^s4]: Salesforce, "Paused Flow Interview Considerations". https://help.salesforce.com/s/articleView?id=platform.flow_considerations_design_pause.htm&language=en_US&type=5 (accessed 2026-11-18)
[^s5]: Salesforce Trailhead, "Avoid Flow Limits". https://trailhead.salesforce.com/content/learn/modules/flow-implementation-1/avoid-flow-limits (accessed 2026-11-18)
[^s6]: Salesforce, "Flow Limits and Considerations". https://help.salesforce.com/s/articleView?id=flow_considerations.htm&language=en_US&type=5 (accessed 2026-11-18)
