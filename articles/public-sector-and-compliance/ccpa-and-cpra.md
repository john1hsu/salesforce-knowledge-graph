---
id: kt:ccpa-and-cpra
type: ExternalConcept
title: CCPA and CPRA
aliases: [California Consumer Privacy Act, California Privacy Rights Act, CCPA, CPRA, Proposition 24, CCPA compliance on Salesforce]
domain: public-sector-and-compliance
summary: >-
  California's consumer privacy law (the CCPA), as amended by the California Privacy Rights Act (CPRA, Proposition 24),
  which gives California residents rights to know, delete, correct and opt out of the sale or sharing of their personal
  information; Salesforce acts as a service provider, while customers use tools such as Privacy Center and the consent
  data model to meet their own obligations.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:gdpr-international-transfers, kt:privacy-center, kt:consent-management-in-data-cloud, kt:data-classification, kt:salesforce-shield]
relations:
  - {predicate: contrastsWith, object: kt:hipaa}
  - {predicate: dependsOn, object: kt:shared-responsibility-model}
sources:
  - id: s1
    title: "Frequently Asked Questions (FAQs)"
    publisher: California Privacy Protection Agency
    url: https://cppa.ca.gov/faq.html
    type: government
    accessed: 2026-11-27
  - id: s2
    title: "California Consumer Privacy Act Regulations (March 2023)"
    publisher: California Privacy Protection Agency
    url: https://cppa.ca.gov/regulations/consumer_privacy_act.html
    type: government
    accessed: 2026-11-27
  - id: s3
    title: "Implement CCPA Compliance in Your Organization (California Consumer Privacy Act Basics)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/california-consumer-privacy-act-basics/implement-ccpa-compliance-in-your-organization
    type: official-learning
    accessed: 2026-11-27
  - id: s4
    title: "CCPA & CPRA Frequently Asked Questions"
    publisher: Salesforce
    url: https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/white-papers/CCPA-FAQ.pdf
    type: official-docs
    accessed: 2026-11-27
  - id: s5
    title: "Handle Privacy Requests in Privacy Center"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/privacy-center/handle-privacy-requests-in-privacy-center
    type: official-learning
    accessed: 2026-11-27
  - id: s6
    title: "Privacy Overview Data Model"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/data-models/guide/privacy-overview.html
    type: official-docs
    accessed: 2026-11-27
created: 2026-11-27
---

# CCPA and CPRA

The California Consumer Privacy Act (CCPA) is California's general consumer privacy statute. The California Privacy Rights Act (CPRA), passed by voters as Proposition 24, did not create a separate law: it amended the CCPA, and those amendments took effect on January 1, 2023. Proposition 24 also created the California Privacy Protection Agency (CPPA), a dedicated regulator governed by a five-member board that adopts regulations, promotes public awareness and enforces the law.[^s1] For Salesforce practitioners, "CCPA compliance" is a customer obligation that Salesforce supports contractually and with platform tooling, not a certification an org can switch on.[^s3][^s4]

## Who it applies to

The law applies to for-profit businesses that do business in California and meet at least one threshold: gross annual revenue in the preceding calendar year of $26.625 million or more (the inflation-adjusted figure effective January 1, 2025); buying, selling or sharing the personal information of 100,000 or more California residents or households; or earning 50% or more of annual revenue from selling or sharing personal information.[^s1] Older material, including Salesforce's own FAQ marked as updated December 2021, still quotes the original $25 million and 50,000-consumer figures, so check thresholds against the CPPA rather than secondary sources.[^s4][^s1] The temporary exemptions for employee and business-to-business data expired on December 31, 2022, so personal information about employees and B2B contacts, typical CRM data, is now in scope.[^s1]

## Consumer rights and business duties

Consumers can ask a business what personal information it holds, have it deleted or corrected, and opt out of its sale or sharing. The CPRA added a category of sensitive personal information, which includes government identifiers, account credentials, precise geolocation, message contents, genetic and biometric data, and health information, with a right to limit its use.[^s1] Businesses must post a "Do Not Sell or Share My Personal Information" (or "Your Privacy Choices") link and must honor opt-out preference signals such as Global Privacy Control.[^s1] Salesforce's Trailhead guidance stresses that businesses must answer verifiable requests within 45 days and keep a reasonable, risk-based security program.[^s3]

