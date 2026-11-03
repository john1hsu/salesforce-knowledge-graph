---
id: kt:dod-cloud-computing-srg
type: ExternalConcept
title: DoD Cloud Computing Security Requirements Guide
aliases: [DoD Cloud Computing SRG, CC SRG, Cloud Service Provider SRG, CSP SRG, DoD cloud SRG, Cloud Computing Mission Owner SRG]
domain: public-sector-and-compliance
summary: >-
  DISA's guidance, issued since 2015 and now split into a Cloud Service Provider SRG and a Mission Owner SRG,
  that defines the DoD impact levels, the FedRAMP+ controls and the provisional authorization process a cloud
  offering such as Salesforce Government Cloud Plus must pass before DoD components can use it.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:government-cloud-plus, kt:fedramp-high, kt:data-residency]
relations:
  - {predicate: hasPart, object: kt:il4-and-il5}
  - {predicate: dependsOn, object: kt:fedramp}
  - {predicate: contrastsWith, object: kt:fedramp}
sources:
  - id: s1
    title: "Cloud Service Provider Security Requirements Guide, Version 1, Release 2 (30 January 2025)"
    publisher: Defense Information Systems Agency (copy hosted by RMF.org)
    url: https://rmf.org/wp-content/uploads/2025/05/DoD-Cloud-Service-Provider-SRG-Jan-2025.pdf
    type: government
    accessed: 2026-11-03
  - id: s2
    title: "Cloud Computing Mission Owner Security Requirements Guide (30 January 2025)"
    publisher: Defense Information Systems Agency (copy hosted by RMF.org)
    url: https://rmf.org/wp-content/uploads/2025/05/DoD-Cloud-Computing-Mission-Owner-SRG-Jan-2025.pdf
    type: government
    accessed: 2026-11-03
  - id: s3
    title: "Cloud Computing Security Requirements Guide (DISA Cyber Standards Branch briefing, May 2018)"
    publisher: Defense Information Systems Agency
    url: https://disa.mil/-/media/Files/DISA/News/Events/Symposium/Cloud-Computing-Security-Requirements-Guide.ashx
    type: government
    accessed: 2026-11-03
  - id: s4
    title: "DISA Issues Cloud Computing Security Requirements Guide (June 24, 2024)"
    publisher: ExecutiveGov
    url: https://executivegov.com/2024/06/disa-issues-cloud-computing-security-requirements-guide/
    type: news
    accessed: 2026-11-03
  - id: s5
    title: "DoD IL2 - Salesforce Government Cloud Plus"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/documents/a005A00000szbDpQAI
    type: official-docs
    accessed: 2026-11-03
  - id: s6
    title: "DoD IL4 - Salesforce Government Cloud Plus Defense"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/documents/a005A00000rU71SQAS
    type: official-docs
    accessed: 2026-11-03
created: 2026-11-03
---

# DoD Cloud Computing Security Requirements Guide

The DoD Cloud Computing Security Requirements Guide (SRG) is the Defense Information Systems Agency's rulebook for putting Department of Defense information in commercial or DoD-run clouds. It tells cloud service providers (CSPs) what they must do to be listed in the DoD Cloud Service Catalog, tells DoD mission owners how to use those services safely, and gives authorizing officials a common basis for assessment.[^s1][^s3] It is issued under DoD Instruction 8500.01 and ties into the DoD Risk Management Framework (DoDI 8510.01), NIST SP 800-53 Rev 5 and CNSSI 1253, and it covers information up to and including SECRET.[^s1] For Salesforce architects it is the document behind every "DoD IL" badge on Government Cloud Plus.[^s5][^s6]

## History and current form

DoD CIO named DISA the enterprise cloud service broker in 2012. DISA's first answer was the Cloud Security Model, whose six levels appeared in 2013–2014; the first Cloud Computing SRG (v1r1) replaced it in January 2015, with major revisions in March 2016 and March 2017.[^s3] The SRG collapsed the six levels into four, folding old levels 1 and 3 into the next level up but keeping the numbers 2, 4, 5 and 6.[^s3] In June 2024 DISA released a version aligned to NIST SP 800-53 Rev 5 and the CNSSP-32 requirements for national security systems, and split the guidance into one document for providers and one for mission owners.[^s4] The current editions, both dated 30 January 2025, are the Cloud Service Provider SRG (Version 1, Release 2) and the Cloud Computing Mission Owner SRG.[^s1][^s2]

## What the provider SRG requires

