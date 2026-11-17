---
id: kt:devops-testing
type: Tool
title: DevOps Testing
aliases: [Salesforce DevOps Testing, DevOps Center Testing, Lifecycle Center Testing]
domain: devops-and-alm
summary: >-
  The testing layer of DevOps Center (now Lifecycle Center) that syncs test suites from Salesforce and partner
  providers, runs them automatically at pipeline stages, and blocks promotion with quality gate rules.
release: "Winter '27"
status: current
broader: [kt:devops-center, kt:testing-strategy]
related: [kt:apex-testing, kt:flow-tests, kt:continuous-integration-for-salesforce]
relations:
  - {predicate: integratesWith, object: kt:code-analyzer}
  - {predicate: integratesWith, object: kt:agentforce-testing-center}
  - {predicate: integratesWith, object: kt:scale-test}
  - {predicate: dependsOn, object: kt:devops-center}
sources:
  - id: s1
    title: "Application Lifecycle Management with DevOps Testing and DevOps Center"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.devops_testing_application_lifecycle_management_with_devops_testing_and_devops_center.htm&type=5
    type: official-docs
    accessed: 2026-11-17
  - id: s2
    title: "Create a Test Suite"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=platform.devops_testing_create_a_test_suite.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-17
  - id: s3
    title: "Supercharge DevOps with Built-In Testing and Quality Gates"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2025/04/supercharge-devops-with-built-in-testing-and-quality-gates
    type: official-blog
    accessed: 2026-11-17
  - id: s4
    title: "Shift Left Natively: Testing and Quality Gates in DevOps Center"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2026/08/shift-left-natively-testing-and-quality-gates-in-devops-center
    type: official-blog
    accessed: 2026-11-17
  - id: s5
    title: "Improve Release Quality with DevOps Center Testing"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/devops-center-tests-quick-look/improve-release-quality-with-devops-center-testing
    type: official-learning
    accessed: 2026-11-17
  - id: s6
    title: "Enhance Development Lifecycles with Winter '26 Innovations"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-architect-certification-maintenance-winter-26/discover-whats-new-with-development-lifecycles-for-winter-26
    type: official-learning
    accessed: 2026-11-17
created: 2026-11-17
---

# DevOps Testing

**DevOps Testing** is Salesforce's testing and quality-enforcement layer for DevOps Center, the pipeline tool now being renamed Lifecycle Center. It gives a team one place to define tests, run them automatically as work moves through the pipeline, and stop changes that fail agreed quality rules.[^s1][^s3] Salesforce announced it as generally available in April 2025, and Trailhead's Winter '26 architect maintenance module also lists it as GA.[^s3][^s6] By August 2026 the developer blog was describing the capability as DevOps Center Testing, native to the platform.[^s4]

## How it works

The building blocks are **test providers**, **test suites**, **stage assignments** and **quality gate rules**.[^s1]

1. **Providers.** An admin configures a provider for an active DevOps Center project and syncs it, which pulls that provider's tests and suites into the Tests and Test Suites tabs.[^s1] Native providers are Apex unit tests, Flow tests and Salesforce Code Analyzer, plus certified partner tools.[^s5] The 2025 launch named ACCELQ, Copado, Panaya, Provar, Quality Clouds and Tricentis as partners, and Scale Test for performance testing.[^s3]
2. **Suites.** A suite groups tests. Where a provider supports it, you can start a new suite from DevOps Testing, but you finish building it in the provider and then run a manual sync before it appears.[^s2]
3. **Stage assignments.** Suites are assigned to pipeline stages, for example the Work Item: Review stage, on the Stage Assignments tab.[^s1] Different stages can use different providers, such as stricter Code Analyzer scanning at staging than in development.[^s5]
4. **Quality gates.** Gate rules define what passing means, such as a minimum pass percentage, a severity threshold, or essential tests that must never fail. A failed gate blocks the change from advancing.[^s5]

Runs are event-driven. Creating a review for a work item, or promoting it, triggers every suite assigned to that stage as one coordinated job.[^s1][^s5] If all gates pass the work item can move on; otherwise the team investigates the failures in DevOps Testing.[^s1] When a run fails because of a gate, an execution error or a configuration problem, a user can re-run tests on demand, and the next promotion attempt triggers a fresh automatic run.[^s5] Results appear on the work item's Related tab and in a Tests Activity History that records every test event and gate decision.[^s5]

