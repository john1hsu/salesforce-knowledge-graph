---
id: kt:public-groups
type: Feature
title: Public Groups
aliases: [public group, Salesforce public groups, regular group, Group (Regular)]
domain: security-and-sharing
summary: >-
  Admin-defined collections of users, roles, roles and subordinates, territories and other public groups that
  act as a single sharing target; stored as Group records of type Regular with membership in GroupMember, and
  used mainly by sharing rules, manual sharing, queues and list-view or folder access.
release: "Winter '27"
status: current
broader: [kt:salesforce-sharing-model]
related: [kt:sharing-rules, kt:queues, kt:role-hierarchy, kt:group-membership-locking, kt:enterprise-territory-management]
relations:
  - {predicate: enables, object: kt:sharing-rules}
  - {predicate: dependsOn, object: kt:role-hierarchy}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: integratesWith, object: kt:sharing-recalculation}
sources:
  - id: s1
    title: "Group (Object Reference for the Salesforce Platform)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_group.htm
    type: official-docs
    accessed: 2026-11-11
  - id: s2
    title: "GroupMember (Object Reference for the Salesforce Platform)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_groupmember.htm
    type: official-docs
    accessed: 2026-11-11
  - id: s3
    title: "Group (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_group.htm
    type: official-docs
    accessed: 2026-11-11
  - id: s4
    title: "Define Sharing Rules (Data Security module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data_security/data_security_sharing_rules
    type: official-learning
    accessed: 2026-11-11
created: 2026-11-11
---

# Public Groups

A public group is a named set of people that an admin defines once and then reuses as the target of sharing. Trailhead describes it as a collection of users, other groups, roles or territories that share a common function, and recommends one whenever a sharing rule would otherwise list more than one or two groups or roles, or any individual user.[^s4] Because the group, not its members, is what sharing rules and other access grants point at, membership can change without editing every rule that uses it.[^s4]

## How it works

In the data model a public group is a `Group` record whose `Type` is `Regular`. The same Group object also represents roles, roles and subordinates, queues, territories, the whole organization, manager groups, Chatter groups and several feature-specific group kinds, so `Type` is what distinguishes a public group from the rest.[^s1] Only public groups are reachable through the API; personal groups are not, and the Organization and manager-related group types are read-only.[^s1]

Membership lives in `GroupMember`. Each row links a `GroupId` to a `UserOrGroupId`, a polymorphic lookup that can hold either a User or another Group, which is how roles, territories and nested public groups become members.[^s2] Rows exist only for direct members of Regular groups: users who inherit membership through a role or a nested subgroup are not listed, so a query on GroupMember alone does not return everyone a group covers.[^s2] GroupMember supports create, delete, query and retrieve but not update; inserting a duplicate row simply returns the existing one.[^s2]

Setup builds a group in two steps: create it under **Public Groups** with a label (the API name fills in automatically) and optional description, then open the group and use **Add Members** to choose from the member types the org offers.[^s4] Those member types can include individual users, roles, roles and subordinates (optionally limited to internal users), territories, territories and subordinates, and other public groups.[^s4]

## Hierarchy access

The **Grant Access Using Hierarchies** checkbox maps to the `doesIncludeBosses` field. When it is on, records shared with the group are also shared with users above the members in the role hierarchy.[^s3] On the Group object the field applies only to Regular and Queue groups, and for Regular groups it is documented as defaulting to true.[^s1] Turning it off is the usual way to share records with a team without automatically exposing them to that team's managers.

## Deploying groups

Public groups are metadata. The Metadata API `Group` type, available since API 24.0, stores each group as a `.group` file in a `groups` folder and supports the `*` wildcard in `package.xml`.[^s3] The type carries the group's label, API name, description (added in API 62.0) and `doesIncludeBosses`; its reference page documents only these group-level fields, so plan membership separately from the group definition.[^s3]

## Limits and gotchas

- For a group with more than 10,000 members, Salesforce recommends managing membership through GroupMember rather than the group's Setup detail page.[^s2]
- Deleting a public group succeeds even if sharing still references it (API 13.0 and later), so check dependent sharing rules first.[^s1]
- `DeveloperName` must be unique per group type; set it explicitly during large data loads to avoid slowdowns.[^s1]
- Groups suit audiences you can predict. Trailhead warns that frequently changing teams, such as interview panels, are poor candidates for sharing-rule targets.[^s4]

## When to use it

Use a public group when the same audience needs access in several places, or when that audience cuts across the role hierarchy, such as recruiters plus hiring managers sharing review records.[^s4] Use a role or role-and-subordinates target directly when the audience already matches the hierarchy, and use a queue when the group should own the work rather than only see it.[^s1][^s4]

## Connections

Public groups sit under the **Salesforce sharing model** and mainly **enable** **sharing rules**, which name a group as the set of users receiving access.[^s4] Their reach **depends on** the **role hierarchy**, both because roles can be members and because hierarchy access extends sharing upward.[^s3][^s4] **Queues** are a sibling Group type with the same hierarchy setting.[^s1] Because group membership feeds sharing, the group **integrates with** **sharing recalculation**, and the operational side of bulk membership changes is covered under **group membership locking**. Territory members tie groups to **Enterprise Territory Management**, and groups are **configured via** the **Metadata API** `Group` type.[^s3][^s4]

## Sources
[^s1]: Salesforce Developers, "Group", Object Reference for the Salesforce Platform. https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_group.htm (accessed 2026-11-11)
[^s2]: Salesforce Developers, "GroupMember", Object Reference for the Salesforce Platform. https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_groupmember.htm (accessed 2026-11-11)
[^s3]: Salesforce Developers, "Group", Metadata API Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_group.htm (accessed 2026-11-11)
[^s4]: Trailhead, "Define Sharing Rules", Data Security module. https://trailhead.salesforce.com/content/learn/modules/data_security/data_security_sharing_rules (accessed 2026-11-11)
