---
id: kt:flow-transaction-boundaries
type: Concept
title: Flow Transaction Boundaries
aliases: [flow transactions, how flows run in transactions, flow transaction control setting, "Let the flow decide"]
domain: automation
summary: >-
  The points at which a running flow interview commits its current database transaction and starts a new one
  (Screen, Local Action and Wait elements, paused-interview resumes, and actions set to start a new transaction),
  which decide what shares governor limits and what a failure can roll back.
release: "Winter '27"
status: current
broader: [kt:transaction-control, kt:flow-builder]
related: [kt:flow-fault-handling, kt:screen-flow, kt:record-triggered-flow, kt:flow-http-callout, kt:bulkification, kt:order-of-execution]
relations:
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: dependsOn, object: kt:order-of-execution}
  - {predicate: alternativeTo, object: kt:asynchronous-apex}
sources:
  - id: s1
    title: "How Flows Run in Transactions (Salesforce Help)"
    publisher: Salesforce
    url: https://help.salesforce.com/s/articleView?id=platform.flow_concepts_transaction.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-11
  - id: s2
    title: "Paused Flow Interview Considerations (Salesforce Help)"
    publisher: Salesforce
    url: https://help.salesforce.com/s/articleView?id=platform.flow_considerations_design_pause.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-11
  - id: s3
    title: "Roll Back Changes After an Error (Trailhead, Flow Implementation II)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/flow-implementation-2/roll-back-changes-after-an-error
    type: official-learning
    accessed: 2026-11-11
  - id: s4
    title: "Record-Triggered Automation (Platform Decision Guides)"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/decision-guides/guide/record-triggered
    type: official-docs
    accessed: 2026-11-11
created: 2026-11-11
---

# Flow Transaction Boundaries

A flow never runs on its own: every flow interview executes inside a database transaction, the unit of work that commits together or rolls back together if any operation in it fails. That transaction can also contain Apex triggers, escalation rules and every other flow interview started by the same save, and all of them draw from one set of per-transaction governor limits.[^s1] A **transaction boundary** is a point in a flow where the current transaction ends (and commits) and a new one begins. Knowing where those boundaries fall tells you which work shares limits, what a later error can undo, and when a callout is allowed.

## Where a transaction starts

The trigger of the flow sets the start. A record create or update starts the transaction for record-triggered automation; a flow URL, custom button or Visualforce page starts one when it is accessed; `Interview.start()` called from a trigger joins the trigger's transaction and shares limits with the rest of the class; and a REST call to the Flows resource or a custom action starts one when the call is made.[^s1]

## Where a transaction ends

Salesforce documents three elements that end the current transaction and open a new one when they run: **Screen**, **Local Action** and **Wait** (the pause element).[^s1] Otherwise the transaction ends when the save's execution order finishes or when every interview in it is done.[^s1]

Screens are the most common boundary. Because a screen commits what came before it, a **Roll Back Records** element placed after a screen can only undo work done since that screen, not earlier DML.[^s3] Trailhead advises putting the rollback on the fault path before any screen that shows the error, since a user who closes the window stops the flow from reaching later elements.[^s3]

Wait elements create a longer gap. The transaction ends the moment the interview pauses; on resume, the work after the Wait runs in a batch transaction shared with other resumed interviews of the same flow version and running user, so resumed interviews doing SOQL or DML can collectively exceed governor limits.[^s2] If an unhandled failure hits one resumed interview, its operations since resuming roll back and the rest of the batch is still attempted.[^s2]

## The action-level transaction setting

Since Winter '26, every flow type can decide at runtime whether an action runs in a new transaction; before that only screen flows had this control. Record-triggered flows can use it only on asynchronous or scheduled paths.[^s1] Custom actions expose three options under Advanced (standard actions only when they make a callout):[^s1]

- **Let the flow decide** (recommended): if the action makes a callout while operations are pending, the flow commits first and runs the action in a new transaction.[^s1]
- **Always start a new transaction**: commits before the action, so earlier work cannot be rolled back if the action fails; debug runs are not supported.[^s1]
- **Always continue in current transaction**: the default for actions configured in Summer '25 or earlier; a callout with pending operations makes the flow fail.[^s1]

## Limits and gotchas

- All interviews in one transaction share its governor limits, so a bulk load of 100 records runs every trigger, process and flow against one budget.[^s1]
- Splitting work with a Screen, Local Action or Wait element is Salesforce's documented way to keep an interview under limits, at the cost of losing all-or-none rollback across the split.[^s1]
- An org processes up to 1,000 time-based resume events per hour; extras slip to the next hour, and a paused interview larger than 1 MB cannot be saved or resumed.[^s2]
- A fault path does not roll anything back; earlier changes in the transaction are kept unless you add Roll Back Records (screen flows) or Custom Error (record-triggered flows).[^s3]
- Flow has no savepoints or partial-success DML, which Apex offers for fine-grained transaction recovery.[^s4]

## When to use which boundary

Keep related writes in one transaction when they must succeed or fail together. Move slow or failure-prone work, such as a simple callout, to a record-triggered flow's Run Asynchronously path, which executes in a separate transaction after the original save commits so a failure there cannot undo the user's save.[^s4] Use Apex when you need savepoints or partial success.[^s4]

## Connections

Flow transaction boundaries are the Flow-side view of **Apex transaction control** and are bounded by **governor limits**. They decide what **flow fault handling**'s rollback elements can reach, shape how **screen flows** and **HTTP callouts from flow** behave, and sit inside the save-time **order of execution** that starts a **record-triggered flow**'s transaction.[^s1][^s3] Splitting a transaction is an alternative to moving work into **asynchronous Apex**, and both complement **bulkification** for staying within limits.[^s4]

## Sources
[^s1]: Salesforce, "How Flows Run in Transactions (Salesforce Help)". https://help.salesforce.com/s/articleView?id=platform.flow_concepts_transaction.htm&language=en_US&type=5 (accessed 2026-11-11)
[^s2]: Salesforce, "Paused Flow Interview Considerations (Salesforce Help)". https://help.salesforce.com/s/articleView?id=platform.flow_considerations_design_pause.htm&language=en_US&type=5 (accessed 2026-11-11)
[^s3]: Salesforce Trailhead, "Roll Back Changes After an Error (Trailhead, Flow Implementation II)". https://trailhead.salesforce.com/content/learn/modules/flow-implementation-2/roll-back-changes-after-an-error (accessed 2026-11-11)
[^s4]: Salesforce Architects, "Record-Triggered Automation (Platform Decision Guides)". https://architect.salesforce.com/docs/architect/decision-guides/guide/record-triggered (accessed 2026-11-11)
