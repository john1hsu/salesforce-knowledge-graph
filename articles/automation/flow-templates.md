---
id: kt:flow-templates
type: Feature
title: Flow Templates
aliases: [flow template, IsTemplate, template flows, packaged flow templates, Use a Template]
domain: automation
summary: >-
  Flows marked with the Template property so that admins in the org, or subscribers of a managed package, can open
  them in Flow Builder, copy them and customize the copy, instead of building the automation from scratch.
release: "Winter '27"
status: current
broader: [kt:flow-builder]
related: [kt:flow-versioning, kt:approval-processes, kt:salesforce-scheduler, kt:screen-flow, kt:custom-metadata-types]
relations:
  - {predicate: consumedBy, object: kt:second-generation-managed-packages}
  - {predicate: queriedWith, object: kt:tooling-api}
sources:
  - id: s1
    title: "Flow | Tooling API Objects"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-tooling/references/tooling-objects/tooling-flow.html
    type: official-docs
    accessed: 2026-11-22
  - id: s2
    title: "Work with Flow Approval Process Templates"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.automate_automated_approvals_build_template.htm&type=5
    type: official-docs
    accessed: 2026-11-22
  - id: s3
    title: "Customize Standard Flow Templates"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=sf.ls_customize_flows.htm&language=en_US
    type: official-docs
    accessed: 2026-11-22
  - id: s4
    title: "Flow Templates"
    publisher: UnofficialSF
    url: https://unofficialsf.com/pauple_helpie/creating-flow-templates/
    type: community
    accessed: 2026-11-22
  - id: s5
    title: "Pre-Built Business Processes: How ISVs Use Flow Templates"
    publisher: Inside the Salesforce Ecosystem (Medium)
    url: https://medium.com/inside-the-salesforce-ecosystem/pre-built-business-processes-how-isvs-use-flow-templates-ddc9910ff93a
    type: community
    accessed: 2026-11-22
created: 2026-11-22
---

# Flow Templates

A **flow template** is a flow version whose Template property is turned on. The flag changes what other people may do with it: anyone who can manage flows can open the template in Flow Builder, copy it, and adapt the copy to their own process.[^s4] In the API the flag is the `IsTemplate` boolean on the Flow object. It has existed since API version 45.0 and defaults to false.[^s1] Templates are how Salesforce, AppExchange partners and admins ship automation as a starting point rather than as a finished, locked component.

## How it works

Templates matter most for packaged flows. A flow installed from a managed package normally can't be viewed or cloned by the subscriber, because the publisher's intellectual property is protected. A packaged flow that is a template is the exception: subscribers can open it in a builder, clone it and customize the clone.[^s1] The Tooling API reflects the same rule. Its `Metadata` field comes back null for managed-package flows unless the flow is a template.[^s1] The same protection applies to standard flows Salesforce provides. Without the Template flag they show a blank canvas. With it, an admin can open the flow and change it, but the changes can't be saved back to the template. They must be saved as a new flow.[^s4]

Templates appear as choices when an admin creates a new flow.[^s4] Salesforce Scheduler is one documented example. Its flows are installed as standard flow templates. The admin goes to Setup, then Flows, then New Flow, chooses **Use a Template**, picks the template and creates an editable flow from it.[^s3] Before activating a Scheduler flow built this way, the admin checks under **Show Advanced** that the flow type is still Salesforce Scheduler Flow, then saves and activates the version.[^s3] Editing these flows needs the Manage Flow permission, and running them needs Run Flows.[^s3]

Flow approval processes use the same mechanism. To make a template, the admin saves the approval process as a new version that has a description, selects **Template** under **Show Advanced**, and saves. An existing approval process can also be converted by editing its version properties.[^s2] Once converted, later changes to the process show up in the template automatically. The template then appears under Templates in the New Automation window, and choosing it opens an editable copy in Flow Builder.[^s2] Approval templates can also be distributed in a managed package, so subscribers can create their own approval processes from them.[^s2]

## Packaging and gotchas

- **A copy is a new flow.** Subscriber changes go into a clone, not the template.[^s4] A push upgrade from the publisher updates only the original template and leaves the subscriber's clone unchanged.[^s5]
- **Hard-coded references break.** Don't make Apex or other components call the template by name, because the clone is what actually runs. ISVs are advised to resolve the flow name through a custom metadata type or pass it in dynamically.[^s5]
- **Ship templates inactive.** Packaging screen-flow templates inactive is recommended. Subscribers then clone and activate their own version.[^s5]
- **Customizing can break variables.** Reordering components or removing steps in a standard template can disrupt the global flow variables it relies on.[^s3]
- **Description is required for approval templates.** An approval process version needs a description before it can be saved as a template.[^s2]

## When to use it

Mark a packaged flow as a template when subscribers are expected to adapt the process, for example to change screens, add fields or insert steps. Leave it as a locked packaged flow when the publisher must control behavior and upgrades. Locked flows keep receiving package upgrades, while template clones belong to the subscriber, who then has to maintain them.[^s1][^s5] Inside one org, a template gives teams a reviewed starting pattern. Each copy then gets its own version history, like any other flow.[^s2][^s4]

## Connections

Templates are a feature of **Flow Builder** and are set on a flow version, so they sit alongside **flow versioning**.[^s2] **Salesforce Scheduler** ships its standard flows as templates.[^s3] ISVs often package **screen flows** as templates, shipped inactive so subscribers activate their own clone.[^s5] **Approval processes** built as flow approval processes can be saved as templates.[^s2] ISVs distribute templates in managed packages such as **second-generation managed packages**, and **custom metadata types** help clones avoid hard-coded references.[^s5] The `IsTemplate` flag is exposed on the Flow object in the **Tooling API**.[^s1]

## Sources

[^s1]: Salesforce Developers, "Flow | Tooling API Objects". https://developer.salesforce.com/docs/platform/api-tooling/references/tooling-objects/tooling-flow.html (accessed 2026-11-22)
[^s2]: Salesforce Help, "Work with Flow Approval Process Templates". https://help.salesforce.com/s/articleView?language=en_US&id=platform.automate_automated_approvals_build_template.htm&type=5 (accessed 2026-11-22)
[^s3]: Salesforce Help, "Customize Standard Flow Templates". https://help.salesforce.com/apex/HTViewHelpDoc?id=sf.ls_customize_flows.htm&language=en_US (accessed 2026-11-22)
[^s4]: UnofficialSF, "Flow Templates". https://unofficialsf.com/pauple_helpie/creating-flow-templates/ (accessed 2026-11-22)
[^s5]: Inside the Salesforce Ecosystem, "Pre-Built Business Processes: How ISVs Use Flow Templates". https://medium.com/inside-the-salesforce-ecosystem/pre-built-business-processes-how-isvs-use-flow-templates-ddc9910ff93a (accessed 2026-11-22)
