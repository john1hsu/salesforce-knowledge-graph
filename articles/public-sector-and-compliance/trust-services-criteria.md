---
id: kt:trust-services-criteria
type: ExternalConcept
title: Trust Services Criteria
aliases: [TSC, AICPA Trust Services Criteria, "TSP Section 100", "2017 Trust Services Criteria"]
domain: public-sector-and-compliance
summary: >-
  The control criteria set by the AICPA's Assurance Services Executive Committee for evaluating controls over
  security, availability, processing integrity, confidentiality and privacy; they are the yardstick a CPA applies in
  SOC 2, SOC 3 and SOC for Cybersecurity engagements, and a 2027 revision is out for comment.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:governance-risk-and-compliance, kt:shared-responsibility-model]
relations:
  - {predicate: consumedBy, object: kt:soc-2}
  - {predicate: consumedBy, object: kt:soc-3}
  - {predicate: dependsOn, object: kt:coso-internal-control-framework}
  - {predicate: contrastsWith, object: kt:nist-sp-800-53}
sources:
  - id: s1
    title: "2017 Trust Services Criteria (With Revised Points of Focus – 2022)"
    publisher: AICPA & CIMA
    url: https://www.aicpa-cima.com/resources/article/2017-trust-services-criteria-with-revised-points-of-focus-2022
    type: standards-body
    accessed: 2026-11-19
  - id: s2
    title: "TSP Section 100, 2017 Trust Services Criteria for Security, Availability, Processing Integrity, Confidentiality, and Privacy (copy hosted by Arpio)"
    publisher: AICPA
    url: https://arpio.io/wp-content/uploads/2020/08/trust-services-criteria.pdf
    type: standards-body
    accessed: 2026-11-19
  - id: s3
    title: "AICPA proposes update of SOC 2 Trust Services Criteria to enhance the relevance, usability and value of CPAs' reports"
    publisher: AICPA & CIMA
    url: https://www.aicpa-cima.com/news/article/aicpa-proposes-update-of-soc-2-r-trust-services-criteria-to-enhance-the-relevance-usability-and-value-of-cpas-reports
    type: standards-body
    accessed: 2026-11-19
  - id: s4
    title: "AICPA proposes improvements to SOC 2 Trust Services Criteria"
    publisher: Journal of Accountancy
    url: https://www.journalofaccountancy.com/news/2026/oct/aicpa-proposes-improvements-to-soc-2-trust-services-criteria.html
    type: news
    accessed: 2026-11-19
  - id: s5
    title: "Technical Line, 2 November 2022: revised SOC 2 points of focus and description criteria"
    publisher: EY
    url: https://ey.com/content/dam/ey-unified-site/ey-com/en-us/technical/accountinglink/documents/ey-ttp17549-221us-11-02-2022.pdf
    type: partner
    accessed: 2026-11-19
  - id: s6
    title: "SOC 2 — Salesforce Compliance"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/soc-2
    type: official-docs
    accessed: 2026-11-19
created: 2026-11-19
---

# Trust Services Criteria

The Trust Services Criteria (TSC) are the control criteria that the AICPA's Assurance Services Executive Committee (ASEC) maintains for evaluating and reporting on controls over information and systems that deliver products or services.[^s1] They cover five areas: security, availability, processing integrity, confidentiality and privacy, and are written for attestation and consulting engagements across a whole entity or a part of it such as a division.[^s1][^s2] The criteria are not a report and not a certificate; they are the benchmark an auditor measures controls against. For Salesforce practitioners that distinction matters, because when a customer's risk team reads Salesforce's SOC 2 report, the opinion in it is expressed against these criteria.[^s2][^s6]

## The five categories

The codified text (TSP Section 100) defines each category in a sentence:[^s2]

- **Security.** Information and systems are protected against unauthorized access, disclosure and damage.[^s2]
- **Availability.** Information and systems are available for operation and use; the criteria set no minimum performance level.[^s2]
- **Processing integrity.** System processing is complete, valid, accurate, timely and authorized.[^s2]
- **Confidentiality.** Information designated as confidential is protected, whether or not it is personal information.[^s2]
- **Privacy.** Personal information is collected, used, retained, disclosed and disposed of appropriately.[^s2]

The confidentiality/privacy split trips people up: confidentiality applies to any sensitive information an entity commits to protect, while privacy applies only to personal information.[^s2]

## How the criteria are structured

The 2017 criteria are organised around the COSO 2013 internal-control framework. The common criteria in series CC1 to CC5 (control environment, communication and information, risk assessment, monitoring activities and control activities) map onto COSO's 17 principles.[^s2] Four further series are supplemental criteria specific to technology: CC6 logical and physical access, CC7 system operations, CC8 change management and CC9 risk mitigation.[^s2] Together CC1 to CC9 form the common criteria that address security; the other categories add their own criteria on top, such as the availability series A1 on capacity management, environmental protection, backup and recovery, and recovery plan testing.[^s2]

