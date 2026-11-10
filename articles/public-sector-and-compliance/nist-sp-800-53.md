---
id: kt:nist-sp-800-53
type: ExternalConcept
title: NIST SP 800-53
aliases: [NIST 800-53, "Security and Privacy Controls for Information Systems and Organizations", SP 800-53 Rev. 5, NIST control catalog]
domain: public-sector-and-compliance
summary: >-
  NIST Special Publication 800-53, the US government's catalog of security and privacy controls organized into 20
  families; its companion SP 800-53B defines the Low, Moderate, High and privacy baselines that FedRAMP tailors
  to assess cloud services such as Salesforce Government Cloud Plus.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:fedramp, kt:government-cloud-plus, kt:dod-cloud-computing-srg, kt:multi-factor-authentication]
relations:
  - {predicate: consumedBy, object: kt:fedramp-high}
  - {predicate: dependsOn, object: kt:fips-199}
  - {predicate: hasPart, object: kt:nist-sp-800-53b}
sources:
  - id: s1
    title: "SP 800-53 Rev. 5, Security and Privacy Controls for Information Systems and Organizations (upd1)"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final
    type: standards-body
    accessed: 2026-11-04
  - id: s2
    title: "SP 800-53 Rev. 5 (September 2020 original, withdrawn)"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/archive/2020-09-23
    type: standards-body
    accessed: 2026-11-04
  - id: s3
    title: "NIST Releases Revision to SP 800-53 Controls"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/News/2025/nist-releases-revision-to-sp-800-53-controls
    type: standards-body
    accessed: 2026-11-04
  - id: s4
    title: "Control Baselines for Information Systems and Organizations: NIST Publishes SP 800-53B"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/news/2020/control-baselines-nist-publishes-sp-800-53b
    type: standards-body
    accessed: 2026-11-04
  - id: s5
    title: "Rev. 5 Baselines Have Been Approved and Released"
    publisher: FedRAMP (GSA)
    url: https://www.fedramp.gov/archive/2023-05-30-rev-5-baselines-have-been-approved-and-released/
    type: government
    accessed: 2026-11-04
  - id: s6
    title: "IRS 1075 — Salesforce Compliance"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/irs-1075
    type: official-docs
    accessed: 2026-11-04
created: 2026-11-04
---

# NIST SP 800-53

NIST Special Publication 800-53, *Security and Privacy Controls for Information Systems and Organizations*, is the control catalog that underpins most US federal security programs, written by the Joint Task Force under the National Institute of Standards and Technology. It describes safeguards that protect an organization's operations and assets, individuals, other organizations and the nation against threats ranging from hostile attacks and human error to natural disasters and privacy risks.[^s2] The controls are deliberately flexible and customizable, and are meant to be selected and implemented through an organization-wide risk management process rather than applied as a fixed checklist.[^s1] For Salesforce practitioners it matters because it is the vocabulary in which FedRAMP, agency authorizations and many customer security questionnaires are expressed.

## Structure and versions

