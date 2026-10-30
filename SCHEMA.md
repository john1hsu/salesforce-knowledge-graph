# Article schema

Each article is one **node** in the graph: `articles/<domain>/<slug>.md`, where the filename equals the id's slug and `<domain>` is a key in `topics/seeds.yaml`.

```markdown
---
id: kt:platform-events                 # stable node id: kt: + lowercase-hyphen slug
type: Feature                          # a class from ontology/ontology.ttl
title: Platform Events
aliases: [platform event, __e object]  # other names; used for duplicate detection
domain: integration                    # a domain key from topics/seeds.yaml
summary: >-                            # 1–2 sentence definition (becomes skos:definition)
  Salesforce's publish/subscribe event messages, defined as custom __e objects and delivered via the event bus.
release: "Winter '27"                  # current Salesforce release the content was verified against
status: current                        # current | beta | pilot | deprecated | retired | concept
broader: [kt:event-driven-architecture]
related: [kt:change-data-capture]
relations:                             # typed edges; predicates must exist in the ontology
  - {predicate: queriedWith, object: kt:pub-sub-api}
  - {predicate: governedBy, object: kt:platform-event-allocations}
  - {predicate: coveredBy, object: kt:integration-architect-certification}
sources:                               # >= 3 total, >= 2 strong, >= 1 official Salesforce
  - id: s1
    title: "Platform Events Developer Guide"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/
    type: official-docs
    accessed: 2026-10-30
created: 2026-10-30
---

# Platform Events

Prose with inline footnote citations after each claim.[^s1]

## How it works
...

## Limits and gotchas
Concrete limits and the release they were checked against.[^s1]

## When to use it (and when not)
Trade-offs vs. alternatives in the graph.[^s2]

## Connections
How this node relates to its neighbours, in prose, with citations.[^s3]

## Sources
[^s1]: Salesforce, "Platform Events Developer Guide". https://developer.salesforce.com/... (accessed 2026-10-30)
```

## Rules enforced by `scripts/kg.py check`

- Required fields: `id, type, title, domain, summary, sources, created, release, status`.
- `release` looks like `Winter '27`; `status` is one of the allowed values; a `deprecated`/`retired` node must have a `replacedBy` relation (its migration path).
- `type` must be a class, and every `relations.predicate` a property, in `ontology/ontology.ttl`.
- Every edge target is a `kt:` id. Targets with no article yet become **frontier** nodes (`graph/frontier.md`).
- Citations: at least 3 sources; at least 2 of a strong type; at least 1 official Salesforce source (`official-docs` or `official-learning`) unless the node is an `ExternalConcept`; https only; no duplicate URLs; every source cited in the body and defined in `## Sources`; every substantive paragraph cited.
- Body of at least 350 words.
- Uniqueness: no duplicate ids, titles or aliases; no near-paraphrase titles; no bodies that overlap another article above the similarity threshold.

## Source types

| type | strong? | examples |
|---|---|---|
| official-docs | yes | help.salesforce.com, developer.salesforce.com docs, architect.salesforce.com (Well-Architected, decision guides), release notes, security.salesforce.com, compliance.salesforce.com |
| official-learning | yes | trailhead.salesforce.com modules, certification exam guides |
| official-blog | yes | developer.salesforce.com/blogs, admin.salesforce.com/blog, engineering.salesforce.com |
| standards-body | yes | IETF RFCs, OASIS (SAML), NIST |
| government | yes | fedramp.gov marketplace, GSA, DoD DISA |
| peer-reviewed / academic / textbook | yes | papers, university material |
| partner | no | recognized SI and ISV write-ups |
| community | no | Salesforce Stack Exchange, MVP blogs |
| news | no | reputable press, for announcements only |

Never cite Wikipedia, content farms, exam-dump sites, or AI-generated pages.
