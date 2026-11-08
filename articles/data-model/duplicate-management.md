---
id: kt:duplicate-management
type: Feature
title: Duplicate Management
aliases: [duplicate rules, matching rules, duplicate rule, matching rule, Salesforce dedupe, DuplicateRule]
domain: data-model
summary: >-
  Salesforce's built-in duplicate detection, in which matching rules define how two records are compared and
  duplicate rules decide whether a potential duplicate is allowed with a warning, blocked, or logged for reporting.
release: "Winter '27"
status: current
broader: [kt:data-quality, kt:data-architecture]
related: [kt:lead-conversion, kt:person-accounts, kt:standard-objects, kt:data-migration-strategy, kt:salesforce-sharing-model]
relations:
  - {predicate: contrastsWith, object: kt:identity-resolution}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: queriedWith, object: kt:apex}
  - {predicate: coveredBy, object: kt:platform-administrator-certification}
sources:
  - id: s1
    title: "Resolve and Prevent Duplicate Data in Salesforce — Duplicate Management module"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/sales_admin_duplicate_management/sales_admin_duplicate_management_unit_2
    type: official-learning
    accessed: 2026-11-08
  - id: s2
    title: "DuplicateRule — Metadata API Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_duplicaterule.htm
    type: official-docs
    accessed: 2026-11-08
  - id: s3
    title: "FindDuplicates Class — Apex Reference Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexcode/apex_class_Datacloud_FindDuplicates.htm
    type: official-docs
    accessed: 2026-11-08
  - id: s4
    title: "DuplicateRecordSet — Object Reference for the Salesforce Platform"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_duplicaterecordset.htm
    type: official-docs
    accessed: 2026-11-08
created: 2026-11-08
---

# Duplicate Management

Duplicate Management is the declarative, in-org mechanism Salesforce uses to stop or flag duplicate CRM records as
they are created or edited. It has two moving parts that only work together: a **matching rule** defines how records
are compared and what counts as a potential duplicate, and a **duplicate rule** defines what happens when one is
found. A matching rule does nothing on its own; it must be referenced by an active duplicate rule.[^s1]

## How it works

Salesforce ships standard matching rules for business accounts, contacts, leads and person accounts. Orgs created in
Winter '15 or earlier have to activate the standard rules they want.[^s1] Each field in a matching rule uses a
matching method. Standard contact and lead rules combine exact matching with fuzzy algorithms: first names can be
compared by initials, Jaro-Winkler distance, Metaphone 3 or name variants (with first and last name transposition
checked), titles by acronym or Kullback-Leibler distance so that abbreviations line up, and mailing streets by edit
distance with weighted sections (street name 50%, number 20%, suffix 15%, suite 15%).[^s1] Admins can add custom
matching rules, for example fuzzy phone matching that ignores country codes.[^s1]

A duplicate rule names its object, one or more matching rules (optionally against a different object, such as
checking new leads against contacts) and separate behaviour for create and for edit. In the `DuplicateRule`
metadata type, `actionOnInsert` and `actionOnUpdate` take `Allow` or `Block`; with `Allow`, the `operationsOnInsert`
and `operationsOnUpdate` arrays can include `alert` (show the warning) and `report` (log the save for duplicate
reporting). Rules carry a `sortOrder`, an optional filter, and alert text that can only be set when the action is
`Allow`.[^s2] In the UI, users see the alert and can continue or cancel; through the API the save fails with a
duplicate error until the request explicitly sets `allowSave` to true.[^s2]

When users bypass a warning and the rule reports, Salesforce records the match in `DuplicateRecordSet` records, each
of which groups one or more `DuplicateRecordItem` children; these objects back custom report types and also hold the
output of duplicate jobs.[^s4] Trailhead's admin path shows building a report type on Accounts or Leads with
Duplicate Record Items to review saves where warnings were ignored.[^s1]

## Limits and gotchas

- A duplicate rule can reference up to **3** matching rules, and an object can have up to **5** active matching
  rules.[^s1]
- The `securityOption` field matters: `EnforceSharingRules` means a duplicate the user cannot see will not block
  their save, while `BypassSharingRules` ignores sharing (other access restrictions still apply) so hidden duplicates
  are still caught.[^s2]
- Standard matching rules do not consider custom fields; you need a custom matching rule for that.[^s3]
- In Apex, `Datacloud.FindDuplicates.findDuplicates()` checks a list of unsaved sObjects against the object's active
  duplicate rules. It accepts at most 50 records per call, all of one object type, and throws an exception when the
  object has no active duplicate rule. Results come back in input order, nested as one `DuplicateResult` per
  duplicate rule and one `MatchResult` per matching rule; custom fields are not returned by default.[^s3]
- Matching rules themselves cannot be configured through the Datacloud Apex API; that is Setup or metadata work.[^s3]

## When to use it (and when not)

Use Duplicate Management as the first line of defence on human-entered sales and service data: warnings for
low-confidence matches, blocking for high-confidence ones, and reporting to measure how often users override.[^s1]
Before a bulk load, decide whether rules should block, alert-and-report, or be temporarily deactivated, because
API callers must opt in with `allowSave` to save records that only trigger an alert.[^s2] For pre-save checks in
custom code, such as a custom LWC form or integration endpoint, `FindDuplicates` reuses the same rules rather than
reimplementing matching logic, within its 50-record batch size.[^s3] For cross-system unification of profiles,
in-org rules are the wrong tool.

## Connections

Duplicate Management is a `kt:data-quality` control and part of a wider `kt:data-architecture`. It runs against
`kt:standard-objects` such as leads, contacts and accounts, has dedicated standard rules for `kt:person-accounts`,
and supports cross-object rules such as checking leads against contacts, which is why it constrains
`kt:lead-conversion`.[^s1][^s2]
Its `securityOption` ties detection to the `kt:salesforce-sharing-model`.[^s2] It contrasts with
`kt:identity-resolution` in Data 360, which links profiles across sources instead of preventing duplicate rows in one
org. Rules deploy through the `kt:metadata-api` as `.duplicateRule` files in `duplicateRules/`, and the same rules are
invoked from `kt:apex` via the Datacloud namespace.[^s2][^s3] Load planning in `kt:data-migration-strategy` should
account for active rules, and duplicate rules are core admin territory tested in the
`kt:platform-administrator-certification`, the audience of the Trailhead admin module.[^s1]

## Sources
[^s1]: Trailhead, "Resolve and Prevent Duplicate Data in Salesforce". https://trailhead.salesforce.com/content/learn/modules/sales_admin_duplicate_management/sales_admin_duplicate_management_unit_2 (accessed 2026-11-08)
[^s2]: Salesforce Developers, "DuplicateRule — Metadata API Developer Guide". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_duplicaterule.htm (accessed 2026-11-08)
[^s3]: Salesforce Developers, "FindDuplicates Class — Apex Reference Guide". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexcode/apex_class_Datacloud_FindDuplicates.htm (accessed 2026-11-08)
[^s4]: Salesforce Developers, "DuplicateRecordSet — Object Reference". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_duplicaterecordset.htm (accessed 2026-11-08)
