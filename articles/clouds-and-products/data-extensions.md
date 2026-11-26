---
id: kt:data-extensions
type: Feature
title: Data Extensions
aliases: [Marketing Cloud data extension, SFMC data extension, sendable data extension]
domain: clouds-and-products
summary: >-
  The tables that store contact and reference data in Marketing Cloud Engagement. Each data extension is
  sendable (mapped to a subscriber through a send relationship) or non-sendable, and is built as a standard,
  filtered or random table that queries, imports, journeys and sends read from.
release: "Winter '27"
status: current
broader: [kt:marketing-cloud-engagement]
related: [kt:contact-builder, kt:automation-studio, kt:journey-builder, kt:marketing-cloud-sql, kt:custom-objects]
relations:
  - {predicate: partOf, object: kt:contact-builder}
  - {predicate: consumedBy, object: kt:journey-builder}
  - {predicate: consumedBy, object: kt:automation-studio}
  - {predicate: queriedWith, object: kt:marketing-cloud-sql}
sources:
  - id: s1
    title: "Learn About Data Extensions (Marketing Cloud Engagement Contact Management)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-contact-management/learn-about-data-extensions
    type: official-learning
    accessed: 2026-11-26
  - id: s2
    title: "Clean Your Data (Marketing Cloud Engagement Account Optimization)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-account-optimization/clean-your-data
    type: official-learning
    accessed: 2026-11-26
  - id: s3
    title: "Manage Data in Data Extensions (Marketing Cloud Engagement APIs)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/managing_data_in_data_extensions.html
    type: official-docs
    accessed: 2026-11-26
  - id: s4
    title: "Create a Data Extension (Marketing Cloud Engagement APIs)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/creating_a_data_extension_using_web_service_api.htm
    type: official-docs
    accessed: 2026-11-26
created: 2026-11-26
---

# Data Extensions

A data extension is the basic storage unit of Marketing Cloud Engagement: a table of fields holding data about contacts or about anything a marketer needs to reference. A data extension can stand alone or be related to other data extensions. It can be queried, used to pull information, or used to send to a subset of subscribers.[^s1] Data arrives by manual import, through Automation Studio, or through the Marketing Cloud Engagement API. Data extensions appear in both Contact Builder and Email Studio, but permissions and sharing are managed in Email Studio.[^s1]

## Kinds of data extension

Trailhead names three construction types. A **standard** data extension has a custom set of fields. A **filtered** data extension is a segment drawn from an existing one by criteria. A **random** data extension takes a random selection of subscribers from a source table.[^s1] The split function in Email Studio can divide a source into as many as 12 random groups at once, which is useful for test cells.[^s1]

Separately, every data extension is either **sendable** or **non-sendable**. A sendable one has a send relationship that maps a field to the subscriber, and contacts sent to from it are added to All Contacts. A non-sendable one holds reference data such as orders, product catalogs, airport codes or weather.[^s1] **Shared** data extensions live in shared folders so several business units can use one table. The owner sets retention, the actions others may take, the sharing window and which business units have access.[^s1] Trailhead recommends sharing a table rather than keeping duplicate copies in each business unit.[^s2]

## Fields, keys and sizing

Fields have explicit types. The API samples include Text, EmailAddress, Number, Decimal (with precision and scale), Date, Boolean, Phone and Locale. Each field can be marked as a primary key, required or nullable, and text fields take a maximum length.[^s4] A sendable data extension should carry only one email address field, and the Subscriber Key should be stored as text even when its values are numeric.[^s1][^s2]

Trailhead's hygiene guidance is to size each column to what it needs: a two-letter state code should be 2 characters, not the default 50. Use the right type, such as Date rather than Text for a birthday.[^s2] Keep a table's total byte size, the sum of its column lengths, under 8,000. Twenty 100-character columns fit, but eight 1,000-character columns do not.[^s2] There is no fixed limit on how many data extensions an account can hold, but an excessive number slows both the UI and the API.[^s2]

Give a primary key to any data extension that is updated or appended to. Imports and queries that don't overwrite the table need one to match rows.[^s2] Good keys include Subscriber_Key for sendable tables, or a product ID or postal code for reference tables.[^s2] Don't put primary keys on triggered-send data extensions, because a retried send could then deliver the same data twice.[^s2] The developer guide also warns against Date fields as primary keys, since SOAP rounds dates to the second, and it recommends external keys of 36 characters or fewer.[^s4]

## Retention

Retention can be set when a data extension is created. Trailhead's advice is to let data expire once it is no longer needed and to remove unneeded tables automatically.[^s2] The API supports **row-based** retention, which deletes individual rows older than the period (the sample uses 48 days). It also supports **object-based** retention, which can reset the clock on each import and act on the whole table at the end of the period.[^s4]

## Working with rows through the API

The SOAP API treats a row as a `DataExtensionObject`. A create request supplies the table's customer key and name/value properties. A retrieve request pages through results, continuing while the status reports more data available.[^s3] Updates and deletes address rows by primary key, so the data extension must have at least one primary column. When there are several, every key must be supplied to delete a row. Using the UpdateAdd save action gives upsert behaviour: existing rows are updated and new ones inserted.[^s3] Responses report an overall status and can carry key or value errors per row.[^s3]

## When to use it (and when not)

Use a sendable data extension as the audience for a send or journey, and non-sendable ones for lookups that personalize content or feed queries.[^s1] Prefer filtered or random data extensions, or query-driven tables, over hand-maintained copies of the same audience. For daily loads, add and update deltas rather than overwriting the whole table.[^s2] Keep each table narrow and purpose-built: size columns tightly, share one copy across business units, and let retention clear data that is no longer used.[^s2]

## Connections

Data extensions are **part of** `kt:contact-builder`, where Data Designer links them into attribute groups tied to the contact record, and they sit under `kt:marketing-cloud-engagement`.[^s1] They are **consumed by** `kt:automation-studio`, which automates their imports, and by `kt:journey-builder`, one of the messaging tools that sends to the subscribers a sendable data extension maps.[^s1] They are **queried with** `kt:marketing-cloud-sql`, since Trailhead lists queries among a data extension's core uses, alongside the API row operations described above.[^s1][^s3] They relate to `kt:custom-objects` as Marketing Cloud's equivalent of a custom table, but they follow their own keying, sendability and retention rules.[^s3][^s4]

## Sources
[^s1]: Trailhead, "Learn About Data Extensions". https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-contact-management/learn-about-data-extensions (accessed 2026-11-26)
[^s2]: Trailhead, "Clean Your Data". https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-account-optimization/clean-your-data (accessed 2026-11-26)
[^s3]: Salesforce Developers, "Manage Data in Data Extensions". https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/managing_data_in_data_extensions.html (accessed 2026-11-26)
[^s4]: Salesforce Developers, "Create a Data Extension". https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/creating_a_data_extension_using_web_service_api.htm (accessed 2026-11-26)
