---
id: kt:change-sets
type: Tool
title: Change Sets
aliases: [change set, outbound change set, inbound change set, deployment connections]
domain: devops-and-alm
summary: >-
  Salesforce's point-and-click Setup tool for sending metadata customizations (not records) from one org to a
  connected, affiliated org, such as from a sandbox to production, as an outbound change set that the target deploys
  as an inbound change set.
release: "Winter '27"
status: current
broader: [kt:application-lifecycle-management]
related: [kt:metadata-api, kt:environment-strategy, kt:sandbox-types]
relations:
  - {predicate: alternativeTo, object: kt:devops-center}
  - {predicate: alternativeTo, object: kt:salesforce-cli}
  - {predicate: dependsOn, object: kt:apex-testing}
  - {predicate: contrastsWith, object: kt:unlocked-packages}
sources:
  - id: s1
    title: "Change Sets"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=changesets.htm
    type: official-docs
    accessed: 2026-10-31
  - id: s2
    title: "Change Sets Best Practices"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=platform.changesets_best_practices.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-10-31
  - id: s3
    title: "Salesforce Developer Limits and Allocations Quick Reference: Platform Metadata"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-app-limits-cheatsheet/guide/salesforce-app-limits-platform-metadata.html
    type: official-docs
    accessed: 2026-10-31
  - id: s4
    title: "DevOps Center for Hybrid Teams"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/09/devops-center-for-hybrid-teams
    type: official-blog
    accessed: 2026-10-31
  - id: s5
    title: "Package Development Model: Enhance Your Development Skills with Package Management"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/ko/content/learn/modules/sfdx_dev_model/sfdx_dev_model_neworganization
    type: official-learning
    accessed: 2026-10-31
created: 2026-10-31
---

# Change Sets

Change sets are the Setup-based way to move customizations from one Salesforce org to another, most often from a sandbox where they were built and tested into production. They carry only changes that can be made in Setup; they never carry records or other data.[^s1] They are available in Enterprise, Performance, Professional, Unlimited and Database.com editions, in both Salesforce Classic and Lightning Experience.[^s1] As of Winter '27 they remain a supported, current tool, although Salesforce positions DevOps Center as the path for teams that outgrow them.[^s4]

## How it works

A change set has two faces. In the org where the work was done, an admin builds an **outbound** change set, adds components, and uploads it. In the receiving org it appears as an **inbound** change set, and nothing changes until someone deploys it. Deployment is all or nothing: the whole set is deployed, not individual components.[^s1]

Uploads travel only over **deployment connections**, which can link only orgs affiliated with the same production org, such as production and one of its sandboxes, or two sandboxes created from that org.[^s1] Unrelated orgs, such as two separate production orgs, cannot exchange change sets. Permissions are split by role: creating and uploading needs *Create and Upload Change Sets*, while editing deployment connections or deploying an inbound set needs both *Deploy Change Sets* and *Modify Metadata Through Metadata API Functions*.[^s1]

Before a planned release, admins can **validate** an inbound set, which performs a test deployment that reports failures without committing changes. Salesforce suggests doing this for scheduled deployments but skipping it for routine ones, because validation takes time and locks the org.[^s2] When the target is production and the set includes Apex, all local tests run by default; deployments into sandboxes do not run tests automatically.[^s2]

## Limits and gotchas (Winter '27)

- **10,000 files.** Inbound and outbound change sets can hold up to 10,000 files of metadata, the same per-operation cap as Metadata API deploy and retrieve.[^s3] If a release exceeds it, Salesforce suggests putting email templates, reports and dashboards in separate sets, since they are numerous and have few dependencies.[^s2]
- **No deletes or renames.** A change set cannot delete or rename a component. Deletions happen by hand in the target org; a rename means deleting the old component there and deploying the new one. Switching a master-detail parent's sharing from Controlled by Parent to Public Read/Write also counts as a deletion.[^s2]
- **Dependencies are on you.** Any interdependent component missing from the target must be added, or the deploy fails. Adding a custom object without its fields deploys an empty object.[^s2]
- **Uploaded sets are frozen.** An uploaded change set cannot be edited. To fix a missing dependency, clone it, add the component and upload again.[^s2]
- **Org locks.** The source org is locked during outbound validation and the target during inbound deployment. Records can still be read and written, but metadata cannot be changed in Setup.[^s2]
- **Access is separate.** Profiles or permission sets must be included for users to see new functionality, and the two behave differently in a change set.[^s2]
- **Slow field-type changes.** Changing a custom field's type may take a long time if many records must be updated, so applying it manually after deployment can be the better option.[^s2]
- **Metadata only.** Teams that need to move metadata and data together are pointed to other tooling.[^s1]

## When to use it (and when not)

Change sets suit admin-led teams that make declarative changes in a sandbox and promote them along a short, fixed path to production. Their weakness is that nothing they move ever passes through version control. Salesforce's own developer blog notes they do not work with the Salesforce CLI or source-driven development, give little visibility into what a release contains, and leave the shared repository missing whatever was deployed this way.[^s4] DevOps Center keeps the clicks-first experience but adds work items, a feature branch per work item, and a pipeline of stages tied to orgs and branches, so declarative and code-based developers commit to one repository.[^s4]

More broadly, change sets belong to org-based development, where production is the source of truth and developers must track by hand what they changed. Trailhead notes that this intermingles teams' work into one release, which is why package-based development moves the source of truth into version control.[^s5]

## Connections

Change sets sit **under** `kt:application-lifecycle-management` as one of its deployment mechanisms, and are **related** to `kt:metadata-api`, whose 10,000-file deploy cap they share.[^s3] Their deployment connections only join affiliated orgs, which ties them to `kt:sandbox-types` and to `kt:environment-strategy`, where those connections encode the promotion path.[^s1] They are an **alternative to** `kt:devops-center`, Salesforce's source-control-backed successor for declarative teams, and to `kt:salesforce-cli`, the source-driven route they cannot participate in.[^s4] They **depend on** `kt:apex-testing`, because production deploys containing Apex run local tests by default.[^s2] They **contrast with** `kt:unlocked-packages`, which make version control rather than production the source of truth.[^s5]

## Sources

[^s1]: Salesforce Help, "Change Sets". https://help.salesforce.com/apex/HTViewHelpDoc?id=changesets.htm (accessed 2026-10-31)
[^s2]: Salesforce Help, "Change Sets Best Practices". https://help.salesforce.com/s/articleView?id=platform.changesets_best_practices.htm&language=en_US&type=5 (accessed 2026-10-31)
[^s3]: Salesforce Developers, "Salesforce Developer Limits and Allocations Quick Reference: Platform Metadata". https://developer.salesforce.com/docs/platform/salesforce-app-limits-cheatsheet/guide/salesforce-app-limits-platform-metadata.html (accessed 2026-10-31)
[^s4]: Salesforce Developers Blog, "DevOps Center for Hybrid Teams". https://developer.salesforce.com/blogs/2024/09/devops-center-for-hybrid-teams (accessed 2026-10-31)
[^s5]: Trailhead, "Package Development Model: Enhance Your Development Skills with Package Management". https://trailhead.salesforce.com/ko/content/learn/modules/sfdx_dev_model/sfdx_dev_model_neworganization (accessed 2026-10-31)
