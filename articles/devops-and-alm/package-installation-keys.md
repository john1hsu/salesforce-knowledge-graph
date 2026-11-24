---
id: kt:package-installation-keys
type: Feature
title: Package Installation Keys
aliases: [package installation key, installation key, package password, password-protected package, installation-key-bypass]
domain: devops-and-alm
summary: >-
  A secret that a package developer attaches to a second-generation managed or unlocked package version so that only
  installers who know the key can see the package's contents and install it.
release: "Winter '27"
status: current
broader: [kt:second-generation-managed-packages, kt:unlocked-packages]
related: [kt:package-versioning-and-ancestry, kt:dev-hub, kt:first-generation-managed-packages, kt:agentexchange, kt:package-dependencies]
relations:
  - {predicate: configuredVia, object: kt:salesforce-cli}
sources:
  - id: s1
    title: "Package Installation Key for Second-Generation Managed Packages"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-config-installkey.html
    type: official-docs
    accessed: 2026-11-24
  - id: s2
    title: "Package Installation Key (Salesforce DX Developer Guide, unlocked packages)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_pkg_config_installkey.htm
    type: official-docs
    accessed: 2026-11-24
  - id: s3
    title: "package version create (Salesforce CLI Command Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_package_version_create.html
    type: official-docs
    accessed: 2026-11-24
  - id: s4
    title: "package version update (Salesforce CLI Command Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_package_version_update.html
    type: official-docs
    accessed: 2026-11-24
  - id: s5
    title: "package install (Salesforce CLI Command Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_package_install.html
    type: official-docs
    accessed: 2026-11-24
  - id: s6
    title: "Installing Packages (Application Installation Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.appExchangeInstallGuide.meta/appExchangeInstallGuide/appexchange_install_installation.htm
    type: official-docs
    accessed: 2026-11-24
created: 2026-11-24
---

# Package Installation Keys

A package installation key is a password-like secret that a developer sets on a package version so that only
authorized subscribers can install it. The developer shares the key with those subscribers, and the installer has to
enter it as the very first step of installation, whether the install runs from Salesforce CLI or from a browser.[^s1]
Until the key is supplied, the package's name and its list of components stay hidden, so the key protects the
package's contents as well as gating the install itself.[^s1][^s2] The same mechanism applies to second-generation
managed packages and to unlocked packages; the two developer guides describe it almost word for word.[^s1][^s2]

## How it works

The key is fixed when a package version is created, not when the package itself is defined. `sf package version
create` requires the developer to make an explicit choice: pass either `--installation-key` (short form `-k`) with a
value, or `--installation-key-bypass` (`-x`) to create a version that has no key.[^s3] The CLI reference warns that a
bypassed version can be installed by anyone, and Salesforce recommends setting a key to protect package contents and
block unauthorized installs.[^s3] A typical command is `sf package version create --package "Expense Manager"
--installation-key "<key>"`, and the bypass form is the same command with `--installation-key-bypass` instead.[^s1][^s2]

Installers then pass the key with `sf package install --package <alias or 04t id> --installation-key "<key>"`. The
install command has an `--installation-key` flag but no bypass flag, because the requirement belongs to the version,
not to the installer.[^s5][^s1] When the install runs in a browser instead, the installer types the key at the first
prompt. Salesforce's installation guide for listings on the marketplace tells installers to enter the password they
received from the publisher if the package is password-protected.[^s6]

To change the key on a version that already exists, the developer runs `sf package version update` with the
version's alias or 04t ID and a new `--installation-key` value. That flag is documented as the new key for a
key-protected package.[^s4][^s1] To see whether a given version requires a key, run `sf package version list` or
`sf package version report`.[^s2]

## Limits and gotchas

The key does not replace licensing or a security review. It gates only who can start an install and see the
component list.[^s1] Keep these points in mind:

- The choice is per version. Each new version needs `--installation-key` or `--installation-key-bypass` again, so CI scripts must pass one every time.[^s3]
- `sf package version update` documents only setting a new key; the pages opened for this article describe no flag for removing a key from an existing version.[^s4]
- A bypassed version is installable by anyone who has its 04t ID, so bypass suits only versions whose contents are not sensitive.[^s3][^s1]

Promotion to released status is a separate gate. Promoting a version requires creating it with `--code-coverage`
and meeting the coverage requirement, whether or not the version has a key.[^s3]

## When to use it (and when not)

Use a key for internal unlocked packages that carry proprietary code, for beta or pilot versions shared with
selected customers, and for any version that should not be installable by anyone holding its ID.[^s3][^s2] Bypass the
key for open-source or freely distributed packages, or for throwaway versions in scratch-org pipelines where no
protection is needed, since the documentation describes bypass as the option when security measures are not
required.[^s1] For first-generation managed packages the install flow still prompts for a publisher-supplied password
when one is set, but the CLI version-creation flags above belong to second-generation packaging.[^s6][^s1]

## Connections

Installation keys are a property of individual versions of **second-generation managed packages** and
**unlocked packages**, which is why both are listed as broader nodes.[^s1][^s2] They are set and changed through
**Salesforce CLI** package commands against the package's **Dev Hub**, and every version created in the
**package versioning and ancestry** chain needs its own key decision.[^s3][^s4] Installers meet the key when they
install from **AgentExchange** listings or directly by version ID with the CLI.[^s6][^s5] It is related to **package
dependencies** because dependent package versions are also installed by version ID with the same install command.[^s5]
**First-generation managed packages** show the same password prompt at install time.[^s6]

## Sources
[^s1]: Salesforce Developers, "Package Installation Key for Second-Generation Managed Packages". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-config-installkey.html (accessed 2026-11-24)
[^s2]: Salesforce Developers, "Package Installation Key" (Salesforce DX Developer Guide). https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_pkg_config_installkey.htm (accessed 2026-11-24)
[^s3]: Salesforce Developers, "package version create". https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_package_version_create.html (accessed 2026-11-24)
[^s4]: Salesforce Developers, "package version update". https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_package_version_update.html (accessed 2026-11-24)
[^s5]: Salesforce Developers, "package install". https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_package_install.html (accessed 2026-11-24)
[^s6]: Salesforce Developers, "Installing Packages" (Application Installation Guide). https://developer.salesforce.com/docs/atlas.en-us.appExchangeInstallGuide.meta/appExchangeInstallGuide/appexchange_install_installation.htm (accessed 2026-11-24)
