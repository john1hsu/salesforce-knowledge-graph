---
id: kt:data-architecture
type: Concept
title: Data Architecture
aliases: [Salesforce data architecture, data architecture and management, enterprise data architecture on Salesforce]
domain: architecture-practice
summary: >-
  The architectural discipline that decides how data is modeled, where it lives, how it moves and how it is
  governed across a Salesforce org and the systems around it, so the solution stays scalable, performant and
  trustworthy as volumes grow.
release: "Winter '27"
status: concept
broader: [kt:well-architected-framework]
related: [kt:large-data-volumes, kt:data-skew, kt:data-residency, kt:data-cloud]
relations:
  - {predicate: hasPart, object: kt:data-migration-strategy}
  - {predicate: hasPart, object: kt:archiving-strategy}
  - {predicate: dependsOn, object: kt:object-relationships}
  - {predicate: configuredVia, object: kt:schema-builder}
  - {predicate: coveredBy, object: kt:platform-data-architect-certification}
  - {predicate: usedBy, object: kt:salesforce-architect}
sources:
  - id: s1
    title: "Data Integration Decision Guide"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/decision-guides/data-integration
    type: official-docs
    accessed: 2026-11-02
  - id: s2
    title: "General Best Practices (Best Practices for Deployments with Large Data Volumes)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-best-practices-general.md
    type: official-docs
    accessed: 2026-11-02
  - id: s3
    title: "The Salesforce Data Model Gallery"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/data-models
    type: official-docs
    accessed: 2026-11-02
  - id: s4
    title: "Work with Schema Builder (Data Modeling)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data_modeling/schema_builder
    type: official-learning
    accessed: 2026-11-02
  - id: s5
    title: "Salesforce Certified Platform Data Architect"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/it/credentials/platformdataarchitect
    type: official-learning
    accessed: 2026-11-02
  - id: s6
    title: "Get Started with Data 360 and Integration"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/fundamentals/guide/get-started-data-360.html
    type: official-docs
    accessed: 2026-11-02
created: 2026-11-02
---

# Data Architecture

Data architecture on Salesforce is the set of design decisions about the shape of the data model, where each kind of data is stored, how it flows between Salesforce and other systems, and how it is kept healthy over its lifetime. Salesforce treats it as a distinct architect specialty: the Platform Data Architect credential is aimed at people who design sound, scalable and high-performing enterprise data management solutions on the platform.[^s5] In this graph it is the umbrella over migration, archiving, large-data-volume design, residency and integration choices, each of which has its own node.

## The questions it answers

A data architecture for a Salesforce programme typically has to settle four things:

- **Model.** Which standard objects are reused, which custom objects are added, and how they relate. Salesforce publishes a Data Model Gallery of diagrams for Sales, Service, Platform, Data 360, industry and public-sector products, each listing its entities, plus a separate notation guide for reading them; architects use these as a starting point before inventing schema.[^s3] Note that the gallery says product names are now Agentforce-branded (Sales Cloud is Agentforce Sales) while some diagrams still carry the older Cloud names.[^s3]
- **Location.** Whether data must physically reside in Salesforce at all. The Architects data-integration guide asks every project to name its source of truth, and its default stance is to minimise replication: if records do not need to live in the org, access them in place through virtualization such as Salesforce Connect instead of copying them.[^s1]
- **Movement.** Which tools carry data in and out. The same guide weighs the existing ESB or ETL estate, timing needs, team skills, maintainability, volume and platform limits, and it warns against building an integration strategy on stewardship tools such as Data Loader or the Data Import Wizard.[^s1]
- **Volume and lifecycle.** How the model behaves at scale and what happens to old records, covered by the large-data-volume and archiving guidance.[^s2]

## Designing for scale

Salesforce's general large-data-volume practices are mostly data-architecture rules rather than tuning tricks. They advise keeping any one user from owning more than 10,000 records and keeping any one parent from having more than 10,000 children, creating several placeholder parents when children have no natural parent (contacts without accounts, for example).[^s2] They also recommend data tiering: spreading data across several objects and fetching related data on demand from another object or an external store.[^s2] These rules exist because ownership and parent concentration drive sharing computation and locking cost, so they need to be built into the model rather than discovered after go-live.

## Tooling

Schema Builder in Setup gives a visual canvas of selected objects and their relationships. Architects can create objects and add relationship, formula and standard fields by dragging elements onto the canvas, and the results also appear in Object Manager; rearranging the layout changes only the picture, not the schema.[^s4] It is useful for explaining a model to stakeholders and for showing how data moves through the system.[^s4]

## Beyond the core org

Modern Salesforce data architecture extends past the transactional org. The Architects fundamentals track pairs Data 360 Architecture with Integration Patterns and recommends reading them in that order; it lists Data 360 design principles including openness, interoperability, multi-model storage, metadata-driven design and governance, and describes federation with Snowflake, Databricks, BigQuery and Redshift instead of duplicating those investments.[^s6] The data-integration guide likewise points to Data 360 for harmonising data from many sources and Data Cloud One for sharing data across orgs without copying it.[^s1]

## When to invest in it

Every implementation makes data-architecture decisions, but they deserve explicit design when the org will hold large volumes, when several systems claim the same customer, when data is subject to location rules, or when multiple orgs must share records.[^s1][^s2] The common failure mode is a model that works in a sandbox but concentrates ownership or children on a few records in production, producing the skew that the volume guidance warns about.[^s2]

## Connections

Data architecture sits within the **Salesforce Well-Architected Framework**, whose resources include the data-integration and Data 360 guides.[^s1][^s6] It **has parts** in **data migration strategy** and **archiving strategy**, which govern how data enters and leaves the org, and it relates to **large data volumes** and **data skew**, whose ownership and parent limits it must respect.[^s2] It **depends on** sound **object relationships** and is **configured via** tools such as **Schema Builder**.[^s4] **Data residency** constrains its location decisions, and **Data 360** (`kt:data-cloud`) extends it to harmonised and federated data.[^s1][^s6] The topic is **covered by** the **Platform Data Architect certification** and is a core responsibility of the **Salesforce architect** role.[^s5]

## Sources
[^s1]: Salesforce Architects, "Data Integration Decision Guide". https://architect.salesforce.com/decision-guides/data-integration (accessed 2026-11-02)
[^s2]: Salesforce, "General Best Practices", Best Practices for Deployments with Large Data Volumes. https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-best-practices-general.md (accessed 2026-11-02)
[^s3]: Salesforce, "The Salesforce Data Model Gallery". https://developer.salesforce.com/docs/platform/data-models (accessed 2026-11-02)
[^s4]: Salesforce Trailhead, "Work with Schema Builder", Data Modeling. https://trailhead.salesforce.com/content/learn/modules/data_modeling/schema_builder (accessed 2026-11-02)
[^s5]: Salesforce Trailhead, "Salesforce Certified Platform Data Architect". https://trailhead.salesforce.com/it/credentials/platformdataarchitect (accessed 2026-11-02)
[^s6]: Salesforce Architects, "Get Started with Data 360 and Integration". https://architect.salesforce.com/docs/architect/fundamentals/guide/get-started-data-360.html (accessed 2026-11-02)
