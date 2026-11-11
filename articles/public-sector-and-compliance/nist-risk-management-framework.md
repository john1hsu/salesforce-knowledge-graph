---
id: kt:nist-risk-management-framework
type: ExternalConcept
title: NIST Risk Management Framework
aliases: [NIST RMF, RMF, NIST SP 800-37, SP 800-37 Rev. 2, RMF 2.0, "Risk Management Framework for Information Systems and Organizations"]
domain: public-sector-and-compliance
summary: >-
  The seven-step process (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor) defined in NIST SP 800-37
  Rev. 2 that US federal agencies use to manage security and privacy risk across a system's life cycle; FedRAMP applies
  it to cloud services, and agency authorizations of Salesforce Government Cloud Plus follow it.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:fedramp, kt:government-cloud-plus, kt:shared-responsibility-model, kt:fips-200]
relations:
  - {predicate: hasPart, object: kt:continuous-monitoring}
  - {predicate: enables, object: kt:authority-to-operate}
  - {predicate: dependsOn, object: kt:nist-sp-800-53}
  - {predicate: dependsOn, object: kt:fips-199}
  - {predicate: consumedBy, object: kt:fisma}
  - {predicate: contrastsWith, object: kt:nist-cybersecurity-framework}
sources:
  - id: s1
    title: "SP 800-37 Rev. 2, Risk Management Framework for Information Systems and Organizations: A System Life Cycle Approach for Security and Privacy"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/pubs/sp/800/37/r2/final
    type: standards-body
    accessed: 2026-11-11
  - id: s2
    title: "RMF Update: NIST Publishes SP 800-37 Rev. 2"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/news/2018/rmf-update-nist-publishes-sp-800-37-rev-2
    type: standards-body
    accessed: 2026-11-11
  - id: s3
    title: "ITL Bulletin, February 2019: Risk Management Framework for Information Systems and Organizations (RMF 2.0)"
    publisher: NIST Information Technology Laboratory
    url: https://csrc.nist.gov/files/pubs/shared/itlb/itlbul2019-02.pdf
    type: standards-body
    accessed: 2026-11-11
  - id: s4
    title: "NIST SP 800-37 Rev. 2 (full text PDF)"
    publisher: NIST
    url: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-37r2.pdf
    type: standards-body
    accessed: 2026-11-11
  - id: s5
    title: "Cloud Security"
    publisher: GSA Cloud Information Center
    url: https://cic.gsa.gov/basics/cloud-security
    type: government
    accessed: 2026-11-11
  - id: s6
    title: "FedRAMP - Salesforce Government Cloud Plus (High)"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/documents/a005A00000t4NpRQAU
    type: official-docs
    accessed: 2026-11-11
created: 2026-11-11
---

# NIST Risk Management Framework

The **NIST Risk Management Framework (RMF)** is the US federal government's structured process for managing the security and privacy risk of information systems. It is defined in NIST Special Publication 800-37 Revision 2, published by the Joint Task Force on 20 December 2018, which superseded Revision 1 from 2014.[^s1] NIST describes the RMF as a disciplined, structured and flexible process that covers categorization, control selection, implementation and assessment, authorization, and continuous monitoring, building security and privacy into the system development life cycle.[^s1] For a Salesforce architect working in the public sector, the RMF is the process behind every agency Authority to Operate (ATO) and behind FedRAMP's cloud authorizations.[^s5]

## The seven steps

Revision 2 organizes the framework into seven steps. Only the first is new; the other six carried over from Revision 1.[^s3]

1. **Prepare** sets the organizational context and priorities for managing security and privacy risk.[^s3]
2. **Categorize** classifies the system and its information by the impact of a loss of confidentiality, integrity or availability.[^s3]
3. **Select** picks an initial set of controls and tailors them to bring risk to an acceptable level.[^s3]
4. **Implement** puts the controls in place and documents how they are deployed in the system and its environment.[^s3]
5. **Assess** checks whether controls are implemented correctly, operate as intended and meet requirements.[^s3]
6. **Authorize** has a senior official accept the remaining risk and approve the system or its common controls.[^s3]
7. **Monitor** tracks control effectiveness, changes and risk on an ongoing basis and reports the security and privacy posture.[^s3]

The Prepare step pulls together guidance previously scattered across several NIST publications (including SP 800-30, 800-39 and 800-160) so that common controls and organization-tailored baselines are identified before system work starts.[^s3]

