---
id: kt:source-tracking
type: Feature
title: Source Tracking
aliases: [Salesforce DX source tracking, sandbox source tracking, SourceMember tracking, Enable Source Tracking in Developer and Developer Pro Sandboxes]
domain: devops-and-alm
summary: >-
  Salesforce DX capability that records metadata changes made in a local project and in a scratch org or
  Developer/Developer Pro sandbox, so Salesforce CLI can preview, deploy or retrieve only what changed and flag conflicts.
release: "Winter '27"
status: current
broader: [kt:salesforce-dx, kt:application-lifecycle-management]
related: [kt:scratch-orgs, kt:devops-center, kt:sandbox-types, kt:change-sets]
relations:
  - {predicate: configuredVia, object: kt:salesforce-cli}
  - {predicate: dependsOn, object: kt:metadata-api}
  - {predicate: queriedWith, object: kt:tooling-api}
  - {predicate: configuredVia, object: kt:dev-hub}
sources:
  - id: s1
    title: "Track Changes Between Your Project and Org (Salesforce DX Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-source-tracking.html
    type: official-docs
    accessed: 2026-11-01
  - id: s2
    title: "Enable Source Tracking in Sandboxes (Salesforce DX Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-setup-enable-source-tracking-sandboxes.html
    type: official-docs
    accessed: 2026-11-01
  - id: s3
    title: "Deploy and Retrieve Changes Identified by Source Tracking"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-source-tracking-pull-push-changes.html
    type: official-docs
    accessed: 2026-11-01
  - id: s4
    title: "Resolve Conflicts Between Your Local Project and Org"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_source_tracking_resolve_conflicts.htm
    type: official-docs
    accessed: 2026-11-01
  - id: s5
    title: "project reset tracking (Salesforce CLI Command Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_project_reset_tracking.html
    type: official-docs
    accessed: 2026-11-01
  - id: s6
    title: "Learn MOAR with Summer '20 Release Highlights for Developers"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2020/06/learn-moar-with-summer-20-release-highlights-for-developers
    type: official-blog
    accessed: 2026-11-01
created: 2026-11-01
---

# Source Tracking

Source tracking is the Salesforce DX mechanism that keeps a record of what has changed between a local project and a target org, a scratch org or a sandbox, whenever source is created, updated or deleted on either side.[^s1] With it, a developer no longer has to remember which components were touched: Salesforce CLI can list remote changes made by teammates in a shared sandbox, deploy or retrieve only the changed components, and warn about conflicts before anything is overwritten.[^s1] The tracking itself has no direct effect on the org; it changes only how the local tooling behaves.[^s1]

## How it works

When tracking is enabled for an org, tracking operations run as part of commands such as `sf project deploy start`. After a deployment the CLI waits for the org's **SourceMember** Tooling API object to update, and it reads that object to know what changed server-side.[^s1] The typical loop is: preview remote and local changes, resolve conflicts, retrieve remote changes into the project, commit them to version control (the historical source of truth), deploy local changes to validate and test, and repeat.[^s3]

The core commands are `sf project retrieve preview` and `sf project deploy preview` to see pending changes, and `sf project retrieve start` / `sf project deploy start`, which with no flags move all changed source.[^s3] Preview output lists each component's type, API name and local path; a blank path means the component exists only in the org.[^s3] Files matched by `.forceignore` are reported separately as ignored and are never moved; Profiles appear as ignored in the documented examples.[^s3]

Scratch orgs track source natively. Sandboxes must opt in, and tracking was first offered for Developer and Developer Pro sandboxes as a beta in Summer '20.[^s6]

## Enabling it in sandboxes

Today source tracking is supported only in **Developer** and **Developer Pro** sandboxes, not in Partial Copy or Full sandboxes or Developer Edition orgs.[^s2] There are two switches:

- **Org-wide**: in production, the Dev Hub Setup page option "Enable Source Tracking in Developer and Developer Pro Sandboxes" (Enterprise, Performance and Unlimited editions). It applies to sandboxes created or refreshed after it is turned on, so existing sandboxes need a refresh.[^s2]
- **Per sandbox**: Sandbox Settings → "Enable Source Tracking in This Sandbox". This is the only route for Professional and Database.com editions; it tracks only changes made after it is enabled and must be re-enabled after each refresh.[^s2]

## Conflicts

A conflict exists when the same component changed both locally and in the org. Preview commands list conflicts separately, and `sf project deploy start` reports them and stops.[^s4] Salesforce recommends merging the versions by hand, then overwriting one side deliberately: deploy the resolved component with `--ignore-conflicts` to keep the local version, or retrieve it with `--ignore-conflicts` to keep the org version, then deploy the remaining non-conflicting changes normally.[^s4] The flag overwrites without merging, so it should be scoped to the specific components in question.[^s4]

## Limits and gotchas

- **Coverage is not universal.** Not every metadata type supports tracking; check the Source Tracking column of the Metadata Coverage Report.[^s1]
- **Performance cost.** Tracking adds queries and waits on SourceMember, so commands can slow down on medium-to-large projects, and deployments to tracked sandboxes can take longer.[^s1][^s2]
- **Refresh wipes it.** Refreshing a sandbox deletes all its tracking information; disabling tracking triggers a cleanup that can take several days, during which it cannot be re-enabled.[^s2]
- **Untracked orgs still work**, but deploy and retrieve then do no conflict checking, so you must name exactly what to move with `--metadata` or `--source-dir`.[^s1]
- **Resetting is destructive.** `sf project reset tracking` deletes or overwrites local and remote tracking files, after which previews may show no changes even when real differences exist; `--revision` resets to a specific SourceMember RevisionCounter instead.[^s5]

## When to use it (and when not)

Use source tracking for iterative development in scratch orgs and dev sandboxes, especially when several people share a sandbox or when declarative changes made in Setup must be pulled back into Git.[^s3] For integration, UAT or Full sandboxes, where tracking is unavailable, move metadata explicitly with manifests or packages.[^s2]

## Connections

Source tracking is a building block of **Salesforce DX** and of source-driven **application lifecycle management**, and it is driven entirely through the **Salesforce CLI** `project` commands.[^s1] It is native in **scratch orgs** and limited to two of the **sandbox types**, which is why the Dev Hub setting governs its rollout.[^s2] Underneath, deployments ride the **Metadata API** while change detection reads the SourceMember object through the **Tooling API**.[^s1][^s5] Because it records changed components automatically, it removes the manual bookkeeping that **change sets** require, and it sits alongside **DevOps Center** as part of the same Git-centred tooling.[^s1]

## Sources
[^s1]: Salesforce Developers, "Track Changes Between Your Project and Org". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-source-tracking.html (accessed 2026-11-01)
[^s2]: Salesforce Developers, "Enable Source Tracking in Sandboxes". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-setup-enable-source-tracking-sandboxes.html (accessed 2026-11-01)
[^s3]: Salesforce Developers, "Deploy and Retrieve Changes Identified by Source Tracking". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-source-tracking-pull-push-changes.html (accessed 2026-11-01)
[^s4]: Salesforce Developers, "Resolve Conflicts Between Your Local Project and Org". https://developer.salesforce.com/docs/atlas.en-us.264.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_source_tracking_resolve_conflicts.htm (accessed 2026-11-01)
[^s5]: Salesforce Developers, "project reset tracking". https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_project_reset_tracking.html (accessed 2026-11-01)
[^s6]: Salesforce Developers Blog, "Learn MOAR with Summer '20 Release Highlights for Developers". https://developer.salesforce.com/blogs/2020/06/learn-moar-with-summer-20-release-highlights-for-developers (accessed 2026-11-01)
