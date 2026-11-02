---
id: kt:fedramp
type: ExternalConcept
title: FedRAMP
aliases: [Federal Risk and Authorization Management Program, FedRAMP Certification, FedRAMP authorization]
domain: public-sector-and-compliance
summary: >-
  The US federal government's program, run by GSA, for assessing and certifying the security of cloud services
  used by federal agencies; offerings are categorized into baselines (Low, Moderate, High, now relabelled Classes
  A-D), and Salesforce's Government Cloud Plus holds the top (High / Class D) authorization.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:government-cloud-plus, kt:public-sector-solutions, kt:il4-and-il5, kt:data-residency]
relations:
  - {predicate: hasPart, object: kt:fedramp-high}
  - {predicate: dependsOn, object: kt:fips-199}
  - {predicate: contrastsWith, object: kt:dod-cloud-computing-srg}
sources:
  - id: s1
    title: "Understanding Baselines and Impact Levels for FedRAMP Authorizations"
    publisher: FedRAMP (GSA)
    url: https://www.fedramp.gov/rev5/baselines
    type: government
    accessed: 2026-11-02
  - id: s2
    title: "FedRAMP Authorization Act"
    publisher: FedRAMP (GSA)
    url: https://fedramp.gov/2026/authority/law/
    type: government
    accessed: 2026-11-02
  - id: s3
    title: "Notice NTC-0004: Initial Outcome from RFC-0020"
    publisher: FedRAMP (GSA)
    url: https://www.fedramp.gov/notices/0004
    type: government
    accessed: 2026-11-02
  - id: s4
    title: "FedRAMP Certification Paths Are Heating Up (July 30, 2026)"
    publisher: FedRAMP (GSA)
    url: https://www.fedramp.gov/2026-07-30-fedramp-certification-paths-are-heating-up/
    type: government
    accessed: 2026-11-02
  - id: s5
    title: "FedRAMP High (Compliance category page)"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/categories/fedramp-high
    type: official-docs
    accessed: 2026-11-02
  - id: s6
    title: "Salesforce FedRAMP (Government Cloud page)"
    publisher: Salesforce
    url: https://www.salesforce.com/fedramp/
    type: official-blog
    accessed: 2026-11-02
created: 2026-11-02
---

# FedRAMP

FedRAMP is the US government's program for assessing and certifying cloud service offerings (CSOs) that federal agencies use. Although an earlier version dated from a 2011 federal CIO memo, the current program rests on the FedRAMP Authorization Act, enacted on December 23, 2022 as Section 5921 of the FY2023 National Defense Authorization Act (Public Law 117-263). The Act added sections 3607–3616 to Title 44 of the US Code, placing the program within the General Services Administration (GSA), creating a FedRAMP Board, and assigning roles to agencies and OMB.[^s2] OMB Memorandum M-24-15 of July 25, 2024 rescinded the 2011 memo and, in FedRAMP's own description, effectively created a new program under the same name.[^s2]

## How categorization works

A cloud offering is categorized under FIPS 199 by the potential impact of a compromise to confidentiality, integrity and availability, using FedRAMP's categorization template in the System Security Plan alongside NIST SP 800-60. Agencies must still categorize the data they themselves place in a provider's environment.[^s1] The baselines are:[^s1]

- **Low**, including the Tailored **LI-SaaS** baseline for low-impact SaaS that holds no personal data beyond login details, with fewer tested controls.[^s1]
- **Moderate**, where loss would cause serious adverse effects; FedRAMP notes most authorized offerings sit here.[^s1]
- **High**, for severe or catastrophic impact, typical of law enforcement, emergency services, financial and health systems.[^s1]

Baselines can't be tailored per security objective: if one of confidentiality, integrity or availability is High, the whole system must meet High.[^s1] Historically there were two routes, an Agency path open to every baseline and a Joint Authorization Board (JAB) path limited to Moderate and High.[^s1]

## Certification classes and FedRAMP 20x

