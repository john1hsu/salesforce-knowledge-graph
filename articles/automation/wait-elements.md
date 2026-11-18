---
id: kt:wait-elements
type: Feature
title: Wait Elements
aliases: [Flow Wait elements, Wait for Amount of Time, Wait Until Date, Wait for Conditions, Pause element, paused flow interviews]
domain: automation
summary: >-
  The Flow Builder elements (Wait for Amount of Time, Wait Until Date and Wait for Conditions) that pause an
  autolaunched flow interview, save it, and resume it later when a time-based or platform event resume event occurs.
release: "Winter '27"
status: current
broader: [kt:flow-builder]
related: [kt:autolaunched-flow, kt:scheduled-paths, kt:flow-orchestrator, kt:flow-fault-handling, kt:subflows]
relations:
  - {predicate: dependsOn, object: kt:flow-transaction-boundaries}
  - {predicate: dependsOn, object: kt:platform-events}
  - {predicate: governedBy, object: kt:flow-limits}
  - {predicate: governedBy, object: kt:governor-limits}
sources:
  - id: s1
    title: "Flow Elements"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.flow_ref_elements.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-18
  - id: s2
    title: "Wait for Conditions Element"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.flow_ref_elements_pause.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-18
  - id: s3
    title: "Wait for Amount of Time Element"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.flow_ref_elements_wait_for_amount_of_time.htm&type=5
    type: official-docs
    accessed: 2026-11-18
  - id: s4
    title: "Paused Flow Interview Considerations"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=platform.flow_considerations_design_pause.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-18
  - id: s5
    title: "Subscribe to Platform Event Messages with Flows (Platform Events Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/platform-events/guide/platform-events-subscribe-flow.html
    type: official-docs
    accessed: 2026-11-18
  - id: s6
    title: "How Do Salesforce Flow Wait Elements Work? Use Cases, Examples and Best Practices"
    publisher: Salesforce Ben
    url: https://www.salesforceben.com/how-do-salesforce-flow-wait-elements-work-use-cases-examples-and-best-practices/
    type: partner
    accessed: 2026-11-18
created: 2026-11-18
---

# Wait Elements

**Wait elements** are the Flow Builder elements that stop a running flow interview, persist it, and pick it up again later. Salesforce Help lists three: **Wait for Amount of Time** resumes an interview after a set duration, **Wait Until Date** resumes it at a specific date and time, and **Wait for Conditions** resumes it once specified conditions are met.[^s1] They are the in-flow way to build "send a reminder in three days" or "continue when the order ships" logic, and the developer guide for platform events still describes the condition-based variant under its earlier name, the **Pause** element.[^s5]

## How it works

Wait for Amount of Time takes a duration and can optionally be told to resume only at a given time of day in a chosen time zone; if the duration ends after that time, the interview waits until the same time on the next day.[^s3] Wait for Conditions is the most flexible: each *wait configuration* becomes its own outgoing connector, defines a resume event, and may carry optional wait conditions that decide at run time whether the interview waits for that event at all.[^s2] The first resume event to occur wins and runs its connector; if no configuration's conditions are met, the interview does not pause and follows the default path instead.[^s2] Salesforce's example sends a contract reminder 30 days before the end date for hot accounts and 14 days before for all others, with each event gated on the account rating.[^s2]

Resume events are either time-based or platform event messages. To wait on an event, an autolaunched flow subscribes at run time and specifies the field values a message must carry to resume the interview, such as a matching order number with a Shipped status.[^s5] Supported events include custom platform events plus standard ones such as BatchApexErrorEvent and FlowExecutionErrorEvent; event data reaches formulas by storing the message in a record variable first.[^s4]

## Limits and gotchas

- Wait elements require an autolaunched flow, and a flow with a Wait element can't be activated or run if it also contains screens, choices or choice sets.[^s3][^s2]
- Salesforce Help states that flows containing Wait elements can't be called, and waits inside autolaunched flows used as screen actions don't work.[^s4]
- An org processes up to 1,000 time-based resume events per hour, with the overflow moving to the next hour; time values don't support minutes or seconds.[^s4]
- A paused interview larger than 1 MB fails to save and can't be resumed; if the user who started it has been deactivated, it fails to resume.[^s4]
- Deactivating a flow version doesn't stop its paused interviews, and a version with paused interviews can't be deleted.[^s4]
- Platform event filter values are capped at 765 characters, and a lead referenced by a paused interview's resume event can't be converted.[^s4]

The transaction model matters most. Pausing ends the current transaction, and resuming starts a new one, but resumed interviews are grouped into a batch, which starts resuming within an hour of the first interview joining it, and they share one transaction.[^s4] Batched DML and SOQL can therefore exceed Apex governor limits, so Salesforce recommends keeping each user's work between waits within limits, splitting work across several Wait elements, and adding fault paths that loop back to the Wait element on "Too many SOQL queries" or "Too many DML operations" errors.[^s4] Time-based waits that reference record date fields are recalculated if the date changes, and a deleted record removes its resume event.[^s4]

## When to use it (and when not)

Use a Wait element when an autolaunched or scheduled process genuinely needs to sit between steps: follow-up emails, renewal kick-offs ahead of an end date, or waiting for a shipment status or event before the next action.[^s6] For time offsets relative to a record change, a record-triggered flow's scheduled paths are the native tool, because a record-triggered flow can't call a subflow that contains a wait.[^s6][^s4] Long waits should be monitored through the Paused and Failed Flow Interviews list, and admins should know that an interview resumes on the flow version it started on even after the flow is updated.[^s6]

## Connections

Wait elements are part of **Flow Builder** and run only in **autolaunched flows**.[^s3] Their pause-and-resume behaviour is defined by **flow transaction boundaries**, and the resumed batch is **governed by** both **flow limits** and **Apex governor limits**.[^s4] Event-based waits **depend on platform events**, the same bus that drives platform event-triggered flows.[^s5] **Scheduled paths** are the time-offset alternative inside record-triggered flows, **fault handling** is the recommended guard for batch-limit errors, and **subflows** are affected because waiting flows can't be called.[^s4][^s6] **Flow Orchestrator** is the graph's node for multi-step processes that span users and stages, where Wait for Conditions also appears.[^s6]

## Sources

[^s1]: Salesforce Help, "Flow Elements". https://help.salesforce.com/s/articleView?id=sf.flow_ref_elements.htm&language=en_US&type=5 (accessed 2026-11-18)
[^s2]: Salesforce Help, "Wait for Conditions Element". https://help.salesforce.com/s/articleView?id=sf.flow_ref_elements_pause.htm&language=en_US&type=5 (accessed 2026-11-18)
[^s3]: Salesforce Help, "Wait for Amount of Time Element". https://help.salesforce.com/s/articleView?language=en_US&id=sf.flow_ref_elements_wait_for_amount_of_time.htm&type=5 (accessed 2026-11-18)
[^s4]: Salesforce Help, "Paused Flow Interview Considerations". https://help.salesforce.com/s/articleView?id=platform.flow_considerations_design_pause.htm&language=en_US&type=5 (accessed 2026-11-18)
[^s5]: Salesforce Developers, "Subscribe to Platform Event Messages with Flows". https://developer.salesforce.com/docs/platform/platform-events/guide/platform-events-subscribe-flow.html (accessed 2026-11-18)
[^s6]: Salesforce Ben, "How Do Salesforce Flow Wait Elements Work? Use Cases, Examples and Best Practices". https://www.salesforceben.com/how-do-salesforce-flow-wait-elements-work-use-cases-examples-and-best-practices/ (accessed 2026-11-18)
