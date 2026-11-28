---
id: kt:controlled-unclassified-information
type: ExternalConcept
title: Controlled Unclassified Information
aliases: [CUI, CUI program, CUI Basic, CUI Specified, 32 CFR Part 2002, Executive Order 13556]
domain: public-sector-and-compliance
summary: >-
  The U.S. executive-branch program, set up by Executive Order 13556 and implemented in 32 CFR Part 2002, that
  standardizes how unclassified information needing safeguarding or dissemination controls is designated, marked,
  protected and decontrolled; on nonfederal systems such as a contractor's Salesforce org, CUI Basic is protected to
  NIST SP 800-171.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:nist-sp-800-171, kt:cmmc, kt:government-cloud-plus, kt:il4-and-il5, kt:data-classification, kt:itar-and-export-controls]
relations:
  - {predicate: dependsOn, object: kt:fips-199}
sources:
  - id: s1
    title: "About Controlled Unclassified Information (CUI)"
    publisher: U.S. National Archives and Records Administration
    url: https://www.archives.gov/cui/about/
    type: government
    accessed: 2026-11-28
  - id: s2
    title: "CUI History"
    publisher: U.S. National Archives and Records Administration
    url: https://www.archives.gov/cui/cui-history
    type: government
    accessed: 2026-11-28
  - id: s3
    title: "32 CFR Part 2002 -- Controlled Unclassified Information (CUI)"
    publisher: eCFR (Office of the Federal Register)
    url: https://www.ecfr.gov/current/title-32/subtitle-B/chapter-XX/part-2002
    type: government
    accessed: 2026-11-28
  - id: s4
    title: "CUI Glossary"
    publisher: U.S. National Archives and Records Administration
    url: https://www.archives.gov/cui/registry/cui-glossary.html
    type: government
    accessed: 2026-11-28
  - id: s5
    title: "Protecting Controlled Unclassified Information: FAQs"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/Projects/protecting-controlled-unclassified-information/faqs
    type: standards-body
    accessed: 2026-11-28
  - id: s6
    title: "Salesforce Government Cloud"
    publisher: Salesforce
    url: https://www.salesforce.com/government/cloud/
    type: official-blog
    accessed: 2026-11-28
created: 2026-11-28
---

# Controlled Unclassified Information

Controlled Unclassified Information (CUI) is information that law, regulation or government-wide policy says must be safeguarded or have its dissemination controlled, but that is not classified under Executive Order 13526 or the Atomic Energy Act.[^s1] The term also names the executive-branch program that governs such information. Executive Order 13556 created the program and made the National Archives (NARA) its Executive Agent. NARA delegated that role to the Director of the Information Security Oversight Office (ISOO).[^s1][^s3]

For Salesforce practitioners, CUI is the reason many public-sector and defense-contractor implementations exist in a separate environment. Contract data, technical data and case records often carry CUI obligations, and those obligations decide which Salesforce offering, controls and assessments apply.[^s6]

## Origins and legal basis

Before the program, agencies protected sensitive unclassified information under a patchwork of their own labels and practices. The CUI program was meant to replace that with one standard across more than 100 departments and agencies and the state, local, tribal, academic and industry partners they share with.[^s2] A presidential task force was appointed in May 2009, and E.O. 13556 established the program in November 2010.[^s2] ISOO published the implementing rule, 32 CFR Part 2002, as a proposed rule in May 2015 and a final rule on 14 September 2016, effective 14 November 2016.[^s2][^s3]

Part 2002 sets policy for designating, safeguarding, disseminating, marking, decontrolling and disposing of CUI, plus self-inspection and oversight.[^s1] It applies directly to executive-branch agencies. It reaches nonfederal entities such as contractors indirectly, through the agreements and contracts under which they receive CUI.[^s3]

## Key concepts

The regulation defines CUI as information the government creates or possesses, or that an entity creates or possesses for the government, which an authority requires or permits an agency to control. It excludes classified information, and information a nonfederal entity holds in its own systems that did not come from or for an agency.[^s3]

- **CUI Registry**: NARA's online catalog of the approved CUI categories and their authorities; only listed categories count as CUI.[^s1][^s3]
- **CUI Basic**: the default subset, where the authority sets no specific handling rules, so the uniform program controls apply.[^s3][^s4]
- **CUI Specified**: the subset whose law or regulation sets its own handling controls that differ from CUI Basic; the Registry identifies these authorities.[^s3][^s4]
- **Limited dissemination controls**: Executive Agent-approved controls that an agency may apply to narrow who can receive a CUI item.[^s4]
- **Decontrol**: an authorized holder removes controls that are no longer needed, either automatically or by agency action.[^s4]

