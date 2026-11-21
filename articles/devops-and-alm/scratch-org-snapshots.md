---
id: kt:scratch-org-snapshots
type: Feature
title: Scratch Org Snapshots
aliases: [scratch org snapshot, org snapshots, sf org create snapshot, OrgSnapshot]
domain: devops-and-alm
summary: >-
  A Dev Hub feature that captures a point-in-time copy of a configured scratch org (packages, features, licences,
  metadata and data) so that new scratch orgs, and package version builds, can start from it instead of being rebuilt
  from scratch each time.
release: "Winter '27"
status: current
broader: [kt:scratch-orgs, kt:salesforce-dx]
related: [kt:org-shape, kt:continuous-integration-for-salesforce, kt:salesforce-cli, kt:sandbox-types]
relations:
  - {predicate: dependsOn, object: kt:dev-hub}
  - {predicate: governedBy, object: kt:scratch-org-allocations}
  - {predicate: consumedBy, object: kt:second-generation-managed-packages}
  - {predicate: consumedBy, object: kt:unlocked-packages}
  - {predicate: alternativeTo, object: kt:org-shape}
sources:
  - id: s1
    title: "Scratch Org Snapshots"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-snapshots-intro.html
    type: official-docs
    accessed: 2026-11-21
  - id: s2
    title: "Create a Scratch Org Snapshot"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-snapshots-create.html
    type: official-docs
    accessed: 2026-11-21
  - id: s3
    title: "Create a Scratch Org Based on a Snapshot"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-snapshots-create-scratch-org.html
    type: official-docs
    accessed: 2026-11-21
  - id: s4
    title: "org create snapshot (Salesforce CLI Command Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_org_create_snapshot.html
    type: official-docs
    accessed: 2026-11-21
  - id: s5
    title: "Enable Scratch Org Snapshots in the Dev Hub Org"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_snapshots_enable_snapshots_devhub.htm
    type: official-docs
    accessed: 2026-11-21
  - id: s6
    title: "When to Use Scratch Org Snapshots in Package Development"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.pkg2_dev.meta/pkg2_dev/dev2gp_so_when_use_snapshot.htm
    type: official-docs
    accessed: 2026-11-21
created: 2026-11-21
---

# Scratch Org Snapshots

A scratch org snapshot is a point-in-time copy of a scratch org, held by the Dev Hub, that captures the org's installed packages, features, limits, licences, metadata and data.[^s1] New scratch orgs can then be created from the snapshot, so a team that needs the same heavy baseline (several dependency packages, sample data, specific settings) configures it once rather than repeating the installs on every org creation.[^s1][^s3] Snapshots are static: to change one, you delete it and capture a new one.[^s1]

## How it works

An admin first turns the feature on in the Dev Hub: in Setup, open **Scratch Orgs** and select **Enable Scratch Org Snapshots**. The setting is listed for Developer, Enterprise, Group, Professional and Unlimited Edition Dev Hubs and is not available in scratch orgs or sandboxes.[^s5] Users who are not admins also need scratch org and snapshot permissions.[^s2]

A snapshot is captured from a running scratch org with `sf org create snapshot`, which needs a `--name`, the `--source-org` to copy and a `--target-dev-hub` (unless that config variable is set).[^s4] The CLI reference recommends putting a reference point such as a version-control tag or commit ID in `--description`, so a team can tell which build a snapshot came from.[^s4] Names are limited to 15 alphanumeric characters, with no spaces or special characters.[^s2] The request starts in an `InProgress` state; `org get snapshot`, `org list snapshot` and `org delete snapshot` complete the command set.[^s2][^s4]

To use it, reference the snapshot by name in a scratch org definition file (`"snapshot": "<name>"` in place of `edition`) or pass `--snapshot` to `sf org create scratch`.[^s3] The definition file must not also set `edition`, `features`, `hasSampleData`, `release` or `sourceOrg`, though a `settings` block can still override settings the snapshot does not carry.[^s3] Changing or deleting a scratch org created this way has no effect on the snapshot itself.[^s3]

