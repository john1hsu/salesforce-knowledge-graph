---
id: kt:salesforce-cli
type: Tool
title: Salesforce CLI
aliases: [sf CLI, sf command, sfdx CLI, sfdx-cli, "@salesforce/cli", sf v2]
domain: devops-and-alm
summary: >-
  Salesforce's plugin-based command-line interface (the `sf` executable, formerly `sfdx`) for authorizing orgs,
  creating scratch orgs and sandboxes, deploying and retrieving source, running tests and scripting CI/CD pipelines.
release: "Winter '27"
status: current
broader: [kt:salesforce-dx, kt:application-lifecycle-management]
related: [kt:scratch-orgs, kt:source-tracking, kt:sandbox-types]
relations:
  - {predicate: integratesWith, object: kt:metadata-api}
  - {predicate: integratesWith, object: kt:devops-center}
  - {predicate: alternativeTo, object: kt:change-sets}
  - {predicate: dependsOn, object: kt:external-client-apps}
  - {predicate: hasPart, object: kt:code-analyzer}
sources:
  - id: s1
    title: "Salesforce CLI Configuration and Tips"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-setup/guide/sfdx-dev-cli.html
    type: official-docs
    accessed: 2026-10-31
  - id: s2
    title: "Move from sfdx (v7) to sf (v2)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-setup/guide/sfdx-setup-move-to-sf-v2.html
    type: official-docs
    accessed: 2026-10-31
  - id: s3
    title: "Salesforce CLI Plugins"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-setup/guide/sfdx-setup-plugins-overview.html
    type: official-docs
    accessed: 2026-10-31
  - id: s4
    title: "Update to the CLI Release Candidate or Nightly"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-setup/guide/sfdx-setup-install-cli-rc.html
    type: official-docs
    accessed: 2026-10-31
  - id: s5
    title: "Authorization (Salesforce DX Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-auth.html
    type: official-docs
    accessed: 2026-10-31
  - id: s6
    title: "Quick Start: Visual Studio Code for Salesforce Development — Make Visual Studio Code Salesforce Ready"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/content/learn/projects/quickstart-vscode-salesforce/vscode-salesforce-ready
    type: official-learning
    accessed: 2026-10-31
created: 2026-10-31
---

# Salesforce CLI

Salesforce CLI is the command-line tool at the centre of source-driven Salesforce development. Developers and pipelines use it to authorize a Dev Hub and other orgs, create scratch orgs, sync source between orgs and version control, and run tests.[^s1] It ships as the `@salesforce/cli` npm package and as OS-specific installers, and the executable is `sf`.[^s2][^s3] Most graphical tooling is layered on top of it. Trailhead's VS Code quick start installs the CLI first, and the Salesforce Extension Pack then runs CLI commands from menus, shortcuts and right-click actions.[^s6]

## sf versus sfdx

The CLI used to ship as `sfdx` (v7), and for a time `sfdx` bundled an early `sf` (v1). On July 12, 2023, sf (v2) became generally available. Salesforce stopped publishing updates to sfdx (v7) and sf (v1), and the download page began offering only sf (v2).[^s2] The two names are aliased, so `sfdx` now runs sf (v2), and existing scripts and VS Code invocations keep working with the same command names and flags.[^s2] Teams still on v7 must uninstall it before installing v2. In CI that means replacing the `sfdx-cli` npm install with `@salesforce/cli`, because keeping both makes the install fail with an `EEXIST` error.[^s2]

## How it works

**Topics and commands.** Commands are grouped under topics, for example `org` for creating and managing orgs and `config` for configuration variables. `--help` gives full detail at each level and `-h` a short summary. `sf commands --json` lists every command along with its flags.[^s1]

**Plugins.** Most of the CLI's functionality comes from plugins, which are themselves npm packages, of three kinds.[^s3]

- *Core plugins* install with the CLI and update with it. Examples are `plugin-org` (`org create scratch`), `plugin-deploy-retrieve` (`project deploy start`), `plugin-auth` (`org login web`), `plugin-data` and `plugin-agent` (`agent test run`).[^s3]
- *Just-in-time plugins* are installed automatically the first time one of their commands runs, then refreshed by `sf update`. Examples are `code-analyzer` and `plugin-flow`.[^s3]
- *User-installed plugins* are added with `sf plugins install` and can be pinned to a version. The CLI checks each plugin's digital signature and prompts before installing an unsigned one. Unattended jobs can list trusted plugins in an allowlist file to skip the prompt.[^s3]

