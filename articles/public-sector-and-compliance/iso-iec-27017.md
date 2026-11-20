---
id: kt:iso-iec-27017
type: ExternalConcept
title: ISO/IEC 27017
aliases: [ISO 27017, "ISO/IEC 27017:2026", "ISO/IEC 27017:2015", "ITU-T X.1631", Cloud security controls code of practice]
domain: public-sector-and-compliance
summary: >-
  The ISO/IEC standard that extends the ISO/IEC 27002 control catalog for cloud services, adding cloud-specific
  guidance and controls for both cloud service providers and customers; the second edition (2026) replaced the 2015
  edition, and Salesforce holds an ISO/IEC 27017 certificate for its corporate services.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:shared-responsibility-model, kt:hyperforce, kt:iso-iec-27018, kt:multitenancy]
relations:
  - {predicate: dependsOn, object: kt:iso-iec-27002}
  - {predicate: consumedBy, object: kt:iso-iec-27001}
sources:
  - id: s1
    title: "ISO/IEC 27017:2026 Information security, cybersecurity and privacy protection — Information security controls based on ISO/IEC 27002 for cloud services"
    publisher: ISO
    url: https://www.iso.org/standard/27017
    type: standards-body
    accessed: 2026-11-20
  - id: s2
    title: "ISO/IEC 27017:2026"
    publisher: IEC Webstore
    url: https://webstore.iec.ch/en/publication/115400
    type: standards-body
    accessed: 2026-11-20
  - id: s3
    title: "ISO/IEC 27017:2026 preview (foreword, introduction and contents)"
    publisher: ANSI Webstore
    url: https://webstore.ansi.org/preview-pages/ISO/preview_ISO+IEC+27017-2026.pdf
    type: standards-body
    accessed: 2026-11-20
  - id: s4
    title: "ISO 27017 — Salesforce Compliance"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/iso-27017
    type: official-docs
    accessed: 2026-11-20
  - id: s5
    title: "General (not service specific) — Salesforce Compliance"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/services/general
    type: official-docs
    accessed: 2026-11-20
  - id: s6
    title: "ISO 27017: Security Controls for Cloud Services"
    publisher: NQA
    url: https://www.nqa.com/en-us/informationsecurity/iso-27017
    type: partner
    accessed: 2026-11-20
created: 2026-11-20
---

# ISO/IEC 27017

ISO/IEC 27017 is the international code of practice for information security in cloud services. It takes the general control catalog of ISO/IEC 27002 and adds two things: extra implementation guidance for the 27002 controls that matter in the cloud, and a small set of additional cloud-specific controls with their own guidance.[^s1][^s2] Unlike many security standards, it is written for both sides of the relationship: the cloud service provider (CSP) and the cloud service customer (CSC).[^s2] For Salesforce practitioners it is the standard that most directly describes who secures what on a multitenant cloud, and it appears in vendor questionnaires next to ISO/IEC 27001 and 27018.[^s4][^s5]

## Editions

The current edition is ISO/IEC 27017:2026, the second edition, published in July 2026 (the IEC Webstore dates it 27 July 2026) by the joint committee ISO/IEC JTC 1/SC 27; it runs to 39 pages.[^s1][^s2] It was prepared together with ITU-T, which publishes the same text as Recommendation ITU-T X.1631.[^s3] The second edition cancels and replaces the first edition, ISO/IEC 27017:2015 (also published as ITU-T X.1631:2015), which was technically revised.[^s3] Its title now follows the newer family naming, "Information security, cybersecurity and privacy protection", and it is labeled a horizontal document applicable to every cloud deployment model, including private cloud.[^s2][^s3]

The revision realigns the standard with ISO/IEC 27002:2022. It adopts that edition's simple taxonomy with control attributes, merges some controls, removes others and introduces several new ones; Annex A maps the 2026 clauses back to the 2015 edition so teams can update older control matrices.[^s3] The ISO page stresses that controls should be selected on the basis of a risk assessment rather than applied wholesale.[^s1]

## Cloud-specific controls

Cloud-specific additions are marked "CLD" and slot into the 27002:2022 numbering. The 2026 table of contents lists four:[^s3]

