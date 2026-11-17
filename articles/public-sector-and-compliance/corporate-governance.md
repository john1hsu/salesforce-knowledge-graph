---
id: kt:corporate-governance
type: ExternalConcept
title: Corporate Governance
aliases: [company governance, board governance, G20/OECD Principles of Corporate Governance]
domain: public-sector-and-compliance
summary: >-
  The rules and practices by which a company is directed and controlled — the relationships among its board,
  managers, shareholders and other stakeholders — benchmarked internationally by the G20/OECD Principles of
  Corporate Governance; it is the top-level system that a GRC program, and ultimately Salesforce-specific
  governance, answers to.
release: "Winter '27"
status: concept
broader: [kt:organizational-governance]
related: [kt:governance-risk-and-compliance, kt:data-breach-risk, kt:salesforce-inc]
relations:
  - {predicate: contrastsWith, object: kt:salesforce-governance}
sources:
  - id: s1
    title: "G20/OECD Principles of Corporate Governance 2023 (full report)"
    publisher: OECD
    url: https://www.oecd.org/en/publications/2023/09/g20-oecd-principles-of-corporate-governance-2023_60836fcb/full-report
    type: government
    accessed: 2026-11-17
  - id: s2
    title: "Leaders endorse revised G20/OECD Principles of Corporate Governance to promote corporate sustainability, market confidence and financial stability"
    publisher: OECD
    url: https://search.oecd.org/newsroom/leaders-endorse-revised-g20-oecd-principles-of-corporate-governance-to-promote-corporate-sustainability-market-confidence-and-financial-stability.htm
    type: government
    accessed: 2026-11-17
  - id: s3
    title: "Corporate governance"
    publisher: Encyclopaedia Britannica (Britannica Money)
    url: https://www.britannica.com/money/corporate-governance
    type: textbook
    accessed: 2026-11-17
  - id: s4
    title: "SEC Adopts Rules on Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure by Public Companies (Press Release 2023-139)"
    publisher: U.S. Securities and Exchange Commission
    url: https://sec.gov/news/press-release/2023-139
    type: government
    accessed: 2026-11-17
  - id: s5
    title: "Salesforce, Inc. Corporate Governance Guidelines (amended and restated March 27, 2025)"
    publisher: Salesforce, Inc.
    url: https://s205.q4cdn.com/626266368/files/doc_governance/2025/Jun/26/Salesforce-Corporate-Governance-Guidelines-A-R-March-26-2024-Final-for-Website-March-2025-9d5830.pdf
    type: official-docs
    accessed: 2026-11-17
created: 2026-11-17
---

# Corporate Governance

**Corporate governance** is the set of rules and practices by which companies are governed or run.[^s3] It settles who holds membership rights in the firm, what those members may decide and claim, and how they are represented — directly by voting for board members, indirectly, or by proxy.[^s3] In shareholder systems such as the British and American models, rights go to the suppliers of financial capital; stakeholder systems extend them to groups such as employees, suppliers, customers and local communities.[^s3]

For Salesforce practitioners it is the outermost layer of governance: listed companies must now describe how their board oversees cybersecurity risk, so board-level direction flows down into risk programs and, in turn, into how systems such as a Salesforce org are run and secured.[^s4]

## Core problem: separating ownership from control

The classic analysis, associated with Berle and Means in the 1930s, is that growing firms separated ownership from day-to-day control, leaving salaried managers rather than owners running the business.[^s3] That creates an **agency problem**: managers may pursue their own goals instead of the owners' interest in profit.[^s3] Remedies include a market for corporate control, in which the threat of takeover disciplines managers, and internal mechanisms such as shareholder votes on executive pay at annual general meetings.[^s3] Large concentrated holders, such as pension funds, are better placed to monitor managers than small dispersed investors, who can free-ride on that monitoring.[^s3]

## The international benchmark: G20/OECD Principles

The **G20/OECD Principles of Corporate Governance** are described by the OECD as the main international benchmark for good corporate governance, and they are one of the Financial Stability Board's Key Standards for Sound Financial Systems.[^s1] They are addressed mainly to policymakers evaluating the legal, regulatory and institutional framework, with the stated aims of market confidence and integrity, economic efficiency, sustainable growth and financial stability.[^s1] The 2023 edition has six chapters: the basis for an effective framework; shareholder rights and key ownership functions; institutional investors, stock markets and other intermediaries; disclosure and transparency; the responsibilities of the board; and sustainability and resilience.[^s1]

