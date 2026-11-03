---
id: kt:data-model-objects
type: Feature
title: Data Model Objects
aliases: [DMO, DMOs, data model object, Data 360 data model objects, Data Cloud data model objects, __dlm objects]
domain: data-cloud-and-ai
summary: >-
  The harmonized objects of the Customer 360 Data Model in Data 360 (formerly Data Cloud): standard or custom
  `__dlm` objects that source data in data lake objects is mapped to, and that identity resolution, insights,
  segmentation, data graphs and Agentforce read instead of the raw source schemas.
release: "Winter '27"
status: current
broader: [kt:data-cloud]
related: [kt:data-architecture, kt:object-relationships]
relations:
  - {predicate: dependsOn, object: kt:data-lake-objects}
  - {predicate: enables, object: kt:identity-resolution}
  - {predicate: enables, object: kt:calculated-insights}
  - {predicate: contrastsWith, object: kt:standard-objects}
  - {predicate: coveredBy, object: kt:data-cloud-consultant-certification}
sources:
  - id: s1
    title: "Object Model in Data 360"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-dev/guide/dc-object-model.html
    type: official-docs
    accessed: 2026-11-03
  - id: s2
    title: "Model Data in Data 360"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-dmo-mapping/guide/c360dm-model-data.html
    type: official-docs
    accessed: 2026-11-03
  - id: s3
    title: "Standard DMOs"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-dmo-mapping/guide/c360dm-si-entity-interface-dmos-introduction.html
    type: official-docs
    accessed: 2026-11-03
  - id: s4
    title: "Salesforce Data Cloud Objects (Object Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_concepts_data_cloud_objects.htm
    type: official-docs
    accessed: 2026-11-03
  - id: s5
    title: "Get to Know Data Model Objects (Customer 360 Data Model for Data Cloud)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/customer-360-data-model-for-customer-data-platform/get-to-know-data-model-objects
    type: official-learning
    accessed: 2026-11-03
  - id: s6
    title: "Map Your Data and Define the Data Model"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/customer-360-audiences-data-ingestion-and-modeling/map-your-data-and-define-the-data-model
    type: official-learning
    accessed: 2026-11-03
created: 2026-11-03
---

# Data Model Objects

**Data model objects (DMOs)** are the harmonized layer of Data 360 (named Data Cloud until October 14, 2025). Ingested
or federated data first lands in **data lake objects (DLOs)**, which keep the shape of the source system; architects
then map DLO fields onto DMOs so that data from many systems is expressed in one standard model, the **Customer 360
Data Model**.[^s2][^s1] A DMO describes a kind of thing or action (an individual, an order, an email open) rather
than a single record, and its fields are the standardized attributes of that thing.[^s5]

## How it works

DMOs do not hold data themselves. They carry metadata pointing to where the data sits in DLOs, and Data 360 APIs and
features read through them. DMO API names end in `__dlm` (DLOs end in `__dlo`), and DMO fields, standard or custom,
end in `__c`.[^s4] When identity resolution merges source records, the output lands in **unified DMOs**, and
calculated insight objects and data graphs are derived from DMO data.[^s1][^s4]

Mapping is done on a canvas with the DLO on one side and the DMO on the other. Salesforce-defined **data bundles**
(for example, the Marketing Cloud Engagement email bundles) arrive with their DMO mappings pre-built, and you can
add or change them afterwards; custom data streams must be mapped by hand.[^s2][^s6] The model is grouped into
**subject areas** such as Party, Engagement, Sales Order, Product and Case.[^s5][^s6] Trailhead lists five DMOs that
every data model must include: Individual, Party Identification, Contact Point Email, Contact Point Phone and
Contact Point Address. Contact details belong on the Contact Point objects rather than on Individual.[^s5][^s6]

Relationships are created when a foreign key is mapped to a primary key. For example, mapping Contact Point Email's
Party field to Individual Id creates a many-to-one link. When no standard DMO fits, you can create a **custom DMO**
from a DLO, and it inherits the DLO's label and API name. A custom DMO is not linked to the rest of the model
automatically, so you must define its relationships yourself, between DMOs rather than between DLOs.[^s6]