FedRAMP is mid-transition. Notice NTC-0004 (February 2026) made "FedRAMP Certification" the single official label and relabelled the Rev5 baselines as classes, deliberately avoiding "levels" so they aren't confused with DoD Impact Levels: Class A is a new pilot baseline, Class B covers LI-SaaS and Low, Class C is Moderate and Class D is High. The notice says the relabelling leaves the requirements, purpose and use of an authorization unchanged, and that the Consolidated Rules for 2026 (CR26) remain valid through December 31, 2028.[^s3] Under the parallel 20x path, intake for Class A opened on August 3, 2026 and for Classes B and C on August 31, 2026, while Class D was slated for an early-adopter pilot in late 2026 before becoming a formal option in early 2027; "FedRAMP Ready" became a legacy Marketplace status.[^s4]

## FedRAMP in the Salesforce ecosystem

Salesforce's compliance portal lists two offerings in its FedRAMP High category: Salesforce Government Cloud Plus and GovSlack, both hosted on AWS. It records that Government Cloud Plus received a JAB provisional Authority to Operate at the High level in May 2020.[^s5] Salesforce's own FedRAMP page already uses the new vocabulary, describing Government Cloud Plus as FedRAMP Class D (formerly High). It states that Public Sector Solutions is authorized to meet FedRAMP and DoD Impact Levels, and points to a help article for the full list of in-scope products.[^s6]

Practitioner gotchas:

- **Authorization is per offering and per boundary, not per vendor.** A FedRAMP-certified Salesforce environment does not certify everything you add to it. Salesforce warns that AppExchange (AgentExchange) apps generally fall outside the authorization boundary, even when they are built natively on the platform.[^s6][^s6]
- **Check the specific product list.** Commercial-cloud features, including some AI and extension products, may be missing from the government boundary or reach it later.[^s6]
- **The agency still owns its decision.** The provider's categorization does not replace the agency's own FIPS 199 analysis of its data.[^s1]
- **Mind the vocabulary shift.** Older documents say "Moderate" and "High"; newer FedRAMP and Salesforce material says "Class C" and "Class D" for the same baselines.[^s3][^s6]

## Connections

FedRAMP `hasPart` its High baseline (`kt:fedramp-high`), which Government Cloud Plus (`kt:government-cloud-plus`, related) implements.[^s5][^s6] It `dependsOn` FIPS 199 categorization (`kt:fips-199`).[^s1] It `contrastsWith` DISA's cloud SRG (`kt:dod-cloud-computing-srg`), whose Impact Levels (`kt:il4-and-il5`, related) build on FedRAMP for defense workloads; FedRAMP chose class letters partly to avoid confusion with them.[^s3][^s6] Public Sector Solutions (`kt:public-sector-solutions`) is among the Salesforce products authorized inside the boundary.[^s6] Data residency (`kt:data-residency`) is a related concern for agencies choosing a government cloud.[^s6]

## Sources

[^s1]: FedRAMP (GSA), "Understanding Baselines and Impact Levels for FedRAMP Authorizations". https://www.fedramp.gov/rev5/baselines (accessed 2026-11-02)
[^s2]: FedRAMP (GSA), "FedRAMP Authorization Act". https://fedramp.gov/2026/authority/law/ (accessed 2026-11-02)
[^s3]: FedRAMP (GSA), "Notice NTC-0004: Initial Outcome from RFC-0020". https://www.fedramp.gov/notices/0004 (accessed 2026-11-02)
[^s4]: FedRAMP (GSA), "FedRAMP Certification Paths Are Heating Up". https://www.fedramp.gov/2026-07-30-fedramp-certification-paths-are-heating-up/ (accessed 2026-11-02)
[^s5]: Salesforce, "FedRAMP High" compliance category. https://compliance.salesforce.com/en/categories/fedramp-high (accessed 2026-11-02)
[^s6]: Salesforce, "Salesforce FedRAMP". https://www.salesforce.com/fedramp/ (accessed 2026-11-02)
