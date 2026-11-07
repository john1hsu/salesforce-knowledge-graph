---
id: kt:profiles
type: SecurityControl
title: Profiles
aliases: [profile, user profile, Salesforce profile, standard profile, custom profile, Profile object]
domain: security-and-sharing
summary: >-
  The single, mandatory, license-bound settings bundle every Salesforce user has; it sets baseline defaults
  such as apps, record types, page layouts, login hours and IP ranges, while most object, field and system
  access is now meant to come from permission sets.
release: "Winter '27"
status: current
broader: [kt:salesforce-sharing-model]
related: [kt:permission-set-groups, kt:record-types, kt:login-flows, kt:session-security-levels, kt:organization-wide-defaults, kt:experience-cloud]
relations:
  - {predicate: contrastsWith, object: kt:permission-sets}
  - {predicate: configuredVia, object: kt:page-layouts}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: configuredVia, object: kt:metadata-api}
sources:
  - id: s1
    title: "Manage Salesforce Object Access (Trailhead, Data Security module)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/en/content/learn/modules/data_security/data_security_objects
    type: official-learning
    accessed: 2026-11-07
  - id: s2
    title: "The Salesforce Admin's Guide to Profiles and Permissions"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2026/the-salesforce-admins-guide-to-profiles-and-permissions
    type: official-blog
    accessed: 2026-11-07
  - id: s3
    title: "Standard Profiles (Salesforce Help)"
    publisher: Salesforce
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.standard_profiles.htm&type=5
    type: official-docs
    accessed: 2026-11-07
  - id: s4
    title: "Profile (Object Reference for the Salesforce Platform)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_profile.htm
    type: official-docs
    accessed: 2026-11-07
  - id: s5
    title: "Using SOQL to Determine Your Force.com User's Permissions"
    publisher: Salesforce Engineering Blog
    url: https://developer.salesforce.com/blogs/engineering/2012/06/using-soql-to-determine-your-users-permissions-2
    type: official-blog
    accessed: 2026-11-07
created: 2026-11-07
---

# Profiles

A profile is the settings bundle that every Salesforce user must have, and each user has exactly one. It is tied to a user license and sets the user's baseline: which apps they see, which record types and page layouts they get, and default access.[^s1] Salesforce's admin guidance lists login IP ranges, login hours, default apps, default record types, page layout assignments and baseline permissions as the profile's job.[^s2] In the API, a profile is a set of permissions controlling what its users can do. A new profile starts empty apart from the permissions its user license requires.[^s4]

## Standard and custom profiles

Every org ships with standard profiles. Which ones exist depends on the edition. Examples include System Administrator, Standard User, Marketing User, Contract Manager, Solution Manager, Minimum Access - Salesforce, Minimum Access - API Only Integrations, and community, partner and Chatter profiles for external and collaboration users.[^s3] The permissions on a standard profile cannot be edited. Admins can still change a few settings on them, such as custom app and tab settings, session settings and password policies.[^s3] Minimum Access - Salesforce grants the fewest platform privileges and expects extra access to come from permission sets and permission set groups. Minimum Access - API Only Integrations is the API-only baseline that replaces the deprecated API Only System Integrations profile.[^s3]

Custom profiles are made by cloning an existing one (Trailhead suggests Minimum Access - Salesforce), editing it, often in the enhanced profile UI, and assigning it from the user record.[^s1] Custom profiles can be renamed and deleted; standard ones cannot.[^s2] Professional, Enterprise, Unlimited, Performance and Developer Editions can create custom profiles. Contact Manager and Group Editions can only assign the standard ones.[^s3]

## The permission-set-led model

Salesforce now describes a permission-set-led model. The profile supplies baseline settings, and permission sets and permission set groups supply most of a user's access. Users can hold many permission sets but only one profile, so access can follow a job or task without a new profile for every role.[^s2] Trailhead's recruiting example gives recruiters, interviewers and hiring managers the same minimal profile and layers each persona's object permissions on through permission sets. It also recommends managing object permissions in permission sets rather than profiles.[^s1] Taking access away means removing a permission from the base profile and from every set that grants it, or muting it inside a permission set group.[^s1]

## How it works under the hood

Since Summer '12, every profile has one underlying permission set, flagged by the `IsOwnedByProfile` field on `PermissionSet`. Profile and permission set permissions therefore combine the same way. Setup shows only the profile, but the API exposes both.[^s5] Querying `PermissionSet` with `IsOwnedByProfile = TRUE` returns the profile-owned sets. Joining `PermissionSetAssignment` and `ObjectPermissions` shows whether a given access comes from a profile or a permission set.[^s5] The `Profile` object itself supports create, query, update and delete, and exposes `UserLicenseId` and `UserType`. Each permission appears as a Boolean field, and the available fields vary by org and license.[^s4]

## Limits and gotchas

- **Admin-level permissions bypass sharing.** View All Data and Modify All Data on System Administrator override sharing settings, so grant them to other profiles with care.[^s1]
- **Standard profiles can over-grant.** Some give more access than users need, which is why a minimal clone is the usual starting point.[^s1]
- **Profile names are filtered.** Since Winter '21, users see other profiles' names only if Profile Filtering is enabled and they have the right permissions.[^s4]
- **License moves change counts.** Moving a user to a profile on a different license type frees a seat in the old license pool and uses one in the new pool.[^s4]
- **Some features need feature licenses** on top of the profile. For example, managing campaigns requires the Marketing User feature license.[^s3]

## Connections

Profiles sit under the **Salesforce sharing model** as its object- and system-level layer. Record visibility comes separately from **organization-wide defaults** and sharing, which View All Data and Modify All Data can override.[^s1] They contrast with **permission sets** (one profile per user, many sets) and are the baseline that **permission set groups** build on.[^s2] Profiles assign **record types** and **page layouts**.[^s1] **Login flows** and **session security levels** are both applied through profile-level settings, and session settings stay editable even on standard profiles.[^s3] Community and partner profiles serve **Experience Cloud** users.[^s3] Profile-owned permission sets are inspected with **SOQL**.[^s5] Profiles are deployed through the **Metadata API** and its Profile type, though the object reference recommends the SOAP `Profile` object for creating empty profiles.[^s4]

## Sources
[^s1]: Salesforce Trailhead, "Manage Salesforce Object Access". https://trailhead.salesforce.com/en/content/learn/modules/data_security/data_security_objects (accessed 2026-11-07)
[^s2]: Salesforce Admins Blog, "The Salesforce Admin's Guide to Profiles and Permissions". https://admin.salesforce.com/blog/2026/the-salesforce-admins-guide-to-profiles-and-permissions (accessed 2026-11-07)
[^s3]: Salesforce, "Standard Profiles", Salesforce Help. https://help.salesforce.com/s/articleView?language=en_US&id=sf.standard_profiles.htm&type=5 (accessed 2026-11-07)
[^s4]: Salesforce, "Profile", Object Reference for the Salesforce Platform. https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_profile.htm (accessed 2026-11-07)
[^s5]: Salesforce Engineering Blog, "Using SOQL to Determine Your Force.com User's Permissions". https://developer.salesforce.com/blogs/engineering/2012/06/using-soql-to-determine-your-users-permissions-2 (accessed 2026-11-07)
