---
id: kt:schedule-triggered-flow
type: Feature
title: Schedule-Triggered Flow
aliases: [schedule-triggered flows, scheduled flow, scheduled flows, scheduled-triggered flow]
domain: automation
summary: >-
  The Flow Builder flow type that starts itself at a set date, time and frequency (once, daily or weekly) and runs
  in the background over the batch of records that match its object and filter conditions, independent of any
  record change.
release: "Winter '27"
status: current
broader: [kt:flow-builder, kt:process-automation]
related: [kt:record-triggered-flow, kt:autolaunched-flow, kt:flow-fault-handling]
relations:
  - {predicate: alternativeTo, object: kt:batch-apex}
  - {predicate: alternativeTo, object: kt:scheduled-apex}
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: configuredVia, object: kt:process-automation-settings}
sources:
  - id: s1
    title: "Autolaunched and Scheduled Flows: Schedule a Flow"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/autolaunched-scheduled-flows/schedule-a-flow
    type: official-learning
    accessed: 2026-11-05
  - id: s2
    title: "Schedule-Triggered Flow Limits and Considerations"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.flow_considerations_trigger_schedule.htm&type=5
    type: official-docs
    accessed: 2026-11-05
  - id: s3
    title: "What Is a Schedule-Triggered Flow?"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2023/what-is-a-schedule-triggered-flow
    type: official-blog
    accessed: 2026-11-05
created: 2026-11-05
---

# Schedule-Triggered Flow

A schedule-triggered flow is a Flow Builder flow that runs in the background at a time you set rather than in response to a record being created, updated or deleted.[^s1] Trailhead places it in the broader autolaunched family of background flows, and positions it for work that should happen at a fixed time, on a daily or weekly cadence, or across many records at once: escalating long-open cases, reminding owners about missing field values, or applying overnight batch updates.[^s1] The Admins blog adds typical examples such as deactivating users who have not logged in for a set period, overdue-payment reminders and one-off bulk field updates.[^s3]

## How it works

In the Start element you choose **Set Schedule** and enter a start date, a start time and a frequency of once, daily or weekly.[^s1][^s3] The schedule follows the org's default time zone from Company Information, not the builder's personal time zone, so check that setting first.[^s1][^s2] Runs are never retroactive: if you activate the flow after its start time has passed, the first run is the next scheduled occurrence, and a one-time flow whose date and time have already passed doesn't run at all.[^s1][^s2]

You can optionally choose **one object** and filter conditions (or run for all records of that object).[^s1] When an object is chosen, the flow's query finds the matching records at run time and processes them as a batch, with `$Record` (shown in some elements as "Triggering Account" and so on) standing for each record in turn; an Update Records element can then update the triggering records in one batch or reach related records such as an account's contacts.[^s1] Without an object, `$Record` is unavailable and the flow simply runs its logic once on schedule.[^s1] Each record retrieved creates one flow interview, and the query batch size defaults to 200 and can be set anywhere from 1 to 200; smaller batches slow processing.[^s2]

The flow runs as the **Default Workflow User** set in Process Automation Settings, so that setting must be filled in; if the flow sends email, the Automated Process User Email Address must match an organization-wide email address.[^s1][^s2] A schedule-triggered flow can't be started any other way than by its schedule.[^s2]

## Limits and gotchas

- **Interview cap.** One flow can create up to 250,000 schedule-triggered interviews, and across all flows the 24-hour limit is 250,000 or the org's user licenses times 200, whichever is greater. Hitting it triggers a flow error email, so size the schedule and filters accordingly.[^s2]
- **Activation permissions.** Activating an autolaunched flow with a trigger requires View All Data, and activation checks Manage Data Export, which interacts with high-assurance session policies.[^s2]
- **Callouts.** A flow processing a batch of records on API version 63.0 or later can make callouts without a Wait element; otherwise a Wait element is needed before callouts, external objects or External Services actions.[^s2]
- **Apex.** Synchronous Apex invoked from the flow counts against synchronous per-transaction limits, and if the "Require User Access to Apex Classes Invoked by Flow" release update is enabled, schedule-triggered flows that call Apex fail.[^s2]
- **Partial failures.** When a records element hits failures on some records, Salesforce rolls back and retries the successful ones; if a later element touches the same failed records, the whole transaction fails.[^s2] Plan fault handling around this.
- **Updating with all `$Record` fields** requires "Filter inaccessible fields from flow requests," or the flow fails on read-only and system fields.[^s2]
- **Operations.** Future runs appear on Setup's Scheduled Jobs page; deleting the job there cancels all future runs, and deactivating then reactivating the flow restores them.[^s2][^s3] After a sandbox refresh, flows that were active can run immediately in the new copy.[^s2] The `SCHEDULED_FLOW_DETAIL` debug-log event shows how many records a run processed.[^s2] Debugging in Flow Builder always uses the oldest matching record, so the Admins blog suggests putting testable logic in a subflow.[^s3]

## When to use it (and when not)

Use a schedule-triggered flow for periodic, time-of-day work over a filtered set of records that admins should own.[^s1][^s3] If the timing should be relative to a particular record's date or change, use a scheduled path on a record-triggered flow instead, which runs once per triggering event.[^s1] The Admins blog frames it as the low-code alternative to scheduled batch Apex, but notes the trade-offs: batch Apex handles far larger volumes (it cites roughly 50,000 queried records for a flow versus up to 50 million for batch Apex), bigger batches (2,000 versus 200) and more flexible schedules such as hourly or monthly. For large data volumes or complex schedules, Apex is the better fit.[^s3]

## Connections

It is one of the flow types built in **Flow Builder** and part of the broader **process-automation** toolset.[^s1] It contrasts with the **record-triggered flow**, whose scheduled paths fire relative to a record event, and with the no-trigger **autolaunched flow**, which only runs when something calls it; its logic is often factored into such a subflow for testing.[^s1][^s3] It is an **alternative to batch Apex** and **scheduled Apex** for periodic processing.[^s3] It is **governed by** per-transaction **governor limits** plus its own 24-hour interview cap, and it is **configured via** **Process Automation Settings**, which supply its running user.[^s2] Its partial-failure and rollback behaviour makes **flow fault handling** essential.[^s2]

## Sources

[^s1]: Trailhead, "Autolaunched and Scheduled Flows: Schedule a Flow". https://trailhead.salesforce.com/content/learn/modules/autolaunched-scheduled-flows/schedule-a-flow (accessed 2026-11-05)
[^s2]: Salesforce Help, "Schedule-Triggered Flow Limits and Considerations". https://help.salesforce.com/s/articleView?language=en_US&id=platform.flow_considerations_trigger_schedule.htm&type=5 (accessed 2026-11-05)
[^s3]: Salesforce Admins Blog, "What Is a Schedule-Triggered Flow?". https://admin.salesforce.com/blog/2023/what-is-a-schedule-triggered-flow (accessed 2026-11-05)
