---
id: kt:soc-3
type: ExternalConcept
title: SOC 3
aliases: [SOC 3 report, System and Organization Controls 3, "SOC for Service Organizations: Trust Services Criteria for General Use Report"]
domain: public-sector-and-compliance
summary: >-
  The AICPA general-use attestation report on a service organization's controls against the Trust Services Criteria;
  it rests on the same kind of examination as SOC 2 but omits the detailed control descriptions and tests, so it can be
  freely distributed. Salesforce lists SOC 3 reports per service and infrastructure, covering security, availability
  and confidentiality.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:hyperforce, kt:agentforce, kt:data-cloud, kt:governance-risk-and-compliance]
relations:
  - {predicate: dependsOn, object: kt:trust-services-criteria}
  - {predicate: contrastsWith, object: kt:soc-2}
  - {predicate: contrastsWith, object: kt:soc-1}
sources:
  - id: s1
    title: "SOC 3® - SOC for Service Organizations: Trust Services Criteria for General Use Report"
    publisher: AICPA & CIMA
    url: https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-3
    type: standards-body
    accessed: 2026-11-21
  - id: s2
    title: "Illustrative SOC 3® Report"
    publisher: AICPA & CIMA
    url: https://www.aicpa-cima.com/resources/download/illustrative-soc-3-r-report
    type: standards-body
    accessed: 2026-11-21
  - id: s3
    title: "SOC 3 - Salesforce Compliance Site"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/categories/soc-3
    type: official-docs
    accessed: 2026-11-21
  - id: s4
    title: "SOC 3 Report - Salesforce Services on Hyperforce"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/documents/a006e00000xpn2GAAQ
    type: official-docs
    accessed: 2026-11-21
  - id: s5
    title: "SOC 3 Report - AI Platform and Agentforce"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/documents/a006e0000115nMYAAY
    type: official-docs
    accessed: 2026-11-21
  - id: s6
    title: "SOC Compliance FAQs"
    publisher: Amazon Web Services
    url: https://aws.amazon.com/compliance/soc-faqs/
    type: partner
    accessed: 2026-11-21
created: 2026-11-21
---

# SOC 3

SOC 3 is the AICPA's "Trust Services Criteria for General Use Report": an attestation by an independent CPA on a service organization's controls relevant to security, availability, processing integrity, confidentiality and privacy.[^s1] Like SOC 2, it is judged against the AICPA Trust Services Criteria, but it does not carry the same level of detail, which is why the AICPA classes it as a general-use report that can be freely distributed.[^s1] For Salesforce practitioners it is the lightweight assurance document: something a prospect, a procurement officer or a public-sector buyer can read for a first look at whether a cloud provider's controls have been independently examined, before anyone requests the full SOC 2.[^s1][^s3]

## What a SOC 3 report contains

The AICPA's illustrative SOC 3 report shows the expected building blocks: management's assertion, a description of the boundaries of the system, the organization's principal service commitments and system requirements, and the service auditor's report.[^s2] The AICPA notes that the example is not prescriptive and that the trust services categories it shows are illustrative, so each organization chooses which categories are in scope, just as it does for SOC 2.[^s2][^s1]

What is missing matters as much as what is present. A SOC 2 report gives restricted readers the detail behind the opinion; a SOC 3 does not, so it cannot replace a SOC 2 when an auditor needs to test reliance on specific controls.[^s1] Cloud providers describe the relationship the same way: AWS calls its SOC 3 a publicly available summary of its SOC 2 report, intended to give an independent assessment of its control environment without disclosing internal information, whereas reviewing its SOC 1 and SOC 2 reports requires an NDA.[^s6] AWS also issues SOC 2 and SOC 3 on the same semi-annual cycle over the same 12-month periods, which illustrates how the two reports usually come from one examination.[^s6]

## Salesforce's SOC 3 reports

Salesforce's compliance site states that its SOC 3 reports cover the security, availability and confidentiality trust services principles; processing integrity and privacy are not named.[^s3] The SOC 3 category lists 31 documents, organized per service and tagged by infrastructure (first party, AWS, Hyperforce, GCP, Azure or OCI), with entries ranging from AI Platform and Agentforce and Salesforce Services on Hyperforce on Google Cloud to Heroku, Quip, Field Service and Marketing Cloud Engagement.[^s3]

Two listings show the scope in practice:

- **Salesforce Services on Hyperforce.** Covers B2C Commerce, Data Cloud, Salesforce Corporate Services, Salesforce Services on Hyperforce and Tableau Next, for 1 November 2025 to 30 April 2026.[^s4]
- **AI Platform and Agentforce.** Covers Agentforce and the Einstein Platform on Hyperforce, for 1 May 2026 to 30 September 2026; it was updated in November 2026.[^s5][^s3]

Despite the report's general-use status, Salesforce's document pages show a login requirement before download, so plan for a compliance-site account rather than a public link.[^s4][^s5]

## Gotchas for architects

- **A SOC 3 is not evidence for testing.** It states that controls were examined, not how; auditors relying on specific controls need the SOC 2.[^s1][^s6]
- **Match services and infrastructure.** Reports are per service and per infrastructure, so check that each cloud in your design, on the infrastructure it runs on, has a listed report.[^s3][^s4]
- **Check the period.** Each listing shows a reporting start and end date; a report for one window says nothing about later changes.[^s4][^s5]
- **Category scope.** Salesforce's SOC 3 names security, availability and confidentiality only; don't cite it as assurance over privacy or processing integrity.[^s3]

## Connections

SOC 3 sits under security compliance frameworks (`kt:security-compliance-frameworks`) alongside the other AICPA SOC reports.[^s1] It `dependsOn` the Trust Services Criteria (`kt:trust-services-criteria`), the yardstick the CPA applies.[^s1] It `contrastsWith` SOC 2 (`kt:soc-2`), the restricted-use report built on the same criteria with full control detail, and with SOC 1 (`kt:soc-1`), which concerns controls relevant to financial reporting rather than the trust services categories.[^s1][^s6] Because Salesforce publishes reports per infrastructure and service, SOC 3 scoping ties to Hyperforce (`kt:hyperforce`), Data Cloud (`kt:data-cloud`) and Agentforce (`kt:agentforce`), each of which appears in its own listing.[^s4][^s5] Within a governance, risk and compliance program (`kt:governance-risk-and-compliance`), a SOC 3 serves as the freely shareable assurance summary, while the SOC 2 serves reviewers who need control-level detail.[^s1][^s6]

## Sources
[^s1]: AICPA & CIMA, "SOC 3® - SOC for Service Organizations: Trust Services Criteria for General Use Report". https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-3 (accessed 2026-11-21)
[^s2]: AICPA & CIMA, "Illustrative SOC 3® Report". https://www.aicpa-cima.com/resources/download/illustrative-soc-3-r-report (accessed 2026-11-21)
[^s3]: Salesforce, "SOC 3 - Salesforce Compliance Site". https://compliance.salesforce.com/en/categories/soc-3 (accessed 2026-11-21)
[^s4]: Salesforce, "SOC 3 Report - Salesforce Services on Hyperforce". https://compliance.salesforce.com/en/documents/a006e00000xpn2GAAQ (accessed 2026-11-21)
[^s5]: Salesforce, "SOC 3 Report - AI Platform and Agentforce". https://compliance.salesforce.com/en/documents/a006e0000115nMYAAY (accessed 2026-11-21)
[^s6]: Amazon Web Services, "SOC Compliance FAQs". https://aws.amazon.com/compliance/soc-faqs/ (accessed 2026-11-21)
