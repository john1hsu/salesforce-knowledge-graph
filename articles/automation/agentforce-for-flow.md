---
id: kt:agentforce-for-flow
type: Feature
title: Agentforce for Flow
aliases: [Einstein for Flow, Drafting Flows with Agentforce, Let Einstein Help You Build, Draft with AI, A4F, AI flow generation]
domain: automation
summary: >-
  The generative AI built into Flow Builder (formerly Einstein for Flow) that drafts a starter flow from a
  natural-language description, summarizes existing flows and, through the Flow Builder Agentforce panel, applies
  prompted changes to a flow that the builder then reviews, accepts or rejects.
release: "Winter '27"
status: current
broader: [kt:flow-builder, kt:agentforce]
related: [kt:screen-flow, kt:record-triggered-flow, kt:schedule-triggered-flow, kt:flow-tests, kt:agentforce-setup-agent]
relations:
  - {predicate: dependsOn, object: kt:data-cloud}
  - {predicate: dependsOn, object: kt:einstein-generative-ai-setup}
  - {predicate: configuredVia, object: kt:process-automation-settings}
  - {predicate: alternativeTo, object: kt:flow-templates}
sources:
  - id: s1
    title: "Drafting Flows with Agentforce (Beta)"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.flow_build_let_einstein_help_you_build_flows.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-24
  - id: s2
    title: "Jen's Top Spring '26 Features for Admins"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2026/jens-top-spring-26-features-for-admins
    type: official-blog
    accessed: 2026-11-24
  - id: s3
    title: "Einstein for Flow: Using Generative AI to Assist Your Flows"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2023/einstein-for-flow-for-salesforce-admins
    type: official-blog
    accessed: 2026-11-24
  - id: s4
    title: "AI Flow Features Every Admin Should Use | Kate Clicks Through It"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2025/ai-flow-features-every-admin-should-use-kate-clicks-through-it
    type: official-blog
    accessed: 2026-11-24
  - id: s5
    title: "How Agentforce Achieved Accurate Flow Generation Across 461 Billion Monthly Executions Using a Constrained DSL"
    publisher: Salesforce Engineering Blog
    url: https://engineering.salesforce.com/?p=8081
    type: official-blog
    accessed: 2026-11-24
  - id: s6
    title: "From Flow Generalists to Champions: Building Agentic AI for Salesforce Automation"
    publisher: Salesforce AI Research
    url: https://www.salesforce.com/blog/agentic-ai-for-flow/
    type: official-blog
    accessed: 2026-11-24
  - id: s7
    title: "Jen's Top Winter '27 Release Features For Admins"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2026/jens-top-winter-27-release-features-for-admins
    type: official-blog
    accessed: 2026-11-24
created: 2026-11-24
---

# Agentforce for Flow

Agentforce for Flow is the generative AI layer inside Flow Builder. A builder describes the automation in plain language and Agentforce drafts a flow to start from, which the builder then refines, tests and activates like any hand-built flow.[^s1][^s2] It began life as **Einstein for Flow**, which Salesforce's admin team described in late 2025 as soon to be renamed Agentforce for Flow.[^s4] The Spring '26 release made what Salesforce called a new and improved version generally available under the Agentforce name.[^s2]

## What it does

The feature has grown from one capability into three:

- **Draft a flow from a prompt.** From Let AI Help You Build, the builder chooses Draft with AI and describes the flow; record-triggered, scheduled and screen flows are supported.[^s2]
- **Summarize a flow.** Agentforce writes a plain-language summary of an existing flow, which can be saved into the flow's description.[^s1][^s4]
- **Evolve an existing flow.** Since Spring '26, the builder opens the Agentforce panel on a flow and asks for changes such as adding a Decision, removing a Loop or adding a fault path; each proposed change is shown for the builder to accept or reject.[^s2]

The original beta was narrower. As of Summer '24, Einstein for Flow generated starter flows of roughly four to six elements using basic formulas, Decision elements, loops, collections and Get, Create and Update Records, across screen, record-triggered, schedule-triggered and autolaunched flows.[^s3] The Spring '26 admin guide gave an example prompt for a ten-element screen flow with a decision and a case-creation action, a sign of how far the scope has widened.[^s2]

## How it works

Salesforce's engineering team describes the generator as an LLM pipeline that turns plain-language instructions into Flow metadata. It moved away from fine-tuned models toward a constrained, multi-level domain-specific language: an "Architect" phase plans the flow's structure and a "Developer" phase emits the detailed metadata, with validation at each stage.[^s5] The DSL is generated from the Flow metadata WSDL, so it follows schema changes each release, and the pipeline calls org APIs at generation time to resolve org-specific details such as objects and fields.[^s5] The team reports coverage of more than 63 flow varieties and scores output on whether it saves, whether it is ready to activate and whether it matches the user's intent.[^s5]

