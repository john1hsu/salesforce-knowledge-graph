---
id: kt:agentforce-vibes-ide
type: Tool
title: Agentforce Vibes IDE
aliases: [Code Builder, Salesforce Code Builder, web-based VS Code for Salesforce, browser IDE for Salesforce]
domain: devops-and-alm
summary: >-
  Salesforce's browser-based development environment, formerly Code Builder: a cloud-hosted Visual Studio Code
  launched from Setup that bundles Salesforce Extensions, Salesforce CLI, GitHub integration and the Agentforce
  Vibes AI extension, and loads the org's metadata into a Salesforce DX project with no local install.
release: "Winter '27"
status: current
broader: [kt:salesforce-dx]
related: [kt:scratch-orgs, kt:sandbox-types, kt:devops-center, kt:agentforce-dx, kt:apex, kt:lightning-web-components]
relations:
  - {predicate: dependsOn, object: kt:salesforce-extensions-for-vs-code}
  - {predicate: dependsOn, object: kt:salesforce-cli}
  - {predicate: alternativeTo, object: kt:salesforce-extensions-for-vs-code}
  - {predicate: integratesWith, object: kt:agentforce-vibes}
  - {predicate: integratesWith, object: kt:code-analyzer}
sources:
  - id: s1
    title: "Agentforce Vibes IDE Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/code-builder/guide
    type: official-docs
    accessed: 2026-11-16
  - id: s2
    title: "Enable Agentforce Vibes IDE"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/code-builder/guide/codebuilder-enable-install.html
    type: official-docs
    accessed: 2026-11-16
  - id: s3
    title: "Supported Editions (Agentforce Vibes IDE)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/code-builder/guide/codebuilder-supported-editions.html
    type: official-docs
    accessed: 2026-11-16
  - id: s4
    title: "Web Versus Desktop (Agentforce Vibes IDE)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/code-builder/guide/codebuilder-differences.html
    type: official-docs
    accessed: 2026-11-16
  - id: s5
    title: "Known Issues and FAQ (Agentforce Vibes IDE)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/code-builder/guide/codebuilder-known-issues.html
    type: official-docs
    accessed: 2026-11-16
  - id: s6
    title: "Set Up Agentforce Vibes IDE (Agentforce Vibes IDE Fundamentals)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agentforce-vibes-ide-fundamentals/set-up-agentforce-vibes-ide
    type: official-learning
    accessed: 2026-11-16
  - id: s7
    title: "New Developer Edition with Agentforce Vibes, Claude and MCP"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2026/04/new-developer-edition-agentforce-vibes-claude-mcp
    type: official-blog
    accessed: 2026-11-16
created: 2026-11-16
---

# Agentforce Vibes IDE

Agentforce Vibes IDE is Salesforce's web-based development environment. It runs Visual Studio Code in the browser and ships with Salesforce Extensions, Salesforce CLI and GitHub integration, so developers can build on the platform without installing anything locally.[^s1] Salesforce previously sold it as **Code Builder**, and its documentation still lives under `code-builder` URLs.[^s7][^s1] It covers Apex, SOQL, Visualforce and Lightning Web Components, and can deploy to and test against scratch orgs, sandboxes and Developer Edition orgs.[^s1]

## How it works

An admin enables the IDE once per org, then developers open it from Setup. Launched that way it is org-aware: it signs in to the org automatically and loads the org's metadata into a Salesforce DX project.[^s1][^s4] On first launch it creates an empty DX project. Developers can add more projects from the sidebar or with **SFDX: Create Project**, and the IDE can manage several DX projects.[^s6] The org you launched from becomes the default org. Other orgs are added with the usual **SFDX: Authorize an Org** or **SFDX: Create a Default Scratch Org** commands, and the status bar shows the connected org.[^s6] New projects include a `.gitignore`, Prettier settings and `.vscode` files for the Replay Debugger. Deploy-on-save exists in `settings.json` but is off by default.[^s6]

The **Agentforce Vibes** extension comes preinstalled and adds an agentic chat that uses MCP tools.[^s1][^s4] The extension has two modes. Plan mode reads the org and drafts an implementation plan, and Act mode writes Apex, LWCs, triggers and tests. It edits local project files for review and deploys nothing unless asked.[^s7]

## Enabling and access

