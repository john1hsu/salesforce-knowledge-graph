---
id: kt:system-landscape-diagrams
type: Concept
title: System Landscape Diagrams
aliases: [system landscape diagram, system landscape, architectural landscape diagram, systems landscape]
domain: architecture-practice
summary: >-
  The broadest architecture picture in a Salesforce programme: a map of the Salesforce products, external systems and
  integration points in an organization's technology ecosystem, used to see topology and dependencies before zooming
  into solution, process and data diagrams; Salesforce Architects publishes landscape templates in its Reference
  Diagrams gallery.
release: "Winter '27"
status: concept
broader: [kt:salesforce-diagrams]
related: [kt:capability-maps, kt:integration-patterns, kt:solution-design-document, kt:reference-architectures, kt:org-strategy, kt:interface-specification-document]
relations:
  - {predicate: usedBy, object: kt:salesforce-architect}
  - {predicate: partOf, object: kt:salesforce-diagrams}
sources:
  - id: s1
    title: "System Landscape (Reference Diagrams)"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/reference-diagrams/guide/section-system-landscape
    type: official-docs
    accessed: 2026-11-22
  - id: s2
    title: "Agentforce System Landscape (Reference Diagrams)"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/reference-diagrams/guide/einstein-system-landscape
    type: official-docs
    accessed: 2026-11-22
  - id: s3
    title: "Salesforce Diagrams: Documentation & Implementation"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/diagrams/framework/docs-implementation
    type: official-docs
    accessed: 2026-11-22
  - id: s4
    title: "Project Documentation for Salesforce B2C Commerce Technical Architects: Document the Architectural Landscape"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/b2c-project-docs-for-technical-architects/b2c-doc-architectural-landscape
    type: official-learning
    accessed: 2026-11-22
  - id: s5
    title: "System landscape diagram"
    publisher: C4 model (Simon Brown)
    url: https://c4model.com/diagrams/system-landscape
    type: community
    accessed: 2026-11-22
created: 2026-11-22
---

# System Landscape Diagrams

A system landscape diagram is the widest-angle picture an architect draws of an implementation. Salesforce Architects describes it as a comprehensive view of an organization's technology ecosystem: the Salesforce products in play, the external systems around them, and the integration points that connect them.[^s1] Its job is to make the topology visible so architects can spot dependencies and plan the implementation strategically, and it doubles as reference documentation for stakeholders.[^s1]

## Where it sits in the diagram hierarchy

In the Salesforce Diagrams framework, the Documentation & Implementation style runs through four levels of zoom. Level 1, "The Big Picture", is an overview of the system landscape or solution: it names the products and technologies involved but deliberately leaves most detail out so the viewer is not overwhelmed.[^s3] Level 2 narrows to a subset of products and adds key integration points and the general direction of data flow; Level 3 brings in sequenced, time-based interactions for a single process; Level 4 is the fine-grained technical specification for a narrow slice.[^s3] A landscape is therefore the entry point that the more detailed solution, process and interaction diagrams zoom into.[^s3]

The same idea exists outside Salesforce. The C4 model calls a landscape a map of the software systems within a chosen scope, such as an enterprise or department, and describes it as essentially a system context diagram without a single system at its centre.[^s5] C4 positions it for people responsible for a portfolio of systems, aimed at technical and non-technical readers, and recommends it especially for larger organizations.[^s5]

## What goes on it

The Salesforce reference landscapes mix Salesforce clouds with non-Salesforce technology. The gallery's examples include a Customer 360 marketing landscape, a retail landscape built around B2C Commerce and Marketing, and an Agentforce landscape.[^s1] The Agentforce example shows how the Einstein trust layer, a generative AI stack (prompt templates, an LLM gateway, external and bring-your-own models) and Data 360 together form the foundation for agentic applications.[^s2] Reference diagrams are offered as images and as editable Lucidchart files, and the framework's level examples are also available as Google Slides and PowerPoint copies.[^s2][^s3]

Trailhead's B2C Commerce architect guidance shows what a project-specific landscape should capture. The architecture diagram gives a visual overview of which systems are in scope and how they interact, including commerce, partner technology and third-party systems.[^s4] It should make clear which system is the system of record for each piece of data.[^s4] A separate data flow diagram traces how data moves between applications and transfer points, and a manual process that involves no system integration is left off the architecture diagram.[^s4]

## Practical guidance and gotchas

- **Keep it at Level 1.** Put time-based sequencing and detailed payloads in lower-level diagrams; the landscape should stay readable at a glance.[^s3]
- **Check it for gaps.** Trailhead's sample is deliberately incomplete, missing flows such as ERP-to-inventory and the format between platform and middleware; reviewing for gaps is part of the job.[^s4]
- **Pair it with tables.** Scheduled jobs, a job execution plan and a summary of third-party integrations live in tables next to the diagram, with per-integration interface specifications below.[^s4]
- **Start from a template.** Adapting a gallery landscape is faster than drawing from scratch and keeps the notation consistent.[^s1][^s2]

## When to use it

Draw a landscape when the question is how the whole ecosystem fits together: mapping dependencies before planning an implementation, or giving stakeholders one shared reference picture.[^s1] C4 suggests the same view for anyone who owns a portfolio of systems rather than a single one.[^s5] It is the wrong tool for integration mechanics or step-by-step behaviour; those belong in Level 2 to Level 4 diagrams, data flow diagrams and integration tables.[^s3][^s4]

## Connections

System landscapes are one of the diagram types in `kt:salesforce-diagrams`, its Level 1 view, and the gallery that hosts them is shared with `kt:reference-architectures`.[^s1][^s3] They are drawn and used by the `kt:salesforce-architect`.[^s1] A `kt:capability-maps` view frames what the business needs to do; a landscape, as a map of the systems within a chosen scope, frames the systems in play.[^s5] The integration points on a landscape are where `kt:integration-patterns` are chosen, and each one is specified in detail in an `kt:interface-specification-document`.[^s4] The Salesforce section groups single-org architecture examples with the landscapes, linking it to `kt:org-strategy`.[^s1] Together with data flow diagrams and integration tables, it forms the project documentation that a `kt:solution-design-document` draws on.[^s4]

## Sources
[^s1]: Salesforce Architects, "System Landscape (Reference Diagrams)". https://architect.salesforce.com/docs/architect/reference-diagrams/guide/section-system-landscape (accessed 2026-11-22)
[^s2]: Salesforce Architects, "Agentforce System Landscape (Reference Diagrams)". https://architect.salesforce.com/docs/architect/reference-diagrams/guide/einstein-system-landscape (accessed 2026-11-22)
[^s3]: Salesforce Architects, "Salesforce Diagrams: Documentation & Implementation". https://architect.salesforce.com/diagrams/framework/docs-implementation (accessed 2026-11-22)
[^s4]: Trailhead, "Project Documentation for Salesforce B2C Commerce Technical Architects: Document the Architectural Landscape". https://trailhead.salesforce.com/content/learn/modules/b2c-project-docs-for-technical-architects/b2c-doc-architectural-landscape (accessed 2026-11-22)
[^s5]: C4 model, "System landscape diagram". https://c4model.com/diagrams/system-landscape (accessed 2026-11-22)
