---
id: kt:data-table-screen-component
type: Feature
title: Data Table Screen Component
aliases: [Flow Data Table, Data Table flow screen component, Data Table Screen Input Component, editable data table in flow]
domain: automation
summary: >-
  A standard screen flow input component that shows a collection of records (or Apex-defined objects) as a table, lets
  the running user select one or many rows, and, since Spring '26, sort columns and edit values inline, returning the
  selected and edited rows to the flow.
release: "Winter '27"
status: current
broader: [kt:screen-flow]
related: [kt:transform-element, kt:collection-filter-and-sort, kt:flow-loop-element, kt:get-records-element]
relations:
  - {predicate: alternativeTo, object: kt:custom-flow-screen-components}
  - {predicate: dependsOn, object: kt:apex-defined-types}
  - {predicate: dependsOn, object: kt:field-level-security}
sources:
  - id: s1
    title: "Data Table Screen Input Component"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.flow_ref_elements_screencmp_data_table.htm&type=5
    type: official-docs
    accessed: 2026-11-20
  - id: s2
    title: "Enhance User Choices with Screen Options (Screen Flows)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/screen-flows/add-more-options-to-your-screens
    type: official-learning
    accessed: 2026-11-20
  - id: s3
    title: "Salesforce Flow Data Table Now Supports Inline Editing and Sorting"
    publisher: Salesforce Time (Yumi Ibrahimzade)
    url: https://salesforcetime.com/2026/02/11/salesforce-flow-data-table-now-supports-inline-editing-and-sorting/
    type: community
    accessed: 2026-11-20
  - id: s4
    title: "Salesforce Spring '26 Release: Editable Data Table for Flow Is Here"
    publisher: Salesforce Ben (Tim Combridge)
    url: https://www.salesforceben.com/salesforce-spring-26-release-editable-data-table-for-flow-is-here/
    type: community
    accessed: 2026-11-20
created: 2026-11-20
---

# Data Table Screen Component

The **Data Table** is one of the standard input components an admin can drop onto a screen in a screen flow. It renders a collection of records as a table so the running user can pick the rows the rest of the flow should act on; the picks are stored in flow variables for later elements.[^s1] It is the declarative answer to the long-standing "show a list, let the user choose" requirement that used to need a custom Lightning web component.[^s4]

## How it works

You point the component at a **Source Collection**, typically the output of a Get Records element. On API version 65.0 and later the source can also be a collection of Apex-defined data types; on 64.0 and earlier it accepts only records.[^s1] A **Unique Identifier** column is required and must hold unique values such as a record ID, because duplicates can cause wrong rows to be selected.[^s1] Columns are added and reordered in the property panel; each column picks a source field, can carry a custom label (which screen readers also announce), and wraps or clips long text.[^s1] For lookup fields the column can show the related record's name and link to it, or fall back to the raw Salesforce ID.[^s1] An optional search bar filters across the whole dataset.[^s1]

**Row Selection Mode** decides the interaction. *Multiple* allows any count between a minimum and maximum, *Single* allows at most one row, and *View only* disables selection.[^s1][^s2] A default-selection collection can preselect rows, and the component shows radio buttons when only one row can be chosen and checkboxes otherwise.[^s1] Trailhead's badge exercise builds a case-creation flow in which the user picks the point of contact from a single-select table of the account's contacts.[^s2]

The component exposes two selection outputs: **First Selected Row** and **Selected Rows**, the latter in table order.[^s1] Trailhead warns that with multiple selection the "first" row is the one the user clicked first, not necessarily the first record sequentially.[^s2]

## Sorting and inline editing (Spring '26)

Spring '26 made the table interactive. Sorting and editing are switched on per column through a "Let Users Modify Data Table" setting, and no Setup change is required.[^s3][^s4] Users click a header to sort, which doesn't change which rows are selected.[^s1] When editing, the user confirms or cancels each change, and in Multiple mode one edit can be applied to every selected row at once.[^s1][^s3] Confirming an edit does **not** save it: the changed records come back in a third output, **Edited Rows**, which you must pass to an Update Records element.[^s3][^s4] Relationship fields such as Owner can't be made editable.[^s4]

## Limits and gotchas

- The table can show up to 1,500 records, and the user can select up to 200 of them; table height tops out at 400 pixels.[^s1]
- Salesforce states the component isn't compatible with mobile devices, so don't design mobile flows around it.[^s1]
- Unsupported data: anyType fields (for example AccountHistory.NewValue), searching Time fields, and the Subject field on Task and Event.[^s1]
- In multicurrency orgs, records in a currency other than the user's personal currency aren't supported.[^s1]
- Formula fields on records not yet committed don't evaluate correctly; compute values with an Assignment or formula resource instead.[^s1]
- Selected rows count against the client payload limit, which surfaces only as a generic error, so avoid large fields such as ContentVersion.VersionData.[^s1]
- With "Show record name" on, sorting and searching are unavailable for that lookup column.[^s1]
- Packaging a flow doesn't automatically include the fields its table displays; add them to the package yourself.[^s1]
- For Get Records performance, let Salesforce choose which fields to store rather than storing all fields.[^s1]

## When to use it (and when not)

Use the standard Data Table whenever a screen flow needs users to choose or quickly adjust a modest set of records on desktop: working through lists of leads, cases or opportunities, or picking contacts.[^s4] Reach for a **custom flow screen component** when you need mobile support, relationship-field editing, or behaviour beyond the standard options.[^s1][^s4] For reshaping the selection afterwards, pair the table with collection elements rather than loops.

## Connections

The Data Table is a component of **screen flows**, usually fed by a **Get Records** element and, on API 65.0 and later, able to display **Apex-defined types**.[^s1] It is the standard **alternative to** a developer-built **custom flow screen component** for record selection.[^s4] Its Selected Rows and Edited Rows outputs are collections, so they are naturally processed by the **Transform element**, **Collection Filter and Sort**, or the **Loop element** before an Update Records step.[^s3] Related record names appear only when the user can access the related object, so what it displays depends on object and **field-level security**.[^s1]

## Sources

[^s1]: Salesforce Help, "Data Table Screen Input Component". https://help.salesforce.com/s/articleView?language=en_US&id=platform.flow_ref_elements_screencmp_data_table.htm&type=5 (accessed 2026-11-20)
[^s2]: Trailhead, "Enhance User Choices with Screen Options" (Screen Flows module). https://trailhead.salesforce.com/content/learn/modules/screen-flows/add-more-options-to-your-screens (accessed 2026-11-20)
[^s3]: Salesforce Time, "Salesforce Flow Data Table Now Supports Inline Editing and Sorting". https://salesforcetime.com/2026/02/11/salesforce-flow-data-table-now-supports-inline-editing-and-sorting/ (accessed 2026-11-20)
[^s4]: Salesforce Ben, "Salesforce Spring '26 Release: Editable Data Table for Flow Is Here". https://www.salesforceben.com/salesforce-spring-26-release-editable-data-table-for-flow-is-here/ (accessed 2026-11-20)
