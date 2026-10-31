---
id: kt:multitenancy
type: Concept
title: Multitenancy
aliases: [multitenant architecture, multi-tenant architecture, Salesforce multitenant kernel]
domain: platform-architecture
summary: >-
  The architectural principle by which one Salesforce instance, database schema and runtime kernel serve many
  customer orgs at once, each isolated by an org (tenant) ID and customized purely through metadata.
release: "Winter '27"
status: concept
broader: [kt:salesforce-platform]
related: [kt:governor-limits, kt:hyperforce, kt:query-optimizer-selectivity]
relations:
  - {predicate: dependsOn, object: kt:metadata-driven-architecture}
  - {predicate: enables, object: kt:governor-limits}
sources:
  - id: s1
    title: "Platform Multitenant Architecture | Get Started with Fundamentals"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/platform-multitenant-architecture
    type: official-docs
    accessed: 2026-10-31
  - id: s2
    title: "The Salesforce Platform - Transformed for Tomorrow | Get Started with Fundamentals"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/platform-transformation
    type: official-docs
    accessed: 2026-10-31
  - id: s3
    title: "Apex Developer Guide: Execution Governors and Limits"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexref/apex_gov_limits.htm
    type: official-docs
    accessed: 2026-10-31
  - id: s4
    title: "Multitenancy and Salesforce Explained (The Apartment Analogy)"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2025/the-apartment-analogy-making-sense-of-salesforces-multitenant-architecture
    type: official-blog
    accessed: 2026-10-31
created: 2026-10-31
---

# Multitenancy

Multitenancy is the foundational design of the Salesforce Platform: a single instance serves many customers, called tenants or **orgs**, while keeping each one isolated and letting each meet its own requirements.[^s1] One instance runs one shared database with a single schema, plus a multitenant kernel that reads each org's metadata and data at runtime.[^s1] Salesforce describes itself as having pioneered the first multitenant cloud platform more than two decades ago, and it applies the principle to all of its services. Every customer gets the same availability and security standard regardless of size.[^s2]

The Salesforce Admins blog uses an apartment-building analogy. Salesforce runs the building-level services, such as front-door security, utility throttling and core infrastructure. Each tenant owns its own unit, decides who gets in, and lays out its rooms as it likes.[^s4]

## How it works

**Org ID isolation.** Every org-specific row carries an OrgID, which the kernel uses to keep each tenant's data and activity private.[^s1] In SalesforceDB the tenant ID is part of the primary key, which clusters a tenant's data together. The application layer adds tenant predicates to every query, and each tenant has its own encryption key.[^s2] Data, metadata, pivot tables and indexes are all physically partitioned by OrgID. Because every query targets exactly one org, the optimizer can prune to that org's partitions instead of scanning whole tables.[^s1]

**Metadata instead of DDL.** Creating a custom object or writing code does not create a database table or compile a binary. The platform stores the definition as metadata and materializes it at runtime, so tenants can change their schema without locks or downtime. The Salesforce-managed kernel is kept separate from tenant-managed metadata, which lets Salesforce, customers and ISVs evolve their parts independently.[^s1]

**Generic storage.** Object and field definitions live in a Universal Data Dictionary (tables such as MT_Objects and MT_Fields). All records live in one MT_Data table, keyed by GUID, OrgID and object ID, with variable-length "flex" value columns. Two fields of the same object can't share a slot, but fields of different objects can. Typed pivot tables (MT_Indexes, MT_Unique_Indexes, MT_Relationships and others) supply indexing, uniqueness and fast joins over this generic store.[^s1]

**Multitenant-aware optimization.** Conventional database statistics ignore per-user visibility, so the platform keeps tenant-, group- and user-level optimizer statistics. It runs pre-queries to measure selectivity before choosing a plan.[^s1]

**Physical layout on Hyperforce.** Each org lives in a Hyperforce **cell**. A cell is what was traditionally called a Salesforce instance, or pod, and it includes the SalesforceDB service. Cells are scale units and blast-radius boundaries, so a failure stays within one cell's tenants. Traffic can also be shifted between cells to manage load.[^s2]

## Limits and gotchas

- **Governor limits are the price of sharing.** Apex runs in a multitenant environment. The runtime enforces limits so that runaway code can't monopolize shared resources, and exceeding a limit throws an exception that can't be handled.[^s3] In Winter '27 (API 68.0), a synchronous transaction gets 100 SOQL queries, 150 DML statements, 10,000 ms of CPU time and a 10 MB heap. Asynchronous transactions get 200 queries, 60,000 ms of CPU time and a 25 MB heap.[^s3]
- **Noisy-neighbor protection runs in several layers.** Beyond Apex limits, the platform caps CPU, memory, queries, DML and callouts.[^s1] Its Vegacache layer gives each customer a guaranteed cache size.[^s2]
- **Shared release cadence.** Salesforce reruns customers' unit tests with each platform release, and production deployments need at least 75% code coverage.[^s1] Tenants don't choose when they upgrade, so automated tests are the safety net.
- **Design for bulk.** Limits push developers toward set-based patterns, such as bulk APIs rather than row-by-row loops.[^s1] The bulk engine can save valid rows and roll back only the faulty ones (partial save), or treat the batch as all-or-nothing.[^s1]

## Why it matters to architects

Multitenancy explains many Salesforce behaviors that surprise people from on-premises backgrounds. Custom objects aren't physical tables, indexing goes through platform-managed pivot tables, and limits are counted per transaction rather than per server.[^s1][^s3] It also brings real benefits: schema changes take effect instantly without downtime, upgrades arrive without customer effort, and per-tenant encryption keys and cell isolation make up a standardized security posture.[^s1][^s2]

## Connections

Multitenancy sits under the **Salesforce Platform** as its core design principle. It **depends on** the **metadata-driven architecture**: storing customizations as metadata, not physical schema, is what lets one kernel and one schema serve every org.[^s1] It **enables** and explains **governor limits**, which exist to stop any one tenant from monopolizing shared resources.[^s3] It relates to **query optimizer selectivity**, because the optimizer's per-org partition pruning and per-user statistics come straight from the tenant model.[^s1] It relates to **Hyperforce**, the public-cloud infrastructure where each org is hosted in an isolated cell.[^s2]

## Sources

[^s1]: Salesforce Architects, "Platform Multitenant Architecture | Get Started with Fundamentals". https://architect.salesforce.com/fundamentals/platform-multitenant-architecture (accessed 2026-10-31)
[^s2]: Salesforce Architects, "The Salesforce Platform - Transformed for Tomorrow | Get Started with Fundamentals". https://architect.salesforce.com/fundamentals/platform-transformation (accessed 2026-10-31)
[^s3]: Salesforce Developers, "Apex Developer Guide: Execution Governors and Limits" (Winter '27, API 68.0). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexref/apex_gov_limits.htm (accessed 2026-10-31)
[^s4]: Joshua Birk, Salesforce Admins Blog, "Multitenancy and Salesforce Explained" (2025-06-30). https://admin.salesforce.com/blog/2025/the-apartment-analogy-making-sense-of-salesforces-multitenant-architecture (accessed 2026-10-31)
