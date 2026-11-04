---
id: kt:slack-platform
type: Product
title: Slack Platform
aliases: [Slack developer platform, Slack API platform, Slack apps]
domain: clouds-and-products
summary: >-
  The developer platform of Slack, the collaboration product Salesforce acquired in 2021: apps built with Bolt
  and the Slack SDKs call the Web API, receive events, and render Block Kit UI on Slack surfaces, and Salesforce
  connects to it through the Salesforce for Slack app, Flow actions and the beta Apex SDK for Slack.
release: "Winter '27"
status: current
broader: [kt:customer-360]
related: [kt:flow-builder, kt:agentforce, kt:apex, kt:sales-cloud, kt:service-cloud]
relations:
  - {predicate: acquiredBy, object: kt:salesforce-inc}
  - {predicate: hasPart, object: kt:block-kit}
  - {predicate: hasPart, object: kt:slack-workflow-builder}
  - {predicate: integratesWith, object: kt:mulesoft-composer}
  - {predicate: governedBy, object: kt:slack-api-rate-limits}
sources:
  - id: s1
    title: "Slack platform overview"
    publisher: Slack (Salesforce)
    url: https://docs.slack.dev/concepts/overview
    type: official-docs
    accessed: 2026-11-04
  - id: s2
    title: "Rate limits"
    publisher: Slack (Salesforce)
    url: https://docs.slack.dev/apis/web-api/rate-limits
    type: official-docs
    accessed: 2026-11-04
  - id: s3
    title: "Build Slack Apps with Bolt (Choose Your Slack Development Path)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/zh-CN/content/learn/modules/choose-your-slack-development-path/build-slack-apps-with-bolt
    type: official-learning
    accessed: 2026-11-04
  - id: s4
    title: "Build Slack Apps (Apex SDK for Slack)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/build.html
    type: official-docs
    accessed: 2026-11-04
  - id: s5
    title: "How Admins Can Connect Salesforce and Slack"
    publisher: Salesforce Admins
    url: https://admin.salesforce.com/blog/2021/how-admins-can-connect-salesforce-and-slack
    type: official-blog
    accessed: 2026-11-04
  - id: s6
    title: "FAQ: Salesforce Completes Slack Acquisition"
    publisher: Salesforce
    url: https://www.salesforce.com/news/wp-json/wp/v2/posts/49205
    type: news
    accessed: 2026-11-04
created: 2026-11-04
---

# Slack Platform

Slack is the messaging and collaboration product that Salesforce acquired; the company announced a definitive agreement on December 1, 2020 and completed the deal on July 21, 2021. Slack kept its own brand, and Salesforce positioned it as the interface for Customer 360, with every Salesforce Cloud and industry solution to be integrated with it.[^s6] The **Slack Platform** is the developer side of that product: the APIs, UI framework, SDKs and tooling used to build apps that live inside Slack, including apps that bring Salesforce data and automation into conversations.[^s1]

## How it works

An app is created either with the Slack CLI or on the app settings page, and receives tokens that authorize it to call the Slack **Web API**; the scopes granted to those tokens decide what it can read and do.[^s1] Apps appear on a set of **surfaces**: messages, modals and canvases are open to every kind of app, while the App Home tab is limited to apps built with Bolt.[^s1] Users start interactions through slash commands and shortcuts, and UI on all these surfaces is described with **Block Kit**, a library of stackable components (sections, buttons and other interactive elements) sent to Slack as JSON over HTTP.[^s1][^s3] The Block Kit Builder lets developers prototype a layout, preview it on desktop and mobile in light and dark modes, and copy the JSON payload into code.[^s3]

**Bolt** is Slack's official framework, available for JavaScript, Python and Java. It sits on the first-party Slack SDKs and bundles server configuration, request and token validation, and simple handlers for messages, events and interactivity; Slack's overview adds that it handles token rotation and rate limiting for you.[^s1][^s3] For no-code users, **Workflow Builder** automates tasks inside Slack, and developers can extend it with custom workflow steps written as functions in a Bolt app.[^s1] The platform also supports AI agents and assistants, with features such as a split-view pane and streamed text responses, and offers developer sandboxes for non-production testing.[^s1]

