---
id: kt:user-licenses
type: Concept
title: User Licenses
aliases: [user license, Salesforce user license, UserLicense, user license types, License Def. ID]
domain: security-and-sharing
summary: >-
  The single license every Salesforce user is assigned, which sets the ceiling of user-level
  functionality and determines which profiles and permission sets that user can be given;
  permission set licenses can raise it, but profiles and permission sets can never exceed it.
release: "Winter '27"
status: current
broader: [kt:salesforce-licensing]
related: [kt:permission-set-licenses, kt:profiles, kt:permission-sets, kt:external-identity-license, kt:integration-security, kt:experience-cloud]
relations:
  - {predicate: enables, object: kt:profiles}
  - {predicate: hasPart, object: kt:permission-set-licenses}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: consumedBy, object: kt:experience-cloud}
sources:
  - id: s1
    title: "Understand How Licenses Work (Salesforce Licensing module)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-licensing/understand-how-licenses-work
    type: official-learning
    accessed: 2026-11-13
  - id: s2
    title: "Give Users the Functionality They Need (Salesforce Licensing module)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-licensing/give-users-the-functionality-they-need
    type: official-learning
    accessed: 2026-11-13
  - id: s3
    title: "UserLicense (Object Reference for the Salesforce Platform)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_userlicense.htm
    type: official-docs
    accessed: 2026-11-13
  - id: s4
    title: "OEM User License Guide (ISVforce Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/oem-user-license-comparison.html
    type: official-docs
    accessed: 2026-11-13
  - id: s5
    title: "Best Practices for Configuring Your Integration User"
    publisher: Salesforce Admins
    url: https://admin.salesforce.com/blog/2023/best-practices-for-configuring-your-integration-user
    type: official-blog
    accessed: 2026-11-13
created: 2026-11-13
---

# User Licenses

A **user license** defines user-level functionality in a Salesforce org, and every user is assigned exactly one.[^s1] Salesforce groups user licenses with platform licenses and permission set licenses as the three kinds of settings license: bundles of permissions and preferences that switch functionality on either for the whole org (platform) or for an individual user (user and permission set licenses).[^s1] The user license is the first thing an admin picks when creating a user, and it decides which profiles and permission sets that user can ever hold.[^s3]

## How it works

Customers don't buy user licenses one by one. They buy an edition plus any add-ons (product licenses), and each of those bundles platform, user and permission set licenses. One edition can contain several kinds of user license; Sales Cloud Enterprise Edition, for example, includes both Full CRM licenses for people who need CRM features and Chatter Free licenses for people who only need Chatter.[^s1] Not every product creates user licenses: Trailhead notes that Heroku defines its functionality at the org level and so ships only platform licenses.[^s1] Provisioning activates purchased licenses in production only; sandboxes must be updated separately.[^s1]

The license is a ceiling, not a grant. A profile is a subset of what the user license (plus any permission set licenses) allows, and permission sets extend access beyond the profile but never past the licenses.[^s2] Trailhead's example is a license that allows reading, editing and deleting records paired with a profile that allows only reading and editing.[^s2] The recommended order is: assign the user license and profile, add permission set licenses with matching permissions, then layer on permission sets.[^s2]

## The UserLicense object

Each license is a `UserLicense` record, which supports `describeSObjects()`, `query()` and `retrieve()` but not writes.[^s3] Useful fields include `LicenseDefinitionKey` (an identifier such as `SFDC` or `PID_CHATTER`), `MasterLabel`, `Status` (`Active` or `Disabled`), `TotalLicenses` and `UsedLicenses`; for login-based portal licenses, `MonthlyLoginsEntitlement` and `MonthlyLoginsUsed` track monthly logins, and a null entitlement means the license is billed per user.[^s3] Anyone with View Setup and Configuration can read the object, and bulk user-creation tools use it to match each profile and permission set to its license.[^s3]

## Common license families

- **Internal CRM and platform licenses**, such as Full CRM, plus restricted options like Chatter Free.[^s1]
- **Salesforce Integration**: API-only (REST, SOAP or Bulk API), with five free per Enterprise, Unlimited and Performance org and one in Developer Edition.[^s5]
- **External (Experience Cloud) licenses** such as Customer Community, Customer Community Plus and Partner Community, which differ in sharing, reporting and sales-data access.[^s4]
- **Identity-only and OEM licenses**, for example Identity for Employees for SSO, and contractually restricted Platform Embedded licenses sold through ISV partners.[^s4]

## Limits and gotchas

- **One per user.** Changing what someone can do usually means a permission set license, not a second user license, because a user can hold only one user license but several PSLs.[^s1]
- **Counting quirk.** From API 64.0, `UsedLicenses` can't be filtered in a SOQL `WHERE` clause; retrieve the rows and filter afterwards.[^s3]
- **Stale counts.** `UsedLicensesLastUpdated` may reflect the previous day when the license count exceeds the org's threshold, so near-real-time audits should allow for lag.[^s3]
- **Integration license has no object access.** It starts with only admin-level API permissions; object access comes from a permission set backed by the Salesforce API Integration permission set license, and assigning a permission set without that license fails.[^s5]

## When to use which

Pick the cheapest license whose ceiling covers the person's job, then shape access with profiles and permission sets.[^s2] Use the Salesforce Integration license for system-to-system users instead of spending a full CRM seat, provided the vendor's integration supports it.[^s5] For external users, choose among the Experience Cloud licenses by how much sharing and data they need, and consider an identity-only license when people just need to sign in.[^s4]

## Connections

User licenses sit under the broader **Salesforce licensing** model and **enable** **profiles** (`kt:profiles`): every profile belongs to a license, and **permission sets** inherit the same ceiling.[^s2][^s3] **Permission set licenses** (`kt:permission-set-licenses`) are the add-on layer that extends a user's license without replacing it.[^s1] The **External Identity license** is one specific user license for customer sign-in, and **Experience Cloud** consumes the external license family.[^s4] License counts are **queried with** SOQL against `UserLicense`.[^s3] The integration license is a building block of **integration security**, since a dedicated, least-privilege user per integration is the recommended pattern.[^s5]

## Sources

[^s1]: Salesforce Trailhead, "Understand How Licenses Work". https://trailhead.salesforce.com/content/learn/modules/salesforce-licensing/understand-how-licenses-work (accessed 2026-11-13)
[^s2]: Salesforce Trailhead, "Give Users the Functionality They Need". https://trailhead.salesforce.com/content/learn/modules/salesforce-licensing/give-users-the-functionality-they-need (accessed 2026-11-13)
[^s3]: Salesforce, "UserLicense", Object Reference. https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_userlicense.htm (accessed 2026-11-13)
[^s4]: Salesforce, "OEM User License Guide", ISVforce Guide. https://developer.salesforce.com/docs/platform/isvforce/guide/oem-user-license-comparison.html (accessed 2026-11-13)
[^s5]: Salesforce Admins, "Best Practices for Configuring Your Integration User". https://admin.salesforce.com/blog/2023/best-practices-for-configuring-your-integration-user (accessed 2026-11-13)
