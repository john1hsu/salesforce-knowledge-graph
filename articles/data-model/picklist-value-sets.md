---
id: kt:picklist-value-sets
type: Feature
title: Picklist Value Sets
aliases: [global value set, global value sets, global picklist, global picklists, GlobalValueSet, standard value set, Promote to Global Value Set]
domain: data-model
summary: >-
  Reusable lists of picklist values that are defined once and shared by several picklist fields: custom global value
  sets an admin creates, and the standard value sets behind standard picklists. Editing the set updates every field that uses it.
release: "Winter '27"
status: current
broader: [kt:custom-fields]
related: [kt:field-dependencies, kt:data-quality, kt:standard-objects, kt:heroku-connect]
relations:
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: queriedWith, object: kt:tooling-api}
  - {predicate: dependsOn, object: kt:record-types}
sources:
  - id: s1
    title: "Picklist Administration: Share Values with Global Value Sets"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/picklist_admin/picklist_admin_global
    type: official-learning
    accessed: 2026-11-16
  - id: s2
    title: "Picklist Administration: Get Started with Picklists"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/picklist_admin/picklist_admin_start
    type: official-learning
    accessed: 2026-11-16
  - id: s3
    title: "Metadata API Developer Guide: GlobalValueSet"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_globalvalueset.htm
    type: official-docs
    accessed: 2026-11-16
  - id: s4
    title: "Tooling API Developer Guide: GlobalValueSet"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/tooling_api_objects_globalvalueset.htm
    type: official-docs
    accessed: 2026-11-16
  - id: s5
    title: "Global Picklists: Define Globally, Use Locally"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2016/12/global-picklists-define-globally-use-locally
    type: official-blog
    accessed: 2026-11-16
  - id: s6
    title: "Why does Connect fail to write a value in my Global Picklist?"
    publisher: Heroku Help
    url: https://help.heroku.com/S35URKRN/why-does-connect-fail-to-write-a-value-in-my-global-picklist
    type: official-docs
    accessed: 2026-11-16
created: 2026-11-16
---

# Picklist Value Sets

A **picklist value set** is the list of values a picklist field offers. Salesforce gives a picklist field its values in one of three ways: **local** values typed in when the field is created and owned by that field alone, a **standard value set** that ships with a standard picklist, or a **global value set** that an admin creates once and shares across many picklist fields.[^s2] The Setup page that manages the shared kinds is called *Picklist Value Sets*, with separate sections for global and standard value sets.[^s1]

Global value sets (originally marketed as *global picklists*) arrived in the Winter '17 release.[^s5] Their purpose is consistency: change a value in the set and every field that references it changes too, and the set's detail page lists each field that uses it.[^s1][^s5]

## Standard vs. global value sets

Standard value sets back standard picklists, and some are shared by more than one field. Lead Source on Lead and Account Source on Account draw on the same set, so editing a value in one place changes it in the other.[^s2] Global value sets bring the same model to custom fields: they can drive both single-select picklists and multi-select picklists, including dependent picklists.[^s5]

## How it works

An admin opens **Setup → Picklist Value Sets**, clicks **New** next to Global Value Sets, enters a label and description, and types the values one per line. Options let the admin sort the values alphabetically and make the first value the default; when both are chosen, Salesforce alphabetizes first and then defaults to the first value in that order.[^s1] When a new picklist field is created in Object Manager, the admin keeps the **Use a global value set** option and picks the set.[^s1]

An existing local picklist can be converted with **Promote to Global Value Set** on the field's edit page, which turns its values into a new global set that other fields can reuse.[^s1] Day-to-day maintenance happens on the set, not the fields: reorder, edit, deactivate, delete, replace and change the default, with every change applying to all referencing fields. Replacing a value can also fill currently blank fields, and deleting a value runs as a background job that emails the admin when done.[^s1] Each field can still carry its own default, including a formula default, independent of the set's default.[^s1]

## Restriction and record types