## Standard DMOs vs. SSOT DMOs

The developer documentation now describes two kinds of Salesforce-defined DMOs. Older **SSOT DMOs** have an `ssot__`
API prefix. Standard DMOs added after January 2026 use a `_std__dlm` suffix instead. The two kinds are separate
entity types, but they support the same queries, field types and relationships, and they behave the same in every
data space. New fields are added only to standard DMOs. Deploying a newer bundle does not replace an existing `ssot__`
DMO, and you can't change a standard DMO's API name or primary key.[^s3] Salesforce labels these pages a developer
preview that may change, so confirm against your org before building on the newest objects.[^s2][^s3]

## Limits and gotchas

- **Primary key design.** Each DMO's primary key must identify exactly one record. In Trailhead's Contact Point
  Email example, someone with several addresses needs a key that combines the person and the email.[^s5][^s6]
- **Model with intent.** If you only know a city, store it as an Individual attribute, not as a partial Contact
  Point Address.[^s6]
- **Packaging.** Data kits are the recommended way to package DMOs. Managed and unmanaged packages support data
  kits only from the default data space, though a kit can be deployed to any data space.[^s4]
- The documentation pages used here give no numeric DMO limits, so check current Data 360 limits documentation
  rather than assuming one.[^s4]

## When to use it (and when not)

Map to a standard DMO whenever one fits, because bundles, identity resolution and segment attributes are designed
around the standard model. Segments are built from DMO attributes such as order value or email engagement
date.[^s5][^s6] Add custom fields before you add custom objects, and create a custom DMO only for data the standard
model cannot represent, accepting that its relationships are yours to maintain.[^s6] DMOs are not CRM sObjects.
They are high-scale Data 360 objects with their own suffixes and access paths, so don't design them as if they were
Account or Contact records.[^s4]

## Connections

DMOs are a building block of `kt:data-cloud` and a key decision in `kt:data-architecture`. They **depend on**
`kt:data-lake-objects`, which hold the data they point to.[^s1][^s4] They **enable** `kt:identity-resolution`,
which needs the Party Identification and Contact Point mappings, and `kt:calculated-insights`, which are computed from
DMO data.[^s5][^s1] Their primary-key and foreign-key relationships resemble `kt:object-relationships` but work
differently, and DMOs **contrast with** CRM `kt:standard-objects`, the sObjects they are often confused
with.[^s4][^s6] Designing DMO mappings is **covered by** `kt:data-cloud-consultant-certification`.

## Sources

[^s1]: Salesforce Developers, "Object Model in Data 360". https://developer.salesforce.com/docs/data/data-cloud-dev/guide/dc-object-model.html (accessed 2026-11-03)
[^s2]: Salesforce Developers, "Model Data in Data 360". https://developer.salesforce.com/docs/data/data-cloud-dmo-mapping/guide/c360dm-model-data.html (accessed 2026-11-03)
[^s3]: Salesforce Developers, "Standard DMOs". https://developer.salesforce.com/docs/data/data-cloud-dmo-mapping/guide/c360dm-si-entity-interface-dmos-introduction.html (accessed 2026-11-03)
[^s4]: Salesforce Developers, "Salesforce Data Cloud Objects" (Object Reference). https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_concepts_data_cloud_objects.htm (accessed 2026-11-03)
[^s5]: Trailhead, "Get to Know Data Model Objects". https://trailhead.salesforce.com/content/learn/modules/customer-360-data-model-for-customer-data-platform/get-to-know-data-model-objects (accessed 2026-11-03)
[^s6]: Trailhead, "Map Your Data and Define the Data Model". https://trailhead.salesforce.com/content/learn/modules/customer-360-audiences-data-ingestion-and-modeling/map-your-data-and-define-the-data-model (accessed 2026-11-03)
