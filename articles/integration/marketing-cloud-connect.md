---
id: kt:marketing-cloud-connect
type: Feature
title: Marketing Cloud Connect
aliases: [MC Connect, MCC, Marketing Cloud Connector, Marketing Cloud Connect managed package]
domain: integration
summary: >-
  The managed-package connector that links a Marketing Cloud Engagement account to a Sales Cloud or Service Cloud
  org, so CRM users can send Marketing Cloud email to leads, contacts, campaigns and reports, CRM records can be
  synchronized into Marketing Cloud data extensions, and email tracking and Journey Builder activity flow back to CRM.
release: "Winter '27"
status: current
broader: [kt:data-integration]
related: [kt:heroku-connect, kt:marketing-cloud-account-engagement, kt:salesforce-marketing-solutions]
relations:
  - {predicate: integratesWith, object: kt:marketing-cloud-engagement}
  - {predicate: integratesWith, object: kt:journey-builder}
  - {predicate: integratesWith, object: kt:contact-builder}
  - {predicate: dependsOn, object: kt:connected-apps}
  - {predicate: dependsOn, object: kt:platform-events}
  - {predicate: requiresLicense, object: kt:marketing-cloud-engagement}
sources:
  - id: s1
    title: "Guide to Marketing Cloud Connect Setup (Marketing Cloud Connect module)"
    publisher: Trailhead (Salesforce)
    url: https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-connect/get-started-with-mc-connect
    type: official-learning
    accessed: 2026-11-20
  - id: s2
    title: "Salesforce CRM Setup & Configuration (Marketing Cloud Connect module)"
    publisher: Trailhead (Salesforce)
    url: https://trailhead.salesforce.com/en/modules/marketing-cloud-connect/units/install-mc-connect
    type: official-learning
    accessed: 2026-11-20
  - id: s3
    title: "Integrate Marketing Cloud with Salesforce CRM (Marketing Cloud Connect module)"
    publisher: Trailhead (Salesforce)
    url: https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-connect/finish-mc-connect-configuration
    type: official-learning
    accessed: 2026-11-20
  - id: s4
    title: "Explore Synchronized Data Sources (Marketing Cloud Engagement Contact Management)"
    publisher: Trailhead (Salesforce)
    url: https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-contact-management/explore-synchronized-data-sources
    type: official-learning
    accessed: 2026-11-20
created: 2026-11-20
---

# Marketing Cloud Connect

Marketing Cloud Connect (MC Connect) is the connector between Marketing Cloud Engagement, which runs outside the core Salesforce Platform, and a Sales Cloud or Service Cloud org. It is installed in the CRM org as a managed package and then authorized from both sides.[^s1][^s2] Once connected, it carries traffic in both directions: email sends, triggered sends and Journey Builder entry events originate from CRM data, while email tracking results, synchronized data extensions and Journey Builder activities become visible in CRM.[^s1]

## How it works

Setup follows six stages: review prerequisites, install the managed package, configure CRM, configure Marketing Cloud, finalize the configuration, and confirm it with a test send.[^s1] Two dedicated system users carry the connection. A **Marketing Cloud Connect API user** in Marketing Cloud authenticates sends, triggered sends, tracking subscription requests and Journey Builder entry events, and must have access to every business unit CRM should reach.[^s1] A **CRM API user** in Salesforce makes the connected app work and exposes tracking data, synchronized data extensions and journey activities in CRM; Trailhead recommends a dedicated licensed user for it.[^s1]

In CRM, the admin enables Custom Platform Events (the package will not install without it), installs the package for admins only, adds the Email Sends and Individual Email Results related lists and action pages to lead and contact layouts, and grants the connector's admin and user checkboxes on user records.[^s2] An empty permission set is created purely for connected-app authorization and must be assigned to the CRM API user and to every user who sends through the connector; the Email Opt Out field must be visible to those profiles.[^s2]

