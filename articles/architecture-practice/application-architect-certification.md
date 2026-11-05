---
id: kt:application-architect-certification
type: Certification
title: Application Architect Certification
aliases: [Salesforce Certified Application Architect, Application Architect credential]
domain: architecture-practice
summary: >-
  A Salesforce architect credential with no exam of its own: it is granted automatically to anyone holding Platform
  App Builder, Platform Data Architect, Platform Developer and Platform Sharing and Visibility Architect, and it is one
  of the two prerequisites listed for Certified Technical Architect.
release: "Winter '27"
status: current
broader: [kt:salesforce-architect]
related: [kt:certified-technical-architect]
relations:
  - {predicate: hasPart, object: kt:platform-data-architect-certification}
  - {predicate: hasPart, object: kt:sharing-and-visibility-architect-certification}
  - {predicate: hasPart, object: kt:platform-app-builder-certification}
  - {predicate: hasPart, object: kt:platform-developer-certification}
  - {predicate: contrastsWith, object: kt:system-architect-certification}
sources:
  - id: s1
    title: "Certification - Salesforce Certified Application Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/applicationarchitect
    type: official-learning
    accessed: 2026-11-05
  - id: s2
    title: "Certification - Salesforce Certified System Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/systemarchitect
    type: official-learning
    accessed: 2026-11-05
  - id: s3
    title: "Certification - Salesforce Certified Technical Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/credentials/technicalarchitect
    type: official-learning
    accessed: 2026-11-05
  - id: s4
    title: "Architect Certifications Overview"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/credentials/architectoverview
    type: official-learning
    accessed: 2026-11-05
  - id: s5
    title: "Certification - Salesforce Certified Platform App Builder"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/platformappbuilder
    type: official-learning
    accessed: 2026-11-05
  - id: s6
    title: "Get Started with Platform Developer I Study Guide"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/ko/content/learn/modules/platform-developer-i-certification-prep-fundamentals-and-database-modeling/pd1-1-get-started
    type: official-learning
    accessed: 2026-11-05
created: 2026-11-05
---

# Application Architect Certification

The Salesforce Certified Application Architect is a credential for architects with a deep understanding of native Salesforce features and functionality, who are skilled at modelling role hierarchies, data, and the right sharing mechanisms for a requirement.[^s1] It is unusual among Salesforce credentials in that there is no Application Architect exam: Trailhead grants it automatically once a candidate has passed four prerequisite certifications.[^s1]

## How it is earned

The four building blocks are Platform App Builder, Platform Data Architect, Platform Developer, and Platform Sharing and Visibility Architect.[^s1] They mix two practitioner-level exams with two architect-level ones:

- **Platform App Builder** certifies the ability to design, build and deploy custom applications with the platform's declarative (clicks-not-code) customization features.[^s5]
- **Platform Developer** covers basic business logic and user interfaces built with the platform's programmatic tools. Trailhead's study guide, still titled for Platform Developer I, weights the exam at 27% developer fundamentals, 28% process automation and logic, 25% user interface, and 20% testing, debugging and deployment.[^s6]
- **Platform Data Architect** covers designing enterprise data management solutions, and **Platform Sharing and Visibility Architect** covers designing for sharing and visibility security requirements.[^s4]

Because the credential is only a roll-up, maintenance happens at the level of the underlying certifications; the credential page itself links to the general maintenance guidance and states no separate requirement.[^s1]

## Where it sits in the architect path

Trailhead's architect catalogue lists fourteen architect credentials, from domain exams such as Data, Integration and Identity and Access Management to product credentials like Heroku, Tableau and MuleSoft.[^s4] Application Architect and System Architect are the two cross-cutting roll-ups. Where Application Architect is about what the platform does natively, the System Architect focuses on off-platform systems, integration and securing access between systems, plus governance and testing of deployments.[^s2] System Architect is earned the same automatic way, from Platform Developer, Development Lifecycle and Deployment Architect, Identity and Access Management Architect, and Integration Architect.[^s2] Platform Developer is therefore the one exam common to both paths.[^s1][^s2]

The Technical Architect credential page lists Application Architect and System Architect under its prerequisites, describing CTAs as experienced in designing secure, high-performance, integrated technical solutions within a customer's landscape.[^s3]

## Gotchas

- **Don't look for an exam to book.** Candidates sometimes search for an Application Architect exam; the credential only appears after the fourth prerequisite is passed.[^s1]
- **Names drift.** The credential page now says "Platform Developer", while the Trailhead prep content still uses the older "Platform Developer I" name for the same exam track.[^s1][^s6]
- **Check logistics at the source.** The credential pages don't state fees, timing or passing scores; those live with each underlying exam's registration, so verify them there rather than in third-party guides.[^s1][^s5]

## When to pursue it

It fits people whose design work is mostly on-platform: object models, declarative and programmatic customization, and record access.[^s1] Practitioners whose work centres on integration, identity and release management will find System Architect the closer match, and anyone aiming at CTA will normally collect both, since the CTA page lists both as prerequisites.[^s2][^s3]

## Connections

- **broader → `kt:salesforce-architect`**: one rung of the Salesforce architect credential ladder.[^s4]
- **hasPart → `kt:platform-data-architect-certification`, `kt:sharing-and-visibility-architect-certification`**: the two architect-level prerequisites.[^s1]
- **hasPart → `kt:platform-app-builder-certification`, `kt:platform-developer-certification`**: the declarative and programmatic practitioner prerequisites.[^s1][^s5][^s6]
- **contrastsWith → `kt:system-architect-certification`**: the sibling roll-up for off-platform integration, identity and deployment, sharing the Platform Developer exam.[^s2]
- **related → `kt:certified-technical-architect`**: the credential that lists Application Architect as a prerequisite.[^s3]

## Sources
[^s1]: Trailhead, "Certification - Salesforce Certified Application Architect". https://trailhead.salesforce.com/credentials/applicationarchitect (accessed 2026-11-05)
[^s2]: Trailhead, "Certification - Salesforce Certified System Architect". https://trailhead.salesforce.com/credentials/systemarchitect (accessed 2026-11-05)
[^s3]: Trailhead, "Certification - Salesforce Certified Technical Architect". https://trailhead.salesforce.com/en/credentials/technicalarchitect (accessed 2026-11-05)
[^s4]: Trailhead, "Architect Certifications Overview". https://trailhead.salesforce.com/en/credentials/architectoverview (accessed 2026-11-05)
[^s5]: Trailhead, "Certification - Salesforce Certified Platform App Builder". https://trailhead.salesforce.com/credentials/platformappbuilder (accessed 2026-11-05)
[^s6]: Trailhead, "Get Started with Platform Developer I Study Guide". https://trailhead.salesforce.com/ko/content/learn/modules/platform-developer-i-certification-prep-fundamentals-and-database-modeling/pd1-1-get-started (accessed 2026-11-05)
