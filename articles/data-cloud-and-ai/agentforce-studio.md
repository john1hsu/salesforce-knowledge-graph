---
id: kt:agentforce-studio
type: Tool
title: Agentforce Studio
aliases: [Agentforce Builder, new Agentforce Builder, Agentforce Studio app]
domain: data-cloud-and-ai
summary: >-
  The Lightning app (opened from the App Launcher) where Salesforce users build, test and monitor Agentforce
  agents: it hosts the new Agentforce Builder for Agent Script agents, prompt templates, data sources, model
  choice, Test Suites and observability tools.
release: "Winter '27"
status: current
broader: [kt:agentforce]
related: [kt:agent-script, kt:agent-development-lifecycle, kt:atlas-reasoning-engine, kt:agent-actions]
relations:
  - {predicate: partOf, object: kt:agentforce}
  - {predicate: hasPart, object: kt:prompt-builder}
  - {predicate: hasPart, object: kt:agentforce-testing-center}
  - {predicate: alternativeTo, object: kt:agentforce-dx}
  - {predicate: dependsOn, object: kt:data-cloud}
sources:
  - id: s1
    title: "Get to Know Agentforce Builder (Introduction to Agentforce Builder)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/introduction-to-agent-builder/get-to-know-agent-builder
    type: official-learning
    accessed: 2026-11-06
  - id: s2
    title: "Explore the New Agentforce Builder (New Agentforce Builder: Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/new-agentforce-builder-quick-look/explore-the-new-agentforce-builder
    type: official-learning
    accessed: 2026-11-06
  - id: s3
    title: "Explore Agent Testing Tools and Considerations"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agentforce-testing-tools-and-strategies/explore-agent-testing-tools-and-considerations
    type: official-learning
    accessed: 2026-11-06
  - id: s4
    title: "Enhance Your Agents in the New Agentforce Builder"
    publisher: Salesforce
    url: https://www.salesforce.com/agentforce/agent-builder/migration/
    type: official-blog
    accessed: 2026-11-06
  - id: s5
    title: "Get Started with Agent Script"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/agent-script.html
    type: official-docs
    accessed: 2026-11-06
  - id: s6
    title: "Testing API Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/testing-api.html
    type: official-docs
    accessed: 2026-11-06
created: 2026-11-06
---

# Agentforce Studio

Agentforce Studio is the workspace in which Salesforce users build, test and monitor AI agents. It is a Lightning app found in the App Launcher; its Agents panel lists existing agents, and its **New Agent** button opens Agentforce Builder.[^s1] The redesigned Agentforce Builder lives inside Studio, so configuration, testing and monitoring happen in one place instead of across many Setup pages.[^s2][^s4]

## How it works

Studio is organized into two panes. **Build** is where you manage agents, launch Agentforce Test Suites, create or edit prompt templates, add data sources such as data libraries, retrievers and search indexes, and pick the AI models agents use. **Observe** collects agent analytics, agent insights and session data for reviewing how agents behave in production.[^s1]

Inside **Agentforce Builder**, an Explorer lists the agent's subagents, actions, variables and data sources. The default **Canvas** is a document-style editor that summarizes the agent's Agent Script as readable blocks, with inline actions such as if/else logic and a resource picker. A toggle switches to the code-based **Script** view, which offers syntax highlighting and real-time validation; edits in either view stay in sync.[^s2][^s5] A built-in Agentforce assistant converts natural-language requests into Agent Script and helps create, test, troubleshoot and refine an agent.[^s2] A new agent can start from a preconfigured template or from a plain-language description of its purpose, which seeds its subagents and actions.[^s1]

Agents are versioned. Work starts as an editable draft, and saving a draft does not make it live. **Commit Version** produces a locked snapshot that can be activated or used to start a new draft; only one version can be live at a time, so activating one deactivates the previous version.[^s2]

## Testing and observability

The **Preview** panel has two modes. **Simulate** checks configuration using mock data without enforcing permissions, running actions or changing data, while **Live Test** runs real actions and changes org data.[^s2][^s3] Previews show an interaction summary of the subagents, actions and reasoning behind each response, along with tracing, variable tracking and per-step timing.[^s2][^s3] **Agentforce Session Tracing** groups reasoning-engine runs, action calls, prompt and gateway inputs and outputs, and errors by session ID, and can also be used to review live conversations after launch.[^s3]

