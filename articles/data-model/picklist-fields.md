---
id: kt:picklist-fields
type: Feature
title: Picklist Fields
aliases: [picklist field, single-select picklist, custom picklist, restricted picklist, unrestricted picklist, inactive picklist values, picklist value API name]
domain: data-model
summary: >-
  The single-select field type that limits a value to a defined list of choices. A picklist pairs a field (type,
  dependency, restriction) with a value set (choices, order, default), and its values can be restricted, deactivated,
  replaced or deleted without rebuilding the field.
release: "Winter '27"
status: current
broader: [kt:custom-fields]
related: [kt:picklist-value-sets, kt:multi-select-picklists, kt:field-dependencies, kt:data-quality, kt:standard-objects]
relations:
  - {predicate: dependsOn, object: kt:record-types}
  - {predicate: configuredVia, object: kt:object-manager}
  - {predicate: consumedBy, object: kt:formula-fields}
sources:
  - id: s1
    title: "Picklist Administration: Get Started with Picklists"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/picklist_admin/picklist_admin_start
    type: official-learning
    accessed: 2026-11-27
  - id: s2
    title: "Picklist Administration: Manage Your Picklist Values"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/picklist_admin/picklist_admin_manage
    type: official-learning
    accessed: 2026-11-27
  - id: s3
    title: "Learn MOAR in Summer '22 with Picklist Field Value Enhancements"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2022/learn-moar-in-summer-22-with-picklist-field-value-enhancements
    type: official-blog
    accessed: 2026-11-27
created: 2026-11-27
---

# Picklist Fields

A **picklist field** lets a user choose one value from a predefined list instead of typing free text. Salesforce treats every picklist as two separable parts: the *field*, which decides the type and whether it is multi-select, dependent or controlling, and the *value set*, which holds the choices, their order, the default and related settings.[^s1] Because the two are managed separately, an admin can change the list of choices without touching the field definition, page layouts or field-level security.[^s1]

Trailhead groups picklists into three kinds: standard picklists that ship on standard objects, custom single-select picklists, and custom multi-select picklists.[^s1] This article covers the single-select field itself; shared value lists are covered under **picklist value sets** and the multi-value variant under **multi select picklists**.

## How it works

An admin creates a custom picklist in Object Manager under Fields & Relationships, choosing the Picklist type, a label (the API name is generated and ends in `__c`), and the values, one per line.[^s1] Values can instead come from a global value set, and standard picklists draw on standard value sets, some of which are shared: Lead Source on Lead and Account Source on Account use the same set, so editing one edits the other.[^s1][^s2] During setup the admin can sort values alphabetically and make the first value the default; if both options are chosen, Salesforce sorts first and then defaults to the first sorted value.[^s1] A default can also be computed with a formula, for example returning a different priority for one profile and `null` to leave the field blank otherwise.[^s1][^s2]

Each value has a **label** shown to users and an **API name** used by formulas, code and integrations. Since Spring '17 the two are distinct, so a label can be reworded without breaking references to the API name, and admins can lock API names against change.[^s2] Changing an API name after it is in use can break those references.[^s2] Values also carry an optional chart color, which Salesforce assigns dynamically when none is set.[^s2]

## Restricted vs. unrestricted

A **restricted** picklist accepts only the values defined in its value set, whether the data arrives through the UI, the API or another application; only admins with edit rights can add values.[^s1] An **unrestricted** picklist also blocks new values in the UI, but the API, automation and integrations can still write values that are not in the list.[^s1] The setting can be changed later from the field's Edit page.[^s1] Only custom picklists can be restricted; standard picklists cannot be restricted, deleted or given formula defaults.[^s1] For data quality, restriction is the stronger guard, because an unrestricted field can quietly accumulate off-list values from imports and integrations.[^s1]

## Managing values over time

The field's Values related list offers New, Reorder, Replace, a printable view and chart colors.[^s2] Retiring a value has three options with different effects:

- **Deactivate** hides the value from the picklist but keeps it on existing records, and it can be reactivated later.[^s2]
- **Replace** swaps a value on existing records for another value or for blank; create the new value first, then run Replace.[^s2]
- **Delete** removes the value and runs as a background job that emails the admin when it finishes.[^s2]

Active and inactive values count together toward the field's value limit, so a long-lived field may need inactive values deleted to make room.[^s2] Replacing a controlling value drops its field dependency, which then has to be rebuilt with the new value.[^s2] Changing a field's type also has side effects: inactive values are lost, and converting a multi-select picklist to a single-select one clears values on existing records.[^s2]

Summer '22 added tools for this clean-up, introduced as betas: an emailed report listing custom picklists with 4,000 or more inactive values, a bulk delete of inactive values that no record uses, and checkbox-driven bulk activate, deactivate, replace and delete actions, all enabled from Setup's Picklist Settings.[^s3] Bulk deletes run in the background, are recorded in Setup Audit Trail and leave behind any inactive values still used by records.[^s3]

## Gotchas

- Standard picklists can control a dependent picklist but cannot themselves be dependent.[^s1]
- With record types, the record type and the controlling value together decide which values a user sees.[^s2]
- A default can be set on a controlling picklist but not on a dependent one.[^s2]

## Connections

A picklist is a kind of **custom fields** field whose values may come from **picklist value sets**; **multi select picklists** are its multi-value sibling.[^s1] It is configured in **object manager**, and it often drives **field dependencies**.[^s1][^s2] Which values appear depends on **record types**, and **formula fields** and formula defaults reference values by API name.[^s2] Restricted picklists on **standard objects** and custom objects are a basic **data quality** control.[^s1]

## Sources
[^s1]: Trailhead, "Picklist Administration: Get Started with Picklists". https://trailhead.salesforce.com/content/learn/modules/picklist_admin/picklist_admin_start (accessed 2026-11-27)
[^s2]: Trailhead, "Picklist Administration: Manage Your Picklist Values". https://trailhead.salesforce.com/content/learn/modules/picklist_admin/picklist_admin_manage (accessed 2026-11-27)
[^s3]: Salesforce Admins Blog, "Learn MOAR in Summer '22 with Picklist Field Value Enhancements". https://admin.salesforce.com/blog/2022/learn-moar-in-summer-22-with-picklist-field-value-enhancements (accessed 2026-11-27)
