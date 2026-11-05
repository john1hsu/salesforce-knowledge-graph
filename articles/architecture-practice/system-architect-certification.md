---
id: kt:system-architect-certification
type: Certification
title: System Architect Certification
aliases: [Salesforce Certified System Architect, System Architect credential]
domain: architecture-practice
summary: >-
  A Salesforce architect credential with no exam of its own, granted automatically once a candidate holds Platform
  Developer, Development Lifecycle and Deployment Architect, Identity and Access Management Architect and Integration
  Architect; it covers off-platform systems, integration and secure system-to-system access, and is a CTA prerequisite.
release: "Winter '27"
status: current
broader: [kt:salesforce-architect]
related: [kt:certified-technical-architect, kt:cta-review-board]
relations:
  - {predicate: hasPart, object: kt:platform-developer-certification}
  - {predicate: hasPart, object: kt:development-lifecycle-and-deployment-architect-certification}
  - {predicate: hasPart, object: kt:identity-and-access-management-architect-certification}
  - {predicate: hasPart, object: kt:integration-architect-certification}
  - {predicate: contrastsWith, object: kt:application-architect-certification}
sources:
  - id: s1
    title: "Certification - Salesforce Certified System Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/credentials/systemarchitect
    type: official-learning
    accessed: 2026-11-05
  - id: s2
    title: "Certification - Salesforce Certified Platform Development Lifecycle and Deployment Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/platformdevelopmentlifecycledeploymentarchitect
    type: official-learning
    accessed: 2026-11-05
  - id: s3
    title: "Certification - Salesforce Certified Platform Identity and Access Management Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/platformidentityandaccessmanagementarchitect
    type: official-learning
    accessed: 2026-11-05
  - id: s4
    title: "Certification - Salesforce Certified Platform Integration Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/platformintegrationarchitect
    type: official-learning
    accessed: 2026-11-05
  - id: s5
    title: "Certification - Salesforce Certified Technical Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/credentials/technicalarchitect
    type: official-learning
    accessed: 2026-11-05
created: 2026-11-05
---

# System Architect Certification

The Salesforce Certified System Architect is the architect credential for people whose design work happens at the edges of an org: Trailhead describes holders as focused on off-platform systems, integration, and securing access between systems.[^s1] The same page adds a delivery dimension, crediting System Architects with managing governance and testing capabilities for deployments and ongoing changes to Salesforce.[^s1] Like its sibling Application Architect, it has no exam to book; it is a roll-up credential that Trailhead grants automatically once its prerequisites are complete.[^s1]

## How it is earned

The credential page lists four prerequisite certifications and states that passing them automatically grants System Architect.[^s1]

- **Platform Developer**: the programmatic, practitioner-level foundation, and the one exam the System Architect path shares with Application Architect.[^s1]
- **Platform Development Lifecycle and Deployment Architect**: certifies experts who assess architecture environments and requirements to implement management solutions on the platform, i.e. release management, environments and deployment governance.[^s2]
- **Platform Identity and Access Management Architect**: certifies architects who design sound, high-performing solutions on the platform that meet single sign-on requirements.[^s3]
- **Platform Integration Architect**: certifies architects who design sound, scalable technical solutions that meet end-to-end integration requirements.[^s4]

Each of the three architect-level pages points to an "Architect Journey" Trailmix as the recommended preparation path for its domain: Development Lifecycle and Deployment, Identity and Access Management, and Integration Architecture respectively.[^s2][^s3][^s4]

## What the credential pages do (and don't) tell you

None of the official credential pages opened for this article states exam logistics such as question count, duration, fee or passing score; they link out to a separate exam experience instead.[^s2][^s3][^s4] The System Architect page likewise states no maintenance requirement of its own and links to the general maintain-and-verify certification pages, so upkeep effectively happens through the underlying certifications.[^s1] Treat any third-party figure for these exams with caution and check the current exam guide before relying on it.

## Gotchas

- **There is no System Architect exam.** The credential appears only after the fourth prerequisite is passed; candidates who search for a booking will not find one.[^s1]
- **It is a cross-domain bundle, not a specialism.** The four parts span code, release management, identity and integration, so a candidate strong in one area (for example integration) still has three other domains to clear.[^s1][^s2][^s3][^s4]
- **Order is up to the candidate.** The page lists the four prerequisites without prescribing a sequence; the practitioner-level Platform Developer exam is a natural first step for CTA-bound candidates because it also counts toward Application Architect.[^s1][^s5]

## When to pursue it

System Architect fits architects whose daily work is connecting Salesforce to the rest of the enterprise: designing integrations, federating identity and single sign-on, and governing how changes move between environments.[^s1][^s3][^s4] Architects whose work is mostly on-platform data modelling and record access are better matched by Application Architect, which the Technical Architect page describes as covering native features and functionality.[^s5] Anyone aiming at Certified Technical Architect needs both, because the CTA credential page lists Application Architect and System Architect as its two prerequisites.[^s5]

## Connections

- **broader → `kt:salesforce-architect`**: one rung on the Salesforce architect credential ladder.[^s1]
- **hasPart → `kt:platform-developer-certification`, `kt:development-lifecycle-and-deployment-architect-certification`, `kt:identity-and-access-management-architect-certification`, `kt:integration-architect-certification`**: the four certifications that roll up into System Architect.[^s1][^s2][^s3][^s4]
- **contrastsWith → `kt:application-architect-certification`**: the sibling roll-up for native, on-platform design; the two share only Platform Developer.[^s1][^s5]
- **related → `kt:certified-technical-architect`, `kt:cta-review-board`**: System Architect is one of the two prerequisites listed on the CTA credential page, so it gates entry to the review board.[^s5]

## Sources
[^s1]: Trailhead, "Certification - Salesforce Certified System Architect". https://trailhead.salesforce.com/en/credentials/systemarchitect (accessed 2026-11-05)
[^s2]: Trailhead, "Certification - Salesforce Certified Platform Development Lifecycle and Deployment Architect". https://trailhead.salesforce.com/credentials/platformdevelopmentlifecycledeploymentarchitect (accessed 2026-11-05)
[^s3]: Trailhead, "Certification - Salesforce Certified Platform Identity and Access Management Architect". https://trailhead.salesforce.com/credentials/platformidentityandaccessmanagementarchitect (accessed 2026-11-05)
[^s4]: Trailhead, "Certification - Salesforce Certified Platform Integration Architect". https://trailhead.salesforce.com/credentials/platformintegrationarchitect (accessed 2026-11-05)
[^s5]: Trailhead, "Certification - Salesforce Certified Technical Architect". https://trailhead.salesforce.com/en/credentials/technicalarchitect (accessed 2026-11-05)
