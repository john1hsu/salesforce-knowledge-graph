---
id: kt:data-residency
type: Concept
title: Data Residency
aliases: [Hyperforce data residency, data localization, in-country data storage, Salesforce data residency]
domain: public-sector-and-compliance
summary: >-
  The requirement or commitment that customer data be stored (and sometimes processed and supported) within a
  particular country or region; in Salesforce it is delivered mainly by choosing a Hyperforce country, optionally
  strengthened by the paid Hyperforce Operating Zone offering.
release: "Winter '27"
status: concept
broader: [kt:data-architecture]
related: [kt:hyperforce, kt:government-cloud-plus, kt:il4-and-il5, kt:multitenancy, kt:gdpr-international-transfers]
relations:
  - {predicate: dependsOn, object: kt:hyperforce}
  - {predicate: requiresLicense, object: kt:hyperforce-operating-zones}
  - {predicate: contrastsWith, object: kt:data-sovereignty}
sources:
  - id: s1
    title: "Hyperforce Data Residency"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000795008&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-02
  - id: s2
    title: "Hyperforce OZ - General Information and FAQ"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000395407&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-02
  - id: s3
    title: "Salesforce Infrastructure & Sub-processors Documentation"
    publisher: Salesforce Compliance
    url: https://compliance.salesforce.com/documents/a00Kd00000z7FAnIAM
    type: official-docs
    accessed: 2026-11-02
  - id: s4
    title: "Transfers of Personal Data to Third Countries or International Organisations"
    publisher: Data Protection Commission (Ireland)
    url: https://dataprotection.ie/en/organisations/international-transfers/transfers-personal-data-third-countries-or-international-organisations
    type: government
    accessed: 2026-11-02
  - id: s5
    title: "Salesforce Launches Hyperforce EU Operating Zone to Give Customers More Control of Their Data"
    publisher: Salesforce Newsroom
    url: https://www.salesforce.com/news/press-releases/2023/03/02/hyperforce-eu-operating-zone-news/
    type: news
    accessed: 2026-11-02
created: 2026-11-02
---

# Data Residency

**Data residency** means keeping customer data in a chosen country or region. Customers usually want this to meet a regulation, a contract term or an internal risk policy. On Salesforce, residency is mainly a hosting choice: under Hyperforce, customer data is generally stored in the country where the org is located, as long as the services the customer uses are available on Hyperforce in that country.[^s1] For stricter needs, Salesforce sells the Hyperforce Operating Zone (HF OZ). It adds limits on transfers and in-region support on top of local storage.[^s2]

## How it works

**Local storage.** Salesforce defines local storage as customer data held *at rest* in the org's country, which Salesforce will not relocate.[^s1] The help article lists Hyperforce on AWS as available for Salesforce Platform–based products in Australia, Brazil, Canada, France, Germany, India, Indonesia, Israel, Italy, Japan, Singapore, South Africa, South Korea, Sweden, Switzerland, the UAE, the UK and the US. It also describes a Hyperforce-on-GCP footprint as planned for the US in November 2026 and the EU in Q1 2027. Salesforce labels that roadmap informational and not a binding commitment.[^s1]

**Operating Zones.** HF OZ combines Hyperforce hosting with customer and technical support staffed by in-region personnel around the clock. Salesforce-initiated transfers of Customer Data out of the region are restricted, with any exceptions written into the contract. It runs only on Hyperforce on AWS.[^s2] The EU zone covers all 27 member states as one zone, so customers can't choose a specific EU country. A separate Switzerland zone keeps data in Switzerland but is supported by EU-based staff.[^s2] Salesforce launched the EU Operating Zone in March 2023 and promoted EU-based support as a key feature.[^s5]

**Per-service truth.** Where any given service actually stores and processes data is set out in Salesforce's Infrastructure & Sub-processors (I&S) documentation. It describes each service's infrastructure, its sub-processors and the countries where customer data is stored and processed. Several services appear in both a first-party and a Hyperforce variant.[^s3]

