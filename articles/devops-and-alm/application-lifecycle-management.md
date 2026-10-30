---
id: kt:application-lifecycle-management
type: Concept
title: Application Lifecycle Management
aliases: [ALM, Salesforce ALM, Salesforce application lifecycle]
domain: devops-and-alm
summary: >-
  The set of tools and methodologies that carry a Salesforce change from requirement to production and beyond,
  organised as plan, build, test, deploy and monitor phases and shaped by the team's chosen development model
  (org-based or package-based).
release: "Winter '27"
status: concept
broader: [kt:well-architected-framework]
related: [kt:sandbox-types, kt:unlocked-packages, kt:scratch-orgs, kt:environment-strategy]
relations:
  - {predicate: hasPart, object: kt:source-tracking}
  - {predicate: configuredVia, object: kt:devops-center}
  - {predicate: enables, object: kt:salesforce-dx}
  - {predicate: contrastsWith, object: kt:agent-development-lifecycle}
sources:
  - id: s1
    title: "Learn About Salesforce Application Lifecycle Management"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-application-lifecycle-management-quick-look/learn-about-salesforce-application-lifecycle-management
    type: official-learning
    accessed: 2026-10-30
  - id: s2
    title: "Imagine a New Source of Truth (Salesforce DX Development Model)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/sfdx_dev_model/sfdx_dev_model_neworganization
    type: official-learning
    accessed: 2026-10-30
  - id: s3
    title: "Say Hello to Lifecycle Center (DevOps Center Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/devops-center-quick-look/say-hello-to-devops-center
    type: official-learning
    accessed: 2026-10-30
  - id: s4
    title: "Salesforce DX Developer Guide: Unlocked Packages"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.254.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_pkg_intro.htm
    type: official-docs
    accessed: 2026-10-30
  - id: s5
    title: "Org Development Model (Salesforce Extensions for VS Code)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/orgdev.html
    type: official-docs
    accessed: 2026-10-30
  - id: s6
    title: "Make Solutions Adaptable (Salesforce Well-Architected module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-well-architected/make-solutions-adaptable
    type: official-learning
    accessed: 2026-10-30
created: 2026-10-30
---

# Application Lifecycle Management

Application Lifecycle Management (ALM) is the discipline that governs how a Salesforce change travels from an idea to production and how it is watched once it gets there. Trailhead defines it as the tools and methodologies that manage an application's life from design through final release.[^s1] On Salesforce the term covers far more than code: declarative configuration, flows, permission sets and even configuration data all move through the same lifecycle, so ALM is as much an admin concern as a developer one.[^s1][^s3]

## The five phases

Salesforce frames every change as passing through five phases.[^s1]

1. **Plan.** Capture clear requirements and the business reason for the change, and organise the work into projects and pipelines that mirror the team's release process.[^s1]
2. **Build.** Make the change in an isolated development environment rather than in production, keeping it on a feature branch until it is ready to share.[^s1]
3. **Test.** Validate the change at each pipeline stage and surface conflicts with other work before it reaches production.[^s1]
4. **Deploy.** Promote tested changes from stage to stage through a repeatable, tracked process that leaves an audit trail of what shipped, when and by whom.[^s1]
5. **Monitor.** Review which components and versions were deployed and by whom, and use DORA delivery metrics to find bottlenecks in the process itself.[^s1]

Salesforce pairs these phases with DevOps principles: continuous delivery, automation, shared responsibility and feedback loops.[^s1]

## Development models: where the truth lives

The most consequential ALM decision is the **source of truth**. In the org-based model, the production org is the authoritative record of all code and customisation. Teams build in sandboxes and ship everything together in a single deployment described by one `package.xml` manifest.[^s2] Developers typically work in a Developer sandbox or Developer Edition org, use other sandbox types for integration, testing and staging, and deploy sets of changes through those orgs toward production.[^s5]

