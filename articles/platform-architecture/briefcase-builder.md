---
id: kt:briefcase-builder
type: Tool
title: Briefcase Builder
aliases: [Briefcase, offline briefcase, BriefcaseDefinition, briefcase rules]
domain: platform-architecture
summary: >-
  Setup tool for defining briefcases: rule-based sets of records that are primed onto mobile devices so assigned
  users and groups can work with them offline in the Field Service mobile app and the Salesforce offline mobile experience.
release: "Winter '27"
status: current
broader: [kt:salesforce-mobile-app, kt:field-service-mobile-app]
related: [kt:work-orders, kt:formula-fields, kt:custom-metadata-types]
relations:
  - {predicate: consumedBy, object: kt:field-service-mobile-app}
  - {predicate: dependsOn, object: kt:field-service}
  - {predicate: dependsOn, object: kt:public-groups}
  - {predicate: configuredVia, object: kt:metadata-api}
sources:
  - id: s1
    title: "Mobile and Offline Developer Guide: Build a Briefcase"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.mobile_offline.meta/mobile_offline/dx_onboard_wizard_briefcase.htm
    type: official-docs
    accessed: 2026-11-25
  - id: s2
    title: "Configure Offline Briefcase for Field Service Mobile: Build a Briefcase"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/offline-briefcase/build-a-briefcase
    type: official-learning
    accessed: 2026-11-25
  - id: s3
    title: "Configure Offline Briefcase for Field Service Mobile: Allow Access to Information Offline"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/offline-briefcase/allow-access-to-information-online
    type: official-learning
    accessed: 2026-11-25
  - id: s4
    title: "Configure Offline Briefcase for Field Service Mobile: Optimize a Briefcase with Advanced Rules"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/offline-briefcase/optimize-a-briefcase-with-advanced-rules
    type: official-learning
    accessed: 2026-11-25
  - id: s5
    title: "Metadata API Developer Guide: BriefcaseDefinition"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_briefcasedefinition.htm
    type: official-docs
    accessed: 2026-11-25
  - id: s6
    title: "Mobile and Offline Developer Guide: Considerations for Field Service Mobile App"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.mobile_offline.meta/mobile_offline/considerations_app_sfs.htm
    type: official-docs
    accessed: 2026-11-25
created: 2026-11-25
---

# Briefcase Builder

Briefcase Builder is the Setup tool admins use to decide which records are available offline on mobile devices. A briefcase is a named set of rules that selects records, is assigned to users or groups, and is associated with one or more mobile apps; the device then primes (downloads) those records so they can be viewed and worked on without a connection.[^s1][^s2] The Metadata API describes a briefcase as making selected records available to specific users and groups while offline in the Salesforce Field Service mobile app for iOS and Android, and the offline experience of the Salesforce mobile app also relies on a briefcase for priming.[^s5][^s1]

## How it works

An admin opens Setup, searches for Briefcase Builder and clicks New Briefcase. The wizard asks for a name, then for **briefcase rules**: an object plus filters, combined with filter logic such as "1 OR 2". In Trailhead's example, a rule on Work Order keeps only records with status New or In Progress, which keeps the briefcase lean and cuts sync time.[^s2] The admin then assigns the briefcase to users or public groups (a worker can hold more than one briefcase), selects the apps it applies to, such as the Field Service apps for iOS and Android, and either activates it or saves it inactive. The Run As User tab previews what a given user would receive before activation.[^s2]

Once active, connected devices sync their briefcase in the background, and offline edits are stored on the device and synced back automatically when connectivity returns. Rules can target standard objects such as Work Order and Account and custom objects alike, and filters can use location, record type or any other field.[^s3] Flows that reference briefcase records can run offline.[^s3]

**Advanced rules.** Related object rules pull in records by relationship rather than by filter alone. Trailhead's pattern starts with a top-level rule on Service Resource filtered to the current user, follows the Location lookup, and then brings in Work Orders through a related list, so each technician gets only the work at their location.[^s4] For criteria a filter can't express, a checkbox formula field (for example, comparing the account's billing state with the running user's state) can be used as the filter.[^s4]