## Limits and gotchas

- **Residency is not "nothing ever leaves."** Even on Hyperforce, some customer data may be stored or accessed outside the country for support and to run the services. Non-customer data, such as Salesforce controller data, can leave the country. Salesforce also doesn't stop customers from moving their own data, for example through integrations.[^s1]
- **Product coverage varies.** Some products have components hosted in other countries, depend on services not yet on Hyperforce, or run on a different Hyperforce substrate. Any of these can change where data lives. Not every product is offered in every country.[^s1]
- **OZ removes features.** OZ covers Sales, Service, Analytics, Platform, Financial Services, Healthcare and Life Sciences, and Experience Cloud. Some features are unavailable in OZ, including MySearch, Chatbot and some Einstein features. OZ SKUs also have some licenses removed.[^s2]
- **Residency is not sovereignty.** Salesforce's OZ FAQ says the offering does not resolve every issue raised by Schrems II. U.S. government access, for example under the CLOUD Act, remains possible and would count as a transfer under EU law. Salesforce tells customers to confirm fit with their own counsel.[^s2]

## When to use it (and when not)

Choose a Hyperforce country when a regulator, customer contract or policy requires data to be stored at rest in a specific jurisdiction. Before committing, check the I&S documentation for every service in scope, including add-ons and AI features.[^s1][^s3] Add an Operating Zone only when you also need in-region support personnel and contractual limits on transfers, and when the features it removes are acceptable.[^s2] For EU personal data, keep in mind that the GDPR controls *transfers*, not storage location as such. Exports outside the EEA need an adequacy decision or safeguards such as Standard Contractual Clauses or Binding Corporate Rules. After the CJEU's Schrems judgment, exporters must also assess whether supplementary measures are needed.[^s4] Residency is one way to reduce that transfer analysis, not a replacement for it.

## Connections

Data residency **depends on Hyperforce** (`kt:hyperforce`), the infrastructure that lets customers pick a hosting country, and it is a cross-cutting concern within **data architecture** (`kt:data-architecture`).[^s1] Its stricter form **requires the Hyperforce Operating Zones** offering (`kt:hyperforce-operating-zones`).[^s2] It **contrasts with data sovereignty** (`kt:data-sovereignty`), which is about which laws can reach the data, a gap the OZ FAQ itself acknowledges.[^s2] For EU data it is closely related to the **GDPR's international-transfer rules** (`kt:gdpr-international-transfers`).[^s4] It relates to **Government Cloud Plus** (`kt:government-cloud-plus`) and **DoD Impact Levels 4 and 5** (`kt:il4-and-il5`), US public-sector offerings whose authorizations add their own location requirements. It also relates to **multitenancy** (`kt:multitenancy`), because shared, globally operated services are where residency exceptions arise.[^s1][^s3]

## Sources
[^s1]: Salesforce Help, "Hyperforce Data Residency". https://help.salesforce.com/s/articleView?id=000795008&language=en_US&type=1 (accessed 2026-11-02)
[^s2]: Salesforce Help, "Hyperforce OZ - General Information and FAQ". https://help.salesforce.com/s/articleView?id=000395407&language=en_US&type=1 (accessed 2026-11-02)
[^s3]: Salesforce Compliance, "Salesforce Infrastructure & Sub-processors Documentation". https://compliance.salesforce.com/documents/a00Kd00000z7FAnIAM (accessed 2026-11-02)
[^s4]: Data Protection Commission (Ireland), "Transfers of Personal Data to Third Countries or International Organisations". https://dataprotection.ie/en/organisations/international-transfers/transfers-personal-data-third-countries-or-international-organisations (accessed 2026-11-02)
[^s5]: Salesforce Newsroom, "Salesforce Launches Hyperforce EU Operating Zone to Give Customers More Control of Their Data". https://www.salesforce.com/news/press-releases/2023/03/02/hyperforce-eu-operating-zone-news/ (accessed 2026-11-02)