In the package-based model the source control repository becomes the source of truth. Developers create scratch orgs from repository source, track what they change there, and pull it back into version control. Teams own individual packages, declare dependencies between them, and release each package on its own schedule.[^s2] Salesforce recommends unlocked packages for most internal business apps and second-generation managed packages for AppExchange distribution. Each package is defined in `sfdx-project.json`, which records its version, dependencies, features and org settings.[^s4]

## Tooling

Lifecycle Center, previously called DevOps Center, is Salesforce's built-in tool for running this lifecycle with clicks or with the Salesforce CLI. It manages branches in a source control repository, tracks each change as a work item, and promotes work items through a release pipeline. It can move configuration data such as custom settings alongside metadata, and its DX Inspector can track changes even in environments without native source tracking.[^s3] You enable it from Setup in a hub org, without installing a package.[^s3]

## Limits and gotchas

- The org-based model tangles unrelated work together. Figuring out what to deploy is often manual, and every project waits for one shared release.[^s2]
- Well-Architected guidance treats a hand-maintained `package.xml` as acceptable only for early-stage or proof-of-concept projects. It also says the same metadata should not be duplicated across packages.[^s6]
- Uninstalling an unlocked package deletes its components, so package boundaries and deprecation plans deserve care up front.[^s4]
- Not every change carries the same risk. Well-Architected recommends different release paths for low-, medium- and high-risk changes, and scale testing for apps with large user counts or data volumes.[^s6]

## When to use which approach

Small teams with modest change volume can run a disciplined org-based process with sandboxes and a tracked pipeline.[^s5][^s3] As an org grows and several teams ship in parallel, the package-based model pays off. It brings clearer dependencies, versioning, CI/CD support and independent releases, at the price of planning how to carve the org into packages.[^s2][^s4] Whichever model is chosen, tie each feature to a named release so stakeholders know when it will land.[^s6]

## Connections

ALM sits **under** `kt:well-architected-framework`, whose Adaptable guidance covers release planning, risk-based release paths and packaging hygiene.[^s6] It **has part** `kt:source-tracking`, which lets changes made in development orgs flow back to version control.[^s2][^s3] It is **configured via** `kt:devops-center` (now Lifecycle Center) and **enables** the `kt:salesforce-dx` source-driven toolchain.[^s3][^s4] It is **related** to `kt:sandbox-types` and `kt:scratch-orgs`, the environments each phase runs in, to `kt:unlocked-packages`, the package type for internal apps, and to `kt:environment-strategy`.[^s2][^s4][^s5] It **contrasts with** `kt:agent-development-lifecycle`; read the two together to see how agent delivery departs from the plan, build, test, deploy and monitor pipeline described here.[^s1]

## Sources

[^s1]: Trailhead, "Learn About Salesforce Application Lifecycle Management". https://trailhead.salesforce.com/content/learn/modules/salesforce-application-lifecycle-management-quick-look/learn-about-salesforce-application-lifecycle-management (accessed 2026-10-30)
[^s2]: Trailhead, "Imagine a New Source of Truth". https://trailhead.salesforce.com/content/learn/modules/sfdx_dev_model/sfdx_dev_model_neworganization (accessed 2026-10-30)
[^s3]: Trailhead, "Say Hello to Lifecycle Center". https://trailhead.salesforce.com/content/learn/modules/devops-center-quick-look/say-hello-to-devops-center (accessed 2026-10-30)
[^s4]: Salesforce, "Salesforce DX Developer Guide: Unlocked Packages". https://developer.salesforce.com/docs/atlas.en-us.254.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_pkg_intro.htm (accessed 2026-10-30)
[^s5]: Salesforce, "Org Development Model". https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/orgdev.html (accessed 2026-10-30)
[^s6]: Trailhead, "Make Solutions Adaptable". https://trailhead.salesforce.com/content/learn/modules/salesforce-well-architected/make-solutions-adaptable (accessed 2026-10-30)
