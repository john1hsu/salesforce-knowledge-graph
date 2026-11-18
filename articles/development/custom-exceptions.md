---
id: kt:custom-exceptions
type: Concept
title: Custom Exceptions
aliases: [Apex custom exceptions, user-defined exceptions, custom exception classes]
domain: development
summary: >-
  Developer-defined Apex exception classes that extend the built-in Exception class, letting code signal and catch
  domain-specific error conditions (such as an invalid order state) instead of relying only on system exceptions.
release: "Winter '27"
status: current
broader: [kt:apex]
related: [kt:limit-exception, kt:transaction-control, kt:apex-testing, kt:trigger-framework-pattern, kt:apex-logging-and-debug-logs]
relations:
  - {predicate: consumedBy, object: kt:lightning-web-components}
  - {predicate: consumedBy, object: kt:aura-components}
sources:
  - id: s1
    title: "Apex Developer Guide: Create Custom Exceptions"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_exception_custom.htm
    type: official-docs
    accessed: 2026-11-18
  - id: s2
    title: "Apex Reference Guide: Exception Class and Built-In Exceptions"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_classes_exception_methods.htm
    type: official-docs
    accessed: 2026-11-18
  - id: s3
    title: "Apex Developer Guide: Exception Statements"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/pages/apex_exception_statements.htm
    type: official-docs
    accessed: 2026-11-18
  - id: s4
    title: "Lightning Web Components Developer Guide: Handle Errors from Apex"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/apex-error-handling.html
    type: official-docs
    accessed: 2026-11-18
created: 2026-11-18
---

# Custom Exceptions

A custom exception is an Apex class that a developer writes to represent an error condition specific to their application, for example `PurchaseException` when an order can't be placed. You declare one by extending the system-defined `Exception` base class, such as `public class MyException extends Exception {}`, and the class name must end with the word `Exception`.[^s1] Because every Apex exception descends from that base class, a custom exception inherits the same constructors and common methods as built-in types such as `DmlException`, `QueryException`, `MathException` or `NullPointerException`.[^s1][^s2]

## How it works

Custom exceptions are full classes. They can be top-level classes or nested inside another class, and they can declare member variables, methods and constructors and implement interfaces, which lets a team attach extra context (an error code, the offending record) to the error.[^s1] Apex gives every exception class four constructor shapes without any code: no arguments, a single message string, a single exception that becomes the cause, or a message plus a cause.[^s1]

The inherited methods are the standard exception toolkit: `getMessage` and `setMessage` for the user-facing text, `getCause` and `initCause` for the wrapped cause (`initCause` only works if no cause is set yet), `getLineNumber`, `getStackTraceString`, and `getTypeName`, which returns the exception's type name.[^s2] Wrapping is the common idiom: catch a low-level system exception, then throw your own exception with the original as its cause, so callers see a meaningful type while `getCause` and the stack trace still show the root failure.[^s1]

You raise a custom exception with `throw`, which takes an exception object, and handle it with `try`/`catch`/`finally`.[^s3] A `try` needs at least one `catch` or a `finally`. Each `catch` handles a distinct type, only the first matching block runs, and a catch for the generic `Exception` type must be the last one.[^s3] A single `finally` runs whether or not anything was thrown, so it suits cleanup.[^s3]

## Hierarchies

User-defined exceptions can form their own inheritance tree. Declaring a `virtual` base such as `BaseException` and extending it with more specific types lets one `catch (BaseException e)` block handle every exception in that family, while code that cares about a specific case can catch the subclass first.[^s1] This mirrors how a catch for the generic `Exception` type catches everything catchable, which is why it must come last.[^s3]

## Limits and gotchas

- Not everything is catchable: limit exceptions, failed `System.assert` calls and license exceptions stop execution outright.[^s3]
- When one of those uncatchable exceptions fires, neither your `catch` blocks nor your `finally` block run, so a custom-exception handler can't recover from them.[^s2][^s3]
- From API version 41.0, statements that can never be reached, such as code after an unconditional `throw`, are compile-time errors.[^s3]
- Name every class that extends `Exception` with the `Exception` suffix, as the Apex Developer Guide instructs.[^s1]

## Custom exceptions at the UI boundary

When Apex called from a Lightning web component throws an unhandled custom exception, the error body the client receives reports the qualified class name as `exceptionType`, sets `isUserDefinedException` to true, and includes a stack trace with class names and line numbers.[^s4] To return only a controlled message, throw `AuraHandledException`, which works for both LWC and Aura; its response body carries just the message, though anything you put in that message, such as the text from `e.getMessage()`, still reaches the browser.[^s4] Some teams instead return a wrapper class whose fields arrive as a JSON string in the message, which the component parses, to standardize error shapes across components.[^s4]

## When to use it (and when not)

Use a custom exception when callers need to distinguish a business-rule failure from a platform failure, or when a service layer should translate many low-level errors into one well-named type.[^s1] For an expected condition such as a possibly null input, the guidance for components is to avoid an exception altogether and use the safe navigation operator, which simply yields null.[^s4]

## Connections

Custom exceptions are a feature of **Apex**. They contrast with **LimitException**, the built-in governor-limit exception that no handler can catch.[^s2][^s3] They are often caught alongside savepoint rollbacks in **Transaction Control**, though an uncatchable exception skips such handlers entirely;[^s3] trigger handlers built on a **trigger framework** often throw domain exceptions, and **Apex testing** asserts that the right type is thrown. Exceptions that cross to the client are consumed by **Lightning Web Components** and **Aura components**, where `AuraHandledException` controls what users see.[^s4] Their stack traces and messages are what developers read in **Apex logging and debug logs**.[^s2]

## Sources
[^s1]: Salesforce Developers, "Apex Developer Guide: Create Custom Exceptions". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_exception_custom.htm (accessed 2026-11-18)
[^s2]: Salesforce Developers, "Apex Reference Guide: Exception Class and Built-In Exceptions". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_classes_exception_methods.htm (accessed 2026-11-18)
[^s3]: Salesforce Developers, "Apex Developer Guide: Exception Statements". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/pages/apex_exception_statements.htm (accessed 2026-11-18)
[^s4]: Salesforce Developers, "Lightning Web Components Developer Guide: Handle Errors from Apex". https://developer.salesforce.com/docs/platform/lwc/guide/apex-error-handling.html (accessed 2026-11-18)
