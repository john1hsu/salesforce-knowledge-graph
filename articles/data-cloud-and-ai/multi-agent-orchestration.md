---
id: kt:multi-agent-orchestration
type: Feature
title: Multi-Agent Orchestration
aliases: [Agentforce multi-agent orchestration, Super Agent, super agents, Connected Subagents, connected subagent, Connected Agents, orchestrator agent]
domain: data-cloud-and-ai
summary: >-
  Agentforce's way of having one orchestrator (Super) agent take every request and delegate it to specialist
  agents declared as Connected Subagents in the same org; generally available in Winter '27, and extended across
  vendors and orgs by MuleSoft Agent Fabric's A2A-based Agent Broker.
release: "Winter '27"
status: current
broader: [kt:agentforce]
related: [kt:agentforce-subagents, kt:agentforce-architecture-patterns, kt:agentforce-employee-agents, kt:atlas-reasoning-engine]
relations:
  - {predicate: configuredVia, object: kt:agent-script}
  - {predicate: dependsOn, object: kt:agent-to-agent-protocol}
  - {predicate: integratesWith, object: kt:mulesoft-anypoint-platform}
  - {predicate: dependsOn, object: kt:model-context-protocol}
  - {predicate: integratesWith, object: kt:mulesoft-agent-fabric}
sources:
  - id: s1
    title: "The Salesforce Developer's Guide to the Winter '27 Release"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2026/10/developers-guide-to-the-winter-27-release
    type: official-blog
    accessed: 2026-11-27
  - id: s2
    title: "What Is Multi-Agent Orchestration, and When To Build a Super Agent or a Single Agent"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2026/what-is-soma-and-when-to-build-a-super-agent-or-a-single-agent
    type: official-blog
    accessed: 2026-11-27
  - id: s3
    title: "How to Set Up a Super Agent with Connected Subagents"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2026/how-to-set-up-a-super-agent-with-connected-subagents
    type: official-blog
    accessed: 2026-11-27
  - id: s4
    title: "MuleSoft Agent Fabric - Deep Dive"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/mulesoft-agent-fabric-deep-dive
    type: official-docs
    accessed: 2026-11-27
  - id: s5
    title: "Agent Fabric Overview"
    publisher: MuleSoft Documentation
    url: https://docs.mulesoft.com/agent-fabric/
    type: official-docs
    accessed: 2026-11-27
  - id: s6
    title: "Orchestrating Multi-Agent Processes with Agent Networks"
    publisher: MuleSoft Documentation
    url: https://docs.mulesoft.com/agent-network/latest/af-use-case-orchestration
    type: official-docs
    accessed: 2026-11-27
created: 2026-11-27
---

# Multi-Agent Orchestration

**Multi-agent orchestration** is the Agentforce capability in which several specialist agents in one Salesforce org work as a team behind a single front door. One orchestrator, which Salesforce calls a **Super Agent**, receives every user message, decides which specialist should handle it, hands over the needed context and takes control back when the specialist is done; the user sees a single conversation and never the handoffs.[^s2] Specialists are separate agents attached to the orchestrator as **Connected Subagents**.[^s2][^s3] The feature was in beta during 2026 and the Winter '27 developer guide announces it as generally available.[^s1][^s2]

## How it works

The orchestrator's Agent Router (the `start_agent` block in Agent Script) is the entry point for every utterance. It compares the request with the description of each Connected Subagent, picks the best match, passes context such as the verified user, a case number or an order ID, waits while the specialist runs its own reasoning and actions, then consolidates the answer.[^s2][^s3] Routing is evaluated again on every message, so a follow-up in the same conversation can land on a different specialist.[^s2] The orchestrator deliberately knows little about each domain beyond which agent owns it, and Connected Subagents answer but do not route further; if one starts calling another, Salesforce advises revisiting the design.[^s2]

In Winter '27 Agent Script, a specialist is declared in a `connected_subagent` block with a `target` that points to the other agent and a `description` used for routing, and the orchestrator hands off to it the same way it moves to any local subagent. The release example also sets a `delegate_escalation` flag on the connected specialist.[^s1] Earlier beta guidance said that `transition to` could not reach a Connected Subagent and that admins had to call the action wrapping it instead, so scripts written during the beta may use that older style.[^s3][^s1]

