---
id: kt:post-install-scripts
type: Feature
title: Post Install Scripts
aliases: [post-install script, post install script, InstallHandler, UninstallHandler, uninstall script, onInstall, postInstallScript]
domain: devops-and-alm
summary: >-
  Apex classes that a managed package runs automatically in the subscriber org: an InstallHandler after the package
  is installed or upgraded, and an optional UninstallHandler before it is uninstalled.
release: "Winter '27"
status: current
broader: [kt:first-generation-managed-packages, kt:second-generation-managed-packages]
related: [kt:push-upgrades, kt:package-versioning-and-ancestry, kt:apex-testing, kt:asynchronous-apex, kt:salesforce-dx]
relations:
  - {predicate: dependsOn, object: kt:apex}
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: dependsOn, object: kt:apex-security-with-sharing}
  - {predicate: configuredVia, object: kt:salesforce-cli}
sources:
  - id: s1
    title: "How Does a Post Install Script Work? (First-Generation Managed Packaging Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg1-dev/guide/apex-post-install-script-intro.html
    type: official-docs
    accessed: 2026-11-20
  - id: s2
    title: "InstallHandler Interface (Apex Reference Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_install_handler.htm
    type: official-docs
    accessed: 2026-11-20
  - id: s3
    title: "Customize Second-Generation Managed Package Installs and Uninstalls Using Scripts"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-customize-installs.html
    type: official-docs
    accessed: 2026-11-20
  - id: s4
    title: "How Does an Uninstall Script Work? (First-Generation Managed Packaging Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg1-dev/guide/apex-uninstall-script-intro.html
    type: official-docs
    accessed: 2026-11-20
  - id: s5
    title: "Example of a Post Install Script (First-Generation Managed Packaging Developer Guide, Winter '27)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.pkg1_dev.meta/pkg1_dev/apex_post_install_script_create.htm
    type: official-docs
    accessed: 2026-11-20
  - id: s6
    title: "Advanced Project Configuration Parameters for Second-Generation Managed Packages"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev2gp-adv-config-file.html
    type: official-docs
    accessed: 2026-11-20
created: 2026-11-20
---

# Post Install Scripts

A post install script is an Apex class, shipped inside a managed package, that the platform runs automatically in a subscriber org once the package has been installed or upgraded.[^s1][^s6] The class implements the `InstallHandler` interface, whose single method is `onInstall(InstallContext context)`.[^s1][^s2] Its counterpart is the uninstall script: a class implementing `UninstallHandler`, whose `onUninstall(UninstallContext context)` method runs in the subscriber org before the package is removed.[^s4][^s6] Package developers use them to seed default records and settings, migrate data between versions, schedule jobs, or tell the installing admin what happened.[^s5][^s2]

## How it works

The `InstallContext` passed to `onInstall` describes the installation. It exposes the subscriber `organizationId()`, the `installerId()` of the user who installed, `isUpgrade()`, `isPush()`, and `previousVersion()`, which is null on a first install and otherwise the three-part version being replaced.[^s1] Comparing that value with `Version.compareTo()` lets one script branch by upgrade path. The official example creates an account and a survey record on a fresh install, does version-specific work when upgrading from 1.0, and adds separate handling for upgrades and push upgrades.[^s5][^s1] `UninstallContext` is smaller, offering only `organizationId()` and `uninstallerId()`.[^s4]

The script runs after the package's tests have run, under default governor limits, as a special system user that represents the package rather than as the installer. That user can be read through `UserInfo` at runtime but does not exist during tests.[^s2] If `onInstall` throws, the install or upgrade is aborted, and the error is emailed to the user named in the package's **Notify on Apex Error** setting; with nobody set, the installation details are lost.[^s2]

For second-generation managed packages the scripts are declared per package directory in `sfdx-project.json` with the optional `postInstallScript` and `uninstallScript` keys, or passed as `--post-install-script` and `--uninstall-script` to `sf package version create`, where the flags override the file.[^s3][^s6] In both cases the named classes must be part of the package's own metadata.[^s3] Error emails for 2GP go to a Dev Hub user set with `--error-notification-username` on `sf package create` or `sf package update`, stored as `PackageErrorUsername` on the Tooling API `Package2` object.[^s3] A separate `postInstallUrl` setting points subscribers to human-readable post-install instructions; it runs nothing.[^s3][^s6]

## Limits and gotchas

- **No session, no synchronous callouts.** The script can't read session IDs, and callouts must be asynchronous; they run only after the script and install commit.[^s2]
- **Async work is allowed.** It can start batch, scheduled and future jobs, which is the usual way to move heavy data work out of the install transaction.[^s2]
- **Avoid `with sharing` callees.** Calling a packaged class declared `with sharing` from the script can stop the package from installing.[^s2]
- **Failure blocks installation.** Any unhandled exception aborts the whole install or upgrade, so guard each step and log rather than throw.[^s2]
- **Test with `Test.testInstall`.** It takes the handler, the prior version (or null) and an optional push flag, so each upgrade path can be unit-tested.[^s2][^s5]
- **Version numbers.** `previousVersion()` is always three-part, and comparing a two-part with a three-part version ignores the patch number.[^s1]

## When to use it (and when not)

Use a post install script for setup that every subscriber needs and that must track the package version, such as default custom settings, initial records, or a one-time data migration on upgrade.[^s1][^s5] Keep it small and idempotent, because it can run on fresh installs, manual upgrades and push upgrades alike, and push it to asynchronous Apex when the work is large.[^s1][^s2] Instructions an admin must follow, such as permission assignments, belong at the `postInstallUrl` page rather than in code.[^s3]

## Connections

Post install scripts are a feature of **first-generation** and **second-generation managed packages**, the two models that document them.[^s1][^s3] They are most useful alongside **push upgrades**, since `isPush()` tells the script that no admin started the install, and alongside **package versioning and ancestry**, because `previousVersion()` drives upgrade logic.[^s1] The code is **Apex**, governed by **governor limits**, unit-tested through **Apex testing**'s `Test.testInstall`, and often hands work to **asynchronous Apex**.[^s2] Its sharing constraint ties it to **Apex security and `with sharing`**.[^s2] For 2GP, scripts are configured through **Salesforce DX** project files and the **Salesforce CLI**.[^s3][^s6]

## Sources

[^s1]: Salesforce Developers, "How Does a Post Install Script Work?". https://developer.salesforce.com/docs/platform/pkg1-dev/guide/apex-post-install-script-intro.html (accessed 2026-11-20)
[^s2]: Salesforce Developers, "InstallHandler Interface", Apex Reference Guide. https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_install_handler.htm (accessed 2026-11-20)
[^s3]: Salesforce Developers, "Customize Second-Generation Managed Package Installs and Uninstalls Using Scripts". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-customize-installs.html (accessed 2026-11-20)
[^s4]: Salesforce Developers, "How Does an Uninstall Script Work?". https://developer.salesforce.com/docs/platform/pkg1-dev/guide/apex-uninstall-script-intro.html (accessed 2026-11-20)
[^s5]: Salesforce Developers, "Example of a Post Install Script". https://developer.salesforce.com/docs/atlas.en-us.264.0.pkg1_dev.meta/pkg1_dev/apex_post_install_script_create.htm (accessed 2026-11-20)
[^s6]: Salesforce Developers, "Advanced Project Configuration Parameters for Second-Generation Managed Packages". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev2gp-adv-config-file.html (accessed 2026-11-20)
