---
id: kt:tx-ramp
type: ExternalConcept
title: TX-RAMP
aliases: [Texas Risk and Authorization Management Program, TX-RAMP certification]
domain: public-sector-and-compliance
summary: >-
  Texas's state program, created by Senate Bill 475 and run by the Department of Information Resources, that
  certifies cloud services used by Texas state agencies and public universities at Level 1 (low impact) or Level 2
  (confidential data, moderate or high impact), with provisional status, reciprocity for FedRAMP and GovRAMP, and
  ongoing continuous monitoring.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:govramp, kt:government-cloud-plus, kt:data-cloud, kt:public-sector-solutions]
relations:
  - {predicate: contrastsWith, object: kt:fedramp}
  - {predicate: hasPart, object: kt:continuous-monitoring}
  - {predicate: dependsOn, object: kt:data-classification}
sources:
  - id: s1
    title: "TX-RAMP Frequently Asked Questions (FAQs)"
    publisher: Texas Department of Information Resources
    url: https://dir.texas.gov/information-security/texas-risk-and-authorization-management-program-tx-ramp/tx-ramp-frequently
    type: government
    accessed: 2026-11-25
  - id: s2
    title: "TX-RAMP Eligibility and Requirements"
    publisher: Texas Department of Information Resources
    url: https://dir.texas.gov/information-security/texas-risk-and-authorization-management-program-tx-ramp/tx-ramp-eligibility
    type: government
    accessed: 2026-11-25
  - id: s3
    title: "Texas Risk and Authorization Management Program (TX-RAMP)"
    publisher: Texas Department of Information Resources
    url: https://dir.texas.gov/information-security/texas-risk-and-authorization-management-program-tx-ramp
    type: government
    accessed: 2026-11-25
  - id: s4
    title: "State of Texas"
    publisher: GovRAMP
    url: https://govramp.org/programs/state-of-texas
    type: standards-body
    accessed: 2026-11-25
  - id: s5
    title: "Texas Risk and Authorization Management Program (TX-RAMP)"
    publisher: UT Southwestern Medical Center
    url: https://www.utsouthwestern.edu/employees/information-security/tx-ramp/index.html
    type: academic
    accessed: 2026-11-25
  - id: s6
    title: "TX-RAMP - Salesforce Services and Additional Services"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/documents/a006e0000161mq5AAA
    type: official-docs
    accessed: 2026-11-25
  - id: s7
    title: "TX-RAMP - Salesforce Government Cloud Plus"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/documents/a006e000013GLnlAAG
    type: official-docs
    accessed: 2026-11-25
  - id: s8
    title: "TX-RAMP - Data Cloud"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/documents/a006e0000161qY6AAI
    type: official-docs
    accessed: 2026-11-25
created: 2026-11-25
---

# TX-RAMP

TX-RAMP, the Texas Risk and Authorization Management Program, is the State of Texas's standard way to assess, certify and continuously monitor cloud services that process the data of Texas state agencies.[^s3] It grew out of Senate Bill 475 of the 87th Legislature, and Texas Government Code section 2054.0593 now requires state agencies to contract only for cloud computing services that comply with the program.[^s1] The Department of Information Resources (DIR) has operated it; DIR notes that House Bill 150 of the 89th Legislature moved its cybersecurity functions to the new Texas Cyber Command.[^s3]

"State agency" here is broad: it includes institutions of higher education and public community colleges, so university systems such as UT Southwestern apply the rules to every third-party cloud service that stores, processes or transmits their data.[^s2][^s5] Only services that meet the statutory definition of cloud computing are in scope, and certification attaches to a specific product, not to a vendor as a whole.[^s2][^s5]

## Certification levels

TX-RAMP sizes the requirement to the data and the system's impact:[^s2][^s1]

- **Level 1** — the minimum for public or non-confidential data and low-impact systems.[^s2]
- **Level 2** — the minimum for confidential or regulated data in moderate- or high-impact systems.[^s2]
- **Provisional** — lets an agency contract for up to 18 months while the provider works toward full certification; it starts with a request form and an acknowledgment and inventory questionnaire.[^s2][^s1]

DIR publishes the controls for each level as a set of TX-RAMP security control baselines, and the contracting agency decides the final minimum level for a given purchase.[^s2][^s1] A low-impact service that holds no confidential state data beyond login details can fall out of scope entirely.[^s5] Full certifications are valid for three years if compliance is maintained, and DIR sends renewal reminders 12 and 6 months before expiry.[^s1] The program charges no fee, does not require a third-party assessment organization, and accepts a fixed list of existing artifacts (such as SOC 2 Type 2, ISO 27001 and HITRUST) to speed review.[^s1]