Information may be shared for any lawful government purpose, which the glossary defines broadly to include authorized activities of nonfederal partners such as state and local law enforcement.[^s2][^s4] Disclosure without such a purpose, or against a dissemination control, is an unauthorized disclosure.[^s4] Under Part 2002, decontrol does not by itself authorize public release, and an unauthorized disclosure does not decontrol the information.[^s3]

## Safeguarding and marking

Part 2002 requires agencies to treat CUI Basic as at least moderate confidentiality impact under FIPS PUB 199.[^s3] For nonfederal information systems, the rule incorporates NIST SP 800-171 as the security requirements for CUI Basic, unless the authority for a category or the agreement with the agency sets something different or stricter.[^s3] NIST explains that SP 800-171 was written as a separate publication because applying the full federal control set to nonfederal systems raised implementation concerns. It keeps moderate-baseline control language but drops federal-centric requirements and focuses on confidentiality.[^s5]

Marked documents carry a banner whose control marking is either "CONTROLLED" or "CUI", at the designating agency's choice.[^s3] NIST is non-regulatory and does not determine whether an organization complies with SP 800-171. Compliance questions go to the contracting agency or prime contractor.[^s5]

## CUI on Salesforce

Salesforce says its Government Cloud can help customers meet CMMC Level 2 and Level 3 requirements for storing and processing CUI. It notes that CMMC is built on NIST 800-171 controls, which are a subset of the NIST 800-53 controls its FedRAMP services are designed to meet.[^s6] Salesforce cites a third-party NIST SP 800-171 attestation performed against Revision 2.[^s6] Government Cloud Plus - Defense is the IL4 and IL5 offering; it requires Common Access Card login and uses salesforce.mil domains.[^s6]

Gotchas:

- **Category drives handling.** Check the Registry entry: a CUI Specified category follows its own authority's handling rules, which can differ from the CUI Basic defaults.[^s3][^s4]
- **Platform attestation is not the customer's compliance.** The org's own access model, field classification and processes still have to meet the requirements the contract imposes.[^s5][^s6]
- **Not every federal record is CUI.** Information not on the Registry is uncontrolled unclassified information, though it remains subject to FISMA.[^s3]

## Connections

CUI sits under `kt:security-compliance-frameworks` (broader) as the information category that several frameworks protect.[^s1] It `dependsOn` `kt:fips-199`, because Part 2002 sets CUI Basic at no less than moderate confidentiality impact.[^s3] It relates to `kt:nist-sp-800-171`, the requirements for CUI Basic on nonfederal systems, and to `kt:cmmc`, which assesses defense contractors against those requirements.[^s3][^s5] It relates to `kt:government-cloud-plus` and `kt:il4-and-il5`, the Salesforce environments and DoD tiers that CUI workloads use.[^s6] It relates to `kt:data-classification`, the practice of labelling data by sensitivity that CUI designation and marking formalize for federal information, and to `kt:itar-and-export-controls`, another regime that restricts who may receive sensitive unclassified defense data.[^s1][^s3]

## Sources

[^s1]: NARA, "About Controlled Unclassified Information (CUI)". https://www.archives.gov/cui/about/ (accessed 2026-11-28)
[^s2]: NARA, "CUI History". https://www.archives.gov/cui/cui-history (accessed 2026-11-28)
[^s3]: eCFR, "32 CFR Part 2002 -- Controlled Unclassified Information (CUI)". https://www.ecfr.gov/current/title-32/subtitle-B/chapter-XX/part-2002 (accessed 2026-11-28)
[^s4]: NARA, "CUI Glossary". https://www.archives.gov/cui/registry/cui-glossary.html (accessed 2026-11-28)
[^s5]: NIST CSRC, "Protecting Controlled Unclassified Information: FAQs". https://csrc.nist.gov/Projects/protecting-controlled-unclassified-information/faqs (accessed 2026-11-28)
[^s6]: Salesforce, "Salesforce Government Cloud". https://www.salesforce.com/government/cloud/ (accessed 2026-11-28)
