---
id: kt:agentforce
type: Product
title: Agentforce
aliases: [Agentforce 360 Platform, Salesforce Agentforce, Agentforce AI agents, Einstein Copilot]
domain: data-cloud-and-ai
summary: >-
  Salesforce's platform for building, grounding and running autonomous AI agents that use large language models,
  trusted CRM and Data 360 data, and actions built from Flows, Apex, prompt templates and APIs to do work for
  employees and customers.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:agent-development-lifecycle, kt:service-cloud, kt:flow-builder]
relations:
  - {predicate: hasPart, object: kt:atlas-reasoning-engine}
  - {predicate: hasPart, object: kt:agent-script}
  - {predicate: dependsOn, object: kt:data-cloud}
  - {predicate: dependsOn, object: kt:einstein-trust-layer}
sources:
  - id: s1
    title: "Discover Agentforce Agents (Agentforce Agents: Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agentforce-agents-quick-look/discover-agentforce-agents
    type: official-learning
    accessed: 2026-10-31
  - id: s2
    title: "Legacy Guide: Agentforce Reasoning, Subagents, Instructions, and Actions"
    publisher: Salesforce
    url: https://www.salesforce.com/agentforce/legacy-guide/
    type: official-blog
    accessed: 2026-10-31
  - id: s3
    title: "Agent Script Flow of Control"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/ascript-flow.html
    type: official-docs
    accessed: 2026-10-31
  - id: s4
    title: "Introducing Hybrid Reasoning with Agent Script"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2025/10/introducing-hybrid-reasoning-with-agent-script
    type: official-blog
    accessed: 2026-10-31
  - id: s5
    title: "Build With Confidence: Inside the New Agentforce Builder"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2026/build-with-confidence-inside-the-new-agentforce-builder
    type: official-blog
    accessed: 2026-10-31
  - id: s6
    title: "Copilot is now Agentforce"
    publisher: Salesforce
    url: https://salesforce.com/artificial-intelligence/einstein-ai-assistant
    type: official-blog
    accessed: 2026-10-31
created: 2026-10-31
---

# Agentforce

Agentforce is Salesforce's platform for autonomous AI agents. An agent is an application that uses a large language model to interpret a conversation or an automated trigger, decides what to do next, and then acts on trusted business data such as CRM records, knowledge articles and external data.[^s1] Agents can work around the clock in websites, self-service portals, messaging apps, mobile apps, the CRM itself and Slack, and they hand off to a human when a request falls outside their scope.[^s1] The employee-facing agent that helps users find data and carry out tasks in their workflow is the product formerly known as Einstein Copilot.[^s6]

## Building blocks

Trailhead describes an agent as a combination of a role (the job it does), knowledge (the data it may use), actions (the tasks it can perform), guardrails (what it must not do and when to escalate), channels, and a reasoning engine.[^s1] Salesforce ships prebuilt agent types such as Service Agent, Sales Development Representative, Sales Coach, Merchandiser, Buyer Agent, Personal Shopper and Campaign Optimizer, and teams can also build their own.[^s1]

- **Subagents (formerly topics).** Each subagent is a job the agent can handle, with a name, a classification description and a scope that says what it can and cannot do.[^s2]
- **Instructions.** Natural-language guidance that shapes action choice, conversation flow and formatting. The model interprets them, so they are not deterministic and cannot enforce hard business rules.[^s2]
- **Actions.** The tools an agent calls: Flows, Apex, prompt templates, MuleSoft APIs and external services. Each has a name, a description and input instructions that the model reads when choosing.[^s2][^s1]
- **Variables and filters.** Context variables come from the session and are read-only; custom variables hold action outputs and state. Filters use them to hide subagents or actions before the model sees them, for example until a user is authenticated.[^s2]

## How reasoning works

In the classic builder, the reasoning engine (Atlas) first classifies a request into a subagent using only names and classification descriptions. It then loads that subagent's scope, instructions and actions plus roughly the last six conversation turns, and asks the model whether to run an action or reply. Action results loop back in until a response is ready. A final grounding check tests the reply for source support, instruction adherence, hallucination and prompt injection, and the agent retries or falls back to a "can't help" message if it fails.[^s2]

