---
id: kt:polymorphic-relationships
type: Concept
title: Polymorphic Relationships
aliases: [polymorphic relationship, polymorphic fields, polymorphic lookup, polymorphic foreign key, WhoId and WhatId, Who and What fields, TYPEOF]
domain: data-model
summary: >-
  Relationship fields whose referenced record can be one of several object types — such as Owner, Who (WhoId) and
  What (WhatId) on Task and Event — queried in SOQL with the Type qualifier or a TYPEOF clause.
release: "Winter '27"
status: current
broader: [kt:object-relationships]
related: [kt:standard-objects, kt:apex, kt:graphql-api, kt:bulk-api-2]
relations:
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: contrastsWith, object: kt:lookup-vs-master-detail}
  - {predicate: coveredBy, object: kt:platform-developer-certification}
sources:
  - id: s1
    title: "Understanding Relationship Fields and Polymorphic Fields (SOQL and SOSL Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-relationships-and-polymorph-keys.html
    type: official-docs
    accessed: 2026-11-07
  - id: s2
    title: "TYPEOF (SOQL and SOSL Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-typeof.html
    type: official-docs
    accessed: 2026-11-07
  - id: s3
    title: "Working with Polymorphic Relationships in SOQL Queries (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/langCon_apex_SOQL_polymorphic_relationships.htm
    type: official-docs
    accessed: 2026-11-07
  - id: s4
    title: "Polymorphic Relationship Filters (GraphQL API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/graphql/guide/filter-polymorphic.md
    type: official-docs
    accessed: 2026-11-07
  - id: s5
    title: "Maximize Sales Productivity: Shared Activities"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/modules/sales_admin_maximize_productivity/units/sales_admin_maximize_productivity_unit_1
    type: official-learning
    accessed: 2026-11-07
created: 2026-11-07
---

# Polymorphic Relationships

A polymorphic relationship is a relationship field whose target can be one of several object types rather than a
single fixed object. Ordinary lookups point at exactly one type — `Account.OwnerId` always references a User — but a
polymorphic field such as `Event.OwnerId` can reference either a User or a Calendar.[^s1] The concept matters most to
developers and data architects who query, report on, or migrate activity and ownership data, because the code that
reads such a field cannot assume which object it will get back.

## The common polymorphic fields

Three relationship names cover most real-world cases.[^s1]

- **Owner** — on Task and Event the owner can be a User or a Calendar.[^s1]
- **Who** (API field `WhoId`, UI label *Name*) — the person an activity is about, typically a Lead or a Contact.
- **What** (API field `WhatId`, UI label *Related To*) — the non-person record an activity is about, such as an
  Account, an Opportunity, a Campaign or a Solution.

In SOQL you traverse these through the relationship name (`Who`, `What`, `Owner`), not the `Id` field name, exactly as
with a normal parent lookup.[^s1] Shared Activities widens the person side of the model: once an admin enables it, a
single task or event can be related to up to 50 contacts, one of which is the primary contact, and the setting can
only be turned off through Salesforce Support.[^s5]

## How to tell a field is polymorphic

A `describeSObjects()` call exposes the metadata. A field is a relationship field when its `relationshipName` is not
null; it is polymorphic when `namePointing` and `polymorphicForeignKey` are both true and `referenceTo` lists more
than one object type. `referenceTo` is also how you discover every type the field may hold.[^s1] From API 46.0 on,
the Enterprise and Tooling WSDLs type polymorphic fields as `sObject` instead of the older `Name` type, which changes
generated client code such as Java stubs.[^s1]

## Querying: Type and TYPEOF

Two SOQL tools handle the "which object is it?" problem.[^s1][^s2]

- **The `Type` qualifier** returns the referenced object's type as a string (`Who.Type`) and can filter in `WHERE`,
  for example `WHERE What.Type IN ('Account', 'Opportunity')`. Because it is a string, operators such as `=` and
  `LIKE` work.[^s1]
- **`TYPEOF`** picks different fields per type inside `SELECT`: `TYPEOF What WHEN Account THEN Phone WHEN
  Opportunity THEN Amount ELSE Name END`. Any number of `WHEN` branches is allowed and one `SELECT` may hold several
  `TYPEOF` expressions. Without an `ELSE`, unmatched types return null; when a `WHERE ... Type IN` filter already
  limits the types, an `ELSE` is ignored at run time. `TYPEOF` has been generally available since API 46.0.

In Apex, the same queries run inline, and code then branches with `instanceof` (for example
`myEvent.What instanceof Account`) and assigns the value to a variable of the concrete type before passing it to
another method.[^s3] The GraphQL API models each polymorphic field as a union type with one member per concrete
object, read with `... on User` inline fragments and filtered through per-type filter inputs; it supports these
fields from API 56.0, with Event and Task added (as beta) in 59.0, and only objects exposed through UI API appear as
possible types.[^s4]

## Limits and gotchas

`TYPEOF` is narrower than ordinary SOQL. Verified against the Winter '27 reference, it:[^s2]

- works only in the `SELECT` clause, and only on fields whose `namePointing` and `relationshipName` qualify;[^s2]
- is not allowed with `COUNT()` or other queries that don't return objects, nor with `GROUP BY`, `ROLLUP`, `CUBE`
  or `HAVING`, nor alongside functions such as `FORMAT` in `SELECT`;
- cannot be nested, cannot appear inside a semi-join subquery's `SELECT` (the outer query is fine), and cannot be
  used in Bulk API queries or Streaming API PushTopic queries.

The documented workaround for the function restriction is a two-step query: fetch IDs with `TYPEOF`, then run the
function query filtered on those IDs.[^s2] Because `ELSE` field lists may only use fields
valid on the generic `Name` type, rich per-object fields must come from explicit `WHEN` branches.[^s2]

## Connections

Polymorphic relationships are a special case of **object relationships** and contrast with the single-target
**lookup vs. master-detail** fields admins create: both traverse parents the same way in **SOQL**, but only
polymorphic fields need `Type` or `TYPEOF` handling.[^s1] They live mainly on **standard objects** — Task, Event and
the Owner field — so activity reporting and migration designs revolve around them.[^s1][^s5] **Apex** code consumes
them with `instanceof` checks,[^s3] the **GraphQL API** exposes them as unions,[^s4] and because `TYPEOF` is
unsupported in Bulk API queries such as those run through **Bulk API 2.0**, large extracts have to filter by `Type` instead.[^s2] Querying them
correctly is part of the **Platform Developer certification** skill set.

## Sources

[^s1]: Salesforce Developers, "Understanding Relationship Fields and Polymorphic Fields". https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-relationships-and-polymorph-keys.html (accessed 2026-11-07)
[^s2]: Salesforce Developers, "TYPEOF". https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-typeof.html (accessed 2026-11-07)
[^s3]: Salesforce Developers, "Working with Polymorphic Relationships in SOQL Queries". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/langCon_apex_SOQL_polymorphic_relationships.htm (accessed 2026-11-07)
[^s4]: Salesforce Developers, "Polymorphic Relationship Filters". https://developer.salesforce.com/docs/platform/graphql/guide/filter-polymorphic.md (accessed 2026-11-07)
[^s5]: Trailhead, "Maximize Sales Productivity: Shared Activities". https://trailhead.salesforce.com/modules/sales_admin_maximize_productivity/units/sales_admin_maximize_productivity_unit_1 (accessed 2026-11-07)
