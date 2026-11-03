---
id: kt:identity-resolution
type: Feature
title: Identity Resolution
aliases: [Data 360 identity resolution, Data Cloud identity resolution, identity resolution ruleset, profile unification]
domain: data-cloud-and-ai
summary: >-
  The Data 360 (formerly Data Cloud) feature that applies rulesets of match rules and reconciliation rules to source
  Individual or Account records, linking records that describe the same person or business into unified profiles
  that feed segmentation, activation, calculated insights and Agentforce.
release: "Winter '27"
status: current
broader: [kt:data-cloud]
related: [kt:data-architecture]
relations:
  - {predicate: dependsOn, object: kt:data-model-objects}
  - {predicate: enables, object: kt:calculated-insights}
  - {predicate: enables, object: kt:agentforce}
  - {predicate: contrastsWith, object: kt:duplicate-management}
  - {predicate: coveredBy, object: kt:data-cloud-consultant-certification}
sources:
  - id: s1
    title: "Identity Resolution Terminology"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=data.c360_a_identity_resolution_terms.htm
    type: official-docs
    accessed: 2026-11-03
  - id: s2
    title: "Identity Resolution Match Rule Terminology"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=data.c360_a_identity_resolution_match_rule_terms.htm
    type: official-docs
    accessed: 2026-11-03
  - id: s3
    title: "Configure Identity Resolution Rulesets (Data and Identity in Data Cloud)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-and-identity-in-salesforce-cdp/configure-identity-resolution-rules
    type: official-learning
    accessed: 2026-11-03
  - id: s4
    title: "Unify Your Data (Explore Data Cloud Core Functionality)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/explore-data-cloud-core-functionality/unify-your-data
    type: official-learning
    accessed: 2026-11-03
  - id: s5
    title: "Data Cloud and Identity Resolution"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/10/data-cloud-and-identity-resolution
    type: official-blog
    accessed: 2026-11-03
  - id: s6
    title: "Real-Time Identity Resolution"
    publisher: Salesforce Blog
    url: https://www.salesforce.com/blog/real-time-identity-resolution/
    type: official-blog
    accessed: 2026-11-03
created: 2026-11-03
---

# Identity Resolution

**Identity resolution** is the step in Data 360 (named Data Cloud until October 2025) that finds the same person or
business across disconnected sources and links their records into one unified profile.[^s5] Each source system
usually identifies a customer with its own primary key, so a CRM Contact, an e-commerce guest record and a loyalty
row for one person never share an ID; identity resolution relies on configurable matching instead of shared keys.[^s5]

## How it works

The unit of configuration is a **ruleset**: a container of match rules and reconciliation rules that says how
multiple data sources are linked into a unified profile.[^s1] A ruleset is built on either the Individual data model
object, producing unified individuals from attributes such as names, or the Account DMO, producing unified accounts
from business name, location and type.[^s1] Rulesets are created on the Identity Resolutions tab, where you choose
the primary DMO, a name and an optional ruleset ID.[^s3]

- **Match rules** decide which source records link. A record only has to satisfy one rule in the ruleset, but it
  must meet every criterion inside that rule, so adding rules raises the consolidation rate while adding criteria
  to a rule lowers it.[^s2]
- **Match methods** transform values before comparison. Exact and Exact Normalized are strict; fuzzy methods are
  more permissive; you can select up to five methods, and not every method fits every object and field.[^s2] A
  typical rule set pairs a fuzzy first name with an exact normalized email, phone or address, or with an exact
  party identifier such as a loyalty number.[^s3]
- **Reconciliation rules** choose which value fills a single-value field, such as First Name, when matched sources
  disagree: the most recent value, the most frequent value, or a ranked source priority.[^s4] Contact points are
  handled differently: unified contact point objects keep every unique email, phone or address from all sources.[^s1]

A **ruleset job** processes source profiles using the data mappings and both rule types; it runs at least once a
day per ruleset and is skipped when nothing has changed.[^s1] Output lands in three object families: unified
profile objects (such as Unified Individual) with summary values, unified contact point objects, and **unified
link objects** that bridge each unified profile back to its source records.[^s1][^s4]

## Limits and gotchas

- Data mapping comes first. Source data must be mapped to the Individual and contact point DMOs before rulesets
  are built, and unmapped required fields show as warnings in the ruleset.[^s5][^s4]
- The Trailhead module states an org can create up to two identity resolution rulesets, often used to A/B test a
  candidate configuration against the live one, and that a ruleset ID is at most four characters and cannot be
  changed once set.[^s3]
- After the first publish, unified profiles appear within 24 hours, and later rule changes are processed daily.[^s3]
  Hands-on exercises switch off automatic runs to control job costs.[^s4]
- **Real-time** matching for Web and Mobile SDK data evaluates in milliseconds but treats fuzzy criteria as
  exact; other sources still wait for batch resolution and Data Graph rebuilds, which can take hours.[^s6] In
  real-time matching, phone and email criteria use Exact Normalized and other criteria use Exact.[^s2]
- Unified profiles are only as reliable as their inputs: know which source holds the freshest data before writing
  match and reconciliation rules, and monitor consolidation rates over time.[^s3]

## When to use it (and when not)

Use identity resolution when profiles must be assembled from several systems that cannot share a key, for
segmentation, activation, calculated insights or reporting on unified customers.[^s1][^s5] Verify results by
querying Individual, Unified Link Individual and Unified Individual together: two source IDs for one person should
return the same unified ID.[^s5] It does not merge or delete the source records themselves; unified link objects
point back to them instead.[^s1] Cleaning duplicates inside one CRM org is a separate job.

## Connections

Identity resolution is a part of `kt:data-cloud` and **depends on** `kt:data-model-objects`, because rulesets act
on mapped Individual, Account and contact point DMOs.[^s5][^s1] It **enables** `kt:calculated-insights`, since
unified link objects are required for insights on unified profiles,[^s1] and it **enables** `kt:agentforce` by
giving agents a unified customer profile during a conversation.[^s6] It **contrasts with**
`kt:duplicate-management`, which works on records inside one org rather than linking across sources. It is
**covered by** `kt:data-cloud-consultant-certification`, and it is a core building block of `kt:data-architecture`
decisions about how a customer's unified profile is assembled from source systems.[^s3][^s5]

## Sources

[^s1]: Salesforce Help, "Identity Resolution Terminology". https://help.salesforce.com/apex/HTViewHelpDoc?id=data.c360_a_identity_resolution_terms.htm (accessed 2026-11-03)
[^s2]: Salesforce Help, "Identity Resolution Match Rule Terminology". https://help.salesforce.com/apex/HTViewHelpDoc?id=data.c360_a_identity_resolution_match_rule_terms.htm (accessed 2026-11-03)
[^s3]: Trailhead, "Configure Identity Resolution Rulesets". https://trailhead.salesforce.com/content/learn/modules/data-and-identity-in-salesforce-cdp/configure-identity-resolution-rules (accessed 2026-11-03)
[^s4]: Trailhead, "Unify Your Data". https://trailhead.salesforce.com/content/learn/projects/explore-data-cloud-core-functionality/unify-your-data (accessed 2026-11-03)
[^s5]: Salesforce Developers Blog, "Data Cloud and Identity Resolution". https://developer.salesforce.com/blogs/2024/10/data-cloud-and-identity-resolution (accessed 2026-11-03)
[^s6]: Salesforce Blog, "Real-Time Identity Resolution". https://www.salesforce.com/blog/real-time-identity-resolution/ (accessed 2026-11-03)
