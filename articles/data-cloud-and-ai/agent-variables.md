---
id: kt:agent-variables
type: Feature
title: Agent Variables
aliases: [Agentforce variables, agent conversation variables, Agentforce context variables, Agent Script variables, ConversationVariable]
domain: data-cloud-and-ai
summary: >-
  Typed, session-scoped values that an Agentforce agent stores and reads deterministically, used to carry
  action outputs between turns and subagents, feed action inputs, branch instructions, and gate which
  actions and subagents the LLM can see.
release: "Winter '27"
status: current
broader: [kt:agentforce, kt:agent-script]
related: [kt:agent-actions, kt:agentforce-subagents, kt:agent-api, kt:atlas-reasoning-engine, kt:prompt-injection]
relations:
  - {predicate: partOf, object: kt:agent-script}
  - {predicate: configuredVia, object: kt:agentforce-studio}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: consumedBy, object: kt:agent-actions}
  - {predicate: mitigates, object: kt:prompt-injection}
sources:
  - id: s1
    title: "Agent Script Reference: Variables (Custom and Linked)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/ascript-ref-variables.html
    type: official-docs
    accessed: 2026-11-26
  - id: s2
    title: "Send Agent Variables with the Agent API"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/agent-api-variables.html
    type: official-docs
    accessed: 2026-11-26
  - id: s3
    title: "Agent Script Pattern: Using Variables Effectively"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/ascript-patterns-variables.html
    type: official-docs
    accessed: 2026-11-26
  - id: s4
    title: "Enforce Business Rules with Action Filters and Variables"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/programmatic-instructions-in-agentforce/enforce-business-rules-with-variables-and-action-filters
    type: official-learning
    accessed: 2026-11-26
  - id: s5
    title: "Agentforce Variables: A New Way to Structure Agent Memory"
    publisher: Salesforce Developers Blog (Olfa Kharrat)
    url: https://developer.salesforce.com/blogs/2025/04/agentforce-variables-a-new-way-to-structure-agent-memory
    type: official-blog
    accessed: 2026-11-26
created: 2026-11-26
---

# Agent Variables

Agent variables are the structured memory of an Agentforce agent. They let the agent remember facts deterministically across conversation turns, track where it is in a process, and keep context for the whole session. Every subagent in the agent can read them.[^s1] Salesforce introduced them as a new kind of memory that actions can pass to each other and that can act as conditions for running actions. That gives them two jobs: grounding that persists across turns, and determinism, because they gate what the LLM is allowed to do.[^s5]

## Kinds of variables

- **Custom variables** are ones you define. They can have an optional default value, and the agent can change them only when they are declared `mutable`.[^s1]
- **Linked variables** are bound to a source and read from it. They cannot have a default value, the agent cannot set them, and they cannot be objects or lists.[^s1]
- **Context variables** are system-supplied facts about the user and session. In the Agent API they use the `$Context.` prefix, and custom fields drop the `__c` suffix.[^s2][^s5]

Linked variables currently draw from the messaging session (`Id`, `MessagingEndUserId`, `EndUserLanguage`), the messaging end user (`ContactId`) and the voice call (`Id`).[^s1] Custom variables support `string`, `number` (IEEE 754 double precision), `boolean`, `object` (JSON), `date` and `list[...]` of primitives or objects. The `id` type is deprecated; use `string` to hold record IDs.[^s1] Names must start with a letter, use only letters, digits and underscores, contain no double underscore, not end in an underscore, and stay within 80 characters.[^s1]

## How values get set and used

In Agent Script, a variable is referenced as `@variables.<name>`, and inside reasoning instructions as `{!@variables.<name>}`. `None`, or an empty string for strings, tests whether a value is missing.[^s1] There are three ways a value gets set. A deterministic `set` can copy an action output into a variable, for example after `run @actions.lookup_current_order`. The LLM can fill a slot through `@utils.setVariables`, where the `...` placeholder asks the model to supply a value. An action output mapping can also write to a variable.[^s3][^s5] LLM slot filling works only for top-level action inputs the model calls. It does not work for chained action inputs, which run deterministically.[^s3]

Variables are useful in three places: as action inputs, in `if` branches of instructions, and in `available when` filters on actions and subagents.[^s3] A filtered action is removed from the LLM's view entirely. In the Trailhead resort-credit example, a Boolean `isCreditIssued` that starts as `False` hides the credit action once it has been set to `True`. Instruction text alone cannot guarantee that.[^s4]

From outside the agent, the Agent API can pass context and custom variables when a session starts or when a message is sent. In Agentforce Builder, a variable can be changed this way only if *Allow value to be set by API* is enabled. In Agent Script, that means `visibility: External`; the default is `Internal`, which lets only actions set the value.[^s2][^s1] Most context variables are read-only once the session starts. The exception is `$Context.EndUserLanguage`, and editable variables can be changed only in a send-message call.[^s2] In metadata, variables are stored as `ConversationVariable` (in BotVersion and BotTemplate) and `ConversationContextVariable` (in Bot and BotTemplate). They have data types including Text, Number, Boolean, Object, Date, DateTime, Currency and Id.[^s2]

## Limits and gotchas

- Variables last for a session and are cleared when the session ends. The Trailhead lesson recommends a flow-based check against records for rules that must hold across sessions.[^s4]
- Using too many variables as action inputs can make the agent choose actions inconsistently. Store an output only when a condition, input or deterministic step needs it.[^s3]
- Linked variables are read-only and cannot hold objects or lists. Copy a value into a custom mutable variable when you need to change it.[^s1]
- Use determinism only where it matters, such as access checks before disclosing data or hard business rules. Leave the rest of the conversation to the reasoning engine.[^s5]

## Connections

Agent variables are part of [[kt:agent-script]] and are configured in Agentforce Builder ([[kt:agentforce-studio]]) or deployed through [[kt:metadata-api]] as conversation variable metadata.[^s1][^s2] They connect [[kt:agent-actions]], because outputs feed variables and variables feed inputs. They are also shared state across [[kt:agentforce-subagents]], which the blog describes as shared memory for multi-agent orchestration.[^s3][^s5] External systems set them through the [[kt:agent-api]].[^s2] Filters built on variables hide actions from the [[kt:atlas-reasoning-engine]]. That helps against [[kt:prompt-injection]], because a user cannot talk the model into calling an action it cannot see.[^s4]

## Sources

[^s1]: Salesforce Developers, "Agent Script Reference: Variables (Custom and Linked)". https://developer.salesforce.com/docs/ai/agentforce/guide/ascript-ref-variables.html (accessed 2026-11-26)
[^s2]: Salesforce Developers, "Send Agent Variables with the Agent API". https://developer.salesforce.com/docs/ai/agentforce/guide/agent-api-variables.html (accessed 2026-11-26)
[^s3]: Salesforce Developers, "Agent Script Pattern: Using Variables Effectively". https://developer.salesforce.com/docs/ai/agentforce/guide/ascript-patterns-variables.html (accessed 2026-11-26)
[^s4]: Trailhead, "Enforce Business Rules with Action Filters and Variables". https://trailhead.salesforce.com/content/learn/modules/programmatic-instructions-in-agentforce/enforce-business-rules-with-variables-and-action-filters (accessed 2026-11-26)
[^s5]: Olfa Kharrat, "Agentforce Variables: A New Way to Structure Agent Memory", Salesforce Developers Blog, 2025-04-17. https://developer.salesforce.com/blogs/2025/04/agentforce-variables-a-new-way-to-structure-agent-memory (accessed 2026-11-26)
