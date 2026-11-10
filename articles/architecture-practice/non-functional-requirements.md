---
id: kt:non-functional-requirements
type: Concept
title: Non-Functional Requirements
aliases: [NFRs, NFR, quality attribute requirements, quality requirements, quality attributes]
domain: architecture-practice
summary: >-
  Requirements that state how well a Salesforce solution must behave (availability, latency, throughput, scalability,
  recoverability, security, usability) rather than what it does; architects express them as measurable targets and
  design, test and monitor against them within platform limits.
release: "Winter '27"
status: concept
broader: [kt:requirements-engineering]
related: [kt:well-architected-framework, kt:solution-design-tradeoffs, kt:architecture-decision-records, kt:scale-test, kt:testing-strategy]
relations:
  - {predicate: usedBy, object: kt:salesforce-architect}
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: implements, object: kt:iso-iec-25010}
  - {predicate: dependsOn, object: kt:event-monitoring}
sources:
  - id: s1
    title: "Eliciting and Specifying Quality Attribute Requirements"
    publisher: Software Engineering Institute, Carnegie Mellon University
    url: https://apps.dtic.mil/sti/pdfs/ADA585655.pdf
    type: academic
    accessed: 2026-11-10
  - id: s2
    title: "ISO/IEC 25010:2023 — Product quality model"
    publisher: ISO/IEC JTC 1/SC 7
    url: https://committee.iso.org/standard/78176.html
    type: standards-body
    accessed: 2026-11-10
  - id: s3
    title: "Reliability | Well-Architected Framework"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/well-architected/guide/reliability.html
    type: official-docs
    accessed: 2026-11-10
  - id: s4
    title: "Salesforce Well-Architected: Build Well-Architected Solutions"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-well-architected/build-well-architected-solutions
    type: official-learning
    accessed: 2026-11-10
  - id: s5
    title: "Salesforce Architecture Center — Well-Architected overview"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/well-architected/overview
    type: official-docs
    accessed: 2026-11-10
created: 2026-11-10
---

# Non-Functional Requirements

Non-functional requirements (NFRs), which software architecture research calls quality attribute requirements, describe how well a system must do its job rather than which jobs it does. The Software Engineering Institute (SEI) defines quality attributes as measurable or testable properties that show how well a system meets its stakeholders' needs, such as availability, modifiability, performance and security.[^s1] A functional requirement says "agents can escalate a case". The matching NFR says the escalation screen must load within a stated time for a stated number of concurrent agents, and that the escalation service must be available for a stated share of business hours.

## Why architects care

SEI notes that how far a system meets its quality attribute requirements depends directly on its architectural structure. It also observes that these requirements are often poorly elicited, even though architecture depends on them.[^s1] On Salesforce that matters because many NFRs are decided by early, hard-to-reverse choices: synchronous or asynchronous processing, one org or several, real-time integration or batch, and Flow or Apex. A vague NFR such as "the system must be fast" cannot drive any of those choices or be tested at the end.

## Making NFRs measurable

The SEI Quality Attribute Workshop turns vague goals into scenarios. A well-formed scenario names a stimulus, an environment and a response. A refined scenario adds the stimulus source, the affected artifact and a response measure, which is the number that decides pass or fail.[^s1] The workshop brainstorms scenarios, merges duplicates, has stakeholders vote on priorities, and refines only the top scenarios into the full six-part form.[^s1] ISO/IEC 25010:2023 provides a common checklist. Its product quality model has nine characteristics, each split into subcharacteristics, for use in eliciting requirements, setting acceptance criteria and defining quality measures. It replaced the withdrawn 2011 edition.[^s2]

## NFRs on Salesforce

Salesforce Well-Architected is the platform's main guide for quality attributes. Its earlier model described trusted solutions as secure, compliant and reliable, easy solutions as intentional, automated and engaging, and adaptable solutions as resilient and composable.[^s4] The current framework has five pillars: Trust, Reliability, Operational Excellence, Resource and Cost Optimization, and Fairness.[^s5] The Reliability pillar gives the most concrete guidance on turning NFRs into numbers:

- **Set targets from business need.** Match reliability investment to how critical each capability is, and do not demand "five nines" for everything.[^s3]
- **Measure with service level indicators.** Track availability, p50/p95/p99 latency, throughput, error rate and recovery time, measured as completed user journeys rather than component uptime.[^s3]
- **Keep solution SLOs below the platform SLA.** The pillar's example pairs a 99.9% platform SLA with a 99.5% solution service level objective to leave an error budget.[^s3]
- **State RTO and RPO per capability.** Recovery time and data-loss tolerances range from minutes or seconds for revenue and financial data to days for historical reporting.[^s3]
- **Design within governor limits.** Treat about 70% of each governor limit as the ceiling under normal load, which leaves headroom for spikes. Record-triggered automation must handle 200 records per invocation.[^s3]

## Limits and gotchas

Platform guarantees do not cover the NFRs you own. Salesforce runs infrastructure failover, but the Reliability pillar says application-layer reliability stays the customer's responsibility whatever the SLA tier.[^s3] Cross-region disaster recovery is a separate paid offering, and multi-org architectures are worth their complexity only when business requirements demand them.[^s3] Performance NFRs need production-scale evidence. The pillar recommends load tests against Full Copy sandboxes with realistic data volumes, concurrent-user and API tests, and Scale Test on Hyperforce Full Copy sandboxes.[^s3] Monitoring has license implications, because some Event Monitoring features need an add-on or Shield and Proactive Monitoring requires Signature Success.[^s3] Recoverability NFRs need restores that are actually tested. The pillar suggests validating restores quarterly, because native Data Export runs only weekly or monthly and offers no point-in-time recovery.[^s3]

## Connections

NFRs sit **broader** under requirements engineering, the discipline that elicits and manages all requirements. They are **used by** the Salesforce architect role, who turns them into designs.[^s1] They **implement** the ISO/IEC 25010 quality model as a shared vocabulary.[^s2] On Salesforce they are **governed by** governor limits, which set hard ceilings on throughput and transaction size,[^s3] and they **depend on** Event Monitoring and similar telemetry to be verified in production.[^s3] They are **related** to the Well-Architected Framework, which organizes quality goals into pillars,[^s5] and to solution design trade-offs and architecture decision records, where competing NFRs are weighed and the choice is written down. Scale Test and the testing strategy are where performance and scalability NFRs are proven before go-live.[^s3]

## Sources

[^s1]: Software Engineering Institute, Carnegie Mellon University, "Eliciting and Specifying Quality Attribute Requirements" (R. Wojcik, 2013). https://apps.dtic.mil/sti/pdfs/ADA585655.pdf (accessed 2026-11-10)
[^s2]: ISO/IEC JTC 1/SC 7, "ISO/IEC 25010:2023 — Systems and software engineering — SQuaRE — Product quality model". https://committee.iso.org/standard/78176.html (accessed 2026-11-10)
[^s3]: Salesforce Architects, "Reliability | Well-Architected Framework". https://architect.salesforce.com/docs/architect/well-architected/guide/reliability.html (accessed 2026-11-10)
[^s4]: Trailhead, "Salesforce Well-Architected: Build Well-Architected Solutions". https://trailhead.salesforce.com/content/learn/modules/salesforce-well-architected/build-well-architected-solutions (accessed 2026-11-10)
[^s5]: Salesforce Architects, "Salesforce Architecture Center — Well-Architected overview". https://architect.salesforce.com/well-architected/overview (accessed 2026-11-10)
