---
id: kt:apex
type: Language
title: Apex
aliases: [Apex programming language, Apex code, Salesforce Apex, Apex language]
domain: development
summary: >-
  Salesforce's strongly typed, object-oriented, Java-like programming language that is compiled, stored and executed
  on the Salesforce Platform to add server-side business logic, data manipulation and transaction control.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:apex-triggers, kt:asynchronous-apex, kt:apex-testing, kt:multitenancy, kt:lightning-web-components]
relations:
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: alternativeTo, object: kt:flow-builder}
sources:
  - id: s1
    title: "Apex Developer Guide (Winter '27, API version 68.0)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_dev_guide.htm
    type: official-docs
    accessed: 2026-11-01
  - id: s2
    title: "Apex Developer Guide: What is Apex?"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/apex-dev/references/apex-dev/apex-intro-what-is-apex.html
    type: official-docs
    accessed: 2026-11-01
  - id: s3
    title: "Apex Developer Guide: How Does Apex Work?"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/apex-dev/references/apex-dev/apex-intro-how-does-apex-work.html
    type: official-docs
    accessed: 2026-11-01
  - id: s4
    title: "Apex Developer Guide: Developing Code in the Cloud"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/apex-dev/references/apex-dev/apex-intro-apex-limitation.html
    type: official-docs
    accessed: 2026-11-01
  - id: s5
    title: "Apex Developer Guide: When Should I Use Apex?"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/apex-dev/references/apex-dev/apex-intro-when-use-apex.html
    type: official-docs
    accessed: 2026-11-01
  - id: s6
    title: "Trailhead: Apex Basics & Database — Get Started with Apex"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/apex_database/apex_database_intro
    type: official-learning
    accessed: 2026-11-01
created: 2026-11-01
---

# Apex

Apex is the proprietary programming language of the Salesforce Platform: a strongly typed, object-oriented language that executes flow-control and transaction-control statements on Salesforce's servers, alongside calls made through the platform APIs.[^s1] Salesforce describes it informally as Java for Salesforce, because it uses classes, typed variables and familiar control statements, yet it behaves much like a database stored procedure — grouping queries and DML into one unit of work on the server.[^s1][^s2] This article was checked against the Winter '27 edition of the Apex Developer Guide (API version 68.0).[^s1]

## Language characteristics

The Developer Guide lists a consistent set of traits.[^s2][^s6]

- **Integrated with the database.** DML statements with built-in exception handling, inline SOQL and SOSL, bulk loops and record locking are part of the language itself.[^s2]
- **Rigorous.** Object and field names are referenced directly, so a bad reference fails at compile time; the platform also records dependencies, so a field or object still used by active Apex cannot be deleted.[^s2]
- **Hosted and multitenant aware.** The platform interprets, executes and controls Apex, and its runtime stops runaway code from monopolising shared resources, failing it with an explicit error.[^s2][^s6]
- **Easy to test.** Unit testing and code-coverage reporting are built in, and Salesforce runs customers' Apex tests before platform upgrades.[^s2]
- **Versioned.** Each class or trigger is saved against an API version, which keeps its behaviour stable as the platform evolves.[^s2][^s6]

Supported constructs include classes, interfaces and inheritance; primitives, sObjects, enums and collections (lists, sets and maps); conditionals and loops; triggers; and transactions with rollback. Unlike Java, Apex is case-insensitive and adds a `global` access modifier that exposes code across namespaces.[^s6]

## How it works

Nothing runs on the client. When a developer saves Apex, the application server compiles it into an abstract instruction set that the Apex runtime interpreter understands, and stores those instructions as metadata. When a user action — a button click, a record save, a page load — invokes the code, the server fetches the compiled instructions, runs them through the interpreter and returns the result; end users see no difference in response time compared with standard platform requests.[^s3] Code can be written locally with the Salesforce Extensions for VS Code or in a browser console, and anonymous Apex lets developers execute snippets on the fly, with debug logs produced as for any other execution.[^s6] The recommended lifecycle is to build in a sandbox, debug with debug logs, unit-test, and distribute through packages.[^s1]

## Limits and gotchas

Apex is deliberately not a general-purpose language. It cannot render UI elements other than error messages, change standard platform functionality (it can only add to it or prevent it), create temporary files, or spawn threads.[^s4] Because every org shares the same infrastructure, governor limits cap how many operations — for example SOQL queries or DML statements — a single process may perform.[^s4] A single request can carry anywhere from 1 to 50,000 records, so code that handles one record at a time is a classic cause of limit exceptions; bulkification is mandatory, not optional.[^s4]

## When to use it (and when not)

Salesforce positions Apex for logic beyond declarative tools: exposing web services and email services, complex validation across several objects, business processes Flow Builder cannot express, custom transaction logic spanning the whole transaction, and logic bound to a save operation regardless of whether it starts in the UI, Visualforce or the SOAP API.[^s5] For custom user interfaces, Lightning Web Components are the recommended model, calling Apex for server-side work; for simple single-record API integrations without savepoints or rollback, the standard SOAP API may be enough.[^s5] In practice, teams prefer Flow for requirements it handles cleanly and reach for Apex when volume, complexity or transactional control demands it.[^s5]

## Connections

Apex is a core capability of the **Salesforce Platform** and inherits its constraints from **multitenancy**, which is why it is governed by **governor limits**.[^s2][^s4] Its database integration makes **SOQL** the native way to read data from Apex.[^s2] Three existing nodes are specialisations of it: **Apex triggers** attach Apex to record events, **asynchronous Apex** defers work to queues and batches, and **Apex testing** covers the built-in unit-test framework.[^s2][^s6] It is the code-based alternative to **Flow Builder** and the server-side partner of **Lightning Web Components**.[^s5]

## Sources
[^s1]: Salesforce Developers, "Apex Developer Guide (Winter '27, API version 68.0)". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_dev_guide.htm (accessed 2026-11-01)
[^s2]: Salesforce Developers, "Apex Developer Guide: What is Apex?". https://developer.salesforce.com/docs/platform/apex-dev/references/apex-dev/apex-intro-what-is-apex.html (accessed 2026-11-01)
[^s3]: Salesforce Developers, "Apex Developer Guide: How Does Apex Work?". https://developer.salesforce.com/docs/platform/apex-dev/references/apex-dev/apex-intro-how-does-apex-work.html (accessed 2026-11-01)
[^s4]: Salesforce Developers, "Apex Developer Guide: Developing Code in the Cloud". https://developer.salesforce.com/docs/platform/apex-dev/references/apex-dev/apex-intro-apex-limitation.html (accessed 2026-11-01)
[^s5]: Salesforce Developers, "Apex Developer Guide: When Should I Use Apex?". https://developer.salesforce.com/docs/platform/apex-dev/references/apex-dev/apex-intro-when-use-apex.html (accessed 2026-11-01)
[^s6]: Salesforce Trailhead, "Apex Basics & Database — Get Started with Apex". https://trailhead.salesforce.com/content/learn/modules/apex_database/apex_database_intro (accessed 2026-11-01)
