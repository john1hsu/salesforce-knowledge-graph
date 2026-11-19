---
id: kt:cobit
type: ExternalConcept
title: COBIT
aliases: [COBIT 7, COBIT 2019, COBIT 5, Control Objectives for Information and Related Technologies, ISACA COBIT framework]
domain: public-sector-and-compliance
summary: >-
  ISACA's framework for the governance and management of enterprise information and technology (I&T), which
  organizes the work into 40 governance and management objectives across five domains and is tailored to each
  enterprise through design factors; the current edition is COBIT 7, successor to COBIT 2019.
release: "Winter '27"
status: concept
broader: [kt:it-governance]
related: [kt:governance-risk-and-compliance, kt:salesforce-governance, kt:salesforce-center-of-excellence, kt:security-compliance-frameworks]
relations:
  - {predicate: integratesWith, object: kt:nist-cybersecurity-framework}
sources:
  - id: s1
    title: "COBIT 7 IT Enterprise Governance Framework"
    publisher: ISACA
    url: https://www.isaca.org/resources/cobit
    type: standards-body
    accessed: 2026-11-19
  - id: s2
    title: "A New COBIT Is in Town, and I Really Like How It Looks"
    publisher: ISACA
    url: https://www.isaca.org/resources/news-and-trends/industry-news/2018/a-new-cobit-is-in-town-and-i-really-like-how-it-looks
    type: community
    accessed: 2026-11-19
  - id: s3
    title: "COBIT Design Factors"
    publisher: ISACA
    url: https://www.isaca.org/resources/news-and-trends/industry-news/2019/cobit-design-factors
    type: community
    accessed: 2026-11-19
  - id: s4
    title: "What is COBIT? A framework for alignment and governance"
    publisher: CIO
    url: https://www.cio.com/article/228151/what-is-cobit-a-framework-for-alignment-and-governance.html
    type: news
    accessed: 2026-11-19
  - id: s5
    title: "New ISACA Resources Offer Step-by-Step Guidance for NIST Cybersecurity Framework Implementation"
    publisher: ISACA
    url: https://www.isaca.org/about-us/newsroom/press-releases/2019/new-isaca-resources-offer-step-by-step-guidance-for-nist-cybersecurity-framework-implementation
    type: standards-body
    accessed: 2026-11-19
  - id: s6
    title: "Learn About Salesforce Governance and Why It Matters (Salesforce Governance with a Center of Excellence)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-governance-with-a-center-of-excellence/learn-about-salesforce-governance-and-why-it-matters
    type: official-learning
    accessed: 2026-11-19
created: 2026-11-19
---

# COBIT

COBIT is ISACA's framework for governing and managing enterprise information and technology (I&T). Where a standard such as ISO/IEC 38500 states governance principles, COBIT turns them into objectives, practices and activities that a CIO, auditor or governance office can assign and measure. ISACA's 2018 launch article calls it a generally accepted framework for I&T governance that covers all of the enterprise's technology, not just the IT department.[^s2] ISACA now presents COBIT 7 as the current edition and says the framework has been in use for 30 years.[^s1]

## History and versions

COBIT started in 1996 as a set of IT control objectives for financial auditors. Version 2 followed in 1998, version 3 in the 2000s, COBIT 4 in 2005, COBIT 4.1 in 2007 and COBIT 5 in 2012. In 2018 ISACA announced COBIT 2019 and dropped the plain version number.[^s4] COBIT 2019 went from 37 processes to 40, replaced COBIT 5's "enablers" with governance components, added design factors and focus areas, and updated the goals cascade and the performance management model.[^s2][^s4] Its performance management model is based on CMMI.[^s4]

COBIT 7 keeps the same scale, with five domains and forty objectives. ISACA has moved the content from a long PDF onto a single digital platform. The framework now has five sections: Introduction and Methodology; Governance and Management Objectives; a Design Guide; an Implementation Guide; and a Governance Assessment and Performance Management Guide. It also brings back formal assessments at three depths: board-level, high-level and detailed.[^s1] The basic tier is free to members and non-members. The design and assessment guides are premium content. A COBIT 7 Foundation certificate is offered now, and a design, implementation and assessment certificate is due in 2027.[^s1]

## How the framework is structured

