---
id: kt:data-sovereignty
type: Concept
title: Data Sovereignty
aliases: [digital sovereignty, cloud sovereignty, sovereign cloud]
domain: public-sector-and-compliance
summary: >-
  The principle that data, and the cloud services that process it, stay subject to the laws, jurisdiction and
  operational control of a chosen state or bloc; broader than data residency because it also covers who can
  compel access, who operates the service and who controls the encryption keys.
release: "Winter '27"
status: concept
broader: [kt:data-governance]
related: [kt:hyperforce, kt:hyperforce-operating-zones, kt:shield-platform-encryption, kt:gdpr-international-transfers, kt:government-cloud-plus]
relations:
  - {predicate: contrastsWith, object: kt:data-residency}
sources:
  - id: s1
    title: "Cloud Sovereignty Framework: Implementation guidance"
    publisher: European Commission
    url: https://commission.europa.eu/document/download/2ad80a48-166f-4c77-a513-80c53ca2a128_en
    type: government
    accessed: 2026-11-12
  - id: s2
    title: "Commission advances cloud sovereignty through strategic procurement"
    publisher: European Commission
    url: https://commission.europa.eu/news-and-media/news/commission-advances-cloud-sovereignty-through-strategic-procurement-2026-04-17_sl
    type: government
    accessed: 2026-11-12
  - id: s3
    title: "Shield Platform Encryption (Salesforce Help PDF guide)"
    publisher: Salesforce Help
    url: https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/security_shield_platform_encryption.pdf
    type: official-docs
    accessed: 2026-11-12
  - id: s4
    title: "How the EU-US Data Privacy Framework Benefits Salesforce Customer Data Transfers"
    publisher: Salesforce Newsroom
    url: https://www.salesforce.com/news/stories/salesforce-transatlantic-data-privacy-update/
    type: official-blog
    accessed: 2026-11-12
  - id: s5
    title: "Hyperforce Operating Zone (EU and Switzerland)"
    publisher: Salesforce
    url: https://www.salesforce.com/platform/data-residence-eu-oz/
    type: official-blog
    accessed: 2026-11-12
  - id: s6
    title: "MuleSoft on Hyperforce in Australia (news story)"
    publisher: Salesforce Newsroom (Australia)
    url: https://www.salesforce.com/au/news/stories/salesforce-mulesoft-hyperforce-australia-2026/
    type: news
    accessed: 2026-11-12
created: 2026-11-12
---

# Data Sovereignty

**Data sovereignty** is the idea that data, and the services that store and process it, should remain under the laws and control of a particular state or bloc. It goes further than **data residency**, which only asks where data sits at rest. A sovereignty assessment also asks which jurisdiction can compel access, who operates and supports the service, who holds the encryption keys, and how dependent the customer is on a foreign supply chain. The European Commission's Cloud Sovereignty Framework makes this explicit by scoring cloud services against eight objectives, of which data and AI sovereignty is only one.[^s1]

## How sovereignty is assessed

The Commission's framework, first presented in October 2025, defines eight sovereignty objectives: strategic, legal and jurisdictional, data and AI, operational, supply chain, technology, security and compliance, and environmental sustainability.[^s1] Each is rated on a Sovereignty Effectiveness Assurance Level (SEAL) scale from SEAL-0 (no sovereignty) through SEAL-1 (jurisdictional), SEAL-2 (data), SEAL-3 (technological) to SEAL-4 (full digital sovereignty), and a service's overall SEAL is the lowest level it reaches on any objective.[^s1]

The framework is already used as a buying criterion. In April 2026 the Commission awarded a sovereign cloud tender for EU institutions worth up to €180 million over six years, split across four providers to avoid dependence on one. Bidders needed at least SEAL-2, and the Commission reported that most awardees reached SEAL-3.[^s2] It said it would publish an updated framework based on lessons from the tender, and invited other organisations to reuse the approach.[^s2]

## Sovereignty levers in Salesforce

On Salesforce, practitioners typically combine several controls, each addressing a different objective; Salesforce itself pairs Operating Zones with Shield for key lifecycle control.[^s5]

