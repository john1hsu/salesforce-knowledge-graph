---
id: kt:trigger-framework-pattern
type: Pattern
title: Trigger Framework Pattern
aliases: [trigger handler pattern, Apex trigger framework, one trigger per object, metadata-driven trigger framework]
domain: development
summary: >-
  An Apex design pattern in which each object has a single, logic-free trigger that dispatches to handler classes
  or metadata-registered actions, giving deterministic ordering, bypass controls and testable, reusable trigger logic.
release: "Winter '27"
status: concept
broader: [kt:apex-triggers]
related: [kt:order-of-execution, kt:apex-testing, kt:flow-trigger-explorer, kt:apex-enterprise-patterns]
relations:
  - {predicate: configuredVia, object: kt:custom-metadata-types}
  - {predicate: alternativeTo, object: kt:record-triggered-flow}
  - {predicate: mitigates, object: kt:governor-limits}
sources:
  - id: s1
    title: "Architect Decision Guide: Record-Triggered Automation"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/decision-guides/guide/record-triggered
    type: official-docs
    accessed: 2026-11-06
  - id: s2
    title: "Trailhead: Apex Enterprise Patterns — Learn Domain Layer Principles"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/apex_patterns_dsl/apex_patterns_dsl_learn_dl_principles
    type: official-learning
    accessed: 2026-11-06
  - id: s3
    title: "Apex Developer Guide: Static and Instance Methods, Variables, and Initialization Code"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_classes_static.htm
    type: official-docs
    accessed: 2026-11-06
  - id: s4
    title: "Trigger Actions Framework (GitHub repository)"
    publisher: mitchspano (open source)
    url: https://github.com/mitchspano/apex-trigger-actions-framework
    type: community
    accessed: 2026-11-06
created: 2026-11-06
---

# Trigger Framework Pattern

A trigger framework is a structural convention for Apex triggers rather than a platform feature: each object gets exactly one trigger, that trigger contains no business logic, and it hands every event to handler code that decides what runs and in what order.[^s1] Salesforce's architecture guidance recommends it because the platform does not guarantee the execution order of several triggers on the same object for the same event, which leads to nondeterministic behaviour and bugs that are hard to reproduce.[^s1] The pattern also answers a language limitation: triggers are not classes, so they cannot be factored or inherit behaviour, and Trailhead describes them as poor homes for even moderately complex logic.[^s2] This article reflects Salesforce guidance as published for the Winter '27 release.[^s1]

## How it works

The core move is delegation. The trigger subscribes to all the events it needs and makes a single call into a dispatcher, which reads the trigger context (before or after, insert or update, the new and old record lists) and invokes the matching handler method.[^s2] Three common flavours exist:

- **Classic handler class.** One class per object (for example an `OpportunityTriggerHandler`) holds a method per context. Order is deterministic because it is written in code, but these handlers tend to grow into monoliths that cause merge conflicts and are hard to test in isolation.[^s1]
- **Domain layer (Apex Enterprise Patterns).** The trigger is one line calling `fflib_SObjectDomain.triggerHandler(...)`, a base class from the open-source fflib library, which routes to methods such as `onBeforeInsert` and `onAfterUpdate` on the object's Domain class. The same Domain class is reused by service-layer code, so object behaviour lives in one place whether it starts from a trigger or a service.[^s2]
- **Metadata-driven framework.** Logic is split into small single-purpose action classes, and execution order is stored in custom metadata instead of code, so admins can reorder, add or remove actions without a deployment. A central handler reads that metadata, checks each action's bypass permission and runs the actions in sequence.[^s1] The open-source Trigger Actions Framework, distributed as an unlocked package, implements this idea and can register both Apex and Flow actions per object.[^s4]

## Limits and gotchas

- **Recursion.** Static variables last only for one Apex transaction, survive repeated firings of the same trigger within it, and let triggers in the same transaction share state through a common class.[^s3] Static variables declared inside the trigger body do not carry across contexts such as before insert and after insert, so frameworks keep them in a class.[^s3] They are also not reset between trigger invocations within one Bulk API request, even though governor limits are.[^s3] Salesforce's guide warns against relying only on static flags or processed-ID sets and recommends running logic only when the relevant field actually changed between old and new values.[^s1]
- **Shared work.** Because every action in a transaction draws on the same governor limits, frameworks cache expensive lookups in static properties so a configuration query runs once per transaction, and use Platform Cache for read-mostly data such as roles or business hours.[^s1]
- **Before-save first.** Updates confined to the triggering record belong in before insert or before update handlers, which avoids an extra DML statement and a second save cycle.[^s1]
- **Bypass is a power tool.** Global or per-user bypasses, typically gated by a custom permission, help with data loads but can silently switch off business rules if not governed.[^s1]

## When to use it (and when not)

Any org with more than trivial Apex trigger logic benefits from at least the classic handler shape. Salesforce's guide favours a single entry point per object and discourages unplanned mixtures of record-triggered flows and Apex triggers; for objects with little automation it suggests converting triggers to ordered flows, while objects with dense automation favour Apex triggers behind a framework.[^s1] Apex remains necessary for after-undelete logic, which record-triggered flows do not support, and a pure Apex framework has a compute edge at very high volumes compared with flows calling invocable Apex.[^s1] Choose the metadata-driven variant when many teams contribute logic to the same objects or admins need to reorder and bypass actions; choose the Domain-layer variant when the codebase already follows service, domain and selector layering.[^s1][^s2]

## Connections

The pattern is a structured way of writing **Apex triggers**, its broader node, and exists to make their place in the save **order of execution** predictable.[^s1] Metadata-driven variants are **configured via** **custom metadata types**, and the trigger handler sits beside **Flow Trigger Explorer**, which assigns order values to flows on the same object, as the two halves of a deterministic automation design.[^s1] It is an **alternative to** putting the same logic in a **record-triggered flow**, and it **mitigates** pressure on **governor limits** through transaction-scoped caching and before-save updates.[^s1] The Domain-layer flavour comes from the **Apex Enterprise Patterns** family, and thin triggers with isolated action classes are easier to cover with **Apex tests**.[^s2][^s4]

## Sources

[^s1]: Salesforce Architects, "Architect Decision Guide: Record-Triggered Automation". https://architect.salesforce.com/docs/architect/decision-guides/guide/record-triggered (accessed 2026-11-06)
[^s2]: Salesforce Trailhead, "Apex Enterprise Patterns — Learn Domain Layer Principles". https://trailhead.salesforce.com/content/learn/modules/apex_patterns_dsl/apex_patterns_dsl_learn_dl_principles (accessed 2026-11-06)
[^s3]: Salesforce Developers, "Apex Developer Guide: Static and Instance Methods, Variables, and Initialization Code". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_classes_static.htm (accessed 2026-11-06)
[^s4]: mitchspano, "Trigger Actions Framework" (GitHub repository). https://github.com/mitchspano/apex-trigger-actions-framework (accessed 2026-11-06)
