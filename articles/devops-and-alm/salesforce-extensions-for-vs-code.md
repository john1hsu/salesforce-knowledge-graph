---
id: kt:salesforce-extensions-for-vs-code
type: Tool
title: Salesforce Extensions for VS Code
aliases: [Salesforce Extensions for Visual Studio Code, Salesforce Extension Pack, salesforcedx-vscode, Salesforce VS Code extensions, Salesforce Extensions for Desktop]
domain: devops-and-alm
summary: >-
  Salesforce's open-source set of Visual Studio Code extensions, installed as the Salesforce Extension Pack, that
  add Apex, Lightning Web Components, Aura and Visualforce language support, org deploy and retrieve, SOQL Builder,
  testing and Apex debuggers on top of Salesforce CLI.
release: "Winter '27"
status: current
broader: [kt:salesforce-dx]
related: [kt:apex, kt:lightning-web-components, kt:source-tracking, kt:scratch-orgs]
relations:
  - {predicate: dependsOn, object: kt:salesforce-cli}
  - {predicate: consumedBy, object: kt:agentforce-vibes-ide}
sources:
  - id: s1
    title: "Salesforce Extensions for Visual Studio Code"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfvscode-extensions/overview
    type: official-docs
    accessed: 2026-11-15
  - id: s2
    title: "Installation Instructions for Desktop (Salesforce Extensions for Visual Studio Code)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/install.html
    type: official-docs
    accessed: 2026-11-15
  - id: s3
    title: "Debug Apex Code (Salesforce Extensions for Visual Studio Code)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/apex-debugging.html
    type: official-docs
    accessed: 2026-11-15
  - id: s4
    title: "Salesforce Development Models (Salesforce Extensions for Visual Studio Code)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/development-models.html
    type: official-docs
    accessed: 2026-11-15
  - id: s5
    title: "Deploy on Save (Salesforce Extensions for Visual Studio Code)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/deploy-on-save.html
    type: official-docs
    accessed: 2026-11-15
  - id: s6
    title: "Web Versus Desktop (Agentforce Vibes IDE)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/code-builder/guide/codebuilder-differences.html
    type: official-docs
    accessed: 2026-11-15
  - id: s7
    title: "Set Up Visual Studio Code (Find and Fix Bugs with Apex Replay Debugger)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/find-and-fix-bugs-with-apex-replay-debugger/apex-replay-debugger-set-up-vscode
    type: official-learning
    accessed: 2026-11-15
created: 2026-11-15
---

# Salesforce Extensions for VS Code

Salesforce Extensions for Visual Studio Code are a set of open-source extensions that turn VS Code into a Salesforce development environment. Salesforce publishes them as the **Salesforce Extension Pack** on both the VS Code Marketplace and the Open VSX registry.[^s1][^s2] The pack covers coding, testing, refactoring and debugging for Apex, Lightning Web Components, Aura and Visualforce. It also adds an **Org Browser** for pulling metadata from an org and a visual **SOQL Builder** whose results can be exported as CSV or JSON.[^s1] The extensions work against scratch orgs, sandboxes and Developer Edition orgs.[^s1]

## How it works

The extensions are a front end to Salesforce CLI rather than a separate engine: the CLI is required even if a developer never types a CLI command, because the extensions call it underneath.[^s2] A setup therefore has three parts: Salesforce CLI, VS Code with the Extension Pack, and a Java Development Kit. Some features, notably the Apex language tooling, need a JDK; the install guide lists versions 11, 17 and 21, and Trailhead recommends JDK 21 and setting `salesforcedx-vscode-apex.java.home` to its install directory.[^s2][^s7] Behind a corporate proxy, the install guide says to set `HTTP_PROXY` and `HTTPS_PROXY` and turn off VS Code's built-in proxy support.[^s2]

The extensions support both Salesforce DX development models. In the **org development model**, developers retrieve from and deploy to orgs without source tracking, such as non-tracked sandboxes, Developer Edition orgs, Trailhead Playgrounds or production. In the **package development model**, a self-contained app or library is built against source-tracked orgs such as scratch orgs and shipped as one package through CI/CD.[^s4] Teams can use different models for different projects or mix them on one project.[^s4]

