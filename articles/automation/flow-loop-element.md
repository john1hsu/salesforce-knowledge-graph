---
id: kt:flow-loop-element
type: Feature
title: Loop Element
aliases: [Flow Loop element, Loop element in Flow, Flow Builder Loop, loops in Flow Builder]
domain: automation
summary: >-
  A Flow Builder element that walks through a collection variable one item at a time, running the elements on its
  For Each path for every item and then following its After Last path; the standard way to apply per-record logic in a
  flow when a Transform element can't do the job.
release: "Winter '27"
status: current
broader: [kt:flow-builder]
related: [kt:flow-bulkification, kt:record-triggered-flow, kt:screen-flow, kt:autolaunched-flow, kt:flow-limits]
relations:
  - {predicate: alternativeTo, object: kt:transform-element}
  - {predicate: alternativeTo, object: kt:collection-filter-and-sort}
  - {predicate: governedBy, object: kt:governor-limits}
sources:
  - id: s1
    title: "Know When to Loop (Loops in Flow Builder)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/loops-in-flow-builder/know-when-to-loop
    type: official-learning
    accessed: 2026-11-17
  - id: s2
    title: "Build a Loop (Loops in Flow Builder)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/fr/content/learn/modules/loops-in-flow-builder/build-a-loop
    type: official-learning
    accessed: 2026-11-17
  - id: s3
    title: "Avoid Flow Limits (Flow Implementation 1)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/flow-implementation-1/avoid-flow-limits
    type: official-learning
    accessed: 2026-11-17
  - id: s4
    title: "Automate This! — Use Loops in Record-Triggered Flows with Sarah Pilzer"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2022/automate-this-use-loops-in-record-triggered-flows-with-sarah-pilzer
    type: official-blog
    accessed: 2026-11-17
created: 2026-11-17
---

# Loop Element

The **Loop** element is Flow Builder's built-in way to iterate. It takes a single setting, a collection variable, and sends each item in that collection, one at a time and in order, through the elements connected to it, which forms a circular path in the flow.[^s1] Most loops run over record collections returned by a Get Records element, but a loop can also walk a collection of single values such as text or numbers.[^s1][^s2]

## How it works

A loop has two outgoing paths. The **For Each** path holds the elements that run once per item, and the **After Last** path is the route the flow takes when every item has been processed.[^s1] On each pass the element places the next item in a special **Current Item from Loop** variable, runs the For Each path, then returns to the Loop element and repeats until the collection is exhausted.[^s1] Inside the For Each path you can reference the current item's fields in Decisions, actions such as Lock Record or Post to Chatter, Assignments and text templates.[^s2]

The current item is overwritten on every pass, so a change you make to it is lost unless you keep a copy.[^s2][^s4] The standard pattern is an **Assignment** element inside the loop that first sets the field on the current item and then uses the Add operator to append that item to a separate record collection variable; one Assignment can do both steps in order.[^s2] Adding a record to a collection does not itself use a DML statement.[^s4]

After the loop finishes, a single **Update Records** (or Create or Delete Records) element on the After Last path saves the whole collection in one operation.[^s2][^s4] A Salesforce Admins example applies this to a record-triggered flow: when one household member's campaign status changes, the flow gets the other members, loops over them to set the new status, collects them, and updates them once after the loop.[^s4]

## Limits and gotchas

Flows run inside Apex transaction limits. Trailhead lists 100 SOQL queries, 150 DML statements, 50,000 records retrieved by SOQL, 10,000 records changed by DML and 10 seconds of CPU time per transaction.[^s3] Each Get Records element costs one query and each Create, Update or Delete Records element costs one DML statement, so a data element inside a loop spends one of each per iteration.[^s3]

- Don't put Get, Create, Update or Delete Records elements inside a loop; query before the loop and write after it.[^s2][^s3]
- Avoid nested loops: element executions multiply, so an element inside two 5-item loops runs 25 times, and with 500 records it runs 2,500 times.[^s1]
- Loops add CPU time, and they are slower than a Transform element, especially on large collections.[^s1]
- A flow started by other automation shares that automation's transaction and therefore its limits.[^s3]
- Screen and Wait elements end the current transaction and start a new one, which resets the count.[^s3]

## When to use it (and when not)

Trailhead's guidance is a ranked order: use a **Transform** element if it can do the job, use a Loop only when Transform can't, and build a **manual loop** (a Decision that routes back to an earlier element) only when neither works.[^s1] Transform is the fastest option and much less likely to hit query and CPU limits, but it can't contain other elements, can't traverse relationships in the source data, and doesn't work with repeaters or choice-set screen components.[^s1] The Loop element can run decisions, actions and any other element that doesn't accept a collection, and it is compatible with every element and screen component.[^s1]

Manual loops are the riskiest choice. They lack the Loop element's built-in optimizations, are the most likely to hit the CPU limit, and can spin forever if unexpected data or user behaviour means the exit path is never taken.[^s1] If the data isn't in a collection yet, Trailhead recommends getting it into one first so a Loop or Transform can process it.[^s1] Placing a Transform inside a loop is acceptable because Transforms are highly optimized.[^s1]

## Connections

The Loop element is a building block of **Flow Builder** and appears in every flow type that processes collections, including **record-triggered**, **screen** and **autolaunched** flows.[^s2][^s4] It is an **alternative to** the **Transform** element, which Salesforce prefers when it fits, and to the **Collection Filter and Collection Sort** elements, which handle filtering and ordering without iterating by hand.[^s1] Because every query and DML element inside it is multiplied by the collection size, it is **governed by** Salesforce's **governor limits**, and it sits at the centre of the **flow bulkification** practice of collecting changes and writing them once.[^s3][^s4] Flow-specific transaction limits are tracked in the **flow limits** node.

## Sources
[^s1]: Trailhead, "Know When to Loop (Loops in Flow Builder)". https://trailhead.salesforce.com/content/learn/modules/loops-in-flow-builder/know-when-to-loop (accessed 2026-11-17)
[^s2]: Trailhead, "Build a Loop (Loops in Flow Builder)". https://trailhead.salesforce.com/fr/content/learn/modules/loops-in-flow-builder/build-a-loop (accessed 2026-11-17)
[^s3]: Trailhead, "Avoid Flow Limits (Flow Implementation 1)". https://trailhead.salesforce.com/content/learn/modules/flow-implementation-1/avoid-flow-limits (accessed 2026-11-17)
[^s4]: Salesforce Admins Blog, "Automate This! — Use Loops in Record-Triggered Flows with Sarah Pilzer". https://admin.salesforce.com/blog/2022/automate-this-use-loops-in-record-triggered-flows-with-sarah-pilzer (accessed 2026-11-17)
