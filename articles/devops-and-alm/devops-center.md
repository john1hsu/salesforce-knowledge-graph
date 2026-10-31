---
id: kt:devops-center
type: Tool
title: DevOps Center
aliases: [Lifecycle Center, Salesforce Lifecycle Center, next-generation DevOps Center, DevOps Center managed package]
domain: devops-and-alm
summary: >-
  Salesforce's built-in change and release management tool, being renamed Lifecycle Center from October 2026, that
  tracks changes as work items in source control and promotes them through a pipeline of stages to production.
release: "Winter '27"
status: current
broader: [kt:application-lifecycle-management]
related: [kt:environment-strategy, kt:scratch-orgs, kt:sandbox-types, kt:source-tracking]
relations:
  - {predicate: alternativeTo, object: kt:change-sets}
  - {predicate: integratesWith, object: kt:salesforce-cli}
  - {predicate: dependsOn, object: kt:apex-testing}
  - {predicate: integratesWith, object: kt:agentforce}
sources:
  - id: s1
    title: "Govern, Manage, and Release Changes with Lifecycle Center"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.devops_center_overview.htm&type=5
    type: official-docs
    accessed: 2026-10-31
  - id: s2
    title: "Application Lifecycle Management Journey with Lifecycle Center"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.next_gen_devops_center_alm_journey.htm&type=5
    type: official-docs
    accessed: 2026-10-31
  - id: s3
    title: "Get Started with Lifecycle Center"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.next_gen_devops_center_get_started.htm&type=5
    type: official-docs
    accessed: 2026-10-31
  - id: s4
    title: "Next-Generation Lifecycle Center for Salesforce DevOps"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/devops-center-quick-look/say-hello-to-devops-center
    type: official-learning
    accessed: 2026-10-31
  - id: s5
    title: "DevOps Center Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/devops-center-dev/guide
    type: official-docs
    accessed: 2026-10-31
created: 2026-10-31
---

# DevOps Center

DevOps Center is Salesforce's own change and release management tool. Salesforce Help states that, beginning October 2026, DevOps Center is being renamed **Lifecycle Center**, so both names appear in current documentation.[^s1] It gives admins, developers, release managers and AI agents one shared source of truth in a source control repository, covering change and release management, governance, analytics and agentic development.[^s1] It is built for teams anywhere on the low-code to pro-code range: people can build with declarative tools in a sandbox, with Salesforce Extensions for VS Code, with the Agentforce Vibes IDE or with Salesforce CLI, and still release through the same pipeline.[^s1][^s5]

## Two generations

The original DevOps Center ships as a managed package. Installing it creates custom objects, with a Project object at the top that is the parent of nearly every other record, and a Repository object that one or more projects reference.[^s5] The next-generation version, now Lifecycle Center, is built into the platform: there is no package to install, and it is turned on from Setup in a Lifecycle Center hub org.[^s4] Help describes the core features of the two versions as the same, with Lifecycle Center adding AI assistance, governance and an extensible interface. The managed package remains supported, and a migration path for projects, pipelines, environments and eligible work items is in Developer Preview.[^s1]

## How it works

- **Work items** describe a requirement, such as a user story or bug fix, and track its change through the release lifecycle. They can be combined and imported from Jira.[^s1][^s2]
- **Pipelines** are an ordered sequence of stages, for example Integration, Staging and Production. Each stage has its own branch in source control.[^s1][^s2]
- **Development environments.** Each team member works in a source-tracked development environment. Environments can be sandboxes, scratch orgs or production orgs connected to the pipeline.[^s1][^s3] The DX Inspector tool tracks metadata changes in a development org and lets the developer view and commit them, which replaces tracking changes by hand.[^s4]
- **Promotion** merges the current stage's branch into the next stage's branch and then deploys to that stage's org. Release managers can promote with clicks or with Salesforce CLI, and can promote metadata together with related configuration data in one operation.[^s1][^s4]
- **Back sync** brings a development environment up to date with changes that reached the first pipeline stage.[^s1]

## Testing, governance and analytics

Testing is on by default, with test providers, test suites and quality gates. Suites can run when a developer opens a review, before promotion, or on demand, and a failed quality gate keeps a work item from advancing.[^s1][^s2] Governance, which sets policies for developers and coding agents and monitors agent activity, is still labeled Beta.[^s1][^s3] The Analytics tab reports DORA metrics, viewable for up to 90 days, and a dashboard of the last 30 days of Agentforce Vibes activity.[^s1][^s3]

## Limits and gotchas (Winter '27)

- Available in Lightning Experience in Enterprise, Performance, Professional, Unlimited and Developer Editions.[^s1][^s5]
- Not available in Government Cloud Plus or the EU Operating Zone. Help warns that turning on the managed package in Government Cloud Plus can send data outside the authorization boundary, and the developer guide says it appears in Government Cloud Setup but should not be enabled there.[^s1][^s5]
- Supported source control providers in the docs are GitHub and Bitbucket. Some Bitbucket features in the managed package are Beta.[^s1][^s3]
- The help pages reviewed for this article do not publish pricing or numeric limits on projects, stages or work items.[^s1]

## When to use it

Help positions the tool directly as an alternative to change sets.[^s1] Choose it when a team wants source control and repeatable, auditable promotion without building its own CI/CD scripts. A solo admin can still deploy metadata and data straight to a target org without a full pipeline.[^s2] Teams that already run a mature Git-based pipeline with Salesforce CLI may keep it and use the CLI integration instead.[^s1]

## Connections

DevOps Center is a tool within **application lifecycle management**, its broader node: it puts the plan, build, test and release stages into a pipeline.[^s2] It is the guided **alternative to change sets**, replacing org-to-org uploads with branches and promotions.[^s1] It **integrates with Salesforce CLI** for promotion, and with **Agentforce** for AI features such as natural-language merge-conflict resolution.[^s4] It **depends on Apex testing** and other test suites for its quality gates.[^s2] Its development environments come from the org's **environment strategy**: **sandbox types** and **scratch orgs** whose changes are captured through **source tracking**.[^s2][^s3]

## Sources

[^s1]: Salesforce Help, "Govern, Manage, and Release Changes with Lifecycle Center". https://help.salesforce.com/s/articleView?language=en_US&id=platform.devops_center_overview.htm&type=5 (accessed 2026-10-31)
[^s2]: Salesforce Help, "Application Lifecycle Management Journey with Lifecycle Center". https://help.salesforce.com/s/articleView?language=en_US&id=platform.next_gen_devops_center_alm_journey.htm&type=5 (accessed 2026-10-31)
[^s3]: Salesforce Help, "Get Started with Lifecycle Center". https://help.salesforce.com/s/articleView?language=en_US&id=platform.next_gen_devops_center_get_started.htm&type=5 (accessed 2026-10-31)
[^s4]: Trailhead, "Next-Generation Lifecycle Center for Salesforce DevOps". https://trailhead.salesforce.com/content/learn/modules/devops-center-quick-look/say-hello-to-devops-center (accessed 2026-10-31)
[^s5]: Salesforce Developers, "DevOps Center Developer Guide". https://developer.salesforce.com/docs/platform/devops-center-dev/guide (accessed 2026-10-31)
