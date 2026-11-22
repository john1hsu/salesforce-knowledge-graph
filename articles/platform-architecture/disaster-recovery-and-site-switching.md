---
id: kt:disaster-recovery-and-site-switching
type: Concept
title: Disaster Recovery and Site Switching
aliases: [site switching, site switch, continuous site switching, Salesforce disaster recovery, Salesforce DR, data center failover]
domain: platform-architecture
summary: >-
  How Salesforce keeps orgs recoverable from a data center or region failure: each instance is kept in two
  geographically separate locations, and Salesforce routinely "site switches" live instances between them, putting
  orgs in read-only mode for part of a maintenance window. On Hyperforce, multi-availability-zone design and an
  optional out-of-region add-on extend the same goal.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform, kt:pod-and-instance-architecture]
related: [kt:instance-refresh-and-org-migration, kt:trust-and-status-site, kt:hyperforce, kt:apex-callouts, kt:heroku-connect, kt:planned-maintenance-windows]
relations:
  - {predicate: contrastsWith, object: kt:backup-and-recover}
  - {predicate: dependsOn, object: kt:read-only-mode}
sources:
  - id: s1
    title: "6 Ways We Deliver on Our Promise of Availability and Performance"
    publisher: Salesforce Engineering
    url: https://engineering.salesforce.com/6-ways-we-deliver-on-our-promise-of-availability-and-performance-123dc0e45b2d
    type: official-blog
    accessed: 2026-11-22
  - id: s2
    title: "Site Switching and Apex Callouts"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2017/10/site-switching-apex-callouts
    type: official-blog
    accessed: 2026-11-22
  - id: s3
    title: "DR Summary and Testing - Salesforce Services on First Party"
    publisher: Salesforce Compliance Site
    url: https://compliance.salesforce.com/en/documents/a005A00000k4ayhQAA
    type: official-docs
    accessed: 2026-11-22
  - id: s4
    title: "Architectural Principles for High Availability on Hyperforce"
    publisher: Salesforce Engineering
    url: https://engineering.salesforce.com/?p=5400
    type: official-blog
    accessed: 2026-11-22
  - id: s5
    title: "What do I need to do about my upcoming Salesforce site switch?"
    publisher: Heroku Help (Salesforce)
    url: https://help.heroku.com/GXAW850T/what-do-i-need-to-do-about-my-upcoming-salesforce-site-switch
    type: official-docs
    accessed: 2026-11-22
  - id: s6
    title: "Salesforce Out of Region Disaster Recovery data sheet"
    publisher: Salesforce
    url: https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/platform/Salesforce-out-of-region-disaster-recovery-data-sheet.pdf
    type: official-docs
    accessed: 2026-11-22
created: 2026-11-22
---

# Disaster Recovery and Site Switching

Disaster recovery (DR) on Salesforce is something the platform does for every customer, not something an admin configures. Salesforce keeps two copies of each customer's systems and services in two geographically diverse locations, so that if one data center suffers a disaster, user traffic can be directed to a completely separate data center in a different region.[^s1] Moving a live instance from its active site to its standby site is called a **site switch**, and Salesforce runs these regularly rather than waiting for a real disaster, alongside related operations such as org migrations and instance refreshes.[^s1]

## How site switching works

Salesforce describes the practice as continuous site switching: switching instances routinely lets it improve operations and infrastructure and helps meet the compliance requirements of many customers.[^s2] A planned site switch, like an instance refresh, puts the org in read-only mode for a portion of the instance's preferred maintenance window.[^s2] Depending on the availability status published with the maintenance on status.salesforce.com, the org is either read-only or completely unavailable during the switch.[^s5]

Salesforce documents the exercises for auditors and customers. Its compliance site publishes a "DR Summary and Testing" report for services on first-party infrastructure that summarizes recent site-switching exercises and their results, refreshed for six-month reporting periods (for example February to July 2026).[^s3] Separate DR summaries cover Salesforce services on Hyperforce and other offerings such as Heroku and MuleSoft.[^s3]

## Disaster recovery on Hyperforce

On Hyperforce, resilience starts inside a single public-cloud region. Each region contains multiple availability zones (AZs), which act as fault domains, and Hyperforce services are usually deployed across three of them.[^s4] Most services run active across AZs; single-primary transactional databases fail over automatically to a standby in a healthy AZ after a brief failover, during which in-flight requests may fail and need a retry.[^s4] The stated design goal is to survive the loss of a whole AZ plus one more component failure in another AZ ("AZ+1"), with a 99.99% availability objective.[^s4] The same post defines recovery time objective (RTO) and recovery point objective (RPO) as the measures DR plans are judged by, but publishes no numeric values for them.[^s4]

For a failure of an entire region, Salesforce sells **Out of Region Disaster Recovery**, powered by Hyperforce. It replicates the customer's instance from its primary region to a secondary geographic location and, after a regional disruption, Salesforce switches the org to the backup instance there.[^s6]

## Gotchas for practitioners

- **Plan for read-only mode.** Apex callouts keep running while the org is read-only, but any DML after the callout fails.[^s2]
- **Check the mode in code.** `System.getApplicationReadWriteMode()` returns `READ_ONLY` when the org or its instance is read-only, so integrations can defer writes.[^s2]
- **Pause write-back integrations.** Heroku Connect retries writes during a read-only switch, and Heroku recommends pausing connections with read-write mappings for the maintenance.[^s5]

## Connections

Site switching is one of the maintenance operations of the `kt:salesforce-platform` and acts on the instances described in `kt:pod-and-instance-architecture`.[^s1] It sits beside `kt:instance-refresh-and-org-migration`, which also puts orgs in read-only mode during a maintenance window, and both are announced through `kt:trust-and-status-site` within `kt:planned-maintenance-windows`.[^s2][^s5] Its behavior depends on `kt:read-only-mode`, which shapes how `kt:apex-callouts` and `kt:heroku-connect` must be written.[^s2][^s5] On `kt:hyperforce`, AZ failover and the out-of-region add-on extend the same model.[^s4][^s6] Out of Region DR keeps a standby copy of a whole instance for failover after a regional disruption, which is a different job from `kt:backup-and-recover`, the customer-run product for backing up and restoring org data.[^s6]

## Sources

[^s1]: Salesforce Engineering, "6 Ways We Deliver on Our Promise of Availability and Performance". https://engineering.salesforce.com/6-ways-we-deliver-on-our-promise-of-availability-and-performance-123dc0e45b2d (accessed 2026-11-22)
[^s2]: Salesforce Developers Blog, "Site Switching and Apex Callouts". https://developer.salesforce.com/blogs/2017/10/site-switching-apex-callouts (accessed 2026-11-22)
[^s3]: Salesforce Compliance Site, "DR Summary and Testing - Salesforce Services on First Party". https://compliance.salesforce.com/en/documents/a005A00000k4ayhQAA (accessed 2026-11-22)
[^s4]: Salesforce Engineering, "Architectural Principles for High Availability on Hyperforce". https://engineering.salesforce.com/?p=5400 (accessed 2026-11-22)
[^s5]: Heroku Help, "What do I need to do about my upcoming Salesforce site switch?". https://help.heroku.com/GXAW850T/what-do-i-need-to-do-about-my-upcoming-salesforce-site-switch (accessed 2026-11-22)
[^s6]: Salesforce, "Salesforce Out of Region Disaster Recovery data sheet". https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/platform/Salesforce-out-of-region-disaster-recovery-data-sheet.pdf (accessed 2026-11-22)
