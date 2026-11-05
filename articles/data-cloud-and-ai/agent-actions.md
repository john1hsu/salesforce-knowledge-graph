---
id: kt:agent-actions
type: Feature
title: Agent Actions
aliases: [Agentforce actions, agent action, custom agent actions, standard agent actions, Copilot actions]
domain: data-cloud-and-ai
summary: >-
  The tools an Agentforce agent can call to do work: prebuilt standard actions plus custom actions that wrap an
  autolaunched flow, an invocable or REST Apex method, or a prompt template, each described in natural language so
  the reasoning engine can choose and fill it.
release: "Winter '27"
status: current
broader: [kt:agentforce]
related: [kt:atlas-reasoning-engine, kt:agent-script, kt:agentforce-testing-center]
relations:
  - {predicate: partOf, object: kt:agentforce}
  - {predicate: dependsOn, object: kt:autolaunched-flow}
  - {predicate: dependsOn, object: kt:apex}
  - {predicate: dependsOn, object: kt:prompt-builder}
  - {predicate: governedBy, object: kt:governor-limits}
sources:
  - id: s1
    title: "Customize Your Agents (Agent Customization: Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agent-customization-quick-look/customize-your-agents
    type: official-learning
    accessed: 2026-11-05
  - id: s2
    title: "Create Custom Actions Using Apex Invocable Method"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/agent-invocablemethod.html
    type: official-docs
    accessed: 2026-11-05
  - id: s3
    title: "Best Practices for Building Agentforce Apex Actions"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2025/05/best-practices-for-building-agentforce-apex-actions
    type: official-blog
    accessed: 2026-11-05
  - id: s4
    title: "Agentforce Workshop: Standard Actions"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/workshops/agentforce-workshop/employee-agents/3-standard-actions
    type: official-learning
    accessed: 2026-11-05
  - id: s5
    title: "Agentforce Workshop: Flow Actions"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/workshops/agentforce-new-workshop/employee-agents/3-flow-actions
    type: official-learning
    accessed: 2026-11-05
  - id: s6
    title: "Create an Apex Agent Action (Agent Customization with Apex)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agent-customization-with-apex/create-an-apex-agent-action
    type: official-learning
    accessed: 2026-11-05
created: 2026-11-05
---

# Agent Actions

Agent actions are the tools an Agentforce agent uses to get things done. An agent can read any data it has access to, but it can change records only through a predefined action, and actions can be configured and chained together.[^s1] Each action belongs to a subagent (formerly a topic), and the reasoning engine decides at run time which available action fits the user's request, sometimes calling several for one complex request. The builder's plan panel shows each step it took.[^s4]

## Standard and custom actions

**Standard actions** are prebuilt in Agentforce Builder and let an agent work with Salesforce data without custom development. Examples include Query Records, Query Records with Aggregate, Get Record Details, Summarize Record, Identify Object by Name, Identify Record by Name, Update Record, and Draft or Revise Email.[^s4] They are added to a subagent by ticking them when the subagent is created or edited, and they are the recommended starting point before custom work.[^s4]

**Custom actions** wrap existing platform functionality, which Trailhead calls the *reference action*. Supported reference types are invocable and REST Apex classes, autolaunched flows, and prompt templates.[^s1] Trailhead divides them by behaviour:[^s1]

- **Deterministic** actions use a flow or Apex to apply business logic and return consistent results.[^s1]
- **Non-deterministic** actions use a prompt template from Prompt Builder. They suit summarising, sentiment analysis, and grounding answers in knowledge or external data.[^s1]
- One action can mix both, for example a flow that performs a cancellation while a prompt gathers the reason.[^s1]

## How an action is configured

To create a custom action, open a subagent's actions, choose to create a new action, pick the reference action type and the specific flow, Apex method or template, then review its inputs and outputs.[^s6][^s5] The reference's inputs and outputs appear in the action, and each gets a natural-language instruction that the model reads.[^s5][^s6] Key settings include:[^s5]

