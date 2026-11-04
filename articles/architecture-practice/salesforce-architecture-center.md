---
id: kt:salesforce-architecture-center
type: Tool
title: Salesforce Architecture Center
aliases: [architect.salesforce.com, Salesforce Architects site, Architect Digital Home]
domain: architecture-practice
summary: >-
  Salesforce's official website for architects at architect.salesforce.com, which hosts the Well-Architected Framework,
  Architecture Fundamentals, Decision Guides and the Salesforce Diagrams framework and galleries; it launched in beta in
  December 2020 and was rebuilt as the hub of the relaunched architecture program in October 2025.
release: "Winter '27"
status: current
broader: [kt:salesforce-architecture-program]
related: [kt:integration-patterns, kt:multitenancy, kt:salesforce-sharing-model, kt:record-triggered-flow, kt:event-driven-architecture, kt:cta-review-board]
relations:
  - {predicate: hasPart, object: kt:well-architected-framework}
  - {predicate: hasPart, object: kt:architect-decision-guides}
  - {predicate: hasPart, object: kt:salesforce-diagrams}
  - {predicate: usedBy, object: kt:salesforce-architect}
sources:
  - id: s1
    title: "Salesforce Architects (Architecture Center home and Well-Architected entry)"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/well-architected
    type: official-docs
    accessed: 2026-11-04
  - id: s2
    title: "Get Started with Platform Decision Guides"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/decision-guides/guide/get-started-platform-decision-guides.html
    type: official-docs
    accessed: 2026-11-04
  - id: s3
    title: "Salesforce Diagrams — Framework Overview"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/diagrams/framework/overview
    type: official-docs
    accessed: 2026-11-04
  - id: s4
    title: "Relaunching the Salesforce Architecture Program"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/relaunching-salesforce-architecture-program/
    type: official-blog
    accessed: 2026-11-04
  - id: s5
    title: "5 Salesforce Architecture Resources Every CTA Candidate Should Use"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/architecture-resources-for-cta/
    type: official-blog
    accessed: 2026-11-04
  - id: s6
    title: "Architects, Welcome Home"
    publisher: Salesforce Architects (Medium)
    url: https://medium.com/salesforce-architects/architects-welcome-home-4bf2a00a5471
    type: official-blog
    accessed: 2026-11-04
created: 2026-11-04
---

# Salesforce Architecture Center

The Salesforce Architecture Center is Salesforce's official website for people who design solutions on its platform, published at architect.salesforce.com. Its home page groups the site into four entry points (the Well-Architected Framework, Architecture Fundamentals, Decision Guides and Diagrams) and adds the architecture blog, videos, Trailhead career content, community links, a sign-up for the Architect Digest newsletter, and an FAQ about the architecture program.[^s1] It is aimed at architects but also at developers, admins and technical leaders who need authoritative guidance on how the platform behaves and how to choose between its tools.[^s1]

## History

Salesforce Architects launched the site in beta in December 2020 as a single "digital home" that pulled together material from dozens of Salesforce teams. The first version organized resources by four modes of architect work (design, deliver, govern and roadmap) and included a combined view of release and maintenance calendars.[^s6] In October 2025 Salesforce relaunched its architecture program and rebuilt the site as the central hub for Well-Architected, diagrams and decision guides. That relaunch added fundamentals on Data 360 architecture, integration patterns, agentic enterprise architecture and the Agent Development Lifecycle, plus new or updated decision guides such as Data 360 Provisioning, Data 360 Interoperability, Asynchronous Processing, Event-Driven Architecture, Data Integration and Building Forms.[^s4]

## What it contains

**Well-Architected Framework.** The site's prescriptive guidance on healthy solutions, presented as of Winter '27 under five pillars: Trust, Reliability, Operational Excellence, Resource and Cost Optimization, and Fairness, with a change log tracking updates.[^s1]

