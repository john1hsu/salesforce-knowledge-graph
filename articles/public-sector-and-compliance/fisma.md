---
id: kt:fisma
type: ExternalConcept
title: FISMA
aliases: [Federal Information Security Modernization Act, Federal Information Security Management Act, FISMA 2014, FISMA 2002, Federal Information Security Modernization Act of 2014]
domain: public-sector-and-compliance
summary: >-
  The US law (2002, amended 2014) requiring every federal agency to run a risk-based information security program,
  authorize its systems, and report annually; it is the statutory root of NIST's security standards and of FedRAMP,
  which together decide how agencies may use Salesforce government clouds.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:authority-to-operate, kt:continuous-monitoring, kt:nist-cybersecurity-framework, kt:government-cloud-plus]
relations:
  - {predicate: enables, object: kt:nist-risk-management-framework}
  - {predicate: enables, object: kt:fedramp}
  - {predicate: dependsOn, object: kt:nist-sp-800-53}
  - {predicate: contrastsWith, object: kt:fedramp-high}
sources:
  - id: s1
    title: "Federal Information Security Modernization Act"
    publisher: Cybersecurity and Infrastructure Security Agency (CISA)
    url: https://www.cisa.gov/federal-information-security-modernization-act
    type: government
    accessed: 2026-11-10
  - id: s2
    title: "FISMA Background — Risk Management Framework"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/projects/risk-management/fisma-background
    type: standards-body
    accessed: 2026-11-10
  - id: s3
    title: "Federal Risk and Authorization Management Program (FedRAMP)"
    publisher: CMS Information Security and Privacy Program
    url: https://security.cms.gov/learn/fedramp
    type: government
    accessed: 2026-11-10
  - id: s4
    title: "FY 2025 Inspector General FISMA Reporting Metrics, Version 2.0"
    publisher: CISA / OMB / CIGIE
    url: https://cisa.gov/sites/default/files/2025-04/Final%20FY%202025%20IG%20FISMA%20Reporting%20Metrics_Ver%202.0_April%202025-508_0.pdf
    type: government
    accessed: 2026-11-10
  - id: s5
    title: "FedRAMP Moderate — Salesforce Compliance"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/fedramp-moderate
    type: official-docs
    accessed: 2026-11-10
  - id: s6
    title: "FedRAMP High — Salesforce Compliance"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/fedramp-high
    type: official-docs
    accessed: 2026-11-10
created: 2026-11-10
---

# FISMA

FISMA is the US federal law that makes every executive-branch agency responsible for securing its own information and systems. The original Federal Information Security Management Act was passed in December 2002 as part of the E-Government Act (Public Law 107-347), and it requires each agency to build, document and run an agency-wide security program, including for systems that contractors or other organizations provide or operate on its behalf.[^s2] The Federal Information Security Modernization Act of 2014 amended that law, keeping the acronym.[^s1] For Salesforce practitioners FISMA is rarely cited by name in a statement of work, but it is the reason the agency asks for an authorization package, a FedRAMP-authorized environment and continuous monitoring evidence.

## What the law requires of agencies

Agencies must give their information protection proportionate to the risk and harm of unauthorized access, use, disclosure, disruption, modification or destruction, and must follow federal security standards, including the mandatory ones NIST develops.[^s2] Through OMB Circular A-130 they must also plan for security, assign responsibility, review system controls periodically, and authorize each system before it goes into operation and again over time.[^s2] That authorization is the agency Authority to Operate, and the "agency-wide" scope is why a SaaS org holding agency data falls inside an agency's FISMA program rather than outside it.[^s2]

## The 2014 modernization

The 2014 act reshaped who does what. It codified the Department of Homeland Security's authority to administer security policy for non-national-security federal systems, and clarified and expanded OMB's oversight of agency practices.[^s1] DHS may issue binding operational directives consistent with OMB policy, provides technical help to civilian agencies on request, and houses the federal incident center.[^s1] The act also required agencies to report major incidents and breaches to Congress as they happen and annually, while directing OMB to rewrite Circular A-130 to remove wasteful reporting.[^s1] NIST describes the overall shift as less paperwork, stronger continuous monitoring, and compliance focused on issues that incidents actually expose.[^s2]

