---
id: kt:data-mask-and-seed
type: Product
title: Data Mask & Seed
aliases: [Salesforce Data Mask & Seed, Data Mask and Seed, Own Accelerate, Salesforce Seeding, sandbox seeding]
domain: devops-and-alm
summary: >-
  Salesforce's add-on for populating sandboxes with reusable, relationship-preserving subsets of production or sandbox
  data while masking sensitive fields; it combines the original Data Mask with seeding capabilities from Own Accelerate.
release: "Winter '27"
status: current
broader: [kt:environment-strategy, kt:data-governance]
related: [kt:sandbox-types, kt:test-data-factory, kt:scratch-orgs, kt:testing-strategy, kt:backup-and-recover]
relations:
  - {predicate: replaces, object: kt:salesforce-data-mask}
  - {predicate: dependsOn, object: kt:sandbox-types}
  - {predicate: alternativeTo, object: kt:sandbox-templates}
  - {predicate: integratesWith, object: kt:backup-and-recover}
sources:
  - id: s1
    title: "Get Started with Seeding (Seeding Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/seeding-basics/get-started-with-seeding
    type: official-learning
    accessed: 2026-11-14
  - id: s2
    title: "Data Masking & Seeding Tools"
    publisher: Salesforce
    url: https://www.salesforce.com/platform/data-masking/
    type: official-blog
    accessed: 2026-11-14
  - id: s3
    title: "A New Level of Data Resilience, Compliance, and Security"
    publisher: Salesforce
    url: https://www.salesforce.com/platform/own-integration/
    type: official-blog
    accessed: 2026-11-14
  - id: s4
    title: "Summer '26 Release: Top Development & Security Features"
    publisher: Salesforce Blog
    url: https://www.salesforce.com/blog/platform-summer-26-release/
    type: official-blog
    accessed: 2026-11-14
  - id: s5
    title: "Platform Add-On Features and Pricing"
    publisher: Salesforce
    url: https://www.salesforce.com/platform/pricing-add-ons/
    type: official-blog
    accessed: 2026-11-14
  - id: s6
    title: "What is Data Seeding? How It Works, Methods, and Best Practices"
    publisher: Salesforce
    url: https://www.salesforce.com/platform/data-seeding/
    type: official-blog
    accessed: 2026-11-14
created: 2026-11-14
---

# Data Mask & Seed

Data Mask & Seed is Salesforce's tool for giving sandboxes realistic test data without exposing the personal data that
production holds. It does two jobs: **seeding**, which copies a chosen, related subset of records into a sandbox, and
**masking**, which de-identifies sensitive fields in every sandbox so teams can test with production-like data while
meeting regimes such as GDPR, CCPA, FINRA and HIPAA.[^s2] Salesforce sells it as a platform add-on for Enterprise and
Unlimited editions, priced at 10% of net spend.[^s5]

## Origins

Salesforce agreed to buy Own Company in September 2024 and, in March 2025, announced that Own's products had joined
the Salesforce Platform. As part of that, the existing Data Mask was extended with the seeding capabilities of Own
Accelerate, and the combined offering was named Data Mask & Seed.[^s3] In the Summer '26 release Salesforce made it
generally available as a core app with a simpler interface, adding automatic detection of personally identifiable
information and automatic insertion of simulated records while keeping the existing features.[^s4]

## How seeding works

Seeding moves datasets from a production org, a sandbox or a backup into another environment; seeding from a backup
needs Backup & Recover.[^s1] Trailhead lists Developer, Developer Pro, Partial Copy and Full sandboxes, plus scratch orgs,
as targets, while the product page lists the four sandbox types.[^s1][^s2] The unit of reuse is a **seed template**, which
can be run against any sandbox that shares the source's metadata structure.[^s1] Trailhead describes three template
styles:

- **Nodes:** you add each object explicitly, starting from a root object and adding children and optional parents.[^s1]
- **Levels:** you pick root objects and say how many levels of related objects below them to include.[^s1]
- **Generate:** you pick objects for which synthetic records are created and seeded, without copying from a source.[^s1]

Filters narrow the records or record types copied, and a *Sample for Coverage* option aims for a dataset that reflects
the spread of values found in production.[^s1] A seed can insert new records, update existing ones or replace them; the
data can be previewed and resized to fit the target sandbox before it is applied.[^s2] Jobs can run incrementally on a
daily, weekly or monthly schedule, and they can bypass trigger automations that would otherwise slow provisioning.[^s1][^s2]
A Seeding Summary report helps diagnose permission and data problems after a run.[^s1]

## How masking works

Masking rules are set per field according to sensitivity, using anonymization, pseudonymization, pattern matching or
deletion. Rules can draw on number ranges, custom lists, a library of fake values or existing data, and can alter part
of a value or append to it, while preserving the field's format.[^s2] Admins can record sensitivity and compliance
categories on standard and custom fields and filter by them, so the same PII is masked consistently across sandboxes.[^s2]

## When to use it (and when not)

Salesforce frames seeding as injecting just enough representative data to test features and automation, as opposed to
cloning everything. Developer sandboxes start empty, Partial Copy sandboxes hold only a sample, and even Full sandboxes
may lack records for new features, so each can need seeding.[^s6] Data Mask & Seed suits teams that refresh many
sandboxes and want repeatable, masked, relationship-aware datasets. For small or code-centric needs, Salesforce also
points to lighter options: Data Import Wizard, Data Loader, the Salesforce CLI, APIs, and Apex such as Batch or
Queueable jobs.[^s6] Its recommended practice is to seed the minimum dataset, validate relationships, keep seed data in
version control and reseed regularly.[^s6]

## Connections

Data Mask & Seed **replaces** `kt:salesforce-data-mask`, the legacy masking package that it grew out of.[^s3] It sits
under `kt:environment-strategy` and `kt:data-governance` because it decides what data each environment holds and how
that data is protected.[^s2][^s6] It **depends on** `kt:sandbox-types`, whose types are its targets, and is an
**alternative to** `kt:sandbox-templates`, the native way of choosing which records a Partial Copy or Full sandbox
receives.[^s1][^s2] It **integrates with** `kt:backup-and-recover`, which lets backups serve as a seeding source.[^s1]
Code-level fixtures from `kt:test-data-factory` remain the right tool for Apex unit tests, while seeded data serves
integration, UAT and training work described in `kt:testing-strategy`; Trailhead also lists `kt:scratch-orgs` as
targets.[^s1][^s6]

## Sources

[^s1]: Trailhead, "Get Started with Seeding (Seeding Basics)". https://trailhead.salesforce.com/content/learn/modules/seeding-basics/get-started-with-seeding (accessed 2026-11-14)
[^s2]: Salesforce, "Data Masking & Seeding Tools". https://www.salesforce.com/platform/data-masking/ (accessed 2026-11-14)
[^s3]: Salesforce, "A New Level of Data Resilience, Compliance, and Security". https://www.salesforce.com/platform/own-integration/ (accessed 2026-11-14)
[^s4]: Salesforce Blog, "Summer '26 Release: Top Development & Security Features". https://www.salesforce.com/blog/platform-summer-26-release/ (accessed 2026-11-14)
[^s5]: Salesforce, "Platform Add-On Features and Pricing". https://www.salesforce.com/platform/pricing-add-ons/ (accessed 2026-11-14)
[^s6]: Salesforce, "What is Data Seeding? How It Works, Methods, and Best Practices". https://www.salesforce.com/platform/data-seeding/ (accessed 2026-11-14)
