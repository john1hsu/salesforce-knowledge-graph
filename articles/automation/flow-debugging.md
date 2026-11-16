---
id: kt:flow-debugging
type: Feature
title: Flow Debugging
aliases: [debug a flow, Flow Builder debug, flow debug panel, debug flows as another user, flow debug details]
domain: automation
summary: >-
  The Debug capability of Flow Builder, which runs a flow interview with chosen inputs, optionally as another user or
  in rollback mode, and shows element-by-element debug details, complemented by Workflow-category debug logs and
  flow error emails for failures outside the builder.
release: "Winter '27"
status: current
broader: [kt:flow-builder]
related: [kt:flow-tests, kt:flow-fault-handling, kt:record-triggered-flow, kt:screen-flow, kt:process-automation-settings]
relations:
  - {predicate: configuredVia, object: kt:process-automation-settings}
  - {predicate: dependsOn, object: kt:salesforce-sharing-model}
  - {predicate: integratesWith, object: kt:apex-logging-and-debug-logs}
  - {predicate: contrastsWith, object: kt:flow-tests}
sources:
  - id: s1
    title: "Make Sure Your Flow Works (Flow Testing and Distribution module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/content/learn/modules/flow-testing-and-distribution/make-sure-your-flow-works
    type: official-learning
    accessed: 2026-11-16
  - id: s2
    title: "Debug Flows as Another User (Flow Implementation 2 module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/flow-implementation-2/debug-flows-as-another-user
    type: official-learning
    accessed: 2026-11-16
  - id: s3
    title: "Fix Access Issues in a Flow (Flow Troubleshooting module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/flow-troubleshooting/fix-access-issues-in-a-flow
    type: official-learning
    accessed: 2026-11-16
  - id: s4
    title: "Process Automation Settings"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.automation_about_settings.htm&amp=&type=5
    type: official-docs
    accessed: 2026-11-16
  - id: s5
    title: "Working with Logs in the Developer Console (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_debugging_system_log_console.htm
    type: official-docs
    accessed: 2026-11-16
  - id: s6
    title: "Salesforce Winter '26 Release: The New Debug Panel in Flow Builder"
    publisher: Salesforce Ben
    url: https://www.salesforceben.com/salesforce-winter-26-release-the-new-debug-panel-in-flow-builder/
    type: community
    accessed: 2026-11-16
created: 2026-11-16
---

# Flow Debugging

Flow debugging is how admins find out why a flow did, or did not, do what they expected. Inside Flow Builder the button bar offers both **Run** and **Debug**. Run executes the most recently saved version of the open flow; Debug does the same but also lets the builder supply values for input variables and display debug details while the flow runs.[^s1] Every run starts a **flow interview**, an instance of the flow whose input data decides which path it follows, so debugging is really the inspection of one interview.[^s1]

## How it works

For a screen flow, choosing to show details places the screens on one side and the debug details on the other, adding a new entry as the user steps through each screen.[^s1] The details record who started the interview, how screen inputs were stored in variables, whether a Get Records element found a match, which outcome a decision took and what each data element did; a final "Transaction Committed" entry shows that the changes were saved.[^s1] When an element fails, the details tab shows its error message and the records it tried to change.[^s2]

The debug options depend on the flow type. The Flow Implementation 2 unit describes two key switches:[^s2]

- **Run automation as another user** executes the interview with the chosen user's permissions.[^s2]
- **Run automation in rollback mode** stops the debug run from changing data; without it, the run commits its changes.[^s2]

For record-triggered flows, the debugger takes a triggering record and a **Convert to Test** action turns the debug inputs into a flow test, mapping the triggering record to the test's initial record and the field changes to its updated record.[^s2] Salesforce Ben reports that the Winter '26 release moved the options into a left-side **debug panel**, grouped the results into searchable summary cards with a link back to each element on the canvas, and split screen-flow debugging into a Screen tab and a Flow Canvas tab.[^s6]

## Debugging as another user

Testing only as an administrator hides permission problems, so the debugger can impersonate a target user.[^s2] An admin first enables **Let admins debug flows as other users** in Process Automation Settings.[^s2] Salesforce Help states that the option lets users with Manage Flow and View All Data choose the running user, and that the setting is available only in sandbox environments.[^s4] Record changes and actions then run as that user, governed by their profile and permission sets, unless the flow always runs in system context, which ignores those object and field permissions.[^s4]

