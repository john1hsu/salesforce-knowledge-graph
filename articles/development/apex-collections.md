---
id: kt:apex-collections
type: Concept
title: Apex Collections
aliases: [Apex List Set and Map, Apex collection types, Apex lists sets and maps]
domain: development
summary: >-
  The three built-in collection types of the Apex language (List, Set and Map), which hold primitives, sObjects,
  user-defined types or other collections and are the basic tool for bulk-safe processing of records.
release: "Winter '27"
status: current
broader: [kt:apex]
related: [kt:bulkification, kt:soql, kt:apex-json-serialization, kt:apex-triggers, kt:apex-defined-types]
relations:
  - {predicate: governedBy, object: kt:governor-limits}
sources:
  - id: s1
    title: "Apex Developer Guide: Collections (Winter '27, API version 68.0)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/langCon_apex_collections.htm
    type: official-docs
    accessed: 2026-11-24
  - id: s2
    title: "Apex Developer Guide: Lists"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/langCon_apex_collections_lists.htm
    type: official-docs
    accessed: 2026-11-24
  - id: s3
    title: "Apex Developer Guide: Sets"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/langCon_apex_collections_sets.htm
    type: official-docs
    accessed: 2026-11-24
  - id: s4
    title: "Apex Developer Guide: Maps"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/apexcode/langCon_apex_collections_maps.htm
    type: official-docs
    accessed: 2026-11-24
  - id: s5
    title: "Trailhead: Apex Basics for Admins, Use Collections"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/apex-basics-for-admins/use-collections
    type: official-learning
    accessed: 2026-11-24
  - id: s6
    title: "Mastering Apex Collections (Philippe Ozil, 2021)"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2021/10/mastering-apex-collections
    type: official-blog
    accessed: 2026-11-24
created: 2026-11-24
---

# Apex Collections

Apex has exactly three collection types: lists, sets and maps.[^s1] Their elements can be primitives, sObjects, user-defined classes, built-in Apex types, or other collections.[^s1] Almost every piece of production Apex leans on them, because the way to stay inside governor limits is to query, transform and write records in groups rather than one at a time.

## The three types

A **List** is an ordered collection whose elements are reached by position, and the first element is always at index 0.[^s2] Duplicates are allowed. Apex also accepts array syntax, so `String[]` and `List<String>` are two ways of writing the same type.[^s2] Assigning through square brackets does not grow a list; `add()` appends, and `add(index, value)` inserts at a position.[^s2][^s5] Trailhead's admin-level unit teaches exactly this: declaring an empty list, declaring one with a fixed size, initialising it with values in braces, and the two ways of adding items.[^s5]

A **Set** is unordered and holds no duplicates.[^s3] It has no index, so you can only iterate over it or test membership. Although Apex stores sets as hash structures internally, the iteration order is deterministic between runs of the same code, and you declare `Set<T>` with no HashSet or TreeSet variants.[^s3]

A **Map** stores key–value pairs in which each key is unique and maps to one value.[^s4] Putting an entry under a key that already exists overwrites the old value, and a key may be null.[^s4] Iteration order is deterministic too, but the guide advises reading entries by key rather than relying on that order.[^s4]

## Equality, keys and sorting

Uniqueness in sets and map keys follows each type's equality rules. String map keys are case-sensitive, so keys that differ only in case are separate entries for `put`, `get`, `containsKey` and `remove`.[^s4] For a user-defined class used as a key, uniqueness comes from that class's own `equals` and `hashCode` methods; for sObjects and other non-primitive keys it comes from comparing field values.[^s4] Changing a field on an sObject after it is used as a key therefore means the map no longer finds it.[^s4]

Salesforce's developer advocates explain the mechanics: sets and map keys check `hashCode` first and fall back to `equals`, while `List.contains` uses `equals` only.[^s6] Converting a list into a set removes duplicates but loses the original order.[^s6] `List.sort()` sorts primitives in natural order, and other element types must implement `Comparable` or the call throws a `System.ListException`.[^s6] sObjects have a built-in sort order, so sorting records by a custom field typically uses a wrapper class that implements `Comparable`.[^s6]

## Limits and gotchas

- Size: the guide sets no cap on how many items a collection holds; the binding constraint is the transaction's heap size limit.[^s1]
- Nesting: lists, sets and maps can each nest collections up to seven levels deep, eight levels in total.[^s2][^s3][^s4]
- Changing a collection while iterating it fails: adding to a set inside its own loop throws `System.FinalException`.[^s6]
- Mutable sObject keys break map lookups once a field value changes after insertion.[^s4]
- JSON serialization of a map works only for keys of types such as Boolean, Date, Datetime, Decimal, Id, Integer, Long, String and Time.[^s4]

## When to use which

Use a list when order or duplicates matter, such as records to insert in sequence or query results. Use a set to gather unique Ids for a filter such as `WHERE Id IN :ids`, or to de-duplicate values.[^s3][^s6] Use a map to look up a related record by key in constant time instead of nesting loops, the classic shape of a bulk-safe trigger.[^s4][^s6]

## Connections

Collections are a core part of `kt:apex`, which is why this node sits under it.[^s1] They put the `kt:bulkification` pattern into practice in `kt:apex-triggers`, where sets of Ids feed `kt:soql` bind variables and maps join the results back to the trigger records.[^s6] Because nothing caps their size except heap, they are governed in practice by `kt:governor-limits`, in particular the Apex heap size limit.[^s1] Map key types also decide whether a structure can be handled by `kt:apex-json-serialization`.[^s4] Wrapper classes and `kt:apex-defined-types` are common element types when records need custom sorting or extra state.[^s6]

## Sources
[^s1]: Salesforce Developers, "Apex Developer Guide: Collections" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/langCon_apex_collections.htm (accessed 2026-11-24)
[^s2]: Salesforce Developers, "Apex Developer Guide: Lists". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/langCon_apex_collections_lists.htm (accessed 2026-11-24)
[^s3]: Salesforce Developers, "Apex Developer Guide: Sets". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/pages/langCon_apex_collections_sets.htm (accessed 2026-11-24)
[^s4]: Salesforce Developers, "Apex Developer Guide: Maps". https://developer.salesforce.com/docs/atlas.en-us.264.0.apexcode.meta/apexcode/langCon_apex_collections_maps.htm (accessed 2026-11-24)
[^s5]: Trailhead, "Apex Basics for Admins: Use Collections". https://trailhead.salesforce.com/content/learn/modules/apex-basics-for-admins/use-collections (accessed 2026-11-24)
[^s6]: Philippe Ozil, "Mastering Apex Collections", Salesforce Developers Blog (2021-10-25). https://developer.salesforce.com/blogs/2021/10/mastering-apex-collections (accessed 2026-11-24)
