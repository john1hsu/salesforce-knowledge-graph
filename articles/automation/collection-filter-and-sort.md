---
id: kt:collection-filter-and-sort
type: Feature
title: Collection Filter and Collection Sort Elements
aliases: [Collection Filter element, Collection Sort element, Flow collection processor, FlowCollectionProcessor, Collection Filter and Sort]
domain: automation
summary: >-
  Two Flow Builder logic elements that work on a collection variable already in memory: Collection Filter copies the
  items that meet conditions or a formula into a new collection, and Collection Sort reorders (and can truncate) the
  collection in place, without a new query or a Loop.
release: "Winter '27"
status: current
broader: [kt:flow-builder]
related: [kt:transform-element, kt:flow-bulkification, kt:screen-flow, kt:einstein-next-best-action]
relations:
  - {predicate: alternativeTo, object: kt:flow-loop-element}
  - {predicate: alternativeTo, object: kt:get-records-element}
  - {predicate: configuredVia, object: kt:metadata-api}
sources:
  - id: s1
    title: "Organize Data in a Collection Variable (Multirecord Elements and Transforms in Flows)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/multirecord-elements-and-transforms-in-flows/organize-data-in-a-collection-variable
    type: official-learning
    accessed: 2026-11-16
  - id: s2
    title: "Flow (Metadata API Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/api-metadata/references/meta-types/metadata-flow.html
    type: official-docs
    accessed: 2026-11-16
  - id: s3
    title: "Learn MOAR in Spring '22 with Flow Enhancements"
    publisher: Salesforce Admins
    url: https://admin.salesforce.com/blog/2022/learn-moar-in-spring-22-with-flow-enhancements
    type: official-blog
    accessed: 2026-11-16
  - id: s4
    title: "How to Use the Collection Sort Element"
    publisher: Salesforce Time
    url: https://salesforcetime.com/2023/08/15/how-to-use-the-collection-sort-element/
    type: community
    accessed: 2026-11-16
created: 2026-11-16
---

# Collection Filter and Collection Sort Elements

**Collection Filter** and **Collection Sort** are logic elements in Flow Builder that operate on a collection variable the flow already holds, such as the output of a Get Records element. Filter removes the items that fail its criteria, and Sort reorders the items and can optionally keep only the first N. Both let a flow reshape a list without issuing another query or writing a Loop with Assignment elements.[^s1] Collection Filter arrived in Spring '22, where Salesforce presented it as a way to narrow an existing record collection by record criteria or by a formula.[^s3]

## How it works

In metadata, both elements are stored as a `FlowCollectionProcessor` node. Its required `collectionProcessorType` is `SortCollectionProcessor` (API 50.0 and later) or `FilterCollectionProcessor` (API 53.0 and later), and its required `collectionReference` names the input collection.[^s2] A third processor type, `RecommendationMapCollectionProcessor` (API 53.0 and later), maps a collection to recommendations.[^s2]

**Collection Filter** takes an input collection and a condition requirement, then evaluates each item against field/operator/value conditions.[^s1] In metadata, the condition logic can be AND, OR, custom logic such as `(1 AND (2 OR 3))`, or a formula; with a formula, the items for which it returns true go into the output.[^s2] The element does not change its input. It produces a new collection, and later elements must reference that output to see the filtered items.[^s1]

**Collection Sort** names a collection variable, one or more sort fields and a direction, and a choice between keeping all items or setting a maximum number to keep.[^s1] Each sort option has a required sort order (`Asc` or `Desc`) and a flag that puts empty strings and nulls first; the flag defaults to false, so they sort last.[^s2] The sort field is required for record and Apex-defined collections and is not supported for primitive collections such as lists of strings or integers.[^s2] When a limit is set together with sort settings, the items are sorted before the limit is applied, and the limit has no default.[^s2] Practitioners report a maximum of three sort fields, applied in priority order.[^s4]

## Limits and gotchas

- **Sort is destructive.** Collection Sort does not create a new collection; it modifies the one you select, so every later reference sees the sorted, truncated list.[^s1]
- **Capture what you need first.** If the original order or count matters, store it before sorting, because the source variable is overwritten.[^s4]
- **Filter output is separate.** Chaining elements means pointing at the Filter's output variable, not the original collection.[^s1]
- **A limit of one still returns a collection.** To use a single record afterwards you still need to extract it from the one-item list.[^s4]
- **A limit is a ceiling.** Setting a limit larger than the collection simply keeps every item.[^s4]

## When to use it (and when not)

If the criteria are known when the data is fetched, do the filtering, sorting and limiting in Get Records, which Salesforce describes as the more efficient option. Use these elements when the criteria only become known later in the flow, for example from a Decision or from screen input.[^s1] They also replace the classic pattern of looping over a collection and building a second list with Assignment elements, since they narrow an existing collection without another query or a loop.[^s3] Collection Sort is also the way to order a collection by more than one field, or to sort a list that did not come from Get Records.[^s4]

## Connections

Both elements are part of **Flow Builder** and are stored through the **Metadata API** as `FlowCollectionProcessor` nodes.[^s2] They are alternatives to a hand-built **Loop element** and complements to **Get Records**, which should do the work when the criteria are known at query time.[^s1] The **Transform element** covers a neighbouring job (reshaping, aggregating or joining collections) in the same Trailhead module, and together they support **flow bulkification** by working on whole collections. They are often used in **screen flows**, where user input decides how to filter or rank records.[^s1] The recommendation-mapping processor type of the same node links them to recommendation work such as **Einstein Next Best Action**.[^s2]

## Sources

[^s1]: Trailhead, "Organize Data in a Collection Variable (Multirecord Elements and Transforms in Flows)". https://trailhead.salesforce.com/content/learn/modules/multirecord-elements-and-transforms-in-flows/organize-data-in-a-collection-variable (accessed 2026-11-16)
[^s2]: Salesforce, "Flow (Metadata API Developer Guide)". https://developer.salesforce.com/docs/platform/api-metadata/references/meta-types/metadata-flow.html (accessed 2026-11-16)
[^s3]: Salesforce Admins, "Learn MOAR in Spring '22 with Flow Enhancements". https://admin.salesforce.com/blog/2022/learn-moar-in-spring-22-with-flow-enhancements (accessed 2026-11-16)
[^s4]: Salesforce Time, "How to Use the Collection Sort Element". https://salesforcetime.com/2023/08/15/how-to-use-the-collection-sort-element/ (accessed 2026-11-16)
