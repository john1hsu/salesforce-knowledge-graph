---
id: kt:apex-triggers
type: Feature
title: Apex Triggers
aliases: [Apex trigger, before trigger, after trigger, database trigger in Salesforce]
domain: development
summary: >-
  Apex code attached to an object that runs automatically before or after records are inserted, updated, deleted,
  merged, upserted or undeleted, processing the affected records in bulk within the same transaction.
release: "Winter '27"
status: current
broader: [kt:apex]
related: [kt:order-of-execution, kt:asynchronous-apex, kt:trigger-framework-pattern, kt:apex-testing]
relations:
  - {predicate: alternativeTo, object: kt:record-triggered-flow}
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: partOf, object: kt:order-of-execution}
sources:
  - id: s1
    title: "Apex Developer Guide (Winter '27): Triggers"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_triggers.htm
    type: official-docs
    accessed: 2026-10-31
  - id: s2
    title: "Apex Developer Guide (Winter '27): Trigger Context Variables"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_triggers_context_variables.htm
    type: official-docs
    accessed: 2026-10-31
  - id: s3
    title: "Trailhead: Apex Triggers — Get Started with Apex Triggers"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/apex_triggers/apex_triggers_intro
    type: official-learning
    accessed: 2026-10-31
  - id: s4
    title: "Apex Triggers in Salesforce: A Complete Guide"
    publisher: Apex Hours
    url: https://www.apexhours.com/demystifying-apex-triggers/
    type: community
    accessed: 2026-10-31
  - id: s5
    title: "Trailhead: Winter '27 Release Highlights"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/winter-27-release-highlights/
    type: official-learning
    accessed: 2026-10-31
created: 2026-10-31
---

# Apex Triggers

An Apex trigger is a block of Apex code bound to a single object that the platform runs automatically when records of that object change. Triggers let developers attach custom behaviour around data changes — validating input, deriving field values, or updating related records — without the caller having to invoke anything explicitly.[^s1] They can be defined on custom objects, on top-level standard objects such as Account and Contact, and on some standard child objects such as CaseComment; the code is stored as metadata under the object it belongs to.[^s1] This article reflects the Apex Developer Guide for the Winter '27 (264) release.[^s1][^s5]

## How it works

A trigger declaration names the trigger, the object, and a comma-separated list of the events that fire it, followed by the code block.[^s3] The supported events are before and after insert, update and delete, plus after undelete. An upsert fires the insert or update triggers as appropriate, and merge operations also fire triggers.[^s1][^s3]

The two timings serve different purposes. **Before** triggers validate or change values on the records being saved; changes to those records persist without a separate DML statement. **After** triggers see system-set values such as the record Id and LastModifiedDate and are the place to change *other* records — the records that fired them are read-only.[^s1][^s3]

Inside the body, code reads the static context variables on the `Trigger` class. `Trigger.new` holds the new versions of the records (insert, update and undelete) and is only modifiable in before triggers; `Trigger.old` and `Trigger.oldMap` hold prior versions (update and delete); `Trigger.newMap` is available in before update and in after insert, update and undelete. Boolean flags such as `isInsert`, `isBefore` and `isAfter` identify the context, and `Trigger.operationType` returns a `System.TriggerOperation` enum value (for example `BEFORE_UPDATE`) that suits a `switch` statement.[^s2]

## Limits and gotchas

- **Bulk execution.** A trigger may receive one record or many. DML on more than 200 records is processed in batches, with the trigger invoked once per batch, and `Trigger.size` reports only the current batch.[^s2][^s3] Code must therefore loop over `Trigger.new` rather than assume a single record.[^s3]
- **Governor limits.** Triggers run inside the caller's transaction and share its limits; Salesforce groups cascading trigger work into one unit and relies on governor limits to stop infinite recursion.[^s1] Putting SOQL or DML inside a loop is the classic way to hit the per-request query cap; collect IDs into collections and query or update once instead.[^s4] Binding `Trigger.new` in a SOQL `IN` clause converts it to IDs automatically, which helps here.[^s2]
- **Self-modification.** Updating or deleting the triggering record from its own before trigger, directly or indirectly, produces a runtime error.[^s1]
- **Callouts.** A trigger cannot wait on an external service; callouts must be made asynchronously, for example via a future method or a Queueable class marked `Database.AllowsCallouts`.[^s1][^s3]
- **Partial saves.** When a bulk API call fires a trigger, valid records can be saved while failing ones are rejected; when Apex DML fires it, one error rolls back the whole operation.[^s3]
- **Field history and odd values.** Field history is not written until the trigger finishes, and fields with invalid values (such as a formula dividing by zero) appear as null in the context collections.[^s1][^s2]

## When to use it (and when not)

Salesforce's guidance is to prefer validation rules and flows for simple validation and field updates, and to reach for triggers when logic is too complex for declarative tools, when performance and scale matter, or when the work is CPU-intensive.[^s3] Common community practice adds structure: keep one trigger per object so that execution order stays under your control, keep the trigger itself free of logic by delegating to a handler class with a method per context, and guard against recursion with static flags or sets of processed IDs.[^s4]

## Connections

Triggers are a feature of **Apex**, their broader node, and fire at fixed steps within the save **order of execution**, alongside flows and validation rules.[^s1] Their declarative **alternative** is the **record-triggered flow**, the recommended first choice for simple validation and field updates.[^s3] Every trigger is **governed by** the platform's **governor limits**, which is why callouts and heavy work are handed off to **asynchronous Apex** such as future methods or Queueable jobs.[^s1][^s3] The handler-class, one-trigger-per-object and recursion-guard conventions are what the graph calls the **trigger framework pattern**, and well-structured handlers are what keep trigger logic easy to cover with **Apex tests**.[^s4]

## Sources

[^s1]: Salesforce Developers, "Apex Developer Guide (Winter '27): Triggers". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_triggers.htm (accessed 2026-10-31)
[^s2]: Salesforce Developers, "Apex Developer Guide (Winter '27): Trigger Context Variables". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_triggers_context_variables.htm (accessed 2026-10-31)
[^s3]: Salesforce Trailhead, "Get Started with Apex Triggers". https://trailhead.salesforce.com/content/learn/modules/apex_triggers/apex_triggers_intro (accessed 2026-10-31)
[^s4]: Apex Hours, "Apex Triggers in Salesforce: A Complete Guide". https://www.apexhours.com/demystifying-apex-triggers/ (accessed 2026-10-31)
[^s5]: Salesforce Trailhead, "Winter '27 Release Highlights". https://trailhead.salesforce.com/content/learn/modules/winter-27-release-highlights/ (accessed 2026-10-31)
