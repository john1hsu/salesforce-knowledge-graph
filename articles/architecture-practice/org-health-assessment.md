---
id: kt:org-health-assessment
type: Concept
title: Org Health Assessment
aliases: [Salesforce org health assessment, org health check, org health review, technical health review, Org Health Accelerator]
domain: architecture-practice
summary: >-
  A structured review of an existing Salesforce org's configuration, code, security settings, limits and adoption
  that combines scanner output (Optimizer, Health Check, Health Insights) with expert judgment to produce a prioritized
  list of risks and remediation work.
release: "Winter '27"
status: concept
broader: [kt:well-architected-framework, kt:salesforce-governance]
related: [kt:technical-debt-in-salesforce, kt:org-check, kt:salesforce-center-of-excellence, kt:salesforce-health-insights]
relations:
  - {predicate: dependsOn, object: kt:salesforce-optimizer}
  - {predicate: dependsOn, object: kt:security-health-check}
sources:
  - id: s1
    title: "Salesforce Org Health Accelerator (datasheet)"
    publisher: Salesforce
    url: https://www.salesforce.com/assets/pdf/success-services/salesforce-org-health.pdf
    type: official-docs
    accessed: 2026-11-27
  - id: s2
    title: "Salesforce Health Insights: Know What to Fix First"
    publisher: Salesforce Blog
    url: https://salesforce.com/blog/salesforce-health-insights
    type: official-blog
    accessed: 2026-11-27
  - id: s3
    title: "Run a Scan and Review the Findings (Salesforce Optimizer)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-optimizer/run-a-report-and-review-the-findings
    type: official-learning
    accessed: 2026-11-27
  - id: s4
    title: "Improve Your Org's Security with Salesforce Health Check"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/security_basics/security_basics_healthcheck
    type: official-learning
    accessed: 2026-11-27
  - id: s5
    title: "Well-Architected Framework"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/well-architected/guide/framework.html
    type: official-docs
    accessed: 2026-11-27
  - id: s6
    title: "Signature Success Plan"
    publisher: Salesforce
    url: https://salesforce.com/eu/services/success-plans/accelerators/org-health-assessment
    type: official-docs
    accessed: 2026-11-27
created: 2026-11-27
---

# Org Health Assessment

An org health assessment is a point-in-time review of a live Salesforce org that asks whether its configuration, customizations, security posture and adoption are still fit for what the business wants to do next. It is usually run before a major expansion, a merger of orgs, a new cloud rollout or a hand-over to a new team. Salesforce's own consultant-led version, the Org Health Accelerator, was positioned for long-time customers planning large projects, with the goals of lower operating cost and faster return on investment.[^s1] Unlike a go-live readiness assessment, which gates a launch, a health assessment looks at an org that is already in production.

## How it works

A typical assessment has three phases, mirroring the structure of Salesforce's accelerator:[^s1]

- **Discovery.** Agree the business goals and measurable success criteria, and run the built-in scanners.[^s1]
- **Analysis.** Review adoption, declarative customizations, sandbox and environment strategy, triggers and Apex.[^s1]
- **Readout.** Present findings ranked by impact, with best practices and a remediation plan.[^s1]

The accelerator datasheet describes a Certified Specialist delivering this over two to three calls (about 2.5 hours in total) across two to four weeks, for customers on Premier or Signature Success Plans; it dates from 2018, so treat the format as illustrative rather than current.[^s1] Salesforce now lists an annual technical health review, Proactive Monitoring of more than 50 implementation health metrics, and Salesforce Health Insights among Signature Success Plan benefits.[^s6]

## The tooling

Scanners do the mechanical part and free the reviewer to judge trade-offs:

- **Salesforce Optimizer** scans an org (production or sandbox) and lists findings, putting items that need review first; the scan typically finishes within an hour.[^s3]
- Optimizer flags, for example, objects with more than 350 fields, multiple Apex triggers on one object, and too many users holding both Modify All Data and Customize Application.[^s3]
- **Health Check** scores security settings from 0 to 100 against Salesforce's standard baseline, or against a custom XML baseline for regulated industries.[^s4]
- Health Check's Fix Risks button resets every flagged setting at once and can break integrations or access, so test fixes in a sandbox first.[^s4]
- **Salesforce Health Insights**, available with Winter '27 for Signature customers on core products, scans on demand and ranks findings from Critical to Compliant.[^s2]
- Health Insights covers product adoption (owned versus used capabilities, 30-day license utilization) and implementation health across security and process automation, drawing on Well-Architected guidance.[^s2]

Salesforce contrasts the in-app scan with a manual review that can take up to three weeks, which is the main reason to start any assessment from tool output.[^s2]

## Gotchas and good practice

Scanner output is evidence, not a verdict. A flagged object with hundreds of fields may be justified by the data model; a low Health Check score may reflect a deliberate, documented exception. The reviewer's job is to connect findings to business risk and cost. The Well-Architected Framework is not an implementation guide, but Salesforce suggests using its pillar documents as a structured checklist for design reviews and for improving an existing implementation, which gives the assessment a consistent rubric.[^s5] Keep the scope explicit, involve stakeholders who will speak openly about pain points, and make the readout actionable: an owner, effort estimate and priority for each item.[^s1] Re-run the scanners after remediation so the next assessment has a baseline.[^s3]

## Connections

The assessment sits under the Well-Architected Framework, whose pillars supply its review criteria, and under Salesforce governance, because findings feed the backlog that a design authority or Center of Excellence prioritizes.[^s5] It depends on Salesforce Optimizer and Security Health Check for raw findings, and increasingly on Salesforce Health Insights for prioritized, continuous scanning.[^s3][^s4][^s2] It is **related** to technical debt, since findings such as redundant triggers or oversized objects are debt made visible,[^s3] and to Org Check, another org-inspection tool in this graph.

## Sources
[^s1]: Salesforce, "Salesforce Org Health Accelerator" (datasheet). https://www.salesforce.com/assets/pdf/success-services/salesforce-org-health.pdf (accessed 2026-11-27)
[^s2]: Salesforce Blog, "Salesforce Health Insights: Know What to Fix First". https://salesforce.com/blog/salesforce-health-insights (accessed 2026-11-27)
[^s3]: Trailhead, "Run a Scan and Review the Findings" (Salesforce Optimizer). https://trailhead.salesforce.com/content/learn/modules/salesforce-optimizer/run-a-report-and-review-the-findings (accessed 2026-11-27)
[^s4]: Trailhead, "Improve Your Org's Security with Salesforce Health Check". https://trailhead.salesforce.com/content/learn/modules/security_basics/security_basics_healthcheck (accessed 2026-11-27)
[^s5]: Salesforce Architects, "Well-Architected Framework". https://architect.salesforce.com/docs/architect/well-architected/guide/framework.html (accessed 2026-11-27)
[^s6]: Salesforce, "Signature Success Plan". https://salesforce.com/eu/services/success-plans/accelerators/org-health-assessment (accessed 2026-11-27)
