---
id: kt:pci-dss
type: ExternalConcept
title: PCI DSS
aliases: [Payment Card Industry Data Security Standard, PCI compliance, PCI DSS v4.0.1, PCI Attestation of Compliance, Salesforce PCI AoC]
domain: public-sector-and-compliance
summary: >-
  The card-industry security baseline, maintained by the PCI Security Standards Council, for every entity that stores,
  processes or transmits cardholder data; Salesforce publishes QSA-issued Attestations of Compliance per service, but
  what an org does with card data stays the customer's responsibility.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:hyperforce, kt:commerce-cloud, kt:data-cloud, kt:heroku, kt:classic-encryption, kt:named-credentials]
relations:
  - {predicate: mitigates, object: kt:data-breach-risk}
  - {predicate: dependsOn, object: kt:shared-responsibility-model}
  - {predicate: dependsOn, object: kt:data-classification}
  - {predicate: contrastsWith, object: kt:hipaa}
sources:
  - id: s1
    title: "PCI DSS (Salesforce Compliance Site)"
    publisher: Salesforce
    url: https://compliance.salesforce.com/jp/pci-dss
    type: official-docs
    accessed: 2026-11-26
  - id: s2
    title: "PCI Attestation of Compliance (AoC) - Salesforce Services on Hyperforce"
    publisher: Salesforce
    url: https://compliance.salesforce.com/documents/a005A00000vvhbPQAQ
    type: official-docs
    accessed: 2026-11-26
  - id: s3
    title: "Storing Sensitive Data (Secure Coding Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/secure-coding/guide/secure-coding-storing-sensitive-data.html
    type: official-docs
    accessed: 2026-11-26
  - id: s4
    title: "PCI Data Security Standard (PCI DSS)"
    publisher: PCI Security Standards Council
    url: https://www.pcisecuritystandards.org/standards/pci-dss/
    type: standards-body
    accessed: 2026-11-26
  - id: s5
    title: "Just Published: PCI DSS v4.0.1"
    publisher: PCI Security Standards Council
    url: https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1
    type: standards-body
    accessed: 2026-11-26
created: 2026-11-26
---

# PCI DSS

The Payment Card Industry Data Security Standard (PCI DSS) is the security baseline the card industry sets for anyone who handles payment account data. The PCI Security Standards Council describes it as a set of technical and operational requirements designed to protect that data.[^s4] Its scope is defined by data, not by company type: it targets entities that store, process or transmit cardholder data (CHD) or sensitive authentication data (SAD), which includes merchants, processors, acquirers, issuers and service providers.[^s4] Salesforce's own compliance site frames it the same way, as an industry information-security standard for organizations handling payment card data from the major brands, Visa, Mastercard, American Express, Discover and JCB.[^s1]

Unlike a law such as HIPAA (`kt:hipaa`), PCI DSS is an industry standard. The Council writes it, but whether a given organization must comply, and how it must validate, is decided by whoever runs the compliance program: a payment brand, an acquirer or a similar entity.[^s4]

## Current version

PCI DSS v4.0.1 was published in June 2024 as a limited revision of v4.0. It fixed formatting and typographical errors and clarified guidance, and the Council states that it neither added nor removed requirements.[^s5] Notable clarifications include restoring the earlier rule that the 30-day patching expectation applies only to critical vulnerabilities, a note on phishing-resistant factors in the multi-factor authentication requirement, and clearer wording on relationships between customers and third-party service providers.[^s5] Version 4.0 was retired on 31 December 2024, leaving v4.0.1 as the only active version. The revision did not move the 31 March 2025 effective date for the requirements v4.0 had future-dated.[^s5]

## How Salesforce evidences PCI DSS

Salesforce does not claim that "Salesforce is PCI compliant" as a single statement. Instead, a Qualified Security Assessor (QSA) assesses its systems and processes every year and issues an Attestation of Compliance (AoC), and the compliance site publishes separate AoCs per service footprint.[^s1] The listing covers, among others, core Salesforce Services on first-party infrastructure and on Hyperforce, Data Cloud together with the Einstein Platform and Agentforce, Heroku, MuleSoft, Commerce Cloud and Government Cloud Plus, along with Approved Scanning Vendor network scan reports.[^s1] The Hyperforce AoC page, for example, names Agentforce and Einstein Platform, Data Cloud and the core Salesforce Services in its scope. The page shows a reporting period starting in December 2025, and the attestation itself requires a login to download.[^s2] The practical consequence for an architect: check the AoC for the exact service and infrastructure the cardholder data will touch, and read its responsibility matrix, which the site publishes alongside the Hyperforce AoC.[^s1]

## Customer responsibilities and gotchas

An AoC covers Salesforce's side of the line, not the customer's configuration or code. Salesforce's Secure Coding Guide lists credit card numbers among the sensitive data that needs extra care and notes that standards such as PCI require special steps when collecting it.[^s3] The guide's storage advice is specific:

- Classic encrypted custom fields use AES with 128-bit keys and are suitable for data such as card information, but not for authentication secrets.[^s3]
- Named Credentials are meant for authentication data, and the guide advises against putting credit card information in them.[^s3]
- When Apex `Crypto` is used, keys must be generated randomly and kept in a protected custom setting or protected custom metadata type.[^s3]

Because PCI DSS scope follows wherever cardholder data is stored, processed or transmitted, the simplest way to shrink it is usually not to store card data in the org at all. Instead, use a payment gateway's tokens and keep only references in Salesforce.[^s4] Data classification is what makes this enforceable: fields tagged as payment data can be audited, masked in sandboxes and excluded from integrations. Teams that copy production data to sandboxes should treat those copies as in scope too, since they also store the data.[^s4]

## Connections

PCI DSS is one of the industry frameworks grouped under security compliance frameworks (`kt:security-compliance-frameworks`) and, like them, mitigates data breach risk (`kt:data-breach-risk`). Its evidence model depends on the the shared responsibility model (`kt:shared-responsibility-model`): Salesforce attests per service, including Hyperforce (`kt:hyperforce`), Data Cloud (`kt:data-cloud`), Heroku (`kt:heroku`) and Commerce Cloud (`kt:commerce-cloud`), while customers own field design, encryption choices such as Classic Encryption (`kt:classic-encryption`) and secret handling via Named Credentials (`kt:named-credentials`).[^s1][^s3] It contrasts with HIPAA (`kt:hipaa`), which is a statute, whereas PCI DSS is an industry standard enforced through payment brands and acquirers.[^s4] It depends on data classification (`kt:data-classification`) to locate cardholder data in the first place.

## Sources
[^s1]: Salesforce, "PCI DSS (Salesforce Compliance Site)". https://compliance.salesforce.com/jp/pci-dss (accessed 2026-11-26)
[^s2]: Salesforce, "PCI Attestation of Compliance (AoC) - Salesforce Services on Hyperforce". https://compliance.salesforce.com/documents/a005A00000vvhbPQAQ (accessed 2026-11-26)
[^s3]: Salesforce, "Storing Sensitive Data (Secure Coding Guide)". https://developer.salesforce.com/docs/platform/secure-coding/guide/secure-coding-storing-sensitive-data.html (accessed 2026-11-26)
[^s4]: PCI Security Standards Council, "PCI Data Security Standard (PCI DSS)". https://www.pcisecuritystandards.org/standards/pci-dss/ (accessed 2026-11-26)
[^s5]: PCI Security Standards Council, "Just Published: PCI DSS v4.0.1". https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1 (accessed 2026-11-26)
