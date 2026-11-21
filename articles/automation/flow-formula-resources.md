---
id: kt:flow-formula-resources
type: Feature
title: Flow Formula Resources
aliases: [flow formula resource, formula resource, flow formulas]
domain: automation
summary: >-
  A read-only Flow Builder resource that calculates a value from a formula expression each time the flow
  references it, used in assignments, decisions and entry conditions.
release: "Winter '27"
status: current
broader: [kt:flow-builder]
related: [kt:record-triggered-flow, kt:workflow-rules, kt:custom-labels]
relations:
  - {predicate: contrastsWith, object: kt:formula-fields}
  - {predicate: governedBy, object: kt:flow-limits}
  - {predicate: consumedBy, object: kt:record-triggered-flow}
sources:
  - id: s1
    title: "Calculate Values in Variables and Formulas"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/flow-build-logic/calculate-values-variables-formulas
    type: official-learning
    accessed: 2026-11-21
  - id: s2
    title: "Understanding and Creating Flow Variables"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/flow-basics/learn-about-flow-variables
    type: official-learning
    accessed: 2026-11-21
  - id: s3
    title: "Automate This! — Use Formulas in Record-Triggered Flows with Aleksandra Radovanovic"
    publisher: Salesforce Admins
    url: https://admin.salesforce.com/blog/2022/automate-this-use-formulas-in-record-triggered-flows-with-aleksandra-radovanovic
    type: official-blog
    accessed: 2026-11-21
  - id: s4
    title: "Three Powerful Formula Functions You Can Use in Flow"
    publisher: Salesforce Admins
    url: https://admin.salesforce.com/blog/2022/three-powerful-formula-functions-you-can-use-in-flow
    type: official-blog
    accessed: 2026-11-21
  - id: s5
    title: "Formulas Quick Reference"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.salesforce_formulas_cheatsheet.meta/salesforce_formulas_cheatsheet/
    type: official-docs
    accessed: 2026-11-21
created: 2026-11-21
---

# Flow Formula Resources

A formula resource is one of the resource types you can create in Flow Builder's Toolbox (New Resource → Resource Type: Formula). You give it an API name, an optional description, an output data type and a formula expression, and the flow can then reference it anywhere a value is accepted.[^s1][^s2] Flow formulas behave much like custom formula fields and support most of the same formula functions, but they live inside a single flow rather than on an object.[^s2]

## How it works

A formula resource has no stored value. Flow Builder recalculates it every time an element accesses it, so a formula that reads a variable can return a different result at two points in the same flow if that variable changed in between.[^s2] It is read-only: you cannot assign a new value to a formula mid-flow, which is the main difference from a variable.[^s1][^s3] The usual pattern is to compute a value in a formula and then copy the result into a variable or a record field with an Assignment element, or to reference it in a Decision outcome or entry condition.[^s3]

Setting the right output data type matters. A formula whose result goes into a text field must be of type Text, and Flow cannot concatenate text with dates or numbers directly, so non-text values are wrapped in `TEXT()`; spacing inside string literals has to be written explicitly, or the pieces run together.[^s1] A Boolean formula can be compared with the `$GlobalConstant.True` constant in a Decision outcome.[^s4] Comparing a formula's output to a field of a different type, such as a number result against a text field, produces an error.[^s3] The formula editor offers a Check Syntax button, which is most useful for long, nested expressions.[^s1]

## Useful functions in record-triggered flows

Record-triggered flows can use `ISNEW()`, `ISCHANGED()` and `PRIORVALUE()` in formula resources, the same change-detection functions admins relied on in workflow rules and Process Builder. A Boolean formula built from them can drive a Decision element or serve as the Start element's entry condition.[^s4] Since Summer '22, entry conditions can also be written directly as a formula in the same builder used for formula fields; the expression must return true or false and can traverse relationships and use merge fields.[^s3] Following general formula guidance, prefer `ISBLANK` over `ISNULL` and `BLANKVALUE` over `NULLVALUE` in new formulas.[^s5]

A common maintainability tip is to reference custom labels through the `$Label` global variable inside a formula instead of hard-coding record IDs or email addresses, so the same flow works after deployment to another org.[^s3]

## Limits and gotchas

Flow formulas have a limited calculation time and a limited number of characters, and Long Text Area fields cannot be used in them because they can exceed the calculation limit.[^s1] A Salesforce Admins article puts the size limit at 3,900 characters per flow formula.[^s3] Typographic (curly) quotation marks pasted from documents break the syntax check and must be replaced with straight quotes.[^s4] Because the value is recomputed on every reference, its result can change between references if its inputs change, so copy it into a variable when you need a fixed snapshot.[^s2]

## When to use it (and when not)

Trailhead advises reaching for a formula only when the logic genuinely needs one; simple arithmetic or text appends can be done with an Assignment element's Add operator, which adds numbers and currency or shifts dates by days.[^s1] Use a formula when the value depends on several inputs, needs functions such as `IF` or `TEXT`, or should collapse a Decision element into a single calculated assignment.[^s3] Use a constant when the value never changes, and a text template when you need rich text with merge fields.[^s2]

## Connections

Formula resources are part of **Flow Builder** and are especially common in **record-triggered flows**, where they bring the change-detection functions admins used in **workflow rules** into Flow.[^s4] They contrast with object-level **formula fields**: both share the formula language, but a flow formula exists only for one flow and is recalculated on each reference.[^s2][^s5] They can read **custom labels** through `$Label`, and are subject to the size and calculation constraints covered in **flow limits**.[^s1][^s3]

## Sources
[^s1]: Trailhead, "Calculate Values in Variables and Formulas". https://trailhead.salesforce.com/content/learn/modules/flow-build-logic/calculate-values-variables-formulas (accessed 2026-11-21)
[^s2]: Trailhead, "Understanding and Creating Flow Variables". https://trailhead.salesforce.com/content/learn/modules/flow-basics/learn-about-flow-variables (accessed 2026-11-21)
[^s3]: Salesforce Admins, "Automate This! — Use Formulas in Record-Triggered Flows with Aleksandra Radovanovic". https://admin.salesforce.com/blog/2022/automate-this-use-formulas-in-record-triggered-flows-with-aleksandra-radovanovic (accessed 2026-11-21)
[^s4]: Salesforce Admins, "Three Powerful Formula Functions You Can Use in Flow". https://admin.salesforce.com/blog/2022/three-powerful-formula-functions-you-can-use-in-flow (accessed 2026-11-21)
[^s5]: Salesforce Developers, "Formulas Quick Reference". https://developer.salesforce.com/docs/atlas.en-us.salesforce_formulas_cheatsheet.meta/salesforce_formulas_cheatsheet/ (accessed 2026-11-21)
