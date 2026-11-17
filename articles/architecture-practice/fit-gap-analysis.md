---
id: kt:fit-gap-analysis
type: Concept
title: Fit-Gap Analysis
aliases: [fit gap analysis, gap-fit analysis, fit/gap analysis, fit-to-standard analysis, requirements gap analysis]
domain: architecture-practice
summary: >-
  A design-phase technique that compares each requirement against what the standard platform (or a chosen
  reference application) already delivers, classifies it as a fit, a configuration, a customization or something
  else, and sizes and prioritizes the gaps so the team builds only what the standard product cannot do.
release: "Winter '27"
status: concept
broader: [kt:solution-design-tradeoffs]
related: [kt:requirements-gathering, kt:build-vs-buy-decisions, kt:capability-maps, kt:salesforce-industries, kt:user-acceptance-testing, kt:commerce-cloud]
relations:
  - {predicate: usedBy, object: kt:salesforce-architect}
  - {predicate: usedBy, object: kt:business-analyst}
  - {predicate: dependsOn, object: kt:user-stories}
  - {predicate: mitigates, object: kt:technical-debt-in-salesforce}
sources:
  - id: s1
    title: "Learn About the Functional Consulting Workflow"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/cc-functional-consulting/cc-functional-consulting-workflow
    type: official-learning
    accessed: 2026-11-17
  - id: s2
    title: "Documenting B2C Commerce Technical Requirements"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/b2c-project-docs-for-technical-architects/b2c-technical-project-docs
    type: official-learning
    accessed: 2026-11-17
  - id: s3
    title: "Comparing Business Requirements and Storefront Design"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/b2c-solution-functional-launch-readiness/b2c-review-business-requirements
    type: official-learning
    accessed: 2026-11-17
  - id: s4
    title: "Map Salesforce Capabilities to Business Needs (Salesforce Industry Blueprints: Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/ko/content/learn/modules/salesforce-industry-blueprints-quick-look/map-salesforce-capabilities-to-business-needs
    type: official-learning
    accessed: 2026-11-17
  - id: s5
    title: "Complete fit-gap analysis"
    publisher: Microsoft Learn
    url: https://learn.microsoft.com/en-us/training/modules/functional-consultant-skills/5-complete-fit-gap-analysis
    type: partner
    accessed: 2026-11-17
  - id: s6
    title: "Optimize your implementation with a fit-to-standard and fit-gap analysis"
    publisher: Microsoft Learn (Dynamics 365 Implementation Guide)
    url: https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/process-focused-solution-fit-to-standard-fit-gap-analysis
    type: partner
    accessed: 2026-11-17
created: 2026-11-17
---

# Fit-Gap Analysis

Fit-gap analysis is the step in solution design where each known requirement is held up against what the platform already does, so the team can see which needs are met out of the box and which require configuration, custom development or another answer.[^s5] On Salesforce projects it sits between discovery and build: Trailhead's functional consulting workflow places a gap analysis in the design phase, alongside the functional specification and data model, so that missing pieces and customization needs surface early.[^s1] The technique is not unique to Salesforce; enterprise application vendors teach the same method, which makes it a shared vocabulary for architects, business analysts and implementation partners.[^s5][^s6]

## How it works

The analyst first makes sure each requirement or user story is fully understood, then breaks down the proposed solution and records a judgment for every item.[^s5] A common worksheet carries four columns:

- **Category** — how far the requirement is from standard behaviour, for example *fit*, *configured*, *custom* or *other*; teams may choose their own labels.[^s5]
- **Level of effort** — a consistent sizing scale such as low/medium/high, 1–10, T-shirt sizes or planning-poker cards.[^s5]
- **Priority** — usually set by the business, though the architect may raise foundational items so the architecture is built first.[^s5]
- **Implementation notes** — a short statement of the intended approach and assumptions, deliberately not a detailed design.[^s5]

The output is a sized, prioritized list showing what can be used as-is, what must be configured and what must be built, which then drives estimates, release planning and the architecture.[^s5] Good results depend on knowing the standard product well; otherwise a requirement that already fits gets rebuilt as a custom feature.[^s5]

