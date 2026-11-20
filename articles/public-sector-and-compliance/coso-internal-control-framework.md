---
id: kt:coso-internal-control-framework
type: ExternalConcept
title: COSO Internal Control Framework
aliases: [COSO, "COSO Internal Control–Integrated Framework", "Internal Control–Integrated Framework", ICIF-2013, COSO 2013, COSO cube]
domain: public-sector-and-compliance
summary: >-
  The Internal Control–Integrated Framework from the Committee of Sponsoring Organizations of the Treadway
  Commission (COSO), first issued in 1992 and refreshed in 2013, which defines internal control around three
  objective categories, five components and 17 principles; it is a framework many US public companies use for
  their Sarbanes-Oxley ICFR assessments and the control backbone beneath the AICPA Trust Services Criteria.
release: "Winter '27"
status: concept
broader: [kt:governance-risk-and-compliance, kt:security-compliance-frameworks]
related: [kt:sarbanes-oxley-act, kt:soc-1, kt:corporate-governance, kt:organizational-governance]
relations:
  - {predicate: consumedBy, object: kt:trust-services-criteria}
  - {predicate: contrastsWith, object: kt:cobit}
  - {predicate: contrastsWith, object: kt:nist-sp-800-53}
sources:
  - id: s1
    title: "Internal Control | COSO (Guidance on Internal Control)"
    publisher: COSO
    url: https://coso.org/guidance-on-ic
    type: standards-body
    accessed: 2026-11-20
  - id: s2
    title: "Internal Control | COSO"
    publisher: COSO
    url: https://coso.org/internal-control
    type: standards-body
    accessed: 2026-11-20
  - id: s3
    title: "Internal Control — Integrated Framework: Framework and Appendices (post public exposure version, September 2012)"
    publisher: COSO
    url: https://experience.famu.edu/administration/audit/standards/coso_IC%20Integrated%20Framework.pdf
    type: standards-body
    accessed: 2026-11-20
  - id: s4
    title: "Newly released COSO framework a fresh look at internal control"
    publisher: Journal of Accountancy (AICPA & CIMA)
    url: https://www.journalofaccountancy.com/news/2013/may/20137970.html
    type: news
    accessed: 2026-11-20
  - id: s5
    title: "Commission Guidance Regarding Management's Report on Internal Control Over Financial Reporting (Release Nos. 33-8810; 34-55929)"
    publisher: U.S. Securities and Exchange Commission, Federal Register
    url: https://www.govinfo.gov/content/pkg/FR-2007-06-27/html/E7-12299.htm
    type: government
    accessed: 2026-11-20
  - id: s6
    title: "4310 Management's annual report on internal control over financial reporting"
    publisher: PwC Viewpoint
    url: https://viewpoint.pwc.com/dt/us/en/sec/financial_reporting_m/financial_reporting___4_US/topic_4_independent__US/4300_report_on_inter_US/4310_managements_ann_US.html
    type: partner
    accessed: 2026-11-20
  - id: s7
    title: "SOC 1 — Salesforce Compliance"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/soc-1
    type: official-docs
    accessed: 2026-11-20
  - id: s8
    title: "Admin Security Workshop — Exercise 1: Using the Audit Trail"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/workshops/admin-security-workshop/monitoring-and-response/1-audit-trail
    type: official-learning
    accessed: 2026-11-20
created: 2026-11-20
---

# COSO Internal Control Framework

The **COSO Internal Control–Integrated Framework** (often abbreviated ICIF-2013, or simply "COSO") is the most widely used model for designing and judging internal control in organizations. It is published by the Committee of Sponsoring Organizations of the Treadway Commission, a private-sector initiative jointly sponsored and funded by five professional bodies: the American Accounting Association, the AICPA, Financial Executives International, the Institute of Management Accountants and the Institute of Internal Auditors.[^s3] COSO first issued the framework in 1992 and refreshed it in 2013.[^s1][^s2]

Salesforce does not implement COSO as a product feature. It matters to Salesforce practitioners because customers running finance-relevant processes on the platform are usually assessed against it, and because Salesforce publishes SOC 1 reports that examine its controls relevant to customers' financial reporting.[^s7][^s6]

## Definition and structure

COSO describes internal control as a process carried out by an entity's board, management and other personnel to give reasonable assurance that objectives will be achieved.[^s3] Those objectives fall into three categories: **operations**, **reporting** (financial and non-financial, internal and external) and **compliance**.[^s3] The 2013 update kept the core definition and the component model of the 1992 original, while making implicit concepts explicit.[^s3][^s4]

The framework has five **components**:[^s4]

- **Control environment**: the tone, integrity, oversight and accountability structures set by the board and management.[^s3][^s4]
- **Risk assessment**: identifying and analyzing risks to objectives, including fraud risk and significant change.[^s3][^s4]
- **Control activities**: the policies and procedures, including technology general controls, that mitigate those risks.[^s3][^s4]
- **Information and communication**: obtaining quality information and communicating it internally and externally.[^s3][^s4]
- **Monitoring activities**: ongoing and separate evaluations that find and correct control deficiencies.[^s3][^s4]

