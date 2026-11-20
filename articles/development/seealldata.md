---
id: kt:seealldata
type: Feature
title: SeeAllData Annotation
aliases: [SeeAllData, "@IsTest(SeeAllData=true)", isTest SeeAllData, SeeAllData=true]
domain: development
summary: >-
  The SeeAllData parameter of the Apex @IsTest annotation, which opts a test class or test method out of the default
  data isolation so it can query pre-existing records in the org; Salesforce recommends isolated (SeeAllData=false)
  data silo tests instead.
release: "Winter '27"
status: current
broader: [kt:apex-testing]
related: [kt:test-data-factory, kt:testing-strategy, kt:custom-settings]
relations:
  - {predicate: alternativeTo, object: kt:test-loaddata}
  - {predicate: contrastsWith, object: kt:test-setup-methods}
  - {predicate: consumedBy, object: kt:apex}
sources:
  - id: s1
    title: "Apex Developer Guide (Winter '27): Isolation of Test Data from Organization Data in Unit Tests"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_testing_data_access.htm
    type: official-docs
    accessed: 2026-11-20
  - id: s2
    title: "Apex Developer Guide (Winter '27): Using the isTest(SeeAllData=True) Annotation"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/pages/apex_testing_seealldata_using.htm
    type: official-docs
    accessed: 2026-11-20
  - id: s3
    title: "Apex Developer Guide (Winter '27): Using Test Setup Methods"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_testing_testsetup_using.htm
    type: official-docs
    accessed: 2026-11-20
  - id: s4
    title: "Prepare for Unit Testing: Get Data for Your Tests"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/apex-testing-prepare-for-unit-testing/get-data-for-your-tests
    type: official-learning
    accessed: 2026-11-20
  - id: s5
    title: "Apex Developer Guide (Winter '27): TestSetup Annotation"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_classes_annotation_testsetup.htm
    type: official-docs
    accessed: 2026-11-20
created: 2026-11-20
---

# SeeAllData Annotation

`SeeAllData` is a parameter of the Apex `@IsTest` annotation. Written as `@IsTest(SeeAllData=true)` on a test class or a test method, it switches off the default isolation between test data and the org's existing records, so the annotated code can query records that were already in the org before the test started.[^s2] Without it, test methods saved at API version 24.0 or later see only the records they create themselves, plus a set of org-management and metadata objects such as User, Profile, Organization, RecordType, CronTrigger and the Apex class, trigger, page and component objects.[^s1] The Winter '27 (API 68.0) Apex Developer Guide still documents the parameter, and it still describes isolated tests, which it calls data silo tests, as the recommended approach.[^s2]

## How it works

The parameter widens what a test can read, not what it can keep. Records the test inserts, updates or deletes are still rolled back when the test ends, even when it can see org data.[^s2] Isolation, and so the effect of lifting it, covers all code running in test context: a trigger fired by an isolated test cannot see org records either.[^s1]

Placement follows precedence rules that often surprise developers:[^s2]

- On the class, `SeeAllData=true` applies to every test method that does not set the parameter itself.[^s2]
- On a single method in an unannotated class, it opens org data to that method only; the other methods stay isolated.[^s2]
- A method marked `SeeAllData=false` inside a class marked `true` is ignored, and the method keeps full access.[^s2]
- The reverse does work: a method marked `true` overrides a class marked `false`.[^s2]

Version matters too. Test code saved at API 23.0 or earlier always had access to org data, and the parameter has no effect on it. When a newer test calls a class saved at an older version, the caller's isolation rules apply inside the called code.[^s1] Since API 28.0 the `VLOOKUP` validation-rule function also respects isolation, and looks up org data during a test only when the test uses `SeeAllData=true`.[^s1]

## Limits and gotchas

- **No test setup.** `@TestSetup` methods work only with default isolation; a class in which the class or any method uses `SeeAllData=true` cannot have one.[^s3][^s5]
- **No parallel flag.** `SeeAllData=true` and `IsParallel=true` cannot be combined on the same test method.[^s2]
- **Environment-dependent results.** Each org has its own data, so a test that reads org records can pass in a sandbox and then fail when deployed somewhere that data is missing.[^s4]
- **Some records still cannot be created.** Isolation is not the only obstacle. Duplicate-name errors on objects such as CollaborationGroup occur with or without the parameter, and field history and Chatter tracked-change records cannot be created in tests because tests never commit.[^s1]
- **Owner traversal in silo tests.** In isolated tests, cross-object references through the Owner relationship aren't supported; a query for `Owner.IsActive` on Account returns null.[^s1]
- **Visualforce requests.** A Visualforce request made during a test runs on a separate thread, where isolation isn't enforced.[^s1]

## When to use it (and when not)

Salesforce's guidance is to create test data in each test wherever possible.[^s1] Trailhead calls reading org data not a best practice and explains why: production data changes over time and differs from developer environments, so tests that rely on it are neither repeatable nor portable.[^s4] The usual alternatives are records built in the test or a `@TestSetup` method, often through a factory class, or CSV files loaded from a static resource with `Test.loadData`, which lets the data change without redeploying code.[^s4][^s3]

The annotation still has a narrow use: code paths that depend on data a test cannot create, where isolation would leave nothing to test against.[^s1] Keeping it at method level rather than class level limits how much of a class depends on org state, and lets the class's other methods stay isolated.[^s2] Because the class then can't have a test setup method, isolated methods that share data should go in a separate class.[^s3]

## Connections

The annotation is part of **Apex testing**, its broader node, and an opt-out from that framework's data isolation.[^s1] It contrasts with **test setup methods**, which require isolation and cannot share a class with it, and with the **test data factory** pattern, which builds the isolated records that make the annotation unnecessary.[^s3][^s4] **Test.loadData** is the static-resource **alternative** for supplying predictable data without reading the org.[^s4] **Custom settings** are a frequent reason developers reach for it, since setting records count as org data that isolated tests cannot see.[^s1] The choice between isolated and org-dependent tests belongs to a wider **testing strategy**, because only isolated tests behave the same way in every environment.[^s4]

## Sources

[^s1]: Salesforce Developers, "Apex Developer Guide (Winter '27): Isolation of Test Data from Organization Data in Unit Tests". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_testing_data_access.htm (accessed 2026-11-20)
[^s2]: Salesforce Developers, "Apex Developer Guide (Winter '27): Using the isTest(SeeAllData=True) Annotation". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/pages/apex_testing_seealldata_using.htm (accessed 2026-11-20)
[^s3]: Salesforce Developers, "Apex Developer Guide (Winter '27): Using Test Setup Methods". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_testing_testsetup_using.htm (accessed 2026-11-20)
[^s4]: Trailhead, "Prepare for Unit Testing: Get Data for Your Tests". https://trailhead.salesforce.com/content/learn/modules/apex-testing-prepare-for-unit-testing/get-data-for-your-tests (accessed 2026-11-20)
[^s5]: Salesforce Developers, "Apex Developer Guide (Winter '27): TestSetup Annotation". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_classes_annotation_testsetup.htm (accessed 2026-11-20)
