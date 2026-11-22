---
id: kt:togaf
type: ExternalConcept
title: TOGAF
aliases: [The Open Group Architecture Framework, TOGAF Standard, TOGAF ADM, TOGAF 10th Edition]
domain: architecture-practice
summary: >-
  The Open Group's open, consensus-based enterprise architecture standard, built around the iterative Architecture
  Development Method (ADM); Salesforce architects meet it when a Salesforce program has to fit an enterprise's
  existing architecture practice, governance and vocabulary.
release: "Winter '27"
status: concept
broader: [kt:enterprise-architecture]
related: [kt:capability-maps, kt:design-authority, kt:architecture-decision-records]
relations:
  - {predicate: hasPart, object: kt:business-architecture}
  - {predicate: usedBy, object: kt:salesforce-architect}
  - {predicate: contrastsWith, object: kt:well-architected-framework}
sources:
  - id: s1
    title: "The TOGAF Pocket Guide: Introduction"
    publisher: The Open Group
    url: https://pubs.opengroup.org/pocket-guides/togaf-pocket-guide/main/introduction.html
    type: standards-body
    accessed: 2026-11-22
  - id: s2
    title: "The TOGAF Pocket Guide: TOGAF Fundamental Content"
    publisher: The Open Group
    url: https://pubs.opengroup.org/pocket-guides/togaf-pocket-guide/main/chap05.html
    type: standards-body
    accessed: 2026-11-22
  - id: s3
    title: "The TOGAF Pocket Guide: The TOGAF Architecture Development Method"
    publisher: The Open Group
    url: https://pubs.opengroup.org/pocket-guides/togaf-pocket-guide/main/chap06.html
    type: standards-body
    accessed: 2026-11-22
  - id: s4
    title: "The TOGAF Pocket Guide: Domain-Specific Guidance"
    publisher: The Open Group
    url: https://pubs.opengroup.org/pocket-guides/togaf-pocket-guide/main/chap04.html
    type: standards-body
    accessed: 2026-11-22
  - id: s5
    title: "An Introduction to the TOGAF Standard, 10th Edition (White Paper W212)"
    publisher: The Open Group
    url: https://pubs.opengroup.org/architecture/w212
    type: standards-body
    accessed: 2026-11-22
  - id: s6
    title: "The Open Group Announces Launch of the TOGAF Standard, 10th Edition"
    publisher: The Open Group
    url: https://www.opengroup.org/open-group-announces-launch-togaf-standard-10th-edition
    type: news
    accessed: 2026-11-22
created: 2026-11-22
---

# TOGAF

TOGAF is an open, industry-consensus framework for enterprise architecture (EA): a standard way to develop, approve, use and maintain an enterprise's architecture, based on an iterative process model plus reusable best practices and assets.[^s1] It is developed by members of The Open Group's Architecture Forum. Version 1 appeared in 1995 and was derived from the US Department of Defense's TAFIM framework.[^s1] It is not a Salesforce product, but it is the vocabulary many enterprise architecture teams use. A Salesforce architect working in a large organization will often find that the CRM program has to pass through a TOGAF-style method and governance.[^s5]

## Structure of the 10th Edition

The Open Group launched the 10th Edition on 25 April 2022 with a modular structure. Stable fundamentals are separated from topic-specific guidance, so new material can be added more often without changing the core.[^s6] The introductory white paper explains why. Version 9 was a single document of about 780 pages that members found hard to adopt, and 9.2 was an interim step that began moving specialist material into separate guides.[^s5] The standard now has two parts: the **Fundamental Content**, which holds the universal concepts, and the **Series Guides**, which make those concepts actionable. A separate TOGAF Library holds emerging ideas, templates and white papers.[^s1]

The Fundamental Content consists of six documents: Introduction and Core Concepts; the Architecture Development Method; ADM Techniques; Applying the ADM; Architecture Content; and Enterprise Architecture Capability and Governance.[^s2] The listed techniques include architecture principles, stakeholder management, gap analysis, migration planning, risk management, and architecture alternatives and trade-offs.[^s2] The Series Guides are grouped by subject: business architecture (business models, capabilities, value streams, business scenarios), data and information architecture, security and risk, agile methods, and reference models.[^s4]

## The Architecture Development Method

The ADM is the core of the standard. It is a repeatable process for deriving an organization-specific architecture, run as a continuous cycle of definition and realization.[^s3] Its phases are:[^s3]

