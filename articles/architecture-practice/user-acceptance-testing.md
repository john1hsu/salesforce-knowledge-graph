---
id: kt:user-acceptance-testing
type: Concept
title: User Acceptance Testing
aliases: [UAT, Salesforce UAT, acceptance testing, business acceptance testing]
domain: architecture-practice
summary: >-
  The final test phase before a Salesforce change goes live, in which business users and subject matter experts
  run real-world scenarios in a sandbox and formally accept or reject the delivery, producing the written sign-off
  that acts as the go/no-go gate for production.
release: "Winter '27"
status: concept
broader: [kt:testing-strategy, kt:application-lifecycle-management]
related: [kt:requirements-gathering, kt:environment-strategy, kt:release-management, kt:change-management-and-adoption, kt:large-data-volumes]
relations:
  - {predicate: usedBy, object: kt:business-analyst}
  - {predicate: dependsOn, object: kt:sandbox-types}
  - {predicate: contrastsWith, object: kt:apex-testing}
  - {predicate: coveredBy, object: kt:business-analyst-certification}
sources:
  - id: s1
    title: "Learn About User Acceptance Testing"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/user-acceptance-testing-video/learn-about-user-acceptance-testing
    type: official-learning
    accessed: 2026-11-15
  - id: s2
    title: "Explore User Acceptance (Salesforce Business Analyst Certification Prep)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-business-analyst-certification-prep/explore-user-acceptance
    type: official-learning
    accessed: 2026-11-15
  - id: s3
    title: "Test New Features Before a Release"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/advanced-salesforce-release-readiness-strategies/test-new-features-before-a-release
    type: official-learning
    accessed: 2026-11-15
  - id: s4
    title: "Ask an Architect: UAT Strategies for Large Data Volume Scenarios"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/ask-an-architect-uat-strategies-for-large-data-volume-scenarios/
    type: official-blog
    accessed: 2026-11-15
  - id: s5
    title: "Secure Testing (sandboxes for building and testing AI)"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/secure-testing/
    type: official-blog
    accessed: 2026-11-15
  - id: s6
    title: "Sandboxes: Staging Environments for Customizing and Testing"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/deploy_sandboxes.pdf
    type: official-docs
    accessed: 2026-11-15
created: 2026-11-15
---

# User Acceptance Testing

User acceptance testing (UAT) is the last checkpoint before a Salesforce project or enhancement reaches production. After the delivery team's own quality assurance has passed the work, end users test it in a sandbox to confirm that what the business asked for is what was built and that it is fit for daily use.[^s1] Trailhead frames it as the moment end users accept or reject the final feature delivery.[^s3] The outcome is usually binary, pass or fail, so UAT doubles as the go/no-go decision for a release.[^s1] Nothing about the practice is Salesforce-specific, but the platform's sandboxes, release cadence and data volumes shape how it is run.[^s1]

## Who runs it

Participants are business stakeholders, end users and business analysts, sometimes joined by IT.[^s1] In Salesforce's own BA practice the analyst owns UAT: picking the testers, coordinating the cycle and collecting the final written sign-off.[^s1] Testers should be real end users or subject matter experts. Trailhead recounts a large project whose scripts did not mirror real work and whose testers were not SMEs: the business signed off, and major gaps surfaced only after go-live.[^s1] Developers stay involved to fix what testers find, while key stakeholders agree the scope before testing begins.[^s4]

## How a UAT cycle works

Preparation decides most of the outcome. The Salesforce BA team's checklist covers these steps:[^s1]

1. Identify testers and approvers, and open a dedicated channel with a regular status cadence.[^s1]
2. Schedule a kickoff, recurring check-ins and triage sessions, and define how bugs and questions are reported.[^s1]
3. Write test scenarios with detailed steps, and have business stakeholders confirm in writing that the scripts cover their expectations.[^s1]
4. Validate the sandbox and confirm the test data is in place before testers start.[^s1]
5. Hold a closing round-up that formally ends UAT, then obtain written business sign-off before deploying.[^s1]

