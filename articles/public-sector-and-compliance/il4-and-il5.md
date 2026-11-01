---
id: kt:il4-and-il5
type: ExternalConcept
title: DoD Impact Levels 4 and 5
aliases: [IL4 and IL5, DoD IL4, DoD IL5, Impact Level 4, Impact Level 5]
domain: public-sector-and-compliance
summary: >-
  The two US Department of Defense cloud security tiers for Controlled Unclassified Information (IL4) and for CUI
  plus unclassified National Security Systems data (IL5), defined in DISA's Cloud Service Provider SRG; in the
  Salesforce ecosystem IL5 workloads run in Government Cloud Plus - Defense.
release: "Winter '27"
status: concept
broader: [kt:fedramp]
related: [kt:government-cloud-plus, kt:agentforce, kt:multi-factor-authentication, kt:data-residency]
relations:
  - {predicate: partOf, object: kt:dod-cloud-computing-srg}
  - {predicate: dependsOn, object: kt:fedramp-high}
sources:
  - id: s1
    title: "Cloud Service Provider Security Requirements Guide, Version 1, Release 2 (30 January 2025)"
    publisher: Defense Information Systems Agency (copy hosted by RMF.org)
    url: https://rmf.org/wp-content/uploads/2025/05/DoD-Cloud-Service-Provider-SRG-Jan-2025.pdf
    type: government
    accessed: 2026-11-01
  - id: s2
    title: "Government Cloud Plus - Defense (Compliance services page)"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/services/salesforce-government-cloud-plus-defense
    type: official-docs
    accessed: 2026-11-01
  - id: s3
    title: "Government Cloud (product and pricing page)"
    publisher: Salesforce
    url: https://www.salesforce.com/government/cloud/
    type: official-blog
    accessed: 2026-11-01
  - id: s4
    title: "Public sector Government Cloud news (April 18, 2023)"
    publisher: Salesforce
    url: https://www.salesforce.com/uk/news/stories/public-sector-government-cloud-news/
    type: news
    accessed: 2026-11-01
  - id: s5
    title: "Salesforce's Agentforce 360 authorized at DOD Impact Level 5"
    publisher: DefenseScoop
    url: https://defensescoop.com/?p=130372
    type: news
    accessed: 2026-11-01
created: 2026-11-01
---

# DoD Impact Levels 4 and 5

Impact Levels (ILs) are the US Department of Defense's way of grading how sensitive the data in a commercial cloud service is, and therefore which security controls the service must meet before DoD components may use it. The levels are defined by the Defense Information Systems Agency (DISA) in its Cloud Service Provider Security Requirements Guide (SRG), most recently issued as Version 1, Release 2 on 30 January 2025.[^s1] For Salesforce architects in the defense space, IL4 and IL5 are the two tiers that matter most, because they cover the Controlled Unclassified Information (CUI) that most DoD business systems handle.[^s1][^s3]

## What each level covers

- **IL2** is the baseline for non-controlled unclassified data, built on the FedRAMP Moderate baseline and reachable over the internet.[^s1]
- **IL4** covers CUI and mission data. It starts from FedRAMP Moderate and adds DoD "FedRAMP+" controls and CNSSI 1253 overlays, accommodating information categorized up to moderate confidentiality and integrity.[^s1]
- **IL5** covers CUI that needs more protection plus unclassified National Security Systems (NSS) data. It is built on the FedRAMP High baseline and accommodates high confidentiality, integrity and availability categorizations.[^s1]
- **IL6** (classified up to SECRET) sits above them and requires SIPRNet or approved CNSSP-11 access.[^s1]

## Separation, location and connectivity

The practical difference between IL4 and IL5 is tenancy. At IL4 a provider may share hardware with other customers if it demonstrates strong virtual separation through encryption and access control, and it must monitor for cross-tenant access attempts.[^s1] At IL5 only the federal government community is eligible: logical separation between DoD and other federal tenants is acceptable, but physical separation from non-DoD and non-federal tenants such as state and local governments or the public is required.[^s1] The SRG also requires DoD data to sit under US jurisdiction, generally in the 50 states, DC and outlying US areas unless the authorizing official approves otherwise.[^s1] IL4 and IL5 workloads used by NIPRNet-connected DoD components reach the cloud through DoD CIO-approved boundaries such as a Boundary Cloud Access Point (BCAP) rather than the open internet.[^s1]

