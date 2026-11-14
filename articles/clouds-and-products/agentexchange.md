---
id: kt:agentexchange
type: Product
title: AgentExchange
aliases: [AppExchange, Salesforce AppExchange, Slack Marketplace, Salesforce marketplace]
domain: clouds-and-products
summary: >-
  Salesforce's unified marketplace where partners publish, and customers discover, buy and install, apps, AI
  agents, components, integrations and consulting services for Salesforce orgs and Slack workspaces; since
  April 2026 it combines the former AppExchange, Slack Marketplace and the original Agentforce-focused AgentExchange.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:agentforce, kt:slack-platform, kt:build-vs-buy-decisions, kt:model-context-protocol-in-agentforce, kt:salesforce-pricing]
relations:
  - {predicate: hasPart, object: kt:appexchange-security-review}
  - {predicate: dependsOn, object: kt:second-generation-managed-packages}
  - {predicate: hasPart, object: kt:agentexchange-go-to-market-app}
  - {predicate: integratesWith, object: kt:slack-platform}
sources:
  - id: s1
    title: "What Is AgentExchange?"
    publisher: Salesforce Developers (AgentExchange Install Guide)
    url: https://developer.salesforce.com/docs/platform/appexchange-install-guide/guide/appexchange-install-whatis.html
    type: official-docs
    accessed: 2026-11-14
  - id: s2
    title: "Experience the New AgentExchange (AgentExchange: Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agentexchange-quick-look/experience-the-new-agentexchange
    type: official-learning
    accessed: 2026-11-14
  - id: s3
    title: "Receive Private Offers from AgentExchange Partners"
    publisher: Salesforce Developers (AgentExchange Install Guide)
    url: https://developer.salesforce.com/docs/platform/appexchange-install-guide/guide/appexchange-install-private-offers.html
    type: official-docs
    accessed: 2026-11-14
  - id: s4
    title: "Go-To-Market App: Prerequisites and Considerations"
    publisher: Salesforce Developers (ISVforce Guide)
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/partner-marketplace-considerations-prerequisites.html
    type: official-docs
    accessed: 2026-11-14
  - id: s5
    title: "Salesforce TDX 2026: only one market now as AgentExchange becomes corporate"
    publisher: diginomica
    url: https://diginomica.com/salesforce-tdx-2026-market-marketbut-actually-only-one-market-now-agentexchange-becomes-corporate
    type: news
    accessed: 2026-11-14
  - id: s6
    title: "Salesforce $50 million partner investment and agent marketplace"
    publisher: Channel Dive
    url: https://www.channeldive.com/news/salesforce-50-million-partner-investment-agent-marketplace/817587/
    type: news
    accessed: 2026-11-14
created: 2026-11-14
---

# AgentExchange

AgentExchange is Salesforce's single marketplace for third-party and Salesforce-built solutions: apps, AI agents, Bolt and Flow solutions, Lightning data, components and consulting services.[^s1] Partners build and package a solution, publish a listing (optionally with a demo or trial), and customers browse, test-drive and install it into a Salesforce org or a Slack workspace, rolling it out to everyone or to selected users.[^s1] Trailhead frames it as one marketplace of agents, apps, integrations and experts across Salesforce and Slack, with more than 12,000 apps and integrations and more than 1,000 agents and skills.[^s2]

## From AppExchange to AgentExchange

For roughly two decades the Salesforce marketplace was AppExchange. In 2025 Salesforce launched a separate AgentExchange for Agentforce agents and tools, and in April 2026, around TDX 2026, it merged AppExchange, the Slack Marketplace and that Agentforce ecosystem into one storefront under the AgentExchange name.[^s5][^s6] Salesforce paired the launch with a $50 million program of funding and technical help for partners building agents.[^s6][^s5] Many docs, URLs and permission names still carry the AppExchange wording, so "AppExchange" is best read as a former name of this node rather than a separate product.[^s1]

## How it works

