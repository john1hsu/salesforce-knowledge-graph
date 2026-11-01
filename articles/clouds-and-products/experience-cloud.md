---
id: kt:experience-cloud
type: Product
title: Experience Cloud
aliases: [Salesforce Experience Cloud, Community Cloud, Salesforce Communities, Experience Cloud sites, digital experiences]
domain: clouds-and-products
summary: >-
  Salesforce's product for building branded, CRM-connected websites, portals and help centers for customers,
  partners and other external audiences, built in Experience Builder on Aura or LWR templates and secured by
  external user licenses and external sharing settings.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:service-cloud, kt:salesforce-sharing-model, kt:role-hierarchy, kt:knowledge-base, kt:experience-cloud-identity]
relations:
  - {predicate: configuredVia, object: kt:experience-builder}
  - {predicate: dependsOn, object: kt:organization-wide-defaults}
  - {predicate: integratesWith, object: kt:service-cloud}
  - {predicate: dependsOn, object: kt:lightning-web-components}
sources:
  - id: s1
    title: "Experience Cloud Basics: Unlock the Potential of Experience Cloud for Engagement (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/community_cloud_basics/communities_intro_to_community_cloud
    type: official-learning
    accessed: 2026-11-01
  - id: s2
    title: "Experience Cloud Site Strategy: Design Your Site (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/experience-cloud-site-strategy/design-your-site
    type: official-learning
    accessed: 2026-11-01
  - id: s3
    title: "Get to Know the LWR Templates for Experience Cloud"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/exp-cloud-lwr/guide/template-overview.html
    type: official-docs
    accessed: 2026-11-01
  - id: s4
    title: "LWR Sites for Experience Cloud: Differences in Behavior Between LWR and Aura Sites"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.exp_cloud_lwr.meta/exp_cloud_lwr/template_differences.htm
    type: official-docs
    accessed: 2026-11-01
  - id: s5
    title: "Share CRM Data with Your Partners: Set External Organization-Wide Defaults (Trailhead project step)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/communities_share_crm_data/set_external_owd
    type: official-learning
    accessed: 2026-11-01
  - id: s6
    title: "Salesforce Communities Licenses"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2014/02/salesforce-communities-licenses
    type: official-blog
    accessed: 2026-11-01
created: 2026-11-01
---

# Experience Cloud

Experience Cloud is Salesforce's product for publishing branded digital experiences, such as customer portals, help forums, support sites and partner portals, that read and write data in the same org as the internal CRM. Trailhead describes a site as a window into the Salesforce org: the data lives in the org, and admins decide which of it is exposed and to which audiences. One org can host several sites for different purposes, and sites can also surface third-party data such as orders or financial records alongside CRM data.[^s1] The product began as Salesforce Communities, with its own family of community user licenses, and was later sold as Community Cloud before taking its current name.[^s6][^s1]

## How it works

Sites are built in Experience Builder from a template, and the template determines the underlying framework. There are three. **Aura** templates (Customer Service, Partner Central, Help Center, Customer Account Portal and Build Your Own) are largely low-code but can load more slowly. **Lightning Web Runtime (LWR)** templates (Build Your Own and the Microsite template for lead-capturing marketing pages) run on a standards-based web stack and generally need developer effort, because fewer prebuilt components exist. **Visualforce** sites have no templates and are built and maintained entirely in code.[^s2] Salesforce's developer docs say LWR templates are built only on Lightning Web Components. They are designed to load fast and scale, but they ship with only the essential out-of-the-box pages and components and lack some Aura features, so the docs recommend reviewing the limitations before you start.[^s3]

LWR and Aura sites behave differently at runtime. An LWR site's components are fixed when the site is published and served as static content, so changes appear only after you republish. Apart from the initial document request and data API calls, every request needed to load a page is HTTP-cacheable. LWR sites can also drop the `/s` URL segment that Aura sites use, run under Lightning Web Security instead of Lightning Locker, and give you full control over head markup.[^s4]