Each test carries a severity. Code Analyzer v5 uses levels 1 (most critical) to 5, and tests from other providers get a default level that can be changed.[^s3] Developers get feedback pointing to the failing location in the code, and Code Analyzer findings can offer an AI-assisted quick fix.[^s3]

## Setup, access and gotchas

DevOps Center must be set up first, with a GitHub project and an active pipeline.[^s1] The 2025 launch shipped DevOps Testing as an AppExchange managed package installed in the DevOps Center org.[^s3] The current Trailhead module says testing is built into Lifecycle Center and needs no separate installation, so check which model your org is on.[^s5]

Users need the DevOps Testing Manager or DevOps Testing User permission set alongside a DevOps Center permission set.[^s1] Creating a suite requires DevOps Testing Manager.[^s2] Salesforce Help lists Lightning Experience in Enterprise, Performance, Unlimited and Developer editions, and Professional Edition with API access.[^s1]

- **Sync is manual after provider-side changes.** Suites created or edited in a provider don't appear until someone runs a sync from the Test Providers tab.[^s2]
- **Check feature stages per provider.** Help still labels the Code Analyzer v5 provider integration as beta.[^s1]
- **Gates should be strict but achievable.** Salesforce advises realistic criteria, because an unreachable gate simply stalls promotion.[^s1]

## When to use it

Use DevOps Testing when a team already releases through DevOps Center and wants tests enforced inside that pipeline rather than in a separate CI server.[^s1][^s4] Teams with their own CI can still call the gates through the CLI or REST API.[^s4] Since mid-2025 it can also run Agentforce Testing Center tests with their own gates, and Flow tests can join suites through Salesforce CLI.[^s6] Agentforce Vibes adds skills that configure providers, assign suites to stages, run suites and explain failures.[^s4]

## Connections

DevOps Testing is a part of **DevOps Center** and depends on its projects, pipelines and work items. It puts a team's **testing strategy** into practice by turning test policy into stage gates.[^s1][^s5] Its native providers link it to **Apex testing**, **Flow tests** and **Code Analyzer**.[^s5] It also integrates with **Agentforce Testing Center** for agent tests and with **Scale Test** for performance tests.[^s6][^s3] For teams that run tests from their own **continuous integration** pipelines, the CLI and API hooks let both approaches share the same gates.[^s4]

## Sources

[^s1]: Salesforce Help, "Application Lifecycle Management with DevOps Testing and DevOps Center". https://help.salesforce.com/s/articleView?language=en_US&id=platform.devops_testing_application_lifecycle_management_with_devops_testing_and_devops_center.htm&type=5 (accessed 2026-11-17)
[^s2]: Salesforce Help, "Create a Test Suite". https://help.salesforce.com/s/articleView?id=platform.devops_testing_create_a_test_suite.htm&language=en_US&type=5 (accessed 2026-11-17)
[^s3]: Salesforce Developers Blog, "Supercharge DevOps with Built-In Testing and Quality Gates" (April 2025). https://developer.salesforce.com/blogs/2025/04/supercharge-devops-with-built-in-testing-and-quality-gates (accessed 2026-11-17)
[^s4]: Salesforce Developers Blog, "Shift Left Natively: Testing and Quality Gates in DevOps Center" (August 2026). https://developer.salesforce.com/blogs/2026/08/shift-left-natively-testing-and-quality-gates-in-devops-center (accessed 2026-11-17)
[^s5]: Trailhead, "Improve Release Quality with DevOps Center Testing". https://trailhead.salesforce.com/content/learn/modules/devops-center-tests-quick-look/improve-release-quality-with-devops-center-testing (accessed 2026-11-17)
[^s6]: Trailhead, "Enhance Development Lifecycles with Winter '26 Innovations". https://trailhead.salesforce.com/content/learn/modules/salesforce-architect-certification-maintenance-winter-26/discover-whats-new-with-development-lifecycles-for-winter-26 (accessed 2026-11-17)
