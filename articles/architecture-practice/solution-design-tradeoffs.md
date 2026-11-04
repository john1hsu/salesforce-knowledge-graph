---
id: kt:solution-design-tradeoffs
type: Concept
title: Solution Design Trade-offs
aliases: [architecture trade-offs, design trade-offs, architectural tradeoff analysis, trade-off analysis]
domain: architecture-practice
summary: >-
  The practice of choosing between competing Salesforce design options (Flow vs. Apex, sync vs. async, click vs. code,
  agentic vs. deterministic) by making explicit which quality attributes each option improves or degrades, and recording why.
release: "Winter '27"
status: concept
broader: [kt:well-architected-framework]
related: [kt:technical-debt-in-salesforce, kt:salesforce-architecture-center, kt:record-triggered-flow, kt:apex-triggers, kt:architecture-decision-records]
relations:
  - {predicate: usedBy, object: kt:salesforce-architect}
  - {predicate: coveredBy, object: kt:certified-technical-architect}
sources:
  - id: s1
    title: "The Architecture Tradeoff Analysis Method (CMU/SEI-98-TR-008)"
    publisher: Software Engineering Institute, Carnegie Mellon University
    url: https://apps.dtic.mil/sti/pdfs/ADA350761.pdf
    type: academic
    accessed: 2026-11-04
  - id: s2
    title: "Architect Decision Guides"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/decision-guides
    type: official-docs
    accessed: 2026-11-04
  - id: s3
    title: "Record-Triggered Automation Decision Guide"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/decision-guides/guide/record-triggered
    type: official-docs
    accessed: 2026-11-04
  - id: s4
    title: "Introducing the New Salesforce Decision Guide Format"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/new-salesforce-decision-guide-format/
    type: official-blog
    accessed: 2026-11-04
  - id: s5
    title: "Well-Architected Overview"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/well-architected/overview
    type: official-docs
    accessed: 2026-11-04
  - id: s6
    title: "How to Make Salesforce Architecture Decisions That Actually Last"
    publisher: Salesforce Ben
    url: https://www.salesforceben.com/how-to-make-salesforce-architecture-decisions-that-actually-last/
    type: community
    accessed: 2026-11-04
created: 2026-11-04
---

# Solution Design Trade-offs

A solution design trade-off is a choice in which improving one quality of a system (performance, security, maintainability, cost, speed of delivery) knowingly weakens another. Software-architecture research has long observed that architects make such choices constantly but often without a principled way to analyse them; the Software Engineering Institute's Architecture Tradeoff Analysis Method (ATAM) was created to make the reasoning explicit by evaluating a design against several quality attributes at once.[^s1] On Salesforce the same idea underpins the Architecture Center: its decision guides are presented as tools for analysing trade-offs and selecting the right platform tools rather than as declarations of one correct answer.[^s2]

## Core vocabulary

ATAM introduced two terms that remain useful in Salesforce design reviews. A **sensitivity point** is a design element where a change noticeably moves one quality attribute; a **tradeoff point** is an element that several attributes are sensitive to at once, so tuning it helps one quality while hurting another.[^s1] The SEI's worked example showed that adding servers raised performance and availability while weakening security, which made server count a tradeoff point.[^s1] In Salesforce terms, the number of automations firing on one object is a comparable tradeoff point: it affects performance, recursion risk and who on the team can maintain the logic.[^s3]

## How Salesforce frames recurring trade-offs

The Architecture Center's decision guides each target a recurring choice: agentic vs. traditional workflow automation, record-triggered automation, asynchronous processing, building forms, event-driven architecture, data integration, and Data 360 provisioning and interoperability.[^s2] They name the criteria to weigh, for example execution path, goal complexity and modality mix for agentic automation, or latency, cost, scalability, governance and complexity for Data 360 interoperability.[^s2] In 2026 Salesforce restructured the guides so that key decision points come first, followed by a product comparison, use cases and a dedicated section on non-functional "ilities" such as scalability and adaptability, explicitly so architects weigh trade-offs before diving into detail.[^s4]

