---
id: kt:scheduled-apex
type: Feature
title: Scheduled Apex
aliases: [Apex Scheduler, Schedulable interface, System.schedule, Schedulable Apex, scheduled Apex jobs]
domain: development
summary: >-
  The asynchronous Apex mode in which a class implementing the Schedulable interface is run by the Apex Scheduler at a
  set time or on a recurring cron-style schedule, registered with System.schedule or from the Scheduled Jobs page in Setup.
release: "Winter '27"
status: current
broader: [kt:asynchronous-apex]
related: [kt:batch-apex, kt:queueable-apex, kt:apex-testing, kt:sandbox-types]
relations:
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: alternativeTo, object: kt:schedule-triggered-flow}
sources:
  - id: s1
    title: "Apex Developer Guide: Apex Scheduler"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_scheduler.htm
    type: official-docs
    accessed: 2026-11-10
  - id: s2
    title: "Apex Developer Guide: Use Batch Apex"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_batch_interface.htm
    type: official-docs
    accessed: 2026-11-10
  - id: s3
    title: "Trailhead: Schedule Jobs Using the Apex Scheduler"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/asynchronous_apex/async_apex_scheduled
    type: official-learning
    accessed: 2026-11-10
created: 2026-11-10
---

# Scheduled Apex

Scheduled Apex is the asynchronous Apex option for running code at a chosen time or on a repeating timetable. A developer writes a class that implements the `Schedulable` interface, whose single method is `execute(SchedulableContext sc)`, and registers it with the Apex Scheduler.[^s1] Typical jobs are recurring maintenance such as nightly clean-ups, reminder generation or kicking off Batch Apex daily or weekly.[^s3] The Apex Developer Guide page checked for this article is the Winter '27 (API 68.0) version.[^s1]

## How it works

A job is registered in code with `System.schedule`, which takes a job name, a cron expression and an instance of the class, and returns the job ID. Job names must be unique among scheduled jobs; reusing one throws an `AsyncException`. Times are interpreted in the running user's time zone, and actual start can slip depending on service availability.[^s1] Admins can also schedule a class without code from Setup's Scheduled Jobs page using **Schedule Apex**, choosing a weekly or monthly frequency, start and end dates and a preferred start time.[^s3]

The cron expression has the fields seconds, minutes, hours, day of month, month, day of week and an optional year. Special characters include `?` (no specific value), `L` (last), `W` (nearest weekday) and `#` (nth weekday of the month), so `0 0 10 ? * MON-FRI` runs at 10 AM on weekdays.[^s1] Apex does not allow a single schedule to fire more than once an hour.[^s1]

The scheduler runs the class in system context, so it executes regardless of the scheduling user's permissions. Salesforce recommends keeping `execute` thin: instantiate a separate class that holds the real logic, or call `Database.executeBatch` to launch a batch job.[^s1] Each scheduled job is represented by a `CronTrigger` record; `SchedulableContext.getTriggerId()` returns its ID, and querying `CronTrigger` (with `CronJobDetail` for the name and a `JobType` of `7`) gives fields such as `TimesTriggered` and `NextFireTime`. `System.abortJob` with that ID stops the job.[^s1]

For the common case of running a batch class once after a delay, `System.scheduleBatch` takes the batch instance, a job name, the number of minutes to wait and an optional scope size, without needing a `Schedulable` class. It returns the `CronTrigger` ID, and the job counts against scheduled Apex limits until it is queued, after which batch limits apply.[^s2]

## Limits and gotchas

- At most **100** scheduled Apex jobs can exist at one time.[^s1]
- Executions draw on the org's rolling 24-hour asynchronous Apex allowance of 250,000 or 200 times the number of user licenses, whichever is greater, a pool shared with Batch, Queueable and future methods.[^s1]
- Synchronous callouts are not supported from scheduled Apex. Enqueue a Queueable that implements `Database.AllowsCallouts`, or launch a batch class that does.[^s1][^s3]
- Scheduling from a trigger is risky: bulk updates can create more jobs than the 100-job cap allows.[^s1][^s3]
- A class with pending or running scheduled jobs cannot be edited in the UI, and deployments of it fail with a "jobs pending or in progress" error unless deployments with Apex jobs are enabled. Even then the job may fail, so the documented approach is to delete the job, deploy, then reschedule.[^s1]
- The job instance keeps member variable values between runs; mark fields `transient` to stop that.[^s1]
- Sandbox refreshes do not copy scheduled jobs, so they must be rescheduled. Jobs due during maintenance downtime run once service resumes, and resuming a paused job runs it once immediately while skipping runs missed during the pause.[^s1]

## Testing

Wrap `System.schedule` in `Test.startTest()` and `Test.stopTest()`; the job then runs synchronously at `stopTest`, after which assertions can check its results and the `CronTrigger` fields.[^s1][^s3]

## When to use it (and when not)

Use Scheduled Apex when code, rather than declarative automation, must run on a calendar: a nightly batch kick-off, a monthly roll-up or a periodic health check that restarts a stalled batch chain.[^s2][^s3] For a one-off delayed batch, `System.scheduleBatch` is simpler.[^s2] For short delays on background work, a Queueable is the documented route for callouts.[^s1]

## Connections

Scheduled Apex is one of the modes of **asynchronous Apex**, its broader node, and is **governed by** **governor limits**, including the shared daily async execution pool.[^s1] It is most often a launcher for **Batch Apex**, through `Database.executeBatch` or the related `System.scheduleBatch`.[^s1][^s2] It is a code-based **alternative to** **schedule-triggered flows** for time-based automation.[^s3] It relates to **Apex testing**, whose start/stop pattern forces scheduled jobs to run, and to **sandbox types**, because refreshed sandboxes arrive without scheduled jobs.[^s1] It relates to **Queueable Apex** as the documented route for callouts that a scheduled job cannot make itself.[^s1]

## Sources

[^s1]: Salesforce Developers, "Apex Developer Guide: Apex Scheduler" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_scheduler.htm (accessed 2026-11-10)
[^s2]: Salesforce Developers, "Apex Developer Guide: Use Batch Apex" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_batch_interface.htm (accessed 2026-11-10)
[^s3]: Trailhead, "Schedule Jobs Using the Apex Scheduler". https://trailhead.salesforce.com/content/learn/modules/asynchronous_apex/async_apex_scheduled (accessed 2026-11-10)
