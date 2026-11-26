---
id: kt:cmmc
type: ExternalConcept
title: Cybersecurity Maturity Model Certification (CMMC)
aliases: [CMMC, CMMC 2.0, CMMC Program, 32 CFR part 170]
domain: public-sector-and-compliance
summary: >-
  The US Department of Defense program, codified in 32 CFR part 170, that requires defense contractors and
  subcontractors to implement and be assessed against prescribed safeguards for Federal Contract Information and
  Controlled Unclassified Information, at three levels built on FAR 52.204-21, NIST SP 800-171 and NIST SP 800-172.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:government-cloud-plus, kt:il4-and-il5, kt:itar-and-export-controls, kt:shared-responsibility-model]
relations:
  - {predicate: dependsOn, object: kt:nist-sp-800-171}
  - {predicate: dependsOn, object: kt:controlled-unclassified-information}
  - {predicate: contrastsWith, object: kt:fedramp}
sources:
  - id: s1
    title: "32 CFR Part 170 — Cybersecurity Maturity Model Certification (CMMC) Program"
    publisher: Electronic Code of Federal Regulations (eCFR)
    url: https://www.ecfr.gov/current/title-32/subtitle-A/chapter-I/subchapter-G/part-170
    type: government
    accessed: 2026-11-26
  - id: s2
    title: "Cybersecurity Maturity Model Certification (CMMC) Program (final rule, 89 FR 83092)"
    publisher: Federal Register (DoD CIO)
    url: https://www.federalregister.gov/documents/2024/10/15/2024-22905/cybersecurity-maturity-model-certification-cmmc-program
    type: government
    accessed: 2026-11-26
  - id: s3
    title: "DFARS Changes to Integrate CMMC Requirements Effective November 10"
    publisher: EDUCAUSE Review
    url: https://er.educause.edu/articles/2025/11/dfars-changes-to-integrate-cmmc-requirements-effective-november-10
    type: news
    accessed: 2026-11-26
  - id: s4
    title: "Salesforce Government Cloud"
    publisher: Salesforce
    url: https://www.salesforce.com/government/cloud/
    type: official-blog
    accessed: 2026-11-26
  - id: s5
    title: "Government Cloud Plus - Defense"
    publisher: Salesforce Compliance Site
    url: https://compliance.salesforce.com/en/services/salesforce-government-cloud-plus-defense
    type: official-docs
    accessed: 2026-11-26
created: 2026-11-26
---

# Cybersecurity Maturity Model Certification (CMMC)

CMMC is the Department of Defense program that sets cybersecurity requirements for defense contractors and their subcontractors so that two kinds of government information are protected in their systems: Federal Contract Information (FCI) and Controlled Unclassified Information (CUI).[^s1] Its rules live in 32 CFR part 170, published as a final rule by the DoD CIO in October 2024 and effective December 16, 2024.[^s2] The program does not invent new controls; it assesses contractors against existing ones: FAR clause 52.204-21, NIST SP 800-171 Revision 2, and a selection of requirements from NIST SP 800-172.[^s1]

## The three levels

The rule defines 15 Level 1 requirements, 110 Level 2 requirements and 24 Level 3 requirements, mapped to those three sources respectively.[^s1]

- **Level 1 (Self):** for FCI only. The contractor self-assesses every year, posts results to SPRS, and may not use a plan of action and milestones (POA&M).[^s2]
- **Level 2 (Self or C3PAO):** for CUI. The 110 NIST SP 800-171 R2 requirements are assessed every three years, either by the contractor or by an authorized third-party assessment organization (C3PAO), with an affirmation every year in between.[^s2]
- **Level 3 (DIBCAC):** for the most critical programs, as designated by the program manager. It adds the 24 selected 800-172 requirements, is assessed every three years by DCMA's DIBCAC, and requires a current Level 2 (C3PAO) status for the same scope first.[^s1][^s2]

## Scoring, POA&Ms and affirmations

A Level 2 assessment is scored out of 110 and Level 3 out of 24. A contractor reaching 80 percent of the maximum, with certain critical requirements met, can receive a Conditional status and put the remaining NOT MET items on a POA&M.[^s2] Those items must be closed within 180 days, verified by a POA&M closeout assessment; otherwise the Conditional status expires.[^s2] A senior affirming official must confirm continued compliance in SPRS after each assessment and annually, and a Level 2 status lapses if the annual affirmation is missed.[^s2] Assessment artifacts must be kept for six years.[^s1]

