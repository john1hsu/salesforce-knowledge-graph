---
id: kt:hitrust-csf
type: ExternalConcept
title: HITRUST CSF
aliases: [HITRUST Common Security Framework, HITRUST certification, HITRUST r2, HITRUST i1, HITRUST e1]
domain: public-sector-and-compliance
summary: >-
  HITRUST's certifiable control framework that harmonizes dozens of security and privacy standards and regulations
  (ISO/IEC 27001/27002, NIST SP 800-53, HIPAA, PCI DSS, GDPR and others) into one control library assessed through
  e1, i1 and r2 assessments; Salesforce holds HITRUST certificates for several services and participates in the
  HITRUST Shared Responsibility and Inheritance Program.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:hipaa, kt:nist-cybersecurity-framework, kt:iso-iec-27001, kt:shared-responsibility-model, kt:hyperforce]
relations:
  - {predicate: contrastsWith, object: kt:soc-2}
sources:
  - id: s1
    title: "HITRUST Framework"
    publisher: HITRUST Alliance
    url: https://hitrustalliance.net/hitrust-framework
    type: standards-body
    accessed: 2026-11-15
  - id: s2
    title: "Introduction to the HITRUST CSF, Version 11.8.0"
    publisher: HITRUST Alliance
    url: https://hitrustalliance.net/hubfs/CSF%20v11.8/Introduction%20to%20HITRUST%20CSF%20v11.8.0.pdf
    type: standards-body
    accessed: 2026-11-15
  - id: s3
    title: "Shared Responsibility and Inheritance Program"
    publisher: HITRUST Alliance
    url: https://hitrustalliance.net/shared-responsibility-and-inheritance-program
    type: standards-body
    accessed: 2026-11-15
  - id: s4
    title: "HITRUST — Salesforce Compliance (category listing)"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/categories/hitrust
    type: official-docs
    accessed: 2026-11-15
  - id: s5
    title: "HITRUST Certificate - Corporate + Salesforce Services (1P & SSoH AWS)"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/documents/a005A00000k4ayfQAA
    type: official-docs
    accessed: 2026-11-15
  - id: s6
    title: "Salesforce is now part of the HITRUST Shared Responsibility and Inheritance program"
    publisher: Salesforce Security
    url: https://security.salesforce.com/blog/hitrust-shared-responsibility-and-inheritance-program
    type: official-blog
    accessed: 2026-11-15
  - id: s7
    title: "HITRUST CSF Assessments: e1, i1, r2—What's the Difference?"
    publisher: Cloud Security Alliance (republished from BARR Advisory)
    url: https://cloudsecurityalliance.org/articles/hitrust-csf-assessments-e1-i1-r2-what-s-the-difference
    type: partner
    accessed: 2026-11-15
created: 2026-11-15
---

# HITRUST CSF

The HITRUST CSF is a control framework for information security, privacy and risk management published by HITRUST, which describes it as a unified, threat-adaptive control library and the foundational control set for every HITRUST assessment.[^s1] Its value is harmonization: instead of testing a system separately against each regulation, an organization implements one set of HITRUST requirements that map to many authoritative sources at once.[^s1][^s2] It is most widely adopted in US healthcare, which is why it often appears next to HIPAA in vendor security reviews.[^s7] For Salesforce practitioners it matters because healthcare and life sciences customers frequently ask for HITRUST evidence, and Salesforce publishes HITRUST certificates and supports control inheritance for customers running their own assessments.[^s4][^s6]

## How the framework is built

The version 11.8.0 introduction (dated May 2026) states that the CSF has 14 control categories made up of 49 control objectives and 156 control specifications, and that its core structure derives from ISO/IEC 27001 and 27002.[^s2] Each control carries an objective, a specification, a risk factor type and implementation requirements.[^s2] That edition integrates 75 major authoritative sources, including HIPAA, NIST SP 800-53, NIST CSF 2.0, PCI DSS v4.0.1, the EU GDPR and the CCPA.[^s2] HITRUST updates the framework regularly; its framework page already links v11.9.0 materials and describes a threat-intelligence engine that adjusts control requirements as breach data changes.[^s1]

Requirements are tailored rather than fixed. Organizational factors (such as data volume and size), compliance factors (such as PCI or GDPR obligations) and system factors (such as internet exposure or third-party access) determine which progressive implementation levels apply, with Level 1 as the baseline and segment-specific levels for cases such as cloud service providers.[^s2]

## Assessment types

HITRUST offers assessments with rising assurance, all drawing on the CSF:[^s1]

