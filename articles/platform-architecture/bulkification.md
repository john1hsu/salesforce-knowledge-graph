---
id: kt:bulkification
type: Pattern
title: Bulkification
aliases: [bulkify, bulkified code, bulk-safe Apex, bulk trigger pattern]
domain: platform-architecture
summary: >-
  The Salesforce design pattern of writing Apex and automation to process a whole collection of records per
  execution, keeping SOQL queries and DML statements out of loops, so code stays within per-transaction governor
  limits whether it receives one record or a 200-record batch.
release: "Winter '27"
status: current
broader: [kt:governor-limits, kt:multitenancy]
related: [kt:apex-triggers, kt:soql, kt:record-triggered-flow, kt:trigger-framework-pattern, kt:flow-bulkification, kt:asynchronous-apex]
relations:
  - {predicate: mitigates, object: kt:limit-exception}
  - {predicate: coveredBy, object: kt:platform-developer-certification}
sources:
  - id: s1
    title: "Trailhead: Bulk Apex Triggers (Apex Triggers module)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/apex_triggers/apex_triggers_bulk
    type: official-learning
    accessed: 2026-11-10
  - id: s2
    title: "Apex Developer Guide: Trigger and Bulk Request Best Practices"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_triggers_bestpract.htm
    type: official-docs
    accessed: 2026-11-10
  - id: s3
    title: "Apex Developer Guide: Running Apex within Governor Execution Limits"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_limits_tips.htm
    type: official-docs
    accessed: 2026-11-10
  - id: s4
    title: "Understanding the Bulk of the Salesforce1 Platform"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2014/08/understanding-bulk-salesforce1-platform
    type: official-blog
    accessed: 2026-11-10
  - id: s5
    title: "Architect Decision Guide: Record-Triggered Automation"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/decision-guides/guide/record-triggered
    type: official-docs
    accessed: 2026-11-10
  - id: s6
    title: "Salesforce Certified Platform Developer Exam Guide"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298965&language=en_US&type=1
    type: official-learning
    accessed: 2026-11-10
created: 2026-11-10
---

# Bulkification

**Bulkification** is the practice of writing Salesforce code and automation so that a single execution handles a whole set of records efficiently instead of assuming it receives one. Trailhead describes bulkified code as able to process large numbers of records while staying inside governor limits, and adds that bulk-designed triggers perform better and use fewer server resources.[^s1] The pattern exists because the platform is multitenant: the runtime caps what any one transaction can consume, and exceeding a cap raises an exception that cannot be handled.[^s3]

## Why code receives records in bulk

A save from the user interface usually fires a trigger for one record, but bulk DML, API calls and data imports fire the same trigger for many records at once.[^s1] Triggers run in batches of 200 records, so inserting 400 records runs a trigger twice.[^s1] The same holds for loads through the API or Data Loader: a 1,000-record insert reaches a before-insert trigger as five 200-record collections in `Trigger.new`.[^s4] The Apex Developer Guide warns that logic assuming one record may work for most UI actions but fails for bulk operations invoked through the SOAP API or Visualforce.[^s2] The architect decision guide scales this up: a 20,000-record load executes a trigger in chunks of 200, or about 100 invocations.[^s5]

## The core techniques

The official guidance reduces to a few rules, each tied to a per-transaction limit:

- **Process every record.** Loop over all of `Trigger.new` rather than reading `Trigger.new[0]`, which silently ignores the rest of the batch.[^s1][^s2]
- **Query once, outside loops.** Collect IDs into a set (for example `Trigger.newMap.keySet()`) and run one SOQL query with an `IN` filter.[^s2] A query inside the loop runs per record and breaks the 100-query synchronous cap; asynchronous Apex allows 200.[^s1]
- **Use relationship queries.** A parent-to-child subquery fetches parents and their children in one call, instead of a second query per parent.[^s1][^s3]
- **DML on collections.** Add changed records to a list inside the loop and issue one `update` or `insert` after it; DML per record fails at the 151st statement.[^s3]
- **Look up, don't re-query.** Build a map from the single query's results and read values from it while iterating, so query and DML counts stay flat as volume grows.[^s4]

Heap is a second constraint. Holding a large result set in one list can exceed the 6 MB synchronous heap limit, while a SOQL `for` loop processes results in batches of 200 to keep memory bounded.[^s3] Trailhead notes that in triggers the SOQL `for` loop adds no batching benefit, because triggers are already batched.[^s1]

## Gotchas

Bulkification keeps the count of statements constant, but it does not make the transaction free. Every chunk of a bulk load is its own trigger invocation. If each one enqueues asynchronous work, a single data load can consume a large share of the org's daily async allowance and starve other processes.[^s5] Flow bulkifies records automatically and removes redundant queries and DML. But it has no native Map or Set structures, and a Get Records element inside a Loop is a common cause of performance problems.[^s5] In Apex, bulk safety is manual and must be coded explicitly.[^s5]

## When it matters most

Every trigger and invocable method should be bulk-safe, because the caller decides how many records arrive.[^s2] The decision guide uses volume as a design input. Low-density automation (1–200 records) suits record-triggered Flow. Batch processing needs careful bulkification, and loads of 2,000–10,000 or more records via the bulk API point toward an Apex trigger framework.[^s5] The Platform Developer exam expects candidates to follow best practices for Apex classes and triggers. It also tests governor limits and their effect on Apex transactions.[^s6]

## Connections

Bulkification is the coding response to **Governor Limits**, its broader concept, which in turn follow from **multitenancy**.[^s3] It `mitigates` **LimitException**, the uncatchable failure that SOQL or DML in loops produces.[^s3] The **Limits class** is how code checks its remaining budget, and **asynchronous Apex** is where work goes when even bulkified code cannot fit one synchronous transaction, at the cost of the daily async allowance.[^s3][^s5] It is a core rule for **Apex triggers** and the **trigger framework pattern**, and it relies on **SOQL** `IN` filters and relationship queries.[^s1][^s2] **Record-triggered Flow** bulkifies automatically, with the loop caveats covered under **Flow bulkification**.[^s5] Loads through **Bulk API 2.0** and Data Loader are what deliver 200-record batches to triggers.[^s4] The topic maps to the **Platform Developer** certification's trigger best-practice and governor-limit objectives.[^s6]

## Sources

[^s1]: Salesforce Trailhead, "Bulk Apex Triggers". https://trailhead.salesforce.com/content/learn/modules/apex_triggers/apex_triggers_bulk (accessed 2026-11-10)
[^s2]: Salesforce Developers, "Trigger and Bulk Request Best Practices". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_triggers_bestpract.htm (accessed 2026-11-10)
[^s3]: Salesforce Developers, "Running Apex within Governor Execution Limits". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_limits_tips.htm (accessed 2026-11-10)
[^s4]: Markus Spohn, "Understanding the Bulk of the Salesforce1 Platform", Salesforce Developers Blog, 2014-08-18. https://developer.salesforce.com/blogs/2014/08/understanding-bulk-salesforce1-platform (accessed 2026-11-10)
[^s5]: Salesforce Architects, "Record-Triggered Automation" decision guide. https://architect.salesforce.com/docs/architect/decision-guides/guide/record-triggered (accessed 2026-11-10)
[^s6]: Salesforce Help, "Salesforce Certified Platform Developer Exam Guide". https://help.salesforce.com/s/articleView?id=005298965&language=en_US&type=1 (accessed 2026-11-10)
