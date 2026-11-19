---
id: kt:apex-defined-types
type: Feature
title: Apex-Defined Types
aliases: [Apex-defined data type, Apex-Defined variable, Apex-defined types in Flow, Apex class data type in Flow]
domain: development
summary: >-
  A Flow data type backed by an Apex class whose @AuraEnabled fields describe a structured object, letting flows,
  invocable actions, External Services and flow screen components pass and manipulate complex, nested data such as
  web-service payloads without converting it to records or text.
release: "Winter '27"
status: current
broader: [kt:apex, kt:flow-builder]
related: [kt:transform-element, kt:custom-flow-screen-components, kt:flow-http-callout, kt:lightning-web-components]
relations:
  - {predicate: consumedBy, object: kt:external-services}
  - {predicate: consumedBy, object: kt:agent-actions}
  - {predicate: consumedBy, object: kt:invocable-methods}
  - {predicate: contrastsWith, object: kt:standard-objects}
sources:
  - id: s1
    title: "Supported Data Types in Flows (Lightning Web Components Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/lwc/guide/use-flow-data-types.html
    type: official-docs
    accessed: 2026-11-19
  - id: s2
    title: "InvocableVariable Annotation (Apex Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_classes_annotation_InvocableVariable.htm
    type: official-docs
    accessed: 2026-11-19
  - id: s3
    title: "Create a Flow Using External Services Actions (Use External Services with a Flow)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/use-external-services-with-a-flow/create-a-flow-using-external-services-actions
    type: official-learning
    accessed: 2026-11-19
  - id: s4
    title: "External Services (Apex Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_external_services.htm
    type: official-docs
    accessed: 2026-11-19
  - id: s5
    title: "Apex-Based Custom Lightning Types (Lightning Types Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/lightning-types/guide/lightning-types-apex.html
    type: official-docs
    accessed: 2026-11-19
  - id: s6
    title: "Part 1: Manipulate Complex Internet Data in Flow Without Code"
    publisher: UnofficialSF
    url: https://unofficialsf.com/part-1-manipulate-complex-internet-data-in-flow-without-code/
    type: community
    accessed: 2026-11-19
  - id: s7
    title: "Part 2: Manipulate Complex Internet Data in Flow Without Code"
    publisher: UnofficialSF
    url: https://unofficialsf.com/part-2-manipulate-complex-internet-data-in-flow-without-code/
    type: community
    accessed: 2026-11-19
created: 2026-11-19
---

# Apex-Defined Types

An **Apex-defined type** is a Flow data type whose shape comes from an Apex class rather than from an sObject or a primitive. The class declares fields marked `@AuraEnabled`, and Flow treats an instance of the class as a structured value that a variable, a collection variable, an invocable action or a screen component can carry.[^s1] It is the bridge that lets declarative automation work with data that has no record behind it, most commonly the nested JSON a web service returns.[^s6]

## How it works

A developer writes a plain Apex class and annotates each property that Flow should see with `@AuraEnabled`. For flow screen components, the supported member types are Boolean, Integer, Long, Decimal, Double, Date, DateTime and String, each usable as a single value or as a List.[^s1] In Flow Builder, an admin creates a variable, sets its data type to **Apex-Defined**, and picks the class; the same choice exists for collection variables, so a list of class instances can be looped over like a record collection.[^s3][^s7] In the LWC mapping of Flow types, the Apex-Defined flow type corresponds to a custom Apex class on the component side.[^s1]

Classes reach Flow in three common ways:

- **Invocable actions.** An `@InvocableMethod` can accept and return wrapper classes; `@InvocableVariable` supports lists of objects created from Apex classes, and lists of lists.[^s2]
- **External Services.** Registering an OpenAPI spec generates Apex classes in the `ExternalService` namespace for the API's objects, and those generated types appear as Apex-Defined choices in Flow.[^s4][^s3]
- **Hand-written payload classes.** UnofficialSF's tutorial models a product API response as classes generated from sample JSON, parses the response in an action, and returns the typed result to the flow.[^s6]

The Trailhead External Services project shows the pattern end to end: two Apex-Defined variables of type `ExternalService__BankService_accountDetails` store the success and the 409-conflict outputs of an action, and later Decision, Assignment and Update Records elements read their `id` fields.[^s3]

## Limits and gotchas

- **Field visibility.** A property without `@AuraEnabled` is invisible to Flow and to screen components.[^s1][^s6]
- **Invocable shapes.** Per the InvocableVariable reference, Apex class objects are supported inside lists or lists of lists, not listed as a single standalone type.[^s2]
- **Constructors.** From API version 66.0, classes used as invocable action parameters need a visible no-argument constructor: public, or global if invoked from outside a managed package.[^s2]
- **Nesting.** The tutorial author had to move nested inner classes into their own files, and had to rename a JSON key that collides with an Apex reserved word.[^s6]
- **Deep paths.** Flow's resource picker exposes first-level fields; deeper fields need dot notation typed by hand.[^s7]
- **Case sensitivity.** Invocable variable names must match exactly what the flow references.[^s2]

## When to use it (and when not)

Use an Apex-defined type when a flow must hold structured, non-persistent data: an API response, a calculation result with several fields, or a payload passed between an action and a screen component.[^s6][^s1] When the data is a Salesforce record, use a Record variable instead.[^s1] When an External Services registration can generate the classes from an API spec, prefer it to hand-written wrappers, because the generated types are strongly typed and avoid manual JSON handling.[^s4][^s3] The `kt:transform-element` can map these values into records without Loop and Assignment chains.

## Connections

Apex-defined types sit under `kt:apex` (they are Apex classes) and `kt:flow-builder` (they are a Flow data type).[^s1] `kt:external-services` and invocable methods consume them as input and output shapes, and `kt:custom-flow-screen-components` built with `kt:lightning-web-components` declare them as properties.[^s4][^s2][^s1] The same `@AuraEnabled` modelling also powers Apex-based custom Lightning types used by `kt:agent-actions`: there each class must be a global top-level class with `@JsonAccess` annotations, and renaming fields or classes can break active actions.[^s5] They contrast with sObject record variables: in the tutorial, Apex-defined values hold the transient API data and are then mapped into Product records that the flow saves.[^s7]

## Sources

[^s1]: Salesforce, "Supported Data Types in Flows" (LWC Developer Guide). https://developer.salesforce.com/docs/platform/lwc/guide/use-flow-data-types.html (accessed 2026-11-19)
[^s2]: Salesforce, "InvocableVariable Annotation" (Apex Developer Guide). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_classes_annotation_InvocableVariable.htm (accessed 2026-11-19)
[^s3]: Trailhead, "Create a Flow Using External Services Actions". https://trailhead.salesforce.com/content/learn/projects/use-external-services-with-a-flow/create-a-flow-using-external-services-actions (accessed 2026-11-19)
[^s4]: Salesforce, "External Services" (Apex Developer Guide). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_external_services.htm (accessed 2026-11-19)
[^s5]: Salesforce, "Apex-Based Custom Lightning Types". https://developer.salesforce.com/docs/platform/lightning-types/guide/lightning-types-apex.html (accessed 2026-11-19)
[^s6]: UnofficialSF, "Part 1: Manipulate Complex Internet Data in Flow Without Code". https://unofficialsf.com/part-1-manipulate-complex-internet-data-in-flow-without-code/ (accessed 2026-11-19)
[^s7]: UnofficialSF, "Part 2: Manipulate Complex Internet Data in Flow Without Code". https://unofficialsf.com/part-2-manipulate-complex-internet-data-in-flow-without-code/ (accessed 2026-11-19)
