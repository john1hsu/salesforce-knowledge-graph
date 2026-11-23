---
id: kt:irs-publication-1075
type: ExternalConcept
title: IRS Publication 1075
aliases: [IRS 1075, Pub 1075, Publication 1075, Tax Information Security Guidelines, FTI safeguards]
domain: public-sector-and-compliance
summary: >-
  The IRS's Tax Information Security Guidelines for federal, state and local agencies, which set the safeguards
  for Federal Tax Information (FTI) under IRC 6103(p)(4); Salesforce Government Cloud Plus carries an IRS 1075
  attestation so agencies can store and process FTI in Salesforce.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:government-cloud-plus, kt:fedramp-high, kt:shield-platform-encryption, kt:public-sector-solutions, kt:data-residency]
relations:
  - {predicate: dependsOn, object: kt:nist-sp-800-53}
  - {predicate: dependsOn, object: kt:fedramp}
  - {predicate: contrastsWith, object: kt:cjis-security-policy}
sources:
  - id: s1
    title: "Publication 1075: Tax Information Security Guidelines For Federal, State and Local Agencies (November 2021)"
    publisher: Internal Revenue Service
    url: https://www.irs.gov/pub/irs-pdf/p1075.pdf
    type: government
    accessed: 2026-11-23
  - id: s2
    title: "Cloud computing environment"
    publisher: Internal Revenue Service
    url: https://www.irs.gov/node/8309
    type: government
    accessed: 2026-11-23
  - id: s3
    title: "Encryption requirements of Publication 1075"
    publisher: Internal Revenue Service
    url: https://www.irs.gov/zh-hant/privacy-disclosure/encryption-requirements-of-publication-1075
    type: government
    accessed: 2026-11-23
  - id: s4
    title: "45-day notifications"
    publisher: Internal Revenue Service
    url: https://www.irs.gov/node/5379
    type: government
    accessed: 2026-11-23
  - id: s5
    title: "IRS 1075 — Salesforce Compliance"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/irs-1075
    type: official-docs
    accessed: 2026-11-23
  - id: s6
    title: "Salesforce Announces Customer Ability to Store and Process Federal Taxpayer Information in Government Cloud Plus"
    publisher: Salesforce
    url: https://www.salesforce.com/news/stories/salesforce-announces-customer-ability-to-store-and-process-federal-taxpayer-information-in-government-cloud-plus/
    type: news
    accessed: 2026-11-23
created: 2026-11-23
---

# IRS Publication 1075

IRS Publication 1075, *Tax Information Security Guidelines For Federal, State and Local Agencies*, is the rulebook for any government agency that receives Federal Tax Information (FTI): federal tax returns, return information and data derived from them. The IRS Office of Safeguards uses it to verify compliance with the safeguard requirements of Internal Revenue Code § 6103(p)(4), identifying and mitigating the risk of loss, breach or misuse of FTI held by outside government agencies.[^s1] The current edition is the November 2021 revision, which supersedes the November 2016 edition and took effect six months after publication.[^s1]

For Salesforce practitioners it matters whenever a state revenue department, benefits agency or city licensing office wants FTI in a CRM record. Typical examples Salesforce cites are a permitting office checking a business's tax status and a state treasury managing taxpayer hearings and appeals.[^s6]

## How it is structured

The 2021 revision rebuilt Section 4.0 around the NIST SP 800-53 Revision 5 security and privacy control catalog, folding in the privacy controls that Revision 4 kept in Appendix J.[^s1] The publication therefore reads as an 800-53 baseline plus IRS-specific parameters, along with chapters on reporting, incident handling and contractor disclosure. It also removed the old safeguard review cycle table, moving that content into its section on the assessment process.[^s1]

Agencies that re-disclose FTI to contractors must notify the IRS at least 45 days before signing the agreement, certify that contractor staff and systems touching FTI sit in the United States or its territories, and bind contractors to the same confidentiality and training standards as the agency. Failure can jeopardize the agency's continued access to FTI.[^s4]

## Cloud requirements that shape a Salesforce design

The IRS treats a multi-tenant SaaS like Salesforce as a cloud, and its cloud guidance adds several hard conditions:[^s2]

