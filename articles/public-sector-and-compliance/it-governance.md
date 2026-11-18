---
id: kt:it-governance
type: ExternalConcept
title: IT Governance
aliases: [governance of IT, enterprise governance of IT, governance of information and technology, I&T governance, ISO/IEC 38500]
domain: public-sector-and-compliance
summary: >-
  The part of organizational governance that directs and controls how an organization uses information
  technology, codified in ISO/IEC 38500 and operationalized by frameworks such as ISACA's COBIT; it sets the
  direction, decision rights and accountability that Salesforce-specific governance and a Center of Excellence
  then carry out for one platform.
release: "Winter '27"
status: concept
broader: [kt:organizational-governance]
related: [kt:corporate-governance, kt:governance-risk-and-compliance, kt:salesforce-center-of-excellence, kt:nist-cybersecurity-framework, kt:cobit]
relations:
  - {predicate: hasPart, object: kt:salesforce-governance}
  - {predicate: hasPart, object: kt:security-governance}
  - {predicate: contrastsWith, object: kt:data-governance}
sources:
  - id: s1
    title: "ISO/IEC 38500:2024 Information technology — Governance of IT for the organization"
    publisher: ISO
    url: https://www.iso.org/standard/81684.html
    type: standards-body
    accessed: 2026-11-18
  - id: s2
    title: "White paper on the differences between ISO/IEC 38500:2015 and ISO/IEC 38500:2024"
    publisher: ISO/IEC JTC 1/SC 40
    url: https://committee.iso.org/sites/jtc1sc40/home/projects/wg-1/published-wg1/content-left-area/isoiec-sc-40-wg-1-develops-the-s/white-paper-on-the-differences-b.html
    type: standards-body
    accessed: 2026-11-18
  - id: s3
    title: "A New COBIT Is in Town, and I Really Like How It Looks"
    publisher: ISACA
    url: https://www.isaca.org/resources/news-and-trends/industry-news/2018/a-new-cobit-is-in-town-and-i-really-like-how-it-looks
    type: community
    accessed: 2026-11-18
  - id: s4
    title: "Cybersecurity Framework FAQs"
    publisher: NIST
    url: https://nist.gov/cyberframework/faqs
    type: standards-body
    accessed: 2026-11-18
  - id: s5
    title: "Learn About Salesforce Governance and Why It Matters (Salesforce Governance with a Center of Excellence)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-governance-with-a-center-of-excellence/learn-about-salesforce-governance-and-why-it-matters
    type: official-learning
    accessed: 2026-11-18
  - id: s6
    title: "Define Your Salesforce CoE (Salesforce Governance with a Center of Excellence)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-governance-with-a-center-of-excellence/define-your-salesforce-coe
    type: official-learning
    accessed: 2026-11-18
created: 2026-11-18
---

# IT Governance

IT governance is the system by which an organization directs and controls its current and future use of information technology. The reference standard, ISO/IEC 38500 (third edition, published February 2024), frames it as a domain within overall organizational governance and offers guiding principles to governing bodies, and those who support them, on the effective, efficient and acceptable use of IT. It applies to organizations of every kind and size: public and private companies, government entities and not-for-profits.[^s1]

## Governance versus management

The distinction that defines the field is between governing IT and managing it. In the 2024 revision of ISO/IEC 38500, management operates inside a framework the governing body sets, and that framework is the mechanism through which the two work together. The new edition also stresses that governance happens throughout the organization, not only in the boardroom.[^s2]

## The main reference frameworks

ISO/IEC 38500:2024 replaces the 2015 edition and is aligned with ISO 37000 on organizational governance. It remains principle-based but grows from six principles to eleven, adopted from ISO 37000, and widens its scope to IT's role in data use and in environmental and social issues. Its governance framework has six elements (direction, capability, policy, delegation, performance and accountability), and the revision adds stakeholder engagement to the model.[^s2]

