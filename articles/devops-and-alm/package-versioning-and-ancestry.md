---
id: kt:package-versioning-and-ancestry
type: Concept
title: Package Versioning and Ancestry
aliases: [package ancestry, package ancestor, ancestorVersion, ancestorId, 2GP version numbering, package version ancestry tree]
domain: devops-and-alm
summary: >-
  How second-generation managed package versions are numbered (MAJOR.MINOR.PATCH.BUILD) and linked to the released
  version they build on, which together decide what subscribers can upgrade from and to.
release: "Winter '27"
status: current
broader: [kt:second-generation-managed-packages, kt:application-lifecycle-management]
related: [kt:package-dependencies, kt:salesforce-dx, kt:appexchange-security-review]
relations:
  - {predicate: configuredVia, object: kt:salesforce-cli}
  - {predicate: dependsOn, object: kt:dev-hub}
  - {predicate: contrastsWith, object: kt:first-generation-managed-packages}
sources:
  - id: s1
    title: "Guidance for Package Version Numbering (Second-Generation Managed Packaging Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/dev2gp-version-guidance.html
    type: official-docs
    accessed: 2026-11-12
  - id: s2
    title: "Package Ancestors for Second-Generation Managed Packages"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-package-ancestor-intro.html
    type: official-docs
    accessed: 2026-11-12
  - id: s3
    title: "Specify a Package Ancestor in the Project File for a Second-Generation Managed Package"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-config-ancestors.html
    type: official-docs
    accessed: 2026-11-12
  - id: s4
    title: "Patch Versions for Second-Generation Managed Packages"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-create-patch-version.html
    type: official-docs
    accessed: 2026-11-12
  - id: s5
    title: "package version displayancestry (Salesforce CLI Command Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_package_version_displayancestry.html
    type: official-docs
    accessed: 2026-11-12
created: 2026-11-12
---

# Package Versioning and Ancestry

Every second-generation managed package (managed 2GP) version carries a version number of the form MAJOR.MINOR.PATCH.BUILD that the developer chooses, plus a platform-assigned subscriber package version ID beginning with `04t`.[^s1] **Ancestry** is the link from each new version to the released version it builds on. It is what lets a managed 2GP break out of strictly linear numbering, and it is what the platform uses to decide which installed versions can upgrade to which newer ones.[^s2]

## How version numbers work

The `versionNumber` attribute of a package directory in `sfdx-project.json` sets the number for the next version. If you hard-code all four parts you must bump it by hand before each build; putting the `NEXT` keyword in the build slot (for example `2.2.0.NEXT`) has the platform assign a unique build number instead.[^s1] The `--version-number` CLI flag overrides the project file for one build but does not write the new value back to `sfdx-project.json`.[^s1] Until promotion, several builds can share the same visible number because their `04t` IDs differ; once a MAJOR.MINOR.PATCH is promoted, no further builds with that combination can be created.[^s1] Salesforce leaves the meaning of major versus minor to the developer.[^s1]

## How ancestry works

Each new version names exactly one ancestor, and only versions already promoted to the managed-released state qualify.[^s2] In the project file the ancestor is given either as `ancestorVersion` (a major.minor.patch number, updated whenever those parts change) or as `ancestorId` (a `04t` ID or version alias, updated on every new version).[^s3] Salesforce recommends the `HIGHEST` keyword with either attribute, which always resolves to the highest promoted version and keeps numbering linear without edits; `NONE` creates a version with no ancestor.[^s3]

With linear ancestry, subscribers can upgrade from any lower version to any higher one, skipping versions if they like.[^s2] Ancestry also allows **branching**: you can abandon a flawed release, say 1.2, and make 1.1 the ancestor of 1.3, or let parallel teams grow a tree of versions instead of a single line.[^s2] Building on anything other than the highest promoted version requires `sf package version create --skip-ancestor-check`, and the same flag is needed to set `NONE` on a package that already has a promoted version.[^s3]

`sf package version displayancestry` prints the tree for a package (`0Ho` ID, all versions) or for one version (`04t`); `--dot-code` emits GraphViz DOT and `--verbose` adds each node's `04t` ID and full version number.[^s5]

## Patch versions

Any version with a non-zero patch number, such as 1.1.2.5, is a patch.[^s4] A patch must name a managed-released ancestor with the same major and minor numbers, may use another patch as that ancestor, and shares the upgrade path of its non-patch sibling, so 1.0.3 upgrades like 1.0.0.[^s4] Patches are restricted to fixes:

- No adding or deleting components, and no new features, settings, package dependencies or web services.[^s4]
- No changes to API or dynamic Apex access, no deprecating Apex, and no new `extends`, `virtual` or `global` relationships or modifiers.[^s4]
- Patch versioning must be requested from Partner Support for the namespace org, and only packages that have passed security review can get it.[^s4]

## Limits and gotchas

- Abandoning a version strands its subscribers: a branch can only upgrade along its own ancestry line, so customers on 1.5 cannot reach 1.7 if 1.5 was abandoned.[^s2]
- A patch can never be the direct ancestor of a non-patch version; use `HIGHEST` or a non-patch ancestor instead.[^s2][^s4]
- Existing customers cannot upgrade to a version built with `NONE`, so use it only for builds you will not promote.[^s3]
- To retire an abandoned build, delete it with `sf package version delete`; if that is not possible, change its installation key so nobody installs it by accident.[^s3]

## When to use it (and when not)

Keep `ancestorVersion: HIGHEST` and `NEXT` for day-to-day work; that gives a predictable, linear upgrade path.[^s1][^s3] Reach for explicit ancestors and `--skip-ancestor-check` only when a promoted release must be abandoned or parallel release trains are planned, and accept that each branch narrows who can upgrade where.[^s2][^s3] Use a patch rather than a new minor when a fix must reach customers who are not ready for new features.[^s4]

## Connections

Versioning and ancestry are a defining part of **second-generation managed packages** and of package-based **application lifecycle management**; the managed 2GP guide presents ancestry as the way to leave strictly linear numbering, which is the main point of contrast with **first-generation managed packages** in this graph.[^s2] They are configured in the **Salesforce DX** project file and driven through the **Salesforce CLI**, with versions owned by the **Dev Hub** that `displayancestry` queries.[^s3][^s5] **Package dependencies** pin to specific versions of other packages, so a package's numbering scheme shapes how dependents reference it, and patch access is tied to passing **security review**.[^s1][^s4]

## Sources

[^s1]: Salesforce Developers, "Guidance for Package Version Numbering". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/dev2gp-version-guidance.html (accessed 2026-11-12)
[^s2]: Salesforce Developers, "Package Ancestors for Second-Generation Managed Packages". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-package-ancestor-intro.html (accessed 2026-11-12)
[^s3]: Salesforce Developers, "Specify a Package Ancestor in the Project File for a Second-Generation Managed Package". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-config-ancestors.html (accessed 2026-11-12)
[^s4]: Salesforce Developers, "Patch Versions for Second-Generation Managed Packages". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-create-patch-version.html (accessed 2026-11-12)
[^s5]: Salesforce Developers, "package version displayancestry (Salesforce CLI Command Reference)". https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_package_version_displayancestry.html (accessed 2026-11-12)
