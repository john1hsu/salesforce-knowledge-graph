---
id: kt:soc-2
type: ExternalConcept
title: SOC 2
aliases: [SOC 2 report, "SOC 2 Type 2", "SOC 2 Type II", System and Organization Controls 2, "SOC for Service Organizations: Trust Services Criteria"]
domain: public-sector-and-compliance
summary: >-
  The AICPA attestation report in which an independent CPA examines a service organization's controls relevant to
  security, availability, processing integrity, confidentiality or privacy; Salesforce publishes SOC 2 reports per
  service and infrastructure, covering security, availability and confidentiality, behind a login on its compliance site.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:hyperforce, kt:nist-sp-800-53, kt:fedramp, kt:marketing-cloud-engagement, kt:data-residency]
relations:
  - {predicate: contrastsWith, object: kt:iso-iec-27001}
  - {predicate: dependsOn, object: kt:trust-services-criteria}
  - {predicate: contrastsWith, object: kt:soc-1}
sources:
  - id: s1
    title: "System and Organization Controls: SOC Suite of Services"
    publisher: AICPA & CIMA
    url: https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services
    type: standards-body
    accessed: 2026-11-07
  - id: s2
    title: "Data Security in the Cloud: SOC Reports for Service Organizations"
    publisher: Wolters Kluwer
    url: https://wolterskluwer.com/en/expert-insights/data-security-in-the-cloud-soc-reports-for-service-orgs
    type: news
    accessed: 2026-11-07
  - id: s3
    title: "SOC 2 — Salesforce Compliance"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/soc-2
    type: official-docs
    accessed: 2026-11-07
  - id: s4
    title: "SOC 2 Report - Salesforce Services on Hyperforce"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/documents/a006e00000xpn20AAA
    type: official-docs
    accessed: 2026-11-07
  - id: s5
    title: "SOC 2 Report - Marketing Cloud Engagement on Hyperforce + Marketing Cloud Growth"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/documents/a006e00000yuiGOAAY
    type: official-docs
    accessed: 2026-11-07
  - id: s6
    title: "SOC 3 — Salesforce Compliance"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/soc-3
    type: official-docs
    accessed: 2026-11-07
created: 2026-11-07
---

# SOC 2

SOC 2 is one of the System and Organization Controls (SOC) services that the AICPA defines for CPAs reporting on system-level controls at a service organization.[^s1] A SOC 2 engagement examines controls relevant to five trust services categories: security, availability, processing integrity, confidentiality and privacy.[^s1] For Salesforce practitioners it is one of the most requested artifacts in vendor-risk reviews: a customer's security or audit team usually asks for Salesforce's SOC 2 report before approving a new cloud, org or integration.[^s3]

## How a SOC 2 report works

A SOC 2 report is an attestation, not a certificate. An independent CPA firm examines management's description of the system and tests its controls against the AICPA Trust Services Criteria, under the attestation standards AT-C 105 and 205.[^s2] The service organization chooses which categories are in scope, so two SOC 2 reports can cover quite different ground.[^s1][^s2]

Reports come in two types. A Type 1 report describes the system and assesses whether controls are suitably designed as of a single date. A Type 2 report covers a period, commonly six to twelve months, and adds testing of whether the controls actually operated effectively throughout it.[^s2] Organizations often start with a Type 1 and use the findings to remediate before a Type 2.[^s2] Distribution matters too: SOC 2 reports are meant for readers who understand the service organization and its controls, whereas a SOC 3 report is a general-use summary of the same kind of examination that leaves out the detailed control descriptions, tests and results and can be shared freely.[^s2]

The AICPA's SOC family also includes SOC 1, which addresses controls relevant to user entities' internal control over financial reporting (prepared under AT-C 320), plus SOC for Cybersecurity and SOC for Supply Chain.[^s1][^s2] The AICPA has issued an exposure draft proposing 2027 SOC 2 Trust Services Criteria and Description Criteria, so the criteria themselves are due to be revised.[^s1]

## Salesforce's SOC 2 reports

