---
id: kt:gdpr-international-transfers
type: ExternalConcept
title: GDPR International Data Transfers
aliases: [GDPR Chapter V, GDPR cross-border transfers, EU data transfer mechanisms, third-country transfers, Schrems II transfers]
domain: public-sector-and-compliance
summary: >-
  The rules in Chapter V of the EU General Data Protection Regulation that govern moving personal data from the EEA
  to a third country or international organisation, which is lawful only under an adequacy decision, an appropriate
  safeguard such as standard contractual clauses or binding corporate rules, or a narrow derogation.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks, kt:data-governance]
related: [kt:data-sovereignty, kt:hyperforce, kt:hyperforce-operating-zones, kt:shield-platform-encryption, kt:shared-responsibility-model]
relations:
  - {predicate: contrastsWith, object: kt:data-residency}
sources:
  - id: s1
    title: "International data transfers (Data Protection Guide for Small Business)"
    publisher: European Data Protection Board
    url: https://www.edpb.europa.eu/sme/be-compliant/international-data-transfers_en
    type: government
    accessed: 2026-11-12
  - id: s2
    title: "Transfers of Personal Data to Third Countries or International Organisations"
    publisher: Data Protection Commission (Ireland)
    url: https://dataprotection.ie/en/organisations/international-transfers/transfers-personal-data-third-countries-or-international-organisations
    type: government
    accessed: 2026-11-12
  - id: s3
    title: "Adequacy decisions"
    publisher: European Commission
    url: https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_lv
    type: government
    accessed: 2026-11-12
  - id: s4
    title: "EU Data Transfer Mechanisms FAQ"
    publisher: Salesforce
    url: https://www.salesforce.com/CONTENT/DAM/WEB/EN_US/WWW/DOCUMENTS/LEGAL/AGREEMENTS/EU-DATA-TRANSFER-MECHANISMS-FAQ.PDF
    type: official-docs
    accessed: 2026-11-12
  - id: s5
    title: "Salesforce BCRs — Salesforce Compliance"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/categories/salesforce-bcrs
    type: official-docs
    accessed: 2026-11-12
  - id: s6
    title: "European General Court dismisses Latombe challenge, upholds EU-US Data Privacy Framework"
    publisher: IAPP
    url: https://iapp.org/news/a/european-general-court-dismisses-latombe-challenge-upholds-eu-us-data-privacy-framework
    type: news
    accessed: 2026-11-12
created: 2026-11-12
---

# GDPR International Data Transfers

Chapter V of the General Data Protection Regulation (GDPR) adds a second layer of rules whenever personal data leaves the European Economic Area (EEA). The regulation does not define "transfer", so the European Data Protection Board (EDPB) uses three cumulative tests: the sender is subject to the GDPR for that processing, it discloses or makes the data available to another organisation, and that recipient sits in a non-EEA country or is an international organisation.[^s1] Meeting Chapter V does not replace the rest of the GDPR: a legal basis, security, data minimisation and, for processors, a processing contract are still required.[^s1]

Because "making available" counts, a Salesforce org can involve transfers even when its data is stored in Europe.[^s1]

## The three routes

A transfer is lawful only through one of three doors, tried in order.[^s1][^s2]

1. **Adequacy (Article 45).** The European Commission decides that a country, territory, sector or international organisation offers essentially equivalent protection; data then flows as if within the EU.[^s1][^s3]
2. **Appropriate safeguards (Articles 46–47).** Without adequacy, the exporter relies on a tool such as standard contractual clauses or binding corporate rules.[^s1][^s2]
3. **Derogations (Article 49).** Narrow exceptions such as explicit consent, contract necessity or legal claims, meant for occasional use and never as routine.[^s1][^s2]

Adequacy is adopted in four steps: a Commission proposal, an EDPB opinion, approval by representatives of the EU countries, and Commission adoption, followed by periodic review.[^s3] The Commission's list includes the UK, Switzerland, Japan, the Republic of Korea and Brazil, and covers the United States only for commercial organisations certified under the EU-US Data Privacy Framework (DPF), whose decision dates from 10 July 2023.[^s3] Recent activity shows the list is live: the UK decisions were renewed in December 2025 and mutual EU-Brazil decisions were adopted in January 2026.[^s3]

## Safeguards, Schrems II and transfer impact assessments

The **standard contractual clauses (SCCs)** adopted on 4 June 2021 come in four modules, covering controller-to-controller, controller-to-processor, processor-to-processor and processor-to-controller transfers.[^s1] Individuals can enforce them as third-party beneficiaries.[^s2] **Binding corporate rules (BCRs)** are group-wide policies approved by a data protection authority, in separate controller and processor forms, suited to multinationals with many intra-group flows.[^s1][^s2] Codes of conduct, certification and authority-approved ad hoc clauses complete the Article 46 toolbox.[^s1]

