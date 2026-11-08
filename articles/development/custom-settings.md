---
id: kt:custom-settings
type: MetadataType
title: Custom Settings
aliases: [custom setting, list custom settings, hierarchy custom settings, hierarchy custom setting, list custom setting]
domain: development
summary: >-
  Custom objects for application configuration whose records are cached in the application cache and read
  through dedicated Apex methods; list settings hold org-wide static data, while hierarchy settings resolve
  values per user, then profile, then org default.
release: "Winter '27"
status: current
broader: [kt:metadata-driven-architecture]
related: [kt:apex, kt:platform-cache, kt:profiles, kt:apex-testing, kt:named-credentials]
relations:
  - {predicate: alternativeTo, object: kt:custom-metadata-types}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: governedBy, object: kt:governor-limits}
sources:
  - id: s1
    title: "Apex Developer Guide: Custom Settings"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_customsettings.htm
    type: official-docs
    accessed: 2026-11-08
  - id: s2
    title: "Apex Reference Guide: Custom Settings Methods"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_methods_system_custom_settings.htm
    type: official-docs
    accessed: 2026-11-08
  - id: s3
    title: "Advanced Custom Metadata Types: Convert Custom Settings to Custom Metadata Types"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/custom_metadata_types_adv/cmt_convert
    type: official-learning
    accessed: 2026-11-08
  - id: s4
    title: "How to Use Custom Metadata Types"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2015/05/how-to-use-custom-metadata-types
    type: official-blog
    accessed: 2026-11-08
created: 2026-11-08
---

# Custom Settings

Custom settings are a special kind of custom object used to store configuration that code, and the platform, need to read often. Their defining trait is that the data is held in the application cache, so reading it through the custom settings methods does not require a fresh database query each time.[^s1] An admin defines a setting in Setup, adds fields, and then uses **Manage** to enter data sets, each identified by a name.[^s1]

## Two flavours: list and hierarchy

- **List custom settings** store reusable, static data that is the same for the whole org and does not vary by user or profile: country codes, dialing prefixes, catalogue numbers and similar lookup tables.[^s1]
- **Hierarchy custom settings** let values be personalised. Organization defaults are overridden by profile values, which are in turn overridden by user values, so the most specific defined value wins for the running user.[^s1]

## How it works in Apex

Apex exposes static methods on the setting's type. For list settings, `getAll()` returns a map of every data set keyed by name, and `getValues(name)` or `getInstance(name)` return one data set.[^s1][^s2] For hierarchy settings, `getOrgDefaults()` returns the org-level record, `getInstance()` resolves the current user's effective values, and `getInstance(userOrProfileId)` resolves them for a given user or profile.[^s1][^s2]

The difference between `getInstance` and `getValues` matters. `getInstance` merges fields across the hierarchy, taking each field from the lowest level where it is defined, whereas `getValues(userOrProfileId)` returns only what is stored at that exact level and leaves undefined fields null.[^s2] When no record exists, `getInstance` returns a new object with a null Id, which code can populate and save with `insert` or `upsert`.[^s2]

## Limits and gotchas

- **SOQL bypasses the cache.** Settings can be queried with SOQL, but such queries do not use the application cache and count like any other query; the Apex methods are what deliver the caching benefit.[^s2] This is the main reason settings help keep code inside governor limits.[^s1]
- **Null-handling depends on API version.** In API 21.0 and earlier, `getInstance()` and `getOrgDefaults()` could return null on an empty hierarchy; later versions return an empty object instead, and `getAll()` returns an empty map when no data sets exist.[^s2] Code written for old API versions may contain null checks that are no longer necessary, or miss checks it now needs for `getValues(name)`, which still returns null for a missing data set.[^s2]
- **Tests do not see org data.** Setting records are copied into sandboxes but are treated as data for Apex test isolation, so tests must create the records they need (ideally in test setup) or use `SeeAllData=true`.[^s1] From API 42.0, inserting a hierarchy record in a test method with the same `SetupOwnerId` as one already created in `@testSetup` throws a `DUPLICATE_VALUE` exception.[^s2]
- **Not a secrets store.** Apart from protected settings installed by a managed package, custom settings are public and readable by every profile, including the guest user. Salesforce advises against storing secrets, tokens, passwords or personal data in them and points to named credentials or encrypted fields instead.[^s1]
- **Packages ship the shape, not the data.** Only the setting definition is packaged; a subscriber org must populate records itself, typically through Apex after installation.[^s1]

## When to use it (and when not)

Because their records are data, custom settings cannot be promoted from a sandbox with the metadata the way custom metadata type records can; Salesforce describes custom metadata types as similar to list custom settings but with records that are metadata.[^s4] Packaging and deploying configuration as metadata also removes the need for install scripts that seed records.[^s4] For that reason list settings are usually best migrated to custom metadata types, which Trailhead describes as straightforward: recreate the type with the `__mdt` suffix, keep field names, and replace `getAll()` calls with SOQL.[^s3]

Hierarchy settings are the exception. Trailhead explicitly does not recommend converting hierarchy settings to custom metadata types,[^s3] because per-user and per-profile resolution has no direct equivalent there. They remain the fit for values that must differ by user or profile, and for configuration that Apex creates or updates at runtime with ordinary DML.[^s1][^s2]

## Connections

Custom settings sit under **metadata-driven architecture** as one of the platform's configuration mechanisms, and are the older **alternative to custom metadata types**, the usual choice for deployable configuration.[^s3][^s4] They are read primarily from **Apex**, and can also be **queried with SOQL**, at the cost of losing the cache.[^s2] Their caching is distinct from **Platform Cache**, which is a separately allocated cache that developers manage explicitly; custom settings caching is automatic.[^s1] Hierarchy settings resolve against **profiles** and users, test code must seed them per **Apex testing** isolation rules, and **named credentials** are the recommended home for the secrets that should never be stored in a setting.[^s1] Using the cached methods helps code stay within **governor limits**.[^s1]

## Sources
[^s1]: Salesforce, "Apex Developer Guide: Custom Settings". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_customsettings.htm (accessed 2026-11-08)
[^s2]: Salesforce, "Apex Reference Guide: Custom Settings Methods". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_methods_system_custom_settings.htm (accessed 2026-11-08)
[^s3]: Trailhead, "Advanced Custom Metadata Types: Convert Custom Settings to Custom Metadata Types". https://trailhead.salesforce.com/content/learn/modules/custom_metadata_types_adv/cmt_convert (accessed 2026-11-08)
[^s4]: Salesforce Developers Blog, "How to Use Custom Metadata Types". https://developer.salesforce.com/blogs/2015/05/how-to-use-custom-metadata-types (accessed 2026-11-08)
