---
id: kt:process-automation-settings
type: Feature
title: Process Automation Settings
aliases: [Process Automation Settings page, FlowSettings, Flow.settings, Default Workflow User setting]
domain: automation
summary: >-
  The org-wide Setup page that controls how flows and legacy processes behave in an org, including the Default
  Workflow User, the Automated Process User email address, whether flows can be deployed as active, and flow
  runtime and error-email options; in metadata it is the FlowSettings settings type.
release: "Winter '27"
status: current
broader: [kt:process-automation, kt:flow-builder]
related: [kt:schedule-triggered-flow, kt:flow-versioning, kt:workflow-rules, kt:flow-fault-handling, kt:change-sets]
relations:
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: dependsOn, object: kt:apex-testing}
  - {predicate: enables, object: kt:schedule-triggered-flow}
sources:
  - id: s1
    title: "Metadata API Developer Guide: FlowSettings"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_flowsettings.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s2
    title: "Build Flows with Autolaunched and Scheduled Triggers: Schedule a Flow"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/autolaunched-scheduled-flows/schedule-a-flow
    type: official-learning
    accessed: 2026-11-09
  - id: s3
    title: "Your Guide to Determining the Flow Running User and Its Execution Context"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2022/your-guide-to-determining-the-flow-running-user-and-its-execution-context
    type: official-blog
    accessed: 2026-11-09
  - id: s4
    title: "Tooling API: FlowTestCoverage"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/tooling_api_objects_flowtestcoverage.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s5
    title: "Workflow: Automating the Process (cheat sheet)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.salesforce_workflow_cheatsheet.meta/salesforce_workflow_cheatsheet/workflow_cheatsheet.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s6
    title: "Jen's Top Winter '27 Release Features for Admins"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2026/jens-top-winter-27-release-features-for-admins
    type: official-blog
    accessed: 2026-11-09
created: 2026-11-09
---

# Process Automation Settings

**Process Automation Settings** is a single, org-wide page in Setup (found by typing its name in Quick Find) that holds the switches governing how Salesforce's declarative automation runs: who scheduled automation runs as, which address automated emails come from, whether flows can be deployed already active, and a collection of flow runtime behaviours.[^s5][^s2] It has no per-flow scope; every value applies to the whole org. In metadata the same options are exposed as the **FlowSettings** settings type, stored in one `Flow.settings` file in the `settings` directory and available since API version 47.0.[^s1]

## What it controls

**Default Workflow User.** Admins pick a user here who acts as the running user for time-based automation. Salesforce has long told admins to set it before building workflow rules.[^s5] Trailhead's scheduled-flow unit makes it a prerequisite: Salesforce must know which user runs a schedule-triggered flow, so a Default Workflow User should be selected on this page first.[^s2] The Salesforce Admins blog adds a version nuance: schedule-triggered flows saved with an API version below 53.0, or at 53.0 and above without a designated workflow user, run as the **Automated Process** user, which also appears in debug logs whenever it is involved.[^s3]

**Automated Process User Email Address.** When a scheduled flow sends email, this field supplies the sender, and it has to be an organization-wide email address.[^s2]

**Deploy processes and flows as active.** By default, change sets and Metadata API deployments land active flows and processes in production as inactive. Turning this option on lets them arrive active, but the org must then meet a flow test coverage requirement: at least one Apex test has to cover the required share of active processes and autolaunched flows, while flows with screens are exempt.[^s4] Coverage is the number of covered flows and processes divided by the total active ones, and coverage records are deleted whenever the flow version is changed and saved.[^s4] The option appears only in production orgs; it defaults to off there and to on in non-production orgs, and deploying an active flow to production runs Apex tests.[^s1]

**Runtime and error behaviour.** FlowSettings also carries options such as letting users pause screen flows and resume paused interviews shared with them, having Create and Update Records elements skip fields the running user can't edit instead of failing, sending flow error emails to the Apex Exception Email recipients rather than the last person who modified the flow, making flows invoked through the REST API respect the caller's profile and permission sets, and enforcing accurate CPU-time measurement for flows and processes.[^s1] Several older entries are now deprecated or removed, so the metadata reference is the safer guide than old blog checklists.[^s1]

## Limits and gotchas

- Because the page is org-wide, flipping a runtime option changes behaviour for every existing flow at once; test in a sandbox first.[^s1]
- Without a Default Workflow User, schedule-triggered flows fall back to the Automated Process user, and scheduled-flow email needs the sender field to hold an organization-wide address.[^s2][^s3]
- Deploying as active ties every production deployment to Apex flow coverage, and editing a flow resets its coverage records, so coverage has to be rebuilt after changes.[^s4]
- Some FlowSettings fields have no documented default or description, and some apply only to certain API versions (reactive screens, for example, applies only to 57.0 and 58.0).[^s1]

## What changed in Winter '27

Winter '27 added a FlowSettings field, available in API version 68.0, that lets users manage flows, orchestrations and approvals from the Automation Lightning app.[^s1] The Salesforce Admins team also points admins to this page to switch on the beta **Flow Test Mode**, which must be enabled here before Test can be used from Flow Builder.[^s6]

## When to use it (and when not)

Visit it when standing up a new org (set the Default Workflow User and sender address before building scheduled automation), when designing a release process that deploys flows active instead of activating them by hand, and when diagnosing org-wide flow behaviour such as error-email routing.[^s2][^s4][^s1] Manage it as source through FlowSettings so the values are versioned and identical across environments, rather than clicking each org by hand.[^s1] It is not where individual flows are configured; per-flow options such as run context and API version live in each flow's properties.[^s3]

## Connections

The page is a configuration surface for **process automation** in general and for **Flow Builder** flows in particular.[^s1] It **enables** the **schedule-triggered flow**, which needs the running user and sender address it supplies, and it once served **workflow rules** in the same way.[^s2][^s5] Its deploy-as-active option shapes **flow versioning** across orgs and how **change sets** and the **Metadata API** (through which it is also **configured via** FlowSettings) deliver flows, and that option **depends on** **Apex testing** coverage.[^s4][^s1] Its error-email choice decides who hears about unhandled faults, the gap that **flow fault handling** is meant to close.[^s1]

## Sources

[^s1]: Salesforce Developers, "Metadata API Developer Guide: FlowSettings". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_flowsettings.htm (accessed 2026-11-09)
[^s2]: Trailhead, "Build Flows with Autolaunched and Scheduled Triggers: Schedule a Flow". https://trailhead.salesforce.com/content/learn/modules/autolaunched-scheduled-flows/schedule-a-flow (accessed 2026-11-09)
[^s3]: Salesforce Admins Blog, "Your Guide to Determining the Flow Running User and Its Execution Context". https://admin.salesforce.com/blog/2022/your-guide-to-determining-the-flow-running-user-and-its-execution-context (accessed 2026-11-09)
[^s4]: Salesforce Developers, "Tooling API: FlowTestCoverage". https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/tooling_api_objects_flowtestcoverage.htm (accessed 2026-11-09)
[^s5]: Salesforce Developers, "Workflow: Automating the Process (cheat sheet)". https://developer.salesforce.com/docs/atlas.en-us.salesforce_workflow_cheatsheet.meta/salesforce_workflow_cheatsheet/workflow_cheatsheet.htm (accessed 2026-11-09)
[^s6]: Salesforce Admins Blog, "Jen's Top Winter '27 Release Features for Admins". https://admin.salesforce.com/blog/2026/jens-top-winter-27-release-features-for-admins (accessed 2026-11-09)