**As metadata.** Briefcases deploy as the `BriefcaseDefinition` type (API version 50.0 and later). Each `BriefcaseRule` has a `targetEntity`, filters, `filterLogic`, `queryScope` (Everything, AssignedToMe or Mine), `orderBy`, `recordLimit` and nested `relatedRules` with a relationship field and direction (ParentToChild or ChildToParent).[^s5] The `type` value distinguishes Standard briefcases, HighVolume briefcases with increased capacity for performance priming in the Field Service mobile app, and auto-generated MobileAppSync briefcases.[^s5]

## Limits and gotchas

- `recordLimit` caps one rule at 50,000 matching records, and a rule's results must also fit the 50,000-record maximum across active briefcases. When more records match, `orderBy` decides which are kept.[^s5]
- The AssignedToMe scope works only for the ServiceAppointment object; filters can't use compound fields, and date literals such as TODAY must be uppercase.[^s5]
- A custom metadata type can be a target only in a top-level rule, with one rule per type and no other fields.[^s5]
- Task records added to a briefcase are not primed in the Field Service mobile app; priming shows an error, and the fix is to remove Task from the briefcase.[^s6]
- Briefcase metadata is available only in orgs where Briefcase Builder and Field Service are enabled.[^s5]
- Every record shown on the offline Landing Page must also be in the user's briefcase, because the page uses it for record details.[^s1]

## When to use it (and when not)

Use Briefcase Builder whenever mobile users need predictable offline data: field technicians, inspectors, or sales reps who work in low-coverage areas. Group users by role and give each group only the objects and records it needs, which keeps priming fast.[^s1][^s3] The Field Service app ships with basic offline support for a limited set of records; briefcases replace that guesswork with explicit scope, and Performance Priming builds on briefcases to sync critical changes every five minutes and to download far more records than standard priming.[^s3] If users are always online, a briefcase adds setup and sync overhead without benefit.

## Connections

Briefcase Builder sits under `kt:salesforce-mobile-app` and `kt:field-service-mobile-app`, the two offline clients that prime from it, and it is consumed by the Field Service app.[^s1][^s5] It depends on `kt:field-service` being enabled for its metadata and is assigned through `kt:public-groups`.[^s5][^s2] Briefcases are deployable through `kt:metadata-api` as `BriefcaseDefinition`.[^s5] Typical rule targets include `kt:work-orders`, criteria can come from `kt:formula-fields`, and `kt:custom-metadata-types` can be primed as top-level rules.[^s2][^s4][^s5]

## Sources

[^s1]: Salesforce Developers, "Mobile and Offline Developer Guide: Build a Briefcase". https://developer.salesforce.com/docs/atlas.en-us.264.0.mobile_offline.meta/mobile_offline/dx_onboard_wizard_briefcase.htm (accessed 2026-11-25)
[^s2]: Trailhead, "Configure Offline Briefcase for Field Service Mobile: Build a Briefcase". https://trailhead.salesforce.com/content/learn/modules/offline-briefcase/build-a-briefcase (accessed 2026-11-25)
[^s3]: Trailhead, "Configure Offline Briefcase for Field Service Mobile: Allow Access to Information Offline". https://trailhead.salesforce.com/content/learn/modules/offline-briefcase/allow-access-to-information-online (accessed 2026-11-25)
[^s4]: Trailhead, "Configure Offline Briefcase for Field Service Mobile: Optimize a Briefcase with Advanced Rules". https://trailhead.salesforce.com/content/learn/modules/offline-briefcase/optimize-a-briefcase-with-advanced-rules (accessed 2026-11-25)
[^s5]: Salesforce Developers, "Metadata API Developer Guide: BriefcaseDefinition". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_briefcasedefinition.htm (accessed 2026-11-25)
[^s6]: Salesforce Developers, "Mobile and Offline Developer Guide: Considerations for Field Service Mobile App". https://developer.salesforce.com/docs/atlas.en-us.mobile_offline.meta/mobile_offline/considerations_app_sfs.htm (accessed 2026-11-25)
