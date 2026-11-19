---
id: kt:custom-flow-screen-components
type: Feature
title: Custom Flow Screen Components
aliases: [custom screen components, LWC flow screen components, lightning__FlowScreen components, flow screen LWC]
domain: automation
summary: >-
  Lightning web components exposed to the lightning__FlowScreen target so admins can drop them onto screen-flow
  screens; they exchange data with the flow through @api properties declared in the component's js-meta.xml,
  report changes with FlowAttributeChangeEvent, can drive navigation, validate input, and can ship a custom
  property editor for Flow Builder.
release: "Winter '27"
status: current
broader: [kt:screen-flow, kt:lightning-web-components]
related: [kt:flow-builder, kt:aura-components, kt:invocable-apex-actions, kt:lightning-data-service]
relations:
  - {predicate: integratesWith, object: kt:flow-builder}
  - {predicate: configuredVia, object: kt:custom-property-editors}
  - {predicate: dependsOn, object: kt:apex-defined-types}
sources:
  - id: s1
    title: "Flow Support (lightning/flowSupport)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-flow-support.html
    type: official-docs
    accessed: 2026-11-19
  - id: s2
    title: "lightning__FlowScreen Target"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/targets-lightning-flow-screen.html
    type: official-docs
    accessed: 2026-11-19
  - id: s3
    title: "Validate User Input for Custom Flow Screen Components"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/use-flow-validate-user-input-for-custom-components.html
    type: official-docs
    accessed: 2026-11-19
  - id: s4
    title: "Runtime Considerations for Flow Screen Components"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/use-flow-runtime-considerations.html
    type: official-docs
    accessed: 2026-11-19
  - id: s5
    title: "Best Practices for Reactivity in Screen Flows"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/use-best-practices-reactivity.html
    type: official-docs
    accessed: 2026-11-19
  - id: s6
    title: "Custom Property Editor JavaScript Interface"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/use-flow-custom-property-editor-interface.html
    type: official-docs
    accessed: 2026-11-19
created: 2026-11-19
---

# Custom Flow Screen Components

## Definition

A **custom flow screen component** is a Lightning web component (LWC) that a developer exposes to Flow Builder so an admin can place it on a screen in a screen flow, next to standard components such as Text or Data Table. It is the main way to give a screen flow UI that the standard component palette can't provide, while the flow itself keeps owning the logic, data and navigation.[^s1][^s2]

## How it works

**Exposure.** In the bundle's `.js-meta.xml`, the component sets `isExposed` to true and lists `lightning__FlowScreen` under `<targets>`. A `<targetConfig targets="lightning__FlowScreen">` block then declares each property the flow can see, and each property's `name` must match a public `@api` property in the JavaScript class.[^s1][^s2] Every `targetConfig` needs at least one `property`, and if the type in the configuration file disagrees with the JavaScript type, the configuration file wins.[^s2]

**Property types and roles.** Supported types are `Boolean`, `Integer`, `String`, `Date` and `DateTime` (ISO 8601), an Apex-defined type written as `apex://Classname`, and an object written as `@salesforce/schema/Objectname`.[^s2] A `propertyType` element lets a component declare a generic type that extends `sObject` or an sObject collection, so the admin picks the concrete object when configuring the screen.[^s2] The `role` attribute restricts a property to `inputOnly` or `outputOnly`; without it the property is both. Other attributes include `required` (default false) and `default`, and a `Double` property with `flowRole="flowRuntimeApiVersion"` receives the flow's runtime API version without appearing in Flow Builder.[^s2]

**Talking back to the flow.** The `lightning/flowSupport` module supplies `FlowAttributeChangeEvent`, which tells the runtime that a property value changed, plus navigation events: `FlowNavigationNextEvent`, `FlowNavigationBackEvent`, `FlowNavigationPauseEvent` and `FlowNavigationFinishEvent`. These events work only in components targeted at `lightning__FlowScreen`.[^s1] A component can declare an `@api availableActions` array and check it, for example for `NEXT`, before asking the runtime to navigate.[^s1]

