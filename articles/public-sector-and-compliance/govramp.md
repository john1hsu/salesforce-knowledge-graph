---
id: kt:govramp
type: ExternalConcept
title: GovRAMP
aliases: [StateRAMP, State Risk and Authorization Management Program, GovRAMP verification]
domain: public-sector-and-compliance
summary: >-
  A nonprofit, FedRAMP-modelled program (founded in 2021 as StateRAMP and rebranded in 2025) that verifies the
  security of cloud products sold to US state and local governments against NIST SP 800-53 controls, with statuses
  from Core through Ready to Provisionally Authorized and Authorized, plus ongoing continuous monitoring.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:government-cloud-plus, kt:cjis-security-policy, kt:tx-ramp]
relations:
  - {predicate: dependsOn, object: kt:nist-sp-800-53}
  - {predicate: contrastsWith, object: kt:fedramp}
  - {predicate: hasPart, object: kt:continuous-monitoring}
sources:
  - id: s1
    title: "StateRAMP Rebrands to GovRAMP: PerfCon"
    publisher: StateTech Magazine
    url: https://statetechmagazine.com/article/2025/04/stateramp-rebrands-to-govramp-perfcon
    type: news
    accessed: 2026-11-13
  - id: s2
    title: "GovRAMP for Service Providers"
    publisher: GovRAMP
    url: https://govramp.org/providers/
    type: standards-body
    accessed: 2026-11-13
  - id: s3
    title: "GovRAMP Introduces Core Status: A New Milestone in Cloud Security Validation"
    publisher: GovRAMP
    url: https://govramp.org/?p=16489
    type: standards-body
    accessed: 2026-11-13
  - id: s4
    title: "GovRAMP Adoption"
    publisher: North Carolina Department of Information Technology
    url: https://it.nc.gov/programs/cybersecurity-risk-management/esrmo-initiatives/govramp-adoption
    type: government
    accessed: 2026-11-13
  - id: s5
    title: "GovRAMP Adoption"
    publisher: Georgia Technology Authority
    url: https://gta.georgia.gov/node/20221
    type: government
    accessed: 2026-11-13
  - id: s6
    title: "Government Cloud Plus (compliance service page)"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/services/salesforce-government-cloud-plus-hyperforce
    type: official-docs
    accessed: 2026-11-13
created: 2026-11-13
---

# GovRAMP

GovRAMP is a nonprofit membership organization that verifies whether cloud products meet a common security bar for US state and local government buyers. It was founded in 2021 by current and former state officials, is headquartered in Indianapolis, and was originally called StateRAMP (the State Risk and Authorization Management Program), a name chosen because it was modelled on the federal FedRAMP program.[^s1] In early 2025 it moved to govramp.org and began operating as GovRAMP, although its legal name stayed StateRAMP. Its leadership said the old name discouraged cities, counties, courts, schools and tribal governments from participating, and the rebrand supports "whole-of-state" models in which a state shares services with local agencies.[^s1]

The core idea is to verify a provider once and let many governments rely on that result, instead of each agency running its own security questionnaire.[^s1] A program management office (PMO) receives continuous security reporting from providers and shares it with participating government members.[^s1]

## How verification works

Providers join as private-sector members, then pursue one of several statuses. GovRAMP builds them on NIST controls and offers packages aligned to Low, Moderate and High impact levels, plus a Moderate package with a CJIS overlay for criminal justice data.[^s2] North Carolina describes the framework as based on NIST SP 800-53 Revision 5.[^s4]

- **Security Snapshot / Progressing Snapshot** — readiness tools scored against the top 40 controls, with no third-party assessor required.[^s2][^s3]
- **Core** — a 12-month, PMO-validated assessment of 60 NIST controls with quarterly continuous monitoring.[^s3]
- **Ready** — 80 controls, assessed by an independent third-party assessment organization (3PAO), with monthly monitoring and an annual assessment.[^s2][^s3]
- **Provisionally Authorized / Authorized** — more than 300 controls with the same 3PAO-plus-PMO structure; Authorized is the program's highest level.[^s2][^s3]

