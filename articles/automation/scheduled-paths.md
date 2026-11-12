---
id: kt:scheduled-paths
type: Feature
title: Scheduled Paths
aliases: [scheduled path, flow scheduled paths, record-triggered flow scheduled path, time-based flow actions]
domain: automation
summary: >-
  An optional branch of an after-save record-triggered flow whose elements run later than the triggering save,
  at an offset before or after the triggering event or a date/time field on the record, processed asynchronously
  in batches and monitored from the Time-Based Automations page.
release: "Winter '27"
status: current
broader: [kt:record-triggered-flow, kt:process-automation]
related: [kt:schedule-triggered-flow, kt:flow-fault-handling, kt:asynchronous-apex]
relations:
  - {predicate: replaces, object: kt:workflow-rules}
  - {predicate: alternativeTo, object: kt:queueable-apex}
  - {predicate: alternativeTo, object: kt:future-methods}
  - {predicate: configuredVia, object: kt:process-automation-settings}
  - {predicate: governedBy, object: kt:governor-limits}
sources:
  - id: s1
    title: "Scheduled Paths"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.flow_concepts_trigger_scheduled_path.htm&type=5
    type: official-docs
    accessed: 2026-11-12
  - id: s2
    title: "Record-Triggered Flows: Add a Scheduled Task to Your Flow"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/record-triggered-flows/add-a-scheduled-task-to-your-flow
    type: official-learning
    accessed: 2026-11-12
  - id: s3
    title: "Schedule Your Path in Salesforce Flow"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2021/03/schedule-your-path-in-salesforce-flow
    type: official-blog
    accessed: 2026-11-12
  - id: s4
    title: "How I Solved It: Run a Flow Scheduled Path Based on a Field Change"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2022/how-i-solved-it-run-a-flow-scheduled-path-based-on-a-field-change
    type: official-blog
    accessed: 2026-11-12
  - id: s5
    title: "Asynchronous Processing on the Lightning Platform"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/fundamentals/guide/async-fundamentals.html
    type: official-docs
    accessed: 2026-11-12
created: 2026-11-12
---

# Scheduled Paths

A scheduled path is an optional branch of a record-triggered flow whose elements are queued when the triggering record change happens but run at a later time.[^s1][^s2] Trailhead's examples show the range of uses: act 6 hours after a case is created, 2 days after an account's renewal date, or 1 month before a warranty expires.[^s2] Scheduled paths arrived in Spring '21 as the flow-based way to do time-relative work on a record, the job that workflow rules handled with time-dependent actions.[^s3]

## How it works

You add scheduled paths from the flow's Start element. Each path gets a label (the API name is generated from it), a **time source**, and an **offset**.[^s1][^s2] The time source is either the moment of the triggering event or a date or date/time field on the record, such as an opportunity's Close Date.[^s1][^s2] The offset is a number plus a direction and unit, for example "5 Days After". Units run from minutes to months, and an offset of 0 means no delay.[^s1][^s2] One flow can hold several paths, so a single trigger can send a confirmation now, an email the day before an appointment and an SMS an hour before it.[^s3]

Scheduled paths are only available in flows that run on **Actions and Related Records** (after-save), not in fast-field-update flows.[^s2] With the update setting "Only when a record is updated to meet the condition requirements", a path is scheduled only when the record's prior version did not meet the entry conditions and the new version does.[^s1] Conditions are re-evaluated on every later update. A pending path stays queued while the conditions remain true and is cancelled once an update makes them false.[^s1] If the time-source field moves to a new future date, the path is rescheduled. The Developers blog shows a test-drive reminder replaced, not duplicated, when the appointment time was edited.[^s1][^s3]

Scheduled paths run in system context, with access to all data. Actions are attributed to the user who changed the record.[^s1] Before you can build one, the **Default Workflow User** must be set in Process Automation Settings. Salesforce uses that user when the triggering user is inactive.[^s1][^s2] Records due in the same minute are grouped into batches. The batch size defaults to 200, which is also the maximum, and can be as low as 1. Lowering it helps a path's actions stay within Apex governor limits.[^s1]

## Limits and gotchas

