---
id: kt:sharing-rules
type: SecurityControl
title: Sharing Rules
aliases: [sharing rule, owner-based sharing rules, ownership-based sharing rules, criteria-based sharing rules, guest user sharing rules, SharingRules metadata type]
domain: security-and-sharing
summary: >-
  Declarative, per-object exceptions to the organization-wide defaults that automatically grant Read Only or
  Read/Write access to a role, territory or public group, selecting records either by who owns them or by
  field criteria.
release: "Winter '27"
status: current
broader: [kt:salesforce-sharing-model]
related: [kt:organization-wide-defaults, kt:role-hierarchy, kt:public-groups, kt:experience-cloud]
relations:
  - {predicate: causes, object: kt:sharing-recalculation}
  - {predicate: alternativeTo, object: kt:apex-managed-sharing}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: coveredBy, object: kt:sharing-and-visibility-architect-certification}
sources:
  - id: s1
    title: "Create Sharing Rules (Data Security module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/content/learn/v/modules/data_security/data_security_sharing_rules
    type: official-learning
    accessed: 2026-11-02
  - id: s2
    title: "Create Sharing Rules (Share CRM Data with Your Partners project)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/communities_share_crm_data/sharing_rules
    type: official-learning
    accessed: 2026-11-02
  - id: s3
    title: "Sharing Rules (Salesforce Security Guide, archived Summer '20 version)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.226.0.securityImplGuide.meta/securityImplGuide/security_sharing_rules_create.htm
    type: official-docs
    accessed: 2026-11-02
  - id: s4
    title: "Group Membership Operations and Sharing Recalculation (Record Access Design)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/draes/guide/draes-group-membership.html
    type: official-docs
    accessed: 2026-11-02
  - id: s5
    title: "Deferred Sharing Calculations (Record Access Design)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.draes.meta/draes/draes_tools_deferred_sharing_maintenance.htm
    type: official-docs
    accessed: 2026-11-02
  - id: s6
    title: "SharingRules (Metadata API Developer Guide, Winter '27)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_sharingrules.htm
    type: official-docs
    accessed: 2026-11-02
created: 2026-11-02
---

# Sharing Rules

Sharing rules are the declarative, lateral layer of the Salesforce record-access model. They let an admin carve automatic exceptions out of a restrictive organization-wide default (OWD) so that a selected set of users gets extra access to a selected set of records, independent of where those users sit in the role hierarchy.[^s1][^s2] A rule can only widen access; it can never make the baseline stricter than the OWD.[^s1]

## How it works

Every rule answers three questions: which records, which users, and what access level.[^s1] Records are chosen in one of two ways. An **owner-based** rule shares the records owned by members of one group (a role, role and subordinates, or public group) with another group. A **criteria-based** rule shares records whose field values match filter conditions, which can be combined with custom AND/OR logic.[^s3][^s2] Further variants exist for specific cases: guest user rules open records to unauthenticated site visitors, user sharing rules can be based on group membership, and account territory rules share accounts by territory.[^s3]

Recipients are expressed as roles, roles and subordinates, territories or public groups. Public groups can bundle individual users, roles, roles with subordinates, territories and other public groups, which is why Trailhead recommends a group whenever a rule targets more than one or two roles or any individual user.[^s1] Access levels are Read Only or Read/Write for the object itself; account rules also set the implicit level for associated contacts, opportunities and cases (where Private is allowed), and campaigns additionally allow Full Access.[^s3][^s2] Rules are maintained in Setup under Sharing Settings, with public groups under Public Groups.[^s1]

Rules work the same way for external users as for internal ones. In Experience Cloud sites the platform generates site-specific groups such as portal roles, which a rule can combine with internal roles, so partner and Customer Community Plus users can be given access to internally owned records and vice versa.[^s2]

In metadata, all rule kinds for an object deploy through the **SharingRules** container type, which covers criteria-based, ownership-based, territory-based and guest user rules; it is current in the Winter '27 (API 68.0) Metadata API guide.[^s6]

## Limits and gotchas

- The Salesforce Security Guide (archived Summer '20 version, checked this run) caps an object at 300 sharing rules in total, of which up to 50 may be criteria-based or guest user rules; confirm against your org's current allocations before relying on headroom.[^s3]
- Guest user rules grant Read Only access only. When secure guest record access is enabled they are the only way to open records to guests, and the guide warns they expose every matching record immediately.[^s3]
- Contact access cannot be set in a rule when the Contact OWD is Controlled by Parent, and any public group a rule needs must exist before the rule is created.[^s3]
- Criteria fields that a rule cannot evaluate directly can be copied into a supported text or number field by automation and filtered on instead.[^s3]
- Rules are tied to roles, groups and territories, so reorganizations are expensive: when a user changes role, the platform recalculates every rule whose source group includes the old or new role, and some rules can become invalid and need editing or deletion.[^s4]
- For large realignments, admins can defer sharing rule (and group membership) calculations, make all changes in a maintenance window, then run a full recalculation; access is not accurate until that recalculation completes.[^s5]

## When to use it (and when not)

Sharing rules fit populations that are predictable and stable. Trailhead's recruiting example shares job applications with a recruiter role, but notes that interviewers, whose membership changes by position, are a poor fit and need another mechanism such as manual sharing.[^s1] Use the role hierarchy for vertical management visibility, sharing rules for repeatable lateral or field-driven exceptions, and manual or programmatic sharing when membership varies record by record in ways criteria cannot express.[^s1]

## Connections

Sharing rules are one layer of the broader **Salesforce sharing model**, sitting above the **organization-wide defaults** they open up and beside the **role hierarchy**, which supplies vertical rather than lateral access.[^s1] Their recipients are usually **public groups**, and in **Experience Cloud** sites they reach external users through site-specific portal groups.[^s2] Changes to rules or to the groups and roles they reference **cause sharing recalculation**, which can be deferred during maintenance.[^s4][^s5] When record selection needs logic beyond field criteria, **Apex managed sharing** is the programmatic **alternative**. Rules are **configured via** the **Metadata API** `SharingRules` type,[^s6] and designing them at scale falls under the Sharing and Visibility Architect certification.

## Sources

[^s1]: Trailhead, "Create Sharing Rules (Data Security module)". https://trailhead.salesforce.com/en/content/learn/v/modules/data_security/data_security_sharing_rules (accessed 2026-11-02)
[^s2]: Trailhead, "Create Sharing Rules (Share CRM Data with Your Partners project)". https://trailhead.salesforce.com/content/learn/projects/communities_share_crm_data/sharing_rules (accessed 2026-11-02)
[^s3]: Salesforce, "Sharing Rules (Salesforce Security Guide, archived Summer '20 version)". https://developer.salesforce.com/docs/atlas.en-us.226.0.securityImplGuide.meta/securityImplGuide/security_sharing_rules_create.htm (accessed 2026-11-02)
[^s4]: Salesforce, "Group Membership Operations and Sharing Recalculation (Record Access Design)". https://developer.salesforce.com/docs/platform/draes/guide/draes-group-membership.html (accessed 2026-11-02)
[^s5]: Salesforce, "Deferred Sharing Calculations (Record Access Design)". https://developer.salesforce.com/docs/atlas.en-us.draes.meta/draes/draes_tools_deferred_sharing_maintenance.htm (accessed 2026-11-02)
[^s6]: Salesforce, "SharingRules (Metadata API Developer Guide, Winter '27)". https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_sharingrules.htm (accessed 2026-11-02)
