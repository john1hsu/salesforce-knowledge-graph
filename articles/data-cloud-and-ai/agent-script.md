---
id: kt:agent-script
type: Language
title: Agent Script
aliases: [Agentforce Agent Script, .agent file, agent script language, hybrid reasoning script]
domain: data-cloud-and-ai
summary: >-
  The compiled, indentation-based language behind Agentforce Builder agents, which mixes deterministic logic
  (conditions, variables, action calls, transitions) with natural-language prompt instructions so that business
  rules run predictably while the LLM handles conversation.
release: "Winter '27"
status: current
broader: [kt:agentforce]
related: [kt:agent-actions, kt:atlas-reasoning-engine, kt:agent-development-lifecycle, kt:agentforce-dx]
relations:
  - {predicate: partOf, object: kt:agentforce}
  - {predicate: configuredVia, object: kt:agentforce-studio}
  - {predicate: dependsOn, object: kt:agent-actions}
  - {predicate: enables, object: kt:atlas-reasoning-engine}
  - {predicate: integratesWith, object: kt:salesforce-dx}
sources:
  - id: s1
    title: "Get Started with Agent Script"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/agent-script.html
    type: official-docs
    accessed: 2026-11-05
  - id: s2
    title: "Agent Script Language Characteristics"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/ascript-lang.html
    type: official-docs
    accessed: 2026-11-05
  - id: s3
    title: "Code Your Agent Using Its Agent Script File"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/agent-dx-nga-script.html
    type: official-docs
    accessed: 2026-11-05
  - id: s4
    title: "Agent Script (Salesforce Help)"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=ai.agent_script.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-05
  - id: s5
    title: "Agent Script Decoded: Intro to Agent Script Language Fundamentals"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2026/02/agent-script-decoded-intro-to-agent-script-language-fundamentals
    type: official-blog
    accessed: 2026-11-05
  - id: s6
    title: "Introducing Hybrid Reasoning with Agent Script"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2025/10/introducing-hybrid-reasoning-with-agent-script
    type: official-blog
    accessed: 2026-11-05
created: 2026-11-05
---

# Agent Script

Agent Script is the language used to build agents in Agentforce Builder. It pairs programmatic expressions for business rules with natural-language instructions for conversation, so agent workflows can be predictable and context-aware rather than resting wholly on the LLM's interpretation.[^s1] Salesforce Help describes it as the way to express if/else logic, transitions between subagents, variables, and the choice of subagents and actions; it is available in Lightning Experience in Enterprise, Performance, Unlimited and Developer Editions, with add-on licences that vary by agent type.[^s4]

## Origins

Salesforce introduced Agent Script on the Developers Blog in October 2025 alongside the new Agentforce Builder. It was then in pilot, with a public beta announced for November 2025.[^s6] The motivation was that workflows such as refunds or loan applications need strict, ordered steps that pure LLM reasoning chains handle unreliably; Salesforce called the blend of structured logic and LLM flexibility "hybrid reasoning".[^s6] Current developer and help documentation present it as the standard way to author builder agents and do not label it beta.[^s1][^s4]

## How it works

A script is made of blocks. The getting-started example uses `system` (global instructions plus welcome and error messages), `config` (such as the agent name), `access` (the default agent user), `language` (locales), `variables`, and `start_agent`, the entry subagent with its own `reasoning` block.[^s1] Subagents were called topics until April 2026; the rename did not change behaviour, so older material still says topic.[^s1]

Inside reasoning instructions there are two kinds of line:[^s2]

- **Logic instructions**, introduced with `->`, run deterministically every time. They enforce rules, run actions, set variables and branch.[^s2]
- **Prompt instructions**, introduced with `|`, are natural language passed to the LLM, which decides how to respond.[^s2] Variable values are injected into prompt text with the `{!@variables.name}` form.[^s2]

At run time every user message starts at `start_agent`. Instructions run top to bottom, and the prompt lines whose conditions pass are concatenated into a single prompt, which is all the LLM sees; it is rebuilt each turn as variables change.[^s5] Actions defined in a subagent do nothing until invoked: `run @actions.x` calls one deterministically, with `with` for inputs and `set` to capture outputs, while listing it under `reasoning.actions` exposes it to the LLM as a tool, optionally guarded by `available when`.[^s5] Transitions are likewise either immediate (a bare `transition to` in logic or `after_reasoning`) or offered to the LLM (`@utils.transition to`), and they are one-way except when a subagent is delegated to and control returns.[^s5]

