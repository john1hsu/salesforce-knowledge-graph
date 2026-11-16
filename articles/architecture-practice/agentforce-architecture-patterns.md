---
id: kt:agentforce-architecture-patterns
type: Pattern
title: Agentforce Architecture Patterns
aliases: [agentic patterns, enterprise agentic architecture patterns, agentic design patterns, multi-agent architecture patterns, agentic integration patterns]
domain: architecture-practice
summary: >-
  Salesforce Architects' catalog of reusable designs for Agentforce solutions: agent types (conversational,
  proactive, ambient, autonomous, collaborative), named agent roles such as Greeter, Operator, Orchestrator and
  Judge & Jury, multi-agent archetypes (SOMA, MOMA, multi-vendor A2A) and integration patterns over MCP and A2A.
release: "Winter '27"
status: concept
broader: [kt:agentforce, kt:solution-design-tradeoffs]
related: [kt:agentforce-subagents, kt:agent-script, kt:architect-decision-guides]
relations:
  - {predicate: dependsOn, object: kt:model-context-protocol-in-agentforce}
  - {predicate: dependsOn, object: kt:agent-to-agent-protocol}
  - {predicate: hasPart, object: kt:multi-agent-orchestration}
  - {predicate: usedBy, object: kt:salesforce-architect}
sources:
  - id: s1
    title: "Enterprise Agentic Architecture and Design Patterns"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/enterprise-agentic-architecture
    type: official-docs
    accessed: 2026-11-16
  - id: s2
    title: "Agentic Patterns"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/agentic-patterns
    type: official-docs
    accessed: 2026-11-16
  - id: s3
    title: "Agentic Integration Patterns"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/fundamentals/guide/agentic-integration-patterns
    type: official-docs
    accessed: 2026-11-16
  - id: s4
    title: "Determining Agentic vs. Traditional Workflow Automation (Decision Guide)"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/decision-guides/guide/determining-agentic-vs-traditional-workflow-automation
    type: official-docs
    accessed: 2026-11-16
  - id: s5
    title: "How to Set Up a Super Agent with Connected Subagents"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2026/how-to-set-up-a-super-agent-with-connected-subagents
    type: official-blog
    accessed: 2026-11-16
created: 2026-11-16
---

# Agentforce Architecture Patterns

Agentforce architecture patterns are the reusable designs that Salesforce Architects publishes for structuring AI agent solutions: which kind of agent to build, which role each agent plays, how several agents divide and coordinate work, and how agents connect to data and other systems. The guidance argues that a single monolithic agent suits common use cases, but that multi-agent designs give more scale, control and flexibility as an organization's agent estate grows, because specialised agents follow instructions more reliably, can be tested and replaced independently, and isolate faults.[^s1] The design principles it names are decomposition, decoupling, reuse, a limited scope per agent and specialisation.[^s1]

## Agent types

The Agentic Patterns guide classifies agents by how they are triggered and how much autonomy they have:[^s2]

- **Conversational**: reactive, multi-turn agents that act as the front door for questions, data lookups and simple commands.[^s2]
- **Proactive**: started by events, data changes or conditions rather than a user prompt; **ambient** agents are a background variant that cut "work about work".[^s2]
- **Autonomous**: given a high-level goal, they plan and run multi-step work with little human involvement.[^s2]
- **Collaborative**: groups of specialised agents, usually coordinated by an orchestrator, working alongside humans.[^s2]

Each type has worked patterns. Examples include an interactive messaging client (one agent across WhatsApp, SMS, Slack and Experience Cloud, grounded in Data 360 and escalating to a live agent), external and internal event-response patterns fed by Data 360 streams, the Pub/Sub API, platform events or Change Data Capture, and an autonomous delegation pattern in which a principal agent pursues a goal within playbooks, scopes and guardrails.[^s2] The guide's trade-off tables double as cautions: badly set escalation thresholds frustrate customers, stale vector stores degrade answers, and autonomous agents need rate limits because uncaught errors are costly to unwind.[^s2]

## Named agent roles

The enterprise whitepaper gives individual agents role names, grouped by function:[^s1]

