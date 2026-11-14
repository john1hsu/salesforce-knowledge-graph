---
id: kt:trust-and-status-site
type: Tool
title: Salesforce Trust and Status Site
aliases: [trust.salesforce.com, status.salesforce.com, Salesforce Trust, Salesforce Status site, Trust Notifications]
domain: platform-architecture
summary: >-
  Salesforce's public transparency site (trust.salesforce.com) and its Status pages (status.salesforce.com), which
  report real-time availability, incidents and maintenance per instance and send subscribable Trust Notifications.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:hyperforce, kt:my-domain, kt:sandbox-types, kt:heroku, kt:security-compliance-frameworks, kt:instance-refresh-and-org-migration]
sources:
  - id: s1
    title: "Get Acquainted with the Critical Incident Center (Critical Incident Management at Salesforce)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/critical-incident-management-at-salesforce/get-acquainted-with-the-critical-incident-center-learn
    type: official-learning
    accessed: 2026-11-14
  - id: s2
    title: "Trust Notification User Guide"
    publisher: Salesforce
    url: https://trust1-public.s3.amazonaws.com/notifiction_guide/en/TrustNotificationGuide.pdf
    type: official-docs
    accessed: 2026-11-14
  - id: s3
    title: "Introducing My Trust Center: Personalized Trust and Status"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2026/introducing-my-trust-center
    type: official-blog
    accessed: 2026-11-14
  - id: s4
    title: "Stay Up-to-Date on Salesforce System Availability with Trust Notifications"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2017/stay-date-salesforce-system-availability-trust-notifications
    type: official-blog
    accessed: 2026-11-14
  - id: s5
    title: "Navigate the Salesforce Trust Site"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/mc_trust/navigate_trust
    type: official-learning
    accessed: 2026-11-14
  - id: s6
    title: "Salesforce Trust is now the primary channel for all Heroku incident and maintenance communications"
    publisher: Heroku Dev Center
    url: https://devcenter.heroku.com/changelog-items/3422
    type: official-docs
    accessed: 2026-11-14
created: 2026-11-14
---

# Salesforce Trust and Status Site

**Salesforce Trust** (trust.salesforce.com) is the public site where Salesforce publishes service health, security and compliance information, and its **Status** pages (status.salesforce.com) show the real-time availability of each instance and product. During an incident it is the primary source of current status, and it also keeps historical status alongside security and compliance material.[^s1] Admins, architects and integration owners use it to tell a platform-side outage apart from a problem in their own org, to plan around scheduled maintenance, and to follow incident updates.

## What the site contains

The Trust site is organised into three areas. **System Status** gives a visual picture of instance health and links to product status sites; most Salesforce products are grouped on the main Salesforce Status site, and Marketing Cloud Engagement health, once on its own site, now appears there too.[^s5] **Security** links to best practices for securing orgs, role-based portals and training. **Compliance** lists the national and international standards Salesforce meets, filterable by country with the relevant compliance badges.[^s5]

Coverage keeps widening: since October 10, 2025, the Salesforce Trust site has been the primary channel for Heroku incident and maintenance communications, with the older Heroku Status site, its API and its emails kept as a parallel backup.[^s6]

## Finding your instance

Status is reported per **instance** (the pod hosting your org), so the first step is knowing which one you are on. The Status site lets you look up an instance by its name, your My Domain, the POD or a MID, or by browsing from a product to its instances.[^s2] Trailhead points admins who don't know their instance to a Salesforce Help knowledge article on viewing instance information for an org.[^s1]

## Trust Notifications

**Trust Notifications** are near real-time emails sent when an instance's availability changes on the Status site, each with a short overview and a link to the incident or maintenance record. They became generally available in June 2017, and anyone can subscribe without a Salesforce user license.[^s4] Events covered include maintenance starting and completing (such as an instance refresh), updates posted during maintenance, detected service disruptions with progress and resolution updates, and optional performance-degradation alerts.[^s4]

Subscribing is self-service: open the Status site, find your instance, choose **Subscribe to Notifications**, confirm through the emailed authentication link, then create an instance or informational subscription and pick the notification types. Service and severity preferences are set per instance, SMS is offered only in some regions, and messages come from alerts@mail.salesforce.com.[^s2]

Gotchas worth knowing:

- After a sandbox refresh, subscribers of the source instance are added to the destination automatically; when an instance is split, subscribers land on both new instances.[^s2]
- An **org migration** does not move your subscription: update it yourself once you learn the new instance.[^s2]
- Trust emails go to whoever subscribed, but incident emails and webinar invitations go only to org admin addresses, so keep admin contacts current.[^s1]

## Incidents and the Critical Incident Center

Salesforce's Critical Incident Center, staffed around the clock, leads major incident response. It updates the Trust site roughly every 30 minutes during an incident, emails org admins once an incident is confirmed and again at restoration, and launches customer webinars within 30 minutes for the most severe events.[^s1]

## My Trust Center

In April 2026 Salesforce introduced **My Trust Center** (my.trust.salesforce.com), an authenticated portal, labelled beta, that shows status, incidents, 90 days of upcoming maintenance, biweekly patch releases and up to a year of history for only your own tenants. Its subscriptions are tenant-level and must be recreated, because legacy notifications don't migrate.[^s3] The public Trust and Status sites keep running in parallel: some products (Agentforce Commerce, Heroku, Slack) aren't in My Trust Center yet, unlicensed users such as partners still need a public view, and teams calling the legacy Trust APIs need time to move. No retirement date for the public Status page has been announced.[^s3]

## Connections

The site sits under `kt:salesforce-platform` as the operational window onto its shared, multitenant infrastructure; it reports health per instance and tenant whatever infrastructure, such as `kt:hyperforce`, hosts them.[^s2][^s3] `kt:my-domain` is one of the lookup keys for finding your instance.[^s2] `kt:sandbox-types` and `kt:instance-refresh-and-org-migration` matter because refreshes and migrations change which instance, and therefore which subscription, applies.[^s2] `kt:heroku` now reports incidents through Salesforce Trust,[^s6] and the Compliance area links to the standards catalogued under `kt:security-compliance-frameworks`.[^s5]

## Sources
[^s1]: Salesforce Trailhead, "Get Acquainted with the Critical Incident Center". https://trailhead.salesforce.com/content/learn/modules/critical-incident-management-at-salesforce/get-acquainted-with-the-critical-incident-center-learn (accessed 2026-11-14)
[^s2]: Salesforce, "Trust Notification User Guide". https://trust1-public.s3.amazonaws.com/notifiction_guide/en/TrustNotificationGuide.pdf (accessed 2026-11-14)
[^s3]: Salesforce Admins Blog, "Introducing My Trust Center: Personalized Trust and Status". https://admin.salesforce.com/blog/2026/introducing-my-trust-center (accessed 2026-11-14)
[^s4]: Salesforce Admins Blog, "Stay Up-to-Date on Salesforce System Availability with Trust Notifications". https://admin.salesforce.com/blog/2017/stay-date-salesforce-system-availability-trust-notifications (accessed 2026-11-14)
[^s5]: Salesforce Trailhead, "Navigate the Salesforce Trust Site". https://trailhead.salesforce.com/content/learn/modules/mc_trust/navigate_trust (accessed 2026-11-14)
[^s6]: Heroku Dev Center, "Salesforce Trust is now the primary channel for all Heroku incident and maintenance communications". https://devcenter.heroku.com/changelog-items/3422 (accessed 2026-11-14)
