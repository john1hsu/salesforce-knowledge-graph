---
id: kt:salesforce-licensing
type: Concept
title: Salesforce Licensing
aliases: [Salesforce license model, Salesforce licensing model, license definitions, settings licenses, product licenses]
domain: platform-architecture
summary: >-
  The layered model by which a Salesforce org's purchased editions and add-ons (product licenses) are
  provisioned as platform, user and permission set licenses (settings licenses) that switch on org-wide and
  per-user permissions and preferences, which profiles and permission sets then grant within those ceilings.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform, kt:metadata-driven-architecture]
related: [kt:user-licenses, kt:permission-set-licenses, kt:licensing-strategy, kt:profiles, kt:permission-sets, kt:sandbox-types, kt:total-cost-of-ownership]
relations:
  - {predicate: hasPart, object: kt:user-licenses}
  - {predicate: hasPart, object: kt:permission-set-licenses}
  - {predicate: enables, object: kt:profiles}
  - {predicate: contrastsWith, object: kt:license-management-app}
  - {predicate: consumedBy, object: kt:api-request-limits}
sources:
  - id: s1
    title: "Understand How Licenses Work (Salesforce Licensing module)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-licensing/understand-how-licenses-work
    type: official-learning
    accessed: 2026-11-20
  - id: s2
    title: "Give Users the Functionality They Need (Salesforce Licensing module)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-licensing/give-users-the-functionality-they-need
    type: official-learning
    accessed: 2026-11-20
  - id: s3
    title: "Keep Up with Upgrades and Add-ons (Salesforce Licensing module)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-licensing/keep-up-with-upgrades-and-addons
    type: official-learning
    accessed: 2026-11-20
  - id: s4
    title: "Choosing the Right Salesforce Edition for Your App"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/isv_plan/isv_plan_editions
    type: official-learning
    accessed: 2026-11-20
  - id: s5
    title: "OEM User License Guide (ISVforce Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.packagingGuide.meta/packageGuide/oem_user_license_comparison.htm
    type: official-docs
    accessed: 2026-11-20
  - id: s6
    title: "TenantUsageEntitlement (Object Reference for the Salesforce Platform)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_tenantusageentitlement.htm
    type: official-docs
    accessed: 2026-11-20
created: 2026-11-20
---

# Salesforce Licensing

Salesforce licensing is the model that turns what a customer buys into what an org and its users can actually do. In Salesforce's terms a license is the contractual agreement between Salesforce and the customer, while a *license definition* is the metadata that describes which features the org receives; each license in an org also carries org-specific data such as start and end dates, the number of users allowed and the number of custom objects allowed.[^s1] Because features are switched on by metadata rather than by separate code bases, licensing is one of the clearest expressions of the platform's metadata-driven, multitenant design.[^s1]

## The layers

Salesforce describes licensing as a stack of bundles:[^s1]

- **Perms and prefs**: permissions are on/off switches that control feature access; preferences are settings a customer can configure, such as time zone or password options.[^s1]
- **Platform licenses** hold org-wide perms and prefs, such as the ability to create custom objects or make API requests.[^s1][^s2]
- **User licenses** hold user-level perms and prefs. Every user gets exactly one, and an edition can contain several user license types.[^s1]
- **Permission set licenses (PSLs)** add user-level functionality on top of the user license, and one user can hold many.[^s1]
- **Product licenses** are the editions and add-ons a customer buys; they bundle the platform, user and permission set licenses, which together are called *settings licenses*.[^s1]

Customers do not buy individual settings licenses. An org has exactly one edition license and any number of add-ons, including none, and an add-on can contain any mix of platform, user and permission set licenses.[^s1] Trailhead's example is an Enterprise Edition Service Cloud org with 100 Full CRM user licenses plus a Service Cloud Einstein add-on that brings 10 Service Cloud Einstein PSLs.[^s1]

## How licenses reach users

Licenses set ceilings; profiles and permission sets grant access inside them. Platform-level perms are turned on or off by Salesforce's provisioning system according to the purchase and cannot be changed by an admin, whereas platform-level prefs such as language or time zone are admin-editable in Setup.[^s2] Each user has one user license (plus optional PSLs), one profile that forms a baseline subset of those licenses, and any number of permission sets that add to the profile; neither profiles nor permission sets can exceed what the user license and PSLs allow.[^s2]

