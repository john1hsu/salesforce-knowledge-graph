---
id: kt:nist-cybersecurity-framework
type: ExternalConcept
title: NIST Cybersecurity Framework
aliases: [NIST CSF, CSF 2.0, "NIST CSWP 29", "Framework for Improving Critical Infrastructure Cybersecurity"]
domain: public-sector-and-compliance
summary: >-
  NIST's voluntary, outcome-based framework for managing cybersecurity risk, organized in version 2.0 (CSWP 29,
  February 2024) into six Functions (Govern, Identify, Protect, Detect, Respond, Recover) plus Profiles and Tiers;
  it says what to achieve and points to control catalogs such as SP 800-53 for how.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:iso-iec-27001, kt:fedramp, kt:hitrust-csf]
relations:
  - {predicate: contrastsWith, object: kt:nist-sp-800-53}
sources:
  - id: s1
    title: "CSWP 29, The NIST Cybersecurity Framework (CSF) 2.0"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final
    type: standards-body
    accessed: 2026-11-07
  - id: s2
    title: "The NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29, PDF)"
    publisher: NIST
    url: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf
    type: standards-body
    accessed: 2026-11-07
  - id: s3
    title: "History and Creation of the CSF 1.1"
    publisher: NIST
    url: https://www.nist.gov/cyberframework/history-and-creation-framework
    type: standards-body
    accessed: 2026-11-07
  - id: s4
    title: "CSWP 6, Framework for Improving Critical Infrastructure Cybersecurity, Version 1.1"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/pubs/cswp/6/cybersecurity-framework-v11/final
    type: standards-body
    accessed: 2026-11-07
  - id: s5
    title: "Salesforce, Inc. response to NIST RFI on evaluating and improving the Cybersecurity Framework"
    publisher: Salesforce (comment letter published by NIST)
    url: https://www.nist.gov/document/salesforce-inc-csf-20-response
    type: official-docs
    accessed: 2026-11-07
  - id: s6
    title: "Salesforce is Now Part of the HITRUST Shared Responsibility and Inheritance Program"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/hitrust/?bc=OTH
    type: official-blog
    accessed: 2026-11-07
created: 2026-11-07
---

# NIST Cybersecurity Framework

The NIST Cybersecurity Framework (CSF) is voluntary guidance from the US National Institute of Standards and Technology for managing cybersecurity risk. Version 2.0, published on 26 February 2024 as NIST Cybersecurity White Paper (CSWP) 29, offers a taxonomy of high-level outcomes that any organization, whatever its size, sector or maturity, can use to understand, assess, prioritize and communicate its cybersecurity efforts.[^s1] It deliberately does not prescribe how to achieve those outcomes; instead it points to online resources that list practices and controls.[^s1] For Salesforce architects, the CSF is the common language many security teams use to describe their program, so it shapes how a Salesforce org's controls are documented and assessed.[^s5]

## History

The framework began with Executive Order 13636, signed on 12 February 2013, which tasked NIST with developing it; version 1.0 followed exactly one year later, on 12 February 2014, after a Request for Information, a Request for Comment and five workshops with government, industry and academia.[^s3] Version 1.1 (CSWP 6), released on 16 April 2018, added a self-assessment section, expanded cyber supply chain risk management guidance, refined authentication, authorization and identity proofing language, and explained how Tiers relate to Profiles.[^s4] Earlier versions carried the title "Framework for Improving Critical Infrastructure Cybersecurity"; CSF 2.0 drops that name, reflecting its broader audience.[^s2] A draft of 2.0 appeared on 8 August 2023 before the final release.[^s1]

## How it works

The framework has three parts. The **CSF Core** is a hierarchy of Functions, Categories and Subcategories; 2.0 defines 22 Categories across six Functions.[^s2]

- **Govern (GV)** — set, communicate and monitor risk strategy, expectations and policy.
- **Identify (ID)** — understand current risks to assets, suppliers and the organization.
- **Protect (PR)** — apply safeguards that lower the likelihood and impact of events.
- **Detect (DE)** — find and analyze possible attacks and compromises.
- **Respond (RS)** — act on detected incidents to contain their effects.
- **Recover (RC)** — restore affected assets and operations.[^s2]