1. **Preliminary**: set up the architecture capability, including principles, a tailored framework, governance and a Request for Architecture Work.[^s3]
2. **A, Architecture Vision**: scope the effort, identify stakeholders, and get a Statement of Architecture Work approved.[^s3]
3. **B, C, D (Business, Information Systems, Technology)**: describe baseline and target architectures and run gap analysis. Phase C covers data and applications.[^s3]
4. **E, Opportunities and Solutions**: the first phase concerned directly with implementation. It produces the initial Architecture Roadmap and any Transition Architectures.[^s3]
5. **F, Migration Planning**: finalize a prioritized Implementation and Migration Plan.[^s3]
6. **G, Implementation Governance**: oversee delivery through compliance reviews and a signed Architecture Contract.[^s3]
7. **H, Architecture Change Management**: handle change. Major change raises a new Request for Architecture Work and starts another cycle.[^s3]

**Requirements Management** sits at the centre and feeds every phase.[^s3] The method can be adapted: it does not require the phases to run in a fixed order and does not prescribe waterfall delivery.[^s3] Series Guides describe applying the ADM with agile sprints.[^s5]

## Key concepts

The standard defines four architecture domains: business, data, application and technology. Security is treated as a concern that runs across all four.[^s4] The **Enterprise Continuum** classifies assets from generic foundation architectures through to organization-specific ones. The **Architecture Repository** stores those assets at different levels of abstraction. The **Content Framework** sorts work products into deliverables, artifacts (catalogs, matrices and diagrams) and building blocks.[^s2] Governance is run by an **Architecture Board** that approves architectural products and resolves conflicts, and compliance is enforced through Architecture Contracts.[^s2]

## Using it on Salesforce programs

TOGAF is aimed at enterprise architecture practitioners and team leads. The white paper notes that implementers and other stakeholders rarely use it directly.[^s5] On a Salesforce program, this usually means the Salesforce team receives architecture principles, a target state and governance checkpoints from the enterprise. The team's job is to map its solution design onto them rather than run the full ADM itself. Gap analysis, the roadmap from Phases E–F and the compliance reviews of Phase G are the touchpoints that matter most in practice.[^s3] TOGAF is product-neutral and covers the whole enterprise, so it does not replace platform-specific guidance on Salesforce limits or design patterns.[^s1]

## Connections

TOGAF is a framework within the broader discipline of `kt:enterprise-architecture`.[^s1] Its business-architecture Series Guides are the source of the capability and value-stream methods used in `kt:capability-maps`, and business architecture is one of its four domains, so it **has part** `kt:business-architecture`.[^s4] The Architecture Board and Architecture Contracts correspond to the role of a `kt:design-authority` in a Salesforce program.[^s2] TOGAF's "architecture alternatives and trade-offs" technique produces the decisions that teams often record as `kt:architecture-decision-records`.[^s2] It is **used by** the `kt:salesforce-architect` who has to work within enterprise governance. It **contrasts with** the `kt:well-architected-framework`: TOGAF is a vendor-neutral method for running architecture across the enterprise, whereas Well-Architected is quality guidance for solutions built on one platform.[^s1][^s3]

## Sources
[^s1]: The Open Group, "The TOGAF Pocket Guide: Introduction". https://pubs.opengroup.org/pocket-guides/togaf-pocket-guide/main/introduction.html (accessed 2026-11-22)
[^s2]: The Open Group, "The TOGAF Pocket Guide: TOGAF Fundamental Content". https://pubs.opengroup.org/pocket-guides/togaf-pocket-guide/main/chap05.html (accessed 2026-11-22)
[^s3]: The Open Group, "The TOGAF Pocket Guide: The TOGAF Architecture Development Method". https://pubs.opengroup.org/pocket-guides/togaf-pocket-guide/main/chap06.html (accessed 2026-11-22)
[^s4]: The Open Group, "The TOGAF Pocket Guide: Domain-Specific Guidance". https://pubs.opengroup.org/pocket-guides/togaf-pocket-guide/main/chap04.html (accessed 2026-11-22)
[^s5]: The Open Group, "An Introduction to the TOGAF Standard, 10th Edition" (White Paper W212). https://pubs.opengroup.org/architecture/w212 (accessed 2026-11-22)
[^s6]: The Open Group, "The Open Group Announces Launch of the TOGAF Standard, 10th Edition". https://www.opengroup.org/open-group-announces-launch-togaf-standard-10th-edition (accessed 2026-11-22)
