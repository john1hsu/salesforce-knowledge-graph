---
id: kt:hyperforce-operating-zones
type: Product
title: Hyperforce Operating Zones
aliases: [Hyperforce Operating Zone, HF OZ, Hyperforce OZ, EU Operating Zone, Hyperforce EU Operating Zone, Switzerland Operating Zone]
domain: platform-architecture
summary: >-
  A paid Hyperforce offering, currently available for the EU and Switzerland, that runs a vetted set of Salesforce
  products on Hyperforce on AWS inside a regional boundary, restricts Salesforce-initiated transfers of customer data
  out of that boundary, and supplies 24/7 support from in-region personnel.
release: "Winter '27"
status: current
broader: [kt:hyperforce]
related: [kt:data-sovereignty, kt:gdpr-international-transfers, kt:salesforce-shield, kt:custom-domains]
relations:
  - {predicate: enables, object: kt:data-residency}
  - {predicate: integratesWith, object: kt:salesforce-shield}
  - {predicate: contrastsWith, object: kt:government-cloud-plus}
sources:
  - id: s1
    title: "Hyperforce OZ - General Information and FAQ"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000395407&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-12
  - id: s2
    title: "Hyperforce Security, Privacy and Architecture"
    publisher: Salesforce
    url: https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/misc/hyperforce-security-privacy-and-architecture.pdf
    type: official-docs
    accessed: 2026-11-12
  - id: s3
    title: "Salesforce Infrastructure and Sub-processors"
    publisher: Salesforce
    url: https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/misc/salesforce-infrastructure-and-subprocessors.pdf
    type: official-docs
    accessed: 2026-11-12
  - id: s4
    title: "Hyperforce Operating Zone (Hyperforce: European Union Public Cloud Infrastructure)"
    publisher: Salesforce
    url: https://salesforce.com/eu/platform/public-cloud-infrastructure/operating-zone?bc=OTH
    type: official-blog
    accessed: 2026-11-12
created: 2026-11-12
---

# Hyperforce Operating Zones

A **Hyperforce Operating Zone (HF OZ)** is a regional boundary layered on top of Hyperforce. Inside it, a selected set of Salesforce products runs on Hyperforce, and customer and technical support comes from staff located in the same region. The goal is stronger data residency and privacy commitments than a plain Hyperforce country choice gives.[^s1] Salesforce introduced the operating-zone idea in 2021 as a set of technology and personnel standards applied within a geographic boundary. For HF OZ, that boundary is about where customer data is stored and processed.[^s1][^s4] The offering was formerly called the EU Operating Zone.[^s2]

## How it works

**Zones.** HF OZ exists only for the European Union and Switzerland, and only on Hyperforce running on AWS.[^s1] In the EU zone, customer data is stored, processed and accessed across the 27 member states as a single zone. Neither customers nor partners can pin storage, processing or support to one EU country.[^s1] In the Switzerland zone, data is stored, processed and accessed in Switzerland, but the support and technical operations staff are EU-based.[^s1] Customers outside EMEA may buy HF OZ too; their data then lives in the zone's region rather than at home.[^s1][^s4]

**Hosting.** Salesforce's sub-processor document lists Amazon Web Services as the HF OZ hosting sub-processor, with Germany and Switzerland as locations. New customers choose one of those countries at signup. Customers who joined the EU Operating Zone before December 17, 2024 have their data stored in Germany, and data may also be processed elsewhere in the EU.[^s3]

**Product vetting and SKUs.** A product must already run on Hyperforce, and Salesforce checks every underlying feature to confirm it does not touch customer data outside the zone.[^s1] The approved set spans Sales, Service, Analytics, Platform, Financial Services, Healthcare and Life Sciences, and Experience Cloud.[^s1] Salesforce sells these through OZ-specific SKUs. Because those SKUs block features that move data out of the region, some licenses were dropped from them.[^s1]

**Support.** HF OZ includes round-the-clock customer and engineering support from in-region personnel.[^s1] Support staff can enter a customer's org only when the customer grants access.[^s2] An HF OZ Premier Success Plan adds coaching and 24x7 local-language support with faster response times.[^s4]

## Limits and gotchas

- **Missing features.** MySearch, Chatbot and some Einstein features are not part of the OZ products, so check license parity before buying.[^s1]
- **Defined exceptions to the boundary.** Data can leave the zone for availability monitoring of an org's configuration copy, incident response, and data a customer hands over in a support case.[^s2]
- **More exceptions.** Support collaboration in encrypted private Slack channels, CDN caching that a customer asks to enable, and legally binding disclosure requests can also process data outside the zone.[^s2]
- **Administrative data in the US.** Setup metadata, such as object names, URLs and custom Apex code, plus search queries (not results) is stored in the United States.[^s2]
- **Custom domain keys.** Private keys a customer supplies for custom domains may be stored in the US, encrypted first with key management systems inside the zone.[^s2]
- **Not a legal shield.** Salesforce states that HF OZ does not settle every issue raised by Schrems II, and local storage does not take data outside the reach of the US CLOUD Act.[^s1]

## When to use it (and when not)

Choose HF OZ when an EU or Swiss organization needs more than storage at rest in a country: contractual limits on Salesforce-initiated transfers and support staff who sit inside the region.[^s1] Pair it with Shield, Event Monitoring and Field Audit Trail when you also need encryption key control and evidence of who accessed data; Salesforce markets those as complements.[^s4] Skip it when the products you need are outside the vetted set, when a missing feature is essential, or when you need a specific EU country, which only a standard Hyperforce country choice can offer.[^s1]

## Connections

HF OZ is a **narrower offering within Hyperforce** (`kt:hyperforce`), and it is the paid option that **enables** the stricter form of **data residency** (`kt:data-residency`).[^s1] It supports, but does not by itself achieve, **data sovereignty** (`kt:data-sovereignty`), since foreign legal access remains possible.[^s1] It is relevant to **GDPR international transfers** (`kt:gdpr-international-transfers`) because it restricts Salesforce-initiated exports.[^s2] It **integrates with Salesforce Shield** (`kt:salesforce-shield`), whose encryption lets customers hold key material outside Salesforce.[^s2][^s4] Its handling of keys for **custom domains** (`kt:custom-domains`) is one of the documented exceptions.[^s2] It **contrasts with Government Cloud Plus** (`kt:government-cloud-plus`): HF OZ is a commercial residency and support boundary offered only for the EU and Switzerland.[^s1]

## Sources
[^s1]: Salesforce Help, "Hyperforce OZ - General Information and FAQ". https://help.salesforce.com/s/articleView?id=000395407&language=en_US&type=1 (accessed 2026-11-12)
[^s2]: Salesforce, "Hyperforce Security, Privacy and Architecture". https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/misc/hyperforce-security-privacy-and-architecture.pdf (accessed 2026-11-12)
[^s3]: Salesforce, "Salesforce Infrastructure and Sub-processors". https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/misc/salesforce-infrastructure-and-subprocessors.pdf (accessed 2026-11-12)
[^s4]: Salesforce, "Hyperforce Operating Zone (Hyperforce: European Union Public Cloud Infrastructure)". https://salesforce.com/eu/platform/public-cloud-infrastructure/operating-zone?bc=OTH (accessed 2026-11-12)
