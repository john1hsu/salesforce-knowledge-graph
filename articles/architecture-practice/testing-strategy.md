---
id: kt:testing-strategy
type: Concept
title: Testing Strategy
aliases: [Salesforce testing strategy, test strategy, Salesforce test plan, test pyramid for Salesforce]
domain: architecture-practice
summary: >-
  The architectural plan for how a Salesforce team verifies changes: which layers of testing (unit, integration,
  end-to-end, UAT, performance) it runs, in which environments and with what data, and which automated quality
  gates must pass before a change is promoted to production.
release: "Winter '27"
status: concept
broader: [kt:application-lifecycle-management, kt:well-architected-framework]
related: [kt:environment-strategy, kt:sandbox-types, kt:salesforce-cli, kt:scale-test]
relations:
  - {predicate: hasPart, object: kt:apex-testing}
  - {predicate: dependsOn, object: kt:code-analyzer}
  - {predicate: mitigates, object: kt:governor-limits}
  - {predicate: configuredVia, object: kt:devops-center}
sources:
  - id: s1
    title: "Operational Excellence - DevOps Patterns (Salesforce Well-Architected)"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/well-architected/guide/operational-excellence-devops-patterns.html
    type: official-docs
    accessed: 2026-11-03
  - id: s2
    title: "Test New Features Before a Release"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/advanced-salesforce-release-readiness-strategies/test-new-features-before-a-release
    type: official-learning
    accessed: 2026-11-03
  - id: s3
    title: "Testing Best Practices (Apex Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_testing_best_practices.htm
    type: official-docs
    accessed: 2026-11-03
  - id: s4
    title: "Load Test on the Salesforce Platform Using Scalability Products"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2025/02/load-test-on-the-salesforce-platform-using-scalability-tools
    type: official-blog
    accessed: 2026-11-03
created: 2026-11-03
---

# Testing Strategy

A testing strategy is the deliberate design of how a Salesforce team proves that a change works before it reaches users: which kinds of tests exist, who runs them, where they run, what data they use, and which results block a release. Trailhead frames the choice around the amount of customization: orgs with no custom code can rely on manual functional and user acceptance testing, small amounts of code add unit tests, and complex code or multi-developer teams should adopt automated tooling.[^s2] Salesforce's Well-Architected guidance treats testing as part of operational excellence and describes a layered test pyramid enforced by pipeline quality gates.[^s1]

## Layers of testing

Trailhead distinguishes five kinds of test: unit tests for the smallest pieces of custom code, integration tests for code that talks to external systems or other Salesforce orgs, functional tests against technical requirements, user acceptance tests (UAT) in which end users accept or reject a feature, and performance tests for large volumes of records or operations.[^s2] Because Salesforce runs its own regression testing of the platform, customers should concentrate on their custom code and on new end-user-facing features, prioritising business processes that are high value, high usage, or both.[^s2]

The Well-Architected DevOps patterns shape these layers as a pyramid: many fast unit tests (hundreds), fewer integration tests run in sandboxes with representative data, and a small set of end-to-end browser tests (under 20) for the most valuable user journeys.[^s1] Unit tests should check business rules, edge cases, error paths and behaviour near governor limits, not platform behaviour such as whether a record saves.[^s1] Trailhead adds that API-level tests are preferable to UI tests, which break when a release changes the interface; UI tests make sense mainly where source code is unavailable, as with a managed package.[^s2]

## Apex test discipline

For Apex, the platform enforces a floor: unit tests must cover at least 75% of Apex code, every trigger needs some coverage, and all tests must pass before deployment.[^s3] Salesforce stresses covering every use case rather than chasing the percentage: positive and negative cases, single and bulk records (bulk trigger tests should use at least 20 records), and different user contexts via `runAs`.[^s3] Tests should create their own data instead of relying on org records, create it before `Test.startTest`, and use `Assert` methods to prove behaviour.[^s3] Unit tests should mock callouts with stubs or dependency injection rather than making live HTTP requests.[^s1]

## Environments, data and gates

The Well-Architected guidance maps layers to environments: Developer sandboxes for per-developer unit testing, Partial Copy sandboxes for integration testing, and Full Copy sandboxes for performance testing and staging, with promotion running dev → integration → UAT → production.[^s1] Sandboxes must point only at test endpoints, and post-refresh scripts should reseed test data and restore integration settings.[^s1] Because Developer sandboxes carry no production data, teams must create test data, and automated runs should reset sandbox state between executions.[^s2]

Quality gates make the strategy enforceable. The recommended pipeline runs Salesforce Code Analyzer for static analysis, isolated unit tests that finish in under 5 minutes, a check-only validation deployment through the Salesforce CLI, and security scanning in which critical findings break the build; the target for a typical change is under 15 minutes end to end.[^s1] After release, smoke tests verify critical flows and rollback procedures should be rehearsed in non-production.[^s1]

## Performance and release testing

Load testing belongs before major releases; Well-Architected suggests testing quarterly at 3x–5x current production volumes.[^s1] Salesforce's Scale Test product books a test slot from Setup, and the scalability team recommends refreshing a Full Copy sandbox first, running a 100-user trial, mocking external APIs, and analysing hotspots such as row-lock errors in Scale Center.[^s4] Trailhead cautions against automating performance tests, since they can hit governor limits, and advises notifying Salesforce Support before running them.[^s2] Each major Salesforce release also needs a pass in a preview sandbox, including testing any Release Updates listed in Setup.[^s2]

## Gotchas and anti-patterns

- Coverage-driven tests written only to reach 75%, with no assertions.[^s1]
- Flaky or order-dependent tests that are re-run until they pass, or failing tests commented out.[^s1]
- Happy-path-only suites with no negative or permission tests.[^s1]
- Parallel test runs can raise `UNABLE_TO_LOCK_ROW`; parallel testing can be disabled in Apex Test options.[^s3]
- False positives, where a test fails although the feature works, especially in UI tests across browsers and profiles.[^s2]

## Connections

Testing strategy sits **under** `kt:application-lifecycle-management`, supplying its test stage, and under `kt:well-architected-framework`, whose DevOps patterns define the pyramid and gates.[^s1] It **has part** `kt:apex-testing`, the platform's unit-test framework and coverage rule,[^s3] and **depends on** `kt:code-analyzer` for static-analysis gates.[^s1] Testing near limits **mitigates** `kt:governor-limits` failures in production,[^s1] and pipelines are **configured via** `kt:devops-center` or the `kt:salesforce-cli`.[^s1] It is **related** to `kt:environment-strategy` and `kt:sandbox-types`, which decide where each layer runs, and to `kt:scale-test`, Salesforce's load-testing product.[^s1][^s4]

## Sources

[^s1]: Salesforce Architects, "Operational Excellence - DevOps Patterns". https://architect.salesforce.com/docs/architect/well-architected/guide/operational-excellence-devops-patterns.html (accessed 2026-11-03)
[^s2]: Trailhead, "Test New Features Before a Release". https://trailhead.salesforce.com/content/learn/modules/advanced-salesforce-release-readiness-strategies/test-new-features-before-a-release (accessed 2026-11-03)
[^s3]: Salesforce, "Testing Best Practices" (Apex Developer Guide). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_testing_best_practices.htm (accessed 2026-11-03)
[^s4]: Salesforce Developers Blog, "Load Test on the Salesforce Platform Using Scalability Products". https://developer.salesforce.com/blogs/2025/02/load-test-on-the-salesforce-platform-using-scalability-tools (accessed 2026-11-03)
