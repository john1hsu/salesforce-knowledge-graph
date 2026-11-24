---
id: kt:rollback-plan
type: Concept
title: Rollback Plan
aliases: [deployment rollback plan, rollback strategy, back-out plan, release rollback, roll back a deployment]
domain: devops-and-alm
summary: >-
  The pre-written, rehearsed procedure for returning a Salesforce org to its last known good state when a release
  fails, including who may order it, the triggers that invoke it, and how metadata and data are reverted.
release: "Winter '27"
status: concept
broader: [kt:release-management]
related: [kt:cutover-plan, kt:hypercare, kt:deployment-validation-and-quick-deploy, kt:branching-strategy, kt:salesforce-cli]
relations:
  - {predicate: dependsOn, object: kt:backup-and-recover}
  - {predicate: dependsOn, object: kt:destructive-changes}
sources:
  - id: s1
    title: "Manage the Launch and Post-Launch Activities"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/cc-project-mgmt/cc-launch-and-post-launch
    type: official-learning
    accessed: 2026-11-24
  - id: s2
    title: "Master Metadata API Deployments with Best Practices"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2025/10/master-metadata-api-deployments-with-best-practices
    type: official-blog
    accessed: 2026-11-24
  - id: s3
    title: "project deploy start (Salesforce CLI Command Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_project_deploy_start.html
    type: official-docs
    accessed: 2026-11-24
  - id: s4
    title: "Deleting Components from an Organization (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_deploy_deleting_files.htm
    type: official-docs
    accessed: 2026-11-24
  - id: s5
    title: "OPS06-BP01 Plan for unsuccessful changes (Operational Excellence Pillar)"
    publisher: AWS Well-Architected Framework
    url: https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_mit_deploy_risks_plan_for_unsucessful_changes.html
    type: partner
    accessed: 2026-11-24
created: 2026-11-24
---

# Rollback Plan

A rollback plan is the documented way back. It says how a team returns production to the last state that worked if a release goes wrong, who is allowed to make that call, and how long it should take. Trailhead's launch unit treats rollout and rollback as twin procedures in a launch plan, both written by the functional architect, and calls rollback the "emergency brake" for launch day.[^s1] AWS's operational guidance frames the same choice more generally: when a change fails, either revert to a known good state or remediate in production, and decide in advance which one applies.[^s5]

## Why Salesforce needs an explicit plan

Salesforce has no "undo release" button. A Metadata API deployment is atomic for the package it carries: by default a component error, and unless you opt out a warning, fails the whole deploy and rolls it back.[^s3] That protects you from a half-applied package, but it does nothing once a deployment has succeeded and the problem only shows up later in user traffic. To get back to the old version you have to make another deployment that carries the previous metadata, plus deletions for components the release added.[^s2][^s4] So a Salesforce rollback plan is a second, pre-built release, not a switch you flip.

The Salesforce CLI makes the partial-deploy risk explicit. Its `--ignore-errors` flag deploys whatever components succeed and skips the rest. The reference says never to use it against production, because the result can be an inconsistent org.[^s3] The Metadata API blog likewise warns that when rollback-on-error is switched off, components deployed before the error stay in the org, and asks teams to think through their rollback needs before using that option.[^s2]

## What the plan contains

A workable Salesforce rollback plan usually has these parts:

- **A known good baseline.** Version control holds the exact metadata currently in production, so you can redeploy the previous state; the Salesforce blog cites Git's ability to revert when a deployment fails.[^s2]
- **A pre-release backup.** Salesforce recommends backing up both metadata and data before a major deployment, and checking Setup Audit Trail for manual changes that source control would miss.[^s2]
- **The reverse deployment, prepared ahead.** A destructive manifest removes components the release introduced. Since API 33.0, pre- and post-destructive manifests control whether deletions run before or after the additions in the same deploy.[^s4]
- **Triggers and authority.** The communication plan names who can sign off a successful go-live and who can declare that it must be rolled back.[^s1] AWS adds that the policy should state what triggers a rollback and when fixing forward is allowed instead.[^s5]
- **Rehearsal.** Trailhead's team rehearsed the rollout in a dry run and tested rollback separately; AWS asks for a documented, tested plan before the production deployment.[^s1][^s5]

## Limits and gotchas

Some changes cannot be cleanly reversed with metadata alone. Deleting components through a destructive manifest needs a companion package.xml that lists no components, wildcards are not supported, and an item referenced by an active Lightning page action override must have that override deactivated first.[^s4] With `purgeOnDelete`, deleted components skip the Recycle Bin, and roll-up summary fields removed through the Metadata API are purged even without it, so the plan should assume those deletions are permanent.[^s4] Data that users created or changed after go-live is the hardest part to reverse, which is why a backup taken just before the deployment matters.[^s2]

A validated deployment is the cheapest insurance. A CLI dry run validates the deploy and runs Apex tests without saving anything to the org, so problems surface before the change and before any rollback is needed.[^s3] Practising the deployment and its recovery in a full sandbox is the recommended way to time both.[^s2] AWS also advises smaller changes, which recover faster, and monitoring that confirms success or failure so the rollback decision isn't made by guesswork while users are active.[^s5]

## When to roll back vs. fix forward

Roll back when the defect blocks critical business processes and no fix can be validated and deployed inside the agreed window. Fix forward when the issue is contained, a corrected deployment can be validated quickly, or reverting would throw away data users have already entered. Either way the decision rule belongs in the plan, agreed before launch.[^s5][^s1]

## Connections

A rollback plan sits **broader** under release management, as the failure path of every production release.[^s2] It is **related** to the cutover plan, which embeds rollback checkpoints in the go-live runbook, and to hypercare, where the plan stays ready until the release stabilises.[^s1] It is **related** to deployment validation and quick deploy and to the Salesforce CLI, whose validate-only and all-or-nothing deploy behaviour reduce how often a rollback is needed,[^s3] and to branching strategy, which keeps the last known good version easy to redeploy.[^s2] It **depends on** destructive changes to remove what a release added[^s4] and on backup and recovery tooling for the data and metadata the release changed.[^s2]

## Sources

[^s1]: Trailhead, "Manage the Launch and Post-Launch Activities". https://trailhead.salesforce.com/content/learn/modules/cc-project-mgmt/cc-launch-and-post-launch (accessed 2026-11-24)
[^s2]: Salesforce Developers Blog, "Master Metadata API Deployments with Best Practices" (2025-10-07). https://developer.salesforce.com/blogs/2025/10/master-metadata-api-deployments-with-best-practices (accessed 2026-11-24)
[^s3]: Salesforce Developers, "project deploy start", Salesforce CLI Command Reference. https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_project_deploy_start.html (accessed 2026-11-24)
[^s4]: Salesforce Developers, "Deleting Components from an Organization", Metadata API Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_deploy_deleting_files.htm (accessed 2026-11-24)
[^s5]: AWS, "OPS06-BP01 Plan for unsuccessful changes", Well-Architected Operational Excellence Pillar. https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_mit_deploy_risks_plan_for_unsucessful_changes.html (accessed 2026-11-24)
