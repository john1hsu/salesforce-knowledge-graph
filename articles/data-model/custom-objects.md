---
id: kt:custom-objects
type: Concept
title: Custom Objects
aliases: [custom object, __c object, custom database table, CustomObject metadata]
domain: data-model
summary: >-
  Org-defined database tables, created in Object Manager or deployed as CustomObject metadata, whose API names end
  in __c and which hold the business data that Salesforce's standard objects don't cover.
release: "Winter '27"
status: current
broader: [kt:data-architecture, kt:metadata-driven-architecture]
related: [kt:custom-fields, kt:object-relationships, kt:lookup-vs-master-detail, kt:field-history-tracking, kt:page-layouts]
relations:
  - {predicate: contrastsWith, object: kt:standard-objects}
  - {predicate: alternativeTo, object: kt:external-objects}
  - {predicate: alternativeTo, object: kt:big-objects}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: configuredVia, object: kt:schema-builder}
  - {predicate: dependsOn, object: kt:organization-wide-defaults}
sources:
  - id: s1
    title: "Custom Objects — Object Reference for the Salesforce Platform (Winter '27, API 68.0)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_custom_objects.htm
    type: official-docs
    accessed: 2026-11-20
  - id: s2
    title: "CustomObject — Metadata API Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/customobject.htm
    type: official-docs
    accessed: 2026-11-20
  - id: s3
    title: "Optimize Customer Data with Standard and Custom Objects — Data Modeling (Trailhead)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/data_modeling/objects_intro
    type: official-learning
    accessed: 2026-11-20
  - id: s4
    title: "Create a Custom Object — Create a Custom Object Quick Look (Trailhead)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/create-a-custom-object-quick-look/create-a-custom-object
    type: official-learning
    accessed: 2026-11-20
created: 2026-11-20
---

# Custom Objects

A custom object is a database table that an org defines for itself, to store information specific to its company or industry rather than the data Salesforce ships with.[^s1][^s3] Trailhead's running example is a real-estate business that adds a Property object next to the standard Account, Contact, Lead and Opportunity objects.[^s3] In the platform's vocabulary the object is the table, its fields are the columns and its records are the rows, and the whole set of objects and fields makes up the org's data model.[^s3] In describe results a custom object reports its `custom` flag as true.[^s1]

## How it is defined

Admins usually create a custom object in Setup: open **Object Manager**, choose **Create → Custom Object**, enter a label and a plural label, and let Salesforce fill in the object name and record name from the label.[^s4] Ticking the option to launch the new custom tab wizard gives the object a tab, and the tab style picked there becomes the object's icon.[^s4] Creating the object also makes the platform generate supporting UI such as a page layout.[^s3] Besides Setup, custom objects can be created through the Metadata API or the Salesforce Extensions for VS Code.[^s1]

Under the hood each object is a `CustomObject` metadata component, available since API version 10.0 and stored in source with an `.object` suffix.[^s2] Every custom object needs a plural label and a name field, which is normally text or an auto number.[^s2] Its metadata also carries the deployment status, the internal and external org-wide sharing defaults, and switches for history tracking, activities, reports, search and feeds.[^s2] Metadata API does not let you update a single field of the definition in isolation, so a deployment should specify all of the object's relevant settings.[^s2]

## Naming and generated pieces

The API name always ends in `__c`: an object labeled Issue becomes `Issue__c`, and names must be unique in the org.[^s1] Relationship fields follow the same convention, with `__c` on the field and `__r` on the relationship name used in SOQL traversals.[^s1] When an unmanaged object later ships in a managed package, the namespace prefix is inserted, turning `name__c` into `prefix__name__c`.[^s1]

Every object gets an 18-character case-insensitive record ID (with a 15-character case-sensitive form) and read-only system fields such as CreatedDate and LastModifiedDate.[^s3] The audit fields can be set on insert only for data migration, and only when the org enables the setting and the user has both Modify All Data and Set Audit Fields upon Record Creation.[^s1] Salesforce also generates companion objects: a `__Share` object for objects that have no master-detail parent, whose sharing reasons Apex can read, and a `__Tag` object.[^s1]

## Gotchas

- New custom objects are not searchable until **Allow Search** (`enableSearch`) is turned on; it is off by default.[^s2]
- Search is switched off for objects that have not been searched in more than 120 days.[^s2]
- Bulk API, sharing and Streaming API access are enabled together as a set; turning one on requires the other two.[^s2]
- A record created through the API without a name takes its record ID as its name.[^s1]
- In the UI, only records whose name field is populated are shown.[^s1]
- As a master-detail child, the object inherits sharing from its parent and is deleted with it, so it gets no `__Share` object.[^s1]

## When to use it (and when not)

Start with the standard objects and add custom fields when a business entity already has a native home; a custom object is for entities that don't.[^s3] Data that should stay in an outside system belongs in an external object, which uses the `__x` suffix instead of `__c` and, for example, cannot have activities enabled.[^s2] Very high-volume data is a separate choice, weighed against big objects.

## Connections

Custom objects **contrast with** standard objects, which Salesforce provides, and are an **alternative to** external objects and big objects when choosing where data lives.[^s1][^s2][^s3] They are **configured via** the Metadata API's `CustomObject` type or in Setup's Object Manager, with Schema Builder as the visual alternative, and they sit under data architecture and the metadata-driven architecture.[^s2][^s4] They are built from custom fields and linked through object relationships, lookup or master-detail, with optional field history tracking.[^s1][^s2] Record access **depends on** the org-wide defaults set in their `sharingModel` and `externalSharingModel`.[^s2]

## Sources

[^s1]: Salesforce Developers, "Custom Objects — Object Reference for the Salesforce Platform" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_custom_objects.htm (accessed 2026-11-20)
[^s2]: Salesforce Developers, "CustomObject — Metadata API Developer Guide". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/customobject.htm (accessed 2026-11-20)
[^s3]: Trailhead, "Optimize Customer Data with Standard and Custom Objects". https://trailhead.salesforce.com/en/data_modeling/objects_intro (accessed 2026-11-20)
[^s4]: Trailhead, "Create a Custom Object". https://trailhead.salesforce.com/content/learn/modules/create-a-custom-object-quick-look/create-a-custom-object (accessed 2026-11-20)