## Access, licensing and sharing

A site can be unauthenticated, open to anyone on the internet, or authenticated. Authenticated access requires external user licenses, while a public site such as a marketing microsite needs no special licenses. Which licenses to buy depends on who the users are, how many there are, which objects they need, which template the site uses, and the org's edition.[^s2]

Salesforce's original description of the license tiers is still a useful mental model. Customer Community targets high-volume business-to-consumer sites and has no roles or sharing rules, so it relies on sharing sets instead. Customer Community Plus adds roles and sharing rules. Partner Community adds those plus reports and dashboards for business-to-business channel use. Licenses can be member-based, meaning per-user seats, or login-based, meaning monthly login capacity that suits infrequent visitors.[^s6] That description dates from 2014, so confirm current editions and pricing with Salesforce before you design around them.

Record visibility for external users starts with **external organization-wide defaults**, which are set separately from the internal defaults and can never be more permissive. Salesforce recommends setting external defaults to Private and opening access through other mechanisms. Exposing reports and dashboards to external users requires a Private external default. When secure guest user record access is enabled, guest users are not treated as external users: their defaults are fixed at Private, and only sharing rules can grant them access.[^s5]

## Gotchas and when to use it

- **Choosing a framework is a long-term decision.** Aura offers faster low-code delivery, while LWR offers better performance and developer control, at the cost of a thinner component catalog and some feature gaps.[^s2][^s3]
- **Republish after changes.** LWR sites serve what was published, not what was last saved.[^s4]
- **License tier drives your sharing design.** A tier without roles cannot use role- or rule-based sharing, so the data model has to work with sharing sets.[^s6][^s5]

Use Experience Cloud when external users need to see or update CRM records, such as cases, orders or deals. For purely public content, a microsite works without licensed users.[^s2]

## Connections

Experience Cloud is an application of the `kt:salesforce-platform`: sites run in the org itself rather than in a separate system.[^s1] It is closely tied to `kt:service-cloud`, because customer-service portals and help centers backed by a `kt:knowledge-base` are its classic use case.[^s1][^s2] It is configured through `kt:experience-builder`, and its LWR sites depend on `kt:lightning-web-components`.[^s2][^s3] External access is an extension of the `kt:salesforce-sharing-model`. It depends on `kt:organization-wide-defaults` (the external settings), and on the `kt:role-hierarchy` for license tiers that include roles.[^s5][^s6] How external users sign in to sites is covered in `kt:experience-cloud-identity`.

## Sources

[^s1]: Trailhead, "Experience Cloud Basics: Unlock the Potential of Experience Cloud for Engagement". https://trailhead.salesforce.com/content/learn/modules/community_cloud_basics/communities_intro_to_community_cloud (accessed 2026-11-01)
[^s2]: Trailhead, "Experience Cloud Site Strategy: Design Your Site". https://trailhead.salesforce.com/content/learn/modules/experience-cloud-site-strategy/design-your-site (accessed 2026-11-01)
[^s3]: Salesforce Developers, "Get to Know the LWR Templates for Experience Cloud". https://developer.salesforce.com/docs/platform/exp-cloud-lwr/guide/template-overview.html (accessed 2026-11-01)
[^s4]: Salesforce Developers, "LWR Sites for Experience Cloud: Differences in Behavior Between LWR and Aura Sites". https://developer.salesforce.com/docs/atlas.en-us.exp_cloud_lwr.meta/exp_cloud_lwr/template_differences.htm (accessed 2026-11-01)
[^s5]: Trailhead, "Share CRM Data with Your Partners: Set External Organization-Wide Defaults". https://trailhead.salesforce.com/content/learn/projects/communities_share_crm_data/set_external_owd (accessed 2026-11-01)
[^s6]: Salesforce Developers Blog, "Salesforce Communities Licenses" (2014). https://developer.salesforce.com/blogs/2014/02/salesforce-communities-licenses (accessed 2026-11-01)
