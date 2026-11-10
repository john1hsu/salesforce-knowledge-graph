---
id: kt:security-compliance-frameworks
type: Concept
title: Security Compliance Frameworks
aliases: [compliance frameworks, security frameworks, regulatory frameworks, Salesforce compliance certifications and attestations]
domain: public-sector-and-compliance
summary: >-
  The family of standards, regulations and audit schemes (NIST CSF, NIST SP 800-53, ISO/IEC 27001, SOC 2, PCI DSS,
  HIPAA, FedRAMP, C5 and others) against which a Salesforce solution is assessed; Salesforce certifies the platform,
  while the customer remains responsible for keeping what it builds inside that certified posture.
release: "Winter '27"
status: concept
broader: [kt:governance-risk-and-compliance]
related: [kt:fedramp, kt:nist-sp-800-53, kt:dod-cloud-computing-srg, kt:data-residency, kt:shield-platform-encryption]
relations:
  - {predicate: hasPart, object: kt:nist-cybersecurity-framework}
  - {predicate: hasPart, object: kt:iso-iec-27001}
  - {predicate: consumedBy, object: kt:well-architected-framework}
sources:
  - id: s1
    title: "Trust (Salesforce Well-Architected guide)"
    publisher: Salesforce
    url: https://architect.salesforce.com/docs/architect/well-architected/guide/trust.html
    type: official-docs
    accessed: 2026-11-05
  - id: s2
    title: "Salesforce Compliance Site: Services"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/services
    type: official-docs
    accessed: 2026-11-05
  - id: s3
    title: "Security Perspective on the Shared Responsibility Model"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/documents/a006e000010nW2FAAU
    type: official-docs
    accessed: 2026-11-05
  - id: s4
    title: "C5 (ISAE 3000) (Salesforce Compliance Site)"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/c5-isae-3000
    type: official-docs
    accessed: 2026-11-05
  - id: s5
    title: "The NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29)"
    publisher: NIST
    url: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf
    type: standards-body
    accessed: 2026-11-05
  - id: s6
    title: "ISO/IEC 27001:2022 Information security management systems — Requirements"
    publisher: IEC Webstore
    url: https://webstore.iec.ch/publication/79694
    type: standards-body
    accessed: 2026-11-05
created: 2026-11-05
---

# Security Compliance Frameworks

Security compliance frameworks are the external yardsticks a Salesforce solution is measured against: voluntary risk frameworks, international management-system standards, independent audit attestations, industry rules and government authorization programs. Salesforce's Well-Architected Trust guide names the ones architects meet most often, including HIPAA, PCI DSS, GDPR, LGPD, CCPA/CPRA, NIST SP 800-53, SOX, HITRUST and FedRAMP, plus national laws such as India's DPDP Act and China's PIPL.[^s1] For a CTA-level design, the practical question is never "is Salesforce compliant?" but which framework applies to which data, and which half of the control set the customer owns.[^s1]

## Kinds of framework

**Outcome frameworks** describe what good looks like without prescribing controls. NIST's Cybersecurity Framework 2.0, published 26 February 2024 as CSWP 29, organizes outcomes under six Functions (Govern, Identify, Protect, Detect, Respond, Recover) and explicitly leaves the "how" to other resources.[^s5] Its Organizational Profiles describe current and target posture, and its Tiers rate the rigor of risk governance from Partial to Adaptive.[^s5]

**Control catalogs and management-system standards** are more prescriptive. ISO/IEC 27001:2022 (edition 3, published 25 October 2022) sets requirements for establishing, running and continually improving an information security management system, and an organization claiming conformity may not exclude any requirement in Clauses 4 to 10.[^s6] NIST SP 800-53 plays the equivalent role for US federal systems; CSF Informative References map its outcomes to specific 800-53 controls.[^s5]

