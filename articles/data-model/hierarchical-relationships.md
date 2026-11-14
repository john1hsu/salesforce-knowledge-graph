---
id: kt:hierarchical-relationships
type: Feature
title: Hierarchical Relationships
aliases: [hierarchical relationship, hierarchical relationship field, user hierarchy field, manager hierarchy, user-to-user lookup]
domain: data-model
summary: >-
  A special lookup relationship field type available only on the User object, used to link one user to another (as the
  standard Manager field does) so that management chains can drive approval routing and other user-to-user logic.
release: "Winter '27"
status: current
broader: [kt:object-relationships]
related: [kt:lookup-vs-master-detail, kt:standard-objects, kt:polymorphic-relationships, kt:user-management]
relations:
  - {predicate: consumedBy, object: kt:approval-processes}
  - {predicate: contrastsWith, object: kt:role-hierarchy}
sources:
  - id: s1
    title: "Data Modeling: Create Object Relationships (unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data_modeling/object_relationships
    type: official-learning
    accessed: 2026-11-14
  - id: s2
    title: "Salesforce Field Reference Guide: User"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.sfFieldRef.meta/sfFieldRef/salesforce_field_reference_User.htm
    type: official-docs
    accessed: 2026-11-14
  - id: s3
    title: "Force.com Platform Fundamentals: Try It Out — Create an Approval Process (archived v36 docs)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.200.0.fundamentals.meta/fundamentals/adg_workflow_approval_process_try_it_out.htm
    type: official-docs
    accessed: 2026-11-14
  - id: s4
    title: "Object Reference: Relationships Among Standard Objects and Fields"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/relationships_among_objects.htm
    type: official-docs
    accessed: 2026-11-14
  - id: s5
    title: "Create a User Role"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=admin_roles.htm
    type: official-docs
    accessed: 2026-11-14
  - id: s6
    title: "Relationships in Salesforce"
    publisher: Salesforce Ben (Jonathan Fox)
    url: https://salesforceben.com/relationships-in-salesforce
    type: community
    accessed: 2026-11-14
created: 2026-11-14
---

# Hierarchical Relationships

A **hierarchical relationship** is the third relationship field type on the Salesforce platform, alongside lookup and
master-detail. Trailhead describes it as a special kind of lookup that exists only on the User object, used to model
management chains between users.[^s1] Practitioners often overlook it because it never appears when you add a field to
an Account, Case or custom object; it is offered only when you create a custom field on User.[^s6]

## How it works

Every org already has one hierarchical field: the standard **Manager** field on User. In the field reference it is the
`ManagerId` reference field (label "Manager ID"), an 18-character ID pointing to another User record; User also carries
a similar standard reference, `DelegatedApproverId`, for the delegated approver.[^s2] An admin can add further custom
hierarchical fields, for example a dotted-line "Mentor" or "Regional Director" field, and each behaves like the Manager
field: it links one user to another user.[^s3]

What makes the field "hierarchical" rather than a plain user lookup is its cycle protection. Salesforce's platform
fundamentals guide explains that the Manager field builds a hierarchy that stops you from choosing someone who reports to
the user directly or indirectly, so no user can end up as their own indirect manager; a custom hierarchical field enforces
the same rule.[^s3] That guarantee is what lets automation walk up the chain without looping.

## Where it is used

The main consumer is approval routing. When an approval step automatically assigns the approver from a user field, the
request can go to the submitter's manager, or (with the option to use the approver field of the record owner) to the
manager named on the record owner's user record.[^s3] A custom hierarchical field can serve as that approver field when
the approval chain is not the reporting line, for instance a finance controller per region.[^s3]

More generally, it is the field type for any user-to-user reference that should form a chain, such as a manager or
reporting line, because the cycle check keeps the chain well formed.[^s1][^s3][^s6]

## Limits and gotchas

- **User only.** You cannot add a hierarchical field to any other object; on other objects use a lookup, including a self-lookup, to model parent–child records.[^s1][^s6]
- **No master-detail on User.** The object reference lists User among the standard objects that cannot be the primary (master) side of a master-detail relationship, so user-to-user links rely on lookup-style fields.[^s4]
- **Not a sharing mechanism.** Record visibility up the management line comes from the role hierarchy, where users get access to records owned by or shared with users in roles below them; roles and their reporting lines are configured separately from user fields such as Manager.[^s5]
- **Data quality matters.** Approval steps that resolve the approver from the Manager field depend on that field being populated for the submitter or record owner, so keep it maintained, for example through user provisioning.[^s3]

## When to use it (and when not)

Use the standard Manager field for the primary reporting line and add a custom hierarchical field only for a second,
genuinely different user chain that automation must follow.[^s3] If the relationship is between a user and a business
record, or between two non-User records, a standard lookup is the right type; master-detail is for tightly bound
child records whose deletion and visibility follow the parent.[^s1] If the goal is data access rather than routing, design
the role hierarchy instead.[^s5]

## Connections

- **Broader:** [Object Relationships](kt:object-relationships) — hierarchical is one of the relationship field types, next to lookup and master-detail.[^s1]
- **Related:** [Lookup vs. Master-Detail Relationships](kt:lookup-vs-master-detail) — a hierarchical field is a specialised, User-only lookup.[^s1] It also sits among the [standard objects](kt:standard-objects) relationship rules that bar User from being a master,[^s4] and like [polymorphic relationships](kt:polymorphic-relationships) it is a special-purpose variant of the basic lookup.
- **consumedBy** [Approval Processes](kt:approval-processes) — approval steps can route to the submitter's or record owner's manager, or to a custom hierarchical field.[^s3]
- **contrastsWith** [Role Hierarchy](kt:role-hierarchy) — the role hierarchy grants record access; the Manager chain models who reports to whom.[^s5]
- **Related:** [User management](kt:user-management) — the field type exists only on User, so the Manager value is maintained as part of each user record.[^s1][^s2]

## Sources
[^s1]: Trailhead, "Data Modeling: Create Object Relationships". https://trailhead.salesforce.com/content/learn/modules/data_modeling/object_relationships (accessed 2026-11-14)
[^s2]: Salesforce Developers, "Salesforce Field Reference Guide: User". https://developer.salesforce.com/docs/atlas.en-us.sfFieldRef.meta/sfFieldRef/salesforce_field_reference_User.htm (accessed 2026-11-14)
[^s3]: Salesforce Developers, "Force.com Platform Fundamentals: Try It Out — Create an Approval Process" (archived v36 docs). https://developer.salesforce.com/docs/atlas.en-us.200.0.fundamentals.meta/fundamentals/adg_workflow_approval_process_try_it_out.htm (accessed 2026-11-14)
[^s4]: Salesforce Developers, "Relationships Among Standard Objects and Fields" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/relationships_among_objects.htm (accessed 2026-11-14)
[^s5]: Salesforce Help, "Create a User Role". https://help.salesforce.com/apex/HTViewHelpDoc?id=admin_roles.htm (accessed 2026-11-14)
[^s6]: Jonathan Fox, "Relationships in Salesforce", Salesforce Ben. https://salesforceben.com/relationships-in-salesforce (accessed 2026-11-14)
