---
id: kt:cjis-security-policy
type: ExternalConcept
title: CJIS Security Policy
aliases: [CJISSECPOL, FBI CJIS Security Policy, CJIS compliance, Criminal Justice Information Services Security Policy]
domain: public-sector-and-compliance
summary: >-
  The FBI Criminal Justice Information Services (CJIS) Division's minimum security requirements for any agency,
  contractor or cloud provider that touches Criminal Justice Information (CJI); Salesforce Government Cloud Plus and
  MuleSoft Government Cloud publish CJIS attestations for law-enforcement customers.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:government-cloud-plus, kt:multi-factor-authentication, kt:mulesoft-anypoint-platform, kt:public-sector-solutions]
relations:
  - {predicate: dependsOn, object: kt:nist-sp-800-53}
  - {predicate: contrastsWith, object: kt:fedramp}
sources:
  - id: s1
    title: "CJIS Security Policy v6.0 (CJISSECPOL), 2024-12-27"
    publisher: Florida Department of Law Enforcement
    url: https://www.fdle.state.fl.us/CJJIS/CJIS_Security_Policy_v6-0_20241227-(2).aspx
    type: government
    accessed: 2026-11-06
  - id: s2
    title: "CJIS Policy & Documents"
    publisher: Texas Department of Public Safety
    url: https://www.dps.texas.gov/node/5816
    type: government
    accessed: 2026-11-06
  - id: s3
    title: "FBI CJIS Security Policy"
    publisher: Indiana Data & Communication System (IDACS)
    url: https://secure.in.gov/idacs/system-security/fbi-cjis-security-policy
    type: government
    accessed: 2026-11-06
  - id: s4
    title: "CJIS (Compliance category page)"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/categories/cjis
    type: official-docs
    accessed: 2026-11-06
  - id: s5
    title: "CJIS - Salesforce Government Cloud Plus"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/documents/a006e000013GLo5AAG
    type: official-docs
    accessed: 2026-11-06
created: 2026-11-06
---

# CJIS Security Policy

The CJIS Security Policy (CJISSECPOL) is the rulebook the FBI's Criminal Justice Information Services Division sets for protecting Criminal Justice Information (CJI) such as criminal history records and fingerprints. It defines a minimum set of security requirements for criminal justice agencies and noncriminal justice agencies that reach FBI CJIS systems, and it covers CJI across its whole lifecycle, at rest and in transit.[^s3] The policy is prepared by the FBI CJIS Information Security Officer and approved by the CJIS Advisory Policy Board and the Compact Council, and it explicitly reaches contractors and private entities that operate in support of justice services, which is how it lands on SaaS vendors like Salesforce.[^s1]

In practice CJIS works differently from a product authorization like FedRAMP. Compliance is audited at the agency level by the state's CJIS Systems Agency (Texas DPS, for instance, publishes its own technical audit framework for scoring findings), while a vendor such as Salesforce offers an independent assessment showing its controls meet the policy, which customers then build on.[^s2][^s5]

## How it is structured

Version 6.0 (dated 27 December 2024) reorganized the policy into policy areas and control families whose identifiers (AC-2, IA-5, AU-11 and so on) mirror the NIST SP 800-53 catalog.[^s1] Texas DPS describes the newer v6.1, released 25 June 2026, as aligned with NIST SP 800-53 Revision 5 and adding updated controls for cloud computing environments.[^s2]

Each state's CJIS Systems Agency (CSA) runs the security program for its user community; its head appoints a CJIS Systems Officer, a role that cannot be outsourced, who in turn appoints an Information Security Officer.[^s1] Contractors with access to CJI are bound by the CJIS Security Addendum (Appendix H of the policy), and Texas DPS states that every contractor employee must sign it before access is granted.[^s1][^s2]

## Requirements practitioners meet in a Salesforce org

Many CJIS controls map directly to org configuration. Examples verified in v6.0 this run:[^s1]

- **Identification and authentication (IA-2):** multi-factor authentication for privileged and non-privileged accounts, both marked Priority 1.[^s1]
- **Passwords (IA-5):** subscriber-chosen memorized secrets of at least 8 characters, and no more than five failed attempts.[^s1]
- **Logon lockout (AC-7):** lock after five consecutive invalid attempts within 15 minutes, until an administrator releases the account.[^s1]
- **Session lock (AC-11):** lock the device after at most 30 minutes of inactivity.[^s1]
- **Account management (AC-2):** disable accounts inactive for 90 calendar days (within a week), and remove temporary or emergency accounts automatically within 72 hours.[^s1]
- **Audit (AU-11):** keep audit records for at least one year.[^s1]

The data-protection families (transmission confidentiality, cryptographic protection and protection at rest) also apply, as do personnel screening rules that require fingerprints for contractor staff before access.[^s1]

## Timelines and gotchas

The modernized policy is phased in. Under v6.0, pre-v5.9 requirements and Priority 1 controls became sanctionable on 1 October 2024, while Priority 2–4 controls sit in a zero-cycle period through 30 September 2027.[^s1] States audit against their own adopted version: Texas, for example, conducts all CJIS audits through 31 March 2027 against v5.9.5 and recommends gap assessments for v6.1 now.[^s2] States may also add supplements; Texas publishes its own Security Policy Supplement.[^s2] Always confirm with the customer's CSA which version and supplement apply.

## Salesforce coverage

Salesforce's compliance portal lists CJIS material for Salesforce Government Cloud Plus and MuleSoft Government Cloud, both hosted on AWS.[^s4] For Government Cloud Plus, an independent assessment found its controls meet CJIS Security Policy version 5.9.1; the attestation applies only to the environment sold as Government Cloud Plus (FedRAMP ID FR2003061248) and is not downloadable, so customers request it from their account representative or the Public Sector Documentation Portal.[^s4][^s5] Commercial Salesforce orgs are not in that scope, and the assessed version trails the current policy, so agencies still own the gap analysis and their share of controls (users, MFA, sessions, audit retention).[^s4][^s5]

## Connections

CJIS sits under `kt:security-compliance-frameworks` as a sector-specific regime and draws its control vocabulary from `kt:nist-sp-800-53`.[^s1][^s2] It contrasts with `kt:fedramp`: FedRAMP authorizes a cloud offering centrally, while CJIS compliance is assessed per agency by the state CSA.[^s1] In Salesforce terms, `kt:government-cloud-plus` and MuleSoft Government Cloud (`kt:mulesoft-anypoint-platform`) are the offerings with CJIS attestations, `kt:public-sector-solutions` is the industry product law-enforcement agencies typically run there, and `kt:multi-factor-authentication` is the org feature that satisfies the policy's IA-2 requirement.[^s1][^s4][^s5]

## Sources

[^s1]: Florida Department of Law Enforcement, "CJIS Security Policy v6.0 (CJISSECPOL), 2024-12-27". https://www.fdle.state.fl.us/CJJIS/CJIS_Security_Policy_v6-0_20241227-(2).aspx (accessed 2026-11-06)
[^s2]: Texas Department of Public Safety, "CJIS Policy & Documents". https://www.dps.texas.gov/node/5816 (accessed 2026-11-06)
[^s3]: Indiana Data & Communication System, "FBI CJIS Security Policy". https://secure.in.gov/idacs/system-security/fbi-cjis-security-policy (accessed 2026-11-06)
[^s4]: Salesforce, "CJIS (Compliance category page)". https://compliance.salesforce.com/en/categories/cjis (accessed 2026-11-06)
[^s5]: Salesforce, "CJIS - Salesforce Government Cloud Plus". https://compliance.salesforce.com/en/documents/a006e000013GLo5AAG (accessed 2026-11-06)
