---
id: kt:scratch-orgs
type: Feature
title: Scratch Orgs
aliases: [scratch org, Salesforce DX scratch org, scratch-def.json, scratch org definition file]
domain: devops-and-alm
summary: >-
  Short-lived, source-driven Salesforce orgs created from a Dev Hub and shaped by a JSON definition file, used for
  feature development, automated testing and CI in Salesforce DX; they live 1 to 30 days (default 7).
release: "Winter '27"
status: current
broader: [kt:salesforce-dx, kt:application-lifecycle-management]
related: [kt:environment-strategy, kt:devops-center, kt:source-tracking]
relations:
  - {predicate: dependsOn, object: kt:dev-hub}
  - {predicate: configuredVia, object: kt:salesforce-cli}
  - {predicate: alternativeTo, object: kt:sandbox-types}
  - {predicate: governedBy, object: kt:scratch-org-allocations}
  - {predicate: enables, object: kt:unlocked-packages}
sources:
  - id: s1
    title: "Scratch Orgs (Salesforce DX Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-scratch-orgs.html
    type: official-docs
    accessed: 2026-11-01
  - id: s2
    title: "Supported Scratch Org Editions and Allocations"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-scratch-orgs-editions-and-allocations.html
    type: official-docs
    accessed: 2026-11-01
  - id: s3
    title: "Build Your Own Scratch Org Definition File"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-scratch-orgs-def-file.html
    type: official-docs
    accessed: 2026-11-01
  - id: s4
    title: "Create Scratch Orgs (Salesforce DX Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs_create.htm
    type: official-docs
    accessed: 2026-11-01
  - id: s5
    title: "Set Up Salesforce DX Tools (App Development with Salesforce DX)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/modules/sfdx_app_dev/units/sfdx_app_dev_setup_dx
    type: official-learning
    accessed: 2026-11-01
created: 2026-11-01
---

# Scratch Orgs

A scratch org is a temporary Salesforce environment built from source rather than copied from production. Salesforce describes it as a source-driven, disposable deployment of code and metadata that can be configured to mimic different editions, features and settings.[^s1] Scratch orgs are the default development environment of Salesforce DX: the source of truth lives in version control, and an org is spun up, populated from that source, used, and thrown away.[^s5]

## How it works

Every scratch org is created from, and tracked by, a **Dev Hub** org. Dev Hub can be enabled in Developer, Enterprise, Unlimited or Performance editions, and the Dev Hub's edition sets how many scratch orgs the team may create; expired orgs are deleted from the Dev Hub along with their ActiveScratchOrgs records.[^s1] Trailhead recommends enabling Dev Hub in a Developer Edition org or Trailhead Playground for learning, though any paid org can serve.[^s5]

A new scratch org is empty: no custom objects, Apex classes, sample data, profiles or permission sets, and a single admin user.[^s1] Its shape comes from a **scratch org definition file**, a JSON blueprint that teams commit to version control so everyone builds the same kind of org. The only required key is `edition` (Developer, Enterprise, Group, Professional, or a Partner variant available only from a partner business org Dev Hub). Optional keys include `features` for add-on functionality, `settings` (any Metadata API setting), `orgName`, `hasSampleData`, `objectSettings`, and `release`, which can select `preview` or `previous` only during release transitions.[^s3][^s2] Two further keys build orgs from existing state: `snapshot` names a snapshot captured from another scratch org, and `sourceOrg` takes a 15-character org ID for Org Shape.[^s3] Snapshots can preserve packages, features, licenses, metadata and data so replicas start pre-configured.[^s1]

Creation runs through the Salesforce CLI with `sf org create scratch`, passing `--definition-file`, an `--alias`, `--set-default` and optionally `--target-dev-hub`. `--duration-days` sets expiry between 1 and 30 days with a default of 7; `--async` returns immediately and `sf org resume scratch` picks the job up later; `--no-namespace` drops the namespace for UAT or package-install testing.[^s4] Source tracking is on by default; `--no-track-source` turns it off locally, which can speed CI, demos and data loads.[^s1]

## Limits and gotchas

- **Allocations** (verified Winter '27): a Developer Edition or trial Dev Hub allows 3 active and 6 daily scratch orgs; Enterprise allows 40 active and 80 daily; Unlimited and Performance allow 100 active and 200 daily. The daily count is a rolling 24-hour window of successful creations, and partners may have different allocations.[^s2]
- **Storage**: each scratch org gets 500 MB of data storage and 50 MB of file storage.[^s2]
- **Expiry is final**: an expired scratch org cannot be restored, so anything not in source control is lost. Deleting an org frees an active slot, but each new creation still counts against the daily allocation.[^s1][^s2]
- **Feature plus setting**: some capabilities need both a `features` entry and a matching `settings` block (Experience Cloud needs the Communities feature and `communitiesSettings`), and some packages install only after `objectSettings` defines sharing models and record types.[^s3]
- **Location**: scratch orgs run on sandbox instances chosen from the Dev Hub's country; Government Cloud and Hyperforce Dev Hubs create them in their own region.[^s1]
- **No personal data**: use synthetic or dummy data only.[^s1]

## When to use it (and when not)

Use scratch orgs for feature branches, package development, automated tests and CI jobs where a clean, reproducible org per task matters more than realistic data volume.[^s1] They do not replace sandboxes: Trailhead notes sandboxes are still needed for user-acceptance testing, continuous delivery and staging, where a copy of production metadata and data is the point.[^s5]

## Connections

Scratch orgs are a core part of `kt:salesforce-dx` and of source-driven `kt:application-lifecycle-management`, and they depend on `kt:dev-hub` for creation and limits.[^s1] They are configured and driven through the `kt:salesforce-cli` and rely on `kt:source-tracking` to sync changes with a local project.[^s4][^s1] They are the usual build environment for `kt:unlocked-packages` and other package development, where the focus shifts from org development to package development.[^s5] In an `kt:environment-strategy` they sit alongside, not instead of, the `kt:sandbox-types` used for UAT and staging, and a pipeline tool such as `kt:devops-center` can promote their work items onward.[^s5] Their capacity is governed by `kt:scratch-org-allocations`, set by the Dev Hub edition.[^s2]

## Sources

[^s1]: Salesforce Developers, "Scratch Orgs". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-scratch-orgs.html (accessed 2026-11-01)
[^s2]: Salesforce Developers, "Supported Scratch Org Editions and Allocations". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-scratch-orgs-editions-and-allocations.html (accessed 2026-11-01)
[^s3]: Salesforce Developers, "Build Your Own Scratch Org Definition File". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-scratch-orgs-def-file.html (accessed 2026-11-01)
[^s4]: Salesforce Developers, "Create Scratch Orgs". https://developer.salesforce.com/docs/atlas.en-us.264.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs_create.htm (accessed 2026-11-01)
[^s5]: Trailhead, "Set Up Salesforce DX Tools". https://trailhead.salesforce.com/modules/sfdx_app_dev/units/sfdx_app_dev_setup_dx (accessed 2026-11-01)
