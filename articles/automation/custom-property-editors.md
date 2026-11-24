---
id: kt:custom-property-editors
type: Feature
title: Custom Property Editors
aliases: [custom property editor, CPE, Flow Builder custom property editor, configurationEditor]
domain: automation
summary: >-
  Lightning web components that replace Flow Builder's standard input form when an admin configures a custom
  flow screen component or an Apex invocable action; they are registered with a configurationEditor attribute or
  modifier and talk to Flow Builder through inputVariables, builderContext, genericTypeMappings, validate() and
  configuration_editor_* events.
release: "Winter '27"
status: current
broader: [kt:flow-builder, kt:lightning-web-components]
related: [kt:screen-flow, kt:apex-defined-types, kt:invocable-actions-api]
relations:
  - {predicate: integratesWith, object: kt:flow-builder}
  - {predicate: consumedBy, object: kt:custom-flow-screen-components}
  - {predicate: consumedBy, object: kt:invocable-apex-actions}
sources:
  - id: s1
    title: "Custom Property Editor JavaScript Interface"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/use-flow-custom-property-editor-interface.html
    type: official-docs
    accessed: 2026-11-24
  - id: s2
    title: "Customize Action and Screen Component UI in Flow Builder"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/use-flow-custom-property-editor.html
    type: official-docs
    accessed: 2026-11-24
  - id: s3
    title: "Example: Custom Property Editor for an Invocable Action"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/use-flow-custom-property-editor-action-example.html
    type: official-docs
    accessed: 2026-11-24
  - id: s4
    title: "Example: Custom Property Editor for a Screen Component"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/use-flow-custom-property-editor-lwc-example.html
    type: official-docs
    accessed: 2026-11-24
  - id: s5
    title: "Example: Generic SObject Input for Invocable Actions"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/use-flow-custom-property-editor-sobject-action-example.html
    type: official-docs
    accessed: 2026-11-24
  - id: s6
    title: "InvocableMethod Annotation (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_classes_annotation_InvocableMethod.htm
    type: official-docs
    accessed: 2026-11-24
created: 2026-11-24
---

# Custom Property Editors

## Definition

A **custom property editor (CPE)** is a Lightning web component that Flow Builder shows in place of its standard property panel when an admin configures an Apex action or a custom flow screen component.[^s2] Instead of one text box or combo box per input, the developer can offer a purpose-built UI, such as a slider, a picker of flow variables or a row editor, so admins enter valid values without knowing the underlying parameter names.[^s2][^s4] The CPE runs only at design time in Flow Builder; the component or action it configures is what runs when the flow executes.[^s6]

## How it is registered

The registration point depends on what is being configured.

- **Screen component:** the component's `.js-meta.xml` names the editor in the `configurationEditor` attribute of its `lightning__FlowScreen` `targetConfig`, e.g. `c-volume-editor`.[^s4][^s1]
- **Invocable action:** the Apex method's `@InvocableMethod` annotation takes a `configurationEditor` modifier naming the editor component.[^s3][^s6]

Without the modifier, Flow Builder falls back to its standard property editor.[^s6] The examples use the `c` namespace and tell developers to substitute the org's own namespace if it has one.[^s4][^s3] The editor itself is an ordinary LWC bundle with its own configuration file.[^s3]

## The JavaScript interface

Flow Builder and the editor exchange data through a small contract of public properties, one method and three events.[^s1]

- **`inputVariables`** holds the current value of each input as `name`, `value` and `valueDataType`; editors usually expose it as an `@api` getter and setter.[^s1][^s3]
- **`builderContext`** describes the flow being built: arrays such as `variables`, `formulas`, `constants`, `screens`, `actionCalls`, `recordLookups` and `stages`, which an editor can use to offer existing resources.[^s1]
- **`elementInfo`** gives the element's `apiName` and a `type` of `Screen` or `Action`, so one editor can tell several instances apart.[^s1]
- **`genericTypeMappings`** lists `typeName`/`typeValue` pairs for generic sObject inputs and outputs, such as `T__param1` mapped to Account.[^s1]

To report a change, the editor dispatches a bubbling, composed event. `configuration_editor_input_value_changed` carries `name`, `newValue` and `newValueDataType`; `configuration_editor_input_value_deleted` carries only `name`; and `configuration_editor_generic_type_mapping_changed` carries `typeName` and `typeValue`.[^s1]

For an action's generic types, inputs are addressed with a `T__` prefix and outputs with `U__`, and the name after the prefix must match the `@InvocableVariable` it refers to.[^s1][^s5] For a screen component, `typeName` refers to the `propertyType` declared in the configuration file, with a `[]` suffix for collections.[^s1]

## Validation and gotchas

An editor can expose `@api validate()`. Flow Builder calls it when the admin clicks **Done**, and the method returns a list of `key` and `errorString` entries.[^s1] Flow Builder displays only the number of errors and blocks saving, so the editor has to render the messages itself, for example with `setCustomValidity()` and `reportValidity()` on its inputs.[^s3][^s4]

Other practical points from the documentation:

- The editor does not change runtime rules: invocable methods must still be static, public or global, one per class, with at most one input parameter.[^s6]
- In managed packages, only global invocable methods appear in subscriber-org Flow Builder, and an added invocable method cannot be removed in later versions.[^s6]
- Values the editor sends must use a data type Flow understands, such as `String`, `Number` or `reference` for a resource.[^s1][^s5]

## When to use it

A CPE is worth building when a component or action is reused by many admins and its inputs are easy to get wrong: interdependent fields, generic sObject types that must be chosen first, or values better picked from the flow's own resources.[^s5][^s2] For a component with a few simple inputs, the standard property editor is less code to maintain.[^s6]

## Connections

- **Broader:** an extension point of **Flow Builder**, built as a **Lightning web component**.[^s2]
- **Consumed by** **custom flow screen components** and **invocable Apex actions**, the two element kinds that can name an editor.[^s4][^s3]
- **Related:** **Screen Flow**, where configured components appear; **Apex-defined types** and generic sObject inputs, whose types the editor can map; and the **Invocable Actions API**.[^s1][^s5]

## Sources

[^s1]: Salesforce Developers, "Custom Property Editor JavaScript Interface". https://developer.salesforce.com/docs/platform/lwc/guide/use-flow-custom-property-editor-interface.html (accessed 2026-11-24)
[^s2]: Salesforce Developers, "Customize Action and Screen Component UI in Flow Builder". https://developer.salesforce.com/docs/platform/lwc/guide/use-flow-custom-property-editor.html (accessed 2026-11-24)
[^s3]: Salesforce Developers, "Example: Custom Property Editor for an Invocable Action". https://developer.salesforce.com/docs/platform/lwc/guide/use-flow-custom-property-editor-action-example.html (accessed 2026-11-24)
[^s4]: Salesforce Developers, "Example: Custom Property Editor for a Screen Component". https://developer.salesforce.com/docs/platform/lwc/guide/use-flow-custom-property-editor-lwc-example.html (accessed 2026-11-24)
[^s5]: Salesforce Developers, "Example: Generic SObject Input for Invocable Actions". https://developer.salesforce.com/docs/platform/lwc/guide/use-flow-custom-property-editor-sobject-action-example.html (accessed 2026-11-24)
[^s6]: Salesforce Developers, "InvocableMethod Annotation (Apex Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_classes_annotation_InvocableMethod.htm (accessed 2026-11-24)
