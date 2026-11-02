---
id: kt:technical-debt-in-salesforce
type: Concept
title: Technical Debt in Salesforce
aliases: [Salesforce tech debt, org technical debt, configuration debt, org clutter]
domain: architecture-practice
summary: >-
  The accumulated cost of expedient configuration and code choices in a Salesforce org (unused metadata,
  outdated automation, hard-coded references, untestable code) that makes later change slower, riskier or impossible.
release: "Winter '27"
status: concept
broader: [kt:well-architected-framework]
related: [kt:solution-design-tradeoffs, kt:code-analyzer, kt:salesforce-optimizer, kt:org-check, kt:apex-triggers, kt:workflow-rules]
sources:
  - id: s1
    title: "Report from Dagstuhl Seminar 16162: Managing Technical Debt in Software Engineering"
    publisher: Dagstuhl Reports (Schloss Dagstuhl)
    url: https://utupub.fi/bitstream/10024/169748/1/dagrep_v006_i004_p110_s16162.pdf
    type: academic
    accessed: 2026-11-02
  - id: s2
    title: "Tech Debt: What It Is and Why You Should Care"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2021/tech-debt-what-it-is-and-why-you-should-care
    type: official-blog
    accessed: 2026-11-02
  - id: s3
    title: "Code Quality Patterns (Well-Architected: Resource and Cost Optimization)"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/well-architected/guide/resource-and-cost-optimization-code-quality-patterns.html
    type: official-docs
    accessed: 2026-11-02
  - id: s4
    title: "Run a Report and Review the Findings (Salesforce Optimizer)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-optimizer/run-a-report-and-review-the-findings
    type: official-learning
    accessed: 2026-11-02
  - id: s5
    title: "Technical Debt: Eliminate Technical Debt to Transform Your Salesforce Org"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/technical-debt
    type: official-learning
    accessed: 2026-11-02
created: 2026-11-02
---

# Technical Debt in Salesforce

Technical debt is the software-engineering name for design and implementation shortcuts that pay off now but make future change more expensive. The widely cited consensus definition from the 2016 Dagstuhl seminar on managing technical debt describes it as constructs that are expedient in the short term yet set up a context in which later changes become costlier or impossible, and it limits the liability to internal qualities, chiefly maintainability and evolvability.[^s1] In a Salesforce org the "constructs" are as often declarative metadata (fields, flows, profiles, page layouts) as they are Apex or Lightning Web Components, so debt accumulates even in orgs that contain little code.[^s2]

## Where it comes from

Salesforce's admin guidance names two root causes. Under deadline pressure, builders ship the first solution that works rather than the one that scales; and because the platform and the team's knowledge keep moving, yesterday's sound design becomes today's outdated one.[^s2] Debt is not automatically bad: a deliberate shortcut can be the right call, but leaving it unpaid raises the cost of every later maintenance task and enhancement.[^s2] The Well-Architected code-quality guidance describes the failure mode for teams that never budget for repayment: debt is talked about but never recorded, sprints leave no room for remediation, and the backlog surfaces as a large refactoring project every 18 to 24 months.[^s3]

## What it looks like in an org

Common forms of declarative debt include inactive validation rules, flows, processes and workflow rules; profiles, permission sets, roles, groups, page layouts and record types assigned to nobody; active users who have not logged in for a long time; unused reports, dashboards and list views; and solutions built on features Salesforce has since superseded.[^s2] Hard-coded record IDs and other literal references, in configuration or code, are a recurring item because they break silently between sandboxes and production.[^s2] Well-Architected also calls out configuration debt from unused custom metadata types and custom settings that pile up over time.[^s3]

In code, the anti-patterns are familiar: business logic written directly in trigger files that grow beyond 300 lines and resist testing, and SOQL or DML inside loops that risks the 100-query and 150-DML-statement limits during bulk operations.[^s3] The recommended shape is the opposite: thin triggers delegating to handler classes, business logic in service classes, SOQL centralised in selector classes, and code organised into packages with one-directional dependencies.[^s3]

## Finding and measuring it

Salesforce Optimizer, launched from Setup, scans an org and reports findings such as objects with more than 350 fields (the per-object maximum is 800, depending on edition), heavy concentrations of sharing rules, flows and validation rules on one object, multiple Apex triggers on the same object, and too many users holding both Modify All Data and Customize Application.[^s4] It runs in production and sandbox orgs of Professional, Enterprise, Performance, Unlimited and Developer editions and usually finishes within an hour.[^s4] The free Salesforce Labs app Org Check applies rules across org components to flag unused licences, missing descriptions, hard-coded IDs and unreferenced components.[^s2] For code, Well-Architected recommends wiring static analysis, ApexGuru and complexity metrics into pull-request validation.[^s3] Trailhead's Technical Debt module frames remediation around prioritising by risk, with units on security gaps, a single source of truth for data and modernising automations.[^s5]

## Managing it

- **Make it visible.** Track each debt item in the backlog with context, business impact and an effort estimate, rather than in hallway conversation.[^s3]
- **Pay down continuously.** Fix debt during related feature work (the "boy scout rule") and let code review verify the improvement; enforce CI/CD quality gates that block merges instead of bypassing them under schedule pressure.[^s3]
- **Split quick wins from projects.** Salesforce's admin guidance suggests one plan for small cleanups of about 30 to 60 minutes that fit into every sprint and a second backlog for larger rework, such as migrating old automation to Flow when it is next enhanced.[^s2]
- **Prevent new debt.** Record Architecture Decision Records in version control and compare the total cost of ownership of declarative and custom options before building.[^s3]

## Connections

Technical debt sits **under** `kt:well-architected-framework`, whose Resource and Cost Optimization code-quality guidance supplies the patterns and anti-patterns above.[^s3] It is **related** to `kt:solution-design-tradeoffs`, because every expedient choice is a trade-off whose cost should be recorded.[^s1][^s3] Detection tools `kt:salesforce-optimizer`, `kt:org-check` and `kt:code-analyzer` (static analysis in the pull-request gate) surface it.[^s4][^s2][^s3] `kt:apex-triggers` is a frequent source when logic lives in trigger bodies or several triggers share an object, and `kt:workflow-rules` represent automation built on superseded features that teams migrate to Flow.[^s3][^s4][^s2]

## Sources

[^s1]: Avgeriou, Kruchten, Ozkaya and Seaman (eds.), "Managing Technical Debt in Software Engineering (Dagstuhl Seminar 16162)", Dagstuhl Reports 6(4), 2016. https://utupub.fi/bitstream/10024/169748/1/dagrep_v006_i004_p110_s16162.pdf (accessed 2026-11-02)
[^s2]: Salesforce Admins Blog, "Tech Debt: What It Is and Why You Should Care" (updated 2025). https://admin.salesforce.com/blog/2021/tech-debt-what-it-is-and-why-you-should-care (accessed 2026-11-02)
[^s3]: Salesforce Architects, "Code Quality Patterns" (Well-Architected). https://architect.salesforce.com/docs/architect/well-architected/guide/resource-and-cost-optimization-code-quality-patterns.html (accessed 2026-11-02)
[^s4]: Trailhead, "Run a Report and Review the Findings" (Salesforce Optimizer). https://trailhead.salesforce.com/content/learn/modules/salesforce-optimizer/run-a-report-and-review-the-findings (accessed 2026-11-02)
[^s5]: Trailhead, "Technical Debt" module. https://trailhead.salesforce.com/content/learn/modules/technical-debt (accessed 2026-11-02)
