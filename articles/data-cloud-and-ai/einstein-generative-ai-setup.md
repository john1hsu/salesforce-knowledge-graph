---
id: kt:einstein-generative-ai-setup
type: Feature
title: Einstein Generative AI Setup
aliases: [Einstein Setup, Turn on Einstein, Turn On Einstein Generative AI, Set Up Einstein Generative AI and Agentforce, enableEinsteinGptPlatform]
domain: data-cloud-and-ai
summary: >-
  The org-level switch and setup sequence that turns on Einstein generative AI in Salesforce: provision Data 360,
  enable "Turn on Einstein" on the Einstein Setup page, configure the Einstein Trust Layer, then add agents; it is the
  prerequisite for Prompt Builder, the Models API, Agentforce agents and AI-assisted setup tools.
release: "Winter '27"
status: current
broader: [kt:agentforce]
related: [kt:prompt-builder, kt:agentforce-setup-agent, kt:agentforce-for-flow, kt:scratch-orgs]
relations:
  - {predicate: dependsOn, object: kt:data-cloud}
  - {predicate: enables, object: kt:einstein-trust-layer}
  - {predicate: enables, object: kt:models-api}
  - {predicate: configuredVia, object: kt:metadata-api}
sources:
  - id: s1
    title: "Set Up Einstein Generative AI and Agentforce"
    publisher: Salesforce Developers (Agentforce Developer Guide)
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/org-setup.html
    type: official-docs
    accessed: 2026-11-24
  - id: s2
    title: "Create an Agentforce-Ready Scratch Org With Salesforce CLI"
    publisher: Salesforce Developers (Agentforce Developer Guide)
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/scratch-org.html
    type: official-docs
    accessed: 2026-11-24
  - id: s3
    title: "Setting Up Your Org for Models API Access (Get Started with the Models API)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/get-started-with-einstein-models-api/prepare-your-org-to-access-the-models-api
    type: official-learning
    accessed: 2026-11-24
  - id: s4
    title: "Configure LLM Data Masking Policies in Einstein AI"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/llm-data-masking-in-the-einstein-trust-layer/configure-llm-data-masking-policies
    type: official-learning
    accessed: 2026-11-24
  - id: s5
    title: "Configure Your Service Assistant for Success (Agentforce Service Assistant)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agentforce-service-assistant/set-up-service-assistant
    type: official-learning
    accessed: 2026-11-24
created: 2026-11-24
---

# Einstein Generative AI Setup

Einstein generative AI setup is the one-time, org-level enablement that every generative AI feature in Salesforce sits on top of. Salesforce's developer guide describes it as a short, ordered sequence: provision Data 360, turn on Einstein, configure the Einstein Trust Layer, and, only if you use agents, set up Agentforce agents.[^s1] Until the org-level switch is on, features such as Prompt Builder, the Models API and generative features inside the clouds have nothing to run on.[^s3][^s4]

## How it works

The sequence starts with Data 360 (formerly Data Cloud). The guide says Data 360 must be provisioned and set up before you turn on Einstein generative AI features, because the Einstein Trust Layer depends on it to work correctly.[^s1] Trailhead says the same thing: without Data 360 you can't see or check the Trust Layer settings.[^s4]

The switch itself is on the **Einstein Setup** page. In Setup, search Quick Find for Einstein Setup and turn on the **Turn on Einstein** toggle.[^s1][^s3] This is the check Trailhead challenges run when they verify an org is AI-ready. The Models API module says its challenge only looks at whether Einstein is enabled in Setup.[^s3]

With Einstein on, the same page links to the Trust Layer through **Go to Einstein Trust Layer**. That is where admins set LLM data masking and the sensitive-data categories to mask.[^s4] Trailhead says you must turn on Einstein generative AI before you can configure masking policies. It also notes that masking changes can take a couple of minutes to apply.[^s4] Feature setup pages often point back to the same switch. For example, Service Assistant setup has a "Turn On Einstein Generative AI" section that sends you to Einstein Setup and tells you to refresh the browser afterwards.[^s5]

## Scratch orgs and metadata

For source-driven development, you don't have to click through Setup. An Agentforce-ready scratch org definition adds the `Einstein1AIPlatform` feature. It also sets `einsteinGptSettings.enableEinsteinGptPlatform` and `agentPlatformSettings.enableAgentPlatform` to true, which turns on Einstein and Agentforce when the org is created.[^s2] Those settings belong to the `EinsteinGptSettings` and `AgentPlatformSettings` Metadata API types, so the enablement can be versioned alongside the rest of a project.[^s2]

## Limits and gotchas

- The scratch-org approach applies to Developer and Enterprise edition orgs, and the Dev Hub must hold the Data 360 licenses.[^s2]
- Salesforce recommends a sandbox rather than a scratch org when you need Data 360 or Agentforce Data Library features.[^s2]
- Order matters. If you turn on Einstein before Data 360 is provisioned, the Trust Layer can't work correctly.[^s1]
- Default masking doesn't catch everything. Trailhead notes that invalid card, SSN or phone values are not masked.[^s4]
- Turning on Einstein doesn't turn on each feature. Individual features such as sales emails or Service Assistant still have their own toggles and configuration.[^s4][^s5]

## When to use it (and when not)

Do this setup once per org, before any project that uses prompt templates, generative features in the clouds, the Models API or Agentforce agents.[^s1][^s3] For repeatable developer environments, prefer the scratch org definition settings over manual toggling. For work that depends on Data 360 data, use a sandbox, as Salesforce recommends.[^s2] Agent creation is a separate, later step. Orgs that only use prompt templates or masking don't need it.[^s1]

## Connections

This node is the foundation of the Agentforce (`kt:agentforce`) stack and depends on Data 360 (`kt:data-cloud`) being provisioned first.[^s1] It unlocks the Einstein Trust Layer (`kt:einstein-trust-layer`), whose masking settings are reached from the Einstein Setup page.[^s4] It also unlocks the Models API (`kt:models-api`), which Trailhead says works in any org with Einstein generative AI and Data 360 enabled.[^s3] Prompt Builder (`kt:prompt-builder`) appears under the Einstein Generative AI area of Setup once the switch is on.[^s4] Setup with Agentforce (`kt:agentforce-setup-agent`) and Agentforce for Flow (`kt:agentforce-for-flow`) both list this setup as a prerequisite. In scratch orgs (`kt:scratch-orgs`) it is enabled through Metadata API (`kt:metadata-api`) settings in the definition file.[^s2]

## Sources
[^s1]: Salesforce Developers, "Set Up Einstein Generative AI and Agentforce". https://developer.salesforce.com/docs/ai/agentforce/guide/org-setup.html (accessed 2026-11-24)
[^s2]: Salesforce Developers, "Create an Agentforce-Ready Scratch Org With Salesforce CLI". https://developer.salesforce.com/docs/ai/agentforce/guide/scratch-org.html (accessed 2026-11-24)
[^s3]: Trailhead, "Setting Up Your Org for Models API Access". https://trailhead.salesforce.com/content/learn/modules/get-started-with-einstein-models-api/prepare-your-org-to-access-the-models-api (accessed 2026-11-24)
[^s4]: Trailhead, "Configure LLM Data Masking Policies in Einstein AI". https://trailhead.salesforce.com/content/learn/modules/llm-data-masking-in-the-einstein-trust-layer/configure-llm-data-masking-policies (accessed 2026-11-24)
[^s5]: Trailhead, "Configure Your Service Assistant for Success". https://trailhead.salesforce.com/content/learn/modules/agentforce-service-assistant/set-up-service-assistant (accessed 2026-11-24)