Salesforce's compliance site describes its SOC 2 reports as covering controls over the security, availability and confidentiality of customer data; processing integrity and privacy are not named.[^s3] Reports are listed per service and per infrastructure (first party, AWS, Hyperforce, GCP or Azure), and downloading any version requires logging in to the compliance site.[^s3][^s4]

Two listings show how this looks in practice:

- **Salesforce Services on Hyperforce.** This report covers Salesforce Services on Hyperforce, B2C Commerce on Hyperforce, Data Cloud and Tableau Next, and also covers IT general controls. Its latest listed version runs from 1 November 2025 to 30 April 2026. Salesforce says that from reports published in June 2026 it is consolidated into one Salesforce Services SOC report spanning corporate, first-party and Hyperforce services.[^s4]
- **Marketing Cloud.** A separate report covers Marketing Cloud Engagement on Hyperforce together with Marketing Cloud Growth; its most recent version covers 1 May 2025 to 30 April 2026.[^s5]

Salesforce also lists SOC 3 reports covering the security, availability and confidentiality principles.[^s6]

## Gotchas for architects

- **Match the report to the design.** A report covers named services on named infrastructure. Check that each cloud in your solution, and where it runs, appears in the report you hand to auditors.[^s3][^s4]
- **Watch the period.** A Type 2 opinion speaks only to its examination period; check the dates against your audit window.[^s2][^s4]
- **Category scope.** If a stakeholder needs assurance over processing integrity or privacy, Salesforce's SOC 2 listing names only security, availability and confidentiality.[^s3]
- **Report ≠ your compliance.** The report describes the provider's controls; what you build and configure in your own org remains yours to control and evidence.[^s2]

## Connections

SOC 2 sits under security compliance frameworks (`kt:security-compliance-frameworks`) as the US audit-report scheme in that family.[^s1] It `dependsOn` the AICPA Trust Services Criteria (`kt:trust-services-criteria`), which define what the CPA tests.[^s1][^s2] It `contrastsWith` ISO/IEC 27001 (`kt:iso-iec-27001`), which is delivered as a certificate against a management-system standard rather than a CPA opinion, and with SOC 1 (`kt:soc-1`), which targets financial-reporting controls instead of the trust services categories.[^s2][^s3] Because Salesforce publishes reports per infrastructure, SOC 2 scoping ties directly to Hyperforce (`kt:hyperforce`) and to data residency (`kt:data-residency`) choices.[^s3][^s4] Marketing Cloud Engagement (`kt:marketing-cloud-engagement`) has its own report, separate from the core platform's.[^s5] Because SOC is a CPA attestation service rather than a government authorization, it is a separate scheme from the US federal FedRAMP program (`kt:fedramp`) and its NIST SP 800-53 (`kt:nist-sp-800-53`) control baseline, which are covered in their own nodes.[^s1]

## Sources
[^s1]: AICPA & CIMA, "System and Organization Controls: SOC Suite of Services". https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services (accessed 2026-11-07)
[^s2]: Wolters Kluwer, "Data Security in the Cloud: SOC Reports for Service Organizations". https://wolterskluwer.com/en/expert-insights/data-security-in-the-cloud-soc-reports-for-service-orgs (accessed 2026-11-07)
[^s3]: Salesforce, "SOC 2 — Salesforce Compliance". https://compliance.salesforce.com/en/soc-2 (accessed 2026-11-07)
[^s4]: Salesforce, "SOC 2 Report - Salesforce Services on Hyperforce". https://compliance.salesforce.com/en/documents/a006e00000xpn20AAA (accessed 2026-11-07)
[^s5]: Salesforce, "SOC 2 Report - Marketing Cloud Engagement on Hyperforce + Marketing Cloud Growth". https://compliance.salesforce.com/en/documents/a006e00000yuiGOAAY (accessed 2026-11-07)
[^s6]: Salesforce, "SOC 3 — Salesforce Compliance". https://compliance.salesforce.com/en/soc-3 (accessed 2026-11-07)
