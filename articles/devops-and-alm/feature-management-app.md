---
id: kt:feature-management-app
type: Tool
title: Feature Management App
aliases: [FMA, Salesforce Feature Management App, feature parameters, Feature Parameters for managed packages]
domain: devops-and-alm
summary: >-
  A Salesforce-provided managed package that extends the License Management App so ISV partners can control
  features in subscriber orgs and collect activation metrics through Boolean, Integer and Date feature parameters
  packaged with their 1GP or 2GP managed packages.
release: "Winter '27"
status: current
broader: [kt:license-management-app, kt:application-lifecycle-management]
related: [kt:second-generation-managed-packages, kt:first-generation-managed-packages, kt:push-upgrades, kt:subscriber-support-console]
relations:
  - {predicate: dependsOn, object: kt:license-management-app}
  - {predicate: dependsOn, object: kt:partner-business-org}
  - {predicate: integratesWith, object: kt:custom-permissions}
  - {predicate: configuredVia, object: kt:apex}
sources:
  - id: s1
    title: "Manage Features in Second-Generation Managed Packages"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_dev2gp_fma_manage_features.htm
    type: official-docs
    accessed: 2026-11-27
  - id: s2
    title: "Install and Set Up the Feature Management App in Your License Management Org"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg1-dev/guide/fma-install.html
    type: official-docs
    accessed: 2026-11-27
  - id: s3
    title: "Feature Parameter Metadata Types and Custom Objects"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-fma-types-objects.html
    type: official-docs
    accessed: 2026-11-27
  - id: s4
    title: "Considerations for Feature Management"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/fma-considerations.html
    type: official-docs
    accessed: 2026-11-27
  - id: s5
    title: "Track Preferences and Activation Metrics with Subscriber-to-LMO Feature Parameters"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/pd-fma-subscriber-to-lmo.html
    type: official-docs
    accessed: 2026-11-27
  - id: s6
    title: "Hide Custom Objects and Custom Permissions in Your Subscribers' Orgs"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/pd-fma-hide-custom-objects-permissions.html
    type: official-docs
    accessed: 2026-11-27
  - id: s7
    title: "Manage Features for AppExchange Partners"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/appexchange_licensing/appexchange_licensing_features
    type: official-learning
    accessed: 2026-11-27
  - id: s8
    title: "Best Practices for Feature Management"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg1-dev/guide/fma-best-practices.html
    type: official-docs
    accessed: 2026-11-27
created: 2026-11-27
---

# Feature Management App

The **Feature Management App (FMA)** is a managed package that extends the License Management App (LMA) and, like it, is installed in the partner's License Management Org (LMO).[^s1] It lets an ISV run pilot programs, dark-launch features, offer limited-time trials and track how subscribers activate features, all through **feature parameters** shipped inside a managed package.[^s1] Feature parameters are offered only to AppExchange partners, who request access by logging a case in the Salesforce Partner Community.[^s7] They work with first- and second-generation managed packages but are not available in unmanaged packages.[^s1][^s2]

## How it works

A feature parameter exists in three forms at once: a Metadata API component in the package, a custom object record in the LMO, and a hidden record in each subscriber org.[^s3] Each parameter has a name, a value and a data flow direction, and the value is a Boolean, Integer or Date.[^s7] String values are deliberately excluded so that no personally identifiable information can travel between orgs.[^s7] The value is writable only in the org where it originates; the receiving org can read it but not change it.[^s7]

When a subscriber first installs the package, the FMA creates one `FeatureParameter__c` record per parameter in the LMO, with fields such as `DataType__c`, `DataFlowDirection__c` and `IntroducedInPackageVersion__c`.[^s3] Junction records linking each feature parameter to the subscriber's `License__c` record then hold that subscriber's value, overriding the default or collecting data depending on the direction.[^s3]

There are two directions:

- **LMO-to-subscriber** parameters are edited in the LMO and read-only in the subscriber org; they act as permissions or limits, such as turning a feature on or capping a resource.[^s1][^s8]
- **Subscriber-to-LMO** parameters are set by package Apex in the subscriber org and sent back to the LMO to report activation metrics.[^s1][^s8]

