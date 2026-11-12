---
id: kt:permission-set-licenses
type: Concept
title: Permission Set Licenses
aliases: [permission set license, PSL, PSLs, PermissionSetLicense, PermissionSetLicenseAssign, permission set license definition, PSLD]
domain: security-and-sharing
summary: >-
  Optional add-on licenses that raise a user's licensed ceiling beyond what their single user license
  allows, so that permission sets can then grant the extra functionality; a user can hold several, and
  ISVs can define their own in second-generation packages.
release: "Winter '27"
status: current
broader: [kt:user-licenses]
related: [kt:permission-sets, kt:permission-set-groups, kt:profiles, kt:user-access-policies, kt:identity-connect]
relations:
  - {predicate: enables, object: kt:permission-sets}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: configuredVia, object: kt:salesforce-cli}
  - {predicate: consumedBy, object: kt:second-generation-managed-packages}
sources:
  - id: s1
    title: "Give Users the Functionality They Need (Salesforce Licensing module)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-licensing/give-users-the-functionality-they-need
    type: official-learning
    accessed: 2026-11-12
  - id: s2
    title: "PermissionSetLicense (Object Reference for the Salesforce Platform)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_permissionsetlicense.htm
    type: official-docs
    accessed: 2026-11-12
  - id: s3
    title: "PermissionSetLicenseAssign (Object Reference for the Salesforce Platform)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_permissionsetlicenseassign.htm
    type: official-docs
    accessed: 2026-11-12
  - id: s4
    title: "Understand Permission Set Licenses (ISVforce Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/gtm-app-psl-understand.html
    type: official-docs
    accessed: 2026-11-12
  - id: s5
    title: "org assign permsetlicense (Salesforce CLI Command Reference)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_org_assign_permsetlicense.html
    type: official-docs
    accessed: 2026-11-12
  - id: s6
    title: "Bulk Assign Permission Set Licenses for Financial Services Cloud"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/bulk_psl_assign_for_financial_services_cloud.pdf
    type: official-docs
    accessed: 2026-11-12
created: 2026-11-12
---

# Permission Set Licenses

A **permission set license (PSL)** is an optional license that gives a user functionality their user license does not include. Every user has exactly one user license, but can hold several PSLs on top of it.[^s1] Salesforce describes the underlying object as a way to grant a specific permission without changing the user's profile or moving them to another one; a PSL can only add access, never take it away.[^s2]

## How it works

Licenses set the ceiling; profiles and permission sets decide what a user actually gets beneath it. A profile or permission set can never grant more than the user's licenses allow, so a PSL on its own grants nothing visible: it unlocks permissions that a permission set (or profile) then switches on.[^s1] The Trailhead licensing module walks through the order an admin follows: assign the PSL to the users who need the feature, then give them the profile or permission sets that turn that feature on.[^s1]

In the data model, each license is a `PermissionSetLicense` record (API 29.0 and later). It carries a unique name, label, expiration date, an `Active`/`Disabled` status (disabled means expired), total and used license counts, and one boolean per permission the license can unlock.[^s2] The link between a user and a license is a `PermissionSetLicenseAssign` record, also available from API 29.0.[^s3] The license object can be queried, and Salesforce notes that a nested query with the assignment object lists the users holding a given license; since Spring '20 only internal users can access the object.[^s2]

## Assigning PSLs

Admins assign PSLs from the user record or in bulk. In scripted and scratch-org work, `sf org assign permsetlicense` assigns one or more licenses (repeat `--name`) to the org's admin or, with repeated `--on-behalf-of`, to named users.[^s5] For bulk loads, Salesforce's Financial Services Cloud guide uses Data Loader to upsert `PermissionSetAssignment` rows, and says that assigning the permission set also assigns its linked PSL. So the admin's real job is to check in Company Information that enough licenses are free before loading.[^s6]

## Limits and gotchas

- **Integrations flag.** A license has an integrations-enabled setting (API 53.0 and later) that is read-only in the API. Features that need it fail when it is off, including session-based permission set setup.[^s2]
- **Counts are finite.** Each assignment consumes one of the license's total count, so a bulk permission set load can fail partway when licenses run out.[^s2][^s6]
- **Expiry.** A license past its expiration date shows a `Disabled` status, so check status as well as counts when auditing.[^s2]

## Permission set licenses for ISVs

ISVs can sell tiered access by defining a `PermissionSetLicenseDefinition` (PSLD) in a second-generation managed package. Subscriber admins assign it like any standard PSL.[^s4] Each PSLD lists the objects and custom permissions it grants and can be limited to certain user license categories, such as internal platform users or partner community members.[^s4] Objects and custom permissions marked as licensed are reachable only through a PSLD that names them explicitly, and every namespace needs at least one PSLD with namespace component access.[^s4] Restrictions apply: PSLs work only in 2GP, only for net-new packages, and only for US-based paying production subscribers. A later version can't change component access, remove or rename a PSLD, or turn an unlicensed component into a licensed one.[^s4]

## When to use it (and when not)

Use a PSL when a feature sits outside the user's base license, for example an add-on such as an Einstein feature for a subset of account executives. Don't buy a different user license for everyone.[^s1] When the user license already includes the feature, no PSL is needed: a plain permission set or permission set group is the right tool. ISVs should keep the number of PSLDs small, because every extra tier is one more assignment for subscriber admins to manage.[^s4]

## Connections

PSLs sit under **user licenses** (`kt:user-licenses`) in the licensing hierarchy and **enable** **permission sets** (`kt:permission-sets`). Permission sets, **permission set groups** and **profiles** grant access only up to the ceiling a PSL raises.[^s1] **Identity Connect** is one feature gated this way: its permission appears as a flag on the license object.[^s2] Licenses are **queried with** SOQL, **configured via** the Salesforce CLI in scripted setups, and **consumed by** second-generation managed packages that ship their own definitions.[^s2][^s5][^s4] **User access policies** are a related way to automate who gets which permission sets and licenses.

## Sources

[^s1]: Salesforce Trailhead, "Give Users the Functionality They Need". https://trailhead.salesforce.com/content/learn/modules/salesforce-licensing/give-users-the-functionality-they-need (accessed 2026-11-12)
[^s2]: Salesforce, "PermissionSetLicense", Object Reference. https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_permissionsetlicense.htm (accessed 2026-11-12)
[^s3]: Salesforce, "PermissionSetLicenseAssign", Object Reference. https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_permissionsetlicenseassign.htm (accessed 2026-11-12)
[^s4]: Salesforce, "Understand Permission Set Licenses", ISVforce Guide. https://developer.salesforce.com/docs/platform/isvforce/guide/gtm-app-psl-understand.html (accessed 2026-11-12)
[^s5]: Salesforce, "org assign permsetlicense", Salesforce CLI Command Reference. https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_org_assign_permsetlicense.html (accessed 2026-11-12)
[^s6]: Salesforce, "Bulk Assign Permission Set Licenses for Financial Services Cloud". https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/bulk_psl_assign_for_financial_services_cloud.pdf (accessed 2026-11-12)
