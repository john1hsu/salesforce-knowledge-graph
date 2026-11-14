---
id: kt:apex-security-with-sharing
type: SecurityControl
title: Apex Sharing Keywords
aliases: [with sharing, without sharing, inherited sharing, Apex sharing declarations, Apex class sharing mode]
domain: development
summary: >-
  The class-level declarations with sharing, without sharing and inherited sharing, which decide whether Apex code
  enforces the running user's record-level sharing. They govern record visibility only; object and field
  permissions are enforced separately through access modes such as user mode.
release: "Winter '27"
status: current
broader: [kt:apex, kt:salesforce-sharing-model]
related: [kt:apex-managed-sharing, kt:field-level-security, kt:soql-injection, kt:apex-triggers, kt:lightning-web-components, kt:appexchange-security-review]
relations:
  - {predicate: dependsOn, object: kt:sharing-rules}
  - {predicate: contrastsWith, object: kt:apex-user-mode}
  - {predicate: coveredBy, object: kt:platform-developer-certification}
sources:
  - id: s1
    title: "Use the with sharing, without sharing, and inherited sharing Keywords (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm
    type: official-docs
    accessed: 2026-11-14
  - id: s2
    title: "Apex Versioned Behavior Changes"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/versioned_behavior_changes.htm
    type: official-docs
    accessed: 2026-11-14
  - id: s3
    title: "Protect Your Application from Sharing Violations (Secure Coding Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/secure-coding/guide/secure-coding-access-control-protect-from-sharing-violations.html
    type: official-docs
    accessed: 2026-11-14
  - id: s4
    title: "Secure Apex Classes (Lightning Web Components Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/apex-security
    type: official-docs
    accessed: 2026-11-14
  - id: s5
    title: "Write Secure Apex Controllers (Secure Server-Side Development)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/secure-serverside-development/write-secure-apex-controllers
    type: official-learning
    accessed: 2026-11-14
  - id: s6
    title: "Salesforce Certified Platform Developer Exam Guide"
    publisher: Salesforce
    url: https://help.salesforce.com/s/articleView?id=005298965&type=1&language=en_US
    type: official-learning
    accessed: 2026-11-14
created: 2026-11-14
---

# Apex Sharing Keywords

Apex classes declare a **sharing mode** with one of three keywords placed before `class`. `with sharing` makes the class respect the running user's sharing rules, `without sharing` ignores them so the code can reach records the user could not otherwise see, and `inherited sharing` adopts the mode of whatever called the class at runtime.[^s1] Because Apex can otherwise query and change data beyond what the user sees in the UI, a missing or careless declaration is one of the most common ways custom code leaks records.[^s3]

## How it works

The mode comes from the class in which a method is **defined**, not from its caller: a method in a `with sharing` class still enforces sharing when a `without sharing` class invokes it. The exception is `inherited sharing`, whose methods take on the caller's mode.[^s1][^s3]

- **Inheritance and nesting:** a subclass without its own keyword takes its parent's mode, but an inner class does not inherit from its outer class. Each class's declaration covers its constructors, initializers and methods.[^s1]
- **`inherited sharing` as an entry point:** when it starts the transaction (an Aura or Visualforce controller, an `@AuraEnabled` method called from LWC, an Apex REST service, async Apex), it runs as `with sharing`.[^s1]
- **Async:** every asynchronous job is a new entry point, so an `inherited sharing` class always runs with sharing there.[^s1]
- **Anonymous Apex and Connect in Apex** always run with sharing.[^s1]
- **Triggers** cannot declare a mode and run without sharing; the guide advises moving logic into declared handler classes.[^s1][^s3]

## Defaults changed in API 67.0

The behavior of a class with **no keyword** depends on its API version. From API 67.0 (Summer '26) such classes run with sharing, and Apex also runs in user mode by default, applying the user's object permissions and field-level security.[^s2] Classes saved at API 66.0 or earlier keep the old rule: Aura and LWC-facing controllers and classes in an inheritance chain that includes an API 67.0+ class run with sharing, a class that is not an entry point takes its caller's mode, and other entry points run without sharing.[^s1] Older training material that describes Apex as "system mode by default" reflects those pre-67.0 classes.[^s5] Salesforce still recommends declaring a keyword explicitly on every class that runs SOQL or DML, so intent survives version upgrades and reviews.[^s1][^s4]

## Limits and gotchas

- **Record access only.** Sharing keywords never enforce object (CRUD) or field-level permissions; enforce those with user-mode operations, `stripInaccessible()` or describe checks.[^s1][^s4][^s5]
- **Behavior differences.** With sharing enforced, queries may return fewer rows and DML can fail, for example when a lookup points at a record the user cannot see.[^s3][^s5]
- **Dual-mode code.** An `inherited sharing` class must be safe whether it ends up running with or without sharing, because its mode is only known at runtime.[^s1]
- **`WITH SECURITY_ENFORCED` is unavailable from API 67.0;** Salesforce points developers to `WITH USER_MODE` instead.[^s2]

## When to use which

Make `with sharing` the default for least privilege. Reserve `without sharing` for small, deliberate elevations, such as letting a community user read a specific record, and keep that code narrow and reviewed.[^s1][^s3] Use `inherited sharing` for reusable service classes called by both secure and privileged callers, and to make intent explicit instead of omitting a keyword.[^s1][^s3] For AppExchange packages, bypassing sharing is acceptable only in limited, documented cases, such as a bespoke policy for the package's own custom objects; it never applies to standard objects.[^s3]

## Connections

The keywords are the code-level switch for the **sharing model** and its **sharing rules**, and sit alongside **Apex managed sharing**, which writes share records rather than filtering by them.[^s1] They complement, rather than replace, object and **field-level security** enforcement through Apex user mode.[^s4] Trigger handlers in **Apex triggers** and `@AuraEnabled` controllers behind **Lightning Web Components** are the places where the choice matters most.[^s1][^s4] Sharing violations are checked in **AppExchange security review**, and preventing data-access security vulnerabilities is an objective of the **Platform Developer certification** exam.[^s3][^s6]

## Sources
[^s1]: Salesforce Developers, "Use the with sharing, without sharing, and inherited sharing Keywords". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm (accessed 2026-11-14)
[^s2]: Salesforce Developers, "Apex Versioned Behavior Changes". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/versioned_behavior_changes.htm (accessed 2026-11-14)
[^s3]: Salesforce Developers, "Protect Your Application from Sharing Violations". https://developer.salesforce.com/docs/platform/secure-coding/guide/secure-coding-access-control-protect-from-sharing-violations.html (accessed 2026-11-14)
[^s4]: Salesforce Developers, "Secure Apex Classes". https://developer.salesforce.com/docs/platform/lwc/guide/apex-security (accessed 2026-11-14)
[^s5]: Trailhead, "Write Secure Apex Controllers". https://trailhead.salesforce.com/content/learn/modules/secure-serverside-development/write-secure-apex-controllers (accessed 2026-11-14)
[^s6]: Salesforce, "Salesforce Certified Platform Developer Exam Guide". https://help.salesforce.com/s/articleView?id=005298965&type=1&language=en_US (accessed 2026-11-14)
