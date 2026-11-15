---
id: kt:total-cost-of-ownership
type: Concept
title: Total Cost of Ownership
aliases: [TCO, total cost of ownership (TCO), lifetime cost of a Salesforce solution]
domain: architecture-practice
summary: >-
  The full direct and indirect cost of acquiring, implementing, running and changing a Salesforce solution over its
  life — licenses and add-ons, third-party apps, implementation, staff, training and the maintenance burden of
  customization — used by architects to compare options rather than looking only at purchase price.
release: "Winter '27"
status: concept
broader: [kt:solution-design-tradeoffs]
related: [kt:build-vs-buy-decisions, kt:technical-debt-in-salesforce, kt:user-licenses, kt:permission-set-licenses, kt:agentexchange, kt:proof-of-concept]
relations:
  - {predicate: usedBy, object: kt:salesforce-architect}
  - {predicate: dependsOn, object: kt:well-architected-framework}
sources:
  - id: s1
    title: "Understand Total Cost of Ownership (Nonprofit Cloud Readiness)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/nonprofit-cloud-readiness/understand-total-cost-of-ownership
    type: official-learning
    accessed: 2026-11-15
  - id: s2
    title: "Understand How Licenses Work (Salesforce Licensing)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-licensing/understand-how-licenses-work
    type: official-learning
    accessed: 2026-11-15
  - id: s3
    title: "Simple (Well-Architected: Easy)"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/well-architected/easy/simple
    type: official-docs
    accessed: 2026-11-15
  - id: s4
    title: "Ecommerce Total Cost of Ownership (TCO)"
    publisher: Salesforce
    url: https://www.salesforce.com/ap/commerce/ecommerce-tco-total-cost-of-ownership/
    type: official-blog
    accessed: 2026-11-15
  - id: s5
    title: "Total Cost of Ownership in the Services Sector: A Case Study"
    publisher: Journal of Supply Chain Management (Hurkens, van der Valk, Wynstra)
    url: https://repub.eur.nl/pub/57069/57069.pdf
    type: peer-reviewed
    accessed: 2026-11-15
created: 2026-11-15
---

# Total Cost of Ownership

Total cost of ownership (TCO) is the practice of counting every cost a choice brings over its life, not just its price tag. In purchasing research it is described as both a tool and a philosophy for understanding the relevant cost of buying from a supplier: it adds the costs of use across the organisation's value chain to the acquisition price, and converts qualitative factors such as quality into money so options can be compared on one basis.[^s5] Salesforce applies the same idea to adopting its platform, describing TCO as the combined direct and indirect costs of setting up and adopting a system.[^s1]

## Why TCO matters on Salesforce

Salesforce stresses that a product such as its nonprofit offering is a platform rather than a finished application: an organisation has to spend time and money defining its needs and building to them before it gets value.[^s1] A subscription price therefore understates the real investment. Salesforce's own commerce guidance makes the same point, suggesting TCO be estimated as initial costs plus ongoing costs multiplied by the timeframe, and noting that the ongoing part usually dominates.[^s4]

## Cost components

Salesforce's readiness guidance lists the hard costs to budget even when some licenses are donated:[^s1]

- **Licenses**: each user needs their own Salesforce license, and consultants or integrations may need extra ones.[^s1]
- **Third-party apps**: AgentExchange products often carry their own license fees on top of Salesforce's.[^s1]
- **Staff**: salaries for dedicated roles such as an admin, plus training to upskill or reskill existing staff.[^s1]
- **Implementation partner fees**, when a consulting partner does the build.[^s1]

Licensing itself is layered, which is why it is easy to under-count. Each org has one edition that bundles platform and user licenses, and can add any number of add-ons, which may include permission set, platform or user licenses; every user holds exactly one user license, while permission set licenses stack features on top of it.[^s2] A design that needs a feature only in an add-on or a permission set license changes the per-user cost of the whole solution, so license fit belongs in the estimate from the start.[^s2]

The commerce guidance adds categories that matter for customer-facing solutions: development and integrations, hosting and infrastructure that scale with traffic, maintenance and support, day-to-day operations, and compliance and security, including the cost of a breach.[^s4] It also warns of costs that appear later, such as transaction fees, add-ons and scaling charges that follow a low entry price, and paying for features nobody uses.[^s4]

## The maintenance side: customization and debt

For architects, the largest variable in TCO is usually how much the team builds. Salesforce's Well-Architected guidance recommends building on prebuilt platform services first, then AppExchange apps, then low-code customization before code, because standard features pick up platform innovation with every release while custom replicas must be maintained by the team.[^s3] It treats technical debt as a natural part of any system and asks teams to schedule its remediation, avoid shortcuts such as hard-coded values, and weigh near-term and long-term costs in build-or-buy decision records.[^s3] It also notes that an undocumented org can cost more to troubleshoot than the time the shortcut saved, and flags legacy automation such as Workflow Rules and Process Builder as an ongoing source of risk.[^s3]

## Using TCO well (and its gotchas)

- **Compare like with like**: price each option over the same horizon, including people, licenses, apps and the cost of future change.[^s4][^s5]
- **Budget for adoption, not just build**: executives, an administrator and departmental power users all need dedicated time for the system to succeed.[^s1]
- **Keep sandboxes in mind**: license changes must be mirrored into sandboxes, by refresh or the Match Production License tool, or testing diverges from production.[^s2]
- **Record the reasoning**: decisions documented with their cost rationale can be revisited when prices, requirements or the platform change.[^s3]

TCO is not a precise forecast. Salesforce's guidance is to set realistic expectations and prepare teams for surprises, and the case-study literature notes that turning qualitative factors into money involves judgement.[^s1][^s5]

## Connections

TCO is one lens **under** `kt:solution-design-tradeoffs` and is **used by** the `kt:salesforce-architect` when comparing designs.[^s3] It is the cost criterion at the heart of `kt:build-vs-buy-decisions`, where `kt:agentexchange` apps bring their own fees and custom builds add `kt:technical-debt-in-salesforce`.[^s1][^s3] License structure — `kt:user-licenses` and `kt:permission-set-licenses` — sets the per-user cost base.[^s2] It **depends on** the `kt:well-architected-framework` guidance on preferring standard features, and a `kt:proof-of-concept` is a common way to test cost assumptions before committing.[^s3]

## Sources

[^s1]: Trailhead, "Understand Total Cost of Ownership", Nonprofit Cloud Readiness module. https://trailhead.salesforce.com/content/learn/modules/nonprofit-cloud-readiness/understand-total-cost-of-ownership (accessed 2026-11-15)
[^s2]: Trailhead, "Understand How Licenses Work", Salesforce Licensing module. https://trailhead.salesforce.com/content/learn/modules/salesforce-licensing/understand-how-licenses-work (accessed 2026-11-15)
[^s3]: Salesforce Architects, "Simple", Well-Architected Framework (Easy). https://architect.salesforce.com/well-architected/easy/simple (accessed 2026-11-15)
[^s4]: Salesforce, "Ecommerce Total Cost of Ownership (TCO)". https://www.salesforce.com/ap/commerce/ecommerce-tco-total-cost-of-ownership/ (accessed 2026-11-15)
[^s5]: Hurkens, van der Valk and Wynstra, "Total Cost of Ownership in the Services Sector: A Case Study", *Journal of Supply Chain Management* (2006). https://repub.eur.nl/pub/57069/57069.pdf (accessed 2026-11-15)
