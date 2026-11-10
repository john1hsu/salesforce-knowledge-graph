---
id: kt:scratch-org-allocations
type: Limit
title: Scratch Org Allocations
aliases: [scratch org limits, ActiveScratchOrgs, DailyScratchOrgs, active scratch org allocation, daily scratch org allocation, snapshot allocation]
domain: devops-and-alm
summary: >-
  The per-Dev Hub caps on how many scratch orgs can exist at once (active allocation) and how many can be created in a
  rolling 24-hour window (daily allocation), set by the Dev Hub's edition, with separate figures for partner business
  orgs and a matching cap on scratch org snapshots.
release: "Winter '27"
status: current
broader: [kt:salesforce-dx]
related: [kt:scratch-orgs, kt:dev-hub, kt:second-generation-managed-packages, kt:salesforce-cli]
relations:
  - {predicate: contrastsWith, object: kt:data-and-file-storage-allocations}
  - {predicate: contrastsWith, object: kt:api-request-limits}
sources:
  - id: s1
    title: "Supported Scratch Org Editions and Allocations"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-scratch-orgs-editions-and-allocations.html
    type: official-docs
    accessed: 2026-11-10
  - id: s2
    title: "Scratch Org Allocations for Salesforce Partners"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg1-dev/guide/isv-partner-scratch-org-allocations.html
    type: official-docs
    accessed: 2026-11-10
  - id: s3
    title: "Manage Scratch Orgs from the Dev Hub Org"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg1-dev/guide/sfdx-dev-scratch-orgs-view-lex.html
    type: official-docs
    accessed: 2026-11-10
  - id: s4
    title: "Scratch Org Snapshots"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-snapshots-intro.html
    type: official-docs
    accessed: 2026-11-10
created: 2026-11-10
---

# Scratch Org Allocations

Scratch org allocations are the quotas a Dev Hub org enforces on scratch org usage. They are not set per developer or per project: the edition of the Dev Hub decides how many scratch orgs the whole team that shares that hub can use.[^s1] Two separate counters apply, and a creation request must fit within both. The **active** allocation is the most scratch orgs that can exist at one time, and the **daily** allocation is the most successful creations that can be started in a rolling 24-hour window.[^s1]

## How it works

The active count goes down whenever a scratch org expires or is deleted, which frees a slot for a new one.[^s1] The daily count is different: it looks back over the preceding 24 hours of successful creations, so it is a sliding window rather than a counter that resets at midnight.[^s1] Deleting an org therefore helps with the active limit but not with the daily one, because the creation has already been counted.

Inside the Dev Hub, two objects show where the quota is going. `ActiveScratchOrg` records track orgs currently in use, while `ScratchOrgInfo` records track the creation requests and keep history, marking each as active, expired or deleted.[^s3] Admins, or users with Salesforce DX permissions, can open the Active Scratch Orgs and Scratch Org Infos list views from the App Launcher and delete rows there. Salesforce states that deleting an active scratch org frees it so it no longer counts against allocations, and that deleting a `ScratchOrgInfo` request also deletes the org it created.[^s3] Expired orgs and their `ActiveScratchOrg` records are removed from the Dev Hub automatically.[^s2]

To see remaining capacity, run `sf limits api display --target-org` against the Dev Hub and read the `ActiveScratchOrgs` and `DailyScratchOrgs` rows, which show both remaining and maximum values.[^s1] Running the same command against a scratch org instead shows that scratch org's own limits.[^s1]

## Allocation figures (verified Winter '27)

Standard Dev Hub editions receive these allocations:[^s1]

| Dev Hub edition | Active | Daily |
|---|---|---|
| Developer Edition or trial | 3 | 6 |
| Enterprise Edition | 40 | 80 |
| Unlimited Edition | 100 | 200 |
| Performance Edition | 100 | 200 [^s1] |

Partners whose Dev Hub is a partner business org (PBO) get different figures. An active PBO allows 150 active and 300 daily scratch orgs, and a trial PBO allows 20 active and 40 daily. In a PBO the daily package version creation limit equals the daily scratch org allocation, and versions created while skipping validation are capped at 500 per day.[^s2] Only a PBO Dev Hub can create the Partner Developer, Partner Enterprise, Partner Group and Partner Professional scratch org editions.[^s1]

Snapshots have a quota of their own. The number of snapshots a Dev Hub can create matches its active scratch org allocation, so a Developer Edition hub gets 3 and an Unlimited hub gets 100, and the CLI reports the daily snapshot counter as `DailyOrgSnapshots`.[^s4] A snapshot expires after 90 days, and its slot is released at once when it expires or is deleted.[^s4]

## Limits and gotchas

- **Shared pool**: every developer and CI pipeline using one Dev Hub draws from the same counters, so a busy pipeline can starve developers.[^s1]
- **Daily limit outlasts deletion**: freeing an active slot does not refund the daily count, which only clears as creations age out of the 24-hour window.[^s1]
- **Trial and Developer Edition hubs are tiny**: 3 active and 6 daily is enough for learning, not for a team or CI; Enterprise or above is the practical floor.[^s1]
- **Storage is separate**: each scratch org has 500 MB of data storage and 50 MB of file storage, independent of how many orgs the hub may create.[^s1]
- **Free Limited Access users**: developers given Dev Hub access through that license may be unable to run the limits command themselves and need an admin to check.[^s1]

## When to use it (and when not)

Plan around these figures when choosing which org hosts the Dev Hub and when designing CI. Short `--duration-days` values, deleting orgs as soon as a job finishes, and reusing a snapshot instead of rebuilding orgs from scratch all stretch the active pool, but none of them raise the daily ceiling.[^s1][^s4] If a pipeline regularly needs more than the daily figure, the answer is a higher Dev Hub edition, or a PBO for ISVs, not more aggressive cleanup.[^s1][^s2]

## Connections

Scratch Org Allocations is a limit within `kt:salesforce-dx`, its **broader** node. It governs `kt:scratch-orgs` and is set by the edition of the `kt:dev-hub` that creates them.[^s1] In a partner business org it also caps daily package version creation for `kt:second-generation-managed-packages`.[^s2] Capacity is checked through the `kt:salesforce-cli` limits command.[^s1] It **contrasts with** `kt:data-and-file-storage-allocations`, which caps storage inside an org rather than the number of orgs, and with `kt:api-request-limits`, the per-org cap on API calls, which is unrelated to how many orgs a Dev Hub may spawn.[^s1]

## Sources

[^s1]: Salesforce Developers, "Supported Scratch Org Editions and Allocations". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-scratch-orgs-editions-and-allocations.html (accessed 2026-11-10)
[^s2]: Salesforce Developers, "Scratch Org Allocations for Salesforce Partners". https://developer.salesforce.com/docs/platform/pkg1-dev/guide/isv-partner-scratch-org-allocations.html (accessed 2026-11-10)
[^s3]: Salesforce Developers, "Manage Scratch Orgs from the Dev Hub Org". https://developer.salesforce.com/docs/platform/pkg1-dev/guide/sfdx-dev-scratch-orgs-view-lex.html (accessed 2026-11-10)
[^s4]: Salesforce Developers, "Scratch Org Snapshots". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-snapshots-intro.html (accessed 2026-11-10)
