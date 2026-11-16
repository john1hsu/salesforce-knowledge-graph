---
id: kt:heroku-connect
type: Feature
title: Heroku Connect
aliases: [herokuconnect add-on, Heroku Connect add-on]
domain: integration
summary: >-
  A Heroku add-on that replicates Salesforce object data into tables in a Heroku Postgres database, one-way or
  bidirectionally, so Heroku apps can read and write CRM data with plain SQL while Connect polls Salesforce for
  changes and pushes database edits back through the SOAP or Bulk API.
release: "Winter '27"
status: current
broader: [kt:heroku, kt:data-integration]
related: [kt:heroku-applink, kt:batch-data-synchronization]
relations:
  - {predicate: dependsOn, object: kt:heroku-postgres}
  - {predicate: alternativeTo, object: kt:salesforce-connect}
  - {predicate: integratesWith, object: kt:change-data-capture}
  - {predicate: integratesWith, object: kt:streaming-api}
sources:
  - id: s1
    title: "Heroku Connect"
    publisher: Heroku Dev Center (Salesforce)
    url: https://devcenter.heroku.com/articles/herokuconnect
    type: official-docs
    accessed: 2026-11-16
  - id: s2
    title: "Writing Data to Salesforce with Heroku Connect"
    publisher: Heroku Dev Center (Salesforce)
    url: https://devcenter.heroku.com/articles/writing-data-to-salesforce-with-heroku-connect
    type: official-docs
    accessed: 2026-11-16
  - id: s3
    title: "Heroku Connect Mapping Configuration Options"
    publisher: Heroku Dev Center (Salesforce)
    url: https://devcenter.heroku.com/articles/mapping-configuration-options
    type: official-docs
    accessed: 2026-11-16
  - id: s4
    title: "Integrate Salesforce and Heroku with Heroku Connect (Salesforce & Heroku Integration)"
    publisher: Trailhead (Salesforce)
    url: https://trailhead.salesforce.com/salesforce_heroku_integration/integrating_with_heroku_connect
    type: official-learning
    accessed: 2026-11-16
  - id: s5
    title: "Change Data Capture for accelerated polling is now available for all Heroku Connect customers"
    publisher: Heroku Dev Center changelog (Salesforce)
    url: https://devcenter.heroku.com/changelog-items/3432
    type: official-docs
    accessed: 2026-11-16
created: 2026-11-16
---

# Heroku Connect

Heroku Connect is a Heroku add-on that keeps a Salesforce org and a Heroku Postgres database in sync. It moves only object and table data, and more than one org can sync into the same database.[^s1] Apps on Heroku then work with that data through ordinary SQL instead of calling Salesforce APIs per request.[^s4] Trailhead frames it as data replication: Salesforce stays the owner of the schema, so a new field is added in Salesforce first and then to the mapping.[^s4]

## How it works

Setup is an OAuth authorization to the org followed by **mappings**, one per object, that choose which fields land in Postgres tables.[^s4] Each mapping is read-only by default; ticking the write-database-updates option makes it read-write.[^s3]

- **Reading from Salesforce.** Standard polling defaults to every 10 minutes, can be set from 2 to 60 minutes in 1-minute steps, and is floored at 10 minutes on the demo plan.[^s3]
- **Accelerated polling.** The Streaming API or Change Data Capture tells Connect that a mapped object changed, prompting an extra poll; notifications inside 10 seconds collapse into one poll.[^s3]
- **Writing to Salesforce.** Postgres triggers record changes on read-write tables into a shared `_trigger_log` table, which Connect polls every 2 minutes or sooner on a `pg_notify`, at most every 10 seconds.[^s2]

CDC support for accelerated polling, for objects the Streaming API doesn't cover, became available to all customers effective 30 October 2025; CDC must be enabled on those objects in the org.[^s5] Accelerated polling is best effort, signals only that data changed, and doesn't count against CDC allocations.[^s3]

## Write algorithms and APIs

