---
id: kt:dev-hub
type: Feature
title: Dev Hub
aliases: [Developer Hub, Dev Hub org, DevHub, Salesforce DX Dev Hub]
domain: devops-and-alm
summary: >-
  The Salesforce org feature that, once enabled, becomes the control point for Salesforce DX: it creates and tracks
  scratch orgs, owns second-generation and unlocked packages, and links registered namespaces. It cannot be disabled
  after it is turned on.
release: "Winter '27"
status: current
broader: [kt:salesforce-dx]
related: [kt:scratch-orgs, kt:source-tracking, kt:environment-strategy]
relations:
  - {predicate: enables, object: kt:scratch-orgs}
  - {predicate: enables, object: kt:unlocked-packages}
  - {predicate: enables, object: kt:second-generation-managed-packages}
  - {predicate: configuredVia, object: kt:salesforce-cli}
  - {predicate: governedBy, object: kt:scratch-org-allocations}
  - {predicate: hasPart, object: kt:namespace-registry}
sources:
  - id: s1
    title: "Select and Enable a Dev Hub Org"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-setup-enable-devhub.html
    type: official-docs
    accessed: 2026-11-01
  - id: s2
    title: "Add Salesforce DX Users"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-setup-add-users.html
    type: official-docs
    accessed: 2026-11-01
  - id: s3
    title: "Add a Limited Access User to Your Dev Hub Org"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg1-dev/guide/sfdx-pkg-add-free-license-user.html
    type: official-docs
    accessed: 2026-11-01
  - id: s4
    title: "Link a Namespace to a Dev Hub Org"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-reg-namespace.html
    type: official-docs
    accessed: 2026-11-01
  - id: s5
    title: "Assign Second-Generation Managed Packaging User Permissions"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-pkg-user-permission.html
    type: official-docs
    accessed: 2026-11-01
created: 2026-11-01
---

# Dev Hub

Dev Hub (Developer Hub) is a capability switched on in an existing Salesforce org that turns it into the administrative home for Salesforce DX work. Salesforce describes it as the place where scratch orgs, packages and namespaces are managed: every scratch org is created against a Dev Hub, and every second-generation or unlocked package version belongs to one.[^s1] It is not a separate product or a special org type; it is a setting on a production, Developer Edition or trial org.[^s1]

## How it works

**Enabling.** A System Administrator opens Setup, searches Quick Find for "Dev Hub" and clicks Enable. Dev Hub is offered in Developer, Enterprise, Performance and Unlimited editions; if the Setup page is missing, the org is probably on an unsupported edition. It cannot be enabled in a sandbox, and the switch is one-way: once on, it cannot be turned off.[^s1]

**Users and permissions.** System administrators can use the Dev Hub by default. Everyone else needs one of four licenses: Salesforce, Salesforce Platform, Developer, or the request-only Salesforce Limited Access - Free license. Salesforce advises against making developers administrators just to reach the Dev Hub; instead, give them a permission set with the needed Dev Hub object access.[^s2] The Limited Access - Free license targets people who build customizations or apps: it grants access to the Dev Hub and development tooling while restricting standard and custom objects in the production org, and is paired with the Limited Access User profile plus a custom permission set.[^s3]

The packaging guide lists the concrete grants. Developers need Read, Create and Delete on Scratch Org Info, Read and Delete on Active Scratch Org, and Read on Namespace Registry to use a linked namespace in a scratch org. The system permission **Create and Update Second-Generation Packages** is required to run `sf package create` and `sf package version create`, which work through Tooling API objects such as Package2 and Package2VersionCreateRequest.[^s5]

**Namespaces.** A namespace is registered in a separate Developer Edition org (not the Dev Hub and not a scratch org) and then linked to the Dev Hub from the Namespace Registries tab using that org's admin credentials. Only after linking can scratch orgs use the namespace. A namespace, once associated with an org, can't be changed or reused, so Salesforce recommends a throwaway namespace for experiments.[^s4]

## Limits and gotchas

- **Edition matters for capacity.** Trial and Developer Edition Dev Hubs are capped at six scratch orgs and package versions per day and three active scratch orgs at a time (verified Winter '27).[^s1]
- **Package versions are tied to the hub.** Trial orgs expire on a set date and Developer Edition orgs can expire from inactivity; when either goes, access to package versions created there goes with it.[^s1]
- **Pick a durable org for packages.** For unlocked packages that will be installed elsewhere, Salesforce recommends enabling Dev Hub in an active production org so the package has an active owner. ISV and OEM partners should make their Partner Business Org the Dev Hub.[^s1][^s5]
- **Location follows the hub.** The Dev Hub's instance decides where its scratch orgs run; Government Cloud and Hyperforce Dev Hubs create scratch orgs on Government Cloud and Hyperforce instances respectively.[^s1]
- **Ancestor gotcha.** If `sfdx-project.json` names an ancestor package version, creating a scratch org for testing also needs the Create and Update Second-Generation Packages permission, unless the `--noancestors` flag is used.[^s5]
- **Only namespaced orgs link.** Orgs without a namespace (sandboxes, scratch orgs, patch and branch orgs) can't be linked to the Namespace Registry.[^s4]

## When to use it (and when not)

Any team adopting source-driven development, scratch orgs or package-based delivery needs exactly one Dev Hub per owning entity, chosen deliberately because the decision is permanent. A Developer Edition hub is fine for learning, but its low daily cap and expiry risk make it a poor home for packages that customers or production orgs depend on.[^s1] Teams that only deploy metadata between sandboxes with change sets or the Metadata API do not need one.

## Connections

Dev Hub is a building block of `kt:salesforce-dx` and the prerequisite for `kt:scratch-orgs`, whose daily and active counts are governed by `kt:scratch-org-allocations` set by the hub's edition.[^s1] It owns `kt:unlocked-packages` and `kt:second-generation-managed-packages`, which developers create through the `kt:salesforce-cli` using the packaging permissions above.[^s5] The `kt:namespace-registry` inside the hub links namespaces for scratch-org and package use.[^s4] Choosing where the hub lives is part of an `kt:environment-strategy`, and the scratch orgs it spawns rely on `kt:source-tracking` to sync with local projects.[^s1][^s2]

## Sources

[^s1]: Salesforce Developers, "Select and Enable a Dev Hub Org". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-setup-enable-devhub.html (accessed 2026-11-01)
[^s2]: Salesforce Developers, "Add Salesforce DX Users". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-setup-add-users.html (accessed 2026-11-01)
[^s3]: Salesforce Developers, "Add a Limited Access User to Your Dev Hub Org". https://developer.salesforce.com/docs/platform/pkg1-dev/guide/sfdx-pkg-add-free-license-user.html (accessed 2026-11-01)
[^s4]: Salesforce Developers, "Link a Namespace to a Dev Hub Org". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-reg-namespace.html (accessed 2026-11-01)
[^s5]: Salesforce Developers, "Assign Second-Generation Managed Packaging User Permissions". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-pkg-user-permission.html (accessed 2026-11-01)
