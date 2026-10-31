---
id: kt:order-of-execution
type: Concept
title: Order of Execution
aliases: [save order of execution, triggers and order of execution, save order, record save procedure]
domain: platform-architecture
summary: >-
  The fixed sequence in which Salesforce runs validation, record-triggered flows, Apex triggers, duplicate rules,
  legacy automation, roll-up recalculation, sharing and commit whenever a record is inserted, updated or upserted.
release: "Winter '27"
status: current
broader: [kt:multitenancy]
related: [kt:apex-triggers, kt:record-triggered-flow, kt:flow-builder, kt:roll-up-summary-field, kt:asynchronous-apex]
relations:
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: configuredVia, object: kt:flow-trigger-explorer}
  - {predicate: causes, object: kt:recursive-save}
sources:
  - id: s1
    title: "Apex Developer Guide: Triggers and Order of Execution"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm
    type: official-docs
    accessed: 2026-10-31
  - id: s2
    title: "Record-Triggered Automation Decision Guide"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/decision-guides/trigger-automation
    type: official-docs
    accessed: 2026-10-31
  - id: s3
    title: "Define the Run Order of Record-Triggered Flows for an Object"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=platform.flow_task_trigger_run_order.htm
    type: official-docs
    accessed: 2026-10-31
  - id: s4
    title: "Meet Flow Trigger Explorer (Record-Triggered Flows module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/record-triggered-flows/meet-flow-trigger-explorer
    type: official-learning
    accessed: 2026-10-31
created: 2026-10-31
---

# Order of Execution

The order of execution is the deterministic pipeline that the Salesforce server walks through every time a record is inserted, updated or upserted. It decides when validation runs, when record-triggered flows and Apex triggers fire, when legacy automation such as workflow rules runs, when parent roll-ups recalculate, and when the transaction commits. The Apex Developer Guide page for Winter '27 (API version 68.0) is the authoritative list. Salesforce notes that the companion flowchart can lag behind that page.[^s1] Almost every "why did my field change twice" or "why did this trigger fire again" question comes down to this sequence.

## The sequence

Before anything reaches the server, the browser only checks dependent picklist values. All other validation is server-side.[^s1] The server then:[^s1]

1. Loads the original record (or initializes a new one for upsert) and overlays the incoming values, running system validation that depends on the request source (standard UI, line-item creation, or API/Apex).[^s1]
2. Runs **before-save record-triggered flows**, then **all before triggers**.[^s1]
3. Re-runs most system validation and all custom validation rules, then **duplicate rules**. A blocking duplicate rule stops the save, so after triggers and later steps never run.[^s1]
4. Saves the record to the database **without committing**, then runs **all after triggers**.[^s1]
5. Runs assignment rules, auto-response rules and **workflow rules**. A workflow field update saves the record again and fires before-update and after-update triggers one more time, even if the original operation was an insert. Custom validation, flows and duplicate rules do not re-run on that pass.[^s1]
6. Runs escalation rules, then Process Builder processes and workflow-launched flows (in no guaranteed order), then **after-save record-triggered flows**, then entitlement rules.[^s1]
7. Recalculates roll-up summary fields on the parent, and on the grandparent if needed. Each ancestor goes through its own save procedure.[^s1]
8. Evaluates criteria-based sharing, **commits** all DML, and only then runs post-commit work: sending email, enqueued queueable jobs and future methods, and asynchronous paths of record-triggered flows.[^s1]

## Limits and gotchas

- **Trigger order is not guaranteed.** If several triggers on one object fire for the same event, Salesforce does not promise their order.[^s1] This is the main reason teams adopt a single trigger per object that delegates to a handler.
- **Trigger.old after workflow updates.** On the re-fire caused by a workflow field update, `Trigger.old` still holds the values from before the original update, not the intermediate values.[^s1]
- **Recursive saves skip steps.** When a save is recursive, the assignment-through-grandparent-roll-up steps are skipped.[^s1] Flow triggers get recursion control and never re-fire on the same record during a recursive save. However, the early validation, trigger and commit stages are re-run when an after-save flow updates its own triggering record. That is why same-record updates belong in before-save flows.[^s2]
- **Partial-success DML retries** fire triggers again, and static variables are not reset between attempts. Guard logic that relies on statics can misbehave.[^s1]
- **Legacy API behaviour.** At API version 53.0 and earlier, after-save flows run after entitlement rules instead of before them.[^s1]
- **Shared limits.** All save-order trees in a transaction share one budget of 10,000 processed DML records and 150 DML statements. Cascading roll-ups and cross-object flows consume it quickly.[^s2]

## Controlling the order

Within Flow, administrators can assign a trigger order from 1 to 2,000 to before-save or after-save flows on the same object. Flows numbered 1–1,000 run first in ascending order, then flows with no value by activation date, then 1,001–2,000. Ties are broken alphabetically by API name. A trigger order never moves a flow across the platform sequence. For example, an after-save flow cannot run ahead of a before trigger.[^s3] Flow Trigger Explorer groups an object's flows into before-save, after-save, asynchronous and scheduled sections, and supports drag-and-drop reordering. Asynchronous flows are not guaranteed to run in the order listed.[^s4]

## When to use what

Salesforce's decision guide recommends before-save flows for same-record field updates. It reports that they run significantly faster than after-save updates, and 10–20x faster than equivalent workflow rules or Process Builder in bulk. After-save flows handle cross-object work and asynchronous paths. Apex triggers remain the place for complex logic, custom `addError()` validation, and anything Flow cannot express. The guide also favours consolidating each object's automation into one tool where practical. Splitting it across many ordered flows does not materially hurt performance.[^s2]

## Connections

The order of execution is a consequence of the platform's shared, metadata-driven runtime, so it sits under **multitenancy** (`kt:multitenancy`). Every step runs inside one transaction **governed by** `kt:governor-limits`.[^s2] It defines where **Apex triggers** (`kt:apex-triggers`) and **record-triggered flows** (`kt:record-triggered-flow`, built in `kt:flow-builder`) fire relative to each other.[^s1] Flow ordering is **configured via** Flow Trigger Explorer (`kt:flow-trigger-explorer`).[^s4] Parent recalculation links it to **roll-up summary fields** (`kt:roll-up-summary-field`). Post-commit scheduling of queueable and future work links it to **asynchronous Apex** (`kt:asynchronous-apex`).[^s1] Same-record after-save updates **cause** recursive saves (`kt:recursive-save`), the main performance trap it creates.[^s2]

## Sources

[^s1]: Salesforce Developers, "Apex Developer Guide: Triggers and Order of Execution". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm (accessed 2026-10-31)
[^s2]: Salesforce Architects, "Record-Triggered Automation Decision Guide". https://architect.salesforce.com/decision-guides/trigger-automation (accessed 2026-10-31)
[^s3]: Salesforce Help, "Define the Run Order of Record-Triggered Flows for an Object". https://help.salesforce.com/apex/HTViewHelpDoc?id=platform.flow_task_trigger_run_order.htm (accessed 2026-10-31)
[^s4]: Trailhead, "Meet Flow Trigger Explorer". https://trailhead.salesforce.com/content/learn/modules/record-triggered-flows/meet-flow-trigger-explorer (accessed 2026-10-31)
