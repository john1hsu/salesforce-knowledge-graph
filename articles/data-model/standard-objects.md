---
id: kt:standard-objects
type: Concept
title: Standard Objects
aliases: [standard object, Salesforce standard objects, common objects, hero objects, legacy objects, original platform objects]
domain: data-model
summary: >-
  The objects Salesforce ships ready-made in every org, such as Account, Contact, Lead and Opportunity, which
  store business and setup data, can be extended with custom fields, and form the base of the platform data model.
release: "Winter '27"
status: current
broader: [kt:data-architecture, kt:metadata-driven-architecture]
related: [kt:object-relationships, kt:person-accounts, kt:record-types, kt:sales-cloud]
relations:
  - {predicate: contrastsWith, object: kt:custom-objects}
  - {predicate: contrastsWith, object: kt:external-objects}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: coveredBy, object: kt:platform-data-architect-certification}
sources:
  - id: s1
    title: "Salesforce Common Objects — Object Reference for the Salesforce Platform (Winter '27, API 68.0)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_concepts_common_objects.htm
    type: official-docs
    accessed: 2026-11-06
  - id: s2
    title: "Overview of Salesforce Objects and Fields — Object Reference for the Salesforce Platform (Winter '27, API 68.0)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects.htm
    type: official-docs
    accessed: 2026-11-06
  - id: s3
    title: "Relationships Among Standard Objects and Fields — Object Reference for the Salesforce Platform (Winter '27, API 68.0)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/relationships_among_objects.htm
    type: official-docs
    accessed: 2026-11-06
  - id: s4
    title: "Understand Custom & Standard Objects — Data Modeling (Trailhead)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/modules/data_modeling/units/objects_intro
    type: official-learning
    accessed: 2026-11-06
created: 2026-11-06
---

# Standard Objects

Standard objects are the database tables Salesforce creates for you: the Object Reference describes them as objects already built by Salesforce, in contrast with custom objects that an admin or developer defines through Setup or the Metadata API.[^s2] Trailhead's data-modeling module gives Account, Contact, Lead and Opportunity as the canonical examples, while a custom object is something like a real-estate company's own Property object.[^s4] Because every org starts with them, standard objects are the first thing an architect maps business entities onto before deciding what needs to be custom.

## Kinds of standard object

The Object Reference groups the objects available in any standard org, for any cloud and without special licensing, into three families.[^s1]

- **Original platform objects** — Account, Contact, Lead and Opportunity, sometimes nicknamed hero or legacy objects. They are the oldest objects on the platform, are customizable, and exist in every cloud built on an org.[^s1]
- **Base platform objects** — data-bearing objects common to most orgs, with SocialPersona given as an example.[^s1]
- **Setup platform objects** — objects that hold configuration rather than business data, such as CompactLayout and CustomField.[^s1]

Beyond these common objects, many more standard objects arrive with specific clouds, editions or features, and an application can only work with the objects it is authorized to see. Access depends on the org's configuration, the user's permissions, the sharing model and object-specific factors.[^s2]

## Fields on standard objects

Every object, standard or custom, carries identity, system and name fields. The identity field is an automatically generated 18-character, case-insensitive record ID; system fields are read-only audit values such as created and last-modified dates; the name field distinguishes records and can be text or an auto-number.[^s4] The API maintains system fields itself, for example generating the ID on create and updating LastModifiedDate on change.[^s2] Standard objects also ship with prebuilt standard fields, and compound fields such as addresses bundle several primitive values into one structured type.[^s4][^s2]

Standard objects are extensible: you add custom fields to them exactly as you would to a custom object, and those fields carry the `__c` suffix in their API names (Trailhead's example is a birthday field on Contact).[^s4] In describe results, custom objects report a `custom` flag of true, which is how code tells the two apart at run time.[^s2] Most API objects are read-write, but some are read-only, and each object's reference entry states which.[^s2]

## Limits and gotchas

Relationship rules are the main constraint. A standard object cannot sit on the detail side of a master-detail relationship whose master is a custom object, so a custom parent that must own Accounts or Cases has to use a lookup instead.[^s3] Some standard objects, Lead among them, also cannot act as the master in a master-detail relationship.[^s3] Master-detail cascades deletes and makes the detail inherit the master's sharing, whereas a lookup has no effect on deletion or security, so the choice changes behaviour, not just schema.[^s3]

## When to use them (and when not)

Prefer a standard object whenever its meaning fits the business entity, and extend it with custom fields rather than building a lookalike custom object; reserve custom objects for information specific to your company or industry that no standard object models.[^s4] Before committing, check the relationship rules above, because a design that needs a standard object as a master-detail child of a custom parent will not work.[^s3] For data held outside Salesforce, external objects map to the remote store, and big objects handle very large volumes; neither replaces standard objects for core CRM records.[^s2]

## Connections

Standard objects are the concrete starting point of **data architecture** and are themselves defined as metadata, which is why they sit under **metadata-driven architecture**.[^s2] They are frequently confused with **custom objects** and **external objects**, which differ in who defines them and where the data lives.[^s2] Their parent-child links follow the rules described in **object relationships**, and those relationships can be traversed in **SOQL** queries.[^s3] **Person accounts** combine the Account and Contact standard objects for consumer models, **record types** tailor a single standard object to several processes, and the original objects form the core of **Sales Cloud**.[^s1][^s4] Choosing between standard, custom and external objects is core design material for the **Platform Data Architect certification**.

## Sources
[^s1]: Salesforce Developers, "Salesforce Common Objects — Object Reference for the Salesforce Platform (Winter '27, API 68.0)". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_concepts_common_objects.htm (accessed 2026-11-06)
[^s2]: Salesforce Developers, "Overview of Salesforce Objects and Fields — Object Reference for the Salesforce Platform (Winter '27, API 68.0)". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects.htm (accessed 2026-11-06)
[^s3]: Salesforce Developers, "Relationships Among Standard Objects and Fields — Object Reference for the Salesforce Platform (Winter '27, API 68.0)". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/relationships_among_objects.htm (accessed 2026-11-06)
[^s4]: Trailhead, "Understand Custom & Standard Objects — Data Modeling". https://trailhead.salesforce.com/en/modules/data_modeling/units/objects_intro (accessed 2026-11-06)
