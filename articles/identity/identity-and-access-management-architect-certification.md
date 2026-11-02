---
id: kt:identity-and-access-management-architect-certification
type: Certification
title: Identity and Access Management Architect Certification
aliases: [Salesforce Certified Platform Identity and Access Management Architect, IAM Architect certification, Plat-Arch-203]
domain: identity
summary: >-
  Salesforce's domain architect credential for designing Salesforce Platform identity solutions, centred on single
  sign-on requirements; it is one of the four certifications that together grant the System Architect credential on
  the path to Certified Technical Architect.
release: "Winter '27"
status: current
broader: [kt:salesforce-architect]
related: [kt:salesforce-identity, kt:single-sign-on-saml, kt:oauth-2-flows-in-salesforce, kt:my-domain, kt:experience-cloud-identity, kt:multi-factor-authentication]
relations:
  - {predicate: partOf, object: kt:system-architect-certification}
  - {predicate: contrastsWith, object: kt:sharing-and-visibility-architect-certification}
sources:
  - id: s1
    title: "Certification - Salesforce Certified Platform Identity and Access Management Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/it/credentials/platformidentityandaccessmanagementarchitect
    type: official-learning
    accessed: 2026-11-02
  - id: s2
    title: "Certification - Architect Overview"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/architectoverview
    type: official-learning
    accessed: 2026-11-02
  - id: s3
    title: "Certification - Salesforce Certified System Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/systemarchitect
    type: official-learning
    accessed: 2026-11-02
  - id: s4
    title: "Salesforce Architect Program FAQs"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298912&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-02
  - id: s5
    title: "Salesforce Certification Maintenance Schedule"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298922&type=1&language=en_US
    type: official-docs
    accessed: 2026-11-02
  - id: s6
    title: "Architect Journey: Identity and Access Management (Trailmix)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/users/strailhead/trailmixes/architect-identity-and-access-management
    type: official-learning
    accessed: 2026-11-02
created: 2026-11-02
---

# Identity and Access Management Architect Certification

The Salesforce Certified Platform Identity and Access Management Architect is the architect-level credential that validates a practitioner's ability to assess an organization's architecture environment and requirements and then design high-performing Salesforce Platform solutions that satisfy single sign-on (SSO) requirements.[^s1] Practitioners often shorten it to "the IAM architect exam". It is listed alongside the other domain architect credentials — Platform Data, Platform Integration, Platform Sharing and Visibility, and Platform Development Lifecycle and Deployment Architect — in Salesforce's architect credential catalogue.[^s2]

## Where it sits in the architect path

The credential is not an end in itself for most candidates; it is a building block. Salesforce grants the **System Architect** credential automatically once a candidate holds four prerequisites: Platform Developer, Platform Development Lifecycle and Deployment Architect, Platform Identity and Access Management Architect, and Platform Integration Architect.[^s3] System Architect, in turn, is described as the credential focused on off-platform systems, integration and securing access between systems, plus deployment governance and testing.[^s2]

To pursue the Certified Technical Architect (CTA), a candidate must already hold both Application Architect and System Architect and must then pass the online Architect Evaluation; passing that makes the candidate eligible for the Architect Review Board exam, which is scheduled within two to four months.[^s4] A candidate who fails the evaluation receives feedback and may re-register after six months.[^s4] In practice, this means every CTA has passed the IAM architect exam on the way.

## What it tests (at a practitioner level)

The official credential page frames the exam around designing SSO-capable identity solutions on the Salesforce Platform rather than around clicking through setup screens.[^s1] Salesforce's recommended study resource is the "Architect Journey: Identity and Access Management" Trailmix, intended to grow architect skills in identity and access management.[^s6][^s1] In this graph, the articles tagged as covered by this credential are the identity building blocks behind those SSO designs: SSO with SAML, OAuth 2.0 and OpenID Connect flows, My Domain, multi-factor authentication and customer/partner identity on Experience Cloud.[^s1]

## Maintenance and gotchas

- **Annual maintenance.** The credential is kept current through the single yearly Architect maintenance badge. The current badge became available in December 2025 and is due in December 2026.[^s5]
- **Expiry is real.** Missing the deadline expires the certification. A recently expired credential can be reinstated through a support case, but that is not guaranteed; if it has lapsed for more than one cycle, the exam must be retaken.[^s5]
- **CTA logistics.** The Architect Review Board is currently delivered online until further notice, and rescheduling it without a fee needs at least 30 days' notice.[^s4]
- **Exam specifics live elsewhere.** The credential page links out to a separate Trailhead Academy exam page for registration details, so check question counts, timing, fees and weightings there at registration time rather than trusting third-party summaries.[^s1]

## When to pursue it

Pursue it if you design login, SSO, API authorization or external-user identity, or if you are on the System Architect / CTA path, because it is mandatory there.[^s3][^s4] If your security work is mainly about who can see which records rather than how users authenticate, the Platform Sharing and Visibility Architect credential is the closer fit.[^s2]

## Connections

- **broader → `kt:salesforce-architect`**: it is one rung of the Salesforce architect credential ladder.[^s2]
- **partOf → `kt:system-architect-certification`**: one of the four certifications that roll up into System Architect.[^s3]
- **contrastsWith → `kt:sharing-and-visibility-architect-certification`**: both are security-flavoured domain architect exams, but one covers authentication and SSO and the other record visibility; they feed different designations.[^s2][^s3]
- **related → `kt:salesforce-identity`, `kt:single-sign-on-saml`, `kt:oauth-2-flows-in-salesforce`, `kt:my-domain`, `kt:experience-cloud-identity`, `kt:multi-factor-authentication`**: the identity features whose articles are tagged as covered by this exam, reflecting its SSO focus.[^s1]

## Sources
[^s1]: Trailhead, "Certification - Salesforce Certified Platform Identity and Access Management Architect". https://trailhead.salesforce.com/it/credentials/platformidentityandaccessmanagementarchitect (accessed 2026-11-02)
[^s2]: Trailhead, "Certification - Architect Overview". https://trailhead.salesforce.com/credentials/architectoverview (accessed 2026-11-02)
[^s3]: Trailhead, "Certification - Salesforce Certified System Architect". https://trailhead.salesforce.com/credentials/systemarchitect (accessed 2026-11-02)
[^s4]: Salesforce Help, "Salesforce Architect Program FAQs". https://help.salesforce.com/s/articleView?id=005298912&language=en_US&type=1 (accessed 2026-11-02)
[^s5]: Salesforce Help, "Salesforce Certification Maintenance Schedule". https://help.salesforce.com/s/articleView?id=005298922&type=1&language=en_US (accessed 2026-11-02)
[^s6]: Trailhead, "Architect Journey: Identity and Access Management". https://trailhead.salesforce.com/en/users/strailhead/trailmixes/architect-identity-and-access-management (accessed 2026-11-02)