## Fit-to-standard first

Some methodologies split the work in two. A *fit-to-standard* pass runs workshops that walk business processes against the product's standard processes, with the motto of adopting wherever possible and adapting only where justified. The *fit-gap* pass follows and decides how to close what remains.[^s6] Options for a gap include extending the platform, buying a partner product, combining standard, custom and partner pieces, or changing the business process itself.[^s6] Each customization is weighed for build and maintenance cost, impact on usability and performance, and the risk that a later release delivers the same capability natively.[^s6]

On Salesforce, the earliest version of this conversation often happens at the capability level. Industry blueprints give a product-agnostic view of the business capabilities common to most customers in a sector, helping stakeholders agree which capabilities matter and which platform capabilities they need before requirements are detailed.[^s4]

## Salesforce practice

In B2C Commerce implementations the functional specification explicitly contains a gap analysis against the chosen reference application, and the functional requirements record standard functionality versus customizations.[^s2] Trailhead's consulting guidance warns that being able to customize something technically is not a reason to do it; customizations should be judged against the platform and its constraints.[^s1]

The same lens returns at launch readiness. Before go-live the build is compared with the functional specification, and any unplanned difference becomes a gap to identify, document and plan.[^s3] Each gap receives an impact and priority score that decides whether it blocks launch: a cosmetic difference may ship, while a missing payment method stops it.[^s3]

## Gotchas

- Treat the worksheet as a means, not the deliverable; the value lies in the decisions it produces, so tool choice matters little.[^s5]
- Forcing users into processes designed for other software, or customizing low-value gaps, erodes usability and can cut teams off from vendor documentation and support.[^s6]
- Re-check the gap list each release cycle, because a native feature may make a planned customization redundant.[^s6]

## Connections

Fit-gap analysis is one of the core **solution design trade-off** activities (`kt:solution-design-tradeoffs`) and takes its input from `kt:requirements-gathering`, scoring individual `kt:user-stories`.[^s5] When a gap is confirmed, the resolution choice is a `kt:build-vs-buy-decisions` question, and capability-level gaps are often first spotted on `kt:capability-maps` or on industry blueprints, which frame sector capabilities much as `kt:salesforce-industries` products are packaged by sector.[^s4][^s6] Preferring fits over customizations **mitigates** `kt:technical-debt-in-salesforce`.[^s6] It is used mainly by the `kt:salesforce-architect` and `kt:business-analyst`, and in `kt:commerce-cloud` projects it reappears in launch-readiness reviews that feed `kt:user-acceptance-testing`.[^s2][^s3]

## Sources

[^s1]: Trailhead, "Learn About the Functional Consulting Workflow". https://trailhead.salesforce.com/content/learn/modules/cc-functional-consulting/cc-functional-consulting-workflow (accessed 2026-11-17)
[^s2]: Trailhead, "Documenting B2C Commerce Technical Requirements". https://trailhead.salesforce.com/content/learn/modules/b2c-project-docs-for-technical-architects/b2c-technical-project-docs (accessed 2026-11-17)
[^s3]: Trailhead, "Comparing Business Requirements and Storefront Design". https://trailhead.salesforce.com/content/learn/modules/b2c-solution-functional-launch-readiness/b2c-review-business-requirements (accessed 2026-11-17)
[^s4]: Trailhead, "Map Salesforce Capabilities to Business Needs", Salesforce Industry Blueprints: Quick Look. https://trailhead.salesforce.com/ko/content/learn/modules/salesforce-industry-blueprints-quick-look/map-salesforce-capabilities-to-business-needs (accessed 2026-11-17)
[^s5]: Microsoft Learn, "Complete fit-gap analysis". https://learn.microsoft.com/en-us/training/modules/functional-consultant-skills/5-complete-fit-gap-analysis (accessed 2026-11-17)
[^s6]: Microsoft Learn, "Optimize your implementation with a fit-to-standard and fit-gap analysis". https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/process-focused-solution-fit-to-standard-fit-gap-analysis (accessed 2026-11-17)
