---
id: kt:restriction-rules
type: SecurityControl
title: Restriction Rules
aliases: [restriction rule, RestrictionRule, record restriction rules, enforcementType Restrict]
domain: security-and-sharing
summary: >-
  Record-level filters that narrow the records specified users can access on supported objects (custom and
  external objects, contracts, events, quotes, tasks, time sheets) after organization-wide defaults and sharing
  have granted access, defined by a user criterion and a record criterion.
release: "Winter '27"
status: current
broader: [kt:salesforce-sharing-model]
related: [kt:organization-wide-defaults, kt:sharing-rules, kt:external-objects, kt:enterprise-territory-management]
relations:
  - {predicate: contrastsWith, object: kt:scoping-rules}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: configuredVia, object: kt:tooling-api}
  - {predicate: coveredBy, object: kt:sharing-and-visibility-architect-certification}
sources:
  - id: s1
    title: "About This Guide (Restriction Rules Developer Guide, Winter '27)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.restriction_rules.meta/restriction_rules/restriction_rules_intro.htm
    type: official-docs
    accessed: 2026-11-02
  - id: s2
    title: "Restriction Rules Considerations (Restriction Rules Developer Guide, Winter '27)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.restriction_rules.meta/restriction_rules/restriction_rules_considerations.htm
    type: official-docs
    accessed: 2026-11-02
  - id: s3
    title: "Restriction Rules Developer Guide, Version 67.0 (Summer '26), PDF"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/262/latest/en-us/sfdc/pdf/restriction_rules.pdf
    type: official-docs
    accessed: 2026-11-02
  - id: s4
    title: "Restriction Rule Examples (Restriction Rules Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.restriction_rules.meta/restriction_rules/restriction_rules_examples.htm
    type: official-docs
    accessed: 2026-11-02
  - id: s5
    title: "RestrictionRule (Metadata API Developer Guide, Winter '27)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_restrictionrule.htm
    type: official-docs
    accessed: 2026-11-02
created: 2026-11-02
---

# Restriction Rules

Restriction rules are a record-level access control that lets an admin limit certain users to a specified subset of records, keeping sensitive or irrelevant data out of their view.[^s1] They are the one declarative sharing feature that subtracts access: every other layer of the Salesforce sharing model opens records up from the organization-wide default, whereas a restriction rule filters what those layers have already granted.[^s3] They run in Lightning Experience on Enterprise, Performance, Unlimited and Developer editions, and Salesforce advises turning off Salesforce Classic first because rules may not behave as intended for Classic users.[^s1][^s2]

## How it works

Users first receive access through org-wide defaults and mechanisms such as sharing rules or enterprise territory management; a restriction rule then narrows that set to the records matching its filter. The developer guide likens this to a list view or report filter that the user cannot remove.[^s3] Each rule has two halves: a **user criterion** (`userCriteria`) choosing who it applies to, for example a profile, a role or all active users, and a **record criterion** (`recordFilter`) choosing which records they may see, such as records they own.[^s3]

Supported objects are custom objects, external objects, contracts, events, quotes, tasks, time sheets and time sheet entries.[^s1] Typical patterns in Salesforce's examples include limiting a group to contracts of one record type, letting a profile see only its own tasks, showing events owned by people in the same role or profile, and matching a custom department field on the record to the user's department, which must be kept populated by automation.[^s4]

Rules are created from the object in Object Manager, through the `RestrictionRule` Tooling API object, or as `RestrictionRule` metadata deployed in `.rule` files under a `restrictionRules` folder; managing them requires the Manage Sharing permission.[^s3] The same metadata type also represents scoping rules: `enforcementType` is `Restrict` for a restriction rule and `Scoping` for a scoping rule, which sets the default records a user sees without removing access.[^s5]

Once active, a rule is enforced across links, list views, lookups, record pages, related lists, reports, search, SOQL and SOSL.[^s2]

## Limits and gotchas

- Active rules per object: two in Enterprise and Developer editions, five in Performance and Unlimited. For any given user, at most one restriction or scoping rule per object should have a user criterion that evaluates to true.[^s2]
- Criteria support only the equals operator; AND, OR and formulas are unsupported, as are null or blank values in record criteria. Record criteria may hold comma-separated values or IDs.[^s2][^s4]
- Dot notation can traverse one lookup level from the target object, owner references must name a type (for example `Owner:User`) because queues are unsupported, and IDs must be the 15-character form.[^s2]
- Restricting a parent does not restrict its children; notes on a restricted contract need another mechanism.[^s2]
- Rules do not apply to code in system mode, and users with View All Data or View All Records (or Modify All) still see everything.[^s2]
- `UserRecordAccess` does not reflect restriction rules, so it can report access a user is actually denied; Open Activities and Activity History apply rules after fetching 50 rows, so Salesforce recommends Activity Timeline.[^s2]
- Org-specific IDs such as roles, profiles and record types must be changed when moving rules between orgs; deleting a picklist value used in a rule breaks the rule.[^s2]
- On large data volumes, expect roughly 3–5% overhead on top of the record filter's own query cost; test the record criteria as a query and ask Support about indexing slow fields.[^s2]
- External objects work with the OData 2.0, OData 4.0 and Cross-Org adapters only, and each rule evaluation can add calls to a source that bills per call.[^s2]

## When to use it (and when not)

Use a restriction rule when the access granted by the baseline and sharing is right for most users but a defined population must see less, such as a profile that should only see its own tasks.[^s3][^s4] If the goal is only to declutter default views without hiding data, a scoping rule is the right tool.[^s5] If users should see more, the answer is sharing rules or the role hierarchy, not a restriction rule. Because the criteria language is limited to single-field equality, complex conditions usually require a helper field maintained by automation.[^s4][^s2]

## Connections

Restriction rules sit inside the **Salesforce sharing model** as the narrowing layer applied after **organization-wide defaults**, **sharing rules** and **enterprise territory management** have granted access.[^s3] They extend to **external objects** reached through Salesforce Connect adapters.[^s2] They **contrast with scoping rules**, which share the same metadata type but only change default visibility.[^s5] They are **configured via** the **Metadata API** and the **Tooling API**,[^s3] and designing record visibility with them falls under the Sharing and Visibility Architect certification.

## Sources

[^s1]: Salesforce, "About This Guide (Restriction Rules Developer Guide, Winter '27)". https://developer.salesforce.com/docs/atlas.en-us.264.0.restriction_rules.meta/restriction_rules/restriction_rules_intro.htm (accessed 2026-11-02)
[^s2]: Salesforce, "Restriction Rules Considerations (Restriction Rules Developer Guide, Winter '27)". https://developer.salesforce.com/docs/atlas.en-us.264.0.restriction_rules.meta/restriction_rules/restriction_rules_considerations.htm (accessed 2026-11-02)
[^s3]: Salesforce, "Restriction Rules Developer Guide, Version 67.0 (Summer '26), PDF". https://resources.docs.salesforce.com/262/latest/en-us/sfdc/pdf/restriction_rules.pdf (accessed 2026-11-02)
[^s4]: Salesforce, "Restriction Rule Examples (Restriction Rules Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.restriction_rules.meta/restriction_rules/restriction_rules_examples.htm (accessed 2026-11-02)
[^s5]: Salesforce, "RestrictionRule (Metadata API Developer Guide, Winter '27)". https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_restrictionrule.htm (accessed 2026-11-02)
