---
id: kt:metadata-driven-architecture
type: Concept
title: Metadata-Driven Architecture
aliases: [metadata-driven design, metadata-driven development, polymorphic application design, metadata framework]
domain: platform-architecture
summary: >-
  The Salesforce design principle in which apps, schema, UI, security and logic are stored as metadata that a shared
  runtime engine interprets on demand, instead of as compiled code or physical database structures.
release: "Winter '27"
status: concept
broader: [kt:salesforce-platform]
related: [kt:custom-metadata-types, kt:record-types, kt:source-tracking, kt:apex]
relations:
  - {predicate: enables, object: kt:multitenancy}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: enables, object: kt:salesforce-dx}
sources:
  - id: s1
    title: "Platform Multitenant Architecture | Get Started with Fundamentals"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/platform-multitenant-architecture
    type: official-docs
    accessed: 2026-11-04
  - id: s2
    title: "Understand the Salesforce Architecture (Agentforce 360 Platform Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/modules/starting_force_com/units/starting_understanding_arch
    type: official-learning
    accessed: 2026-11-04
  - id: s3
    title: "Metadata API Developer Guide: Understanding Metadata API"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_intro.htm
    type: official-docs
    accessed: 2026-11-04
  - id: s4
    title: "Demystifying the Salesforce Metadata API"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2022/03/demystifying-the-salesforce-metadata-api
    type: official-blog
    accessed: 2026-11-04
  - id: s5
    title: "The Design of the Force.com Multitenant Internet Application Development Platform (SIGMOD '09)"
    publisher: ACM SIGMOD
    url: https://pubs.dbs.uni-leipzig.de/cloud/sites/cloud.pubs.dbs.uni-leipzig.de/files/p889-weissman-1.pdf
    type: peer-reviewed
    accessed: 2026-11-04
created: 2026-11-04
---

# Metadata-Driven Architecture

Metadata-driven architecture is the principle that a Salesforce application is a description rather than a program. Object definitions, fields, page layouts, security settings, automation and even compiled Apex are stored as metadata, and a shared runtime engine reads that description to produce the running app for each org.[^s1][^s5] Trailhead sums it up as the platform being powered by metadata, which it defines simply as data about data: strip the values out of a record and the empty structure that remains, such as an address, a price or a bedroom count, is metadata.[^s2]

## How it works

**Separation of layers.** Salesforce's 2009 SIGMOD paper describes four cleanly separated parts: the compiled runtime engine (kernel), application data, base application metadata, and each tenant's own metadata and customizations. Because they are distinct, Salesforce can upgrade the kernel, change core apps, or let a customer customize components with little risk to the other layers.[^s5] The current Architects guidance makes the same point: the Salesforce-managed kernel stays apart from tenant-managed metadata, so Salesforce, customers and ISVs evolve their parts independently.[^s1]

**Polymorphic, materialized at runtime.** A single statically compiled executable cannot fit thousands of tenants, so the application must be polymorphic, adapting to each org at runtime.[^s5] Creating an object or saving code therefore does not create a table or compile a binary; the platform records metadata and uses it to dynamically materialize virtual components when they are needed.[^s1] Even the APIs follow suit: the same metadata generates each org's custom REST and SOAP interfaces.[^s1] Trailhead notes that every new field automatically gets an API name, which is what lets one field appear in a mobile app, a custom page or an email template.[^s2]

**Caching.** Because the engine consults metadata constantly, recently used metadata is held in large in-memory caches to avoid disk I/O and recompilation.[^s1] Compiled Apex is itself stored as metadata, then loaded into a per-org cache on first execution so later users in that org reuse it.[^s1]

**Dependency awareness.** The paper explains that the platform validates queries embedded in Apex and tracks dependencies, so a metadata change cannot silently break code that relies on it.[^s5]

## Working with metadata

Metadata is accessed through **metadata types** and **components**: a type defines the structure of a kind of setting, and a component is one instance of it.[^s3] The Metadata API deploys, retrieves, creates, updates and deletes these components to move customizations between orgs, but it never touches business records; those go through the REST or SOAP API.[^s3] Deploy and retrieve move complete sets of components named in a manifest and overwrite the target, whereas push and pull use source tracking to move only changes and report conflicts.[^s4] Change sets and DevOps Center use the Metadata API under the hood.[^s4] In Winter '27 the Metadata API is at version 68.0.[^s3]

## Limits and gotchas

- **Not all features are equally exposed.** Support for a given feature varies by API version, so the Metadata Coverage Report is worth checking before planning automated deployments.[^s4]
- **Configuration is code.** Because layouts, permissions and automation are all metadata, they need the same version control, review and testing as Apex; the Developers Blog lists schema, processes, presentation, authorization and general configuration as metadata.[^s4]
- **Speed has a cost.** Metadata is stored and served as soon as it is created, which makes declarative building fast[^s2], but it also means a production change takes effect immediately. Salesforce reruns customers' unit tests on each platform release to catch breaking changes, which only helps if those tests exist.[^s1]

## Why it matters

The principle explains why low-code and pro-code customizations coexist, why upgrades arrive without customer effort, and why AppExchange packages can install whole applications: a package is simply third-party metadata.[^s1] Trailhead also places Data 360 within the same metadata framework, so the pattern now extends beyond the core CRM schema.[^s2]

## Connections

Metadata-driven architecture is a core principle of the **Salesforce Platform** and **enables multitenancy**: storing definitions as metadata rather than physical schema is what lets one kernel serve every org.[^s1][^s5] It is **configured via** the **Metadata API**, and its source-tracked, file-based form **enables Salesforce DX** workflows built on **source tracking**.[^s3][^s4] **Custom metadata types** and **record types** are concrete examples of this model, and **Apex** participates in it because compiled code is stored and cached as metadata.[^s1]

## Sources

[^s1]: Salesforce Architects, "Platform Multitenant Architecture | Get Started with Fundamentals". https://architect.salesforce.com/fundamentals/platform-multitenant-architecture (accessed 2026-11-04)
[^s2]: Trailhead, "Understand the Salesforce Architecture" (Agentforce 360 Platform Basics). https://trailhead.salesforce.com/modules/starting_force_com/units/starting_understanding_arch (accessed 2026-11-04)
[^s3]: Salesforce Developers, "Metadata API Developer Guide: Understanding Metadata API" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_intro.htm (accessed 2026-11-04)
[^s4]: Neha Ahlawat, Salesforce Developers Blog, "Demystifying the Salesforce Metadata API" (2022-03-01). https://developer.salesforce.com/blogs/2022/03/demystifying-the-salesforce-metadata-api (accessed 2026-11-04)
[^s5]: Craig D. Weissman and Steve Bobrowski, "The Design of the Force.com Multitenant Internet Application Development Platform", SIGMOD '09. https://pubs.dbs.uni-leipzig.de/cloud/sites/cloud.pubs.dbs.uni-leipzig.de/files/p889-weissman-1.pdf (accessed 2026-11-04)