Revision 5 was finalized in September 2020 and superseded Revision 4 from 2015.[^s2] That September text was itself withdrawn in December 2020 in favour of an errata update (upd1), which is the current base publication.[^s1] Rev. 5 consolidated security and privacy into one catalog and covers both functionality (how strong a control's mechanisms are) and assurance (how confident one can be that they work).[^s1] It groups controls into 20 families, including Access Control, Audit and Accountability, Configuration Management, Identification and Authentication, Incident Response, System and Communications Protection, PII Processing and Transparency, and Supply Chain Risk Management.[^s2]

NIST now ships incremental releases of the catalog in machine-readable form. Release 5.2.0, published in August 2025 in response to Executive Order 14306, focused on the security and reliability of software updates and patches, adding controls such as SA-15(13), SA-24 and SI-02(07) and revising others.[^s1][^s3] The catalog is distributed through NIST's CPRT tool and as OSCAL (JSON, XML, YAML), which compliance tooling can ingest directly.[^s1][^s3] Assessment procedures live in the companion SP 800-53A.[^s1]

## Baselines and tailoring

SP 800-53 itself is only the menu; SP 800-53B selects from it. That companion defines three security baselines for low-, moderate- and high-impact systems plus a separate privacy baseline that applies regardless of impact level, and it gives tailoring guidance and a method for building overlays for particular communities or technologies.[^s4] A system's impact level is set by its FIPS 199 categorization, which is why FedRAMP's Low, Moderate and High baselines map onto these NIST tiers.[^s4][^s5]

## How Salesforce encounters it

FedRAMP did not invent its own control set: in May 2023 its Joint Authorization Board approved Rev. 5 baselines built on SP 800-53 Rev. 5 and 800-53B, adding cloud-specific guidance for many controls.[^s5] Two gotchas follow. First, privacy controls outside the FedRAMP baselines remain at the agency's discretion, and Program Management (PM) controls stay an agency responsibility, so a FedRAMP authorization for Salesforce does not discharge everything an agency owes under 800-53.[^s5] Second, assessment artefacts can lag the current revision: Salesforce's IRS Publication 1075 attestation for Government Cloud Plus was assessed against SP 800-53 revision 4 while leveraging FedRAMP High baseline controls, so architects should check which revision a given audit letter cites.[^s6]

The practical consequence is a split of responsibility: the cloud provider's authorization covers the baseline controls it was assessed on, while the agency still owns PM controls, any privacy controls it chooses beyond the baseline, and its own authorization decision. Salesforce points customers to the Government Cloud Plus FedRAMP package and the auditor's attestation letter as inputs to that decision rather than a substitute for it.[^s5][^s6]

## Connections

NIST SP 800-53 sits under the broader family of security compliance frameworks (`kt:security-compliance-frameworks`).[^s1] Its baselines are defined in the companion SP 800-53B (`kt:nist-sp-800-53b`), and the impact level that selects a baseline `dependsOn` FIPS 199 categorization (`kt:fips-199`).[^s4] FedRAMP (`kt:fedramp`) and its strictest tier, FedRAMP High (`kt:fedramp-high`), use the catalog as their control source.[^s5] Government Cloud Plus (`kt:government-cloud-plus`) is the Salesforce environment assessed against those controls, including for IRS 1075.[^s6] It is related to DISA's Cloud Computing SRG (`kt:dod-cloud-computing-srg`), the defense-side counterpart covered in its own article, and the catalog's Identification and Authentication family is the control area that platform features such as multi-factor authentication (`kt:multi-factor-authentication`) speak to.[^s2]

## Sources
[^s1]: NIST CSRC, "SP 800-53 Rev. 5, Security and Privacy Controls for Information Systems and Organizations (upd1)". https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final (accessed 2026-11-04)
[^s2]: NIST CSRC, "SP 800-53 Rev. 5 (September 2020 original, withdrawn)". https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/archive/2020-09-23 (accessed 2026-11-04)
[^s3]: NIST CSRC, "NIST Releases Revision to SP 800-53 Controls". https://csrc.nist.gov/News/2025/nist-releases-revision-to-sp-800-53-controls (accessed 2026-11-04)
[^s4]: NIST CSRC, "Control Baselines for Information Systems and Organizations: NIST Publishes SP 800-53B". https://csrc.nist.gov/news/2020/control-baselines-nist-publishes-sp-800-53b (accessed 2026-11-04)
[^s5]: FedRAMP (GSA), "Rev. 5 Baselines Have Been Approved and Released". https://www.fedramp.gov/archive/2023-05-30-rev-5-baselines-have-been-approved-and-released/ (accessed 2026-11-04)
[^s6]: Salesforce, "IRS 1075 — Salesforce Compliance". https://compliance.salesforce.com/en/irs-1075 (accessed 2026-11-04)
