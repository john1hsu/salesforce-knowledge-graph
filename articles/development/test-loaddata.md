---
id: kt:test-loaddata
type: Feature
title: Test.loadData
aliases: [Test loadData, loadData method, CSV test data, static resource test data, Loading Test Data]
domain: development
summary: >-
  The Apex Test.loadData method, which inserts test records for one sObject type from a CSV file stored as a static
  resource and returns the inserted records, so test data can be maintained as a file instead of in code.
release: "Winter '27"
status: current
broader: [kt:apex-testing]
related: [kt:test-data-factory, kt:test-setup-methods, kt:testing-strategy]
relations:
  - {predicate: alternativeTo, object: kt:seealldata}
  - {predicate: dependsOn, object: kt:static-resources}
  - {predicate: consumedBy, object: kt:apex}
sources:
  - id: s1
    title: "Apex Developer Guide (Winter '27): Loading Test Data"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_testing_load_data.htm
    type: official-docs
    accessed: 2026-11-20
  - id: s2
    title: "Prepare for Unit Testing: Get Data for Your Tests"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/apex-testing-prepare-for-unit-testing/get-data-for-your-tests
    type: official-learning
    accessed: 2026-11-20
  - id: s3
    title: "Month of Testing: Advanced Topics in Salesforce Unit Testing (Part 3 of 3)"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2018/05/month-of-testing-advanced-topics-in-salesforce-unit-testing-part-3-of-3
    type: official-blog
    accessed: 2026-11-20
created: 2026-11-20
---

# Test.loadData

**Test.loadData** is a method of the Apex `Test` class that populates test records from a file rather than from code. The developer stores a comma-separated file as a static resource and calls `Test.loadData(sObjectType, 'resourceName')` inside a test; the method inserts one record per data row and returns them as a list of sObjects.[^s1] The Winter '27 (API version 68.0) Apex Developer Guide documents it under "Loading Test Data".[^s1]

## How it works

The CSV's first line names the fields, and every following line holds the values for one record.[^s1] The setup has three steps: author the CSV, upload it under Setup as a static resource, and reference the resource by name from the test method. A typical call is `List<sObject> ls = Test.loadData(Account.sObjectType, 'myResource');`, after which the test can assert on the list size and cast elements to the concrete type, such as `(Account)ls[0]`.[^s1]

Because the call happens inside a test, the inserted records follow the normal rules of isolated Apex tests: they exist only for the test's transaction and are rolled back when it ends, so no cleanup is needed.[^s2] Trailhead pairs the method with a `@TestSetup` method so that the CSV is loaded once and the records are available to every test method in the class, each of which still has to query them.[^s2]

Related records can be loaded from separate files. The Salesforce Developers blog shows adding an `Id` column to the parent CSV and a lookup column (for example `AccountId`) in the child CSV that points at those values, then loading the parent file before the child.[^s3]

## Limits and gotchas

- One call loads one sObject type, so a multi-object fixture needs one static resource and one call per object, ordered parent first.[^s1][^s3]
- The method already performs the insert; the guide describes the return value as the inserted records, so older examples that insert the list again should not be copied.[^s1][^s3]
- Records loaded in `@TestSetup` are reset between test methods, so a change made in one method is not visible in the next.[^s2]
- The blog suggests naming each resource after its test class and object, such as `MyClass_tests.Account.csv`, to keep fixtures traceable.[^s3]

The CSV lives in a static resource, so it has to travel with the test class in every deployment, and the guide states no row limit for the method.[^s1] Trailhead notes that `Test.startTest()` and `Test.stopTest()` give the code under test a fresh set of governor limits, so loading fixtures before `startTest` keeps that setup work out of the measured block.[^s2]

## When to use it (and when not)

File-based data suits fixtures that change often or that non-developers maintain: Trailhead notes that a CSV lets teams vary inputs without deploying code, and the blog adds that admins and QA staff can add rows themselves.[^s2][^s3] A **test data factory** is the better fit when records need computed values, many variations, or deep object graphs, since a factory method can build related records in a single line of Apex.[^s2] Both are preferable to `SeeAllData=true`, which Trailhead calls not a best practice because it ties tests to whatever data the org happens to contain.[^s2]

## Connections

Test.loadData is part of **Apex testing**, its broader node, and one of the four data approaches Trailhead teaches alongside brute-force inserts, **test data factories** and **test setup methods**.[^s2] It is an **alternative to SeeAllData**: both give a test predictable records, but loadData keeps the test isolated from org data.[^s2] It **depends on static resources**, which hold the CSV files, and is called from **Apex** test code.[^s1] Choosing between file-based and code-based fixtures is part of a broader **testing strategy**.[^s3]

## Sources

[^s1]: Salesforce Developers, "Apex Developer Guide (Winter '27): Loading Test Data". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_testing_load_data.htm (accessed 2026-11-20)
[^s2]: Trailhead, "Prepare for Unit Testing: Get Data for Your Tests". https://trailhead.salesforce.com/content/learn/modules/apex-testing-prepare-for-unit-testing/get-data-for-your-tests (accessed 2026-11-20)
[^s3]: Salesforce Developers Blog, "Month of Testing: Advanced Topics in Salesforce Unit Testing (Part 3 of 3)". https://developer.salesforce.com/blogs/2018/05/month-of-testing-advanced-topics-in-salesforce-unit-testing-part-3-of-3 (accessed 2026-11-20)