The CSP SRG applies to commercial and non-DoD providers, DoD programs acting as providers, and their integrators, brokers and subcontractors, regardless of who owns the infrastructure.[^s1] Its central idea is reuse of FedRAMP rather than a parallel assessment. DoD leverages FedRAMP JAB provisional authorizations and agency ATOs (where a FedRAMP-accredited 3PAO did the assessment); at Impact Level 2, a FedRAMP Moderate or High authorization is treated as essentially sufficient, with no extra NIST control assessments.[^s1] Above that, DoD adds "FedRAMP+" controls and parameter values, derived by comparing the FedRAMP Moderate baseline with the CNSSI 1253 baseline; DISA's 2018 briefing noted that moving from IL4 to IL5 needed nine further enhancements.[^s1][^s3] The guide also stresses that impact levels are a DoD-only construct and do not map onto FedRAMP baselines.[^s1]

## Two-step authorization

Authorization happens in two steps. First, the DISA authorizing official grants a DoD Provisional Authorization (PA) on behalf of DoD CIO, and it attaches to a specific cloud service offering, not to the provider as a whole.[^s1] For IL4 and IL5 there are three routes: an existing or in-process FedRAMP JAB authorization (preferred), a FedRAMP-listed agency ATO, or, in limited cases, a DoD component's own assessment; a DoD component must sponsor the offering through the DoD Cloud Authorization Services site.[^s1] A PA can be revoked if the offering loses its FedRAMP authorization or breaches SRG or contract obligations.[^s1] Second, each mission owner's authorizing official still issues an ATO for its own system through the RMF.[^s1][^s2]

## The mission owner side

The Mission Owner SRG lists what the customer, not the provider, must do: obtain the ATO, register the offering in DoD's SNAP system and its ports and protocols in the PPSM registry, appoint a certified cybersecurity service provider for defensive cyber operations, and write incident reporting, data spill and data ownership terms into the contract.[^s2] It also sets a shared-responsibility model: for SaaS the provider secures the whole stack, while the mission owner remains accountable for its DoD data, identity management and any configuration it controls.[^s2] Connectivity for higher levels runs through Cloud Access Points, such as the NIPRNet Boundary CAP.[^s2]

## How it applies to Salesforce

Salesforce describes the SRG as DoD's layer of requirements on top of FedRAMP that any provider serving DoD must meet.[^s5] DISA has granted Government Cloud and Government Cloud Plus an IL2 PA based on Salesforce's FedRAMP Moderate and High ATOs, and an IL4 PA for Government Cloud Plus built on its FedRAMP authorization plus additional independent assessments.[^s5][^s6] Both authorizations are scoped to the environment sold as Government Cloud Plus, so an org on commercial Salesforce does not inherit them.[^s5][^s6] Because a PA covers the provider's boundary only, a DoD Salesforce program still has to configure the org (CAC/PKI login, encryption key control, STIG-aligned settings) and earn its own ATO.[^s2]

## Connections

The SRG `hasPart` the impact levels, of which IL4 and IL5 (`kt:il4-and-il5`) are the tiers most Salesforce defense programs target.[^s1] It `dependsOn` FedRAMP (`kt:fedramp`) as its control foundation yet `contrastsWith` it, since impact levels are not FedRAMP baselines; IL5 rests specifically on FedRAMP High (`kt:fedramp-high`, related).[^s1] Government Cloud Plus (`kt:government-cloud-plus`, related) is the Salesforce offering that holds SRG provisional authorizations, and data residency (`kt:data-residency`, related) matters because the SRG governs where DoD data may live.[^s5][^s6] It sits under the broader family of security compliance frameworks (`kt:security-compliance-frameworks`).[^s3]

## Sources

[^s1]: Defense Information Systems Agency, "Cloud Service Provider Security Requirements Guide, Version 1, Release 2" (30 January 2025). https://rmf.org/wp-content/uploads/2025/05/DoD-Cloud-Service-Provider-SRG-Jan-2025.pdf (accessed 2026-11-03)
[^s2]: Defense Information Systems Agency, "Cloud Computing Mission Owner Security Requirements Guide" (30 January 2025). https://rmf.org/wp-content/uploads/2025/05/DoD-Cloud-Computing-Mission-Owner-SRG-Jan-2025.pdf (accessed 2026-11-03)
[^s3]: Defense Information Systems Agency, "Cloud Computing Security Requirements Guide" briefing (May 2018). https://disa.mil/-/media/Files/DISA/News/Events/Symposium/Cloud-Computing-Security-Requirements-Guide.ashx (accessed 2026-11-03)
[^s4]: ExecutiveGov, "DISA Issues Cloud Computing Security Requirements Guide" (June 24, 2024). https://executivegov.com/2024/06/disa-issues-cloud-computing-security-requirements-guide/ (accessed 2026-11-03)
[^s5]: Salesforce, "DoD IL2 - Salesforce Government Cloud Plus". https://compliance.salesforce.com/en/documents/a005A00000szbDpQAI (accessed 2026-11-03)
[^s6]: Salesforce, "DoD IL4 - Salesforce Government Cloud Plus Defense". https://compliance.salesforce.com/en/documents/a005A00000rU71SQAS (accessed 2026-11-03)
