---
id: kt:salesforce-dx
type: Tool
title: Salesforce DX
aliases: [SFDX, Salesforce Developer Experience, DX project, Salesforce DX project, sfdx-project.json]
domain: devops-and-alm
summary: >-
  Salesforce's developer tooling for source-driven development across the app lifecycle: a local project kept in
  version control as the source of truth, worked on with Salesforce CLI, scratch orgs, a Dev Hub and packaging.
release: "Winter '27"
status: current
broader: [kt:application-lifecycle-management]
related: [kt:devops-center, kt:change-sets, kt:sandbox-types]
relations:
  - {predicate: hasPart, object: kt:salesforce-cli}
  - {predicate: hasPart, object: kt:scratch-orgs}
  - {predicate: hasPart, object: kt:source-tracking}
  - {predicate: hasPart, object: kt:dev-hub}
  - {predicate: enables, object: kt:unlocked-packages}
  - {predicate: dependsOn, object: kt:metadata-api}
sources:
  - id: s1
    title: "How Salesforce Developer Experience (DX) Tooling Changes the Way You Work"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-intro.html
    type: official-docs
    accessed: 2026-11-01
  - id: s2
    title: "Salesforce DX Project Structure and Source Format"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-source-file-format.html
    type: official-docs
    accessed: 2026-11-01
  - id: s3
    title: "Salesforce DX Project Configuration"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-ws-config.html
    type: official-docs
    accessed: 2026-11-01
  - id: s4
    title: "Select and Enable a Dev Hub Org"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-setup-enable-devhub.html
    type: official-docs
    accessed: 2026-11-01
  - id: s5
    title: "App Development with Salesforce DX: Get Ready to Create an App"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/sfdx_app_dev/sfdx_app_dev_create_app
    type: official-learning
    accessed: 2026-11-01
  - id: s6
    title: "Salesforce DX Is Now Generally Available"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2017/10/salesforce-dx-is-now-generally-available
    type: official-blog
    accessed: 2026-11-01
created: 2026-11-01
---

# Salesforce DX

Salesforce DX (Developer Experience) is Salesforce's set of tooling for building and managing apps on the platform across their whole lifecycle, built around source-driven development, governed team collaboration and modern agile practice.[^s1] Its central idea is that code and metadata live outside the org, and that the version control system, not any org, holds the authoritative copy.[^s1] Developers can pair the tooling with any IDE or editor; the DX tools need the **API Enabled** system permission because they work programmatically against orgs.[^s1]

Salesforce DX reached general availability on October 17, 2017, alongside the Winter '18 release, after an open beta that began in June 2017.[^s6] Salesforce described that launch as a first wave centred on the CLI, scratch orgs and Visual Studio Code extensions, designed so teams could adopt the pieces incrementally.[^s6]

## Building blocks

- **Salesforce CLI**, the command line used for development, continuous integration and delivery.[^s1]
- **Scratch orgs**, short-lived configurable orgs for development and automation.[^s1]
- **Dev Hub**, the production or Developer Edition org that creates and manages scratch orgs, unlocked packages, second-generation managed packages and namespaces.[^s4]
- **Packaging**, **source tracking**, sandbox support and optional tools such as Salesforce Extensions for VS Code and DevOps Center, all documented in the same developer guide.[^s1]

Salesforce's suggested starting path is: install the CLI, enable Dev Hub, try a sample repository, create an app, then migrate existing customizations by retrieving them with the Metadata API into a DX project.[^s1]

## The DX project

A DX project is a local folder holding package metadata plus the files needed to sync with orgs.[^s5] `sfdx-project.json` marks the folder as a project and records source paths, namespace and API version; `config/project-scratch-def.json` describes the shape of scratch orgs; and source usually sits under `force-app`.[^s5] The CLI reads `sfdx-project.json` to decide which source to track between project and org, and the `.sf` folder of local org state should be kept out of source control.[^s5]

Key `sfdx-project.json` settings include the required `packageDirectories` list (only one may be the default, which receives retrieved changes and is used for second-generation packages), `namespace`, `sfdcLoginUrl`, `packageAliases`, `replacements` for string substitution before deploy, and `sourceApiVersion`, which controls which fields of each metadata type are deployed, retrieved and converted.[^s3]

## Source format

DX projects use **source format**, a different file layout from the **metadata format** the Metadata API expects; retrieves store files in source format and the CLI converts them back on deploy.[^s2] Custom objects and their translations are decomposed into subdirectories by default so large files are easier to navigate and produce fewer merge conflicts; other types such as permission sets and custom labels can opt in via the beta `sourceBehaviorOptions` setting, changed with `project convert source-behavior` rather than by hand.[^s2][^s3] XML-bearing files carry an `-meta.xml` suffix, and static resource archives are expanded into folders on retrieve and re-zipped on deploy.[^s2]

## Limits and gotchas

- Dev Hub is available in Developer, Enterprise, Performance and Unlimited editions, cannot be enabled in a sandbox, and cannot be disabled once enabled.[^s4]
- The Dev Hub org's edition caps how many scratch orgs can be created per day and be active at once; deleting a scratch org frees an allocation.[^s5]
- Folder names such as `lwc`, `aura`, `experiences` and `documents` are required, not conventions.[^s2]
- `pushPackageDirectoriesSequentially` is deprecated along with the old `force:source:push`; deploy packages in order with separate `project deploy start` calls.[^s3]

## When to use it (and when not)

Adopt DX when a team wants Git as the source of truth, repeatable disposable environments and package-based releases.[^s1] Because adoption can be incremental, teams can first move org customizations into a DX project and version control, then add scratch orgs and packaging later.[^s6][^s1] Teams that want a guided interface for managing deployments can add DevOps Center, which Salesforce lists among the optional DX tools.[^s1]

## Connections

Salesforce DX is the umbrella for source-driven **application lifecycle management**. It **has parts** the **Salesforce CLI**, **scratch orgs**, **source tracking** and the **Dev Hub**, which in turn **enables** **unlocked packages** and second-generation managed packages.[^s1][^s4] Every deploy and retrieve ultimately **depends on** the **Metadata API**, with the CLI translating between source and metadata formats.[^s2] Its version-controlled project contrasts with org-to-org **change sets**, which keep no external source of truth; the guide also covers working with **sandbox types**, and lists **DevOps Center** as an optional companion tool.[^s1]

## Sources
[^s1]: Salesforce Developers, "How Salesforce Developer Experience (DX) Tooling Changes the Way You Work". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-intro.html (accessed 2026-11-01)
[^s2]: Salesforce Developers, "Salesforce DX Project Structure and Source Format". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-source-file-format.html (accessed 2026-11-01)
[^s3]: Salesforce Developers, "Salesforce DX Project Configuration". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-ws-config.html (accessed 2026-11-01)
[^s4]: Salesforce Developers, "Select and Enable a Dev Hub Org". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-setup-enable-devhub.html (accessed 2026-11-01)
[^s5]: Trailhead, "App Development with Salesforce DX: Get Ready to Create an App". https://trailhead.salesforce.com/content/learn/modules/sfdx_app_dev/sfdx_app_dev_create_app (accessed 2026-11-01)
[^s6]: Salesforce Developers Blog, "Salesforce DX Is Now Generally Available". https://developer.salesforce.com/blogs/2017/10/salesforce-dx-is-now-generally-available (accessed 2026-11-01)
