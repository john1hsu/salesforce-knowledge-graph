---
id: kt:divisions
type: Feature
title: Divisions
aliases: [Salesforce divisions, Division object, record divisions, default division, global division]
domain: data-model
summary: >-
  A Salesforce feature, enabled by Customer Support for large orgs, that tags records with a logical segment of the org's data (such as a region or business unit) so searches, reports and list views can be pre-filtered to a smaller, more relevant set of records.
release: "Winter '27"
status: current
broader: [kt:large-data-volumes]
related: [kt:standard-objects, kt:user-management, kt:skinny-tables, kt:custom-indexes]
relations:
  - {predicate: queriedWith, object: kt:sosl}
  - {predicate: contrastsWith, object: kt:salesforce-sharing-model}
sources:
  - id: s1
    title: "Large Data Volumes Best Practices: Divisions"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-infrastructure-divisions.html
    type: official-docs
    accessed: 2026-11-16
  - id: s2
    title: "Object Reference for the Salesforce Platform (Winter '27): Division"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_division.htm
    type: official-docs
    accessed: 2026-11-16
  - id: s3
    title: "SOQL and SOSL Reference: WITH DivisionFilter"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.252.0.soql_sosl.meta/soql_sosl/sforce_api_calls_sosl_with.htm
    type: official-docs
    accessed: 2026-11-16
  - id: s4
    title: "Large Data Volumes Best Practices: Infrastructure for Systems with Large Data Volumes"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-infrastructure-for-performance.html
    type: official-docs
    accessed: 2026-11-16
  - id: s5
    title: "Large Data Volumes Best Practices: Searching"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-best-practices-searching.html
    type: official-docs
    accessed: 2026-11-16
created: 2026-11-16
---

# Divisions

Divisions are a Salesforce feature for partitioning an org's data into logical segments, such as business units or
regions like "North America" or "Healthcare", represented by the standard `Division` object.[^s2] Salesforce positions
them as a large-data-volume technique: splitting records into, for example, US, EMEA and APAC divisions keeps each
segment smaller so queries and reports return fewer records.[^s1] The Division object is only available when the
org has the Division permission turned on, and admins cannot switch it on themselves; it is enabled by contacting
Salesforce Customer Support.[^s1][^s2]

## Eligibility

The Large Data Volumes best-practices guide describes divisions as aimed at big deployments and gives a threshold of
more than one million records in a single object and more than 35 licenses.[^s1] The same guide lists divisions among
the platform's infrastructure features for LDV performance, alongside the query optimizer, database statistics, skinny
tables and indexes.[^s4]

## How it works

When divisions are first enabled, Salesforce creates a global division; further divisions are created as needed.[^s2]
Each division record carries a name (up to 80 characters), an active flag, a flag marking the org's global default
division, and a sort order that controls where it appears in the Division picklist when users are created or
edited.[^s2] Users and groups get a `DefaultDivision` field, while other division-enabled objects get a field named
`Division`; a user's division is stamped on records that user owns or creates.[^s2] Checking for `DefaultDivision` on
User or Group is the documented way to confirm the feature is on in an org.[^s2]

Through the API the Division object supports create, update, upsert, query and retrieve, plus `getUpdated` and
`getDeleted`, but `delete()` is not among its supported calls; the object instead exposes an Active flag.[^s2] Customer Portal users cannot access the object.[^s2]

## Searching by division

The object reference notes that division values can make searches, reports and list views faster and more relevant on
large data sets.[^s2] In SOSL, the optional `WITH DIVISION` clause, placed after `RETURNING`, filters every result by
the division field and applies that filter before other filters; the division can be named rather than given as an
ID.[^s3] Salesforce recommends this pre-filter over filtering on division in a `WHERE` clause because it is
faster.[^s2] A search scoped to one division also returns records in the global division, and users can search by
division whether or not they hold the "Affected by Divisions" permission.[^s3] The LDV searching guidance likewise
suggests partitioning data with divisions as one way to improve search performance in some cases.[^s5]

## Gotchas

- The User object has a separate standard text field named `Division`, similar to Company or Department, that is unrelated to the Division object; the lookup that matters is `DefaultDivision`.[^s2]
- Because enabling divisions requires Customer Support and the object cannot be deleted through the API, treat the decision as long-lived and plan the segment design before requesting it.[^s1][^s2]
- Global-division records appear in every division-scoped search, so leaving many records in the global division reduces the filtering benefit.[^s3]

## When to use it (and when not)

Divisions fit orgs that already meet the LDV threshold and whose users mostly work within one natural segment, so
pre-filtering search and reporting to that segment trims result sets.[^s1][^s2] For orgs that are not near that
scale, or whose performance problem is a slow query rather than broad result sets, the other LDV infrastructure
options such as indexes and skinny tables are the more common levers.[^s4]

## Connections

Divisions sit under **large data volumes** as one of the platform's partitioning techniques, next to **skinny tables**
and **custom indexes** in Salesforce's list of LDV infrastructure features.[^s1][^s4] They are queried with **SOSL**
through the `WITH DIVISION` filter.[^s3] They add a field to **standard objects** and a default division to users,
which makes them part of **user management**.[^s2] They contrast with the **sharing model**: the sources describe
divisions as a way to make searches, reports and list views faster and more relevant, not as a record-access
control, so visibility still comes from sharing.[^s1][^s2]

## Sources

[^s1]: Salesforce Developers, "Large Data Volumes Best Practices: Divisions". https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-infrastructure-divisions.html (accessed 2026-11-16)
[^s2]: Salesforce Developers, "Object Reference for the Salesforce Platform (Winter '27): Division". https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_division.htm (accessed 2026-11-16)
[^s3]: Salesforce Developers, "SOQL and SOSL Reference: WITH DivisionFilter". https://developer.salesforce.com/docs/atlas.en-us.252.0.soql_sosl.meta/soql_sosl/sforce_api_calls_sosl_with.htm (accessed 2026-11-16)
[^s4]: Salesforce Developers, "Large Data Volumes Best Practices: Infrastructure for Systems with Large Data Volumes". https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-infrastructure-for-performance.html (accessed 2026-11-16)
[^s5]: Salesforce Developers, "Large Data Volumes Best Practices: Searching". https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-best-practices-searching.html (accessed 2026-11-16)