The CJEU's *Schrems II* judgment (C-311/18, 2020) added a duty to check, case by case, whether the destination country's law or practice, such as government access powers, undermines the safeguard, and to add supplementary measures or suspend the transfer if it does.[^s1][^s2] For SCC-based transfers this assessment is documented as a **transfer impact assessment (TIA)**.[^s1]

The DPF itself has survived its first court test: on 3 September 2025 the EU General Court dismissed Philippe Latombe's annulment action and confirmed the 2023 adequacy decision, although the ruling can be appealed to the Court of Justice and privacy groups signalled further challenges.[^s6]

## How Salesforce handles it

Salesforce documents several mechanisms, each of which it describes as sufficient on its own for transfers out of the EEA or UK.[^s4]

- **Processor BCRs:** an EU Processor BCR approved in 2015 and a UK Processor BCR approved by the ICO in 2023.[^s5]
- **BCR scope:** both cover Salesforce Services, Data Cloud, Agentforce, Heroku, MuleSoft, Slack, Tableau Cloud and Marketing Cloud, including Hyperforce infrastructure.[^s5]
- **SCCs:** the 2021 clauses apply to all services, with the UK addendum for UK transfers; both BCRs and SCCs are built into the Data Processing Addendum.[^s4]
- **DPF certification:** Salesforce certified to the EU-US DPF in July 2023, plus the Swiss-US DPF and the UK Extension.[^s4]

Salesforce's FAQ notes that EU exporters relying on SCCs or BCRs for US transfers must still run a TIA, while DPF-based transfers need none; it points to encryption and transparency reports as supplementary measures.[^s4]

## Gotchas for architects

Choosing an EU Hyperforce region is a residency decision, not a transfer analysis: remote access, sub-processors and support from outside the EEA can still be transfers under the EDPB's definition.[^s1] Transfer mechanisms are also a shared responsibility. Salesforce supplies the contractual and certified tools, but the customer as exporter keeps the TIA duty and must confirm that the adequacy decisions it relies on remain in force.[^s1][^s4] Finally, Article 49 derogations are not a fallback for systematic CRM replication; regulators treat them as exceptional.[^s1]

## Connections

Chapter V is one of the regimes grouped under security compliance frameworks (`kt:security-compliance-frameworks`) and a pillar of data governance (`kt:data-governance`) for EU personal data.[^s1] It `contrastsWith` data residency (`kt:data-residency`): residency is where data is stored, while transfer rules ask who can access it from which country.[^s1] It overlaps with data sovereignty (`kt:data-sovereignty`), because *Schrems II* turned foreign government access into a transfer question.[^s2] Hyperforce (`kt:hyperforce`) is the infrastructure Salesforce's BCRs list for most services, and Hyperforce Operating Zones (`kt:hyperforce-operating-zones`) are a related location control that still leaves the transfer analysis to be done; Shield Platform Encryption (`kt:shield-platform-encryption`) is the kind of encryption measure the Salesforce FAQ names as supplementary, and the shared responsibility model (`kt:shared-responsibility-model`) explains why the TIA stays with the customer.[^s4][^s5]

## Sources
[^s1]: European Data Protection Board, "International data transfers". https://www.edpb.europa.eu/sme/be-compliant/international-data-transfers_en (accessed 2026-11-12)
[^s2]: Data Protection Commission (Ireland), "Transfers of Personal Data to Third Countries or International Organisations". https://dataprotection.ie/en/organisations/international-transfers/transfers-personal-data-third-countries-or-international-organisations (accessed 2026-11-12)
[^s3]: European Commission, "Adequacy decisions". https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_lv (accessed 2026-11-12)
[^s4]: Salesforce, "EU Data Transfer Mechanisms FAQ". https://www.salesforce.com/CONTENT/DAM/WEB/EN_US/WWW/DOCUMENTS/LEGAL/AGREEMENTS/EU-DATA-TRANSFER-MECHANISMS-FAQ.PDF (accessed 2026-11-12)
[^s5]: Salesforce, "Salesforce BCRs". https://compliance.salesforce.com/en/categories/salesforce-bcrs (accessed 2026-11-12)
[^s6]: IAPP, "European General Court dismisses Latombe challenge, upholds EU-US Data Privacy Framework". https://iapp.org/news/a/european-general-court-dismisses-latombe-challenge-upholds-eu-us-data-privacy-framework (accessed 2026-11-12)
