---
id: kt:itar-and-export-controls
type: ExternalConcept
title: ITAR and Export Controls
aliases: [ITAR, International Traffic in Arms Regulations, export-controlled data, ITAR technical data, EAR and ITAR in the cloud]
domain: public-sector-and-compliance
summary: >-
  The US export control regimes (the State Department's ITAR for defense articles and technical data, and
  Commerce's EAR for dual-use items) as they bear on storing controlled data in a SaaS platform such as
  Salesforce: what counts as an export, the end-to-end encryption carve-outs, and why defense contractors
  look to Government Cloud Plus.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:government-cloud-plus, kt:il4-and-il5, kt:data-residency, kt:shield-platform-encryption, kt:data-classification]
relations:
  - {predicate: contrastsWith, object: kt:irs-publication-1075}
  - {predicate: dependsOn, object: kt:shared-responsibility-model}
sources:
  - id: s1
    title: "22 CFR § 120.54 - Activities that are not exports, reexports, retransfers, or temporary imports"
    publisher: U.S. Department of State (eCFR text via Cornell Legal Information Institute)
    url: https://www.law.cornell.edu/cfr/text/22/120.54
    type: government
    accessed: 2026-11-25
  - id: s2
    title: "22 CFR Part 120 Subpart C - Definitions"
    publisher: U.S. Department of State (eCFR text via Cornell Legal Information Institute)
    url: https://www.law.cornell.edu/cfr/text/22/part-120/subpart-C
    type: government
    accessed: 2026-11-25
  - id: s3
    title: "15 CFR § 734.18 - Activities that are not exports, reexports, or transfers"
    publisher: U.S. Department of Commerce, BIS (eCFR text via Cornell Legal Information Institute)
    url: https://www.law.cornell.edu/cfr/text/15/734.18
    type: government
    accessed: 2026-11-25
  - id: s4
    title: "2025 Defense Export Handbook"
    publisher: U.S. Department of Commerce, International Trade Administration
    url: https://www.trade.gov/sites/default/files/2025-01/2025%20Defense%20Export%20Handbook.pdf
    type: government
    accessed: 2026-11-25
  - id: s5
    title: "Advisory opinion on grid and cloud computing services (January 13, 2009)"
    publisher: U.S. Department of Commerce, Bureau of Industry and Security
    url: https://www.bis.gov/media/1343
    type: government
    accessed: 2026-11-25
  - id: s6
    title: "Salesforce Government Cloud Plus (datasheet)"
    publisher: Salesforce
    url: https://www.salesforce.com/en-us/wp-content/uploads/sites/4/Salesforce-Government-Cloud-Plus-Datasheet.pdf
    type: official-docs
    accessed: 2026-11-25
  - id: s7
    title: "Government Cloud Plus - Defense — Salesforce Compliance"
    publisher: Salesforce
    url: https://compliance.salesforce.com/jp/services/salesforce-government-cloud-plus-defense
    type: official-docs
    accessed: 2026-11-25
created: 2026-11-25
---

# ITAR and Export Controls

US export controls restrict who may receive certain goods, software and technical information, and they follow the data into the cloud. Two regimes matter most. The International Traffic in Arms Regulations (ITAR, 22 CFR parts 120–130) govern the manufacture, export and temporary import of defense articles, defense services and brokering for items on the US Munitions List, and are administered by the State Department's Directorate of Defense Trade Controls (DDTC).[^s4] The Export Administration Regulations (EAR) cover commercial and dual-use items and are administered by the Commerce Department's Bureau of Industry and Security (BIS).[^s4][^s3]

For Salesforce practitioners the topic appears when an aerospace or defense manufacturer, or a government contractor, wants drawings, specifications or program data in CRM records, Files or Knowledge.[^s6] The question is then not "is Salesforce ITAR certified" but whether putting that data in a given org could hand it to a foreign person or move it abroad.[^s1][^s5]

## What is controlled

ITAR "technical data" is information, other than software, needed to design, develop, produce, operate or maintain defense articles (blueprints, drawings, plans and the like), plus classified information about USML items and software directly related to defense articles.[^s2] General scientific and engineering principles taught in schools, public-domain information and basic marketing material are excluded.[^s2] The ITAR's definitions section also defines export, release, U.S. person and foreign person, which together decide whether giving someone access counts as an export.[^s2] Manufacturers and exporters of USML items must register with DDTC, and nearly all USML items need a license to leave the country.[^s4]

## Cloud storage and the encryption carve-outs