- **Require input to execute action** (per input): the agent must collect the value, usually from the user, before running.[^s5]
- **Show in conversation** (per output): displays the output to the user in the chat.[^s5]
- **Require user confirmation**: the agent restates what it is about to change and waits for approval, which suits write actions.[^s5]
- **Follow-up action**: runs automatically after success, for example setting a variable that later instructions or conditions test.[^s5]

For Apex, the developer guide shows a class whose method carries `@InvocableMethod` with a `label` and `description`, taking a list of request wrappers and returning a list of responses whose fields are `@InvocableVariable`s; that annotation makes the method available in Agentforce Builder.[^s2] The variable descriptions pre-fill the action's input and output instructions, and whether an input is required comes from the code, so changing it means editing the Apex.[^s6] Changes take effect only after the agent version is committed and activated.[^s6]

## Limits and gotchas

- Actions don't bulkify by default and each runs in its own transaction, so write bulk-safe Apex and instruct the agent to pass all records in one call.[^s3]
- If a composite action hits CPU timeouts, split it; push long work to Queueable Apex and tell the user how to check status later.[^s3]
- Instructions sequence actions non-deterministically. When order matters, build one composite action in Apex or Flow, or pass data between actions through variables.[^s3]
- Declare Apex classes `with sharing` and run queries and DML in user mode. Verify the user before running private actions, and return only needed fields from public ones.[^s3]
- Keep labels and descriptions identical in code and in the action configuration, wrap logic in try-catch, and return friendly messages; use `Database` methods with `allOrNone` set to false for partial success.[^s3]

## When to use which

Start with standard actions for generic record lookup, summarisation and drafting.[^s4] Use a flow when an admin should own deterministic logic in low code; agent-ready flows can also narrow the data an agent sees.[^s1] Use Apex for complex logic or reuse across objects, since a developer can package it for admins to use without code.[^s1][^s3] Use a prompt template when the output is generated language.[^s1] Test with the builder's preview, Agentforce Testing Center for bulk inputs, and Apex unit tests for the code underneath.[^s3]

## Connections

Agent actions are **part of** `kt:agentforce`, and the `kt:atlas-reasoning-engine` selects among them using their descriptions.[^s4][^s6] Custom actions **depend on** `kt:autolaunched-flow`, `kt:apex` and `kt:prompt-builder` templates as their reference actions.[^s1][^s2] Apex actions are **governed by** `kt:governor-limits`, since each action runs in its own transaction and can hit CPU timeouts.[^s3] They are **related** to `kt:agent-script`, whose conditions and variables decide when actions run, and to `kt:agentforce-testing-center`, used to bulk-test them.[^s5][^s3]

## Sources

[^s1]: Trailhead, "Customize Your Agents". https://trailhead.salesforce.com/content/learn/modules/agent-customization-quick-look/customize-your-agents (accessed 2026-11-05)
[^s2]: Salesforce Developers, "Create Custom Actions Using Apex Invocable Method". https://developer.salesforce.com/docs/ai/agentforce/guide/agent-invocablemethod.html (accessed 2026-11-05)
[^s3]: Salesforce Developers Blog, "Best Practices for Building Agentforce Apex Actions". https://developer.salesforce.com/blogs/2025/05/best-practices-for-building-agentforce-apex-actions (accessed 2026-11-05)
[^s4]: Salesforce Developers, "Agentforce Workshop: Standard Actions". https://developer.salesforce.com/workshops/agentforce-workshop/employee-agents/3-standard-actions (accessed 2026-11-05)
[^s5]: Salesforce Developers, "Agentforce Workshop: Flow Actions". https://developer.salesforce.com/workshops/agentforce-new-workshop/employee-agents/3-flow-actions (accessed 2026-11-05)
[^s6]: Trailhead, "Create an Apex Agent Action". https://trailhead.salesforce.com/content/learn/modules/agent-customization-with-apex/create-an-apex-agent-action (accessed 2026-11-05)
