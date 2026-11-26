---
id: kt:object-manager
type: Tool
title: Object Manager
aliases: [Salesforce Object Manager, Setup Object Manager]
domain: data-model
summary: >-
  The Lightning Experience Setup tool that lists every standard and custom object in an org and gives admins one
  place to manage each object's settings, such as fields and relationships, page layouts, compact layouts, record
  types, buttons and links.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform, kt:metadata-driven-architecture]
related: [kt:custom-objects, kt:standard-objects, kt:custom-fields, kt:page-layouts, kt:compact-layouts, kt:record-types]
relations:
  - {predicate: alternativeTo, object: kt:schema-builder}
sources:
  - id: s1
    title: "Learn to Use Setup and the Object Manager"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/setup-quick-look/learn-to-use-setup-and-the-object-manager
    type: official-learning
    accessed: 2026-11-26
  - id: s2
    title: "Object Manager (Salesforce Style Guide for Documentation and User Interface Text)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.salesforce_pubs_style_guide.meta/salesforce_pubs_style_guide/style_object_manager.htm
    type: official-docs
    accessed: 2026-11-26
  - id: s3
    title: "Understand Sales Cloud Data Models"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/sales-cloud-configuration-basics/understand-data-models
    type: official-learning
    accessed: 2026-11-26
  - id: s4
    title: "Optimize Customer Data with Standard and Custom Objects"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/modules/data_modeling/units/objects_intro
    type: official-learning
    accessed: 2026-11-26
  - id: s5
    title: "Take a Tour of Setup Home in Lightning Experience"
    publisher: Salesforce Admins
    url: https://admin.salesforce.com/blog/2020/setup-home-lightning-experience
    type: official-blog
    accessed: 2026-11-26
  - id: s6
    title: "Learn Lightning: Create & Edit Objects"
    publisher: Salesforce Admins
    url: https://admin.salesforce.com/blog/2016/learn-lightning-create-edit-objects
    type: official-blog
    accessed: 2026-11-26
created: 2026-11-26
---

# Object Manager

**Object Manager** is the part of Setup where admins manage objects. Trailhead calls it "a one-stop shop for managing all objects in your org": one list holds both standard objects such as Account and Contact and the org's custom objects.[^s1] Salesforce's own style guide describes it as a streamlined tool for reaching the management settings of standard and custom objects, and gives fields, page layouts and compact layouts as examples of those settings.[^s2] The style guide also states that Object Manager is available only in Lightning Experience.[^s2]

## How it works

Admins reach it from the gear icon on any Lightning page: open **Setup**, then click the **Object Manager** tab.[^s1] There is a shortcut from a record as well. While viewing an object, click the gear icon and choose **Edit Object** to jump straight to that object's page in Object Manager.[^s3] Once open, it shows every object the admin can edit and customize.[^s3]

Selecting an object opens its detail page, with the object's settings in a left-hand pane. To add a field to Account, for example, an admin selects Account, opens **Fields & Relationships** and clicks **New**.[^s1] Trailhead names fields, layouts, record types, buttons and links among the settings managed this way.[^s1] The Salesforce Admins blog makes the same point for Lightning Experience: most object settings, including fields, layouts, record types, buttons and links, live in Object Manager.[^s5]

New custom objects start from the **Create | Custom Object** menu at the top right of Object Manager.[^s1][^s4] The admin enters a label and plural label (for example Property and Properties), and Salesforce fills in the object name and record name automatically. An optional box launches the New Custom Tab Wizard after saving.[^s4] When the object is created, the platform builds supporting pieces such as its page layout for you.[^s4] Fields added through Fields & Relationships get API names ending in `__c`, which marks them as custom (a Currency field labelled Price becomes `Price__c`).[^s4]

## Limits and gotchas

- **Lightning only.** Object Manager doesn't exist in Salesforce Classic. Seeing all standard and custom objects in one view was billed as a Lightning-only advantage.[^s2][^s6]
- **Quick Find can miss object settings.** Quick Find searches Setup pages by title. The Admins blog advises checking Object Manager when Quick Find doesn't turn up what you need.[^s5]
- **Same configuration, new entry point.** Creating and editing objects in Lightning differs from Classic mainly in where the process starts. The settings and metadata are the same.[^s6]
- **Setup domain.** Setup pages are served from `*.salesforce-setup.com`, so a locked-down network may need to allow that domain before Object Manager loads.[^s1]

## When to use it (and when not)

Use Object Manager for detailed, per-object configuration: defining fields and relationships, arranging layouts, setting up record types, and editing buttons and links.[^s1][^s5] For a visual overview of how objects relate, Schema Builder's diagram is the alternative view of the same data model. Clicks in Setup change one org at a time, so changes that must reach other orgs belong in a deployment process rather than repeated manual edits.

## Connections

Object Manager is a Setup tool of the **Salesforce platform**, and it edits the org metadata at the heart of its **metadata-driven architecture**.[^s2] It is the main entry point for **custom objects** and for changes to **standard objects**.[^s1][^s4] From an object's page, admins manage **custom fields** under Fields & Relationships, along with **page layouts**, **compact layouts** and **record types**.[^s1][^s2][^s5] It is an **alternative to Schema Builder**: both create objects and fields, but Object Manager organizes them as per-object settings pages.[^s1]

## Sources
[^s1]: Trailhead, "Learn to Use Setup and the Object Manager". https://trailhead.salesforce.com/content/learn/modules/setup-quick-look/learn-to-use-setup-and-the-object-manager (accessed 2026-11-26)
[^s2]: Salesforce Developers, "Object Manager (Salesforce Style Guide for Documentation and User Interface Text)". https://developer.salesforce.com/docs/atlas.en-us.salesforce_pubs_style_guide.meta/salesforce_pubs_style_guide/style_object_manager.htm (accessed 2026-11-26)
[^s3]: Trailhead, "Understand Sales Cloud Data Models". https://trailhead.salesforce.com/content/learn/modules/sales-cloud-configuration-basics/understand-data-models (accessed 2026-11-26)
[^s4]: Trailhead, "Optimize Customer Data with Standard and Custom Objects". https://trailhead.salesforce.com/en/modules/data_modeling/units/objects_intro (accessed 2026-11-26)
[^s5]: Salesforce Admins, "Take a Tour of Setup Home in Lightning Experience". https://admin.salesforce.com/blog/2020/setup-home-lightning-experience (accessed 2026-11-26)
[^s6]: Salesforce Admins, "Learn Lightning: Create & Edit Objects". https://admin.salesforce.com/blog/2016/learn-lightning-create-edit-objects (accessed 2026-11-26)
