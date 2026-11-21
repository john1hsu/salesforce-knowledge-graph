---
id: kt:reference-architectures
type: Concept
title: Reference Architectures
aliases: [Reference Architecture Gallery, Salesforce Reference Diagrams, reference architecture diagram, Salesforce reference architecture]
domain: architecture-practice
summary: >-
  Reusable, high-level architecture blueprints that capture recommended patterns and best practices for a class of
  solution; Salesforce publishes them as Reference Diagrams in the Reference Architecture Gallery on
  architect.salesforce.com, grouped into five diagram types with editable Lucidchart templates.
release: "Winter '27"
status: current
broader: [kt:salesforce-diagrams, kt:salesforce-architecture-center]
related: [kt:capability-maps, kt:solution-design-document, kt:integration-patterns, kt:org-strategy, kt:data-cloud, kt:agentforce]
relations:
  - {predicate: partOf, object: kt:salesforce-architecture-center}
  - {predicate: usedBy, object: kt:salesforce-architect}
sources:
  - id: s1
    title: "Salesforce Diagrams (Reference Diagrams and Reference Architecture Gallery)"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/diagrams
    type: official-docs
    accessed: 2026-11-21
  - id: s2
    title: "Drive Architectural Alignment with Salesforce Reference Diagrams"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/architectural-alignment-reference-diagrams/
    type: official-blog
    accessed: 2026-11-21
  - id: s3
    title: "System Landscape | Reference Diagrams"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/reference-diagrams/guide/section-system-landscape
    type: official-docs
    accessed: 2026-11-21
  - id: s4
    title: "Agentforce System Landscape | Reference Diagrams"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/reference-diagrams/guide/einstein-system-landscape
    type: official-docs
    accessed: 2026-11-21
  - id: s5
    title: "Understanding Salesforce Architecture Diagrams"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/archdia/archdia-1
    type: official-learning
    accessed: 2026-11-21
  - id: s6
    title: "NIST Cloud Computing Reference Architecture (SP 500-292)"
    publisher: NIST
    url: https://www.nist.gov/publications/nist-cloud-computing-reference-architecture?i=c3
    type: standards-body
    accessed: 2026-11-21
created: 2026-11-21
---

# Reference Architectures

A **reference architecture** is a high-level, reusable picture of how a kind of solution should be put together. It records recommended patterns and best practices rather than the exact build of one project. Trailhead frames it as a broad overview of a system's design, often used to explain a solution's vision and strategy to executives and stakeholders.[^s5] Its house analogy: the blueprint shows there is a bathroom but not what color the sink is.[^s5] The idea is not Salesforce-specific. NIST's SP 500-292 (2011), for example, publishes a cloud computing reference architecture and taxonomy as a common reference point for government-wide use.[^s6]

In the Salesforce ecosystem the term usually means the **Reference Diagrams** that Salesforce Architects publish on architect.salesforce.com. The diagrams page pairs how-to guides with a **Reference Architecture Gallery** of ready-made examples.[^s1]

## What the gallery contains

The diagrams page has two parts. The *Reference Diagrams* guides cover how to build Salesforce diagrams, the standard components (shown as a Data 360 architecture kit), and Salesforce's data model notation.[^s1] The *Reference Architecture Gallery* is organized under five headings: Capability Map, Interaction Process Flow, Solution Architecture, System Landscape and Roadmap.[^s1] At this writing it lists about 25 entries. Examples include a business capability map, a Center of Excellence map, asynchronous processing with Platform Events, the claim-check and queuing integration flows, zero-copy data integration with Data 360, a single-org architecture, a role-hierarchy landscape, and several Agentforce roadmaps and release plans.[^s1]

Each entry links to a guide page with a short description and the editable assets. The **Agentforce System Landscape** entry is one example. It shows the products and systems available with Agentforce, including the Einstein Trust Layer and the generative AI stack (prompt templates, LLM gateway, external models and bring-your-own-model) alongside Data 360. The page links to a Lucid editor and an image download.[^s4] The System Landscape section frames these diagrams as a full view of an organization's technology ecosystem: Salesforce products, external systems and the integration points between them.[^s3]

