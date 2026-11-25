---
id: kt:go-live-readiness-assessment
type: Concept
title: Go-Live Readiness Assessment
aliases: [go-live readiness review, launch readiness review, go-live checklist, launch gate, site readiness assessment, go/no-go readiness review]
domain: architecture-practice
summary: >-
  The structured review held in the weeks before a Salesforce launch that checks whether the solution, data, people
  and support model are ready, logs risks and blockers with owners, and feeds the go/no-go decision.
release: "Winter '27"
status: concept
broader: [kt:release-management, kt:application-lifecycle-management]
related: [kt:cutover-plan, kt:user-acceptance-testing, kt:hypercare, kt:data-migration-strategy, kt:change-management-and-adoption, kt:non-functional-requirements]
relations:
  - {predicate: dependsOn, object: kt:testing-strategy}
  - {predicate: dependsOn, object: kt:security-health-check}
  - {predicate: dependsOn, object: kt:scale-test}
  - {predicate: dependsOn, object: kt:rollback-plan}
sources:
  - id: s1
    title: "Prepare to Launch (B2C Commerce Site Readiness Assessment)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-b2c-commerce-site-readiness-assessment/prepare-to-launch
    type: official-learning
    accessed: 2026-11-25
  - id: s2
    title: "Manage the Launch and Post-Launch Activities"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/cc-project-mgmt/cc-launch-and-post-launch
    type: official-learning
    accessed: 2026-11-25
  - id: s3
    title: "Use Health Check to Scan Your Security Configurations"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/security_basics/security_basics_healthcheck
    type: official-learning
    accessed: 2026-11-25
  - id: s4
    title: "Use the go-live checklist to make sure your solution is ready for go-live"
    publisher: Microsoft Learn (Dynamics 365 implementation guide)
    url: https://learn.microsoft.com/dynamics365/guidance/implementation-guide/prepare-go-live-checklist
    type: partner
    accessed: 2026-11-25
  - id: s5
    title: "Prepare to go live"
    publisher: Microsoft Learn (Dynamics 365 implementation guide)
    url: https://learn.microsoft.com/dynamics365/guidance/implementation-guide/prepare-to-go-live
    type: partner
    accessed: 2026-11-25
created: 2026-11-25
---

# Go-Live Readiness Assessment

A go-live readiness assessment is the last formal checkpoint before a new Salesforce solution reaches its users. It asks one question from several angles: is the build, the data, the organization and the support model ready, and if not, what must be fixed first? Salesforce's own delivery methodology for B2C Commerce calls this checkpoint the Launch Gate, the final review of a site readiness assessment covering storefront performance, security and delivery; passing it means the site may launch.[^s1] Microsoft's implementation guidance for business applications describes the same practice as a go-live readiness review run with all parties, ending in a list of risks, mitigations and a go/no-go recommendation.[^s5] The practice is tool-neutral, so it applies equally to a Sales Cloud rollout, an org merge or an Experience Cloud launch.

## What gets assessed

Microsoft's go-live checklist groups readiness into eleven areas, each with checkbox tasks and a sign-off.[^s4] Translated to a Salesforce program they are:

- **Scope and acceptance.** The delivered scope matches what was agreed, and the business has accepted the solution.[^s4]
- **Testing completion.** UAT, system integration testing and performance testing have met their exit criteria with business sign-off.[^s4]
- **Realistic UAT.** Testers used real security roles and migrated data, not System Administrator for everyone.[^s4]
- **Data migration.** Loads were rehearsed several times, checked for duplicates and corruption, and fit the cutover window.[^s4]
- **Cutover.** The cutover plan covers dependencies, timing, roles and verification, and has been tested and signed off.[^s4]
- **External dependencies.** Integrations, vendors and licences are confirmed, with enough licences for every user.[^s4][^s5]
- **People.** Training, sponsorship and a super-user network are in place for day one.[^s4]
- **Operational support.** Monitoring, help-desk routing, escalation paths and the handover to support are defined.[^s4][^s5]