G20 leaders endorsed the revised Principles at their September 2023 summit in New Delhi, after an 18-month review, and the OECD published them on 11 September 2023.[^s2][^s1] The revision updated guidance on shareholder rights, institutional investors, disclosure and board responsibilities, and for the first time added guidance on sustainability and resilience, including climate-related risks.[^s2] Implementation is tracked in the OECD Corporate Governance Factbook, whose 2023 edition covers 49 jurisdictions.[^s2]

## How it reaches technology and security decisions

Regulators increasingly make the board's oversight of technology risk an explicit disclosure item. In July 2023 the U.S. SEC adopted rules requiring public companies to report material cybersecurity incidents under Form 8-K Item 1.05, generally within four business days of determining materiality.[^s4] Under Regulation S-K Item 106, annual reports must also describe the processes for managing material cybersecurity risks, the **board's oversight** of those risks, and management's role and expertise in handling them.[^s4] A breach in a CRM system that holds customer data is therefore not only an IT event: if material, it becomes a governance and disclosure event for the company's board.[^s4]

## Example: Salesforce's own guidelines

Salesforce, Inc. publishes Corporate Governance Guidelines, first adopted in December 2004 and most recently amended and restated on 27 March 2025.[^s5] They make the stockholder-elected board the company's ultimate decision-making body outside matters reserved to stockholders, and require that the board never have less than a majority of independent directors, judged against NYSE criteria.[^s5] The board must maintain Audit, Compensation, and Nominating and Corporate Governance committees made up of independent directors, and the independent directors elect a Lead Independent Director for a two-year term.[^s5] The guidelines themselves do not set out board oversight of risk, cybersecurity or privacy; those topics sit elsewhere in a company's governance documents and regulatory filings.[^s5][^s4]

## Connections

Corporate governance sits under the wider idea of organizational governance (`kt:organizational-governance`, broader), here applied to companies.[^s3] Governance, risk and compliance (`kt:governance-risk-and-compliance`) is the management discipline that puts board-level direction into practice through risk management and compliance controls. Data breach risk (`kt:data-breach-risk`) connects to it through the SEC's requirement that boards oversee, and companies disclose, material cybersecurity risks and incidents.[^s4] Salesforce, Inc. (`kt:salesforce-inc`) is a worked example of a listed company's governance guidelines.[^s5] It **contrasts with** Salesforce governance (`kt:salesforce-governance`): the latter is the platform-level program that steers how one org is changed and run, while corporate governance concerns how the company as a whole is directed and held accountable to its owners.[^s3][^s1]

## Sources

[^s1]: OECD, "G20/OECD Principles of Corporate Governance 2023 (full report)". https://www.oecd.org/en/publications/2023/09/g20-oecd-principles-of-corporate-governance-2023_60836fcb/full-report (accessed 2026-11-17)
[^s2]: OECD, "Leaders endorse revised G20/OECD Principles of Corporate Governance to promote corporate sustainability, market confidence and financial stability". https://search.oecd.org/newsroom/leaders-endorse-revised-g20-oecd-principles-of-corporate-governance-to-promote-corporate-sustainability-market-confidence-and-financial-stability.htm (accessed 2026-11-17)
[^s3]: Encyclopaedia Britannica, "Corporate governance" (Britannica Money). https://www.britannica.com/money/corporate-governance (accessed 2026-11-17)
[^s4]: U.S. Securities and Exchange Commission, "SEC Adopts Rules on Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure by Public Companies" (Press Release 2023-139). https://sec.gov/news/press-release/2023-139 (accessed 2026-11-17)
[^s5]: Salesforce, Inc., "Corporate Governance Guidelines" (amended and restated March 27, 2025). https://s205.q4cdn.com/626266368/files/doc_governance/2025/Jun/26/Salesforce-Corporate-Governance-Guidelines-A-R-March-26-2024-Final-for-Website-March-2025-9d5830.pdf (accessed 2026-11-17)
