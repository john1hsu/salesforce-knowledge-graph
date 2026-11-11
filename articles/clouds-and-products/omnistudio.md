---
id: kt:omnistudio
type: Feature
title: Omnistudio
aliases: [OmniStudio, Salesforce Omnistudio, Vlocity OmniStudio, Omnistudio for Managed Packages]
domain: clouds-and-products
summary: >-
  Salesforce's low-code suite for guided, industry-specific digital experiences, made of FlexCards and
  Omniscripts for the UI and Integration Procedures and Data Mappers for server-side data work; it began in the
  Vlocity managed packages and now runs natively on the platform's standard runtime and standard data model.
release: "Winter '27"
status: current
broader: [kt:salesforce-industries]
related: [kt:screen-flow, kt:experience-cloud, kt:public-sector-solutions, kt:health-cloud, kt:omnistudio-developer-certification, kt:omnistudio-consultant-certification]
relations:
  - {predicate: dependsOn, object: kt:lightning-web-components}
  - {predicate: integratesWith, object: kt:business-rules-engine}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: configuredVia, object: kt:salesforce-cli}
  - {predicate: alternativeTo, object: kt:flow-builder}
sources:
  - id: s1
    title: "Get to Know Omnistudio and Its Features (Omnistudio Development Essentials)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/omnistudio-development-essentials/get-to-know-omnistudio-and-its-features
    type: official-learning
    accessed: 2026-11-11
  - id: s2
    title: "Explore Data Mapper Integration Within Omnistudio (Omnistudio Data Mapper Fundamentals)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/omnistudio-data-mapper-fundamentals/explore-data-mapper-integration-within-omnistudio
    type: official-learning
    accessed: 2026-11-11
  - id: s3
    title: "OmniStudioSettings (Industries Common Resources Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_omnistudiosettings.htm
    type: official-docs
    accessed: 2026-11-11
  - id: s4
    title: "Migrate from Managed Package Runtime to the Omnistudio Standard Runtime"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2026/08/migrate-from-managed-package-runtime-to-the-omnistudio-standard-runtime
    type: official-blog
    accessed: 2026-11-11
  - id: s5
    title: "Automate Your Move to the Omnistudio Standard Runtime with the New Migration Assistant"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2025/12/automate-your-move-to-the-omnistudio-standard-runtime-with-the-new-migration-assistant
    type: official-blog
    accessed: 2026-11-11
  - id: s6
    title: "Prepare for Your Salesforce Omnistudio Developer Certification (trail)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/content/learn/trails/prepare-for-your-salesforce-omnistudio-developer-certification
    type: official-learning
    accessed: 2026-11-11
  - id: s7
    title: "Prepare for Your Salesforce Omnistudio Consultant Certification (trail)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/trails/prepare-for-your-salesforce-omnistudio-consultant-certification
    type: official-learning
    accessed: 2026-11-11
created: 2026-11-11
---

# Omnistudio

Omnistudio is a suite of declarative tools and services for building guided, omnichannel business processes on Salesforce. Salesforce organizes it into three layers: a Digital Experience layer for the user interface, a Service Management layer for data retrieval and transformation, and a Developer Experience layer for moving components between orgs.[^s1] It is the shared UI-and-data toolkit of the Industry Clouds, and Industry Cloud licenses include the full suite along with prebuilt industry components that teams customize rather than build from scratch.[^s1]

## Components

The four core building blocks map onto the first two layers.[^s1][^s2]

- **FlexCards** show contextual information and actions at a glance, as cards on record pages, consoles or sites.[^s1]
- **Omniscripts** guide a user step by step through a process such as an application, enrollment or claim.[^s1]
- **Integration Procedures** are declarative server-side processes that run many actions in a single server call.[^s1]
- **Data Mappers** read, transform and write data; the types are Turbo Extract, Extract, Transform and Load.[^s1][^s2]

FlexCards and Omniscripts are built on Lightning Web Components, can be placed on Experience Cloud sites, and through the OmniOut feature can also be embedded in third-party websites.[^s1] A typical pattern has a FlexCard call a Turbo Extract or Extract to fetch display data, an Omniscript load its data JSON from an Extract and save it with a Load, and an Integration Procedure chain several Data Mappers, branches and external calls into one reusable server-side unit.[^s2] Trailhead's guidance is to pick the lightest Data Mapper type for the job and to centralize Data Mapper calls inside Integration Procedures for reuse and performance; Data Mappers also apply field-level security automatically.[^s2] Design Assistant flags component-health and complexity problems in the designers, and OmniAnalytics tracks how users interact with Omniscripts and FlexCards.[^s1]

## Managed package vs. standard runtime