For batch evaluation, Studio's **Tests** tab hosts **Test Suites (Beta)**, which run dozens or hundreds of scenarios from an uploaded CSV or AI-generated inputs and report expected versus actual subagents, actions and responses with pass/fail results.[^s3] Programmatic testing goes through the Testing API, which also gives access to Agentforce Testing Center, or through the Agentforce DX command line and VS Code tools.[^s6]

## Limits and gotchas

- **Legacy builder cutoff.** Starting the week of July 13, 2026, new agents can be created only in the new builder, and new voice agents can no longer be created in the legacy builder. Legacy agents keep running and stay editable, but Salesforce has no new features planned for the legacy builder.[^s4]
- **Upgrade behavior.** The in-Studio upgrade creates a draft in the new builder and leaves the legacy agent untouched. Activating the rebuilt agent automatically deactivates the legacy original.[^s4]
- **Permissions.** The legacy builder lives in Setup and needs admin-level permissions. Studio builders don't need admin-level access, though users still need Agentforce permissions.[^s4][^s1]
- **Data 360 dependency.** Session Tracing, and some other observability tools, require Data 360.[^s3][^s1]
- **Test with care.** Salesforce says to run Test Suites only in a sandbox, never in production, because tests can modify CRM data. They also consume billable generative AI requests or credits. Results are probabilistic, so each org has to set its own pass/fail baseline.[^s3]

## When to use it (and when not)

Studio is the default, low-code path for admins and builders who want to configure, preview and monitor agents in the browser. Teams that need source control, CI pipelines or local editing can instead retrieve the agent's Agent Script file into a Salesforce DX project and work on it with Agentforce DX and its VS Code extension.[^s5][^s6] Salesforce's migration guidance pairs the two: a UI-driven conversion in Studio closely mirrors the original agent, while the CLI path suits teams that want to redesign the agent from scratch.[^s4]

## Connections

Agentforce Studio is **part of** `kt:agentforce`, whose agents it builds and monitors.[^s1] It is where `kt:agent-script` is authored and where the graph-based `kt:atlas-reasoning-engine` runs during previews.[^s2] Its Build pane **has parts** `kt:prompt-builder`, through prompt templates, and agent testing, which links it to `kt:agentforce-testing-center`.[^s1][^s6] It is the click-based **alternative to** the pro-code `kt:agentforce-dx` tools,[^s5] and it **depends on** `kt:data-cloud` (Data 360) for session tracing.[^s3] Subagents assemble `kt:agent-actions`, and Studio's build, test and observe flow maps onto the `kt:agent-development-lifecycle`.[^s1][^s3]

## Sources
[^s1]: Trailhead, "Get to Know Agentforce Builder". https://trailhead.salesforce.com/content/learn/modules/introduction-to-agent-builder/get-to-know-agent-builder (accessed 2026-11-06)
[^s2]: Trailhead, "Explore the New Agentforce Builder". https://trailhead.salesforce.com/content/learn/modules/new-agentforce-builder-quick-look/explore-the-new-agentforce-builder (accessed 2026-11-06)
[^s3]: Trailhead, "Explore Agent Testing Tools and Considerations". https://trailhead.salesforce.com/content/learn/modules/agentforce-testing-tools-and-strategies/explore-agent-testing-tools-and-considerations (accessed 2026-11-06)
[^s4]: Salesforce, "Enhance Your Agents in the New Agentforce Builder". https://www.salesforce.com/agentforce/agent-builder/migration/ (accessed 2026-11-06)
[^s5]: Salesforce Developers, "Get Started with Agent Script". https://developer.salesforce.com/docs/ai/agentforce/guide/agent-script.html (accessed 2026-11-06)
[^s6]: Salesforce Developers, "Testing API Developer Guide". https://developer.salesforce.com/docs/ai/agentforce/guide/testing-api.html (accessed 2026-11-06)