- **5.38 Shared roles and responsibilities** within a cloud computing environment, allocated between CSP and CSC.[^s3]
- **5.39 Agreement on roles and responsibilities of the cloud service partner**, for third parties in the chain.[^s3]
- **8.35 Segregation in virtual computing environments**, keeping one tenant's environment apart from others.[^s3]
- **8.36 Detection and prevention of unauthorized use of cloud services**.[^s3]

A separate Annex B covers monitoring of cloud services.[^s3] Under the 2015 edition, certification bodies described the cloud topics as shared roles, removal or return of customer assets at contract end, virtual-environment segregation, virtual machine hardening, documented administrator procedures, customer monitoring of cloud activity, and aligning virtual and physical network security.[^s6] Some of those topics no longer appear as separate CLD controls in the 2026 contents, so check Annex A before reusing a 2015-based checklist.[^s3]

## Certification and Salesforce

ISO/IEC 27017 builds on 27001 and 27002, and certification bodies audit it on that foundation: an initial two-stage audit, a three-year certificate and annual surveillance audits.[^s6] Salesforce describes 27017 as guidance on the information security aspects of cloud computing that supplements 27002 and 27001.[^s4] Its compliance site lists an ISO/IEC 27017:2015 certificate for corporate services, alongside ISO/IEC 27001:2022 and ISO/IEC 27018:2019 certificates, with infrastructure scope covering first-party data centers, AWS and Hyperforce.[^s5] The 27017-specific page also lists an AWS-only document, so match each document to the infrastructure your org actually runs on.[^s4]

## Gotchas for architects

- **Edition mismatch.** Salesforce's listed certificate is against the 2015 edition while the 2026 edition is now current; ask which edition a vendor's certificate cites.[^s3][^s5]
- **Not a standalone ISMS.** 27017 assumes a 27001 management system; its controls extend that scope rather than replace it.[^s4][^s6]
- **Customer duties remain.** The CSC guidance means a certified provider does not discharge the customer's own controls, such as access management in the org.[^s2][^s3]
- **Privacy is a different standard.** Protection of personal data in public clouds is the subject of 27018, a separate certificate.[^s5]

## Connections

ISO/IEC 27017 sits under security compliance frameworks (`kt:security-compliance-frameworks`). It `dependsOn` ISO/IEC 27002 (`kt:iso-iec-27002`), whose controls it extends, and is `consumedBy` ISO/IEC 27001 (`kt:iso-iec-27001`), the certifiable ISMS within which its controls are audited.[^s1][^s4][^s6] Its shared-roles control is the standards-body form of the shared responsibility model (`kt:shared-responsibility-model`), and its virtual-segregation control speaks to multitenancy (`kt:multitenancy`).[^s3] Salesforce's certificate scope includes Hyperforce (`kt:hyperforce`) and pairs it with ISO/IEC 27018 (`kt:iso-iec-27018`), the companion standard for personal data in the cloud.[^s5]

## Sources
[^s1]: ISO, "ISO/IEC 27017:2026 Information security, cybersecurity and privacy protection — Information security controls based on ISO/IEC 27002 for cloud services". https://www.iso.org/standard/27017 (accessed 2026-11-20)
[^s2]: IEC Webstore, "ISO/IEC 27017:2026". https://webstore.iec.ch/en/publication/115400 (accessed 2026-11-20)
[^s3]: ANSI Webstore, "ISO/IEC 27017:2026 preview (foreword, introduction and contents)". https://webstore.ansi.org/preview-pages/ISO/preview_ISO+IEC+27017-2026.pdf (accessed 2026-11-20)
[^s4]: Salesforce, "ISO 27017 — Salesforce Compliance". https://compliance.salesforce.com/en/iso-27017 (accessed 2026-11-20)
[^s5]: Salesforce, "General (not service specific) — Salesforce Compliance". https://compliance.salesforce.com/en/services/general (accessed 2026-11-20)
[^s6]: NQA, "ISO 27017: Security Controls for Cloud Services". https://www.nqa.com/en-us/informationsecurity/iso-27017 (accessed 2026-11-20)
