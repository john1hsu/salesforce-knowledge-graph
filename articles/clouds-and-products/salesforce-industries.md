---
id: kt:salesforce-industries
type: Product
title: Salesforce Industries
aliases: [Vlocity, Industry Clouds, Salesforce Industry Clouds, Industries clouds]
domain: clouds-and-products
summary: >-
  The family of industry-specific Salesforce clouds that grew out of the 2020 Vlocity acquisition, built on the
  Salesforce Platform with industry data models and a shared layer of common features such as Omnistudio,
  Context Service and Business Rules Engine.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:public-sector-solutions, kt:revenue-cloud, kt:financial-services-cloud]
relations:
  - {predicate: hasPart, object: kt:omnistudio}
  - {predicate: hasPart, object: kt:context-service}
  - {predicate: hasPart, object: kt:business-rules-engine}
  - {predicate: acquiredBy, object: kt:salesforce-inc}
  - {predicate: queriedWith, object: kt:connect-api}
sources:
  - id: s1
    title: "Get Started with Industries Common Developer Resources (Industries Common Resources Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/salesforce_industries_dev_guide.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s2
    title: "Vlocity: Powering the Future of Salesforce Industries"
    publisher: Salesforce
    url: https://www.salesforce.com/news/stories/vlocity-powering-the-future-of-salesforce-industries/
    type: official-blog
    accessed: 2026-11-09
  - id: s3
    title: "Introducing Salesforce Industries and OmniStudio for Architects"
    publisher: Salesforce Architects
    url: https://medium.com/salesforce-architects/introducing-salesforce-industries-and-omnistudio-for-architects-d0063f4a6cb8
    type: official-blog
    accessed: 2026-11-09
  - id: s4
    title: "Get to Know Omnistudio and Its Features (Omnistudio Development Essentials)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/omnistudio-development-essentials/get-to-know-omnistudio-and-its-features
    type: official-learning
    accessed: 2026-11-09
  - id: s5
    title: "Migrate from Managed Package Runtime to the Omnistudio Standard Runtime"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2026/08/migrate-from-managed-package-runtime-to-the-omnistudio-standard-runtime
    type: official-blog
    accessed: 2026-11-09
  - id: s6
    title: "Omnistudio (Industries Common Resources Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/industries/industries-common-dev/guide/omnistudio-overview.html
    type: official-docs
    accessed: 2026-11-09
created: 2026-11-09
---

# Salesforce Industries

Salesforce Industries is the umbrella for Salesforce's vertical clouds. These are products for financial services, health, public sector, communications, media, energy and utilities, insurance, manufacturing and consumer goods, built on the Salesforce Platform.[^s3] The name comes from Vlocity, an independent vendor of industry-specific cloud and mobile software that was already native to the platform. Salesforce closed its acquisition of Vlocity on June 1, 2020, and the business was renamed Salesforce Industries. Vlocity's founder, David Schmaier, became CEO of Industries at Salesforce.[^s2] Today the term covers both the older Vlocity-derived managed packages and the newer industry clouds delivered natively on the core platform, many of which now carry Agentforce branding, such as Agentforce Financial Services and Agentforce Health.[^s5]

## How it is structured

Salesforce Architects describe the offering as layers on top of the core platform and standard object model:[^s3]

- **Industry data models.** Sector-specific objects that are additive. They extend standard objects or add new ones rather than duplicating existing entities. The insurance model, for example, covers producers, products, rating and quoting, policies and claims.
- **Industry processes.** Prebuilt solutions for sector workflows and their regulatory and security requirements.
- **Omnistudio.** A declarative toolkit for guided, multichannel experiences.[^s3]

Underneath sits a set of **Industries common features**. Salesforce defines these as features included in more than one Industries product. They are documented once in the Industries Common Resources Developer Guide, which covers their data model, APIs, Apex and invocable actions. Product-specific behaviour stays in each cloud's own guide.[^s1] The common features include:

- Business Rules Engine and Context Service
- Data Processing Engine and Batch Management
- Discovery Framework, Action Launcher and Actionable Segmentation
- Intelligent Document Reader, Identity Verification and Timeline
- Omnistudio itself[^s1]

