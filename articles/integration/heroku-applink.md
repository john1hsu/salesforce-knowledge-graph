---
id: kt:heroku-applink
type: Feature
title: Heroku AppLink
aliases: [AppLink, Heroku Integration, heroku-applink add-on]
domain: integration
summary: >-
  A Heroku add-on that publishes a Heroku app's OpenAPI-described endpoints into connected Salesforce orgs as
  External Services, so Apex, Flow, Agentforce and Data Cloud can invoke them while the app works on Salesforce
  data under a chosen user context (user, user-plus or authorized-user).
release: "Winter '27"
status: current
broader: [kt:heroku]
related: [kt:heroku-connect, kt:salesforce-functions]
relations:
  - {predicate: dependsOn, object: kt:external-services}
  - {predicate: dependsOn, object: kt:external-client-apps}
  - {predicate: enables, object: kt:agent-actions}
  - {predicate: integratesWith, object: kt:data-cloud}
  - {predicate: mitigates, object: kt:governor-limits}
sources:
  - id: s1
    title: "Heroku AppLink"
    publisher: Heroku Dev Center (Salesforce)
    url: https://devcenter.heroku.com/articles/heroku-applink
    type: official-docs
    accessed: 2026-11-15
  - id: s2
    title: "Getting Started with Heroku AppLink and Salesforce"
    publisher: Heroku Dev Center (Salesforce)
    url: https://devcenter.heroku.com/articles/getting-started-heroku-applink
    type: official-docs
    accessed: 2026-11-15
  - id: s3
    title: "Heroku AppLink User Modes"
    publisher: Heroku Dev Center (Salesforce)
    url: https://devcenter.heroku.com/articles/heroku-applink-user-modes
    type: official-docs
    accessed: 2026-11-15
  - id: s4
    title: "AppLink Architecture Overview (Heroku AppLink Integrations)"
    publisher: Trailhead (Salesforce)
    url: https://trailhead.salesforce.com/content/learn/modules/heroku-applink-integrations/applink-architecture-overview
    type: official-learning
    accessed: 2026-11-15
  - id: s5
    title: "When to Use Heroku AppLink (Heroku AppLink Integrations)"
    publisher: Trailhead (Salesforce)
    url: https://trailhead.salesforce.com/ko/content/learn/modules/heroku-applink-integrations/when-to-use-heroku-applink
    type: official-learning
    accessed: 2026-11-15
created: 2026-11-15
---

# Heroku AppLink

Heroku AppLink, formerly called Heroku Integration, is a Heroku add-on that exposes a Heroku app's APIs as services inside Salesforce. Admins and developers can then run those APIs as actions from Flow, Apex, Data Cloud and Agentforce, and AppLink enforces Salesforce user permissions whenever the app touches org data.[^s1] It lets teams write logic in languages and libraries the platform doesn't offer, while keeping the Salesforce security model in the loop.[^s4]

## How it works

An AppLink setup has several moving parts, all documented in the Dev Center getting-started guide:[^s2]

- **Add-on** (`heroku-applink`): provisions the connection and sets the `HEROKU_APPLINK_API_URL` and `HEROKU_APPLINK_TOKEN` config vars.[^s2]
- **CLI plugin**: adds commands such as `salesforce:connect`, `salesforce:publish`, `salesforce:publications` and `datacloud:connect`.[^s2]
- **Service mesh buildpack**: a proxy in front of the app that validates and authenticates incoming Salesforce and Data Cloud requests; it must run before the language buildpack.[^s2]
- **SDKs** for Node.js and Python, which add user and org context to requests and provide DML against Salesforce and Data Cloud.[^s2][^s1]
- **`api-spec.yaml`**: an OpenAPI 3.0 description of the operations that get published to Salesforce.[^s2]

The flow is: provision the add-on, deploy, run `salesforce:connect` against an org (login.salesforce.com for production, test.salesforce.com for sandboxes and scratch orgs), then `salesforce:publish` the spec.[^s2] Publishing creates an External Service and API actions in the org, adds the APIs to API Catalog, and can generate Agentforce agent actions.[^s1] Each publication is listed under Setup › Heroku › Apps.[^s2] One app can be connected to several Salesforce or Data Cloud orgs, but each org needs its own connection.[^s1]

