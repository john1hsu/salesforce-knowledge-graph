---
id: kt:flow-run-context
type: Concept
title: Flow Run Context
aliases: [flow execution context, flow running user, flow run mode, system context without sharing, system context with sharing, flow user context]
domain: automation
summary: >-
  The security mode a flow runs in (user context, system context with sharing, or system context without sharing)
  together with the user it runs as, which together decide what objects, fields and records each flow type can
  read and change.
release: "Winter '27"
status: current
broader: [kt:flow-builder, kt:salesforce-sharing-model]
related: [kt:screen-flow, kt:record-triggered-flow, kt:schedule-triggered-flow, kt:autolaunched-flow, kt:platform-event-triggered-flow, kt:apex-user-mode]
relations:
  - {predicate: dependsOn, object: kt:field-level-security}
  - {predicate: dependsOn, object: kt:principle-of-least-privilege}
  - {predicate: configuredVia, object: kt:process-automation-settings}
  - {predicate: consumedBy, object: kt:experience-cloud}
sources:
  - id: s1
    title: "Grant Flow Permissions and Context (Trailhead, Flow Implementation 2)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/flow-implementation-2/grant-flow-permissions-and-context
    type: official-learning
    accessed: 2026-11-25
  - id: s2
    title: "Your Guide to Determining the Flow Running User and Its Execution Context"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2022/your-guide-to-determining-the-flow-running-user-and-its-execution-context
    type: official-blog
    accessed: 2026-11-25
  - id: s3
    title: "Security Considerations for Flow Design (Secure Coding Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/secure-coding/guide/secure-coding-considerations-flow-design.html
    type: official-docs
    accessed: 2026-11-25
  - id: s4
    title: "Flow Security (Experience Cloud Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/communities-dev/guide/communities-dev-security-guest-users-flows.html
    type: official-docs
    accessed: 2026-11-25
created: 2026-11-25
---

# Flow Run Context

Every flow interview answers two questions before it touches data: **who** is it running as, and **which security mode** applies to that user. The mode is one of three. In **user context** the flow sees only the objects, fields and records the running user can access. In **system context with sharing** every object and field is available, but record visibility still follows the user's org-wide defaults, sharing rules and manual shares. In **system context without sharing** objects, fields and records are all open, regardless of sharing.[^s1] The secure coding guide describes the same split as user mode (CRUD and field-level security applied automatically), system mode with sharing (sharing applied, CRUD and FLS not enforced) and system mode without sharing (all records returned).[^s3]

## Defaults by flow type

Salesforce's Trailhead summary, which it calls simplified, gives these defaults:[^s1]

- Record-triggered and schedule-triggered flows: system context without sharing, with no alternative mode.[^s1]
- Screen flows: user context by default, optionally system context with or without sharing.[^s1]
- Autolaunched flows: inherit the context of whatever started them, optionally fixed to with or without sharing.[^s1]

The Admins blog adds that platform event-triggered flows also run in system context without sharing, that an autolaunched flow invoked from Apex always runs in system mode without sharing, and that a screen flow called as a subflow inherits its parent's context unless set otherwise.[^s2] The secure coding guide frames the rule more broadly: flows started from the UI default to user mode, other flows default to system mode without sharing, and flows called from Apex take on the calling Apex context.[^s3] Because these statements differ slightly at the edges, the guide recommends always setting the execution context explicitly in the flow's advanced run-mode settings rather than relying on a default.[^s3]

## Who the flow runs as

Context only matters relative to a user. Apart from schedule-triggered flows, flows run as the **current user**: the person who created or last modified the triggering record, or who clicked the action, launched the subflow or otherwise started the interview.[^s2] Schedule-triggered flows run as the Automated Process user when the flow's "API Version for Running the Flow" is below 53.0, or when it is 53.0 or later and no Default Workflow User is set in Process Automation Settings; otherwise they run as that default workflow user.[^s2] Standard platform events are sometimes published by the Automated Process user, and debug logs record such flows under that user.[^s2]

Permission to start a flow at all is separate from the mode it runs in. A user needs either the **Flow User** checkbox on the user record or the **Run Flows** permission from a profile or permission set; Run Flows covers any active flow whose access is not restricted, while running inactive flows needs **Manage Flow**.[^s1] Even then, a flow in user context fails if the user lacks, say, Create on Case or edit access to a field it sets.[^s1]

## Gotchas

- Even inside a system-context screen flow, components that query the database themselves (lookups, address, dependent picklists, file upload) still apply the running user's permissions.[^s2]
- Flows behave like global classes with no IP protection; anyone allowed to run a screen flow can start it with their own inputs and cancel it.[^s3][^s4]
- Users who can run a subflow can read its outputs and change its inputs, so grant access to the top-level flow only.[^s4]
- Record-triggered flows run in system mode, so when they change unrelated records Salesforce advises limiting what they do and checking authorization.[^s3]

## Recommended practice

Salesforce's guidance is least privilege: give each user only what the job needs, and restrict access to specific flows instead of relying on broad Run Flows.[^s1] The Admins blog says system context without sharing should be used sparingly.[^s2] The secure coding guide recommends that screen flows run in user mode, that privileged steps live in small system-mode subflows called from unprivileged parent flows, that inputs marked available for input be validated, and that flow names reveal their mode so reviewers can spot privileged ones.[^s3] For guest and external users of Experience Cloud sites, Salesforce recommends overriding the default run-flow permission so only named site guest profiles, external profiles or permission sets can run a flow, and avoiding system context where possible.[^s4]

## Connections

Run context sits under **Flow Builder**, where the mode is chosen, and under the **sharing model**, which supplies the record rules that "with sharing" enforces.[^s1] It decides how **screen**, **record-triggered**, **schedule-triggered**, **platform event-triggered** and **autolaunched** flows behave, and it depends on **field-level security** and object permissions when a flow runs in user context.[^s1][^s3] The scheduled-flow running user is configured through **Process Automation Settings**.[^s2] It is the flow counterpart of **Apex user mode**, which the secure coding guide suggests for custom access checks, and it is a recurring concern for **Experience Cloud** sites that expose flows to guests.[^s3][^s4] The whole topic applies the **principle of least privilege**.[^s1]

## Sources

[^s1]: Salesforce Trailhead, "Grant Flow Permissions and Context" (Flow Implementation 2). https://trailhead.salesforce.com/content/learn/modules/flow-implementation-2/grant-flow-permissions-and-context (accessed 2026-11-25)
[^s2]: Salesforce Admins Blog, "Your Guide to Determining the Flow Running User and Its Execution Context". https://admin.salesforce.com/blog/2022/your-guide-to-determining-the-flow-running-user-and-its-execution-context (accessed 2026-11-25)
[^s3]: Salesforce Developers, "Security Considerations for Flow Design", Secure Coding Guide. https://developer.salesforce.com/docs/platform/secure-coding/guide/secure-coding-considerations-flow-design.html (accessed 2026-11-25)
[^s4]: Salesforce Developers, "Flow Security", Experience Cloud Developer Guide. https://developer.salesforce.com/docs/platform/communities-dev/guide/communities-dev-security-guest-users-flows.html (accessed 2026-11-25)
