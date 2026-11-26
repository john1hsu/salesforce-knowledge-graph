---
id: kt:block-kit
type: Feature
title: Block Kit
aliases: [Slack Block Kit, Block Kit UI framework, Block Kit Builder, Slack blocks]
domain: development
summary: >-
  Slack's JSON-based UI framework of blocks, block elements and composition objects that apps use to lay out
  messages, modals and the App Home tab, with interactive components whose clicks and submissions are delivered
  to the app as block_actions and view_submission payloads.
release: "Winter '27"
status: current
broader: [kt:slack-platform]
related: [kt:agentforce-in-slack, kt:slack-workflow-builder, kt:lightning-web-components]
relations:
  - {predicate: partOf, object: kt:slack-platform}
  - {predicate: governedBy, object: kt:slack-api-rate-limits}
  - {predicate: consumedBy, object: kt:agentforce-in-slack}
sources:
  - id: s1
    title: "Block Kit"
    publisher: Slack (Salesforce)
    url: https://docs.slack.dev/block-kit/
    type: official-docs
    accessed: 2026-11-26
  - id: s2
    title: "Handling user interaction in your Slack apps"
    publisher: Slack (Salesforce)
    url: https://docs.slack.dev/interactivity/handling-user-interaction
    type: official-docs
    accessed: 2026-11-26
  - id: s3
    title: "Break Down Block Kit"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/slack-block-kit/break-down-block-kit
    type: official-learning
    accessed: 2026-11-26
  - id: s4
    title: "Manage Interactivity"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/slack-block-kit/manage-interactivity
    type: official-learning
    accessed: 2026-11-26
created: 2026-11-26
---

# Block Kit

**Block Kit** is the UI framework Slack apps use to build what users see and click. It is made of three kinds of parts: **blocks**, the visual components arranged into a layout; **block elements**, which are usually interactive components such as buttons and menus; and **composition objects**, which define text, options and other interactive details inside certain blocks and elements.[^s1] For Salesforce teams it is the layer that turns record data, approvals and agent replies into structured Slack messages instead of plain text.

## How it works

A layout is a JSON `blocks` array. Each block is a JSON object with a required `type` field, and the blocks stack in the order they appear in the array.[^s1] Apps place blocks on **surfaces**: messages, modals and the app's Home tab.[^s1][^s3] Not every block works everywhere. Trailhead notes that almost every layout block can live on all three surfaces, while the file block, which displays a remote file, can appear only in a message.[^s3]

Interactive block elements include buttons, date pickers, select and multi-select menus, overflow menus, plain-text input, radio buttons, checkboxes and time pickers. They sit inside section, context, input and actions blocks.[^s3] Slack's current documentation also recommends newer blocks for AI and agent experiences, among them rich text, container, alert, carousel, data visualization and task card blocks, and positions Block Kit for streamed agent responses.[^s1]

**Block Kit Builder** is a visual prototyping sandbox for choosing, configuring and previewing every available block with drag-and-drop, and Slack says it can be paired with its MCP and Skills plugin so a coding agent builds and validates layouts.[^s1]

## Interactivity

When a user clicks an interactive component, Slack sends a `block_actions` payload to the app's Request URL, configured under Interactivity & Shortcuts in the app settings; select menus that load options dynamically use a separate Options Load URL.[^s4] Submitting a modal sends `view_submission`, cancelling one sends `view_closed`, and shortcuts send `shortcut` or `message_actions` payloads.[^s2] Payloads arrive as an HTTP POST whose form-encoded `payload` parameter holds JSON, and a distributed app's Request URL must use HTTPS.[^s2] The payload carries the user, the container where the action happened, the `state.values` of inputs, the `actions` array with `block_id` and `action_id`, and a `response_url`.[^s4]

## Limits and gotchas

- A message can hold up to 50 blocks, and a modal or Home tab up to 100.[^s1]
- The app must return HTTP 200 within 3 seconds of receiving a payload, or the user sees an error, so do slow work after acknowledging.[^s2]
- A `response_url` can be used up to 5 times within 30 minutes; after that, post through the normal messaging APIs.[^s2]
- A `trigger_id`, needed to open a modal, expires in three seconds and can be used for only one operation.[^s2]
- Global shortcut payloads carry no `response_url`, so replies need another route.[^s2]
- Screen readers read the top-level `text` field, so include meaningful fallback text or let Slack build it from the blocks.[^s1]

## When to use it (and when not)

Use Block Kit when a Salesforce integration needs structured, actionable Slack output: a record summary with Approve and Reject buttons, a modal that collects case details, or an App Home dashboard.[^s1][^s4] For a simple notification, plain message text or a declarative Salesforce-to-Slack action is enough. Inside Salesforce itself, the equivalent UI layer is Lightning Web Components; Block Kit is the Slack-side counterpart and is rendered by Slack, not by the browser.[^s1][^s3]

## Connections

Block Kit is `partOf` `kt:slack-platform`, its `broader` parent, and is `governedBy` `kt:slack-api-rate-limits`, the Slack API throttles covered in that node, which apply to the calls that publish block layouts.[^s1] It is `consumedBy` `kt:agentforce-in-slack`, as Slack recommends specific blocks for agent and AI responses.[^s1] It is related to `kt:slack-workflow-builder`, whose workflows also surface in Slack's UI, and to `kt:lightning-web-components`, the comparable component framework on the Salesforce side.[^s3][^s4]

## Sources
[^s1]: Slack (Salesforce), "Block Kit". https://docs.slack.dev/block-kit/ (accessed 2026-11-26)
[^s2]: Slack (Salesforce), "Handling user interaction in your Slack apps". https://docs.slack.dev/interactivity/handling-user-interaction (accessed 2026-11-26)
[^s3]: Trailhead, "Break Down Block Kit". https://trailhead.salesforce.com/content/learn/modules/slack-block-kit/break-down-block-kit (accessed 2026-11-26)
[^s4]: Trailhead, "Manage Interactivity". https://trailhead.salesforce.com/content/learn/modules/slack-block-kit/manage-interactivity (accessed 2026-11-26)
