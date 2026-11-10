---
id: kt:authority-to-operate
type: ExternalConcept
title: Authority to Operate
aliases: [Authorization to Operate, agency authorization to operate, approval to operate, security authorization, agency ATO]
domain: public-sector-and-compliance
summary: >-
  The formal, risk-based decision by a senior US federal official (the authorizing official) to let an information
  system operate and to accept its residual risk; for a Salesforce government org it is the agency's own sign-off,
  usually issued by reusing the provider's FedRAMP security package.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks, kt:nist-risk-management-framework]
related: [kt:fisma, kt:government-cloud-plus, kt:fedramp-high, kt:public-sector-solutions]
relations:
  - {predicate: contrastsWith, object: kt:fedramp}
  - {predicate: dependsOn, object: kt:nist-sp-800-53}
  - {predicate: dependsOn, object: kt:continuous-monitoring}
sources:
  - id: s1
    title: "authorization to operate (ATO) — Glossary"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/glossary/term/authorization_to_operate
    type: standards-body
    accessed: 2026-11-10
  - id: s2
    title: "Agency Authorization Playbook — Authorization"
    publisher: FedRAMP (GSA)
    url: https://www.fedramp.gov/legacy/playbook/agency/authorization/authorization/
    type: government
    accessed: 2026-11-10
  - id: s3
    title: "Reusing Authorizations for Cloud Products Quick Guide"
    publisher: FedRAMP (GSA)
    url: https://www.fedramp.gov/assets/resources/documents/Reusing_Authorizations_for_Cloud_Products_Quick_Guide.pdf
    type: government
    accessed: 2026-11-10
  - id: s4
    title: "How can an agency reuse an existing security package for a FedRAMP Authorized product?"
    publisher: FedRAMP Help Center (GSA)
    url: https://help.fedramp.gov/hc/en-us/articles/27702813350555-How-can-an-agency-reuse-an-existing-security-package-for-a-FedRAMP-Authorized-product
    type: government
    accessed: 2026-11-10
  - id: s5
    title: "FedRAMP High — Salesforce Compliance"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/fedramp-high
    type: official-docs
    accessed: 2026-11-10
  - id: s6
    title: "Salesforce Launches Government Cloud Plus, Achieves FedRAMP Provisional Authority to Operate at the High Security Impact Level"
    publisher: Salesforce
    url: https://www.salesforce.com/news/press-releases/2020/06/18/salesforce-launches-government-cloud-plus-achieves-fedramp-provisional-authority-to-operate-at-the-high-security-impact-level/
    type: news
    accessed: 2026-11-10
created: 2026-11-10
---

# Authority to Operate

