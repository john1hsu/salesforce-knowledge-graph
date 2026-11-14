---
id: kt:process-builder
type: Feature
title: Process Builder
aliases: [Lightning Process Builder, Salesforce Process Builder, Process Builder processes, invocable process]
domain: automation
summary: >-
  Salesforce's legacy point-and-click tool for building "processes" that run actions when a record changes, a
  platform event arrives or another process invokes them; support and bug fixes ended December 31, 2025, existing
  processes still run, and Salesforce directs customers to migrate them to Flow with the Migrate to Flow tool.
release: "Winter '27"
status: deprecated
broader: [kt:process-automation]
related: [kt:workflow-rules, kt:platform-events, kt:order-of-execution, kt:technical-debt-in-salesforce, kt:migrate-to-flow-tool]
relations:
  - {predicate: replacedBy, object: kt:record-triggered-flow}
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: contrastsWith, object: kt:flow-builder}
sources:
  - id: s1
    title: "Process Builder"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=platform.process_overview.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-04
  - id: s2
    title: "Process Limits"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=platform.process_limits.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-04
  - id: s3
    title: "Salesforce Workflow Rules & Process Builder End of Support"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&amp=&id=001096524&amp=&type=1
    type: official-docs
    accessed: 2026-11-04
  - id: s4
    title: "Migrate Workflows and Processes to Flows: Understand Automation Changes"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/migrate-workflows-and-processes-to-flows/understand-automation-changes
    type: official-learning
    accessed: 2026-11-04
  - id: s5
    title: "Subscribe to Platform Event Messages with Processes"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_subscribe_process.htm
    type: official-docs
    accessed: 2026-11-04
  - id: s6
    title: "Automate This! Migrate Workflow Rules and Processes to Flow"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2022/automate-this-migrate-workflow-rules-and-processes-to-flow
    type: official-blog
    accessed: 2026-11-04
created: 2026-11-04
---

# Process Builder

Process Builder is a declarative automation tool in which an admin assembles a "process" on a visual canvas: criteria decide when a group of actions should fire, and the actions do routine work such as creating or updating records, sending emails or posting to Chatter.[^s1] It was the successor to workflow rules for many years, but Salesforce now recommends Flow Builder for all new automation. Support and updates for Process Builder ended on December 31, 2025, and Salesforce no longer fixes bugs in it; processes that are already active keep running, and admins can still activate, deactivate and edit them.[^s1][^s3] For a practitioner today, Process Builder is legacy automation to inventory and migrate, not a tool to design with.

## How it works

A process belongs to one of three types. A **record change** process starts when a record is created or updated; an **event** process starts when a platform event message is received; and an **invocable** process starts only when something else, such as another process, calls it.[^s1] Each criteria node gates an action group, and action groups hold immediate actions and, for record change processes only, scheduled actions.[^s1] The built-in actions include Create a Record, Update Records, Invoke a Process, Post to Chatter, Use a Quick Action, Send an Email, Send a Custom Notification, Submit for Approval, a set of Quip actions, and the two escape hatches, Launch a Flow and Call Apex Code, for logic the canvas cannot express.[^s1]

Event processes subscribe automatically once their trigger names a platform event and a related object. They evaluate messages in replay-ID order, in batches of up to 2,000 messages, asynchronously and in their own transaction. Debug logs appear under the Automated Process user, but actions run as the user who published the event, so audit fields point to the publisher. When processes, flows and paused flow interviews all subscribe to the same event, their order is not guaranteed.[^s5]

## Limits and gotchas

Processes share the Apex governor limits of the transaction that fired them, and if anything they launch pushes the total over a limit, the whole transaction rolls back.[^s2] Every Create a Record or quick action costs one DML statement, and every Update Records action costs one SOQL query plus one DML statement.[^s2] In Enterprise, Unlimited, Performance and Developer Editions an org can hold 4,000 processes and 2,000 active processes per process type (5 of each in Essentials and Professional). Each process allows 50 versions and 200 criteria nodes. Process API names must be unique across all processes and flows.[^s2] Salesforce's admin team also noted design-level costs: every process adds an initialization phase to each save it takes part in, and many processes consume resources even when no criteria match.[^s6] To find what is still live, sort the Status column on the Process Builder page under Setup > Process Automation.[^s3]

## Migration to Flow

The Migrate to Flow tool converts record change processes whose actions are record create, record update, invoke flow, invoke Apex and email alert. It does not convert event or invocable processes, processes with scheduled actions or field traversals, or invocable actions. Other actions migrate partially and are flagged for follow-up in Flow Builder.[^s4] After migration, a recursive process evaluates the record only once, so test it. Invoked flows that make callouts or pause should move to an asynchronous path.[^s4] Salesforce's advice is to review automation before converting it rather than translate it one-to-one. Retire dead processes, split complex ones into a flow per decision point, merge simple ones on the same object into a fast-field-update flow, and put scheduled actions in their own flow.[^s6]

## When to use it (and when not)

Do not build new processes. Salesforce positions Flow Builder as the primary automation tool. Entry conditions, Fast Field Updates, a single tool to debug and Flow Trigger Explorer for ordering all favour flows.[^s4][^s3] The only reason to open Process Builder is to understand, deactivate or temporarily patch an existing process while its flow replacement is built and tested.[^s1][^s3]

## Connections

Process Builder sits under the broader **process-automation** toolset and is **replaced by record-triggered flows** built in **Flow Builder**, which it **contrasts with** as the older, design-time model.[^s4][^s6] It ended support on the same date as its sibling, **workflow rules**.[^s3] Event processes are a legacy subscriber to **platform events**, and every process is **governed by** the transaction's **governor limits**.[^s5][^s2] Processes add steps to the save **order of execution** and are a standard item on a **technical debt** register until they are migrated.[^s6][^s3]

## Sources
[^s1]: Salesforce Help, "Process Builder". https://help.salesforce.com/s/articleView?id=platform.process_overview.htm&language=en_US&type=5 (accessed 2026-11-04)
[^s2]: Salesforce Help, "Process Limits". https://help.salesforce.com/s/articleView?id=platform.process_limits.htm&language=en_US&type=5 (accessed 2026-11-04)
[^s3]: Salesforce Help, "Salesforce Workflow Rules & Process Builder End of Support". https://help.salesforce.com/s/articleView?language=en_US&amp=&id=001096524&amp=&type=1 (accessed 2026-11-04)
[^s4]: Trailhead, "Migrate Workflows and Processes to Flows: Understand Automation Changes". https://trailhead.salesforce.com/content/learn/projects/migrate-workflows-and-processes-to-flows/understand-automation-changes (accessed 2026-11-04)
[^s5]: Salesforce Developers, "Subscribe to Platform Event Messages with Processes". https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_subscribe_process.htm (accessed 2026-11-04)
[^s6]: Salesforce Admins Blog, "Automate This! Migrate Workflow Rules and Processes to Flow". https://admin.salesforce.com/blog/2022/automate-this-migrate-workflow-rules-and-processes-to-flow (accessed 2026-11-04)