Pure LLM reasoning proved brittle for processes that must follow strict, ordered steps, such as refunds or loan applications.[^s4] Salesforce therefore made Atlas configurable for **hybrid reasoning**. Agents are written in **Agent Script**, a readable declarative language that is compiled into an Agent Graph the engine follows.[^s4] Script blocks run deterministically, setting variables, calling actions, evaluating if/else conditions and handling transitions. Only after they resolve does the model receive a single assembled prompt and start reasoning.[^s3] Every request enters at the `start_agent` block, the agent router, which picks a subagent. Transitions are one-way and discard the prompt built so far.[^s3]

The new Agentforce Builder exposes Agent Script through a canvas view and a script view that stay in sync, an AI assistant that drafts topics and actions, and previews that run against mock data.[^s5] It lives in the Agentforce Studio app. The classic builder in Setup remains available with no announced sunset date, and classic and new agents can coexist.[^s5][^s2] With the change, Salesforce renamed topics to subagents, Topic Selector to Agent Router, and Connected Agent to Connected Subagent.[^s2]

## Limits and gotchas

- Salesforce's guidance is to keep an agent to about 10–15 subagents and no more than 15 actions per subagent, because overlap and clutter reduce classification consistency.[^s2]
- Put rules that must always hold, such as refund eligibility, inside action code, filters or Agent Script, not in instructions.[^s2][^s4]
- Make subagent names short, verb-led and non-overlapping; the router sees only names and descriptions when it classifies.[^s2]
- Agent Script was announced as a pilot in October 2025 with a public beta planned for the following month, so check the current release notes before relying on specific script features.[^s4]

## When to use it (and when not)

Use Agentforce when a task needs natural-language understanding or judgement across varied requests, such as answering service questions or guiding a buyer. For deterministic automation with no language understanding, a record-triggered flow or Apex is cheaper, more predictable and easier to test. Even inside an agent, Salesforce recommends pushing fixed logic into actions or script.[^s2][^s4]

## Connections

Agentforce sits **under** `kt:salesforce-platform`, of which Salesforce describes it as a part.[^s2] It **has parts** `kt:atlas-reasoning-engine` and `kt:agent-script`.[^s2][^s4] It **depends on** `kt:data-cloud` (Data 360), which Salesforce calls integral to Agentforce, and on `kt:einstein-trust-layer`, which supplies built-in protections.[^s2][^s1] Its actions call `kt:flow-builder` flows, Apex and prompt templates.[^s2] It is **related** to `kt:agent-development-lifecycle`, the method for building, testing and running agents, and to `kt:service-cloud`, where service agents work next to human reps.[^s1]

## Sources

[^s1]: Trailhead, "Discover Agentforce Agents". https://trailhead.salesforce.com/content/learn/modules/agentforce-agents-quick-look/discover-agentforce-agents (accessed 2026-10-31)
[^s2]: Salesforce, "Legacy Guide: Agentforce Reasoning, Subagents, Instructions, and Actions". https://www.salesforce.com/agentforce/legacy-guide/ (accessed 2026-10-31)
[^s3]: Salesforce Developers, "Agent Script Flow of Control". https://developer.salesforce.com/docs/ai/agentforce/guide/ascript-flow.html (accessed 2026-10-31)
[^s4]: Salesforce Developers Blog, "Introducing Hybrid Reasoning with Agent Script". https://developer.salesforce.com/blogs/2025/10/introducing-hybrid-reasoning-with-agent-script (accessed 2026-10-31)
[^s5]: Salesforce Admins Blog, "Build With Confidence: Inside the New Agentforce Builder". https://admin.salesforce.com/blog/2026/build-with-confidence-inside-the-new-agentforce-builder (accessed 2026-10-31)
[^s6]: Salesforce, "Copilot is now Agentforce". https://salesforce.com/artificial-intelligence/einstein-ai-assistant (accessed 2026-10-31)
