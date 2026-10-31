---
id: kt:flow-builder
type: Tool
title: Flow Builder
aliases: [Salesforce Flow Builder, Salesforce Flow]
domain: automation
summary: >-
  Salesforce's declarative, canvas-based tool for building flows (screen, autolaunched and triggered), and the
  platform's recommended replacement for Workflow Rules and Process Builder.
release: "Winter '27"
status: current
broader: [kt:process-automation]
related: [kt:record-triggered-flow, kt:screen-flow, kt:flow-orchestrator]
relations:
  - {predicate: alternativeTo, object: kt:apex-triggers}
  - {predicate: replaces, object: kt:workflow-rules}
  - {predicate: replaces, object: kt:process-builder}
  - {predicate: governedBy, object: kt:governor-limits}
sources:
  - id: s1
    title: "Flow Basics: Meet Flow Builder"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/flow-basics/meet-flow-builder
    type: official-learning
    accessed: 2026-10-30
  - id: s2
    title: "Record-Triggered Flows: Get Started with Triggered Flows"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/record-triggered-flows/get-started-with-triggered-flows
    type: official-learning
    accessed: 2026-10-30
  - id: s3
    title: "Autolaunched and Scheduled Flows: Get Started with Autolaunched Flows"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/autolaunched-scheduled-flows/get-started-with-autolaunched-flows
    type: official-learning
    accessed: 2026-10-30
  - id: s4
    title: "Record-Triggered Automation Decision Guide"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/decision-guides/guide/record-triggered
    type: official-docs
    accessed: 2026-10-30
  - id: s5
    title: "Salesforce Workflow Rules & Process Builder End of Support"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=000389396&type=1
    type: official-docs
    accessed: 2026-10-30
created: 2026-10-30
---

# Flow Builder

Flow Builder is the point-and-click tool in Salesforce Setup for designing, testing and activating flows. A flow is drawn as a diagram of elements joined by connectors, so admins can automate business processes without writing code.[^s1] It is now the platform's main declarative automation tool: Salesforce ended support for Workflow Rules and Process Builder on December 31, 2025 and directs customers to move that automation to Flow Builder.[^s5]

## How it works

The builder has three main areas. The **toolbox** lists the flow's elements and resources and is where new resources are created. The **canvas** is where elements are placed and connected. The **button bar** shows activation status, last-saved time, and errors and warnings.[^s1] Elements come in three groups: *interaction* elements (Screen, Action, Subflow), *data* elements (Get, Create, Update and Delete Records) and *logic* elements (Assignment, Decision, Loop, Collection Sort, Collection Filter). Connectors set the order in which elements run. Resources such as variables, formulas, text templates, records and record collections do not appear on the canvas, but elements refer to them.[^s1]

Flows are versioned. **Save As New Version** keeps the earlier versions, and **Activate** chooses which version users run, so an admin can roll back by reactivating an older version. **Run** and **Debug** always use the most recently saved version, not unsaved edits. Record-triggered flows also support saved test scenarios through **View Tests**.[^s1] Trailhead recommends Auto-Layout over Free-Form for arranging the canvas.[^s1]

## Flow types

Trailhead sorts flows into three general types: screen, autolaunched and triggered.[^s2] **Screen flows** take user input. An **Autolaunched Flow (No Trigger)** runs without user interaction when something else starts it, such as a custom button, a parent flow's Subflow element, Apex, a Visualforce page, Flow Orchestration, an external API call, or an Agentforce agent action.[^s3] **Triggered flows** start on a schedule (for example, nightly batch work), when a platform event message arrives, or when a record is created, updated or deleted.[^s2] Trailhead calls the record-triggered flow the most commonly used kind of automation.[^s2]

A record-triggered flow can be optimized for **Fast Field Updates**, which run before the triggering record is saved and are best for changing that record or showing a custom error. It can instead be optimized for **Actions and Related Records**, which run after the save to change other records, call subflows or send alerts. Trailhead says the before-save option performs best because it puts little load on the database.[^s2]

## Limits and gotchas

The Architects decision guide says to use a before-save update whenever automation only needs to change fields on the triggering record. That avoids a second DML operation and a recursive save, whichever tool is used.[^s4] Invocable Apex actions are available only in the after-save context. Flow has no after-undelete context, so logic that must run on undelete needs Apex.[^s4] Flow cannot share state across trigger invocations in a transaction the way Apex static variables or Platform Cache can. The guide also does not recommend Flow for high-performance bulk processing because of governor-limit risk.[^s4]

On design, the guide calls it an anti-pattern to put all of an object's automation into one large "mega-flow". It recommends Flow Trigger Explorer for ordering flows on the same object and warns against patterns such as Get Records inside a loop.[^s4] It also advises choosing one automation tool as the entry point for each object.[^s4]

## When to use it (and when not)

The decision guide calls the record-triggered flow the platform's main declarative tool for record-triggered automation. It recommends Flow for objects with low automation density (fewer than 15 automations per object in its density table) and for simple cross-object DML.[^s4] For high-density objects, complex cross-object logic, or cases that need fine control over deduplication and error handling, it points to Apex triggers. Its hybrid pattern uses Flow for orchestration and calls Invocable Apex for heavy computation.[^s4]

## Connections

Flow Builder sits under **process automation** in general. Its main products are the **record-triggered flow** and the **screen flow**, each of which deserves its own node.[^s2] It **replaces** Workflow Rules and Process Builder, whose support ended at the close of 2025. Existing processes keep running but no longer get bug fixes, which is why migration is the recommended path.[^s5] It is the declarative **alternative to Apex triggers**, and the Architects decision guide frames the choice between them by automation density and complexity.[^s4] Like all transaction logic, flows are **governed by governor limits**, the main reason the guide sends bulk-heavy work to Apex.[^s4]

## Sources

[^s1]: Trailhead, "Flow Basics: Meet Flow Builder". https://trailhead.salesforce.com/content/learn/modules/flow-basics/meet-flow-builder (accessed 2026-10-30)
[^s2]: Trailhead, "Record-Triggered Flows: Get Started with Triggered Flows". https://trailhead.salesforce.com/content/learn/modules/record-triggered-flows/get-started-with-triggered-flows (accessed 2026-10-30)
[^s3]: Trailhead, "Autolaunched and Scheduled Flows: Get Started with Autolaunched Flows". https://trailhead.salesforce.com/content/learn/modules/autolaunched-scheduled-flows/get-started-with-autolaunched-flows (accessed 2026-10-30)
[^s4]: Salesforce Architects, "Record-Triggered Automation Decision Guide". https://architect.salesforce.com/docs/architect/decision-guides/guide/record-triggered (accessed 2026-10-30)
[^s5]: Salesforce Help, "Salesforce Workflow Rules & Process Builder End of Support". https://help.salesforce.com/s/articleView?language=en_US&id=000389396&type=1 (accessed 2026-10-30)
