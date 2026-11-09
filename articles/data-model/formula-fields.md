---
id: kt:formula-fields
type: Feature
title: Formula Fields
aliases: [formula field, calculated field, cross-object formula, formula custom field]
domain: data-model
summary: >-
  A read-only custom field type whose value is computed from an expression over the record's own fields, related
  parent records, functions and operators, evaluated when the record is read rather than stored as entered data.
release: "Winter '27"
status: current
broader: [kt:custom-fields]
related: [kt:object-relationships, kt:validation-rules, kt:custom-indexes]
relations:
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: alternativeTo, object: kt:record-triggered-flow}
  - {predicate: contrastsWith, object: kt:roll-up-summary-field}
  - {predicate: coveredBy, object: kt:platform-app-builder-certification}
  - {predicate: coveredBy, object: kt:platform-administrator-certification}
sources:
  - id: s1
    title: "Use Formula Fields (Formulas and Validations module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/modules/point_click_business_logic/units/formula_fields
    type: official-learning
    accessed: 2026-11-09
  - id: s2
    title: "Create a Formula Field (Quick Data Insights with Formulas)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/quick-data-insights-with-formulas/create-a-formula-field-2
    type: official-learning
    accessed: 2026-11-09
  - id: s3
    title: "Tips for Reducing Formula Size (tip sheet, Spring '23)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/242/latest/en-us/sfdc/pdf/salesforce_formula_size_tipsheet.pdf
    type: official-docs
    accessed: 2026-11-09
  - id: s4
    title: "How I Solved This: Beat the Formula Compile Error"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2022/how-i-solved-this-beat-the-formula-compile-error
    type: official-blog
    accessed: 2026-11-09
  - id: s5
    title: "Formula Class (Apex Reference Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_class_System_Formula.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s6
    title: "Force.com SOQL Best Practices: Nulls and Formula Fields"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2013/02/force-com-soql-best-practices-nulls-and-formula-fields
    type: official-blog
    accessed: 2026-11-09
created: 2026-11-09
---

# Formula Fields

A formula field is a custom field whose value comes from an expression rather than from user input. It can be added to any standard or custom object, and typical uses are dividing two numbers into a percentage, turning a value into a hyperlink, or counting the days between two dates.[^s1] Because the platform does the arithmetic, users never type or maintain the result, and the same logic applies consistently on record pages, list views and reports.[^s1][^s2]

## How it works

An admin creates the field from Object Manager under Fields & Relationships by choosing the Formula data type and then a return type such as Text, Number, Currency or Checkbox; numeric and currency results also take a decimal-places setting.[^s2] The expression is written in a Simple or Advanced editor. The Advanced editor offers Insert Field, Insert Operator and a searchable function list, and Trailhead recommends using it even for easy formulas.[^s1][^s2] Check Syntax validates the expression, flags a result that does not match the chosen return type, and reports the compiled size.[^s1][^s2]

Formulas are not limited to the current record. A **cross-object formula** walks up relationship fields to read a parent's fields, for example `Account.Industry` on a Contact, or `Job_Application__r.Candidate__r.First_Name__c` on a custom object two hops away.[^s2][^s1] A blank-field setting controls null handling: "treat blank fields as zeroes" suits numeric math, while "treat blank fields as blanks" suits text results.[^s2]

Values are not stored with the record; they are calculated on the fly whenever the field is read, which is why a filter on a formula field has to compute the expression for each candidate row.[^s6] In Apex, `Formula.recalculateFormulas()` refreshes every formula on a list of in-memory SObjects without saving them, and it only consumes SOQL when fields the formula needs are missing from those records.[^s5]

## Limits and gotchas

- **Size.** Salesforce's formula-size tip sheet (Spring '23 edition) lists a maximum of 3,900 characters of formula text, including spaces and comments, and 4,000 bytes when saved.[^s3] The same tip sheet gives a compiled-size maximum of 15,000 bytes for all editions, while a 2022 Salesforce Admins blog example reports the compile error against a 5,000-character maximum. Treat the editor's reported compiled size as authoritative for your org.[^s3][^s4]
- **Compiled size snowballs.** Every referenced field adds its own compiled size, so referencing another formula field pulls in that formula's whole query; splitting logic into helper formulas does not reduce the total.[^s3]
- **Size fixes.** Reference each field once, prefer `CASE()` over nested `IF()`, put the most common result in the `CASE()` default, and call expensive functions such as `HYPERLINK()` once.[^s3][^s4] When that is not enough, store the value in a plain field populated by automation; the Admins blog replaced a heavy formula with a number field set by an after-save record-triggered flow.[^s4]
- **Picklists and dates.** Picklist values work only inside certain functions, so they are usually wrapped in `TEXT()`; Date/Time values need `DATEVALUE()` before date arithmetic with `TODAY()`.[^s2]
- **Query performance.** Formula fields are not indexed by default, so filtering on them over large objects can force full scans. Support can index a formula only if it is deterministic: references to other objects, `TODAY()` or `NOW()`, owner, auto-number and most audit fields, multi-select picklists, long text and multicurrency amounts all disqualify it.[^s6]

## When to use it (and when not)

Use a formula when the value can be derived at read time from the record and its parents and must always be current. Use a roll-up summary when the input is a set of child records. Use a stored field set by a record-triggered flow when the logic exceeds size limits, must be indexed, or should be fixed at a point in time.[^s3][^s4][^s6] For report or SOQL filters on large objects, put date logic directly in the filter against an indexed field instead of filtering on a non-deterministic formula.[^s6]

## Connections

A formula field is one of the data types of **custom fields**, its broader node.[^s1] Cross-object references depend on **object relationships** to reach parent records, and it **contrasts with** the **roll-up summary field**, which aggregates children rather than reading parents.[^s2] Because values are computed when read, formula fields used in **SOQL** filters raise selectivity questions; only deterministic formulas can be backed by **custom indexes**.[^s6] A **record-triggered flow** that writes a stored field is the usual **alternative** when a formula hits compile limits.[^s4] Trailhead teaches formula fields in the same module as **validation rules**, which reuse the formula language to block bad saves, and the formula-builder skills it covers are admin and app-builder fundamentals.[^s1]

## Sources

[^s1]: Trailhead, "Use Formula Fields". https://trailhead.salesforce.com/en/modules/point_click_business_logic/units/formula_fields (accessed 2026-11-09)
[^s2]: Trailhead, "Create a Formula Field". https://trailhead.salesforce.com/content/learn/modules/quick-data-insights-with-formulas/create-a-formula-field-2 (accessed 2026-11-09)
[^s3]: Salesforce, "Tips for Reducing Formula Size" (Spring '23). https://resources.docs.salesforce.com/242/latest/en-us/sfdc/pdf/salesforce_formula_size_tipsheet.pdf (accessed 2026-11-09)
[^s4]: Salesforce Admins Blog, "How I Solved This: Beat the Formula Compile Error". https://admin.salesforce.com/blog/2022/how-i-solved-this-beat-the-formula-compile-error (accessed 2026-11-09)
[^s5]: Salesforce Developers, "Formula Class" (Apex Reference Guide). https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_class_System_Formula.htm (accessed 2026-11-09)
[^s6]: Salesforce Developers Blog, "Force.com SOQL Best Practices: Nulls and Formula Fields". https://developer.salesforce.com/blogs/2013/02/force-com-soql-best-practices-nulls-and-formula-fields (accessed 2026-11-09)
