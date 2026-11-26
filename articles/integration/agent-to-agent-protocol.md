---
id: kt:agent-to-agent-protocol
type: ExternalConcept
title: Agent2Agent (A2A) Protocol
aliases: [A2A, A2A protocol, Agent-to-Agent Protocol, Agent2Agent]
domain: integration
summary: >-
  An open, vendor-neutral protocol, now a Linux Foundation project, that lets AI agents built on different
  platforms discover each other through Agent Cards and exchange tasks, messages and artifacts over HTTP using
  JSON-RPC 2.0 and Server-Sent Events; Salesforce agents reach it today through a MuleSoft Agent Fabric A2A bridge.
release: "Winter '27"
status: concept
broader: [kt:integration-patterns]
related: [kt:agentforce-architecture-patterns, kt:model-context-protocol-in-agentforce, kt:agentforce]
relations:
  - {predicate: contrastsWith, object: kt:model-context-protocol}
  - {predicate: enables, object: kt:multi-agent-orchestration}
  - {predicate: integratesWith, object: kt:agent-api}
  - {predicate: consumedBy, object: kt:mulesoft-anypoint-platform}
  - {predicate: dependsOn, object: kt:oauth-2-0}
sources:
  - id: s1
    title: "Agent2Agent (A2A) Protocol Specification"
    publisher: A2A Project
    url: https://google-a2a.github.io/A2A/specification
    type: standards-body
    accessed: 2026-11-26
  - id: s2
    title: "A2A Protocol Surpasses 150 Organizations, Lands in Major Cloud Platforms, and Sees Enterprise Production Use in First Year"
    publisher: The Linux Foundation
    url: https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year
    type: news
    accessed: 2026-11-26
  - id: s3
    title: "Google Cloud donates A2A to Linux Foundation"
    publisher: Google Developers Blog
    url: https://developers.googleblog.com/en/google-cloud-donates-a2a-to-linux-foundation/
    type: partner
    accessed: 2026-11-26
  - id: s4
    title: "Make an Agent A2A-Compliant (Agent Fabric)"
    publisher: MuleSoft (Salesforce)
    url: https://docs.mulesoft.com/general/exp-services-create-a2a-bridge
    type: official-docs
    accessed: 2026-11-26
  - id: s5
    title: "Agentic Patterns and Implementation with Agentforce"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/agentic-patterns
    type: official-docs
    accessed: 2026-11-26
  - id: s6
    title: "Agent2Agent Protocol: The Standard for AI Agent Interoperability"
    publisher: Salesforce
    url: https://www.salesforce.com/agentforce/ai-agents/agent2agent-protocol/
    type: official-blog
    accessed: 2026-11-26
created: 2026-11-26
---

# Agent2Agent (A2A) Protocol

The Agent2Agent (A2A) protocol is an open standard for agent interoperability: a "client" agent finds a "remote" agent, learns what it can do, and hands it work, regardless of which vendor or framework built either side.[^s6] Google donated A2A to the Linux Foundation in June 2025, forming the Agent2Agent project with Amazon Web Services, Cisco, Google, Microsoft, Salesforce, SAP and ServiceNow as founding members.[^s3] By April 2026 the Linux Foundation reported more than 150 supporting organizations, SDKs in five languages, and a v1.0 release that it calls the first stable specification.[^s2]

## How it works

A2A deliberately reuses existing web standards rather than inventing a new transport: requests travel over HTTP(S) with JSON-RPC 2.0 payloads, and streaming uses Server-Sent Events.[^s1] The main building blocks are:[^s1][^s6]

- **Agent Card**: a JSON document, published at a well-known URI, that advertises the agent's identity, endpoint, skills, capabilities and accepted security schemes.[^s1]
- **Task**: the unit of work, with a lifecycle that includes submitted, working, input-required, auth-required, completed, canceled, failed and rejected.[^s1]
- **Message and Part**: conversational turns from the user or agent role, carrying text, file or structured data parts.[^s1]
- **Artifact**: the output a remote agent produces for a task, which can be streamed in chunks.[^s1]

