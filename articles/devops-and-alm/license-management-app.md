---
id: kt:license-management-app
type: Tool
title: License Management App
aliases: [LMA, Salesforce License Management App, License Management Org, LMO]
domain: devops-and-alm
summary: >-
  A Salesforce-provided managed package that ISV partners install in their partner business org to receive a lead
  and a license record for every install of their 1GP or 2GP managed packages, and to change seats, expiration and
  status of those licenses in subscriber orgs.
release: "Winter '27"
status: current
broader: [kt:agentexchange, kt:application-lifecycle-management]
related: [kt:first-generation-managed-packages, kt:second-generation-managed-packages, kt:push-upgrades]
relations:
  - {predicate: dependsOn, object: kt:partner-business-org}
  - {predicate: integratesWith, object: kt:partner-console}
  - {predicate: hasPart, object: kt:subscriber-support-console}
sources:
  - id: s1
    title: "Manage Licenses for Managed Packages"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg2_dev/lma_intro.htm
    type: official-docs
    accessed: 2026-11-18
  - id: s2
    title: "Install the License Management App"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/lma-install-app.html
    type: official-docs
    accessed: 2026-11-18
  - id: s3
    title: "Manage Your Licenses (App Licensing and Customer Support for AgentExchange)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/appexchange_licensing/appexchange_licensing_manage
    type: official-learning
    accessed: 2026-11-18
  - id: s4
    title: "Best Practices for the License Management App"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.pkg1_dev.meta/pkg1_dev/lma_best_practices.htm
    type: official-docs
    accessed: 2026-11-18
  - id: s5
    title: "Associate a Package with the License Management App"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/lma_associate_package.htm
    type: official-docs
    accessed: 2026-11-18
created: 2026-11-18
---

# License Management App

The **License Management App (LMA)** is a managed package that Salesforce gives to eligible partners so they can manage leads and licenses for the solutions they sell on AgentExchange (formerly AppExchange).[^s1] Each time a customer installs one of the partner's managed packages, the LMA creates a lead record for that prospect and a license record that reflects the package's licensing terms.[^s1][^s3] The org that hosts the LMA is called the **License Management Org (LMO)**.[^s2] The app is English-only, needs the System Administrator profile to configure, and runs in Enterprise, Performance and Unlimited Editions.[^s1]

## How it works

The LMA ships custom objects for packages, package versions, licenses and leads.[^s1] A **Package** record represents a listed package and ties customers to it; a **Package Version** record shows which customers run which version; a **License** record enforces the licensing restrictions in one customer org.[^s3] The app creates the package, version and license records automatically.[^s4]

Packages reach the LMA through the Salesforce Partner Console. For first-generation packages the partner connects each packaging org; for second-generation packages connecting the Dev Hub links every 2GP package that Dev Hub owns. The partner then registers a package version, logs in to the LMO to finish, and sets the default license behaviour.[^s5] Later versions inherit the association. One LMO can manage many 1GP and 2GP packages, but each package belongs to only one LMO.[^s5]

A license carries three key settings.[^s3]

- **Expiration**: the date after which the customer loses access, or "Does not expire".[^s3]
- **Seats**: how many users may use the package, up to 99,000,000, or a **site license** covering every user in the org.[^s3]
- **Status**: Trial (up to 90 days), Active, Suspended (blocks access), or Uninstalled, which is set automatically and locks the record.[^s3]

Partners change these through the **Modify License** action, for example to convert a trial or add seats, and can refresh licenses to resynchronise records across all installations.[^s1][^s3] The bundled **Subscriber Support Console** lists subscriber orgs and, when a subscriber grants login access, lets the partner log in to troubleshoot.[^s1]

## Limits and gotchas

- **Use Modify License, not Edit.** Treat LMA objects as read-only; edit licenses only through Modify License, never directly or via code.[^s3][^s4]
- **Customisations can break record creation.** Required custom fields, or triggers, workflow or validation rules that depend on them, can stop the LMA working.[^s4]
- **Only released versions appear.** Beta versions are hidden: only managed-released 1GP and promoted 2GP versions show up, and unlocked packages are not supported at all.[^s5]
- **Status transitions are one-way.** A trial converted to Active can't return to Trial, and an Uninstalled license can't be modified.[^s3]
- **Org restrictions.** The LMA can't share an org with Slack or the Declarative Lookup Rollup Summaries package, and Developer Edition orgs may only be used to test LMA integrations.[^s2]

## When to use it (and when not)

Salesforce strongly recommends the partner business org as the LMO, because it carries partner-specific entitlements; another Enterprise, Unlimited or Performance production org can be used after logging a Partner Community case.[^s2][^s4] Partners usually find the LMA already installed after standard partner signup.[^s3] Inside a package, the Apex `isCurrentUserLicensed` method checks whether the running user holds a seat, and list views can separate install-generated leads from other leads.[^s4] Apex triggers on LMA records are a common way to alert sales operations to uninstalls or expiring licenses.[^s3] Teams that distribute internal unlocked packages have no use for the LMA, since those packages can't be registered with it.[^s5]

## Connections

The LMA sits within the **AgentExchange** partner ecosystem and the ISV side of **application lifecycle management**.[^s1][^s3] It licenses **first-generation** and **second-generation managed packages**, and the versions it tracks are the same ones partners deliver with **push upgrades**.[^s5] It **depends on** a **partner business org** as its recommended home, **integrates with** the **Partner Console**, where packages are registered, and **includes** the **Subscriber Support Console** for troubleshooting customer orgs.[^s1][^s2][^s5]

## Sources

[^s1]: Salesforce Developers, "Manage Licenses for Managed Packages". https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg2_dev/lma_intro.htm (accessed 2026-11-18)
[^s2]: Salesforce Developers, "Install the License Management App". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/lma-install-app.html (accessed 2026-11-18)
[^s3]: Trailhead, "Manage Your Licenses" (App Licensing and Customer Support for AgentExchange). https://trailhead.salesforce.com/content/learn/modules/appexchange_licensing/appexchange_licensing_manage (accessed 2026-11-18)
[^s4]: Salesforce Developers, "Best Practices for the License Management App". https://developer.salesforce.com/docs/atlas.en-us.264.0.pkg1_dev.meta/pkg1_dev/lma_best_practices.htm (accessed 2026-11-18)
[^s5]: Salesforce Developers, "Associate a Package with the License Management App". https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/lma_associate_package.htm (accessed 2026-11-18)
