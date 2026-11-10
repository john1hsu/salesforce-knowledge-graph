---
id: kt:custom-index-limits
type: Limit
title: Custom Index Limits
aliases: [custom index allocation, maximum custom indexes per object, external ID field limit, external IDs per object limit, index limits]
domain: platform-architecture
summary: >-
  The caps and eligibility rules that bound Salesforce custom indexes: by default 25 custom indexes and 25 External ID
  fields per object (raisable through Salesforce Support), a set of field types that can never be indexed, and the
  separate, fixed index rules for custom big objects.
release: "Winter '27"
status: current
broader: [kt:governor-limits, kt:custom-indexes]
related: [kt:external-id-fields, kt:query-optimizer-selectivity, kt:large-data-volumes, kt:big-objects, kt:formula-fields]
relations:
  - {predicate: contrastsWith, object: kt:data-and-file-storage-allocations}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: dependsOn, object: kt:multitenancy}
sources:
  - id: s1
    title: "How Many External ID Fields Can I Create Per Object in Salesforce"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewSolution?id=000005081
    type: official-docs
    accessed: 2026-11-10
  - id: s2
    title: "Best Practices for Deployments with Large Data Volumes: Indexes"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-infrastructure-indexes.html
    type: official-docs
    accessed: 2026-11-10
  - id: s3
    title: "Best Practices for Deployments with Large Data Volumes (PDF)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/256/latest/en-us/sfdc/pdf/salesforce_large_data_volumes_bp.pdf
    type: official-docs
    accessed: 2026-11-10
  - id: s4
    title: "Metadata API Developer Guide: CustomIndex"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_customindex.htm
    type: official-docs
    accessed: 2026-11-10
  - id: s5
    title: "Big Objects Implementation Guide: Define and Deploy Custom Big Objects"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.bigobjects.meta/bigobjects/big_object_define.htm
    type: official-docs
    accessed: 2026-11-10
created: 2026-11-10
---

# Custom Index Limits

**Custom index limits** are the per-object caps and eligibility rules that decide how many extra database indexes an
org can have and which fields may carry one. They matter whenever a data architect plans indexes for a large object,
because the cap is shared between indexes requested from Salesforce Support and the indexes that are created
automatically whenever a field is marked as an External ID.[^s1] This node covers the allocation itself; how indexes are
built and used is described under **custom indexes**, and when the optimizer actually picks one is described under
**query optimizer selectivity**.

## The per-object allocation

Salesforce Help states that, by default, an entity can have at most 25 custom indexes, and separately that an object
can have at most 25 External ID fields.[^s1] The two numbers are linked: designating a field as an External ID also
indexes it, so every External ID consumes index capacity on that object.[^s1][^s2] The default is not a hard ceiling.
To exceed 25, a System Administrator logs a case with Salesforce Support giving the Organization ID, the object and
the business justification.[^s1]

Because External IDs are the only self-service way to get an index, and they are allowed only on Auto Number, Email,
Number and Text fields, the allocation is easy to spend by accident: integration teams often add an External ID per
source system, each one quietly taking an index slot that a later performance fix might need.[^s2][^s3] Any other field
type, including standard fields, needs Support to create the index, or a `CustomIndex` component deployed through the
Metadata API.[^s3] The `CustomIndex` type exists from API version 50.0, and its documentation still directs admins to
contact Salesforce Customer Support before creating one, so the request path, rather than the metadata file, is the
real control point.[^s4]

## Fields that cannot be indexed

Some fields can never receive a custom index, regardless of allocation. The large data volumes guide lists
multi-select picklists, long text area, rich text area and encrypted text fields, binary fields, and currency fields in
multicurrency orgs.[^s3] Non-deterministic formula fields are also excluded: formulas that reference other objects,
use dynamic date functions such as TODAY or NOW, or depend on owner, autonumber, division or most audit fields
(CreatedDate and CreatedById being the exceptions).[^s3] Changing the definition of an indexed formula triggers an
index rebuild.[^s3]

Nulls are a further limit on usefulness. Index tables leave out empty values by default; Support can create
null-inclusive indexes, but an existing index must be explicitly enabled and rebuilt.[^s2] A two-column index follows
the same restrictions as a single-column one, except that its second column may contain nulls.[^s2][^s3]

## An index is not a guarantee

Holding an index does not mean queries use it. The index table caps how many records an indexed search can usefully
return, and the optimizer applies stricter thresholds to custom indexes than to standard ones.[^s2] The current guide
gives the custom-index threshold as under 10% of the first million records and under 5% of the rest, against 30% and
15% for standard indexes.[^s2] Spending an index slot on a field whose typical filter is not selective therefore
consumes allocation for no gain.

## Big object indexes

Custom big objects follow a different, stricter rule set. Every big object index field must be required, long text
area and URL fields are not allowed, and text fields in the index may total no more than 100 characters, with Email
counted as 80 and Phone as 40; Support can raise that length limit.[^s5] Once deployed, a big object index cannot be
edited or deleted, so changing it means building a new big object.[^s5]

## Practical guidance

- Inventory indexes and External IDs on hot objects before adding integration keys, so slots stay free for tuning.[^s1]
- Reuse one External ID per external system where possible, rather than a key per integration flow.[^s1][^s2]
- Prefer cross-object filters on an already indexed field over an unindexable formula that reaches across lookups.[^s3]
- For big objects, fix the index design before deployment, because it can never be changed afterwards.[^s5]

## Connections

These limits are one of the platform's **governor limits** and constrain the **custom indexes** feature, whose index
tables exist because of the shared-table design of **multitenancy**.[^s2] They are spent by **external ID fields**, and
they only pay off when filters pass the thresholds in **query optimizer selectivity**.[^s1][^s2] Index components can
be deployed through the **Metadata API**.[^s4] They are a planning input for **large data volumes**, sit alongside the
fixed index rules for **big objects**, and exclude many **formula fields**.[^s3][^s5] Unlike **data and file storage
allocations**, which measure capacity consumed by records, index limits count structures per object.[^s1]

## Sources
[^s1]: Salesforce Help, "How Many External ID Fields Can I Create Per Object in Salesforce". https://help.salesforce.com/apex/HTViewSolution?id=000005081 (accessed 2026-11-10)
[^s2]: Salesforce Developers, "Best Practices for Deployments with Large Data Volumes: Indexes". https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-infrastructure-indexes.html (accessed 2026-11-10)
[^s3]: Salesforce, "Best Practices for Deployments with Large Data Volumes (PDF)". https://resources.docs.salesforce.com/256/latest/en-us/sfdc/pdf/salesforce_large_data_volumes_bp.pdf (accessed 2026-11-10)
[^s4]: Salesforce Developers, "Metadata API Developer Guide: CustomIndex". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_customindex.htm (accessed 2026-11-10)
[^s5]: Salesforce Developers, "Big Objects Implementation Guide: Define and Deploy Custom Big Objects". https://developer.salesforce.com/docs/atlas.en-us.bigobjects.meta/bigobjects/big_object_define.htm (accessed 2026-11-10)