An Authority to Operate (ATO; NIST's glossary spells it "authorization to operate") is a senior federal official's formal decision to let an information system run, accepting the risk that remains once an agreed set of security and privacy controls is in place.[^s1] The decision also covers common controls that agency systems inherit, and it is granted for a defined period under terms the authorizing official sets.[^s1] NIST notes that the older phrase "approval to operate" was retired from the Risk Management Framework in 2010, and lists "security authorization" as a synonym.[^s1] For a Salesforce public-sector project, the ATO is the gate between a configured org and go-live: no agency ATO, no production agency data.

## Where the definition comes from

The glossary entry traces the term to OMB Circular A-130 (2016) and repeats it in NIST SP 800-37 Rev. 2, SP 800-53 Rev. 5 and SP 800-53A Rev. 5, as well as CNSSI 4009 for national security systems.[^s1] In other words, the ATO is the "Authorize" outcome of the NIST Risk Management Framework, and the controls it weighs are the SP 800-53 controls selected for the system.[^s1] The same glossary page carries a separate, unrelated ATO meaning for PIV credential issuers under SP 800-79-2, which is easy to confuse in search results.[^s1]

## How an agency issues an ATO for a cloud service

FedRAMP's agency playbook describes the authorizing official (AO) as the person who issues the ATO for a cloud service offering, and stresses that the decision is risk-based.[^s2] Before signing, the agency reviews the authorization package: the System Security Plan and its appendices, the Security Assessment Plan, the Security Assessment Report and the Plan of Action and Milestones, looking for inconsistencies between control narratives, diagrams, findings and open items.[^s2] The agency must formally accept operationally required risks, such as essential components left outside the tested boundary, and approve deviation requests such as risk adjustments and false positives.[^s2] FedRAMP offers an ATO letter template, but the closeout process differs by agency, and testing of the customer's own controls in the agency's GRC tool may happen before or after the ATO is signed.[^s2] FedRAMP labels this playbook legacy content while it moves to consolidated rules for 2026, so check current requirements before relying on its details.[^s2]

## Reusing a FedRAMP package

Most agencies adopting Salesforce do not commission a fresh assessment. If an offering is listed as FedRAMP Authorized on the Marketplace, its package is available for reuse: the agency requests access, reviews the package and issues its own ATO based on that review.[^s4] FedRAMP's quick guide adds the mechanics:

- Access is requested with a signed Package Access Request Form and NDA; it lasts 60 days and can be extended in 30-day increments.[^s3]
- The agency studies the Customer Implementation Summary and Customer Responsibility Matrix to learn which controls it must implement itself.[^s3]
- It decides whether its data types or mission require controls beyond the authorized baseline before issuing the ATO.[^s3]
- The signed ATO letter is emailed to the FedRAMP PMO, which gives the agency's users permanent package access.[^s3]

The quick guide also cites the A-130 requirement that each system be authorized individually, with explicit risk acceptance, so another agency's ATO is evidence, not a substitute.[^s3]

## ATO versus P-ATO in the Salesforce context

A provisional ATO (P-ATO) is issued at the program level rather than by the consuming agency. Salesforce Government Cloud Plus received a P-ATO at the high impact level from the FedRAMP Joint Authorization Board in May 2020.[^s5] Salesforce announced it as a dedicated instance on AWS GovCloud (US) suitable for the most sensitive unclassified data, with the JAB providing continuous monitoring.[^s6] Each agency still signs its own ATO against that package, and afterwards it keeps reviewing the provider's monthly continuous monitoring deliverables; FedRAMP suggests multi-agency groups to share that work.[^s3]

## Connections

The ATO sits under security compliance frameworks (`kt:security-compliance-frameworks`) and is the authorization outcome of the NIST Risk Management Framework (`kt:nist-risk-management-framework`).[^s1] It `dependsOn` the SP 800-53 controls it weighs (`kt:nist-sp-800-53`) and on continuous monitoring (`kt:continuous-monitoring`) to stay valid.[^s1][^s3] It `contrastsWith` FedRAMP (`kt:fedramp`): FedRAMP produces a reusable package, while the ATO is each agency's own risk acceptance.[^s4] FISMA (`kt:fisma`) is the statute that requires it; Government Cloud Plus (`kt:government-cloud-plus`) and FedRAMP High (`kt:fedramp-high`) are the Salesforce environment and baseline most high-impact ATOs rely on,[^s5] and Public Sector Solutions (`kt:public-sector-solutions`) is a typical workload being authorized.

## Sources
[^s1]: NIST CSRC, "authorization to operate (ATO)". https://csrc.nist.gov/glossary/term/authorization_to_operate (accessed 2026-11-10)
[^s2]: FedRAMP, "Agency Authorization Playbook — Authorization". https://www.fedramp.gov/legacy/playbook/agency/authorization/authorization/ (accessed 2026-11-10)
[^s3]: FedRAMP, "Reusing Authorizations for Cloud Products Quick Guide". https://www.fedramp.gov/assets/resources/documents/Reusing_Authorizations_for_Cloud_Products_Quick_Guide.pdf (accessed 2026-11-10)
[^s4]: FedRAMP Help Center, "How can an agency reuse an existing security package for a FedRAMP Authorized product?". https://help.fedramp.gov/hc/en-us/articles/27702813350555-How-can-an-agency-reuse-an-existing-security-package-for-a-FedRAMP-Authorized-product (accessed 2026-11-10)
[^s5]: Salesforce, "FedRAMP High — Salesforce Compliance". https://compliance.salesforce.com/en/fedramp-high (accessed 2026-11-10)
[^s6]: Salesforce, "Salesforce Launches Government Cloud Plus, Achieves FedRAMP Provisional Authority to Operate at the High Security Impact Level". https://www.salesforce.com/news/press-releases/2020/06/18/salesforce-launches-government-cloud-plus-achieves-fedramp-provisional-authority-to-operate-at-the-high-security-impact-level/ (accessed 2026-11-10)