- **Interaction**: Greeter (detects intent and hands off to a human), Operator (also routes to specialist agents), Orchestrator (stays the user's single point of contact while forwarding work to a swarm of specialists and aggregating replies), Listener/Feed and Workspace.[^s1]
- **Specialist**: Answerbot (cited knowledge answers), Domain SME, Interrogator (assembles context across systems to end swivel-chair lookups) and Prioritizer.[^s1]
- **Utility and data**: Generator, Data Steward (checks quality before save), Zen Data Gardener (scheduled grooming), Configurer, Judge & Jury (a judge agent checks juror agents' outputs for consistency and grounding) and Model of Models.[^s1]
- **Long-running**: Project Manager, which creates tasks, tracks completion and notifies stakeholders.[^s1]

An "agentic map" template lays these out in user, agent, context/action and source layers, so architects can see which agents share actions and data.[^s1]

## Multi-agent archetypes

For coordination across agents, the whitepaper defines four archetypes. In **SOMA** (single org, multiple agents) a supervisor agent is the front door and routes to specialists inside one org under shared governance.[^s1] In **MOMA** (multi org, multiple agents) the supervisor delegates to agents in other orgs over the Agent-to-Agent (A2A) protocol while each org keeps its autonomy and the user's identity flows through.[^s1] Two multi-vendor variants add third-party agents, led either by a Salesforce supervisor with MuleSoft facades for systems that don't speak A2A, or by a neutral MuleSoft-hosted orchestrator for requests that start outside Salesforce.[^s1]

In the product, the SOMA shape appears as a Super Agent that routes to Connected Subagents, labelled beta in Salesforce Help at the time of writing.[^s5] Routing is driven mainly by each subagent's description, so descriptions must not overlap; the Salesforce Admins blog recommends a one-sentence test for each subagent, adding deterministic checks in Agent Script to the router, and testing after adding each subagent.[^s5]

## Integration patterns

A companion guide lists eleven agentic integration patterns in three groups.[^s3] *Action invocation* covers sequential, parallel and asynchronous actions, cross-system tool calls over the Model Context Protocol (MCP) and cross-agent delegation over A2A.[^s3] *Agent invocation* covers synchronous calls through the Agent API, exposing business capabilities as MCP tools, publishing agents as A2A services, and event-driven agents started by Data 360-triggered flows or platform events.[^s3] *Grounding* covers retrieval-augmented generation and injecting verified customer context into action inputs.[^s3] Its cross-cutting rules are to make every write idempotent because retries and event redelivery repeat actions, sanitise model-inferred inputs against prompt injection, use named credentials with least privilege, and treat partial success as normal.[^s3]

## When not to use an agent

The architects' decision guide starts from the opposite direction: if every branch of a process can be defined at design time, use Flow or Apex, and adding an agent to a fully deterministic path is an anti-pattern.[^s4] Agents earn their latency and cost where intent is unstructured or goals are open-ended; a common hybrid lets an agent plan and reason while Flow or Apex owns transactions, and Agent Script is recommended where regulated processes need full auditability.[^s4] Irreversible actions such as financial transactions should require human approval, and each added agent or handoff adds failure risk, so start with minimal orchestration and grow it under real load.[^s4]

## Connections

These patterns structure solutions built **under** `kt:agentforce` and are a specialised case of `kt:solution-design-tradeoffs`, **used by** the `kt:salesforce-architect` planning an agent estate.[^s1] The SOMA shape **has part** `kt:multi-agent-orchestration`, realised as Super Agents routing to `kt:agentforce-subagents`, with deterministic routing written in `kt:agent-script`.[^s5] The patterns **depend on** `kt:model-context-protocol-in-agentforce` for tool access and on `kt:agent-to-agent-protocol` for cross-org and cross-vendor delegation.[^s1][^s3] The agentic-vs-traditional guide is one of the `kt:architect-decision-guides`.[^s4]

## Sources

[^s1]: Salesforce Architects, "Enterprise Agentic Architecture and Design Patterns". https://architect.salesforce.com/fundamentals/enterprise-agentic-architecture (accessed 2026-11-16)
[^s2]: Salesforce Architects, "Agentic Patterns". https://architect.salesforce.com/fundamentals/agentic-patterns (accessed 2026-11-16)
[^s3]: Salesforce Architects, "Agentic Integration Patterns". https://architect.salesforce.com/docs/architect/fundamentals/guide/agentic-integration-patterns (accessed 2026-11-16)
[^s4]: Salesforce Architects, "Determining Agentic vs. Traditional Workflow Automation". https://architect.salesforce.com/docs/architect/decision-guides/guide/determining-agentic-vs-traditional-workflow-automation (accessed 2026-11-16)
[^s5]: Salesforce Admins Blog, "How to Set Up a Super Agent with Connected Subagents" (Jennifer W. Lee, 2026-08-20). https://admin.salesforce.com/blog/2026/how-to-set-up-a-super-agent-with-connected-subagents (accessed 2026-11-16)
