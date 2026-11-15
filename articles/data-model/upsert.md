---
id: kt:upsert
type: Concept
title: Upsert
aliases: [upsert operation, upsert call, insert or update, Database.upsert, upsert DML]
domain: data-model
summary: >-
  A single write operation that inserts a record when its matching key finds no existing record and updates the
  record when the key finds exactly one, available in Apex DML, SOAP API, REST API and Bulk API 2.0.
release: "Winter '27"
status: current
broader: [kt:data-integration]
related: [kt:data-loader, kt:data-migration-strategy, kt:batch-data-synchronization, kt:object-relationships, kt:duplicate-management]
relations:
  - {predicate: dependsOn, object: kt:external-id-fields}
  - {predicate: queriedWith, object: kt:soap-api}
  - {predicate: queriedWith, object: kt:rest-api}
  - {predicate: queriedWith, object: kt:bulk-api-2}
  - {predicate: consumedBy, object: kt:apex}
sources:
  - id: s1
    title: "upsert() — SOAP API Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_upsert.htm
    type: official-docs
    accessed: 2026-11-15
  - id: s2
    title: "Upserting Records — Apex Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/langCon_apex_dml_examples_upsert.htm
    type: official-docs
    accessed: 2026-11-15
  - id: s3
    title: "Upsert Records Using sObject Rows by External ID — REST API Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-rest/guide/resources-sobject-upsert-patch.html
    type: official-docs
    accessed: 2026-11-15
  - id: s4
    title: "Step 5: Bulk Upsert — Bulk API 2.0 and Bulk API Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-asynch/guide/walkthrough-upsert.html
    type: official-docs
    accessed: 2026-11-15
  - id: s5
    title: "Manipulate Records with DML — Apex Basics & Database"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/apex_database/apex_database_dml
    type: official-learning
    accessed: 2026-11-15
created: 2026-11-15
---

# Upsert

**Upsert** is Salesforce's combined insert-or-update operation. Each incoming record carries a matching key; if the
key matches no existing record, Salesforce creates one, and if it matches exactly one, Salesforce updates that
record.[^s1][^s5] The same semantics are exposed in Apex DML, SOAP API, REST API and Bulk API 2.0, which is why
upsert is the default verb for integrations and repeatable data loads: the caller does not need to know in advance
whether a record already exists.[^s1][^s3][^s4] Salesforce's SOAP guide recommends it over plain create to avoid
creating duplicates.[^s1]

## How it works

**Choosing the key.** In Apex, if no field is named, upsert matches on the record ID: rows with a null ID are
inserted and rows with an ID are updated.[^s2][^s5] More commonly the caller names a match field. On custom objects
that must be a custom field marked as an **external ID**; on standard objects it can be any field whose `idLookup`
property is true, such as Contact or User Email.[^s2][^s5] The API surfaces always take an external ID field name:
SOAP's `upsert(externalIdFieldName, sObjects)`, REST's `PATCH /sobjects/<Object>/<field>/<value>`, and the
`externalIdFieldName` property of a Bulk API 2.0 ingest job.[^s1][^s3][^s4]

**Three outcomes per record.** Zero matches creates a record, one match updates it, and more than one match is an
error for that record, which is neither inserted nor updated.[^s1][^s5] REST answers a multiple-match upsert with an
HTTP 300 and changes nothing, and it offers an `updateOnly` parameter that turns the call into a pure update.[^s3]

**Knowing what happened.** Results report which path each record took: Apex's `Database.UpsertResult.isCreated()`,
the SOAP `UpsertResult` created flag, and the `sf__Created` column in Bulk API 2.0 successful results.[^s1][^s2][^s4]

**Setting parents by key.** An upsert can set a lookup by assigning a parent sObject that holds only the parent's
external ID, so no query for the parent's Salesforce ID is needed; the parent must already exist.[^s1]

## Limits and gotchas

- **Batch size.** A SOAP `upsert()` call accepts at most 200 records, all of the same object type.[^s1]
- **Case sensitivity.** Matching is case-sensitive unless the field is Unique and set to treat values as duplicates regardless of case.[^s1][^s2]
- **Permissions.** A unique external ID needs no extra permission; a non-unique one requires View All Data.[^s1][^s2][^s3]
- **Duplicates in one call.** If two records in the same SOAP call share an external ID value, both are marked as errors and neither is saved.[^s1]
- **Error handling in Apex.** The `upsert` statement throws a `DmlException` on failure; `Database.upsert` with `allOrNone` set to false saves valid rows and reports the rest.[^s2][^s5]
- **Sharing and FLS.** To enforce sharing and field-level security in Apex, write `upsert as user` or pass `AccessLevel.USER_MODE`.[^s2]
- **URL-encoded keys.** REST puts the key in the path, so an email key ending in a domain such as `.inc` can return 404; SOAP or a different key avoids it.[^s3]
- **No merge.** Upsert cannot be combined with `merge()`.[^s1]

## When to use it (and when not)

Use upsert when a source system owns the identity of a record and loads must be safe to re-run: nightly syncs
or migrations replayed after a fix, where the same row may arrive more than once.[^s1][^s4] Prefer plain insert
when every row is known to be new and no key exists, and plain update (or REST `updateOnly`) when creating a record
by accident would be worse than a failed row.[^s3] Upsert is not a duplicate-matching engine: it matches only on the
one key field, so fuzzy matching on names or addresses still needs duplicate rules.[^s1][^s5]

## Connections

Upsert sits under **data integration** as the idempotent write that most sync and migration patterns rely on, and it
depends on **external ID fields** to carry the source-system key.[^s1][^s2] It is reached through **SOAP API**,
**REST API** and **Bulk API 2.0**, and it is consumed by **Apex** DML; **Data Loader** exposes it as one of its core
operations.[^s1][^s3][^s4][^s5] The parent-by-key technique ties it to **object relationships**, its role in reloads
ties it to **data migration strategy** and **batch data synchronization**, and its single-key matching is the reason
**duplicate management** remains a separate concern.[^s1][^s4]

## Sources
[^s1]: Salesforce Developers, "upsert() — SOAP API Developer Guide". https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_upsert.htm (accessed 2026-11-15)
[^s2]: Salesforce Developers, "Upserting Records — Apex Developer Guide". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/langCon_apex_dml_examples_upsert.htm (accessed 2026-11-15)
[^s3]: Salesforce Developers, "Upsert Records Using sObject Rows by External ID — REST API Developer Guide". https://developer.salesforce.com/docs/platform/api-rest/guide/resources-sobject-upsert-patch.html (accessed 2026-11-15)
[^s4]: Salesforce Developers, "Step 5: Bulk Upsert — Bulk API 2.0 and Bulk API Developer Guide". https://developer.salesforce.com/docs/platform/api-asynch/guide/walkthrough-upsert.html (accessed 2026-11-15)
[^s5]: Trailhead, "Manipulate Records with DML — Apex Basics & Database". https://trailhead.salesforce.com/content/learn/modules/apex_database/apex_database_dml (accessed 2026-11-15)
