---
id: kt:nist-sp-800-53b
type: ExternalConcept
title: NIST SP 800-53B
aliases: [NIST 800-53B, "Control Baselines for Information Systems and Organizations", SP 800-53B control baselines, NIST control baselines]
domain: public-sector-and-compliance
summary: >-
  NIST Special Publication 800-53B, the companion to SP 800-53 Rev. 5 that allocates catalog controls to Low,
  Moderate and High security baselines plus an impact-independent privacy baseline, and gives the tailoring and
  overlay guidance that turns a baseline into a system's control set; the starting point FedRAMP aligned its Rev. 5
  baselines to when authorizing cloud services such as Salesforce Government Cloud Plus.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:fedramp, kt:fedramp-high, kt:government-cloud-plus]
relations:
  - {predicate: partOf, object: kt:nist-sp-800-53}
  - {predicate: dependsOn, object: kt:fips-199}
  - {predicate: dependsOn, object: kt:fips-200}
sources:
  - id: s1
    title: "SP 800-53B, Control Baselines for Information Systems and Organizations"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/pubs/sp/800/53/b/upd1/final
    type: standards-body
    accessed: 2026-11-09
  - id: s2
    title: "NIST SP 800-53B, Control Baselines for Information Systems and Organizations (PDF)"
    publisher: NIST
    url: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53B.pdf
    type: standards-body
    accessed: 2026-11-09
  - id: s3
    title: "Control Baselines for Information Systems and Organizations: NIST Publishes SP 800-53B"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/news/2020/control-baselines-nist-publishes-sp-800-53b
    type: standards-body
    accessed: 2026-11-09
  - id: s4
    title: "Understanding Baselines and Impact Levels for FedRAMP Authorizations"
    publisher: FedRAMP (GSA)
    url: https://www.fedramp.gov/rev5/baselines
    type: government
    accessed: 2026-11-09
  - id: s5
    title: "Rev. 5 Baselines Have Been Approved and Released"
    publisher: FedRAMP (GSA)
    url: https://www.fedramp.gov/archive/2023-05-30-rev-5-baselines-have-been-approved-and-released/
    type: government
    accessed: 2026-11-09
  - id: s6
    title: "FedRAMP High - Salesforce Compliance Site"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/categories/fedramp-high
    type: official-docs
    accessed: 2026-11-09
  - id: s7
    title: "Access Government Cloud Compliance Documentation"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=ind.government_cloud_access_documentation.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-09
created: 2026-11-09
---

# NIST SP 800-53B

NIST Special Publication 800-53B, *Control Baselines for Information Systems and Organizations*, is the Joint Task Force publication that says which controls from the SP 800-53 Rev. 5 catalog a system should start with. It defines security baselines for low-, moderate- and high-impact systems, a privacy baseline that applies regardless of impact level, tailoring guidance with the working assumptions behind control selection, and guidance for building overlays.[^s1] NIST announced it in October 2020 as a companion to SP 800-53 Rev. 5, naming federal organizations as the primary audience.[^s3] For Salesforce architects it is the layer between "which impact level is this workload" and "which controls must the hosting cloud and the agency actually show".

## Versions and formats

The final publication is dated September 2020, with updates as of 10 December 2020.[^s1] NIST also publishes the baselines as a spreadsheet and as OSCAL content, and points to the Security Control Overlay Repository (SCOR) for shared overlays.[^s1][^s3] A minor release, 5.2.0, issued on 27 August 2025, made no changes to the baselines; the version number was bumped to stay consistent with SP 800-53 and 800-53A.[^s1] In practice, a control set built on the 2020 baselines has not been invalidated by later catalog releases, though new catalog controls may still be worth adding through tailoring.

## How a baseline is selected

The selection starts from a FIPS 199 categorization of confidentiality, integrity and availability. Following the FIPS 200 high-water mark, a system is low only if all three are low, moderate if any is moderate and none high, and high if any is high; that level picks the security baseline.[^s2] Controls are deliberately not split by security objective, because NIST treats the three objectives as highly interdependent.[^s2] Chapter Three then lays out one allocation table per control family, showing which controls and enhancements fall into the privacy, low, moderate and high baselines; some controls are assigned to no baseline and are adopted only through tailoring.[^s2]

## Tailoring, assumptions and overlays

