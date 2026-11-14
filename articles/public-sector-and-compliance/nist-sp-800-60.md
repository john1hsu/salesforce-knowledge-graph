---
id: kt:nist-sp-800-60
type: ExternalConcept
title: NIST SP 800-60
aliases: [NIST 800-60, SP 800-60 Vol. 1 Rev. 1, "Guide for Mapping Types of Information and Information Systems to Security Categories", SP 800-60 Rev. 2, NIST information types catalog]
domain: public-sector-and-compliance
summary: >-
  NIST Special Publication 800-60, the guide and catalog US federal agencies and FedRAMP cloud providers use to map the
  information types a system handles to provisional FIPS 199 impact levels, then roll them up into the system's security
  category; it is the working method behind deciding whether a Salesforce government org needs a Low, Moderate or High baseline.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:nist-sp-800-53, kt:government-cloud-plus, kt:data-classification, kt:fedramp-high]
relations:
  - {predicate: implements, object: kt:fips-199}
  - {predicate: partOf, object: kt:nist-risk-management-framework}
  - {predicate: consumedBy, object: kt:fedramp}
sources:
  - id: s1
    title: "SP 800-60 Vol. 1 Rev. 1, Guide for Mapping Types of Information and Information Systems to Security Categories"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/pubs/sp/800/60/v1/r1/final
    type: standards-body
    accessed: 2026-11-14
  - id: s2
    title: "NIST Special Publication 800-60 Volume I Revision 1 (PDF)"
    publisher: NIST
    url: https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-60v1r1.pdf
    type: standards-body
    accessed: 2026-11-14
  - id: s3
    title: "SP 800-60 Rev. 2 (Initial Working Draft), Guide for Mapping Types of Information and Systems to Security Categories"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/pubs/sp/800/60/r2/iwd
    type: standards-body
    accessed: 2026-11-14
  - id: s4
    title: "Categorize Step: Tips and Techniques for Systems (RMF Quick Start Guide)"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/CSRC/media/Projects/Risk-Management/documents/categorize/QSG_categorize_tips-and-techniques-for-systems.pdf
    type: standards-body
    accessed: 2026-11-14
  - id: s5
    title: "Understanding Baselines and Impact Levels for FedRAMP Authorizations"
    publisher: FedRAMP (GSA)
    url: https://www.fedramp.gov/rev5/baselines
    type: government
    accessed: 2026-11-14
  - id: s6
    title: "FedRAMP High — Salesforce Compliance"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/fedramp-high
    type: official-docs
    accessed: 2026-11-14
created: 2026-11-14
---

# NIST SP 800-60

NIST Special Publication 800-60, *Guide for Mapping Types of Information and Information Systems to Security Categories*, is the practical companion to FIPS 199. Where FIPS 199 defines the Low, Moderate and High impact levels for confidentiality, integrity and availability, SP 800-60 tells an agency how to apply them: list the kinds of information a system handles, look each one up in a catalog of provisional ratings, adjust, and roll the results up into one system category.[^s2] The current final edition is Volume I Revision 1, published in August 2008 under FISMA, which superseded the original June 2004 volume; Volume II Revision 1 holds the catalog itself.[^s1] For a Salesforce architect, SP 800-60 is the worksheet that turns "we hold case files and payment data" into a FedRAMP baseline decision.

## The two volumes

Volume I is the methodology. Volume II is a set of appendices giving provisional impact levels and the rationale for each information type, plus the laws and executive orders that make certain information sensitive or critical.[^s2] The catalog splits information into two families. Mission-based types describe what government does for citizens and how it delivers those services; management and support types cover the back-office functions every agency shares, such as finance, human resources and IT management.[^s2] Revision 1 built this taxonomy on the Business Reference Model of OMB's Federal Enterprise Architecture.[^s2]

## How categorization works

The guide lays out four steps.[^s2]

1. Identify every information type the system takes in, stores, processes or outputs, using the catalog's taxonomies.[^s2]
2. Select a provisional Low, Moderate or High level per objective for each type, from Volume II or from the FIPS 199 criteria.[^s2]
3. Review the provisional levels against the agency's mission, environment, data sharing and legal duties, and adjust them, documenting each change and its reason.[^s2]
4. Set the system category from the highest level found for each objective across all types, then take the highest objective as the overall impact level.[^s2]

