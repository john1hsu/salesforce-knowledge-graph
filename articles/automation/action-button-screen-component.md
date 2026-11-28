---
id: kt:action-button-screen-component
type: Feature
title: Action Button Screen Component
aliases: [Flow Action Button, Action Button component, screen flow action button, Flow Action Buttons]
domain: automation
summary: >-
  A standard screen flow component that, when the running user clicks it, runs an active autolaunched flow in the
  background and exposes that flow's outputs (plus an IsSuccess flag) to other components on the same screen, so a
  screen can query, calculate or call out without moving to a new screen.
release: "Winter '27"
status: current
broader: [kt:screen-flow]
related: [kt:repeater-screen-component, kt:data-table-screen-component, kt:flow-choice-resources, kt:custom-flow-screen-components, kt:flow-http-callout]
relations:
  - {predicate: dependsOn, object: kt:autolaunched-flow}
  - {predicate: dependsOn, object: kt:flow-run-context}
  - {predicate: alternativeTo, object: kt:subflows}
  - {predicate: alternativeTo, object: kt:screen-actions}
sources:
  - id: s1
    title: "Standard Flow Screen Components"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_screencmp.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-28
  - id: s2
    title: "Data Safety When Running Screen and Autolaunched Flows in System Context"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.flow_distribute_context_data_safety_system_context.htm&amp=&language=en_US&amp=&type=5
    type: official-docs
    accessed: 2026-11-28
  - id: s3
    title: "Summer '24 Feature Deep Dive: Create Richer Screen Flows with Action Buttons (Beta)"
    publisher: Salesforce Admins Blog (Adam White)
    url: https://admin.salesforce.com/blog/2024/screen-flows-and-action-buttons-summer-24-be-release-ready
    type: official-blog
    accessed: 2026-11-28
  - id: s4
    title: "Unlock New Automation Possibilities With Spring '25 Flow Features"
    publisher: Salesforce Admins Blog (David Fromstein)
    url: https://admin.salesforce.com/blog/2025/unlock-new-automation-possibilities-with-spring-25-flow-features-be-release-ready
    type: official-blog
    accessed: 2026-11-28
  - id: s5
    title: "10 New Flow Features in Salesforce Winter '25"
    publisher: Salesforce Ben (Tim Combridge)
    url: https://www.salesforceben.com/10-new-flow-features-in-salesforce-winter-25/
    type: community
    accessed: 2026-11-28
  - id: s6
    title: "Salesforce Summer '25 Release: Enhance Your Screen Flows With Screen Actions"
    publisher: Salesforce Ben (Andreea Doroftei)
    url: https://www.salesforceben.com/salesforce-summer-25-release-enhance-your-screen-flows-with-screen-actions/
    type: community
    accessed: 2026-11-28
created: 2026-11-28
---
# Action Button Screen Component

The **Action Button** is one of the standard components a builder can drop onto a screen in a screen flow. When the running user clicks it, it triggers a screen action that runs an **active autolaunched flow**, and the results of that flow can be shown on the same screen as the button.[^s1] Salesforce positions it as a way to cut the number of screens a user has to click through, because lookups, calculations and callouts that used to need their own screen can now happen in place.[^s1][^s3]

The component arrived as a beta in Summer '24 and became generally available in Winter '25, when the beta label was removed and buttons gained the ability to be disabled.[^s3][^s5] It is listed among the standard screen components in current Salesforce Help.[^s1]

## How it works

Building with an Action Button is a two-part job. First the builder creates (or reuses) an autolaunched flow, marks its input variables *Available for Input* and its result variables *Available for Output*, sets the outputs with an Assignment, then tests and activates it; only an active flow appears in the button's flow picker.[^s3] Inside that flow the usual elements are available, such as Get Records, loops, Transform, Collection Filter, and invocable and Apex actions, and Salesforce also lists callouts and subflows among the work a button can trigger.[^s3][^s4]

Second, the builder adds the Action Button to a screen, gives it an API name and label, picks the autolaunched flow and maps screen components or variables to its inputs. The button's *View Output Resources* pane lists what the flow returns.[^s3] Other components reference those values through the button's API name, then *Results*, then the output variable.[^s3] Every Action Button also exposes an **IsSuccess** value, which builders use with component visibility, input validation or the Disabled and Read Only input states, for example to hide a result panel or block the Next button until the action has run successfully.[^s3]

