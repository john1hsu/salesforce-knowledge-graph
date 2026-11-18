---
id: kt:marketing-cloud-next
type: Product
title: Marketing Cloud Next
aliases: [Marketing Cloud Next Growth Edition, Marketing Cloud Next Advanced Edition, Marketing Cloud Growth Edition, Marketing Cloud Advanced Edition, MC Next]
domain: clouds-and-products
summary: >-
  Salesforce's agentic marketing product built natively on the core Salesforce Platform, using Data 360
  (Data Cloud) as its data layer, Flow Builder for orchestration and Agentforce for segment, content and
  campaign assistance; sold as Growth and Advanced editions for B2B, B2C and hybrid marketing.
release: "Winter '27"
status: current
broader: [kt:salesforce-marketing-solutions]
related: [kt:marketing-cloud-account-engagement, kt:loyalty-management, kt:tableau-next, kt:experience-cloud]
relations:
  - {predicate: dependsOn, object: kt:data-cloud}
  - {predicate: dependsOn, object: kt:identity-resolution}
  - {predicate: dependsOn, object: kt:data-graphs}
  - {predicate: configuredVia, object: kt:flow-builder}
  - {predicate: integratesWith, object: kt:agentforce}
  - {predicate: alternativeTo, object: kt:marketing-cloud-engagement}
sources:
  - id: s1
    title: "Get Started with Marketing Cloud Next Channel Marketing"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/channel-marketing-fundamentals-for-marketing-cloud-next/get-started-with-marketing-cloud-next-channel-marketing
    type: official-learning
    accessed: 2026-11-18
  - id: s2
    title: "Explore Marketing Cloud Next Use Cases (Marketing Cloud Next Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-next-basics/explore-marketing-cloud-next-use-cases
    type: official-learning
    accessed: 2026-11-18
  - id: s3
    title: "Prepare Your Org for Email Sending (Marketing Cloud Next Email Sending Essentials)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-next-email-sending-essentials/prepare-your-org-for-email-sending
    type: official-learning
    accessed: 2026-11-18
  - id: s4
    title: "Set Up a Marketing Cloud Next Campaign (Campaign Optimization with Flows in Marketing Cloud Next)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/campaign-optimization-with-flows-in-marketing-cloud-next/set-up-a-marketing-cloud-next-campaign
    type: official-learning
    accessed: 2026-11-18
  - id: s5
    title: "Marketing Cloud Next Documentation Resources"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/marketing/marketing-cloud-growth/guide/mc-resources-documentation.html
    type: official-docs
    accessed: 2026-11-18
  - id: s6
    title: "Prepare for Your Marketing Cloud Next Consultant Certification (trail)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/trails/prepare-for-your-marketing-cloud-next-consultant-certification
    type: official-learning
    accessed: 2026-11-18
  - id: s7
    title: "Salesforce Marketing Cloud Innovations Enable Marketers to Build Lasting Customer Relationships with Actionable Data and AI Agents"
    publisher: Salesforce Newsroom
    url: https://www.salesforce.com/news/?p=81453
    type: news
    accessed: 2026-11-18
created: 2026-11-18
---

# Marketing Cloud Next

Marketing Cloud Next is Salesforce's newer marketing automation product, described by Trailhead as a unified, AI-powered platform built entirely on the Salesforce Platform rather than on separate infrastructure.[^s1] It is licensed as a Growth Edition and an Advanced Edition, and it targets B2B, B2C and hybrid marketing from one system.[^s1] Its developer documentation still lives under a "marketing-cloud-growth" path, a trace of Marketing Cloud Growth Edition, the small and midsize business offering that an Advanced Edition with more automation and AI later expanded on.[^s5][^s7]

## How it works

**Data layer.** Data 360 (Data Cloud) is the foundation: sales, service and marketing share one database, so a change such as a newly logged support case is visible to marketing without a sync job, and a related email can be paused at once.[^s1] Data 360 supplies customer profiles, consent, marketing assets and campaign metrics to the product.[^s5] Setup follows the usual Data 360 path: data streams (optionally seeded from prebuilt data kits) bring in CRM records and engagement activity, an identity resolution ruleset merges records into a Unified Individual, and a data graph shapes the related records an email needs.[^s3] A data graph is only required when a message uses more than one record type, and it should hold only the fields the flow uses, because extra data adds complexity and can affect performance.[^s4]

**Enablement and roles.** An admin enables the product from Marketing Cloud Basic Settings in Setup; provisioning can take up to 15 minutes, after which users work in the Marketing app.[^s3] Trailhead frames the work around three roles: a Marketing Cloud admin, a Data Cloud architect who owns streams, identity resolution and the data model, and a Marketing Cloud manager who builds campaigns and sends.[^s3]

