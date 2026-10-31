---
id: kt:role-hierarchy
type: SecurityControl
title: Role Hierarchy
aliases: [user role hierarchy, roles, UserRole, grant access using hierarchies]
domain: security-and-sharing
summary: >-
  The tree of user roles in a Salesforce org that opens record access vertically: users in a role can see and edit
  the records owned by or shared with users in roles beneath them, on top of the organization-wide defaults.
release: "Winter '27"
status: current
broader: [kt:salesforce-sharing-model]
related: [kt:organization-wide-defaults, kt:sharing-rules, kt:implicit-sharing, kt:data-skew, kt:lookup-vs-master-detail]
relations:
  - {predicate: alternativeTo, object: kt:enterprise-territory-management}
  - {predicate: causes, object: kt:sharing-recalculation}
sources:
  - id: s1
    title: "Create a Role Hierarchy (Data Security module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data_security/data_security_roles
    type: official-learning
    accessed: 2026-10-31
  - id: s2
    title: "Platform Sharing Architecture"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/platform-sharing-architecture
    type: official-docs
    accessed: 2026-10-31
  - id: s3
    title: "Behind the Scenes of Record Ownership in Salesforce"
    publisher: Salesforce Engineering (Salesforce Developers Blog)
    url: https://developer.salesforce.com/blogs/engineering/2013/10/behind-the-scenes-of-record-ownership-in-salesforce
    type: official-blog
    accessed: 2026-10-31
created: 2026-10-31
---

# Role Hierarchy

The role hierarchy is the tree of roles that sits on top of the organization-wide defaults (OWDs) in Salesforce's record-level security. Where OWDs set the most restrictive baseline, the hierarchy opens access upward: a user can view, edit and report on data that is owned by, or shared with, users in roles below theirs.[^s1] In practice this means a manager always has at least the access their subordinates have, whatever the OWD for the object says.[^s2]

## How it works

Access flows strictly vertically. A user inherits the access of every role beneath them, but not the access of peers: two users in the same role do not automatically see each other's records.[^s3][^s2] Inherited access mirrors the subordinate's level, so if a subordinate only has read access to a record, the managers above them also get read access, and this applies to both owned and shared records.[^s2] Each user can hold only one role.[^s3]

Under the hood, Salesforce maintains a role group for each role. Users in higher roles become members of the role groups beneath them, so the CEO in a typical tree is a member of every other role's group. Group membership tables record these memberships alongside public groups, queues and territories, and a record shared to a group needs only one share row rather than one per member. When a user opens a record, the platform checks profile, permission set and OWD access, then direct shares, then shares to the user's groups, and grants the least restrictive level it finds.[^s3]

For standard objects hierarchy access is always on. For custom objects, the **Grant Access Using Hierarchies** checkbox in the Organization-Wide Defaults list controls it; it is checked by default, and clearing it limits the object's records to their owners and to users granted access through other sharing features.[^s1][^s2] The same setting can keep records shared to a group hidden from users above the group's members.[^s2]

Roles also drive child implicit sharing: the level of access an account owner gets to the account's contacts, opportunities and cases (View, Edit or none) is set on the owner's role. This applies only to those three standard objects, not to custom objects.[^s2]

## Design guidance

Roles do not need to match the org chart. Each role should represent a distinct level of data access, and Trailhead recommends starting from the org chart and then merging job titles that need the same access into one role, for example combining staff and junior engineers into a single engineering role.[^s1][^s2] When an org also uses Enterprise Territory Management, Salesforce advises using the role hierarchy for HR-style reporting and the territory hierarchy for the sales structure, and warns against making the two hierarchies identical because that generates needless sharing work.[^s2]

## Limits and gotchas

The following figures were verified against Salesforce's sharing architecture guide during the Winter '27 release.[^s2]

- Orgs created in Spring '21 or later can have up to 5,000 roles; older orgs start at 500 and can ask Salesforce Support for more.[^s2]
- Salesforce recommends keeping the hierarchy to no more than 10 levels of branches.[^s2]
- Structural realignments should happen no more than quarterly. For bulk hierarchy changes on objects with over two million records, Support can defer sharing calculations.[^s2]
- High-volume customer licenses do not support roles, and neither do Chatter Free and Chatter External licenses.[^s2]

Ownership skew is the main performance trap. Salesforce recommends a ratio of no more than about 10,000 records per owner. A user who owns more than that should ideally have no role at all. If that user needs a role to share records, it should sit at the top of the hierarchy in its own branch.[^s2] The reason is that moving a user who owns a large share of an object's records to another role triggers sharing recalculations that can run for a long time; such users should not be moved around the tree.[^s3]

## Connections

The role hierarchy is one layer of the broader **Salesforce sharing model**, applied after **organization-wide defaults** and extended by **sharing rules**, which can target roles or roles-and-subordinates.[^s1][^s2] It drives **implicit sharing** to account children.[^s2] It is an **alternative to** the **Enterprise Territory Management** hierarchy for modelling sales access.[^s2] Changes to it **cause** **sharing recalculation**, and its performance is bounded by ownership and **data skew** ratios.[^s2][^s3] Detail records in a master-detail relationship have no Owner field of their own, so ownership-based hierarchy access reaches them only through the master, which ties this node to **lookup vs. master-detail** design.[^s3]

## Sources

[^s1]: Trailhead, "Create a Role Hierarchy (Data Security module)". https://trailhead.salesforce.com/content/learn/modules/data_security/data_security_roles (accessed 2026-10-31)
[^s2]: Salesforce Architects, "Platform Sharing Architecture". https://architect.salesforce.com/fundamentals/platform-sharing-architecture (accessed 2026-10-31)
[^s3]: Salesforce Engineering, "Behind the Scenes of Record Ownership in Salesforce". https://developer.salesforce.com/blogs/engineering/2013/10/behind-the-scenes-of-record-ownership-in-salesforce (accessed 2026-10-31)