## Reciprocity with FedRAMP and GovRAMP

Providers can reach a level through DIR's own assessment or by evidence of an equivalent external authorization: FedRAMP Low or StateRAMP Category 1 for Level 1, and FedRAMP Moderate or StateRAMP Category 2 for Level 2.[^s2] Since October 30, 2024 these products are no longer added automatically; the provider must file a TX-RAMP request, and the reciprocal certification lasts only while the external status is maintained.[^s1] GovRAMP (the renamed StateRAMP) says its Core, Ready, Provisional and Authorized statuses satisfy Level 2, that FedRAMP LI-SaaS is not accepted, and that reciprocity runs one way: a TX-RAMP certificate does not confer GovRAMP status.[^s4]

## Continuous monitoring

Certified providers carry the monitoring burden: annual vulnerability reporting at Level 1, quarterly reporting at Level 2, and disclosure of any breach to DIR within 48 hours of discovery.[^s1] Services certified through FedRAMP or GovRAMP report through those programs instead, so DIR advises agencies to add contract clauses requiring notice if that status changes.[^s1] Agencies may not renew a contract for a non-compliant service, and a lapse can lead to revocation of use.[^s5][^s1]

## TX-RAMP in Salesforce projects

Salesforce publishes TX-RAMP evidence per service on its compliance site. Salesforce Services and Additional Services hold Level 2 certification with a reporting period from May 10, 2024 to May 10, 2027.[^s6] Data Cloud holds Level 2 for May 28, 2024 to May 28, 2027.[^s8] Government Cloud Plus holds Level 2 from November 17, 2023, and the same page notes that the Education Suite has only a provisional authorization, with a recommendation that customers make a risk-based decision about it.[^s7] The documents themselves sit behind a compliance-site login.[^s6] Practical checks for a Texas agency or university deal:

- **Map every service in the design.** Certification is per product, so an add-on without its own TX-RAMP evidence is a gap.[^s5][^s6]
- **Watch the end dates.** The three-year terms above expire in 2027, so plan for renewal evidence during long contracts.[^s1][^s6]
- **Confirm in DIR's list.** DIR maintains the certified products list and warns some entries may be missing, so verify before award.[^s3][^s1]

## Connections

TX-RAMP is one of the security compliance frameworks (`kt:security-compliance-frameworks`) and a state-level sibling of GovRAMP (`kt:govramp`), whose statuses it accepts for Level 2.[^s4] It `contrastsWith` FedRAMP (`kt:fedramp`): it reuses FedRAMP Low and Moderate authorizations but issues its own levels for Texas buyers.[^s2] Continuous monitoring (`kt:continuous-monitoring`) is part of every certification, and the level an agency needs `dependsOn` how its data is classified (`kt:data-classification`).[^s1][^s2] Government Cloud Plus (`kt:government-cloud-plus`), Data Cloud (`kt:data-cloud`) and the core services behind Public Sector Solutions (`kt:public-sector-solutions`) carry Salesforce's Level 2 evidence.[^s6][^s7][^s8]

## Sources

[^s1]: Texas Department of Information Resources, "TX-RAMP Frequently Asked Questions (FAQs)". https://dir.texas.gov/information-security/texas-risk-and-authorization-management-program-tx-ramp/tx-ramp-frequently (accessed 2026-11-25)
[^s2]: Texas Department of Information Resources, "TX-RAMP Eligibility and Requirements". https://dir.texas.gov/information-security/texas-risk-and-authorization-management-program-tx-ramp/tx-ramp-eligibility (accessed 2026-11-25)
[^s3]: Texas Department of Information Resources, "Texas Risk and Authorization Management Program (TX-RAMP)". https://dir.texas.gov/information-security/texas-risk-and-authorization-management-program-tx-ramp (accessed 2026-11-25)
[^s4]: GovRAMP, "State of Texas". https://govramp.org/programs/state-of-texas (accessed 2026-11-25)
[^s5]: UT Southwestern Medical Center, "Texas Risk and Authorization Management Program (TX-RAMP)". https://www.utsouthwestern.edu/employees/information-security/tx-ramp/index.html (accessed 2026-11-25)
[^s6]: Salesforce, "TX-RAMP - Salesforce Services and Additional Services". https://compliance.salesforce.com/en/documents/a006e0000161mq5AAA (accessed 2026-11-25)
[^s7]: Salesforce, "TX-RAMP - Salesforce Government Cloud Plus". https://compliance.salesforce.com/en/documents/a006e000013GLnlAAG (accessed 2026-11-25)
[^s8]: Salesforce, "TX-RAMP - Data Cloud". https://compliance.salesforce.com/en/documents/a006e0000161qY6AAI (accessed 2026-11-25)
