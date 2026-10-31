---
id: kt:apex-testing
type: Feature
title: Apex Testing
aliases: [Apex unit tests, Apex test classes, Apex code coverage, IsTest annotation, Salesforce 75% code coverage rule]
domain: development
summary: >-
  The built-in Apex unit-testing framework — @IsTest classes and methods, isolated test data, Test.startTest/stopTest
  and the Assert class — whose passing tests and 75% code coverage are required before Apex can be deployed to production
  or packaged for AppExchange.
release: "Winter '27"
status: current
broader: [kt:apex]
related: [kt:apex-triggers, kt:asynchronous-apex, kt:testing-strategy, kt:metadata-api]
relations:
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: enables, object: kt:application-lifecycle-management}
  - {predicate: dependsOn, object: kt:test-data-factory}
sources:
  - id: s1
    title: "Apex Developer Guide (Winter '27): Testing Apex"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_testing_intro.htm
    type: official-docs
    accessed: 2026-10-31
  - id: s2
    title: "Apex Developer Guide (Winter '27): Writing Tests"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_intro_writing_tests.htm
    type: official-docs
    accessed: 2026-10-31
  - id: s3
    title: "Apex Developer Guide (Winter '27): Using Limits, startTest, and stopTest"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_testing_tools_start_stop_test.htm
    type: official-docs
    accessed: 2026-10-31
  - id: s4
    title: "Apex Developer Guide (Winter '27): Isolation of Test Data from Organization Data in Unit Tests"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_testing_data_access.htm
    type: official-docs
    accessed: 2026-10-31
  - id: s5
    title: "Apex Developer Guide (Winter '27): Using Test Setup Methods"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_testing_testsetup_using.htm
    type: official-docs
    accessed: 2026-10-31
  - id: s6
    title: "Trailhead: Apex Testing — Test Apex Triggers"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/apex_testing/apex_testing_triggers
    type: official-learning
    accessed: 2026-10-31
created: 2026-10-31
---

# Apex Testing

Apex testing is the unit-testing framework built into the Apex language. Test code lives in classes annotated `@IsTest`, runs on the Salesforce platform itself, and is a hard gate on delivery: before Apex can be deployed to production or packaged for AppExchange, unit tests must cover at least 75% of the Apex code and every one of those tests must pass.[^s1][^s2] Salesforce also runs customers' tests in all orgs that contain Apex to check that its own service upgrades have not changed behaviour, so tests protect the org as well as the deployment.[^s1] This article was verified against the Apex Developer Guide for Winter '27 (API version 68.0).[^s1]

## How it works

A unit test method is flagged with `@IsTest` and must sit inside a class that is itself annotated `@IsTest`. The older `testMethod` keyword is equivalent, but Salesforce recommends the annotation because the keyword may be versioned out. Test methods take no arguments, commit no data to the database and send no email.[^s2]

**Data isolation.** Since API version 24.0, test methods cannot see pre-existing org records — standard objects, custom objects or custom settings — only the data they create. A handful of setup-style objects such as User, Profile, Organization, RecordType and ApexClass remain visible. Annotating a class or method with `@IsTest(SeeAllData=true)` lifts the restriction, but Salesforce recommends creating test data inside each test wherever possible. The isolation applies to everything running in test context, including triggers.[^s4]

**Shared setup.** A single static, argument-less `@TestSetup` method per class runs once before the test methods and creates records they all share. Changes a test method makes to those records are rolled back when that method ends, so each method sees the original data, and everything is rolled back when the class finishes. Each method, including setup, is its own transaction, so static variables set during setup do not carry over.[^s5]

**Limits and async boundaries.** `Test.startTest()` marks where the code under test begins and gives it a fresh set of governor limits; `Test.stopTest()` restores the original context. Each may be called only once per test method. Asynchronous work enqueued after `startTest` is collected and then executed synchronously at `stopTest`, which is how tests verify future, Queueable and batch jobs.[^s3] The Trailhead pattern wraps the action that fires a trigger in this block so that data-setup usage does not count against the test, then checks outcomes with `Assert` methods such as `Assert.areEqual` and `Assert.isTrue`.[^s6]

## Limits and gotchas

- **What coverage counts.** Calls to `System.debug`, test methods and test classes are excluded from coverage; every trigger must have some coverage, and all classes and triggers must compile.[^s1][^s2]
- **All local tests run on deploy.** For production deployments every unit test in the org namespace runs by default.[^s2]
- **Percentage is not the goal.** Salesforce advises covering positive and negative cases and both single-record and bulk scenarios rather than chasing 75%; code invoked via SOAP API or a standard set controller can receive up to 200 records at a time.[^s1][^s6]
- **startTest is once-only.** The limit reset adds a context rather than resetting everything: after `stopTest`, code again draws on the limits consumed before `startTest`.[^s3]
- **Async failures cut processing short.** An unhandled exception during `stopTest` halts the synchronous replay — for example, a failing batch `execute` prevents `finish` from running in test context.[^s3]
- **Setup restrictions.** `@TestSetup` is unsupported in any class that uses `SeeAllData=true`, and a fatal error in setup fails the whole class.[^s5]
- **Data you cannot fake.** Records that depend on committed data, such as field history rows, cannot be created in tests, and `Owner` relationship traversals return null in isolated tests.[^s4]
- **Tooling quirk.** Running a subset of tests in Developer Console may not refresh coverage correctly; use Run All to update it.[^s6]

## When to use it (and when not)

Every Apex class and trigger headed for production needs tests, so the question is how, not whether. Use `@TestSetup` or a test-utility class when several methods need the same records — Trailhead moves data creation into a reusable utility for exactly this reason — and keep `SeeAllData=true` for the rare objects that cannot be created in tests.[^s5][^s6][^s4] Write tests to the cases that matter rather than to the coverage figure: positive, negative, single-record and bulk paths each deserve a test method.[^s1]

## Connections

Apex testing is a feature of **Apex**, its broader node, and is most often exercised against **Apex triggers**, which must each carry some coverage before deployment.[^s1][^s6] Because `startTest`/`stopTest` reset and restore limits, the framework is **governed by** the platform's **governor limits**, and its synchronous replay at `stopTest` is how **asynchronous Apex** gets verified.[^s3] Every production deployment — including those made through the **Metadata API** — must clear the 75%-and-all-passing gate, which makes testing an **enabler** of **application lifecycle management**.[^s2] Reusable record builders — the **test data factory** pattern — are the usual answer to data isolation, and unit tests form one layer of an org-wide **testing strategy**.[^s4][^s6]

## Sources

[^s1]: Salesforce Developers, "Apex Developer Guide (Winter '27): Testing Apex". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_testing_intro.htm (accessed 2026-10-31)
[^s2]: Salesforce Developers, "Apex Developer Guide (Winter '27): Writing Tests". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_intro_writing_tests.htm (accessed 2026-10-31)
[^s3]: Salesforce Developers, "Apex Developer Guide (Winter '27): Using Limits, startTest, and stopTest". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_testing_tools_start_stop_test.htm (accessed 2026-10-31)
[^s4]: Salesforce Developers, "Apex Developer Guide (Winter '27): Isolation of Test Data from Organization Data in Unit Tests". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_testing_data_access.htm (accessed 2026-10-31)
[^s5]: Salesforce Developers, "Apex Developer Guide (Winter '27): Using Test Setup Methods". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_testing_testsetup_using.htm (accessed 2026-10-31)
[^s6]: Salesforce Trailhead, "Apex Testing: Test Apex Triggers". https://trailhead.salesforce.com/content/learn/modules/apex_testing/apex_testing_triggers (accessed 2026-10-31)