## The five diagram types

Salesforce's 2026 refresh of the diagrams settles on five core types.[^s2]

- **Capability maps** and **roadmaps** suit business stakeholders who need the what and the when.[^s2]
- **System landscapes** show which products and systems are involved and how they connect.[^s2][^s3]
- **Solution architectures** are the implementation-team view of a specific design.[^s2]
- **Interaction process flows** show the sequence of steps between systems, which the refresh streamlined.[^s2]

The same refresh updated the diagrams for Agentforce, accessibility and product renames such as Data Cloud becoming Data 360. It also retired diagrams that had been made for the Decision Guides and Fundamentals content.[^s2] The older Salesforce Diagrams framework also treats data models as a diagram type, but the gallery's five headings leave them out.[^s1]

## How to use them

The recommended workflow is to open the gallery, browse by use case, industry or product, open the closest template in Lucidchart, and adapt it. Salesforce's advice is not to start from a blank canvas.[^s2] Lucidchart offers three Salesforce shape libraries (Salesforce Header, Salesforce Cards and Salesforce Icons), so adapted diagrams keep the standard notation.[^s2] Salesforce describes the payoff as alignment: a shared diagram works as a visual contract between business and technical stakeholders.[^s2]

**Gotchas.** A reference diagram is a starting point, not a design decision. Trailhead contrasts it with a **solution architecture diagram**, which is more prescriptive and names the specific tools and resources a delivery team will use.[^s5] Names also drift during renames: the System Landscape guide still lists a "Customer 360 Marketing" landscape that the gallery calls "Data 360 Marketing", and the Agentforce page's URL still says "einstein".[^s1][^s3][^s4]

## When to use it (and when not)

Use a reference architecture early: in discovery, pre-sales, or when a programme needs one shared target picture before detailed design. Move to solution architecture diagrams and a solution design document once scope and licensing are fixed.[^s5][^s2] Reference diagrams show what is recommended, not why one option was chosen for this customer. That reasoning belongs in design trade-off records.[^s2]

## Connections

Reference architectures are the example library of `kt:salesforce-diagrams` and are **part of** the `kt:salesforce-architecture-center`, where the gallery lives.[^s1] The `kt:salesforce-architect` role **uses** them to align stakeholders.[^s2] The gallery's capability-map entries are worked examples of `kt:capability-maps`, and its interaction flows (claim check, queuing, Platform Events) illustrate `kt:integration-patterns`.[^s1] The single-org architecture entry relates to `kt:org-strategy`.[^s1] Many entries are built around `kt:data-cloud` (Data 360) and `kt:agentforce`.[^s1][^s4] Once a project moves from vision to build, the prescriptive detail belongs in a `kt:solution-design-document`.[^s5]

## Sources
[^s1]: Salesforce Architects, "Salesforce Diagrams" (Reference Diagrams and Reference Architecture Gallery). https://architect.salesforce.com/diagrams (accessed 2026-11-21)
[^s2]: Peter Laird, "Drive Architectural Alignment with Salesforce Reference Diagrams", Salesforce blog, June 2026. https://www.salesforce.com/blog/architectural-alignment-reference-diagrams/ (accessed 2026-11-21)
[^s3]: Salesforce Architects, "System Landscape | Reference Diagrams". https://architect.salesforce.com/docs/architect/reference-diagrams/guide/section-system-landscape (accessed 2026-11-21)
[^s4]: Salesforce Architects, "Agentforce System Landscape | Reference Diagrams". https://architect.salesforce.com/docs/architect/reference-diagrams/guide/einstein-system-landscape (accessed 2026-11-21)
[^s5]: Trailhead, "Understanding Salesforce Architecture Diagrams". https://trailhead.salesforce.com/content/learn/modules/archdia/archdia-1 (accessed 2026-11-21)
[^s6]: NIST, "NIST Cloud Computing Reference Architecture", Special Publication 500-292, September 2011. https://www.nist.gov/publications/nist-cloud-computing-reference-architecture?i=c3 (accessed 2026-11-21)
