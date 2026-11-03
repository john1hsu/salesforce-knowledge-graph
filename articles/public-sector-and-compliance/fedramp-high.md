---
id: kt:fedramp-high
type: ExternalConcept
title: FedRAMP High
aliases: [FedRAMP High baseline, FedRAMP High impact level, FedRAMP Class D, Class D certification]
domain: public-sector-and-compliance
summary: >-
  The most stringent FedRAMP security baseline, for unclassified federal data whose compromise could have a severe
  or catastrophic effect; built on the NIST SP 800-53 high baseline plus FedRAMP additions, relabelled Class D in
  2026, and the level at which Salesforce Government Cloud Plus is authorized.
release: "Winter '27"
status: concept
broader: [kt:fedramp]
related: [kt:government-cloud-plus, kt:il4-and-il5, kt:public-sector-solutions]
relations:
  - {predicate: dependsOn, object: kt:fips-199}
  - {predicate: dependsOn, object: kt:nist-sp-800-53}
  - {predicate: contrastsWith, object: kt:dod-cloud-computing-srg}
sources:
  - id: s1
    title: "Understanding Baselines and Impact Levels for FedRAMP Authorizations"
    publisher: FedRAMP (GSA)
    url: https://www.fedramp.gov/rev5/baselines
    type: government
    accessed: 2026-11-03
  - id: s2
    title: "Control Baselines for Information Systems and Organizations: NIST Publishes SP 800-53B"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/news/2020/control-baselines-nist-publishes-sp-800-53b
    type: standards-body
    accessed: 2026-11-03
  - id: s3
    title: "FedRAMP Publishes Draft Rev. 5 Baselines (archived, December 2021)"
    publisher: FedRAMP (GSA)
    url: https://www.fedramp.gov/archive/2021-12-21-FedRAMP-Publishes-Draft-Rev-5-Baselines
    type: government
    accessed: 2026-11-03
  - id: s4
    title: "RFC-0033: 20x Phase 4 Development Tracks for 20x Class D"
    publisher: FedRAMP (GSA)
    url: https://www.fedramp.gov/rfcs/0033/
    type: government
    accessed: 2026-11-03
  - id: s5
    title: "FedRAMP - Salesforce Government Cloud Plus (High)"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/documents/a005A00000t4NpRQAU
    type: official-docs
    accessed: 2026-11-03
  - id: s6
    title: "Salesforce Government Cloud"
    publisher: Salesforce
    url: https://www.salesforce.com/government/cloud/
    type: official-blog
    accessed: 2026-11-03
created: 2026-11-03
---

# FedRAMP High

FedRAMP High is the top baseline of the US federal cloud authorization program. FedRAMP introduced it for the government's most sensitive unclassified data, where losing confidentiality, integrity or availability could have a severe or catastrophic effect on agency operations, assets or individuals, including risks to life and of financial ruin. FedRAMP's own examples are law enforcement and emergency services systems, financial systems and health systems.[^s1] In the program's 2026 vocabulary the same baseline is called **Class D**, and Salesforce now describes Government Cloud Plus as FedRAMP Class D.[^s6]

## Where the requirements come from

The baseline is a control selection, not a separate standard. NIST SP 800-53B, published in October 2020, defines low, moderate and high security control baselines keyed to a system's impact level, plus a separate privacy baseline.[^s2] FedRAMP layers its own additions on top: when it released the draft Rev. 5 baselines in December 2021, it added 22 controls above the NIST high baseline (versus 17 for Moderate and 1 for Low), and it scored every High control against MITRE ATT&CK techniques to choose them on a threat basis.[^s3] Salesforce's explainer puts the High total at more than 420 controls and calls out physically separated network components, continuous threat hunting, supply chain risk management and fail-safe availability as distinguishing requirements.[^s6]

## How a system lands at High

Categorization follows FIPS 199, documented in FedRAMP's categorization template in the System Security Plan with NIST SP 800-60 as the guide to information types. FedRAMP does not let providers tailor by security objective: if any single objective (say, integrity) is High, the whole offering must meet High.[^s1] High offerings could be authorized through either the Agency path or the Joint Authorization Board path.[^s1] Each customer agency must still run its own FIPS 199 analysis of the data it places in the provider's environment.[^s1]