## NIST's role and the standards behind it

FISMA assigns NIST the job of writing security standards and guidance for non-national-security systems.[^s2] The resulting toolkit is the Risk Management Framework, a seven-step process (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor) described in SP 800-37 Rev. 2, backed by SP 800-53 Rev. 5 for controls, SP 800-53A for assessing them and SP 800-53B for baselines.[^s2] Since 2009 a Joint Task Force with DoD, ODNI and CNSS has worked to make this one framework across civilian and national security systems.[^s2]

## Annual evaluation

FISMA requires an annual independent evaluation of each agency's security program by its Inspector General, or an independent external auditor.[^s4] For FY 2025, OMB and CIGIE built the IG metrics around NIST CSF 2.0 functions, scoring domains such as supply chain risk, identity and access management, continuous monitoring and incident response on a five-level maturity scale.[^s4] OMB treats Level 4, Managed and Measurable, or higher as effective, though IGs may judge otherwise based on the agency's risk profile.[^s4]

## How it shapes Salesforce deals

FedRAMP applies FISMA to cloud services. Salesforce's own compliance pages describe the FedRAMP requirements as established in accordance with FISMA, and present reuse of assessments across agencies as the program's point.[^s5] The two are not the same thing, and the differences matter in practice:

- FISMA covers every agency system and technology; FedRAMP covers only cloud service offerings, adding cloud-specific controls to the same SP 800-53 catalog.[^s3]
- A FISMA authorization is agency-specific and need not use a third-party assessor; a FedRAMP authorization requires a 3PAO and can be reused by many agencies.[^s3]
- A FISMA boundary can contain several cloud offerings, while a FedRAMP boundary covers only the one offering.[^s3]
- A FedRAMP authorization at the same or lower impact level is presumed adequate, but it does not replace the CIO's FISMA duty to assess the agency's own needs.[^s3]

So an agency still reviews the controls that remain its responsibility in a Salesforce org, using the provider's customer responsibility matrix, and documents them in its own ATO.[^s3] For high-impact data, Salesforce Government Cloud Plus holds a JAB provisional authorization at the high level, issued in May 2020.[^s6]

## Connections

FISMA sits under security compliance frameworks (`kt:security-compliance-frameworks`) as the statute the others implement.[^s2] It `enables` the NIST Risk Management Framework (`kt:nist-risk-management-framework`) and `dependsOn` the SP 800-53 control catalog (`kt:nist-sp-800-53`).[^s2] It also `enables` FedRAMP (`kt:fedramp`), and `contrastsWith` FedRAMP High (`kt:fedramp-high`): agency-specific authorization versus a reusable cloud baseline.[^s3] Related nodes are the Authority to Operate (`kt:authority-to-operate`) and continuous monitoring (`kt:continuous-monitoring`) the law requires, the NIST CSF (`kt:nist-cybersecurity-framework`) that frames the IG metrics,[^s4] and Government Cloud Plus (`kt:government-cloud-plus`).[^s6]

## Sources
[^s1]: CISA, "Federal Information Security Modernization Act". https://www.cisa.gov/federal-information-security-modernization-act (accessed 2026-11-10)
[^s2]: NIST CSRC, "FISMA Background". https://csrc.nist.gov/projects/risk-management/fisma-background (accessed 2026-11-10)
[^s3]: CMS, "Federal Risk and Authorization Management Program (FedRAMP)". https://security.cms.gov/learn/fedramp (accessed 2026-11-10)
[^s4]: CISA/OMB/CIGIE, "FY 2025 Inspector General FISMA Reporting Metrics, Version 2.0". https://cisa.gov/sites/default/files/2025-04/Final%20FY%202025%20IG%20FISMA%20Reporting%20Metrics_Ver%202.0_April%202025-508_0.pdf (accessed 2026-11-10)
[^s5]: Salesforce, "FedRAMP Moderate — Salesforce Compliance". https://compliance.salesforce.com/en/fedramp-moderate (accessed 2026-11-10)
[^s6]: Salesforce, "FedRAMP High — Salesforce Compliance". https://compliance.salesforce.com/en/fedramp-high (accessed 2026-11-10)