The core model splits governance from management. The one governance domain is Evaluate, Direct and Monitor (EDM). The four management domains are Align, Plan and Organize (APO); Build, Acquire and Implement (BAI); Deliver, Service and Support (DSS); and Monitor, Evaluate and Assess (MEA). Each objective has a code, for example BAI06 for managed IT changes.[^s2] Each objective is supported by seven kinds of component: processes; organizational structures; information flows; people, skills and competencies; culture, ethics and behavior; policies and procedures; and services, infrastructure and applications.[^s2][^s4]

COBIT does not apply the same governance system to every enterprise. Its Design Guide uses design factors to tailor the core model. In COBIT 2019 there are eleven, grouped as contextual (size, geopolitics, threat landscape), strategic (enterprise strategy, the role of IT, risk appetite) and tactical (sourcing model, delivery methods such as Agile or DevOps, technology adoption).[^s3] From these, an enterprise ranks which objectives matter most, sets a target capability level for each, and chooses component variants. ISACA's design toolkit spreadsheet supports this step.[^s3]

## Using COBIT with other frameworks

COBIT is designed to work alongside other frameworks. In 2019 ISACA published a guide on implementing the NIST Cybersecurity Framework using COBIT 2019. It maps CSF steps and activities to COBIT practices, cascades COBIT goals to the CSF, and includes a profile template and an action-planning guide.[^s5] COBIT supplies the governance structure, roles and performance measures. The control and assurance frameworks supply the subject-specific requirements.[^s4][^s5]

## Relevance to Salesforce programs

A Salesforce org falls under the same enterprise I&T governance that COBIT describes. Trailhead defines Salesforce governance as the people, processes and tools that decide what gets built and in what order, which standards builders follow, and how changes are designed and deployed. It names SOX, GDPR and CCPA compliance among the benefits.[^s6] In practice, a Center of Excellence can use COBIT objectives to frame its work. For example, BAI06 covers release and change control and APO objectives cover roadmap prioritization. That gives auditors familiar terms for checking platform controls.[^s2][^s6]

## Connections

COBIT sits under `kt:it-governance` (broader) and puts that discipline into practice as a generally accepted framework for I&T governance.[^s2] It supplies the governance layer of `kt:governance-risk-and-compliance` programs and sits alongside the control catalogs in `kt:security-compliance-frameworks`; it began as a set of control objectives for auditors.[^s4][^s5] It **integrates with** `kt:nist-cybersecurity-framework` through ISACA's published implementation guide.[^s5] At platform level, `kt:salesforce-governance` and the `kt:salesforce-center-of-excellence` that delivers it are where COBIT-style objectives become concrete Salesforce standards and release processes.[^s6]

## Sources

[^s1]: ISACA, "COBIT 7 IT Enterprise Governance Framework". https://www.isaca.org/resources/cobit (accessed 2026-11-19)
[^s2]: ISACA (Mark Thomas), "A New COBIT Is in Town, and I Really Like How It Looks", 10 December 2018. https://www.isaca.org/resources/news-and-trends/industry-news/2018/a-new-cobit-is-in-town-and-i-really-like-how-it-looks (accessed 2026-11-19)
[^s3]: ISACA (Abdul Rafeq), "COBIT Design Factors", 4 February 2019. https://www.isaca.org/resources/news-and-trends/industry-news/2019/cobit-design-factors (accessed 2026-11-19)
[^s4]: CIO (Sarah K. White), "What is COBIT? A framework for alignment and governance", 12 June 2023. https://www.cio.com/article/228151/what-is-cobit-a-framework-for-alignment-and-governance.html (accessed 2026-11-19)
[^s5]: ISACA, "New ISACA Resources Offer Step-by-Step Guidance for NIST Cybersecurity Framework Implementation", 17 December 2019. https://www.isaca.org/about-us/newsroom/press-releases/2019/new-isaca-resources-offer-step-by-step-guidance-for-nist-cybersecurity-framework-implementation (accessed 2026-11-19)
[^s6]: Salesforce Trailhead, "Learn About Salesforce Governance and Why It Matters". https://trailhead.salesforce.com/content/learn/modules/salesforce-governance-with-a-center-of-excellence/learn-about-salesforce-governance-and-why-it-matters (accessed 2026-11-19)
