---
id: kt:sosl
type: Language
title: SOSL
aliases: [Salesforce Object Search Language, SOSL query, SOSL search]
domain: development
summary: >-
  Salesforce Object Search Language, the text-search language that finds words across many fields and
  objects in a single query through the platform search index, used from Apex and the APIs.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:apex, kt:knowledge-base, kt:salesforce-sharing-model]
relations:
  - {predicate: contrastsWith, object: kt:soql}
  - {predicate: governedBy, object: kt:governor-limits}
  - {predicate: usedBy, object: kt:apex}
  - {predicate: coveredBy, object: kt:platform-developer-certification}
sources:
  - id: s1
    title: "SOQL and SOSL Reference: SOSL Syntax"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-sosl-syntax.html
    type: official-docs
    accessed: 2026-11-07
  - id: s2
    title: "SOQL and SOSL Reference: SOSL Limits on Search Results"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-sosl-limits.html
    type: official-docs
    accessed: 2026-11-07
  - id: s3
    title: "Salesforce Developer Limits and Allocations Quick Reference: SOQL and SOSL Limits for Search Queries"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_soslsoql.htm
    type: official-docs
    accessed: 2026-11-07
  - id: s4
    title: "Apex Developer Guide: Execution Governors and Limits"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_gov_limits.htm
    type: official-docs
    accessed: 2026-11-07
  - id: s5
    title: "Trailhead: Apex Basics & Database — Write SOSL Queries"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/apex_database/apex_database_sosl
    type: official-learning
    accessed: 2026-11-07
created: 2026-11-07
---

# SOSL

SOSL (Salesforce Object Search Language) is the platform's text-search language. Where SOQL retrieves records from one object with exact field filters, SOSL looks for words across fields on many standard and custom objects at once, and Trailhead likens its behavior to Apache Lucene.[^s5] It can be run inline in Apex, from the Developer Console Query Editor, or through the APIs.[^s5][^s1]

## How it works

A SOSL statement has one mandatory clause, `FIND`, which carries the search text. Every other clause is optional and follows `FIND` in a fixed order: `IN` (the search group), `RETURNING` (which objects and fields come back), several `WITH` filters (division, data category, snippet, network, price book, metadata), `LIMIT`, and `UPDATE TRACKING`/`UPDATE VIEWSTAT` for Salesforce Knowledge article search statistics. `WHERE`, `ORDER BY`, `LIMIT` and `OFFSET` are written inside each object's `RETURNING` specification rather than at the top level.[^s1] Without `RETURNING`, a query returns only the IDs of matching records; in Apex the `RETURNING` clause is required.[^s1]

The search group narrows which fields are scanned: `ALL FIELDS` (the default), `NAME FIELDS`, `EMAIL FIELDS`, `PHONE FIELDS` or `SIDEBAR FIELDS`.[^s1] Search text is split into terms at spaces, punctuation and letter–digit boundaries, matching is case-insensitive, and SOSL matches whole words, so a search for one word also finds longer values containing it. Phrases go in double quotes; `AND`, `OR` and parentheses combine terms; `*` matches zero or more characters and `?` exactly one, in the middle or at the end of a term.[^s5] In Apex the search term is wrapped in single quotes, while the Query Editor and API use curly braces.[^s5]

In Apex, a SOSL query returns a `List<List<SObject>>`: one inner list per object, in the order the objects appear in `RETURNING`, which the developer casts to typed lists such as `Account[]`.[^s5] Spell correction is on by default, and `WITH SNIPPET` returns roughly 300-character excerpts, adjustable from 100 to 500.[^s1]

## Limits and gotchas

Verified against Winter '27:

- **Per transaction in Apex:** 20 SOSL queries, synchronous or asynchronous, and at most 2,000 records returned by a single SOSL query.[^s4]
- **Total results:** 2,000 rows by default from API version 28.0 on (200 in earlier versions), including results from child objects, unless the query sets its own limits.[^s3][^s1]
- **Per-object caps:** a single-object search returns up to 250 records unless a `WHERE` or `ORDER BY` clause is added, which raises it to 2,000; in a multi-object search each object gets the lesser of 2,000 divided by the number of objects, or 250.[^s2]
- **Query length:** a search string over 4,000 characters silently drops logical operators (so `AND` can behave like `OR`), and over 10,000 characters returns no rows; the whole statement is bounded by the org's SOQL statement limit, 100,000 characters by default, after which a `MALFORMED_SEARCH` error is raised.[^s3][^s1]
- **Sharing and crowding:** results honour sharing and permissions, so only users with View All Data see the full set. Broad terms can match more records than the limits allow and crowd out the record a user wants; narrowing the term or searching one object helps.[^s2]

## When to use it (and when not)

Choose SOQL when you know which object holds the data and need precise filters, relationships or aggregates; choose SOSL when the user supplies free text and the match could be in several objects or fields, such as a global "find this name, email or phone" box.[^s5] Because SOSL is word-based and result counts are capped and filtered by sharing, it is a poor fit for exhaustive reporting or exact-match lookups, which SOQL handles better.[^s2][^s5]

## Connections

SOSL **contrasts with** **SOQL**: both are read-only query languages from the same reference, and they are often confused.[^s5] It is **governed by** Apex **governor limits** that cap SOSL calls and rows per transaction,[^s4] and is **used by** **Apex** code that embeds inline searches.[^s5] Its `UPDATE TRACKING`/`VIEWSTAT` and data-category clauses tie it to **Salesforce Knowledge** search,[^s1] and its sharing-aware results depend on the **sharing model**.[^s2] Writing SOSL alongside SOQL is part of the **Platform Developer certification** skill set taught in the Apex database module.[^s5]

## Sources
[^s1]: Salesforce Developers, "SOQL and SOSL Reference: SOSL Syntax". https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-sosl-syntax.html (accessed 2026-11-07)
[^s2]: Salesforce Developers, "SOQL and SOSL Reference: SOSL Limits on Search Results". https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-sosl-limits.html (accessed 2026-11-07)
[^s3]: Salesforce Developers, "Salesforce Developer Limits and Allocations Quick Reference: SOQL and SOSL Limits for Search Queries". https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_soslsoql.htm (accessed 2026-11-07)
[^s4]: Salesforce Developers, "Apex Developer Guide: Execution Governors and Limits". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_gov_limits.htm (accessed 2026-11-07)
[^s5]: Trailhead, "Apex Basics & Database: Write SOSL Queries". https://trailhead.salesforce.com/content/learn/modules/apex_database/apex_database_sosl (accessed 2026-11-07)
