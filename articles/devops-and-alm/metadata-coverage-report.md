---
id: kt:metadata-coverage-report
type: Tool
title: Metadata Coverage Report
aliases: [Metadata Coverage report, metadata coverage, Salesforce Metadata Coverage Report]
domain: devops-and-alm
summary: >-
  Salesforce's per-API-version reference table showing, for every metadata type, which deployment and development
  channels support it: Metadata API, source tracking, unlocked packages, 2GP and 1GP managed packages, change sets
  and the Apex Metadata API.
release: "Winter '27"
status: current
broader: [kt:metadata-api, kt:application-lifecycle-management]
related: [kt:source-tracking, kt:unlocked-packages, kt:second-generation-managed-packages, kt:first-generation-managed-packages, kt:change-sets, kt:custom-metadata-types]
sources:
  - id: s1
    title: "Metadata Coverage Report"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/metadata-coverage/
    type: official-docs
    accessed: 2026-11-15
  - id: s2
    title: "Break Up Your Metadata (Unlocked Packages for Customers)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/unlocked-packages-for-customers/break-up-your-metadata
    type: official-learning
    accessed: 2026-11-15
  - id: s3
    title: "Track Changes Between Your Project and Org (Salesforce DX Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-source-tracking.html
    type: official-docs
    accessed: 2026-11-15
  - id: s4
    title: "Supported Metadata Types (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_metadata_supported_types.htm
    type: official-docs
    accessed: 2026-11-15
  - id: s5
    title: "Change Sets"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=changesets.htm
    type: official-docs
    accessed: 2026-11-15
  - id: s6
    title: "Components Available in Second-Generation Managed Packages"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/packaging_packageable_components.htm
    type: official-docs
    accessed: 2026-11-15
created: 2026-11-15
---

# Metadata Coverage Report

The Metadata Coverage Report is a reference page on the Salesforce Developers site that answers one practical question:
can this kind of metadata travel through this channel? It is a large table with one row per metadata type, from
AccessControlPolicy and ApexClass through Flow, Profile, the many `*Settings` types and Territory2. Each row links to
that type's reference page and has a check mark under every channel that supports it.[^s1] Trailhead calls it the
source of truth for metadata coverage across channels, which is why other Salesforce docs point to it rather than
keeping their own lists.[^s2]

## What the columns mean

The report has seven channel columns after the type name:[^s1]

- **Metadata API**: the type can be retrieved and deployed with the Metadata API and the tools built on it.[^s1]
- **Source Tracking**: Salesforce CLI can detect changes to the type in source-tracked orgs.[^s1][^s3]
- **Unlocked Packaging**, **2GP** and **1GP**: the type can go in an unlocked package, a second-generation managed package or a first-generation managed package.[^s1][^s2]
- **ChangeSets**: the type can be added to an outbound change set.[^s1]
- **Apex API**: the type can be read or deployed from Apex through the `Metadata` namespace.[^s1][^s4]

A footnoted check mark (marker 1) means the component can only go in a package that has no namespace. Territory2 is
one example: its last check carries that marker.[^s1]

## Versions

The report is versioned by release. A selector lists Winter '27 (API 68.0) as the latest, with earlier releases going
back to Spring '20 (API 48.0), each at its own versioned URL.[^s1] Coverage changes from release to release, so check
the version that matches the `sourceApiVersion` or package API version you deploy with, not only the latest.[^s1]

## How it is used

- **Source-driven development**: the Salesforce DX guide doesn't list trackable types. It sends you to the report's Source Tracking column instead.[^s3]
- **Package design**: Trailhead notes that almost any metadata can go in an unlocked package and leaves the exceptions to the report.[^s2]
- **Managed packaging**: the 2GP developer guide has its own "Packageable In" notes, but it points to the report to confirm whether a component works in 1GP, 2GP or both.[^s6]
- **Choosing a channel**: change sets carry only changes you can make in Setup, and what they can hold varies by experience and edition. A missing ChangeSets check therefore means you need another channel, such as a CLI deploy or a package.[^s5][^s1]

## Limits and gotchas

- **Apex coverage is narrow.** The Apex Metadata API can reach only custom metadata type records and page layouts, so most rows have no Apex API check.[^s4][^s1]
- **Source tracking needs the org to allow it.** A type can have a Source Tracking check, but tracking still works only in orgs where it is turned on. Elsewhere, deploys and retrieves still work, with no conflict detection, and you name exactly what to move with `--source-dir` or `--metadata`.[^s3]
- **A check mark doesn't mean a clean move.** The report shows that a channel supports a type. It doesn't cover the feature dependencies or edition differences that can still make a change set or package fail.[^s5]
- **Namespace footnotes matter for ISVs.** A footnoted type can't go in a namespaced managed package. It works only in a package without a namespace, such as an unlocked package created without one.[^s1]

## Connections

The report is a companion to the **Metadata API**. It is the coverage view of the types that API exposes, and its
first column is that API itself.[^s1] It belongs to **application lifecycle management** because choosing between
**change sets**, **source tracking** and packages starts with whether the metadata can use that channel.[^s5][^s3]
Its packaging columns map to **unlocked packages**, **second-generation managed packages** and
**first-generation managed packages**, and the packaging docs send readers to it to settle what each can hold.[^s2][^s6]
The Apex API column covers **custom metadata types**, whose records are one of the few things Apex can deploy.[^s4]

## Sources

[^s1]: Salesforce Developers, "Metadata Coverage Report". https://developer.salesforce.com/docs/metadata-coverage/ (accessed 2026-11-15)
[^s2]: Trailhead, "Break Up Your Metadata" (Unlocked Packages for Customers). https://trailhead.salesforce.com/content/learn/modules/unlocked-packages-for-customers/break-up-your-metadata (accessed 2026-11-15)
[^s3]: Salesforce Developers, "Track Changes Between Your Project and Org" (Salesforce DX Developer Guide). https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-source-tracking.html (accessed 2026-11-15)
[^s4]: Salesforce Developers, "Supported Metadata Types" (Apex Developer Guide). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_metadata_supported_types.htm (accessed 2026-11-15)
[^s5]: Salesforce Help, "Change Sets". https://help.salesforce.com/apex/HTViewHelpDoc?id=changesets.htm (accessed 2026-11-15)
[^s6]: Salesforce Developers, "Components Available in Second-Generation Managed Packages". https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/packaging_packageable_components.htm (accessed 2026-11-15)
