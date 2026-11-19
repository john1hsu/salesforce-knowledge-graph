---
id: kt:journey-builder
type: Feature
title: Journey Builder
aliases: [Marketing Cloud Journey Builder, SFMC Journey Builder]
domain: clouds-and-products
summary: >-
  The Marketing Cloud Engagement application for designing and running automated, multi-step, multi-channel
  customer journeys on a drag-and-drop canvas, where contacts enter from one entry source and move through
  message, advertising, flow-control, data-update and Sales and Service Cloud activities.
release: "Winter '27"
status: current
broader: [kt:marketing-cloud-engagement]
related: [kt:loyalty-management, kt:salesforce-marketing-solutions, kt:marketing-cloud-next]
relations:
  - {predicate: partOf, object: kt:marketing-cloud-engagement}
  - {predicate: dependsOn, object: kt:contact-builder}
  - {predicate: integratesWith, object: kt:automation-studio}
  - {predicate: integratesWith, object: kt:marketing-cloud-connect}
sources:
  - id: s1
    title: "Get Started with Journey Builder (Journey Builder Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/journey-builder-basics/get-started-with-journey-builder
    type: official-learning
    accessed: 2026-11-19
  - id: s2
    title: "Prepare the Entry Source (Journey Builder Campaigns)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/journey-builder-campaigns/prepare-the-entry-source
    type: official-learning
    accessed: 2026-11-19
  - id: s3
    title: "Journey Builder Glossary"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/glossary.html
    type: official-docs
    accessed: 2026-11-19
  - id: s4
    title: "Build Custom Activities and Events"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/creating-activities
    type: official-docs
    accessed: 2026-11-19
  - id: s5
    title: "Marketing Cloud Journey Builder Implementation Guide (PDF)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/mc_jb_implementation_guide.pdf
    type: official-docs
    accessed: 2026-11-19
created: 2026-11-19
---

# Journey Builder

Journey Builder is the Marketing Cloud Engagement application for creating and managing automated, multi-channel marketing campaigns. Trailhead stresses that it is not a standalone product: it orchestrates content and audiences that are built in Email Studio, Mobile Studio, Advertising Studio, Content Builder and Contact Builder, and it is opened from the Marketing Cloud Engagement top navigation.[^s1] Salesforce's implementation guide calls it the primary place for sending messages and designing multi-step journeys.[^s5] Typical uses are welcome series, promotions, re-engagement after an abandoned cart or search, and retention messages such as birthday or renewal reminders.[^s1]

## How it works

A **journey** is the unit of work. Developers know it as an "interaction": it is built on the canvas from an entry event, a contact filter, a set of activities and an optional goal, and it is stored as a JSON journey specification.[^s3] Every journey starts from an **entry source**. The options include data extensions, API events, audiences, CloudPages and Salesforce data, and an entry source can belong to one journey or be shared by several.[^s1] A single journey uses only one entry source.[^s2]

- **Data extension entry** reads a sendable data extension on a schedule. Trailhead says the check can run from daily to annually, and you can also set how long the source keeps running.[^s2]
- **API event entry** suits customer activity that happens outside Marketing Cloud. It is the recommended pattern for event-based entry, but someone has to build the calling endpoint.[^s2]
- For bulk injection, the **Fire Event** activity in Automation Studio pushes large batches of contacts into a journey.[^s3]

After entry, contacts move through **canvas activities**:[^s1]

- **Message activities** send email, SMS, push notifications and other content.
- **Advertising activities**: Ad Audience builds an advertising audience, and Ad Campaign creates an audience plus a simple Facebook campaign.[^s1]
- **Flow control** includes Wait, Wait Until, Split (random or Einstein-driven routing) and Join.[^s1]
- **Customer Updates** writes contact values back to a data extension.[^s1]
- **Sales and Service Cloud activities** create or update CRM records such as Task, Lead, Contact, Case, Opportunity and Campaign Member, or convert a lead.[^s1]

