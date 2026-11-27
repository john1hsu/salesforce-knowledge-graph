---
id: kt:package-uninstall
type: Feature
title: Package Uninstall
aliases: [uninstall a package, uninstalling a package, package uninstallation, sf package uninstall, force:package:uninstall, uninstall export file]
domain: devops-and-alm
summary: >-
  Removing an installed package from a subscriber org, from Setup's Installed Packages page or (for
  second-generation packages) with sf package uninstall; it deletes every package component and its data, can save a
  short-lived export file first, and is blocked while outside components still reference the package.
created: 2026-11-27
release: "Winter '27"
status: current
broader: [kt:second-generation-managed-packages, kt:first-generation-managed-packages]
related: [kt:post-install-scripts, kt:unlocked-packages, kt:custom-objects, kt:record-types, kt:sharing-rules]
relations:
  - {predicate: configuredVia, object: kt:salesforce-cli}
  - {predicate: dependsOn, object: kt:roll-up-summary-field}
sources:
  - id: s1
    title: "Uninstall a Second-Generation Managed Package"
    publisher: Salesforce Developers (Second-Generation Managed Packaging Developer Guide)
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-installed-pkgs-uninstall.html
    type: official-docs
    accessed: 2026-11-27
  - id: s2
    title: "Uninstall a First-Generation Managed Package"
    publisher: Salesforce Developers (First-Generation Managed Packaging Developer Guide)
    url: https://developer.salesforce.com/docs/platform/pkg1-dev/guide/packaging-uninstall.html
    type: official-docs
    accessed: 2026-11-27
  - id: s3
    title: "package uninstall (Salesforce CLI Command Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_package_uninstall.html
    type: official-docs
    accessed: 2026-11-27
  - id: s4
    title: "After Installing a Package (Application Installation Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/appexchange-install-guide/guide/appexchange-install-postinstall.html
    type: official-docs
    accessed: 2026-11-27
---

# Package Uninstall

**Package uninstall** is how a subscriber org removes a package it installed, whether a marketplace app, a
first-generation (1GP) or second-generation (2GP) managed package, or an internal package. An uninstall deletes every
component the package brought, including components the publisher has since deprecated.[^s1][^s2] For a managed
package it also removes the data stored in those components, plus customizations the subscriber layered on them, such
as custom fields or links.[^s4] It is a one-way operation, so the main design questions are what to save first and
what will stop it from running.

## How to run it

In the browser the process is the same for every package type. Open Setup, find **Installed Packages** with Quick
Find, click **Uninstall** beside the package, choose whether to save and export a copy of the package's data, then
confirm with "Yes, I want to uninstall" and click Uninstall.[^s1][^s2][^s4]

Second-generation packages can also be removed from the command line. `sf package uninstall` (old alias
`force:package:uninstall`) takes a required `--package` (`-p`), which is either a package version ID starting with
`04t` or a version alias, and a `--target-org` (`-o`) unless a default target org is configured.[^s3] `--wait` (`-w`)
sets how many minutes to wait for the uninstall status and defaults to 0, so by default the command returns at once
and the uninstall runs in the background.[^s3] `sf package installed list` shows what is installed. The CLI reference
states that first-generation packages are uninstalled from Setup, not with this command.[^s3] The 2GP guide gives the
example `sf package uninstall --package "Expense Manager@2.3.0-5"`.[^s1]

## What gets deleted, and the export file

Deleting a packaged custom object also deletes its dependent parts: custom fields, validation rules, custom buttons and
links, workflow rules and approval processes.[^s2][^s4] Because records go too, the uninstall page offers to save an
export file. It holds the package's data along with related notes and attachments. When the uninstall finishes,
Salesforce emails a download link to the user who ran it, and the file is also listed under Installed Packages with
Download and Del links.[^s4] Salesforce deletes export files two days after the uninstall completes, so the
installation guide advises copying the file somewhere else promptly.[^s4]

## What blocks an uninstall

An uninstall fails when something outside the package still points at a package component. The documented
blockers are:[^s1][^s2][^s4]

- A component on a standard object, such as a packaged custom field on Account, that another component references.[^s1][^s2]
- A custom object in the package that a component in a different package references.[^s1][^s2]
- A component the subscriber added to a packaged folder after installation, such as a report saved there.[^s1][^s4]
- A packaged letterhead used by an email template that was created after the install.[^s1][^s2]
- A packaged custom field that Einstein Prediction Builder or Case Classification references.[^s1][^s2]
- Removing the package would leave no active business or person account record types.[^s1][^s4]
- A background job, such as a roll-up summary field recalculation, is still updating a field the package added.[^s1][^s2]

In practice, teams remove or repoint the referencing components first (a report, a formula, a flow, another
package's field) and wait for running recalculation jobs to finish before trying again.[^s1][^s4]

## Gotchas and when to use it

- Check references before scheduling the work: each blocker above stops the whole uninstall, not just one component.[^s1][^s2]
- For a managed package whose licence has simply expired, uninstalling may be unnecessary: criteria-based sharing rules on its fields are flagged "(expired)" and stop recalculating, but existing shares remain.[^s4]
- Script CLI uninstalls with a non-zero `--wait` when a pipeline must know the result before its next step.[^s3]
- Treat the two-day export window as part of the plan, and download the file before relying on it for an audit or a data migration.[^s4]

## Connections

- **Broader:** `kt:second-generation-managed-packages` and `kt:first-generation-managed-packages`. Uninstall is the last step in a subscriber's package lifecycle for both, and only the 2GP path supports the CLI.[^s1][^s2][^s3]
- **Related:** `kt:unlocked-packages` are also second-generation packages listed under Installed Packages and removed the same way.[^s3] `kt:post-install-scripts` is the publisher-side code tied to install and uninstall events; this node covers the subscriber steps in Setup and the CLI.[^s1][^s3]
- **Related:** `kt:custom-objects` (deleting a packaged object deletes its fields, rules and buttons), `kt:record-types` (the account record type blocker) and `kt:sharing-rules` (expired-licence behaviour).[^s2][^s4]
- **Configured via** `kt:salesforce-cli`, through `sf package uninstall`.[^s3]
- **Depends on** `kt:roll-up-summary-field` jobs: a pending recalculation on a packaged field blocks the uninstall.[^s1]

## Sources
[^s1]: Salesforce Developers, "Uninstall a Second-Generation Managed Package". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-installed-pkgs-uninstall.html (accessed 2026-11-27)
[^s2]: Salesforce Developers, "Uninstall a First-Generation Managed Package". https://developer.salesforce.com/docs/platform/pkg1-dev/guide/packaging-uninstall.html (accessed 2026-11-27)
[^s3]: Salesforce Developers, "package uninstall" (Salesforce CLI Command Reference). https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_package_uninstall.html (accessed 2026-11-27)
[^s4]: Salesforce Developers, "After Installing a Package" (Application Installation Guide). https://developer.salesforce.com/docs/platform/appexchange-install-guide/guide/appexchange-install-postinstall.html (accessed 2026-11-27)