**Architecture Fundamentals.** Explanations of how the platform works underneath, including architecture basics (transactions, metadata versus data, platform APIs), integration patterns, multitenant architecture and platform sharing architecture. These cover design constraints that a customer cannot change, so they explain why certain limits exist.[^s5]

**Decision Guides.** Comparisons that help architects pick between overlapping tools. The platform guides cover asynchronous processing, building forms, choosing between agentic and traditional workflow automation, event-driven architecture, a step-based async framework, and record-triggered automation (Flow versus hybrid Flow with invocable Apex versus Apex triggers).[^s2] Data guides cover data integration and Data 360 interoperability and provisioning.[^s1]

**Diagrams.** The Salesforce Diagrams framework defines six diagram types (capability map, system landscape, solution architecture, roadmap, interaction/process/flow, and data model) and a "kit of parts" of standard components: header, cards, card attributes, connectors, card icons and footers.[^s3] Its Reference Architecture Gallery and Data Model Gallery supply examples and templates, and Salesforce's guidance is that each diagram should carry one message and read left to right, top to bottom.[^s3]

## How to use it, and gotchas

Salesforce's advice to Certified Technical Architect candidates shows the intended workflow: use the fundamentals to close knowledge gaps found in mock reviews, use decision guides to structure and justify choices by citing established patterns, test a design against each Well-Architected pillar, and practice reproducing in-scope data models from the galleries.[^s5] The same advice warns about solutions in which each component is sound on its own but the whole feels fragmented.[^s5]

Three practical gotchas apply. First, the content changes between releases. The Well-Architected pillars were reorganized in 2026, so older posts that list Secure, Reliable, Engaging and Composable reflect an earlier structure than the five pillars shown on the site today.[^s1][^s5] Second, decision guides compare options and give recommendations. They are inputs to a trade-off decision, not rules, and they don't replace checking the limits for a specific org. Third, some resources live elsewhere: the Architect Digest newsletter is a LinkedIn sign-up, and the diagram templates are built for Lucidchart. Salesforce notes that footer icons in template-based diagrams can come detached from their cards.[^s1][^s3]

## Connections

The Center is the public face of the broader `kt:salesforce-architecture-program` that Salesforce relaunched in 2025.[^s4] It **has part** `kt:well-architected-framework`, `kt:architect-decision-guides` and `kt:salesforce-diagrams`, its three main bodies of guidance.[^s1][^s2][^s3] Its fundamentals explain `kt:multitenancy`, the `kt:salesforce-sharing-model` and `kt:integration-patterns`.[^s5] Its decision guides cover `kt:record-triggered-flow` versus Apex and `kt:event-driven-architecture` tooling.[^s2] It is **used by** the `kt:salesforce-architect` role, and Salesforce points candidates for the `kt:cta-review-board` to it as core preparation material.[^s5]

## Sources

[^s1]: Salesforce Architects, "Salesforce Architects (Architecture Center home and Well-Architected entry)". https://architect.salesforce.com/well-architected (accessed 2026-11-04)
[^s2]: Salesforce Architects, "Get Started with Platform Decision Guides". https://architect.salesforce.com/docs/architect/decision-guides/guide/get-started-platform-decision-guides.html (accessed 2026-11-04)
[^s3]: Salesforce Architects, "Salesforce Diagrams — Framework Overview". https://architect.salesforce.com/diagrams/framework/overview (accessed 2026-11-04)
[^s4]: Salesforce, "Relaunching the Salesforce Architecture Program" (Christophe Coenraets, 2025-10-12). https://www.salesforce.com/blog/relaunching-salesforce-architecture-program/ (accessed 2026-11-04)
[^s5]: Salesforce, "5 Salesforce Architecture Resources Every CTA Candidate Should Use". https://www.salesforce.com/blog/architecture-resources-for-cta/ (accessed 2026-11-04)
[^s6]: Salesforce Architects, "Architects, Welcome Home" (Zayne Turner, 2020-12-17). https://medium.com/salesforce-architects/architects-welcome-home-4bf2a00a5471 (accessed 2026-11-04)
