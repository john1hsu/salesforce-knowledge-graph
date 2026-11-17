---
id: kt:instance-refresh-and-org-migration
type: Concept
title: Instance Refresh and Org Migration
aliases: [instance refresh, org migration, org split, instance split, instance migration]
domain: platform-architecture
summary: >-
  Salesforce-run maintenance that moves orgs onto different infrastructure: an instance refresh moves a whole
  instance, an org migration moves one org to another instance (for example to Hyperforce). Both change the
  instance name and hostnames, so instance-specific references and allowlists must be cleaned up beforehand.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform, kt:multitenancy]
related: [kt:trust-and-status-site, kt:my-domain, kt:hyperforce, kt:heroku-connect, kt:login-ip-ranges-and-trusted-ip-ranges]
relations:
  - {predicate: contrastsWith, object: kt:sandbox-types}
  - {predicate: configuredVia, object: kt:hyperforce-assistant}
sources:
  - id: s1
    title: "Salesforce maintenance windows and notifications (Knowledge Article 000176208)"
    publisher: Salesforce Help
    url: https://help.salesforce.com/HTViewSolution?id=000176208
    type: official-docs
    accessed: 2026-11-17
  - id: s2
    title: "Update Your Salesforce Org for Your New Domain (Identity Implementation Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/domain_name_guidelines.htm
    type: official-docs
    accessed: 2026-11-17
  - id: s3
    title: "Supporting Org Migrations (ISV Technical Enablement Plugin)"
    publisher: Salesforce
    url: https://forcedotcom.github.io/isvte-sfdx-plugin/en/usage/orgmigration
    type: official-docs
    accessed: 2026-11-17
  - id: s4
    title: "Upgrade to Hyperforce with Confidence Using Hyperforce Assistant"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2023/upgrade-to-hyperforce-with-confidence-using-hyperforce-assistant
    type: official-blog
    accessed: 2026-11-17
  - id: s5
    title: "What do I need to do about my upcoming Salesforce instance refresh?"
    publisher: Heroku Help
    url: https://help.heroku.com/0HFMVV4B/what-do-i-need-to-do-about-my-upcoming-salesforce-instance-refresh
    type: official-docs
    accessed: 2026-11-17
  - id: s6
    title: "Prepare Your AppExchange App to Support Org Migrations"
    publisher: Inside the Salesforce Ecosystem (Medium)
    url: https://medium.com/inside-the-salesforce-ecosystem/appexchange-app-org-migrations-e49aa0c5231e
    type: community
    accessed: 2026-11-17
created: 2026-11-17
---

# Instance Refresh and Org Migration

Every Salesforce org lives on an **instance** (a pod such as NA12) inside Salesforce's shared, multitenant infrastructure. From time to time Salesforce moves orgs to different infrastructure, and the two forms customers hear about most are the **instance refresh** and the **org migration**. In both cases the instance-specific hostname of the org changes, for example away from a host such as na12.salesforce.com.[^s4][^s5] Anything that assumed the org would stay put, from hard-coded links to firewall rules, can break.

## Instance refresh vs. org migration

- **Instance refresh**: Salesforce-scheduled maintenance on an instance that changes the hostname of the orgs on it and leaves them read-only while it runs.[^s5]
- **Org migration**: a single org moves to a different instance, either within the same data center or from first-party data centers to public-cloud infrastructure such as Hyperforce or Government Cloud.[^s6]

The Hyperforce programme made org migrations routine: Salesforce is retiring its own data centers and moving every customer onto Hyperforce, at no extra charge, with admins responsible for getting their orgs ready.[^s4]

## What happens during the window

Instance refreshes are scheduled maintenance. Salesforce tends to plan maintenance for the first and third weekends of the month within instance-specific windows, and users often keep read-only access to their data while it runs.[^s1] A refresh specifically puts the org in read-only mode, so integrations that write to Salesforce must retry or pause until it ends.[^s5]

