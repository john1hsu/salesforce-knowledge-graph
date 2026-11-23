---
id: kt:mulesoft-composer
type: Product
title: MuleSoft Composer
aliases: [MuleSoft Composer for Salesforce, Composer flows, invocable Composer flows]
domain: integration
summary: >-
  MuleSoft's no-code integration tool, used standalone or as an app inside a Salesforce org, in which admins and
  business users build event- or schedule-triggered flows that move and sync data between Salesforce and other
  systems through prebuilt connectors.
release: "Winter '27"
status: current
broader: [kt:data-integration]
related: [kt:mulesoft-anypoint-platform, kt:application-network, kt:point-to-point-integration, kt:external-services, kt:mulesoft-for-flow-integration]
relations:
  - {predicate: integratesWith, object: kt:salesforce-platform}
  - {predicate: integratesWith, object: kt:slack-platform}
  - {predicate: consumedBy, object: kt:flow-builder}
  - {predicate: dependsOn, object: kt:named-credentials}
sources:
  - id: s1
    title: "Building Process Automation with MuleSoft Composer"
    publisher: MuleSoft (Salesforce)
    url: https://docs.mulesoft.com/composer/ms_composer_overview
    type: official-docs
    accessed: 2026-11-23
  - id: s2
    title: "Composer Connector Reference"
    publisher: MuleSoft (Salesforce)
    url: https://docs.mulesoft.com/composer/ms_composer_reference
    type: official-docs
    accessed: 2026-11-23
  - id: s3
    title: "MuleSoft Composer Release Notes"
    publisher: MuleSoft (Salesforce)
    url: https://docs.mulesoft.com/composer/ms_composer_ms_release_notes
    type: official-docs
    accessed: 2026-11-23
  - id: s4
    title: "MuleSoft Composer Glossary"
    publisher: MuleSoft (Salesforce)
    url: https://docs.mulesoft.com/composer/ms_composer_glossary
    type: official-docs
    accessed: 2026-11-23
  - id: s5
    title: "Explore MuleSoft Composer (MuleSoft Composer Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/mulesoft-composer-basics/explore-mulesoft-composer
    type: official-learning
    accessed: 2026-11-23
  - id: s6
    title: "Introducing Invocable Composer Flows: Automate End-to-End Across All of Salesforce"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2023/introducing-invocable-composer-flows-automate-end-to-end-across-all-of-salesforce
    type: official-blog
    accessed: 2026-11-23
created: 2026-11-23
---

# MuleSoft Composer

MuleSoft Composer is a no-code, visual tool for automating data integration between systems and keeping their data in sync in near real time.[^s1] It targets people who are not integration developers: a flow is assembled from a source system, a trigger and a set of actions, with no Mule application or DataWeave code to write.[^s1][^s5] It comes in two forms: a standalone web app that needs no installation, and **MuleSoft Composer for Salesforce**, an app an admin installs into an org and users open from the App Launcher; both require the *MuleSoft Composer User* permission set.[^s5]

## How it works

A Composer **flow** is an automated process that connects to a system and performs actions on its data.[^s4] Every flow starts with a trigger, and the first step must connect to a system even when that system is the Salesforce org hosting Composer.[^s4] Trailhead lists three trigger kinds: a system event (such as a new or changed record), an invocation by HTTP POST from an external system, and a scheduler that runs the flow at an interval you choose.[^s5] The documentation's scheduling example is a run every 10 minutes.[^s1]

After the trigger come system actions that read, change or send data, plus local variables.[^s5] Flow control is limited to If/Else, For Each over a set of records, and an Error Handler block with a watched section and an on-error section.[^s5] Fields are mapped with "data pills" carried forward from earlier steps.[^s4] Connections pair a connector with credentials, never expose those credentials, can be reused across flows, and belong only to the user who created them.[^s1]

The build lifecycle is plan, design and test, activate, monitor and deactivate. Tests run against a single record, and changes take effect only once the flow is activated in production.[^s1][^s5] Each run is recorded in Run History on the flow detail page, where failed runs are flagged.[^s5]

## Connectors