- **Who enables it.** Only a System Administrator can turn it on: open Agentforce Vibes in Setup and accept the terms.[^s2]
- **Shared terms.** That one agreement also covers DevOps Center, DX Inspector and Scale Center.[^s2]
- **Prerequisites.** The org needs API access, and Professional Edition needs the API add-on.[^s2][^s3]
- **Who can use it.** After enablement, any user with the View All Data permission can open the IDE. Standard users cannot enable it themselves.[^s2][^s6]
- **Where it runs.** It is supported in Developer Edition orgs and sandboxes (Lightning Experience), in Enterprise, Unlimited and Professional editions.[^s3]
- **Scratch orgs.** Scratch orgs of those editions are supported. Developer Edition scratch orgs need the `AgentforceVibesIDEForDE` feature.[^s3]
- **Developer Edition.** Since TDX in April 2026, every Developer Edition org gets the IDE and the Vibes extension at no cost.[^s7]

## Limits and gotchas

- **Not everywhere.** The IDE is not available in Government Cloud or in the EU Operating Zone. Other EU orgs are supported under standard terms.[^s3]
- **Hosting.** Each user gets a separate, isolated instance on AWS that only that user can access. Data is encrypted at rest and in transit.[^s5]
- **Instance lifetime.** Resetting an instance destroys its data immediately. An instance inactive for 30 days is deleted along with its data, so commit work to source control.[^s5]
- **Marketplace.** The IDE cannot reach the Microsoft VS Code Marketplace. Extensions come from Open VSX, so some desktop extensions may be missing.[^s4]
- **Updates and auth.** Salesforce keeps the bundled extensions up to date. Third-party authorization flows work differently than on the desktop.[^s4]
- **AI usage caps.** In Developer Edition, the Vibes extension defaulted to Claude Sonnet 4.5 with 110 requests and 1.5 million tokens a month. Monthly refreshes ran to May 31, 2026, followed by one non-refreshing allocation.[^s7]

## When to use it (and when not)

Choose the IDE for zero-install onboarding, locked-down laptops, workshops, or quick fixes in a sandbox, where launching from Setup removes CLI installs and org authorization.[^s4][^s6] Choose desktop VS Code with Salesforce Extensions when developers need Microsoft Marketplace extensions or their own toolchain, or keep long-lived local state that should not depend on a cloud instance surviving 30 days of inactivity.[^s4][^s5] Teams in Government Cloud or the EU Operating Zone must use the desktop route.[^s3]

## Connections

The IDE is a hosted delivery of **Salesforce DX** (broader). It **depends on** the **Salesforce Extensions for VS Code** and **Salesforce CLI** that it bundles, and is the browser **alternative to** installing those extensions on a desktop.[^s1][^s4] It **integrates with** the **Agentforce Vibes** extension for agentic coding, which in turn works with **Code Analyzer** and **DevOps Center**.[^s7] Its terms are shared with **DevOps Center**.[^s2] It deploys to **scratch orgs**, **sandboxes** and Developer Edition orgs, and edits **Apex** and **Lightning Web Components**.[^s1] It sits alongside **Agentforce DX**, the pro-code toolset for building agents in the same DX projects.[^s7]

## Sources
[^s1]: Salesforce Developers, "Agentforce Vibes IDE Developer Guide". https://developer.salesforce.com/docs/platform/code-builder/guide (accessed 2026-11-16)
[^s2]: Salesforce Developers, "Enable Agentforce Vibes IDE". https://developer.salesforce.com/docs/platform/code-builder/guide/codebuilder-enable-install.html (accessed 2026-11-16)
[^s3]: Salesforce Developers, "Supported Editions (Agentforce Vibes IDE)". https://developer.salesforce.com/docs/platform/code-builder/guide/codebuilder-supported-editions.html (accessed 2026-11-16)
[^s4]: Salesforce Developers, "Web Versus Desktop (Agentforce Vibes IDE)". https://developer.salesforce.com/docs/platform/code-builder/guide/codebuilder-differences.html (accessed 2026-11-16)
[^s5]: Salesforce Developers, "Known Issues and FAQ (Agentforce Vibes IDE)". https://developer.salesforce.com/docs/platform/code-builder/guide/codebuilder-known-issues.html (accessed 2026-11-16)
[^s6]: Trailhead, "Set Up Agentforce Vibes IDE". https://trailhead.salesforce.com/content/learn/modules/agentforce-vibes-ide-fundamentals/set-up-agentforce-vibes-ide (accessed 2026-11-16)
[^s7]: Salesforce Developers Blog, "New Developer Edition with Agentforce Vibes, Claude and MCP". https://developer.salesforce.com/blogs/2026/04/new-developer-edition-agentforce-vibes-claude-mcp (accessed 2026-11-16)
