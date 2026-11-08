---
id: kt:fips-200
type: ExternalConcept
title: FIPS 200
aliases: [FIPS PUB 200, "Minimum Security Requirements for Federal Information and Information Systems", FIPS 200 minimum security requirements]
domain: public-sector-and-compliance
summary: >-
  Federal Information Processing Standard 200, the NIST standard that sets minimum security requirements in 17
  security-related areas for federal information systems and directs agencies to meet them by selecting the
  NIST SP 800-53 control baseline matching the system's FIPS 199 impact level; the bridge between categorization
  and the control baselines behind FedRAMP authorizations of services such as Salesforce Government Cloud Plus.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:fips-199, kt:nist-sp-800-53, kt:nist-sp-800-53b, kt:government-cloud-plus]
relations:
  - {predicate: dependsOn, object: kt:fips-199}
  - {predicate: dependsOn, object: kt:nist-sp-800-53}
  - {predicate: usedBy, object: kt:fedramp}
sources:
  - id: s1
    title: "FIPS 200, Minimum Security Requirements for Federal Information and Information Systems"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/pubs/fips/200/final
    type: standards-body
    accessed: 2026-11-08
  - id: s2
    title: "ITL Bulletin, March 2006: Minimum Security Requirements for Federal Information and Information Systems (FIPS 200)"
    publisher: NIST Information Technology Laboratory
    url: https://csrc.nist.gov/files/pubs/shared/itlb/itlbul2006-03.pdf
    type: standards-body
    accessed: 2026-11-08
  - id: s3
    title: "Request for Comments on Draft FIPS 200 (Federal Register Vol. 70, No. 135)"
    publisher: U.S. Government Publishing Office (govinfo)
    url: https://www.govinfo.gov/content/pkg/FR-2005-07-15/pdf/05-13992.pdf
    type: government
    accessed: 2026-11-08
  - id: s4
    title: "Control Baselines for Information Systems and Organizations: NIST Publishes SP 800-53B"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/news/2020/control-baselines-nist-publishes-sp-800-53b
    type: standards-body
    accessed: 2026-11-08
  - id: s5
    title: "Rev5 Transition"
    publisher: FedRAMP (GSA)
    url: https://fedramp.gov/rev5/rev5-transition
    type: government
    accessed: 2026-11-08
  - id: s6
    title: "Salesforce FedRAMP and Government Cloud"
    publisher: Salesforce
    url: https://www.salesforce.com/fedramp/
    type: official-docs
    accessed: 2026-11-08
created: 2026-11-08
---

# FIPS 200

FIPS 200, *Minimum Security Requirements for Federal Information and Information Systems*, is the NIST standard that tells US federal agencies what baseline of security they must provide for each category of system. Published in March 2006, it is the second of the two standards FISMA required, after FIPS 199, and it superseded the older NIST SP 800-26 self-assessment guide.[^s1] Its purpose is to set a minimum level of security due diligence and to make control selection more consistent and repeatable across agencies through a risk-based process.[^s1] For Salesforce architects it explains why a government workload lands on a particular control baseline, and therefore which authorized environment can host it.

## Scope and status

The standard covers federal government information that is not classified under the relevant executive orders or the Atomic Energy Act, and federal information systems other than national security systems.[^s2] State, local and tribal governments and private critical-infrastructure operators were encouraged, but not required, to consider it.[^s3] FISMA's information security program obligations extend to systems that a contractor or another organization provides or manages for an agency, which is how commercial cloud services come into scope.[^s2] FIPS 200 took effect on approval on 9 March 2006, and agencies were expected to comply within one year.[^s2] The CSRC page still lists the 2006 final as the current edition, with no withdrawal shown.[^s1]

## The 17 security-related areas

