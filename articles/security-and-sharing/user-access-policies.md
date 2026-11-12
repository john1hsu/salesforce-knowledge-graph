---
id: kt:user-access-policies
type: Feature
title: User Access Policies
aliases: [user access policy, UserAccessPolicy, UAP]
domain: security-and-sharing
summary: >-
  Setup-defined rules that grant or revoke permission sets, permission set groups, permission set licenses,
  package licenses, public groups and queues for every user who matches a set of criteria, either
  automatically when users are created or updated, or on demand as a bulk migration.
release: "Winter '27"
status: current
broader: [kt:user-management]
related: [kt:permission-sets, kt:permission-set-groups, kt:permission-set-licenses, kt:public-groups, kt:queues]
relations:
  - {predicate: contrastsWith, object: kt:profiles}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: queriedWith, object: kt:tooling-api}
sources:
  - id: s1
    title: "Get Started with User Access Policies (Trailhead, User Access Policies module)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/user-access-policies/get-started-with-user-access-policies
    type: official-learning
    accessed: 2026-11-12
  - id: s2
    title: "Create a User Access Policy (Trailhead, User Access Policies module)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/user-access-policies/create-user-access-policy
    type: official-learning
    accessed: 2026-11-12
  - id: s3
    title: "Migrate Users with User Access Policies (Trailhead, User Access Policies module)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/ko/content/learn/modules/user-access-policies/migrate-users-with-user-access-policies
    type: official-learning
    accessed: 2026-11-12
  - id: s4
    title: "UserAccessPolicy (Metadata API Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_useraccesspolicy.htm
    type: official-docs
    accessed: 2026-11-12
  - id: s5
    title: "Permissions Updates | Learn MOAR Spring '23"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2023/permissions-updates-learn-moar-spring-23
    type: official-blog
    accessed: 2026-11-12
  - id: s6
    title: "The Future of User Management | Summer '24 Be Release Ready"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2024/the-future-of-user-management-summer-24-be-release-ready
    type: official-blog
    accessed: 2026-11-12
created: 2026-11-12
---

# User Access Policies

**User access policies** let an admin describe, once, which users should get which access, and let Salesforce apply that access to every matching user in a single operation instead of assigning each permission set, license or group membership by hand.[^s1] A policy pairs user **criteria** with a list of **grant** or **revoke** actions, and it can target permission sets, permission set groups, permission set licenses, package licenses, public groups and queues.[^s1][^s4] Roles and profiles are not assignable through a policy; they can only be used as criteria.[^s1][^s3]

The feature began as a closed beta, when orgs could have up to 20 active policies, and became generally available in Summer '24 with a higher active-policy ceiling.[^s5][^s6]

## How it works

A policy is created in Setup under **User Access Policies**, after the feature is switched on in **User Management Settings** (which also turns on the enhanced user management interface).[^s2] Each policy has a name, an optional **Order**, criteria and actions.[^s2]

**Criteria** select users by assigned profile or role and by fields on the user record such as title, department or division.[^s1] In Setup, a user must match all of a policy's filters for it to apply.[^s2] In metadata the filters are combined by a `booleanFilter` expression, and each filter has a type (for example `Profile`, `UserRole`, `PermissionSetGroup` or `User` for a user-record field) and an operation such as `equals`, `notEquals`, `in` or `includes`.[^s4]

**Actions** each grant or revoke one access mechanism, identified by its developer name.[^s2][^s4] A typical new-hire policy grants a permission set group, adds the user to a public group and grants a permission set license together.[^s2]

Policies run in one of two modes:

- **Active (automated):** the policy fires when a matching user is created, updated, or both, as chosen with **Automate Policy**, then **Activate**.[^s1][^s2]
- **Manual:** nothing runs until the admin clicks **Apply Policy**, picks users from the list of matches (or applies to all), and the changes run as one operation; manual policies can be reapplied.[^s1][^s3]

Each policy's detail page has a **Recent User Access Changes** tab that shows when it ran and which users it changed.[^s2][^s3] Policies are also metadata: the `UserAccessPolicy` type (API 57.0 and later) lives in the `useraccesspolicies` folder with the `.useraccesspolicy` suffix, and the Spring '23 beta notes say policies can be moved with the Tooling API, Metadata API and first- and second-generation packages.[^s4][^s5]

## Limits and gotchas

Limits verified against Winter '27 documentation:

- An org can have up to **200 active** user access policies.[^s1][^s6]
- A policy can hold up to **20 actions**, at most **3 filters** on applicable users and up to **10 filters** on user fields of type Checkbox, Number, Picklist or Text.[^s2]
- The `order` value is an integer from 0 to 10,000; when a user matches several active policies, only the active policy with the lowest value applies.[^s4]

Other behaviors worth knowing:

- An active policy does not touch users who already match; it applies only when a user is created or a record update makes the user match.[^s1] To bring existing users into line, use a manual policy.[^s1][^s3]
- Deploying a policy whose status is `Active` lands it in `Design` status, so it must be re-activated in the target org.[^s4]
- A profile can't be revoked, because every user keeps exactly one; after a migration, strip the profile's permissions instead.[^s3]

## When to use it (and when not)

Use active policies for joiner and mover automation: provisioning new hires by role or profile, and adjusting access when a promotion, department change or group addition changes a user's attributes.[^s1] Use manual policies for one-time bulk work such as migrating access off profiles onto permission sets and permission set groups, annual group and queue realignments, feature rollouts, and removing licenses from inactive users.[^s1][^s3] Because policies are criteria-driven and stored as metadata, the assignment logic stays declarative, visible in Setup and deployable from source control.[^s4][^s6]

Their actions cover only permissions, licenses and group or queue membership; record-level visibility still comes from the sharing model, which policies affect only indirectly through group and queue membership.[^s1][^s4]

## Connections

User access policies sit under `kt:user-management` and operate on `kt:permission-sets`, `kt:permission-set-groups`, `kt:permission-set-licenses`, `kt:public-groups` and `kt:queues`, the access mechanisms their actions grant and revoke.[^s1][^s4] They `contrastsWith` `kt:profiles`: a profile can be used as a criterion but not assigned, and the feature's main migration use is moving access off profiles.[^s3][^s5] Policies are `configuredVia` the `kt:metadata-api` as the `UserAccessPolicy` type and, per the beta announcement, are also available through the `kt:tooling-api`.[^s4][^s5]

## Sources

[^s1]: Salesforce Trailhead, "Get Started with User Access Policies". https://trailhead.salesforce.com/content/learn/modules/user-access-policies/get-started-with-user-access-policies (accessed 2026-11-12)
[^s2]: Salesforce Trailhead, "Create a User Access Policy". https://trailhead.salesforce.com/content/learn/modules/user-access-policies/create-user-access-policy (accessed 2026-11-12)
[^s3]: Salesforce Trailhead, "Migrate Users with User Access Policies". https://trailhead.salesforce.com/ko/content/learn/modules/user-access-policies/migrate-users-with-user-access-policies (accessed 2026-11-12)
[^s4]: Salesforce, "UserAccessPolicy", Metadata API Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_useraccesspolicy.htm (accessed 2026-11-12)
[^s5]: Salesforce Admins Blog, "Permissions Updates | Learn MOAR Spring '23". https://admin.salesforce.com/blog/2023/permissions-updates-learn-moar-spring-23 (accessed 2026-11-12)
[^s6]: Salesforce Admins Blog, "The Future of User Management | Summer '24 Be Release Ready". https://admin.salesforce.com/blog/2024/the-future-of-user-management-summer-24-be-release-ready (accessed 2026-11-12)
