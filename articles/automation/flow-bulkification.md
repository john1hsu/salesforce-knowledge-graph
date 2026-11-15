---
id: kt:flow-bulkification
type: Concept
title: Flow Bulkification
aliases: [flow bulkification in transactions, bulkify flows, bulkified flow, flow interview bulkification]
domain: automation
summary: >-
  How Salesforce Flow groups the interviews of a multi-record transaction so that their Get, Create, Update and
  Delete operations run as shared SOQL queries and DML statements, and the matching design rule of keeping data
  elements out of loops so a flow stays within per-transaction governor limits.
release: "Winter '27"
status: current
broader: [kt:bulkification, kt:flow-builder]
related: [kt:record-triggered-flow, kt:flow-transaction-boundaries, kt:flow-fault-handling, kt:code-analyzer, kt:apex-triggers]
relations:
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: governedBy, object: kt:flow-limits}
  - {predicate: mitigates, object: kt:limit-exception}
sources:
  - id: s1
    title: "Flow Bulkification in Transactions (Salesforce Help)"
    publisher: Salesforce
    url: https://help.salesforce.com/s/articleView?id=flow_concepts_bulkification.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-15
  - id: s2
    title: "Bulkified Record Processing to Avoid CPU Limits Example (Salesforce Help)"
    publisher: Salesforce
    url: https://help.salesforce.com/s/articleView?id=platform.automate_flow_build_example_bulkified_processing.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-15
  - id: s3
    title: "Trailhead: Avoid Flow Limits (Flow Implementation module)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/flow-implementation-1/avoid-flow-limits
    type: official-learning
    accessed: 2026-11-15
  - id: s4
    title: "Record-Triggered Automation Decision Guide"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/decision-guides/guide/record-triggered
    type: official-docs
    accessed: 2026-11-15
  - id: s5
    title: "Flow Scanner Rules Reference (Salesforce Code Analyzer)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-code-analyzer/guide/rules-flow.html
    type: official-docs
    accessed: 2026-11-15
  - id: s6
    title: "How Flows Run in Transactions (Salesforce Help)"
    publisher: Salesforce
    url: https://help.salesforce.com/s/articleView?language=en_US&id=flow_concepts_transaction.htm&type=0
    type: official-docs
    accessed: 2026-11-15
created: 2026-11-15
---

# Flow Bulkification

**Flow bulkification** has two halves. The first is something the Flow runtime does for you: when one transaction starts a flow for many records, Salesforce runs one flow interview per record and then merges the interviews' database work into shared operations.[^s1] The second is something the builder must do: inside a single interview, nothing is merged, so Get, Create, Update and Delete Records elements placed inside a Loop still run once per iteration.[^s1][^s3] A flow is only bulk-safe when both halves line up.

## How the runtime bulkifies interviews

When a flow runs for multiple records at once, each interview proceeds until it reaches a bulkifiable element. Salesforce then collects every interview waiting at that same element, executes their operations together, and repeats the cycle until all interviews finish.[^s1] Salesforce's documentation describes elements that do DML, SOQL or work outside the flow (such as sending email) as bulkifiable. Its lists include Create, Update and Delete Records, Get Records, the Quick Action, Post to Chatter, Submit for Approval and Send Email core actions, Email Alert elements, and some Apex actions.[^s1]

Salesforce's worked example updates 100 cases through Data Loader. The flow's Get Records step runs as one SOQL query instead of 100. When the interviews split down two branches, each branch's Chatter posts are created in one DML statement per branch, so the work still finishes in a handful of statements.[^s1] Branching therefore costs extra operations per distinct element reached, not per record.

## What the runtime does not fix

Consolidation happens across interviews, not within one. A Create Records element inside a loop issues a DML operation on every pass, and a Get Records inside a loop issues a query on every pass.[^s1][^s3] Trailhead lists the per-transaction ceilings these patterns hit: 100 SOQL queries, 50,000 records retrieved, 150 DML statements, 10,000 records changed by DML, and 10 seconds of CPU time.[^s3] A flow started by Apex or other automation shares that transaction, so it shares the same budget.[^s3][^s6]

