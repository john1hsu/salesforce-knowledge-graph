---
id: kt:iso-iec-27001
type: ExternalConcept
title: ISO/IEC 27001
aliases: [ISO 27001, "ISO/IEC 27001:2022", ISMS standard, "Information security management systems — Requirements"]
domain: public-sector-and-compliance
summary: >-
  The international standard that sets requirements for an information security management system (ISMS), certified
  by accredited third-party audits; Salesforce lists ISO/IEC 27001:2022 certificates for its services and infrastructure (first party, AWS and
  Hyperforce) on its compliance site.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:nist-sp-800-53, kt:nist-cybersecurity-framework, kt:hyperforce, kt:data-residency, kt:fedramp]
relations:
  - {predicate: dependsOn, object: kt:iso-iec-27002}
  - {predicate: contrastsWith, object: kt:soc-2}
sources:
  - id: s1
    title: "ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements"
    publisher: IEC Webstore
    url: https://webstore.iec.ch/publication/79694
    type: standards-body
    accessed: 2026-11-06
  - id: s2
    title: "ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls"
    publisher: IEC Webstore
    url: https://webstore.iec.ch/en/publication/74287
    type: standards-body
    accessed: 2026-11-06
  - id: s3
    title: "SP 800-53 Rev. 5, Security and Privacy Controls for Information Systems and Organizations (upd1)"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final
    type: standards-body
    accessed: 2026-11-06
  - id: s4
    title: "ISO 27001 — Salesforce Compliance"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/iso-27001
    type: official-docs
    accessed: 2026-11-06
  - id: s5
    title: "General (not service specific) — Salesforce Compliance"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/services/general
    type: official-docs
    accessed: 2026-11-06
  - id: s6
    title: "How to Prepare for ISO/IEC 27001:2022"
    publisher: Cloud Security Alliance
    url: https://cloudsecurityalliance.org/articles/how-to-prepare-for-iso-iec-27001-2022
    type: partner
    accessed: 2026-11-06
created: 2026-11-06
---

# ISO/IEC 27001

ISO/IEC 27001 is the international standard that specifies requirements for establishing, implementing, maintaining and continually improving an information security management system (ISMS), including how an organization assesses and treats its information security risks.[^s1] The current edition, ISO/IEC 27001:2022 (edition 3), was published on 25 October 2022 by joint committee ISO/IEC JTC 1/SC 27 and is written generically so that it applies to organizations of any type or size.[^s1] For Salesforce practitioners it matters in two ways: Salesforce's own certification is a standard item in customer security reviews, and many customers run their own ISMS that must account for Salesforce as a supplier.[^s4][^s5]

## How the standard works

The standard is a management-system standard, not a technical checklist. Its mandatory requirements sit in Clauses 4 to 10 (context, leadership, planning, support, operation, performance evaluation and improvement), and an organization claiming conformity may not exclude any of them.[^s1] The 2022 revision added subclause 6.3, which requires changes to the ISMS to be planned, and tidied wording in the risk-treatment clauses that previously referred to control objectives.[^s6]

Controls come from Annex A, which mirrors the catalog in the companion standard ISO/IEC 27002. ISO/IEC 27002:2022, published 15 February 2022, provides a reference set of generic controls with implementation guidance and is designed to be used within an ISMS based on 27001.[^s2] In that revision the 114 controls of the 2013 edition were consolidated into 93, reorganized into new Clauses 5 to 8.[^s6] The organization records which controls apply and why in a Statement of Applicability, which transition audits had to update alongside the risk treatment plan.[^s6]

## Certification and the 2013 transition

Certification is granted by an accredited certification body after an audit, then maintained through surveillance audits. Salesforce describes its certificates as running three years between renewal audits, with annual surveillance audits in between.[^s4] Organizations certified to the 2013 edition had a 36-month transition; the deadline to move to the 2022 version was 31 October 2025, after which 2013-based certificates expire or are withdrawn.[^s6]

## Salesforce's certification

Salesforce's compliance site lists ISO 27001 coverage for office sites, development centers, support centers and data centers, with documents labeled by infrastructure: first-party data centers, AWS and Hyperforce.[^s4] Its corporate-level ("General") service lists an ISO/IEC 27001:2022 certificate alongside ISO/IEC 27017:2015 (cloud security) and ISO/IEC 27018:2019 (protection of personal data in public clouds), each updated on 30 October 2026, and points readers to the Audits and Certifications section of each service's Security, Privacy and Architecture documentation for product-specific scope.[^s5]

## Gotchas for architects

- **Scope, not brand.** A certificate covers a defined scope. Check that the specific cloud or product in your design, and the infrastructure it runs on, is listed for the certificate you rely on.[^s4][^s5]
- **Corporate versus service scope.** The General listing applies to Salesforce as an entity without the context of a specific service, so product-level questions belong to that product's Security, Privacy and Architecture documentation.[^s5]
- **Not one-to-one with NIST.** NIST publishes a crosswalk from SP 800-53 Rev. 5 to ISO/IEC 27001:2022 but warns that relationships are not always one-to-one and should not be read as equivalence.[^s3]

## Connections

ISO/IEC 27001 sits under security compliance frameworks (`kt:security-compliance-frameworks`) as the management-system standard at the international end of that family.[^s1] It `dependsOn` ISO/IEC 27002 (`kt:iso-iec-27002`), whose control catalog supplies Annex A.[^s2] NIST SP 800-53 (`kt:nist-sp-800-53`) is the US federal control catalog that NIST crosswalks to it, while the NIST Cybersecurity Framework (`kt:nist-cybersecurity-framework`) is an outcome framework often used alongside it, and the crosswalk is the usual bridge when a design must also satisfy the US federal FedRAMP program (`kt:fedramp`), which is covered in its own node.[^s3] Salesforce lists its certificates by infrastructure, which ties the standard to Hyperforce (`kt:hyperforce`) and to data residency (`kt:data-residency`) decisions about where certified services run.[^s4][^s5] It `contrastsWith` SOC 2 (`kt:soc-2`): both appear on Salesforce's corporate compliance listing, but ISO 27001 is delivered as a certificate against a management-system standard, whereas SOC 1 and SOC 2 are delivered as audit reports.[^s4][^s5]

## Sources
[^s1]: IEC Webstore, "ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements". https://webstore.iec.ch/publication/79694 (accessed 2026-11-06)
[^s2]: IEC Webstore, "ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls". https://webstore.iec.ch/en/publication/74287 (accessed 2026-11-06)
[^s3]: NIST CSRC, "SP 800-53 Rev. 5, Security and Privacy Controls for Information Systems and Organizations (upd1)". https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final (accessed 2026-11-06)
[^s4]: Salesforce, "ISO 27001 — Salesforce Compliance". https://compliance.salesforce.com/en/iso-27001 (accessed 2026-11-06)
[^s5]: Salesforce, "General (not service specific) — Salesforce Compliance". https://compliance.salesforce.com/en/services/general (accessed 2026-11-06)
[^s6]: Cloud Security Alliance, "How to Prepare for ISO/IEC 27001:2022". https://cloudsecurityalliance.org/articles/how-to-prepare-for-iso-iec-27001-2022 (accessed 2026-11-06)
