---
id: kt:organizational-governance
type: ExternalConcept
title: Organizational Governance
aliases: [governance of organizations, organisational governance, ISO 37000]
domain: public-sector-and-compliance
summary: >-
  The system by which any organization (company, public agency, nonprofit) is directed, overseen and held
  accountable by its governing body, benchmarked internationally by ISO 37000:2021 and structured in practice by
  the IIA's Three Lines Model; corporate governance and IT governance are its company-level and technology-level
  applications, and Salesforce governance ultimately answers to it.
release: "Winter '27"
status: concept
broader: [kt:management]
related: [kt:governance-risk-and-compliance, kt:data-governance, kt:salesforce-center-of-excellence]
relations:
  - {predicate: hasPart, object: kt:corporate-governance}
  - {predicate: hasPart, object: kt:it-governance}
sources:
  - id: s1
    title: "ISO 37000:2021 Governance of organizations — Guidance"
    publisher: ISO
    url: https://www.iso.org/standard/65036.html
    type: standards-body
    accessed: 2026-11-18
  - id: s2
    title: "ISO 37000 - the first ever international benchmark for good governance"
    publisher: ISO/TC 309
    url: https://committee.iso.org/ISO_37000_Governance
    type: standards-body
    accessed: 2026-11-18
  - id: s3
    title: "The IIA's Three Lines Model: An update of the Three Lines of Defense"
    publisher: The Institute of Internal Auditors
    url: https://www.theiia.org/globalassets/site/communication/2020/three-lines-model-updated.pdf
    type: standards-body
    accessed: 2026-11-18
  - id: s4
    title: "Governance"
    publisher: Encyclopaedia Britannica (Mark Bevir)
    url: https://www.Britannica.Com/topic/governance
    type: textbook
    accessed: 2026-11-18
  - id: s5
    title: "What is ISO 26000?"
    publisher: ASQ
    url: https://asq.org/quality-resources/iso-26000
    type: community
    accessed: 2026-11-18
created: 2026-11-18
---

# Organizational Governance

**Organizational governance** is the system by which an organization of any kind — a listed company, a government agency, a university, a nonprofit — is directed, overseen and held to account. In the broadest sense, governance means patterns of rule or practices of governing, and scholars use the term precisely because such rule extends beyond the formal authority of the state.[^s4] Applied to a single organization, it is the work of the **governing body** (a board, council, commission or trustees) in setting purpose and strategy, delegating authority to management, and checking that the organization delivers on that purpose ethically and responsibly.[^s2][^s1]

For Salesforce practitioners, organizational governance is the outermost frame: the accountability chain that runs from a board or agency head through IT leadership down to the change board and Center of Excellence that decide what happens in one org, with the governing body remaining ultimately accountable for what is delegated.[^s2][^s3]

## The international benchmark: ISO 37000

**ISO 37000:2021, *Governance of organizations — Guidance*** was published in September 2021 by ISO technical committee ISO/TC 309; it is a 36-page first edition and was reviewed and confirmed in 2026.[^s1] It gives principles and guidance so that governing bodies can meet their responsibilities and the organizations they govern can fulfil their purpose, and it explicitly applies to all organizations whatever their type, size, location, structure or purpose.[^s1] ISO/TC 309, whose secretariat is held by the UK's BSI, describes it as the first international benchmark for good governance, developed with experts from more than 70 countries; it is guidance that complements laws and sector rules rather than adding regulatory requirements.[^s2]

The standard is organized around eleven principles: purpose, value generation model, strategy, oversight, accountability, stakeholder engagement, leadership, data and decisions, risk governance, social responsibility, and viability and performance over time.[^s2] Under them the governing body clarifies purpose and values, takes a long-term view of risk, maintains an internal control system with reliable assurance, defines roles and reporting lines, sets the tone for an ethical culture, and remains ultimately accountable for the organization's acts and omissions.[^s2] Two of these principles matter directly to CRM programs: **data and decisions** treats data as a strategic resource for decision-making, and **risk governance** makes uncertainty a board-level concern rather than only an IT one.[^s2]

An older ISO guidance standard, ISO 26000 on social responsibility (2010), already listed organizational governance as one of its seven core subjects, alongside human rights, labor practices, the environment, fair operating practices, consumer issues and community development.[^s5] It frames good governance as decision-making that weighs societal expectations and builds in accountability, transparency, ethical conduct and stakeholder input; like ISO 37000, it is guidance and is not certifiable.[^s5]

## Putting it into practice: the Three Lines Model

The Institute of Internal Auditors' **Three Lines Model** (July 2020, replacing the earlier "Three Lines of Defense") is the most widely used way to assign governance roles inside an organization.[^s3] It distinguishes:

- **Governing body** — ultimately accountable to stakeholders; sets risk appetite, delegates to management, oversees risk and compliance, and establishes internal audit.[^s3]
- **First line (management)** — delivers products and services and owns day-to-day risk, reporting to the governing body.[^s3]
- **Second line (management)** — provides expertise, monitoring and challenge on risk topics such as compliance, internal control, security and quality.[^s3]
- **Third line (internal audit)** — gives independent, objective assurance and advice, accountable to the governing body and independent of management.[^s3]

The IIA stresses that the lines distinguish roles rather than form a rigid hierarchy, that they operate concurrently, and that governance is a shared responsibility achieved by all three working together.[^s3] In a Salesforce context, admins and developers who run the org sit in the first line, security and compliance teams who review access and controls sit in the second, and internal auditors who test those controls sit in the third.[^s3]

## Connections

Organizational governance sits under `kt:management` (broader), as the direction-and-accountability layer above day-to-day managing.[^s3] It **has parts** that this graph treats separately: `kt:corporate-governance`, the board-and-shareholder system of a company, and `kt:it-governance`, the governance of technology use codified in ISO/IEC 38500.[^s1][^s2] `kt:governance-risk-and-compliance` is the management discipline that turns governing-body direction into risk and compliance controls, mirroring the Three Lines roles.[^s3] `kt:data-governance` applies the "data and decisions" principle to the data itself.[^s2] `kt:salesforce-center-of-excellence` is the body that carries governance down to a single Salesforce program.

## Sources

[^s1]: ISO, "ISO 37000:2021 Governance of organizations — Guidance". https://www.iso.org/standard/65036.html (accessed 2026-11-18)
[^s2]: ISO/TC 309, "ISO 37000 - the first ever international benchmark for good governance". https://committee.iso.org/ISO_37000_Governance (accessed 2026-11-18)
[^s3]: The Institute of Internal Auditors, "The IIA's Three Lines Model: An update of the Three Lines of Defense" (July 2020). https://www.theiia.org/globalassets/site/communication/2020/three-lines-model-updated.pdf (accessed 2026-11-18)
[^s4]: Encyclopaedia Britannica, Mark Bevir, "Governance". https://www.Britannica.Com/topic/governance (accessed 2026-11-18)
[^s5]: ASQ, "What is ISO 26000?". https://asq.org/quality-resources/iso-26000 (accessed 2026-11-18)
