---
id: kt:field-audit-trail
type: Feature
title: Field Audit Trail
aliases: [FAT, field history retention, field history archive, Shield Field Audit Trail]
domain: security-and-sharing
summary: >-
  Salesforce Shield component (also sold separately) that extends Field History Tracking to up to 200 fields per
  object and keeps archived field history in the FieldHistoryArchive big object until it is explicitly deleted,
  under per-object retention policies deployed through Metadata API.
release: "Winter '27"
status: current
broader: [kt:salesforce-shield]
related: [kt:shield-platform-encryption, kt:event-monitoring, kt:archiving-strategy, kt:tooling-api, kt:security-compliance-frameworks]
relations:
  - {predicate: dependsOn, object: kt:field-history-tracking}
  - {predicate: dependsOn, object: kt:big-objects}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: requiresLicense, object: kt:salesforce-shield}
  - {predicate: coveredBy, object: kt:platform-data-architect-certification}
sources:
  - id: s1
    title: "Field Audit Trail — Field History Retention Implementation Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/field-history-retention/guide/field-audit-trail.html
    type: official-docs
    accessed: 2026-11-06
  - id: s2
    title: "Metadata: HistoryRetentionPolicy"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/field-history-retention/guide/field-history-meta-historyretentionpolicy.html
    type: official-docs
    accessed: 2026-11-06
  - id: s3
    title: "Delete Field History and Field Audit Trail Data"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/field-history-retention/guide/field-history-delete.html
    type: official-docs
    accessed: 2026-11-06
  - id: s4
    title: "Tooling: HistoryRetentionJob"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/field-history-retention/guide/field-history-tooling-api-objects-historyretentionjob.html
    type: official-docs
    accessed: 2026-11-06
  - id: s5
    title: "Configure Field Audit Trail"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/field-audit-trail-basics/configure-field-audit-trail
    type: official-learning
    accessed: 2026-11-06
  - id: s6
    title: "Protect Apps with Shield"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/secure-salesforce-configuration/protect-apps-with-shield
    type: official-learning
    accessed: 2026-11-06
created: 2026-11-06
---

# Field Audit Trail

Field Audit Trail (FAT) is the compliance-grade layer on top of standard field history. It lets an org reconstruct what a record looked like on any past date, which supports regulatory audits, internal governance and customer-service investigations.[^s6] It is one of the four Shield components, alongside Platform Encryption, Event Monitoring and Data Detect, and can also be bought as a standalone licence for Enterprise, Performance and Unlimited Editions; Salesforce enables it on request, and it works in Lightning Experience only.[^s1][^s6]

## How it works

FAT does not capture changes on its own. An admin first switches on Field History Tracking for the object and picks fields; FAT then raises the per-object ceiling to 200 tracked fields and moves aged history out of the object's history table into `FieldHistoryArchive`, a platform-managed big object.[^s1] Neither the live history nor the archive consumes the org's data storage allocation.[^s1]

Archiving is driven by a **retention policy** defined per object. Once FAT is on, Salesforce attaches a default policy to every supported object; a custom policy is declared as a `historyRetentionPolicy` element inside the object's metadata and deployed through Metadata API, and it can ship in managed or unmanaged packages. Only custom policies come back when you retrieve metadata.[^s1][^s2] The policy has four settings:[^s2]

- `archiveAfterMonths` (required, 1–18, default 18): how long rows stay in the history related list before being copied to the archive.[^s2]
- `archiveRetentionYears`: how long archived rows should be kept. It is a reminder only; nothing is deleted automatically.[^s2]
- `gracePeriodDays` (0–10, default 1): applies only to the first archive run.[^s2]
- `description`: free text.[^s2]

The first copy after a policy is deployed sweeps all qualifying history and can be slow; later runs move only the delta since the previous copy.[^s1] The copy leaves the original rows in place, so the in-platform history can be deleted separately once archived.[^s4] Admins can also work through the Shield Home setup pages, where the Trailhead walkthrough sets Archive After and Grace Period on the object and then inspects results with Field History Explorer.[^s5]