Agent Script is compiled: saving an agent version turns the script into lower-level metadata used by the reasoning engine.[^s2] The launch post says compilation produces an Agent Graph that the Atlas Reasoning Engine consumes.[^s6]

## Authoring surfaces

In Agentforce Builder an author can describe the agent in chat and have it converted to subagents, actions and instructions; edit it in Canvas view, which shows the script as expandable blocks; or edit raw script in Script view with highlighting, autocompletion and validation.[^s1][^s4] With Agentforce DX, the script is a file named `<API-name>.agent` inside `aiAuthoringBundles/<bundle-name>/` in a DX project. `sf agent validate authoring-bundle` compiles it, and a VS Code language server adds error squiggles and an outline view.[^s3] Successful validation means the bundle can be published to the org and then activated.[^s3]

## Limits and gotchas

- Indentation defines structure. Mixing tabs and spaces causes parse errors, and lines at the same level must match.[^s2] The Developers Blog recommends three spaces per level and no tabs.[^s5]
- Expressions are basic. Arithmetic is limited to `+` and `-`, so multiplication, division or modulo belong in a Flow or Apex action. There is no `else if`, and booleans are written `True`/`False`.[^s5][^s2]
- `@` references resolve only to blocks in the script or built-in utilities, not to arbitrary org fields.[^s5]
- Linked variables are read-only, need a `source`, and cannot have a default. `...` is only for action-input slot filling, never a variable default.[^s5]
- Only logic instructions are deterministic. Control-flow decisions buried in long prompt text remain at the LLM's discretion.[^s2][^s5]
- Tooling uses "agent" and "authoring bundle" interchangeably. Enabling Agentforce Vibes skills can sharply increase token use.[^s3]

## When to use it

Use logic instructions for anything that must always happen, such as verification, required data lookups, ordering of steps and guardrails in `after_reasoning`. Keep prompt instructions for tone and open-ended conversation.[^s5] Use Canvas view when admins collaborate on an agent, and use Script view or DX files when developers want source control and validation in their own tools.[^s1][^s3]

## Connections

Agent Script is **part of** `kt:agentforce` and is authored in Agentforce Builder (`kt:agentforce-studio`).[^s1][^s4] It **depends on** `kt:agent-actions`, which it invokes deterministically or exposes as tools.[^s5] Its compiled output **enables** the configurable `kt:atlas-reasoning-engine`.[^s6] It **integrates with** `kt:salesforce-dx` through `kt:agentforce-dx` authoring bundles, which slot into the `kt:agent-development-lifecycle`.[^s3]

## Sources

[^s1]: Salesforce Developers, "Get Started with Agent Script". https://developer.salesforce.com/docs/ai/agentforce/guide/agent-script.html (accessed 2026-11-05)
[^s2]: Salesforce Developers, "Agent Script Language Characteristics". https://developer.salesforce.com/docs/ai/agentforce/guide/ascript-lang.html (accessed 2026-11-05)
[^s3]: Salesforce Developers, "Code Your Agent Using Its Agent Script File". https://developer.salesforce.com/docs/ai/agentforce/guide/agent-dx-nga-script.html (accessed 2026-11-05)
[^s4]: Salesforce Help, "Agent Script". https://help.salesforce.com/s/articleView?id=ai.agent_script.htm&language=en_US&type=5 (accessed 2026-11-05)
[^s5]: Salesforce Developers Blog, "Agent Script Decoded: Intro to Agent Script Language Fundamentals". https://developer.salesforce.com/blogs/2026/02/agent-script-decoded-intro-to-agent-script-language-fundamentals (accessed 2026-11-05)
[^s6]: Salesforce Developers Blog, "Introducing Hybrid Reasoning with Agent Script". https://developer.salesforce.com/blogs/2025/10/introducing-hybrid-reasoning-with-agent-script (accessed 2026-11-05)
