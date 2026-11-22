---
id: kt:iso-iec-27018
type: ExternalConcept
title: ISO/IEC 27018
aliases: [ISO 27018, "ISO/IEC 27018:2025", "ISO/IEC 27018:2019", Code of practice for PII protection in public clouds, PII in public clouds standard]
domain: public-sector-and-compliance
summary: >-
  The ISO/IEC standard giving control objectives, controls and guidelines, built on ISO/IEC 27002, for protecting
  personally identifiable information (PII) in public clouds acting as PII processors; the third edition (2025) is
  current, and Salesforce lists ISO/IEC 27018:2019 certificates covering most of its cloud services.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:iso-iec-27017, kt:gdpr-international-transfers, kt:shared-responsibility-model, kt:hyperforce, kt:iso-iec-29100]
relations:
  - {predicate: dependsOn, object: kt:iso-iec-27002}
  - {predicate: consumedBy, object: kt:iso-iec-27001}
sources:
  - id: s1
    title: "ISO/IEC 27018:2025 Information security, cybersecurity and privacy protection — Guidelines for protection of PII in public clouds acting as PII processors"
    publisher: ISO
    url: https://www.iso.org/standard/27018
    type: standards-body
    accessed: 2026-11-22
  - id: s2
    title: "ISO/IEC 27018:2025"
    publisher: IEC Webstore
    url: https://webstore.iec.ch/en/publication/109374
    type: standards-body
    accessed: 2026-11-22
  - id: s3
    title: "ISO 27018 — Salesforce Compliance"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/iso-27018
    type: official-docs
    accessed: 2026-11-22
  - id: s4
    title: "ISO 27018 category — Salesforce Compliance"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/categories/iso-27018
    type: official-docs
    accessed: 2026-11-22
  - id: s5
    title: "Salesforce Services Security, Privacy, and Architecture"
    publisher: Salesforce
    url: https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/misc/salesforce-security-privacy-and-architecture.pdf?bc=OTH
    type: official-docs
    accessed: 2026-11-22
created: 2026-11-22
---

# ISO/IEC 27018

ISO/IEC 27018 is the international code of practice for protecting personally identifiable information (PII) in public cloud services where the cloud provider acts as a **PII processor**, that is, it handles personal data on behalf of customers rather than for its own purposes.[^s1][^s2] It sets commonly accepted control objectives, controls and guidelines that implement the privacy principles of ISO/IEC 29100 in a public cloud setting, while taking regulatory requirements for PII protection into account.[^s2] Salesforce summarizes it as the standard for privacy protections when cloud service providers process personal information, and lists it alongside ISO/IEC 27001 and 27017 in its compliance documentation.[^s3][^s5]

## Edition and scope

The current edition is ISO/IEC 27018:2025, the third edition, published by the joint committee ISO/IEC JTC 1/SC 27; the IEC Webstore dates it 26 August 2025 and lists 35 pages.[^s1][^s2] It carries the newer family title "Information security, cybersecurity and privacy protection".[^s1] The 2025 edition is aligned with ISO/IEC 27002:2022 and adds a new Annex B with extended implementation guidance.[^s1] Earlier editions remain in circulation through certificates: Salesforce's listed certificates cite ISO/IEC 27018:2019.[^s4]

The standard applies to organizations of every type and size, public, private, government or not-for-profit, that process PII as processors through cloud computing under contract to other organizations.[^s2] The IEC abstract notes it may also be relevant to organizations acting as PII **controllers**, although its guidance is written from the processor's side.[^s2] ISO describes the life cycle it covers as collection, storage, processing, transmission and deletion of PII handled by public cloud providers for their customers, and names a second audience: organizations that evaluate cloud providers or outsource data processing.[^s1]

## How it relates to the 27000 family