Interaction follows three phases: discovery via the Agent Card, authentication and authorization, then communication either synchronously, as an SSE stream, or through push notifications to a client webhook.[^s6] Authentication is ordinary HTTP auth (bearer tokens, API keys, OAuth 2.0, OpenID Connect) declared in the card; credentials are obtained out of band and the server must authenticate every request.[^s1] Version 1.0 added multi-protocol support, multi-tenancy, modernized security flows and signed Agent Cards.[^s2]

## A2A in the Salesforce ecosystem

Salesforce frames A2A as the complement to the Model Context Protocol (MCP): MCP lets a model reach outward to tools and data, while A2A governs how autonomous agents coordinate with one another.[^s6][^s2] The Architects' agentic-patterns guide names A2A as the communication protocol behind collaborative "agent swarm" designs, where an orchestrator decomposes a request and delegates pieces to specialist agents.[^s5]

Agentforce agents are not natively A2A-compliant; MuleSoft Agent Fabric closes that gap with an **A2A bridge**, a chain of policies on an Omni Gateway that puts an A2A facade in front of a non-A2A agent and translates calls into the Agentforce Agent API, with no change to the source agent.[^s4] Setting one up requires an Anypoint Platform account, a managed or self-managed Omni Gateway, the agent registered in Portfolio, and the matching Exchange and API Manager permissions.[^s4] The bridged instance publishes its card at `.well-known/agent-card.json`.[^s4]

## Limits and gotchas

- The bridge advertises a single JSON-RPC interface and keeps task state in gateway memory, so state is lost on a gateway restart.[^s4]
- Agentforce bridges lack async tasks, task resubscription and push notifications, and support input-required only partly.[^s4]
- The well-known Agent Card path changed across spec versions (`agent.json` in the 0.2.x specification), so check which version a remote agent implements.[^s1][^s4]
- When a platform adds native A2A, the documented migration is to disable the bridge and point clients at the native endpoint.[^s4]

## When to use it (and when not)

Use A2A when work must cross agent boundaries owned by different teams, orgs or vendors, for example an Agentforce service agent delegating to a billing agent on another cloud.[^s5] For an agent calling a tool, API or data source, MCP or a standard agent action is the better fit; inside one Salesforce org, native orchestration of subagents avoids the extra gateway hop.[^s6][^s5]

## Connections

A2A is a cross-vendor case of `kt:integration-patterns`, and it **contrasts with** `kt:model-context-protocol`, whose Salesforce client is `kt:model-context-protocol-in-agentforce`.[^s6] It **enables** `kt:multi-agent-orchestration` and underpins the swarm designs in `kt:agentforce-architecture-patterns`.[^s5] Through the MuleSoft bridge it **integrates with** `kt:agent-api` and is **consumed by** `kt:mulesoft-anypoint-platform` (Agent Fabric).[^s4] Its security model **depends on** standard schemes such as `kt:oauth-2-0`.[^s1] It relates to `kt:agentforce`, whose agents it makes reachable from other platforms.[^s4]

## Sources
[^s1]: A2A Project, "Agent2Agent (A2A) Protocol Specification". https://google-a2a.github.io/A2A/specification (accessed 2026-11-26)
[^s2]: The Linux Foundation, "A2A Protocol Surpasses 150 Organizations…" (April 9, 2026). https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year (accessed 2026-11-26)
[^s3]: Google Developers Blog, "Google Cloud donates A2A to Linux Foundation" (June 23, 2025). https://developers.googleblog.com/en/google-cloud-donates-a2a-to-linux-foundation/ (accessed 2026-11-26)
[^s4]: MuleSoft, "Make an Agent A2A-Compliant". https://docs.mulesoft.com/general/exp-services-create-a2a-bridge (accessed 2026-11-26)
[^s5]: Salesforce Architects, "Agentic Patterns and Implementation with Agentforce". https://architect.salesforce.com/fundamentals/agentic-patterns (accessed 2026-11-26)
[^s6]: Salesforce, "Agent2Agent Protocol: The Standard for AI Agent Interoperability". https://www.salesforce.com/agentforce/ai-agents/agent2agent-protocol/ (accessed 2026-11-26)