In Marketing Cloud, the API user opens the Salesforce Integration setting, keeps Scope by User off, and connects the account by logging in as the CRM API user.[^s3] Back in CRM, the admin edits the policies of the resulting connected app (admin-approved users pre-authorized, relaxed IP restrictions, refresh token expired immediately), sets a default workflow user, saves session settings so the wizard can add IP allowlisting, and runs the configuration wizard.[^s3] The final screen chooses send options, an error notification address, which tracking data to bring back to CRM, and at least one business unit; each Marketing Cloud user who sends is then linked to a CRM user so their status reads Integrated.[^s3]

## Synchronized data sources

Data moves from CRM into Marketing Cloud through **Synchronized Data Sources** in Contact Builder. The admin picks objects and fields, chooses which records to pull (all, since a date, or where a checkbox is true) and sets a polling interval in minutes or hours.[^s4] Each synced object becomes a data extension named after the object with a _Salesforce suffix, and these sit at the top level of an Enterprise account; to segment or share them across business units, use a query or filter activity into a shared data extension.[^s4] Once started, a sync can be paused but not deleted, and the order in which objects are added matters because Marketing Cloud builds relationships from them.[^s4]

## Limits and gotchas

- One Marketing Cloud account normally connects to one CRM org; multi-org setups exist but are a separate design.[^s1]
- Supported CRM editions are Enterprise, Unlimited and Performance, plus Developer Edition sandboxes.[^s1]
- The connector recognizes a subscriber only when its subscriber key is the CRM contact or lead ID, so older accounts may need a subscriber key migration.[^s1]
- MC Connect screens run in Salesforce Classic; Lightning Experience users are redirected there when they open its tabs.[^s1]
- Every synchronized contact or lead counts as a contact in Contact Builder, even if it is never emailed.[^s4]
- Tracking data written back to CRM consumes org data storage, so choose tracking options deliberately.[^s3]

User roles also differ: integrated users can send to Salesforce reports and campaigns, CRM-only users see email results but cannot send, and Marketing Cloud-only users can send to synced data extensions but not to reports or campaigns.[^s1]

## When to use it (and when not)

Use MC Connect when marketing runs in Marketing Cloud Engagement but the system of record for leads and contacts is a Sales or Service Cloud org, and marketers or sales users need CRM-driven sends and engagement history on the record.[^s1][^s4] Its synced data extensions are copies of CRM data on a polling schedule, so segment them in Marketing Cloud rather than treating them as a live view of CRM.[^s4]

## Connections

MC Connect is a form of `kt:data-integration` and **integrates with** `kt:marketing-cloud-engagement`, `kt:contact-builder` (where synchronized data sources live) and `kt:journey-builder` (entry events and CRM activities).[^s1][^s4] It **depends on** `kt:connected-apps` for authorization and on `kt:platform-events` being enabled for installation, and it **requires** a Marketing Cloud Engagement license alongside Sales or Service Cloud.[^s1][^s2][^s3] Like `kt:heroku-connect`, it replicates CRM records into another Salesforce product's data store; it belongs to `kt:salesforce-marketing-solutions` and relates to `kt:marketing-cloud-account-engagement`, another product in the same family.[^s4]

## Sources

[^s1]: Trailhead (Salesforce), "Guide to Marketing Cloud Connect Setup". https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-connect/get-started-with-mc-connect (accessed 2026-11-20)
[^s2]: Trailhead (Salesforce), "Salesforce CRM Setup & Configuration". https://trailhead.salesforce.com/en/modules/marketing-cloud-connect/units/install-mc-connect (accessed 2026-11-20)
[^s3]: Trailhead (Salesforce), "Integrate Marketing Cloud with Salesforce CRM". https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-connect/finish-mc-connect-configuration (accessed 2026-11-20)
[^s4]: Trailhead (Salesforce), "Explore Synchronized Data Sources". https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-contact-management/explore-synchronized-data-sources (accessed 2026-11-20)
