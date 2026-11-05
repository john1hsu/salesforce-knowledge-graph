---
id: kt:implicit-sharing
type: Concept
title: Implicit Sharing
aliases: [built-in sharing, implicit grants, parent implicit sharing, child implicit sharing]
domain: security-and-sharing
summary: >-
  The non-configurable record access Salesforce derives automatically between accounts and their child contacts,
  opportunities and cases (and for Experience Cloud users), rather than from ownership, roles or sharing rules.
release: "Winter '27"
status: current
broader: [kt:salesforce-sharing-model]
related: [kt:role-hierarchy, kt:organization-wide-defaults, kt:experience-cloud, kt:sharing-recalculation]
relations:
  - {predicate: causes, object: kt:data-skew}
  - {predicate: contrastsWith, object: kt:sharing-rules}
  - {predicate: configuredVia, object: kt:role-hierarchy}
  - {predicate: coveredBy, object: kt:sharing-and-visibility-architect-certification}
sources:
  - id: s1
    title: "Implicit Sharing (Designing Record Access for Enterprise Scale)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/draes/guide/draes-object-relationships-implicit-sharing.html
    type: official-docs
    accessed: 2026-11-05
  - id: s2
    title: "Access Grants (Record-Level Access: Under the Hood)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/salesforce-record-access-under-the-hood/guide/uth-grants.html
    type: official-docs
    accessed: 2026-11-05
  - id: s3
    title: "Platform Sharing Architecture"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/platform-sharing-architecture
    type: official-docs
    accessed: 2026-11-05
  - id: s4
    title: "Parent-Child Data Skew (Designing Record Access for Enterprise Scale)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/draes/guide/draes-object-relationships-parent-child-data-skew.html
    type: official-docs
    accessed: 2026-11-05
created: 2026-11-05
---

# Implicit Sharing

Implicit sharing is record access that Salesforce defines and maintains on its own, as opposed to access an administrator grants through ownership, sharing rules, teams, manual shares or Apex.[^s1] Salesforce's record-access internals describe it as a set of non-configurable behaviors built into the Sales, Service and portal applications, sometimes called "built-in sharing", and classify it as a third kind of grant alongside explicit grants and group membership grants.[^s2] Because it is built in, it cannot be switched on or off, and it does not apply to custom objects.[^s3]

## How it works

**Parent implicit sharing.** A user who can see a child case, contact or opportunity automatically gets read-only access to the parent account.[^s1] The architect fundamentals page lists orders among the child objects that trigger this upward visibility as well.[^s3] The access is view-only: a user who reaches an opportunity through an owner-based sharing rule can open its account but cannot edit it.[^s1] It is not produced by the View All permission on the child object, and it does not apply where the child is set to Controlled by Parent.[^s1]

**Child implicit sharing.** The account owner gets access to the account's child contacts, opportunities and cases.[^s1] The level is configured on the owner's role in the role hierarchy, where each of those child objects is set to View, Edit or No access when the role is defined.[^s3] The same mechanism lets account sharing rules and account teams carry child-record access according to their settings, and losing access to the account removes the derived access to its children.[^s1] View All on the parent object does not grant it.[^s1]

**External-user variants.** Experience Cloud site sharing gives customer and partner users access to their own account and its contacts, and gives a portal user access to cases on which they are the contact; the account and contacts are shared with the lowest role under the external account.[^s1] High Volume sharing serves role-less license types (Customer Community, High Volume Customer Portal, Authenticated Website) through sharing sets, and High Volume Parent sharing gives share-group members read-only access to the parent accounts of records shared that way.[^s1]

## Limits and gotchas

- **Account hierarchy is not a sharing hierarchy.** Access to a parent account does not flow down to its child accounts; only the role and territory hierarchies propagate access that way.[^s3]
- **Removal is the expensive operation.** When a user loses access to one child, Salesforce has to examine every other child of that account before it can drop the parent implicit share, which becomes costly on accounts with many children.[^s1]
- **Parent-child data skew.** Salesforce flags performance risk when roughly 10,000 or more child records hang off a single account, a pattern often created by parking unassigned contacts under a placeholder account; frequent visibility changes on such an account repeatedly trigger the sibling check.[^s4] The architecture guidance gives a 1:10,000 parent-to-child ratio as the point where performance degrades and recommends staying below it.[^s3]
- **Not visible as configuration.** Because no rule record exists, access that users "mysteriously" have to an account is often parent implicit sharing from a child they can see; it must be reasoned about rather than switched off.[^s2][^s3]

## When to use it (and when not)

Implicit sharing is not chosen; it is a consequence of using the standard account model. Design around it: keep Private organization-wide defaults meaningful by remembering that any child grant exposes the account read-only, set role-level child access deliberately, and distribute child records across real accounts instead of catch-all accounts to avoid skew.[^s1][^s3][^s4] When parent-to-child access needs to be uniform and simple, Controlled by Parent avoids the parent implicit share altogether for that child object.[^s1]

## Connections

Implicit sharing is one layer of the **Salesforce sharing model**, sitting beside explicit grants such as **sharing rules**, which an administrator configures, whereas implicit access cannot be.[^s2] Child access is configured on roles in the **role hierarchy**, and its interaction with Private or Controlled by Parent **organization-wide defaults** determines whether it applies.[^s1][^s3] Its sibling-scanning behavior is a major cause of the cost behind **data skew** and long **sharing recalculation** work on large accounts.[^s3][^s4] The external-user variants matter for **Experience Cloud** designs, and the topic is core material for the **Sharing and Visibility Architect certification**.[^s1]

## Sources

[^s1]: Salesforce, "Implicit Sharing", Designing Record Access for Enterprise Scale. https://developer.salesforce.com/docs/platform/draes/guide/draes-object-relationships-implicit-sharing.html (accessed 2026-11-05)
[^s2]: Salesforce, "Access Grants", Record-Level Access: Under the Hood. https://developer.salesforce.com/docs/platform/salesforce-record-access-under-the-hood/guide/uth-grants.html (accessed 2026-11-05)
[^s3]: Salesforce Architects, "Platform Sharing Architecture". https://architect.salesforce.com/fundamentals/platform-sharing-architecture (accessed 2026-11-05)
[^s4]: Salesforce, "Parent-Child Data Skew", Designing Record Access for Enterprise Scale. https://developer.salesforce.com/docs/platform/draes/guide/draes-object-relationships-parent-child-data-skew.html (accessed 2026-11-05)
