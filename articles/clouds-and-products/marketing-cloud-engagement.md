---
id: kt:marketing-cloud-engagement
type: Product
title: Marketing Cloud Engagement
aliases: [ExactTarget, ExactTarget Marketing Cloud, Salesforce Marketing Cloud, SFMC, MCE]
domain: clouds-and-products
summary: >-
  Salesforce's B2C cross-channel marketing platform (formerly ExactTarget), which runs outside the core
  Salesforce platform and combines Contact Builder data extensions, Email and Mobile Studio messaging,
  Automation Studio and Journey Builder orchestration, connected to CRM through Marketing Cloud Connect.
release: "Winter '27"
status: current
broader: [kt:salesforce-marketing-solutions]
related: [kt:sales-cloud, kt:service-cloud, kt:data-cloud, kt:marketing-cloud-account-engagement]
relations:
  - {predicate: hasPart, object: kt:journey-builder}
  - {predicate: hasPart, object: kt:automation-studio}
  - {predicate: hasPart, object: kt:contact-builder}
  - {predicate: integratesWith, object: kt:marketing-cloud-connect}
  - {predicate: alternativeTo, object: kt:marketing-cloud-next}
sources:
  - id: s1
    title: "Discover Salesforce Marketing Solutions (Salesforce Marketing Cloud Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/ko/content/learn/modules/salesforce-marketing-cloud-quick-look/discover-salesforce-marketing-solutions
    type: official-learning
    accessed: 2026-11-03
  - id: s2
    title: "Get Started with Journey Builder (Journey Builder Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/content/learn/modules/journey-builder-basics/get-started-with-journey-builder
    type: official-learning
    accessed: 2026-11-03
  - id: s3
    title: "Learn About Data Extensions (Marketing Cloud Engagement Contact Management)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/content/learn/modules/marketing-cloud-contact-management/learn-about-data-extensions
    type: official-learning
    accessed: 2026-11-03
  - id: s4
    title: "Explore Synchronized Data Sources (Marketing Cloud Engagement Contact Management)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-contact-management/explore-synchronized-data-sources
    type: official-learning
    accessed: 2026-11-03
  - id: s5
    title: "Understand Contacts and Contact Model Relationships"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/pt-BR/content/learn/modules/marketing-cloud-contact-management/understand-contacts-and-contact-model-relationships
    type: official-learning
    accessed: 2026-11-03
  - id: s6
    title: "Automation Studio and SQL in Marketing Cloud"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2023/02/automation-studio-and-sql-in-marketing-cloud
    type: official-blog
    accessed: 2026-11-03
  - id: s7
    title: "Get Started with Marketing Cloud Next Channel Marketing"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/channel-marketing-fundamentals-for-marketing-cloud-next/get-started-with-marketing-cloud-next-channel-marketing
    type: official-learning
    accessed: 2026-11-03
created: 2026-11-03
---

# Marketing Cloud Engagement

Marketing Cloud Engagement is Salesforce's cross-channel marketing platform for building personalized customer journeys across the customer lifecycle. It descends from the ExactTarget acquisition and was long sold simply as "Marketing Cloud"; Salesforce now distinguishes it from sibling products such as Marketing Cloud Account Engagement (formerly Pardot), Personalization (formerly Interaction Studio) and Intelligence (formerly Datorama).[^s1] Unlike Sales Cloud or Service Cloud, it runs on a separate marketing platform that connects to Salesforce CRM through a managed package, and its focus is primarily B2C.[^s7]

## How it works

The product is a set of "studios" and "builders" that share one contact database. **Contact Builder** stores contacts relationally: a contact is anyone you can message on any channel, and every subscriber is a contact but not every contact is a subscriber.[^s5] The **contact key** (called the subscriber key in Email Studio) is the identifier that ties one person together across email, mobile and other channels, so it must be assigned consistently and included in every sendable data extension.[^s5]

Data lives mainly in **data extensions**, which are tables of fields that can stand alone or relate to each other. Standard, filtered and random data extensions exist; a *sendable* data extension is mapped to a subscriber through a send relationship, while a non-sendable one holds reference data such as orders or products used for personalization.[^s3] Trailhead recommends storing the subscriber key as text and keeping a single email-address field in a sendable data extension.[^s3]