**Organizational Profiles** describe a Current Profile (outcomes being achieved and how well) and a Target Profile (outcomes selected and prioritized for the organization's goals); Community Profiles give sector or technology baselines to start from.[^s2] **Tiers** (Partial, Risk Informed, Repeatable, Adaptive) describe the rigor of risk governance and management; NIST frames them as something to move up when risk, mandates or cost-benefit justify it, not as maturity levels to chase for their own sake.[^s2]

Around the Core, NIST publishes **Informative References** that map outcomes to standards and regulations, **Implementation Examples** that sketch notional actions, and **Quick-Start Guides**.[^s2] Supply chain risk management now sits under Govern as GV.SC, with ten Subcategories covering supplier prioritization, contract requirements, due diligence, monitoring, incident coordination and end-of-relationship activities.[^s2]

## Using it with Salesforce

- **Outcomes, not controls.** An SP 800-53 control may be only one of several Informative References needed for a single CSF Subcategory, so a CSF profile for a Salesforce org still has to be translated into concrete configuration and controls.[^s2]
- **Salesforce as a supplier.** Because GV.SC asks organizations to prioritize suppliers by criticality and fold them into incident response, a Salesforce org holding sensitive data typically appears in a customer's supply chain risk register.[^s2]
- **Salesforce's own use.** In its 2022 comment letter to NIST, Salesforce described using the CSF as a maturity model calibrated by an outside firm, and asked NIST for clearer per-Tier requirements, mappings to SP 800-53 and ISO standards, and a cloud addendum mapped to FedRAMP and DoD cloud baselines.[^s5]
- **Inheritance through HITRUST.** Healthcare customers often meet CSF expectations through the HITRUST CSF, which consolidates the NIST framework with HIPAA, ISO 27001 and SOC 2; Salesforce participates in HITRUST's Shared Responsibility and Inheritance program so customers can reuse its validated controls in their own assessments.[^s6]

## Connections

The CSF sits under security compliance frameworks (`kt:security-compliance-frameworks`) as the outcome-level member of that family.[^s1] It `contrastsWith` NIST SP 800-53 (`kt:nist-sp-800-53`): the CSF states outcomes, while SP 800-53 is a control catalog that serves as one of its Informative References and complements it through the NIST Risk Management Framework.[^s2] It is related to ISO/IEC 27001 (`kt:iso-iec-27001`), the management-system standard that Salesforce asked NIST to map the CSF against, and to FedRAMP (`kt:fedramp`), the federal cloud baseline Salesforce proposed a CSF cloud addendum for.[^s5] The HITRUST CSF (`kt:hitrust-csf`) is related as an assessable framework that folds the NIST CSF into a single control set with Salesforce control inheritance.[^s6]

## Sources
[^s1]: NIST CSRC, "CSWP 29, The NIST Cybersecurity Framework (CSF) 2.0". https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final (accessed 2026-11-07)
[^s2]: NIST, "The NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29, PDF)". https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf (accessed 2026-11-07)
[^s3]: NIST, "History and Creation of the CSF 1.1". https://www.nist.gov/cyberframework/history-and-creation-framework (accessed 2026-11-07)
[^s4]: NIST CSRC, "CSWP 6, Framework for Improving Critical Infrastructure Cybersecurity, Version 1.1". https://csrc.nist.gov/pubs/cswp/6/cybersecurity-framework-v11/final (accessed 2026-11-07)
[^s5]: Salesforce, "Salesforce, Inc. response to NIST RFI on evaluating and improving the Cybersecurity Framework". https://www.nist.gov/document/salesforce-inc-csf-20-response (accessed 2026-11-07)
[^s6]: Salesforce, "Salesforce is Now Part of the HITRUST Shared Responsibility and Inheritance Program". https://www.salesforce.com/blog/hitrust/?bc=OTH (accessed 2026-11-07)
