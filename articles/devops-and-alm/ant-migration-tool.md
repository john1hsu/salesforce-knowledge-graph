---
id: kt:ant-migration-tool
type: Tool
title: Ant Migration Tool
aliases: [ANT Migration Tool, ant-salesforce.jar, Salesforce Ant tasks, sf:deploy Ant task]
domain: devops-and-alm
summary: >-
  Salesforce's retired Java/Apache Ant-based command-line utility for retrieving and deploying metadata and Apex
  between a local directory and an org through the Metadata API, driven by build.xml targets and a package.xml
  manifest; retired with Spring '24 in favour of Salesforce CLI.
release: "Winter '27"
status: retired
broader: [kt:application-lifecycle-management]
related: [kt:package-xml-manifest, kt:deployment-validation-and-quick-deploy, kt:continuous-integration-for-salesforce]
relations:
  - {predicate: replacedBy, object: kt:salesforce-cli}
  - {predicate: integratesWith, object: kt:metadata-api}
  - {predicate: alternativeTo, object: kt:change-sets}
  - {predicate: dependsOn, object: kt:apex-testing}
sources:
  - id: s1
    title: "Ant Migration Tool (Salesforce Migration Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/salesforce-migration-guide/guide
    type: official-docs
    accessed: 2026-11-19
  - id: s2
    title: "Deploying Changes to a Salesforce Org (Ant Migration Tool Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.daas.meta/daas/forcemigrationtool_deploy.htm
    type: official-docs
    accessed: 2026-11-19
  - id: s3
    title: "Deploying a Recent Validation (Ant Migration Tool Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.daas.meta/daas/forcemigrationtool_deploy_validation.htm
    type: official-docs
    accessed: 2026-11-19
  - id: s4
    title: "Prerequisites for Using the Ant Migration Tool"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/salesforce-migration-guide/guide/forcemigrationtool-prereq.html
    type: official-docs
    accessed: 2026-11-19
  - id: s5
    title: "Moving on from the Ant Migration Tool to sf CLI (v2)"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/01/moving-on-from-the-ant-migration-tool-to-sf-cli-v2
    type: official-blog
    accessed: 2026-11-19
  - id: s6
    title: "Retrieving Components (Ant Migration Tool Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.daas.meta/daas/forcemigrationtool_retrieve.htm
    type: official-docs
    accessed: 2026-11-19
created: 2026-11-19
---

# Ant Migration Tool

The Ant Migration Tool is a command-line utility, built on Java and Apache Ant, that moves metadata between a local directory and a Salesforce org by calling the Metadata API to retrieve and deploy Apex and other components.[^s1] For more than a decade it was the standard way to script Salesforce deployments outside the browser. Salesforce **retired it with Spring '24**: it keeps working against future API versions, but it receives no new functionality and no support, and features that Ant cannot handle will not be added to it. Salesforce recommends Salesforce CLI for managing metadata changes instead.[^s1][^s2]

## How it works

A project contains a `build.xml` file with named Ant targets and a `package.xml` manifest listing the components to move. The guide's first step is usually `ant retrieveUnpackaged`, which pulls the components named in `package.xml`; `ant -p` lists the available targets, and the sample `build.xml` ships with targets for the various retrieve and deploy options.[^s6] Which package gets deployed is decided by the manifest, not by the target.[^s1] Typical uses were seeding test environments with many setup changes, multistage build-test-release processes, repeatable deployments with the same parameters, scripted promotion from staging to production, and overnight batch deployments.[^s1]

The deploy task points at either a `deployRoot` directory or a `zipFile`, one of which is required.[^s2] Key options include:

- `checkOnly` (default false) validates without saving, so a later deployment can reuse the results without rerunning tests.[^s2]
- `testLevel` picks the tests: `NoTestRun`, `RunSpecifiedTests` (with nested `runTest` elements), `RunLocalTests` or `RunAllTestsInOrg`; it needs API version 34.0 or later.[^s2]
- `rollbackOnError` (default true) rolls back everything on any failure and must stay true for production.[^s2]
- `purgeOnDelete` skips the Recycle Bin for components in `destructiveChanges.xml`, but only in Developer Edition or sandbox orgs.[^s2]
- `maxPoll` (default 200) and `pollWaitMillis` (default 10,000 ms) control polling; a deployment can still succeed after polling stops.[^s2]
- `trace` prints SOAP traffic to the console and exposes the login password in plain text, so keep it out of shared CI logs.[^s2]

