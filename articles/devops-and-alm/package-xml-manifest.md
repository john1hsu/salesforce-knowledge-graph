---
id: kt:package-xml-manifest
type: Feature
title: package.xml Manifest
aliases: [package.xml, project manifest, Metadata API manifest, destructiveChanges.xml]
domain: devops-and-alm
summary: >-
  The XML project manifest that tells the Metadata API (and Salesforce CLI) which metadata components, grouped by
  type, to retrieve or deploy, with companion destructiveChanges manifests that list components to delete.
release: "Winter '27"
status: current
broader: [kt:metadata-api]
related: [kt:change-sets, kt:source-tracking, kt:unlocked-packages, kt:apex-testing]
relations:
  - {predicate: partOf, object: kt:metadata-api}
  - {predicate: configuredVia, object: kt:salesforce-cli}
  - {predicate: alternativeTo, object: kt:source-tracking}
sources:
  - id: s1
    title: "Constructing a Project Manifest (Ant Migration Tool Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.daas.meta/daas/daas_package.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s2
    title: "Step 2: Build a Package.xml Manifest (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta.%20%20/api_meta/meta_quickstart_retrieve_build_manifest.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s3
    title: "Deleting Components from an Organization (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_deploy_deleting_files.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s4
    title: "project generate manifest (Salesforce CLI Command Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_project_generate_manifest.html
    type: official-docs
    accessed: 2026-11-09
  - id: s5
    title: "Deploy Metadata Using the Manifest"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/package-xml/package-xml-deploy
    type: official-learning
    accessed: 2026-11-09
  - id: s6
    title: "Metadata (Metadata API Developer Guide, Metadata Types)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/metadata.htm
    type: official-docs
    accessed: 2026-11-09
created: 2026-11-09
---

# package.xml Manifest

A `package.xml` file is the project manifest for file-based Metadata API work: it lists the metadata components to pull from or push to an org in a single retrieve or deploy request, and only one such package can be retrieved or deployed at a time.[^s1] It is the selective alternative to moving a whole project, which is useful for a quick change to a few components, though Trailhead cautions that it is not a substitute for package development when shipping entire apps.[^s5]

## How it works

The file has a `<Package>` root in the Metadata API namespace. Inside it, each `<types>` block pairs one `<name>` (the metadata type, such as `CustomObject` or `Profile`) with one or more `<members>` entries naming components by their full name, and a closing `<version>` element sets the Metadata API version.[^s1][^s2] An optional `<fullName>` names a server-side package to deploy into; without it, components land in the `unpackaged` package, and it is ignored on retrieve.[^s1] When deploying, every file in the payload must use the same API version as the manifest.[^s1] In Winter '27 the current Metadata API version is 68.0, which is also the version Salesforce's own examples now use.[^s6][^s2]

Members are named by full name. Custom fields are listed under the `CustomField` type in `Object.Field__c` form, and standard and custom objects share the `CustomObject` type, so both go in the same `<types>` block.[^s1] Putting `*` in `<members>` selects every component of a type, but some components, standard objects among them, do not honour the wildcard and must be listed one by one.[^s2] Each type's page in the Metadata Types reference has a section stating whether that type supports the wildcard in `package.xml`.[^s6]

## Deleting metadata: destructive changes

Deletions use a separate manifest with the same format, `destructiveChanges.xml`, deployed alongside a `package.xml` that lists no components but still supplies the API version; wildcards are not allowed in a destructive manifest.[^s3] Since API 33.0 you can choose ordering: `destructiveChangesPre.xml` deletes before additions and updates, while `destructiveChangesPost.xml` deletes afterwards (but before tests run), which suits cases such as editing an Apex class to drop a reference to a custom object and then deleting that object.[^s3] Setting `purgeOnDelete` skips the Recycle Bin.[^s3]

## Generating and using it with Salesforce CLI

Hand-writing manifests is error-prone, so `sf project generate manifest` builds one from local source (`--source-dir`), from named types or components (`--metadata`), or from an org (`--from-org`), and its `--type` flag emits `destructiveChanges.xml`, `destructiveChangesPre.xml` or `destructiveChangesPost.xml` instead of the default `package.xml`.[^s4] When building from an org, managed and unlocked package metadata is excluded unless `--include-packages` is set, and `--excluded-metadata` drops whole types.[^s4] A manifest is then passed to deploy with the `-x` flag, for example `sf project deploy start -x ./package.xml`, so only the listed components move.[^s5]

## Limits and gotchas

- A retrieve or deploy defaults to a 10,000-file limit, and Apex tests run during deployment add time; scoping the manifest tightly helps with both.[^s5]
- Standard objects and fields on them are never pulled in implicitly; name them explicitly.[^s1]
- In a destructive deploy, missing components do not stop the rest from being attempted, and a custom object or page tied to an active Lightning page cannot be deleted until its action override is deactivated.[^s3]
- After deleting Apex classes or triggers, run all local tests to find lingering references.[^s3]
- The Ant Migration Tool that popularised `package.xml` was retired with Spring '24; Salesforce CLI is the recommended tool.[^s1]

## Connections

The manifest is **part of** `kt:metadata-api`: it is the file that scopes each file-based deploy or retrieve.[^s2] It is **configured via** `kt:salesforce-cli`, which generates manifests and accepts them on deploy and retrieve.[^s4][^s5] It is an **alternative to** `kt:source-tracking`, which works out changed components automatically instead of from an explicit list, and it is **related** to `kt:change-sets`, the click-based way to choose components, and to `kt:unlocked-packages`, which Trailhead points to for whole-app delivery.[^s5] It is **related** to `kt:apex-testing` because tests run inside deployments, including after post-destructive deletions.[^s3]

## Sources

[^s1]: Salesforce Developers, "Constructing a Project Manifest". https://developer.salesforce.com/docs/atlas.en-us.daas.meta/daas/daas_package.htm (accessed 2026-11-09)
[^s2]: Salesforce Developers, "Step 2: Build a Package.xml Manifest". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta.%20%20/api_meta/meta_quickstart_retrieve_build_manifest.htm (accessed 2026-11-09)
[^s3]: Salesforce Developers, "Deleting Components from an Organization". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_deploy_deleting_files.htm (accessed 2026-11-09)
[^s4]: Salesforce Developers, "project generate manifest". https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_project_generate_manifest.html (accessed 2026-11-09)
[^s5]: Trailhead, "Deploy Metadata Using the Manifest". https://trailhead.salesforce.com/content/learn/modules/package-xml/package-xml-deploy (accessed 2026-11-09)
[^s6]: Salesforce Developers, "Metadata" (Metadata Types). https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/metadata.htm (accessed 2026-11-09)