Apex calls the generated classes synchronously or asynchronously, and Flow uses the generated action with no code.[^s2] Data Cloud can push events to the app through a Data Action Target webhook created with the CLI.[^s1]

## User modes

The SDK applies Salesforce permissions in one of three modes:[^s3]

- **`user`** (default): the app can do only what the invoking user can do.[^s3]
- **`user-plus`**: the invoking user's access plus a session-based permission set declared in the OpenAPI spec, for controlled elevation such as editing one restricted field.[^s3]
- **`authorized-user`**: the app runs as a designated user. This is the only mode for Heroku-initiated work such as worker dynos and nightly jobs, and a dedicated integration user is recommended.[^s3]

Trailhead calls the third pattern "named user mode" and notes that field-level security and sharing still apply through the OAuth-based user context.[^s4]

## Limits and gotchas

- **Region latency.** AppLink is available in all Common Runtime and Private Space regions, but the service itself runs in `virginia`, so apps hosted far away pay extra CLI and invocation latency.[^s1]
- **Editions.** Only Salesforce editions with API access can be connected.[^s1]
- **Permissions on both sides.** Operators need `deploy` or `operate` access to the Heroku app. In Salesforce, users need the Manage Heroku AppLink permission, and callers need the permission set generated at publish time.[^s2]
- **Connected apps are going away.** From Spring '26 new connected apps can't be created, so publish with an external client app; that flag needs Summer '26 or later.[^s2]
- **Removal is destructive.** Deleting the add-on removes all connections, authorizations and publications, so check that nothing still references the generated actions first.[^s2]
- **Environment hygiene.** Dev Center advises against mixing environment types, for example wiring a production org to a staging app.[^s1]

## When to use it (and when not)

Trailhead recommends AppLink for logic too complex for Flow, heavy computation, specialized libraries, or orchestrating many external APIs. Governor-limit timeouts in Apex or Flow are named as a signal to consider it.[^s5] For simple CRUD, approvals or low-complexity callouts, Flow, Apex or plain External Services are enough.[^s5] MuleSoft remains the choice for enterprise-wide orchestration, with AppLink handling Salesforce-specific computation alongside it.[^s5] For high-volume data access, Heroku Connect syncs CRM data into Postgres and can be combined with AppLink.[^s4]

## Connections

AppLink is a narrower part of `kt:heroku`, the add-on that bridges Heroku apps to orgs.[^s1] It is **related** to `kt:heroku-connect`, the data-sync bridge it is often paired with.[^s4] It **depends on** `kt:external-services`, because every publication becomes an External Service, and on `kt:external-client-apps`, now required for the publish authorization.[^s1][^s2] It **enables** `kt:agent-actions` by generating Agentforce actions from the OpenAPI spec.[^s1] It **integrates with** `kt:data-cloud` through Data Cloud connections and Data Action Targets.[^s1] It **mitigates** `kt:governor-limits` by moving long-running or compute-heavy logic off-platform.[^s5]

## Sources

[^s1]: Heroku Dev Center, "Heroku AppLink". https://devcenter.heroku.com/articles/heroku-applink (accessed 2026-11-15)
[^s2]: Heroku Dev Center, "Getting Started with Heroku AppLink and Salesforce". https://devcenter.heroku.com/articles/getting-started-heroku-applink (accessed 2026-11-15)
[^s3]: Heroku Dev Center, "Heroku AppLink User Modes". https://devcenter.heroku.com/articles/heroku-applink-user-modes (accessed 2026-11-15)
[^s4]: Trailhead, "AppLink Architecture Overview". https://trailhead.salesforce.com/content/learn/modules/heroku-applink-integrations/applink-architecture-overview (accessed 2026-11-15)
[^s5]: Trailhead, "When to Use Heroku AppLink". https://trailhead.salesforce.com/ko/content/learn/modules/heroku-applink-integrations/when-to-use-heroku-applink (accessed 2026-11-15)