The difference from ordinary subagents matters. A subagent (formerly a topic) is a bundle of instructions and actions inside one agent, while a Connected Subagent is a whole agent with its own subagents, actions and data access.[^s2] The orchestrator can still keep shared subagents of its own for cross-cutting work such as identity verification, content safety, disambiguation and the decision to hand off to a human, so each specialist does not carry a copy of that logic.[^s3]

## Limits and gotchas

- Salesforce recommends no more than 7 Connected Subagents per orchestrator; this is guidance, not an enforced limit.[^s2]
- The beta supported service-agent orchestrators with service-agent specialists, and employee-agent orchestrators with either employee or service specialists.[^s2]
- Description-only routing was right about 80% of the time in Salesforce's worked example; the rest needed deterministic conditions on variables and negative guardrails.[^s3]
- Overlapping or vague descriptions are the most common cause of misrouting, so a description that needs the word "and" should be split.[^s2][^s3]
- Build and test each specialist alone, then connect and re-test routing one specialist at a time.[^s3]

## When to use it (and when not)

A single agent with several subagents remains the right shape when the work stays in one domain and shares the same data access.[^s2] A Super Agent pays off when one agent hits context overload, when generalist instructions start misapplying logic across domains, or when work naturally hands off between teams but users still want one entry point; a typical example is an employee-services agent fronting HR, IT and facilities specialists.[^s2] Multi-agent orchestration in Agentforce is scoped to agents in one org; an agent cannot reach data or permissions in another org.[^s2]

For networks that span orgs or vendors, Salesforce's answer is **MuleSoft Agent Fabric**. Its Agent Broker is an LLM-driven router, written in Agent Script inside an agent network project, that delegates tasks only to A2A-compliant agents; Agentforce agents join through an A2A bridge, and tools are reached over MCP.[^s5][^s6] Agent networks support sequential, parallel, conditional and hierarchical routing, and Salesforce Architects recommend hierarchies of brokers over one flat broker because too many options degrade routing accuracy and inflate context.[^s6][^s4] Agent Fabric adds a registry, gateway policies for A2A and MCP traffic and a visualizer for the resulting topology.[^s4][^s5]

## Connections

Multi-agent orchestration is a feature of `kt:agentforce` and builds on `kt:agentforce-subagents`: the orchestrator hands off to a Connected Subagent much as it moves to a local subagent, and both are **configured via** `kt:agent-script`.[^s1][^s3] Each specialist still runs its own reasoning loop, the job of the `kt:atlas-reasoning-engine` in every agent.[^s2] It is the product form of the multi-agent archetypes described in `kt:agentforce-architecture-patterns`, and an employee-agent orchestrator fronting HR, IT and facilities specialists is Salesforce's own example built from `kt:agentforce-employee-agents`.[^s2] Beyond one org it **depends on** `kt:agent-to-agent-protocol` and `kt:model-context-protocol`, and it **integrates with** `kt:mulesoft-anypoint-platform` and its `kt:mulesoft-agent-fabric`, whose broker is the cross-vendor orchestration layer.[^s4][^s5]

## Sources

[^s1]: Salesforce Developers Blog, "The Salesforce Developer's Guide to the Winter '27 Release" (2026-10-05). https://developer.salesforce.com/blogs/2026/10/developers-guide-to-the-winter-27-release (accessed 2026-11-27)
[^s2]: Salesforce Admins Blog, "What Is Multi-Agent Orchestration, and When To Build a Super Agent or a Single Agent" (Jennifer W. Lee, 2026-07-27). https://admin.salesforce.com/blog/2026/what-is-soma-and-when-to-build-a-super-agent-or-a-single-agent (accessed 2026-11-27)
[^s3]: Salesforce Admins Blog, "How to Set Up a Super Agent with Connected Subagents" (Jennifer W. Lee, 2026-08-20). https://admin.salesforce.com/blog/2026/how-to-set-up-a-super-agent-with-connected-subagents (accessed 2026-11-27)
[^s4]: Salesforce Architects, "MuleSoft Agent Fabric - Deep Dive". https://architect.salesforce.com/fundamentals/mulesoft-agent-fabric-deep-dive (accessed 2026-11-27)
[^s5]: MuleSoft Documentation, "Agent Fabric Overview". https://docs.mulesoft.com/agent-fabric/ (accessed 2026-11-27)
[^s6]: MuleSoft Documentation, "Orchestrating Multi-Agent Processes with Agent Networks". https://docs.mulesoft.com/agent-network/latest/af-use-case-orchestration (accessed 2026-11-27)