Subscriber-side code writes metrics with `System.FeatureManagement.setPackageBooleanValue`, `setPackageDateValue` and `setPackageIntegerValue`, passing the parameter name and value.[^s5] The resulting values appear on the LMA license record and can also be viewed from the Subscriber Support Console.[^s5][^s7]

The FMA can also hide packaged functionality. A custom object whose visibility is set to Protected, or a custom permission marked as a Protected Component, stays hidden from subscribers until package code calls `System.FeatureManagement.changeProtection()` to unprotect it, for example after a pilot ends.[^s6]

## Setup

Install the LMA first, then log a Partner Community case (product "Partner Programs & Benefits", topic "ISV Technology Request") to get FMA access, and install it from the welcome email.[^s2] In the LMO, add the Feature Parameters tab and add the Feature Parameter Booleans, Dates and Integers related lists to the license page layout, with columns such as Data Flow Direction and Value.[^s2] For a 2GP package, each feature parameter is defined in its own XML file in the project and added to the package.[^s3]

## Limits and gotchas

- After a parameter ships in a released package version, its data flow direction cannot be changed.[^s3][^s4]
- In the LMO, edit only the value field on LMO-to-subscriber junction records, and never create or delete feature parameters there.[^s4]
- LMO edits reach subscriber orgs asynchronously and can take several minutes; subscriber-to-LMO values written by Apex can take up to 24 hours to arrive.[^s4]
- Don't let package Apex modify LMO-to-subscriber values in a subscriber org, and don't edit subscriber-to-LMO values in the LMO; either change leaves the two orgs out of sync.[^s5][^s8]
- Once an unprotected custom object reaches subscribers, it cannot be made Protected again.[^s6]
- Salesforce advises consulting your legal team before collecting activation metrics or releasing hidden features, and collecting only aggregated data.[^s1][^s6]
- Test with a test package and a test LMO before turning the feature set on for a production package.[^s8]

## When to use it (and when not)

Use the FMA when one package version must behave differently per customer: tiered editions, trials of premium features, gradual rollouts or usage caps such as a maximum number of e-signatures.[^s8] It complements, rather than replaces, the LMA's seat and expiration controls, which apply to the whole package.[^s1] Because metric values can lag by up to a day, it is not a real-time usage-billing channel.[^s4]

## Connections

The FMA is an extension of the **License Management App** and depends on the LMO that the partner business org hosts.[^s1][^s2] It is used with **second-generation** and **first-generation managed packages**, and push upgrades propagate junction records asynchronously.[^s3][^s4] Feature values are configured through **Apex** `FeatureManagement` methods, can gate **custom permissions**, and are visible in the **Subscriber Support Console**.[^s5][^s6]

## Sources
[^s1]: Salesforce Developers, "Manage Features in Second-Generation Managed Packages". https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_dev2gp_fma_manage_features.htm (accessed 2026-11-27)
[^s2]: Salesforce Developers, "Install and Set Up the Feature Management App in Your License Management Org". https://developer.salesforce.com/docs/platform/pkg1-dev/guide/fma-install.html (accessed 2026-11-27)
[^s3]: Salesforce Developers, "Feature Parameter Metadata Types and Custom Objects". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-fma-types-objects.html (accessed 2026-11-27)
[^s4]: Salesforce Developers, "Considerations for Feature Management". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/fma-considerations.html (accessed 2026-11-27)
[^s5]: Salesforce Developers, "Track Preferences and Activation Metrics with Subscriber-to-LMO Feature Parameters". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/pd-fma-subscriber-to-lmo.html (accessed 2026-11-27)
[^s6]: Salesforce Developers, "Hide Custom Objects and Custom Permissions in Your Subscribers' Orgs". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/pd-fma-hide-custom-objects-permissions.html (accessed 2026-11-27)
[^s7]: Trailhead, "Manage Features for AppExchange Partners". https://trailhead.salesforce.com/content/learn/modules/appexchange_licensing/appexchange_licensing_features (accessed 2026-11-27)
[^s8]: Salesforce Developers, "Best Practices for Feature Management". https://developer.salesforce.com/docs/platform/pkg1-dev/guide/fma-best-practices.html (accessed 2026-11-27)
