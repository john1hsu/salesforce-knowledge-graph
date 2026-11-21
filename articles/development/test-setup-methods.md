---
id: kt:test-setup-methods
type: Feature
title: Test Setup Methods
aliases: ["@TestSetup", TestSetup annotation, test setup method, testSetup]
domain: development
summary: >-
  Apex methods annotated with @TestSetup that run once at the start of a test class to create records shared by
  every test method in it, with each method's changes rolled back so the next one starts from the same data.
release: "Winter '27"
status: current
broader: [kt:apex-testing]
related: [kt:test-data-factory, kt:test-loaddata, kt:testing-strategy]
relations:
  - {predicate: contrastsWith, object: kt:seealldata}
  - {predicate: consumedBy, object: kt:apex}
  - {predicate: dependsOn, object: kt:transaction-control}
sources:
  - id: s1
    title: "Apex Developer Guide (Winter '27): Using Test Setup Methods"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_testing_testsetup_using.htm
    type: official-docs
    accessed: 2026-11-21
  - id: s2
    title: "Apex Developer Guide (Winter '27): TestSetup Annotation"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_classes_annotation_testsetup.htm
    type: official-docs
    accessed: 2026-11-21
  - id: s3
    title: "Apex Testing: Prepare for Unit Testing — Get Data for Your Tests"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/apex-testing-prepare-for-unit-testing/get-data-for-your-tests
    type: official-learning
    accessed: 2026-11-21
  - id: s4
    title: "Advanced Apex Testing — Generate Data for Tests"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/unit-testing-on-the-lightning-platform/generate-data-for-tests
    type: official-learning
    accessed: 2026-11-21
created: 2026-11-21
---

# Test Setup Methods

A **test setup method** is a method in an Apex test class marked with the `@TestSetup` annotation. It creates the common records that the class's test methods need, so each test does not have to build the same fixture itself.[^s1][^s2] The method is declared as `@TestSetup static void methodName() {}`: it is static, takes no arguments and returns nothing.[^s2] The Winter '27 (API version 68.0) Apex Developer Guide documents the feature in both its testing chapter and its annotation reference.[^s1][^s2]

## How it works

When the class runs, the test framework executes the setup method first, before any test method.[^s1] The records it inserts are visible to every test method in the class. If one test updates or deletes those records, the change is rolled back when that test finishes, so the next test sees the data exactly as setup left it; all setup records are rolled back at the end of the class.[^s1] Because the fixture is inserted once per class instead of once per method, the guide says the approach can cut test execution time.[^s1]

Each test method, and the setup method itself, runs as its own transaction. The class's static context is reinitialized before each one, so static initializers run again and any static variable set during setup is gone by the time a test method starts.[^s1] Shared state therefore has to live in records, not in static fields.

Setup records are not passed to the test methods: each test still queries for the data it needs.[^s3] Trailhead's worked example inserts an account with five contacts through a factory, adds one more contact in the setup method, and then has the test query and assert six contacts.[^s3][^s4] Both Trailhead units describe the platform as calling setup before individual test methods; read alongside the developer guide, that means each method starts from the setup state, while the inserts themselves happen once.[^s1][^s3][^s4]

## Limits and gotchas

- **One per class.** A test class can contain only one test setup method.[^s1][^s2]
- **Isolation only.** Setup works only in the default data-isolation mode; if the class or any of its methods uses `@IsTest(SeeAllData=true)`, setup methods are not supported in that class.[^s1][^s2]
- **API version.** Because data isolation exists from API version 24.0, test setup methods are only available for classes at 24.0 or later.[^s1][^s2]
- **Fatal errors stop the class.** A DML exception or failed assertion inside setup fails the entire class, and none of its tests run.[^s1]
- **Coverage blind spot.** When setup calls a non-test method in another class, no code coverage is calculated for that method.[^s1]
- **No static carry-over.** Static variables changed in setup are discarded when the setup transaction ends.[^s1]

Trailhead adds that wrapping the code under test in `Test.startTest()` and `Test.stopTest()` gives it a fresh set of governor limits, so fixture work done earlier does not trigger false limit failures.[^s3]

## When to use it (and when not)

Trailhead teaches four ways to get test data: brute-force inserts inside each test, test data factories, `@TestSetup` methods, and CSV files loaded with `Test.loadData`.[^s3][^s4] Setup methods are not an alternative to the others so much as a place to call them: the Trailhead examples call a factory from setup, and also call `Test.loadData` from a setup method to load accounts from a static resource.[^s3] Use setup when several methods in one class need the same baseline records. Keep per-test inserts for data that only one test needs, since a large shared fixture slows every class run and makes it harder to see what each test depends on.[^s3] Trailhead notes that brute-force setup inside each test tends to produce long tests that are hard to follow.[^s3] Org-data access through `SeeAllData=true` is described as not a best practice and is incompatible with setup methods in the same class.[^s1][^s3]

## Connections

Test setup methods are part of **Apex testing**, their broader node, and they rely on that framework's data isolation.[^s1] They usually call a **test data factory** to build records, and **Test.loadData** can be called from them to populate fixtures from CSV files.[^s3] They **contrast with SeeAllData**: one shares data the test created, the other reads data the org already has, and the two cannot be combined in one class.[^s1][^s2] The rule that each method is its own transaction ties them to Apex **transaction control**, which explains why static state does not survive setup.[^s1] They are written in **Apex**, and deciding how much data to share per class is part of a team's **testing strategy**.[^s3]

## Sources

[^s1]: Salesforce Developers, "Apex Developer Guide (Winter '27): Using Test Setup Methods". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_testing_testsetup_using.htm (accessed 2026-11-21)
[^s2]: Salesforce Developers, "Apex Developer Guide (Winter '27): TestSetup Annotation". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_classes_annotation_testsetup.htm (accessed 2026-11-21)
[^s3]: Trailhead, "Apex Testing: Prepare for Unit Testing — Get Data for Your Tests". https://trailhead.salesforce.com/content/learn/modules/apex-testing-prepare-for-unit-testing/get-data-for-your-tests (accessed 2026-11-21)
[^s4]: Trailhead, "Advanced Apex Testing — Generate Data for Tests". https://trailhead.salesforce.com/content/learn/modules/unit-testing-on-the-lightning-platform/generate-data-for-tests (accessed 2026-11-21)
