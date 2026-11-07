---
id: kt:first-generation-managed-packages
type: Feature
title: First-Generation Managed Packages
aliases: [managed 1GP, 1GP, first-generation managed packaging, 1GP managed package, packaging org packages]
domain: devops-and-alm
summary: >-
  Salesforce's original packaging technology for ISV partners: an upgradeable, namespaced managed package whose
  metadata lives in a dedicated Developer Edition packaging org, released in linear versions with patches built in
  separate patch orgs. Still supported, but Salesforce steers new apps to managed 2GP.
release: "Winter '27"
status: current
broader: [kt:application-lifecycle-management]
related: [kt:appexchange-security-review, kt:tooling-api]
relations:
  - {predicate: replacedBy, object: kt:second-generation-managed-packages}
  - {predicate: contrastsWith, object: kt:package-dependencies}
  - {predicate: alternativeTo, object: kt:unlocked-packages}
  - {predicate: dependsOn, object: kt:namespace-registry}
sources:
  - id: s1
    title: "First-Generation Managed Packaging Developer Guide (PDF)"
    publisher: Salesforce Developers
    url: https://resources.docs.salesforce.com/260/latest/en-us/sfdc/pdf/pkg1_dev.pdf
    type: official-docs
    accessed: 2026-11-07
  - id: s2
    title: "Comparison of First- and Second-Generation Managed Packages"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-comparison.html
    type: official-docs
    accessed: 2026-11-07
  - id: s3
    title: "Create and Upload Patches in First-Generation Managed Packages"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg1-dev/guide/patches-creating.html
    type: official-docs
    accessed: 2026-11-07
  - id: s4
    title: "Components Available in First-Generation Managed Packages"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg1-dev/guide/first-gen-packageable-components.html
    type: official-docs
    accessed: 2026-11-07
  - id: s5
    title: "Move to 2GP: Migrate Your Managed Packages with Ease"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg1-dev/guide/move-to-second-gen-pkg.html
    type: official-docs
    accessed: 2026-11-07
  - id: s6
    title: "Create a Packaging Org (CumulusCI for Managed Packages)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/cumulusci-for-managed-packages/create-a-packaging-org
    type: official-learning
    accessed: 2026-11-07
created: 2026-11-07
---

# First-Generation Managed Packages

First-generation managed packaging (managed 1GP) is the original way Salesforce partners distribute and sell apps. A managed package is upgradeable, carries a namespace, and is sold through AppExchange (now AgentExchange) with user-based licenses tracked by the License Management App.[^s1] Its defining trait is that a **packaging org**, a Developer Edition org configured with the package's namespace, holds the metadata and is where new versions are created.[^s6] The newer managed 2GP model moved that source of truth to version control, and Salesforce's own guide suggests 2GP for new apps.[^s1][^s2]

## How it works

A partner registers a namespace prefix in the packaging org through Package Manager in Setup. Prefixes are globally unique and up to 15 alphanumeric characters; they must start with a letter and cannot contain two consecutive underscores.[^s1][^s6] The packaging org owns the package, a packaging org can own only one managed package, and a namespace can be associated with only one package. Because each package needs its own namespace, `global` Apex is the only way to share code across a partner's 1GP packages.[^s2]

Versions are uploaded from the packaging org. A **Managed - Beta** upload is for testing and pilot feedback; its components remain editable in the packaging org until a released version is uploaded, and beta versions install only in scratch, sandbox, Developer Edition or Environment Hub test orgs and can't be pushed to customers.[^s1][^s3] A **Managed - Released** upload creates an upgradeable version and locks some metadata attributes.[^s3] Version numbers follow major.minor.patch.build, and the versioning model is linear: each release builds on the previous one.[^s1][^s2]

Patches are built in a separate **patch development org**, created from Setup > Packages against a Managed - Released major version. Patch versioning is enabled through a Partner Community case and is only available to packages that have passed security review. Uploads can also be started through the Tooling API's PackageUploadRequest object, and patches reach subscribers by install link or a scheduled push upgrade.[^s3]

## Limits and gotchas

- **Org sprawl.** Every package and patch version needs its own org, so long-lived products can accumulate many orgs and credentials to manage.[^s1]
- **Patches are narrow.** A patch can't add or delete components, add `global` or `virtual` modifiers, new web services, new class relationships or new dependencies, deprecate Apex, or change API and dynamic Apex access. A dependency removed in a patch can only be restored in a new major or minor version.[^s3]
- **Released metadata is sticky.** Metadata added to a 1GP package generally stays in it.[^s1] Per component, properties are developer-editable, subscriber-editable or locked, and removing a component from a released package usually deprecates it rather than deleting it in subscriber orgs. Removals need Salesforce approval through a Partner Community case.[^s4]
- **Manual steps.** Some operations, such as creating and uninstalling packages, can't be automated, unlike 2GP where every packaging operation runs through Salesforce CLI.[^s2]
- **Dependency direction.** 1GP packages can't depend on 2GP packages, which shapes migration order for package families.[^s1]

## When to use it (and when not)

Partners with existing 1GP customers keep maintaining those packages until they migrate. If no customers still run a partner's 1GP packages, Salesforce says to skip migration and build new 2GP packages instead.[^s5] Migration converts the 1GP package to 2GP, then installs the 2GP version into subscriber orgs that already have the matching major and minor 1GP version. It does not change the package's metadata or disrupt subscriber data.[^s5] For a company's internal apps, unlocked packages are the alternative, since they need no packaging org or listing.[^s2]

## Connections

1GP is part of **application lifecycle management** for ISVs. It is **replaced by second-generation managed packages** through the package-migration path.[^s2][^s5] It **depends on the namespace registry** model, with the namespace bound to the packaging org rather than a Dev Hub.[^s2] Its one-way dependency rules **contrast with** the more flexible **package dependencies** of 2GP and unlocked packages.[^s1] It is an **alternative to unlocked packages** for distribution. Patch eligibility ties it to **AppExchange security review**, and uploads can be scripted through the **Tooling API**.[^s3]

## Sources

[^s1]: Salesforce Developers, "First-Generation Managed Packaging Developer Guide" (PDF). https://resources.docs.salesforce.com/260/latest/en-us/sfdc/pdf/pkg1_dev.pdf (accessed 2026-11-07)
[^s2]: Salesforce Developers, "Comparison of First- and Second-Generation Managed Packages". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-comparison.html (accessed 2026-11-07)
[^s3]: Salesforce Developers, "Create and Upload Patches in First-Generation Managed Packages". https://developer.salesforce.com/docs/platform/pkg1-dev/guide/patches-creating.html (accessed 2026-11-07)
[^s4]: Salesforce Developers, "Components Available in First-Generation Managed Packages". https://developer.salesforce.com/docs/platform/pkg1-dev/guide/first-gen-packageable-components.html (accessed 2026-11-07)
[^s5]: Salesforce Developers, "Move to 2GP: Migrate Your Managed Packages with Ease". https://developer.salesforce.com/docs/platform/pkg1-dev/guide/move-to-second-gen-pkg.html (accessed 2026-11-07)
[^s6]: Trailhead, "Create a Packaging Org" (CumulusCI for Managed Packages). https://trailhead.salesforce.com/content/learn/modules/cumulusci-for-managed-packages/create-a-packaging-org (accessed 2026-11-07)
