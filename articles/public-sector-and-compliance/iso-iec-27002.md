---
id: kt:iso-iec-27002
type: ExternalConcept
title: ISO/IEC 27002
aliases: [ISO 27002, "ISO/IEC 27002:2022", "Information security controls", ISO 27002 control catalog]
domain: public-sector-and-compliance
summary: >-
  The ISO/IEC code of practice that supplies a reference set of 93 generic information security controls, each with a
  purpose and implementation guidance, used to select and implement controls within an ISO/IEC 27001 information
  security management system and extended for cloud services by ISO/IEC 27017.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:iso-iec-27017, kt:shared-responsibility-model, kt:hyperforce, kt:secure-coding]
relations:
  - {predicate: consumedBy, object: kt:iso-iec-27001}
  - {predicate: contrastsWith, object: kt:nist-sp-800-53}
sources:
  - id: s1
    title: "ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls"
    publisher: IEC Webstore
    url: https://webstore.iec.ch/en/publication/74287
    type: standards-body
    accessed: 2026-11-16
  - id: s2
    title: "ISO/IEC 27002:2022 — Understanding the Update"
    publisher: Cloud Security Alliance
    url: https://cloudsecurityalliance.org/articles/iso-iec-27002-2022-understanding-the-update
    type: partner
    accessed: 2026-11-16
  - id: s3
    title: "Key Changes in ISO/IEC 27002:2022"
    publisher: SGS
    url: https://www.sgs.com/en-ch/news/2022/07/key-changes-in-iso-iec-27002-2022
    type: partner
    accessed: 2026-11-16
  - id: s4
    title: "ISO 27017 — Salesforce Compliance"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/iso-27017
    type: official-docs
    accessed: 2026-11-16
  - id: s5
    title: "General (not service specific) — Salesforce Compliance"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/services/general
    type: official-docs
    accessed: 2026-11-16
  - id: s6
    title: "SP 800-53 Rev. 5, Security and Privacy Controls for Information Systems and Organizations (upd1)"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final
    type: standards-body
    accessed: 2026-11-16
created: 2026-11-16
---

# ISO/IEC 27002

ISO/IEC 27002 is the international code of practice for information security controls. It gives organizations a general reference set of controls together with implementation guidance, intended to be used inside an information security management system (ISMS) built on ISO/IEC 27001, to apply recognized good practice, or as the starting point for an organization's own security guidelines.[^s1] The current edition, ISO/IEC 27002:2022 (edition 3.0), was published on 15 February 2022 by the joint committee ISO/IEC JTC 1/SC 27 and runs to 152 pages.[^s1] Where 27001 says what an ISMS must do, 27002 describes how individual controls can be implemented, which is why Salesforce practitioners meet it whenever a customer maps its own control set or reviews a vendor's security posture.[^s1][^s5]

## How the catalog is organized

The 2022 edition cut the catalog from 114 controls to 93: 11 controls are new, 24 merge two or more 2013 controls, and 58 were reviewed and revised.[^s2] The 14 control domains of the 2013 edition were replaced by four themes: organizational, people, physical and technological.[^s2][^s3] The control objective that sat above groups of controls in 2013 is gone; instead each control carries its own purpose statement explaining why it should be implemented.[^s3]

Each control is also tagged with five attributes, each holding values, so that an organization can sort and filter the catalog in views other than the four themes, for example during risk assessment and treatment.[^s2][^s3] Annex A of the standard explains how to use the attributes, and using them is optional: an organization may ignore some or define its own, such as a maturity model.[^s2][^s3] Annex B maps the 2022 controls back to the 2013 edition, which helps teams update older control matrices.[^s2]

## Controls added in 2022

The 11 new controls reflect how security practice changed in the cloud era: threat intelligence, information security for use of cloud services, ICT readiness for business continuity, physical security monitoring, configuration management, information deletion, data masking, data leakage prevention, monitoring activities, web filtering and secure coding.[^s3] Several of these map naturally onto Salesforce design decisions, such as masking data in non-production orgs, governing what leaves the platform, and secure development practices for custom code.[^s3]

## Relationship to ISO/IEC 27001 and certification

ISO/IEC 27002 is guidance, not a certifiable requirements standard: organizations are certified against 27001, and 27002 explains the controls they choose.[^s1] Annex A of 27001 is designed to align with 27002, so the 2022 revision of 27002 drove an amendment to 27001 that replaced its Annex A with the new control set.[^s3] Its guidance can also be used outside any certification effort, for example as the starting point for an organization's own security guidelines.[^s1]

The 27002 catalog is also the base for sector extensions. ISO/IEC 27017 is a code of practice for cloud computing that recommends cloud-specific controls supplementing the guidance in ISO 27002 and ISO 27001, with implementation guidance for cloud service providers.[^s4] Salesforce lists an ISO/IEC 27017:2015 certificate for its corporate services, alongside its ISO/IEC 27001:2022 and ISO/IEC 27018:2019 certificates, covering first-party, AWS and Hyperforce infrastructure.[^s5]

## Gotchas for architects

- **No "27002 certificate".** Ask a vendor for its 27001 certificate and scope; 27002 conformance is evidenced through that ISMS.[^s1][^s5]
- **Check the edition.** Control numbers and names changed in 2022, so map older questionnaires through Annex B.[^s2]
- **Cloud controls live in 27017.** Shared cloud responsibilities are addressed by 27017's supplementary controls, not by 27002 alone.[^s4]
- **Crosswalks are not equivalence.** NIST publishes an OLIR crosswalk from SP 800-53 Rev. 5 to 27001:2022 but warns not to assume equivalency from relationship tables.[^s6]

## Connections

ISO/IEC 27002 sits under security compliance frameworks (`kt:security-compliance-frameworks`) as the control-catalog half of the ISO 27000 family.[^s1] It is `consumedBy` ISO/IEC 27001 (`kt:iso-iec-27001`), whose Annex A reuses its control set.[^s3] ISO/IEC 27017 (`kt:iso-iec-27017`) extends it for cloud providers, which ties it to the shared responsibility model (`kt:shared-responsibility-model`) and to Hyperforce (`kt:hyperforce`), one of the infrastructures in Salesforce's certificate scope.[^s4][^s5] Its new secure coding control relates it to secure coding practice (`kt:secure-coding`).[^s3] It `contrastsWith` NIST SP 800-53 (`kt:nist-sp-800-53`), the US federal control catalog that NIST crosswalks to the ISO family with an explicit caveat that mappings are not one-to-one.[^s6]

## Sources
[^s1]: IEC Webstore, "ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls". https://webstore.iec.ch/en/publication/74287 (accessed 2026-11-16)
[^s2]: Cloud Security Alliance, "ISO/IEC 27002:2022 — Understanding the Update". https://cloudsecurityalliance.org/articles/iso-iec-27002-2022-understanding-the-update (accessed 2026-11-16)
[^s3]: SGS, "Key Changes in ISO/IEC 27002:2022". https://www.sgs.com/en-ch/news/2022/07/key-changes-in-iso-iec-27002-2022 (accessed 2026-11-16)
[^s4]: Salesforce, "ISO 27017 — Salesforce Compliance". https://compliance.salesforce.com/en/iso-27017 (accessed 2026-11-16)
[^s5]: Salesforce, "General (not service specific) — Salesforce Compliance". https://compliance.salesforce.com/en/services/general (accessed 2026-11-16)
[^s6]: NIST CSRC, "SP 800-53 Rev. 5, Security and Privacy Controls for Information Systems and Organizations (upd1)". https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final (accessed 2026-11-16)