**Campaigns and orchestration.** Instead of Journey Builder and Automation Studio, orchestration runs in standard Flow Builder, for both segment-based and real-time, event-triggered automation.[^s1] A campaign record holds a flow summary in which the marketer sets the schedule, the audience segment and message or wait elements; email content is stored in a Salesforce CMS workspace.[^s4] Activation does not send immediately: the platform refreshes audience data first and then sends at the scheduled time to qualifying contacts.[^s4]

**Channels.** Email is included in both editions; SMS, WhatsApp and RCS are paid add-ons in both.[^s1] Push and in-app messages come through Mobile App Messaging, and landing pages and forms are built on Experience Cloud, saving form data to Data 360 and CRM objects.[^s1]

**AI and analytics.** Agentforce is built in to draft content, build segments from natural-language descriptions and handle two-way conversations, while analytics are driven by Data 360 and Tableau Next.[^s1][^s2] Trailhead's use cases span real-time segmentation, AI-orchestrated cross-channel journeys, lead scoring and hand-off to sales, loyalty rewards and paid-media optimization.[^s2]

## Developer surface

Developers use Salesforce Platform and Data 360 APIs rather than a separate marketing API: REST, Bulk API 2.0, SOAP, Tooling and Metadata APIs (the last two can manage the flows that run campaigns), plus Data 360 Connect REST resources for segment publication, identity resolution rulesets and calculated insights, and Connect API for uploading files to a CMS workspace.[^s5]

## Limits and gotchas

- Segment counting and publishing, data graph builds and ruleset publishing each run as jobs that take minutes, so schedule campaigns with lead time.[^s4]
- Data graphs carry refresh intervals and consumption cost; a less frequent refresh is suggested when timing is not critical.[^s4]
- SMS, WhatsApp and RCS are separately licensed add-ons, not part of the base editions.[^s1]
- Data 360 usage is billable, which the certification trail treats as a planning topic.[^s6]

## When to use it (and when not)

Choose Marketing Cloud Next when marketing should share one data model and one automation tool with Sales and Service, and when B2B and B2C motions need to live together.[^s1] Marketing Cloud Engagement remains the separate-infrastructure option built on data extensions, SQL-based segmentation, Journey Builder and Marketing Cloud Connect, which suits established high-volume B2C programs already invested in that stack.[^s1] Salesforce also publishes a certification for the product, the Marketing Cloud Next Consultant, whose prep trail covers setup, consent, Data 360 modelling, flows, Agentforce and analytics.[^s6]

## Connections

Marketing Cloud Next sits under `kt:salesforce-marketing-solutions` and is an **alternative to** `kt:marketing-cloud-engagement`, the older stack it is compared against in Trailhead.[^s1] It **depends on** `kt:data-cloud` as its data layer and, within it, on `kt:identity-resolution` and `kt:data-graphs` for unified profiles and personalization data.[^s3][^s4] It is **configured via** `kt:flow-builder` for campaign orchestration and **integrates with** `kt:agentforce` for segment and content generation.[^s1] It relates to `kt:tableau-next` for analytics and `kt:experience-cloud` for landing pages, to `kt:marketing-cloud-account-engagement` as Salesforce's other B2B marketing product, and to `kt:loyalty-management`, which its loyalty use case draws on.[^s1][^s2]

## Sources

[^s1]: Trailhead, "Get Started with Marketing Cloud Next Channel Marketing". https://trailhead.salesforce.com/content/learn/modules/channel-marketing-fundamentals-for-marketing-cloud-next/get-started-with-marketing-cloud-next-channel-marketing (accessed 2026-11-18)
[^s2]: Trailhead, "Explore Marketing Cloud Next Use Cases". https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-next-basics/explore-marketing-cloud-next-use-cases (accessed 2026-11-18)
[^s3]: Trailhead, "Prepare Your Org for Email Sending". https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-next-email-sending-essentials/prepare-your-org-for-email-sending (accessed 2026-11-18)
[^s4]: Trailhead, "Set Up a Marketing Cloud Next Campaign". https://trailhead.salesforce.com/content/learn/modules/campaign-optimization-with-flows-in-marketing-cloud-next/set-up-a-marketing-cloud-next-campaign (accessed 2026-11-18)
[^s5]: Salesforce Developers, "Marketing Cloud Next Documentation Resources". https://developer.salesforce.com/docs/marketing/marketing-cloud-growth/guide/mc-resources-documentation.html (accessed 2026-11-18)
[^s6]: Trailhead, "Prepare for Your Marketing Cloud Next Consultant Certification". https://trailhead.salesforce.com/content/learn/trails/prepare-for-your-marketing-cloud-next-consultant-certification (accessed 2026-11-18)
[^s7]: Salesforce Newsroom, "Salesforce Marketing Cloud Innovations Enable Marketers to Build Lasting Customer Relationships with Actionable Data and AI Agents". https://www.salesforce.com/news/?p=81453 (accessed 2026-11-18)
