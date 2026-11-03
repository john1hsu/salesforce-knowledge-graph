---
id: kt:sharing-recalculation
type: Concept
title: Sharing Recalculation
aliases: [sharing rule recalculation, group membership calculation, deferred sharing calculations, defer sharing calculation, Apex sharing recalculation]
domain: security-and-sharing
summary: >-
  The background work Salesforce performs to rebuild record access after changes to org-wide defaults, sharing
  rules, roles, territories, groups or ownership; covers sharing rule and group membership calculation, Apex
  managed sharing recalculation, and the Defer Sharing Calculations tool used for large realignments.
release: "Winter '27"
status: current
broader: [kt:salesforce-sharing-model]
related: [kt:sharing-rules, kt:organization-wide-defaults, kt:role-hierarchy, kt:data-skew, kt:enterprise-territory-management, kt:large-data-volumes]
relations:
  - {predicate: dependsOn, object: kt:batch-apex}
  - {predicate: alternativeTo, object: kt:apex-managed-sharing}
  - {predicate: causes, object: kt:group-membership-locking}
  - {predicate: coveredBy, object: kt:sharing-and-visibility-architect-certification}
sources:
  - id: s1
    title: "Deferred Sharing Calculations (Designing Record Access for Enterprise Scale, Winter '27)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.draes.meta/draes/draes_tools_deferred_sharing_maintenance.htm
    type: official-docs
    accessed: 2026-11-03
  - id: s2
    title: "Group Membership Locking (Designing Record Access for Enterprise Scale, Winter '27)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.draes.meta/draes/draes_group_membership_locking.htm
    type: official-docs
    accessed: 2026-11-03
  - id: s3
    title: "Recalculating Apex Managed Sharing (Apex Developer Guide, Winter '27)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_bulk_sharing_recalc.htm
    type: official-docs
    accessed: 2026-11-03
  - id: s4
    title: "Defer Sharing Calculation (Best Practices for Deployments with Large Data Volumes)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-techniques-deferred-sharing-calculation.html
    type: official-docs
    accessed: 2026-11-03
  - id: s5
    title: "Defer Sharing Calculations tip sheet (Winter '23 edition, PDF)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/242/latest/en-us/sfdc/pdf/salesforce_defer_sharing_tipsheet.pdf
    type: official-docs
    accessed: 2026-11-03
created: 2026-11-03
---

# Sharing Recalculation

Sharing recalculation is the work Salesforce does behind the scenes to bring stored record access back in line with the sharing configuration after something changes. Two engines are involved: **group membership calculation**, which rebuilds the groups implied by roles, territories, public groups and users, and **sharing rule calculation**, which re-evaluates which records each rule shares with which groups.[^s5] Custom objects that use Apex managed sharing have a third, code-driven variant: **Apex sharing recalculation**.[^s3] In small orgs these jobs finish quickly and go unnoticed; in large orgs they are a major factor in planning realignments and data loads.[^s1][^s4]

## How it works

Salesforce's tip sheet lists the triggers. Group membership calculation runs after changes to roles, territories, groups, users or portal account ownership. Sharing rule calculation runs after changes to the org-wide default sharing model, creating, editing or deleting sharing rules, creating or transferring records, changing public group members, creating or activating users, changing or re-parenting roles, territory user and re-parenting changes, and changes to roles, territories or groups referenced by sharing rules.[^s5] Until a calculation completes, users' effective access does not reflect the new configuration.[^s1]

While group membership is being updated, the sharing system locks the tables holding membership data so that concurrent changes cannot produce wrong access. Conflicting operations fail with errors such as "could not acquire lock" or "Group membership operation already in progress" and must be retried. A role change that sets off a sharing rule recalculation can hold those locks for longer. Granular locking, on by default, lets unrelated operations (for example, changes in separate hierarchies) proceed in parallel.[^s2]

For **Apex managed sharing**, an admin associates a class implementing `Database.Batchable` with a custom object under its Apex Sharing Recalculations setting; a class can be associated only once per object. Salesforce runs the class automatically whenever the object's org-wide default changes, and an admin can also start it from the object page, for instance when locking stopped Apex from granting access. The run adds Apex-managed shares and removes redundant ones; progress is monitored on the Apex Jobs page.[^s3]

