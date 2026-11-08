---
id: kt:salesforce-diagrams
type: Tool
title: Salesforce Diagrams
aliases: [Salesforce Diagrams framework, Salesforce architecture diagrams, Salesforce Diagram Framework]
domain: architecture-practice
summary: >-
  Salesforce Architects' standard for drawing architecture diagrams: two styles (Marketing, Strategy & Sales vs.
  Documentation & Implementation), four C4-inspired levels of detail, six diagram types, a kit of standard
  components, and templates in a Reference Architecture Gallery on architect.salesforce.com.
release: "Winter '27"
status: current
broader: [kt:salesforce-architecture-center]
related: [kt:data-architecture, kt:solution-design-tradeoffs, kt:architecture-decision-records, kt:integration-patterns, kt:cta-review-board]
relations:
  - {predicate: partOf, object: kt:salesforce-architecture-center}
  - {predicate: usedBy, object: kt:salesforce-architect}
sources:
  - id: s1
    title: "Salesforce Diagrams: Framework Overview"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/diagrams/framework/overview
    type: official-docs
    accessed: 2026-11-08
  - id: s2
    title: "Salesforce Diagrams: Documentation & Implementation"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/diagrams/framework/docs-implementation
    type: official-docs
    accessed: 2026-11-08
  - id: s3
    title: "Salesforce Diagrams: Marketing, Strategy & Sales"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/diagrams/framework/marketing-strategy-sales
    type: official-docs
    accessed: 2026-11-08
  - id: s4
    title: "Introducing Salesforce Diagrams"
    publisher: Salesforce Architects (Medium)
    url: https://medium.com/salesforce-architects/introducing-salesforce-diagrams-a8fa7bc4a3e
    type: official-blog
    accessed: 2026-11-08
  - id: s5
    title: "Salesforce Architecture Diagrams: Quick Look — Understanding Salesforce Architecture Diagrams"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/archdia/archdia-1
    type: official-learning
    accessed: 2026-11-08
created: 2026-11-08
---

# Salesforce Diagrams

Salesforce Diagrams is the diagramming standard published by Salesforce Architects on architect.salesforce.com. It defines how to draw Salesforce architecture pictures so that they look consistent and carry the right amount of detail for their audience. The framework's stated goals are to communicate ideas to many kinds of stakeholders, to give delivery teams a single source of truth on an implementation, and to help business stakeholders make purchasing and technology decisions.[^s1]

## Why it exists

Salesforce introduced the framework in June 2021. The launch post argued that architects had drifted away from formal modeling languages such as UML and SysML for the sake of agility, and that searching for Salesforce diagrams mostly returned ad-hoc, outdated static images.[^s4] Surveys with more than 800 responses, plus workshops, found inconsistent detail and appearance, no Salesforce-provided icons or templates, and no single trustworthy place to find resources.[^s4] The answer was a lightweight framework with a common notation, built by Salesforce's design systems team, and a gallery of templates.[^s4]

## How it works

**Two styles.** Diagrams are split by purpose and audience. *Marketing, Strategy & Sales* diagrams answer why a team is doing something: capabilities and products that deliver business value. *Documentation & Implementation* diagrams answer how: an implementation-ready view of the solution's functionality.[^s4] Trailhead frames a similar split between high-level reference architecture diagrams, often shown to executives to present vision and strategy, and more prescriptive solution architecture diagrams that name the specific tools a delivery team needs.[^s5]

**Four levels of detail.** Borrowing from the C4 model, each style runs from Level 1 to Level 4.[^s4] In the Documentation & Implementation style, Level 1 is "the big picture", a broad system landscape with little detail. Level 2 is a piece of the whole, adding integration points and the general direction of data flow but no time-based interactions. Level 3 is a process or interaction view with sequenced steps and data flows. Level 4, "the double click", zooms into one narrow part of a process for fine-grained technical specification.[^s2] The Marketing, Strategy & Sales levels follow the same arc, from business capabilities and product positioning down to a single channel's process in enough detail that delivery teams can start writing user stories.[^s3]

**Six diagram types.** The overview lists capability maps, system landscapes, solution architecture, roadmaps, interaction/process/flow diagrams, and data models.[^s1] Each type is meant to be used as a template once the author has defined the message, the audience, and the logical scope.[^s1]

**Standard components.** Every diagram has a header (title plus a short statement of purpose, scope and message) and is built from cards that stand for systems, concepts or entities. Cards carry attributes, icons and footers, and connectors show the relationships between them.[^s1]

## Principles and gotchas

The framework asks diagrams to read left to right and top to bottom, to convey one message each, and to stick to the critical information for one topic. When a picture gets crowded, the guidance is to draw several diagrams instead of one overloaded one.[^s1] The level model enforces this: keep time-based sequencing out of Level 2 and save it for Level 3.[^s2]

Templates are offered in Lucidchart, Google Slides and PowerPoint.[^s3][^s4] The Reference Architecture Gallery holds examples for every diagram type except data models, which live in a separate Data Model Gallery on developer.salesforce.com.[^s1] One known Lucidchart quirk is that footer icons can come undocked from their card in template-based diagrams, so they have to be dragged back into the footer.[^s1]

## When to use it (and when not)

Use the framework when diagrams have to work for both executives and delivery teams, or when a programme needs one shared visual language across partners. Pick the style by audience, then the level by how much detail the decision in hand needs.[^s3][^s4] It is a communication standard, not a modeling language. It does not replace UML-style rigor where that is required, and it does not record why a design was chosen.[^s4]

## Connections

Salesforce Diagrams is **part of** the `kt:salesforce-architecture-center`, alongside the Well-Architected framework and decision guides, and is **used by** the `kt:salesforce-architect` role to communicate designs to stakeholders.[^s1][^s5] Its data model type and the Data Model Gallery tie it to `kt:data-architecture`.[^s1] Level 2 and Level 3 diagrams are how architects show `kt:integration-patterns` and data flows.[^s2] Diagrams make a chosen design visible, while `kt:solution-design-tradeoffs` and `kt:architecture-decision-records` capture why it was chosen.[^s4] Trailhead describes diagrams as the way architects present a proposed design to stakeholders and project teams, and that same skill is what a candidate exercises at the `kt:cta-review-board`.[^s5]

## Sources
[^s1]: Salesforce Architects, "Salesforce Diagrams: Framework Overview". https://architect.salesforce.com/diagrams/framework/overview (accessed 2026-11-08)
[^s2]: Salesforce Architects, "Salesforce Diagrams: Documentation & Implementation". https://architect.salesforce.com/diagrams/framework/docs-implementation (accessed 2026-11-08)
[^s3]: Salesforce Architects, "Salesforce Diagrams: Marketing, Strategy & Sales". https://architect.salesforce.com/diagrams/framework/marketing-strategy-sales (accessed 2026-11-08)
[^s4]: Marc Braga, "Introducing Salesforce Diagrams", Salesforce Architects (Medium), June 2021. https://medium.com/salesforce-architects/introducing-salesforce-diagrams-a8fa7bc4a3e (accessed 2026-11-08)
[^s5]: Trailhead, "Salesforce Architecture Diagrams: Quick Look — Understanding Salesforce Architecture Diagrams". https://trailhead.salesforce.com/content/learn/modules/archdia/archdia-1 (accessed 2026-11-08)
