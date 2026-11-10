---
id: kt:namespace-registry
type: Feature
title: Namespace Registry
aliases: [Namespace Registries, linked namespaces, Dev Hub namespace registry, Link Namespace]
domain: devops-and-alm
summary: >-
  The Dev Hub app (Namespace Registries) where a namespace created in a separate Developer Edition org is linked to
  the Dev Hub, so that namespaced scratch orgs, unlocked packages and second-generation managed packages can use it.
release: "Winter '27"
status: current
broader: [kt:salesforce-dx]
related: [kt:scratch-orgs, kt:first-generation-managed-packages, kt:package-dependencies]
relations:
  - {predicate: partOf, object: kt:dev-hub}
  - {predicate: enables, object: kt:second-generation-managed-packages}
  - {predicate: consumedBy, object: kt:unlocked-packages}
sources:
  - id: s1
    title: "Link a Namespace to a Dev Hub Org"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-reg-namespace.html
    type: official-docs
    accessed: 2026-11-08
  - id: s2
    title: "Create and Register Your Namespace for Second-Generation Managed Packages"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-create-namespace.html
    type: official-docs
    accessed: 2026-11-08
  - id: s3
    title: "Namespaces for Second-Generation Managed Packages"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-plan-namespaces.html
    type: official-docs
    accessed: 2026-11-08
  - id: s4
    title: "Understanding Namespaces (Unlocked Packages)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_pkg_plan_namespaces.htm
    type: official-docs
    accessed: 2026-11-08
  - id: s5
    title: "How Scratch Orgs Fit in the Package Development Workflow"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/dev2gp-so-how-fit-pkg-dev.html
    type: official-docs
    accessed: 2026-11-08
  - id: s6
    title: "Avoid Namespace Collisions in Second-Generation Managed Packages"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-namespace-collisions.html
    type: official-docs
    accessed: 2026-11-08
created: 2026-11-08
---

# Namespace Registry

The Namespace Registry is the part of a Dev Hub org where packaging teams link namespaces they own, so that Salesforce DX tooling can use them. A namespace is not created in the Dev Hub itself: it is registered in a separate Developer Edition org and then linked through the **Namespace Registries** app, after which the Dev Hub can create namespaced scratch orgs and namespaced packages.[^s1][^s2] Sandboxes, scratch orgs, patch orgs and branch orgs used for namespaced package work all depend on the namespace being linked to the registry.[^s1]

## What a namespace is

A namespace is an alphanumeric identifier of 1 to 15 characters that keeps a package's contents distinct from every other package in a subscriber org. Each component in the package has the namespace prepended to its API name, so a custom object `Insurance_Agent__c` in the Acme namespace becomes `Acme__Insurance_Agent__c`.[^s3] Second-generation managed packages always carry a namespace; unlocked packages may be created with or without one.[^s3][^s4]

## How it works

Linking is a three-org workflow:[^s1][^s2]

1. **Create the namespace** in a new Developer Edition org that is separate from both the Dev Hub and any scratch org: in Setup open Package Manager, edit Namespace Settings, check availability, and save (optionally without associating a package).[^s2]
2. **Link it** by logging in to the Dev Hub as a System Administrator, or as a user with the Salesforce DX Namespace Registry permissions, opening **Namespace Registries** from the App Launcher, clicking **Link Namespace**, and authenticating to the Developer Edition org in the pop-up. Pop-ups from the Dev Hub must be allowed. The **All Namespace Registries** list view then shows every linked namespace.[^s1]
3. **Use it** by setting the `namespace` attribute in `sfdx-project.json`; new packages created from that project are associated with the namespace.[^s2]

When a scratch org is created from that project, the namespace (and any ancestry settings) is copied into the org, so metadata created in or deployed to it is prefixed with the package namespace. Salesforce prefers such namespaced scratch orgs for development. For testing an installed package, the CLI's `--no-namespace` flag creates a scratch org without the namespace.[^s5]

## Limits and gotchas

- **Permanent choices.** Once a namespace is associated with an org it cannot be changed or reused, so Salesforce advises using a throwaway namespace for trials and experiments.[^s1] A package's namespace is likewise fixed at package creation and cannot be changed afterwards.[^s3]
- **One namespace per package.** Many packages can share one namespace, but a single package can belong to only one; teams working across several namespaces should keep one Salesforce DX project per namespace.[^s3][^s4]
- **Naming.** Pick an informative name and never name a namespace after a person.[^s3]
- **Collision rules.** Packages that share a namespace must not contain components with the same API name. Two first-generation packages, or a 1GP and a 2GP, cannot be installed together if they use the same namespace, whereas multiple 2GP packages, or a 2GP and a namespaced unlocked package, can share one.[^s6]
- **Install targets.** A no-namespace unlocked package cannot be installed into a namespaced org, and 2GP packages fail to install into 1GP packaging and patch orgs.[^s6]

## When to use it (and when not)

Any ISV building managed 2GP packages must register and link a namespace; Salesforce recommends one shared namespace for all of a publisher's 2GP packages because code sharing is simpler, while a product that may be sold or spun off can be isolated on its own namespace, which transfers with the package.[^s2][^s3] Enterprise teams using unlocked packages can skip namespaces when they want to keep existing API names of migrated metadata, and adopt one when they want packaged metadata to be distinguishable or need to avoid API-name collisions between teams. Within a shared namespace, public Apex is visible to sibling packages only when annotated `@namespaceAccessible`, while `global` Apex is visible across namespaces.[^s4]

## Connections

The registry is a component of the `kt:dev-hub` (`partOf`), the control org of `kt:salesforce-dx`. It `enables` `kt:second-generation-managed-packages`, which cannot exist without a linked namespace, and is optionally `usedBy` `kt:unlocked-packages`.[^s2][^s4] Linked namespaces shape `kt:scratch-orgs`, which inherit the project namespace at creation.[^s5] It is related to `kt:first-generation-managed-packages`, whose namespace lives in the packaging org and whose collision rules with 2GP differ, and to `kt:package-dependencies`, since dependent packages in one namespace share code through `@namespaceAccessible`.[^s4][^s6]

## Sources
[^s1]: Salesforce Developers, "Link a Namespace to a Dev Hub Org". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-reg-namespace.html (accessed 2026-11-08)
[^s2]: Salesforce Developers, "Create and Register Your Namespace for Second-Generation Managed Packages". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-create-namespace.html (accessed 2026-11-08)
[^s3]: Salesforce Developers, "Namespaces for Second-Generation Managed Packages". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-plan-namespaces.html (accessed 2026-11-08)
[^s4]: Salesforce Developers, "Understanding Namespaces (Unlocked Packages)". https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_pkg_plan_namespaces.htm (accessed 2026-11-08)
[^s5]: Salesforce Developers, "How Scratch Orgs Fit in the Package Development Workflow". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/dev2gp-so-how-fit-pkg-dev.html (accessed 2026-11-08)
[^s6]: Salesforce Developers, "Avoid Namespace Collisions in Second-Generation Managed Packages". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/sfdx-dev-dev2gp-namespace-collisions.html (accessed 2026-11-08)