- **Discovery:** semantic, intent-based search, plus recommendations inside Agentforce Builder based on the agent being built.[^s2]
- **Trust:** listings go through a security review with technical audits and vulnerability scans before publication.[^s2]
- **Install rights:** anyone can browse and test-drive; installing requires a Salesforce or Slack admin or the Download AgentExchange Packages permission.[^s1]
- **Publishing rights:** only Salesforce partners can make listings public, and publishers need the Create and Upload AgentExchange Packages permissions.[^s1]

### Private offers and billing

Some partners sell through private offers: negotiated pricing and contract terms that the customer reviews and accepts inside its own org rather than by email.[^s3] A user with the Manage Billing User permission opts in under Offers Marketplace in Setup, requests or receives an offer, and accepts it from the Partner Offers tab on the Your Account page; Salesforce then creates the order, licenses and invoice.[^s3] Salesforce acts as billing agent, so marketplace purchases land in the same account as other Salesforce purchases.[^s2][^s5]

## Limits and gotchas

The partner-side Go-To-Market App that powers private offers has tight constraints in Winter '27:[^s4]

- It serves US-based customers only, and only customers new to that partner.[^s4]
- It supports only seat-based managed packages native to the platform; layered and consumption pricing are excluded.[^s4]
- Contracts run 12 months, payment is NET30 by ACH debit in USD, invoiced one day before the start date.[^s4]
- Orders don't auto-renew, and offer cancellations and partner-initiated refunds aren't supported yet.[^s4]

Security review checks security, not fit: a reviewed listing can still clash with an org's automation or data model. The install flow supports a read-only test drive and deployment to a selected group of users, so use both before a full rollout.[^s1][^s2]

## When to use it

Check AgentExchange before building something generic such as document generation, e-signature or a prebuilt agent skill; a listed package can be cheaper than custom code once maintenance is counted. Prefer building when the need is core differentiation or when the package's data access and pricing model don't fit.[^s1][^s2]

## Connections

AgentExchange sits on top of the `kt:salesforce-platform` and is the "buy" side of `kt:build-vs-buy-decisions`.[^s1] Its trust gate is the `kt:appexchange-security-review`, and partner solutions typically ship as `kt:second-generation-managed-packages`, the only packaging that supports permission set licenses for private offers.[^s2][^s4] It lists `kt:agentforce` agents and skills, including tools reachable through `kt:model-context-protocol-in-agentforce`, and absorbed the Slack Marketplace for `kt:slack-platform` apps.[^s2][^s5] Marketplace purchases complement standard `kt:salesforce-pricing`, and partners transact them through the `kt:agentexchange-go-to-market-app`.[^s3][^s4]

## Sources

[^s1]: Salesforce Developers, "What Is AgentExchange?". https://developer.salesforce.com/docs/platform/appexchange-install-guide/guide/appexchange-install-whatis.html (accessed 2026-11-14)
[^s2]: Trailhead, "Experience the New AgentExchange". https://trailhead.salesforce.com/content/learn/modules/agentexchange-quick-look/experience-the-new-agentexchange (accessed 2026-11-14)
[^s3]: Salesforce Developers, "Receive Private Offers from AgentExchange Partners". https://developer.salesforce.com/docs/platform/appexchange-install-guide/guide/appexchange-install-private-offers.html (accessed 2026-11-14)
[^s4]: Salesforce Developers, "Go-To-Market App: Prerequisites and Considerations". https://developer.salesforce.com/docs/platform/isvforce/guide/partner-marketplace-considerations-prerequisites.html (accessed 2026-11-14)
[^s5]: diginomica, "Salesforce TDX 2026: only one market now as AgentExchange becomes corporate". https://diginomica.com/salesforce-tdx-2026-market-marketbut-actually-only-one-market-now-agentexchange-becomes-corporate (accessed 2026-11-14)
[^s6]: Channel Dive, "Salesforce $50 million partner investment and agent marketplace". https://www.channeldive.com/news/salesforce-50-million-partner-investment-agent-marketplace/817587/ (accessed 2026-11-14)
