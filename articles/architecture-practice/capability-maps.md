---
id: kt:capability-maps
type: Concept
title: Capability Maps
aliases: [capability map, business capability map, business capability model, capability mapping, technical capability map]
domain: architecture-practice
summary: >-
  A business-architecture artifact that lays out what an organization must be able to do, independent of its org
  chart, processes and systems, so architects can tie business drivers to Salesforce products, find gaps and
  prioritize a roadmap; Salesforce Architects publishes capability-map templates in its Reference Architecture Gallery.
release: "Winter '27"
status: concept
broader: [kt:business-architecture]
related: [kt:salesforce-diagrams, kt:salesforce-center-of-excellence, kt:architecture-decision-records, kt:value-streams, kt:salesforce-industries]
relations:
  - {predicate: usedBy, object: kt:salesforce-architect}
  - {predicate: enables, object: kt:technology-roadmaps}
sources:
  - id: s1
    title: "TOGAF Series Guide: Business Capabilities, Version 2"
    publisher: The Open Group
    url: https://pubs.opengroup.org/togaf-standard/business-architecture/business-capabilities.html
    type: standards-body
    accessed: 2026-11-10
  - id: s2
    title: "TOGAF Series Guide: Business Capability Planning"
    publisher: The Open Group
    url: https://pubs.opengroup.org/togaf-standard/business-architecture/business-capability-planning.html
    type: standards-body
    accessed: 2026-11-10
  - id: s3
    title: "Capability Map (Reference Diagrams)"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/reference-diagrams/guide/section-capability-map.html
    type: official-docs
    accessed: 2026-11-10
  - id: s4
    title: "Business Capability Map (Reference Diagrams)"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/reference-diagrams/guide/business-capability-map
    type: official-docs
    accessed: 2026-11-10
  - id: s5
    title: "Design a Business Capability Map (Diagramming Essentials)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/fr/content/learn/modules/diagramming-essentials/design-a-business-capability-map
    type: official-learning
    accessed: 2026-11-10
  - id: s6
    title: "Architect's Guide to Effective Roadmaps"
    publisher: Salesforce Architects (Marc Braga)
    url: https://medium.com/salesforce-architects/architects-guide-to-effective-roadmaps-fa8cbbb573e9
    type: official-blog
    accessed: 2026-11-10
created: 2026-11-10
---

# Capability Maps

A capability map is a picture of everything an organization needs to be able to do, drawn so that business and technical stakeholders can see how strategy, capabilities and technology fit together.[^s1][^s3] The Open Group defines a business capability simply as a business's ability to do something, and it stresses that a capability states *what* the business does rather than how, why or where it does it.[^s1] Salesforce Architects treats capability maps as a strategic planning tool for aligning business goals with the technical implementation, and publishes ready-made templates for them.[^s3]

## What a capability map contains

In TOGAF's business-architecture guidance, a capability map is the complete and stable set of an enterprise's business capabilities, grouped into categories and shown at a chosen level of detail.[^s1] Because it is deliberately independent of the current organization structure, processes, IT systems and products, it changes far less often than any of them.[^s1] Each capability is delivered by four kinds of enabler: people, processes, information and resources such as systems and assets. Those enablers can be swapped while the capability itself stays put.[^s1]

Two structuring techniques keep a map readable. *Stratification* sorts top-level capabilities into strategic (direction-setting), core (customer-facing) and supporting (behind-the-scenes) tiers. *Leveling* decomposes each level-1 capability into children, typically to three to six levels.[^s1] Names follow a noun-verb pattern built on a business object, such as "Project Management", and each description begins "the ability to…".[^s1]

## The Salesforce flavour

The Salesforce Architects Reference Architecture Gallery has a capability-map section with four diagrams: a generic Business Capability Map, a Data 360 Technical Capability Map, a Loyalty Management Capability Map, and a Center of Excellence diagram.[^s3] The business template places business drivers, meaning the strategic goals or external pressures that force change (for example revenue growth, cost reduction or customer retention), above the capabilities, with high-level Salesforce product positioning beneath. It is offered as an editable Lucid template and a downloadable image.[^s4]

