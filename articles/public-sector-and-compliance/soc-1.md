---
id: kt:soc-1
type: ExternalConcept
title: SOC 1
aliases: [SOC 1 report, "SOC 1 Type 2", "SOC 1 Type II", "SOC for Service Organizations: ICFR", System and Organization Controls 1]
domain: public-sector-and-compliance
summary: >-
  The AICPA attestation report, performed under AT-C section 320, in which a service auditor examines a service
  organization's controls that are relevant to its customers' internal control over financial reporting; Salesforce
  publishes SOC 1 reports per service and infrastructure on its compliance site.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:hyperforce, kt:shared-responsibility-model, kt:governance-risk-and-compliance, kt:sarbanes-oxley-act]
relations:
  - {predicate: contrastsWith, object: kt:soc-2}
sources:
  - id: s1
    title: "Explaining the 3 faces of SOC"
    publisher: Journal of Accountancy (AICPA & CIMA)
    url: https://www.journalofaccountancy.com/newsletters/2016/jun/3-face-of-soc/
    type: news
    accessed: 2026-11-17
  - id: s2
    title: "Reporting on an Examination of Controls at a Service Organization Relevant to User Entities' Internal Control Over Financial Reporting (SOC 1) Guide"
    publisher: AICPA & CIMA
    url: https://www.aicpa-cima.com/cpe-learning/publication/reporting-on-an-examination-of-controls-at-a-service-organization-relevant-to-user-entities-internal-control-over-financial-reporting-soc-1-guide
    type: standards-body
    accessed: 2026-11-17
  - id: s3
    title: "SOC 1 — Salesforce Compliance"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/soc-1
    type: official-docs
    accessed: 2026-11-17
  - id: s4
    title: "SOC 1 Report - Salesforce Services on Hyperforce"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/documents/a006e00000xpn1JAAQ
    type: official-docs
    accessed: 2026-11-17
  - id: s5
    title: "SOC 1 Report - Corporate Services"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/documents/a005A00000qM6abQAC
    type: official-docs
    accessed: 2026-11-17
  - id: s6
    title: "Subservice Organizations in SOC Reports: Carve-Out vs. Inclusive Method"
    publisher: Compass IT Compliance
    url: https://www.compassitc.com/blog/subservice-organizations-in-soc-reports-carve-out-vs.-inclusive-method
    type: partner
    accessed: 2026-11-17
created: 2026-11-17
---

# SOC 1

SOC 1 is the AICPA System and Organization Controls report on a service organization's controls that are relevant to a user entity's internal control over financial reporting (ICFR).[^s1] A CPA acting as service auditor performs the examination under the attestation standard AT-C section 320, and the AICPA maintains a dedicated SOC 1 guide for these engagements, most recently revised in a 2025 edition.[^s2] For Salesforce customers, SOC 1 matters whenever an org holds or processes data that flows into the financial statements, such as orders, billing, revenue or commissions, because the customer's external auditor may ask how the cloud provider's controls support that data.[^s3]

## How a SOC 1 report works

A SOC 1 report describes the service organization's system and states control objectives, then the service auditor gives an opinion on them.[^s1] A Type 1 report covers the fairness of the system description and the suitability of control design as of a specified date. A Type 2 report adds an opinion on whether the controls operated effectively throughout a period, along with a description of the auditor's tests and their results.[^s1] Use of the report is restricted to the service organization's management, its user entities and the user entities' auditors.[^s1]

The report's main reader is the user auditor: the firm auditing a customer's financial statements. The AICPA guide is written for both service auditors and those user auditors, and it covers how a type 1 or type 2 report is used in a financial-statement audit.[^s2] It also gives reporting guidance for subservice organizations and for software-as-a-service providers.[^s2]

Two features of the report shift work back to the customer. Complementary user entity controls (CUECs) are controls the customer is expected to operate so that the provider's control objectives are achieved.[^s6] And when a provider relies on a subservice organization, such as an infrastructure host, the report can either include that party's controls in testing (the inclusive method) or exclude them (the carve-out method). Carve-out is the more common approach, and the opinion then covers only the provider's own controls.[^s6][^s2]

