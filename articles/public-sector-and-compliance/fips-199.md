---
id: kt:fips-199
type: ExternalConcept
title: FIPS 199
aliases: [FIPS PUB 199, "Standards for Security Categorization of Federal Information and Information Systems", FIPS 199 security categorization, security categorization]
domain: public-sector-and-compliance
summary: >-
  Federal Information Processing Standard 199, the NIST standard that rates federal information and systems Low,
  Moderate or High for each of confidentiality, integrity and availability; the resulting impact level picks the
  NIST SP 800-53 baseline and the FedRAMP baseline a cloud service such as Salesforce Government Cloud Plus must meet.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:fedramp, kt:nist-sp-800-53, kt:government-cloud-plus, kt:nist-sp-800-60]
relations:
  - {predicate: enables, object: kt:fips-200}
  - {predicate: usedBy, object: kt:fedramp-high}
sources:
  - id: s1
    title: "FIPS 199, Standards for Security Categorization of Federal Information and Information Systems"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/pubs/fips/199/final
    type: standards-body
    accessed: 2026-11-05
  - id: s2
    title: "ITL Bulletin, March 2004: Federal Information Processing Standard (FIPS) 199"
    publisher: NIST Information Technology Laboratory
    url: https://csrc.nist.gov/files/pubs/shared/itlb/itlbul2004-03.pdf
    type: standards-body
    accessed: 2026-11-05
  - id: s3
    title: "ITL Bulletin, March 2006: Minimum Security Requirements for Federal Information and Information Systems (FIPS 200)"
    publisher: NIST Information Technology Laboratory
    url: https://csrc.nist.gov/files/pubs/shared/itlb/itlbul2006-03.pdf
    type: standards-body
    accessed: 2026-11-05
  - id: s4
    title: "Understanding Baselines and Impact Levels for FedRAMP Authorizations"
    publisher: FedRAMP (GSA)
    url: https://www.fedramp.gov/rev5/baselines
    type: government
    accessed: 2026-11-05
  - id: s5
    title: "SP 800-60 Rev. 2 (Initial Working Draft), Guide for Mapping Types of Information and Systems to Security Categories"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/pubs/sp/800/60/r2/iwd
    type: standards-body
    accessed: 2026-11-05
  - id: s6
    title: "FedRAMP High — Salesforce Compliance"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/fedramp-high
    type: official-docs
    accessed: 2026-11-05
created: 2026-11-05
---

# FIPS 199

FIPS 199, *Standards for Security Categorization of Federal Information and Information Systems*, is the NIST standard US federal agencies use to classify their information and systems by how much harm a security failure would cause. It was finalized in February 2004 and remains the current, unwithdrawn version.[^s1] The categories reflect the potential damage to an agency's operations, assets or people if information were accessed, used, disclosed, disrupted, modified or destroyed without authorization.[^s1] NIST wrote it because FISMA, Title III of the E-Government Act of 2002, directed it to produce a categorization standard for agencies.[^s2] For Salesforce architects it is the first question behind any government deal: the categorization decides which FedRAMP baseline the cloud service must hold.

## How categorization works

FIPS 199 rates three security objectives separately. Confidentiality concerns authorized restrictions on access and disclosure, including privacy; integrity concerns improper modification or destruction, including authenticity and non-repudiation; availability concerns timely and reliable access.[^s2] Each objective gets one of three potential impact levels. Low means a loss would have a limited adverse effect, such as degraded but workable mission capability or minor harm. Moderate means a serious effect, such as significantly reduced effectiveness or significant financial loss or harm short of loss of life. High means a severe or catastrophic effect, including loss of primary mission functions or loss of life.[^s2]

A security category is therefore a triple, for example moderate confidentiality, moderate integrity and low availability.[^s2] An agency first categorizes each information type the system handles; the system's rating for each objective is the highest rating among those information types, and system data such as password files must be protected at the level of the most critical user data.[^s2] NIST SP 800-60 supplies the method and a catalog of federal information types with provisional impact levels. A Rev. 2 working draft, released in January 2024, proposes stronger privacy handling, an updated taxonomy aligned with the NARA CUI registry, and folding in SP 800-122.[^s5]

## From category to controls

FIPS 199 does not itself prescribe controls. Its companion FIPS 200 requires categorization to happen before controls are chosen, then collapses the triple into one system impact level: a system is high-impact if any objective is high, moderate if the highest is moderate, and low only if all three are low.[^s3] That single level selects the low, moderate or high control baseline from NIST SP 800-53, which agencies may then tailor.[^s3]

## How Salesforce encounters it

FedRAMP applies the same scheme to cloud service offerings. Low covers limited adverse effects, with a tailored LI-SaaS variant for SaaS storing no PII beyond login data; Moderate covers serious effects and is where most authorized offerings sit; High covers severe or catastrophic effects in areas such as law enforcement, emergency services, finance and health.[^s4] FedRAMP does not let baselines be tailored per objective: if any one objective needs High, the system must meet High for all three.[^s4] Providers record their categorization in the FedRAMP FIPS 199 Categorization Template (Appendix K of the System Security Plan), following SP 800-60.[^s4]

Two practical gotchas follow. First, the provider's categorization is not the customer's: each agency must do its own FIPS 199 analysis of the data it puts into the provider's environment.[^s4] Second, that analysis drives the product choice. Data categorized High needs a High-authorized environment, and Salesforce's Government Cloud Plus received a JAB provisional authorization at the high impact level in May 2020.[^s6] A Moderate or Low categorization opens more options, so architects should obtain the agency's categorization before committing to an environment rather than defaulting to the strictest one.

## Connections

FIPS 199 belongs to the broader family of security compliance frameworks (`kt:security-compliance-frameworks`).[^s1] It `enables` FIPS 200 (`kt:fips-200`), which turns the category into minimum requirements, and through it the baseline selection in NIST SP 800-53 (`kt:nist-sp-800-53`, related).[^s3] SP 800-60 (`kt:nist-sp-800-60`, related) is the guidance for mapping information types to its categories.[^s5] FedRAMP (`kt:fedramp`, related) reuses its Low, Moderate and High levels, and FIPS 199 is `usedBy` FedRAMP High (`kt:fedramp-high`), the baseline required once a category reaches High on any objective.[^s4] Government Cloud Plus (`kt:government-cloud-plus`, related) is the Salesforce environment authorized at that level.[^s6]

## Sources
[^s1]: NIST CSRC, "FIPS 199, Standards for Security Categorization of Federal Information and Information Systems". https://csrc.nist.gov/pubs/fips/199/final (accessed 2026-11-05)
[^s2]: NIST ITL, "ITL Bulletin, March 2004: Federal Information Processing Standard (FIPS) 199". https://csrc.nist.gov/files/pubs/shared/itlb/itlbul2004-03.pdf (accessed 2026-11-05)
[^s3]: NIST ITL, "ITL Bulletin, March 2006: Minimum Security Requirements for Federal Information and Information Systems (FIPS 200)". https://csrc.nist.gov/files/pubs/shared/itlb/itlbul2006-03.pdf (accessed 2026-11-05)
[^s4]: FedRAMP (GSA), "Understanding Baselines and Impact Levels for FedRAMP Authorizations". https://www.fedramp.gov/rev5/baselines (accessed 2026-11-05)
[^s5]: NIST CSRC, "SP 800-60 Rev. 2 (Initial Working Draft)". https://csrc.nist.gov/pubs/sp/800/60/r2/iwd (accessed 2026-11-05)
[^s6]: Salesforce, "FedRAMP High — Salesforce Compliance". https://compliance.salesforce.com/en/fedramp-high (accessed 2026-11-05)