Salesforce AI Research's earlier work on the same product used "ready-to-activate" as its main metric. It reported that many generated flows on a hard test set were not activation-ready, though most could be activated after only a few human edits.[^s6] The original Einstein for Flow beta was built on Salesforce AI Research's CodeGen model.[^s3]

## Setup and licensing

Salesforce Help lists these prerequisites for drafting: turn on Einstein generative AI, confirm Data 360 is provisioned and enabled, and select the Agentforce flow automation option in Process Automation Settings.[^s1] The Spring '26 notes name the eligible editions: Essentials, Pro Suite, Professional, Enterprise, Performance, Unlimited and Developer with Foundations or Agentforce 1 Editions. Drafting does not consume generative AI credits.[^s2] The Flow Builder Agentforce panel needs no extra admin configuration once Agentforce is enabled, but it depends on an Agentforce employee-agent org permission.[^s2] Help also states that the account is opted out of the global data model by default.[^s1]

## Limits and gotchas

- **Review every draft.** Salesforce has advised from the start that AI-generated flows be reviewed before testing or activation.[^s3] Research results confirm that generated flows often need a few edits before they are ready to activate.[^s6]
- **Labels lag the product.** The Spring '26 admin notes call drafting GA, while the Help page for drafting still carries a Beta label. Check the edition and terms that apply to your org.[^s1][^s2]
- **Not the Setup agent.** Setup with Agentforce, a separate beta in Setup, can also create flows and explain formulas, but it needs its own permissions and runs outside Flow Builder.[^s2]
- **Headless use is separate.** Winter '27 adds headless Agentforce for Flow tooling used from AI coding terminals, for example to propose and build flow test scenarios. Its permission-set requirements differ from the in-builder panel.[^s7]

## When to use it (and when not)

Use Agentforce for Flow to get past a blank canvas, to explain an inherited flow, or to make routine structural edits quickly. For a repeatable, vetted starting point, a flow template is the deterministic alternative. For complex or high-volume automation, treat the draft as scaffolding and apply the same bulkification, fault-handling and test discipline as for any flow.[^s3][^s5]

## Connections

Agentforce for Flow is part of Flow Builder (`kt:flow-builder`) and one of the Agentforce (`kt:agentforce`) capabilities.[^s2] It drafts screen (`kt:screen-flow`), record-triggered (`kt:record-triggered-flow`) and scheduled (`kt:schedule-triggered-flow`) flows.[^s2] It depends on Data 360 (`kt:data-cloud`) and on Einstein generative AI setup (`kt:einstein-generative-ai-setup`), and it is switched on through Process Automation Settings (`kt:process-automation-settings`).[^s1] Flow templates (`kt:flow-templates`) are the non-AI alternative for a head start. Flow tests (`kt:flow-tests`) are where Winter '27's headless tooling generates scenarios.[^s7] The Agentforce Setup agent (`kt:agentforce-setup-agent`) is a separate assistant that can also create flows from Setup.[^s2]

## Sources
[^s1]: Salesforce Help, "Drafting Flows with Agentforce (Beta)". https://help.salesforce.com/s/articleView?id=sf.flow_build_let_einstein_help_you_build_flows.htm&language=en_US&type=5 (accessed 2026-11-24)
[^s2]: Salesforce Admins Blog, "Jen's Top Spring '26 Features for Admins". https://admin.salesforce.com/blog/2026/jens-top-spring-26-features-for-admins (accessed 2026-11-24)
[^s3]: Salesforce Admins Blog, "Einstein for Flow: Using Generative AI to Assist Your Flows". https://admin.salesforce.com/blog/2023/einstein-for-flow-for-salesforce-admins (accessed 2026-11-24)
[^s4]: Salesforce Admins Blog, "AI Flow Features Every Admin Should Use | Kate Clicks Through It". https://admin.salesforce.com/blog/2025/ai-flow-features-every-admin-should-use-kate-clicks-through-it (accessed 2026-11-24)
[^s5]: Salesforce Engineering Blog, "How Agentforce Achieved Accurate Flow Generation Across 461 Billion Monthly Executions Using a Constrained DSL". https://engineering.salesforce.com/?p=8081 (accessed 2026-11-24)
[^s6]: Salesforce AI Research, "From Flow Generalists to Champions: Building Agentic AI for Salesforce Automation". https://www.salesforce.com/blog/agentic-ai-for-flow/ (accessed 2026-11-24)
[^s7]: Salesforce Admins Blog, "Jen's Top Winter '27 Release Features For Admins". https://admin.salesforce.com/blog/2026/jens-top-winter-27-release-features-for-admins (accessed 2026-11-24)