A global value set is always **restricted** and cannot be made unrestricted, so only values defined in the set can be stored in its fields.[^s1] Restricted picklists stop users from adding new values, which is what keeps the data clean.[^s2] Integrations feel this directly: a Heroku Connect write that carries a value outside the set fails with Salesforce's *bad value for restricted picklist field* error. Heroku's fix for global-value-set fields is to edit the record type and assign the set's values to the field, then retry the failed writes.[^s6] In other words, the set defines the allowed values, but each record type still has to enable them.[^s6]

## Metadata and APIs

In the Metadata API a set is the `GlobalValueSet` type, stored with the `.globalValueSet` suffix in the `globalValueSets` folder. The type dates from API version 38.0; in API 37.0 it was named `GlobalPicklist`.[^s3] Its `masterLabel` and `sorted` fields are required, `description` is capped at 255 characters, and `customValue` holds at most 1,000 values, inactive values included.[^s3] Custom picklist fields built on a global set are of type `ValueSet` and inherit the set's values.[^s3] Sets created at API version 57.0 or later get a `__gvs` suffix appended to their developer name, and CRUD-based calls must include it in `fullName`.[^s3][^s4]

The Tooling API exposes the same component as the `GlobalValueSet` object (API 39.0+). Its `Metadata` and `FullName` fields can be queried only when the result has at most one row, and a retrieve returns both active and inactive values with properties such as label, color, default and active flag.[^s4]

## Limits and gotchas

- **1,000 values per set**, counting inactive values, so retire values with care rather than letting them accumulate.[^s3]
- **Always restricted**: imports and integrations that send unknown values fail rather than adding them.[^s1][^s6]
- **Shared blast radius**: a rename or deletion hits every field on every object that uses the set, so values must make sense for all of them.[^s1]
- **Developer-name suffix**: deployment scripts and `package.xml` entries for sets created at API 57.0+ must use the `__gvs` name.[^s3][^s4]

## When to use it (and when not)

Use a global value set when several fields across objects must offer the same governed list, such as regions, product lines or industries; consistency comes at the cost of flexibility.[^s1] Salesforce's launch guidance advised against a global set when only one field needs the values, or when you do not want API inserts validated against the list.[^s5] For values that depend on another field, layer a field dependency on top; for per-process subsets, rely on record types.[^s5][^s6]

## Connections

Picklist value sets are a configuration of **custom fields** and serve **data quality** by enforcing one governed list. They combine with **field dependencies**, which can use a global set in a dependent picklist, and they depend on **record types**, which decide which of the set's values each process exposes.[^s5][^s6] Standard value sets belong to **standard objects** such as Lead and Account.[^s2] Sets are deployed through the **Metadata API** and inspected through the **Tooling API**, and their restricted nature surfaces as write errors in integrations such as **Heroku Connect**.[^s3][^s4][^s6]

## Sources
[^s1]: Trailhead, "Picklist Administration: Share Values with Global Value Sets". https://trailhead.salesforce.com/content/learn/modules/picklist_admin/picklist_admin_global (accessed 2026-11-16)
[^s2]: Trailhead, "Picklist Administration: Get Started with Picklists". https://trailhead.salesforce.com/content/learn/modules/picklist_admin/picklist_admin_start (accessed 2026-11-16)
[^s3]: Salesforce Developers, "Metadata API Developer Guide: GlobalValueSet". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_globalvalueset.htm (accessed 2026-11-16)
[^s4]: Salesforce Developers, "Tooling API Developer Guide: GlobalValueSet". https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/tooling_api_objects_globalvalueset.htm (accessed 2026-11-16)
[^s5]: Salesforce Developers Blog, "Global Picklists: Define Globally, Use Locally". https://developer.salesforce.com/blogs/2016/12/global-picklists-define-globally-use-locally (accessed 2026-11-16)
[^s6]: Heroku Help, "Why does Connect fail to write a value in my Global Picklist?". https://help.heroku.com/S35URKRN/why-does-connect-fail-to-write-a-value-in-my-global-picklist (accessed 2026-11-16)