Omnistudio began as **Omnistudio for Managed Packages**, the Vlocity-era version that stores definitions in custom objects of the industry packages (for example `OmniScript__c` and `DRBundle__c`).[^s1][^s4] The newer Omnistudio is built into the core platform: it uses standard designers, the standard runtime and a standard data model in which Omniscripts live in `OmniProcess`, Data Mappers in `OmniDataTransform` and FlexCards in `OmniUiCard`.[^s1][^s4] An **Omnistudio Hybrid** option lets managed-package orgs build with the standard designers and runtime.[^s1] Salesforce says that since Summer '25 Omnistudio has been package-free for new customers, and that its long-term aim is to move everyone to the standard runtime and retire the packages, without giving a sunset date.[^s4]

The standard runtime works only with the standard data model.[^s4] Salesforce's internal testing averaged roughly 2.1 seconds on it versus about 5.1 seconds on a managed-package runtime.[^s4] Org-level switches live in the `OmniStudioSettings` metadata type, including `enableStandardOmniStudioRuntime` and `enableOmniStudioMetadata`; the latter exposes Omnistudio components to the Metadata and Tooling APIs and cannot be turned off once enabled.[^s3]

## Migration and deployment

The **Omnistudio Migration Assistant** is a Salesforce CLI plugin with an assess mode that reports blockers and a migrate mode that converts components to the standard data model and rewrites references.[^s5][^s4] Some work stays manual: Angular-based Omniscripts must first be rebuilt as LWC Omniscripts, calculation procedures and matrices move to Business Rules Engine, and industry-specific custom objects are not mapped automatically, which the Salesforce blog calls an often-underestimated effort.[^s5][^s4] Standard-runtime component names may not contain special characters such as underscores, so stripping them can produce duplicate Data Mapper names that assess mode flags.[^s5] After migration, deployment uses Salesforce CLI and standard metadata rather than the Vlocity Build Tool, and orgs on the Vlocity packages must be on Winter '26 or later before migrating.[^s4][^s1]

## When to use it

Omnistudio fits multi-step, data-heavy, customer- or agent-facing processes in Industry Cloud orgs, especially where prebuilt industry components already exist.[^s1] Outside those licenses, Screen Flow in Flow Builder is the platform-wide alternative for guided processes. Salesforce offers Omnistudio Developer and Omnistudio Consultant certifications; both preparation trails cover FlexCards, Omniscripts, Integration Procedures and Data Mappers, with the consultant trail adding best-fit solution design.[^s6][^s7]

## Connections

Omnistudio is part of [[kt:salesforce-industries]] and is used across Industry Clouds such as [[kt:public-sector-solutions]] and [[kt:health-cloud]].[^s1] Its UI components depend on [[kt:lightning-web-components]] and run on [[kt:experience-cloud]] sites.[^s1] It integrates with [[kt:business-rules-engine]], which takes over the old calculation procedures and matrices.[^s5] In the standard runtime it is configured and deployed through [[kt:metadata-api]] and [[kt:salesforce-cli]].[^s3][^s4] It is an alternative to [[kt:flow-builder]] and [[kt:screen-flow]] for guided processes, and its skills are certified by [[kt:omnistudio-developer-certification]] and [[kt:omnistudio-consultant-certification]].[^s6][^s7]

## Sources

[^s1]: Trailhead, "Get to Know Omnistudio and Its Features". https://trailhead.salesforce.com/content/learn/modules/omnistudio-development-essentials/get-to-know-omnistudio-and-its-features (accessed 2026-11-11)
[^s2]: Trailhead, "Explore Data Mapper Integration Within Omnistudio". https://trailhead.salesforce.com/content/learn/modules/omnistudio-data-mapper-fundamentals/explore-data-mapper-integration-within-omnistudio (accessed 2026-11-11)
[^s3]: Salesforce Developers, "OmniStudioSettings". https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/meta_omnistudiosettings.htm (accessed 2026-11-11)
[^s4]: Salesforce Developers Blog, "Migrate from Managed Package Runtime to the Omnistudio Standard Runtime". https://developer.salesforce.com/blogs/2026/08/migrate-from-managed-package-runtime-to-the-omnistudio-standard-runtime (accessed 2026-11-11)
[^s5]: Salesforce Developers Blog, "Automate Your Move to the Omnistudio Standard Runtime with the New Migration Assistant". https://developer.salesforce.com/blogs/2025/12/automate-your-move-to-the-omnistudio-standard-runtime-with-the-new-migration-assistant (accessed 2026-11-11)
[^s6]: Trailhead, "Prepare for Your Salesforce Omnistudio Developer Certification". https://trailhead.salesforce.com/en/content/learn/trails/prepare-for-your-salesforce-omnistudio-developer-certification (accessed 2026-11-11)
[^s7]: Trailhead, "Prepare for Your Salesforce Omnistudio Consultant Certification". https://trailhead.salesforce.com/content/learn/trails/prepare-for-your-salesforce-omnistudio-consultant-certification (accessed 2026-11-11)
