---
id: kt:field-history-tracking
type: Feature
title: Field History Tracking
aliases: [field history, field history tracking (FHT), object history tracking, history related list]
domain: data-model
summary: >-
  Built-in Salesforce feature that records old and new values of up to 20 selected fields per object in a
  related history object, kept for 18–24 months; Field Audit Trail extends it for long-term, audit-grade retention.
release: "Winter '27"
status: current
broader: [kt:data-architecture]
related: [kt:field-audit-trail, kt:big-objects, kt:archiving-strategy, kt:person-accounts, kt:record-triggered-flow]
relations:
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: contrastsWith, object: kt:field-audit-trail}
  - {predicate: coveredBy, object: kt:platform-data-architect-certification}
sources:
  - id: s1
    title: "Track Object Field History"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.tracking_field_history_for_standard_objects.htm&type=5
    type: official-docs
    accessed: 2026-11-05
  - id: s2
    title: "Salesforce Field History Tracking: Storage Limits and Data Retention"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000383595&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-05
  - id: s3
    title: "Understanding Salesforce Field History Tracking on Record Creation"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000389209&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-05
  - id: s4
    title: "Field Audit Trail — Field History Retention Implementation Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/field-history-retention/guide/field-audit-trail.html
    type: official-docs
    accessed: 2026-11-05
  - id: s5
    title: "SOQL with FieldHistoryArchive"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/field-history-retention/guide/field-history-soql.html
    type: official-docs
    accessed: 2026-11-05
  - id: s6
    title: "Get Started with Field Audit Trail"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/field-audit-trail-basics/get-started-with-field-audit-trail
    type: official-learning
    accessed: 2026-11-05
created: 2026-11-05
---

# Field History Tracking

Field History Tracking (FHT) is the declarative auditing feature that records changes to selected fields on standard and custom objects. Each tracked change is written to the object's related history object and shown in the History related list on the record page, giving users and admins a who-changed-what-when trail without code.[^s1][^s2] It is aimed at short-term operational troubleshooting rather than long-term compliance archiving, which is the job of its paid extension, Field Audit Trail.[^s6]

## How it works

Tracking is enabled per object from Setup (Field History Tracking), after which an admin picks the fields to follow and adds the history related list to page layouts. Tracking starts at the moment it is switched on; it is not retroactive.[^s1] For most fields both the old and new value are stored. Multi-select picklists and large text fields are tracked as "changes only": the history shows that the field was edited, but not the values.[^s1] Custom objects inside managed packages can be tracked too, though a package upgrade does not change subscriber history settings even if the developer altered them.[^s1]

Record creation behaves differently from updates. Creating a record logs a single "created" entry with the user and timestamp; values a user types into tracked fields on that first save are not logged as changes. Values written into tracked fields by automation (Apex, Flow, or legacy workflow) during the create transaction are, however, included in the creation entry.[^s3]

## Limits and gotchas

Verified against Winter '27:

- **20 fields per object.** Standard and custom fields together count toward the limit; on Account the limit is shared between business and person accounts.[^s1][^s2]
- **Retention of 18–24 months.** FHT history is kept for 18 to 24 months; Trailhead describes it as 18 months in the UI and up to 24 months through the API.[^s2][^s6]
- **No data-storage cost.** Field history records do not count against an org's data storage allocation.[^s2]
- **Untrackable fields.** Formula, roll-up summary and auto-number fields, Created By and Last Modified By, fields flagged for AI prediction, Opportunity Expected Revenue, and the Master Solution fields on Solutions cannot be tracked.[^s1]
- **Person contact records** are not tracked, and tracking cannot be turned off for an object whose fields Apex references.[^s1]
- **Deletion cascades.** Deleting a record also deletes its history rows from the history object.[^s2]

## Field Audit Trail: when 18 months isn't enough

Field Audit Trail (FAT), sold with Salesforce Shield or as its own licence, extends FHT to up to 200 tracked fields per object and copies history into the `FieldHistoryArchive` big object, where it stays until explicitly deleted.[^s4][^s2] Retention is governed per object by a `HistoryRetentionPolicy` deployed through Metadata API; with no custom policy, a default policy archives data after 18 months in production and after one month in sandboxes.[^s4] Archived rows survive deletion of the parent record and must be purged through REST, SOAP or Tooling API.[^s2][^s4] Querying the archive follows big-object rules: filter on `FieldHistoryType` first, then `ParentId` or `CreatedDate`; only the last filter may use a range or `IN`; operators such as `!=` and `LIKE` are rejected; and an unbounded query returns at most 2,000 rows per batch.[^s5] One gotcha is that turning on Platform Encryption does not encrypt data already archived; that requires Salesforce to re-archive it.[^s4]

## When to use it (and when not)

Use FHT for everyday "who changed this status?" questions, dispute resolution, and reports on recent changes, keeping the 20-field budget for fields that drive business decisions.[^s1][^s6] For regulatory regimes that demand multi-year, provable audit trails, plan for Field Audit Trail or an external archive, because standard history will age out.[^s6][^s4]

## Connections

FHT is part of the org's broader **data architecture**: the history tables are a data-retention decision, which is why it pairs with an **archiving strategy** and, at scale, with **big objects**, the storage technology behind `FieldHistoryArchive`.[^s4][^s2] It **contrasts with Field Audit Trail**, which shares the concept but differs in field limit, retention and licensing.[^s4] History rows and the archive are **queried with SOQL**, the archive under big-object filter rules.[^s5] The **person accounts** link reflects the shared 20-field budget on Account, and the **record-triggered flow** link reflects that automation-written values at create time do appear in history.[^s1][^s3]

## Sources

[^s1]: Salesforce Help, "Track Object Field History". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.tracking_field_history_for_standard_objects.htm&type=5 (accessed 2026-11-05)
[^s2]: Salesforce Help, "Salesforce Field History Tracking: Storage Limits and Data Retention". https://help.salesforce.com/s/articleView?id=000383595&language=en_US&type=1 (accessed 2026-11-05)
[^s3]: Salesforce Help, "Understanding Salesforce Field History Tracking on Record Creation". https://help.salesforce.com/s/articleView?id=000389209&language=en_US&type=1 (accessed 2026-11-05)
[^s4]: Salesforce Developers, "Field Audit Trail". https://developer.salesforce.com/docs/platform/field-history-retention/guide/field-audit-trail.html (accessed 2026-11-05)
[^s5]: Salesforce Developers, "SOQL with FieldHistoryArchive". https://developer.salesforce.com/docs/platform/field-history-retention/guide/field-history-soql.html (accessed 2026-11-05)
[^s6]: Trailhead, "Get Started with Field Audit Trail". https://trailhead.salesforce.com/content/learn/modules/field-audit-trail-basics/get-started-with-field-audit-trail (accessed 2026-11-05)
