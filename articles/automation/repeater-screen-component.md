---
id: kt:repeater-screen-component
type: Feature
title: Repeater Screen Component
aliases: [Flow Repeater, Repeater component, Screen Flow Repeater, repeater in flow]
domain: automation
summary: >-
  A screen flow component that repeats a set of child screen components so the running user can enter, edit or remove
  several records on one screen; its Added, Prepopulated, Deleted and All Items outputs are then processed with a Loop
  and saved in bulk.
release: "Winter '27"
status: current
broader: [kt:screen-flow]
related: [kt:data-table-screen-component, kt:get-records-element, kt:flow-assignment-element, kt:collection-filter-and-sort, kt:flow-data-elements]
relations:
  - {predicate: dependsOn, object: kt:flow-loop-element}
  - {predicate: alternativeTo, object: kt:custom-flow-screen-components}
sources:
  - id: s1
    title: "Create and Update Records Efficiently with Repeater"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/loops-in-flow-builder/create-and-update-records-with-a-repeater
    type: official-learning
    accessed: 2026-11-27
  - id: s2
    title: "Enhance Flow Builder Skills by Looping through Repeaters"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/loops-in-flow-builder/loop-through-a-repeater
    type: official-learning
    accessed: 2026-11-27
  - id: s3
    title: "Flow Enhancements | Summer '24 Be Release Ready"
    publisher: Salesforce Admins Blog (Adam White)
    url: https://admin.salesforce.com/blog/2024/flow-enhancements-summer-24-be-release-ready
    type: official-blog
    accessed: 2026-11-27
  - id: s4
    title: "Deep Dive: The Salesforce Flow Repeater Component"
    publisher: Salesforce Ben (Tim Combridge)
    url: https://www.salesforceben.com/deep-dive-the-salesforce-flow-repeater-component/
    type: community
    accessed: 2026-11-27
created: 2026-11-27
---

# Repeater Screen Component

The **Repeater** is a screen flow component that lets a user enter and update several records on a single screen. At runtime it shows the set of fields an admin placed inside it, and each click of its **Add** button renders another copy of that set; a **Remove** button deletes a copy.[^s1] Trailhead's example is a sales rep entering every attendee contact for an account on one screen, and the Salesforce Admins blog uses collecting several insurance-policy beneficiaries.[^s1][^s3] It is a Screen Flow feature only and cannot be placed in autolaunched or record-triggered flows.[^s4]

## History

Salesforce Ben dates the component's first appearance to Spring '24, and the Salesforce Admins blog announced it as generally available in Summer '24, when it gained support for most standard GA screen components as children, conditional visibility, input validation, help text, and debugger output.[^s4][^s3] Winter '25 added prepopulation from existing data, plus toggles for whether users may add their own items and whether they may remove prepopulated ones; turning off user input gives a read-only repeater for confirming data.[^s4]

## How it works

The component sits in the **Display** section of the screen's component list. Admins drag child components into its drop zone, and only those children are repeated; the Trailhead example uses Name, Text, Email and Phone components.[^s1] To edit existing records, **Configure Data Source** sets *Collection for Prepopulated Items* to a record collection, typically from a Get Records element filtered on the current account. Each child's default value is then mapped from the **Repeater Prepopulated Items** section of the resource picker, which appears only inside a repeater with a data source. At runtime the repeater renders one set of components per item in the collection.[^s1]

Trailhead stresses that the flow has no built-in knowledge that the children correspond to record fields: the repeater needs the collection, and every child needs its own mapping.[^s1]

## Outputs and saving the data

The repeater does not write to the database itself. It exposes four collection outputs: **Added Items** (only rows the user added), **Prepopulated Items** (only prepopulated rows), **Deleted Items** (rows the user removed), and **All Items** (all of them together).[^s2] Trailhead recommends a separate loop for each group you need, such as passing Deleted Items to a Delete Records element.[^s2]

The documented save pattern loops over All Items with a Loop element. On the For Each path, an Assignment builds a single record variable and adds it to a record collection. It sets the record ID from the current item, the parent account ID from the flow's recordId, and each field from the item.[^s2] On the After Last path, one Create Records element runs on that collection with **Update Existing Records** turned on and Record ID as the matching field, which makes it an upsert.[^s2] If the ID isn't carried into each record, the upsert inserts a new record for every row, duplicating ones that already exist.[^s2]

## Limits and gotchas

- Transform elements can't process repeater output; use a Loop with an Assignment instead.[^s2]
- Salesforce Ben adds that the output also can't feed Collection Filter, Collection Sort, or another repeater.[^s4]
- Salesforce Ben reports a ceiling of 30 instances per repeater at runtime.[^s4]
- Action Buttons can't be placed inside a repeater, and formulas can't reference other components in the same repeater instance, though formulas referencing components outside it work.[^s3]
- At GA, Collection Choice Sets inside a repeater were not yet reactive. A repeater also couldn't be embedded in a section or given columns.[^s3]
- All Items is empty when the repeater holds only display components or the user adds nothing. It is null, not empty, when conditional visibility hides every child, so null-check before looping.[^s4]

## When to use it (and when not)

Use a repeater when users need to **type in** a variable number of new or changed records, such as line items, attendees or beneficiaries, without a separate screen per record.[^s1][^s3] Because one Create Records element saves the whole collection after the loop, it also avoids a screen-and-save round trip per record.[^s2] It is a poor fit when the design needs unsupported children such as Action Buttons, sections or columns, or more than the reported 30 rows.[^s3][^s4] In the graph, the Data Table screen component is the neighbour for selecting from an existing list, and a custom Lightning web component screen component is the usual fallback when standard components can't express the screen.

## Connections

The repeater is a component of **Screen Flow** and is usually seeded by the **Get Records** element.[^s1] Its output **depends on the Loop element**, an **Assignment** element and the **Create Records** data element to be saved, because Transform can't read it.[^s2] Salesforce Ben notes that **Collection Filter and Sort** can't consume it either.[^s4] Its unsupported children and layouts are listed in the Summer '24 release guidance.[^s3] It is a sibling of the **Data Table** screen component, and a **custom flow screen component** is the alternative when standard children fall short.

## Sources
[^s1]: Trailhead, "Create and Update Records Efficiently with Repeater". https://trailhead.salesforce.com/content/learn/modules/loops-in-flow-builder/create-and-update-records-with-a-repeater (accessed 2026-11-27)
[^s2]: Trailhead, "Enhance Flow Builder Skills by Looping through Repeaters". https://trailhead.salesforce.com/content/learn/modules/loops-in-flow-builder/loop-through-a-repeater (accessed 2026-11-27)
[^s3]: Salesforce Admins Blog, Adam White, "Flow Enhancements | Summer '24 Be Release Ready". https://admin.salesforce.com/blog/2024/flow-enhancements-summer-24-be-release-ready (accessed 2026-11-27)
[^s4]: Salesforce Ben, Tim Combridge, "Deep Dive: The Salesforce Flow Repeater Component". https://www.salesforceben.com/deep-dive-the-salesforce-flow-repeater-component/ (accessed 2026-11-27)
