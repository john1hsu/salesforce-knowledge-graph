---
id: kt:object-relationships
type: Concept
title: Object Relationships
aliases: [salesforce relationship types, relationship fields, object relationship types, data model relationships]
domain: data-model
summary: >-
  The family of relationship field types that connect Salesforce objects (lookup, master-detail, many-to-many via a
  junction object, hierarchical, and the external and indirect lookups used with external objects) and that define how
  records reference, depend on, and are queried through one another.
release: "Winter '27"
status: current
broader: [kt:data-architecture]
related: [kt:salesforce-sharing-model, kt:external-objects]
relations:
  - {predicate: hasPart, object: kt:lookup-vs-master-detail}
  - {predicate: hasPart, object: kt:junction-object}
  - {predicate: enables, object: kt:roll-up-summary-field}
  - {predicate: queriedWith, object: kt:soql}
sources:
  - id: s1
    title: "Object Reference: Relationships Among Standard Objects and Fields"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/relationships_among_objects.htm
    type: official-docs
    accessed: 2026-11-02
  - id: s2
    title: "Data Modeling: Create Object Relationships (unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/modules/data_modeling/units/object_relationships
    type: official-learning
    accessed: 2026-11-02
  - id: s3
    title: "Understanding Relationship Names, Custom Objects, and Custom Fields"
    publisher: Salesforce Developers (SOQL and SOSL Reference)
    url: https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-relationships-and-custom-objects.html
    type: official-docs
    accessed: 2026-11-02
  - id: s4
    title: "Understanding Relationship Query Limitations"
    publisher: Salesforce Developers (SOQL and SOSL Reference)
    url: https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_relationships_query_limits.htm
    type: official-docs
    accessed: 2026-11-02
  - id: s5
    title: "Salesforce Platform App Builder Certification Handbook — External lookups"
    publisher: Packt (via O'Reilly)
    url: https://www.oreilly.com/library/view/salesforce-platform-app/9781785283697/ch02s04.html
    type: textbook
    accessed: 2026-11-02
created: 2026-11-02
---

# Object Relationships

Object relationships are the field types that tie one Salesforce object to another. A relationship field stored on one
object points at a record of another, which is what lets an account show its contacts, a property show its offers, or a
user point at a manager. The platform offers a small, fixed menu of relationship kinds, and each one carries different
consequences for deletion, ownership, security, reporting and querying, so choosing among them is one of the earliest
and least reversible data-model decisions.[^s1][^s2]

## The relationship types

- **Lookup** — a loosely coupled one-to-one or one-to-many link. It does not affect deletion or record security, and the
  field is not required unless you make it so; use it when the two objects are only sometimes related and each can stand
  on its own with its own tab.[^s1][^s2]
- **Master-detail** — a tightly coupled parent-child link in which the master controls behaviours of the detail, such as
  who can see it, and deleting the master deletes its details. The field always lives on the detail object.[^s1][^s2]
- **Many-to-many** — not a separate field type but a pattern: a custom junction object holding two master-detail fields,
  one to each related object. For Task and Event, API version 34.0 added the JunctionIdList field type so the many-to-many
  link can be managed without touching junction records directly; such fields are read-only in Apex.[^s1]
- **Hierarchical** — a special lookup that exists only on the User object, used to model chains of users such as
  manager relationships.[^s2]
- **External lookup and indirect lookup** — the extra kinds offered for external objects, alongside standard lookup.[^s1]
  An external lookup links to an external object whose data lives outside Salesforce; an indirect lookup lets an external
  object act as the child of a standard or custom object, matching on a unique external ID field on the parent rather
  than on Salesforce record IDs — for example, showing ERP sales orders in an account's related list.[^s5]

## How relationships surface in queries

Every relationship has a name that SOQL uses to traverse it. For custom relationships the API name ends in `__r`
instead of `__c`, and the child relationship name defaults to the plural of the child object. Child-to-parent traversal
uses dot notation in the field list and `WHERE` clause, while parent-to-child traversal uses a nested subquery on the
child relationship name.[^s3]

## Limits and gotchas

Relationship queries carry their own ceilings, checked for Winter '27. A single query may name at most 55 child-to-parent
relationships and at most 20 parent-to-child relationships; a custom object can have up to 40 relationships, so all of
them fit in one query. Child-to-parent paths can go up to five levels deep. Parent-to-child nesting was limited to two
levels in API version 57.0 and earlier and is five levels from API version 58.0 on via REST, SOAP and Apex — but not for
big objects, external objects, Bulk API or Bulk API 2.0. Each type named in a polymorphic `TYPEOF` clause counts against
the relationship limit, while reusing the same relationship in one query counts only once.[^s4]

Master-detail has structural restrictions worth knowing before modelling: a standard object cannot be the detail side
when the master is a custom object; several standard objects (including Lead, Product2, PriceBook2 and User) cannot be
masters; detail records lack their own owner; and reparenting is blocked unless the relationship's reparenting option
is enabled. Custom detail objects also cannot use sharing rules, manual sharing or queues.[^s1] Trailhead also cautions
that each relationship adds complexity, so changing or deleting related objects, records or fields needs care.[^s2]

## Choosing a relationship

Start from dependency: if a child record is meaningless without its parent, master-detail fits; if the link is
optional or the objects need independent security, use lookup; reserve hierarchical for user-to-user chains; and use
a junction object when each side can relate to many records on the other.[^s2][^s1] When the data stays in an external
system, the choice narrows to lookup, external lookup or indirect lookup, depending on whether the keys are Salesforce
IDs, external-object IDs or a parent's external ID field.[^s1][^s5]

## Connections

This node is the umbrella for the graph's data-model articles. It **has parts** `kt:lookup-vs-master-detail`, which
compares the two core one-to-many field types in depth, and `kt:junction-object`, the many-to-many pattern.[^s1]
Master-detail **enables** `kt:roll-up-summary-field` aggregation, and relationships are **queried with** `kt:soql`
through relationship names and nested subqueries.[^s3][^s4] It is **related** to `kt:salesforce-sharing-model`, because a
master-detail child inherits its master's access, and to `kt:external-objects`, which rely on external and indirect
lookups.[^s1] It sits **under** `kt:data-architecture`, where relationship choices shape volumes, skew and integration
keys.[^s2]

## Sources

[^s1]: Salesforce Developers, "Object Reference: Relationships Among Standard Objects and Fields". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/relationships_among_objects.htm (accessed 2026-11-02)
[^s2]: Trailhead, "Data Modeling: Create Object Relationships". https://trailhead.salesforce.com/en/modules/data_modeling/units/object_relationships (accessed 2026-11-02)
[^s3]: Salesforce Developers, "Understanding Relationship Names, Custom Objects, and Custom Fields". https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-relationships-and-custom-objects.html (accessed 2026-11-02)
[^s4]: Salesforce Developers, "Understanding Relationship Query Limitations". https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_relationships_query_limits.htm (accessed 2026-11-02)
[^s5]: Packt via O'Reilly, "Salesforce Platform App Builder Certification Handbook — External lookups". https://www.oreilly.com/library/view/salesforce-platform-app/9781785283697/ch02s04.html (accessed 2026-11-02)