## Connecting Salesforce and Slack

Admins have several declarative options. The free Salesforce for Slack package from AppExchange adds a Slack Setup app in Salesforce; it lets users see Slack messages related to a record, send records to Slack, and post record alerts to channels, with custom objects needing extra configuration. Admins can place a Send to Slack action on record pages, and flows can post to channels or users through the Slack: Post Message invocable action, with destination IDs stored in custom metadata rather than hard-coded. MuleSoft Composer offers a paid, no-code route for multi-system integrations that end in Slack messages.[^s5]

For pro-code teams on the Salesforce side, the **Apex SDK for Slack** defines a Slack app as SlackApp metadata in an SFDX project, renders views (home tab, message or modal) that translate to Block Kit, and handles shortcuts, buttons, slash commands and events in Apex. Salesforce documentation still labels it **Beta**, meaning it is not generally available and may be discontinued without notice.[^s4]

## Limits and gotchas

Web API methods are rate limited per app per workspace in tiers: Tier 1 allows 1+ requests per minute, Tier 2 20+, Tier 3 50+ and Tier 4 100+. Some methods have special limits; `chat.postMessage`, for example, is guided at about one message per second per channel plus a workspace-wide cap. A throttled call returns HTTP 429 with a `Retry-After` header, and the limit does not affect other methods or other workspaces.[^s2] The Events API delivers at most 30,000 events per workspace per app per 60 minutes, after which Slack sends an `app_rate_limited` event.[^s2] Because the Apex SDK is beta, production designs should not depend on it without accepting that risk.[^s4]

## When to use it (and when not)

Use the declarative Salesforce for Slack app and Flow actions when the goal is alerts, record sharing and simple notifications.[^s5] Build a Bolt app when you need custom interactive UI, App Home experiences, slash commands or custom Workflow Builder steps, and host it where it can reach both Slack and Salesforce APIs.[^s1][^s3] High-volume notification designs should batch or route through channels with the per-channel posting guideline in mind, rather than firing one message per record change.[^s2]

## Connections

Slack is a Salesforce acquisition (`acquiredBy kt:salesforce-inc`) placed under `kt:customer-360` as its conversational interface.[^s6] It `hasPart` Block Kit and Slack Workflow Builder, and API usage is `governedBy` the Slack API rate limits.[^s1][^s2] On the Salesforce side it is reached from `kt:flow-builder` through Slack actions, from `kt:apex` through the beta SDK, and from `kt:mulesoft-composer` for no-code integrations.[^s4][^s5] Record alerts and sharing make it a companion to `kt:sales-cloud` and `kt:service-cloud` work, and its agent features relate it to `kt:agentforce`.[^s1][^s5]

## Sources
[^s1]: Slack (Salesforce), "Slack platform overview". https://docs.slack.dev/concepts/overview (accessed 2026-11-04)
[^s2]: Slack (Salesforce), "Rate limits". https://docs.slack.dev/apis/web-api/rate-limits (accessed 2026-11-04)
[^s3]: Trailhead, "Build Slack Apps with Bolt". https://trailhead.salesforce.com/zh-CN/content/learn/modules/choose-your-slack-development-path/build-slack-apps-with-bolt (accessed 2026-11-04)
[^s4]: Salesforce Developers, "Build Slack Apps (Apex SDK for Slack)". https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/build.html (accessed 2026-11-04)
[^s5]: Salesforce Admins, "How Admins Can Connect Salesforce and Slack" (2021). https://admin.salesforce.com/blog/2021/how-admins-can-connect-salesforce-and-slack (accessed 2026-11-04)
[^s6]: Salesforce, "FAQ: Salesforce Completes Slack Acquisition" (2021). https://www.salesforce.com/news/wp-json/wp/v2/posts/49205 (accessed 2026-11-04)