The record-triggered automation guide is the clearest worked example. It measures **automation density** across three dimensions (number of automations, records per transaction, downstream DML) and maps it to a standard: fewer than 15 automations with 0–1 downstream DML points to record-triggered Flow; 15–30 with 2–4 to a hybrid of Flow plus invocable Apex; more than 30, or 5+ downstream DML, to an Apex trigger framework.[^s3] The trade-off is explicit: Flow is quicker to build, maintainable by admins and bulkifies automatically, while Apex offers savepoints, partial DML and richer data structures but demands developer skills and manual bulkification.[^s3] Team skills are therefore treated as a design input, not an afterthought.[^s3]

At the framework level, Well-Architected now organises qualities into five areas (Trust, Reliability, Operational Excellence, Resource and Cost Optimization, Fairness) and positions itself as help for navigating trade-offs among them, pointing to decision guides and patterns for the specifics.[^s5]

## Making trade-offs durable

Common Salesforce examples include Flow vs. Apex, synchronous vs. asynchronous integration, Platform Events vs. Change Data Capture, data replication vs. virtualisation, and permission set groups vs. profiles; none has a universally right answer, because the choice depends on scale, skills, compliance and expected change.[^s6] Practitioners therefore recommend recording each significant choice in an architecture decision record that lists the options considered, the constraints at the time, the risks knowingly accepted and the conditions that should trigger a revisit, such as volume growth or a new platform capability.[^s6] ATAM likewise counts documented design rationale among the method's main benefits, and stresses analysing early, when changing course is cheapest.[^s1]

## Gotchas

- Treating a guide's default as a rule: the decision guides warn where a tool is a poor fit, so the scenario still has to be scored against the criteria.[^s2]
- Mixing approaches without governance: the record-triggered guide advises one entry point per object, because combining flows and triggers on the same object fragments ownership and makes ordering unpredictable.[^s3]
- Leaving rationale unwritten: when decision-makers leave, only outcomes remain and settled debates get reopened.[^s6]

## Connections

Trade-off analysis sits **under** `kt:well-architected-framework`, whose pillars supply the qualities being traded.[^s5] The `kt:salesforce-architecture-center` hosts the decision guides that apply it to specific choices.[^s2][^s4] `kt:record-triggered-flow` and `kt:apex-triggers` are the two sides of its best-documented example.[^s3] Unrecorded or unrevisited trade-offs become `kt:technical-debt-in-salesforce`, which is why `kt:architecture-decision-records` capture the accepted risks and revisit triggers.[^s6] The practice is **used by** every `kt:salesforce-architect` and is what the `kt:certified-technical-architect` credential tests when candidates justify their designs.[^s1][^s2]

## Sources

[^s1]: Kazman, Klein, Barbacci, Longstaff, Lipson and Carriere, "The Architecture Tradeoff Analysis Method", CMU/SEI-98-TR-008, Software Engineering Institute, 1998. https://apps.dtic.mil/sti/pdfs/ADA350761.pdf (accessed 2026-11-04)
[^s2]: Salesforce Architects, "Architect Decision Guides". https://architect.salesforce.com/decision-guides (accessed 2026-11-04)
[^s3]: Salesforce Architects, "Record-Triggered Automation Decision Guide". https://architect.salesforce.com/docs/architect/decision-guides/guide/record-triggered (accessed 2026-11-04)
[^s4]: Salesforce, "Introducing the New Salesforce Decision Guide Format" (March 2026). https://www.salesforce.com/blog/new-salesforce-decision-guide-format/ (accessed 2026-11-04)
[^s5]: Salesforce Architects, "Well-Architected Overview". https://architect.salesforce.com/well-architected/overview (accessed 2026-11-04)
[^s6]: Senthil Jayachandran, "How to Make Salesforce Architecture Decisions That Actually Last", Salesforce Ben. https://www.salesforceben.com/how-to-make-salesforce-architecture-decisions-that-actually-last/ (accessed 2026-11-04)