The 2013 edition spread **17 principles** across these five components.[^s4] Each principle is supported by *points of focus*, typical characteristics that help management judge whether the principle is present and functioning.[^s3] An effective system needs all five components, and the relevant principles, to be present and working together.[^s3]

## History and transition

COSO released the updated framework in May 2013.[^s4] It allowed a transition period during which the 1992 version stayed acceptable, and organizations were asked to disclose which version they used; COSO treated the 1992 framework as superseded from December 15, 2014.[^s4][^s1] COSO has since added companion guidance that applies the same framework to new subjects, including internal control over sustainability reporting (2023), robotic process automation (2024) and generative AI (2026).[^s1][^s2]

## Role in Sarbanes-Oxley reporting

SEC rules (Item 308(a) of Regulation S-K) require management of a US public company to report annually on internal control over financial reporting (ICFR), and the evaluation must use a suitable, recognized control framework.[^s6] In its 2007 interpretive guidance for management, the SEC named COSO's framework as an example of a suitable framework, alongside Canada's CoCo guidance and the UK Turnbull Report.[^s5] Many companies follow COSO, though other frameworks are also acceptable.[^s6] Accelerated filers also need an auditor's attestation on ICFR, which in practice is planned around the same components and principles.[^s6]

## Applying it to a Salesforce org

When Salesforce hosts financially significant processes (quoting, billing, revenue schedules, commissions), the org's configuration becomes part of the control activities and monitoring that management evaluates under a suitable framework.[^s6][^s3] Salesforce's SOC 1 reports cover the provider's side of that boundary, giving assurance over controls in its own environment.[^s7] On the customer side, monitoring evidence often comes from Setup Audit Trail, which tracks changes to security settings such as MFA requirements, login IP ranges and permission set assignments, and from Login History, which records each login attempt.[^s8] COSO says which control objectives to cover but prescribes no Salesforce settings, so teams map their own org controls to its principles.[^s3]

## Connections

COSO sits under `kt:governance-risk-and-compliance`, the discipline that turns governing-body direction into risk and compliance controls, and under `kt:security-compliance-frameworks` as one of the reference frameworks auditors use.[^s3] It is `consumedBy` the `kt:trust-services-criteria`, the reverse of that node's `dependsOn` edge to COSO: SOC 2 and SOC 3 examinations judge controls against criteria that build on this framework. It underpins management's ICFR assessment under the `kt:sarbanes-oxley-act`, which is also why a service organization's `kt:soc-1` report matters to its customers' auditors.[^s5][^s6] It complements `kt:corporate-governance` and `kt:organizational-governance`, where the board's oversight role forms the control environment.[^s3] It `contrastsWith` `kt:cobit`, which addresses governance of information and technology specifically, and with `kt:nist-sp-800-53`, a catalog of specific security and privacy controls, whereas COSO is a principles-based model spanning operations, reporting and compliance.[^s3]

## Sources
[^s1]: COSO, "Internal Control | COSO (Guidance on Internal Control)". https://coso.org/guidance-on-ic (accessed 2026-11-20)
[^s2]: COSO, "Internal Control | COSO". https://coso.org/internal-control (accessed 2026-11-20)
[^s3]: COSO, "Internal Control — Integrated Framework: Framework and Appendices" (post public exposure version, September 2012). https://experience.famu.edu/administration/audit/standards/coso_IC%20Integrated%20Framework.pdf (accessed 2026-11-20)
[^s4]: Journal of Accountancy (AICPA & CIMA), "Newly released COSO framework a fresh look at internal control". https://www.journalofaccountancy.com/news/2013/may/20137970.html (accessed 2026-11-20)
[^s5]: U.S. SEC, "Commission Guidance Regarding Management's Report on Internal Control Over Financial Reporting", Federal Register Vol. 72, No. 123 (June 27, 2007). https://www.govinfo.gov/content/pkg/FR-2007-06-27/html/E7-12299.htm (accessed 2026-11-20)
[^s6]: PwC Viewpoint, "4310 Management's annual report on internal control over financial reporting". https://viewpoint.pwc.com/dt/us/en/sec/financial_reporting_m/financial_reporting___4_US/topic_4_independent__US/4300_report_on_inter_US/4310_managements_ann_US.html (accessed 2026-11-20)
[^s7]: Salesforce, "SOC 1 — Salesforce Compliance". https://compliance.salesforce.com/en/soc-1 (accessed 2026-11-20)
[^s8]: Salesforce Developers, "Admin Security Workshop — Exercise 1: Using the Audit Trail". https://developer.salesforce.com/workshops/admin-security-workshop/monitoring-and-response/1-audit-trail (accessed 2026-11-20)
