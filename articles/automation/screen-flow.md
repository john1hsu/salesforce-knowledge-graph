---
id: kt:screen-flow
type: Feature
title: Screen Flow
aliases: [screen flows, flow with screens, guided flow, interactive flow]
domain: automation
summary: >-
  A Flow Builder flow type that presents one or more screens to a user, collects their input and acts on
  it; launched from Lightning pages, actions, the utility bar, Experience Builder pages and other entry
  points, and running in user context by default.
release: "Winter '27"
status: current
broader: [kt:flow-builder, kt:process-automation]
related: [kt:record-triggered-flow, kt:autolaunched-flow, kt:flow-orchestrator, kt:experience-cloud]
relations:
  - {predicate: integratesWith, object: kt:lightning-web-components}
  - {predicate: dependsOn, object: kt:salesforce-sharing-model}
  - {predicate: dependsOn, object: kt:autolaunched-flow}
sources:
  - id: s1
    title: "Screen Flows: Build a Screen Flow"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/screen-flows/build-a-screen-flow
    type: official-learning
    accessed: 2026-11-01
  - id: s2
    title: "Screen Flow Distribution: Get Started with Flow Distribution"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/screen_flow_distribution/screen_flow_distribution_intro
    type: official-learning
    accessed: 2026-11-01
  - id: s3
    title: "Make Screen Flows Reactive"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=platform.flow_build_make_reactive.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-01
  - id: s4
    title: "Your Guide to Determining the Flow Running User and Its Execution Context"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2022/your-guide-to-determining-the-flow-running-user-and-its-execution-context
    type: official-blog
    accessed: 2026-11-01
  - id: s5
    title: "Security Considerations for Flow Design"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/secure-coding/guide/secure-coding-considerations-flow-design.html
    type: official-docs
    accessed: 2026-11-01
created: 2026-11-01
---

# Screen Flow

A screen flow is the interactive flow type in Flow Builder: it shows screens to a person, gathers their answers, and then uses those answers to do work such as creating or updating records. Trailhead's example is a support agent on a call who follows a scripted screen and whose answers become a new Case.[^s1] Unlike record-triggered or scheduled flows, which run in the background, a screen flow only runs when a user launches it from somewhere in the UI.[^s2]

## How it works

The building block is the **Screen** element. Each screen has a label that admins see on the canvas, and a set of components dragged from the Components list: Display Text for guidance or a call script, Text and Long Text Area for input, Toggle for yes/no choices, and many more. Inputs can be marked required so the user cannot finish without answering.[^s1] Between screens the flow uses the usual logic and data elements; in the Trailhead build, a formula turns the toggle into a Case status and a Create Records element saves the case.[^s1] Variables marked **Available for input** let the launching page pass in context such as the current record's Account and Contact IDs.[^s1] A gotcha that trips newcomers: some components expose their answer through a property, so a toggle is read as `{!Toggle.value}`, not as the component itself.[^s1]

**Reactivity** lets components on one screen update as the user types or selects, without a round trip to the next screen. A *source* component drives a *reactive* component, and **screen actions** call an autolaunched flow from inside the screen to fetch or process data. Salesforce says this supports single-page-style screens and fewer clicks, and it needs API version 59.0 or later.[^s3]

## Where users run it

Screen flows can be placed on Lightning pages, flow actions, the utility bar, Experience Builder pages, custom Lightning components, Visualforce pages, web tabs, and custom buttons and links; some of these work only in Lightning Experience.[^s2] Several of these methods depend on the **Run Flows** user permission by default, which admins grant through a profile or permission set.[^s2]

## Running context and security

A top-level screen flow runs as the current user in **user context** by default, so object permissions and field-level access come from that user's profile and permission sets; the builder can instead choose system context with sharing. A screen flow called as a subflow inherits its caller's context unless set otherwise.[^s4] System with sharing ignores object and field permissions but still respects record access such as org-wide defaults, the role hierarchy and sharing rules; system without sharing ignores record access too, and the Admins blog advises using it sparingly.[^s4] Even when a screen flow runs in system context, components that query the database (lookups, dependent picklists, file upload and similar) still honour the running user's permissions.[^s4]

Salesforce's secure-coding guidance recommends that screen flows run in user mode, that the execution context be set explicitly and documented, that privileged steps be isolated in system-mode subflows, and that any variable available for input be validated like other user input.[^s5]

## Limits and gotchas

- Not every screen component is reactive; check support before designing around it, and review custom components against the LWC guide.[^s3]
- Reactive source and target values must share a data type; manually set outputs, labels and help text do not react; validation on custom components doesn't fire on reactive changes; and only the `$Flow` global variable is reactive, not `$Organization`, `$Profile`, custom labels or custom settings.[^s3]
- Mapping a DateTime into a Time field converts it to GMT, and that conversion persists across screens.[^s3]
- Granting broad system context to a screen flow on a public or guest-facing page widens data exposure; Salesforce reserves system without sharing for specific cases backed by extra validation.[^s5]

## When to use it (and when not)

Use a screen flow when a person must supply or confirm information: guided data entry, call scripts, wizards and self-service forms. If nothing needs user input, an autolaunched or record-triggered flow is the right shape, since those run without screens.[^s2][^s4]

## Connections

Screen flow is a flow type built in **Flow Builder** under the wider **process-automation** toolset, a sibling of **record-triggered** and **autolaunched** flows.[^s2] It **depends on autolaunched flows** for reactive screen actions, and its screens can host custom **Lightning Web Components**.[^s3] Because it runs in user context by default, what it can read and change is **governed by the sharing model**.[^s4] It can be embedded on **Experience Cloud** pages through Experience Builder.[^s2] It is also listed as related to **Flow Orchestrator**, the graph's node for multi-step, multi-user processes.

## Sources

[^s1]: Trailhead, "Screen Flows: Build a Screen Flow". https://trailhead.salesforce.com/content/learn/modules/screen-flows/build-a-screen-flow (accessed 2026-11-01)
[^s2]: Trailhead, "Screen Flow Distribution: Get Started with Flow Distribution". https://trailhead.salesforce.com/content/learn/modules/screen_flow_distribution/screen_flow_distribution_intro (accessed 2026-11-01)
[^s3]: Salesforce Help, "Make Screen Flows Reactive". https://help.salesforce.com/s/articleView?id=platform.flow_build_make_reactive.htm&language=en_US&type=5 (accessed 2026-11-01)
[^s4]: Salesforce Admins Blog, "Your Guide to Determining the Flow Running User and Its Execution Context". https://admin.salesforce.com/blog/2022/your-guide-to-determining-the-flow-running-user-and-its-execution-context (accessed 2026-11-01)
[^s5]: Salesforce Developers, "Security Considerations for Flow Design". https://developer.salesforce.com/docs/platform/secure-coding/guide/secure-coding-considerations-flow-design.html (accessed 2026-11-01)