## Limits and lifecycle (verified Winter '27)

- **Allocation.** Active and daily snapshot allocations follow the Dev Hub edition: 3 for Developer, 40 for Enterprise, and 100 for Unlimited and Performance. Check them with `sf org list limits` (`ActiveOrgSnapshots`, `DailyOrgSnapshots`).[^s1]
- **Storage.** A snapshot has the same 200 MB data storage limit as a scratch org.[^s1]
- **Expiry.** Snapshots expire 90 days after creation, releasing the allocation immediately; data is kept for 100 days, so an expired snapshot's data is deleted 10 days after expiry.[^s1]
- **Not copied.** Connected apps, external credentials and named credentials are not captured, so integrations must be configured again in each new org.[^s1]

## Gotchas

You can snapshot only a scratch org that was not itself created from a snapshot and has no namespace.[^s2] Finish configuring the source org before running the command, because later changes may not all be captured, and keep the source lean, since capture time grows with org size.[^s2] Snapshots belong to one Dev Hub, and scratch orgs must be created from that same hub.[^s1] Allow a longer `--wait` when creating orgs from a snapshot, because creation can take longer.[^s3] During a Salesforce preview window, the new org follows the snapshot's release rather than the Dev Hub's: a snapshot captured on the preview release yields preview orgs even from a non-preview hub.[^s3]

## When to use it

Snapshots suit CI pipelines and developer onboarding where every org needs the same stable dependencies installed. Salesforce is explicit that they do not replace source-driven development, version control or user acceptance testing in sandboxes.[^s1] For packaging, a snapshot can speed up `package version create` when a second-generation or unlocked package depends on large, stable packages whose install time dominates the build.[^s6] The catch is that managed package versions built from a snapshot cannot be promoted to Released, so a release candidate must be rebuilt without one; unlocked package versions built this way can be promoted.[^s6]

## Connections

Snapshots are a capability **within** `kt:scratch-orgs` and the wider `kt:salesforce-dx` toolchain, and they **depend on** the `kt:dev-hub`, which stores them and must create every org based on them.[^s1][^s5] Their counts are **governed by** `kt:scratch-org-allocations`, which shares the same edition-based figures.[^s1] They are **consumed by** `kt:second-generation-managed-packages` and `kt:unlocked-packages` builds to skip dependency installs.[^s6] They are an **alternative to** `kt:org-shape`, the other way to give scratch orgs a predefined shape; the two cannot be combined, since a snapshot-based definition file may not set `sourceOrg`.[^s3] They are related to `kt:continuous-integration-for-salesforce`, `kt:salesforce-cli` (the `org` snapshot commands) and `kt:sandbox-types`, which remain the place for user acceptance testing.[^s1][^s4]

## Sources

[^s1]: Salesforce Developers, "Scratch Org Snapshots". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-snapshots-intro.html (accessed 2026-11-21)
[^s2]: Salesforce Developers, "Create a Scratch Org Snapshot". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-snapshots-create.html (accessed 2026-11-21)
[^s3]: Salesforce Developers, "Create a Scratch Org Based on a Snapshot". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-snapshots-create-scratch-org.html (accessed 2026-11-21)
[^s4]: Salesforce Developers, "org create snapshot". https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_org_create_snapshot.html (accessed 2026-11-21)
[^s5]: Salesforce Developers, "Enable Scratch Org Snapshots in the Dev Hub Org". https://developer.salesforce.com/docs/atlas.en-us.264.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_snapshots_enable_snapshots_devhub.htm (accessed 2026-11-21)
[^s6]: Salesforce Developers, "When to Use Scratch Org Snapshots in Package Development". https://developer.salesforce.com/docs/atlas.en-us.264.0.pkg2_dev.meta/pkg2_dev/dev2gp_so_when_use_snapshot.htm (accessed 2026-11-21)
