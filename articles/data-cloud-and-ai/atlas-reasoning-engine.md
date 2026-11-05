---
id: kt:atlas-reasoning-engine
type: Feature
title: Atlas Reasoning Engine
aliases: [Atlas, Agentforce reasoning engine, Atlas reasoning]
domain: data-cloud-and-ai
summary: >-
  The reasoning engine inside Agentforce that routes each request to a subagent, then runs a reason-act-observe
  loop over that subagent's instructions and actions, grounded in Data 360 and checked before replying; since
  Agent Script it can mix deterministic steps with LLM reasoning (hybrid reasoning).
release: "Winter '27"
status: current
broader: [kt:agentforce]
related: [kt:agent-development-lifecycle, kt:prompt-builder]
relations:
  - {predicate: partOf, object: kt:agentforce}
  - {predicate: configuredVia, object: kt:agent-script}
  - {predicate: implements, object: kt:retrieval-augmented-generation-in-salesforce}
  - {predicate: dependsOn, object: kt:data-cloud}
  - {predicate: dependsOn, object: kt:einstein-trust-layer}
sources:
  - id: s1
    title: "Discover the Atlas Reasoning Engine (Reasoning in Artificial Intelligence)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/reasoning-in-artificial-intelligence/discover-the-atlas-reasoning-engine
    type: official-learning
    accessed: 2026-11-05
  - id: s2
    title: "How the Atlas Reasoning Engine Powers Agentforce"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/atlas-reasoning-engine/
    type: official-blog
    accessed: 2026-11-05
  - id: s3
    title: "Introducing Hybrid Reasoning with Agent Script"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2025/10/introducing-hybrid-reasoning-with-agent-script
    type: official-blog
    accessed: 2026-11-05
  - id: s4
    title: "Legacy Guide: Agentforce Reasoning, Subagents, Instructions, and Actions"
    publisher: Salesforce
    url: https://www.salesforce.com/agentforce/legacy-guide/
    type: official-blog
    accessed: 2026-11-05
  - id: s5
    title: "The Agentforce Guide to Context Engineering"
    publisher: Salesforce
    url: https://www.salesforce.com/agentforce/guide
    type: official-blog
    accessed: 2026-11-05
  - id: s6
    title: "Resolve Routing, Action, and Prompting Issues (Agent Behavior Troubleshooting in Agentforce)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agent-behavior-troubleshooting-in-agentforce/resolve-routing-action-and-prompting-issues
    type: official-learning
    accessed: 2026-11-05
created: 2026-11-05
---

# Atlas Reasoning Engine

Atlas is the component Salesforce calls the brain of Agentforce: the engine that interprets what a user or event wants, decides which tools to use, and keeps going until the goal is met.[^s1] It was incubated at Salesforce AI Research and combines several techniques, including retrieval-augmented generation, to plan and choose actions for both simple and complex jobs.[^s2][^s1]

## Why it was built

Before Atlas, Salesforce's assistant used chain-of-thought prompting: the model wrote a multistep plan up front and executed it in order. Internal testing with thousands of Salesforce sellers showed three weaknesses. Conversations felt mechanical, follow-up questions about information already in the chat went badly, and every added action made latency and answer quality worse.[^s2] Atlas replaced that design with ReAct-style prompting, which tested better.[^s2]

## How it works

The core is a loop of reasoning, acting and observing. The engine reasons about the next step, runs an action, inspects the result and repeats, and it may stop to ask the user a clarifying question or confirm something mid-task.[^s1][^s2]

Scale comes from **subagent classification** (subagents were previously called topics). Each subagent maps to one intent and carries its own instructions, policies and permitted actions, so the model only ever chooses from a narrow, relevant set. Salesforce says this is what lets one agent cover thousands of scenarios safely.[^s2][^s1] In the legacy engine, a turn proceeds as follows:[^s4]

