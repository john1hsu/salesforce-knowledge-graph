---
id: kt:second-generation-managed-packages
type: Feature
title: Second-Generation Managed Packages
aliases: [managed 2GP, 2GP, second-generation managed packaging, 2GP managed package]
domain: devops-and-alm
summary: >-
  Salesforce's current packaging technology for ISV partners: immutable, versioned managed packages built from source
  control with Salesforce CLI and a Dev Hub, sharing one namespace, and distributed to subscribers via AgentExchange.
release: "Winter '27"
status: current
broader: [kt:application-lifecycle-management, kt:salesforce-dx]
related: [kt:scratch-orgs, kt:apex-testing, kt:code-analyzer]
relations:
  - {predicate: dependsOn, object: kt:dev-hub}
  - {predicate: configuredVia, object: kt:salesforce-cli}
  - {predicate: alternativeTo, object: kt:unlocked-packages}
  - {predicate: replaces, object: kt:first-generation-managed-packages}
  - {predicate: dependsOn, object: kt:namespace-registry}
sources:
  - id: s1
    title: "Second-Generation Managed Packaging Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_dev2gp.htm
    type: official-docs
    accessed: 2026-11-01
  - id: s2
    title: "Before You Create Second-Generation Managed Packages"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-before.html
    type: official-docs
    accessed: 2026-11-01
  - id: s3
    title: "Workflow for Second-Generation Managed Packages"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-workflow.html
    type: official-docs
    accessed: 2026-11-01
  - id: s4
    title: "Code Coverage for Second-Generation Managed Packages"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-code-coverage.html
    type: official-docs
    accessed: 2026-11-01
  - id: s5
    title: "Gaps Between First-Generation and Second-Generation Managed Packaging"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-known-limitations.html
    type: official-docs
    accessed: 2026-11-01
  - id: s6
    title: "Move to Managed 2GP with Package Migrations"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2025/06/move-to-managed-2gp-with-package-migrations
    type: official-blog
    accessed: 2026-11-01
created: 2026-11-01
---

# Second-Generation Managed Packages

Second-generation managed packaging (managed 2GP) is how Salesforce ISV partners build, version and distribute commercial apps. Packages are created and managed with Salesforce CLI or scripts, can go through security review, and can be listed on AgentExchange. Unlike first-generation packaging, there are no packaging or patch orgs: the version control system is the source of truth for the package's metadata.[^s1] Salesforce recommends that customers and system integrators who are not distributing to many customers use unlocked packages instead.[^s1]

## How it works

Before building, a partner enables Dev Hub and second-generation packaging in its Partner Business Org, installs Salesforce CLI, and registers a namespace. The namespace is a 1–15 character alphanumeric prefix that isolates the package's components in a subscriber org; to use it in scratch orgs, the Developer Edition org where it was registered must be linked to the Dev Hub. Developers need a license plus a permission set granting Dev Hub access.[^s2] A key difference from 1GP is that several managed 2GP packages can share one namespace, and Salesforce advises using a single namespace across all of a partner's packages because it makes sharing code between them easier.[^s2][^s6]

The workflow runs from a DX project: authorize the Dev Hub, build metadata in a scratch org, set the namespace in `sfdx-project.json`, run `sf package create --package-type Managed` once, then repeatedly run `sf package version create` and install each version into a clean scratch org with `sf package install` for testing.[^s3] Each package version is an immutable snapshot. New versions start as beta and stay beta until promoted to managed-released.[^s3] Packages can declare explicit dependencies on other packages, version ancestry lets teams branch development, and patch versions can be created directly from the CLI.[^s6] Partners can also push upgrades to subscriber orgs without customer action, choosing the target orgs, version and timing, which is useful for hot fixes.[^s1]

## Limits and gotchas

- **Namespace and Dev Hub are permanent.** After a package is created, you can't add or change its namespace, and you can't move it to a different Dev Hub.[^s3]
- **75% Apex coverage to release.** Coverage is calculated only when a version is created with `--code-coverage`. Promotion fails if coverage was not computed, or if it is below 75%. Every Apex trigger in the package must also have test coverage. Versions built with `--skip-validation` have no coverage figure, so they can't be promoted.[^s4]
- **Betas are dead ends.** A beta version can't be upgraded, so keep betas out of sandboxes in your release pipeline.[^s1]
- **Remaining feature gaps versus 1GP.** Package versions can't be deprecated, Apex `VersionProvider` isn't supported, and you can't set a default label language.[^s5]

## Migrating from 1GP

Package migration became generally available in Summer '25. `sf package convert` turns the latest managed-released 1GP version into a beta 2GP version, which must be promoted and needs coverage computed. Installing it in a subscriber org that has the same major.minor 1GP version migrates that subscriber, and push upgrades can do this with `--migrate-to-2gp`. The subscriber's metadata is not changed. After a subscriber migrates, every later upgrade or patch for that org must come from 2GP. Salesforce suggests migrating leaf packages, the ones no other package depends on, before base packages.[^s6]

## When to use it (and when not)

Choose managed 2GP for any new app sold or distributed to many unrelated orgs. It provides IP-protected, upgradeable releases with license management through the License Management App and feature flags through the Feature Management App.[^s1] For internal apps that one company deploys to its own orgs, unlocked packages provide the same source-driven model without a namespace or listing overhead. Change sets and unpackaged Metadata API deployments do not produce versioned, upgradeable artifacts.[^s1][^s6]

## Connections

Managed 2GP is a practice within **Salesforce DX** and **application lifecycle management**. It depends on a **Dev Hub**, which owns the package and links the registered namespace (**namespace registry**).[^s2] It is driven by **Salesforce CLI** and tested in **scratch orgs**.[^s3] The coverage gate links it to **Apex testing**.[^s4] Its sibling is **unlocked packages**, the recommended option for customers.[^s1] It replaces **first-generation managed packages** through the package-migration path. Partners can gate version creation on a clean **Code Analyzer** scan in CI.[^s6]

## Sources

[^s1]: Salesforce Developers, "Second-Generation Managed Packaging Developer Guide". https://developer.salesforce.com/docs/atlas.en-us.264.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_dev2gp.htm (accessed 2026-11-01)
[^s2]: Salesforce Developers, "Before You Create Second-Generation Managed Packages". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-before.html (accessed 2026-11-01)
[^s3]: Salesforce Developers, "Workflow for Second-Generation Managed Packages". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-workflow.html (accessed 2026-11-01)
[^s4]: Salesforce Developers, "Code Coverage for Second-Generation Managed Packages". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-code-coverage.html (accessed 2026-11-01)
[^s5]: Salesforce Developers, "Gaps Between First-Generation and Second-Generation Managed Packaging". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-known-limitations.html (accessed 2026-11-01)
[^s6]: Salesforce Developers Blog, "Move to Managed 2GP with Package Migrations" (June 2025). https://developer.salesforce.com/blogs/2025/06/move-to-managed-2gp-with-package-migrations (accessed 2026-11-01)
