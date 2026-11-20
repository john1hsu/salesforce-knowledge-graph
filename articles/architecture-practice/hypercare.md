---
id: kt:hypercare
type: Concept
title: Hypercare
aliases: [hypercare period, post-go-live support, go-live support, stabilization period, hypercare support]
domain: architecture-practice
summary: >-
  The short, deliberately over-staffed support period that follows a Salesforce go-live, in which the project and
  support teams watch the new solution closely, fix issues fast and then hand it over to business-as-usual support
  once agreed exit criteria are met.
release: "Winter '27"
status: concept
broader: [kt:release-management, kt:change-management-and-adoption]
related: [kt:user-acceptance-testing, kt:salesforce-center-of-excellence, kt:statement-of-work, kt:salesforce-governance, kt:service-cloud]
relations:
  - {predicate: partOf, object: kt:application-lifecycle-management}
  - {predicate: dependsOn, object: kt:rollback-plan}
sources:
  - id: s1
    title: "Hypercare Defined: A Complete Guide with Benefits and Best Practices"
    publisher: Salesforce
    url: https://www.salesforce.com/service/hypercare/
    type: official-blog
    accessed: 2026-11-20
  - id: s2
    title: "Manage the Launch and Post-Launch Activities"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/cc-project-mgmt/cc-launch-and-post-launch
    type: official-learning
    accessed: 2026-11-20
  - id: s3
    title: "Plan your support operations (Dynamics 365 implementation guide)"
    publisher: Microsoft Learn
    url: https://learn.microsoft.com/en-za/Dynamics365/guidance/implementation-guide/transition-to-support-operations
    type: partner
    accessed: 2026-11-20
  - id: s4
    title: "Hypercare Strategy (Accelerate Cookbook for Content Hub)"
    publisher: Sitecore
    url: https://developers.sitecore.com/learn/accelerate/content-hub/final-steps/hypercare-strategy
    type: partner
    accessed: 2026-11-20
created: 2026-11-20
---

# Hypercare

Hypercare is the period immediately after a go-live when a team provides support well above its normal level. Salesforce describes it as a short stretch of elevated, high-touch support following a major change, such as a new release, a CRM migration or a platform rollout.[^s1] Microsoft's implementation guidance frames it the same way: extra resources and attention are put on users and business processes for a short time after go-live.[^s3] The practice is not unique to Salesforce; Salesforce's own guidance applies it to service teams absorbing a launch, and its delivery methodology ends projects with a formal support handover.[^s1][^s2]

## How long it lasts

There is no fixed length. Salesforce says hypercare typically lasts one to four weeks after a major launch, shorter for small changes and longer for migrations or platform rollouts.[^s1] Sitecore's delivery cookbook plans its hypercare phase for 2-3 weeks starting immediately after go-live, extendable if the client needs it.[^s4] The more useful advice is to end hypercare on evidence, not on the calendar: stable case volumes and consistent system performance are the signals Salesforce names.[^s1] Microsoft recommends fixing an end date in advance anyway, with an action plan for reaching the exit criteria by then.[^s3]

## Phases and activities

Salesforce breaks hypercare into four phases:[^s1]

1. **Plan and prepare.** Review risks, update knowledge articles, train support reps, define escalation paths and optionally set up a war room.[^s1]
2. **Go live and respond fast.** Watch support channels, case queues and system performance, escalate technical issues quickly, and hold daily check-ins or a shared chat channel.[^s1]
3. **Stabilize.** Review the most common cases, refine workflows and update knowledge content based on what users actually ask.[^s1]
4. **Return to normal operations.** Close temporary queues and channels, move cases back to standard workflows, return staffing to usual levels and run a short retrospective.[^s1]

Sitecore adds a named hypercare team (technical lead, implementation team members, a project manager as the single contact for users, and a product owner who prioritizes), real-time monitoring of jobs, logs and failed logins, and a structured feedback loop with power users.[^s4] Typical hypercare metrics are case volume, time to resolution, repeat issue rates, system performance indicators and customer feedback.[^s1]

## Handover to business-as-usual support

The end of hypercare is a handover, and it works best when planned from the start. Microsoft advises beginning the transition to support during implementation, rehearsing it during UAT, and involving future support staff in design, testing and training.[^s3] Its example exit criteria are no critical issues open, key processes running efficiently, SLAs being met, and the support team resolving most issues without extra help.[^s3] In Salesforce's B2C Commerce project methodology the equivalent step is called transition governance: a formal transfer of information in which the build team walks the customer's support team through the solution, followed by documentation and access checks and a project retrospective.[^s2] That Trailhead unit also introduces the customer to Salesforce Support before launch, so the support path is known before it is needed.[^s2]

## Gotchas

- **Unclear escalation paths.** Cases stall when reps do not know who owns a technical fix; define the path before launch.[^s1]
- **Knowledge gaps.** Support reps meet questions the documentation does not answer yet; update articles during stabilization.[^s1]
- **Disappearing partners.** Implementation partner staff may already be on the next phase and resist support work, so agree their hypercare role up front.[^s3]
- **No tested way back.** Trailhead calls the rollback plan the emergency brake and has teams test it before launch.[^s2]
- **Hidden failures.** Monitoring views filtered to the logged-in user can hide background-job failures affecting other users.[^s4]

## Connections

Hypercare sits **broader** under release management, as the final step of putting a release into production, and under change management and adoption, because its first weeks shape whether users trust the new system.[^s1][^s3] It is **part of** application lifecycle management, closing the loop between deployment and steady-state operations.[^s3] It **depends on** a rollback plan, which gives the hypercare team a tested way out if a defect cannot be fixed forward.[^s2] It is **related** to user acceptance testing, where Microsoft recommends rehearsing the support handover;[^s3] to the Center of Excellence and Salesforce governance, which own support after the handover;[^s3] to the statement of work, where a partner's share of post-go-live support should be agreed up front;[^s3] and to Service Cloud, whose case queues, knowledge and dashboards are the tools Salesforce's guidance uses to run hypercare.[^s1]

## Sources

[^s1]: Salesforce, "Hypercare Defined: A Complete Guide with Benefits and Best Practices". https://www.salesforce.com/service/hypercare/ (accessed 2026-11-20)
[^s2]: Trailhead, "Manage the Launch and Post-Launch Activities". https://trailhead.salesforce.com/content/learn/modules/cc-project-mgmt/cc-launch-and-post-launch (accessed 2026-11-20)
[^s3]: Microsoft Learn, "Plan your support operations" (Dynamics 365 implementation guide). https://learn.microsoft.com/en-za/Dynamics365/guidance/implementation-guide/transition-to-support-operations (accessed 2026-11-20)
[^s4]: Sitecore, "Hypercare Strategy" (Accelerate Cookbook for Content Hub). https://developers.sitecore.com/learn/accelerate/content-hub/final-steps/hypercare-strategy (accessed 2026-11-20)
