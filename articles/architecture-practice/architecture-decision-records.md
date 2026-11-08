---
id: kt:architecture-decision-records
type: ExternalConcept
title: Architecture Decision Records
aliases: [ADR, ADRs, architectural decision record, architecture decision log]
domain: architecture-practice
summary: >-
  Short, numbered, append-only documents that each capture one architecturally significant decision, its context,
  the options weighed and its consequences; a general software-architecture practice that Salesforce architects use
  to record choices such as org strategy or Flow vs. Apex.
release: "Winter '27"
status: concept
broader: [kt:solution-design-tradeoffs]
related: [kt:salesforce-diagrams, kt:well-architected-framework, kt:architect-decision-guides, kt:org-strategy, kt:salesforce-dx]
relations:
  - {predicate: usedBy, object: kt:salesforce-architect}
  - {predicate: mitigates, object: kt:technical-debt-in-salesforce}
sources:
  - id: s1
    title: "Documenting Architecture Decisions"
    publisher: Cognitect (Michael Nygard)
    url: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
    type: community
    accessed: 2026-11-08
  - id: s2
    title: "Architecture Decision Record"
    publisher: martinfowler.com (Martin Fowler)
    url: https://www.martinfowler.com/bliki/ArchitectureDecisionRecord.html
    type: community
    accessed: 2026-11-08
  - id: s3
    title: "Architectural Decision Records (CSSE6400 Software Architecture lecture notes)"
    publisher: The University of Queensland (Richard Thomas)
    url: https://csse6400.uqcloud.net/handouts/adr.pdf
    type: academic
    accessed: 2026-11-08
  - id: s4
    title: "Architectural Decisions: A Human-Led, AI-Powered Approach"
    publisher: Salesforce Architects (Dave Norris)
    url: https://www.salesforce.com/blog/architectural-decisions-human-led-ai-powered-approach/
    type: official-blog
    accessed: 2026-11-08
  - id: s5
    title: "Architecture decision record"
    publisher: Microsoft Learn (Azure Well-Architected Framework)
    url: https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record
    type: partner
    accessed: 2026-11-08
created: 2026-11-08
---

# Architecture Decision Records

An architecture decision record (ADR) is a short document that captures a single architecturally significant decision: the forces that shaped it, what was decided, and what follows from it.[^s1][^s2] The format is not Salesforce-specific, but Salesforce's own architects recommend it as a practical template for explaining the reasoning behind technical choices to future team members and for building stakeholder alignment during a project.[^s4]

## Origin and purpose

Michael Nygard proposed the lightweight ADR format in a 2011 Cognitect post. His motivation was that teams lose track of why earlier decisions were made, so newcomers either follow them blindly or reverse them without knowing what they protected.[^s1] Martin Fowler notes that Nygard did not invent the idea of a decision log; he drew on Philippe Kruchten's decision registers and on the style of software pattern writing.[^s2] University teaching material makes the same point and adds that ADRs also remind the original authors of their own reasoning months later.[^s3]

## Structure

Nygard's template has five parts: a short noun-phrase title, a neutral description of the context, the decision written as active "We will…" sentences, a status, and the consequences, whether positive, negative or neutral.[^s1] Later guidance adds the serious alternatives with their pros and cons, a confidence level, and the product changes that should trigger a re-evaluation.[^s2][^s5] The University of Queensland notes add a date and a one-line summary, often written as a Y-statement.[^s3] The Salesforce Architects template uses four core sections (context, considered options, decision, consequences) plus metadata such as decision-makers, people consulted and informed, and an AI-usage disclosure.[^s4]

## Lifecycle rules

ADRs are numbered sequentially and the numbers are never reused.[^s1] Typical statuses are proposed, accepted and superseded; once accepted, a record is not edited. A changed decision gets a new ADR that supersedes and links to the old one, so the log shows how long each decision governed the work.[^s2][^s5] Microsoft's Well-Architected guidance recommends starting the log at the beginning of a workload, back-filling known decisions on brownfield systems, and recording only choices that affect structure or key quality attributes or are hard to reverse.[^s5] Teaching notes suggest reviewing an ADR about a month after it is written, before much is built on it.[^s3]

## Where they live

The common advice is to keep ADRs as numbered Markdown files in the source repository they describe, for example under `doc/adr`, so they can be diffed and reviewed like code.[^s1][^s2][^s3] Fowler cautions that a code repository suits ecosystem-wide decisions less well and can be awkward for non-developers.[^s2] For Salesforce teams, that trade-off matters because many key decisions (org strategy, sharing model, licensing) span several projects.

## Using ADRs on Salesforce

Salesforce's architecture blog demonstrates an ADR for single-org versus multi-org strategy. It scores the options against the Well-Architected pillars (Trusted, Easy, Adaptable) rather than generic pros and cons, and weighs factors such as sharing and security, governor limits, license cost, deployment pipelines, reporting, and the later cost of splitting or merging orgs.[^s4] The same article shows AI drafting an ADR through chained prompts, with the architect reviewing each step. It stresses that a human stays accountable and that inputs should not be shared with public models that train on them.[^s4]

## Gotchas

- An ADR without context and rationale is of little use, because readers cannot tell whether it still applies when circumstances change.[^s5]
- Do not hide negative consequences, and split a decision into separate records when it spans short-, mid- and long-term phases.[^s5]
- Keep each record to one or two pages and link to supporting material rather than embedding it.[^s1][^s2]

## Connections

ADRs sit under `kt:solution-design-tradeoffs`: trade-off analysis produces a decision, and the ADR preserves it together with its accepted risks.[^s2][^s4] `kt:architect-decision-guides` help an architect *make* a platform choice, while an ADR *records* the choice made for a specific org.[^s4] `kt:salesforce-diagrams` show what was built, and ADRs explain why.[^s2] The Salesforce example grounds its criteria in the `kt:well-architected-framework` and applies them to `kt:org-strategy`.[^s4] Keeping ADRs in version control alongside `kt:salesforce-dx` source follows the repository-storage advice.[^s3] The practice is **used by** the `kt:salesforce-architect` and **mitigates** `kt:technical-debt-in-salesforce`, because recorded rationale stops later changes from unknowingly undoing earlier intent.[^s1][^s5]

## Sources

[^s1]: Michael Nygard, "Documenting Architecture Decisions", Cognitect blog, 15 Nov 2011. https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions (accessed 2026-11-08)
[^s2]: Martin Fowler, "Architecture Decision Record", martinfowler.com. https://www.martinfowler.com/bliki/ArchitectureDecisionRecord.html (accessed 2026-11-08)
[^s3]: Richard Thomas, "Architectural Decision Records", CSSE6400 Software Architecture, The University of Queensland. https://csse6400.uqcloud.net/handouts/adr.pdf (accessed 2026-11-08)
[^s4]: Dave Norris, "Architectural Decisions: A Human-Led, AI-Powered Approach", Salesforce Architects blog. https://www.salesforce.com/blog/architectural-decisions-human-led-ai-powered-approach/ (accessed 2026-11-08)
[^s5]: Microsoft Learn, "Architecture decision record", Azure Well-Architected Framework. https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record (accessed 2026-11-08)
