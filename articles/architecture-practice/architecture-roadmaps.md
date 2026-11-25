---
id: kt:architecture-roadmaps
type: Concept
title: Architecture Roadmaps
aliases: [architecture roadmap, technology roadmap, business capability roadmap, capability roadmap, system roadmap, component roadmap, feature roadmap, Salesforce roadmap]
domain: architecture-practice
summary: >-
  A phased, prioritized view of how a Salesforce program moves from its current state to a target state over roughly
  the next 12–24 months, drawn as business (capability, feature) or technology (system, component) roadmaps for
  different audiences and grounded in capability gap analysis; TOGAF calls the equivalent artifact the Architecture Roadmap.
release: "Winter '27"
status: concept
broader: [kt:enterprise-architecture]
related: [kt:capability-maps, kt:togaf, kt:salesforce-center-of-excellence, kt:salesforce-diagrams, kt:fit-gap-analysis, kt:release-management]
relations:
  - {predicate: usedBy, object: kt:salesforce-architect}
  - {predicate: dependsOn, object: kt:capability-maps}
  - {predicate: contrastsWith, object: kt:statement-of-work}
sources:
  - id: s1
    title: "Architect's Guide to Effective Roadmaps"
    publisher: Salesforce Architects (Marc Braga)
    url: https://medium.com/salesforce-architects/architects-guide-to-effective-roadmaps-fa8cbbb573e9
    type: official-blog
    accessed: 2026-11-25
  - id: s2
    title: "Roadmap (Reference Diagrams)"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/reference-diagrams/guide/section-roadmap
    type: official-docs
    accessed: 2026-11-25
  - id: s3
    title: "Capability Roadmap (Diagram Template Gallery)"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/diagrams/template-gallery/capability-roadmap
    type: official-docs
    accessed: 2026-11-25
  - id: s4
    title: "The TOGAF Standard, Phase E: Opportunities & Solutions"
    publisher: The Open Group
    url: https://pubs.opengroup.org/togaf-standard/adm/chap09.html
    type: standards-body
    accessed: 2026-11-25
  - id: s5
    title: "The TOGAF Standard, Phase F: Migration Planning"
    publisher: The Open Group
    url: https://pubs.opengroup.org/togaf-standard/adm/chap10.html
    type: standards-body
    accessed: 2026-11-25
  - id: s6
    title: "Implement Your Salesforce CoE's Core Capabilities (Salesforce Governance with a Center of Excellence)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-governance-with-a-center-of-excellence/implement-your-salesforce-coes-core-capabilities
    type: official-learning
    accessed: 2026-11-25
created: 2026-11-25
---

# Architecture Roadmaps

An architecture roadmap is the plan that shows how a Salesforce program gets from where it is today to where the business wants it to be. Salesforce Architects describes a good roadmap as prioritized, validated and well defined. It is a phased plan for roughly the next 12 to 24 months, oriented to business value, and ideally fits on a single view.[^s1] Just as important is what it is not: it is not a statement of work, a requirements document, a five-year long-range plan, or a task-level project plan.[^s1] In the TOGAF Standard the same idea appears as the Architecture Roadmap, a timeline of work packages and Transition Architectures leading from the Baseline to the Target Architecture.[^s4]

## Four roadmap types for four audiences

Salesforce Architects splits roadmaps into two styles with two types each, because one roadmap rarely serves every stakeholder.[^s1]

- **Business roadmaps** prepare the business for change and align IT investment with business priorities.[^s1]
  - A *capability roadmap* tells executives which capabilities will be enabled in a timeframe. It groups them and shows order, dependencies and the kind of business value each delivers.[^s1][^s3]
  - A *feature roadmap* zooms into one capability and lists its supporting features, for business resource planning, budgeting and change management.[^s1][^s2]
- **Technology roadmaps** prepare technology teams for change, support budget and resource allocation, and expose cross-team dependencies.[^s1]
  - A *system roadmap* shows which systems will be implemented when, grouped into functional areas, with order and dependencies.[^s1][^s2]
  - A *component roadmap* goes down to the functionality of specific technology components and their timeframes.[^s1][^s2]

The Reference Diagrams gallery publishes templates for all four types. It also offers an Agentforce Release Plan for a first generative AI release and an example Agentforce Roadmap for rolling AI out across a Customer 360 implementation.[^s2]

## How a roadmap is built

