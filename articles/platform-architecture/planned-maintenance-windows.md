---
id: kt:planned-maintenance-windows
type: Concept
title: Planned Maintenance Windows
aliases: [preferred maintenance windows, Preferred Salesforce Maintenance Schedule, Salesforce system maintenance windows, scheduled maintenance, release maintenance windows]
domain: platform-architecture
summary: >-
  The recurring time slots in which Salesforce performs scheduled system maintenance, major release upgrades and
  patch releases on each instance, published per region with advance Trust notifications and sometimes involving
  read-only access or brief unavailability.
release: "Winter '27"
status: concept
broader: [kt:salesforce-platform]
related: [kt:trust-and-status-site, kt:salesforce-seasonal-releases, kt:sandbox-preview, kt:instance-refresh-and-org-migration, kt:disaster-recovery-and-site-switching, kt:patch-releases]
relations:
  - {predicate: dependsOn, object: kt:pod-and-instance-architecture}
  - {predicate: dependsOn, object: kt:read-only-mode}
  - {predicate: contrastsWith, object: kt:hyperforce}
sources:
  - id: s1
    title: "Preferred Salesforce Maintenance Schedule"
    publisher: Salesforce Help
    url: https://help.salesforce.com/HTViewSolution?id=000176208
    type: official-docs
    accessed: 2026-11-27
  - id: s2
    title: "Salesforce Release Process and Transitioning Tips"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/modules/sf_releases/units/sf_releases_start
    type: official-learning
    accessed: 2026-11-27
  - id: s3
    title: "Site Switching and Apex Callouts"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2017/10/site-switching-apex-callouts
    type: official-blog
    accessed: 2026-11-27
  - id: s4
    title: "What do I need to do about my upcoming Salesforce site switch?"
    publisher: Heroku Help
    url: https://help.heroku.com/GXAW850T/what-do-i-need-to-do-about-my-upcoming-salesforce-site-switch
    type: official-docs
    accessed: 2026-11-27
  - id: s5
    title: "Admin Release Countdown: Get Ready for Winter '27"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2026/admin-winter-27-release-countdown
    type: official-blog
    accessed: 2026-11-27
created: 2026-11-27
---

# Planned Maintenance Windows

Salesforce runs a shared, multitenant service, so customers don't choose when their org is patched or upgraded. Instead Salesforce publishes **preferred maintenance windows**: recurring, region-specific time slots in which it performs system maintenance, major release upgrades and patch releases on each instance. The schedule is published for planning only and Salesforce can change it at its discretion.[^s1] Knowing your instance's windows lets admins avoid scheduling go-lives, data loads or batch jobs on top of them.

## Three kinds of maintenance

**System maintenance** covers infrastructure work such as instance refreshes. For core Salesforce it is scheduled, whenever possible and only when needed, on the first and third weekends of a month; if a month starts on a Sunday, the first and third full weekends are used.[^s1] Each instance group has a fixed four-hour slot in Pacific Time. Most NA and CS instances use Saturday 7:00–11:00 p.m. PT, a named set of NA instances and US commercial Hyperforce use Sunday 12:00–4:00 a.m. PT, European Hyperforce regions use Saturday 2:00–6:00 p.m. PT, and Asia-Pacific Hyperforce regions use a Saturday morning PT slot. Instances that share infrastructure may occasionally move to a neighbouring window.[^s1]

**Release maintenance** applies the three seasonal major releases. Sandboxes are upgraded first, roughly 4–6 weeks before production, and production dates are published up to a year ahead on the Trust status site.[^s2] For Winter '27, Salesforce told admins that sandbox preview began August 28 and that production orgs received the release across September 4, October 2 and October 9, depending on instance.[^s5]

**Patch and daily releases** fix issues between major releases. Patches are scheduled weekly, usually on Tuesday, Wednesday or Thursday with Asia-Pacific a day later, and daily releases ship as needed on any day; both are typically deployed without downtime where possible.[^s1]

## What users experience

During many system maintenance windows customers keep read-only access to their data rather than losing access entirely.[^s1] Planned instance refreshes and site switches put an org in read-only mode for part of the window, and Apex callouts can still run then, so code that calls out and then performs DML should check `System.getApplicationReadWriteMode()` before writing.[^s3] Depending on the availability status posted for a maintenance, an org may instead be completely unavailable, which matters for integrations such as Heroku Connect that write back to Salesforce.[^s4]

Major releases are lighter. On Hyperforce each production release runs in a 30-minute window announced 60 days ahead, needs no downtime, and simply prompts online users to log in again; on first-party infrastructure the instance is unavailable for up to five minutes. In both cases feature enablement completes within 24 hours of the window.[^s1]

## Notification timeline

Trust Notifications go out when a system maintenance schedule is posted and 10 days before maintenance that affects a whole instance, then at its start and end; about a week ahead a login pop-up also shows the dates.[^s1] For major releases, Salesforce emails release dates two months before production upgrades and posts release notes about a month before.[^s1] Emergency maintenance is the exception: it can be announced less than a week in advance.[^s1]

## Gotchas

- **Windows are per instance, not per org edition.** Look up your instance and its sandboxes separately, because sandboxes and production upgrade on different dates.[^s2]
- **Other clouds keep their own schedules.** Marketing Cloud Engagement, Commerce Cloud, Account Engagement and Heroku have separate windows or notice rules from core Salesforce.[^s1]
- **Plan integrations for read-only periods.** Pausing write-back syncs before a read-only window avoids failed writes that otherwise need retrying.[^s4]

## Connections

Maintenance windows are an operational property of the `kt:salesforce-platform` and are defined per instance, so they depend on `kt:pod-and-instance-architecture`.[^s1] They are announced and tracked on `kt:trust-and-status-site`, and they are when `kt:salesforce-seasonal-releases`, `kt:sandbox-preview` upgrades and `kt:patch-releases` are applied.[^s1][^s2] `kt:instance-refresh-and-org-migration` and `kt:disaster-recovery-and-site-switching` are the system-maintenance operations that most often trigger `kt:read-only-mode`.[^s3][^s4] The node contrasts with `kt:hyperforce`, whose release windows are shorter and downtime-free compared with first-party instances.[^s1]

## Sources
[^s1]: Salesforce Help, "Preferred Salesforce Maintenance Schedule". https://help.salesforce.com/HTViewSolution?id=000176208 (accessed 2026-11-27)
[^s2]: Salesforce Trailhead, "Salesforce Release Process and Transitioning Tips". https://trailhead.salesforce.com/modules/sf_releases/units/sf_releases_start (accessed 2026-11-27)
[^s3]: Salesforce Developers Blog, "Site Switching and Apex Callouts". https://developer.salesforce.com/blogs/2017/10/site-switching-apex-callouts (accessed 2026-11-27)
[^s4]: Heroku Help, "What do I need to do about my upcoming Salesforce site switch?". https://help.heroku.com/GXAW850T/what-do-i-need-to-do-about-my-upcoming-salesforce-site-switch (accessed 2026-11-27)
[^s5]: Salesforce Admins Blog, "Admin Release Countdown: Get Ready for Winter '27". https://admin.salesforce.com/blog/2026/admin-winter-27-release-countdown (accessed 2026-11-27)