Omnistudio is described as services, components and data model objects that together make up Industry Cloud applications. It is available in Lightning Experience in Enterprise, Unlimited and Developer editions. Its Business REST APIs follow conventions similar to Connect REST API, and some are also exposed as Apex.[^s6]

## Managed package versus standard runtime

The original Vlocity products shipped as native managed packages that added industry functionality to an existing org.[^s3] Omnistudio for Managed Packages was the version designed for Industry Clouds. Industry Cloud licences include Omnistudio plus prebuilt, customisable industry components.[^s4] Salesforce has since built a standard version into the core platform. It uses standard objects and standard designers, and a hybrid option lets managed-package orgs use the standard designers and runtime.[^s4]

The two runtimes differ in which data model they support:[^s5]

- **Managed package runtime.** The legacy runtime. It supports both the packages' custom objects and the standard data model.[^s5]
- **Standard runtime.** Works only with the standard data model.[^s5]

The legacy packages include the Vlocity packages for Communications, Media and Energy, Insurance and Public Sector, and the Omnistudio Foundation package used with Financial Services Cloud and Health Cloud. New customers have been package-free since Summer '25. Salesforce says it intends to move every customer to the standard runtime and retire the packages, but has published no date. The Omnistudio Migration Assistant, a Salesforce CLI plugin, assesses and migrates orgs, and requires the Vlocity Winter '26 package or later first.[^s5]

## Gotchas and when it fits

- **Check the package model before designing.** Two Industries orgs can differ in their data model (custom package objects vs. standard objects), their deployment tooling (the Omnistudio Build Tool vs. the Salesforce CLI) and their migration path.[^s4][^s5]
- **Prefer standard components.** Architects are advised to extend the industry data model rather than rebuild it, and to favour declarative tools over code.[^s3]
- **Choose the right front end.** Flow suits employee-facing processes, while OmniScript is the suggested default for external users and industry-specific processes.[^s3]

Use an Industries cloud when its data model and processes already match the sector. A generic Sales or Service Cloud build is simpler when only a few industry fields are needed.[^s3]

## Connections

Salesforce Industries has a **broader** node, `kt:salesforce-platform`, because it extends the core platform and object model.[^s3] It **has part** `kt:omnistudio`, its declarative experience layer.[^s6] It also **has part** `kt:context-service` and `kt:business-rules-engine`, two of the common features shared across Industries products.[^s1] Its Business REST APIs are **queried with** `kt:connect-api` conventions.[^s6] The Vlocity business behind it was **acquired by** `kt:salesforce-inc` in 2020.[^s2] It is **related** to `kt:public-sector-solutions`, one of the industry products built on a Vlocity package, and to `kt:revenue-cloud`, which uses several of the same shared Industries features.[^s5][^s1]

## Sources
[^s1]: Salesforce, "Get Started with Industries Common Developer Resources", Industries Common Resources Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.industries_reference.meta/industries_reference/salesforce_industries_dev_guide.htm (accessed 2026-11-09)
[^s2]: Salesforce, "Vlocity: Powering the Future of Salesforce Industries". https://www.salesforce.com/news/stories/vlocity-powering-the-future-of-salesforce-industries/ (accessed 2026-11-09)
[^s3]: Salesforce Architects, "Introducing Salesforce Industries and OmniStudio for Architects". https://medium.com/salesforce-architects/introducing-salesforce-industries-and-omnistudio-for-architects-d0063f4a6cb8 (accessed 2026-11-09)
[^s4]: Trailhead, "Get to Know Omnistudio and Its Features". https://trailhead.salesforce.com/content/learn/modules/omnistudio-development-essentials/get-to-know-omnistudio-and-its-features (accessed 2026-11-09)
[^s5]: Salesforce Developers Blog, "Migrate from Managed Package Runtime to the Omnistudio Standard Runtime". https://developer.salesforce.com/blogs/2026/08/migrate-from-managed-package-runtime-to-the-omnistudio-standard-runtime (accessed 2026-11-09)
[^s6]: Salesforce, "Omnistudio", Industries Common Resources Developer Guide. https://developer.salesforce.com/docs/industries/industries-common-dev/guide/omnistudio-overview.html (accessed 2026-11-09)