**Configuration.** Config variables can be global or local to a Salesforce DX project, and local values win inside the project directory. Environment variables cover other settings. Errors print to the terminal, while all log messages go to a dated, rotating JSON log file under the user's home directory.[^s1]

## Authorization

You authorize an org once and then target it with `--target-org`, `--target-dev-hub`, an alias or a default org.[^s5] The **web flow** (`org login web`) opens a browser, so it suits interactive work but not CI. Without `--client-id` it uses a default connected app called Salesforce CLI. The **JWT flow** (`org login jwt`) is the recommended CI option. It needs a certificate, its signing private key and an external client app. The **SFDX auth URL** (`org login sfdx-url`) is the other option for automated environments.[^s5] The CLI requires an external client app (preferred) or a connected app in the target org.[^s5]

## Limits and gotchas

- **Weekly releases.** The stable channel is released weekly. A release candidate ships alongside each stable release, and a nightly build comes out daily. Salesforce suggests running CI against both stable and RC. `sf update stable-rc` or the npm tag `latest-rc` switches channel. `sf version` does not show which channel you are on.[^s4]
- **Step-up authentication.** If an org requires high-assurance authentication, the JWT flow and SFDX auth URL cannot be used for headless login.[^s5]
- **Local credentials.** Auth files are encrypted locally with 128-bit encryption by default, and 256-bit encryption can be turned on.[^s1]
- **Telemetry.** The CLI sends anonymous usage and error data by default, which can be disabled.[^s1]
- **API versions.** The API version and the source API version both affect deploys and retrieves. They are often set to the same value but behave differently.[^s1]

## When to use it (and when not)

Use the CLI for anything that must be repeatable and scripted: source-driven and package-based development, CI/CD pipelines, scratch org automation and test execution.[^s1][^s5] Teams that prefer clicks to commands can get most of the same operations through the VS Code extensions, which call the CLI underneath.[^s6] Its `project deploy start` command, provided by the core `plugin-deploy-retrieve` plugin, gives teams a deployment step they can script and repeat.[^s3]

## Connections

The CLI sits **under** `kt:salesforce-dx`, the source-driven toolset it anchors, and `kt:application-lifecycle-management`, whose build and deploy phases it automates.[^s1] It **integrates with** `kt:metadata-api` through `plugin-deploy-retrieve`, and is **related** to `kt:scratch-orgs`, `kt:sandbox-types` and `kt:source-tracking`, which `plugin-org` and source sync manage.[^s3][^s1] Because `project deploy start` gives a scriptable deployment route, this graph treats it as an **alternative to** `kt:change-sets`. It also **integrates with** `kt:devops-center`, whose article records it as an integration point.[^s3] It **depends on** `kt:external-client-apps`, which JWT authorization requires.[^s5] It **has part** `kt:code-analyzer`, delivered as a just-in-time plugin.[^s3]

## Sources

[^s1]: Salesforce Developers, "Salesforce CLI Configuration and Tips". https://developer.salesforce.com/docs/platform/sfdx-setup/guide/sfdx-dev-cli.html (accessed 2026-10-31)
[^s2]: Salesforce Developers, "Move from sfdx (v7) to sf (v2)". https://developer.salesforce.com/docs/platform/sfdx-setup/guide/sfdx-setup-move-to-sf-v2.html (accessed 2026-10-31)
[^s3]: Salesforce Developers, "Salesforce CLI Plugins". https://developer.salesforce.com/docs/platform/sfdx-setup/guide/sfdx-setup-plugins-overview.html (accessed 2026-10-31)
[^s4]: Salesforce Developers, "Update to the CLI Release Candidate or Nightly". https://developer.salesforce.com/docs/platform/sfdx-setup/guide/sfdx-setup-install-cli-rc.html (accessed 2026-10-31)
[^s5]: Salesforce Developers, "Authorization". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-auth.html (accessed 2026-10-31)
[^s6]: Trailhead, "Make Visual Studio Code Salesforce Ready". https://trailhead.salesforce.com/en/content/learn/projects/quickstart-vscode-salesforce/vscode-salesforce-ready (accessed 2026-10-31)