A companion task, `sf:deployRecentValidation`, takes a `recentValidationId` and deploys a validation that succeeded for the target within the last 10 days without rerunning tests. It requires that tests passed in that validation and that coverage rules were met (75% overall for all-tests or local-tests runs, or 75% per class and trigger under `RunSpecifiedTests`).[^s3]

## Limits and gotchas

- **Payload limits.** A single retrieve or deploy can carry up to 10,000 files, with a 39 MB zip and 600 MB unzipped; larger sets must be split into batches.[^s2][^s6]
- **Default test levels.** Without an explicit level, development environments run no tests, while production deployments containing Apex default to `RunLocalTests`.[^s2]
- **Java and Ant versions.** Tool versions 51.0 and later need Java 11 or later, and Apache Ant 1.6 or later is required; Java 6 cannot connect because it uses TLS 1.0.[^s4]
- **Credentials in files.** Connection details (`username`, `password`, `sessionId`, `serverurl`) are passed as Ant properties, usually kept in per-org properties files, which the CLI replaces with org aliases.[^s3][^s5]
- **Frozen feature set.** The Developers Blog warns that pipelines still on Ant may break if back-end APIs change, and that metadata types and features after API v59.0 are not supported.[^s5]

## When to use it (and when not)

Do not start new work on the Ant Migration Tool. Its role passes to Salesforce CLI (`sf` v2), which Salesforce describes as the primary tool for Metadata API work.[^s5] The migration path maps fairly directly: `sf project generate manifest --source-dir` builds a `package.xml`, `sf project retrieve preview/start` and `sf project deploy preview/start` replace the Ant targets, org aliases replace per-org properties files, and source-tracked orgs let deploys and retrieves act only on changed metadata.[^s5] Teams with existing Ant pipelines should plan that move before an API change breaks a release rather than after.[^s5]

## Connections

- **Replaced by** `kt:salesforce-cli`: Salesforce's recommended replacement for all metadata deploy and retrieve work.[^s1][^s5]
- **Integrates with** `kt:metadata-api`: every Ant task is a wrapper around Metadata API `retrieve()` and `deploy()` calls, so it inherits that API's file and size limits.[^s2][^s6]
- **Related** `kt:package-xml-manifest`: the manifest decides what a target moves, a pattern Salesforce CLI still supports.[^s1][^s5]
- **Related** `kt:deployment-validation-and-quick-deploy`: `checkOnly` plus `sf:deployRecentValidation` was Ant's form of validate-then-quick-deploy.[^s2][^s3]
- **Depends on** `kt:apex-testing`: test levels and coverage thresholds gate every production deployment the tool makes.[^s2][^s3]
- **Alternative to** `kt:change-sets` and an early building block of `kt:continuous-integration-for-salesforce`: it offered scripted, repeatable, schedulable deployments instead of point-and-click moves.[^s1]

## Sources

[^s1]: Salesforce, "Ant Migration Tool" (Salesforce Migration Guide). https://developer.salesforce.com/docs/platform/salesforce-migration-guide/guide (accessed 2026-11-19)
[^s2]: Salesforce, "Deploying Changes to a Salesforce Org" (Ant Migration Tool Guide). https://developer.salesforce.com/docs/atlas.en-us.daas.meta/daas/forcemigrationtool_deploy.htm (accessed 2026-11-19)
[^s3]: Salesforce, "Deploying a Recent Validation" (Ant Migration Tool Guide). https://developer.salesforce.com/docs/atlas.en-us.daas.meta/daas/forcemigrationtool_deploy_validation.htm (accessed 2026-11-19)
[^s4]: Salesforce, "Prerequisites for Using the Ant Migration Tool". https://developer.salesforce.com/docs/platform/salesforce-migration-guide/guide/forcemigrationtool-prereq.html (accessed 2026-11-19)
[^s5]: Salesforce Developers Blog, "Moving on from the Ant Migration Tool to sf CLI (v2)" (January 2024). https://developer.salesforce.com/blogs/2024/01/moving-on-from-the-ant-migration-tool-to-sf-cli-v2 (accessed 2026-11-19)
[^s6]: Salesforce, "Retrieving Components" (Ant Migration Tool Guide). https://developer.salesforce.com/docs/atlas.en-us.daas.meta/daas/forcemigrationtool_retrieve.htm (accessed 2026-11-19)
