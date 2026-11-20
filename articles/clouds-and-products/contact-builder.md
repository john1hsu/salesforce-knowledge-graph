---
id: kt:contact-builder
type: Feature
title: Contact Builder
aliases: [Marketing Cloud Contact Builder, SFMC Contact Builder]
domain: clouds-and-products
summary: >-
  The Marketing Cloud Engagement application that holds the account's contact data model: it stores contacts
  and their channel addresses under one contact key, and links data extensions into attribute groups and
  populations that Journey Builder and the messaging channels use.
release: "Winter '27"
status: current
broader: [kt:marketing-cloud-engagement]
related: [kt:journey-builder, kt:automation-studio, kt:marketing-cloud-connect]
relations:
  - {predicate: partOf, object: kt:marketing-cloud-engagement}
  - {predicate: hasPart, object: kt:data-extensions}
  - {predicate: consumedBy, object: kt:journey-builder}
  - {predicate: integratesWith, object: kt:marketing-cloud-connect}
sources:
  - id: s1
    title: "Understand Contacts and Contact Model Relationships (Marketing Cloud Engagement Contact Management)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-contact-management/understand-contacts-and-contact-model-relationships
    type: official-learning
    accessed: 2026-11-20
  - id: s2
    title: "Organize Your Data (Contact Builder Implementation Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/contact-builder-implementation-basics/organize-data
    type: official-learning
    accessed: 2026-11-20
  - id: s3
    title: "Configure Contact Models (Marketing Cloud Engagement Contact Management)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-contact-management/configure-contact-models
    type: official-learning
    accessed: 2026-11-20
  - id: s4
    title: "Design Your Data Model (Marketing Cloud Engagement Data Management)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-data-management/design-your-mc-data-model
    type: official-learning
    accessed: 2026-11-20
  - id: s5
    title: "Build Your Data Model (Marketing Cloud Engagement Data Management)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-data-management/build-your-data-model
    type: official-learning
    accessed: 2026-11-20
  - id: s6
    title: "Manage Contact Data (Marketing Cloud Engagement Contact Management)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-contact-management/manage-contact-data
    type: official-learning
    accessed: 2026-11-20
created: 2026-11-20
---

# Contact Builder

Contact Builder is the Marketing Cloud Engagement application that manages contact data for every Marketing Cloud channel. Trailhead describes it as working like a relational database: it lets marketers define how contact information is stored, related and reused across email, mobile and journeys.[^s1] A **contact** is anyone the account messages. A **subscriber** is a contact who has opted in to a particular channel, so every subscriber is a contact but not every contact is a subscriber. Contacts brought in from Sales or Service Cloud, or through REST API imports, show up in All Contacts without ever being subscribers.[^s1]

## Components

Contact Builder groups its work into a handful of tools: **All Contacts**, **Data Designer**, **Data Extensions**, **Imports** and **Contacts Configuration**. Some modules also list **Data Sources**.[^s2][^s1]

- **All Contacts** gives each contact one record, with its interactions, subscriptions and channel addresses: email addresses, mobile numbers and push device IDs.[^s1]
- **Data extensions** are the tables that hold contact data. Each row is a contact, each column an attribute, and each cell a value.[^s2]
- **Data Designer** is where attributes are defined, grouped and related to the contact. It has tabs for Data Sources, Data Extensions, Attribute Groups and Populations.[^s3][^s4]
- **Contacts Configuration** holds account-level settings, including whether Contact Delete is enabled and how long the suppression period lasts.[^s6]

Data Designer has its own vocabulary. An **attribute group** is a data model, an **attribute set** is a table (data extension) within it, and an **attribute** is a field.[^s2] Attribute groups join tables on a shared field, for example a customers table linked to a purchases table, and connect to the contact through the Contact Key.[^s3] Other apps, such as MobileConnect, can reuse them.[^s2] **Populations** are large master subsets of contacts that share a theme, such as drivers versus riders. Each one is stored in its own data extension and is used by Journey Builder, MobileConnect and MobilePush.[^s2][^s3]

## The contact key

The **Contact Key** is the unique identifier that ties a person's channel addresses together. Without it, the same person reached by email and by SMS counts as two contacts. Salesforce also assigns a backend Contact ID.[^s1] The Email Studio **Subscriber Key** becomes the Contact Key in Contact Builder. It has to be consistent across the account and present in every sendable data extension. Keying on Subscriber Key rather than email address lets one address belong to several records, such as family members who share an inbox.[^s1]

