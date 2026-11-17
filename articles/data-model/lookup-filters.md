---
id: kt:lookup-filters
type: Feature
title: Lookup Filters
aliases: [lookup filter, filtered lookup, filtered lookups, dependent lookup, dependent lookups, related lookup filters, lookupFilter]
domain: data-model
summary: >-
  An administrator-defined filter on a lookup, master-detail or hierarchical relationship field that restricts which
  target records users can pick and save, using criteria on the source record, the target record, the running user
  and records one relationship away from the target.
release: "Winter '27"
status: current
broader: [kt:object-relationships, kt:data-quality]
related: [kt:lookup-vs-master-detail, kt:hierarchical-relationships, kt:field-dependencies, kt:page-layouts, kt:custom-fields, kt:unlocked-packages]
relations:
  - {predicate: alternativeTo, object: kt:validation-rules}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: consumedBy, object: kt:visualforce}
sources:
  - id: s1
    title: "Lookup Filters"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.fields_lookup_filters.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-17
  - id: s2
    title: "Considerations for Lookup Filters"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=sf.fields_lookup_filters_notes.htm&language=en_us
    type: official-docs
    accessed: 2026-11-17
  - id: s3
    title: "Limitations on Lookup Filters"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=fields_lookup_limitations.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-17
  - id: s4
    title: "Define Lookup Filters"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.fields_lookup_filters_defining.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-17
  - id: s5
    title: "Customize a Salesforce Object: Create Lookup Filters"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/customize-a-salesforce-object/create-lookup-filters
    type: official-learning
    accessed: 2026-11-17
  - id: s6
    title: "Metadata API Developer Guide: NamedFilter"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/namedfilter.htm
    type: official-docs
    accessed: 2026-11-17
created: 2026-11-17
---

# Lookup Filters

A lookup filter is an administrator setting on a lookup, master-detail or hierarchical relationship field that narrows
which target records are valid for that field and which records the lookup search shows. Typical uses are allowing only
active accounts on an opportunity, only accounts of a given record type, or only contacts that belong to the case's own
account.[^s1] The feature works in Salesforce Classic and Lightning Experience in every edition except Database.com, and
managing filters needs the Customize Application permission.[^s1]

## How it works

Filters are defined on the relationship field itself: edit the field, open **Show Filter Settings** in the lookup filter
section, and build criteria rows of field, operator, and either a fixed value or another field. **Insert Suggested
Criteria** proposes rows based on the object's relationships, and **Add Filter Logic** combines rows with Boolean
conditions. The admin then chooses required or optional, picks the standard or a custom error message for required
filters, can add explanatory text for the lookup dialog, and leaves **Enable this filter** selected.[^s4]

Criteria can compare fields on four kinds of record: the record being edited (the source), the target record, the
running user (including profile and role), and records directly related to the target.[^s1] A Trailhead project shows
both patterns: a Backup Agent user lookup limited by the user's profile name, and the case Contact Name field limited
so the contact's account equals the case's account, a field-to-field comparison usually called a dependent lookup.[^s5]
Field-to-field comparisons must use compatible types; for example, a picklist on one side can only be compared with
text, text area, email or URL fields, and a date can be compared with date, date/time or roll-up summary fields.[^s1]

**Required versus optional.** A required filter blocks saving a value that fails the criteria and shows an error that
admins can customize. An optional filter, a Classic-only behaviour, lets users click to show all results and save a
non-matching value. In Lightning Experience every lookup filter behaves as required, whatever Setup says.[^s1]

**Enforcement.** Filters are enforced on data loaded through the API, which has supported them since API version
16.0.[^s2] In metadata, the old standalone NamedFilter type was removed as of API version 30.0, and filters are now
carried by the `lookupFilter` field of the CustomField component.[^s6]

## Limits and gotchas

The Help limitations page, checked for Winter '27, gives these numbers:[^s3]

- Each object can have up to five active required lookup filters.[^s3]
- In Classic you can have an unlimited number of optional lookup filters.[^s3]
- One lookup filter accepts up to 10 criteria rows.[^s3]

Each unique related-object relationship that a required filter references counts against the **target** object's
limit, while optional filters don't; the target object's Related Lookup Filters list shows what is counting.[^s2][^s1]
Spanning is only one relationship level deep, and filters stop working if the criteria include a master-detail
relationship field.[^s2]

Other behaviours that surprise teams, all from the considerations page:[^s2]

- A new filter doesn't clear existing values that no longer match; the next edit of that record forces a valid value.[^s2]
- Filter comparisons are case-sensitive, and switching a required filter to optional deletes its custom error message.[^s2]
- In Lightning Experience a filter fails if a field used in its criteria is missing from the page layout or list view.[^s2]
- Changing a record's owner in Classic doesn't re-validate fields that have active filters.[^s2]
- A filter on the target must be deployed together with the object it points to; a filter removed in a later unlocked package version stays in subscriber orgs until deleted by hand.[^s2]
- A filter that admits only inactive users leaves no valid choices, because inactive users are never valid in user lookups.[^s2]

## When to use it (and when not)

Use a lookup filter when the goal is to steer users toward the right records while they search, or to automate a
narrowing that users would otherwise do by hand. Salesforce recommends a validation rule instead when the object is near
its lookup filter limit or the rule needs a complex formula, since validation rules can reach parent fields and use
functions such as ISNEW and ISCHANGED.[^s2] Validation rules only reject a bad save, though; they don't shape the
search results users see.

## Connections

Lookup filters belong to the relationship-field toolkit described under **object relationships** and
**lookup vs. master-detail**, and they apply equally to user-to-user **hierarchical relationships**.[^s1] They are
a **data quality** control that sits alongside **validation rules** as an alternative enforcement point.[^s2]
They are the relationship-field counterpart of **field dependencies**, which filter picklist values by a controlling
field, and they rely on **page layouts** in Lightning because criteria fields must be on the layout.[^s2] Filters
travel as part of **custom fields** metadata through the **Metadata API**, are honoured by dependent lookups in
**Visualforce** pages, and need care when shipped in **unlocked packages**.[^s6][^s2]

## Sources

[^s1]: Salesforce Help, "Lookup Filters". https://help.salesforce.com/s/articleView?id=sf.fields_lookup_filters.htm&language=en_US&type=5 (accessed 2026-11-17)
[^s2]: Salesforce Help, "Considerations for Lookup Filters". https://help.salesforce.com/apex/HTViewHelpDoc?id=sf.fields_lookup_filters_notes.htm&language=en_us (accessed 2026-11-17)
[^s3]: Salesforce Help, "Limitations on Lookup Filters". https://help.salesforce.com/s/articleView?id=fields_lookup_limitations.htm&language=en_US&type=5 (accessed 2026-11-17)
[^s4]: Salesforce Help, "Define Lookup Filters". https://help.salesforce.com/s/articleView?id=sf.fields_lookup_filters_defining.htm&language=en_US&type=5 (accessed 2026-11-17)
[^s5]: Trailhead, "Customize a Salesforce Object: Create Lookup Filters". https://trailhead.salesforce.com/content/learn/projects/customize-a-salesforce-object/create-lookup-filters (accessed 2026-11-17)
[^s6]: Salesforce Developers, "Metadata API Developer Guide: NamedFilter". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/namedfilter.htm (accessed 2026-11-17)
