---
id: kt:flow-choice-resources
type: Feature
title: Flow Choice Resources
aliases: [flow choice resource, choice set, record choice set, picklist choice set, collection choice set]
domain: automation
summary: >-
  The Flow Builder resources (Choice, Record Choice Set, Picklist Choice Set and Collection Choice Set) that
  supply the selectable options shown by picklist, radio button, checkbox group and multi-select screen components.
release: "Winter '27"
status: current
broader: [kt:flow-builder]
related: [kt:custom-flow-screen-components, kt:data-table-screen-component, kt:flow-formula-resources, kt:picklist-value-sets]
relations:
  - {predicate: consumedBy, object: kt:screen-flow}
  - {predicate: dependsOn, object: kt:get-records-element}
  - {predicate: contrastsWith, object: kt:flow-loop-element}
sources:
  - id: s1
    title: "Give Users a Choice (Screen Flows module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/screen-flows/give-users-a-choice
    type: official-learning
    accessed: 2026-11-23
  - id: s2
    title: "Picklist Choice Set Resource"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.flow_ref_resources_picklistchoice.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-23
  - id: s3
    title: "Picklist Screen Input Component"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=flow_ref_elements_screencmp_picklist.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-23
  - id: s4
    title: "Create a Flow with a Multi-Select Picklist"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/loop-manually-through-multiple-choices-in-flows/create-a-flow-with-a-multi-select-picklist
    type: official-learning
    accessed: 2026-11-23
  - id: s5
    title: "Screen Flow Choice Field Values Do Not Update Picklist or Text Fields"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000385593&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-23
created: 2026-11-23
---

# Flow Choice Resources

Choice resources are the Flow Builder resources that feed options into a screen flow's multiple-choice components. Most choice-based screen components need at least one of them, and the options they produce appear in single-select Picklist and Radio Buttons components or multi-select Checkbox Group and Multi-Select Picklist components.[^s1][^s3] There are four kinds: a manual **Choice**, a **Record Choice Set**, a **Picklist Choice Set** and a **Collection Choice Set**.[^s1]

## The four resource types

A **Choice** is a single, hand-entered option such as Yes or No, or High, Medium and Low. Builders add one per option, and Flow Builder offers an inline shortcut that creates a manual choice straight from the component's Choice field without opening the New Resource window.[^s1] Each manual choice needs a Stored Value: if it is left empty, the choice passes null to any record field it is mapped to in a Create or Update Records element, a known support issue whose fix is to enter the literal stored value and reactivate the flow.[^s5]

A **Record Choice Set** queries an object with optional filter conditions and turns each matching record into an option. The builder sets a Choice Label (the text users see, often Name) and a Choice Value (what the component stores, often Id), and can sort results and preselect a default, for example the current contact passed in through an input variable.[^s1][^s4] Trailhead warns that it only returns the first 200 records, so large objects need a filter.[^s1]

A **Picklist Choice Set** reads the values of an existing picklist or multi-select picklist field on a chosen object, so new field values appear in the flow without editing it.[^s2] The object and data type can't be changed after saving, and options are sorted using the running user's translated value.[^s2]

A **Collection Choice Set** builds options from a record collection the flow already holds, such as contacts returned by an earlier Get Records element.[^s1]

## How selections are stored

The component stores the Choice Value of the selected option, so a record choice set using Id hands later elements a record ID.[^s1] Multi-select components return a single text string of values separated by semicolons rather than a collection; Trailhead calls this unstructured data, because elements such as Get Records only accept a true collection.[^s4] Turning on Let Users Select Multiple Options on a choice component switches its data type to Text and removes any non-text choices.[^s3] The component's data type also restricts which choices fit, so a Number component can't use a Text choice.[^s3]

## Limits and gotchas

- Picklist choice sets can't be filtered, so all values show even where record types narrow the picklist on layouts.[^s2]
- A picklist choice set always shows the value label and stores the API value; neither can be customized.[^s2]
- Stored values come from the org's default language, labels from the running user's language.[^s2]
- Some fields that look like picklists, such as Event Subject, aren't true picklists and can't be used; use a record choice set or manual choices instead.[^s2]
- Knowledge article picklists aren't supported in a picklist choice set.[^s2]
- Dynamic choice sets (record or collection) must produce unique values, or selections can be set incorrectly.[^s3]
- From Flow Runtime API version 52, picklists start with a --None-- option that counts as null and blocks a required field.[^s3]
- Checkbox Group, Choice Lookup and Multi-Select Picklist selections can't be fed to Loop or Transform elements directly.[^s4]

## When to use which

Use a picklist choice set when the options already exist as a field and should stay in sync with it; use a record choice set when users pick records, such as contacts on an account, and the list can be filtered to a manageable size.[^s1][^s2] Use a collection choice set when the records were already retrieved or computed earlier in the flow, and manual choices for short, fixed lists that exist only in the flow.[^s1] Plan for multi-select results up front: they arrive as one delimited string, so any per-record processing needs extra conversion steps, and Trailhead advises reserving manual loops for when they are truly needed.[^s4]

## Connections

Choice resources are a resource type in **Flow Builder** and are consumed by **screen flows**, alongside the standard and **custom flow screen components** that render them.[^s1][^s3] A collection choice set depends on records fetched with the **Get Records element**, and turning a multi-select result back into records also ends in a Get Records query.[^s1][^s4] Because the **Loop element** can't iterate a multi-select result, Trailhead teaches a manual loop of Decision and Assignment elements, often with **flow formula resources** to split the string.[^s4] Picklist choice sets reuse the values of an existing picklist field, which may itself draw on shared **picklist value sets**; the **data table screen component** is a related screen component for presenting records.[^s2][^s3]

## Sources
[^s1]: Trailhead, "Give Users a Choice (Screen Flows module)". https://trailhead.salesforce.com/content/learn/modules/screen-flows/give-users-a-choice (accessed 2026-11-23)
[^s2]: Salesforce Help, "Picklist Choice Set Resource". https://help.salesforce.com/s/articleView?id=sf.flow_ref_resources_picklistchoice.htm&language=en_US&type=5 (accessed 2026-11-23)
[^s3]: Salesforce Help, "Picklist Screen Input Component". https://help.salesforce.com/s/articleView?id=flow_ref_elements_screencmp_picklist.htm&language=en_US&type=5 (accessed 2026-11-23)
[^s4]: Trailhead, "Create a Flow with a Multi-Select Picklist". https://trailhead.salesforce.com/content/learn/modules/loop-manually-through-multiple-choices-in-flows/create-a-flow-with-a-multi-select-picklist (accessed 2026-11-23)
[^s5]: Salesforce Help, "Screen Flow Choice Field Values Do Not Update Picklist or Text Fields". https://help.salesforce.com/s/articleView?id=000385593&language=en_US&type=1 (accessed 2026-11-23)
