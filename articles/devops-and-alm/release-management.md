---
id: kt:release-management
type: Concept
title: Release Management
aliases: [Salesforce release management, release process, release planning, release strategy]
domain: devops-and-alm
summary: >-
  The discipline of planning, building, testing, deploying and communicating a coordinated set of approved changes to
  a Salesforce org, including scheduling those releases around Salesforce's own three seasonal platform upgrades.
release: "Winter '27"
status: concept
broader: [kt:application-lifecycle-management]
related: [kt:environment-strategy, kt:branching-strategy, kt:change-management-and-adoption]
relations:
  - {predicate: hasPart, object: kt:deployment-validation-and-quick-deploy}
  - {predicate: hasPart, object: kt:package-xml-manifest}
  - {predicate: dependsOn, object: kt:sandbox-types}
sources:
  - id: s1
    title: "Org Development Model: Plan for Changes to Your Org"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/org-development-model/plan-for-changes-to-your-org2
    type: official-learning
    accessed: 2026-11-14
  - id: s2
    title: "Salesforce DX Development Model: Release Your App"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/sfdx_dev_model/sfdx_dev_model_release
    type: official-learning
    accessed: 2026-11-14
  - id: s3
    title: "Package Development Readiness: Develop a Release Management Strategy"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/package-development-readiness/develop-a-release-management-strategy
    type: official-learning
    accessed: 2026-11-14
  - id: s4
    title: "Get to Know the Salesforce Release Process"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/sf_releases/sf_releases_start
    type: official-learning
    accessed: 2026-11-14
  - id: s5
    title: "Admin Release Countdown: Get Ready for Winter '27"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2026/admin-winter-27-release-countdown
    type: official-blog
    accessed: 2026-11-14
  - id: s6
    title: "Release Management in Agentforce IT Service: Get to Know Release Management"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/release-management-in-agentforce-it-service/get-to-know-release-management
    type: official-learning
    accessed: 2026-11-14
created: 2026-11-14
---

# Release Management

**Release management** is the practice of deciding what goes into a release, moving it through test environments, deploying it to production and telling users what changed. Salesforce's own training frames a release as the planning, testing and deployment of approved changes, and describes the work as a trade-off between speed and stability.[^s6] On the Salesforce Platform it has two sides: releasing a team's own customizations, and absorbing the platform upgrades that Salesforce ships to every org on a fixed seasonal schedule.[^s1][^s4]

## How a release moves through environments

In the org development model, each developer or admin builds in a personal Developer sandbox. Work is then combined in a shared Developer Pro sandbox to build the release, user-acceptance tested in a partial copy sandbox, and deployed to production. A full sandbox with production data supports user training afterwards.[^s1] All changes are stored in source control, which gives revision history and lets the team revert files and automate testing and deployment.[^s1]

The same unit names three tracking tools that keep a multi-person release coherent:

- A **change list** of what each person changed in their development org.[^s1]
- A **deployment run list** of manual steps to perform before and after the deployment.[^s1]
- A **project management tool**, such as Agile Accelerator or Jira, for the work itself.[^s1]

The release artifact is a `package.xml` manifest that lists the components to deploy, first to sandboxes and then to production.[^s1]

In the package development model, version control rather than production becomes the source of truth. Continuous integration runs automated tests on each merged change, a package version is installed in each test environment, the production steps are rehearsed in a sandbox, and the same version is then installed in production.[^s2] Changes that are not packaged can still be deployed with the Salesforce CLI command `project deploy start`.[^s2]

## Planning around Salesforce's seasonal releases

Salesforce upgrades every org three times a year, in the Spring, Summer and Winter releases, and all customers run the same version.[^s4] Each release cycle begins about 3 months before production, and sandbox instances are upgraded 4 to 6 weeks before production in the Sandbox Preview.[^s4] Upgrade dates appear on the Trust site up to a year ahead, and Trailhead advises planning backward from the sandbox and production dates of the next 2 or 3 releases.[^s4]

For Winter '27, Sandbox Preview began on August 28, 2026. Production upgrades followed on September 4, October 2 and October 9, depending on the instance.[^s5] Sandboxes had to be refreshed before a cut-off to land on a preview instance.[^s5] During that window sandboxes and production can run different platform versions, so a team's release calendar needs to account for which version each environment is on.[^s4][^s5]

## Strategy and governance

A release management strategy has to answer practical questions. Who deploys and migrates changes between environments? Who handles end-user training and update messages? How do teams see what other teams are releasing, and when?[^s3] Trailhead stresses that faster release models only work when teams have that visibility. It also advises a deliberate system for using sandboxes and scratch orgs, and a repository and branch structure that supports collaboration rather than isolating teams.[^s3] Emergency releases that fix critical issues sit beside regularly scheduled ones. A release manager coordinates schedules, assesses risk and dependencies, and monitors each release.[^s6]

## Gotchas

- A release that skips the integration stage often fails on conflicting changes from other team members; build the release in a shared org first.[^s1][^s3]
- Manual setup steps that metadata cannot carry are easy to forget unless they sit in the deployment run list.[^s1]
- A sandbox kept on the current platform version cannot be used to test the next seasonal release, so decide refresh timing before the preview cut-off.[^s4][^s5]

## Connections

Release management is the deployment-and-delivery part of **application lifecycle management** (`kt:application-lifecycle-management`).[^s1][^s2] It **depends on sandbox types** (`kt:sandbox-types`), since each stage of a release maps to a specific sandbox, and it is shaped by the wider **environment strategy** (`kt:environment-strategy`).[^s1][^s3] Its artifacts include the **package.xml manifest** (`kt:package-xml-manifest`), and pre-validating a production deployment with **deployment validation and quick deploy** (`kt:deployment-validation-and-quick-deploy`) is one step inside it.[^s1] A **branching strategy** (`kt:branching-strategy`) decides how changes are combined into a release.[^s3] **Change management and adoption** (`kt:change-management-and-adoption`) covers the user-facing half: training and communicating what each release brings.[^s3][^s6]

## Sources
[^s1]: Trailhead, "Org Development Model: Plan for Changes to Your Org". https://trailhead.salesforce.com/content/learn/modules/org-development-model/plan-for-changes-to-your-org2 (accessed 2026-11-14)
[^s2]: Trailhead, "Salesforce DX Development Model: Release Your App". https://trailhead.salesforce.com/content/learn/modules/sfdx_dev_model/sfdx_dev_model_release (accessed 2026-11-14)
[^s3]: Trailhead, "Package Development Readiness: Develop a Release Management Strategy". https://trailhead.salesforce.com/content/learn/modules/package-development-readiness/develop-a-release-management-strategy (accessed 2026-11-14)
[^s4]: Trailhead, "Get to Know the Salesforce Release Process". https://trailhead.salesforce.com/content/learn/modules/sf_releases/sf_releases_start (accessed 2026-11-14)
[^s5]: Salesforce Admins Blog, "Admin Release Countdown: Get Ready for Winter '27". https://admin.salesforce.com/blog/2026/admin-winter-27-release-countdown (accessed 2026-11-14)
[^s6]: Trailhead, "Release Management in Agentforce IT Service: Get to Know Release Management". https://trailhead.salesforce.com/content/learn/modules/release-management-in-agentforce-it-service/get-to-know-release-management (accessed 2026-11-14)