## Class D and FedRAMP 20x

Under the 20x modernization, FedRAMP's RFC-0033 sets out a Class D pilot for cloud-hosted services that it says will be significantly more robust than 20x Class C or Rev5 Class D. Proposed entry conditions include six months of Class C certification without corrective action, running on a Class D certified IaaS/PaaS, and new key security indicators covering assurance engineering, automation, availability and foreign ownership, control or influence. The pilot is capped at 10 participants for FY27 Q1-Q2, with final pilot requirements due November 18, 2026 and an application window of December 1-4, 2026.[^s4] Pilot participants must first hold a Class C certification compliant with the 2026 Consolidated Rules (CR26) by December 1, 2026, and submit a final package by March 17, 2027.[^s4]

## FedRAMP High in Salesforce

Salesforce's compliance portal lists a FedRAMP High security package for Government Cloud Plus, FedRAMP ID FR2003061248, covering SaaS and PaaS in a Government Community Cloud deployment model; it applies only to the environment branded and sold as Government Cloud Plus.[^s5] Federal agencies request the package through the FedRAMP PMO from a .gov or .mil address, while state, local and partner organizations go through their Salesforce account executive.[^s5] Salesforce says Government Cloud Plus runs on AWS GovCloud (US) and holds a JAB provisional ATO at Class D.[^s6]

Practitioner gotchas:

- **High is a ceiling for the boundary, not a property of your org's add-ons.** Salesforce notes that AppExchange apps sit outside the authorization boundary, even native ones.[^s6]
- **High is not a DoD Impact Level.** Salesforce lists Government Cloud Plus as Class D plus IL2; IL4 and IL5 workloads need Government Cloud Plus - Defense.[^s6]
- **Ask for the package, not just the badge.** Agencies reviewing a High authorization should obtain the security package itself through the documented access process.[^s5]

## Connections

FedRAMP High is the strictest baseline of `kt:fedramp` (broader).[^s1] It `dependsOn` FIPS 199 categorization (`kt:fips-199`) and on the NIST SP 800-53 control catalog and its 800-53B baselines (`kt:nist-sp-800-53`).[^s1][^s2] Government Cloud Plus (`kt:government-cloud-plus`) is the Salesforce environment authorized at this level, and Public Sector Solutions (`kt:public-sector-solutions`) is among the products Salesforce says are authorized for government use.[^s5][^s6] It `contrastsWith` DISA's Cloud Computing SRG (`kt:dod-cloud-computing-srg`), whose Impact Levels 4 and 5 (`kt:il4-and-il5`) govern defense data and are served by a separate Defense environment.[^s6]

## Sources

[^s1]: FedRAMP (GSA), "Understanding Baselines and Impact Levels for FedRAMP Authorizations". https://www.fedramp.gov/rev5/baselines (accessed 2026-11-03)
[^s2]: NIST CSRC, "Control Baselines for Information Systems and Organizations: NIST Publishes SP 800-53B". https://csrc.nist.gov/news/2020/control-baselines-nist-publishes-sp-800-53b (accessed 2026-11-03)
[^s3]: FedRAMP (GSA), "FedRAMP Publishes Draft Rev. 5 Baselines". https://www.fedramp.gov/archive/2021-12-21-FedRAMP-Publishes-Draft-Rev-5-Baselines (accessed 2026-11-03)
[^s4]: FedRAMP (GSA), "RFC-0033: 20x Phase 4 Development Tracks for 20x Class D". https://www.fedramp.gov/rfcs/0033/ (accessed 2026-11-03)
[^s5]: Salesforce, "FedRAMP - Salesforce Government Cloud Plus (High)". https://compliance.salesforce.com/en/documents/a005A00000t4NpRQAU (accessed 2026-11-03)
[^s6]: Salesforce, "Salesforce Government Cloud". https://www.salesforce.com/government/cloud/ (accessed 2026-11-03)