FIPS 200 states its requirements as 17 security-related areas spanning management, operational and technical concerns.[^s3] They are access control; awareness and training; audit and accountability; certification, accreditation and security assessments; configuration management; contingency planning; identification and authentication; incident response; maintenance; media protection; personnel security; physical and environmental protection; planning; risk assessment; system and services acquisition; system and communications protection; and system and information integrity.[^s2] Each area is a short outcome statement, for example limiting access to authorized users and permitted transactions, or identifying and correcting flaws promptly and guarding against malicious code.[^s2] The areas map to the control families of SP 800-53; NIST's current page labels the certification and accreditation area as assessment, authorization and monitoring, the newer family name.[^s1] The acquisition area is the one that reaches third parties: it requires that providers of outsourced services protect agency information.[^s2]

## How the requirements are met

FIPS 200 does not list controls itself. The agency first categorizes the system under FIPS 199, then collapses the three ratings into one level: low only when all of confidentiality, integrity and availability are low, moderate when the highest is moderate, and high when any is high.[^s2] That level selects the low, moderate or high control baseline from NIST SP 800-53.[^s3] Agencies then tailor the baseline: scoping guidance considers technology, common controls, public access, physical conditions, size and risk; organization-specific values are set; extra controls can be added; and compensating controls may stand in for prescribed ones where justified.[^s2] Since SP 800-53 Revision 5, the low, moderate and high security baselines, plus a privacy baseline that applies at every impact level, live in the companion SP 800-53B, along with tailoring and overlay guidance.[^s4]

## How Salesforce encounters it

FedRAMP carries this scheme into cloud authorizations: its High, Moderate and Low baselines (plus a tailored LI-SaaS baseline) are aligned to SP 800-53 Revision 5.[^s5] Salesforce says Government Cloud Plus holds a JAB provisional authorization at FedRAMP Class D, formerly called FedRAMP High, and that such services are designed to meet SP 800-53 controls.[^s6] Two gotchas matter in design. First, the authorization boundary is narrower than the ecosystem: Salesforce notes that AgentExchange apps generally sit outside it, so add-ons need their own review.[^s6] Second, a provider's authorization does not move the agency's FISMA duty: the security program must still cover systems a contractor operates for it, and scoping, tailoring and supplementing the baseline remain agency decisions.[^s2]

## Connections

FIPS 200 belongs to the family of security compliance frameworks (`kt:security-compliance-frameworks`).[^s1] It `dependsOn` FIPS 199 (`kt:fips-199`, related), whose categorization must come first, and on NIST SP 800-53 (`kt:nist-sp-800-53`, related), the catalog that supplies the controls.[^s2] SP 800-53B (`kt:nist-sp-800-53b`, related) now holds the baselines and tailoring guidance FIPS 200 points to.[^s4] FIPS 200 is `usedBy` FedRAMP (`kt:fedramp`), whose baselines apply the same requirement-to-baseline method to cloud services.[^s5] Government Cloud Plus (`kt:government-cloud-plus`, related) is the Salesforce environment authorized at the top baseline.[^s6]

## Sources
[^s1]: NIST CSRC, "FIPS 200, Minimum Security Requirements for Federal Information and Information Systems". https://csrc.nist.gov/pubs/fips/200/final (accessed 2026-11-08)
[^s2]: NIST ITL, "ITL Bulletin, March 2006: Minimum Security Requirements for Federal Information and Information Systems (FIPS 200)". https://csrc.nist.gov/files/pubs/shared/itlb/itlbul2006-03.pdf (accessed 2026-11-08)
[^s3]: Federal Register via govinfo, "Request for Comments on Draft FIPS 200", Vol. 70, No. 135, 15 July 2005. https://www.govinfo.gov/content/pkg/FR-2005-07-15/pdf/05-13992.pdf (accessed 2026-11-08)
[^s4]: NIST CSRC, "Control Baselines for Information Systems and Organizations: NIST Publishes SP 800-53B". https://csrc.nist.gov/news/2020/control-baselines-nist-publishes-sp-800-53b (accessed 2026-11-08)
[^s5]: FedRAMP (GSA), "Rev5 Transition". https://fedramp.gov/rev5/rev5-transition (accessed 2026-11-08)
[^s6]: Salesforce, "Salesforce FedRAMP and Government Cloud". https://www.salesforce.com/fedramp/ (accessed 2026-11-08)
