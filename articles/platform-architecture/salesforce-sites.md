---
id: kt:salesforce-sites
type: Feature
title: Salesforce Sites
aliases: [Force.com Sites, Salesforce Platform Sites, public Visualforce sites, salesforce-sites.com sites]
domain: platform-architecture
summary: >-
  A platform feature for publishing public, login-free websites and web apps built from Visualforce pages that run on
  Salesforce servers against the org's own data, metered by daily bandwidth, service request time and monthly page views.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:custom-domains, kt:static-resources, kt:trust-and-status-site, kt:organization-wide-defaults]
relations:
  - {predicate: dependsOn, object: kt:visualforce}
  - {predicate: dependsOn, object: kt:my-domain}
  - {predicate: alternativeTo, object: kt:experience-cloud}
  - {predicate: configuredVia, object: kt:custom-domains}
  - {predicate: queriedWith, object: kt:apex}
sources:
  - id: s1
    title: "Salesforce Sites"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=platform.sites_overview.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-23
  - id: s2
    title: "Salesforce Sites Usage and Billing"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&amp=&id=sites_limits.htm&type=0
    type: official-docs
    accessed: 2026-11-23
  - id: s3
    title: "Set Up Salesforce Sites"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=platform.sites_setup_overview.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-23
  - id: s4
    title: "Create Public Websites Using Salesforce Sites on the Salesforce Platform"
    publisher: Salesforce Help (Knowledge Article 000385457)
    url: https://help.salesforce.com/s/articleView?id=000385457&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-23
  - id: s5
    title: "Salesforce Sites (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.248.0.apexcode.meta/api/apex_forcecom_sites.htm
    type: official-docs
    accessed: 2026-11-23
  - id: s6
    title: "Protecting Your Data: Essential Actions to Secure Experience Cloud Guest User Access"
    publisher: Salesforce Security blog
    url: https://www.salesforce.com/blog/protecting-your-data-essential-actions-to-secure-experience-cloud-guest-user-access/
    type: official-blog
    accessed: 2026-11-23
created: 2026-11-23
---

# Salesforce Sites

Salesforce Sites (historically Force.com Sites) lets an org publish public websites and applications that are tied directly to its data and need no visitor login. Pages are built in Visualforce, served from Salesforce's own servers, and can carry the company's branding; a public site can also hand off to a portal for login or self-registration.[^s1] Sites is available in Developer, Enterprise, Performance and Unlimited editions, in both Salesforce Classic and Lightning Experience, and is subject to additional terms of use.[^s1][^s3]

## How it works

Setup is short: enable Sites from Setup, create and configure a site, associate Visualforce pages (and use, hide or replace the standard and error pages), choose a site template, optionally connect a portal for login, adjust the public access settings, and then click **Activate**. Creating sites needs the Customize Application permission, while editing public access settings needs Manage Users.[^s3] The public access settings govern the site's guest user, so everything an anonymous visitor can read or write is decided by that profile.[^s3]

Every site gets a Salesforce-managed address derived from My Domain, such as `MyDomainName.my.salesforce-sites.com` in production, with separate formats for sandboxes and Developer Edition orgs. A branded custom domain points a CNAME at a target that contains the org's 18-character ID and the `live.siteforce.com` suffix.[^s1] In Apex, the `Site` and `Cookie` classes manage sites, and built-in URL rewriting can turn record-style URLs into friendlier, search-indexable ones.[^s5]

## Limits and gotchas

Usage is metered three ways. Bandwidth (origin plus cache traffic) and service request time (origin processing time) are tracked per site over a rolling 24 hours, and monthly page views are counted across all sites in the org, which is also the basis for billing.[^s2] Developer Edition allows one site and has no page-view allocation, while Enterprise and Performance allow up to 25 sites; in production those editions get 40 GB of bandwidth and 60 hours of service request time per day, with much smaller sandbox allocations.[^s2]

Page-view counting has sharp edges. Unauthenticated page requests count, including the Authorization Required error page and AJAX traffic such as JavaScript remoting and action pollers, whereas static resources, attachments, images, robots.txt and other error pages do not.[^s2] A site over its daily bandwidth or request-time allocation keeps running only while spare capacity exists, with no service guarantee. If page views run past 110% for four straight months, or reach 300% in a single month, Salesforce can disable the org's sites after notifying administrators.[^s2]

Sites go down with their org: during major-release maintenance visitors see a maintenance page or a custom Service Not Available page. Sites and Experience Cloud sites can share a domain only when enhanced domains are deployed.[^s1] Caching of pages and static resources, efficient and selective SOQL, and load testing at realistic concurrency are the main defences against hitting these allocations.[^s2][^s4]

## When to use it (and when not)

Salesforce's guidance positions Sites for public, unauthenticated experiences: informational pages, store locators or product catalogs built with Visualforce and Apex, and simple apps that capture visitor input into Salesforce records.[^s4] It is a poor fit for heavy file transfer or processing, which strains the daily bandwidth allocation, and confidential data should never be published on it.[^s4] When visitors must log in or content needs password protection, the recommended choice is Experience Cloud rather than Sites.[^s4]

Because anonymous access is the whole point, the guest user is the main risk. Salesforce Security's guidance for Experience Cloud guest users carries over in spirit: start the guest profile from zero access, keep default external access Private, and disable guest API access unless it is truly required.[^s6]

## Connections

Sites is a capability of the `kt:salesforce-platform` and **depends on** `kt:visualforce` for its pages and on `kt:my-domain` for its default address.[^s1] It is **configured via** `kt:custom-domains` when a branded URL is needed, and its server-side logic is written in `kt:apex` using the `Site` class.[^s1][^s5] It is an **alternative to** `kt:experience-cloud`, which Salesforce recommends once authentication enters the picture.[^s4] Related nodes cover `kt:static-resources`, which do not count toward page views; the `kt:trust-and-status-site`, where maintenance windows that take sites offline are published; and `kt:organization-wide-defaults`, whose external access settings bound what guest users can see.[^s1][^s2][^s6]

## Sources

[^s1]: Salesforce Help, "Salesforce Sites". https://help.salesforce.com/s/articleView?id=platform.sites_overview.htm&language=en_US&type=5 (accessed 2026-11-23)
[^s2]: Salesforce Help, "Salesforce Sites Usage and Billing". https://help.salesforce.com/s/articleView?language=en_US&amp=&id=sites_limits.htm&type=0 (accessed 2026-11-23)
[^s3]: Salesforce Help, "Set Up Salesforce Sites". https://help.salesforce.com/s/articleView?id=platform.sites_setup_overview.htm&language=en_US&type=5 (accessed 2026-11-23)
[^s4]: Salesforce Help, "Create Public Websites Using Salesforce Sites on the Salesforce Platform" (000385457). https://help.salesforce.com/s/articleView?id=000385457&language=en_US&type=1 (accessed 2026-11-23)
[^s5]: Salesforce Developers, "Salesforce Sites", Apex Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.248.0.apexcode.meta/api/apex_forcecom_sites.htm (accessed 2026-11-23)
[^s6]: Salesforce Security, "Protecting Your Data: Essential Actions to Secure Experience Cloud Guest User Access". https://www.salesforce.com/blog/protecting-your-data-essential-actions-to-secure-experience-cloud-guest-user-access/ (accessed 2026-11-23)
