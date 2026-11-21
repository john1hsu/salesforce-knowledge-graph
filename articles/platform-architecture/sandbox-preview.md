---
id: kt:sandbox-preview
type: Concept
title: Sandbox Preview
aliases: [Salesforce Preview, preview sandbox, preview window, sandbox preview window, preview instance]
domain: platform-architecture
summary: >-
  The window in each seasonal release, roughly four to six weeks before the production upgrade, when sandboxes on
  preview instances (and preview scratch orgs) get the upcoming release early so teams can test it against their own
  configuration.
release: "Winter '27"
status: current
broader: [kt:salesforce-seasonal-releases]
related: [kt:sandbox-types, kt:scratch-orgs, kt:release-management, kt:release-updates, kt:environment-strategy]
relations:
  - {predicate: partOf, object: kt:salesforce-seasonal-releases}
  - {predicate: dependsOn, object: kt:pod-and-instance-architecture}
  - {predicate: enables, object: kt:testing-strategy}
  - {predicate: configuredVia, object: kt:dev-hub}
sources:
  - id: s1
    title: "Access Sandbox Preview for New Features (Salesforce Releases)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/sf_releases/sf-releases-sandbox-preview
    type: official-learning
    accessed: 2026-11-21
  - id: s2
    title: "Select the Salesforce Release for a Scratch Org (Salesforce DX Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-scratch-orgs-version-selection.html
    type: official-docs
    accessed: 2026-11-21
  - id: s3
    title: "Be Release Ready: The Admin Habit That Saves You Every Time"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2026/be-release-ready-the-admin-habit-that-saves-you-every-time
    type: official-blog
    accessed: 2026-11-21
  - id: s4
    title: "Admin Release Countdown: Get Ready for Spring '26"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2025/admin-spring-26-release-dates-countdown
    type: official-blog
    accessed: 2026-11-21
created: 2026-11-21
---

# Sandbox Preview

**Sandbox preview** is the stretch of every seasonal release when some sandboxes are upgraded to the upcoming release ahead of production, so admins and developers can try new features and regression-test them against their own configuration and data instead of a blank org. It starts approximately four to six weeks before the production upgrade.[^s1] The Salesforce DX documentation calls the same window **Salesforce Preview**: during it both sandboxes and scratch orgs can run the next release early, and scratch orgs created on it are called preview scratch orgs.[^s2]

## How it works

Sandboxes live on instances that are either **preview** or **non-preview**. Preview instances are upgraded at the start of the window; non-preview instances receive the release later, sometimes only after production itself has been upgraded.[^s1] Which kind of instance a sandbox sits on is decided by its most recent refresh, and the timing of that refresh matters: a refresh before the preview cutoff usually lands the sandbox on a preview instance, while a sandbox refreshed during the preview window moves to a non-preview instance.[^s1] So a sandbox you want to keep on the new release should not be refreshed after the cutoff, or it can lose the upgrade.[^s1]

To see where you stand, read the **Location** column under Setup > Sandboxes and look each instance up in Salesforce's Sandbox Preview Guide, which tells you whether that sandbox needs action and by when.[^s1][^s3] Each release's countdown gives a concrete deadline; for Spring '26, admins who wanted early access in a sandbox not already slated for preview had to act before 5 p.m. Pacific on January 8, and preview began on January 9.[^s4]

For scratch orgs, the window has published dates. The DX guide lists Winter '27 preview as August 30 to October 10, 2026, Spring '27 as January 10 to February 20, 2027, and Summer '27 as May 9 to June 12, 2027; the start is when sandbox instances are upgraded and the end is when every instance is on the GA release.[^s2] You choose the version with `"release": "preview"` or `"previous"` in the scratch org definition file or the `--release` flag of `sf org create scratch` (the flag wins), relative to the Dev Hub's own version, and you should set the API version to match.[^s2] Your existing Dev Hub and its limits work; no special trial Dev Hub is needed.[^s2]

## Limits and gotchas

- **Relative values can fail.** If the Dev Hub is already on the newest release, `preview` errors; if it is on the GA release, `previous` errors.[^s2]
- **Transition days.** Sandbox instances start upgrading several days before the official preview start, before the Dev Hub moves, so a scratch org can land on preview unexpectedly; recreate it shortly before the start or wait and use `previous`.[^s2]
- **Refresh erases.** Activating a refreshed sandbox deletes the sandbox it replaces, including its current configuration and data, so plan refreshes made only to change instance.[^s1]
- **Pre-release orgs differ.** A pre-release org is an earlier build available before Salesforce Preview; it is not built for scale, has no Support SLAs, and has none of your customisations.[^s2]

## When to use it (and when not)

Salesforce's admin guidance is to keep a deliberate mix: at least one sandbox on preview for regression testing and feature evaluation, and non-preview sandboxes as the deployment path.[^s1][^s3] Deploy "from like states" — non-preview sandbox to non-preview production — because a preview sandbox can carry new permissions or metadata that break a deployment to a production org still on the old release, and source control does not record which release a target org runs.[^s3] If a regression appears in preview, reproduce it in a non-preview sandbox first to confirm it is new, then open a Support case.[^s3] Release updates with enforcement dates also deserve testing in a preview sandbox well before they switch on.[^s3]

## Connections

Sandbox preview is part of Salesforce's **seasonal releases**, the three-releases-a-year cadence, and it only works because the platform upgrades by instance, linking it to **pod and instance architecture**.[^s1] It shapes **environment strategy** and **release management** (which sandboxes stay on the deployment path), applies to the **sandbox types** you refresh, and extends to **scratch orgs** created through a **Dev Hub**.[^s2][^s3] It is where teams exercise **testing strategy** and upcoming **release updates** before production changes.[^s3]

## Sources

[^s1]: Trailhead, "Access Sandbox Preview for New Features". https://trailhead.salesforce.com/content/learn/modules/sf_releases/sf-releases-sandbox-preview (accessed 2026-11-21)
[^s2]: Salesforce, "Select the Salesforce Release for a Scratch Org", Salesforce DX Developer Guide. https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-scratch-orgs-version-selection.html (accessed 2026-11-21)
[^s3]: Salesforce Admins Blog, "Be Release Ready: The Admin Habit That Saves You Every Time". https://admin.salesforce.com/blog/2026/be-release-ready-the-admin-habit-that-saves-you-every-time (accessed 2026-11-21)
[^s4]: Salesforce Admins Blog, "Admin Release Countdown: Get Ready for Spring '26". https://admin.salesforce.com/blog/2025/admin-spring-26-release-dates-countdown (accessed 2026-11-21)
