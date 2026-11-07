---
id: kt:package-dependencies
type: Feature
title: Package Dependencies
aliases: [package dependency, sfdx-project.json dependencies, transitive package dependencies, modular packaging]
domain: devops-and-alm
summary: >-
  The mechanism by which a second-generation package version (unlocked or managed 2GP) declares, in sfdx-project.json,
  the other package versions it builds on, which fixes the install order and lets an org be split into layered, modular packages.
release: "Winter '27"
status: current
broader: [kt:application-lifecycle-management, kt:salesforce-dx]
related: [kt:unlocked-packages, kt:second-generation-managed-packages, kt:custom-metadata-types, kt:apex-enterprise-patterns]
relations:
  - {predicate: configuredVia, object: kt:salesforce-cli}
  - {predicate: dependsOn, object: kt:dev-hub}
  - {predicate: contrastsWith, object: kt:first-generation-managed-packages}
sources:
  - id: s1
    title: "Project Configuration File for Unlocked Packages (Salesforce DX Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_pkg_config_file.htm
    type: official-docs
    accessed: 2026-11-07
  - id: s2
    title: "package version displaydependencies (Salesforce CLI Command Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_package_version_displaydependencies.html
    type: official-docs
    accessed: 2026-11-07
  - id: s3
    title: "Which Package Types Can Your Package Depend On? (Second-Generation Managed Packaging Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-dependency-overview.html
    type: official-docs
    accessed: 2026-11-07
  - id: s4
    title: "Explore the Easy Spaces App Packaging Architecture"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/quick-start-explore-the-easyspaces-sample-app/explore-the-app-packaging-architecture
    type: official-learning
    accessed: 2026-11-07
  - id: s5
    title: "5 Anti-Patterns in Package Dependency Design and How to Avoid Them"
    publisher: Salesforce Architects
    url: https://medium.com/salesforce-architects/5-anti-patterns-in-package-dependency-design-and-how-to-avoid-them-87bb50331cb8
    type: official-blog
    accessed: 2026-11-07
created: 2026-11-07
---

# Package Dependencies

A **package dependency** is a declaration that one package version needs another package to be installed first. In second-generation packaging, dependencies are listed per package directory in the optional `dependencies` attribute of `sfdx-project.json`; leaving it out means the package stands alone.[^s1] Dependencies are what turn a single "happy soup" org into a set of layered packages, each versioned and released on its own cadence, with the platform enforcing which layers must be present before another can install.[^s1][^s4]

## How it works

Each entry in the `dependencies` array names a package and a version. For a package owned by the same Dev Hub you can give a version alias (for example `MyPackage@0.1.0.1`) or a package name plus `versionNumber`; packages from outside the Dev Hub are referenced by an alias that includes the version, and a bare `04t` subscriber package version ID also works.[^s1] The `LATEST` keyword in the build segment (such as `1.3.0.LATEST`) pins the major, minor and patch while picking up the newest build at version-creation time.[^s1] An entry can carry a `branch` value when the dependency lives on a different branch than the dependent package, or `"branch": ""` when it has none.[^s1]

When there are several dependencies, they are listed in installation order, base libraries first.[^s1] Setting `calculateTransitiveDependencies` to `true` lets you list only direct dependencies and have the indirect ones computed for you.[^s1] With that flag on, `sf package version displaydependencies` emits the version's dependency graph as GraphViz DOT code; `--edge-direction root-last` orders it from the farthest leaf to the base package, which is the order the packages must be installed, and `--verbose` labels each node with its `04t` ID and version number.[^s2]

## Which package types can depend on which

Salesforce publishes a support matrix. An unlocked package may depend on first-generation managed, second-generation managed and other unlocked packages. A managed 2GP may depend on 1GP and 2GP managed packages, but depending on an unlocked package is marked not recommended. A 1GP managed package may depend on other 1GP packages but not on a managed 2GP, because the platform blocks installing 2GP packages into 1GP packaging orgs; Partner Support can grant case-by-case exceptions.[^s3] Depending on an unmanaged package is marked not recommended for every package type, and the matrix lists no supported dependencies for unmanaged packages themselves.[^s3]

## A worked example

The Easy Spaces sample app on Trailhead splits into four unlocked packages. `ESObjects` (objects, fields, layouts, permission sets) and `ESBaseStylesLWC` (styling, themes, page template) have no dependencies; `ESBaseCodeLWC` (reusable components, custom metadata, Lightning Message Service channels) depends on both; and `ESSpaceMgmtLWC`, which holds most of the app, depends on all three, using version specifiers like `4.0.0.LATEST`.[^s4] The implied install order is the two base packages, then the shared code layer, then the app layer.[^s4]

## Limits and gotchas

- `LATEST` only floats the build number; the major, minor and patch you name stay fixed, so moving to a new base release means editing the specifier.[^s1]
- Hard compile-time references across packages create tight coupling: changing a base service ripples into every dependent package, and tests that reach into another package's internals can force extra dependencies just to compile.[^s5]
- Salesforce architects recommend dependency injection to keep packages loosely coupled: program to interfaces, register implementations in custom metadata, and let an injector or event orchestrator in a core package load them at runtime, so subscriber packages never reference each other directly.[^s5]
- Packages that each add their own automation to shared objects like Account or Case can conflict; a trigger handler framework that enforces one automation entry point per object avoids this.[^s5]

## When to use it (and when not)

Use dependencies when an org is large enough that teams need independent release cycles and a shared base (data model, common services) consumed by several apps.[^s4][^s5] Start by extracting one well-defined, self-contained package rather than modularising everything at once; mixing packaged and unpackaged metadata is normal during that transition.[^s5]

## Connections

Package dependencies are a core practice of package-based **application lifecycle management** and the **Salesforce DX** project model, declared in `sfdx-project.json` and inspected with the **Salesforce CLI**.[^s1][^s2] Packages and their versions are owned by a **Dev Hub**, which is why same-Dev-Hub dependencies can use aliases.[^s1] They apply to both **unlocked packages** and **second-generation managed packages**, while the support matrix sets them against **first-generation managed packages**, which cannot depend on 2GP.[^s3] Loose coupling between packages leans on **custom metadata types** and the **Apex Enterprise Patterns** selector and factory layers.[^s5]

## Sources

[^s1]: Salesforce Developers, "Project Configuration File for Unlocked Packages (Salesforce DX Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_pkg_config_file.htm (accessed 2026-11-07)
[^s2]: Salesforce Developers, "package version displaydependencies (Salesforce CLI Command Reference)". https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_package_version_displaydependencies.html (accessed 2026-11-07)
[^s3]: Salesforce Developers, "Which Package Types Can Your Package Depend On?". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-dependency-overview.html (accessed 2026-11-07)
[^s4]: Trailhead, "Explore the Easy Spaces App Packaging Architecture". https://trailhead.salesforce.com/content/learn/projects/quick-start-explore-the-easyspaces-sample-app/explore-the-app-packaging-architecture (accessed 2026-11-07)
[^s5]: Salesforce Architects, "5 Anti-Patterns in Package Dependency Design and How to Avoid Them" (2021). https://medium.com/salesforce-architects/5-anti-patterns-in-package-dependency-design-and-how-to-avoid-them-87bb50331cb8 (accessed 2026-11-07)
