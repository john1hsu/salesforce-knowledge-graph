---
id: kt:cta-review-board
type: Certification
title: CTA Review Board
aliases: [Technical Architect Review Board, CTA board exam, Technical Architect Review Board Exam, Architect Review Board Evaluation]
domain: architecture-practice
summary: >-
  The scenario-based, judged assessment that grants the Salesforce Certified Technical Architect (CTA) credential:
  candidates design an end-to-end solution to a hypothetical case under time pressure, present it to a panel of CTA
  judges and defend it in Q&A, after first passing a shorter Architect Review Board Evaluation.
release: "Winter '27"
status: current
broader: [kt:certified-technical-architect]
related: [kt:salesforce-architect, kt:well-architected-framework, kt:solution-design-tradeoffs, kt:salesforce-architecture-center, kt:data-architecture, kt:integration-patterns]
relations:
  - {predicate: dependsOn, object: kt:application-architect-certification}
  - {predicate: dependsOn, object: kt:system-architect-certification}
  - {predicate: usedBy, object: kt:salesforce-architect}
sources:
  - id: s1
    title: "Certified Technical Architect Credential"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/architectreviewboard
    type: official-learning
    accessed: 2026-11-04
  - id: s2
    title: "5 Salesforce Architecture Resources Every CTA Candidate Should Use"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/architecture-resources-for-cta/
    type: official-blog
    accessed: 2026-11-04
  - id: s3
    title: "Becoming a Salesforce Certified Technical Architect, 2nd Edition — The CTA review board's structure and format"
    publisher: Packt
    url: https://packtpub.com/en-ph/product/becoming-a-salesforce-certified-technical-architect-9781803239439/chapter/chapter-1-starting-your-journey-as-a-cta-1/section/the-cta-review-boards-structure-and-format-ch01lvl1sec03
    type: textbook
    accessed: 2026-11-04
  - id: s4
    title: "Salesforce CTA Review Board to Become Virtual"
    publisher: Salesforce Ben
    url: https://www.salesforceben.com/salesforce-cta-review-board-to-become-virtual/
    type: news
    accessed: 2026-11-04
created: 2026-11-04
---

# CTA Review Board

The CTA Review Board is the final, judged assessment for the Salesforce Certified Technical Architect credential, the top rung of the Salesforce architect credential ladder. Unlike the multiple-choice exams below it, the board tests whether a candidate can design a complete solution for a realistic business scenario and then justify it live. Trailhead structures the credential as two steps: an Architect Review Board Evaluation followed by the Technical Architect Review Board Exam, and both must be passed to earn the CTA.[^s1]

## Eligibility

To initially qualify, a candidate must already hold the System Architect and Application Architect credentials, which themselves are earned by stacking domain architect certifications.[^s1] Registration includes a prerequisite review before the candidate is scheduled. Salesforce also recommends extensive hands-on experience and a personal study plan, and offers CTA601, an expert-led virtual workshop through Trailhead Academy, for experienced architects preparing for the board.[^s1]

## How it works

Both steps follow the same rhythm: read a hypothetical scenario, design and justify a solution in a fixed preparation window, present it, then face questions.[^s1] The published timings are:

| Step | Delivery | Preparation | Presentation | Q&A | Other |
|---|---|---|---|---|---|
| Architect Review Board Evaluation | Online only | 60 min | 30 min | 30 min | 45 min feedback and discussion |
| Technical Architect Review Board Exam | Online or in-person | 180 min | 45 min | 40 min | —[^s1] |

The evaluation is assigned to a CTA after the prerequisite review and ends with a dedicated feedback block, so it doubles as a calibrated rehearsal for the full exam.[^s1] Fees listed on Trailhead are $1,500 USD to register for the evaluation ($750 retake) and $4,500 USD for the exam ($2,250 retake), plus applicable taxes.[^s1]

In the full exam the presentation must walk end to end through the solution and show how each element answers the scenario's requirements. A panel of three CTA judges then probes and challenges it; candidates are expected to defend their choices and adjust the design where a challenge exposes a gap.[^s3]

## Artifacts and tooling

Candidates present diagrams such as a system landscape and data model rather than prose alone. In 2023 Salesforce moved the exam to digitally produced artifacts built with designated tools and stopped accepting hand-drawn diagrams; the board had already gone online in 2020.[^s4] Since then Trailhead has listed the exam itself as available online or in person, while the evaluation step remains online only.[^s1]

## Limits and gotchas

- The credential page does not publish the domain weightings; it points candidates to a separate exam guide and tells them to self-study each domain focus area.[^s1]
- A common failure mode is the "per-requirement trap": answering every requirement well in isolation while the overall design becomes fragmented, for example mixing an LWC for one form and a screen flow for another without a coherent reason.[^s2]
- Knowledge alone rarely fails candidates; Salesforce's architecture evangelists argue the gap is usually a connecting mental model plus the ability to reason quickly and communicate trade-offs under time pressure.[^s2]
- Fees and timings are stated as published at the time of writing and can change between releases; check the credential page before registering.[^s1]

## Preparing with official resources

Salesforce's Architecture Program recommends five resource families for CTA candidates: fundamentals content on how the platform works (multitenancy, sharing, integration patterns), the Reference Architecture and Data Model galleries, decision guides (building forms, record-triggered automation, asynchronous processing, data integration), the Well-Architected Framework, and the architecture blog including its communication-focused series.[^s2] It specifically suggests reproducing the data models of in-scope clouds such as Sales, Service and Experience Cloud, and presenting mock boards to people unfamiliar with the solution.[^s2]

## Connections

The board is the assessment component of `kt:certified-technical-architect`, so that credential is its broader node; it `dependsOn` the Application Architect and System Architect certifications that gate eligibility.[^s1] It validates the `kt:salesforce-architect` role at its most senior level.[^s1] Defending a design before judges means articulating `kt:solution-design-tradeoffs` concisely, and Salesforce points candidates to the `kt:well-architected-framework` and the decision guides and galleries of the `kt:salesforce-architecture-center` to structure them, with `kt:data-architecture` and `kt:integration-patterns` among the fundamentals a board solution must cover.[^s2]

## Sources

[^s1]: Trailhead, "Certified Technical Architect Credential". https://trailhead.salesforce.com/credentials/architectreviewboard (accessed 2026-11-04)
[^s2]: Salesforce, "5 Salesforce Architecture Resources Every CTA Candidate Should Use" (Lilith Van Biesen, 2026-06-24). https://www.salesforce.com/blog/architecture-resources-for-cta/ (accessed 2026-11-04)
[^s3]: Bahri Bahri, *Becoming a Salesforce Certified Technical Architect*, 2nd ed. (Packt, 2023), "The CTA review board's structure and format". https://packtpub.com/en-ph/product/becoming-a-salesforce-certified-technical-architect-9781803239439/chapter/chapter-1-starting-your-journey-as-a-cta-1/section/the-cta-review-boards-structure-and-format-ch01lvl1sec03 (accessed 2026-11-04)
[^s4]: Lars Malmqvist, "Salesforce CTA Review Board to Become Virtual", Salesforce Ben (updated 2023-10-30). https://www.salesforceben.com/salesforce-cta-review-board-to-become-virtual/ (accessed 2026-11-04)
