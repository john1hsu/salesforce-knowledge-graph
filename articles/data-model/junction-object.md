---
id: kt:junction-object
type: Pattern
title: Junction Object
aliases: [junction objects, many-to-many relationship, many-to-many object relationship, linking object, association object]
domain: data-model
summary: >-
  A custom object with two master-detail relationship fields, used on the Salesforce platform to model a many-to-many
  relationship between two objects; each junction record represents one pairing of a record from each master.
release: "Winter '27"
status: current
broader: [kt:object-relationships]
related: [kt:salesforce-sharing-model, kt:data-skew, kt:apex-triggers]
relations:
  - {predicate: dependsOn, object: kt:lookup-vs-master-detail}
  - {predicate: enables, object: kt:roll-up-summary-field}
sources:
  - id: s1
    title: "Create a Many-to-Many Object Relationship"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.relationships_manytomany.htm&type=5
    type: official-docs
    accessed: 2026-11-01
  - id: s2
    title: "Considerations for Object Relationships"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.relationships_considerations.htm&type=5
    type: official-docs
    accessed: 2026-11-01
  - id: s3
    title: "Relationships Among Standard Objects and Fields"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/relationships_among_objects.htm
    type: official-docs
    accessed: 2026-11-01
  - id: s4
    title: "Build a Data Model for a Recruiting App: Create a Junction Object for Job Postings"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/build-a-data-model-for-a-recruiting-app/junction-object-job-postings
    type: official-learning
    accessed: 2026-11-01
  - id: s5
    title: "How Salesforce Uses Junction Objects to Enrich Reporting"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2022/how-salesforce-uses-junction-objects-to-enrich-reporting
    type: official-blog
    accessed: 2026-11-01
created: 2026-11-01
---

# Junction Object

A **junction object** is the standard Salesforce pattern for a many-to-many relationship: a custom object that carries two master-detail relationship fields, one pointing at each of the objects being linked.[^s1] Every junction record stands for exactly one pairing. In the Trailhead recruiting example, a Job Posting links one Position to one Job Posting Site; because each posting is many-to-one with both parents, Positions and Sites end up many-to-many with each other.[^s4] The object reference describes the same structure, noting that custom objects with two master-detail relationships have been supported since API version 11.0.[^s3]

## How it works

Building one takes a few declarative steps: create the custom object (Salesforce suggests naming it for the association, such as BugCaseAssociation, with an auto-number record name and no tab), add the first master-detail field, add the second, then relabel and customise the related list each master shows.[^s1] The order matters. The first master-detail field becomes the **primary** relationship and the second the **secondary**; if the primary is deleted or converted to a lookup, the secondary is promoted.[^s1][^s2] The primary master supplies the junction object's page colour and icon, and junction records inherit the primary master record's owner and, where divisions are used, its division.[^s1][^s2]

Security is derived from both parents. Whether a user can see or edit a junction record depends on their access to both master records combined with the sharing setting on each master-detail field; with Read/Write sharing settings on both, editing a junction record needs Read/Write on both masters.[^s2] Because junction records sit on the detail side, they have no visible owner and cannot use sharing rules, manual sharing or queues.[^s3]

The junction is a full-featured object: roll-up summary fields can be defined on both masters, formula fields and validation rules can reference fields on either master, and Apex triggers can run on the masters and the junction itself.[^s2] For reporting, Salesforce provides two standard report types, primary-with-junction-and-secondary and the reverse, and the master named first sets the scope of records the report can show.[^s1][^s2] A related pattern exists for activities: from API version 34.0, the JunctionIdList field on Task and Event lets code manage the many-to-many links without touching junction records directly, though these fields are read-only in Apex.[^s3]

## Limits and gotchas

These rules were checked against Help for Winter '27:[^s2]

- A custom object can have at most 2 master-detail relationships, so a junction object uses up its whole allowance.
- A custom junction object cannot itself be the master of another master-detail relationship, so it cannot have detail objects.
- A many-to-many self-relationship is not allowed; the two master-detail fields cannot point at the same master object.
- When either master record is deleted, its junction records are deleted to the Recycle Bin; when both masters are deleted, the junction record is removed permanently.
- A parent with more than 200 junction records cannot be deleted while the junction has a roll-up summary field rolling up to the other parent; junction records must be deleted first.
- As a best practice, keep a master-detail relationship under 10,000 child records, and note that a master-detail field cannot be added to an object that already holds data unless you start with a populated lookup and convert it.
- Standard objects cannot be the detail side of a custom object, and some standard objects, including Lead, Product2 and User, cannot be the master.[^s3]

## When to use it (and when not)

Use a junction object when both sides of the relationship are independent records, when the link itself carries attributes (dates, status, roles), or when you need to report in both directions. Salesforce's own Admin Relations team replaced an ever-growing topic picklist with a Topic object and a Content Topic junction so topics could be added without deployments and reported on from either side.[^s5] If the linking records need their own owner and sharing, lookup fields are the looser option: lookups leave deletion and security independent, so you give up inherited access, cascade deletion and declarative roll-ups to the parents.[^s2][^s3] A single master that accumulates a very large number of junction children works against the 10,000-child guidance, so design high-volume links with that ceiling in mind.[^s2]

## Connections

The junction object is a specialisation of **object relationships** and **depends on** the master-detail side of the **lookup vs. master-detail** choice, since it is literally two master-detail fields on one custom object.[^s1] Master-detail is what **enables** **roll-up summary fields** on both parents.[^s2] Access to junction records is an application of the **Salesforce sharing model**, inherited from both masters rather than granted directly.[^s2][^s3] Large fan-in to a single master links it to **data skew**, and the ability to put **Apex triggers** on both masters and the junction makes it a common place for cross-object automation.[^s2]

## Sources

[^s1]: Salesforce Help, "Create a Many-to-Many Object Relationship". https://help.salesforce.com/s/articleView?language=en_US&id=sf.relationships_manytomany.htm&type=5 (accessed 2026-11-01)
[^s2]: Salesforce Help, "Considerations for Object Relationships". https://help.salesforce.com/s/articleView?language=en_US&id=sf.relationships_considerations.htm&type=5 (accessed 2026-11-01)
[^s3]: Salesforce Developers, "Relationships Among Standard Objects and Fields". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/relationships_among_objects.htm (accessed 2026-11-01)
[^s4]: Trailhead, "Build a Data Model for a Recruiting App: Create a Junction Object for Job Postings". https://trailhead.salesforce.com/content/learn/projects/build-a-data-model-for-a-recruiting-app/junction-object-job-postings (accessed 2026-11-01)
[^s5]: Salesforce Admins Blog, "How Salesforce Uses Junction Objects to Enrich Reporting". https://admin.salesforce.com/blog/2022/how-salesforce-uses-junction-objects-to-enrich-reporting (accessed 2026-11-01)