Each criterion comes with **points of focus**, which describe important characteristics of the criterion to help management design controls and help practitioners judge them. They are not a checklist: an entity need not address every point of focus and may tailor them to its situation.[^s2][^s5]

## Engagements that use them

The same criteria drive several AICPA services. A SOC 2 examination reports on controls relevant to one or more categories; a SOC 3 report gives a general-use opinion without the detailed tests; SOC for Cybersecurity evaluates an entity-wide cybersecurity risk-management program using the security, availability and confidentiality criteria; and SOC for Supply Chain applies them to systems that produce or distribute goods.[^s2] Practitioners can also use them in readiness work under consulting standards, where no opinion is issued.[^s2]

## Revisions

In 2022 the AICPA revised the points of focus without changing the 2017 criteria themselves. Additions covered more granular risk assessment, logical access across all account types including service accounts, software patching, data recoverability in response to ransomware, and privacy points that distinguish data controllers from processors.[^s5] The companion SOC 2 description criteria were updated at the same time.[^s5]

On 28 October 2026 the AICPA issued an exposure draft of 2027 SOC 2 Trust Services Criteria and Description Criteria. It proposes merging overlapping criteria, removing outdated ones, adding new ones and rewording others for clarity.[^s3] New points of focus address AI governance, model monitoring, prompt manipulation, data poisoning, transparency of AI-generated outputs, training data management and automated decision-making.[^s3][^s4] Comments are due 15 January 2027; if approved, the criteria would apply to engagements beginning on or after 31 December 2027, with early adoption permitted.[^s3][^s4]

## Why it matters on Salesforce projects

Salesforce states that its SOC 2 reports cover controls over the security, availability and confidentiality of customer data, so processing integrity and privacy are not among the categories it names.[^s6] When a stakeholder asks for assurance on those two categories, the answer has to come from other evidence or from the customer's own controls.[^s6] The AI-related points of focus in the 2027 draft are also worth tracking for teams deploying generative AI features, because future SOC 2 reports may be tested against them.[^s3]

## Connections

The TSC sit under security compliance frameworks (`kt:security-compliance-frameworks`) as the AICPA's criteria set.[^s1] They are `consumedBy` SOC 2 (`kt:soc-2`) and SOC 3 (`kt:soc-3`), which report against them.[^s2] They `dependsOn` the COSO internal-control framework (`kt:coso-internal-control-framework`), whose 17 principles anchor the common criteria.[^s2] They `contrastsWith` NIST SP 800-53 (`kt:nist-sp-800-53`): both are often mapped to each other, but the TSC are high-level criteria with optional points of focus, not a prescriptive control catalogue.[^s2][^s5] Because a service auditor's opinion covers only the provider's controls, they relate to the shared responsibility model (`kt:shared-responsibility-model`) and to governance, risk and compliance programs (`kt:governance-risk-and-compliance`) that consume the resulting reports.[^s2][^s6]

## Sources
[^s1]: AICPA & CIMA, "2017 Trust Services Criteria (With Revised Points of Focus – 2022)". https://www.aicpa-cima.com/resources/article/2017-trust-services-criteria-with-revised-points-of-focus-2022 (accessed 2026-11-19)
[^s2]: AICPA, "TSP Section 100, 2017 Trust Services Criteria for Security, Availability, Processing Integrity, Confidentiality, and Privacy" (copy hosted by Arpio). https://arpio.io/wp-content/uploads/2020/08/trust-services-criteria.pdf (accessed 2026-11-19)
[^s3]: AICPA & CIMA, "AICPA proposes update of SOC 2 Trust Services Criteria to enhance the relevance, usability and value of CPAs' reports". https://www.aicpa-cima.com/news/article/aicpa-proposes-update-of-soc-2-r-trust-services-criteria-to-enhance-the-relevance-usability-and-value-of-cpas-reports (accessed 2026-11-19)
[^s4]: Journal of Accountancy, "AICPA proposes improvements to SOC 2 Trust Services Criteria". https://www.journalofaccountancy.com/news/2026/oct/aicpa-proposes-improvements-to-soc-2-trust-services-criteria.html (accessed 2026-11-19)
[^s5]: EY, "Technical Line, 2 November 2022: revised SOC 2 points of focus and description criteria". https://ey.com/content/dam/ey-unified-site/ey-com/en-us/technical/accountinglink/documents/ey-ttp17549-221us-11-02-2022.pdf (accessed 2026-11-19)
[^s6]: Salesforce, "SOC 2 — Salesforce Compliance". https://compliance.salesforce.com/en/soc-2 (accessed 2026-11-19)
