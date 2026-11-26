---
id: kt:flow-data-elements
type: Feature
title: Create, Update and Delete Records Elements
aliases: [Create Records element, Update Records element, Delete Records element, Flow DML elements, Flow write elements]
domain: automation
summary: >-
  The three Flow Builder data elements that write to Salesforce: Create Records inserts one or many records,
  Update Records changes the triggering, related or matching records, and Delete Records removes records to the
  Recycle Bin; each element that runs costs one DML statement against the transaction's limits.
release: "Winter '27"
status: current
broader: [kt:flow-builder]
related: [kt:get-records-element, kt:flow-loop-element, kt:flow-assignment-element, kt:record-triggered-flow, kt:flow-transaction-boundaries]
relations:
  - {predicate: governedBy, object: kt:flow-limits}
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: dependsOn, object: kt:flow-bulkification}
sources:
  - id: s1
    title: "Work with Salesforce Records in Flows (Data and Actions in Flows)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-and-actions-in-flows/work-sf-records-flows
    type: official-learning
    accessed: 2026-11-26
  - id: s2
    title: "Update and Retrieve Multiple Records (Multirecord Elements and Transforms in Flows)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/multirecord-elements-and-transforms-in-flows/update-and-retrieve-multiple-records
    type: official-learning
    accessed: 2026-11-26
  - id: s3
    title: "Avoid Flow Limits (Flow Implementation 1)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/flow-implementation-1/avoid-flow-limits
    type: official-learning
    accessed: 2026-11-26
  - id: s4
    title: "Automate This! — Update Related Records with Flow"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2022/automate-this-update-related-records-with-flow
    type: official-blog
    accessed: 2026-11-26
created: 2026-11-26
---

# Create, Update and Delete Records Elements

Flow Builder has a small family of **data elements** that read and write Salesforce records. Get Records reads; **Create Records**, **Update Records** and **Delete Records** write. Changing a flow variable never touches the database on its own: a value only reaches a record when one of these elements runs.[^s1] Each write element that executes counts as one DML statement, so these three elements are where most flow governor-limit problems start.[^s3]

## How each element works

**Create Records** can insert a record for any object visible in Object Manager, including standard, custom and some API-only objects; Trailhead warns that API-only objects tend to carry extra requirements or downstream effects.[^s1] Field values can be set manually, one field at a time, which suits data coming from several sources, such as a Task whose owner and Related To ID come from the triggering Account while Subject and Status are typed in.[^s1] To insert many records at once, the element takes a record collection variable instead of a single record.[^s1][^s3]

**Update Records** offers several ways to pick its targets. In a record-triggered flow it can update the record that triggered the flow; in a before-save flow optimized for Fast Field Updates, that is the only option, and values are typically pulled from the `Triggering` (or `$Record`) global variable, for example copying the parent Account's phone onto a new Contact.[^s1] The **Update Related Records** option starts from the triggering record and walks a relationship: Trailhead's example closes every open Case on the Account of a lost retention Opportunity with one element, filtered to Status not equal to Closed.[^s2] Update Records can also write a record collection built earlier in the flow, which is the pattern the Admins blog uses to change Division on all of an Account's open Opportunities after a loop.[^s4]

**Delete Records** is configured like the other two, by object and filter conditions, and the records it removes go to the Recycle Bin.[^s1] Trailhead's guidance is blunt: delete only when the record should never have existed and nothing needs to remember it, and test the flow thoroughly in a sandbox before activating it.[^s1]

## Limits and gotchas

Trailhead's flow-limits unit lists the per-transaction limits these elements consume:[^s3]

- **DML statements:** 150 per transaction, with each Create, Update or Delete Records element causing one.[^s3]
- **Records written:** 10,000 records created, updated or deleted by DML per transaction.[^s3]
- **Hidden queries:** the filter conditions on Update Records and Delete Records also cost a SOQL query, against the 100-query limit.[^s3]

The classic failure is a data element inside a loop. Trailhead notes that a loop over more than a few records containing Get, Create, Update or Delete Records can quickly exhaust the 100-query or 150-statement limit, so reads belong before the loop and writes after it.[^s3] Its worked example adds each cloned Opportunity Product to a record collection with an Assignment element, then inserts them all with one Create Records element set to create multiple records, a single DML statement.[^s3] The Admins blog calls updating records inside a loop bad practice for the same reason and collects changes before one final Update Records.[^s4]

Filters matter even without a loop. A scheduled flow that unchecks a box on every Contact fails once it touches more than 10,000 records; adding a filter so only checked records are updated keeps it under the limit.[^s3] Trailhead's related-records example likewise filters out closed Cases, because updating years of old records can slow the transaction or exceed governor limits.[^s2] Flows launched by Apex or other automation share the first transaction's limits, and a Screen or Wait element ends the current transaction and starts a new one.[^s3]

For same-record changes, a before-save flow is the faster choice: the Admins blog notes the triggering record is saved only once, so it passes through assignment, workflow and auto-response rules only once.[^s4]

## Connections

These elements sit under **Flow Builder** alongside the **Get Records element**, which supplies the records and IDs they usually act on.[^s1] They are **governed by flow limits** and the underlying **governor limits**, which count each one as a DML statement.[^s3] Using them safely **depends on flow bulkification**: pairing a **Loop element** and **Assignment element** to build a collection, then writing it once.[^s3][^s4] They appear most often in **record-triggered flows**, where the triggering record and its related records are the natural targets.[^s1][^s2] Because Screen and Wait elements split transactions, **flow transaction boundaries** decide which writes share one set of limits.[^s3]

## Sources

[^s1]: Trailhead, "Work with Salesforce Records in Flows (Data and Actions in Flows)". https://trailhead.salesforce.com/content/learn/modules/data-and-actions-in-flows/work-sf-records-flows (accessed 2026-11-26)
[^s2]: Trailhead, "Update and Retrieve Multiple Records (Multirecord Elements and Transforms in Flows)". https://trailhead.salesforce.com/content/learn/modules/multirecord-elements-and-transforms-in-flows/update-and-retrieve-multiple-records (accessed 2026-11-26)
[^s3]: Trailhead, "Avoid Flow Limits (Flow Implementation 1)". https://trailhead.salesforce.com/content/learn/modules/flow-implementation-1/avoid-flow-limits (accessed 2026-11-26)
[^s4]: Salesforce Admins Blog, "Automate This! — Update Related Records with Flow". https://admin.salesforce.com/blog/2022/automate-this-update-related-records-with-flow (accessed 2026-11-26)