- **24-hour interview cap.** An org can run up to 250,000 scheduled-path interviews per 24 hours, or its user licenses times 200, whichever is greater. Paths that run immediately don't count, and overflow waits until the limit resets.[^s1]
- **No prior values.** `$Record__Prior` isn't supported in scheduled-path elements or in entry-condition formulas.[^s1] The Admins blog adds that "is changed" checks on the path don't behave as expected. Its fix is a before-save flow that sets a switch field for the scheduled path to read and reset.[^s4]
- **Retries.** A failed interview sends an error email and is retried up to 5 times, at about 15, 30, 60, 120 and 240 minutes. In a mixed-result bulk run, the batch rolls back and the successful interviews retry immediately, up to 2 times.[^s1]
- **Limits context.** Asynchronous limits apply, but synchronous Apex the flow calls counts against synchronous per-transaction limits.[^s1] A scheduled path that tries to schedule itself again fails with `MAX_DEPTH_IN_FLOW_EXECUTION`.[^s1]
- **Deactivation.** Deactivating the flow cancels pending work, but the items stay listed until their scheduled time. If a new active version exists by then, they run under that version.[^s1]
- **No SLA.** Like other asynchronous flow work, scheduled paths have no service-level guarantee and run when resources are available.[^s5]

## Monitoring and testing

Pending paths are listed on the **Time-Based Automations** Setup page. Its Scheduled Date column shows the next attempt, but the retry count isn't displayed.[^s1] Debug logs record `FLOW_SCHEDULED_PATH_QUEUED` when a path is queued.[^s1] In Flow Builder's debugger you can choose the scheduled path to run, skip the start conditions, and run as if the record were created or updated.[^s2] The Admins blog suggests a 0-minute offset while testing, then restoring the real delay before you activate the flow.[^s4]

## When to use it (and when not)

Use a scheduled path when the timing depends on a specific record: a reminder before its due date, or a follow-up after its status changes.[^s2][^s5] For periodic sweeps over many records on a fixed calendar, a schedule-triggered flow fits better. Salesforce's architects note that it runs with synchronous limits.[^s5] Compared with Apex, scheduled paths have no per-transaction enqueue cap, while future methods allow 50 per synchronous transaction. Queueable Apex adds job IDs, chaining and a delay of up to 10 minutes.[^s5]

## Connections

Scheduled paths are part of the **record-triggered flow** and the wider **process automation** toolset.[^s1] They **replace** the time-dependent actions of **workflow rules**.[^s3] They are a low-code **alternative to queueable Apex** and **future methods** for deferred work, alongside **asynchronous Apex** generally.[^s5] They contrast with the **schedule-triggered flow**, which runs on a calendar rather than relative to a record.[^s5] They depend on **Process Automation Settings** for the Default Workflow User.[^s1][^s2] They are **governed by** Apex **governor limits** and their own 24-hour interview cap, and their retry and rollback behaviour makes **flow fault handling** relevant.[^s1]

## Sources

[^s1]: Salesforce Help, "Scheduled Paths". https://help.salesforce.com/s/articleView?language=en_US&id=platform.flow_concepts_trigger_scheduled_path.htm&type=5 (accessed 2026-11-12)
[^s2]: Trailhead, "Record-Triggered Flows: Add a Scheduled Task to Your Flow". https://trailhead.salesforce.com/content/learn/modules/record-triggered-flows/add-a-scheduled-task-to-your-flow (accessed 2026-11-12)
[^s3]: Salesforce Developers Blog, "Schedule Your Path in Salesforce Flow". https://developer.salesforce.com/blogs/2021/03/schedule-your-path-in-salesforce-flow (accessed 2026-11-12)
[^s4]: Salesforce Admins Blog, "How I Solved It: Run a Flow Scheduled Path Based on a Field Change". https://admin.salesforce.com/blog/2022/how-i-solved-it-run-a-flow-scheduled-path-based-on-a-field-change (accessed 2026-11-12)
[^s5]: Salesforce Architects, "Asynchronous Processing on the Lightning Platform". https://architect.salesforce.com/docs/architect/fundamentals/guide/async-fundamentals.html (accessed 2026-11-12)
