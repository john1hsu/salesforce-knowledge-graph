---
id: kt:agentforce-subagents
type: Feature
title: Agentforce Subagents
aliases: [Agentforce topics, agent topics, agent subagents, Topic Selector]
domain: data-cloud-and-ai
summary: >-
  The units of work inside an Agentforce agent (called topics until April 2026): each subagent has a name,
  classification description, scope, instructions and a set of actions, and the Agent Router picks one per
  request based only on names and descriptions.
release: "Winter '27"
status: current
broader: [kt:agentforce]
related: [kt:agentforce-testing-center, kt:agent-development-lifecycle]
relations:
  - {predicate: partOf, object: kt:agentforce}
  - {predicate: dependsOn, object: kt:agent-actions}
  - {predicate: configuredVia, object: kt:agent-script}
  - {predicate: configuredVia, object: kt:agentforce-studio}
  - {predicate: consumedBy, object: kt:atlas-reasoning-engine}
sources:
  - id: s1
    title: "Legacy Guide: Agentforce Reasoning, Subagents, Instructions, and Actions"
    publisher: Salesforce
    url: https://www.salesforce.com/agentforce/legacy-guide/
    type: official-blog
    accessed: 2026-11-11
  - id: s2
    title: "Agent Script Reference"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/ascript-reference.html
    type: official-docs
    accessed: 2026-11-11
  - id: s3
    title: "Customize Agent Topics (Agent Builder Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agent-builder-basics/customize-agent-topics
    type: official-learning
    accessed: 2026-11-11
  - id: s4
    title: "Resolve Routing, Action, and Prompting Issues"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agent-behavior-troubleshooting-in-agentforce/resolve-routing-action-and-prompting-issues
    type: official-learning
    accessed: 2026-11-11
  - id: s5
    title: "Build with Agentforce Builder"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/quick-start-assemble-a-service-agent-with-agentforce-builder/build-with-agentforce-builder
    type: official-learning
    accessed: 2026-11-11
created: 2026-11-11
---

# Agentforce Subagents

A **subagent** is one job an Agentforce agent knows how to do, such as checking an order or resetting a password. Salesforce compares subagents to specialized departments: each carries its own expertise, actions and instructions, plus a scope that fixes what the agent may and may not do in that area.[^s1] Until April 2026 the same building block was called a **topic**. Salesforce renamed topics to subagents with no functional change, renamed the Topic Selector to the **Agent Router**, and renamed Connected Agent to Connected Subagent; both terms still appear during the transition.[^s1][^s2] Older Trailhead content and many existing orgs still use "topics".[^s3]

## Anatomy of a subagent

Every subagent is defined by a handful of fields, and each one plays a different role at run time.[^s1][^s3]

- **Name (label)**: a short label that, together with the classification description, is used to route requests.[^s1]
- **Classification description**: says which user messages should trigger this subagent; it is the main input to routing.[^s1][^s3]
- **Scope**: a job-description-style statement of what the agent can and cannot do inside this subagent.[^s1][^s3]
- **Instructions**: natural-language guidance on which actions to pick, how to converse, and business context.[^s1]
- **Actions**: the standard and custom actions the subagent may call; one action can be reused across several subagents.[^s1]

## How routing works

On each message the reasoning engine first classifies the request into the most relevant subagent. For that step it sees only subagent names and classification descriptions, and it falls back to a default classification when nothing matches.[^s1] Once a subagent is chosen, its scope, instructions and actions are injected into the prompt along with the user message and recent history, typically the last six turns.[^s1] In the new Agentforce Builder this first step is itself a subagent, the Agent Router, which compares the conversation history and latest message with subagent names and descriptions.[^s4][^s5]

**Filters** make availability deterministic. A subagent-level filter decides whether a subagent can be classified at all, and an action-level filter decides which of its actions are offered, based on context variables (fixed at session start) or custom variables (set from action outputs).[^s1] A typical use is hiding account-related subagents until the customer is authenticated.[^s1] A subagent can also be removed from the router's references so it is reachable only through a transition from another subagent.[^s4]

## Building subagents

In the classic builder, admins add subagents from the Asset Library of standard topics, which lists each one with its label, classification description and scope, or create a custom one when nothing fits.[^s3] Salesforce recommends starting from preconfigured topics and actions and reading their instructions before changing them.[^s3] In the new Agentforce Builder, new service agents ship with default subagents; each subagent has its own folder in the explorer, and admins add one with the plus icon or ask the Agentforce Assistant in plain language.[^s5] The canvas and script views stay in sync.[^s5] In Agent Script a subagent is a top-level `subagent` block with a `reasoning` section of instructions and actions, `start_agent` marks the routing entry point, and `transition to @subagent.<name>` moves control between subagents; the older `topic` keyword is deprecated.[^s2]

## Limits and gotchas

- Salesforce advises about 10–15 subagents per agent; too many or overlapping ones make classification inconsistent.[^s1]
- Keep each subagent to no more than 15 actions to limit latency.[^s1]
- Names should be short, start with a verb and not overlap in meaning; review existing subagents before adding one.[^s1]
- Classification descriptions should use the customer's own phrasing and keywords, in natural language, distinct from other descriptions.[^s1]
- Instructions are interpreted by the LLM and are non-deterministic; words like "always" and "never" are read literally.[^s1]
- Put critical business rules in actions, filters or Agent Script logic rather than instructions.[^s1][^s4]

When the agent skips the expected subagent, Salesforce's troubleshooting guidance is to start with the Agent Router: look for unclear or overlapping descriptions, filters that exclude the subagent, and context variables that were never initialized.[^s4] If prompt changes don't fix it, add programmatic logic through Agent Script's hybrid reasoning.[^s4]

## Connections

Subagents are **part of** `kt:agentforce` and are the units the `kt:atlas-reasoning-engine` **consumes** when it classifies and plans.[^s1] Each **depends on** `kt:agent-actions` for anything it actually does.[^s1] Subagents are **configured via** `kt:agentforce-studio`, where the Agentforce Builder lives, and via `kt:agent-script`, whose `subagent` blocks define them in code.[^s5][^s2] Because routing hinges on names, descriptions and filters, subagent changes are natural candidates for the build-test-iterate loop of `kt:agent-development-lifecycle` and for regression checks in `kt:agentforce-testing-center`.[^s1][^s4]

## Sources

[^s1]: Salesforce, "Legacy Guide: Agentforce Reasoning, Subagents, Instructions, and Actions". https://www.salesforce.com/agentforce/legacy-guide/ (accessed 2026-11-11)
[^s2]: Salesforce Developers, "Agent Script Reference". https://developer.salesforce.com/docs/ai/agentforce/guide/ascript-reference.html (accessed 2026-11-11)
[^s3]: Trailhead, "Customize Agent Topics". https://trailhead.salesforce.com/content/learn/modules/agent-builder-basics/customize-agent-topics (accessed 2026-11-11)
[^s4]: Trailhead, "Resolve Routing, Action, and Prompting Issues". https://trailhead.salesforce.com/content/learn/modules/agent-behavior-troubleshooting-in-agentforce/resolve-routing-action-and-prompting-issues (accessed 2026-11-11)
[^s5]: Trailhead, "Build with Agentforce Builder". https://trailhead.salesforce.com/content/learn/modules/quick-start-assemble-a-service-agent-with-agentforce-builder/build-with-agentforce-builder (accessed 2026-11-11)
