---
id: kt:test-data-factory
type: Pattern
title: Test Data Factory
aliases: [TestDataFactory, test utility class, Apex test utility classes, test data builder]
domain: development
summary: >-
  An Apex testing pattern in which a public @IsTest utility class exposes reusable methods that build (and optionally
  insert) the records unit tests need, so every test creates its own isolated, predictable data instead of relying on
  org data.
release: "Winter '27"
status: current
broader: [kt:apex-testing]
related: [kt:testing-strategy, kt:bulkification, kt:apex-enterprise-patterns, kt:scratch-orgs]
relations:
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: alternativeTo, object: kt:test-loaddata}
  - {predicate: contrastsWith, object: kt:seealldata}
sources:
  - id: s1
    title: "Apex Developer Guide (Winter '27): Common Test Utility Classes for Test Data Creation"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_testing_utility_classes.htm
    type: official-docs
    accessed: 2026-11-14
  - id: s2
    title: "Apex Developer Guide (Winter '27): Using Test Setup Methods"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_testing_testsetup_using.htm
    type: official-docs
    accessed: 2026-11-14
  - id: s3
    title: "Apex Testing: Create Test Data for Apex Tests"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/apex_testing/apex_testing_data
    type: official-learning
    accessed: 2026-11-14
  - id: s4
    title: "Prepare for Unit Testing: Get Data for Your Tests"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/apex-testing-prepare-for-unit-testing/get-data-for-your-tests
    type: official-learning
    accessed: 2026-11-14
created: 2026-11-14
---

# Test Data Factory

A **test data factory** is a public Apex class annotated with `@IsTest` that holds reusable methods for creating the records unit tests need. Test methods call it to set up accounts, contacts, opportunities or whole related record networks before exercising the code under test. Salesforce documents these as "common test utility classes"; `TestDataFactory` is the conventional class name used in the Apex Developer Guide and on Trailhead.[^s1][^s3]

## How it works

Factory methods are written like any other Apex methods: they take parameters and return values, and they must be `public` or `global` so other test classes can see them. The guide's example takes an account count and a contacts-per-account count, so `createTestRecords(5,3)` yields five accounts with three contacts each.[^s1] The Trailhead version, `createAccountsWithOpps(numAccts, numOppsPerAcct)`, inserts the accounts, builds opportunities linked through `AccountId`, inserts them in a single DML statement and returns the accounts; tests then query for the child opportunities.[^s3]

A common refinement is a `doInsert` flag, so the same method can return unsaved records (when a test wants to tweak fields or test the insert itself) or persist them. Factories can also build a related network in one call, such as an account with five contacts.[^s4]

Because the class is annotated `@IsTest`, it runs only in test context and cannot be called from production code. The same annotation excludes it from the org's Apex code size limit, an advantage a plain helper class without the annotation does not get.[^s1][^s3]

## Pairing with @TestSetup

Factories are usually called from a `@TestSetup` method. That method runs once before the test methods in its class, and the records it creates are visible to every test method; changes a test makes to them are rolled back after that test, so the next method sees the original state. A class can have only one test setup method, and it is not supported when the class or a method uses `@IsTest(SeeAllData=true)`.[^s2] Creating shared data once reduces execution time compared with each method building and rolling back its own records.[^s2] Setup records are not returned to test methods, so each test must query for what it needs.[^s4]

## Limits and gotchas

- Setup data changes counts: adding a contact in `@TestSetup` made a query that expected five contacts return six on Trailhead.[^s4]
- A fatal error in a setup method, such as a DML exception or failed assertion, fails the whole test class and no further tests run.[^s2]
- If test setup calls a non-test method in another class, no code coverage is calculated for that method.[^s2]
- Factory DML still counts against the test transaction's governor limits; wrap the code under test in `Test.startTest()`/`Test.stopTest()` so it gets a fresh set of limits.[^s3][^s4]
- Test data is rolled back when each test finishes, so factories never need cleanup code, and static variable changes made during setup do not carry into test methods.[^s2][^s4]

## When to use it (and when not)

Salesforce's guidance is that each test should create its own records rather than read org data: tests that depend on existing data can pass in one org and fail after deployment to another, which is why `SeeAllData=true` is described as not a best practice.[^s4] A factory keeps that per-test data creation short and readable, and makes bulk cases cheap: the Trailhead tests call the same method with 200 records to verify trigger bulkification.[^s3]

When testers want to change input data without redeploying Apex, `Test.loadData` with a CSV static resource is the alternative; it is typically invoked from `@TestSetup` too.[^s4] Many teams combine both: CSV for large reference datasets, a factory for records whose fields vary per test.

## Connections

The factory is a building block of **Apex testing**, its broader node, supplying the isolated data that the framework's default data isolation expects, and it is the opposite approach to relying on **SeeAllData** org data.[^s1][^s4] It is an **alternative to** CSV-driven **Test.loadData**, and the two are often combined inside a `@TestSetup` method.[^s2][^s4] Bulk factory calls are how tests prove **bulkification** of triggers, and the DML they perform is **governed by** the transaction's **governor limits**.[^s3] Because Apex tests cannot be written in production, factories live in development environments such as sandboxes, Developer Edition orgs or **scratch orgs**, and they form the data layer of the unit-test tier in a wider **testing strategy**.[^s4]

## Sources
[^s1]: Salesforce Developers, "Apex Developer Guide (Winter '27): Common Test Utility Classes for Test Data Creation". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_testing_utility_classes.htm (accessed 2026-11-14)
[^s2]: Salesforce Developers, "Apex Developer Guide (Winter '27): Using Test Setup Methods". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_testing_testsetup_using.htm (accessed 2026-11-14)
[^s3]: Trailhead, "Apex Testing: Create Test Data for Apex Tests". https://trailhead.salesforce.com/content/learn/modules/apex_testing/apex_testing_data (accessed 2026-11-14)
[^s4]: Trailhead, "Prepare for Unit Testing: Get Data for Your Tests". https://trailhead.salesforce.com/content/learn/modules/apex-testing-prepare-for-unit-testing/get-data-for-your-tests (accessed 2026-11-14)
