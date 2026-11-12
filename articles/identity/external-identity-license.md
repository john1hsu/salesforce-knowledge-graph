---
id: kt:external-identity-license
type: Product
title: External Identity License
aliases: [External Identity user license, External Identity User profile, Customer 360 Identity license, Customer Identity license]
domain: identity
summary: >-
  The Salesforce user license, sold in blocks of active users, that gives customers, partners and other external
  users a login identity (self-registration, sign-in, profile management and single sign-on to web and mobile apps)
  with only narrow CRM data access; it underpins Salesforce Customer Identity and can be upgraded to a Community license.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity, kt:user-licenses]
related: [kt:experience-cloud-identity, kt:headless-identity, kt:permission-set-licenses, kt:profiles, kt:experience-cloud]
relations:
  - {predicate: enables, object: kt:experience-cloud-identity}
  - {predicate: alternativeTo, object: kt:customer-community-licenses}
  - {predicate: dependsOn, object: kt:role-hierarchy}
  - {predicate: consumedBy, object: kt:api-experience-hub}
sources:
  - id: s1
    title: "External Identity License Details (Salesforce Identity Implementation Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/users_license_types_external_identity.htm
    type: official-docs
    accessed: 2026-11-12
  - id: s2
    title: "Customer 360 Identity (Salesforce Identity Implementation Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/identity_external.htm
    type: official-docs
    accessed: 2026-11-12
  - id: s3
    title: "Prepare Your Org for Salesforce Customer Identity (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/identity_external/identity_external_prepare
    type: official-learning
    accessed: 2026-11-12
  - id: s4
    title: "Salesforce Customer Identity module, introduction unit (Trailhead)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/identity_external/identity_external_intro
    type: official-learning
    accessed: 2026-11-12
  - id: s5
    title: "API Experience Hub Licensing"
    publisher: MuleSoft (Salesforce)
    url: https://docs.mulesoft.com/api-experience-hub/licensing
    type: official-docs
    accessed: 2026-11-12
created: 2026-11-12
---

# External Identity License

The External Identity license is the user license behind Salesforce Customer Identity (documented as Customer 360 Identity). It is designed for people outside the company network, such as customers, purchasers, patients, partners and dealers, and Salesforce sells it in blocks of active users rather than as named seats priced like internal licenses.[^s1][^s2] Where an internal user license is about access to CRM data, this license is mostly about identity: letting an external person register once and then sign in to your sites and apps with a single account.[^s2][^s4]

## What it includes

The license lets external users self-register, log in, update their own profile, and reach web and mobile apps through one identity.[^s1][^s2] Customer 360 Identity adds out-of-the-box social single sign-on, automatic registration of new users through social sign-on without a sign-up form, and movement between your sites and third-party websites without repeated login screens; a social sign-on can create both the user and an associated contact that then drives downstream work such as a welcome task or email campaign.[^s2] Trailhead frames the business case around customers who expect one login across sales, service and partner apps, a consistent experience across devices, and the option to use social credentials.[^s4]

The license is available in Classic and Lightning Experience in Enterprise, Performance, Unlimited and Developer Editions. Administrators need Manage Users to assign and manage the users and Customize Application to enable Experience Cloud sites. Developer Edition orgs get five External Identity licenses, and the license is included free with all paid Community user licenses in Enterprise, Performance and Unlimited Editions.[^s1]

## Data access and the default profile

Access is deliberately thin. The license exposes a short list of standard objects, for example read and update on Accounts, create/read/update on Contacts, Assets and Individuals, and read-only Documents, plus up to ten custom objects per profile (custom objects from managed packages don't count). Chatter people, groups, feeds and private messages are included.[^s1] Since Spring '19, new orgs get a stricter default External Identity User profile: for example it grants only read on Accounts even though the license allows update, and admins widen access by cloning that profile and changing object permissions. Users provisioned before Spring '19 keep the older behaviour.[^s1]

Setting up Customer Identity uses that profile directly. Trailhead's setup clones the External Identity User profile, creates a role under the role hierarchy for the owner of customer records, and creates an account to hold the registered customers, because the feature needs a profile with this license, a role and an account.[^s3]

## Limits and gotchas

- Salesforce recommends staying under 10 million unique logins per month; above that you may incur extra charges and degraded functionality, so talk to Salesforce first.[^s1]
- File uploads are capped at 2 GB through the web interface and 100 MB from a mobile device.[^s1]
- Extra storage scales with active users, for example 150 MB at 25,000 users and 10 GB at 1,000,000 users.[^s1]
- The license also adds data storage and API request allocations, so check org capacity before a large rollout.[^s1]
- Usernames must be unique within the org that owns the Experience Cloud site.[^s1]
- Experience Cloud objects such as Cases, Contracts, Notes, Orders and Tasks are not included; upgrade users to a Community license for them.[^s1]

## When to use it (and when not)

Choose this license when external users mainly need to authenticate (sign up, sign in, use SSO into your apps and APIs) and touch little CRM data. If they need to work cases, orders or other service records in a portal, a Community license is the better fit, and the documented upgrade path keeps the same users.[^s1] Licence counts can also be driven by other Salesforce products: MuleSoft's API Experience Hub requires External Identity licenses for portal consumers, with a minimum package of 100 service access requests needing at least 2,000 of them.[^s5]

## Connections

The license is the commercial foundation of `kt:salesforce-identity` for external users and sits alongside other user licenses (`kt:user-licenses`); `kt:permission-set-licenses` and `kt:profiles` then shape what each user can do.[^s1] It enables the login and self-registration features of `kt:experience-cloud-identity` and the API-driven flows of `kt:headless-identity`, and it is the lighter-weight alternative to Community licenses for `kt:experience-cloud` sites.[^s1][^s2] Setup depends on a role in the `kt:role-hierarchy` that owns the customer account.[^s3] MuleSoft's `kt:api-experience-hub` consumes it for portal users.[^s5]

## Sources

[^s1]: Salesforce Developers, "External Identity License Details", Salesforce Identity Implementation Guide. https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/users_license_types_external_identity.htm (accessed 2026-11-12)
[^s2]: Salesforce Developers, "Customer 360 Identity", Salesforce Identity Implementation Guide. https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/identity_external.htm (accessed 2026-11-12)
[^s3]: Trailhead, "Prepare Your Org for Salesforce Customer Identity". https://trailhead.salesforce.com/content/learn/modules/identity_external/identity_external_prepare (accessed 2026-11-12)
[^s4]: Trailhead, "Salesforce Customer Identity module, introduction unit". https://trailhead.salesforce.com/content/learn/modules/identity_external/identity_external_intro (accessed 2026-11-12)
[^s5]: MuleSoft, "API Experience Hub Licensing". https://docs.mulesoft.com/api-experience-hub/licensing (accessed 2026-11-12)
