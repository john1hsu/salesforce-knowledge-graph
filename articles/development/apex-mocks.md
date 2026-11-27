---
id: kt:apex-mocks
type: Tool
title: ApexMocks
aliases: [fflib-apex-mocks, fflib ApexMocks, Apex Mocks, fflib_ApexMocks, ApexMocks framework]
domain: development
summary: >-
  An open-source, Mockito-inspired mocking framework for Apex, maintained under the apex-enterprise-patterns GitHub
  organization, that generates mock objects at run time through the Salesforce Stub API so unit tests can stub return
  values and verify calls on a class's injected dependencies.
release: "Winter '27"
status: current
broader: [kt:apex-testing]
related: [kt:testing-strategy, kt:test-data-factory]
relations:
  - {predicate: dependsOn, object: kt:apex-stub-api}
  - {predicate: dependsOn, object: kt:apex-interfaces}
  - {predicate: integratesWith, object: kt:apex-enterprise-patterns}
  - {predicate: alternativeTo, object: kt:apex-mockery}
sources:
  - id: s1
    title: "Apex Developer Guide: Build a Mocking Framework with the Stub API (Winter '27, API version 68.0)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_testing_stub_api.htm
    type: official-docs
    accessed: 2026-11-27
  - id: s2
    title: "Apex Reference Guide: StubProvider Interface"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_interface_System_StubProvider.htm
    type: official-docs
    accessed: 2026-11-27
  - id: s3
    title: "Advanced Apex Testing: Use Mock and Stub Objects"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/content/learn/modules/unit-testing-on-the-lightning-platform/mock-stub-objects
    type: official-learning
    accessed: 2026-11-27
  - id: s4
    title: "apex-enterprise-patterns/fflib-apex-mocks (README)"
    publisher: GitHub (apex-enterprise-patterns)
    url: https://github.com/apex-enterprise-patterns/fflib-apex-mocks
    type: community
    accessed: 2026-11-27
  - id: s5
    title: "Introducing apex-mockery, a Unit Test Mocking Library"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2023/06/introducing-apex-mockery-a-unit-test-mocking-library
    type: official-blog
    accessed: 2026-11-27
created: 2026-11-27
---

# ApexMocks

ApexMocks is an open-source mocking framework for Apex, published as the `fflib-apex-mocks` repository under the apex-enterprise-patterns GitHub organization and licensed BSD-3-Clause.[^s4] Its README credits the Java library Mockito as its inspiration, and it lets a unit test replace a class's collaborators with generated fakes, decide what those fakes return, and then check how the code under test called them.[^s4] It is a community project, not a Salesforce product, but it sits on a platform feature Salesforce documents and supports: the Stub API.[^s4][^s1]

## Mocks, stubs and why Apex needs them

Trailhead describes mocks and stubs as closely related fakes that stand in for real objects: a mock replaces a whole object, while a stub replaces individual methods.[^s3] The platform has long offered narrow mocking hooks such as `HttpCalloutMock` for callouts, and the Advanced Apex Testing module shows a hand-written stub built on `StubProvider` and `Test.createStub()`.[^s3] Writing such stubs by hand for every dependency is repetitive, which is the gap a general framework like ApexMocks fills.[^s3][^s4]

## How it works

The Stub API consists of the `System.StubProvider` interface and the `Test.createStub()` method; the platform creates stub objects at run time as anonymous subclasses of the class being mocked, so no mock classes need to be written, packaged or deployed.[^s1] `StubProvider` has a single method, `handleMethodCall()`, which receives the stubbed object, the method name, its return type, the parameter types and names, and the argument values, and returns the value the fake should produce.[^s2] ApexMocks implements that callback generically: a test asks `fflib_ApexMocks` for a mock of a type, and the framework records every call routed through `handleMethodCall()`.[^s4][^s2]

A typical test has three phases.[^s4] Between `startStubbing()` and `stopStubbing()` the test declares, `when(...)`-style, what each mocked method should return for given arguments.[^s4] The test then injects the mock into the class under test and runs it.[^s4] Finally `verify()` asserts that a method was called, a given number of times or (with `NEVER`) not at all.[^s4] The README links to community tutorials covering argument matchers, in-order verification and custom answers, and it supplies `fflib_ApexMocksUtils.setReadOnlyFields` for setting values such as formula fields on in-memory test records.[^s4]

## Limits and gotchas

- ApexMocks assumes dependency injection: the class under test must receive its collaborators, for example as constructor arguments typed to an interface, rather than instantiating them itself.[^s4]
- Because it rides on the Stub API, it inherits that API's rules: the mocked type must be in the same namespace as the `Test.createStub()` call.[^s1]
- The Stub API cannot mock static methods (including future methods), private methods, properties, triggers, inner classes, system types, Batchable classes, or classes with only private constructors.[^s1]
- Iterators cannot be used as the return type or a parameter type of a stubbed method.[^s1]
- Triggers cannot be mocked, so tests built on stubs complement rather than replace tests that run real DML through trigger logic.[^s1][^s3]

## When to use it (and when not)

ApexMocks pays off in codebases already layered around interfaces and injected services, because generated stubs need no extra mock classes to package or deploy.[^s4][^s1] For a few simple dependencies a hand-written `StubProvider` may be enough.[^s3] Salesforce engineers later open-sourced apex-mockery, a lighter library also built on the Stub API that offers spies, `whenCalledWith(...)` stubbing and `Expect.that(...)` assertions; it is a reasonable alternative for teams that prefer its style.[^s5]

## Connections

ApexMocks is a tool within **Apex testing**, its broader node, and it **depends on** the **Apex Stub API**, which Salesforce released in Spring '17.[^s1][^s5] It also **depends on** **Apex interfaces**, because injecting a mock requires code that depends on a contract rather than a concrete class.[^s4] It **integrates with** the **Apex Enterprise Patterns**, whose service, domain and selector layers are the injected collaborators it most often replaces, and **apex-mockery** is an **alternative** built on the same platform API.[^s4][^s5] Within a **testing strategy**, it covers fast isolated unit tests, while a **test data factory** remains the tool for tests that need real records.[^s3]

## Sources

[^s1]: Salesforce Developers, "Apex Developer Guide: Build a Mocking Framework with the Stub API" (Winter '27, API version 68.0). https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/apex_testing_stub_api.htm (accessed 2026-11-27)
[^s2]: Salesforce Developers, "Apex Reference Guide: StubProvider Interface". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_interface_System_StubProvider.htm (accessed 2026-11-27)
[^s3]: Trailhead, "Advanced Apex Testing: Use Mock and Stub Objects". https://trailhead.salesforce.com/en/content/learn/modules/unit-testing-on-the-lightning-platform/mock-stub-objects (accessed 2026-11-27)
[^s4]: apex-enterprise-patterns, "fflib-apex-mocks" README, GitHub. https://github.com/apex-enterprise-patterns/fflib-apex-mocks (accessed 2026-11-27)
[^s5]: Salesforce Developers Blog, "Introducing apex-mockery, a Unit Test Mocking Library" (June 20, 2023). https://developer.salesforce.com/blogs/2023/06/introducing-apex-mockery-a-unit-test-mocking-library (accessed 2026-11-27)
