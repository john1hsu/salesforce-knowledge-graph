---
id: kt:unmanaged-packages
type: Feature
title: Unmanaged Packages
aliases: [unmanaged package, unmanaged 1GP package, Package Manager unmanaged package]
domain: devops-and-alm
summary: >-
  A first-generation Salesforce package built in Setup's Package Manager and uploaded to produce an install link.
  Installed components become fully editable in the subscriber org, but the publisher loses control of them and the
  package cannot be upgraded, so it suits open-source drops, samples and one-time templates rather than ongoing delivery.
release: "Winter '27"
status: current
broader: [kt:application-lifecycle-management]
related: [kt:first-generation-managed-packages, kt:agentexchange, kt:package-xml-manifest, kt:tooling-api]
relations:
  - {predicate: alternativeTo, object: kt:unlocked-packages}
  - {predicate: alternativeTo, object: kt:change-sets}
  - {predicate: contrastsWith, object: kt:push-upgrades}
sources:
  - id: s1
    title: "Developing and Distributing Unmanaged Packages"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg1-dev/guide/packaging-developing-unmanaged.html
    type: official-docs
    accessed: 2026-11-22
  - id: s2
    title: "Create and Upload an Unmanaged Package"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg1-dev/guide/packaging-uploading-unmanaged.html
    type: official-docs
    accessed: 2026-11-22
  - id: s3
    title: "Components Available in Unmanaged Packages"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg1-dev/guide/packaging-unmanaged-components.html
    type: official-docs
    accessed: 2026-11-22
  - id: s4
    title: "What's an Unlocked Package?"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-unlocked-pkg-whats-a-package.html
    type: official-docs
    accessed: 2026-11-22
  - id: s5
    title: "Install and Customize a Salesforce Labs Solution"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-labs-basics/install-and-customize-a-salesforce-labs-solution
    type: official-learning
    accessed: 2026-11-22
  - id: s6
    title: "Prepare Your Org and Install Developer Tools (package.xml module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/package-xml/package-xml-get-gear
    type: official-learning
    accessed: 2026-11-22
created: 2026-11-22
---

# Unmanaged Packages

An **unmanaged package** is the simplest way to bundle Salesforce metadata from one org and install it in another. Salesforce documents it inside the first-generation packaging guide and positions it for distributing open-source projects or as a one-time drop of an app that the recipient is expected to customize after installation.[^s1] Once installed, the components can be edited in the receiving org, and the developer who uploaded the package has no control over them and cannot change or upgrade them.[^s1] In other words, an unmanaged package is a copy, not a relationship: after install the metadata belongs to the subscriber.

Unmanaged packages are still common in the ecosystem. Trailhead notes that roughly one in four Salesforce Labs packages is unmanaged, so admins can edit their objects, fields, automation and Apex directly without pulling source from a repository.[^s5] Trailhead modules also use them to "drop-ship" sample metadata into a playground: the learner pastes a package ID into the install page, installs for admins only, and then finds the new custom object and tab in the org.[^s6]

## How it works

The publisher builds the package in Setup. In **Package Manager** they create a new package, then use the Components tab to add each component by type, and finally click Upload.[^s2] A successful upload sends an email containing the installation link; Salesforce warns that the link can take a few minutes to become active, so it should not be shared immediately.[^s2] Uploads can also be scripted through the **Tooling API** using the PackageUploadRequest object.[^s1]

Components join the package either **explicitly** or **implicitly**. Explicit components must be added one by one, while implicit ones ride along when a component that depends on them, usually a custom object, is added.[^s3] For example, a custom field on a standard object has to be added explicitly, but a field on a custom object in the package is included automatically with its object.[^s3] The same split applies to triggers, validation rules, page layouts and record types: explicit on standard objects, implicit on packaged custom objects.[^s3]

On install, Salesforce checks for name clashes with existing metadata. A few component types, such as reports, dashboards, documents, Classic email templates, folders, letterheads and list views, can be renamed automatically when a conflict occurs; for the rest, including Apex classes, custom objects, Lightning components, Visualforce pages, static resources and tabs, a conflict blocks the installation.[^s3]

## Limits and gotchas

- **No upgrades.** Unmanaged packages can't be upgraded and push upgrades don't apply; to move to a newer version you uninstall and reinstall, which overwrites local customizations unless you save them first.[^s5]
- **Keep the source org.** Salesforce advises installing an unmanaged package only while the org that uploaded it still exists, because installs can fail once that org is gone.[^s1]
- **Size cap.** The combined size of S-Controls and documents in the package must stay under 10 MB.[^s3]
- **Uninstall order.** If the package depends on metadata in another package, those dependencies must be removed before either package can be uninstalled; for sandboxes, remove them in production first and then create or refresh the sandbox.[^s2]
- **Not a deployment tool.** Salesforce explicitly says not to use unmanaged packages to move changes from sandbox to production.[^s1]
- **No vendor support for Labs apps.** Salesforce Labs solutions, including the unmanaged ones, are not officially supported.[^s5]

## When to use it (and when not)

Use an unmanaged package to hand someone a starting point they will own: a sample app, a template, a training dataset of metadata, or an open-source utility.[^s1][^s6] For moving work between your own environments, Salesforce points to the Salesforce Extensions for VS Code, the Ant Migration Tool, or change sets in Enterprise, Unlimited and Performance editions.[^s1]

When the same metadata must be maintained over time, an **unlocked package** is the modern alternative. Its versions are immutable artifacts installed and upgraded by version number, it records which metadata came from which package, and admins can still edit packaged metadata in production when governance allows.[^s4] Commercial apps that need upgrades and IP protection belong in managed packages instead; Trailhead summarizes the trade-off as managed packages being easily upgradeable but locked once installed.[^s5]

## Connections

Unmanaged packages are a practice within **application lifecycle management**, built with the same Package Manager tooling as **first-generation managed packages** and scriptable through the **Tooling API**.[^s1][^s2] They are an **alternative to unlocked packages**, which add versioning and upgrades, and to **change sets** and other deployment tools for org-to-org promotion.[^s1][^s4] They **contrast with push upgrades**, which cannot be applied to them.[^s5] Many are distributed through **AgentExchange** listings, where the App Details section shows whether a solution is managed or unmanaged.[^s5] The explicit-versus-implicit component model parallels how a **package.xml manifest** lists metadata for retrieval and deployment.[^s3][^s6]

## Sources

[^s1]: Salesforce Developers, "Developing and Distributing Unmanaged Packages". https://developer.salesforce.com/docs/platform/pkg1-dev/guide/packaging-developing-unmanaged.html (accessed 2026-11-22)
[^s2]: Salesforce Developers, "Create and Upload an Unmanaged Package". https://developer.salesforce.com/docs/platform/pkg1-dev/guide/packaging-uploading-unmanaged.html (accessed 2026-11-22)
[^s3]: Salesforce Developers, "Components Available in Unmanaged Packages". https://developer.salesforce.com/docs/platform/pkg1-dev/guide/packaging-unmanaged-components.html (accessed 2026-11-22)
[^s4]: Salesforce Developers, "What's an Unlocked Package?". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-unlocked-pkg-whats-a-package.html (accessed 2026-11-22)
[^s5]: Trailhead, "Install and Customize a Salesforce Labs Solution". https://trailhead.salesforce.com/content/learn/modules/salesforce-labs-basics/install-and-customize-a-salesforce-labs-solution (accessed 2026-11-22)
[^s6]: Trailhead, "Prepare Your Org and Install Developer Tools" (package.xml module). https://trailhead.salesforce.com/content/learn/modules/package-xml/package-xml-get-gear (accessed 2026-11-22)