**Automation Studio** runs scheduled batch work, notably SQL query activities that read data extensions and system data views (such as sends, opens and subscribers) and write the result to a target data extension.[^s6] **Journey Builder** orchestrates multi-step, multi-channel campaigns such as welcome series, abandoned-cart re-engagement and renewal reminders. Each journey starts from an entry source (a data extension, API event, CloudPage or Salesforce data, for example) and then moves contacts through message, advertising, flow-control (wait, split, join) and data-update activities. It relies on content and audiences from Email Studio, Mobile Studio, Advertising Studio, Content Builder and Contact Builder.[^s2]

## CRM integration

**Marketing Cloud Connect** links Marketing Cloud Engagement to a Salesforce org. With synchronized data sources, you pick Salesforce objects and fields, and each object becomes a data extension named with a `_Salesforce` suffix that refreshes on an interval you set in minutes or hours.[^s4] Journey Builder also gains a set of Sales and Service Cloud activities (for example, creating or updating CRM records) only when the connector is installed.[^s2]

## Limits and gotchas

- Every synchronized contact or lead counts as a contact in Contact Builder, even if you never message it.[^s4]
- A synchronized data source can't be deleted once started, only paused. Synced data extensions sit at the top level of an Enterprise account and can't be moved into shared folders, so you must copy them with a query or filter to share them across business units.[^s4]
- A SQL query activity is deactivated automatically after 24 consecutive failures. Salesforce also advises limiting queries to about six months of data, staggering hourly automations, and not importing into and querying the same data extension in overlapping steps.[^s6]
- Data extensions don't usually store subscriber status, so you must join to list or subscriber data views to respect opt-outs.[^s6]

## When to use it (and when not)

Choose Marketing Cloud Engagement for high-volume B2C messaging with mature SQL segmentation, AMPscript/SSJS content and Journey Builder orchestration. Salesforce's newer **Marketing Cloud Next** is built directly on the Salesforce Platform with Data 360 as its data layer, Flow-based orchestration and B2B, B2C and hybrid support. Trailhead presents the two side by side rather than announcing a retirement for Engagement.[^s7] For B2B lead nurturing that lives inside the CRM, Account Engagement is the usual alternative.[^s1]

## Connections

Marketing Cloud Engagement belongs to the broader Salesforce marketing product family alongside Account Engagement and Marketing Cloud Next, which is its main architectural alternative.[^s1][^s7] It **has parts** Contact Builder, Automation Studio and Journey Builder, and **integrates with** Sales Cloud and Service Cloud through Marketing Cloud Connect.[^s2][^s4] Data 360 (Data Cloud) is related as the unified data layer that Marketing Cloud Next builds on.[^s7]

## Sources
[^s1]: Trailhead, "Discover Salesforce Marketing Solutions". https://trailhead.salesforce.com/ko/content/learn/modules/salesforce-marketing-cloud-quick-look/discover-salesforce-marketing-solutions (accessed 2026-11-03)
[^s2]: Trailhead, "Get Started with Journey Builder". https://trailhead.salesforce.com/en/content/learn/modules/journey-builder-basics/get-started-with-journey-builder (accessed 2026-11-03)
[^s3]: Trailhead, "Learn About Data Extensions". https://trailhead.salesforce.com/en/content/learn/modules/marketing-cloud-contact-management/learn-about-data-extensions (accessed 2026-11-03)
[^s4]: Trailhead, "Explore Synchronized Data Sources". https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-contact-management/explore-synchronized-data-sources (accessed 2026-11-03)
[^s5]: Trailhead, "Understand Contacts and Contact Model Relationships". https://trailhead.salesforce.com/pt-BR/content/learn/modules/marketing-cloud-contact-management/understand-contacts-and-contact-model-relationships (accessed 2026-11-03)
[^s6]: Salesforce Developers Blog, "Automation Studio and SQL in Marketing Cloud". https://developer.salesforce.com/blogs/2023/02/automation-studio-and-sql-in-marketing-cloud (accessed 2026-11-03)
[^s7]: Trailhead, "Get Started with Marketing Cloud Next Channel Marketing". https://trailhead.salesforce.com/content/learn/modules/channel-marketing-fundamentals-for-marketing-cloud-next/get-started-with-marketing-cloud-next-channel-marketing (accessed 2026-11-03)