NIST describes the baselines as starting points rather than minimum sets: organizations may add, remove or specialize controls, but not drop them arbitrarily.[^s2] Tailoring covers designating common controls, applying scoping considerations, choosing compensating controls, assigning organization-defined parameter values, supplementing the baseline, and recording implementation detail, with every decision documented in the security and privacy plans.[^s2] Controls tied to legal or policy requirements should not be tailored out.[^s2] The baselines also rest on assumptions, such as networked, multi-user, general-purpose systems; they do not by themselves address insider threats, advanced persistent threats, classified information or cross-domain needs, which may call for added controls.[^s2] Overlays package such specializations for a community, technology or environment, and national security systems instead follow CNSS guidance such as CNSSI 1253.[^s2]

Two concepts matter most for SaaS. Common controls can be inherited, so a system need not re-implement them, but owners and authorizing officials must confirm the inherited protection is adequate; hybrid controls are split between a common control provider and the system.[^s2] The privacy baseline, meanwhile, is driven by OMB Circular A-130 and the processing of personally identifiable information, and is tailored from a privacy risk assessment.[^s3][^s2]

## How Salesforce encounters it

FedRAMP's Rev. 5 baselines were updated to correspond with SP 800-53 Rev. 5 and SP 800-53B, and added cloud-specific guidance for many controls.[^s5] FedRAMP offers High, Moderate, Low and a tailored LI-SaaS baseline, and it does not let a provider tailor by security objective: one high objective puts the whole system at High.[^s4] The key gotcha is coverage. FedRAMP leaves privacy controls outside its baselines to agency discretion and keeps Program Management controls with the agency, so the 800-53B privacy baseline is not satisfied simply because a cloud service is authorized.[^s5] Customer agencies must also run their own FIPS 199 analysis for the data they put in a provider's environment.[^s4]

Salesforce Government Cloud Plus received a provisional ATO at the high impact level from the FedRAMP Joint Authorization Board in May 2020, and the Salesforce compliance site lists its FedRAMP High package.[^s6] Eligible Government Cloud Plus customers request access to the FedRAMP and DoD authorization packages through a secure portal; that material is confidential and must be referenced rather than reproduced.[^s7] Those packages are where an agency confirms which baseline controls it inherits from Salesforce and which remain its own to implement.[^s7][^s2]

## Connections

SP 800-53B sits under security compliance frameworks (`kt:security-compliance-frameworks`) and is `partOf` the NIST SP 800-53 family (`kt:nist-sp-800-53`), whose catalog it allocates.[^s1] It `dependsOn` FIPS 199 (`kt:fips-199`) for categorization and FIPS 200 (`kt:fips-200`) for the high-water mark that maps a category to a baseline.[^s2] FedRAMP (`kt:fedramp`, related) aligned its Rev. 5 baselines to it, and FedRAMP High (`kt:fedramp-high`, related) corresponds to its high baseline.[^s5][^s4] Government Cloud Plus (`kt:government-cloud-plus`, related) is the Salesforce environment authorized at that level.[^s6]

## Sources
[^s1]: NIST CSRC, "SP 800-53B, Control Baselines for Information Systems and Organizations". https://csrc.nist.gov/pubs/sp/800/53/b/upd1/final (accessed 2026-11-09)
[^s2]: NIST, "NIST SP 800-53B, Control Baselines for Information Systems and Organizations" (PDF). https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53B.pdf (accessed 2026-11-09)
[^s3]: NIST CSRC, "Control Baselines for Information Systems and Organizations: NIST Publishes SP 800-53B". https://csrc.nist.gov/news/2020/control-baselines-nist-publishes-sp-800-53b (accessed 2026-11-09)
[^s4]: FedRAMP (GSA), "Understanding Baselines and Impact Levels for FedRAMP Authorizations". https://www.fedramp.gov/rev5/baselines (accessed 2026-11-09)
[^s5]: FedRAMP (GSA), "Rev. 5 Baselines Have Been Approved and Released". https://www.fedramp.gov/archive/2023-05-30-rev-5-baselines-have-been-approved-and-released/ (accessed 2026-11-09)
[^s6]: Salesforce, "FedRAMP High - Salesforce Compliance Site". https://compliance.salesforce.com/en/categories/fedramp-high (accessed 2026-11-09)
[^s7]: Salesforce Help, "Access Government Cloud Compliance Documentation". https://help.salesforce.com/s/articleView?id=ind.government_cloud_access_documentation.htm&language=en_US&type=5 (accessed 2026-11-09)