Volume I also lists special factors that can push a rating up. Aggregation can make a combined dataset more sensitive than its parts, and low-impact data may deserve more protection when it gives access to other critical systems. Privacy-protected information sets a floor on confidentiality.[^s2] An information type may be rated not applicable for confidentiality (public data, for example), but a whole system may not.[^s2]

NIST's RMF quick-start guide puts responsibility for categorization on the information or system owner, working with security, enterprise architecture and data-sharing partners. It calls categorization the most important RMF step, because the impact level drives the SP 800-53 baseline and the rigor of every later step. The analysis and rationale belong in the system security plan.[^s4]

## Revision 2

In January 2024 NIST released an initial working draft of Revision 2 for pre-draft comment, with comments due by 18 March 2024.[^s3] It proposes to treat privacy better during categorization and align the method with RMF (SP 800-37 Rev. 2). It would also update the taxonomy to current federal information types, including the NARA CUI registry, and fold in SP 800-122's PII guidance so that publication can be withdrawn.[^s3] NIST also plans to publish the information types and provisional levels as data through its Cybersecurity and Privacy Reference Tool.[^s3] Until Revision 2 is final, Volume I and Volume II Revision 1 remain the editions cited in practice.[^s1]

## How Salesforce encounters it

FedRAMP tells cloud providers to categorize their systems with FIPS 199 together with SP 800-60 Volume II Revision 1, and to record the result in the FIPS 199 Categorization Template, Appendix K of the System Security Plan.[^s5] FedRAMP does not allow tailoring by objective, so one High objective puts the whole offering on the High baseline. Customer agencies must still run their own FIPS 199 analysis of the data they bring.[^s5] Salesforce's Government Cloud Plus holds a JAB provisional authorization at the high impact level, granted in May 2020.[^s6]

In practice, an architect sizing a public-sector Salesforce implementation should ask for the agency's SP 800-60 worksheet early. FedRAMP associates High with areas such as law enforcement, emergency services, finance and health, while most authorized offerings sit at Moderate. The answer decides which Salesforce environment is eligible, so do not assume one before the categorization exists.[^s5]

## Connections

SP 800-60 is one of the security compliance frameworks (`kt:security-compliance-frameworks`) and `implements` FIPS 199 (`kt:fips-199`) by turning its definitions into a repeatable method.[^s2] It is `partOf` the NIST Risk Management Framework (`kt:nist-risk-management-framework`) as the core of the Categorize step, and its output selects the NIST SP 800-53 baseline (`kt:nist-sp-800-53`, related).[^s4] It is `consumedBy` FedRAMP (`kt:fedramp`), which requires it for the Appendix K template, and reaching High on any objective leads to FedRAMP High (`kt:fedramp-high`, related) and environments such as Government Cloud Plus (`kt:government-cloud-plus`, related).[^s5][^s6] Its information-type inventory is a federal form of data classification (`kt:data-classification`, related).[^s2]

## Sources
[^s1]: NIST CSRC, "SP 800-60 Vol. 1 Rev. 1, Guide for Mapping Types of Information and Information Systems to Security Categories". https://csrc.nist.gov/pubs/sp/800/60/v1/r1/final (accessed 2026-11-14)
[^s2]: NIST, "NIST Special Publication 800-60 Volume I Revision 1" (PDF). https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-60v1r1.pdf (accessed 2026-11-14)
[^s3]: NIST CSRC, "SP 800-60 Rev. 2 (Initial Working Draft)". https://csrc.nist.gov/pubs/sp/800/60/r2/iwd (accessed 2026-11-14)
[^s4]: NIST CSRC, "Categorize Step: Tips and Techniques for Systems". https://csrc.nist.gov/CSRC/media/Projects/Risk-Management/documents/categorize/QSG_categorize_tips-and-techniques-for-systems.pdf (accessed 2026-11-14)
[^s5]: FedRAMP (GSA), "Understanding Baselines and Impact Levels for FedRAMP Authorizations". https://www.fedramp.gov/rev5/baselines (accessed 2026-11-14)
[^s6]: Salesforce, "FedRAMP High — Salesforce Compliance". https://compliance.salesforce.com/en/fedramp-high (accessed 2026-11-14)
