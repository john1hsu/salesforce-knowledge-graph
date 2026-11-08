---
id: kt:apex-enterprise-patterns
type: Pattern
title: Apex Enterprise Patterns
aliases: [fflib, fflib-apex-common, AEP, Apex separation of concerns, service domain selector pattern]
domain: development
summary: >-
  A family of layered design patterns for Apex, adapted from Martin Fowler's enterprise application patterns, that
  splits code into Service, Domain, Selector and Unit of Work layers and is implemented by the open-source fflib library.
release: "Winter '27"
status: concept
broader: [kt:apex]
related: [kt:trigger-framework-pattern, kt:batch-apex, kt:package-dependencies]
relations:
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: dependsOn, object: kt:transaction-control}
  - {predicate: mitigates, object: kt:technical-debt-in-salesforce}
  - {predicate: integratesWith, object: kt:apex-mocks}
sources:
  - id: s1
    title: "Trailhead: Apex Enterprise Patterns: Service Layer — Learn About Separation of Concerns"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/apex_patterns_sl/apex_patterns_sl_soc
    type: official-learning
    accessed: 2026-11-08
  - id: s2
    title: "Trailhead: Apex Enterprise Patterns: Service Layer — Learn Service Layer Principles"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/apex_patterns_sl/apex_patterns_sl_learn_sl_principles
    type: official-learning
    accessed: 2026-11-08
  - id: s3
    title: "Trailhead: Apex Enterprise Patterns: Service Layer — Learn Unit of Work Principles"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/apex_patterns_sl/apex_patterns_sl_learn_uow_principles
    type: official-learning
    accessed: 2026-11-08
  - id: s4
    title: "Trailhead: Apex Enterprise Patterns: Domain & Selector Layers — Learn Selector Layer Principles"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/apex_patterns_dsl/apex_patterns_dsl_learn_selector_l_principles
    type: official-learning
    accessed: 2026-11-08
  - id: s5
    title: "fflib-apex-common (GitHub repository)"
    publisher: apex-enterprise-patterns (open source)
    url: https://github.com/apex-enterprise-patterns/fflib-apex-common
    type: community
    accessed: 2026-11-08
created: 2026-11-08
---

# Apex Enterprise Patterns

Apex Enterprise Patterns (often shortened to "fflib", after the library that implements them) are a set of layered design conventions for organising large Apex codebases. They apply the principle of separation of concerns, which Trailhead frames as partitioning code into layers so it is easier to navigate, changes in one layer have limited impact on others, and individual layers can be reworked or replaced as requirements evolve.[^s1] Each pattern is adapted from Martin Fowler's catalogue of enterprise application architecture patterns; for example, the Service pattern defines an application's boundary as a layer of available operations.[^s2] They are a coding discipline rather than a platform feature, so nothing changes about them between releases; this article reflects Trailhead guidance as published during the Winter '27 release.[^s1]

## The layers

- **Service layer.** The entry point for every client of the business logic. Trailhead lists Apex UI controllers (Visualforce and `@AuraEnabled` methods), Apex REST and SOAP web services, invocable methods, inbound email handlers, and Batch, Scheduled and Queueable Apex as callers; triggers are deliberately absent because their logic belongs to the Domain layer.[^s2] Services are named after the business operation (for example `calculateTax`, not a name tied to one customer or screen), accept lists so they are bulk-safe, run `with sharing` by default and elevate only inside a private `without sharing` inner class, stay stateless, and own the database transaction for their method.[^s2] Errors are signalled by throwing exceptions or returning partial results, leaving each caller to marshal them, such as a Lightning controller wrapping them for the UI while a batch job logs them.[^s2]
- **Domain layer.** Logic tied to a specific object and its records, such as validation, defaulting and calculations on insert, update or delete, which runs whether the change comes from a service, the UI or an API.[^s2]
- **Selector layer.** Based on Fowler's Data Mapper, renamed because on Salesforce it mostly returns native SObject records.[^s4] Selectors centralise SOQL so that queries, the set of fields they return, and security checks stay consistent; scattered inline queries drift apart, return unpredictable fields that cause `SObjectException` errors, and make security easy to forget.[^s4] Each method returns a minimal, predictable field set as its contract, uses compile-time field references so referenced fields cannot be deleted, and is an instance method so callers can configure it, including opting in or out of sharing and permission enforcement.[^s4]
- **Unit of Work.** Based on Fowler's pattern of tracking the objects affected by a business transaction. Code registers new and changed records during processing, and a single `commitWork` call performs the DML in bulk inside a savepoint, resolving parent-child relationships along the way.[^s3]

