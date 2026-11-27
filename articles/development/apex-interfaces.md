---
id: kt:apex-interfaces
type: Concept
title: Apex Interfaces
aliases: [Apex interface, interface keyword in Apex, implements keyword, Apex interface implementation]
domain: development
summary: >-
  Apex type declarations that list method signatures without bodies; a class that uses the implements keyword must
  supply every method, which lets code depend on a contract (a data type) rather than on a concrete class.
release: "Winter '27"
status: current
broader: [kt:apex]
related: [kt:apex-enterprise-patterns, kt:apex-collections, kt:sandboxpostcopy-interface, kt:apex-testing, kt:second-generation-managed-packages]
relations:
  - {predicate: enables, object: kt:batch-apex}
  - {predicate: enables, object: kt:apex-mocks}
sources:
  - id: s1
    title: "Apex Developer Guide: Interfaces (Winter '27, API version 68.0)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_classes_interfaces.htm
    type: official-docs
    accessed: 2026-11-27
  - id: s2
    title: "Apex Developer Guide: Extending a Class (Winter '27, API version 68.0)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_classes_extending.htm
    type: official-docs
    accessed: 2026-11-27
  - id: s3
    title: "Apex Developer Guide: Custom Iterators (Winter '27, API version 68.0)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_classes_iterable.htm
    type: official-docs
    accessed: 2026-11-27
  - id: s4
    title: "Apex Reference Guide: Callable Interface"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_interface_System_Callable.htm
    type: official-docs
    accessed: 2026-11-27
created: 2026-11-27
---

# Apex Interfaces

An Apex interface resembles a class in which none of the methods are implemented: it declares method signatures, and their bodies are left empty. A class opts in with the `implements` keyword and must then provide a body for every method the interface declares. Salesforce presents interfaces as an abstraction layer that separates what a method promises from how it is carried out.[^s1]

## How it works

An interface is declared with the `interface` keyword, for example a `PurchaseOrder` interface with a single `discount()` method. Two classes, one for customers and one for employees, can each implement it and return different discounts. Methods inside the interface carry no access modifiers and consist only of their signature.[^s1]

Declaring an interface also declares a new data type. A variable typed as the interface can hold any instance of a class that implements it, or of a sub-interface type, so calling code can work against the contract and stay unaware of which concrete class it received.[^s1]

Apex has single inheritance for classes: a class can extend only one other class, but it can implement more than one interface. Interfaces can also extend other interfaces, and the extending interface then exposes all methods of the one it extends. This is how Apex combines a single class hierarchy (built with `virtual`, `abstract` and `override`) with multiple contracts per class.[^s2]

## Platform interfaces you implement

Many platform features are entered by implementing a Salesforce-defined interface. Custom iteration uses `Iterator` (methods `hasNext`, returning a Boolean, and `next`) and `Iterable` (a single `iterator` method that returns an Iterator). The guide requires these methods to be declared `global` or `public`, and its example `next()` throws `NoSuchElementException` when no items remain. A Batch Apex class implementing `Database.Batchable` can return an `Iterable` from its `start` method instead of a query locator, which suits data from outside Salesforce or built from several queries.[^s3]

`System.Callable` is a generic interface with one method, `call(String action, Map<String,Object> args)`, returning an Object. Salesforce describes it as a way to build loosely coupled integrations between Apex classes or triggers, including code in separate packages, where callers cast an instance to `Callable` rather than compiling against the provider's class.[^s4]

## Limits and gotchas

- A class that implements an interface must define all of its methods, or it does not compile.[^s1]
- After a class is uploaded in a Managed - Released package version, you cannot add a method to a `global` interface.[^s1]
- From API version 61.0, a private method is no longer overridden by a same-signature instance method in a subclass; API 60.0 and earlier did override it.[^s1]
- From API version 65.0, abstract and override methods need a `protected`, `public` or `global` modifier; without one the method defaults to private and fails to compile.[^s2]
- Salesforce warns that `Callable` is not meant to replace specific interfaces and is unrelated to Java's asynchronous `Callable`.[^s4]

## When to use it (and when not)

Define an interface when several implementations must be interchangeable, such as pricing rules, integration adapters or strategies selected from metadata, or when tests need a substitute implementation, because callers depend only on the interface type.[^s1] Prefer a `virtual` or `abstract` base class when implementations should share code, since interfaces carry no method bodies; a class can still extend one base class while implementing interfaces.[^s2] Reach for `Callable` only when compile-time coupling must be avoided, for example across packages; otherwise a specific, typed interface gives clearer contracts.[^s4]

## Connections

Interfaces are a core language feature of `kt:apex`, which is why this node sits under it.[^s1] They enable `kt:batch-apex`, whose classes implement `Database.Batchable` and can take their records from a custom `Iterable`, a link that also ties them to `kt:apex-collections`.[^s3] Because a variable typed as an interface accepts any implementing class, they are the mechanism behind the layered service designs of `kt:apex-enterprise-patterns`, the substitutable fakes of `kt:apex-mocks`, and dependency swapping in `kt:apex-testing`.[^s1] `kt:sandboxpostcopy-interface` is one example of a Salesforce-defined interface that a class implements to plug into a platform process.[^s1] The rule that methods cannot be added to a released global interface is a packaging constraint relevant to `kt:second-generation-managed-packages`.[^s1]

## Sources
[^s1]: Salesforce Developers, "Apex Developer Guide: Interfaces" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_classes_interfaces.htm (accessed 2026-11-27)
[^s2]: Salesforce Developers, "Apex Developer Guide: Extending a Class" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_classes_extending.htm (accessed 2026-11-27)
[^s3]: Salesforce Developers, "Apex Developer Guide: Custom Iterators" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_classes_iterable.htm (accessed 2026-11-27)
[^s4]: Salesforce Developers, "Apex Reference Guide: Callable Interface". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_interface_System_Callable.htm (accessed 2026-11-27)
