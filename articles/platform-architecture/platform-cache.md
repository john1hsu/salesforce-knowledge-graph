---
id: kt:platform-cache
type: Feature
title: Platform Cache
aliases: [Salesforce Platform Cache, Org Cache, Session Cache, Cache.Org, Cache.Session, platform cache partitions]
domain: platform-architecture
summary: >-
  An in-memory, partitioned cache on the Salesforce Platform that Apex and Visualforce use to keep reusable data
  (org-wide or per user session) close at hand, cutting repeated queries, callouts and computation; entries can be
  evicted at any time, so every read must tolerate a miss.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:governor-limits, kt:soql, kt:apex-callouts, kt:custom-metadata-types, kt:custom-settings, kt:second-generation-managed-packages]
relations:
  - {predicate: configuredVia, object: kt:platform-cache-partitions}
  - {predicate: consumedBy, object: kt:apex}
sources:
  - id: s1
    title: "Platform Cache Features (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/pages/apex_platform_cache_features.htm
    type: official-docs
    accessed: 2026-11-08
  - id: s2
    title: "Platform Cache Limits (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_platform_cache_limits.htm
    type: official-docs
    accessed: 2026-11-08
  - id: s3
    title: "Platform Cache Best Practices (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_platform_cache_best_practices.htm
    type: official-docs
    accessed: 2026-11-08
  - id: s4
    title: "Platform Cache Basics: Get Started with Platform Cache"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/platform_cache/platform_cache_get_started
    type: official-learning
    accessed: 2026-11-08
  - id: s5
    title: "Platform Cache Basics: Use Platform Cache"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/modules/platform_cache/units/platform_cache_use
    type: official-learning
    accessed: 2026-11-08
  - id: s6
    title: "Set Up a Platform Cache Partition with Provider Free Capacity"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg1-dev/guide/data-platform-cache-setup-provider-capacity.html
    type: official-docs
    accessed: 2026-11-08
created: 2026-11-08
---

# Platform Cache

Platform Cache is a memory layer on the Salesforce Platform where Apex code (and Visualforce pages) can park data that is expensive to fetch or compute and reuse it on later requests. It comes in two flavours: **session cache**, tied to one user's session, and **org cache**, shared across all users, requests and profiles in the org.[^s1] Trailhead stresses that it is a temporary space: cached values can disappear at any moment, so the cache is an accelerator, never a system of record.[^s5]

## How it works

Capacity is carved into **partitions** in Setup (Platform Cache). Each partition has a session segment and an org segment with separately allocated space, and one partition can be marked default so code can omit the namespace and partition name; otherwise keys take the form `Namespace.Partition.Key`.[^s5] Apex reads and writes through `Cache.Org` and `Cache.Session`, or through `Cache.OrgPartition` and `Cache.SessionPartition` when working within one partition, while Visualforce reads values via the `$Cache.Org` and `$Cache.Session` globals.[^s5] Cache operations are transactional: if the Apex transaction fails, its cache writes roll back.[^s1] An optional `Cache.Visibility` setting controls whether code outside the owning namespace can see a value.[^s1]

Each entry has a time-to-live (`ttlsecs`). Session cache entries also die when the session ends, and a session lasts at most eight hours.[^s1] When a partition fills up, Salesforce evicts entries using a least-recently-used (LRU) algorithm.[^s5] The `Cache.CacheBuilder` interface wraps the "check for a miss, then load and store" logic so developers don't hand-write it each time.[^s3]

## Limits and gotchas (Winter '27)

The Winter '27 Apex Developer Guide lists these limits:[^s2]

- Total cache by edition: Enterprise 10 MB; Unlimited and Performance 30 MB; all other editions 0 MB. More can be purchased.[^s2]
- Keys: at most 50 characters. Minimum partition size: 1 MB.[^s2]
- Single cached item: 100 KB for both org and session cache.[^s2]
- Local (per-request, per-partition) cache: 500 KB for session cache, 1,000 KB for org cache.[^s2]
- TTL: minimum 300 seconds; session maximum 28,800 seconds (8 hours); org maximum 172,800 seconds (48 hours), with an org default of 86,400 seconds (24 hours).[^s2]

Professional Edition doesn't support Platform Cache.[^s1] Developer Edition orgs start at 0 MB and can request a 10 MB trial, and other editions can get a 30 MB trial; without capacity, cache calls still execute but nothing is stored and reads return null.[^s4] Trailhead suggests sizing partitions at 5 MB or more.[^s5]

Practical gotchas: putting an item larger than 100 KB throws `Cache.ItemSizeLimitExceededException`; overflowing the local cache can evict items before commit and cause surprising misses; `Cache.Org.getKeys()` and `getCapacity()` are expensive; and calling `contains()` before `get()` doubles the work — just `get()` and test for null.[^s3] A few large items (lists or wrapper objects) are cheaper than many tiny keys, because each item adds serialization and commit overhead.[^s3]

## When to use it (and when not)

Good candidates are data reused across a session or across users that changes slowly and tolerates slight staleness — navigation menus, schedules, a daily exchange-rate snapshot, a shopping cart — and results of costly queries or calculations such as weekly sales totals.[^s4] Rapidly changing, real-time values like stock quotes are a poor fit.[^s4] Because any read can miss, code must always fall back to the database query or API callout; allocating zero capacity is an easy way to test the 100% miss path.[^s5]

## Packaging and ISVs

Security-reviewed managed packages get 3 MB of **Provider Free** capacity that is allocated automatically to the package's partition on install; it is locked in the subscriber org and can't be reassigned, though subscribers can add their own capacity on top.[^s6] Packaged partitions must be non-default, and ISVs can also buy protected namespace cache in 10 MB blocks that only their namespace's Apex can reach.[^s5]

## Connections

Platform Cache sits under the **Salesforce Platform** and helps code stay within **governor limits**: serving a value from memory avoids repeating **SOQL** queries and **Apex callouts**, with those remaining the fallback on a miss.[^s5] It is consumed from **Apex** and configured through **Platform Cache partitions**.[^s5] It complements, rather than replaces, **custom metadata types** and **custom settings**, which are durable configuration stores, whereas the cache is volatile.[^s5] In **large data volume** orgs it helps by caching aggregate results instead of re-running heavy queries.[^s4] Managed-package authors (for example with **second-generation managed packages**) rely on Provider Free capacity after the security review.[^s6]

## Sources

[^s1]: Salesforce Developers, "Platform Cache Features" (Apex Developer Guide). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/pages/apex_platform_cache_features.htm (accessed 2026-11-08)
[^s2]: Salesforce Developers, "Platform Cache Limits" (Apex Developer Guide, Winter '27). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_platform_cache_limits.htm (accessed 2026-11-08)
[^s3]: Salesforce Developers, "Platform Cache Best Practices" (Apex Developer Guide). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_platform_cache_best_practices.htm (accessed 2026-11-08)
[^s4]: Trailhead, "Platform Cache Basics: Get Started with Platform Cache". https://trailhead.salesforce.com/content/learn/modules/platform_cache/platform_cache_get_started (accessed 2026-11-08)
[^s5]: Trailhead, "Platform Cache Basics: Use Platform Cache". https://trailhead.salesforce.com/modules/platform_cache/units/platform_cache_use (accessed 2026-11-08)
[^s6]: Salesforce Developers, "Set Up a Platform Cache Partition with Provider Free Capacity". https://developer.salesforce.com/docs/platform/pkg1-dev/guide/data-platform-cache-setup-provider-capacity.html (accessed 2026-11-08)
