---
id: kt:get-records-element
type: Feature
title: Get Records Element
aliases: [Get Records, Flow Get Records element, Get Records in Flow Builder, Record Lookup element]
domain: automation
summary: >-
  The Flow Builder data element that queries Salesforce records matching filter conditions and stores the first
  match or all matches, with all or selected fields, for later elements to use; each one costs a SOQL query against
  the transaction's limits.
release: "Winter '27"
status: current
broader: [kt:flow-builder]
related: [kt:flow-loop-element, kt:record-triggered-flow, kt:autolaunched-flow, kt:flow-bulkification, kt:flow-fault-handling]
relations:
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: governedBy, object: kt:flow-limits}
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: alternativeTo, object: kt:collection-filter-and-sort}
sources:
  - id: s1
    title: "Combine Variables and Data Elements (Data and Actions in Flows)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-and-actions-in-flows/combine-variables-data-elements
    type: official-learning
    accessed: 2026-11-20
  - id: s2
    title: "Update and Retrieve Multiple Records (Multirecord Elements and Transforms in Flows)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/multirecord-elements-and-transforms-in-flows/update-and-retrieve-multiple-records
    type: official-learning
    accessed: 2026-11-20
  - id: s3
    title: "Avoid Flow Limits (Flow Implementation 1)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/flow-implementation-1/avoid-flow-limits
    type: official-learning
    accessed: 2026-11-20
  - id: s4
    title: "The Ultimate Guide to Flow Best Practices and Standards"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2021/the-ultimate-guide-to-flow-best-practices-and-standards
    type: official-blog
    accessed: 2026-11-20
  - id: s5
    title: "Create Flow Element to Get Contact ID from Email Address (Loan Prequalification Agent)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/ai/loan-agent/guide/create-flow-element-to-get-contact-id.html
    type: official-docs
    accessed: 2026-11-20
created: 2026-11-20
---

# Get Records Element

**Get Records** is the Flow Builder element that reads data from the org. You choose an object, define filter conditions and an optional sort, and decide how many matching records to keep and which of their fields to store; later elements then reference the stored record or collection.[^s1] It is the flow counterpart of a SOQL query, and Salesforce counts each Get Records element that runs as one query against the transaction's limits.[^s3]

## How it works

Configuration follows a fixed sequence. You pick the **object** (for example Opportunity Contact Role, User or Contact) and add **filter conditions**, combined with AND logic when all conditions must be met; filters can compare a field to a value from the triggering record, an input variable or an earlier screen.[^s1][^s5] An optional **sort** orders the results, such as by CreatedDate descending, so that "only the first record" returns the newest match.[^s1][^s5]

**How Many Records to Store** offers two choices. *Only the first record* produces a single record variable, while *All records* returns every match in one record collection variable in which each record keeps its fields and ID.[^s1][^s2] **How to Store Record Data** controls the fields. The default, *Automatically store all fields*, creates a variable holding the whole record; *Choose fields and let Salesforce do the rest* keeps the automatic variable but loads only selected fields, which Trailhead recommends for objects with hundreds of custom fields.[^s1] An advanced option assigns chosen fields to separate variables you create yourself, for instance saving only a Contact's ID into a text variable.[^s5]

Automatically created variables are named after the object and the element, such as "Opportunity Contact Role from Get Decision Maker". The variable exists from the start of the flow but stays empty until the element runs.[^s1] A downstream Create Records, Update Records, Decision or Loop element then uses the stored data.[^s1][^s2]

## Limits and gotchas

Trailhead lists the per-transaction limits a flow shares: 100 SOQL queries and 50,000 records retrieved by SOQL, alongside 150 DML statements, 10,000 DML rows and 10 seconds of CPU time.[^s3] Each Get Records element uses one query, and so do the filter conditions of Update Records and Delete Records elements.[^s3]

- Never place a Get Records element inside a loop; query once before the loop and write once after it, or the 100-query limit arrives quickly.[^s3][^s4]
- Filter narrowly: retrieving every record of a large object risks touching records you didn't intend and hitting execution limits.[^s1][^s3]
- Follow each Get Records with a Decision that checks the result is not empty; use the Is Empty operator to catch both null and empty collections.[^s4]
- Add a fault path so query errors reach an error screen, email alert or logging step; `$Flow.FaultMessage` carries the error text.[^s4][^s5]
- In Experience Cloud screen flows, avoid storing all fields on records that feed screen components, because unneeded data can be visible in browser developer tools.[^s4]
- A flow started by other automation shares that automation's transaction and its limits.[^s3]

## When to use it (and when not)

Use Get Records whenever a flow needs data that isn't already in a variable: related records for an update, a matching contact for a screen flow, or a Record Type or public group looked up by developer name instead of a hard-coded ID.[^s4][^s5] In record-triggered flows, filter conditions on the Start element work like Get Records filters, and specific entry criteria keep the flow, and its queries, from running for irrelevant records.[^s3][^s4]

When the records are already in a collection, the **Collection Filter** and **Collection Sort** elements narrow or reorder them without another query. The In and Not In filter operators let one Get Records replace a query repeated per item.[^s4] For scheduled flows, the Admins guide notes that one interview is created per record the Start element selects, so querying inside a single interview can be the better design for large volumes.[^s4]

## Connections

Get Records is a core **Flow Builder** data element used across **record-triggered** and **autolaunched** flows.[^s1][^s2] Under the hood it is **queried with SOQL**, so it is **governed by** both the **flow limits** and the platform **governor limits**.[^s3] Its output is what the **Loop** element iterates over, and querying before a loop and writing after it is the heart of **flow bulkification**.[^s3][^s4] The **Collection Filter and Sort** elements are an **alternative** when data is already loaded, and **flow fault handling** covers the fault path every query should have.[^s4]

## Sources
[^s1]: Trailhead, "Combine Variables and Data Elements (Data and Actions in Flows)". https://trailhead.salesforce.com/content/learn/modules/data-and-actions-in-flows/combine-variables-data-elements (accessed 2026-11-20)
[^s2]: Trailhead, "Update and Retrieve Multiple Records (Multirecord Elements and Transforms in Flows)". https://trailhead.salesforce.com/content/learn/modules/multirecord-elements-and-transforms-in-flows/update-and-retrieve-multiple-records (accessed 2026-11-20)
[^s3]: Trailhead, "Avoid Flow Limits (Flow Implementation 1)". https://trailhead.salesforce.com/content/learn/modules/flow-implementation-1/avoid-flow-limits (accessed 2026-11-20)
[^s4]: Salesforce Admins Blog, "The Ultimate Guide to Flow Best Practices and Standards". https://admin.salesforce.com/blog/2021/the-ultimate-guide-to-flow-best-practices-and-standards (accessed 2026-11-20)
[^s5]: Salesforce Developers, "Create Flow Element to Get Contact ID from Email Address (Loan Prequalification Agent)". https://developer.salesforce.com/docs/ai/loan-agent/guide/create-flow-element-to-get-contact-id.html (accessed 2026-11-20)
