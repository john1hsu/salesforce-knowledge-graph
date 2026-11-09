---
id: kt:flow-versioning
type: Feature
title: Flow Versioning
aliases: [flow versions, flow version, flow version activation, active flow version, Save As New Version]
domain: automation
summary: >-
  The way Salesforce stores each saved revision of a flow as a numbered version under one flow definition, with at
  most one version active at a time, so admins can build and test a new version, activate it to replace the old one,
  and keep earlier versions for reference or reactivation.
release: "Winter '27"
status: current
broader: [kt:flow-builder]
related: [kt:subflows, kt:change-sets, kt:metadata-api, kt:flow-trigger-explorer]
relations:
  - {predicate: governedBy, object: kt:flow-limits}
  - {predicate: configuredVia, object: kt:process-automation-settings}
sources:
  - id: s1
    title: "General Flow Limits"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=flow_considerations_limit.htm&type=0
    type: official-docs
    accessed: 2026-11-09
  - id: s2
    title: "Flow Management Considerations"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=flow_considerations_manage.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-09
  - id: s3
    title: "Flow Version Properties"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.flow_ref_properties.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-09
  - id: s4
    title: "Subflow Element"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.flow_ref_elements_subflow.htm&type=5
    type: official-docs
    accessed: 2026-11-09
  - id: s5
    title: "Change Set Considerations for Flows"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.flow_considerations_change_sets.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-09
  - id: s6
    title: "Deploy Processes and Flows as Active"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.flow_distribute_deploy_active.htm&type=5
    type: official-docs
    accessed: 2026-11-09
created: 2026-11-09
---

# Flow Versioning

**Flow versioning** is how Salesforce keeps the history of a flow. A flow is a single definition with a fixed API name, and each revision saved from Flow Builder becomes a numbered **version** of it. Admins edit and test a new version while an older one keeps running, then activate the new one when it is ready. Each flow can hold up to 50 versions in every edition.[^s1] The flow's API name can't be changed once the flow is saved, which is what keeps every version tied to the same definition.[^s3]

## How it works

Only one version of a flow runs at a time. When you activate a version, the version that was active before is deactivated automatically, so swapping versions is a single action rather than a deactivate-then-activate sequence.[^s2] Deactivated versions stay in the org, which means you can roll back by reactivating an earlier version.

Some properties are frozen once a version has been active. The version's label, description and interview label can be edited only on inactive flows and versions, so changes go into a new version saved with **Save As**.[^s3] Each version also records its own **API version for running the flow**, which controls which versioned runtime behaviour it gets. That value does not move forward when Salesforce ships a new release; it changes only when someone with the Manage Flow permission edits it, ideally after reading the release notes for the versions in between.[^s3] Saving as a new version keeps the source version's runtime API version, and Flow Builder won't save a new version as a different flow type; to change type, save as a new flow instead.[^s3] If versions of one flow differ in type, the active version, or the latest when none is active, decides the flow's type.[^s2]

Interviews already running are not moved to a new version. They finish on the version they started with, and a flow with paused interviews can't be deleted until those interviews finish or are deleted.[^s2]

## Versions and subflows

A parent flow's Subflow element points at a flow, not a version number. From API version 61.0, screen flows and record-triggered flows call the referenced flow's active version, falling back to its latest version when none is active; for non-admin users, a call to a flow with no active version fails at runtime.[^s4] For debugging, a Debug option or the `?latestSub=true` URL parameter forces parents to run the latest version of each referenced flow.[^s4] So activating a new child version changes every parent at once.

## Deployment

Versioning shapes how flows move between orgs. A change set can carry only one version of a flow, and if the source has no active version, the latest inactive one is sent.[^s5] Each deployment creates a new version in the target org, and an active flow arrives there inactive by default, so someone must activate it after deployment.[^s5] Production orgs can change that with **Deploy processes and flows as active** in Process Automation Settings, which lets change sets and the Metadata API deploy new active versions. It requires a flow test coverage percentage, and at least one Apex test must cover that share of active processes and autolaunched flows; flows with screens are exempt. Non-production orgs don't show the setting because they can always deploy active versions.[^s6][^s5]

## Limits and gotchas

- 50 versions per flow; old versions count, so delete unused ones before you hit the cap.[^s1]
- To delete an active version, deactivate it first. Flows that were never activated can be deleted at any time.[^s2]
- If the user who activated a flow is later deactivated, the flow stops working, for every flow type.[^s2]
- Managed-package flows that aren't templates can only be activated or deactivated, not edited.[^s3]

## When to use it (and when not)

Treat a new version as the unit of change: build it, debug it, then activate it in a quiet window, and keep the previous version as an instant rollback path.[^s2] For moving changes between sandboxes and production, rely on source-driven deployment rather than many hand-made versions, and remember that every deployment adds a version to the target org.[^s5] Versioning is not version control: it keeps no branch history or diffs across orgs, so pair it with a repository.

## Connections

Flow versioning is a core behaviour of **Flow Builder** and of every flow type built there. It determines what **subflows** call at runtime.[^s4] Deployment through **change sets** or the **Metadata API** creates versions in the target, and **Process Automation Settings** controls whether they arrive active.[^s5][^s6] **Flow Trigger Explorer** is another place admins see and switch versions of record-triggered flows. The per-flow version cap sits among the wider flow limits.[^s1]

## Sources

[^s1]: Salesforce Help, "General Flow Limits". https://help.salesforce.com/s/articleView?language=en_US&id=flow_considerations_limit.htm&type=0 (accessed 2026-11-09)
[^s2]: Salesforce Help, "Flow Management Considerations". https://help.salesforce.com/s/articleView?id=flow_considerations_manage.htm&language=en_US&type=5 (accessed 2026-11-09)
[^s3]: Salesforce Help, "Flow Version Properties". https://help.salesforce.com/s/articleView?id=sf.flow_ref_properties.htm&language=en_US&type=5 (accessed 2026-11-09)
[^s4]: Salesforce Help, "Subflow Element". https://help.salesforce.com/s/articleView?language=en_US&id=platform.flow_ref_elements_subflow.htm&type=5 (accessed 2026-11-09)
[^s5]: Salesforce Help, "Change Set Considerations for Flows". https://help.salesforce.com/s/articleView?id=sf.flow_considerations_change_sets.htm&language=en_US&type=5 (accessed 2026-11-09)
[^s6]: Salesforce Help, "Deploy Processes and Flows as Active". https://help.salesforce.com/s/articleView?language=en_US&id=platform.flow_distribute_deploy_active.htm&type=5 (accessed 2026-11-09)
