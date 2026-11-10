---
id: kt:validation-rules
type: Feature
title: Validation Rules
aliases: [validation rule, custom validation rule, error condition formula, ValidationRule]
domain: data-model
summary: >-
  Declarative, per-object rules whose error condition formula is evaluated on save; when the formula returns true,
  Salesforce blocks the save and shows a custom error message on a field or at the top of the page.
release: "Winter '27"
status: current
broader: [kt:data-quality, kt:formula-fields]
related: [kt:custom-fields, kt:duplicate-management, kt:data-migration-strategy]
relations:
  - {predicate: dependsOn, object: kt:order-of-execution}
  - {predicate: configuredVia, object: kt:custom-permissions}
  - {predicate: configuredVia, object: kt:permission-sets}
  - {predicate: contrastsWith, object: kt:apex-triggers}
  - {predicate: contrastsWith, object: kt:record-triggered-flow}
  - {predicate: queriedWith, object: kt:tooling-api}
sources:
  - id: s1
    title: "Validation Rules (Formulas and Validations module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/point_click_business_logic/validation_rules
    type: official-learning
    accessed: 2026-11-10
  - id: s2
    title: "Get Started with Validation Rules (Validation Rules module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/fr/content/learn/modules/validation-rules/get-started-with-validation-rules
    type: official-learning
    accessed: 2026-11-10
  - id: s3
    title: "Implement Best Practices (Validation Rules module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/validation-rules/implement-best-practices
    type: official-learning
    accessed: 2026-11-10
  - id: s4
    title: "Bypass Your Validation Rules (Validation Rules module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/validation-rules/bypass-your-validation-rules
    type: official-learning
    accessed: 2026-11-10
  - id: s5
    title: "Triggers and Order of Execution (Apex Developer Guide, Winter '27)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm
    type: official-docs
    accessed: 2026-11-10
  - id: s6
    title: "ValidationRule (Tooling API Developer Guide, Winter '27)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/tooling_api_objects_validationrule.htm
    type: official-docs
    accessed: 2026-11-10
created: 2026-11-10
---

# Validation Rules

A validation rule checks the data on a record before Salesforce lets it be saved. Each rule holds a formula that looks at one or more fields and returns True or False; True means the data is invalid, so the save is blocked and the rule's error message is shown, while False lets the record save.[^s1] Typical uses are enforcing a format such as a phone number or account-number length, capping a discount percentage, or requiring certain fields at particular stages of a business process, and Trailhead also positions them for regulated industries that must check data against external standards.[^s1][^s2]

## How it works

Admins create rules per object in Object Manager under Validation Rules, entering a rule name, an optional description, the error condition formula and an error message, then using Check Syntax before saving.[^s1][^s2] The formula describes the *bad* data, not the good data, and it can be written as a bare condition without wrapping it in `IF(condition, TRUE, FALSE)`.[^s2] The language is the same one used by formula fields, so examples combine functions such as `AND`, `OR`, `NOT`, `ISBLANK`, `ISNUMBER`, `LEN`, `CONTAINS`, `YEAR` and `TODAY`.[^s1] An error location setting places the message under a specific field or at the top of the page.[^s1][^s2]

Validation rules are metadata. The Tooling API exposes a `ValidationRule` object (available since API version 34.0) with fields such as `Active`, `Description`, `ErrorDisplayField`, `ErrorMessage` and a `Metadata` structure that carries the `errorConditionFormula`.[^s6] If the display field is missing or not on the page layout, the error falls back to the top of the page, and the error message is limited to 255 characters.[^s6]

### Where they run in a save

In the Winter '27 order of execution, custom validation rules run after before-save triggers and alongside a second pass of system validation, and before duplicate rules and after triggers.[^s5] Only for User-object edits from a standard edit page and for multiline items such as quote lines do they also run in the early system-validation step.[^s5] They are not re-run after a workflow field update re-saves the record.[^s5] The practical consequence is that values set by before-save automation are what the rule evaluates, so automation, roll-ups or a related-record update can surface a validation error even though the user never touched the failing field.[^s2][^s3]

## Limits and gotchas

- **Existing data.** A new rule also applies to old records; a user editing an unrelated field on a non-compliant record is blocked, even without edit access to the offending field.[^s3]
- **Guard with change functions.** Wrap conditions in `ISNEW()` or `ISCHANGED(field)` so the rule fires only on create or when the relevant field changes; `PRIORVALUE(field)` compares with the previous value.[^s3]
- **One scenario per rule.** A combined rule cannot say which field is missing or show the error on more than one field, so split it.[^s3]
- **Picklists.** Picklist values need wrapping, for example `TEXT(PRIORVALUE(Picklist__c))`, before `ISBLANK` checks.[^s4]
- **Error message length.** The message is capped at 255 characters.[^s6]

## Design practices

Trailhead recommends messages that state what triggered the rule and how to fix it, an error code such as `[OPP001]` that support staff can trace, and rule names that reuse the code, for example `OPP001_Close_Date_After_Today`.[^s3] Test both the blocked path and the allowed path, including editing other fields on a record that already violates the rule.[^s3]

For historical-data correction or data loads, a bypass can be built from a custom permission: the formula includes `NOT($Permission.Bypass_...)` and the permission is granted through a permission set.[^s4] Trailhead suggests a session-based permission set activated by a flow only when needed, and warns that bypasses should be rare because well-guarded rules seldom need them.[^s4]

## When to use it (and when not)

Use a validation rule for declarative, single-record checks that must hold no matter which channel saves the record, since it runs inside the save itself.[^s5] Logic that must query unrelated records, or that should correct data rather than reject it, belongs in a before-save record-triggered flow or an Apex trigger, which run before validation.[^s5] Duplicate detection is a separate step that runs after validation.[^s5]

## Connections

Validation rules are a core **data quality** control and reuse the **formula fields** language, their two broader nodes.[^s1] They **depend on** the **order of execution**, which fixes where they run relative to **Apex triggers**, **record-triggered flows** and **duplicate management**.[^s5] Bypasses are **configured via** **custom permissions** granted through **permission sets**.[^s4] As metadata they can be **queried with** the **Tooling API**.[^s6] Rules on **custom fields** often matter most during a **data migration**, where loads may need a controlled bypass.[^s4]

## Sources

[^s1]: Trailhead, "Validation Rules" (Formulas and Validations). https://trailhead.salesforce.com/content/learn/modules/point_click_business_logic/validation_rules (accessed 2026-11-10)
[^s2]: Trailhead, "Get Started with Validation Rules". https://trailhead.salesforce.com/fr/content/learn/modules/validation-rules/get-started-with-validation-rules (accessed 2026-11-10)
[^s3]: Trailhead, "Implement Best Practices". https://trailhead.salesforce.com/content/learn/modules/validation-rules/implement-best-practices (accessed 2026-11-10)
[^s4]: Trailhead, "Bypass Your Validation Rules". https://trailhead.salesforce.com/content/learn/modules/validation-rules/bypass-your-validation-rules (accessed 2026-11-10)
[^s5]: Salesforce Developers, "Triggers and Order of Execution" (Winter '27). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm (accessed 2026-11-10)
[^s6]: Salesforce Developers, "ValidationRule" (Tooling API, Winter '27). https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/tooling_api_objects_validationrule.htm (accessed 2026-11-10)