**Authorization and attestation schemes** test a provider against a catalog. The Trust guide lists Salesforce's SOC 1/2/3 attestations, ISO 27001, 27017 and 27018 certifications, PCI DSS Level 1 validation and HIPAA-eligible services covered by Business Associate Agreements.[^s1] Germany's BSI C5 catalogue is covered by an ISAE 3000 (Revised) report on Salesforce Services.[^s4]

## How it works on Salesforce

The Salesforce Compliance site organizes certifications and audit documents by service, and many documents require a login to download.[^s2][^s3] Scope differs per service: the services directory shows separate FedRAMP package IDs for Government Cloud Plus, MuleSoft Government Cloud, Own by Salesforce, Slack and GovSlack.[^s2] The Trust guide stresses that FedRAMP authorization covers Government Cloud Plus and MuleSoft Government Cloud, not the commercial multi-tenant platform.[^s1]

Underneath every certification is shared responsibility. Salesforce acts as data processor and secures the platform; customers must review the available security capabilities and configure their org to meet their own regulatory and contractual obligations.[^s3] The Trust guide puts it bluntly: certifications reduce the compliance burden but do not remove the architect's responsibility for custom objects, code, integrations and configuration.[^s1]

## Gotchas and practitioner guidance

- **Check scope, not the logo.** A certification applies to named services and environments; confirm the specific service on the Compliance site before promising a framework to a customer.[^s2]
- **Don't hardcode regulatory figures.** Retention periods, data-subject-request deadlines and breach-notification windows vary by jurisdiction and change, so parameterize them from a maintained source.[^s1]
- **Map data tiers to controls.** Classify data, then attach controls per tier, such as Shield Platform Encryption and Field Audit Trail for restricted data, private org-wide defaults and segregation of duties for PHI and payments.[^s1]
- **Keep cardholder data out.** The guide recommends gateway tokenization so primary account numbers never land in Salesforce.[^s1]
- **Validate continuously.** Run Security Health Check regularly, stream Event Monitoring to a SIEM and add automated compliance checks to CI/CD; thin logging is a common audit failure.[^s1]

## Connections

This node groups the framework articles in the graph and sits under governance, risk and compliance (`kt:governance-risk-and-compliance`).[^s1] It `hasPart` the NIST Cybersecurity Framework (`kt:nist-cybersecurity-framework`) and ISO/IEC 27001 (`kt:iso-iec-27001`), the outcome and management-system ends of the spectrum.[^s5][^s6] NIST SP 800-53 (`kt:nist-sp-800-53`, related) supplies the control catalog that FedRAMP (`kt:fedramp`, related) assesses against, with FIPS 199 categorization choosing the baseline, while the DoD Cloud Computing SRG (`kt:dod-cloud-computing-srg`, related) is the defense counterpart.[^s1][^s5] Data residency (`kt:data-residency`, related) is the jurisdictional side of the same obligations, which the Trust guide says should be settled per data category early in design.[^s1] The Salesforce Well-Architected Framework (`kt:well-architected-framework`) `usedBy` relation reflects that its Trust pillar is where these frameworks are turned into design guidance.[^s1]

## Sources
[^s1]: Salesforce, "Trust (Salesforce Well-Architected guide)". https://architect.salesforce.com/docs/architect/well-architected/guide/trust.html (accessed 2026-11-05)
[^s2]: Salesforce, "Salesforce Compliance Site: Services". https://compliance.salesforce.com/en/services (accessed 2026-11-05)
[^s3]: Salesforce, "Security Perspective on the Shared Responsibility Model". https://compliance.salesforce.com/en/documents/a006e000010nW2FAAU (accessed 2026-11-05)
[^s4]: Salesforce, "C5 (ISAE 3000) (Salesforce Compliance Site)". https://compliance.salesforce.com/en/c5-isae-3000 (accessed 2026-11-05)
[^s5]: NIST, "The NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29)". https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf (accessed 2026-11-05)
[^s6]: IEC Webstore, "ISO/IEC 27001:2022 Information security management systems — Requirements". https://webstore.iec.ch/publication/79694 (accessed 2026-11-05)
