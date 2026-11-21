---
id: kt:api-experience-hub
type: Product
title: API Experience Hub
aliases: [Anypoint API Experience Hub, AEH, MuleSoft API Experience Hub, API developer portal]
domain: integration
summary: >-
  MuleSoft's developer-portal product, built on Salesforce Experience Cloud, that publishes APIs, agents, LLMs and MCP
  servers curated in Anypoint Exchange to internal, partner or external developers for self-service discovery,
  access requests and interactive documentation; the successor to API Community Manager.
release: "Winter '27"
status: current
broader: [kt:mulesoft-anypoint-platform]
related: [kt:api-led-connectivity]
relations:
  - {predicate: dependsOn, object: kt:experience-cloud}
  - {predicate: requiresLicense, object: kt:external-identity-license}
  - {predicate: configuredVia, object: kt:experience-builder}
  - {predicate: integratesWith, object: kt:single-sign-on-saml}
  - {predicate: replaces, object: kt:api-community-manager}
sources:
  - id: s1
    title: "API Experience Hub Overview"
    publisher: MuleSoft Documentation (Salesforce)
    url: https://docs.mulesoft.com/api-experience-hub/
    type: official-docs
    accessed: 2026-11-21
  - id: s2
    title: "Getting Started with API Experience Hub"
    publisher: MuleSoft Documentation (Salesforce)
    url: https://docs.mulesoft.com/api-experience-hub/prerequisites
    type: official-docs
    accessed: 2026-11-21
  - id: s3
    title: "Anypoint API Experience Hub Release Notes"
    publisher: MuleSoft Documentation (Salesforce)
    url: https://docs.mulesoft.com/release-notes/api-experience-hub/api-experience-hub-release-notes
    type: official-docs
    accessed: 2026-11-21
  - id: s4
    title: "Increase API Engagement with Anypoint API Experience Hub"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2023/06/increase-api-engagement-with-anypoint-api-experience-hub
    type: official-blog
    accessed: 2026-11-21
  - id: s5
    title: "Salesforce's New API Experience Hub Makes It Easy for Companies to Boost API Adoption"
    publisher: Salesforce Newsroom
    url: https://www.salesforce.com/news/stories/anypoint-api-experience-hub
    type: news
    accessed: 2026-11-21
created: 2026-11-21
---

# API Experience Hub

API Experience Hub (AEH, originally announced as Anypoint API Experience Hub) is MuleSoft's product for building developer portals. A portal is a single place where internal teams, partners or external developers discover and consume an organization's APIs and, increasingly, its AI agents.[^s1] MuleSoft describes it as the next-generation evolution of API Community Manager, and every portal it creates runs on Salesforce Experience Cloud.[^s1] Salesforce announced it on May 2, 2023 as part of MuleSoft's universal API management story, with availability in June 2023.[^s5] The Salesforce Developers Blog covered the release on June 13, 2023.[^s4]

## How it works

Setup starts in Anypoint Platform rather than in Salesforce Setup. An admin assigns permissions, then links an Anypoint organization to a new or existing Salesforce org by choosing the environment type, entering a custom domain if one exists, logging in and allowing permissions.[^s2] Next comes styling the portal from an out-of-the-box template (logos, fonts, color schemes). The admin then curates the catalog by importing services from Anypoint Exchange, sets which versions are visible, approves guest access requests, previews, and publishes.[^s1][^s2] Anypoint Platform handles deployment, catalog and user management, so a team can stand up a portal without deep Salesforce skills.[^s1]

A published portal has three core pages:[^s1]

- **Home**: a banner, title, carousel and navigation by service type.[^s1]
- **Services**: a searchable, filterable catalog of everything the admin has published.[^s1]
- **Service details**: name, type, version, lifecycle state, contact, overview, and documentation with an interactive API console.[^s1]

Developers self-register, search the catalog and download specs. They request access to a service instance, which registers a client application, and then track their apps on a My Applications page.[^s2] Admins can go beyond the template in Experience Builder, which offers drag-and-drop layout and custom Lightning Web Components. They can also enable Chatter feed tracking and Google Analytics.[^s1][^s4]

## Requirements, limits and gotchas

The getting-started guide lists these prerequisites, as verified for Winter '27:[^s2]

- An Anypoint Platform organization in production, plus an Organization Administrator of the main organization.[^s2]
- A Salesforce org on Enterprise, Unlimited or Performance edition.[^s2]
- The System Administrator profile or the `AEH_Anypoint` permission set in the org used for linking.[^s2]
- An API Experience Hub license and at least 2,000 External Identity licenses, which back the package's minimum of 100 service access requests.[^s2]

Missing prerequisites tend to surface as failures during Salesforce linking, so check licenses before the first connection.[^s2] Capacity has grown over time. Portals scaled to 1,000 APIs in February 2025, and from November 2025 new portals scale to 7,000 assets. In May 2026 the 7,000-asset default applied with no opt-in.[^s3] The January 2026 release raised the user-group limit from 20 to 100 and added multi-valued SAML attributes for mapping single sign-on groups.[^s3] The managed package reaches sandboxes at least eight days before production pushes, so test upgrades in a linked sandbox first.[^s3]

## What changed recently

The May 2026 release widened the catalog from classic APIs to agents, LLMs, MCP servers, GraphQL and gRPC services. It also renamed the admin area "API management" to "Catalog management".[^s3] The October 2026 release, pushed to production on October 10, 2026, added OpenAPI 3.1 publishing and console viewing. It also improved Salesforce error messages and fixed member lists to handle up to 500 members.[^s3]

## When to use it (and when not)

Use API Experience Hub when APIs are already designed and governed in Anypoint Platform and need a branded, self-service storefront with access requests and client onboarding. That is the consumption end of an API-led program.[^s4][^s5] It is a heavier choice than a plain documentation site. It needs an Experience Cloud org and external identity licensing, so a team that only needs internal reference docs may be content with Anypoint Exchange alone.[^s1][^s2]

## Connections

API Experience Hub is part of `kt:mulesoft-anypoint-platform`, which manages its catalog and users, and is **related** to `kt:api-led-connectivity`, whose reusable APIs it exposes to consumers.[^s1][^s4] It **depends on** `kt:experience-cloud`, which powers every portal, and is **configured via** `kt:experience-builder` for layout and component customization.[^s1][^s4] It **requires** `kt:external-identity-license` seats for portal users.[^s2] It **integrates with** `kt:single-sign-on-saml` for identity-provider login and SAML-driven group mapping.[^s3] It **replaces** `kt:api-community-manager`, the earlier Experience Cloud-based API portal it evolved from.[^s1]

## Sources

[^s1]: MuleSoft Documentation, "API Experience Hub Overview". https://docs.mulesoft.com/api-experience-hub/ (accessed 2026-11-21)
[^s2]: MuleSoft Documentation, "Getting Started with API Experience Hub". https://docs.mulesoft.com/api-experience-hub/prerequisites (accessed 2026-11-21)
[^s3]: MuleSoft Documentation, "Anypoint API Experience Hub Release Notes". https://docs.mulesoft.com/release-notes/api-experience-hub/api-experience-hub-release-notes (accessed 2026-11-21)
[^s4]: Salesforce Developers Blog, "Increase API Engagement with Anypoint API Experience Hub". https://developer.salesforce.com/blogs/2023/06/increase-api-engagement-with-anypoint-api-experience-hub (accessed 2026-11-21)
[^s5]: Salesforce Newsroom, "Salesforce's New API Experience Hub Makes It Easy for Companies to Boost API Adoption". https://www.salesforce.com/news/stories/anypoint-api-experience-hub (accessed 2026-11-21)