Scripts trace back to the acceptance criteria written during requirements work, and they should exercise the key personas of the project.[^s1] On small projects functional testing can be folded into UAT, and UAT can be combined with end-user training when feedback is cheap to act on.[^s3] When choosing what to cover, favour business processes that are high value, heavily used, or both, along with the device, browser and profile combinations most users actually have.[^s3]

## Environments and data

Salesforce's sandbox guide names the Partial Copy sandbox, which holds metadata plus a sample of data, as suited to quality assurance work such as UAT, integration testing and training; only Full sandboxes support performance testing, load testing and staging.[^s6] Salesforce also recommends running UAT against a full data set where possible, because a Full Copy sandbox reproduces real business conditions and gives more realistic feedback, and it advises masking sensitive data in test environments.[^s5] Sandbox Preview lets teams run acceptance tests in a sandbox already upgraded to the next release before it reaches production.[^s3]

For large data volume (LDV) solutions, Salesforce architects describe LDV as over 5 million records, thousands of concurrent users, parents with more than 10,000 children, or over 100GB of storage.[^s4] Their advice is to dedicate a sandbox to load testing, since a shared UAT sandbox is unavailable for functional testing while load tests run, and to finish those tests at least three to four weeks before go-live so there is time to fix what they reveal.[^s4] Business users must still complete and sign off UAT before the project can launch.[^s4]

## Gotchas

- **Unrealistic scripts or testers.** Sign-off from people who do not do the work daily gives false confidence.[^s1]
- **Skipped preparation.** Missing test data or an unvalidated sandbox burns tester time and goodwill.[^s1]
- **Treating found defects as failure.** Problems caught in a well-run UAT are the point: they prevent a bad release.[^s1]

## Connections

UAT sits **broader** under the testing strategy, as its final layer, and under application lifecycle management, where it gates promotion to production.[^s3] It **contrasts with** Apex unit testing: unit tests are needed only when an org has custom code, whereas manual functional and acceptance testing applies to every org.[^s3] It is **used by** the business analyst, and it **depends on** sandbox types, since the sandbox chosen sets the realism of the data.[^s1][^s6] It is **covered by** the Salesforce Business Analyst certification, whose User Acceptance section is 12% of the exam and covers test scripts, stakeholder sign-off and go/no-go decisions.[^s2] It is **related** to requirements gathering, which produces the acceptance criteria UAT verifies; environment strategy and release management, which place the UAT sandbox in the pipeline; change management and adoption, which prepares the same end users for go-live; and large data volumes, which change how UAT must be planned.[^s4][^s1]

## Sources

[^s1]: Trailhead, "Learn About User Acceptance Testing". https://trailhead.salesforce.com/content/learn/modules/user-acceptance-testing-video/learn-about-user-acceptance-testing (accessed 2026-11-15)
[^s2]: Trailhead, "Explore User Acceptance" (Salesforce Business Analyst Certification Prep). https://trailhead.salesforce.com/content/learn/modules/salesforce-business-analyst-certification-prep/explore-user-acceptance (accessed 2026-11-15)
[^s3]: Trailhead, "Test New Features Before a Release". https://trailhead.salesforce.com/content/learn/modules/advanced-salesforce-release-readiness-strategies/test-new-features-before-a-release (accessed 2026-11-15)
[^s4]: Salesforce, "Ask an Architect: UAT Strategies for Large Data Volume Scenarios". https://www.salesforce.com/blog/ask-an-architect-uat-strategies-for-large-data-volume-scenarios/ (accessed 2026-11-15)
[^s5]: Salesforce, "Secure Testing (sandboxes for building and testing AI)". https://www.salesforce.com/blog/secure-testing/ (accessed 2026-11-15)
[^s6]: Salesforce, "Sandboxes: Staging Environments for Customizing and Testing". https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/deploy_sandboxes.pdf (accessed 2026-11-15)