Trailhead's troubleshooting example shows the payoff: a debug run as a sales associate failed on a Create Records element, which traced back to a profile that could not create opportunities, and assigning a permission set fixed it.[^s3] Another unit traces an insufficient-access error on a task to an autolaunched flow running in system context with sharing against a Private activities default; it suggests changing the flow's run context instead of loosening org-wide security, while still applying least privilege.[^s2]

## Beyond the builder: errors in running flows

Not every failure can be reproduced on the canvas. When a flow interview fails, Salesforce sends an error email listing what ran, what failed and the data involved, including user-entered data.[^s4] **Send Process or Flow Error Email to** in Process Automation Settings decides whether it goes to the user who last modified the flow or to the Apex exception email recipients.[^s4] Trailhead adds that the email is written in the running user's default language and that common root causes include wrong fields or variables, the running user's object and field-level security, too many SOQL queries and null values.[^s3]

For automations triggered by other transactions, **debug logs** fill the gap. The Workflow log category carries flow events: interview start, finish, error and pause, element begin, end and error, fault paths, assignment, loop and subflow detail, limit usage, and flow action events.[^s5] Log levels are cumulative from NONE to FINEST, and most Workflow events log between INFO and FINER.[^s5]

## Limits and gotchas

- Debug runs work against the org's real data, so Trailhead recommends debugging in a sandbox and using rollback mode.[^s3][^s2]
- Debugging as another user requires the Process Automation Setting, both Manage Flow and View All Data, and a sandbox.[^s4]
- System-context flows ignore the impersonated user's object and field access, so a clean debug run there proves little about permissions.[^s4]
- Error emails can contain user-entered data, so choose the recipients deliberately.[^s4]

## When to use it (and when not)

Use Debug while building and whenever a reported failure can be reproduced with known inputs; use the "as another user" option for permission bugs. Debugging is manual and one-off, so once a path behaves correctly, capture it as a **flow test** (Convert to Test for record-triggered flows) to guard against regressions.[^s2] For failures in production or inside bulk transactions, rely on error emails and Workflow-category debug logs instead.[^s4][^s5]

## Connections

Flow debugging is a capability of **Flow Builder** and is enabled and tuned through **Process Automation Settings**.[^s1][^s4] It feeds and contrasts with **flow tests**: debug is exploratory, tests are repeatable.[^s2] Impersonation exposes the **sharing model** and permission sets, and failures it reveals are often handled with **flow fault handling**.[^s3] The **debug logs** of the Workflow category extend debugging to flows that run outside the builder, such as **record-triggered flows** fired by other transactions.[^s5]

## Sources

[^s1]: Trailhead, "Make Sure Your Flow Works (Flow Testing and Distribution module)". https://trailhead.salesforce.com/en/content/learn/modules/flow-testing-and-distribution/make-sure-your-flow-works (accessed 2026-11-16)
[^s2]: Trailhead, "Debug Flows as Another User (Flow Implementation 2 module)". https://trailhead.salesforce.com/content/learn/modules/flow-implementation-2/debug-flows-as-another-user (accessed 2026-11-16)
[^s3]: Trailhead, "Fix Access Issues in a Flow (Flow Troubleshooting module)". https://trailhead.salesforce.com/content/learn/modules/flow-troubleshooting/fix-access-issues-in-a-flow (accessed 2026-11-16)
[^s4]: Salesforce Help, "Process Automation Settings". https://help.salesforce.com/s/articleView?language=en_US&id=platform.automation_about_settings.htm&amp=&type=5 (accessed 2026-11-16)
[^s5]: Salesforce Developers, "Working with Logs in the Developer Console (Apex Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_debugging_system_log_console.htm (accessed 2026-11-16)
[^s6]: Salesforce Ben, "Salesforce Winter '26 Release: The New Debug Panel in Flow Builder". https://www.salesforceben.com/salesforce-winter-26-release-the-new-debug-panel-in-flow-builder/ (accessed 2026-11-16)
