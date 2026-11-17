---
id: kt:org-shape
type: Feature
title: Org Shape for Scratch Orgs
aliases: [org shape, scratch org shape, sourceOrg, Enable Org Shape for Scratch Orgs, sf org create shape]
domain: devops-and-alm
summary: >-
  A Salesforce DX feature that captures a production-type source org's edition, features, limits, package
  licenses and Boolean Metadata API settings as an internal shape in the Dev Hub, so scratch orgs can be created
  to mirror that org by naming it as sourceOrg instead of hand-writing every feature and setting.
release: "Winter '27"
status: current
broader: [kt:scratch-orgs, kt:salesforce-dx]
related: [kt:sandbox-types, kt:first-generation-managed-packages]
relations:
  - {predicate: dependsOn, object: kt:dev-hub}
  - {predicate: configuredVia, object: kt:salesforce-cli}
  - {predicate: enables, object: kt:unlocked-packages}
  - {predicate: integratesWith, object: kt:devops-center}
sources:
  - id: s1
    title: "Create a Scratch Org Based on an Org Shape (Salesforce DX Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_shape_intro.htm
    type: official-docs
    accessed: 2026-11-17
  - id: s2
    title: "Create and Manage Org Shapes (Salesforce DX Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-shape-create-shape.html
    type: official-docs
    accessed: 2026-11-17
  - id: s3
    title: "Enable Org Shape for Scratch Orgs (Salesforce DX Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_shape_enable_org_shape.htm
    type: official-docs
    accessed: 2026-11-17
  - id: s4
    title: "Org Shape Permissions (Salesforce DX Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_shape_permissions.htm
    type: official-docs
    accessed: 2026-11-17
  - id: s5
    title: "Scratch Org Definition for Org Shape (Salesforce DX Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-shape-scratch-def.html
    type: official-docs
    accessed: 2026-11-17
  - id: s6
    title: "Scratch Org Definition Files vs Org Shape in Package Development (Second-Generation Packaging Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/dev2gp-so-orgshape-vs-def-file.html
    type: official-docs
    accessed: 2026-11-17
created: 2026-11-17
---

# Org Shape for Scratch Orgs

**Org Shape for Scratch Orgs** lets a team build scratch orgs that look like an existing org without writing the scratch org definition by hand. The Dev Hub records a "shape" of a source org, an internal system file that nobody can open or view, and a scratch org created from it inherits that org's edition and baseline configuration.[^s1] The shape copies the source org's setup but none of its extra data or metadata, so the resulting scratch org is still a clean, source-driven environment.[^s2]

## What a shape captures

According to the Salesforce DX Developer Guide, a shape holds the source org's features, edition, limits, the licenses associated with its installed packages (but not the packages themselves), and Metadata API settings that have Boolean fields.[^s1] It leaves out settings with integer or string fields, metadata types, data and some features; any of these can be added manually to the definition file.[^s1] The management page gives Lightning Experience Themes and AddressSettings entries as examples of what is not carried over.[^s2] To actually use a package's functionality you still install the package in the scratch org.[^s1]

## How it works

Setup has two sides. In the Dev Hub, open **Scratch Orgs** in Setup, switch on **Enable Org Shape for Scratch Orgs** and enter the Dev Hub's org ID. If the source org is a different org, repeat the toggle there and enter the Dev Hub's ID. Org IDs must be the 15-character form, and a source org can list up to 50 Dev Hub org IDs.[^s3] Shapes are supported for Developer, Group, Professional, Unlimited and Enterprise edition source orgs; sandboxes and scratch orgs cannot be the source.[^s3][^s1]

A Dev Hub admin grants the **Shape Representation** object's Create and Edit permission to people who create shapes, and Delete to people who remove them; building a scratch org from an existing shape needs only the usual scratch org permissions. These can be added to an existing Salesforce DX permission set, and org shape users must hold the Salesforce user license.[^s4]

After authorizing both the Dev Hub and the source org with the Salesforce CLI, a developer runs `sf org create shape` against the source org. The command starts an asynchronous job, and the shape moves from `InProgress` to `Active` when it is ready to use.[^s2] The definition file then replaces `edition` with `sourceOrg`, set to the source org's 15-character ID, and can add further `features` and `settings` on top of what the shape provides.[^s5]

## Limits and gotchas

- **One active shape.** Only one shape can be active at a time; creating a shape again for the same org replaces it.[^s2]
- **Shapes go stale.** A shape is tied to a Salesforce release, so recreate it after the source org upgrades or its features, settings or licenses change.[^s1][^s2]
- **Release transitions.** When the Dev Hub and source org are on different releases, add `release`: `previous` (shape on Current, Dev Hub on Preview) or `preview` (the reverse).[^s5]
- **DevOps Center.** A shape with DevOps Center enabled still needs the `DevOpsCenter` feature and the `enableDevOpsCenterGA` Dev Hub setting in the definition.[^s5]
- **Deleting is shared.** Removing a shape someone else created does not need Modify All Records, because the org has only one active shape.[^s4]

## When to use it (and when not)

Salesforce's packaging guide recommends an explicit, hand-written scratch org definition file for managed packages distributed on AgentExchange, where dependencies should be stated outright. Org shape suits unlocked packages and teams moving from first- to second-generation packaging: shaping the old 1GP packaging org helps ensure the features the package metadata relies on are captured, and the same `sourceOrg` value can be used when creating package versions.[^s6] For an environment that needs production data or full metadata, rather than just production's configuration baseline, a sandbox is still the tool.[^s1][^s2]

## Connections

Org shape is a capability of **scratch orgs** and part of the **Salesforce DX** toolset, and it depends on the **Dev Hub**, where the feature is enabled and the shape is stored.[^s3][^s4] Shapes are created and managed through the **Salesforce CLI**.[^s2] It enables **unlocked package** development and eases migration from **first-generation managed packages**.[^s6] It integrates with **DevOps Center** through the extra feature and setting a shaped scratch org needs.[^s5] Because sandboxes cannot be used as a source, it complements rather than replaces **sandbox types**.[^s1]

## Sources

[^s1]: Salesforce Developers, "Create a Scratch Org Based on an Org Shape". https://developer.salesforce.com/docs/atlas.en-us.264.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_shape_intro.htm (accessed 2026-11-17)
[^s2]: Salesforce Developers, "Create and Manage Org Shapes". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-shape-create-shape.html (accessed 2026-11-17)
[^s3]: Salesforce Developers, "Enable Org Shape for Scratch Orgs". https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_shape_enable_org_shape.htm (accessed 2026-11-17)
[^s4]: Salesforce Developers, "Org Shape Permissions". https://developer.salesforce.com/docs/atlas.en-us.264.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_shape_permissions.htm (accessed 2026-11-17)
[^s5]: Salesforce Developers, "Scratch Org Definition for Org Shape". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-shape-scratch-def.html (accessed 2026-11-17)
[^s6]: Salesforce Developers, "Scratch Org Definition Files vs Org Shape in Package Development". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/dev2gp-so-orgshape-vs-def-file.html (accessed 2026-11-17)