The Trailhead *Diagramming Essentials* module walks through customizing that template for a fictional real-estate firm. Drivers go across the top under a single vision statement, and capability categories run in columns with functional details below. Categories that do not yet exist are flagged with an asterisk to separate new capabilities from the current stack.[^s5] Unlike TOGAF's product-neutral map, the Salesforce template mixes in product positioning, so it works best as a solution-facing view built on top of a neutral capability model.[^s1][^s4]

## How architects use one

A capability map is the input to most planning conversations. TOGAF lists a common vocabulary, sharper investment focus, project alignment and stakeholder agreement before solutioning among its benefits.[^s1] Heat maps colour capabilities by a chosen lens. In the guide's maturity example, green means at target, yellow one level short, red two or more levels short, and purple a capability that is wanted but does not yet exist. Other lenses include strategic contribution, cost, coverage and criticality.[^s1]

Capability-based planning then maps capabilities to value-stream stages to see which ones matter most to stakeholders. It finds gaps in each capability's people, process, application or data components and sequences them into plateaus that become the roadmap.[^s2] Salesforce Architects describes the same chain for Salesforce programs: build the capability map with dependent teams, run a capability gap analysis of today's state against the needed capabilities, then let that analysis set the phasing and choice of roadmap. A business capability roadmap is aimed at executives.[^s6]

## Gotchas

- Don't copy the org chart. Naming capabilities after departments ties the map to structures that change often and hides duplicated capabilities across units.[^s1]
- Avoid vague names that mix several concepts, and check for cross-cutting capabilities, such as business planning, that no single unit owns.[^s1]
- Bottom-up mapping without governance and senior sponsorship is slow and hard to reconcile. TOGAF suggests combining a top-down pass of about 20–30 high-level capabilities with bottom-up detail.[^s1]
- Heat-map colours are usually a team judgment, not a formal score, so record the reasoning behind them.[^s2]

## Connections

Capability maps are a core artifact of `kt:business-architecture`, and TOGAF links them to `kt:value-streams`, whose stages show which capabilities create stakeholder value.[^s1][^s2] They are drawn with the templates and iconography of `kt:salesforce-diagrams`, and the same gallery section includes a diagram for the `kt:salesforce-center-of-excellence`, the body that usually owns the map and its priorities.[^s3][^s5] The map is **used by** the `kt:salesforce-architect` and **enables** `kt:technology-roadmaps` through gap analysis.[^s6] Decisions taken while closing a gap can be preserved as `kt:architecture-decision-records`.[^s2] Industry-specific maps such as the Loyalty Management and Data 360 examples connect capability thinking to `kt:salesforce-industries` products.[^s3]

## Sources

[^s1]: The Open Group, "TOGAF Series Guide: Business Capabilities, Version 2". https://pubs.opengroup.org/togaf-standard/business-architecture/business-capabilities.html (accessed 2026-11-10)
[^s2]: The Open Group, "TOGAF Series Guide: Business Capability Planning". https://pubs.opengroup.org/togaf-standard/business-architecture/business-capability-planning.html (accessed 2026-11-10)
[^s3]: Salesforce Architects, "Capability Map" reference diagrams. https://architect.salesforce.com/docs/architect/reference-diagrams/guide/section-capability-map.html (accessed 2026-11-10)
[^s4]: Salesforce Architects, "Business Capability Map". https://architect.salesforce.com/docs/architect/reference-diagrams/guide/business-capability-map (accessed 2026-11-10)
[^s5]: Trailhead, "Design a Business Capability Map", Diagramming Essentials module. https://trailhead.salesforce.com/fr/content/learn/modules/diagramming-essentials/design-a-business-capability-map (accessed 2026-11-10)
[^s6]: Marc Braga, "Architect's Guide to Effective Roadmaps", Salesforce Architects, 21 Mar 2023. https://medium.com/salesforce-architects/architects-guide-to-effective-roadmaps-fa8cbbb573e9 (accessed 2026-11-10)
