---
id: kt:patch-releases
type: Concept
title: Patch Releases
aliases: [Salesforce patch release, Salesforce patches, daily releases, emergency releases]
domain: platform-architecture
summary: >-
  The small, frequent releases Salesforce uses between its three seasonal upgrades to ship bug fixes and minor
  changes to every instance, normally without downtime and announced through Trust and My Trust Center.
release: "Winter '27"
status: concept
broader: [kt:salesforce-platform]
related: [kt:salesforce-seasonal-releases, kt:planned-maintenance-windows, kt:trust-and-status-site, kt:marketing-cloud-engagement, kt:financial-services-cloud]
relations:
  - {predicate: dependsOn, object: kt:multitenancy}
sources:
  - id: s1
    title: "Preferred Salesforce Maintenance Schedule"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000386064&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-28
  - id: s2
    title: "Introducing My Trust Center: A Personalized Approach to Trust and Status"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2026/introducing-my-trust-center
    type: official-blog
    accessed: 2026-11-28
  - id: s3
    title: "Understand the Financial Services Cloud Release Process"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/financial-services-cloud-release-readiness/understand-the-financial-services-cloud-release-process
    type: official-learning
    accessed: 2026-11-28
created: 2026-11-28
---

# Patch Releases

A patch release is one of the small updates Salesforce deploys between its three major releases a year. Salesforce's maintenance documentation groups release activity into three kinds: major releases, patch releases and daily releases. Patches and daily releases carry scheduled and ad hoc application fixes and are meant to be invisible to customers.[^s1] Trailhead describes the same mechanism from the product side: bug fixes and minor changes go out as patches rather than waiting for the next seasonal release.[^s3]

## How it works

Patches roll across the fleet on a regular rhythm rather than on fixed public dates. The Help article on the preferred maintenance schedule says patch releases are scheduled weekly and normally reach instances on a Tuesday, Wednesday or Thursday, with Asia-Pacific instances following a day later.[^s1] Daily releases are the as-needed channel for urgent fixes and can land on any day of the week.[^s1] Where possible both kinds are deployed in off-peak hours and with no downtime, which is the main operational difference from a major release: on first-party instances a major release can make the instance unavailable for up to five minutes.[^s1]

A weekly schedule does not mean a patch every week. Trailhead notes that patches are sometimes skipped, for example around a major release or a large event such as Dreamforce.[^s3] The Admins Blog, announcing My Trust Center in April 2026, describes patch releases as happening every two weeks, so treat the cadence as a planning assumption, not a guarantee, and check the actual events for your own instances.[^s2]

Other clouds run their own variants. For Marketing Cloud Engagement the same Help article lists major, patch and emergency releases; its patches roll out over two weeks, starting on a Thursday and finishing on the following Thursday, and emergency releases happen as needed on any day, all without downtime.[^s1]

## Visibility and notification

Seasonal releases are announced a year ahead, but patches are visible mainly through Trust tooling. My Trust Center, the authenticated per-tenant portal, shows detailed deployment information for patch releases and feature enablement four to five days before a patch goes live, together with the patch's release notes.[^s2] Admins can subscribe to patch-release events alongside incidents and maintenance windows, and the portal keeps a year of history; at launch Salesforce said sandbox orgs were still being added.[^s2]

## Gotchas

- **Behaviour can change mid-release.** Bug fixes arrive in patches between seasonal releases, so a process can change weeks after an upgrade; retest after fixes you rely on land.[^s1][^s3]
- **Regional offsets.** Asia-Pacific instances usually get a patch a day after other regions, which matters for global regression checks.[^s1]
- **No downtime is a goal, not a promise.** Salesforce deploys patches without downtime "whenever possible", so schedule critical loads with that caveat in mind.[^s1]
- **Subscriptions don't migrate.** Legacy Trust notifications don't carry over to My Trust Center; patch alerts must be set up again there.[^s2]

## Connections

Patch releases are an operational property of the **Salesforce platform** and depend on **multitenancy**: because every customer runs the same codebase, one fix can be rolled out to every instance on a common schedule.[^s1] They complement **Salesforce seasonal releases**, which deliver new features three times a year, while patches carry fixes in between.[^s1][^s3] They are deployed inside the regional rhythm described under **planned maintenance windows**, and announced on the **Trust and Status site** and My Trust Center.[^s1][^s2] **Marketing Cloud Engagement** has its own two-week patch and emergency release process, and **Financial Services Cloud** uses weekly patches for bug fixes between its major releases.[^s1][^s3]

## Sources
[^s1]: Salesforce Help, "Preferred Salesforce Maintenance Schedule". https://help.salesforce.com/s/articleView?id=000386064&language=en_US&type=1 (accessed 2026-11-28)
[^s2]: Salesforce Admins Blog, "Introducing My Trust Center: A Personalized Approach to Trust and Status". https://admin.salesforce.com/blog/2026/introducing-my-trust-center (accessed 2026-11-28)
[^s3]: Trailhead, "Understand the Financial Services Cloud Release Process". https://trailhead.salesforce.com/content/learn/modules/financial-services-cloud-release-readiness/understand-the-financial-services-cloud-release-process (accessed 2026-11-28)