ISO/IEC 27018 is not a standalone certifiable management system. It is built on ISO/IEC 27002, extending and adapting that control catalog for cloud PII processing, and it complements an information security management system (ISMS) run under ISO/IEC 27001.[^s1] In practice a provider is certified against 27001 with 27018 (and often 27017) added to the scope. Salesforce describes exactly this arrangement: it operates an ISMS for its covered services under ISO 27001, aligned to ISO 27017 and ISO 27018, and states that an independent third party has certified that ISMS against all three.[^s5] The certificate and the Statement of Applicability are published on Salesforce's compliance website.[^s5]

## Salesforce certificate coverage

Salesforce's compliance site lists two ISO/IEC 27018:2019 certificates.[^s4]

- **Main certificate**: infrastructure first party, AWS and Hyperforce; services include Salesforce Services (first party and Hyperforce), Data Cloud, Agentforce and Einstein Platform, Heroku, MuleSoft, Tableau Cloud and several Marketing Cloud products.[^s4]
- **Slack certificate**: infrastructure AWS; services Slack and GovSlack.[^s4]

The Security, Privacy, and Architecture document (published 18 November 2025) applies its ISO statement only to its own Covered Services and lists exclusions, among them Communications Cloud, Consumer Goods Cloud, Salesforce Starter, Salesforce Foundations, DevOps Center, Privacy Center and Salesforce Backup.[^s5] That document also excludes some products, such as Marketing Cloud and B2C Commerce, that appear on the certificate listing, so the two listings do not have identical scope.[^s4][^s5]

## Gotchas for architects

- **Edition mismatch.** The listed certificates cite the 2019 edition while the 2025 edition is current, so ask which edition a vendor's certificate covers before mapping controls.[^s1][^s4]
- **Check the exclusion list.** A product on the general covered-services list can still be excluded from the ISO statement; confirm each cloud and add-on your design uses.[^s5]
- **Processor, not controller.** The certificate addresses Salesforce's duties as processor; your organization's obligations as controller, such as lawful basis and consent, are not discharged by it.[^s2][^s3]
- **Match the infrastructure.** Certificates are scoped by infrastructure (first party, AWS, Hyperforce), so match the document to where your org actually runs.[^s3][^s4]

## Connections

ISO/IEC 27018 sits under security compliance frameworks (`kt:security-compliance-frameworks`). It `dependsOn` ISO/IEC 27002 (`kt:iso-iec-27002`), whose controls it extends, and is `consumedBy` ISO/IEC 27001 (`kt:iso-iec-27001`), the certifiable ISMS in whose scope it is audited.[^s1][^s5] Its companion for general cloud security controls is ISO/IEC 27017 (`kt:iso-iec-27017`); Salesforce aligns its ISMS to both.[^s5] It implements the privacy principles of ISO/IEC 29100 (`kt:iso-iec-29100`).[^s2] The processor-versus-controller split mirrors the shared responsibility model (`kt:shared-responsibility-model`), and the same processor and controller roles frame GDPR transfer analysis (`kt:gdpr-international-transfers`).[^s2] Salesforce's certificate scope includes Hyperforce (`kt:hyperforce`).[^s4]

## Sources
[^s1]: ISO, "ISO/IEC 27018:2025 Information security, cybersecurity and privacy protection — Guidelines for protection of PII in public clouds acting as PII processors". https://www.iso.org/standard/27018 (accessed 2026-11-22)
[^s2]: IEC Webstore, "ISO/IEC 27018:2025". https://webstore.iec.ch/en/publication/109374 (accessed 2026-11-22)
[^s3]: Salesforce, "ISO 27018 — Salesforce Compliance". https://compliance.salesforce.com/en/iso-27018 (accessed 2026-11-22)
[^s4]: Salesforce, "ISO 27018 category — Salesforce Compliance". https://compliance.salesforce.com/en/categories/iso-27018 (accessed 2026-11-22)
[^s5]: Salesforce, "Salesforce Services Security, Privacy, and Architecture". https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/misc/salesforce-security-privacy-and-architecture.pdf?bc=OTH (accessed 2026-11-22)
