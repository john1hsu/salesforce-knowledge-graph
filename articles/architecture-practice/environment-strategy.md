---
id: kt:environment-strategy
type: Concept
title: Environment Strategy
aliases: [sandbox strategy, Salesforce environment strategy, environment plan, org landscape for releases]
domain: architecture-practice
summary: >-
  The architectural plan for which non-production environments (sandboxes, scratch orgs and preview orgs) a
  Salesforce team runs, what each one is for, how changes and data flow between them, and when they are refreshed.
release: "Winter '27"
status: concept
broader: [kt:application-lifecycle-management]
related: [kt:scratch-orgs, kt:change-sets, kt:org-strategy, kt:salesforce-data-mask]
relations:
  - {predicate: hasPart, object: kt:sandbox-types}
  - {predicate: configuredVia, object: kt:devops-center}
  - {predicate: dependsOn, object: kt:sandbox-templates}
sources:
  - id: s1
    title: "Deploy Your Changes and Sandboxes (Salesforce Help PDF)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/deploy_sandboxes.pdf
    type: official-docs
    accessed: 2026-10-31
  - id: s2
    title: "Build and Release Your App with Metadata API (Salesforce DX Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-build-mdapi.html
    type: official-docs
    accessed: 2026-10-31
  - id: s3
    title: "Use Sandboxes to Manage Change"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/nonprofit-success-pack-maintenance/use-sandboxes-to-manage-change
    type: official-learning
    accessed: 2026-10-31
  - id: s4
    title: "Get to Know Salesforce Data Mask"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-data-mask/get-to-know-salesforce-data-mask
    type: official-learning
    accessed: 2026-10-31
  - id: s5
    title: "Admin Release Countdown: Get Ready for Winter '27"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2026/admin-winter-27-release-countdown
    type: official-blog
    accessed: 2026-10-31
created: 2026-10-31
---

# Environment Strategy

An environment strategy is the deliberate design of a Salesforce team's non-production landscape: how many sandboxes and other orgs exist, which stage of delivery each one serves, which direction changes are allowed to flow, what data each holds, and how refreshes line up with the release calendar. Salesforce's own guidance stresses that changes should be built in a sandbox and then deployed to production, and that sandboxes are also where teams preview and test new Salesforce releases before they reach production.[^s3] Because each sandbox type copies different amounts of metadata and data and can be refreshed on a different cadence, the choice of environments shapes how fast and how safely a team can ship.[^s1]

## The building blocks

Salesforce offers four sandbox types. Developer and Developer Pro sandboxes copy metadata only, with 200 MB and 1 GB of data storage respectively, and both can be refreshed once a day. Partial Copy sandboxes add a sample of production data defined by a required sandbox template, hold up to 5 GB of data, and refresh every 5 days. Full sandboxes copy metadata and all data and can be refreshed every 29 days.[^s1] The refresh interval is counted from when copying starts, not from when the refresh was requested.[^s1] According to Salesforce Help, only Full sandboxes support performance testing, load testing and staging.[^s1]

## A reference pipeline

The Salesforce DX Developer Guide describes a four-stage org development pipeline that many teams use as a baseline:[^s2]

1. **Develop.** Each team member builds in their own Developer sandbox, which contains no production data, so work proceeds in parallel.[^s2]
2. **Integrate.** Work is merged into a shared Developer Pro sandbox, which can be seeded with test data.[^s2]
3. **Test.** A Partial sandbox hosts user acceptance testing against realistic data.[^s2]
4. **Stage and release.** The release is deployed to a Full sandbox, regression-tested there, and then deployed to production; afterwards the Full sandbox can double as a training environment.[^s2]

Throughout, source control holds all changes, and running local tests in a development sandbox before release reduces the tests needed in the production deployment.[^s2]

## Promotion paths and release timing

When teams move changes with change sets, each pair of orgs needs a deployment connection, and each org must be authorised to send or receive. Those authorisations enforce the promotion path, for example letting production accept changes only from a test org.[^s1] Salesforce recommends limiting production changes while a sandbox is being created or refreshed, because changes made to production after a sandbox is copied do not sync to it.[^s1]

Major releases add a second dimension. Preview sandboxes are upgraded roughly six weeks before production, while non-preview sandboxes stay on the current release and are the ones to build production-bound changes in.[^s1] Trailhead advises keeping at least one sandbox on preview for the whole preview window.[^s3] For Winter '27, sandboxes had to be refreshed before 27 August to land on the intended instance, preview began on 28 August, and production upgrades followed on 4 September, 2 October and 9 October.[^s5]

## Limits and gotchas

- Sandboxes do not send email when they hit their storage limit; they simply stop accepting new data.[^s1]
- Big Object records, archived activities, password history and setup audit trail history are not copied into any sandbox.[^s1]
- New sandboxes that are not activated within 30 days are deleted.[^s1]
- Copying production data into Partial or Full sandboxes carries its privacy obligations with it. Salesforce Data Mask can scramble, replace or delete sensitive field values in Full and Partial sandboxes, but masking is one-way: restoring original values requires a refresh.[^s4]

## When to adjust the baseline

Smaller teams can keep the landscape lean: a sandbox for building features, a preview sandbox during release windows, and a Partial Copy or Full sandbox when training needs real-world data, or a Developer sandbox with sample data when it does not.[^s3] Larger programmes add per-developer orgs, a dedicated integration org and a Full staging org so that parallel streams can be merged and load-tested before go-live.[^s2][^s1] Whatever the size, an explicit plan for refresh cadence, data seeding and masking, and preview-sandbox assignment keeps environments representative without exposing sensitive data.[^s1][^s4]

## Connections

Environment strategy sits **under** `kt:application-lifecycle-management`, providing the build, test and deploy stages with places to run.[^s2] It **has part** `kt:sandbox-types`, the four sandbox editions whose storage and refresh limits constrain the design, and **depends on** `kt:sandbox-templates`, which decide what data Partial and Full sandboxes receive.[^s1] It is **configured via** `kt:devops-center`, which promotes work through a pipeline of these environments, and is **related** to `kt:scratch-orgs` (the source-driven alternative to per-developer sandboxes), `kt:change-sets` (whose deployment connections encode promotion paths), `kt:org-strategy` (how many production orgs exist at all) and `kt:salesforce-data-mask` (protecting copied production data).[^s1][^s2][^s4]

## Sources

[^s1]: Salesforce, "Deploy Your Changes and Sandboxes" (Help PDF). https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/deploy_sandboxes.pdf (accessed 2026-10-31)
[^s2]: Salesforce, "Build and Release Your App with Metadata API". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-build-mdapi.html (accessed 2026-10-31)
[^s3]: Trailhead, "Use Sandboxes to Manage Change". https://trailhead.salesforce.com/content/learn/modules/nonprofit-success-pack-maintenance/use-sandboxes-to-manage-change (accessed 2026-10-31)
[^s4]: Trailhead, "Get to Know Salesforce Data Mask". https://trailhead.salesforce.com/content/learn/modules/salesforce-data-mask/get-to-know-salesforce-data-mask (accessed 2026-10-31)
[^s5]: Salesforce Admins Blog, "Admin Release Countdown: Get Ready for Winter '27". https://admin.salesforce.com/blog/2026/admin-winter-27-release-countdown (accessed 2026-10-31)