Notice comes through several channels. For maintenance that needs customer action, such as updating network settings and hard-coded references before an instance refresh, Salesforce aims to email admins months ahead; instance-wide Trust Notifications go out about ten days before, and emergency maintenance can come with under a week's notice.[^s1]

## What breaks, and how to prepare

The common failure is code or configuration that names a specific instance. Salesforce's ISV tooling warns that URLs such as na144.salesforce.com tie code to one instance and can make a customer's org migration fail; it recommends My Domain or login URLs instead.[^s3]

Preparation checklist:

- **Remove hard-coded instance URLs** from Apex, Visualforce, custom apps and email templates; point them at the My Domain URL.[^s2][^s3]
- **Build URLs dynamically**: relative links inside the org, and URLFOR or the Apex URL class when code must generate them.[^s6]
- **Let API clients follow the login response**: use the server URL returned at login rather than a stored host name.[^s2]
- **Update firewalls and proxies** that filter by hostname or IP so they allow all published Salesforce ranges and domains, which Hyperforce requires.[^s2][^s6]
- **Use My Domain for streaming clients** so subscriptions survive instance refreshes and org migrations.[^s2]

For Hyperforce moves specifically, **Hyperforce Assistant** in Setup turns these checks into a guided checklist, scanning code for hard-coded references and testing connectivity to the target instance; the Hyperforce-specific schedule and gotchas are covered under `kt:hyperforce`.[^s4]

Connected systems need attention too. Heroku Connect, for example, authorizes against the org's hostname: without My Domain it must be re-authorized after a refresh, while a My Domain hostname avoids that step.[^s5] AppExchange partners are told never to assume where an org lives and to document that customer extensions can reintroduce hard-coded references.[^s6]

## Connections

This is an operational concern of `kt:salesforce-platform` and a direct consequence of `kt:multitenancy`: orgs share instances whose infrastructure Salesforce maintains and replaces on its own schedule.[^s1][^s6] `kt:my-domain` is the main defence, because a stable My Domain hostname outlives instance changes,[^s2][^s5] and `kt:hyperforce` is the destination behind most current org migrations, prepared with `kt:hyperforce-assistant`.[^s4] `kt:trust-and-status-site` publishes the maintenance and sends the notifications.[^s1] An instance refresh is Salesforce-scheduled maintenance announced on that site, not the customer-initiated sandbox refresh described under `kt:sandbox-types`, though the two are easily confused by name.[^s1] `kt:heroku-connect` and IP-based controls such as `kt:login-ip-ranges-and-trusted-ip-ranges` are typical dependencies to re-check.[^s5][^s6]

## Sources
[^s1]: Salesforce Help, "Salesforce maintenance windows and notifications (Knowledge Article 000176208)". https://help.salesforce.com/HTViewSolution?id=000176208 (accessed 2026-11-17)
[^s2]: Salesforce, "Update Your Salesforce Org for Your New Domain". https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/domain_name_guidelines.htm (accessed 2026-11-17)
[^s3]: Salesforce, "Supporting Org Migrations (ISV Technical Enablement Plugin)". https://forcedotcom.github.io/isvte-sfdx-plugin/en/usage/orgmigration (accessed 2026-11-17)
[^s4]: Salesforce Admins Blog, "Upgrade to Hyperforce with Confidence Using Hyperforce Assistant". https://admin.salesforce.com/blog/2023/upgrade-to-hyperforce-with-confidence-using-hyperforce-assistant (accessed 2026-11-17)
[^s5]: Heroku Help, "What do I need to do about my upcoming Salesforce instance refresh?". https://help.heroku.com/0HFMVV4B/what-do-i-need-to-do-about-my-upcoming-salesforce-instance-refresh (accessed 2026-11-17)
[^s6]: Inside the Salesforce Ecosystem, "Prepare Your AppExchange App to Support Org Migrations". https://medium.com/inside-the-salesforce-ecosystem/appexchange-app-org-migrations-e49aa0c5231e (accessed 2026-11-17)