## How the pieces fit

A typical flow is: a caller invokes a service method; the service uses a selector to load records, hands them to a Domain class that applies object-level behaviour, registers the resulting changes with a Unit of Work, and commits once.[^s4][^s3] Batch Apex fits the same shape, because a batch `start` method can return a `QueryLocator` from a selector method.[^s4] The fflib-apex-common library supplies base classes for these layers, originated in a Dreamforce 2012 presentation, is BSD-3-Clause licensed, and is distributed as Salesforce DX source with no deployment dependencies; the companion ApexMocks library is recommended, not required, for Mockito-style mocking in application tests.[^s5]

## Limits and gotchas

- **Commit once per scope.** Call `commitWork` only once in a service method, and when one service calls another, pass the outer Unit of Work in rather than creating a second one.[^s3]
- **Handled exceptions don't roll back.** The platform rolls back on an unhandled exception, but a caught one can leave partial writes; the Unit of Work's savepoint exists to prevent that.[^s3]
- **Register types in dependency order.** The Unit of Work constructor takes the list of SObject types it will touch, ordered so related records are written correctly.[^s3]
- **Field sets versus heap.** Consistent selector field sets can conflict with heap usage on large data volumes, so the contract has to be balanced against size.[^s4]
- **Not for every org.** Trailhead considers separation of concerns typically unnecessary for small, one-off solutions with one or two developers, few objects and a standard UI, or for data-centric apps built mostly declaratively; it sees definite benefits on large projects with many developers and objects.[^s1]

## When to use it (and when not)

Adopt the patterns when you are adding or replacing a UI, exposing a public API over your logic, scaling processing with Batch Apex and need identical results to interactive use, or when controllers are doing more than passing data to and from the user.[^s1] For smaller teams, the service and selector ideas can be adopted on their own without the full library, since Trailhead notes the Unit of Work is helpful but not required for a service layer.[^s3]

## Connections

The patterns are a way of structuring **Apex**, their broader node.[^s2] Because trigger logic belongs in the Domain layer, it underpins one flavour of the **trigger framework pattern**, and services are designed to be called unchanged from **Batch Apex**.[^s2][^s4] Selectors are the single home for **SOQL**, and the Unit of Work **depends on** the savepoint and rollback mechanics of **transaction control**.[^s4][^s3] Clear layering **mitigates** **technical debt** by limiting the blast radius of change, and it eases the loose coupling that **package dependencies** need when an org is split into packages.[^s1] Unit testing each layer in isolation is where the companion **ApexMocks** library **integrates with** fflib.[^s5]

## Sources

[^s1]: Salesforce Trailhead, "Apex Enterprise Patterns: Service Layer — Learn About Separation of Concerns". https://trailhead.salesforce.com/content/learn/modules/apex_patterns_sl/apex_patterns_sl_soc (accessed 2026-11-08)
[^s2]: Salesforce Trailhead, "Apex Enterprise Patterns: Service Layer — Learn Service Layer Principles". https://trailhead.salesforce.com/content/learn/modules/apex_patterns_sl/apex_patterns_sl_learn_sl_principles (accessed 2026-11-08)
[^s3]: Salesforce Trailhead, "Apex Enterprise Patterns: Service Layer — Learn Unit of Work Principles". https://trailhead.salesforce.com/content/learn/modules/apex_patterns_sl/apex_patterns_sl_learn_uow_principles (accessed 2026-11-08)
[^s4]: Salesforce Trailhead, "Apex Enterprise Patterns: Domain & Selector Layers — Learn Selector Layer Principles". https://trailhead.salesforce.com/content/learn/modules/apex_patterns_dsl/apex_patterns_dsl_learn_selector_l_principles (accessed 2026-11-08)
[^s5]: apex-enterprise-patterns, "fflib-apex-common" (GitHub repository). https://github.com/apex-enterprise-patterns/fflib-apex-common (accessed 2026-11-08)