## Provisional authorization vs. ATO

DISA issues a Provisional Authorization (PA) to a specific cloud service offering, not to a vendor as a whole; it records an evaluated level of risk. The PA is a pre-approval only: each mission owner's authorizing official still issues its own Authority to Operate after assessing risk to its systems.[^s1] A Salesforce org therefore inherits controls from the authorized boundary but does not become authorized by itself.

## How it applies to Salesforce

In April 2023 Salesforce announced that Government Cloud Plus - Defense had received a DISA IL5 provisional authorization, while Government Cloud Plus already held FedRAMP High and IL4.[^s4] Salesforce now describes the Defense environment as a dedicated, physically isolated instance of its PaaS and SaaS infrastructure for DoD and its contractors to store and process IL5 data, including CUI and unclassified NSS data, with its IL5 documentation tagged Hyperforce.[^s2] Its product page lists IL4 and IL5 support for the Defense edition and adds operational requirements that shape any design: Common Access Card as the MFA factor, salesforce.mil domains, connection via the DISA BCAP from a NIPRNet IP range, and EEMSG for email security.[^s3] Eligibility is narrow: contractors may buy it only to directly support a DoD mission owner with IL4 or IL5 data, not for their own internal use.[^s3]

In August 2026 DefenseScoop reported that DoD had authorized Salesforce's Agentforce 360 platform at IL5, running on AWS GovCloud, with Army Human Resources Command as the first DoD customer.[^s5]

## Gotchas

- **Pick the level from the data, not the customer.** A DoD customer with only IL2 data does not need the Defense edition; CUI and NSS data drive the choice.[^s1][^s3]
- **Network and identity constraints are architectural.** BCAP-only connectivity and CAC-based login affect integrations, mobile access and external users, so validate them early.[^s3]
- **Check each feature's boundary.** A platform authorization does not guarantee every product or AI capability is available inside it; reported conditions for the Agentforce IL5 approval included constraints on which AI models could be enabled.[^s5]

## Connections

IL4 and IL5 are `partOf` DISA's cloud SRG (`kt:dod-cloud-computing-srg`) and extend FedRAMP (`kt:fedramp`, broader); IL5 `dependsOn` the FedRAMP High baseline (`kt:fedramp-high`).[^s1] The levels are what Government Cloud Plus (`kt:government-cloud-plus`, related) implements for DoD customers: its Defense variant carries the IL5 authorization.[^s2][^s4] Related nodes include Agentforce (`kt:agentforce`), now reported as IL5-authorized; multi-factor authentication (`kt:multi-factor-authentication`), satisfied by CAC in the Defense edition; and data residency (`kt:data-residency`), since the SRG mandates US jurisdiction for DoD data.[^s1][^s3][^s5]

## Sources

[^s1]: Defense Information Systems Agency, "Cloud Service Provider Security Requirements Guide, Version 1, Release 2" (30 January 2025). https://rmf.org/wp-content/uploads/2025/05/DoD-Cloud-Service-Provider-SRG-Jan-2025.pdf (accessed 2026-11-01)
[^s2]: Salesforce, "Government Cloud Plus - Defense" compliance services page. https://compliance.salesforce.com/en/services/salesforce-government-cloud-plus-defense (accessed 2026-11-01)
[^s3]: Salesforce, "Government Cloud" product and pricing page. https://www.salesforce.com/government/cloud/ (accessed 2026-11-01)
[^s4]: Salesforce, public sector Government Cloud news (April 18, 2023). https://www.salesforce.com/uk/news/stories/public-sector-government-cloud-news/ (accessed 2026-11-01)
[^s5]: DefenseScoop, report on Agentforce 360 DoD IL5 authorization (August 5, 2026). https://defensescoop.com/?p=130372 (accessed 2026-11-01)
