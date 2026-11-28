---
id: kt:apex-hammer-test
type: Concept
title: Apex Hammer Test
aliases: [The Hammer, Apex Hammer, Hammer testing, Hammertime]
domain: devops-and-alm
summary: >-
  Salesforce's internal pre-release regression process that runs customers' Apex tests twice, on the current production
  version and on the upcoming release candidate, and compares the results to catch platform changes that would break
  customer code before the seasonal upgrade.
release: "Winter '27"
status: concept
broader: [kt:salesforce-seasonal-releases, kt:testing-strategy]
related: [kt:apex-testing, kt:seealldata, kt:sandbox-preview, kt:release-updates, kt:release-management]
relations:
  - {predicate: dependsOn, object: kt:apex-testing}
  - {predicate: contrastsWith, object: kt:user-acceptance-testing}
sources:
  - id: s1
    title: "Here Comes the Hammer"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2013/05/here-comes-the-hammer
    type: official-blog
    accessed: 2026-11-28
  - id: s2
    title: "Apex Developer Guide: Isolation of Test Data from Organization Data in Unit Tests"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/pages/apex_testing_data_access.htm
    type: official-docs
    accessed: 2026-11-28
  - id: s3
    title: "Plan Testing for Salesforce New Features (Advanced Salesforce Release Readiness Strategies)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/advanced-salesforce-release-readiness-strategies/test-new-features-before-a-release
    type: official-learning
    accessed: 2026-11-28
created: 2026-11-28
---

# Apex Hammer Test

The Apex Hammer Test, usually just "the Hammer", is the name Salesforce engineers gave to an internal regression process run before each seasonal release. Customers' existing Apex tests are executed twice, once on the version currently in production and once on the release candidate, and the two sets of results are compared. A test that passes on one version should pass on the other; a test that fails should fail on both, at the same point. Any difference flags a possible platform regression for engineers to investigate before customers are upgraded.[^s1] It is a Salesforce-side process, not a feature that admins configure, which is why this node is modelled as a concept rather than a Setup feature.

## How it works

The Salesforce Developers Blog described the process in 2013. The Hammer runs in the gap between the internal release freeze and the sandbox release, a window the author nicknamed "Hammertime". Because Salesforce staff may not view customer data, the runs happen inside Salesforce's secure data centres, and engineers compare test outcomes rather than reading customers' debug logs.[^s1] The post put the scale at over 60 million tests, each run twice, within a few weeks before sandboxes received the new release, and it noted that Visualforce, packaging, Trialforce and dashboards go through a similar comparison.[^s1] For the release just completed, it reported that the runs surfaced dozens of potential regressions that were fixed before the upgrade. The figures belong to that release and are not current numbers.[^s1]

The purpose is Salesforce's upgrade promise. Salesforce upgrades orgs three times a year and commits that customer customisations keep working. The Hammer lets it check that promise against real customer code rather than only its own test suites.[^s1] Current Trailhead release-readiness training makes the same point from the customer side: Salesforce product teams do thorough regression testing, so most existing functionality should keep working after a release, and customers should spend their own testing on new features and their custom code.[^s3]

## Why your tests matter to it

Coverage alone helps here. The blog's answer to "why require coverage without assertions?" is that running the code is enough for the Hammer to see whether its behaviour changes between versions. Code with no test coverage cannot be checked at all, and the post names uncovered code and unpredictable web service callouts as things that slip through.[^s1]

Test data design also matters. Tests that use `SeeAllData=true` need access to live org data, which makes Hammer runs slower and more complex. Data-silo tests (`SeeAllData=false`) create their own records, and the post calls them faster and more reliable to run.[^s1] The Apex Developer Guide makes isolation the default: since API version 24.0, test methods can see only the data they create, apart from setup objects such as User, Profile, RecordType and ApexClass. Salesforce recommends creating test data in each test rather than turning on SeeAllData.[^s2] A suite built that way gives the Hammer, and your own pipeline, deterministic results that do not depend on whatever records happen to exist in production.[^s2]

## Limits and gotchas

- The Hammer only finds differences in behaviour your tests exercise; untested paths and external callouts are outside its reach.[^s1]
- It does not replace customer testing. Trailhead advises testing in a sandbox upgraded to the new release before production gets it, including release updates and new features that affect users.[^s3]
- Data-silo tests have their own quirks. For example, Owner relationship fields queried across objects return null, and record IDs should not be shared between test data and org data.[^s2]
- The published scale and defect counts date from 2013. Treat them as an illustration of the process, not as current statistics.[^s1]

## Connections

The Hammer belongs under **Salesforce seasonal releases**, since it runs once per release before the sandbox upgrade, and under **testing strategy**, as the platform-side half of release regression testing.[^s1][^s3] It **depends on** **Apex testing**: its only input is the customer's Apex test suite, so test coverage and assertions decide what it can catch.[^s1] It is closely tied to the **SeeAllData annotation**, because isolated tests make Hammer runs faster and more reliable.[^s1][^s2] For customers, the follow-on steps are **sandbox preview** and **release updates**, where teams test the new release and pending behaviour changes in their own orgs, and they sit inside **release management**.[^s3] It **contrasts with** **user acceptance testing**: the Hammer is automated and run by Salesforce on code, while UAT is run by the customer's users against business processes.[^s3]

## Sources
[^s1]: Salesforce Developers Blog, "Here Comes the Hammer". https://developer.salesforce.com/blogs/2013/05/here-comes-the-hammer (accessed 2026-11-28)
[^s2]: Salesforce Developers, "Apex Developer Guide: Isolation of Test Data from Organization Data in Unit Tests". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/pages/apex_testing_data_access.htm (accessed 2026-11-28)
[^s3]: Trailhead, "Plan Testing for Salesforce New Features". https://trailhead.salesforce.com/content/learn/modules/advanced-salesforce-release-readiness-strategies/test-new-features-before-a-release (accessed 2026-11-28)