## Deferring calculations for large realignments

The **Defer Sharing Calculations** page in Setup lets an admin **Suspend** group membership or sharing rule calculations, **Resume** them, and **Recalculate** sharing rules in full. The permission is off by default and is enabled by contacting Salesforce.[^s5] The documented workflow: gather all role, group and sharing rule changes; rehearse in a full copy sandbox to estimate run time; suspend at the start of an agreed maintenance window; apply the changes in bulk; resume; then run a full sharing rule recalculation, either immediately or later.[^s1] The large data volumes guide frames the payoff as making many changes quickly and letting recalculation run overnight or over a weekend.[^s4]

## Limits and gotchas

- Suspending group membership calculation also suspends sharing rule calculation, and resuming group membership needs a full sharing rule recalculation.[^s1][^s5]
- After resuming sharing rule calculation you must click Recalculate; otherwise changes made while suspended are not reflected.[^s5]
- Some calculations cannot be suspended because they protect data integrity, and group membership locking can still happen while calculations are deferred.[^s1]
- Keep the deferral as short as possible, since access is stale until recalculation finishes. Rehearse in a full copy sandbox refreshed within the last 30 days.[^s1]
- Admins get an email only when recalculation completes. Suspend, resume and recalculate actions are logged in the Setup Audit Trail.[^s5]
- Apex sharing recalculation applies only to custom objects, and the object's org-wide default must not already be Public Read/Write.[^s3]
- Locking errors are common during bulk loads, integrations, period-end realignments, and deployments or Apex tests that touch group membership. Build retry logic, stagger these jobs, and fall back to serial processing if parallel loads collide.[^s2]

## When to use it (and when not)

Deferral is worth the extra steps only for large, complex realignments where the business can agree to downtime. If changes normally finish within the workday or weekend, it adds little.[^s1] For routine changes, let calculations run, and schedule group maintenance so that jobs do not overlap; the Recalculate button on its own is meant for cases where sharing rule updates failed or misbehaved.[^s2][^s5] When sharing logic is too complex for criteria or owner-based rules, Apex managed sharing with a recalculation class is the programmatic alternative.[^s3]

## Connections

Sharing recalculation is part of the **Salesforce sharing model** and is triggered by changes to **organization-wide defaults**, **sharing rules**, the **role hierarchy** and **enterprise territory management**.[^s5] It is slowest in **large data volume** orgs and is aggravated by **data skew**, so deferral appears in Salesforce's LDV guidance.[^s4] It **causes** **group membership locking** errors when operations overlap.[^s2] **Apex managed sharing** is the programmatic alternative to rule-based sharing, and its recalculation **depends on** **batch Apex**.[^s3] Planning recalculation is part of the scope of the Sharing and Visibility Architect certification.

## Sources

[^s1]: Salesforce, "Deferred Sharing Calculations (Designing Record Access for Enterprise Scale, Winter '27)". https://developer.salesforce.com/docs/atlas.en-us.264.0.draes.meta/draes/draes_tools_deferred_sharing_maintenance.htm (accessed 2026-11-03)
[^s2]: Salesforce, "Group Membership Locking (Designing Record Access for Enterprise Scale, Winter '27)". https://developer.salesforce.com/docs/atlas.en-us.264.0.draes.meta/draes/draes_group_membership_locking.htm (accessed 2026-11-03)
[^s3]: Salesforce, "Recalculating Apex Managed Sharing (Apex Developer Guide, Winter '27)". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_bulk_sharing_recalc.htm (accessed 2026-11-03)
[^s4]: Salesforce, "Defer Sharing Calculation (Best Practices for Deployments with Large Data Volumes)". https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-techniques-deferred-sharing-calculation.html (accessed 2026-11-03)
[^s5]: Salesforce, "Defer Sharing Calculations tip sheet (Winter '23 edition, PDF)". https://resources.docs.salesforce.com/242/latest/en-us/sfdc/pdf/salesforce_defer_sharing_tipsheet.pdf (accessed 2026-11-03)