## Rollout through contracts

Part 170 defines four phases that add requirements one year apart, beginning when the companion DFARS acquisition rule takes effect: self-assessments first, then Level 2 C3PAO certification, then Level 3, and finally full implementation including option periods on older contracts.[^s1] That DFARS rule (case 2019-D041) was released September 10, 2025 and took effect November 10, 2025, so Phase 1 began then and Phase 2 follows twelve months later, in November 2026.[^s3] Under it, contractors need their score or certification posted in SPRS to compete, and offerors supply CMMC unique identifiers for each system that handles FCI or CUI.[^s3] Requirements flow down: a prime under Level 2 (C3PAO) must require Level 2 (C3PAO) of subcontractors handling CUI.[^s2]

## Cloud services and scope

Cloud is where CMMC meets platforms like Salesforce. DFARS 252.204-7012 already requires contractors to confirm that any cloud service provider handling CUI meets the FedRAMP Moderate baseline or equivalent requirements, and CMMC carries that expectation into assessments.[^s2] Part 170 treats a provider as an External Service Provider only when CUI or security protection data is processed, stored or transmitted on its assets, and the contractor's own connecting infrastructure stays in scope.[^s1] Controls a contractor inherits from a provider still have to be documented, which is why the shared responsibility split matters.[^s1]

## CMMC and Salesforce

CMMC levels are assigned to the contractor (the organization seeking assessment), not to its cloud vendor.[^s2] Salesforce's Government Cloud FAQ accordingly says Government Cloud can help customers meet CMMC requirements, specifically Levels 2 and 3, and points to a NIST 800-171 Rev 2 attestation letter from a 3PAO on its compliance portal.[^s4] Government Cloud Plus holds a FedRAMP Class D (formerly High) JAB P-ATO and runs on AWS GovCloud (US), well above the Moderate floor.[^s4] For defense workloads, Government Cloud Plus - Defense is a physically isolated, dedicated instance designed for Impact Level 5 data including CUI, and the compliance site lists a CMMC and Salesforce whitepaper alongside it.[^s5] Gotchas: Defense users must log in with a Common Access Card as the MFA token, and contractors can use that edition only in support of a DoD mission owner's contract, not for internal use.[^s4] Apps from AgentExchange sit outside the authorization boundary by default.[^s4]

## Connections

CMMC is one of the `kt:security-compliance-frameworks` (broader).[^s1] It `dependsOn` NIST SP 800-171 (`kt:nist-sp-800-171`), whose 110 requirements form Level 2, and on the CUI category (`kt:controlled-unclassified-information`) it protects.[^s1] It `contrastsWith` FedRAMP (`kt:fedramp`): FedRAMP authorizes the cloud provider, while CMMC assesses the contractor, which may inherit controls from a FedRAMP Moderate or higher provider.[^s2] Salesforce environments for this work are Government Cloud Plus (`kt:government-cloud-plus`) and its Defense edition at DoD Impact Levels 4 and 5 (`kt:il4-and-il5`).[^s4][^s5] Export-controlled defense data raises the related concerns in `kt:itar-and-export-controls`, and the split of inherited controls is the `kt:shared-responsibility-model`.[^s1]

## Sources

[^s1]: eCFR, "32 CFR Part 170 — Cybersecurity Maturity Model Certification (CMMC) Program". https://www.ecfr.gov/current/title-32/subtitle-A/chapter-I/subchapter-G/part-170 (accessed 2026-11-26)
[^s2]: Federal Register (DoD CIO), "Cybersecurity Maturity Model Certification (CMMC) Program", final rule, 89 FR 83092. https://www.federalregister.gov/documents/2024/10/15/2024-22905/cybersecurity-maturity-model-certification-cmmc-program (accessed 2026-11-26)
[^s3]: Jarrett Cummings, EDUCAUSE Review, "DFARS Changes to Integrate CMMC Requirements Effective November 10". https://er.educause.edu/articles/2025/11/dfars-changes-to-integrate-cmmc-requirements-effective-november-10 (accessed 2026-11-26)
[^s4]: Salesforce, "Salesforce Government Cloud". https://www.salesforce.com/government/cloud/ (accessed 2026-11-26)
[^s5]: Salesforce Compliance Site, "Government Cloud Plus - Defense". https://compliance.salesforce.com/en/services/salesforce-government-cloud-plus-defense (accessed 2026-11-26)
