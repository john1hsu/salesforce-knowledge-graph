---
id: kt:data-cloud-one
type: Feature
title: Data Cloud One
aliases: [Data 360 companion orgs, companion connection, companion connections, Data Cloud One companion org, Data 360 home org]
domain: data-cloud-and-ai
summary: >-
  Salesforce's multi-org connectivity architecture for Data 360 (formerly Data Cloud): one home org hosts the
  Data 360 instance, and other Salesforce orgs connect to it as companion orgs that use its unified data and many
  Data 360 features through the Data Cloud One app, without running their own instance.
release: "Winter '27"
status: current
broader: [kt:data-cloud]
related: [kt:org-strategy, kt:digital-wallet, kt:data-spaces, kt:zero-copy-data-sharing, kt:calculated-insights, kt:data-cloud-triggered-flows]
relations:
  - {predicate: dependsOn, object: kt:data-spaces}
  - {predicate: dependsOn, object: kt:data-residency}
  - {predicate: alternativeTo, object: kt:zero-copy-data-sharing}
  - {predicate: consumedBy, object: kt:agentforce}
sources:
  - id: s1
    title: "Data 360 Provisioning"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/decision-guides/data-360-provisioning
    type: official-docs
    accessed: 2026-11-21
  - id: s2
    title: "Connect Multiple Orgs with Data Cloud One (Data Cloud One: Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-cloud-one-quick-look/connect-multiple-orgs-with-data-cloud-one
    type: official-learning
    accessed: 2026-11-21
  - id: s3
    title: "Get Started with Data Cloud One (Data Cloud One: Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-cloud-one-quick-look/get-started-with-data-cloud-one
    type: official-learning
    accessed: 2026-11-21
  - id: s4
    title: "Data Cloud One Is Now Generally Available"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/10/data-cloud-one-is-now-generally-available
    type: official-blog
    accessed: 2026-11-21
  - id: s5
    title: "Redefining Multi-Org Strategy for Salesforce Admins With Data Cloud One"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2024/redefining-multi-org-strategy-with-data-cloud-one
    type: official-blog
    accessed: 2026-11-21
created: 2026-11-21
---

# Data Cloud One

Data Cloud One is how a company that runs several Salesforce orgs uses one Data 360 instance across all of them.
Salesforce's architects describe it as a multi-org connectivity architecture in which a single home org hosts the
Data 360 instance and the other orgs attach as companion orgs.[^s1] Users in a companion org reach unified profiles,
calculated insights and many Data 360 features through a Data Cloud One app, so they don't need a separate instance
or custom integration code.[^s2] The feature became generally available in October 2024, when Data 360 was still
called Data Cloud; Salesforce still uses the Data Cloud One name while calling the platform itself Data 360.[^s4][^s2]

Before Data Cloud One, the standard Salesforce CRM connector could bring CRM data from many orgs into Data 360, but
it doesn't sync metadata back or give those orgs access to Data 360 data or features. The only workarounds were
custom Apex and Flow integrations or a Data 360 instance in every org.[^s2] Salesforce's launch post illustrates
the gap with a three-org bank, where a cross-org request could take up to two weeks by hand.[^s4]

## How it works

- **Home org.** This is the org where Data 360 is provisioned. It sets the instance's region, owns administration and companion connections, and does all ingestion, identity resolution and unification.[^s1]
- **Data spaces.** On the home org, admins (or users with the Data 360 architect permission set) split data into `kt:data-spaces` and choose which ones to share with each companion.[^s3]
- **Companion connection.** This link from a companion org to the home org shares the metadata of the chosen data spaces: data model objects, the unified profile schema, calculated insights, segments and more.[^s1][^s2]
- **Companion org and app.** Once the connection is active and the first metadata sync finishes, the Data Cloud One app appears in the companion org.[^s3] Its users can build segments, insights, activations, data actions and prompts, and can use Data 360 data in Flow, Prompt Builder and Agentforce.[^s3][^s1]