The Salesforce method has four steps: collaborate, focus, prioritize and deliver.[^s1] First, work with the dependent teams to build a capability map of the business drivers and the capabilities the vision needs. Next, run a capability gap analysis of today's state against those capabilities. Then use the gap analysis and the business objectives to choose the phasing and priorities. Finally, pick the roadmap style and type that suit the audience and present it.[^s1] Phasing themes help stakeholders follow the logic. Examples are crawl-walk-run, low-hanging fruit first, or foundational, then strategic, then transformational.[^s1]

TOGAF formalizes the same chain. In Phase E, gaps from the business, data, application and technology architectures are merged into one consolidated gaps, solutions and dependencies matrix. They are grouped into work packages, and Transition Architectures are added wherever change has to be incremental. Each Transition Architecture should deliver measurable business value, and they need not be evenly spaced.[^s4] Those pieces are combined into a draft roadmap. Phase F then prioritizes projects by cost, benefit and risk, reviews the spans between transitions against business value and risk, and confirms the final roadmap behind the Implementation and Migration Plan.[^s4][^s5]

## Ownership and governance

In a Salesforce Center of Excellence, the roadmap belongs to the transformation-management capability, which explains the *why* behind the work. The CoE collects requested projects and initiatives into an ordered list, turns them into a schedule of features and milestones, and publishes and updates it for the organization.[^s6] It decides priority with business cases and ROI metrics and with a fair, documented intake process.[^s6] The roadmap then feeds environment and release management. That function keeps a predictable release schedule and still leaves room for maintenance and technical debt.[^s6]

## Gotchas

- Tie every phase to business value statements, objectives and KPIs. That link is what settles disputes between stakeholders over priority.[^s1]
- State the risks of the chosen sequence and the alternatives you rejected. Otherwise the roadmap reads as a wish list.[^s1]
- Don't give executives a component roadmap or engineers a capability roadmap. Match the type to the audience.[^s1]
- A roadmap built without a capability map and gap analysis tends to sequence projects by who asked loudest rather than by dependency.[^s1][^s4]
- Treat the roadmap as a living document. TOGAF revises it in Phase F as increments are finalized, and the CoE republishes it as priorities change.[^s5][^s6]

## Connections

A roadmap **depends on** `kt:capability-maps`. The capability map and its gap analysis set the phasing, and `kt:fit-gap-analysis` supplies the solution-level gaps that become work packages.[^s1][^s4] TOGAF's Architecture Roadmap and Transition Architectures come from `kt:togaf`, part of the wider `kt:enterprise-architecture` discipline.[^s4][^s5] Roadmaps are drawn with the templates of `kt:salesforce-diagrams` and owned by the `kt:salesforce-center-of-excellence`, whose schedule drives `kt:release-management`.[^s2][^s6] The roadmap is **used by** the `kt:salesforce-architect`. It **contrasts with** a `kt:statement-of-work`, which binds delivery scope, whereas a roadmap stays a strategic, phased view.[^s1]

## Sources

[^s1]: Marc Braga, "Architect's Guide to Effective Roadmaps", Salesforce Architects, 21 Mar 2023. https://medium.com/salesforce-architects/architects-guide-to-effective-roadmaps-fa8cbbb573e9 (accessed 2026-11-25)
[^s2]: Salesforce Architects, "Roadmap" reference diagrams. https://architect.salesforce.com/docs/architect/reference-diagrams/guide/section-roadmap (accessed 2026-11-25)
[^s3]: Salesforce Architects, "Capability Roadmap" template. https://architect.salesforce.com/diagrams/template-gallery/capability-roadmap (accessed 2026-11-25)
[^s4]: The Open Group, "The TOGAF Standard, Phase E: Opportunities & Solutions". https://pubs.opengroup.org/togaf-standard/adm/chap09.html (accessed 2026-11-25)
[^s5]: The Open Group, "The TOGAF Standard, Phase F: Migration Planning". https://pubs.opengroup.org/togaf-standard/adm/chap10.html (accessed 2026-11-25)
[^s6]: Trailhead, "Implement Your Salesforce CoE's Core Capabilities", Salesforce Governance with a Center of Excellence module. https://trailhead.salesforce.com/content/learn/modules/salesforce-governance-with-a-center-of-excellence/implement-your-salesforce-coes-core-capabilities (accessed 2026-11-25)
