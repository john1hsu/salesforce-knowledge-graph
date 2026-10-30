---
id: kt:lookup-vs-master-detail
type: Concept
title: Lookup vs. Master-Detail Relationships
aliases: [lookup relationship, master-detail relationship, lookup field vs master-detail field, parent-child relationship types]
domain: data-model
summary: >-
  The two core one-to-many relationship field types on the Salesforce platform: a loosely coupled lookup that leaves
  deletion and security independent, and a tightly coupled master-detail in which the parent controls the child's
  ownership, sharing and deletion and can roll up its values.
release: "Winter '27"
status: current
broader: [kt:object-relationships]
related: [kt:junction-object, kt:salesforce-sharing-model, kt:record-locking]
relations:
  - {predicate: enables, object: kt:roll-up-summary-field}
  - {predicate: causes, object: kt:data-skew}
sources:
  - id: s1
    title: "Data Modeling: Create Object Relationships"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data_modeling/object_relationships
    type: official-learning
    accessed: 2026-10-30
  - id: s2
    title: "Object Reference: Relationships Among Standard Objects and Fields"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/relationships_among_objects.htm
    type: official-docs
    accessed: 2026-10-30
  - id: s3
    title: "Considerations for Object Relationships"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=relationships_considerations.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-10-30
  - id: s4
    title: "Roll-Up Summary Field"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.fields_about_roll_up_summary_fields.htm&type=5
    type: official-docs
    accessed: 2026-10-30
  - id: s5
    title: "Effects of Converting a Salesforce Master-Detail Relationship to a Lookup Relationship"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000385143&language=en_US&type=1
    type: official-docs
    accessed: 2026-10-30
  - id: s6
    title: "Managing Lookup Skew in Salesforce to Avoid Record Lock Exceptions"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/engineering/2013/04/managing-lookup-skew-to-avoid-record-lock-exceptions
    type: official-blog
    accessed: 2026-10-30
created: 2026-10-30
---

# Lookup vs. Master-Detail Relationships

Lookup and master-detail are the two relationship field types a Salesforce admin chooses between when linking one object to another in a one-to-many way. A lookup simply links two objects so that related records can be reached from either side; a master-detail is a tighter bond in which the parent (master) governs certain behaviours of the child (detail), and the detail is not meant to exist on its own.[^s1] In both cases the relationship field lives on the child (many) side; for master-detail it is always created on the detail object.[^s1]

## How each behaves

**Lookup.** A lookup links two objects but by default affects neither deletion nor security, and the field is not automatically required.[^s2] When the referenced record is deleted, an optional lookup offers three behaviours: clear the value (the default), refuse deletion while the link exists, or cascade-delete the child. Cascade delete is limited to custom lookups on custom objects, is disabled unless Salesforce turns it on for the org, and bypasses sharing and security when it runs.[^s3] A hierarchical relationship is a special lookup available only on the User object, used for chains such as a user's manager.[^s1]

**Master-detail.** Deleting a master record deletes its detail records too.[^s1] The detail has no Owner field of its own: ownership comes from the master, and the detail inherits the master's sharing and security settings. Custom detail objects therefore cannot use sharing rules, manual sharing or queues, and the relationship field is required on the detail page layout.[^s2] Child records cannot be reparented unless an admin enables the "Allow reparenting" option.[^s3] Only master-detail parents support roll-up summary fields, which compute COUNT, SUM, MIN or MAX across detail records on the master.[^s4]

## Limits and gotchas

Limits verified against Winter '27 documentation:[^s3]

- A custom object can have at most 2 master-detail relationships, plus many lookups; every relationship field counts toward the object's custom field allocation.[^s3]
- Multilevel master-detail chains support up to 3 custom detail levels, and an object can appear only once in such a chain.[^s3]
- Standard objects cannot be the detail side of a custom object, and a custom junction object cannot itself be the master of another master-detail relationship.[^s3]
- Salesforce recommends no more than 10,000 detail records per master record.[^s3]
- You cannot add a master-detail field to a custom object that already has data; create a lookup, populate it on every record, then convert.[^s3]

Some standard objects, including Lead, User, Product2 and BusinessHours, cannot be on the master side at all.[^s2] Roll-ups reach only one level: a master cannot summarise subdetail records directly, so the intermediate detail needs its own roll-up field.[^s3]

Conversions are where projects get hurt. Converting master-detail to lookup is blocked while the master has roll-up summary fields that reference the detail, so those must be deleted first.[^s4][^s5] Afterwards deletion no longer cascades, the child needs its own security model, and reports built on the old relationship's report type turn obsolete.[^s5] Converting lookup to master-detail requires a value in every record's lookup field and switches the child's org-wide default to Controlled by Parent.[^s3]

Locking is the performance trap. Each insert or update locks the record referenced by every lookup field for the length of the save, so when huge numbers of children point at one parent ("lookup skew") concurrent loads and long-running triggers collide in record-lock errors. Salesforce's engineering guidance is to shorten save time, spread children across more parents, use a picklist when the parent carries no data, and serialise bulk jobs.[^s6]

## When to use which

Choose master-detail when the child has no meaning without its parent, should share the parent's security, and you need declarative roll-ups; choose a lookup when the relationship is optional, the child needs its own owner and sharing, or the parent is a standard object that cannot be a master.[^s1][^s2] A many-to-many relationship is modelled with a custom junction object carrying two master-detail fields; the first one created is primary and supplies the junction record's owner.[^s2][^s3] Access to a junction record then depends on access to both masters.[^s3]

## Connections

Both types are kinds of **object relationship**, the broader concept.[^s1] Master-detail is what **enables** the **roll-up summary field**[^s4] and is the building block of the **junction object**.[^s2] The choice is effectively a **sharing model** decision, because master-detail detail records inherit access from the parent while lookups keep it independent.[^s2] Heavy fan-in to one parent **causes** **data skew** and **record locking** contention, which is why shorter saves (fewer triggers and workflow rules, more asynchronous work) are the first mitigation.[^s6]

## Sources

[^s1]: Trailhead, "Data Modeling: Create Object Relationships". https://trailhead.salesforce.com/content/learn/modules/data_modeling/object_relationships (accessed 2026-10-30)
[^s2]: Salesforce Developers, "Object Reference: Relationships Among Standard Objects and Fields". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/relationships_among_objects.htm (accessed 2026-10-30)
[^s3]: Salesforce Help, "Considerations for Object Relationships". https://help.salesforce.com/s/articleView?id=relationships_considerations.htm&language=en_US&type=5 (accessed 2026-10-30)
[^s4]: Salesforce Help, "Roll-Up Summary Field". https://help.salesforce.com/s/articleView?language=en_US&id=platform.fields_about_roll_up_summary_fields.htm&type=5 (accessed 2026-10-30)
[^s5]: Salesforce Help, "Effects of Converting a Salesforce Master-Detail Relationship to a Lookup Relationship". https://help.salesforce.com/s/articleView?id=000385143&language=en_US&type=1 (accessed 2026-10-30)
[^s6]: Salesforce Developers Blog, "Managing Lookup Skew in Salesforce to Avoid Record Lock Exceptions". https://developer.salesforce.com/blogs/engineering/2013/04/managing-lookup-skew-to-avoid-record-lock-exceptions (accessed 2026-10-30)
