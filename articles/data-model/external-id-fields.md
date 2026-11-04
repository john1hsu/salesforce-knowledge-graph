---
id: kt:external-id-fields
type: Feature
title: External ID Fields
aliases: [external ID, external id field, External ID attribute, externalIdFieldName]
domain: data-model
summary: >-
  A custom text, number or email field flagged with the External ID attribute so it holds a record's key from another
  system, is indexed, and can be used to match records in upserts and to set relationships without Salesforce IDs.
release: "Winter '27"
status: current
broader: [kt:custom-fields, kt:data-integration]
related: [kt:data-migration-strategy, kt:bulk-api-2, kt:composite-api, kt:object-relationships, kt:large-data-volumes]
relations:
  - {predicate: queriedWith, object: kt:rest-api}
  - {predicate: queriedWith, object: kt:soap-api}
  - {predicate: governedBy, object: kt:custom-index-limits}
  - {predicate: enables, object: kt:upsert}
  - {predicate: coveredBy, object: kt:platform-data-architect-certification}
sources:
  - id: s1
    title: "How Many External ID Fields Can I Create Per Object in Salesforce"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewSolution?id=000005081
    type: official-docs
    accessed: 2026-11-04
  - id: s2
    title: "upsert() — SOAP API Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_upsert.htm
    type: official-docs
    accessed: 2026-11-04
  - id: s3
    title: "Insert or Update (Upsert) a Record Using an External ID — REST API Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-rest/guide/dome-upsert.html
    type: official-docs
    accessed: 2026-11-04
  - id: s4
    title: "Custom Fields — Object Reference for the Salesforce Platform (API 68.0)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/custom_fields.htm
    type: official-docs
    accessed: 2026-11-04
created: 2026-11-04
---

# External ID Fields

An external ID field is a custom field marked with the **External ID** attribute so that it stores the identifier a
record has in some system outside Salesforce, such as an ERP customer number or a billing account key. The attribute
can be set on custom text, number or email fields only, and it is available in all editions.[^s1][^s4] Once flagged,
the field becomes a matching key: integrations and data loads can find "the same" record by its source-system key
instead of first looking up the 15/18-character Salesforce record ID.[^s1][^s2]

## How it works

**Indexing.** External ID fields are indexed automatically, so selective query filters on them run fast. That makes
them a cheap way to get an index on a key you will filter by often, without asking Support for a custom index.[^s1]

**Upsert matching.** The upsert operation (insert-or-update) takes the name of an external ID field. For custom
objects it matches on a field that has the External ID attribute; for standard objects it can also match on fields
with the `idLookup` property, which is usually, but not always, the ID or name field.[^s2] The outcome depends on
how many records match the incoming value: none creates a new record, one updates it, and several produce an error
instead of a guess.[^s2] The REST API exposes the same logic as a `PATCH` to
`/sobjects/{Object}/{ExternalIdField}/{value}`; since API 46.0 it answers 201 with `created: true` on insert, 200 with
`created: false` on update, and 300 with the list of candidates when the value matches more than one record. Adding
`updateOnly=true` turns the call into update-only.[^s3]

**Relationships without IDs.** An external ID can stand in for a foreign key. In SOAP you set the relationship field
to an sObject that carries only the parent's external ID; in REST you nest the relationship name (for example
`Merchandise__r`) with the parent's external ID field and value. The parent must already exist when you upsert this
way.[^s2][^s3] This is what lets a migration load parents and children from the source system's keys in two passes
without a lookup-and-replace step in between.

## Limits and gotchas

- **Per-object allocation.** The default is 25 external ID fields per object, raised only through a Support case;
  because they are indexed, they draw on the same default of 25 custom indexes per object.[^s1]
- **Uniqueness and case.** External ID does not imply Unique. Matching is case-insensitive only when the field is
  also Unique and set to treat "ABC" and "abc" as duplicates; otherwise it is case-sensitive, so review existing
  values before switching.[^s2] The `unique` and `caseSensitive` attributes cannot be changed through data API
  calls.[^s4]
- **Permissions.** Upserting on a non-unique external ID requires the View All Data permission; a unique one needs
  nothing special.[^s2]
- **Duplicates in one batch.** If two records in the same SOAP call share an external ID value, all of them fail and
  none is created; a SOAP upsert also accepts at most 200 records of one object type.[^s2]
- **Not for merge.** External IDs cannot be used to identify records in the merge call.[^s2]
- **Master-detail.** Pointing an existing child at a different parent through an external ID fails with
  `INVALID_FIELD_FOR_INSERT_UPDATE` when the master-detail relationship does not allow reparenting.[^s3]

## When to use it (and when not)

Add an external ID to every object that is loaded or synchronized from another system: it makes reruns idempotent
(an upsert retried after a partial failure updates instead of duplicating) and removes the need to keep a mapping
table of Salesforce IDs.[^s1][^s2] Make it Unique unless the source genuinely allows repeats, both to avoid the
multiple-match error and the View All Data requirement.[^s2] Don't flag fields as external IDs merely to index
them if they will never be used for matching: each one consumes the shared index allocation.[^s1] For records that
originate in Salesforce and are only read elsewhere, the Salesforce ID is usually the better key.

## Connections

External ID is an attribute of `kt:custom-fields` and a building block of `kt:data-integration`. It is the
matching key behind the `kt:upsert` operation exposed by the `kt:soap-api`, the `kt:rest-api`, `kt:bulk-api-2`
and `kt:composite-api` requests,[^s2][^s3] and the main technique in `kt:data-migration-strategy` for loading
related records via `kt:object-relationships` without pre-fetching parent IDs.[^s2] Because each external ID is
indexed, it counts against `kt:custom-index-limits` and matters in `kt:large-data-volumes` designs, where
selective filters depend on indexed fields.[^s1] In the graph it is linked as **covered by** the Platform Data
Architect certification (`kt:platform-data-architect-certification`).

## Sources
[^s1]: Salesforce Help, "How Many External ID Fields Can I Create Per Object in Salesforce". https://help.salesforce.com/apex/HTViewSolution?id=000005081 (accessed 2026-11-04)
[^s2]: Salesforce Developers, "upsert()", SOAP API Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_upsert.htm (accessed 2026-11-04)
[^s3]: Salesforce Developers, "Insert or Update (Upsert) a Record Using an External ID", REST API Developer Guide. https://developer.salesforce.com/docs/platform/api-rest/guide/dome-upsert.html (accessed 2026-11-04)
[^s4]: Salesforce Developers, "Custom Fields", Object Reference for the Salesforce Platform (API 68.0). https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/custom_fields.htm (accessed 2026-11-04)