A **FedRAMP Fast Track** lets providers submit existing federal artifacts (readiness and security assessment reports and continuous-monitoring documentation) for the PMO to review against GovRAMP requirements, cutting duplicate work.[^s2] GovRAMP's own pages don't describe this as automatic reciprocity, so a FedRAMP authorization is an input to verification rather than a substitute for it.[^s2]

## Why practitioners are hearing about it now

States are writing GovRAMP into procurement. North Carolina began adding GovRAMP-aligned risk requirements to new cloud contracts on April 1, 2026, with an on-ramp period, and makes full compliance mandatory for cloud contracts from April 1, 2027; existing contracts align at renewal.[^s4] Georgia's policy took effect for new cloud procurements on October 1, 2026 and becomes mandatory for all cloud procurements on July 1, 2027, with existing contracts aligning on renewal, extension or major modification.[^s5] Georgia lists Core, Ready, Provisionally Authorized and Authorized as the relevant statuses, and stresses that GovRAMP status doesn't replace its own policies or guarantee an agency can use a product.[^s5]

## GovRAMP in Salesforce projects

For a Salesforce public-sector deal, the compliance question shifts from "is Salesforce authorized?" to "which offering, at which status, for which state's rules?" Salesforce's compliance listing for Government Cloud Plus shows FedRAMP High, CJIS, TX-RAMP and DoD IL2 documents, among others.[^s6] Those are the artifacts a team would bring to a GovRAMP Fast Track review or a state security office, but they are not themselves a GovRAMP status.[^s2][^s6] Practical gotchas:

- **Verify status in GovRAMP's directory, per product.** Status attaches to a specific cloud offering, and Georgia points buyers to the Program Participants directory to confirm it.[^s5]
- **Mind the boundary.** Compliance documents are published per Salesforce service, so check that every service in the solution has its own evidence.[^s6]
- **Expect continuous monitoring.** States explicitly expect ongoing reporting after the initial assessment, not a one-time certificate.[^s4][^s5]

## Connections

GovRAMP sits under the broader family of security compliance frameworks (`kt:security-compliance-frameworks`) and `dependsOn` the NIST SP 800-53 control catalogue (`kt:nist-sp-800-53`).[^s4] It `contrastsWith` FedRAMP (`kt:fedramp`): it copies the federal model and accepts FedRAMP artifacts through Fast Track, but serves state and local buyers with its own statuses.[^s1][^s2] Continuous monitoring (`kt:continuous-monitoring`) is a built-in part of every verified status.[^s3] Its CJIS overlay links it to the CJIS Security Policy (`kt:cjis-security-policy`).[^s2] Government Cloud Plus (`kt:government-cloud-plus`) holds the federal and Texas TX-RAMP (`kt:tx-ramp`) documents that state reviewers typically ask for.[^s6]

## Sources

[^s1]: StateTech Magazine, "StateRAMP Rebrands to GovRAMP: PerfCon". https://statetechmagazine.com/article/2025/04/stateramp-rebrands-to-govramp-perfcon (accessed 2026-11-13)
[^s2]: GovRAMP, "GovRAMP for Service Providers". https://govramp.org/providers/ (accessed 2026-11-13)
[^s3]: GovRAMP, "GovRAMP Introduces Core Status". https://govramp.org/?p=16489 (accessed 2026-11-13)
[^s4]: North Carolina Department of Information Technology, "GovRAMP Adoption". https://it.nc.gov/programs/cybersecurity-risk-management/esrmo-initiatives/govramp-adoption (accessed 2026-11-13)
[^s5]: Georgia Technology Authority, "GovRAMP Adoption". https://gta.georgia.gov/node/20221 (accessed 2026-11-13)
[^s6]: Salesforce, "Government Cloud Plus" compliance service page. https://compliance.salesforce.com/en/services/salesforce-government-cloud-plus-hyperforce (accessed 2026-11-13)