**Validation.** Adding an `@api validate()` method lets the component check its own input. It returns `{ isValid: true }`, or `isValid: false` with an `errorMessage`. It must be a regular method: Salesforce notes that an arrow-function `validate` isn't recognised for flow screen targets.[^s3]

## Runtime behaviour and gotchas

Salesforce documents several runtime rules that commonly surprise developers.[^s4]

- If the admin sets no default for an input, Flow passes `null` at run time, so the component needs a null handler.[^s4]
- When the component is hidden by conditional visibility, all its outputs are set to `null` as the user leaves the screen.[^s4]
- Every input attribute is also an output attribute by default, unless `role` says otherwise.[^s4][^s2]

The reactivity guidance is stricter still. A component shouldn't assign to its own `@api` properties; it should dispatch a `FlowAttributeChangeEvent` from an event handler, with a value whose type matches the property's Flow data type.[^s5] To react to values pushed in by the flow, use `@api` getter/setter pairs and keep internal state in undecorated or `@track` fields.[^s5] For a derived output, fire its event in both the driving setter and `connectedCallback`, because the component isn't in the DOM when the setter first runs.[^s5] Don't fire attribute-change and navigation events together, which risks race conditions, and don't rely on the runtime reading `@api` values when the user clicks Next or Finish, a fallback kept only for backward compatibility.[^s5]

## Custom property editors

By default Flow Builder renders a generic form for the component's inputs. A `targetConfig` can instead name a **custom property editor**, another LWC, in its `configurationEditor` attribute.[^s2][^s6] Flow Builder passes the editor `inputVariables`, a `builderContext` describing the flow's screens, variables and actions, `genericTypeMappings` and `elementInfo`. The editor reports edits by dispatching a `configuration_editor_input_value_changed` event.[^s6] Its own `validate()` runs when the admin clicks Done and returns key/error pairs; Flow Builder shows only the error count, so the editor must display the messages itself.[^s6]

## When to use it

Build a custom screen component when a screen needs interaction the standard components can't deliver, such as a bespoke picker, a visual summary or a third-party widget, and keep branching in the flow: navigation events belong in handlers for user actions, while screen-skipping logic belongs in flow elements.[^s5][^s1] For logic with no UI, an invocable Apex action is usually the simpler extension point.

## Connections

- **Broader:** a building block of **Screen Flow** and a specialised use of **Lightning Web Components**.[^s1][^s2]
- **Integrates with Flow Builder**, where admins place and configure the component, and is **configured via** an optional custom property editor.[^s6]
- **Depends on Apex-defined types** when a property is typed `apex://…`.[^s2]
- **Related:** Aura components, invocable Apex actions, Lightning Data Service.

## Sources

[^s1]: Salesforce Developers, "Flow Support (lightning/flowSupport)". https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-flow-support.html (accessed 2026-11-19)
[^s2]: Salesforce Developers, "lightning__FlowScreen Target". https://developer.salesforce.com/docs/platform/lwc/guide/targets-lightning-flow-screen.html (accessed 2026-11-19)
[^s3]: Salesforce Developers, "Validate User Input for Custom Flow Screen Components". https://developer.salesforce.com/docs/platform/lwc/guide/use-flow-validate-user-input-for-custom-components.html (accessed 2026-11-19)
[^s4]: Salesforce Developers, "Runtime Considerations for Flow Screen Components". https://developer.salesforce.com/docs/platform/lwc/guide/use-flow-runtime-considerations.html (accessed 2026-11-19)
[^s5]: Salesforce Developers, "Best Practices for Reactivity in Screen Flows". https://developer.salesforce.com/docs/platform/lwc/guide/use-best-practices-reactivity.html (accessed 2026-11-19)
[^s6]: Salesforce Developers, "Custom Property Editor JavaScript Interface". https://developer.salesforce.com/docs/platform/lwc/guide/use-flow-custom-property-editor-interface.html (accessed 2026-11-19)
