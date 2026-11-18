---
id: kt:design-authority
type: Concept
title: Design Authority
aliases: [Design Authority board, DA, Salesforce design authority, architecture design authority]
domain: architecture-practice
summary: >-
  The architecture-focused subgroup of a Salesforce Center of Excellence that sets architectural guidelines, reviews
  how requests will be built for cross-team impact, approves rare exceptions to standards, and records the
  decisions and trade-offs it makes so they stay visible and revisitable.
release: "Winter '27"
status: concept
broader: [kt:salesforce-center-of-excellence, kt:salesforce-governance]
related: [kt:architecture-decision-records, kt:solution-design-tradeoffs, kt:data-migration-strategy, kt:principle-of-least-privilege, kt:well-architected-framework]
relations:
  - {predicate: partOf, object: kt:salesforce-center-of-excellence}
  - {predicate: dependsOn, object: kt:salesforce-architect}
  - {predicate: mitigates, object: kt:technical-debt-in-salesforce}
sources:
  - id: s1
    title: "Implement Your Salesforce CoE's Core Capabilities (Salesforce Governance with a Center of Excellence)"
    publisher: Trailhead (Salesforce)
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-governance-with-a-center-of-excellence/implement-your-salesforce-coes-core-capabilities
    type: official-learning
    accessed: 2026-11-18
  - id: s2
    title: "Learn About Salesforce Governance and Why It Matters (Salesforce Governance with a Center of Excellence)"
    publisher: Trailhead (Salesforce)
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-governance-with-a-center-of-excellence/learn-about-salesforce-governance-and-why-it-matters
    type: official-learning
    accessed: 2026-11-18
  - id: s3
    title: "Architectural Decisions: A Human-Led, AI-Powered Approach"
    publisher: Salesforce Architects (Dave Norris)
    url: https://www.salesforce.com/blog/architectural-decisions-human-led-ai-powered-approach/
    type: official-blog
    accessed: 2026-11-18
  - id: s4
    title: "Build a Salesforce Center of Excellence That Keeps Pace with AI"
    publisher: Salesforce (Allison Park)
    url: https://www.salesforce.com/blog/center-of-excellence-ai-governance/?bc=OTH
    type: official-blog
    accessed: 2026-11-18
  - id: s5
    title: "Why Design Authority Is Crucial in Salesforce Architecture"
    publisher: Salesforce Ben (Senthil Jayachandran)
    url: https://www.salesforceben.com/why-design-authority-is-crucial-in-salesforce-architecture/
    type: community
    accessed: 2026-11-18
created: 2026-11-18
---

# Design Authority

A **Design Authority (DA)** is the body inside a Salesforce governance model that owns architectural direction. Trailhead describes it as a subgroup of the Center of Excellence (CoE) that sets architectural guidelines and handles exceptions to them.[^s1] Practitioners frame it as a shared forum for architectural stewardship, where decisions with long-term impact are discussed and aligned before they harden into constraints.[^s5] It is not a Salesforce feature or setting; it is an operating practice, which is why it sits in the architecture-practice domain.

## Why it exists

Salesforce governance is a framework of people, processes and tools that answers questions such as who decides what gets built, which standards admins, developers and architects follow, and how changes are designed and deployed.[^s2] Trailhead argues that clear architectural standards plus a consistent build, test and release process let teams extend an org with confidence.[^s2] The DA is the part of that framework that holds the standards. Without it, sensible short-term choices pile up and are never revisited, a slow architectural drift that ends in accidental technical debt.[^s5]

## What it does

Trailhead's CoE module gives the DA several concrete responsibilities:[^s1]

