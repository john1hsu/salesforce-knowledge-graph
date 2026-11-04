---
id: kt:flow-fault-handling
type: Pattern
title: Flow Fault Handling
aliases: [flow fault path, fault connector, flow error handling, $Flow.FaultMessage]
domain: automation
summary: >-
  The practice of routing a failing Flow Builder element down a fault connector (fault path) to recover,
  notify or log, using $Flow.FaultMessage, Roll Back Records and Custom Error to control what is saved
  and what the user sees.
release: "Winter '27"
status: current
broader: [kt:flow-builder, kt:process-automation]
related: [kt:record-triggered-flow, kt:screen-flow, kt:autolaunched-flow, kt:transaction-control]
relations:
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: integratesWith, object: kt:code-analyzer}
  - {predicate: dependsOn, object: kt:order-of-execution}
sources:
  - id: s1
    title: "Flow Implementation 2: Roll Back Changes After an Error"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/flow-implementation-2/roll-back-changes-after-an-error
    type: official-learning
    accessed: 2026-11-04
  - id: s2
    title: "Other Examples of Error Handling in Flows"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=platform.flow_build_logic_fault_examples.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-04
  - id: s3
    title: "Troubleshooting Flow Run Time Errors"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.flow_troubleshoot_email.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-04
  - id: s4
    title: "Flow Scanner Rules Reference (Salesforce Code Analyzer)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-code-analyzer/guide/rules-flow.html
    type: official-docs
    accessed: 2026-11-04
  - id: s5
    title: "The Ultimate Guide to Flow Best Practices and Standards"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2021/the-ultimate-guide-to-flow-best-practices-and-standards
    type: official-blog
    accessed: 2026-11-04
created: 2026-11-04
---

# Flow Fault Handling

Flow fault handling is how a Flow Builder flow decides what happens when one of its elements fails. Any element that can fail — record operations, actions, subflows — can be given a **fault connector**, a separate outgoing path the flow follows instead of the normal connector when that element throws an error.[^s2][^s4] The error text is available on that path in the global variable `$Flow.FaultMessage`, which builders surface on a screen, put into a notification, or store in a log or case record.[^s2] Salesforce's admin guidance names skipped fault paths as one of the most common flow-building mistakes, and recommends deciding up front who gets notified and whether failures are logged.[^s5]

## How it works

A flow runs inside a database transaction. If it fails without a fault path, the platform rolls back that transaction's changes so nothing is partially saved.[^s1] Adding a fault path changes this: the error is treated as handled, the flow continues down the fault branch, and work done earlier in the transaction is **not** automatically undone.[^s1] That trade-off is the core design decision — a fault path buys a friendlier outcome at the risk of partial completion (for example, an account marked Active without its matching onboarding case).[^s1]

Two elements let builders restore all-or-nothing behaviour on a fault path:

- **Roll Back Records** (screen flows) undoes the current transaction only. A Screen element ends one transaction and starts another, so changes committed before an earlier screen are not reverted. Place the rollback *before* any error screen, because the flow pauses at screens and the user may close the window rather than continue.[^s1]
- **Custom Error** (record-triggered flows) shows a message to the user, rolls back the current transaction and blocks the triggering save. It can also be used on a normal path as a declarative validation — including on deletes, where validation rules don't run. Its message is capped at 255 characters.[^s1]

In a record-triggered flow the difference is visible to users: with no fault path, an error shows a message and blocks the triggering change; with a fault path, the triggering change still completes even though the flow failed.[^s1]

## Common patterns

Salesforce documents several fault-path designs: send the user back to a screen to correct inputs; display the error and ask them to contact IT; automatically create a case containing the fault message and show the case number; or deliberately ignore an error by pointing the fault connector at the same element as the normal connector.[^s2] For consistency across many flows, the admin best-practices guide recommends a shared error-handling subflow that receives `$Flow.FaultMessage` and sends one standard email or screen, and, in larger orgs, logging flow errors alongside Apex errors in a log object.[^s5] Several fault connectors in one flow can point to the same Custom Error element.[^s1]

## Limits and gotchas

- Unhandled failures generate an error email to either the admin who last modified the flow or the Apex exception email recipients; it includes the flow name and version, the failing element, a stack trace and links back to Flow Builder. A failure across a batch of interviews can produce several emails or one combined email, and an email may still be sent even when a fault connector exists.[^s3]
- Debugging is harder when the error originates in a subflow called from Apex or Lightning components, because detailed errors aren't always returned.[^s5]
- Rollback tools are flow-type specific; in flow types without one, weigh whether partial completion is acceptable before adding a fault path.[^s1]
- Fault paths don't fix design problems such as DML inside loops, which exhaust per-transaction governor limits; Code Analyzer's Flow Scanner flags that separately.[^s4]

## When to use it

Add fault paths to every element that can fail when users need a clear message or support needs a record of the error; leave an element unhandled (or use Custom Error) when an all-or-nothing rollback is the safer outcome.[^s1][^s5] Salesforce Code Analyzer's Flow Scanner enforces this as a high-severity **MissingFaultHandler** rule covering DML elements, actions and subflows.[^s4]

## Connections

Fault handling is a practice within **Flow Builder** and wider **process automation**, applied differently in **record-triggered flows** (Custom Error, blocking saves), **screen flows** (Roll Back Records, error screens) and **autolaunched flows**.[^s1] Its rollback semantics are an instance of **transaction control** and interact with the save **order of execution**.[^s1] Static checks for missing fault handlers come from **Code Analyzer**, whose companion rules target patterns that breach **governor limits**.[^s4]

## Sources

[^s1]: Trailhead, "Flow Implementation 2: Roll Back Changes After an Error". https://trailhead.salesforce.com/content/learn/modules/flow-implementation-2/roll-back-changes-after-an-error (accessed 2026-11-04)
[^s2]: Salesforce Help, "Other Examples of Error Handling in Flows". https://help.salesforce.com/s/articleView?id=platform.flow_build_logic_fault_examples.htm&language=en_US&type=5 (accessed 2026-11-04)
[^s3]: Salesforce Help, "Troubleshooting Flow Run Time Errors". https://help.salesforce.com/s/articleView?id=sf.flow_troubleshoot_email.htm&language=en_US&type=5 (accessed 2026-11-04)
[^s4]: Salesforce Developers, "Flow Scanner Rules Reference". https://developer.salesforce.com/docs/platform/salesforce-code-analyzer/guide/rules-flow.html (accessed 2026-11-04)
[^s5]: Salesforce Admins Blog, "The Ultimate Guide to Flow Best Practices and Standards". https://admin.salesforce.com/blog/2021/the-ultimate-guide-to-flow-best-practices-and-standards (accessed 2026-11-04)
