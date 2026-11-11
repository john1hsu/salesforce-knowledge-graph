---
id: kt:development-lifecycle-and-deployment-architect-certification
type: Certification
title: Development Lifecycle and Deployment Architect Certification
aliases: [Salesforce Certified Platform Development Lifecycle and Deployment Architect, Plat-Arch-202, Development Lifecycle and Deployment Architect]
domain: architecture-practice
summary: >-
  Salesforce's domain architect credential (exam Plat-Arch-202) for designing application lifecycle management,
  environment, testing and release strategies on the Salesforce Platform; it is one of the four certifications that
  together grant System Architect on the path to Certified Technical Architect.
release: "Winter '27"
status: current
broader: [kt:salesforce-architect]
related: [kt:application-lifecycle-management, kt:environment-strategy, kt:sandbox-types, kt:unlocked-packages, kt:metadata-api, kt:testing-strategy]
relations:
  - {predicate: partOf, object: kt:system-architect-certification}
  - {predicate: contrastsWith, object: kt:integration-architect-certification}
sources:
  - id: s1
    title: "Salesforce Certified Platform Development Lifecycle and Deployment Architect Exam Guide"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298968&language=en_US&type=1
    type: official-learning
    accessed: 2026-11-11
  - id: s2
    title: "Certification - Salesforce Certified Platform Development Lifecycle and Deployment Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/platformdevelopmentlifecycledeploymentarchitect
    type: official-learning
    accessed: 2026-11-11
  - id: s3
    title: "Certification - Salesforce Certified System Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/systemarchitect
    type: official-learning
    accessed: 2026-11-11
  - id: s4
    title: "Certification - Architect Overview"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/credentials/architectoverview
    type: official-learning
    accessed: 2026-11-11
created: 2026-11-11
---

# Development Lifecycle and Deployment Architect Certification

The Salesforce Certified Platform Development Lifecycle and Deployment Architect is the architect-level credential for how change gets planned, built, tested and released on the Salesforce Platform. Trailhead describes holders as experts at assessing architecture environments and requirements so they can implement management solutions on the platform.[^s2] The official exam guide frames the audience as experienced professionals who apply DevOps, application lifecycle management (ALM) and governance to Salesforce and who can explain solutions and trade-offs to both business and IT stakeholders.[^s1] It is one of the architect credentials listed on Trailhead's architect overview page.[^s4]

## Who it is for

The exam guide sketches a typical candidate: a computer-science degree or equivalent, two to three years of Salesforce Platform experience, and one to two years each in Salesforce DevOps, governance committees and ALM, plus familiarity with agile, waterfall or hybrid delivery.[^s1] It names roles such as Technical Lead, Delivery Lead, Release Manager, Environment Manager, Ops Manager, Test Manager and Technical Architect.[^s1] In practice this is the release-management and DevOps exam of the architect track rather than a coding exam.

## Exam format

Per the exam guide opened for this article, the exam (code Plat-Arch-202 on Trailhead Academy) has the following format.[^s1][^s2]

- 60 scored multiple-choice questions, plus up to 5 unscored questions that do not affect the result.[^s1]
- 105 minutes; passing score 65%.[^s1]
- Registration fee US$400 and retake fee US$200, plus applicable taxes.[^s1]
- Proctored onsite or online; no reference materials allowed and no prerequisite certification.[^s1]

## Exam outline

The guide divides the exam into eight lifecycle-shaped sections whose weightings add up to 100%.[^s1]

| Section | Weight | Focus (paraphrased)[^s1] |
|---|---|---|
| Application Lifecycle Management | 8% | Methodology risks and benefits; governance matched to customer maturity |
| Planning | 13% | ALM maturity, environment risks, governance frameworks, seasonal-release risk |
| System Design | 15% | Agile tooling, org strategy, sandbox strategy, deployment tooling |
| Building | 14% | Branching and merging, test data and unit tests, org- vs package-based development, scratch orgs vs sandboxes, code quality |
| Deploying | 14% | Metadata and Tooling API capabilities and limits, pre/post-deployment steps, reference data |
| Testing | 13% | Test methodology, execution and coverage, a secure unified test-data strategy |
| Releasing | 13% | Managed, unmanaged and unlocked packages; sandbox-to-release mapping; release management |
| Operating | 10% | Direct-to-production changes and bringing them back into ALM; shared release artifacts across orgs |

The weighting rewards breadth: no section exceeds 15%, so a candidate strong only in packaging or only in source control will struggle.[^s1]

## Gotchas

- **The guide's question bank is pinned to an older release.** It states the questions align to Spring '23, so newer tooling may be absent from the exam even when it matters in real projects.[^s1]
- **It is a building block, not an end point.** Passing it alongside Platform Developer, Identity and Access Management Architect and Integration Architect automatically grants System Architect.[^s3]
- **Credential pages omit logistics.** The Trailhead credential page gives only a description and links to Trailhead Academy and an exam-prep Trailmix, so the help-site exam guide is the place to confirm fees, timing and outline.[^s2][^s1]
- **Operations count.** The Operating section tests how emergency production changes flow back into source control and the release process, not just how to deploy.[^s1]

## Connections

- **broader → `kt:salesforce-architect`**: one of the domain credentials on the Salesforce architect ladder.[^s4]
- **partOf → `kt:system-architect-certification`**: one of the four prerequisites that roll up into System Architect.[^s3]
- **contrastsWith → `kt:integration-architect-certification`**: a sibling System Architect prerequisite; this exam governs how change moves between environments, while Integration Architect covers how systems exchange data.[^s3]
- **related → `kt:application-lifecycle-management`, `kt:environment-strategy`, `kt:sandbox-types`**: the ALM, planning and system-design sections test these directly.[^s1]
- **related → `kt:unlocked-packages`, `kt:metadata-api`, `kt:testing-strategy`**: the releasing, deploying and testing sections cover package types, Metadata API deployment and test strategy.[^s1]

## Sources
[^s1]: Salesforce Help, "Salesforce Certified Platform Development Lifecycle and Deployment Architect Exam Guide". https://help.salesforce.com/s/articleView?id=005298968&language=en_US&type=1 (accessed 2026-11-11)
[^s2]: Trailhead, "Certification - Salesforce Certified Platform Development Lifecycle and Deployment Architect". https://trailhead.salesforce.com/credentials/platformdevelopmentlifecycledeploymentarchitect (accessed 2026-11-11)
[^s3]: Trailhead, "Certification - Salesforce Certified System Architect". https://trailhead.salesforce.com/credentials/systemarchitect (accessed 2026-11-11)
[^s4]: Trailhead, "Certification - Architect Overview". https://trailhead.salesforce.com/en/credentials/architectoverview (accessed 2026-11-11)