COBIT 2019 is the most widely used operational framework. It defines 40 governance and management objectives, each mapped to one process. COBIT keeps the governance/management split in its structure: governance objectives sit in the Evaluate, Direct and Monitor (EDM) domain. Management objectives sit in four domains: Align, Plan and Organize; Build, Acquire and Implement; Deliver, Service and Support; and Monitor, Evaluate and Assess. ISACA is explicit that COBIT is not a business-process framework and does not govern specific technologies.[^s3]

For cybersecurity, NIST CSF 2.0 added a Govern (GV) function that covers risk tolerance, roles and responsibilities, and policy. NIST moved governance out of Identify so that it would visibly support the whole program and align with enterprise risk management and legal obligations.[^s4]

## Applying it to a Salesforce org

A Salesforce org is one IT asset among many, so enterprise IT governance decides the questions above the platform: investment, risk appetite and who holds decision rights. Salesforce's own Trailhead guidance describes Salesforce governance as a framework of people, processes and tools. Its job is to answer who decides what gets built and in what order, which standards builders must follow, and how changes ship without breaking existing functionality.[^s5] The same module warns that weak governance builds up "governance debt": technical debt, inconsistent data, shadow IT and higher costs to fix problems after deployment.[^s5]

The usual operating vehicle is a Center of Excellence. Trailhead describes it as a cross-functional steering committee and knowledge hub whose members include executive sponsors, architects and team leads. It works through three pillars: vision (a prioritized roadmap), standards, and enablement.[^s6] Seen through ISO/IEC 38500, the CoE carries the delegated direction and accountability elements for one platform, and IT representatives keep its release schedules in step with the systems around it.[^s2][^s6]

## Connections

IT governance sits under `kt:organizational-governance` (broader). It is the IT-focused sibling of `kt:corporate-governance`, which governs the company as a whole, and the "G" in `kt:governance-risk-and-compliance`.[^s1][^s2] It has two parts in this graph: `kt:salesforce-governance`, its platform-specific application, and `kt:security-governance`, the security slice that NIST CSF 2.0 now treats as its own Govern function (`kt:nist-cybersecurity-framework`).[^s4][^s5] `kt:salesforce-center-of-excellence` is the body that carries it out for Salesforce.[^s6] `kt:cobit` is the operational framework most often used to put it in place.[^s3] It contrasts with `kt:data-governance`: data governance sets policy for the data itself, while IT governance sets direction and accountability for the technology portfolio that holds that data.[^s2][^s5]

## Sources

[^s1]: ISO, "ISO/IEC 38500:2024 Information technology — Governance of IT for the organization". https://www.iso.org/standard/81684.html (accessed 2026-11-18)
[^s2]: ISO/IEC JTC 1/SC 40, "White paper on the differences between ISO/IEC 38500:2015 and ISO/IEC 38500:2024". https://committee.iso.org/sites/jtc1sc40/home/projects/wg-1/published-wg1/content-left-area/isoiec-sc-40-wg-1-develops-the-s/white-paper-on-the-differences-b.html (accessed 2026-11-18)
[^s3]: ISACA, "A New COBIT Is in Town, and I Really Like How It Looks". https://www.isaca.org/resources/news-and-trends/industry-news/2018/a-new-cobit-is-in-town-and-i-really-like-how-it-looks (accessed 2026-11-18)
[^s4]: NIST, "Cybersecurity Framework FAQs". https://nist.gov/cyberframework/faqs (accessed 2026-11-18)
[^s5]: Salesforce Trailhead, "Learn About Salesforce Governance and Why It Matters". https://trailhead.salesforce.com/content/learn/modules/salesforce-governance-with-a-center-of-excellence/learn-about-salesforce-governance-and-why-it-matters (accessed 2026-11-18)
[^s6]: Salesforce Trailhead, "Define Your Salesforce CoE". https://trailhead.salesforce.com/content/learn/modules/salesforce-governance-with-a-center-of-excellence/define-your-salesforce-coe (accessed 2026-11-18)