1. Classify the message into a subagent using only subagent names and classification descriptions, with a default classification when nothing fits.[^s4]
2. Build a prompt from that subagent's scope, instructions and actions, the user message and recent history (typically the last six turns).[^s4]
3. Let the model either invoke an action, whose output is fed back for another pass, or answer.[^s4]
4. Check the draft answer for grounding, adherence to scope and instructions, hallucination and prompt-injection risk; retry if it fails, then fall back to a standard cannot-help message.[^s4]

Beyond chat, Atlas can start work proactively when CRM data changes, an email arrives or a meeting approaches. It retrieves structured and unstructured data from Data 360, web search and internal documents, and it treats transfer to a human as an ordinary action.[^s2][^s1] It also exposes the reasoning behind its choices, which admins can inspect in Agentforce Builder to tune behaviour.[^s1][^s2]

## Hybrid reasoning

Purely model-driven chains proved brittle for processes that must run in a fixed order, such as refunds or loan applications.[^s3] Salesforce therefore made Atlas configurable. Developers write **Agent Script**, a compiled language that produces a specification called the Agent Graph; Atlas consumes that graph so loops and multi-subagent coordination run as designed.[^s3] Salesforce describes the result as one engine that combines probabilistic LLM reasoning with deterministic, rules-based execution.[^s5] Once a subagent is chosen, scripted actions run before the model evaluates instructions, and scripted transitions run again after each action, before the engine picks its next step.[^s5] The router itself, now called the Agent Router, becomes a configurable element that can hold conditions, actions and variables.[^s5][^s6]

## Limits and gotchas

- Salesforce advises about 10–15 subagents per agent and at most 15 actions per subagent; overlap and clutter make classification inconsistent and slow the loop.[^s4]
- Routing sees only names and descriptions, so give each subagent a distinct, non-overlapping role and state business rules explicitly rather than expecting inference.[^s6]
- When a subagent or action never fires, check availability filters first, then missing context variables, permissions and description wording. The engine will not infer context variables from instructions.[^s6]
- The legacy guide's step-by-step flow describes the older engine; the newer builder's flow differs, so verify behaviour against the guide for the builder you use.[^s4][^s5]

## Connections

Atlas is **part of** and **narrower than** `kt:agentforce`, the product it powers.[^s1] It is **configured via** `kt:agent-script`, whose compiled Agent Graph drives hybrid reasoning.[^s3] It **implements** `kt:retrieval-augmented-generation-in-salesforce`, drawing on Data 360, so it **depends on** `kt:data-cloud`.[^s2] It **depends on** `kt:einstein-trust-layer` for toxicity detection, zero data retention and prompt-injection defence.[^s2] Prompt templates from `kt:prompt-builder` are among the actions it can select, and testing and observing its decisions is part of the `kt:agent-development-lifecycle`.[^s2][^s1]

## Sources

[^s1]: Trailhead, "Discover the Atlas Reasoning Engine". https://trailhead.salesforce.com/content/learn/modules/reasoning-in-artificial-intelligence/discover-the-atlas-reasoning-engine (accessed 2026-11-05)
[^s2]: Salesforce, "How the Atlas Reasoning Engine Powers Agentforce". https://www.salesforce.com/blog/atlas-reasoning-engine/ (accessed 2026-11-05)
[^s3]: Salesforce Developers Blog, "Introducing Hybrid Reasoning with Agent Script". https://developer.salesforce.com/blogs/2025/10/introducing-hybrid-reasoning-with-agent-script (accessed 2026-11-05)
[^s4]: Salesforce, "Legacy Guide: Agentforce Reasoning, Subagents, Instructions, and Actions". https://www.salesforce.com/agentforce/legacy-guide/ (accessed 2026-11-05)
[^s5]: Salesforce, "The Agentforce Guide to Context Engineering". https://www.salesforce.com/agentforce/guide (accessed 2026-11-05)
[^s6]: Trailhead, "Resolve Routing, Action, and Prompting Issues". https://trailhead.salesforce.com/content/learn/modules/agent-behavior-troubleshooting-in-agentforce/resolve-routing-action-and-prompting-issues (accessed 2026-11-05)