On Salesforce, the security slice of this review usually includes Health Check, which scores the org from 0 to 100 against Salesforce's standard values or a custom baseline imported as XML.[^s3] The module warns that the Fix Risks button changes many settings at once and can break integrations or user access, so remediation found during readiness should be tested in a sandbox first.[^s3]

## How the review runs

Timing matters. Microsoft notes that a review held only a few days before go-live risks a delay, while one held too early judges an immature project; the aim is to leave enough time to mitigate blockers and prepare production.[^s5] Salesforce's Launch Gate is more specific: the first review happens two to three weeks before the planned go-live date, and there are at most two reviews, the second re-checking only the items that failed.[^s1] Before the review, features should be ready for business use, load testing complete and UAT finished or nearly so, and the reviewers need admin access to staging and production plus the specifications, project plan, load-test results and data mappings.[^s1]

Findings are graded. In the Launch Gate, a launch blocker such as missing SSL certificates, disabled caching or a failed load test fails the assessment automatically; the reviewers then recommend delaying, though the customer makes the final call.[^s1] Critical items, such as undesignated support contacts, must also be resolved quickly.[^s1] Each finding should carry an owner and a target date, and blockers need either a fix or an agreed workaround before go-live.[^s5]

## Outputs and the go/no-go decision

The assessment does not itself launch anything. Its outputs are a risk and issue list with recommendations, a mitigation plan with an owner per action, and a recommendation on whether the planned date is feasible; Microsoft places the go/no-go decision with the steering committee.[^s5] In Salesforce's launch guidance, the Launch Gate also requires completed code, business-preparedness and launch-readiness reviews, a launch checklist in which every task has an owner, and a communication plan that names who may declare success or order a rollback.[^s2] Operational items such as purging test data and naming support contacts fall to the customer, but the implementation partner is expected to drive them to completion.[^s1]

## Gotchas

Treating the checklist as paperwork is the common failure: Microsoft advises reviewers to challenge vague answers rather than accept them.[^s5] Another is skipping the rollback rehearsal; Salesforce's launch unit tests the rollback procedure alongside a launch dry run.[^s2] Finally, readiness covers people as well as code: unresolved training or support gaps are valid reasons for a no-go.[^s4]

## Connections

The assessment sits **broader** under release management and application lifecycle management, as the gate between build and production.[^s5] It **depends on** a testing strategy whose UAT, integration and performance results it audits,[^s4] on scale testing for the load results Launch Gate requires,[^s1] on Security Health Check for the security baseline,[^s3] and on a rehearsed rollback plan.[^s2] It is **related** to the cutover plan, which it validates against the cutover window and which then executes the go decision;[^s5] to user acceptance testing and data migration strategy, two of its main evidence streams;[^s4] to non-functional requirements, the performance and security targets it checks;[^s1] to change management and adoption, which supplies training and sponsorship readiness;[^s4] and to hypercare, the support period its operational-readiness checks prepare for.[^s2][^s5]

## Sources

[^s1]: Trailhead, "Prepare to Launch" (Salesforce B2C Commerce Site Readiness Assessment). https://trailhead.salesforce.com/content/learn/modules/salesforce-b2c-commerce-site-readiness-assessment/prepare-to-launch (accessed 2026-11-25)
[^s2]: Trailhead, "Manage the Launch and Post-Launch Activities". https://trailhead.salesforce.com/content/learn/modules/cc-project-mgmt/cc-launch-and-post-launch (accessed 2026-11-25)
[^s3]: Trailhead, "Use Health Check to Scan Your Security Configurations". https://trailhead.salesforce.com/content/learn/modules/security_basics/security_basics_healthcheck (accessed 2026-11-25)
[^s4]: Microsoft Learn, "Use the go-live checklist to make sure your solution is ready for go-live" (Dynamics 365 implementation guide). https://learn.microsoft.com/dynamics365/guidance/implementation-guide/prepare-go-live-checklist (accessed 2026-11-25)
[^s5]: Microsoft Learn, "Prepare to go live" (Dynamics 365 implementation guide). https://learn.microsoft.com/dynamics365/guidance/implementation-guide/prepare-to-go-live (accessed 2026-11-25)