Each connection uses one write algorithm for all its read-write mappings.[^s2] **Ordered Writes** (the default) replays the trigger log in order, so Salesforce field history sees every change, but a failed insert blocks later changes for that mapping until it is fixed.[^s2] **Merged Writes** condenses changes to fill SOAP messages, retries failed inserts on the next update, and can hide intermediate values from Apex triggers.[^s2]

Connect switches to the Bulk API only for Ordered Writes on a mapping with a unique identifier, with 2,000 to 10,000 contiguous same-type changes, on API v39 or later; otherwise it sends SOAP messages of up to 200 records.[^s2] The unique identifier is an External ID field marked Unique, and Dev Center recommends UUIDs rather than integer sequences to fill it.[^s3]

## Limits and gotchas

- **Demo plan.** It syncs at most 10,000 rows across all mappings and keeps the trigger log for 7 days, against 31 on paid plans.[^s1]
- **Integration user.** Use a dedicated API-enabled user per add-on with View All or Modify All on mapped objects; row-by-row permission checks otherwise slow syncs.[^s1]
- **Per-user caps.** Salesforce allows 10 concurrent queries and, by default, 5 OAuth tokens per user, so shared users cause reauthorization pauses.[^s1]
- **Postgres sizing.** Production needs at least a `-4` tier plan, a UTC database, and no Heroku Postgres connection pooling, which Connect doesn't support.[^s1]
- **What isn't synced.** Archived Tasks and Events, partial (filtered-subset) syncs and binary data are unsupported; store files elsewhere and sync a URI.[^s3]
- **Writes are partial too.** `TRUNCATE` isn't captured, and Connect can't guarantee transaction-accurate ordering of writes.[^s2]
- **Fixed org.** A connection can't be repointed to another org, and a refreshed sandbox counts as a new org.[^s1]
- **Destructive removal.** Removing the add-on drops the mapped tables, so back them up first.[^s1]

## When to use it (and when not)

Trailhead's model case is a consumer-facing site reading a product catalog from Postgres, with reactions such as likes written back to Salesforce for sales and marketing.[^s4] Replication suits apps that need fast local SQL over a copy of CRM data, while Salesforce Connect proxies external data into the org without copying it.[^s4] Sync is low latency but not real-time, so it is a poor fit where every change must reach Salesforce immediately.[^s4]

## Connections

Heroku Connect is a part of `kt:heroku` and a form of `kt:data-integration`, specifically scheduled replication akin to `kt:batch-data-synchronization`.[^s1][^s4] It **depends on** `kt:heroku-postgres`, the only database it syncs to.[^s1] It is an **alternative to** `kt:salesforce-connect`, the proxying approach Trailhead contrasts it with.[^s4] It **integrates with** `kt:streaming-api` and `kt:change-data-capture` for accelerated polling.[^s3][^s5] It is **related** to `kt:heroku-applink`, another Heroku add-on bridging to Salesforce; Connect itself is purely a data integration.[^s1]

## Sources

[^s1]: Heroku Dev Center, "Heroku Connect". https://devcenter.heroku.com/articles/herokuconnect (accessed 2026-11-16)
[^s2]: Heroku Dev Center, "Writing Data to Salesforce with Heroku Connect". https://devcenter.heroku.com/articles/writing-data-to-salesforce-with-heroku-connect (accessed 2026-11-16)
[^s3]: Heroku Dev Center, "Heroku Connect Mapping Configuration Options". https://devcenter.heroku.com/articles/mapping-configuration-options (accessed 2026-11-16)
[^s4]: Trailhead, "Integrate Salesforce and Heroku with Heroku Connect". https://trailhead.salesforce.com/salesforce_heroku_integration/integrating_with_heroku_connect (accessed 2026-11-16)
[^s5]: Heroku Dev Center, "Change Data Capture for accelerated polling is now available for all Heroku Connect customers". https://devcenter.heroku.com/changelog-items/3432 (accessed 2026-11-16)