Results can also drive reactive choices: Salesforce paired the feature with reactive collection choice sets so picklist, radio and choice-lookup options can refresh from what the action returned.[^s3]

## Limits and gotchas

- The called flow must be autolaunched and active, and the button always runs the active version, whereas a subflow can be set to run the latest version, which matters when debugging.[^s3]
- During the beta Salesforce cited a hard limit of 1 MB of data per screen, so returning wide records or large collections (for example a big data-table selection) can hit it.[^s3]
- The resource picker may not show a new action's outputs in some places (such as a collection choice set) until the builder clicks Done in the screen editor.[^s3]
- An action's output can be referenced only on the screen where it is configured; to use the values later in the flow, run the same logic again through a Subflow element.[^s2]

## Security considerations

A screen action executes from the user's browser and then the server, unlike a subflow, which runs entirely on the server, so Salesforce advises treating the called flow as an exposed endpoint.[^s3] The called autolaunched flow can have a different run context from the screen flow that hosts the button; system context is not inherited and must be switched on explicitly for the action, and Salesforce recommends keeping these flows in user context where possible.[^s2][^s3] Guidance for system-context flows, especially on Experience Cloud sites with external users, is to query only named fields rather than all fields, return only the records and fields the screen needs, avoid guessable inputs, and keep create, update and delete work in the screen flow or a subflow rather than in the button's flow.[^s2][^s3] Guest or restricted-access flows also need access granted to the flow the button calls.[^s3]

## When to use it (and when not)

Use an Action Button when the user should decide when the work runs: a "check availability" or "calculate price" step whose output then fills fields or toggles visibility on the same screen.[^s3][^s4] Spring '25 introduced **Screen Actions**, which run the same kind of autolaunched flow automatically, without a click, configured on the Screen element and triggered by input changes or screen load; they suit automatic look-ups such as duplicate checks as the user types.[^s4][^s6] A Subflow element remains the choice for logic that must run on the server between screens, including any record writes.[^s2][^s3]

## Connections

The Action Button is a component of **screen flows** and **depends on autolaunched flows**, which supply its logic, and on the **flow run context** settings that decide whose permissions those flows use.[^s1][^s2] It is an **alternative to subflows** (server-side, between screens) and to **screen actions** (automatic, no button).[^s3][^s4] It is related to the other in-screen building blocks it often feeds or sits beside: the **repeater**, the **data table**, **flow choice resources** that refresh reactively, **custom flow screen components**, and **HTTP callouts**, one of the operations a button-triggered flow can perform.[^s3][^s4]

## Sources

[^s1]: Salesforce Help, "Standard Flow Screen Components". https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_screencmp.htm&language=en_US&type=5 (accessed 2026-11-28)
[^s2]: Salesforce Help, "Data Safety When Running Screen and Autolaunched Flows in System Context". https://help.salesforce.com/s/articleView?id=sf.flow_distribute_context_data_safety_system_context.htm&amp=&language=en_US&amp=&type=5 (accessed 2026-11-28)
[^s3]: Salesforce Admins Blog (Adam White), "Summer '24 Feature Deep Dive: Create Richer Screen Flows with Action Buttons (Beta)". https://admin.salesforce.com/blog/2024/screen-flows-and-action-buttons-summer-24-be-release-ready (accessed 2026-11-28)
[^s4]: Salesforce Admins Blog (David Fromstein), "Unlock New Automation Possibilities With Spring '25 Flow Features". https://admin.salesforce.com/blog/2025/unlock-new-automation-possibilities-with-spring-25-flow-features-be-release-ready (accessed 2026-11-28)
[^s5]: Salesforce Ben (Tim Combridge), "10 New Flow Features in Salesforce Winter '25". https://www.salesforceben.com/10-new-flow-features-in-salesforce-winter-25/ (accessed 2026-11-28)
[^s6]: Salesforce Ben (Andreea Doroftei), "Salesforce Summer '25 Release: Enhance Your Screen Flows With Screen Actions". https://www.salesforceben.com/salesforce-summer-25-release-enhance-your-screen-flows-with-screen-actions/ (accessed 2026-11-28)