**Deploy on Save** sends each saved file to the default org. It is turned on with `salesforcedx-vscode-core.push-or-deploy-on-save.enabled`, and Salesforce recommends setting it per workspace rather than globally. Against a source-tracked org a save pushes tracked source; against an untracked org it runs a source deploy. Only one deployment runs at a time, and files saved meanwhile are queued into the next one.[^s5]

## Debugging options

The pack includes three Apex debuggers with different licensing:[^s3]

- **Apex Replay Debugger** is free. It replays execution from a debug log, and Salesforce calls it the right choice for most cases.[^s3]
- **Interactive Debugger** pauses code in real time. Performance and Unlimited Edition orgs include one licence, Enterprise Edition can buy it, and Trial and Developer Edition orgs cannot use it.[^s3]
- **ISV Customer Debugger** lets a package publisher debug managed-package code in a subscriber sandbox or a scratch org.[^s3]
- **Scratch org debugging** with either live debugger needs the `DebugApex` feature, plus an Apex Debugger licence on the Dev Hub.[^s3]

## Limits and gotchas

- On a large shared sandbox, Deploy on Save can silently overwrite another developer's work; turning on **Detect Conflicts At Sync** checks for conflicts on deploys started from VS Code.[^s5]
- The install guide sets a minimum VS Code version for current Extension Pack releases. Older pack versions remain for teams that cannot upgrade the editor, but Salesforce does not fix them.[^s2]
- Release notes are published weekly through the Marketplace changelog rather than with the platform release notes, so check the changelog when behaviour changes.[^s1]

## When to use it (and when not)

Use the desktop extensions when developers need their own toolchain, version control and any VS Code Marketplace extension. The browser-based **Agentforce Vibes IDE** packages VS Code, the same Salesforce extensions and Salesforce CLI. It is launched from Setup, authenticates to the org and loads its metadata into a project automatically, and Salesforce keeps its extensions up to date.[^s6] The trade-offs: it cannot reach the Microsoft Marketplace (only Open VSX), and third-party authorization works differently.[^s6] Either way, pick the development model per project: the org model for direct work against untracked orgs, the package model for source-tracked, CI-driven delivery.[^s4]

## Connections

The extensions are the editor layer of **Salesforce DX** (broader). They depend on **Salesforce CLI** for every org operation.[^s2] Their main languages are **Apex** and **Lightning Web Components**, Deploy on Save behaves differently depending on whether the target org has **source tracking**, and **scratch orgs** are the usual source-tracked target in the package model.[^s1][^s4][^s5] The **Agentforce Vibes IDE** consumes the same extensions in the browser.[^s6]

## Sources

[^s1]: Salesforce Developers, "Salesforce Extensions for Visual Studio Code". https://developer.salesforce.com/docs/platform/sfvscode-extensions/overview (accessed 2026-11-15)
[^s2]: Salesforce Developers, "Installation Instructions for Desktop". https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/install.html (accessed 2026-11-15)
[^s3]: Salesforce Developers, "Debug Apex Code". https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/apex-debugging.html (accessed 2026-11-15)
[^s4]: Salesforce Developers, "Salesforce Development Models". https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/development-models.html (accessed 2026-11-15)
[^s5]: Salesforce Developers, "Deploy on Save". https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/deploy-on-save.html (accessed 2026-11-15)
[^s6]: Salesforce Developers, "Web Versus Desktop (Agentforce Vibes IDE)". https://developer.salesforce.com/docs/platform/code-builder/guide/codebuilder-differences.html (accessed 2026-11-15)
[^s7]: Trailhead, "Set Up Visual Studio Code". https://trailhead.salesforce.com/content/learn/projects/find-and-fix-bugs-with-apex-replay-debugger/apex-replay-debugger-set-up-vscode (accessed 2026-11-15)
