---
id: kt:big-objects
type: Feature
title: Big Objects
aliases: [big object, custom big objects, __b object, __b objects]
domain: data-model
summary: >-
  Salesforce objects, suffixed __b, backed by a horizontally scalable, non-transactional distributed store that keeps
  hundreds of millions or billions of records queryable through a fixed composite index.
release: "Winter '27"
status: current
broader: [kt:large-data-volumes, kt:data-architecture]
related: [kt:archiving-strategy, kt:external-objects, kt:field-history-tracking, kt:data-skew, kt:data-cloud]
relations:
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: dependsOn, object: kt:queueable-apex}
  - {predicate: contrastsWith, object: kt:external-objects}
  - {predicate: coveredBy, object: kt:platform-data-architect-certification}
sources:
  - id: s1
    title: "Big Objects — Big Objects Implementation Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/big-object-impl-guide/guide/big-object.html
    type: official-docs
    accessed: 2026-11-04
  - id: s2
    title: "Big Objects Best Practices"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.bigobjects.meta/bigobjects/big_object_considerations.htm
    type: official-docs
    accessed: 2026-11-04
  - id: s3
    title: "Big Objects: Define Custom Big Objects"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/big_objects/big_objects_define_custom_big_objects
    type: official-learning
    accessed: 2026-11-04
  - id: s4
    title: "SOQL with Big Objects"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.254.0.bigobjects.meta/bigobjects/big_object_querying.htm
    type: official-docs
    accessed: 2026-11-04
created: 2026-11-04
---

# Big Objects

A big object is a Salesforce object built to hold and serve very large data volumes on the platform itself, either data archived from ordinary objects or datasets loaded from outside systems. Salesforce describes performance as consistent whether the object holds one million, a hundred million or a billion records, and treats that scale as the defining trait. Unlike regular sObjects, which sit on a relational, transactional database and typically hold millions of rows, big objects sit on a horizontally scalable distributed database that is non-transactional.[^s1]

There are two kinds. **Standard big objects** ship with Salesforce products and cannot be customised; `FieldHistoryArchive`, which backs Field Audit Trail, is the usual example. **Custom big objects** are ones you define for your own data, such as a historical inventory log.[^s1]

## How it works

A custom big object has an API name ending in `__b` (custom objects use `__c`), and the name must be unique across standard, custom, external and big objects in the org. You can define it in Setup or through Metadata API. Supported field types are Lookup Relationship, Date/Time, Email, Number, Phone, Text, Text Area (Long) and URL.[^s3][^s2]

The heart of the design is the **index**, which acts as the composite primary key and is the only way to filter. It needs between one and five custom fields, all required; Long Text Area fields are not allowed, and the text fields in it may total no more than 100 characters. A new big object stays *In Development* until it has an index, and once created the index cannot be edited or deleted: changing it means building a new big object.[^s3]

Writes are idempotent on the index: inserting a record whose index values already exist overwrites that record instead of creating a duplicate, so a failed load can simply be retried. Data arrives through Data Loader, Bulk API or SOAP API with a CSV, or from Apex with `Database.insertImmediate`.[^s3][^s1] Supported access paths are SOQL, Bulk, Chatter and SOAP APIs; the implementation guide states REST API is not supported.[^s1]

Queries must filter on index fields starting from the first one, in order, with no gaps. `=` and `IN` work on any of those fields (only one `IN` per query), and range operators are allowed only on the last field filtered. `!=`, `LIKE`, `NOT IN`, `INCLUDES`, `EXCLUDES`, aggregate functions and subqueries are not allowed.[^s4]

## Limits and gotchas

- An org can create up to 100 big objects; field limits follow custom-object limits for the org's license type. Enterprise, Performance, Unlimited and Developer Editions include big objects for up to 1 million records.[^s2]
- No transactions, triggers, flows, processes or Salesforce mobile app support. Only object and field permissions apply; sharing rules do not.[^s1]
- Batch writes can partially fail. Salesforce's guidance is to retry the whole batch until the call succeeds rather than hunting for failed rows, and to check `Database.SaveResult`.[^s2]
- To touch a big object from sObject automation, use asynchronous Apex; a `Queueable` isolates the DML and avoids mixed-DML errors. Apex tests that mix DML fail, so use the stub API to mock it.[^s2][^s3]
- Big objects do not support encryption: encrypted data archived into them is stored as clear text, except field history archived through the Shield field history archive.[^s2]
- No standard UI: show data with custom Lightning or Visualforce components. Salesforce Connect cannot reach big objects in another org.[^s2]

## When to use it (and when not)

Salesforce positions big objects for three jobs: enriching a 360-degree customer view with high-volume detail such as clickstream or billing events, keeping long-term audit and usage history for compliance, and archiving old records so core CRM objects stay fast.[^s1] They suit append-mostly data you look up by a known key. They are a poor fit when users need ad hoc filtering, aggregation, sharing-based visibility or record-triggered automation, because the fixed index and missing transactional features rule those out.[^s4][^s1]

## Connections

Big objects are one of the platform's main tools for **large data volumes** and an option in **data architecture** and **archiving strategy** decisions, where moving cold rows off standard objects relieves query and sharing load.[^s1] They **contrast with external objects**: both handle data you don't keep in ordinary objects, but big objects store it inside Salesforce while external objects read it live from another system.[^s2] Their standard example, `FieldHistoryArchive`, links them to **field history tracking** and Field Audit Trail.[^s1] They are **queried with SOQL** under strict index rules[^s4], can be **configured via Metadata API**[^s2], and **depend on Queueable Apex** when written from triggers or flows.[^s2]

## Sources

[^s1]: Salesforce Developers, "Big Objects — Big Objects Implementation Guide". https://developer.salesforce.com/docs/platform/big-object-impl-guide/guide/big-object.html (accessed 2026-11-04)
[^s2]: Salesforce Developers, "Big Objects Best Practices". https://developer.salesforce.com/docs/atlas.en-us.bigobjects.meta/bigobjects/big_object_considerations.htm (accessed 2026-11-04)
[^s3]: Trailhead, "Big Objects: Define Custom Big Objects". https://trailhead.salesforce.com/content/learn/modules/big_objects/big_objects_define_custom_big_objects (accessed 2026-11-04)
[^s4]: Salesforce Developers, "SOQL with Big Objects". https://developer.salesforce.com/docs/atlas.en-us.254.0.bigobjects.meta/bigobjects/big_object_querying.htm (accessed 2026-11-04)
