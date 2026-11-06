---
id: kt:agentforce-dx
type: Tool
title: Agentforce DX
aliases: [Agentforce DX pro-code tools, Salesforce CLI agent plugin, plugin-agent, Agentforce DX VS Code extension]
domain: devops-and-alm
summary: >-
  The pro-code toolset that extends Salesforce DX to Agentforce agents: a Salesforce CLI plugin and a VS Code
  extension for authoring Agent Script bundles, previewing, testing, publishing, activating and syncing agents as
  source-controlled metadata.
release: "Winter '27"
status: current
broader: [kt:salesforce-dx, kt:agentforce]
related: [kt:agent-development-lifecycle, kt:agentforce-testing-center, kt:scratch-orgs, kt:source-tracking]
relations:
  - {predicate: dependsOn, object: kt:salesforce-cli}
  - {predicate: dependsOn, object: kt:metadata-api}
  - {predicate: implements, object: kt:agent-script}
  - {predicate: alternativeTo, object: kt:agentforce-studio}
sources:
  - id: s1
    title: "Build Agents with Agentforce DX"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/agent-dx.html
    type: official-docs
    accessed: 2026-11-06
  - id: s2
    title: "Synchronize Your Development Org with Your DX Project"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/agent-dx-synch.html
    type: official-docs
    accessed: 2026-11-06
  - id: s3
    title: "Manage an Agent with Agentforce DX"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/agent-dx-manage.html
    type: official-docs
    accessed: 2026-11-06
  - id: s4
    title: "Test an Agent with Agentforce DX"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/agent-dx-test.html
    type: official-docs
    accessed: 2026-11-06
  - id: s5
    title: "Get Started with Agentforce DX (Create an Agent Using Pro-Code Tools)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/create-an-agent-using-pro-code-tools/get-started-with-agentforce-dx
    type: official-learning
    accessed: 2026-11-06
  - id: s6
    title: "Introducing Agentforce DX Pro-Code Tools"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2025/05/introducing-agentforce-dx-pro-code-tools
    type: official-blog
    accessed: 2026-11-06
created: 2026-11-06
---

# Agentforce DX

Agentforce DX is the pro-code side of building Agentforce agents. It takes the Salesforce DX model, where a local project in version control is the source of truth, and extends it to agents, so an agent's definition can be authored, reviewed, deployed and promoted like any other metadata.[^s1] The tools reached general availability in May 2025 as a Salesforce CLI plugin plus a VS Code and Code Builder extension, and Salesforce aimed them at developers who already know Salesforce metadata rather than low-code builders.[^s6]

## What it consists of

- **CLI plugin.** The `plugin-agent` plugin adds the `sf agent` command family to Salesforce CLI; `sf plugins inspect agent` shows its version.[^s5] Running `sf update` and then any agent command installs it if missing.[^s6]
- **VS Code extensions.** The Agentforce DX extension previews and tests agents and moves agent metadata between the project and orgs. The companion Agentforce Vibes extension helps write supporting Apex. Both ship with the Salesforce Extension Pack.[^s1][^s5]
- **Release cadence.** Salesforce CLI and its core plugins release weekly, so agent commands change faster than the three seasonal platform releases. Check the CLI release notes rather than the platform notes for new flags.[^s1]

## How it works

The development loop centres on an **authoring bundle** (metadata type `AiAuthoringBundle`) that holds the agent's Agent Script file, the blueprint for its subagents, instructions and actions.[^s1][^s2] A developer generates the bundle, edits the script, and checks it with `sf agent validate authoring-bundle`.[^s5] The agent can be previewed in simulated or live mode from VS Code, the CLI or Agentforce Builder.[^s1] Custom actions are ordinary Apex classes and autolaunched flows developed alongside the script.[^s1]

Publishing (`sf agent publish authoring-bundle`) pushes the bundle to the org and produces the runnable agent metadata, namely `Bot`, `BotVersion` and `GenAiPlannerBundle`.[^s5][^s2] Publishing does not make the agent live. `sf agent activate` does that, prompting for a version when there is more than one unless `--api-name` and `--version` are passed, and `sf agent deactivate` takes it offline again. `sf org open agent` jumps to the agent in Agentforce Builder.[^s3]

