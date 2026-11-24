---
id: kt:statement-of-work
type: Concept
title: Statement of Work
aliases: [SOW, statement of work best practices, implementation statement of work]
domain: architecture-practice
summary: >-
  The contract document in which a Salesforce consulting partner and a customer agree what an implementation will
  deliver, how and when it will be done, who is responsible for what, and what it costs. Once signed it is the scope
  baseline, and any departure from it goes through a formal change request.
release: "Winter '27"
status: concept
broader: [kt:salesforce-governance]
related: [kt:requirements-gathering, kt:solution-design-document, kt:fit-gap-analysis, kt:risk-and-assumption-logs, kt:user-acceptance-testing, kt:data-migration-strategy, kt:rough-order-of-magnitude-estimate]
relations:
  - {predicate: dependsOn, object: kt:requirements-gathering}
  - {predicate: hasPart, object: kt:change-order-process}
  - {predicate: contrastsWith, object: kt:performance-work-statement}
sources:
  - id: s1
    title: "Understand Statements of Work (Statement of Work Best Practices)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/sow-best-practices/understand-a-sow
    type: official-learning
    accessed: 2026-11-19
  - id: s2
    title: "Build a Statement of Work (Statement of Work Best Practices)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/sow-best-practices/build-a-sow
    type: official-learning
    accessed: 2026-11-19
  - id: s3
    title: "FAR 37.602 Performance work statement"
    publisher: U.S. General Services Administration (Acquisition.gov)
    url: https://www.acquisition.gov/far/37.602
    type: government
    accessed: 2026-11-19
created: 2026-11-19
---

# Statement of Work

A statement of work (SOW) is the agreement between a Salesforce consulting partner and a customer that pins down an implementation project: what work will be done, by whom, how, when, and for how much. Salesforce's partner training treats a well-built SOW as a legal agreement that sets a baseline, so that any later change to it needs a formal change request.[^s1] It is written collaboratively over several conversations during the sales cycle, not assembled from a generic internet template. Trailhead says a good SOW is not marketing material, is not vague or open to interpretation, and leaves no doubt about roles and responsibilities.[^s1] The term is generic contracting language, not a Salesforce product.

## Where it fits in the sales cycle

Trailhead describes the SOW as the last step of the implementation sales process. Discovery comes first. A rough order of magnitude follows, naming the likely services, people and a cost range. Then a proposal gives a more detailed overview and a tighter estimate.[^s1] Only in the SOW phase does the consultant commit to project-specific activities, timelines, costs and deliverables, where deliverables are the items owed to the customer under the contract.[^s1] Done well, it forces the difficult conversations before the project starts. It also builds a shared view of responsibilities and timing and shows that the partner can estimate effort per deliverable. Trailhead's worked example shows the customer redlining the draft, the scope shrinking from three initiatives to two with some work taken in-house, and the price falling to match before signature.[^s1]

## What a SOW contains

Trailhead says every SOW should cover the same ground, grouped in whatever order reads logically for the customer. It recommends seven sections.[^s2]

- **Background:** the customer's needs, business objectives and measures of success, restated because executives, signatories and delivery teams all read the document.[^s2]
- **Scope:** every feature and function to be built, plus explicit answers on training, change management, data migration, integrations, UAT and post-go-live support.[^s2]
- **Out of scope:** listing exclusions explicitly is the partner's main defence against later feature requests.[^s2]
- **Approach:** the phases, their inputs and outputs, milestones, sign-offs, project and quality management, rather than a bare label such as Agile or Waterfall.[^s2]
- **Customer responsibilities:** the customer's own deliverables, dependencies and named roles; if the customer misses them, the partner may be unable to meet its obligations.[^s2]
- **Schedule and fees:** team roles, deliverable timelines, travel expenses, a rate table by role, and the pricing model.[^s2]
- **Terms, conditions and assumptions:** change orders, termination and warranty, plus the conditions assumed true, such as email response times and on-site network access.[^s2]

Most SOWs sit under a professional services agreement (PSA), which sets the general terms of how partner and customer work together; lawyers on both sides reconcile any conflicts.[^s2]

## Pricing and gotchas

Trailhead names two pricing models. Under a fixed rate the customer pays one amount for the whole project. Under time and materials the customer pays only for hours worked. Either way, the SOW has to state what happens when scope changes.[^s2] Customers usually push for a lower price. The legitimate levers are less scope, a lower hourly rate or an explicit discount. Trailhead warns against cutting estimated hours while keeping the same scope, because the shortfall surfaces later in delivery.[^s2] Every customer-requested change should arrive as a written change order, which keeps the signed baseline meaningful.[^s2]

## Public-sector contrast

U.S. federal buyers often use a different instrument. Under FAR 37.602, agencies doing performance-based acquisition should, as far as practicable, describe work by its required results rather than how it is done or how many hours it takes. Performance is judged against measurable standards.[^s3] The agency may write a performance work statement (PWS) itself, or issue a statement of objectives that bidders turn into a PWS. That statement of objectives covers purpose, scope, period and place of performance, background, objectives and constraints, but does not itself become part of the contract.[^s3]

## Connections

The SOW **depends on** `kt:requirements-gathering`. Its scope, approach and assumptions are only as good as the discovery that came before.[^s1] Its signed scope then becomes the baseline that the `kt:solution-design-document` elaborates and that `kt:fit-gap-analysis` and later scope reviews are measured against.[^s2] The assumptions and customer dependencies it lists belong in the project's `kt:risk-and-assumption-logs`.[^s2] Data migration and user acceptance testing are two of the scope questions it must answer explicitly, linking it to `kt:data-migration-strategy` and `kt:user-acceptance-testing`.[^s2] It **has part** `kt:change-order-process`, the written-request mechanism that keeps scope changes controlled.[^s2] It **contrasts with** the outcome-based `kt:performance-work-statement` used in federal acquisition.[^s3] It falls under `kt:salesforce-governance` as the commercial control on what a project may deliver.[^s1]

## Sources
[^s1]: Salesforce Trailhead, "Understand Statements of Work", Statement of Work Best Practices. https://trailhead.salesforce.com/content/learn/modules/sow-best-practices/understand-a-sow (accessed 2026-11-19)
[^s2]: Salesforce Trailhead, "Build a Statement of Work", Statement of Work Best Practices. https://trailhead.salesforce.com/content/learn/modules/sow-best-practices/build-a-sow (accessed 2026-11-19)
[^s3]: U.S. General Services Administration, "FAR 37.602 Performance work statement", Acquisition.gov. https://www.acquisition.gov/far/37.602 (accessed 2026-11-19)
