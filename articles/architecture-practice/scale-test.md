---
id: kt:scale-test
type: Product
title: Scale Test
aliases: [Salesforce Scale Test, Salesforce load testing, Salesforce performance testing, scale testing, Test Scheduler]
domain: architecture-practice
summary: >-
  A paid Salesforce add-on that lets teams run load tests at full production volume inside a Hyperforce Full
  Copy sandbox, with tools to plan tests from production traffic, book test slots, and compare performance
  results across runs.
release: "Winter '27"
status: current
broader: [kt:testing-strategy]
related: [kt:sandbox-types, kt:large-data-volumes, kt:record-locking, kt:well-architected-framework]
relations:
  - {predicate: integratesWith, object: kt:scale-center}
  - {predicate: dependsOn, object: kt:hyperforce}
  - {predicate: hasPart, object: kt:apexguru}
sources:
  - id: s1
    title: "Plan, Schedule, and Run Scale Tests (Scale Test Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/scale-test-quick-look/plan-schedule-and-run-scale-tests
    type: official-learning
    accessed: 2026-11-09
  - id: s2
    title: "Load Test on the Salesforce Platform Using Scalability Tools"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2025/02/load-test-on-the-salesforce-platform-using-scalability-tools
    type: official-blog
    accessed: 2026-11-09
  - id: s3
    title: "Application Scaling and Performance Testing (Scale Test)"
    publisher: Salesforce
    url: https://salesforce.com/platform/application-scaling-performance-testing
    type: official-docs
    accessed: 2026-11-09
created: 2026-11-09
---

# Scale Test

Scale Test is a paid Salesforce add-on for proving that an org can survive business spikes before they happen. It runs load tests at 100% of expected production volume inside an existing Full Copy sandbox, can show the production org's peak business hours or hotspots for a chosen window, and surfaces front-end optimisation targets such as the most-used and slowest pages, most-used Lightning components and most-used REST APIs.[^s1] It belongs to Salesforce's scalability suite and is designed to be used alongside Scale Center, which handles diagnosis.[^s1] Salesforce positions it for Sales Cloud, Service Cloud and Experience Cloud workloads, and states that it reads only observability data from test runs rather than business data.[^s3]

## How it works

The product has three parts. **Test Plan Creation** analyses the past 30 days of production peak-hour data and recommends use cases, metrics and throughput in requests per second; the report is asynchronous and split into test use cases and server-side metrics.[^s2][^s1] **Test Scheduler**, reached from Setup by searching for Scale Test, is a calendar on which an admin books a continuous block of one day to two weeks on the sandbox's instance; slots are first-come, first-served and bookings show as Confirmed, Live or Completed.[^s1] **Test Execution** shows server-side traffic such as triggers, platform events and DML so the team can refine scripts, and compares metrics across recent runs.[^s1] During a booked window Salesforce adds compute capacity to the sandbox infrastructure so a full-size load test is possible.[^s2]

Salesforce does not generate the load itself in the typical setup: teams script API traffic with a tool such as JMeter, or browser journeys with Selenium to measure Lightning page and component load times, and can generate synthetic data with Snowfakery.[^s1][^s2] A Trial Accuracy Checker compares a sandbox baseline against a production baseline and scores how closely the test workload matches production across UI, API, database-read and database-write traffic.[^s2]

## Limits and gotchas

- **Environment.** Scale Test needs a Full Copy sandbox on Hyperforce, although production itself need not be on Hyperforce; it is not available in Developer Edition or Trailhead Playground orgs.[^s1] Refresh the Full Copy sandbox from production first so data and metadata match and results are not false positives.[^s2]
- **Licensing.** Test days are bought as an add-on through an account executive, and public pricing is not listed.[^s1][^s3] Access is granted with the ScaleTestingServiceStandardUserPS or ScaleTestingServiceAdvancedUserPS permission sets; only the advanced set includes the Test Scheduler.[^s3]
- **Booking rules.** New slots need at least two weeks' notice and cancellations at least one week; the maximum requests per second must be submitted before booking; testing is confined to the 24-hour windows of confirmed days; and booked days should be cancelled before a sandbox is refreshed or deleted to avoid charges.[^s3]
- **Retention.** Test Plan Creation reports stay available for 30 days and Trial Accuracy reports for 15 days.[^s3]
- **Warm-up runs.** The developer guidance has teams complete a 100-user test before booking the full load slot, and size concurrency with a 5 to 10 user run first.[^s2]
- **External systems.** Stub external APIs with realistic responses as close to Salesforce as possible, and make sure sandbox middleware has production-like capacity, or the test measures the wrong bottleneck.[^s2]

## When to use it (and when not)

Use Scale Test before a known surge, such as a launch, seasonal peak or large user rollout, and as a recurring step in each release cycle so key performance indicators can be tracked over time.[^s1] Salesforce recommends keeping performance and scalability testing separate from functional and regression testing, and revisiting personas and peak request volumes with each release.[^s1] A worked example from Salesforce sets the goal as ten times normal throughput with no errors and no response-time degradation, and sizes virtual users with Little's Law from response, think and wait times.[^s2] For everyday unit and regression coverage, Apex tests and functional suites remain the right tools; Scale Test is the costly, scheduled exercise for capacity questions.

## Connections

Scale Test is one layer of a `kt:testing-strategy` (`broader`), the performance tier that sits after unit and functional testing.[^s1] It runs on the Full Copy sandbox type described in `kt:sandbox-types` and depends on that sandbox being hosted on `kt:hyperforce`.[^s1] It integrates with `kt:scale-center`, whose org-performance and consolidated reports diagnose row-lock, concurrent-Apex and connection-pool errors found during a run, and the product page lists `kt:apexguru` AI code analysis as available within it.[^s2][^s3] Row-lock findings tie it to `kt:record-locking`, while volume-driven slowdowns connect it to `kt:large-data-volumes`; both are scalability concerns that the `kt:well-architected-framework` asks architects to design for.[^s2]

## Sources
[^s1]: Trailhead, "Plan, Schedule, and Run Scale Tests (Scale Test Quick Look)". https://trailhead.salesforce.com/content/learn/modules/scale-test-quick-look/plan-schedule-and-run-scale-tests (accessed 2026-11-09)
[^s2]: Salesforce Developers Blog, "Load Test on the Salesforce Platform Using Scalability Tools". https://developer.salesforce.com/blogs/2025/02/load-test-on-the-salesforce-platform-using-scalability-tools (accessed 2026-11-09)
[^s3]: Salesforce, "Application Scaling and Performance Testing (Scale Test)". https://salesforce.com/platform/application-scaling-performance-testing (accessed 2026-11-09)