- **Set guidelines**: for example when to build with Flow versus Apex, and when to build custom versus buy a third-party app.[^s1]
- **Review construction**: check how each request will be built, looking for duplicate data structures and unexpected automation or integration interactions.[^s1]
- **Approve exceptions**: sign off on the rare cases where an existing guideline must be relaxed or ignored.[^s1]
- **Review migrations**: examine planned metadata for data migrations before construction starts, alongside the CoE members who own data models.[^s1]
- **Guard data access**: work with security and compliance staff on who can see what, using least privilege and laws such as GDPR and CCPA.[^s1]
- **Promote reuse**: keep a library of reusable assets and push delivery teams to use it.[^s1]

Where no CoE standard covers a situation, Trailhead suggests falling back on community-vetted best practice.[^s1]

## How it operates

Membership is not prescribed by Salesforce. In larger enterprises the forum usually brings data, integration and security perspectives together with Salesforce technical leadership, typically owned by a lead platform architect; in small teams those roles may collapse into one or two people.[^s5] Whoever sits on it, Salesforce's own architecture blog holds that the Salesforce architect stays accountable for every key architectural decision.[^s3]

Rather than meeting on a fixed calendar for everything, a practical DA scales its effort to a decision's weight: routine items can be handled asynchronously, while high-impact trade-offs get a focused session.[^s5] Its main output is a lightweight decision record stating what was decided, why that option beat the alternatives, and what it enables or constrains.[^s5] Salesforce's architecture blog recommends the Architecture Decision Record format, with context, considered options, decision and consequences, for exactly this purpose.[^s3] It is also wise to agree in advance who may authorize an emergency override and how that decision gets revisited after release.[^s5]

## Gotchas

The most common failure is turning the DA into a delivery gate or code-review bottleneck that slows every change.[^s5] It should not take design ownership away from solution architects or try to act as the whole CoE.[^s5] AI work raises the stakes: Salesforce's CoE guidance asks architects to flag risks to the data structures agents depend on before a sprint starts, and wants a named approver and formal sign-off for schema changes.[^s4] A DA that reviews only at the end of a build misses that window.

## Connections

The DA is **part of** `kt:salesforce-center-of-excellence`, and both sit **under** `kt:salesforce-governance`, the broader framework of people, process and tools.[^s1][^s2] It **depends on** `kt:salesforce-architect`, the role accountable for architectural decisions and usually the DA's owner.[^s3][^s5] Its decisions are captured as `kt:architecture-decision-records` and argued with the vocabulary of `kt:solution-design-tradeoffs` and the `kt:well-architected-framework`.[^s3] By making trade-offs explicit, it **mitigates** `kt:technical-debt-in-salesforce`.[^s5] Its review of migration metadata ties it to `kt:data-migration-strategy`, and its data-access guidance applies the `kt:principle-of-least-privilege`.[^s1]

## Sources

[^s1]: Trailhead, "Implement Your Salesforce CoE's Core Capabilities", Salesforce Governance with a Center of Excellence. https://trailhead.salesforce.com/content/learn/modules/salesforce-governance-with-a-center-of-excellence/implement-your-salesforce-coes-core-capabilities (accessed 2026-11-18)
[^s2]: Trailhead, "Learn About Salesforce Governance and Why It Matters", Salesforce Governance with a Center of Excellence. https://trailhead.salesforce.com/content/learn/modules/salesforce-governance-with-a-center-of-excellence/learn-about-salesforce-governance-and-why-it-matters (accessed 2026-11-18)
[^s3]: Dave Norris, "Architectural Decisions: A Human-Led, AI-Powered Approach", Salesforce Architecture Blog. https://www.salesforce.com/blog/architectural-decisions-human-led-ai-powered-approach/ (accessed 2026-11-18)
[^s4]: Allison Park, "Build a Salesforce Center of Excellence That Keeps Pace with AI", Salesforce blog. https://www.salesforce.com/blog/center-of-excellence-ai-governance/?bc=OTH (accessed 2026-11-18)
[^s5]: Senthil Jayachandran, "Why Design Authority Is Crucial in Salesforce Architecture", Salesforce Ben. https://www.salesforceben.com/why-design-authority-is-crucial-in-salesforce-architecture/ (accessed 2026-11-18)
