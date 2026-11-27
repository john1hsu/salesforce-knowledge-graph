---
id: kt:slack-workflow-builder
type: Tool
title: Slack Workflow Builder
aliases: [Workflow Builder, Slack workflows, Slack Workflow Builder steps]
domain: automation
summary: >-
  Slack's no-code automation tool: a workflow starts from a trigger (a link, schedule, webhook, emoji reaction,
  posted message, list update or channel join) and runs Slack, connector and custom steps, including Salesforce
  connector steps that create or update records and run active autolaunched flows.
release: "Winter '27"
status: current
broader: [kt:slack-platform, kt:process-automation]
related: [kt:block-kit, kt:record-triggered-flow, kt:agentforce-in-slack, kt:slack-api-rate-limits]
relations:
  - {predicate: partOf, object: kt:slack-platform}
  - {predicate: integratesWith, object: kt:autolaunched-flow}
  - {predicate: alternativeTo, object: kt:flow-builder}
  - {predicate: contrastsWith, object: kt:mulesoft-composer}
sources:
  - id: s1
    title: "Guide to Slack Workflow Builder"
    publisher: Slack (Salesforce)
    url: https://slack.com/help/articles/360035692513-Guide-to-Slack-Workflow-Builder
    type: official-docs
    accessed: 2026-11-27
  - id: s2
    title: "Build a workflow: Create a workflow in Slack"
    publisher: Slack (Salesforce)
    url: https://slack.com/help/articles/17542172840595-Guide-to-Workflow-Builder
    type: official-docs
    accessed: 2026-11-27
  - id: s3
    title: "Workflow steps"
    publisher: Slack (Salesforce)
    url: https://docs.slack.dev/workflows/workflow-steps
    type: official-docs
    accessed: 2026-11-27
  - id: s4
    title: "Enhance Your Slack Workflows with Steps (Business Process Automation with Slack's Workflow Builder)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/business-process-automation-with-slacks-workflow-builder/add-steps-to-a-workflow
    type: official-learning
    accessed: 2026-11-27
  - id: s5
    title: "Build No-Code Slack and Salesforce Automations With Flow"
    publisher: Salesforce Admins
    url: https://admin.salesforce.com/blog/2025/build-no-code-slack-and-salesforce-automations-with-flow
    type: official-blog
    accessed: 2026-11-27
created: 2026-11-27
---

# Slack Workflow Builder

**Workflow Builder** is the no-code tool inside Slack for automating everyday tasks and processes. A workflow can be a single message or a multi-step process, and it can reach other systems through connector steps; builders start from a template or from scratch.[^s1] By default anyone on a paid Slack plan except Frontline Members can build workflows, while members and guests can run them, and owners or admins can narrow who builds.[^s1][^s2]

## How it works

A workflow has a **trigger**, a sequence of **steps**, **variables** (outputs of earlier steps that later steps can use), optional **buttons**, and one or more **workflow managers** who can edit, unpublish and delete it; the builder becomes a manager automatically.[^s2] The available triggers are: from a link (a Start Workflow button that only works inside Slack), from a webhook, on a schedule, when a list item is updated, when a message containing chosen keywords is posted, when a person joins a channel, and when a given emoji reaction is used in a channel.[^s2] Link-triggered workflows can be found in the Workflow gallery, a channel's Workflows tab or search.[^s1]

Steps come in three kinds. **Slack steps** (send a message, add someone to a channel, forms, canvas and list actions, delays and AI steps) are available to everyone by default. **Connector steps** perform actions in third-party services such as Google Sheets, Jira Cloud, DocuSign or Zoom, but only once an admin has approved the connector and the user has authenticated to the service. **Custom steps** are built by an organization's developers and are available to app collaborators.[^s2][^s4] Buttons pause a run until someone clicks; they can continue the workflow, start another one or open a link, and can be restricted to certain people or given an expiry.[^s2][^s4] Form responses become variables for later steps and can be downloaded as CSV.[^s4]

## Salesforce steps

