---
id: kt:einstein-bots
type: Feature
title: Einstein Bots
aliases: [Einstein Bot, Einstein Enhanced Bots, enhanced bots, standard bots, Service Cloud chatbots, Bot Builder]
domain: data-cloud-and-ai
summary: >-
  Service Cloud's rule-based conversational bots, built in Bot Builder from dialogs, intents, entities and variables,
  that greet customers on messaging channels, run scripted transactions and hand off to human agents or Agentforce
  agents through Omni-Channel.
release: "Winter '27"
status: current
broader: [kt:service-cloud]
related: [kt:agentforce, kt:omni-channel, kt:knowledge-base, kt:flow-builder, kt:messaging-for-in-app-and-web]
relations:
  - {predicate: partOf, object: kt:service-cloud}
  - {predicate: requiresLicense, object: kt:service-cloud}
  - {predicate: alternativeTo, object: kt:agentforce}
  - {predicate: integratesWith, object: kt:omni-channel}
  - {predicate: dependsOn, object: kt:messaging-for-in-app-and-web}
  - {predicate: integratesWith, object: kt:flow-builder}
sources:
  - id: s1
    title: "Einstein Chatbot Benefits & Planning (Einstein Bots Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/service_bots_basics/learn-about-einstein-bots
    type: official-learning
    accessed: 2026-11-28
  - id: s2
    title: "Learn Chatbot Prerequisites & Enable Bots (Einstein Bots Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/service_bots_basics/enable-einstein-bots
    type: official-learning
    accessed: 2026-11-28
  - id: s3
    title: "Plan Chatbot Content (Einstein Bots Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/service_bots_basics/plan-your-bot-content
    type: official-learning
    accessed: 2026-11-28
  - id: s4
    title: "Build and Implement Your Bot (Einstein Bots Project Planning)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/einstein-bots-project-planning/build-and-implement-your-bot
    type: official-learning
    accessed: 2026-11-28
  - id: s5
    title: "The Seamless Handoff: Integrating Einstein Enhanced Bots with Agentforce Agents"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2025/12/the-seamless-handoff-integrating-einstein-enhanced-bots-with-agentforce-agents
    type: official-blog
    accessed: 2026-11-28
  - id: s6
    title: "Bots to Agents: Your Step by Step Guide (webinar)"
    publisher: Salesforce
    url: https://www.salesforce.com/eu/events/webinars/agentforce-bots-to-agents
    type: official-blog
    accessed: 2026-11-28
created: 2026-11-28
---

# Einstein Bots

Einstein Bots are Service Cloud's chatbots: applications that simulate a human conversation over text so customers can get routine help without waiting for an agent. Salesforce positions a bot as one more service channel alongside phone, email, text and social, with benefits such as case deflection, shorter wait times and quick redirects to the right person.[^s1] Unlike Agentforce agents, bots are not driven by a large language model; Trailhead notes that they rely on strictly defined conversational rules and take considerable expertise and time to set up, whereas Agentforce reasons over instructions with far less configuration.[^s1]

## How it works

A bot is assembled in Bot Builder from a few building blocks.[^s3]

- **Dialogs** are conversation snippets that define what the bot can do, such as Welcome, Main Menu, Order Status and Transfer to Agent.[^s3]
- **Dialog intents** capture why the customer is contacting the bot, usually as a verb phrase, and train the natural-language model.[^s3]
- **Entities** describe data to collect; system entities include Text, Date, Number, Money, Boolean and Object, and custom entities are allowed.[^s3]
- **Variables** hold collected values; each is tied to an entity and can be passed into and out of dialogs or inserted into messages.[^s3]

Natural-language understanding is optional. A purely menu-driven bot can still answer order-status or store-hours questions, and Salesforce's planning guidance suggests launching menu-first and adding NLP later.[^s1][^s4] To train intents, Bot Builder needs three to five intents with at least 20 utterances each to get started, and more balanced, unique utterances improve accuracy; Model Management and Bot Training data help tune the model afterwards.[^s4] Actions let a dialog call a flow or Apex, for example to create a case or update a record, and variables such as a case number enable object searches; variable names must match between Flow and Bot Builder.[^s4]

