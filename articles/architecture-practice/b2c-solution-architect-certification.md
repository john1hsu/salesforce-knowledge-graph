---
id: kt:b2c-solution-architect-certification
type: Certification
title: B2C Solution Architect Certification
aliases: [Salesforce Certified B2C Solution Architect, B2C Solution Architect credential]
domain: architecture-practice
summary: >-
  A Salesforce architect credential with its own exam that validates designing multi-cloud B2C customer solutions
  across service, commerce and marketing; Trailhead lists Platform App Builder and Platform Integration Architect as
  prerequisites, and the exam weights discovery, data models and integration most heavily.
release: "Winter '27"
status: current
broader: [kt:salesforce-architect, kt:salesforce-certification-program]
related: [kt:commerce-cloud, kt:data-cloud, kt:marketing-cloud-engagement, kt:service-cloud, kt:identity-resolution]
relations:
  - {predicate: dependsOn, object: kt:platform-app-builder-certification}
  - {predicate: dependsOn, object: kt:integration-architect-certification}
  - {predicate: contrastsWith, object: kt:b2c-commerce-architect-certification}
sources:
  - id: s1
    title: "Certification - Salesforce Certified B2C Solution Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/credentials/b2csolutionarchitect
    type: official-learning
    accessed: 2026-11-12
  - id: s2
    title: "B2C Solution Architect Certification Prep: Get Started (unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/b2c-study-cert-get-started/b2c-p1-study-cert-get-started
    type: official-learning
    accessed: 2026-11-12
  - id: s3
    title: "Review Data Model and Management"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/b2c-solution-architect-cert-prep-architecture-and-integration/b2b-p2-data-model-and-management
    type: official-learning
    accessed: 2026-11-12
  - id: s4
    title: "Review Integration (B2C Solution Architect Cert Prep)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/b2c-solution-architect-cert-prep-architecture-and-integration/b2b-p3-ntegration
    type: official-learning
    accessed: 2026-11-12
  - id: s5
    title: "B2C Solution Architect Certification: Guiding Companies Through Digital Transformation"
    publisher: Trailhead (Medium)
    url: https://medium.com/trailhead/salesforce-b2c-solution-architect-certification-39af4bef3d7c
    type: official-blog
    accessed: 2026-11-12
created: 2026-11-12
---

# B2C Solution Architect Certification

The Salesforce Certified B2C Solution Architect credential recognizes architects who design and drive multi-cloud solutions that deliver business value for a consumer-facing customer.[^s1] Unlike the roll-up credentials Application Architect and System Architect, it is earned by passing its own exam, and Trailhead lists prerequisite certifications that must be held first.[^s1] Trailhead's study module pitches it at people with knowledge and experience across multiple Salesforce clouds, noting that solution architects who bridge business needs and technical implementation typically bring two to three years of experience.[^s2]

## Prerequisites and how they changed

The current credential page lists two prerequisites: Platform App Builder and Platform Integration Architect.[^s1] That is a slimmer set than at launch. Trailhead's announcement of the credential, published around the end of 2020, listed three prerequisites that could be earned in any order: Marketing Cloud Email Specialist, Platform App Builder and the then-named Integration Architecture Designer.[^s5] Candidates following older study guides should therefore check the live credential page rather than assume a Marketing Cloud credential is still required.[^s1][^s5]

## What the exam covers

The Trailhead study module breaks the exam into five sections with these weightings:[^s2]

- **Discovery and Customer Success**: 27%, the largest single section.[^s2]
- **Functional Capabilities and Business Value**: 7%.[^s2]
- **Architecture Design**: 18%.[^s2]
- **Data Models and Management**: 25%.[^s2]
- **Integration**: 23%.[^s2]

Data and integration together make up nearly half of the exam, which reflects the credential's multi-cloud focus. The data unit asks candidates to explain how commerce entities such as profiles, orders and products relate between systems of record and systems of engagement, to establish which system owns which data, and to reason about a unified individual ID and identity constraints across clouds.[^s3] It also covers privacy features across clouds, including Marketing Cloud consent management and restriction of processing for a contact, and when a custom privacy solution is justified over out-of-the-box features.[^s3] Migration strategy, data-loading choices by volume, and extending the standard data model for high-volume processing round out the section.[^s3]

The integration unit focuses on connecting Salesforce Service, B2C Commerce and Marketing Cloud.[^s4] It reviews real-time versus batch exchange and synchronous versus asynchronous messaging, and names platform tools such as Platform Events and Change Data Capture for propagating changes to external systems.[^s4] It also expects candidates to weigh out-of-the-box features against custom integration given system limits, and to cover authentication with SSO, MFA and two-way TLS while respecting regional legal requirements.[^s4] Identity resolution in Data 360 appears as the mechanism for consolidating profiles from multiple sources.[^s4]

## Exam logistics: where to look

Neither the credential page nor the study module opened for this article states the question count, time limit, passing score or fee; the credential page links out to a separate exam registration experience and a maintain-certifications resource for those details.[^s1][^s2] Treat third-party figures with caution and confirm them against the official exam guide before booking.

## Gotchas

- **It is not the B2C Commerce Architect.** Trailhead lists B2C Commerce Architect as a separate related credential; that one is product-specific, while this one spans clouds.[^s1]
- **Business skills are tested heavily.** Discovery and customer success outweighs architecture design, so pure technical study leaves a large gap.[^s2]
- **Prerequisites are not historical.** The prerequisite list has changed since launch, so rely on the current credential page.[^s1][^s5]

## Connections

- **broader → `kt:salesforce-architect`, `kt:salesforce-certification-program`**: one of the architect-level credentials in Salesforce's certification catalogue.[^s1]
- **dependsOn → `kt:platform-app-builder-certification`, `kt:integration-architect-certification`**: the two prerequisites on the current credential page.[^s1]
- **contrastsWith → `kt:b2c-commerce-architect-certification`**: a related but product-specific commerce credential.[^s1]
- **related → `kt:commerce-cloud`, `kt:service-cloud`, `kt:marketing-cloud-engagement`**: the clouds whose integration the exam tests.[^s4][^s5]
- **related → `kt:data-cloud`, `kt:identity-resolution`**: unifying customer profiles across clouds is a core data-model topic.[^s3][^s4]

## Sources
[^s1]: Trailhead, "Certification - Salesforce Certified B2C Solution Architect". https://trailhead.salesforce.com/en/credentials/b2csolutionarchitect (accessed 2026-11-12)
[^s2]: Trailhead, "B2C Solution Architect Certification Prep: Get Started (unit)". https://trailhead.salesforce.com/content/learn/modules/b2c-study-cert-get-started/b2c-p1-study-cert-get-started (accessed 2026-11-12)
[^s3]: Trailhead, "Review Data Model and Management". https://trailhead.salesforce.com/content/learn/modules/b2c-solution-architect-cert-prep-architecture-and-integration/b2b-p2-data-model-and-management (accessed 2026-11-12)
[^s4]: Trailhead, "Review Integration (B2C Solution Architect Cert Prep)". https://trailhead.salesforce.com/content/learn/modules/b2c-solution-architect-cert-prep-architecture-and-integration/b2b-p3-ntegration (accessed 2026-11-12)
[^s5]: Trailhead (Medium), "B2C Solution Architect Certification: Guiding Companies Through Digital Transformation". https://medium.com/trailhead/salesforce-b2c-solution-architect-certification-39af4bef3d7c (accessed 2026-11-12)