- **Location (data and AI objective).** A Hyperforce Operating Zone processes and stores customer data in the EU and Switzerland and restricts transfers outside the zone boundary.[^s5]
- **Operations and support.** The Operating Zone is supported 24/7 by EU-based personnel, and in-region support is designed to keep access to data inside the region.[^s5]
- **Key control.** With Shield Platform Encryption, Bring Your Own Key lets the customer generate key material outside Salesforce and revoke Salesforce's access on demand.[^s3]
- **External key custody.** Cache-Only Keys keep the data encryption key in a customer-run key service that Salesforce calls through a named credential; they apply to field-level encryption only, not Database Encryption.[^s3]
- **Legal transfer basis.** For EU personal data, Salesforce relies on processor Binding Corporate Rules, Standard Contractual Clauses and the EU-US Data Privacy Framework.[^s4]

Regional deployments of other Salesforce products follow the same pattern. MuleSoft on Hyperforce in Australia, generally available from August 2026, runs its control plane, runtime plane and regional services in the country, and Salesforce marketed it to regulated sectors on local data sovereignty grounds.[^s6]

## Limits and gotchas

Residency controls do not by themselves settle the legal and jurisdictional objective. Salesforce's own account of EU transfers traces how the 2020 Schrems II ruling invalidated the Privacy Shield, and how its successor, the Data Privacy Framework (adequacy decision of July 10, 2023), rests on US Executive Order 14086 limiting surveillance and adding a redress court.[^s4] A future ruling against that framework would change the analysis regardless of where an org is hosted. Salesforce points customers to its data processing addendum commitments on challenging government access requests, and to customer-controlled key management, as complements to EU hosting.[^s4]

Key control has operational costs. Cache-Only Keys are cached and re-fetched after cache flushes, which occur at least every 72 hours, so the customer's key service becomes a dependency of the org.[^s3] BYOK uploads are rate-limited (once every 24 hours in production), and Database Encryption tenant secrets cannot be deleted once uploaded.[^s3] Operating Zones include only a vetted subset of products and features, so sovereignty requirements can rule out functionality.[^s5]

## Connections

Data sovereignty is a facet of **data governance** (`kt:data-governance`) and **contrasts with data residency** (`kt:data-residency`): residency is the location layer, while sovereignty adds jurisdiction, operations and supply chain.[^s1] In Salesforce, location and operational controls come from **Hyperforce** (`kt:hyperforce`) and its **Operating Zones** (`kt:hyperforce-operating-zones`), and key control from **Shield Platform Encryption** (`kt:shield-platform-encryption`).[^s3][^s5] For EU personal data, sovereignty debates overlap with the **GDPR's international-transfer rules** (`kt:gdpr-international-transfers`).[^s4] **Government Cloud Plus** (`kt:government-cloud-plus`) is a related US public-sector answer to the same question: an isolated environment with its own authorization boundary for government data.

## Sources

[^s1]: European Commission, "Cloud Sovereignty Framework: Implementation guidance". https://commission.europa.eu/document/download/2ad80a48-166f-4c77-a513-80c53ca2a128_en (accessed 2026-11-12)
[^s2]: European Commission, "Commission advances cloud sovereignty through strategic procurement" (April 17, 2026). https://commission.europa.eu/news-and-media/news/commission-advances-cloud-sovereignty-through-strategic-procurement-2026-04-17_sl (accessed 2026-11-12)
[^s3]: Salesforce Help, "Shield Platform Encryption (Salesforce Help PDF guide)" (PDF). https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/security_shield_platform_encryption.pdf (accessed 2026-11-12)
[^s4]: Salesforce Newsroom, "How the EU-US Data Privacy Framework Benefits Salesforce Customer Data Transfers" (July 18, 2023). https://www.salesforce.com/news/stories/salesforce-transatlantic-data-privacy-update/ (accessed 2026-11-12)
[^s5]: Salesforce, "Hyperforce Operating Zone (EU and Switzerland)". https://www.salesforce.com/platform/data-residence-eu-oz/ (accessed 2026-11-12)
[^s6]: Salesforce Newsroom (Australia), "MuleSoft on Hyperforce in Australia (news story)" (August 11, 2026). https://www.salesforce.com/au/news/stories/salesforce-mulesoft-hyperforce-australia-2026/ (accessed 2026-11-12)
