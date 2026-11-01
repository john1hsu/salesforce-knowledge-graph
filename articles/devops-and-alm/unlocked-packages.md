---
id: kt:unlocked-packages
type: Feature
title: Unlocked Packages
aliases: [unlocked package, org-dependent unlocked package, org-dependent package]
domain: devops-and-alm
summary: >-
  A second-generation packaging option for customers' internal apps: a versioned, immutable container of metadata
  built from version control with Salesforce CLI and a Dev Hub, whose installed components stay editable in the target org.
release: "Winter '27"
status: current
broader: [kt:application-lifecycle-management, kt:salesforce-dx]
related: [kt:scratch-orgs, kt:apex-testing]
relations:
  - {predicate: dependsOn, object: kt:dev-hub}
  - {predicate: configuredVia, object: kt:salesforce-cli}
  - {predicate: alternativeTo, object: kt:second-generation-managed-packages}
  - {predicate: contrastsWith, object: kt:change-sets}
sources:
  - id: s1
    title: "Unlocked Packages (Salesforce DX Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.250.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_pkg_intro.htm
    type: official-docs
    accessed: 2026-11-01
  - id: s2
    title: "What's an Unlocked Package?"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-unlocked-pkg-whats-a-package.html
    type: official-docs
    accessed: 2026-11-01
  - id: s3
    title: "Create Org-Dependent Unlocked Packages"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-unlocked-pkg-org-dependent.html
    type: official-docs
    accessed: 2026-11-01
  - id: s4
    title: "Push a Package Upgrade"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-unlocked-pkg-push-upgrade.html
    type: official-docs
    accessed: 2026-11-01
  - id: s5
    title: "Know Your Orgs"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-unlocked-pkg-before-know-orgs.html
    type: official-docs
    accessed: 2026-11-01
  - id: s6
    title: "Unlocked Packages for Customers: Build Your First Unlocked Package"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/unlocked-packages-for-customers/build-your-first-unlocked-package
    type: official-learning
    accessed: 2026-11-01
created: 2026-11-01
---

# Unlocked Packages

An unlocked package is a container of related metadata (features, customizations and schema) that lets a team add, change and remove metadata in an org in a trackable way, and apply the same package to many orgs.[^s2] Salesforce positions them for internal business apps: unless you distribute through AppExchange, they are the recommended package type for most use cases, while AppExchange partners should use second-generation managed packages instead.[^s1] Typical uses are carving existing org metadata into packages, packaging a new app, or extending an AppExchange app.[^s1]

The defining principle is source-driven: the authoritative copy of the packaged metadata is the version control system, not whatever currently sits in an org.[^s1] Unlike managed packages, unlocked packages are not subject to per-component manageability rules.[^s2]

## How it works

Every package belongs to exactly one **Dev Hub** org, which is also where namespaces are linked and where `sf package` commands are authorized; packages bound for production should live in a Dev Hub that is a production org, because if a non-production Dev Hub expires the installed package can no longer be updated.[^s5] A namespace is optional and needs a separate namespace org linked to the Dev Hub.[^s5]

Each package gets an entry in `sfdx-project.json` describing its alias, version details, dependencies, features and org settings.[^s1] The Trailhead workflow runs `sf package create --package-type Unlocked`, which records a `0Ho` package ID under `packageAliases`, then `sf package version create`, then `sf package install` into a scratch org or other target.[^s6] Choosing no namespace is advised when migrating unpackaged ("happy soup") metadata, so API names do not change.[^s6]

Adding metadata produces a new **package version**. Each version is an immutable snapshot with its own number, which makes it usable as a CI/CD artifact; installing a version behaves much like a metadata deployment, and subscribers move forward by upgrading.[^s2] New versions start as beta and can go only to scratch orgs, sandboxes and Developer Edition orgs; `sf package version promote` marks a version released so it can be installed anywhere, including production.[^s6] An installation key can protect a version from unauthorized installs.[^s6]

Upgrades can also be pushed: push upgrades are on by default for unlocked packages and are started from Salesforce CLI or the SOAP API (not the UI), letting the owner choose orgs, version and timing — useful for urgent fixes.[^s4] Apex is compiled when a pushed upgrade installs, and a push works even when the version requires a password.[^s4]

## Limits and gotchas

- Apex in a version must reach **75%** code coverage before it can be promoted and installed in production.[^s6][^s3]
- "Unlocked" means admins can edit packaged metadata directly in production for emergencies, but the next package upgrade can overwrite those changes; Salesforce recommends governance so admins report such edits to developers.[^s2]
- When a version is built, profile settings unrelated to the package's own metadata are discarded.[^s1]
- Uninstalling removes all of the package's components, including deprecated ones.[^s1]
- Package creation, version creation and installation can each take several minutes.[^s6]

## Org-dependent variant

An **org-dependent** unlocked package (created with the `--org-dependent` flag) may reference unpackaged metadata in the install org. Validation shifts from version creation to installation, so it installs only into orgs containing that metadata and cannot depend on other packages.[^s3] Salesforce skips code coverage for these packages but still urges thorough Apex testing, and recommends developing in a sandbox with source tracking enabled.[^s3] It is a pragmatic first step for orgs too tangled to package cleanly.

## When to use it (and when not)

Choose unlocked packages when an enterprise wants modular, versioned, repeatable releases of its own customizations driven from Git.[^s1][^s2] Choose second-generation managed packages to sell or distribute IP on AppExchange.[^s1] Compared with the traditional model of AppExchange packages plus loose unpackaged metadata, packages give a clear inventory of which component came from which package in the installed org.[^s1][^s2]

## Connections

Unlocked packages are a building block of package-based **application lifecycle management** and part of the **Salesforce DX** toolset. They **depend on** the **Dev Hub**, which owns them, and are **configured via** the **Salesforce CLI**.[^s5][^s6] **Scratch orgs** are the usual place to build and test versions, and **Apex testing** gates promotion through the coverage rule.[^s6] They are the internal-app **alternative to** **second-generation managed packages**, and **contrast with** **change sets**, which move metadata between orgs without a versioned artifact or a source-control source of truth.[^s1][^s2]

## Sources
[^s1]: Salesforce Developers, "Unlocked Packages (Salesforce DX Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.250.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_pkg_intro.htm (accessed 2026-11-01)
[^s2]: Salesforce Developers, "What's an Unlocked Package?". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-unlocked-pkg-whats-a-package.html (accessed 2026-11-01)
[^s3]: Salesforce Developers, "Create Org-Dependent Unlocked Packages". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-unlocked-pkg-org-dependent.html (accessed 2026-11-01)
[^s4]: Salesforce Developers, "Push a Package Upgrade". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-unlocked-pkg-push-upgrade.html (accessed 2026-11-01)
[^s5]: Salesforce Developers, "Know Your Orgs". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-unlocked-pkg-before-know-orgs.html (accessed 2026-11-01)
[^s6]: Trailhead, "Unlocked Packages for Customers: Build Your First Unlocked Package". https://trailhead.salesforce.com/content/learn/modules/unlocked-packages-for-customers/build-your-first-unlocked-package (accessed 2026-11-01)
