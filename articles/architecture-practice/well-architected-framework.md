---
id: kt:well-architected-framework
type: Concept
title: Salesforce Well-Architected Framework
aliases: [Salesforce Well-Architected, Well-Architected, Trusted Easy Adaptable]
domain: architecture-practice
summary: >-
  Salesforce's official architecture guidance for designing and reviewing solutions, organized since September 2026
  into five pillars (Trust, Reliability, Operational Excellence, Resource and Cost Optimization, Fairness), each with an
  Agentic Enterprise variant; it replaced the earlier Trusted/Easy/Adaptable model.
release: "Winter '27"
status: current
broader: [kt:salesforce-architecture-center]
related: [kt:solution-design-tradeoffs, kt:governor-limits, kt:technical-debt-in-salesforce, kt:agentforce]
relations:
  - {predicate: hasPart, object: kt:agent-development-lifecycle}
  - {predicate: usedBy, object: kt:salesforce-architect}
sources:
  - id: s1
    title: "Salesforce Well-Architected Framework"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/well-architected/guide/framework.html
    type: official-docs
    accessed: 2026-10-30
  - id: s2
    title: "Well-Architected Change Log"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/well-architected/guide/change-log.html
    type: official-docs
    accessed: 2026-10-30
  - id: s3
    title: "Meet the New Well-Architected Framework"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/new-well-architected-framework/
    type: official-blog
    accessed: 2026-10-30
  - id: s4
    title: "Salesforce Architecture Center — Well-Architected overview"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/well-architected/overview
    type: official-docs
    accessed: 2026-10-30
  - id: s5
    title: "Salesforce Well-Architected: Build Well-Architected Solutions"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-well-architected/build-well-architected-solutions
    type: official-learning
    accessed: 2026-10-30
created: 2026-10-30
---

# Salesforce Well-Architected Framework

The Salesforce Well-Architected Framework is Salesforce's official body of principles and guidance for weighing trade-offs, making design decisions and building trusted solutions on the platform, now framed explicitly around the "Agentic Enterprise".[^s4] It is published on the Architecture Center and is aimed at architects, developers, administrators and technical leaders, from people new to architecture to experienced enterprise architects.[^s4]

## How it is structured

The current framework has five pillars, each describing one dimension of solution quality, setting out design principles, identifying common patterns and giving guidance for both traditional platform capabilities and agentic AI workloads.[^s1]

- **Trust** — identity and access, data governance, integration security and secure development; for agents, controlling permitted actions, auditing what agents did and securing agent-to-platform boundaries.[^s1]
- **Reliability** — governor limits, asynchronous processing, circuit breakers, capacity planning, load testing, multi-org patterns, disaster recovery and health modeling; it recommends treating 70% of a limit as an operational ceiling.[^s1]
- **Operational Excellence** — observability, DevOps, automation, incident management and continuous improvement, including a five-phase Agent Development Lifecycle for agents.[^s1]
- **Resource and Cost Optimization** — code organization, packaging, data lifecycle management, build-vs-buy analysis, license and sandbox optimization and cost governance; for agents, token usage and consumption-based costs.[^s1]
- **Fairness** — accessibility (WCAG 2.2 AA for custom components), non-discrimination, privacy architecture and AI ethics governance, with explainability, contestability and human-in-the-loop oversight for agents.[^s1]

The Agentic Enterprise material is not a sixth pillar but an overlay: every pillar has a companion agentic variant describing what changes when systems act autonomously, on the premise that agents must meet the same standards as any other enterprise solution.[^s1][^s3]

## History: from Trusted/Easy/Adaptable to five pillars

The original framework grouped guidance under three capabilities. Trusted solutions were secure, compliant and reliable; Easy solutions were intentional, automated and engaging; Adaptable solutions were resilient and composable. Each behavior had a white paper listing dimensions and considerations, with patterns (approaches that work) and anti-patterns (approaches that do not) in priority order.[^s5] Salesforce announced the evolved five-pillar framework on its architecture blog in September 2026, citing growing complexity, faster change and the need to design for probabilistic agent behavior; it was developed by the Office of the Chief Architect with input from hundreds of architects.[^s3] The change log records that fundamentals and decision guides such as Platform Sharing Architecture, Data Integration and Event-Driven Architecture were updated from the "legacy Trusted/Easy/Adaptable model" to the new taxonomy.[^s2]

## Applying it (and gotchas)

Salesforce suggests using the pillar documents as a structured checklist in design reviews, and starting new solutions with Trust and Reliability as foundations before addressing the other three pillars.[^s1] The framework names four recurring tensions — trust vs. cost, reliability vs. cost, operational excellence vs. speed, and fairness vs. agent autonomy — and stresses that there is no universal answer; the aim is to make these trade-offs deliberately rather than discover them in production.[^s1] A practical gotcha: much existing training material, including the Trailhead module, still teaches the three-capability model, so teams should map older review checklists onto the five pillars rather than mixing vocabularies.[^s5][^s2] The Architecture Center pairs the framework with decision guides, fundamentals, patterns and diagram resources, and recommends reading the framework first, then the decision guides and patterns for a given use case.[^s4]

## Connections

The framework is the central guidance on the Salesforce Architecture Center, alongside its decision guides and diagrams.[^s4] It is the vocabulary for discussing solution design trade-offs and technical debt, and its Reliability pillar is where governor limits are treated as a design constraint.[^s1] Its agentic overlay ties it to Agentforce and contains the Agent Development Lifecycle as part of Operational Excellence.[^s1][^s3] Its primary users are Salesforce architects running design reviews.[^s4]

## Sources

[^s1]: Salesforce Architects, "Salesforce Well-Architected Framework". https://architect.salesforce.com/docs/architect/well-architected/guide/framework.html (accessed 2026-10-30)
[^s2]: Salesforce Architects, "Well-Architected Change Log". https://architect.salesforce.com/docs/architect/well-architected/guide/change-log.html (accessed 2026-10-30)
[^s3]: Salesforce, "Meet the New Well-Architected Framework" (Salesforce Architecture Blog, 2026-09-14). https://www.salesforce.com/blog/new-well-architected-framework/ (accessed 2026-10-30)
[^s4]: Salesforce Architects, "Well-Architected overview". https://architect.salesforce.com/well-architected/overview (accessed 2026-10-30)
[^s5]: Trailhead, "Salesforce Well-Architected: Build Well-Architected Solutions". https://trailhead.salesforce.com/content/learn/modules/salesforce-well-architected/build-well-architected-solutions (accessed 2026-10-30)