The edition determines much of the ceiling. For example, Trailhead's ISV planning unit notes that Starter is limited to five user licenses and lacks record types, that Professional Edition has no limit on user licenses, and that active validation rules per object are 20 in Starter and Professional but 200 in Enterprise and Unlimited.[^s4] The same unit lists API restrictions for Starter and Professional orgs, such as no Bulk API, Streaming API or platform events.[^s4]

## Provisioning, upgrades and sandboxes

Provisioning is the process that activates licenses. It runs on an initial purchase, on an upgrade or add-on purchase, and when a patch release changes a license definition, and it applies only to production orgs, not to Demo, Developer, Scratch or Trial orgs.[^s1] An edition upgrade moves the org to a higher edition (for example Enterprise to Unlimited), while an add-on adds features without changing the edition; either way the admin still has to assign the new licenses, profiles or permission sets before anyone can use the features.[^s3]

Sandboxes do not follow production automatically. A refresh copies production's metadata, and the Match Production Licenses tool syncs sandbox license counts without a refresh, adding licenses the sandbox lacks and removing ones production no longer has.[^s3] Programmatically, the TenantUsageEntitlement object represents the features and functions an org has access to and is available from API version 28.0.[^s6]

## Gotchas

- The ceiling a user license sets is absolute: no profile or permission set can grant more than the user license and PSLs allow.[^s2]
- Buying an add-on does not by itself give anyone access; assigning the PSL and a suitable profile or permission set is a separate admin step.[^s3]
- After an upgrade, forgetting to match licenses in sandboxes leaves test environments unable to reproduce production behaviour.[^s3]
- ISV OEM deals use contractually restricted licenses such as Force.com Platform Embedded, whose Starter variant is limited to 10 objects.[^s5]

## Connections

Salesforce Licensing is the parent concept for `kt:user-licenses` and `kt:permission-set-licenses`, the two user-level layers of the stack,[^s1] and it `enables` `kt:profiles` and `kt:permission-sets`, which can only grant what the licenses allow.[^s2] It sits under `kt:salesforce-platform` and `kt:metadata-driven-architecture` because license definitions are metadata that switch features on per org.[^s1] Platform licenses carry org-level allowances such as API requests, linking it to `kt:api-request-limits`.[^s2] `kt:sandbox-types` matter because sandboxes need license matching after production changes.[^s3] The commercial side — choosing editions and add-ons and costing them — belongs to `kt:licensing-strategy` and `kt:total-cost-of-ownership`, while `kt:license-management-app` belongs to the ISV side of licensing, alongside partner-specific arrangements such as the OEM embedded user licenses.[^s5]

## Sources
[^s1]: Salesforce Trailhead, "Understand How Licenses Work". https://trailhead.salesforce.com/content/learn/modules/salesforce-licensing/understand-how-licenses-work (accessed 2026-11-20)
[^s2]: Salesforce Trailhead, "Give Users the Functionality They Need". https://trailhead.salesforce.com/content/learn/modules/salesforce-licensing/give-users-the-functionality-they-need (accessed 2026-11-20)
[^s3]: Salesforce Trailhead, "Keep Up with Upgrades and Add-ons". https://trailhead.salesforce.com/content/learn/modules/salesforce-licensing/keep-up-with-upgrades-and-addons (accessed 2026-11-20)
[^s4]: Salesforce Trailhead, "Choosing the Right Salesforce Edition for Your App". https://trailhead.salesforce.com/isv_plan/isv_plan_editions (accessed 2026-11-20)
[^s5]: Salesforce Developers, "OEM User License Guide", ISVforce Guide. https://developer.salesforce.com/docs/atlas.en-us.packagingGuide.meta/packageGuide/oem_user_license_comparison.htm (accessed 2026-11-20)
[^s6]: Salesforce Developers, "TenantUsageEntitlement", Object Reference. https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_tenantusageentitlement.htm (accessed 2026-11-20)