Journey Builder keeps two views of a contact. **Entry data** is a snapshot taken at entry and never changes. **Contact data** reflects the current values in Contact Builder. Comparing the two lets a split detect an attribute that changed mid-journey.[^s2] The toolbar holds goal and exit-criteria settings, along with validate, test and activate. Journey History traces one contact's path by contact key.[^s1]

## Versions, settings and extensibility

**Versions** let a marketer revise a running journey without disrupting the contacts already in it. Copying a journey keeps its entry source, goal and activity flow in a new draft.[^s5] Journey settings control **re-entry** (the implementation guide's example uses *No re-entry*) and which email address the journey sends to.[^s5] Channel address priority can rank a primary and a secondary email for each journey version.[^s3]

Developers can add **custom activities and custom entry events**. These are web apps that load in the canvas iframe, defined by a `config.json` and wired to Journey Builder through the Postmonger event library.[^s4] Salesforce requires them to be hosted on an SSL web server on port 443 and registered as an endpoint in an installed package.[^s4] The Interaction REST resource creates, reads, updates, publishes and stops journeys, and an audit log records each version's history.[^s3]

## Limits and gotchas

- Sales and Service Cloud activities only work with Marketing Cloud Connect installed, and the implementation guide lists the connector as a requirement for Core/Advanced and Enterprise 2.0 accounts.[^s1][^s5]
- Enterprise 1.0 accounts using Lock & Publish don't support the Salesforce Event entry source, and Enterprise 1.0 can't copy journeys from a parent to a child business unit.[^s5]
- Journeys share processing resources. The guide advises scheduling journey reports no more than once every four hours and requesting 30 days of activity or less.[^s5]
- If a journey's data is spread over several data extensions, combine it first (for example with an Automation Studio SQL Query activity) and pre-filter it to speed up processing.[^s2]
- Salesforce Customer Support doesn't cover custom Journey Builder activities and events, so their owners have to support them.[^s4]

## When to use it (and when not)

Use Journey Builder when Marketing Cloud Engagement is the messaging platform and you need event- or schedule-driven customer lifecycle campaigns across channels.[^s1] Use Automation Studio for batch data preparation feeding a journey rather than for the journey logic itself.[^s2] Journey Builder is for marketing contacts in Marketing Cloud Engagement; its CRM activities can create tasks, cases or leads for sales and service teams, but only through Marketing Cloud Connect.[^s1]

## Connections

Journey Builder is **part of** `kt:marketing-cloud-engagement` and **depends on** `kt:contact-builder` for its data model and contact key.[^s1][^s5] It **integrates with** `kt:automation-studio`, which prepares entry data and fires batch entry events, and with `kt:marketing-cloud-connect`, which unlocks the CRM activities and Salesforce data entry.[^s2][^s3][^s1] It sits under `kt:salesforce-marketing-solutions` and relates to `kt:loyalty-management`, which delivers loyalty messages through journeys, and to `kt:marketing-cloud-next`, the newer marketing product in the same family.[^s1]

## Sources
[^s1]: Trailhead, "Get Started with Journey Builder". https://trailhead.salesforce.com/content/learn/modules/journey-builder-basics/get-started-with-journey-builder (accessed 2026-11-19)
[^s2]: Trailhead, "Prepare the Entry Source". https://trailhead.salesforce.com/content/learn/modules/journey-builder-campaigns/prepare-the-entry-source (accessed 2026-11-19)
[^s3]: Salesforce Developers, "Journey Builder Glossary". https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/glossary.html (accessed 2026-11-19)
[^s4]: Salesforce Developers, "Build Custom Activities and Events". https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/creating-activities (accessed 2026-11-19)
[^s5]: Salesforce, "Marketing Cloud Journey Builder Implementation Guide". https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/mc_jb_implementation_guide.pdf (accessed 2026-11-19)