## Setup and prerequisites

Trailhead lists three prerequisites: a Service Cloud license, Salesforce Sites, and Messaging for In-App and Web, which places the chat window on a website or mobile app.[^s2] An admin turns on Einstein Bots in Setup, creates a bot from the wizard (for example a Standard Bot from the Intro Template), edits it in Bot Builder and activates it.[^s2] Bots can draw answers from Lightning or Classic Knowledge.[^s1]

## Enhanced bots and Agentforce handoff

Enhanced bots run on the Messaging for In-App and Web channel and route through Omni-Channel. A December 2025 Salesforce Developers post describes a hybrid design: the enhanced bot handles entry, spam filtering and deterministic transactions such as logging a case or checking status, then hands complex, open-ended questions to an Agentforce Service agent.[^s5] The handoff writes context to a custom field on the Messaging Session record through a flow, then the Transfer To Agent system dialog invokes an outbound Omni-Channel flow (set on the Bot Overview page) whose Route Work action picks the right agent, queue or skill, with a fallback queue.[^s5] The post argues that keeping routine traffic on the bot lowers Agentforce consumption costs and keeps strict process adherence where it matters.[^s5]

## Limits and gotchas

- Design every bot with an exit: guidance calls for a persistent menu option to reach a human agent and to end the chat, and for the greeting to say the customer is talking to a bot.[^s3]
- A bot must know where to redirect customers it cannot help, so routing and queues should be in place before the bot is built.[^s1]
- Rule-based dialogs grow brittle as use cases multiply; Salesforce now runs migration guidance and a self-service migration tool for moving bot use cases to Agentforce.[^s6]

## When to use it (and when not)

Use Einstein Bots for high-volume, predictable transactions where low latency, fixed wording and compliance matter more than flexibility.[^s5] For open-ended questions, multi-step reasoning or grounding in many knowledge sources, an Agentforce Service agent is the better fit, and Salesforce's own messaging frames bots as reaching their limits in task complexity and reasoning.[^s6] Many orgs combine the two rather than choosing one.[^s5]

## Connections

Einstein Bots are part of Service Cloud and require its license.[^s2] They depend on Messaging for In-App and Web as their channel and on Omni-Channel for routing transfers.[^s2][^s5] Actions call into Flow Builder flows or Apex, answers can come from the Knowledge Base, and Agentforce is both their LLM-based alternative and, in hybrid designs, the escalation target.[^s1][^s4][^s5]

## Sources
[^s1]: Trailhead, "Einstein Chatbot Benefits & Planning". https://trailhead.salesforce.com/content/learn/modules/service_bots_basics/learn-about-einstein-bots (accessed 2026-11-28)
[^s2]: Trailhead, "Learn Chatbot Prerequisites & Enable Bots". https://trailhead.salesforce.com/content/learn/modules/service_bots_basics/enable-einstein-bots (accessed 2026-11-28)
[^s3]: Trailhead, "Plan Chatbot Content". https://trailhead.salesforce.com/content/learn/modules/service_bots_basics/plan-your-bot-content (accessed 2026-11-28)
[^s4]: Trailhead, "Build and Implement Your Bot". https://trailhead.salesforce.com/content/learn/modules/einstein-bots-project-planning/build-and-implement-your-bot (accessed 2026-11-28)
[^s5]: Salesforce Developers Blog, "The Seamless Handoff: Integrating Einstein Enhanced Bots with Agentforce Agents" (2025-12-09). https://developer.salesforce.com/blogs/2025/12/the-seamless-handoff-integrating-einstein-enhanced-bots-with-agentforce-agents (accessed 2026-11-28)
[^s6]: Salesforce, "Bots to Agents: Your Step by Step Guide". https://www.salesforce.com/eu/events/webinars/agentforce-bots-to-agents (accessed 2026-11-28)
