---
id: kt:management
type: ExternalConcept
title: Management
aliases: [organizational management, functions of management, planning organizing leading controlling]
domain: public-sector-and-compliance
summary: >-
  The process of guiding how an organization develops, maintains and allocates its resources to reach its goals,
  usually described as planning, organizing, leading and controlling; compliance frameworks such as ISO management
  system standards, ISO/IEC 38500 and COBIT build on it and separate it from governance, which directs and
  oversees management.
release: "Winter '27"
status: concept
broader: [kt:business-administration]
related: [kt:organizational-governance, kt:governance-risk-and-compliance, kt:iso-iec-27001, kt:cobit, kt:salesforce-center-of-excellence]
relations:
  - {predicate: contrastsWith, object: kt:it-governance}
sources:
  - id: s1
    title: "Introduction to Business 2e — 6.1 The Role of Management"
    publisher: OpenStax (Gitman, McDaniel, Shah et al.)
    url: https://openstax.org/books/introduction-business-2e/pages/6-1-the-role-of-management
    type: textbook
    accessed: 2026-11-23
  - id: s2
    title: "Principles of Management — Ch. 1 Introduction"
    publisher: OpenStax (Bright, Cortes et al.)
    url: https://openstax.org/books/principles-management/pages/1-introduction
    type: textbook
    accessed: 2026-11-23
  - id: s3
    title: "What is a management system?"
    publisher: ISO
    url: https://iso.org/management-system-standards.html
    type: standards-body
    accessed: 2026-11-23
  - id: s4
    title: "Exploring MSS"
    publisher: ISO/IEC Joint Technical Coordination Group on MSS
    url: https://committee.iso.org/sites/jtcg/home/exploring-mss.html
    type: standards-body
    accessed: 2026-11-23
  - id: s5
    title: "To govern, or not to govern information technology"
    publisher: Communications of the ACM
    url: https://cacm.acm.org/research/to-govern-it-or-not-to-govern-it
    type: academic
    accessed: 2026-11-23
  - id: s6
    title: "COBIT IT Enterprise Governance Framework"
    publisher: ISACA
    url: https://isaca.org/cobit
    type: standards-body
    accessed: 2026-11-23
created: 2026-11-23
---

# Management

**Management** is the process of guiding how an organization develops, maintains and allocates its resources so that it reaches its goals; managers are the people who carry that process out.[^s1] Textbooks judge it on two measures: **efficiency**, getting work done with the fewest resources, and **effectiveness**, actually producing the result that was wanted.[^s1]

In compliance work the word carries a narrower, structural meaning. Standards and audit frameworks repeatedly separate the people who *govern* an organization (set direction, hold to account) from the people who *manage* it (plan and run the work), and then define what a management system must contain.[^s5][^s3] Understanding that split is what lets a Salesforce team map its admins, release managers and Center of Excellence to the roles an auditor expects to see.[^s5]

## The four functions

The classic textbook model describes management as four linked functions that repeat as a cycle: anticipate problems or opportunities and plan for them, coordinate and allocate resources, guide people, then review results and adjust.[^s1]

- **Planning** — setting objectives, weighing alternatives and choosing strategies to reach them.[^s1]
- **Organizing** — designing jobs, building the structure that groups them, and staffing the positions.[^s1]
- **Leading** — motivating employees and resolving conflicts so the plan gets done.[^s1]
- **Controlling** — measuring performance, comparing it with standards and adjusting where results fall short.[^s1]

Older lists stretch the same work into planning, organizing, staffing, directing, coordinating, reporting and controlling.[^s2] OpenStax's management text warns that such lists are tidy abstractions: field research on managers found their actual day is a fragmented, hectic flow of short activities rather than neat functional steps.[^s2]

## Management systems

ISO defines a **management system** as the way an organization manages the interrelated parts of its business to achieve objectives such as quality, efficiency, environmental performance or health and safety.[^s3] How elaborate it must be depends on context: a small firm may need little documentation, while a heavily regulated one may need extensive records and controls.[^s3] ISO publishes more than 80 management system standards (MSS), including ISO 9001 for quality, ISO 50001 for energy and the ISO/IEC 27000 family for information security.[^s3]

These standards share one **Harmonized Structure** (HS), the common text historically published as Annex SL: identical clause numbers in the same order, identical clause titles, shared terms and core definitions, and common core requirements.[^s3][^s4] Because the skeleton is the same, an organization can run an integrated management system that satisfies several standards at once.[^s3] ISO itself does not certify anyone, and certification to an MSS is optional; organizations that want it use an external certification body.[^s3]

## Management versus governance

The clearest compliance statement of the split is ISO/IEC 38500, the first international standard for governance of IT (2008, derived from Australia's AS 8015). In its model the governing body **evaluates, directs and monitors**, while managers **plan, build, run and monitor** the IT that serves the organization.[^s5] A CACM analysis of the standard argues that much of what organizations label "IT governance" is in fact IT management, and that governance mainly defines who makes decisions and how, leaving architecture, infrastructure and investment choices to management.[^s5] It also notes the standard does not expect board members to know how to design, build or operate IT systems.[^s5]

ISACA's COBIT applies the same division to enterprise technology, describing itself as covering both governance and management across business and IT functions, organized into five domains and forty objectives.[^s6]

## Connections

Management sits under `kt:business-administration` (broader), the wider field of running organizations. `kt:organizational-governance` is the direction-and-accountability layer above it, and `kt:governance-risk-and-compliance` is where management turns that direction into risk and compliance controls.[^s5] It `contrastsWith` `kt:it-governance`: ISO/IEC 38500 assigns evaluate-direct-monitor to the governing body and plan-build-run to managers, and confusing the two is a common failure.[^s5] `kt:iso-iec-27001` is a management system standard built on the Harmonized Structure, and `kt:cobit` separates governance objectives from management ones.[^s3][^s6] In a Salesforce program, `kt:salesforce-center-of-excellence` is where these management functions — planning releases, organizing teams, controlling change — are carried out for the org.

## Sources

[^s1]: OpenStax (Gitman, McDaniel, Shah et al.), "Introduction to Business 2e — 6.1 The Role of Management". https://openstax.org/books/introduction-business-2e/pages/6-1-the-role-of-management (accessed 2026-11-23)
[^s2]: OpenStax (Bright, Cortes et al.), "Principles of Management — Ch. 1 Introduction". https://openstax.org/books/principles-management/pages/1-introduction (accessed 2026-11-23)
[^s3]: ISO, "What is a management system?". https://iso.org/management-system-standards.html (accessed 2026-11-23)
[^s4]: ISO/IEC JTCG, "Exploring MSS". https://committee.iso.org/sites/jtcg/home/exploring-mss.html (accessed 2026-11-23)
[^s5]: Communications of the ACM, "To govern, or not to govern information technology". https://cacm.acm.org/research/to-govern-it-or-not-to-govern-it (accessed 2026-11-23)
[^s6]: ISACA, "COBIT IT Enterprise Governance Framework". https://isaca.org/cobit (accessed 2026-11-23)