## Salesforce's SOC 1 reports

Salesforce's compliance site describes its SOC 1 reports as primarily examining controls relevant to customers' financial reporting, covering IT general controls plus controls over the availability, confidentiality and security of customer data.[^s3] Reports are listed per service and per infrastructure (first party, AWS, GCP and Hyperforce).[^s3]

- **Salesforce Services on Hyperforce.** Its scope includes core Salesforce services, B2C Commerce, Data Cloud and Tableau Next. The latest listed version covers 1 November 2025 to 30 April 2026, and earlier versions follow six-month periods.[^s4]
- **Corporate Services.** This report covers common controls shared across services, including risk management, logical and physical security, change management, incident management and business continuity.[^s5]
- **Consolidation.** From reports published in June 2026, the Corporate Services, Hyperforce and First Party reports are combined into one Salesforce Services SOC report.[^s4][^s5]

Downloading any version requires logging in to the compliance site.[^s4][^s5]

## Gotchas for architects

- **Check scope against your design.** A report names specific services and infrastructure; confirm that each cloud you rely on for financial data appears in it.[^s3][^s4]
- **Mind the period.** Salesforce's reports cover six-month windows, so an audit year usually needs two reports, plus a bridge letter for any gap.[^s4][^s6]
- **Own your CUECs.** User provisioning, permissions and the configuration you build in your org remain your controls to evidence.[^s6]
- **Follow carve-outs.** If a subservice organization is carved out, obtain and review that party's own SOC report too.[^s6]

## Connections

SOC 1 sits under security compliance frameworks (`kt:security-compliance-frameworks`) as the financial-reporting member of the AICPA SOC family.[^s1] It `contrastsWith` SOC 2 (`kt:soc-2`), which uses the Trust Services Criteria for security, availability, processing integrity, confidentiality or privacy instead of ICFR-focused control objectives.[^s1] Its reason to exist is ICFR, which is why it relates to the Sarbanes-Oxley Act (`kt:sarbanes-oxley-act`) and to governance, risk and compliance programs (`kt:governance-risk-and-compliance`) that collect provider evidence.[^s2][^s3] Because Salesforce publishes reports per infrastructure, scoping ties to Hyperforce (`kt:hyperforce`).[^s4] The split between the provider's tested controls and the customer's CUECs is a concrete case of the shared responsibility model (`kt:shared-responsibility-model`).[^s6]

## Sources
[^s1]: Journal of Accountancy (AICPA & CIMA), "Explaining the 3 faces of SOC". https://www.journalofaccountancy.com/newsletters/2016/jun/3-face-of-soc/ (accessed 2026-11-17)
[^s2]: AICPA & CIMA, "Reporting on an Examination of Controls at a Service Organization Relevant to User Entities' Internal Control Over Financial Reporting (SOC 1) Guide". https://www.aicpa-cima.com/cpe-learning/publication/reporting-on-an-examination-of-controls-at-a-service-organization-relevant-to-user-entities-internal-control-over-financial-reporting-soc-1-guide (accessed 2026-11-17)
[^s3]: Salesforce, "SOC 1 — Salesforce Compliance". https://compliance.salesforce.com/en/soc-1 (accessed 2026-11-17)
[^s4]: Salesforce, "SOC 1 Report - Salesforce Services on Hyperforce". https://compliance.salesforce.com/en/documents/a006e00000xpn1JAAQ (accessed 2026-11-17)
[^s5]: Salesforce, "SOC 1 Report - Corporate Services". https://compliance.salesforce.com/en/documents/a005A00000qM6abQAC (accessed 2026-11-17)
[^s6]: Compass IT Compliance, "Subservice Organizations in SOC Reports: Carve-Out vs. Inclusive Method". https://www.compassitc.com/blog/subservice-organizations-in-soc-reports-carve-out-vs.-inclusive-method (accessed 2026-11-17)
