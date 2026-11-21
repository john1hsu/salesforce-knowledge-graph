---
id: kt:sarbanes-oxley-act
type: ExternalConcept
title: Sarbanes-Oxley Act
aliases: [SOX, Sarbanes-Oxley, "Sarbanes-Oxley Act of 2002", SOX compliance, "Public Law 107-204", SOX 404]
domain: public-sector-and-compliance
summary: >-
  The US federal law enacted on 30 July 2002 to improve the accuracy and reliability of public-company
  disclosures; it created the PCAOB, requires officer certification of periodic reports and, under Section 404,
  a management assessment of internal control over financial reporting (ICFR) with auditor attestation for
  larger issuers, which pulls the configuration and access controls of a Salesforce org holding financial data
  into audit scope.
release: "Winter '27"
status: concept
broader: [kt:governance-risk-and-compliance, kt:corporate-governance]
related: [kt:soc-1, kt:coso-internal-control-framework, kt:setup-audit-trail, kt:field-audit-trail, kt:login-history]
relations:
  - {predicate: contrastsWith, object: kt:hipaa}
sources:
  - id: s1
    title: "Public Law 107-204 — Sarbanes-Oxley Act of 2002"
    publisher: U.S. Government Publishing Office (govinfo)
    url: https://www.govinfo.gov/content/pkg/PLAW-107publ204/html/PLAW-107publ204.htm
    type: government
    accessed: 2026-11-21
  - id: s2
    title: "Sarbanes-Oxley Act: Compliance Costs Are Higher for Larger Companies but More Burdensome for Smaller Ones (GAO-25-107500)"
    publisher: U.S. Government Accountability Office
    url: https://files.gao.gov/reports/GAO-25-107500/index.html
    type: government
    accessed: 2026-11-21
  - id: s3
    title: "Internal Control Over Financial Reporting in Exchange Act Periodic Reports of Non-Accelerated Filers and Newly Public Companies (Release 33-8731)"
    publisher: U.S. Securities and Exchange Commission
    url: https://www.sec.gov/rule-release/33-8731
    type: government
    accessed: 2026-11-21
  - id: s4
    title: "SetupAuditTrail | Object Reference for the Salesforce Platform"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_setupaudittrail.htm
    type: official-docs
    accessed: 2026-11-21
  - id: s5
    title: "Exercise 1: Using the Audit Trail (Salesforce Admin Security Workshop)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/workshops/admin-security-workshop/monitoring-and-response/1-audit-trail
    type: official-learning
    accessed: 2026-11-21
created: 2026-11-21
---

# Sarbanes-Oxley Act

The Sarbanes-Oxley Act of 2002 (SOX) is a US federal statute, Public Law 107-204, enacted on 30 July 2002. Its stated purpose is to protect investors by making corporate disclosures under the securities laws more accurate and reliable.[^s1] The Act is organized into eleven titles covering auditor oversight, auditor independence, corporate responsibility, enhanced financial disclosures and criminal penalties.[^s1] For Salesforce teams it is rarely a direct requirement on the platform. Instead it becomes a requirement on any org whose data feeds a public company's financial statements, such as opportunities, orders, billing, revenue schedules or commissions.[^s1][^s2]

## Key provisions

- **Section 101 (PCAOB).** Creates the Public Company Accounting Oversight Board, a nonprofit body of five members, of whom at most two may be CPAs.[^s1]
- **Section 103 (audit standards).** Requires registered audit firms to keep audit workpapers for at least seven years and to have a second partner review each audit.[^s1]
- **Section 302 (officer certification).** The principal executive and financial officers certify each annual and quarterly report and take responsibility for internal controls and for evaluating them.[^s1]
- **Section 404(a) (management assessment).** Every annual report must include an internal control report with management's assessment of ICFR effectiveness as of fiscal year end.[^s1][^s2]
- **Section 404(b) (auditor attestation).** The company's registered public accounting firm attests to and reports on management's assessment, as part of the audit rather than as a separate engagement.[^s1]
- **Section 409 (real-time disclosure).** Issuers must disclose material changes in financial condition or operations rapidly and in plain English.[^s1]

## Who has to comply

Section 404(a) applies to all public companies, but 404(b) attestation does not. GAO reports that the Dodd-Frank Act of 2010 permanently exempted issuers with less than $75 million in public float, and that emerging growth companies under the 2012 JOBS Act are exempt for up to five years.[^s2] Applying the internal control rules to smaller and newly public companies was a long-running question; the SEC proposed dedicated rules for non-accelerated filers and newly public companies in August 2006.[^s3][^s2] Compliance is costly: in a GAO sample, nonexempt companies had audit costs 19% higher than exempt ones, and median audit fees rose about $219,000 in the year a company lost its exemption.[^s2]

## What SOX means for a Salesforce org

Auditors test ICFR controls that touch financial data, so a CRM that originates bookings or revenue figures is in scope alongside the ERP. In practice that means evidencing who can change configuration, who has access, and when changes happened.[^s2][^s4] Salesforce's SetupAuditTrail object records changes made in Setup for at least the last 180 days, including the action, the Setup section and any Login-As user who performed it, and it can be queried with SOQL for evidence extraction.[^s4] Salesforce's admin security workshop shows downloading six months of Setup Audit Trail as CSV to review permission set assignments, MFA and login IP range changes, and pairing it with Login History for failed or restricted logins.[^s5] Because the in-org window is limited, plan to export these logs regularly if an audit period runs longer than the retention window.[^s4][^s5]


## Connections

SOX sits under governance, risk and compliance (`kt:governance-risk-and-compliance`) and corporate governance (`kt:corporate-governance`) because it is a legal mandate on how public companies govern financial reporting.[^s1] It is related to the COSO internal control framework (`kt:coso-internal-control-framework`), described in its own node as a common basis for the Section 404 assessment, and to SOC 1 (`kt:soc-1`), the provider-side report written for customers' ICFR audits.[^s1][^s2] Inside the org, configuration evidence comes from Setup Audit Trail (`kt:setup-audit-trail`) and authentication evidence from Login History (`kt:login-history`), while Field Audit Trail (`kt:field-audit-trail`) addresses longer retention of data-change history.[^s4][^s5] It `contrastsWith` HIPAA (`kt:hipaa`): both are US federal statutes that drive Salesforce controls, but SOX targets the integrity of financial reporting rather than the privacy of health information.[^s1]

## Sources
[^s1]: U.S. Government Publishing Office (govinfo), "Public Law 107-204 — Sarbanes-Oxley Act of 2002". https://www.govinfo.gov/content/pkg/PLAW-107publ204/html/PLAW-107publ204.htm (accessed 2026-11-21)
[^s2]: U.S. Government Accountability Office, "Sarbanes-Oxley Act: Compliance Costs Are Higher for Larger Companies but More Burdensome for Smaller Ones (GAO-25-107500)". https://files.gao.gov/reports/GAO-25-107500/index.html (accessed 2026-11-21)
[^s3]: U.S. Securities and Exchange Commission, "Internal Control Over Financial Reporting in Exchange Act Periodic Reports of Non-Accelerated Filers and Newly Public Companies (Release 33-8731)". https://www.sec.gov/rule-release/33-8731 (accessed 2026-11-21)
[^s4]: Salesforce, "SetupAuditTrail | Object Reference for the Salesforce Platform". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_setupaudittrail.htm (accessed 2026-11-21)
[^s5]: Salesforce Developers, "Exercise 1: Using the Audit Trail (Salesforce Admin Security Workshop)". https://developer.salesforce.com/workshops/admin-security-workshop/monitoring-and-response/1-audit-trail (accessed 2026-11-21)
