---
id: kt:solution-design-document
type: Concept
title: Solution Design Document
aliases: [solution design doc, SDD, technical design specification, TSD, technical specification, software design description]
domain: architecture-practice
summary: >-
  The versioned, signed-off project document in which an architect records how a Salesforce solution will meet its
  requirements: in-scope systems and diagrams, data flows and systems of record, integrations, customizations, design
  options and risks. Delivery teams build from it and support teams use it to understand the implementation.
release: "Winter '27"
status: concept
broader: [kt:solution-design-tradeoffs]
related: [kt:requirements-gathering, kt:fit-gap-analysis, kt:architecture-decision-records, kt:non-functional-requirements, kt:user-acceptance-testing, kt:b2c-solution-architect-certification]
relations:
  - {predicate: usedBy, object: kt:salesforce-architect}
  - {predicate: hasPart, object: kt:salesforce-diagrams}
  - {predicate: dependsOn, object: kt:requirements-gathering}
sources:
  - id: s1
    title: "Document Requirements and Build the Storefront"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/cc-project-mgmt/cc-document-and-build
    type: official-learning
    accessed: 2026-11-18
  - id: s2
    title: "Document the Architectural Landscape (Project Documentation for Salesforce B2C Commerce Technical Architects)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/b2c-project-docs-for-technical-architects/b2c-doc-architectural-landscape
    type: official-learning
    accessed: 2026-11-18
  - id: s3
    title: "Review Solution Design for Architects (Cert Prep: B2B Solution Architect: Delivery and Design)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/b2b-solution-architect-cert-delivery-and-design/review-design
    type: official-learning
    accessed: 2026-11-18
  - id: s4
    title: "IEEE 1016-2009: Standard for Information Technology—Systems Design—Software Design Descriptions"
    publisher: IEEE (via ANSI Webstore)
    url: https://webstore.ansi.org/Standards/IEEE/IEEE10162009
    type: standards-body
    accessed: 2026-11-18
created: 2026-11-18
---

# Solution Design Document

A solution design document (SDD) is the project document in which the architect writes down how a Salesforce solution will deliver its agreed requirements. Salesforce's own delivery guidance pairs two specifications. The functional design specification answers what the system does, from the user's point of view. The technical design specification answers how it does it, with enough technical precision for developers to build from.[^s1] In everyday Salesforce consulting, "solution design document" usually means that technical half, sometimes with the functional design folded in. The term is generic, not a Salesforce product. The wider software-engineering equivalent is the software design description defined by IEEE 1016, which treats the document as a representation of a design used to communicate design information to its stakeholders.[^s4]

## What goes in it

Trailhead's B2C Commerce material for technical architects shows what a Salesforce design document typically records once discovery has turned business requirements into technical capabilities.[^s2]

- **Architecture diagram:** the systems in scope, how they interact, and which system is the system of record for each data type.[^s2]
- **Data flow diagram:** how data moves between applications, how often, and through which transfer points.[^s2]
- **Import/export and job plan:** each scheduled job's source, target, frequency, full or delta type, and dependencies, sequenced so that replication finishes before peak traffic.[^s2]
- **Integrations:** a summary table by integration type, with a separate interface specification document per third-party provider, either linked or embedded.[^s2]
- **Customizations, growth and risks:** key custom builds, volume and performance assumptions, known gaps with their workarounds, and the design trade-offs and risks taken.[^s2]

The technical specification in the storefront guidance also covers data mapping, system integration, SEO and analytics, load testing and accessibility.[^s1] At the solution-architect level, Salesforce expects the design to set out the design options considered, the risks of each and how critical they are, and the option recommended to meet both functional and non-functional requirements.[^s3]

## Lifecycle: review, sign-off and change control

Salesforce's guidance places the specifications in the requirements phase, before any build. The project has to pass a specification review milestone, and any issues the reviewers raise must be resolved before moving on.[^s1] Before build starts, the documents get a date and version stamp, and the customer signs off on them. Under iterative delivery, sign-off is iterative as well.[^s1] Once the design document is shared, the architect is expected to lead stakeholders to final acceptance and resolve any concerns they raise.[^s3]

After sign-off, the technical specification becomes the main build reference for developers. Support teams later use it to understand what was built.[^s1] Changes go through change control. A scope gap analysis compares the statement of work and high-level design with what has changed since, and each gap becomes a change order and a project-plan update. Version stamping keeps everyone working from the official baseline.[^s1]

## Gotchas

- Write the design for the people who will read it. One architecture diagram can't answer every question, so split detail across the diagrams, tables and interface specifications.[^s2]
- Keep manual steps visible. The B2C guidance allows manual processes, such as image approval, to be left off the data flow diagram, so the document needs to record them somewhere else.[^s2]
- An unversioned document can't settle scope disputes. Freeze and version each release of the specification, and route every later change through a change order.[^s1]

## Connections

The SDD depends on `kt:requirements-gathering` and on the outcome of `kt:fit-gap-analysis`. Delivery guidance compares the design back to the statement of work and high-level design to find scope gaps, and only requirements that deviate from the standard reference application need functional specification.[^s1] It is where the results of `kt:solution-design-tradeoffs` are written up: options, risks and the recommendation.[^s3] Its diagrams follow the notation of `kt:salesforce-diagrams`, from system landscapes to data flows.[^s2] `kt:architecture-decision-records` complement it by keeping the reasoning behind individual decisions, and `kt:non-functional-requirements` are one of the two requirement sets the recommended design must satisfy.[^s3] It is **used by** the `kt:salesforce-architect` role, and Salesforce's B2C Commerce technical-architect training covers this documentation in detail, which makes it useful background for `kt:b2c-solution-architect-certification` candidates.[^s2] The signed-off specification is also the baseline that `kt:user-acceptance-testing` validates the build against.[^s1]

## Sources
[^s1]: Salesforce Trailhead, "Document Requirements and Build the Storefront". https://trailhead.salesforce.com/content/learn/modules/cc-project-mgmt/cc-document-and-build (accessed 2026-11-18)
[^s2]: Salesforce Trailhead, "Document the Architectural Landscape", Project Documentation for Salesforce B2C Commerce Technical Architects. https://trailhead.salesforce.com/content/learn/modules/b2c-project-docs-for-technical-architects/b2c-doc-architectural-landscape (accessed 2026-11-18)
[^s3]: Salesforce Trailhead, "Review Solution Design for Architects", Cert Prep: B2B Solution Architect: Delivery and Design. https://trailhead.salesforce.com/content/learn/modules/b2b-solution-architect-cert-delivery-and-design/review-design (accessed 2026-11-18)
[^s4]: IEEE, "IEEE 1016-2009: Standard for Information Technology—Systems Design—Software Design Descriptions", ANSI Webstore listing. https://webstore.ansi.org/Standards/IEEE/IEEE10162009 (accessed 2026-11-18)