Setup takes four point-and-click steps. Add the free Data Cloud One Companion Org SKU to each companion org, connect
each companion to the home org, share data spaces from the home org, then give users access in each companion org
based on governance needs.[^s3] Connections are managed under Data Cloud Setup's companion connections page.[^s5]

## Limits and gotchas

- **Connections.** At GA, every home org came with three free companion connections. More are available as add-on licenses, which Trailhead calls Additional Connection licenses.[^s4][^s3]
- **Credits.** Data Cloud One is part of the existing Data 360 SKU, but everything a companion org does (queries, segment runs, flows, AI and Trust Layer logging) uses the home org's credits. Usage per org appears in `kt:digital-wallet`.[^s4][^s1]
- **Residency.** All companion-org data becomes resident in the home org's region. Companions in other regions may get slower queries.[^s3][^s1]
- **No ingestion in companions.** Companion orgs can't ingest or unify data. Not every Data 360 feature is in the Data Cloud One app yet, and Salesforce says some features are still being made fully compatible.[^s1][^s2]
- **Hard to change later.** Changing the home org is difficult and disruptive. Turning an existing Data 360 org into a companion means deprovisioning it, which deletes its data and metadata. That can take months and can lose data, so move data and metadata (for example with `kt:data-kits`) first.[^s1][^s3]

## When to use it (and when not)

Salesforce's decision guide recommends Data Cloud One with one home org for enterprises that have several
Salesforce orgs. It suggests running as few Data 360 instances as possible, because each extra one adds cost and
repeats identity resolution and segmentation.[^s1] The preferred default is to use an existing production org as
the home org. A new dedicated org gives cleaner governance and a free choice of region, but it needs a new license
and takes longer to deliver value.[^s1]

Separate Data 360 instances make sense only when compliance, residency or business-unit independence requires them.
Those instances can then work together through zero-copy data sharing between Data 360 orgs. That shares access to
objects rather than copying them, and the guide calls it a federation strategy rather than a replacement for Data
Cloud One. A hybrid of several Data Cloud One clusters is also possible.[^s1]

## Connections

Data Cloud One is a narrower part of `kt:data-cloud` and is one of the main ways to put an `kt:org-strategy` with
several orgs into practice.[^s1] It depends on `kt:data-spaces`, the units it shares, and on `kt:data-residency`,
because the home org's region applies to every companion.[^s3] It is an alternative to running separate instances
linked by `kt:zero-copy-data-sharing`.[^s1] Companion orgs use `kt:calculated-insights`, `kt:data-cloud-triggered-flows`
and `kt:agentforce` features on the shared data, and their credit use is tracked in `kt:digital-wallet`.[^s5][^s1]

## Sources
[^s1]: Salesforce Architects, "Data 360 Provisioning". https://architect.salesforce.com/decision-guides/data-360-provisioning (accessed 2026-11-21)
[^s2]: Trailhead, "Connect Multiple Orgs with Data Cloud One". https://trailhead.salesforce.com/content/learn/modules/data-cloud-one-quick-look/connect-multiple-orgs-with-data-cloud-one (accessed 2026-11-21)
[^s3]: Trailhead, "Get Started with Data Cloud One". https://trailhead.salesforce.com/content/learn/modules/data-cloud-one-quick-look/get-started-with-data-cloud-one (accessed 2026-11-21)
[^s4]: Salesforce Developers Blog, "Data Cloud One Is Now Generally Available". https://developer.salesforce.com/blogs/2024/10/data-cloud-one-is-now-generally-available (accessed 2026-11-21)
[^s5]: Salesforce Admins Blog, "Redefining Multi-Org Strategy for Salesforce Admins With Data Cloud One". https://admin.salesforce.com/blog/2024/redefining-multi-org-strategy-with-data-cloud-one (accessed 2026-11-21)