Both regimes carve out encrypted storage. Under ITAR, sending, taking or storing technical data is not an export when all of these hold:[^s1]

- The data is unclassified and secured with end-to-end encryption.[^s1]
- The cryptography uses FIPS 140-2 (or successor) modules with NIST-guided key management, or other means at least comparable to AES-128.[^s1]
- The data is not intentionally sent to a person in, or stored in, a country proscribed under 22 CFR 126.1, and is not sent from one.[^s1]

End-to-end means the data is never unencrypted between the originator and the intended recipient, and no third party, including the cloud provider, is given the means to decrypt.[^s1] Data passing over the internet is not deemed stored in the countries it transits, and merely having access to properly encrypted data is not a release.[^s1] The EAR's version in 15 CFR 734.18 is similar but speaks of "technology" and "software" and bars intentional storage in Country Group D:5 countries.[^s3]

BIS has also said that a provider selling raw computing capacity is not exporting anything subject to the EAR unless it ships controlled software or technology itself, and is not the exporter of data that users generate.[^s5] That places the compliance burden on the customer who uploads and shares controlled data.[^s5]

## Salesforce design implications

Salesforce's Government Cloud Plus datasheet describes a dedicated AWS GovCloud (US) environment operated and supported by screened, qualified U.S. citizens, with customer data processed and stored solely in the continental U.S., and lists aerospace and defense organizations among its eligible users.[^s6] Government Cloud Plus - Defense is a physically isolated instance for the Department of Defense and its contractors, aimed at IL5 data such as Controlled Unclassified Information.[^s7] Neither page states an ITAR compliance claim, so personnel and residency properties are inputs to the customer's own export analysis, not a substitute for it.[^s6][^s7]

The ITAR encryption carve-out is hard to meet with provider-managed keys, because the provider must have no way to decrypt; server-side encryption alone does not obviously qualify.[^s1] A defensible design therefore combines a U.S.-person-operated environment, classification of controlled records, and access controls that keep foreign-person users away from them, documenting who in their own organization may see technical data.[^s2][^s6]

## Connections

Export controls sit under `kt:security-compliance-frameworks` as a sector-specific regime, and they `dependsOn` `kt:shared-responsibility-model`, because BIS places the exporter role on the user rather than the computing provider.[^s5] `kt:government-cloud-plus` and `kt:il4-and-il5` describe the US-person, onshore environments defense customers evaluate, and `kt:data-residency` frames the storage-location conditions in the carve-outs.[^s1][^s6][^s7] `kt:shield-platform-encryption` and `kt:data-classification` are the controls a design would use to tag and protect technical data, though no regulation names a product.[^s1] The regime contrasts with `kt:irs-publication-1075`: that one protects tax data under IRS oversight, while ITAR controls defense technical data under DDTC licensing.[^s4]

## Sources

[^s1]: U.S. Department of State, "22 CFR § 120.54 - Activities that are not exports, reexports, retransfers, or temporary imports" (via Cornell LII). https://www.law.cornell.edu/cfr/text/22/120.54 (accessed 2026-11-25)
[^s2]: U.S. Department of State, "22 CFR Part 120 Subpart C - Definitions" (via Cornell LII). https://www.law.cornell.edu/cfr/text/22/part-120/subpart-C (accessed 2026-11-25)
[^s3]: U.S. Department of Commerce, BIS, "15 CFR § 734.18 - Activities that are not exports, reexports, or transfers" (via Cornell LII). https://www.law.cornell.edu/cfr/text/15/734.18 (accessed 2026-11-25)
[^s4]: U.S. Department of Commerce, International Trade Administration, "2025 Defense Export Handbook". https://www.trade.gov/sites/default/files/2025-01/2025%20Defense%20Export%20Handbook.pdf (accessed 2026-11-25)
[^s5]: U.S. Department of Commerce, Bureau of Industry and Security, "Advisory opinion on grid and cloud computing services (January 13, 2009)". https://www.bis.gov/media/1343 (accessed 2026-11-25)
[^s6]: Salesforce, "Salesforce Government Cloud Plus (datasheet)". https://www.salesforce.com/en-us/wp-content/uploads/sites/4/Salesforce-Government-Cloud-Plus-Datasheet.pdf (accessed 2026-11-25)
[^s7]: Salesforce, "Government Cloud Plus - Defense — Salesforce Compliance". https://compliance.salesforce.com/jp/services/salesforce-government-cloud-plus-defense (accessed 2026-11-25)