- **e1 (Essentials, 1-year):** foundational assurance; HITRUST lists 43 core controls and a one-year validity.[^s1]
- **i1 (Implemented, 1-year):** threat-adaptive, moderate assurance with 182 control requirements, valid one year.[^s1][^s7]
- **r2 (Risk-based, 2-year):** tailored, highest-assurance assessment that evaluates policy, procedure, implementation, measurement and management, valid two years with an interim review.[^s1][^s7]

HITRUST also offers AI security and AI risk management assessments built on CSF controls.[^s1]

## Salesforce's certificates and inheritance

Salesforce's compliance site lists separate HITRUST certificates by service and infrastructure. As checked this run, the listing includes a combined certificate for Corporate and Salesforce Services (first party, AWS and Hyperforce), plus certificates for Marketing Cloud Engagement, Marketing Cloud Next, Data 360 (Data Cloud), MuleSoft, and older entries for Salesforce Services on Hyperforce and Government Cloud Plus.[^s4] The combined certificate's reporting period runs from 5 June 2026 to 5 June 2028, and from that letter it adds Corporate Services and Salesforce Services on Hyperforce AWS to scope.[^s5]

Salesforce is enrolled in HITRUST's Shared Responsibility and Inheritance Program.[^s5] A customer pursuing its own HITRUST assessment creates inheritance requests in HITRUST's MyCSF tool, Salesforce approves or rejects each one against its HITRUST Shared Responsibility Matrix, and approved results are imported for the assessor to review.[^s6] Without inheritance, assessors may decline to rely on a provider's SOC 2 Type 2 controls they have not tested themselves.[^s6] HITRUST says organizations can inherit 70 to 85 percent of assessment requirements from participating cloud providers.[^s3]

## Gotchas for architects

- **Check scope per service.** Certificates differ by product and infrastructure, so confirm the exact cloud and hosting model in your design is listed before citing HITRUST in a security questionnaire.[^s4][^s5]
- **Inheritance is not transfer of responsibility.** The shared responsibility matrix defines which controls the provider owns; customer-side configuration, users and data stay with the customer.[^s3][^s6]
- **HITRUST and HIPAA are different things.** HIPAA is one of many sources the CSF maps, and HITRUST offers separate Insights Reports to restate results in HIPAA terms.[^s1][^s2]

## Connections

The HITRUST CSF sits under security compliance frameworks (`kt:security-compliance-frameworks`) as a harmonizing, certifiable framework.[^s1] It is related to HIPAA (`kt:hipaa`), the US health privacy law that is one of its mapped sources and the main reason healthcare buyers ask for it, and to the NIST Cybersecurity Framework (`kt:nist-cybersecurity-framework`) and ISO/IEC 27001 (`kt:iso-iec-27001`), which it also integrates, the latter as its structural base.[^s2] Its inheritance program is a formal version of the shared responsibility model (`kt:shared-responsibility-model`), with a matrix that assigns each control to provider or customer.[^s3][^s6] Salesforce lists certificates by infrastructure, linking it to Hyperforce (`kt:hyperforce`).[^s4][^s5] It `contrastsWith` SOC 2 (`kt:soc-2`): both appear in vendor reviews, but HITRUST certifies against a prescriptive control library, and assessors may not accept SOC 2 testing in place of inherited HITRUST controls.[^s6]

## Sources
[^s1]: HITRUST Alliance, "HITRUST Framework". https://hitrustalliance.net/hitrust-framework (accessed 2026-11-15)
[^s2]: HITRUST Alliance, "Introduction to the HITRUST CSF, Version 11.8.0". https://hitrustalliance.net/hubfs/CSF%20v11.8/Introduction%20to%20HITRUST%20CSF%20v11.8.0.pdf (accessed 2026-11-15)
[^s3]: HITRUST Alliance, "Shared Responsibility and Inheritance Program". https://hitrustalliance.net/shared-responsibility-and-inheritance-program (accessed 2026-11-15)
[^s4]: Salesforce, "HITRUST — Salesforce Compliance (category listing)". https://compliance.salesforce.com/en/categories/hitrust (accessed 2026-11-15)
[^s5]: Salesforce, "HITRUST Certificate - Corporate + Salesforce Services (1P & SSoH AWS)". https://compliance.salesforce.com/en/documents/a005A00000k4ayfQAA (accessed 2026-11-15)
[^s6]: Salesforce Security, "Salesforce is now part of the HITRUST Shared Responsibility and Inheritance program". https://security.salesforce.com/blog/hitrust-shared-responsibility-and-inheritance-program (accessed 2026-11-15)
[^s7]: Cloud Security Alliance, "HITRUST CSF Assessments: e1, i1, r2—What's the Difference?". https://cloudsecurityalliance.org/articles/hitrust-csf-assessments-e1-i1-r2-what-s-the-difference (accessed 2026-11-15)
