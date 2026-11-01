---
id: kt:salesforce-platform
type: Product
title: Salesforce Platform
aliases: [Lightning Platform, Force.com, Salesforce core platform]
domain: platform-architecture
summary: >-
  The shared, multitenant, metadata-driven foundation (infrastructure, data layer, runtime, automation, code, UI and
  APIs) on which Salesforce builds its own clouds and on which customers and ISVs build custom apps; marketed since
  Dreamforce 2025 as part of the Agentforce 360 Platform.
release: "Winter '27"
status: current
broader: [kt:platform-as-a-service]
related: [kt:multitenancy, kt:metadata-driven-architecture]
relations:
  - {predicate: dependsOn, object: kt:hyperforce}
  - {predicate: hasPart, object: kt:apex}
  - {predicate: hasPart, object: kt:flow-builder}
  - {predicate: enables, object: kt:service-cloud}
sources:
  - id: s1
    title: "The Salesforce Platform - Transformed for Tomorrow | Get Started with Fundamentals"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/platform-transformation
    type: official-docs
    accessed: 2026-11-01
  - id: s2
    title: "Architecture Basics | Get Started with Fundamentals"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/architecture-basics
    type: official-docs
    accessed: 2026-11-01
  - id: s3
    title: "Agentforce 360 Platform Basics"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/modules/starting_force_com
    type: official-learning
    accessed: 2026-11-01
  - id: s4
    title: "Get to Know the Salesforce Release Process (Salesforce Releases)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/modules/sf_releases/units/sf_releases_start
    type: official-learning
    accessed: 2026-11-01
  - id: s5
    title: "Salesforce press release: Agentforce 360 (2025-10-13)"
    publisher: Salesforce
    url: https://www.salesforce.com/in/news/press-releases/2025/10/13/agentic-enterprise-announcement/
    type: news
    accessed: 2026-11-01
created: 2026-11-01
---

# Salesforce Platform

The Salesforce Platform is the common foundation under every Salesforce org. It is a layered stack in which each layer's capabilities flow up into the layers above it. From the bottom up, it runs from public-cloud infrastructure (Hyperforce) through a metadata framework and a data layer to AI and app platform services. Salesforce lists its guiding principles as enterprise-grade trust, multitenancy, metadata-driven design, API first, openness and interoperability, and agentic.[^s1] Sales Cloud, Service Cloud and the other Salesforce clouds are apps that Salesforce Engineering builds on this platform. Tenants receive them through licensing and provisioning, alongside whatever their own admins, developers and ISV partners build.[^s1]

**Naming.** Salesforce has rebranded the platform several times. Trailhead's introductory module still lives at a `starting_force_com` URL, but it is now titled "Agentforce 360 Platform Basics," while its page description still says Salesforce Platform.[^s3] At Dreamforce on 13 October 2025, Salesforce announced Agentforce 360 as generally available. The announcement presented the Agentforce 360 Platform as the foundation for enterprise AI agents, Data 360 as the unified data layer, Customer 360 apps as the business logic, and Slack as the conversational interface.[^s5] In this graph, `kt:salesforce-platform` is the general-purpose application platform, and the agent product line is a separate node, `kt:agentforce`.

## How it works

**Multitenant orgs.** Each customer org is a tenant on shared infrastructure. Because tenants share it, the platform caps resources per transaction and per org so that no one tenant can monopolize compute. It also enforces a fixed order of execution for database operations.[^s2]

**Metadata framework.** Apps are defined as metadata on top of a stable abstraction made up of an object-relational mapper, a prescribed order of execution and a "Core" runtime. Core remains the single system of record for application metadata, which is synchronized to caches inside independent services.[^s1] Metadata and data follow different lifecycles. Metadata is copied into every sandbox, moves through the Metadata API, can be packaged, and does not count against storage. Data is copied only into full or partial copy sandboxes, moves through data loads, can't be packaged, and does count against storage.[^s2]

**Data and infrastructure.** The data layer combines a multitenant relational database with a petabyte-scale lakehouse that Data 360 uses for analytics and AI.[^s1] SalesforceDB extends PostgreSQL and separates compute from storage. It includes the tenant ID in every primary key, gives each tenant its own encryption key, and runs across three availability zones with automated failover.[^s1] Hyperforce hosts all of this on public cloud providers. It is organized into instances, functional domains, cells and supercells. A cell is what was traditionally called a Salesforce instance, and it acts as a blast-radius boundary.[^s1]

**Building blocks.** For low-code automation, Flow Builder supports record-triggered, scheduled or event-driven, screen and orchestrator flows. For pro-code logic, Apex supports triggers, web services and custom APIs. The Lightning Web Stack covers UI, Heroku provides cloud-native compute, and an API-first portfolio aims to expose everything the standard UI can do.[^s1] Declarative and programmatic logic share one transaction model, and in both cases the rule is to work with the order of execution, not around it.[^s2]

## Limits and gotchas

- **Limits are per org and per transaction.** Edition and enabled features determine org-wide allowances, including a rolling count of API calls. Apex has its own governor limits, which differ by code type.[^s2]
- **You don't choose your upgrade date.** Salesforce ships three seasonal releases a year (Spring, Summer and Winter), upgrades every customer automatically, and keeps all customers on the same version. Sandboxes are upgraded first, 4–6 weeks before production.[^s4] Each release also increments the version of every platform API. APIs remain backward compatible, but adopting new behavior can require refactoring, so plan regular maintenance.[^s2]
- **Custom settings are data; custom metadata types are metadata.** That difference decides whether a configuration value can be packaged and deployed, or has to be loaded as data.[^s2]

## When to use it (and when not)

Build on the platform when the app needs Salesforce data, its security and sharing model, or its automation, because you inherit the trust, compliance and release machinery for free.[^s1] Work that needs long-running compute or non-Salesforce runtimes fits better on Heroku or an external service integrated through APIs. Those workloads would otherwise run into per-transaction limits.[^s1][^s2]

## Connections

The Salesforce Platform is Salesforce's **platform-as-a-service** offering. Its design rests on **multitenancy** and a **metadata-driven architecture**, both listed among its core principles.[^s1] It **depends on Hyperforce** for infrastructure.[^s1] It **has** **Apex** and **Flow Builder** as its pro-code and low-code logic tools.[^s1] It **enables** clouds such as **Service Cloud**, which Salesforce builds as native apps on top of the platform.[^s1] Agentforce sits on this foundation as the agent layer of the Agentforce 360 lineup.[^s5]

## Sources

[^s1]: Salesforce Architects, "The Salesforce Platform - Transformed for Tomorrow | Get Started with Fundamentals". https://architect.salesforce.com/fundamentals/platform-transformation (accessed 2026-11-01)
[^s2]: Salesforce Architects, "Architecture Basics | Get Started with Fundamentals". https://architect.salesforce.com/fundamentals/architecture-basics (accessed 2026-11-01)
[^s3]: Trailhead, "Agentforce 360 Platform Basics". https://trailhead.salesforce.com/modules/starting_force_com (accessed 2026-11-01)
[^s4]: Trailhead, "Get to Know the Salesforce Release Process". https://trailhead.salesforce.com/modules/sf_releases/units/sf_releases_start (accessed 2026-11-01)
[^s5]: Salesforce, press release announcing Agentforce 360 (2025-10-13). https://www.salesforce.com/in/news/press-releases/2025/10/13/agentic-enterprise-announcement/ (accessed 2026-11-01)
