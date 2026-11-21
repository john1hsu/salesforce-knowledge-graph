---
id: kt:salesforce-seasonal-releases
type: Concept
title: Salesforce Seasonal Releases
aliases: [Salesforce major releases, Spring Summer Winter releases, Salesforce release cycle, release weekend, three releases a year]
domain: platform-architecture
summary: >-
  Salesforce's cadence of three major platform upgrades a year, named Spring, Summer and Winter, which are applied
  automatically to every org on a published schedule, preceded by release notes, pre-release orgs and a sandbox
  preview window.
release: "Winter '27"
status: concept
broader: [kt:salesforce-platform]
related: [kt:release-management, kt:release-updates, kt:trust-and-status-site, kt:sandbox-types, kt:testing-strategy]
relations:
  - {predicate: dependsOn, object: kt:multitenancy}
  - {predicate: hasPart, object: kt:sandbox-preview}
sources:
  - id: s1
    title: "Get to Know the Salesforce Release Process (Salesforce Releases)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/sf_releases/sf_releases_start
    type: official-learning
    accessed: 2026-11-21
  - id: s2
    title: "Salesforce Releases"
    publisher: Salesforce
    url: https://www.salesforce.com/releases/
    type: official-docs
    accessed: 2026-11-21
  - id: s3
    title: "What Admins Need to Know About Salesforce Releases"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2021/salesforce-release-overview
    type: official-blog
    accessed: 2026-11-21
  - id: s4
    title: "Admin Release Countdown: Get Ready for Winter '27"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2026/admin-winter-27-release-countdown
    type: official-blog
    accessed: 2026-11-21
  - id: s5
    title: "Optimize Your Salesforce Release Process (Advanced Salesforce Release Readiness Strategies)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/advanced-salesforce-release-readiness-strategies/master-the-release-readiness-process
    type: official-learning
    accessed: 2026-11-21
created: 2026-11-21
---

# Salesforce Seasonal Releases

Salesforce ships new platform functionality three times a year in seasonal releases named Spring, Summer and Winter. Every customer is upgraded automatically, so all orgs run the same version, and the upgrade itself needs only about five minutes of scheduled maintenance.[^s1] The names follow the northern hemisphere seasons.[^s3] In practice Spring usually lands in February, Summer in June and Winter in October; Winter '27 is the release currently in production, and some individual products also ship smaller updates monthly.[^s2]

## How a release unfolds

Each release begins roughly three months before it reaches production, and the work for customers is to understand and test it before it arrives.[^s1] The cycle has a predictable set of milestones:

- **Pre-release org.** A Developer Edition org on the new release, usually available three to four weeks before sandbox preview starts; it has none of your customisations.[^s5]
- **Release notes.** Published ahead of the upgrade; Trailhead suggests reading the orientation sections first, then Salesforce Overall, then the clouds and add-ons you license.[^s5]
- **Sandbox preview.** Sandboxes on preview instances are upgraded first, four to six weeks before production.[^s1][^s2]
- **Release weekends.** Production instances are upgraded in waves during scheduled release weekends, so the date depends on your instance.[^s2][^s3]

Winter '27 illustrates the timing. The Admins Blog countdown listed pre-release sign-up on August 13, 2026, release notes on August 19, a sandbox refresh deadline of August 27 before 5 p.m. PT to land on a preview instance, sandbox preview from August 28, and production upgrades on September 4, October 2 and October 9.[^s4]

Upgrade dates are published well in advance on the Salesforce Trust site, which Trailhead says can be up to a year ahead; the Major Release Maintenance Schedule there shows sandbox and production dates per instance.[^s1][^s2]

## Feature lifecycle within releases

A release does not mean every feature is finished. Features can arrive as a pilot open to a small set of opted-in orgs, as a beta for public testing with limited support, or as generally available.[^s3] The release notes state how and when each feature becomes available, including whether it is on automatically or must be enabled by an admin.[^s5] Behaviour changes that Salesforce will eventually enforce are tracked separately as release updates with their own due dates.[^s3]

## Gotchas

- **Sandbox placement matters.** Whether a sandbox is on a preview or non-preview instance depends on when it was last refreshed relative to the deadline.[^s3][^s4]
- **Don't cross versions.** Salesforce strongly recommends against deploying changes from a preview sandbox to a non-preview environment.[^s3]
- **Dates vary by instance.** Check the Trust maintenance calendar for your own instance rather than assuming the first release weekend.[^s2][^s3]
- **Plan several releases out.** Trailhead advises noting sandbox and production dates for the next two or three releases.[^s1]

Because the upgrade is not optional, the realistic choice is how early to look. Teams that regression-test in a preview sandbox and read the notes for their clouds catch conflicts weeks before production; teams that wait see the changes when users do.[^s3][^s5]

## Connections

Seasonal releases are a property of the **Salesforce platform** as a whole, which is why the node sits under it, and they depend on **multitenancy**: one shared codebase lets Salesforce upgrade every customer at once on the same version.[^s1] **Sandbox preview** is the phase where most customer testing happens, and the choice among **sandbox types** decides how realistic that testing is.[^s1][^s3] A customer's own **release management** has to schedule around these upgrades, and a **testing strategy** should include a regression pass per release.[^s3][^s5] **Release updates** are the per-change enforcement mechanism that rides on the seasonal cycle, and the **Trust and Status site** is where instance-specific upgrade dates are published.[^s1][^s3]

## Sources
[^s1]: Trailhead, "Get to Know the Salesforce Release Process". https://trailhead.salesforce.com/content/learn/modules/sf_releases/sf_releases_start (accessed 2026-11-21)
[^s2]: Salesforce, "Salesforce Releases". https://www.salesforce.com/releases/ (accessed 2026-11-21)
[^s3]: Salesforce Admins Blog, "What Admins Need to Know About Salesforce Releases". https://admin.salesforce.com/blog/2021/salesforce-release-overview (accessed 2026-11-21)
[^s4]: Salesforce Admins Blog, "Admin Release Countdown: Get Ready for Winter '27". https://admin.salesforce.com/blog/2026/admin-winter-27-release-countdown (accessed 2026-11-21)
[^s5]: Trailhead, "Optimize Your Salesforce Release Process". https://trailhead.salesforce.com/content/learn/modules/advanced-salesforce-release-readiness-strategies/master-the-release-readiness-process (accessed 2026-11-21)
