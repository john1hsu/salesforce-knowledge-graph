---
id: kt:risk-and-assumption-logs
type: ExternalConcept
title: Risk and Assumption Logs
aliases: [RAID log, risk register, assumptions log, risk and issue log]
domain: architecture-practice
summary: >-
  Living project registers that record each identified risk with its probability, impact, owner and response, and
  each planning assumption with what happens if it proves false; a general project-management practice that
  Salesforce implementation teams and architects use to surface and govern delivery and design risk.
release: "Winter '27"
status: concept
broader: [kt:salesforce-governance]
related: [kt:architecture-decision-records, kt:non-functional-requirements, kt:solution-design-tradeoffs, kt:salesforce-center-of-excellence, kt:einstein-trust-layer]
relations:
  - {predicate: usedBy, object: kt:salesforce-architect}
  - {predicate: contrastsWith, object: kt:architecture-decision-records}
sources:
  - id: s1
    title: "Project Risk Management Techniques (Best Practices for Project Management module)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/best-practices-for-project-management/manage-risk
    type: official-learning
    accessed: 2026-11-12
  - id: s2
    title: "Conduct a Risk Assessment for AI Projects"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=generative_ai_plan_trust.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-12
  - id: s3
    title: "Chapter 20: Risk management (Government Project Delivery Framework, Teal Book)"
    publisher: UK Government Project Delivery Function
    url: https://projectdelivery.gov.uk/teal-book/home/part-e-planning-and-control/chapter-20-risk-management/
    type: government
    accessed: 2026-11-12
  - id: s4
    title: "Risks vs. issues"
    publisher: PMI (PM Network, D. Sankararajan and N. K. Shrivastava, 2012)
    url: https://www.pmi.org/learning/library/risks-vs-issues-project-failure-2328
    type: community
    accessed: 2026-11-12
created: 2026-11-12
---

# Risk and Assumption Logs

A risk log (usually called a risk register) is the running list of uncertain events that could affect a project, each scored and assigned a response; an assumption log records the things the plan takes as true without full evidence. Trailhead's project-management content treats the risk register as the standard place to record risks once they are identified, and names brainstorming and interviews as the usual ways to find them.[^s1] UK government delivery guidance folds the two together: significant assumptions should be logged as risks, stating the assumption and the impact if it turns out to be false.[^s3] Many teams extend the pair into a combined "RAID" log of risks, assumptions, issues and dependencies.

## What goes in the register

Trailhead's example register captures the risk type (threat), a source category such as strategic, operational, technical or compliance, a name, and a description of the consequence, for instance downtime that leaves customer data unavailable.[^s1] The UK Teal Book lists a fuller set of fields: an ID, date raised, cause/event/impact description, category, owner, likelihood and impact scores, current and target ratings, response actions and residual rating. Closed risks stay on the register with the date, reason and who closed them, so the history survives for lessons learned.[^s3]

## Scoring and exposure

The Trailhead unit uses a simple qualitative method. Probability and impact are each rated 1 (low) to 3 (high), the risk score is their product, and scores of 1–3, 4–6 and 7–9 count as low, moderate and high exposure. Averaging the individual scores gives an overall project exposure; in the worked example, four risks totalling 24 average 6, a moderate exposure at which the team chose to proceed.[^s1] The unit stresses that this is iterative: the register is revisited and updated throughout the project rather than filled in once at kickoff.[^s1]

## Owners and responses

Every risk needs one named owner with the authority or expertise to plan, carry out and monitor its response, and no single owner should be overloaded.[^s3] Trailhead adds that sponsors, key stakeholders and subject-matter experts should help identify risks and own some of them, because the project team alone may miss strategic or functional exposure.[^s1] Responses to threats are to avoid, treat, transfer, share or accept them; opportunities can be exploited, enhanced, shared or rejected. Approved responses go into the plan, residual risk is recorded, and a risk that exceeds its tolerance is escalated to a more senior manager.[^s3]

## Risks versus issues

The distinction is timing. A risk is a future, uncertain event, while an issue has already happened and needs action now, so risks get mitigation plans and issues get prioritized resolution plans.[^s4] When a risk materializes it moves to the issue log and the risk is closed on the register.[^s3][^s4] PMI authors suggest weighting attention toward the risk register early in a project, when uncertainty is highest, and toward the issue log near the end. They also suggest reviewing which issues were never logged as risks, to improve identification on the next project.[^s4]

## Applying it on Salesforce projects

Salesforce applies the same discipline to generative AI. Before grounding prompts in business or customer data, teams are told to identify the risks (breaches, compliance problems, reputational harm), work with stakeholders to estimate how likely each is to cause harm, and document a prioritized list of risk areas alongside the specific guardrails that mitigate each one.[^s2] Many of those guardrails come from the Einstein Trust Layer, including secure data retrieval, data masking, zero data retention, prompt-injection defense and toxicity detection.[^s2]

Practical gotchas:

- Log significant assumptions as risks, recording what happens to the plan if each proves false.[^s3]
- Keep closed risks visible instead of deleting them, so later teams can trace why a mitigation exists.[^s3]
- Don't let the log replace action: an issue cannot be "mitigated," it has to be resolved.[^s4]

## Connections

The practice sits under `kt:salesforce-governance`, since the register is how a governance body sees and escalates delivery risk against agreed tolerances.[^s3] It is **used by** the `kt:salesforce-architect`, and it **contrasts with** `kt:architecture-decision-records`: an ADR captures a choice that has been made and its accepted consequences, while the risk log tracks uncertainty that is still open. A design trade-off in `kt:solution-design-tradeoffs` often creates a residual risk that belongs on the log, and an unverified volume or performance target in `kt:non-functional-requirements` is a classic assumption to record.[^s3] A `kt:salesforce-center-of-excellence` is a natural home for a register shared across projects, because it is the body that sets tolerances and receives escalations.[^s3] For AI work, each logged risk is mapped to a guardrail, and many of those guardrails come from the `kt:einstein-trust-layer`.[^s2]

## Sources

[^s1]: Salesforce Trailhead, "Project Risk Management Techniques", Best Practices for Project Management module. https://trailhead.salesforce.com/content/learn/modules/best-practices-for-project-management/manage-risk (accessed 2026-11-12)
[^s2]: Salesforce Help, "Conduct a Risk Assessment for AI Projects". https://help.salesforce.com/s/articleView?id=generative_ai_plan_trust.htm&language=en_US&type=5 (accessed 2026-11-12)
[^s3]: UK Government Project Delivery Function, "Chapter 20: Risk management", Government Project Delivery Framework (Teal Book). https://projectdelivery.gov.uk/teal-book/home/part-e-planning-and-control/chapter-20-risk-management/ (accessed 2026-11-12)
[^s4]: D. Sankararajan and N. K. Shrivastava, "Risks vs. issues", PM Network 26(6), PMI, 2012. https://www.pmi.org/learning/library/risks-vs-issues-project-failure-2328 (accessed 2026-11-12)
