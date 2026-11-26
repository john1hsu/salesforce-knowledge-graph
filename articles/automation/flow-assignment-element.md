---
id: kt:flow-assignment-element
type: Feature
title: Assignment Element
aliases: [Flow Assignment element, Assignment element in Flow, Flow Builder Assignment, assignment operators in Flow]
domain: automation
summary: >-
  A Flow Builder element that sets or changes the values of flow variables in memory, one ordered row at a time, using
  operators such as Equals, Add and Subtract for single values and Add, Remove and related operators for collections;
  it never writes to the database by itself.
release: "Winter '27"
status: current
broader: [kt:flow-builder]
related: [kt:flow-loop-element, kt:flow-decision-element, kt:get-records-element, kt:flow-formula-resources, kt:flow-bulkification]
relations:
  - {predicate: alternativeTo, object: kt:collection-filter-and-sort}
sources:
  - id: s1
    title: "Set and Change Variable Values (Improve Process Automation with Flow Builder)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/flow-build-logic/set-change-variable-values
    type: official-learning
    accessed: 2026-11-26
  - id: s2
    title: "Calculate Values in Variables and Formulas"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/flow-build-logic/calculate-values-variables-formulas
    type: official-learning
    accessed: 2026-11-26
  - id: s3
    title: "Assign First Selection to a Text Collection"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/loop-manually-through-multiple-choices-in-flows/assign-first-selection-to-a-text-collection
    type: official-learning
    accessed: 2026-11-26
  - id: s4
    title: "Assign Selections to a Text Variable"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/loop-manually-through-multiple-choices-in-flows/assign-selections-to-a-text-variable
    type: official-learning
    accessed: 2026-11-26
  - id: s5
    title: "Automate This! — How to Use Loops in Flow"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2022/automate-this-how-to-use-loops-in-flow
    type: official-blog
    accessed: 2026-11-26
  - id: s6
    title: "Collection Assignment Operators in Flow"
    publisher: Salesforce Time
    url: https://salesforcetime.com/2022/10/07/collection-assignment-operators-in-flow/
    type: community
    accessed: 2026-11-26
created: 2026-11-26
---

# Assignment Element

The **Assignment** element is how a flow puts a value into a variable or changes the value it already holds.[^s1] It is Flow Builder's equivalent of an assignment statement in code: you pick a variable (or a field on a record variable), choose an operator that controls how the variable is updated, and supply a value.[^s1] The value can be typed text, an existing resource such as another variable or a formula, or a mix of the two, so a row like `The color is {!colorFormula}` produces a combined string.[^s1]

## How it works

One Assignment element can hold many rows, and Salesforce runs them in the order they are listed.[^s1] Order matters: a later row can read a value that an earlier row in the same element just set. Trailhead's address example uses one Assignment with five rows to copy City, Country, Zip/Postal Code, State/Province and Street from the billing address to the shipping fields of a record variable.[^s1]

The operators on offer depend on the variable's data type:

- **Equals** replaces the variable's current value with the new one, and it works for every type.[^s1]
- **Add** on a text variable appends text to the end; on a number or currency variable it does real arithmetic (4 plus 2 gives 6, not 42).[^s2]
- **Subtract** lowers number and currency values, and Add or Subtract on a date moves it forward or back by a number of days.[^s2]

Collection variables get a wider set. Add appends an item (or a whole collection of the same type) to the end, and **Add At Start** puts it at the beginning.[^s6] **Remove First**, **Remove Before First** and **Remove After First** find the first matching item and remove it, everything before it, or everything after it.[^s6] **Remove All** removes every instance of the value, **Remove Uncommon** keeps only items that also appear in a second collection, and **Remove Position** removes the item at a numbered position.[^s6] Text variables, by contrast, offer only Equals and Add.[^s6]

## Limits and gotchas

The most common surprise is that an Assignment changes values only in the flow's memory. Setting fields on a record variable doesn't save them to the record; you still need an Update Records element to write the change.[^s1] The Value field accepts a single data source, so when a value has to be built from several inputs, assign them to an intermediate variable or a formula first.[^s1]

Type mixing is restricted. You can't combine a text variable with non-text resources such as dates or number fields directly; the fix is a formula that converts them with `TEXT()`, which you then assign.[^s2] Long text fields can't be used in flow formulas, and formulas have limited calculation time and character counts.[^s2] Formulas also don't store their results, so a manual loop that recalculates a formula on each pass needs an Assignment inside the loop to keep the value.[^s3]

Remove Position fails at run time if the position you pass is larger than the number of items in the collection, so guard it with a Decision or a count first.[^s6]

## When to use it (and when not)

Inside loops, Assignment is the piece that makes bulk updates possible. The Salesforce Admins pattern for updating records in a loop uses five elements in a fixed order: Get Records, Loop, an Assignment that drafts the field changes on the current item, a second Assignment that adds that item to a new collection, and one Update Records after the loop.[^s5] Because nothing is written until the end, the flow changes data once instead of once per record, which conserves shared resources and stays inside governor limits.[^s5]

Assignment also handles string building. When a multi-select screen returns unstructured selections that can't go straight into a collection, Trailhead uses Equals to store the selection and then Add with a semicolon as a delimiter so formulas can split the string later.[^s4] A later step in the same project uses Equals to capture one parsed value and Add to push it into a text collection variable.[^s3]

For filtering or ordering a whole collection by criteria, the dedicated Collection Filter and Collection Sort elements are usually clearer than chains of Remove operators, which match only exact items or positions.[^s6]

## Connections

Assignment is a core logic element of **Flow Builder**. It pairs most often with the **Loop** element, where it drafts per-item changes and collects records for a single write, the heart of **flow bulkification**.[^s5] **Get Records** supplies the collections it changes, and **Decision** elements commonly branch on the values it sets.[^s4][^s5] It stores the outputs of **flow formula resources**, which can't persist values themselves.[^s3] For collection clean-up it is an **alternative to** the **Collection Filter and Collection Sort** elements.[^s6]

## Sources
[^s1]: Trailhead, "Set and Change Variable Values (Improve Process Automation with Flow Builder)". https://trailhead.salesforce.com/content/learn/modules/flow-build-logic/set-change-variable-values (accessed 2026-11-26)
[^s2]: Trailhead, "Calculate Values in Variables and Formulas". https://trailhead.salesforce.com/content/learn/modules/flow-build-logic/calculate-values-variables-formulas (accessed 2026-11-26)
[^s3]: Trailhead, "Assign First Selection to a Text Collection". https://trailhead.salesforce.com/content/learn/modules/loop-manually-through-multiple-choices-in-flows/assign-first-selection-to-a-text-collection (accessed 2026-11-26)
[^s4]: Trailhead, "Assign Selections to a Text Variable". https://trailhead.salesforce.com/content/learn/modules/loop-manually-through-multiple-choices-in-flows/assign-selections-to-a-text-variable (accessed 2026-11-26)
[^s5]: Salesforce Admins Blog, "Automate This! — How to Use Loops in Flow". https://admin.salesforce.com/blog/2022/automate-this-how-to-use-loops-in-flow (accessed 2026-11-26)
[^s6]: Salesforce Time, "Collection Assignment Operators in Flow". https://salesforcetime.com/2022/10/07/collection-assignment-operators-in-flow/ (accessed 2026-11-26)