## Regulation and enforcement

The CPPA's first CPRA rulemaking was approved by the Office of Administrative Law and became effective on March 29, 2023.[^s2] A later package covering automated decisionmaking technology (ADMT), privacy risk assessments and cybersecurity audits became effective January 1, 2026, with phased compliance deadlines; ADMT-specific requirements apply from January 1, 2027, including notice, opt-out where applicable, and information about how the technology worked.[^s1] The agency enforces through investigations, audits and administrative actions, and cannot pursue a violation that occurred more than five years earlier. Since January 1, 2024, it has also run the data broker registry under the Delete Act (SB 362).[^s1] The ADMT rules are directly relevant to orgs deploying predictive or generative AI features on consumer data.[^s1]

## How Salesforce fits

Salesforce states that it is a service provider to its customers under the CCPA and offers a Data Processing Addendum with CCPA-specific terms; customers on an earlier DPA, or with a master subscription agreement and no DPA, can sign the current one at any time.[^s4][^s3] The customer remains the business that answers consumers, so the platform question is how to find, export, delete and suppress one person's data across objects.[^s3]

Privacy Center is the main tool for that. It models a request lifecycle of receive, verify, execute and respond, and tracks each request with a customizable Privacy Request object.[^s5] Right-to-be-forgotten policies delete or mask data in a top-level object such as Individual and its related Person Account, Contact, Lead and User records, run from the RTBF Requests tab or a daily job. Portability policies compile a subject's personal data into JSON, retrievable from the Portability Log for 60 days, and Privacy Hold fields block processing where data must be retained.[^s5] Opt-out and consent preferences belong in the privacy and consent data model, built around the Individual entity with contact points, consent actions, data use purposes and communication subscriptions, which also underpins consent in Data 360.[^s6]

Gotchas: deleting a CRM record does not purge copies in integrated systems, backups or downstream analytics, so map every place personal information flows before promising deletion; and the 45-day clock means request intake and verification must be automated rather than handled in email.[^s3][^s5]

## Connections

CCPA and CPRA sit under **Security and Compliance Frameworks** as a regulatory regime rather than a security control framework.[^s1] They are the US state counterpart most often compared with the EU's GDPR, whose transfer rules are covered in **GDPR International Data Transfers**, and they contrast with **HIPAA**, a sector-specific health law, whereas the CCPA is a general consumer statute covering any personal information a qualifying business holds.[^s1] Compliance depends on the **Shared Responsibility Model**, because Salesforce supplies terms and tools while the customer configures and runs them.[^s3] Operationally the law is met with **Privacy Center** for requests,[^s5] the consent model behind **Consent Management in Data Cloud**,[^s6] while **Data Classification** (tagging which fields hold sensitive personal information) and **Salesforce Shield** are natural places to implement the risk-based security program the law expects.[^s3]

## Sources
[^s1]: California Privacy Protection Agency, "Frequently Asked Questions (FAQs)". https://cppa.ca.gov/faq.html (accessed 2026-11-27)
[^s2]: California Privacy Protection Agency, "California Consumer Privacy Act Regulations (March 2023)". https://cppa.ca.gov/regulations/consumer_privacy_act.html (accessed 2026-11-27)
[^s3]: Salesforce Trailhead, "Implement CCPA Compliance in Your Organization". https://trailhead.salesforce.com/content/learn/modules/california-consumer-privacy-act-basics/implement-ccpa-compliance-in-your-organization (accessed 2026-11-27)
[^s4]: Salesforce, "CCPA & CPRA Frequently Asked Questions". https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/white-papers/CCPA-FAQ.pdf (accessed 2026-11-27)
[^s5]: Salesforce Trailhead, "Handle Privacy Requests in Privacy Center". https://trailhead.salesforce.com/content/learn/modules/privacy-center/handle-privacy-requests-in-privacy-center (accessed 2026-11-27)
[^s6]: Salesforce Developers, "Privacy Overview Data Model". https://developer.salesforce.com/docs/platform/data-models/guide/privacy-overview.html (accessed 2026-11-27)