- **FedRAMP first:** only cloud offerings FedRAMP-authorized for medium (moderate) impact systems may hold FTI, but FedRAMP or a 3PAO attestation alone does not satisfy Publication 1075.[^s2]
- **Onshore only:** FTI must reside in systems under U.S. legal jurisdiction, and all access and support, including backup sites, must be performed from the U.S.[^s2]
- **45-day cloud notification:** the agency notifies Safeguards at least 45 days before moving FTI into a cloud, documenting its own controls, the provider's FedRAMP status, data center locations and encryption.[^s2]
- **Isolation and labelling:** FTI must be isolated from other tenants, kept separate from other data where possible, and otherwise labelled down to the data element.[^s2]

Encryption follows the latest FIPS 140 validated mechanisms. FTI sent over the internet or by email must be encrypted, SHA-1 is banned for digital signatures, and FTI must be encrypted at rest in vendor-operated FedRAMP cloud environments.[^s3] Where a deployment model cannot meet a requirement, Safeguards may accept compensating controls that give equal protection, evaluated during the notification review.[^s2]

## Salesforce coverage and gotchas

Salesforce Government Cloud Plus has been assessed by an outside auditor as meeting IRS 1075 while leveraging FedRAMP High baseline controls; the review used NIST SP 800-53 revision 4, not the revision 5 baseline of the current publication.[^s5] Customers get the letter of attestation from their account representative and should review the Government Cloud Plus FedRAMP package alongside it.[^s5] Salesforce announced the capability in March 2021, describing Government Cloud Plus as an isolated instance on AWS GovCloud (US) and offering a pre-populated form agencies can send to the Office of Safeguards to declare their intent to hold FTI.[^s6]

Three gotchas follow. Commercial orgs are out of scope, so FTI belongs only in Government Cloud Plus.[^s5] The attestation covers the provider, not the agency: the 45-day notification, field-level labelling, user access and audit configuration remain the customer's job.[^s2] And the attested NIST revision trails the publication's, so an agency may need its own gap analysis.[^s1][^s5]

## Connections

Publication 1075 is a sector-specific regime under `kt:security-compliance-frameworks` and `dependsOn` `kt:nist-sp-800-53` for its control catalog.[^s1] It also `dependsOn` `kt:fedramp`, because FedRAMP authorization is a precondition for any FTI cloud, and `kt:fedramp-high` is the baseline Salesforce's attestation leverages.[^s2][^s5] `kt:government-cloud-plus` is the only Salesforce environment in scope, `kt:public-sector-solutions` is the industry product agencies run there, and `kt:data-residency` frames its onshore rule.[^s2][^s5] `kt:shield-platform-encryption` is a natural candidate for the at-rest encryption the IRS expects in vendor clouds, though the IRS guidance itself names no product.[^s3] It contrasts with `kt:cjis-security-policy`: both overlay 800-53, but CJIS protects criminal justice data audited by state agencies, while Publication 1075 protects tax data overseen by the IRS Office of Safeguards.[^s1]

## Sources

[^s1]: Internal Revenue Service, "Publication 1075: Tax Information Security Guidelines For Federal, State and Local Agencies (November 2021)". https://www.irs.gov/pub/irs-pdf/p1075.pdf (accessed 2026-11-23)
[^s2]: Internal Revenue Service, "Cloud computing environment". https://www.irs.gov/node/8309 (accessed 2026-11-23)
[^s3]: Internal Revenue Service, "Encryption requirements of Publication 1075". https://www.irs.gov/zh-hant/privacy-disclosure/encryption-requirements-of-publication-1075 (accessed 2026-11-23)
[^s4]: Internal Revenue Service, "45-day notifications". https://www.irs.gov/node/5379 (accessed 2026-11-23)
[^s5]: Salesforce, "IRS 1075 — Salesforce Compliance". https://compliance.salesforce.com/en/irs-1075 (accessed 2026-11-23)
[^s6]: Salesforce, "Salesforce Announces Customer Ability to Store and Process Federal Taxpayer Information in Government Cloud Plus". https://www.salesforce.com/news/stories/salesforce-announces-customer-ability-to-store-and-process-federal-taxpayer-information-in-government-cloud-plus/ (accessed 2026-11-23)