The connector reference lists 30 connectors, among them Salesforce, Salesforce Marketing Cloud, Slack, Tableau, NetSuite, Workday, ServiceNow, Jira, Zendesk, SAP S/4HANA Cloud, Snowflake, Google Sheets and Stripe.[^s2] It also includes generic HTTP and REST Consumer connectors for systems without a dedicated one, and a MuleSoft RPA connector for driving bots.[^s2] Behaviour differs by connector because each target system stores and exposes data differently, so each has its own trigger and action reference.[^s2] Event triggers on most connectors poll the target API, and since late 2023 a **Polling Frequency** setting controlling how often Composer checks for changes has been required on them.[^s3]

## Invoking Composer from Salesforce

Composer flows can be called from Flow Builder, Flow Orchestration, another Composer flow, an Apex callout or a plain HTTP request.[^s3] The Admins blog describes the setup: a flow begins with an Invoke trigger that accepts primitive or JSON-shaped inputs. On activation, Composer issues a flow URL, a client ID and secret, and an OpenAPI spec.[^s6] The admin then creates a Named Credential and External Credential and registers the spec as an External Service so Flow Builder can call the flow as an authenticated action.[^s6] Later releases added outputs returned to the caller, including lists of primitives and objects.[^s3][^s6]

## Limits and gotchas

- **Usage is metered**: the Usage Summary shows monthly tasks and credit usage per flow, so busy polling flows cost credits.[^s1][^s4]
- **Task definitions differ**: a task is an insert, update or delete in a target system; a Composer task is any connector action, reads included.[^s4]
- **Auto-deactivation**: since May 2026, a flow with 100 or more consecutive errors over 10 or more days is switched off.[^s3]
- **Connection ownership**: connections are private to their creator, so plan shared service users for team-owned flows.[^s1]
- **No Trailhead Playground**: Composer is not available there, so hands-on practice needs a licensed org.[^s5]

Releases are delivered automatically, and fixes still ship per connector; the October 2026 notes, for example, tightened WSDL handling in the ServiceNow connector.[^s3]

## When to use it (and when not)

Composer suits simple point-to-point syncs owned by admins or business teams. Typical cases are creating a NetSuite sales order when an opportunity is Closed Won, or escalating cases between Service Cloud, Jira and Zendesk.[^s1][^s5] When integrations need reusable APIs, complex transformation, high volume or central API governance, build Mule applications on Anypoint Platform instead. Composer has a separate login and shares only Exchange API assets in the same Anypoint organization.[^s1][^s3] Because invocable Composer flows are themselves reached from Flow through External Services, a REST API that Flow can call directly may not need the extra Composer hop.[^s6]

## Connections

Composer is a no-code entry point into `kt:data-integration` and sits alongside `kt:mulesoft-anypoint-platform`, with which it shares Exchange API assets.[^s1][^s3] Its flows are mostly `kt:point-to-point-integration`, and they let business users extend an `kt:application-network`.[^s1] It `integratesWith` the `kt:salesforce-platform` and `kt:slack-platform` through prebuilt connectors.[^s2] Invocable flows are `consumedBy` `kt:flow-builder` via `kt:external-services` and `dependsOn` `kt:named-credentials` for authenticated callouts.[^s6] The MuleSoft docs site also lists `kt:mulesoft-for-flow-integration`, a clicks-not-code option for point-to-point integration, kept here as a separate node.[^s1]

## Sources
[^s1]: MuleSoft, "Building Process Automation with MuleSoft Composer". https://docs.mulesoft.com/composer/ms_composer_overview (accessed 2026-11-23)
[^s2]: MuleSoft, "Composer Connector Reference". https://docs.mulesoft.com/composer/ms_composer_reference (accessed 2026-11-23)
[^s3]: MuleSoft, "MuleSoft Composer Release Notes". https://docs.mulesoft.com/composer/ms_composer_ms_release_notes (accessed 2026-11-23)
[^s4]: MuleSoft, "MuleSoft Composer Glossary". https://docs.mulesoft.com/composer/ms_composer_glossary (accessed 2026-11-23)
[^s5]: Trailhead, "Explore MuleSoft Composer". https://trailhead.salesforce.com/content/learn/modules/mulesoft-composer-basics/explore-mulesoft-composer (accessed 2026-11-23)
[^s6]: Salesforce Admins Blog, "Introducing Invocable Composer Flows". https://admin.salesforce.com/blog/2023/introducing-invocable-composer-flows-automate-end-to-end-across-all-of-salesforce (accessed 2026-11-23)
