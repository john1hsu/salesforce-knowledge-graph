---
id: kt:governance-risk-and-compliance
type: ExternalConcept
title: Governance, Risk and Compliance
aliases: [GRC, "governance, risk, and compliance", "security GRC", integrated GRC]
domain: public-sector-and-compliance
summary: >-
  The integrated management discipline, named and modeled by OCEG, that aligns how an organization sets direction
  (governance), handles uncertainty (risk management) and meets legal, regulatory and policy obligations (compliance);
  for a Salesforce org it is the program that decides which frameworks apply, which risks are accepted, and which
  controls are evidenced.
release: "Winter '27"
status: concept
broader: [kt:corporate-governance]
related: [kt:salesforce-governance, kt:data-governance, kt:shared-responsibility-model, kt:nist-cybersecurity-framework]
relations:
  - {predicate: hasPart, object: kt:security-compliance-frameworks}
sources:
  - id: s1
    title: "What Is GRC (Governance, Risk, and Compliance)?"
    publisher: OCEG
    url: https://oceg.org/ideas/what-is-grc
    type: community
    accessed: 2026-11-14
  - id: s2
    title: "The NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29, PDF)"
    publisher: NIST
    url: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf
    type: standards-body
    accessed: 2026-11-14
  - id: s3
    title: "Manage Security Risks (Cybersecurity Training for Executives)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/executive-security-awareness/manage-security-risks
    type: official-learning
    accessed: 2026-11-14
  - id: s4
    title: "Manage Compliance Risks and Implement Controls (Cybersecurity Compliance Analyst Responsibilities)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/cybersecurity-compliance-analyst-responsibilities/manage-compliance-risks-and-implement-controls
    type: official-learning
    accessed: 2026-11-14
  - id: s5
    title: "Make Solutions Trusted (Salesforce Well-Architected)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-well-architected/make-solutions-secure
    type: official-learning
    accessed: 2026-11-14
  - id: s6
    title: "Trust and Compliance Documentation"
    publisher: Salesforce
    url: https://www.salesforce.com/company/legal/trust-and-compliance-documentation/
    type: official-docs
    accessed: 2026-11-14
created: 2026-11-14
---

# Governance, Risk and Compliance

Governance, risk and compliance (GRC) is the practice of running three traditionally separate programs as one system. OCEG, the nonprofit that coined the acronym and says it was using it as early as 2002, defines GRC as the integrated capabilities that let an organization reliably achieve its objectives, address uncertainty and act with integrity, an outcome it calls "Principled Performance."[^s1] OCEG's founder published the first peer-reviewed academic paper on the subject in 2007.[^s1] GRC is not a product or a single department: OCEG stresses that integration needs neither one mega-department nor one software system, only shared processes and information.[^s1]

## The three parts

- **Governance** sets direction: objectives, policies, roles, accountability and oversight of how well strategy is carried out.[^s1][^s2]
- **Risk management** identifies uncertainty that could block those objectives and decides how much of it to tolerate.[^s1][^s4]
- **Compliance** proves the organization meets laws, regulations, contracts and its own policies, usually through controls and audits.[^s1][^s4]

OCEG argues that running these as silos raises cost, hides risk and produces too many unpleasant surprises, and its GRC Capability Model (the "Red Book," now at version 3.5) organizes the integrated alternative into four components: Learn, Align, Perform and Review.[^s1]

## How it shows up in security frameworks

NIST's Cybersecurity Framework 2.0 made governance an explicit Function, Govern (GV), placed at the center because it shapes how the other five Functions are carried out.[^s2] Its categories read like a GRC charter: organizational context, risk management strategy (including risk appetite and tolerance), roles and authorities, policy, oversight, and cybersecurity supply chain risk management.[^s2] Subcategory GV.OC-03 asks organizations to understand and manage their legal, regulatory and contractual cybersecurity requirements, and NIST positions Govern as the bridge that folds cybersecurity into enterprise risk management.[^s2]

## Risk treatment and controls

Salesforce's Trailhead material on the compliance analyst role describes the day-to-day mechanics. Compliance gaps are logged as findings with an owner and a plan of action; each risk is then mitigated with controls, accepted when it falls within tolerance (with exceptions signed off by executives or the board), or transferred, for example through cyber insurance or outsourcing.[^s4] Controls come in three kinds: management controls such as regulations and policies, operational controls such as a change advisory board, and technical controls such as automated change tooling or allowlisting.[^s4] The policies documenting those controls become the evidence base for internal and external audits.[^s4] Trailhead's executive security training assigns this work to a security GRC team, with control executives accountable for ensuring control owners perform controls on time and for tracking corrective actions.[^s3]

## Applying GRC to a Salesforce org

- **Inherit what Salesforce attests.** Salesforce's SPARC documents describe each service's architecture, audits and certifications, and the Infrastructure and Sub-processors document lists where data is stored and processed.[^s6]
- **Own the customer side.** Configuration, users and data remain the customer's to govern, so a GRC program maps each applicable obligation to org-level controls and owners.[^s4][^s6]
- **Design for evidence.** Salesforce Well-Architected treats a compliant solution as one that follows legal and ethical guidelines, recommending a maintained data dictionary with field classifications and documented data storage locations for residency rules.[^s5]
- **Watch for change.** Salesforce publishes a change log and sub-processor notifications that a GRC team can subscribe to as inputs to periodic risk review.[^s6]

## Connections

GRC sits under corporate governance (`kt:corporate-governance`, broader), the board-level system it serves.[^s1] It `hasPart` security compliance frameworks (`kt:security-compliance-frameworks`), the standards and regulations its compliance arm maps controls to, and it relates to the NIST Cybersecurity Framework (`kt:nist-cybersecurity-framework`), whose Govern Function expresses GRC for cybersecurity.[^s2] Salesforce governance (`kt:salesforce-governance`) and data governance (`kt:data-governance`) are narrower, platform- and data-specific programs that a GRC function oversees and draws evidence from.[^s1][^s5] The shared responsibility model (`kt:shared-responsibility-model`) defines which controls a Salesforce customer inherits and which it must run and evidence itself.[^s6]

## Sources

[^s1]: OCEG, "What Is GRC (Governance, Risk, and Compliance)?". https://oceg.org/ideas/what-is-grc (accessed 2026-11-14)
[^s2]: NIST, "The NIST Cybersecurity Framework (CSF) 2.0" (CSWP 29). https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf (accessed 2026-11-14)
[^s3]: Salesforce Trailhead, "Manage Security Risks" (Cybersecurity Training for Executives). https://trailhead.salesforce.com/content/learn/modules/executive-security-awareness/manage-security-risks (accessed 2026-11-14)
[^s4]: Salesforce Trailhead, "Manage Compliance Risks and Implement Controls". https://trailhead.salesforce.com/content/learn/modules/cybersecurity-compliance-analyst-responsibilities/manage-compliance-risks-and-implement-controls (accessed 2026-11-14)
[^s5]: Salesforce Trailhead, "Make Solutions Trusted" (Salesforce Well-Architected). https://trailhead.salesforce.com/content/learn/modules/salesforce-well-architected/make-solutions-secure (accessed 2026-11-14)
[^s6]: Salesforce, "Trust and Compliance Documentation". https://www.salesforce.com/company/legal/trust-and-compliance-documentation/ (accessed 2026-11-14)