## Monitoring and deleting

Each archive run is visible through the Tooling API object `HistoryRetentionJob`, which records the cutoff date, start time, duration, number of rows retained and a status such as CopyRunning, CopySucceeded, CopyFailed or NothingToArchive (with matching Delete statuses).[^s4] Archived data is read through the API only; there is no UI view of the big object.[^s1]

Removing archived rows is deliberate and API-driven. Users need the Delete From Field History and Delete From Field History Archive permissions; live history rows are removed with Apex or SOAP `delete()`, while archive rows require SOAP `deleteByExample()` or Apex `Database.deleteImmediate()`.[^s3] The template record must supply every field in the big object's index; partial indexes, non-indexed fields and wildcards are rejected.[^s3] Deleting a production record removes its live history but not its archived copies, which persist until purged.[^s1]

## Limits and gotchas

Verified against Winter '27:

- **Field ceiling inconsistency.** The implementation guide states 200 fields per object, while Trailhead units cite 60 and 50; treat the developer guide as authoritative and confirm your entitlement with Salesforce.[^s1][^s6][^s5]
- **Sandbox default.** The default policy archives after 18 months in production but after one month in sandboxes, so test archive behaviour appears quickly in a sandbox.[^s1]
- **Untrackable fields.** Formula, roll-up summary and auto-number fields, Created By, Last Modified By, long text and multi-select fields cannot be audited.[^s1]
- **Encryption is not retroactive.** Turning on Platform Encryption leaves existing archive data unencrypted until Salesforce re-archives it on request.[^s1]
- **Permission to define policies.** The HistoryRetentionPolicy component requires the RetainFieldHistory permission.[^s2]

## When to use it (and when not)

Choose FAT when a regulation or audit regime requires change history beyond the standard 18–24 month window, or when more than 20 fields per object need auditing.[^s1][^s6] Because `archiveRetentionYears` never purges data, pair it with a scheduled deletion job if your policy also demands that data be destroyed after a period.[^s2][^s3] For reporting-heavy analytics on old history, plan for API extraction, since the archive has no UI.[^s1]

## Connections

FAT is part of **Salesforce Shield** and **requires** its licence or a standalone FAT licence.[^s6][^s1] It **depends on Field History Tracking**, which still decides which fields are captured, and on **big objects**, the storage technology behind the archive.[^s1] Policies are **configured via Metadata API**, archive runs are monitored through the **Tooling API**, and the archive is **queried with SOQL** under big-object index rules.[^s2][^s4][^s1] It sits beside **Shield Platform Encryption** (whose coverage of archived data is not automatic) and **Event Monitoring** as Shield's audit pillar, and feeds an org's **archiving strategy** and **compliance frameworks**.[^s1][^s6]

## Sources

[^s1]: Salesforce Developers, "Field Audit Trail". https://developer.salesforce.com/docs/platform/field-history-retention/guide/field-audit-trail.html (accessed 2026-11-06)
[^s2]: Salesforce Developers, "Metadata: HistoryRetentionPolicy". https://developer.salesforce.com/docs/platform/field-history-retention/guide/field-history-meta-historyretentionpolicy.html (accessed 2026-11-06)
[^s3]: Salesforce Developers, "Delete Field History and Field Audit Trail Data". https://developer.salesforce.com/docs/platform/field-history-retention/guide/field-history-delete.html (accessed 2026-11-06)
[^s4]: Salesforce Developers, "Tooling: HistoryRetentionJob". https://developer.salesforce.com/docs/platform/field-history-retention/guide/field-history-tooling-api-objects-historyretentionjob.html (accessed 2026-11-06)
[^s5]: Trailhead, "Configure Field Audit Trail". https://trailhead.salesforce.com/content/learn/modules/field-audit-trail-basics/configure-field-audit-trail (accessed 2026-11-06)
[^s6]: Trailhead, "Protect Apps with Shield". https://trailhead.salesforce.com/content/learn/modules/secure-salesforce-configuration/protect-apps-with-shield (accessed 2026-11-06)
