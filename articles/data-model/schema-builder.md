---
id: kt:schema-builder
type: Tool
title: Schema Builder
aliases: [Salesforce Schema Builder, schema builder canvas]
domain: data-model
summary: >-
  A Setup tool that draws selected Salesforce objects, their fields and their relationships on a drag-and-drop canvas,
  and lets admins create custom objects and fields (including formula and relationship fields) directly from that view.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform, kt:metadata-driven-architecture]
related: [kt:object-relationships, kt:custom-fields, kt:formula-fields, kt:salesforce-diagrams, kt:platform-app-builder-certification]
relations:
  - {predicate: enables, object: kt:data-architecture}
  - {predicate: dependsOn, object: kt:field-level-security}
  - {predicate: alternativeTo, object: kt:object-manager}
sources:
  - id: s1
    title: "Data Modeling: Work with Schema Builder"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data_modeling/schema_builder
    type: official-learning
    accessed: 2026-11-11
  - id: s2
    title: "Schema Builder Considerations"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.schema_builder_considerations.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-11
  - id: s3
    title: "Create Objects with Schema Builder"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=schema_builder_elements_objects.htm&type=5
    type: official-docs
    accessed: 2026-11-11
  - id: s4
    title: "Create Custom Objects and Fields with Spring '12 Schema Builder"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2012/02/create-custom-objects-and-fields-with-spring-12-schema-builder
    type: official-blog
    accessed: 2026-11-11
  - id: s5
    title: "Study Up on Data Modeling and Management"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/platform-app-builder-pt2/platform-app-builder-data-modeling-and-management
    type: official-learning
    accessed: 2026-11-11
created: 2026-11-11
---

# Schema Builder

**Schema Builder** is the Setup tool for looking at, and editing, an org's data model as a picture. Trailhead sums it up as a way to "visualize and edit your data model": objects appear as boxes on a canvas, their fields are listed inside, and relationship lines connect them.[^s1] Admins open it by typing "Schema Builder" into the Setup Quick Find box.[^s1] It works in both Salesforce Classic and Lightning Experience and in all editions, though creating custom objects requires the **Customize Application** permission.[^s3]

## How it works

The left panel controls what's on the canvas. Checkboxes pick which objects to show, **Clear All** empties the canvas, and **Auto-Layout** arranges the selected objects automatically.[^s1] Dragging boxes around changes only the diagram. Moving an object on the canvas never alters the object or its relationships.[^s1]

The **Elements** tab turns the diagram into an editor. Drag the **Object** element onto the canvas, fill in the definition and save, and a new custom object exists.[^s1][^s3] Drag a field type onto an object and save to add a field. Ordinary fields, formula fields and relationship fields can all be created this way.[^s1] Everything built here is ordinary metadata, so the new objects and fields also show up in Object Manager just as if they had been created there.[^s1] Setup's object pages remain an equal alternative for creating the same objects.[^s3]

## Limits and gotchas

Salesforce's considerations page lists several behaviours that surprise first-time users:[^s2]

- **Layout autosaves, Auto-Layout is final.** Each object move is saved, and an Auto-Layout can't be undone.[^s2]
- **Large schemas are slow.** Many objects and fields can make the canvas load slowly. Hiding relationship lines improves performance.[^s2]
- **No export.** You can't export a schema from Schema Builder, for example to reuse it in another org. Moving a model between orgs needs metadata deployment instead.[^s2]
- **Objects made elsewhere stay hidden.** Objects created by an app or the API aren't added to the canvas automatically. Tick them in the left panel to show them.[^s2]
- **Permissive default field-level security.** New custom fields are visible and editable for internal profiles by default, apart from profiles cloned from Partner User or Customer Portal Manager. Formula and roll-up summary fields are visible but read-only.[^s2] Review field access right after building, because a field created from the canvas is open to most internal users.
- **Name collisions.** Keep each field's name and label unique within its object. A custom field that shares a standard field's name or label makes merge fields return the custom value.[^s2]
- **Zoom isn't remembered** between sessions.[^s2]

## When to use it (and when not)

Use Schema Builder to understand an unfamiliar org, to sketch and build a small model quickly, or to walk stakeholders through how records connect. Trailhead points to explaining data flow to colleagues as a typical use.[^s1] For detailed field configuration, page layouts or bulk changes, the object pages in Setup and metadata-based tooling are the better fit. For diagrams you need to share, version or reuse, a separate modelling or diagramming standard works better, because Schema Builder can't export its canvas.[^s2][^s3]

The tool has a long history. It first appeared as a beta in Winter '12, and Spring '12 added the ability to create objects and fields by drag and drop.[^s4] It remains exam material. Salesforce's Platform App Builder cert-prep unit lists Schema Builder capabilities and considerations among the topics of the Data Modeling and Management section. That section counts for 22% of the exam.[^s5]

## Connections

Schema Builder sits within the **Salesforce platform** and its **metadata-driven architecture**: what it draws and creates is org metadata.[^s1] It is a working view of **object relationships**, and it creates **custom fields**, including **formula fields** and relationship fields.[^s1] It **depends on field-level security** because of the default access it grants to new fields.[^s2] It is an **alternative to Object Manager** for creating objects and fields.[^s1][^s3] It **enables data architecture** work by making a model visible to architects and stakeholders. For formal diagrams, the **Salesforce Diagrams** standard is the complement, since Schema Builder can't export.[^s2] Its considerations appear in the **Platform App Builder** certification prep.[^s5]

## Sources
[^s1]: Trailhead, "Data Modeling: Work with Schema Builder". https://trailhead.salesforce.com/content/learn/modules/data_modeling/schema_builder (accessed 2026-11-11)
[^s2]: Salesforce Help, "Schema Builder Considerations". https://help.salesforce.com/s/articleView?id=sf.schema_builder_considerations.htm&language=en_US&type=5 (accessed 2026-11-11)
[^s3]: Salesforce Help, "Create Objects with Schema Builder". https://help.salesforce.com/s/articleView?language=en_US&id=schema_builder_elements_objects.htm&type=5 (accessed 2026-11-11)
[^s4]: Salesforce Developers Blog, "Create Custom Objects and Fields with Spring '12 Schema Builder". https://developer.salesforce.com/blogs/2012/02/create-custom-objects-and-fields-with-spring-12-schema-builder (accessed 2026-11-11)
[^s5]: Trailhead, "Study Up on Data Modeling and Management". https://trailhead.salesforce.com/content/learn/modules/platform-app-builder-pt2/platform-app-builder-data-modeling-and-management (accessed 2026-11-11)