## The collection pattern

The documented fix is to move data elements out of the loop:

- Query once with Get Records **before** the loop, filtered as tightly as possible, and iterate over the resulting collection.[^s3]
- Inside the loop, use Assignment elements to set field values on a record variable and add it to a record collection variable; this step does no DML.[^s2]
- After the loop, one Create, Update or Delete Records element processes the whole collection in a single statement.[^s2][^s3]

In Salesforce's Closed Won example, an opportunity with five team members needs five DML operations when tasks are created inside the loop but only one when they are collected first. The loop version causes `APEX_CPU_TIME_LIMIT_EXCEEDED` errors under bulk updates.[^s2] Salesforce also advises testing with realistic volumes (for example, mass-updating 10 to 20 records in a sandbox) and checking debug logs for CPU time, rather than debugging a single record.[^s2]

## Limits and gotchas

- If any interview in the batch hits a governor limit, every interview in the transaction fails and its operations roll back without a retry.[^s1]
- For errors other than governor limits, Salesforce retries saving the successful record changes in the bulk operation up to three times; external-data operations are not rolled back.[^s1]
- Flow has no native Map or Set types and cannot cache state across flows or invocations in one transaction, so complex, high-volume logic is a weaker fit than Apex.[^s4]
- Entry conditions and before-save (fast field update) flows for same-record changes cut work more than splitting logic across many flows does.[^s4][^s2]

## When to use it (and when not)

Treat every record-triggered and autolaunched flow as if it will receive a bulk load, because data loads and API clients decide the batch size, not the builder.[^s2] The Architects decision guide places user-driven and small API loads (1–200 records) comfortably within Flow's range. For bulk API loads of 2,000–10,000+ records it points to Apex, where bulkification is coded explicitly with Maps and Sets.[^s4]

## Connections

Flow bulkification is the Flow-specific form of the broader **bulkification** pattern and is part of how flows built in **Flow Builder** run.[^s1] It is **governed by** per-transaction **governor limits**, which the flow-level limit set restates for Flow, and it **mitigates** the limit exceptions that queries or DML in loops cause.[^s3] It matters most for **record-triggered flows**, whose interviews arrive in batches, and it interacts with **flow transaction boundaries**, since Screen, Local Action and Wait elements decide which interviews share one budget.[^s6] When a governor limit is breached, every interview fails together, so **flow fault handling** cannot rescue that transaction.[^s1] **Code Analyzer**'s Flow Scanner flags the anti-pattern with its high-severity DbInLoop rule, and **Apex triggers** are the alternative when volume outgrows Flow.[^s5][^s4]

## Sources
[^s1]: Salesforce, "Flow Bulkification in Transactions (Salesforce Help)". https://help.salesforce.com/s/articleView?id=flow_concepts_bulkification.htm&language=en_US&type=5 (accessed 2026-11-15)
[^s2]: Salesforce, "Bulkified Record Processing to Avoid CPU Limits Example (Salesforce Help)". https://help.salesforce.com/s/articleView?id=platform.automate_flow_build_example_bulkified_processing.htm&language=en_US&type=5 (accessed 2026-11-15)
[^s3]: Salesforce Trailhead, "Avoid Flow Limits (Flow Implementation module)". https://trailhead.salesforce.com/content/learn/modules/flow-implementation-1/avoid-flow-limits (accessed 2026-11-15)
[^s4]: Salesforce Architects, "Record-Triggered Automation Decision Guide". https://architect.salesforce.com/docs/architect/decision-guides/guide/record-triggered (accessed 2026-11-15)
[^s5]: Salesforce Developers, "Flow Scanner Rules Reference (Salesforce Code Analyzer)". https://developer.salesforce.com/docs/platform/salesforce-code-analyzer/guide/rules-flow.html (accessed 2026-11-15)
[^s6]: Salesforce, "How Flows Run in Transactions (Salesforce Help)". https://help.salesforce.com/s/articleView?language=en_US&id=flow_concepts_transaction.htm&type=0 (accessed 2026-11-15)
