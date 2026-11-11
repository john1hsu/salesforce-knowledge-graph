---
id: kt:flow-tests
type: Feature
title: Flow Tests
aliases: [flow testing, Flow Builder tests, automated flow tests, FlowTest, Flow Test Mode]
domain: automation
summary: >-
  Declarative, automated tests built in Flow Builder that run a flow against simulated triggering data and check
  assertions about its path and results, stored as FlowTest metadata and runnable from the UI or the Salesforce CLI.
release: "Winter '27"
status: current
broader: [kt:flow-builder, kt:testing-strategy]
related: [kt:record-triggered-flow, kt:autolaunched-flow, kt:apex-testing, kt:process-automation-settings, kt:flow-fault-handling]
relations:
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: queriedWith, object: kt:tooling-api}
  - {predicate: consumedBy, object: kt:salesforce-cli}
  - {predicate: dependsOn, object: kt:record-triggered-flow}
  - {predicate: contrastsWith, object: kt:apex-testing}
sources:
  - id: s1
    title: "Create Flow Tests (Flow Implementation 1 module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/flow-implementation-1/create-flow-tests
    type: official-learning
    accessed: 2026-11-11
  - id: s2
    title: "Drive Your Flow Development with Tests (Flow Implementation 1 module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/flow-implementation-1/drive-your-flow-development-with-tests
    type: official-learning
    accessed: 2026-11-11
  - id: s3
    title: "FlowTest (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_flowtest.htm
    type: official-docs
    accessed: 2026-11-11
  - id: s4
    title: "FlowTest (Tooling API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/tooling_api_objects_flowtest.htm
    type: official-docs
    accessed: 2026-11-11
  - id: s5
    title: "flow run test (Salesforce CLI Command Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_flow_run_test.html
    type: official-docs
    accessed: 2026-11-11
  - id: s6
    title: "Flow Test Mode (Beta): The Future of Flow Testing"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2026/flow-test-mode-beta-the-future-of-flow-testing
    type: official-blog
    accessed: 2026-11-11
created: 2026-11-11
---

# Flow Tests

Flow tests are automated checks that admins build inside Flow Builder instead of writing Apex. A test simulates the data that starts a flow, runs the flow, and then evaluates assertions, statements of what the automation should have done. Because the test works on simulated data, running it does not change the org's real records, and tests can be rerun after every change as regression checks.[^s2] Under the hood each test is a `FlowTest` metadata component that checks a record-triggered, autolaunched or Data Cloud-triggered flow for expected results and run-time failures before the flow is activated.[^s3]

## How it works

A test is created from **View Tests → Create** in Flow Builder. The author names it and picks the trigger it simulates, record **Created** or **Updated**; one test covers one of those events, so a flow that reacts to both needs separate tests.[^s1] Trailhead describes four parts: test details (trigger and path), an initial triggering record, an updated triggering record (update tests only), and assertions. Execution follows three stages, Change, Run and Check.[^s2]

- **Initial triggering record**: values typed by hand or copied from an existing record; the copy is not saved or modified.[^s1]
- **Updated triggering record**: the field changes that fire an update-triggered flow; these are also never saved to the org.[^s1]
- **Assertions**: a resource, operator and expected value, plus an optional failure message shown in the debug details.[^s1]

Assertions can check that a decision outcome was taken, that a `$Record` field holds the expected value after the run, or, with the **Was Visited** operator, that an action element such as an email alert executed.[^s1] Results appear in the Result column of the View Tests list, and **Run Test and View Details** shows the path taken and which assertions passed or failed.[^s1]

In metadata, a test lives in the `flowtests` folder with the `.flowtest` suffix and has been available since API 55.0. Its ordered test points sit at the flow's `Start` or `Finish`; parameters supply the initial or updated triggering record, input variables (API 66.0+) or a scheduled path to run (API 56.0+). If any assertion evaluates to false, the run fails.[^s3] Recent versions add options such as `doesCommitChanges`, `doesSkipStartConditions`, `doesTestWaitElement`, `runTestAsUser` and mock outputs on a test point.[^s3] The same tests are exposed as the Tooling API `FlowTest` object, whose `TestType` field (API 66.0+) distinguishes tests with and without assertions.[^s4]

From the command line, `sf flow run test` runs flow tests asynchronously by default and returns a test run ID; `--synchronous` waits for results, and output can be human-readable, TAP, JUnit or JSON, which suits CI pipelines.[^s5] The related `sf logic run test` runs Flow and Apex tests together.[^s5]

## Flow Test Mode (beta)

The Salesforce Admins team describes **Flow Test Mode**, a beta workspace that replaces the Debug button with a Test tab. A debug run can be saved as a named manual test scenario holding the triggering record, input variables and mocked outputs, then turned into an automated regression test by adding assertions.[^s6] It is switched on with **Enable Flow Test Mode (Beta)** in Process Automation Settings and supports record-triggered and autolaunched flows in beta, with screen and scheduled flows planned.[^s6] Mocking lets a test define outputs for subflows and actions, such as a fake HTTP callout response, without running them.[^s6]

## Limits and gotchas

- Trailhead's flow-test unit still teaches the Tests feature for record-triggered flows only; other flow types were tested manually with Debug.[^s2]
- The flow needs at least one element on the Run Immediately path before tests can be built, and an asserted resource or action must already exist in the flow.[^s2]
- A test evaluates either a create or an update, never both, so each trigger event needs its own test.[^s1]
- Running tests with `sf flow run test` requires the View All Data permission.[^s5]
- A deployed Test Mode test needs the beta enabled in the target org as well.[^s6]

## When to use it (and when not)

Use flow tests to lock in the behaviour of record-triggered and autolaunched flows: decision paths, field updates and actions, especially before activating a new version. They are lighter than Apex test classes for admins, but they assert only what the flow touches. When a flow calls Apex, needs realistic multi-record data, or must be checked alongside triggers in one transaction, Apex tests remain the stronger tool, and `sf logic run test` lets a pipeline run both.[^s5][^s2]

## Connections

Flow tests are part of **Flow Builder** and one layer of a broader **testing strategy**. They exercise **record-triggered** and **autolaunched flows**, and complement rather than replace **Apex testing**.[^s2][^s3] They are deployed through the **Metadata API** as `FlowTest`, are queryable as a **Tooling API** object, and are run in pipelines by the **Salesforce CLI**.[^s3][^s4][^s5] **Process Automation Settings** is where Flow Test Mode is enabled.[^s6]

## Sources

[^s1]: Trailhead, "Create Flow Tests (Flow Implementation 1 module)". https://trailhead.salesforce.com/content/learn/modules/flow-implementation-1/create-flow-tests (accessed 2026-11-11)
[^s2]: Trailhead, "Drive Your Flow Development with Tests (Flow Implementation 1 module)". https://trailhead.salesforce.com/content/learn/modules/flow-implementation-1/drive-your-flow-development-with-tests (accessed 2026-11-11)
[^s3]: Salesforce Developers, "FlowTest (Metadata API Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_flowtest.htm (accessed 2026-11-11)
[^s4]: Salesforce Developers, "FlowTest (Tooling API Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/tooling_api_objects_flowtest.htm (accessed 2026-11-11)
[^s5]: Salesforce Developers, "flow run test (Salesforce CLI Command Reference)". https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_flow_run_test.html (accessed 2026-11-11)
[^s6]: Salesforce Admins Blog, "Flow Test Mode (Beta): The Future of Flow Testing". https://admin.salesforce.com/blog/2026/flow-test-mode-beta-the-future-of-flow-testing (accessed 2026-11-11)