Trailhead's guidance for choosing the key is to reuse the existing subscriber key, use a value unrelated to any single channel, and use a value that won't change as the customer behaves. With Marketing Cloud Connect it recommends the CRM Lead or Contact ID.[^s4] Link attribute groups and populations on the Contact Key, not on an email field. If email really is the join, store it in a separate text attribute and link on that.[^s3]

## Building a data model

The data-management module sets out a planning sequence. List every data source and pick a database of record, the source of truth for opt-in status. Move in only the data you need for segmentation or personalization, store sensitive values such as birthdate only when essential, and label each field's type before creating the data extensions.[^s4] For each data extension, check the sendable flag, retention, data types and lengths, primary key, and a send relationship that maps to the contact key.[^s5]

In Data Designer you create an attribute group and use **Link Data Extensions** to attach each table. Linked fields must share a data type. Cardinality can be one-to-one, one-to-many or many-to-many, but Trailhead notes that many-to-many isn't used with contacts. Its example links a customer one-to-one to a customer table and one-to-many to purchases.[^s5] Map subscriber data to the contact model before importing, so the subscriber's key matches the contact's key, and deduplicate and validate the data first.[^s5]

## Limits and gotchas

- Trailhead advises against creating more than three populations per account, for performance reasons.[^s2][^s3]
- In current Journey Builder, populations are usually unnecessary. Keep them for complex queries, field-level encryption or API entry sources.[^s3]
- Data flows one way: Email Studio data appears in Contact Builder, but Contact Builder data doesn't appear in Email Studio.[^s1]
- You can apply a retention policy to a data extension with fewer than 100 million records. The default policy deletes unused data extensions after 6 months, and cleanup runs nightly.[^s6]
- Contact deletion is a hard delete from the account and every sendable data extension, and it can't be undone.[^s6]
- Deleted contacts are first suppressed for a 2-day default period, which is configurable. Only sendable data extensions are cleaned, so subscriber data in non-sendable ones has to be removed by hand.[^s6]
- Deletion also loses tracking history. Trailhead suggests unsubscribing contacts or moving them to another journey instead, and keeping a deletion log so data sources don't re-add them.[^s6]

## When to use it (and when not)

Use Contact Builder to design the relational model behind Marketing Cloud Engagement messaging: which tables describe a contact, how they join, and which key identifies the person across channels.[^s3][^s4] Plan the model before connecting data, and bring in only the contacts you will actually message.[^s3] Journey logic itself belongs in Journey Builder, which reads populations and contact data from this model. Reach for a population only when a journey needs a large, specific segment or contacts that aren't yet in All Contacts.[^s2][^s3]

## Connections

Contact Builder is **part of** `kt:marketing-cloud-engagement` and **has part** `kt:data-extensions`, the tables its attribute groups link together.[^s1][^s2] It is **consumed by** `kt:journey-builder`, whose populations and contact data come from the Contact Builder model.[^s2] It **integrates with** `kt:marketing-cloud-connect`: CRM contacts flow into All Contacts, and the CRM Lead or Contact ID is the recommended contact key when the connector is used.[^s1][^s4] It relates to `kt:automation-studio`, the product's scheduled data-processing app. Contact Builder's own Imports tool handles loading files into data extensions directly.[^s2]

## Sources
[^s1]: Trailhead, "Understand Contacts and Contact Model Relationships". https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-contact-management/understand-contacts-and-contact-model-relationships (accessed 2026-11-20)
[^s2]: Trailhead, "Organize Your Data". https://trailhead.salesforce.com/content/learn/modules/contact-builder-implementation-basics/organize-data (accessed 2026-11-20)
[^s3]: Trailhead, "Configure Contact Models". https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-contact-management/configure-contact-models (accessed 2026-11-20)
[^s4]: Trailhead, "Design Your Data Model". https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-data-management/design-your-mc-data-model (accessed 2026-11-20)
[^s5]: Trailhead, "Build Your Data Model". https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-data-management/build-your-data-model (accessed 2026-11-20)
[^s6]: Trailhead, "Manage Contact Data". https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-contact-management/manage-contact-data (accessed 2026-11-20)
