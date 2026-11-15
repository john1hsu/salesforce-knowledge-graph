---
id: kt:data-kits
type: Feature
title: Data Kits
aliases: [data kit, Data 360 data kits, Data Cloud data kits, DevOps data kit, standard data kit, Data Package Kit Definition]
domain: data-cloud-and-ai
summary: >-
  Containers in Data 360 (formerly Data Cloud) that bundle Data 360 metadata such as data streams, data models and
  calculated insights so it can be packaged or deployed to another org and published there in dependency order.
release: "Winter '27"
status: current
broader: [kt:data-cloud]
related: [kt:data-streams, kt:calculated-insights, kt:data-graphs, kt:data-model-objects, kt:scratch-orgs, kt:unlocked-packages]
relations:
  - {predicate: dependsOn, object: kt:data-spaces}
  - {predicate: consumedBy, object: kt:second-generation-managed-packages}
  - {predicate: consumedBy, object: kt:change-sets}
  - {predicate: configuredVia, object: kt:package-xml-manifest}
sources:
  - id: s1
    title: "Packages and Data Kits"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-dev/guide/packages-data-kits.html
    type: official-docs
    accessed: 2026-11-15
  - id: s2
    title: "Create and Package a Data Kit (Packaging and Data Kits in Data 360)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/packaging-and-data-kits-in-salesforce-cdp/create-and-package-a-data-kit
    type: official-learning
    accessed: 2026-11-15
  - id: s3
    title: "Workflow for Data 360 Second-Generation Managed Packages"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-dev/guide/data-cloud-2gp-workflow.htm
    type: official-docs
    accessed: 2026-11-15
  - id: s4
    title: "Use CLI to Deploy Changes from a Sandbox to Data 360"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-dev/guide/dc-deploy_data_kit_using_cli.html
    type: official-docs
    accessed: 2026-11-15
  - id: s5
    title: "Deploy and Validate Your Data 360 Configurations (Data 360 Sandboxes)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-360-sandboxes/deploy-and-validate-your-data-360-configurations
    type: official-learning
    accessed: 2026-11-15
created: 2026-11-15
---

# Data Kits

A data kit is the container Data 360 (formerly Data Cloud) uses to move its own configuration between orgs. Data 360
metadata, the definitions of data streams, data models, calculated insights and similar components, can't be dropped
straight into a package: it must first be added to a data kit, and the data kit is then added to the package. A kit
carries definitions only, never the records themselves.[^s1]

## How it works

Kits are built in Data Cloud Setup under Developer Tools, Data Kits. An admin or developer picks a kit type, then adds
data stream bundles (grouped by connector, for example Salesforce CRM), data models, calculated insights and other
components.[^s2] Two kit types appear in the documentation: a **Standard** kit, used for packaging, and a **DevOps** kit,
used to promote changes from a sandbox to production.[^s2][^s4]

Each kit has a **publishing sequence**. It is generated from component creation time and decides the order in which
components are created in the target org, so upstream items (a calculated insight) must come before downstream ones
(a segment that uses it), or the deployment fails.[^s2][^s5]

From the kit page you download a `package.xml` manifest (a Connect REST API endpoint can return it too), retrieve the
metadata with the Salesforce CLI into a project kept apart from other metadata, and commit it to source control.[^s2][^s4]
In the subscriber or target org, the person deploying chooses the connection and data space to deploy into, and one org
can deploy the same kit to several data spaces.[^s2]

## Packaging and deployment paths

- **Unmanaged packages** let customer teams carry Data 360 metadata from a test org to production.[^s1]
- **Managed packages** are how partners distribute on AppExchange; the org needs an enabled namespace.[^s1]
- **2GP managed packages** need a Dev Hub plus a namespace org, the Data Cloud Architect permission set, and promotion before production installs.[^s3]
- **Change sets** work for simple moves between connected orgs, using the Data Package Kit Definition component type.[^s5]
- **CLI or Metadata API** is the recommended repeatable, version-controlled route, alone or under tools like Copado or Gearset.[^s5]

## Limits and gotchas

- Since Winter '25, Data 360 metadata and other platform metadata can't share a package; unlocked packages can't hold Data 360 metadata.[^s1]
- Managed-package Data 360 components are locked: subscribers can add components, but edits to deployed ones are overwritten on redeploy.[^s1]
- Not every Data 360 component is packageable; check the Data 360 Extensibility Readiness Matrix before designing a kit.[^s1][^s3]
- Deploying a kit doesn't automatically deploy its data streams, data models and calculated insights; those are deployed separately.[^s3]
- Key qualifier files must be deleted from the retrieved project before a CLI deploy; Salesforce's guide says not to skip it.[^s4]
- Connector authorizations aren't copied, so inactive connectors must be reauthorized in production and the kit redeployed.[^s4]
- Retrieved file names are inconsistent, so `git diff`, blame and merge track kit changes poorly, and reused insights can collide.[^s5]

Deployed streams arrive as drafts and identity resolution does not run on its own: after deploying, teams start
ingestion, run the ruleset and validate unified profiles against known test records.[^s5] Beta 2GP versions install
only in scratch orgs, and enabling Data 360 in scratch orgs requires a Partner Support case.[^s3]

## When to use it (and when not)

Use a Standard kit inside a managed package when shipping a Data 360 solution to other customers, and a DevOps kit with
the CLI when promoting configuration from a Data 360 sandbox to production.[^s1][^s4] For Salesforce Platform metadata
(Apex, flows, objects), use ordinary packages or deployments instead; keeping the two kinds of metadata in separate
packages is mandatory, not a style choice.[^s1]

## Connections

Data kits are a capability of `kt:data-cloud`. They bundle `kt:data-streams`, `kt:data-model-objects`,
`kt:calculated-insights` and `kt:data-graphs`, and every deployment targets matching `kt:data-spaces`, which must exist
in the target org first.[^s4][^s5] They travel inside `kt:second-generation-managed-packages` built from
`kt:scratch-orgs`, or through `kt:change-sets` for simple moves, and are retrieved through a
`kt:package-xml-manifest`.[^s3][^s5] Unlike most metadata, they can't go into `kt:unlocked-packages`.[^s1]

## Sources

[^s1]: Salesforce Developers, "Packages and Data Kits". https://developer.salesforce.com/docs/data/data-cloud-dev/guide/packages-data-kits.html (accessed 2026-11-15)
[^s2]: Trailhead, "Create and Package a Data Kit". https://trailhead.salesforce.com/content/learn/modules/packaging-and-data-kits-in-salesforce-cdp/create-and-package-a-data-kit (accessed 2026-11-15)
[^s3]: Salesforce Developers, "Workflow for Data 360 Second-Generation Managed Packages". https://developer.salesforce.com/docs/data/data-cloud-dev/guide/data-cloud-2gp-workflow.htm (accessed 2026-11-15)
[^s4]: Salesforce Developers, "Use CLI to Deploy Changes from a Sandbox to Data 360". https://developer.salesforce.com/docs/data/data-cloud-dev/guide/dc-deploy_data_kit_using_cli.html (accessed 2026-11-15)
[^s5]: Trailhead, "Deploy and Validate Your Data 360 Configurations". https://trailhead.salesforce.com/content/learn/modules/data-360-sandboxes/deploy-and-validate-your-data-360-configurations (accessed 2026-11-15)
