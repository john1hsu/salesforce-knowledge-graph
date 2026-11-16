---
id: kt:scoping-rules
type: Feature
title: Scoping Rules
aliases: [scoping rule, enforcementType Scoping, Filter by scope, USING SCOPE scopingRule]
domain: security-and-sharing
summary: >-
  Admin-defined user and record criteria that set which records a user sees by default in list views, reports
  and SOQL on supported objects, without removing any access granted by the sharing model.
release: "Winter '27"
status: current
broader: [kt:salesforce-sharing-model]
related: [kt:organization-wide-defaults, kt:screen-flow, kt:duplicate-management, kt:large-data-volumes]
relations:
  - {predicate: contrastsWith, object: kt:restriction-rules}
  - {predicate: configuredVia, object: kt:tooling-api}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: queriedWith, object: kt:soql}
sources:
  - id: s1
    title: "Scoping Rules (Scoping Rules Developer Guide, Winter '27)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.scoping_rules.meta/scoping_rules/scoping_rules_about.htm
    type: official-docs
    accessed: 2026-11-16
  - id: s2
    title: "Considerations for Scoping Rules (Scoping Rules Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.scoping_rules.meta/scoping_rules/scoping_rules_considerations.htm
    type: official-docs
    accessed: 2026-11-16
  - id: s3
    title: "Use the SOQL Operator in Scoping Rule Record Criteria (Scoping Rules Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.scoping_rules.meta/scoping_rules/scoping_rules_quickstart_use_soql_operator.htm
    type: official-docs
    accessed: 2026-11-16
  - id: s4
    title: "USING SCOPE (SOQL and SOSL Reference)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/api/sforce_api_calls_soql_select_using_scope.htm
    type: official-docs
    accessed: 2026-11-16
  - id: s5
    title: "Learn MOAR in Winter '23 with Scoping Rules"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2022/learn-moar-in-winter-23-with-scoping-rules
    type: official-blog
    accessed: 2026-11-16
  - id: s6
    title: "Scoping Rule Examples (Scoping Rules Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.scoping_rules.meta/scoping_rules/scoping_rules_examples.htm
    type: official-docs
    accessed: 2026-11-16
created: 2026-11-16
---

# Scoping Rules

Scoping rules let an admin decide which records a user sees **by default**, so people can concentrate on the records relevant to their job rather than everything they are allowed to open.[^s1] They do not change access: a user can still view and report on any record that the sharing settings allow, and can widen the view or search to reach records outside the scope.[^s1] That makes them a usability feature built on sharing-model plumbing, rather than a security control. They run in Lightning Experience on Performance, Unlimited and Developer editions, on custom objects and on the standard Account, Case, Contact, Event, Lead, Opportunity and Task objects.[^s1]

## How it works

Each rule pairs a **user criterion**, which picks the users it applies to, with a **record criterion**, which picks the records those users see.[^s5] Users who match the user criterion get a **Filter by scope** option in list views and reports; selecting it narrows the results to the record criterion.[^s5] In SOQL, the developer guide says the rule applies by default unless the query names a different scope,[^s1] and the `USING SCOPE` clause offers a `scopingRule` filter that exists only once an admin has activated a scoping rule on the queried object.[^s4]

Salesforce's examples include showing tasks for one bank branch held in a custom `Branch__c` field, showing contacts whose owner works in the user's department, filtering by division, and matching a comma-separated list of name values.[^s6] A regional variant compares an account field to a custom field on the user, and a screen flow in the utility bar can let users change that user field themselves, which effectively switches their scope.[^s5][^s1]

Rules are built in Object Manager or through the `RestrictionRule` object in the Tooling API or Metadata API, and they move between orgs in change sets or unlocked packages.[^s1] For record criteria that depend on another object, such as a junction object, a `SOQL()` operator is available only when the rule is created through the API. Its subquery must include `USING SCOPE EVERYTHING`, it may reference only `$User.Id`, and the queried object cannot be the rule's own target object.[^s3][^s2] Managing scoping rules requires the Manage Sharing permission.[^s3]

## Limits and gotchas

- Up to 2 active scoping rules per object in Developer editions and up to 5 in Performance and Unlimited editions.[^s2]
- Only one scoping or restriction rule per object should match a given user. Salesforce doesn't validate this, and when two match only one is observed.[^s1][^s2]
- Without the SOQL operator, criteria allow only EQUALS, with no AND or OR; null or blank record criteria values are unsupported.[^s2]
- Dot notation reaches one lookup level, owner references need a type such as `Owner:User`, and queues are unsupported.[^s2]
- Related lists ignore scope, except contact roles: a Contact rule silently filters contact roles on accounts, opportunities, cases and contracts.[^s2]
- Scoping rules also trim the potential duplicates shown by duplicate rules, even when those rules bypass sharing.[^s2]
- To disable a rule, first delete the list views and reports that use Filter by scope; otherwise they break and can't be edited.[^s2]
- Don't edit `targetEntity` after creation; delete and recreate. Deleting a referenced custom permission or picklist value breaks the rule.[^s2]
- Salesforce can disable rules that perform poorly on large data volumes, so test in a sandbox and check SOQL-based criteria in an API client first.[^s2][^s3]

## When to use it (and when not)

Use a scoping rule when users legitimately need broad access but work mostly in one slice, such as an agent who serves several agencies but usually focuses on one; it replaces a pile of personalised list views and reports.[^s1][^s5] When users must be prevented from seeing records, a scoping rule is the wrong tool, because its filter can be dropped; use a restriction rule, or tighter org-wide defaults and sharing.[^s1][^s2]

## Connections

Scoping rules sit alongside the **Salesforce sharing model** and the **organization-wide defaults** it starts from, but only shape default visibility on top of them.[^s1] They **contrast with restriction rules**, which share the `RestrictionRule` type and a per-user limit yet actually remove access.[^s1][^s2] They are **configured via** the **Tooling API** and **Metadata API**, honoured in **SOQL** through `USING SCOPE`, and often paired with a **screen flow** that lets users switch scope.[^s1][^s4][^s5] Their reach into **duplicate management** and their tuning for **large data volumes** are covered in the considerations.[^s2]

## Sources

[^s1]: Salesforce, "Scoping Rules (Scoping Rules Developer Guide, Winter '27)". https://developer.salesforce.com/docs/atlas.en-us.264.0.scoping_rules.meta/scoping_rules/scoping_rules_about.htm (accessed 2026-11-16)
[^s2]: Salesforce, "Considerations for Scoping Rules (Scoping Rules Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.scoping_rules.meta/scoping_rules/scoping_rules_considerations.htm (accessed 2026-11-16)
[^s3]: Salesforce, "Use the SOQL Operator in Scoping Rule Record Criteria (Scoping Rules Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.scoping_rules.meta/scoping_rules/scoping_rules_quickstart_use_soql_operator.htm (accessed 2026-11-16)
[^s4]: Salesforce, "USING SCOPE (SOQL and SOSL Reference)". https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/api/sforce_api_calls_soql_select_using_scope.htm (accessed 2026-11-16)
[^s5]: Salesforce Admins Blog, "Learn MOAR in Winter '23 with Scoping Rules". https://admin.salesforce.com/blog/2022/learn-moar-in-winter-23-with-scoping-rules (accessed 2026-11-16)
[^s6]: Salesforce, "Scoping Rule Examples (Scoping Rules Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.scoping_rules.meta/scoping_rules/scoping_rules_examples.htm (accessed 2026-11-16)