Syncing uses the standard `sf project retrieve start` and `sf project deploy start` commands. For orgs without source tracking you name what to move, either the bundle (`AiAuthoringBundle:<name>`) or the pseudo type `Agent:<name>`, which expands to all of the agent's component metadata.[^s2]

Testing follows a spec-first flow: `sf agent generate test-spec` writes a YAML file of test cases. `sf agent test create` turns it into a test in the org and syncs the related metadata back to the project. `sf agent test run` executes it, and the results can feed a CI pipeline to catch regressions.[^s4] Salesforce chose YAML for these artefacts because it is readable and diffs well in source control.[^s6]

## Limits and gotchas

- `Agent:` is not a real metadata type. Retrieving it also pulls the Apex and flows behind the agent's actions, but deploying or deleting it leaves that Apex and those flows untouched.[^s2]
- Deleting an `AiAuthoringBundle` also removes its `Bot`, `BotVersion` and `GenAiPlannerBundle`. Use a wildcard such as `MyAgent*` to target every version of a bundle, and `sf project deploy preview` / `retrieve preview` to see changes first.[^s2]
- Deactivating an agent ends its open conversations and makes it unreachable on every channel, so treat it as a production change.[^s3]
- The CLI test commands map to the legacy Testing Center flow. They do not cover the New Testing Center in Agentforce Studio, which is in beta.[^s4]

## When to use it

Use Agentforce DX when agents must live in Git, go through code review and move through scratch orgs, sandboxes and CI like the rest of the codebase. It also suits agents whose actions are heavy on Apex, because preview and debugging stay in the IDE.[^s1][^s6] Agentforce Builder in the browser remains the faster choice for admins and low-code teams, and the two approaches share the same authoring bundle, so a published agent can be opened and edited in Builder.[^s1][^s6]

## Connections

Agentforce DX sits **under** `kt:salesforce-dx`, which it extends to agents, and `kt:agentforce`, whose agents it builds.[^s1] It **depends on** `kt:salesforce-cli`, which hosts the agent plugin, and on `kt:metadata-api` for retrieve and deploy.[^s5][^s2] It **implements** the `kt:agent-script` language in authoring bundles, and is the pro-code **alternative to** the browser-based `kt:agentforce-studio` builder.[^s1] It is **related** to `kt:agent-development-lifecycle`, whose build, test and deploy phases it automates, and to `kt:agentforce-testing-center`, whose legacy tests the CLI creates and runs.[^s4] It is also related to `kt:scratch-orgs` and `kt:source-tracking`, which determine how agent metadata syncs between org and project.[^s2]

## Sources

[^s1]: Salesforce Developers, "Build Agents with Agentforce DX". https://developer.salesforce.com/docs/ai/agentforce/guide/agent-dx.html (accessed 2026-11-06)
[^s2]: Salesforce Developers, "Synchronize Your Development Org with Your DX Project". https://developer.salesforce.com/docs/ai/agentforce/guide/agent-dx-synch.html (accessed 2026-11-06)
[^s3]: Salesforce Developers, "Manage an Agent with Agentforce DX". https://developer.salesforce.com/docs/ai/agentforce/guide/agent-dx-manage.html (accessed 2026-11-06)
[^s4]: Salesforce Developers, "Test an Agent with Agentforce DX". https://developer.salesforce.com/docs/ai/agentforce/guide/agent-dx-test.html (accessed 2026-11-06)
[^s5]: Trailhead, "Get Started with Agentforce DX". https://trailhead.salesforce.com/content/learn/projects/create-an-agent-using-pro-code-tools/get-started-with-agentforce-dx (accessed 2026-11-06)
[^s6]: Salesforce Developers Blog, "Introducing Agentforce DX Pro-Code Tools". https://developer.salesforce.com/blogs/2025/05/introducing-agentforce-dx-pro-code-tools (accessed 2026-11-06)