The Salesforce connector provides steps to **create or update a record** and to **run a Salesforce flow**, and the Sales Elevate category adds steps such as creating a Salesforce channel or finding a channel's Salesforce record.[^s4] The Run a Flow step maps Slack variables to the flow's input variables, and only active autolaunched flows can be called; flow output variables, such as a new opportunity link, can be posted back in a message.[^s5] In the other direction, a record-triggered flow can post to Slack with the Send a Slack Message action, which the Salesforce Admins team notes runs only on the asynchronous path and needs the target conversation ID.[^s5]

## Custom steps

Developers extend Workflow Builder with **custom workflow steps**: functions in an app, either Slack-hosted (Deno Slack SDK and Slack CLI) or self-hosted with Bolt for JavaScript, Python or Java. A Bolt app subscribes to the `function_executed` event, declares the step's callback ID and input and output parameters, and must finish each run by reporting success or an error.[^s3] Custom steps cannot be built on the Free plan, cannot be distributed publicly or listed in the Slack Marketplace, and an Enterprise organization's app must be org-ready and installed at the org level.[^s3]

## Limits and gotchas

- Workflow Builder needs a paid plan, and posting to a channel requires posting permission in that channel.[^s2]
- External Slack Connect users cannot run workflows that contain connector steps or your organization's custom steps, and they can use member-built workflows only if owners and admins allow it.[^s2][^s3]
- A coded workflow cannot be imported whole into Workflow Builder; only its custom functions can be exposed as steps.[^s3]
- Connector steps run with either each user's credentials or the builder's, which the builder chooses, so plan Salesforce permissions accordingly.[^s2]

## When to use it (and when not)

Use Workflow Builder when the process lives in Slack: intake forms, approvals by button, emoji-driven handoffs or scheduled reminders, calling Salesforce through the connector when records must change.[^s4][^s5] Keep record logic such as account, contact and opportunity creation in an autolaunched flow and let the Slack workflow collect input and call it, as Salesforce's own examples do.[^s5] When the starting event is a Salesforce data change, such as an opportunity closing, start in a record-triggered flow and post into Slack from there.[^s5]

## Connections

Workflow Builder is `partOf` `kt:slack-platform` and sits under `kt:process-automation` as Slack's declarative automation layer.[^s1] It `integratesWith` `kt:autolaunched-flow` through the Run a Flow step, and is the Slack-side `alternativeTo` `kt:flow-builder`, while `kt:record-triggered-flow` is the usual way to push Salesforce events back into Slack.[^s5] Custom steps are app functions built with Bolt or the Deno Slack SDK, which ties the tool to the same developer platform as `kt:block-kit` and `kt:slack-api-rate-limits`.[^s3] It `contrastsWith` `kt:mulesoft-composer`, Salesforce's no-code integration tool that runs outside Slack, whereas Workflow Builder reaches third-party systems only through approved connector steps, among them AI steps that make it a neighbour of `kt:agentforce-in-slack`.[^s4]

## Sources
[^s1]: Slack (Salesforce), "Guide to Slack Workflow Builder". https://slack.com/help/articles/360035692513-Guide-to-Slack-Workflow-Builder (accessed 2026-11-27)
[^s2]: Slack (Salesforce), "Build a workflow: Create a workflow in Slack". https://slack.com/help/articles/17542172840595-Guide-to-Workflow-Builder (accessed 2026-11-27)
[^s3]: Slack (Salesforce), "Workflow steps". https://docs.slack.dev/workflows/workflow-steps (accessed 2026-11-27)
[^s4]: Trailhead, "Enhance Your Slack Workflows with Steps". https://trailhead.salesforce.com/content/learn/modules/business-process-automation-with-slacks-workflow-builder/add-steps-to-a-workflow (accessed 2026-11-27)
[^s5]: Salesforce Admins, "Build No-Code Slack and Salesforce Automations With Flow" (2025). https://admin.salesforce.com/blog/2025/build-no-code-slack-and-salesforce-automations-with-flow (accessed 2026-11-27)
