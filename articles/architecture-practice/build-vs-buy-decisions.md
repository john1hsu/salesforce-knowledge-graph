---
id: kt:build-vs-buy-decisions
type: Concept
title: Build vs. Buy Decisions
aliases: [build versus buy, build-or-buy, make-or-buy decision, clicks vs. code vs. AppExchange]
domain: architecture-practice
summary: >-
  The architect's choice, requirement by requirement, between standard configuration, custom development and a
  third-party AppExchange (AgentExchange) product, weighed on fit, total cost, support, longevity, security and limits.
release: "Winter '27"
status: concept
broader: [kt:solution-design-tradeoffs]
related: [kt:agentexchange, kt:appexchange-security-review, kt:technical-debt-in-salesforce, kt:second-generation-managed-packages, kt:governor-limits, kt:architecture-decision-records]
relations:
  - {predicate: usedBy, object: kt:salesforce-architect}
sources:
  - id: s1
    title: "What Is a Salesforce Architect?"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/what-is-a-salesforce-architect/
    type: official-blog
    accessed: 2026-11-13
  - id: s2
    title: "Get Started with AppExchange (AppExchange Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/appexchange_basics/appexchange_basics_overview
    type: official-learning
    accessed: 2026-11-13
  - id: s3
    title: "Understand the Need for Solution Security (ISV Security Review)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/modules/isv_security_review/units/isv_security_review_intro
    type: official-learning
    accessed: 2026-11-13
  - id: s4
    title: "Execution Governors and Limits (Apex Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexref/apex_gov_limits.htm
    type: official-docs
    accessed: 2026-11-13
  - id: s5
    title: "Component attributes and their importance in decisions and component selection"
    publisher: Software Quality Journal (Springer)
    url: https://link.springer.com/article/10.1007/s11219-019-09465-2
    type: peer-reviewed
    accessed: 2026-11-13
created: 2026-11-13
---

# Build vs. Buy Decisions

A build-vs-buy decision is the recurring architectural call on whether a business requirement should be met with what the platform already provides, with something the team builds, or with a product someone else has built. Salesforce describes it as a core responsibility of its architects: each requirement is analysed to decide whether standard configuration (clicks), custom programming (code) or a third-party AppExchange tool should solve it.[^s1] Unlike a two-way make-or-buy choice, the Salesforce version therefore has three options, and many solutions end up mixing them.

## Why the question keeps coming up

Every Salesforce org is extended over time, and each extension either adds code the team must own or adds a dependency on a vendor. Salesforce frames the architect's goal as keeping the solution robust as its user base grows while minimising technical debt, and cites a typical trade-off: shipping something fast now can raise maintenance costs later.[^s1] Building is the option most exposed to that debt, because every line of Apex, Lightning component or complex flow becomes the team's to test, document and upgrade.

The broader software-engineering evidence points the same way. A 2020 survey of 157 practitioners in the *Software Quality Journal* found that about 90% considered in-house development, often alongside open-source or commercial off-the-shelf (COTS) components, and that no respondent considered COTS alone.[^s5] Cost was the most frequently chosen decision criterion (77%), followed by support of the component, predicted longevity and how well an off-the-shelf part fits the product.[^s5] Component size was rarely weighted, which the authors read as a sign that integration effort is underestimated.[^s5]

## Evaluating the "buy" option

On Salesforce, "buy" usually means a listing on the marketplace Trailhead now calls AgentExchange, which carries apps, agents, components and consulting partners.[^s2] Trailhead's own worked example has an admin weigh manual data compilation, building a solution in Salesforce, and finding an existing marketplace product, and pick the last because a tool probably already exists and time is short.[^s2] Before browsing, it recommends settling a short list of criteria:[^s2]

- **Solution type**: a packaged app or agent for quick integration, or a consultant for complex custom needs.[^s2]
- **Functionality**: which features are must-haves and which are nice-to-haves.[^s2]
- **Budget**: free versus paid, and one-time payment versus subscription.[^s2]
- **Stakeholders, testing and compatibility**: who needs what by when, where it can be tested safely, and which product, edition or feature it requires.[^s2]

Many providers offer trials, and Trailhead advises testing in a sandbox or Developer Edition org before installing anything in production.[^s2]

Security is the other filter. Marketplace solutions go through Salesforce's security review, in which the Product Security team attacks the solution using common web threats such as injection and cross-site scripting, plus Salesforce-specific checks on CRUD and field-level security enforcement, which Trailhead names as the most common reason for failing.[^s3] Passing shows the vendor met a minimum bar against common attacks; it is not a guarantee, so the buyer's own data-access and permission review still applies.[^s3]

## Limits and runtime behaviour

Bought and built code share one transaction, so governor limits are part of the decision. Code in a certified managed package gets its own per-namespace allowance for most per-transaction limits (for example its own 150 DML statements and 100 synchronous SOQL queries), separate from the org's own code.[^s4] Total heap size, maximum CPU time and maximum transaction execution time, however, are shared by everything in the transaction, and non-certified packages draw on the org's limits.[^s4] A heavy third-party package can therefore still exhaust CPU time that custom triggers on the same object depend on.

## Making and recording the call

A sound decision scores each option against the same criteria (fit, total cost over time, support and longevity, security posture, limit consumption, and the skills needed to maintain it) and records why one was chosen, so the choice can be revisited when the vendor, the requirement or the platform changes. Salesforce positions this weighing of options, rather than a fixed preference for clicks, code or packages, as what distinguishes the architect role.[^s1]

## Connections

Build vs. buy is a specific case **under** `kt:solution-design-tradeoffs`, and it is **used by** every `kt:salesforce-architect`.[^s1] The "buy" side runs through `kt:agentexchange` and is screened by the `kt:appexchange-security-review`.[^s2][^s3] Vendors usually ship as `kt:second-generation-managed-packages`, whose certified namespaces receive separate `kt:governor-limits` allowances except for heap, CPU and execution time.[^s4] The "build" side accrues `kt:technical-debt-in-salesforce`, and `kt:architecture-decision-records` are where the reasoning and revisit triggers belong.[^s1][^s5]

## Sources

[^s1]: Salesforce, "What Is a Salesforce Architect?". https://www.salesforce.com/blog/what-is-a-salesforce-architect/ (accessed 2026-11-13)
[^s2]: Trailhead, "Get Started with AppExchange", AppExchange Basics module. https://trailhead.salesforce.com/appexchange_basics/appexchange_basics_overview (accessed 2026-11-13)
[^s3]: Trailhead, "Understand the Need for Solution Security", ISV Security Review module. https://trailhead.salesforce.com/modules/isv_security_review/units/isv_security_review_intro (accessed 2026-11-13)
[^s4]: Salesforce Developers, "Execution Governors and Limits", Apex Reference Guide. https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexref/apex_gov_limits.htm (accessed 2026-11-13)
[^s5]: Chatzipetrou, Papatheocharous, Wnuk et al., "Component attributes and their importance in decisions and component selection", *Software Quality Journal* 28, 567–593 (2020). https://link.springer.com/article/10.1007/s11219-019-09465-2 (accessed 2026-11-13)
