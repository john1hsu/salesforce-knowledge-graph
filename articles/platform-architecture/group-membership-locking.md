---
id: kt:group-membership-locking
type: Concept
title: Group Membership Locking
aliases: [group membership lock, granular locking, "Group membership operation already in progress", could not acquire lock, org-wide group membership lock]
domain: platform-architecture
summary: >-
  The org-wide lock Salesforce takes on its group membership tables while roles, territories, public groups, queues
  or user role assignments change, so that sharing data stays consistent; conflicting operations wait and then fail,
  and granular locking lets unrelated operations run in parallel.
release: "Winter '27"
status: current
broader: [kt:record-locking, kt:salesforce-sharing-model]
related: [kt:role-hierarchy, kt:enterprise-territory-management, kt:public-groups, kt:queues, kt:large-data-volumes]
relations:
  - {predicate: dependsOn, object: kt:sharing-recalculation}
  - {predicate: coveredBy, object: kt:sharing-and-visibility-architect-certification}
sources:
  - id: s1
    title: "Group Membership Locking (Designing Record Access for Enterprise Scale)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/draes/guide/draes-group-membership-locking.html
    type: official-docs
    accessed: 2026-11-10
  - id: s2
    title: "Group Membership Operation Already in Progress: Managing Group Membership Locks for Success"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2012/09/group-membership-operation-already-in-progress-managing-group-membership-locks-for-success
    type: official-blog
    accessed: 2026-11-10
  - id: s3
    title: "Salesforce Group Membership and Sharing for Peak Performance"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2013/01/salesforce-group-membership-sharing-for-peak-performance
    type: official-blog
    accessed: 2026-11-10
  - id: s4
    title: "Force.com Record Locking Cheatsheet"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2014/07/record-locking-cheat-sheet
    type: official-blog
    accessed: 2026-11-10
  - id: s5
    title: "Deferred Sharing Calculations (Designing Record Access for Enterprise Scale)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/draes/guide/draes-tools-deferred-sharing-maintenance.html
    type: official-docs
    accessed: 2026-11-10
created: 2026-11-10
---

# Group Membership Locking

**Group membership locking** is the concurrency control Salesforce applies to the tables that record who belongs to
which group. While membership data is being updated, the sharing system locks those tables so that two simultaneous
changes cannot leave access data inaccurate.[^s1] Unlike ordinary row locks on business records, this lock protects the
sharing infrastructure itself, and in its classic form it is organization-wide: only one group membership operation can
hold it at a time.[^s4] It is a frequent cause of failed integrations and realignment jobs in large orgs.

## How it works

Salesforce models visibility through a central Group object that underpins the role hierarchy, territory hierarchy,
public groups and queues.[^s2] Groups add a level of indirection to sharing: one share row granted to a group stands
in for a row per member, which keeps share tables (already hundreds of millions of rows in enterprise orgs) smaller.[^s3]
The price is that every change to that structure needs the exclusive lock, whatever the group type: roles,
territories, queues, public groups and private groups.[^s3][^s4]

Operations that take the lock for the length of their transaction include creating, deleting or moving a role or
territory; adding or removing a user from a territory; provisioning an internal user into an existing role; changing a
user's role; provisioning a portal (external) user under an account; changing a portal account's owner; and changing the
role of a user who owns portal accounts.[^s2] The lock is usually held only briefly, but a change that sets off a
sharing rule recalculation, such as a role change, can hold it much longer.[^s1]

When an operation cannot get the lock it fails with "could not acquire lock" or "Group membership operation already in
progress".[^s1] Salesforce's engineering guidance describes the platform waiting up to 10 seconds for the lock; an
exception results when a holder keeps it longer, or when queued operations together exceed that wait.[^s2]

## Granular locking

Granular locking, which is on by default, relaxes the single global lock. Operations may run at the same time when the
roles or groups involved have no hierarchical or other relationship.[^s1] In practice this means groups in separate
hierarchies can change concurrently, public groups and roles without territories are not blocked by territory work,
users can be added to territories and public groups in parallel, and external users can be provisioned in existing
accounts without waiting; external user creation needs a lock only when a new external role must be created.[^s1] A
long operation such as deleting a role then blocks only a small set of others. Role reparenting, which includes
changing the owner of a customer or partner account, still blocks almost every other group update, and changing a
user's role can run alongside only role insertion, territory insertion and user provisioning.[^s1] High-volume
Experience Cloud user provisioning can run with any group membership operation.[^s1]

## Limits and gotchas

- **Typical triggers.** Large data loads or integrations that change roles, groups or user assignments; an admin
  editing a role or a new external user being provisioned while those run; end-of-quarter or year-end realignments;
  and deployments or Apex tests that update group membership.[^s1]
- **Deferral does not remove it.** Deferring sharing calculations suspends sharing rule and group membership
  calculation, but group membership locking can still occur while calculations are deferred.[^s5]
- **Dynamic groups hurt.** Highly dynamic group membership raises contention; for high-volume automated movement of
  users, sharing directly to records can scale better than churning group membership.[^s3]
- **Mitigation.** Schedule group maintenance jobs so they do not overlap, build retry logic into integrations, and fall
  back to serial processing if parallel loads collide.[^s1] Keep lock-holding transactions lean, tune batch sizes so a
  lock is never held beyond the wait window, and run large changes in maintenance windows.[^s2] Group maintenance
  updates in particular should run serially.[^s4]

## When to design for it

Treat group membership locking as a design constraint whenever automation moves users between roles, territories or
groups at volume, or when Experience Cloud provisioning runs alongside sharing-model changes. Prefer stable groups for
teams of several users sharing the same access, and avoid groups for one or very few users.[^s3]

## Connections

Group membership locking is a specialised form of **record locking** within the **Salesforce sharing model**.[^s4] It is
triggered by changes to the **role hierarchy**, **enterprise territory management**, **public groups** and **queues**,
and its duration depends on the **sharing recalculation** a change sets off.[^s1][^s2] It is most acute in **large data
volume** orgs with huge share tables, and the access-design trade-offs it forces are the territory of the **Sharing and
Visibility Architect certification**.[^s3][^s5]

## Sources
[^s1]: Salesforce Developers, "Group Membership Locking (Designing Record Access for Enterprise Scale)". https://developer.salesforce.com/docs/platform/draes/guide/draes-group-membership-locking.html (accessed 2026-11-10)
[^s2]: Salesforce Developers Blog, "Group Membership Operation Already in Progress: Managing Group Membership Locks for Success". https://developer.salesforce.com/blogs/2012/09/group-membership-operation-already-in-progress-managing-group-membership-locks-for-success (accessed 2026-11-10)
[^s3]: Salesforce Developers Blog, "Salesforce Group Membership and Sharing for Peak Performance". https://developer.salesforce.com/blogs/2013/01/salesforce-group-membership-sharing-for-peak-performance (accessed 2026-11-10)
[^s4]: Salesforce Developers Blog, "Force.com Record Locking Cheatsheet". https://developer.salesforce.com/blogs/2014/07/record-locking-cheat-sheet (accessed 2026-11-10)
[^s5]: Salesforce Developers, "Deferred Sharing Calculations (Designing Record Access for Enterprise Scale)". https://developer.salesforce.com/docs/platform/draes/guide/draes-tools-deferred-sharing-maintenance.html (accessed 2026-11-10)