## What Revision 2 changed

NIST's announcement lists seven objectives for the update: connect senior leadership with system-level risk decisions, strengthen preparatory activities, show how the NIST Cybersecurity Framework can be implemented through the RMF, integrate privacy risk management, align with the systems-engineering processes of SP 800-160, incorporate supply chain risk management, and allow organization-generated control selection alongside baseline selection to support the consolidated catalog in SP 800-53 Rev. 5.[^s2] The ITL bulletin calls RMF 2.0 the first NIST publication to fully integrate privacy risk management into the existing security risk process.[^s3]

## Levels, roles and authorization decisions

The RMF operates across three levels: the organization, the mission or business process, and the individual information system.[^s4] The **authorizing official** issues authorization decisions; a senior accountable official for risk management (or risk executive function) links organization-level and system-level risk.[^s4] Decisions include an authorization to operate or to use for a single system, and a **common control authorization** for controls that many systems inherit.[^s4] Authorization is not meant to be a one-time event: the RMF promotes near real-time risk management and ongoing authorization through continuous monitoring.[^s1][^s4]

## How it applies to Salesforce

Cloud services do not get a separate framework. GSA's Cloud Information Center points agencies to SP 800-37 Rev. 2 for applying the RMF, to SP 800-53 Rev. 5 for the low, moderate and high control baselines, and to FedRAMP as the standardized, reuse-once-authorized approach to assessing and authorizing cloud products.[^s5] Agencies remain accountable under FISMA for systems they run in the cloud, can inherit controls from the cloud provider under a shared responsibility model, and must keep the service operating within the parameters of their ATO.[^s5]

In practice, an agency building on Salesforce Government Cloud Plus runs its own RMF cycle for its app while inheriting the provider's FedRAMP package. Salesforce lists that package for Government Cloud Plus on Hyperforce, covering SaaS and PaaS in a government community cloud deployment model; federal agencies request access to it through FedRAMP's package-access process.[^s6] The customer's Select, Implement and Assess work then concentrates on the controls it does not inherit from the provider.[^s5]

## Connections

The RMF sits under security compliance frameworks (`kt:security-compliance-frameworks`).[^s1] It `hasPart` continuous monitoring (`kt:continuous-monitoring`), its Monitor step, and `enables` the Authority to Operate (`kt:authority-to-operate`) issued in its Authorize step.[^s4] It `dependsOn` FIPS 199 (`kt:fips-199`) for categorization and on the SP 800-53 catalog (`kt:nist-sp-800-53`) for control selection.[^s5] FIPS 200 (`kt:fips-200`) is a related federal standard in the same chain. It is `consumedBy` FISMA (`kt:fisma`), the statute listed among its governing authorities, and `contrastsWith` the NIST Cybersecurity Framework (`kt:nist-cybersecurity-framework`), which Revision 2 maps to rather than replaces.[^s1][^s2] FedRAMP (`kt:fedramp`), Government Cloud Plus (`kt:government-cloud-plus`) and the shared responsibility model (`kt:shared-responsibility-model`) are how the framework reaches Salesforce deployments.[^s5][^s6]

## Sources

[^s1]: NIST CSRC, "SP 800-37 Rev. 2, Risk Management Framework for Information Systems and Organizations". https://csrc.nist.gov/pubs/sp/800/37/r2/final (accessed 2026-11-11)
[^s2]: NIST CSRC, "RMF Update: NIST Publishes SP 800-37 Rev. 2" (December 2018). https://csrc.nist.gov/news/2018/rmf-update-nist-publishes-sp-800-37-rev-2 (accessed 2026-11-11)
[^s3]: NIST ITL, "ITL Bulletin, February 2019: RMF 2.0". https://csrc.nist.gov/files/pubs/shared/itlb/itlbul2019-02.pdf (accessed 2026-11-11)
[^s4]: NIST, "SP 800-37 Rev. 2" (PDF). https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-37r2.pdf (accessed 2026-11-11)
[^s5]: GSA Cloud Information Center, "Cloud Security". https://cic.gsa.gov/basics/cloud-security (accessed 2026-11-11)
[^s6]: Salesforce Compliance, "FedRAMP - Salesforce Government Cloud Plus (High)". https://compliance.salesforce.com/en/documents/a005A00000t4NpRQAU (accessed 2026-11-11)
