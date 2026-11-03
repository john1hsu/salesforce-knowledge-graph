---
id: kt:service-cloud
type: Product
title: Service Cloud
aliases: [Agentforce Service, Salesforce Service Cloud, Service Cloud Essentials]
domain: clouds-and-products
summary: >-
  Salesforce's customer service product, now marketed as Agentforce Service, built around the Case object, the
  Lightning Service Console, multichannel intake and routing, knowledge, and SLA tracking, with AI agents working beside human reps.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:experience-cloud, kt:knowledge-base, kt:queues, kt:flow-builder, kt:field-service]
relations:
  - {predicate: hasPart, object: kt:omni-channel}
  - {predicate: hasPart, object: kt:entitlement-management}
  - {predicate: hasPart, object: kt:lightning-service-console}
  - {predicate: integratesWith, object: kt:agentforce}
  - {predicate: configuredVia, object: kt:service-setup-assistant}
sources:
  - id: s1
    title: "Agentforce Service Basics: the Service Console (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/service_lex/service_lex_cloud
    type: official-learning
    accessed: 2026-10-31
  - id: s2
    title: "Agentforce Service Basics: channels, automation and rollout (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/service_lex/service_lex_connect
    type: official-learning
    accessed: 2026-10-31
  - id: s3
    title: "Set Up Your Contact Center Instantly (Service Setup Assistant Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/service-setup-assistant-quick-look/set-up-your-contact-center-instantly
    type: official-learning
    accessed: 2026-10-31
  - id: s4
    title: "Set Up Milestones (Entitlement Management for Lightning Experience)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/entitlement-management-for-lightning-experience/set-up-milestones
    type: official-learning
    accessed: 2026-10-31
  - id: s5
    title: "Learn About Macros, Service Console, and Case Feed"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/service-cloud-essentials-features/learn-about-macros-service-console-and-case-feed
    type: official-learning
    accessed: 2026-10-31
  - id: s6
    title: "Agentforce Service (formerly Service Cloud) product overview (Taiwan)"
    publisher: Salesforce
    url: https://www.salesforce.com/tw/products/service-cloud/overview/
    type: news
    accessed: 2026-10-31
created: 2026-10-31
---

# Service Cloud

Service Cloud is Salesforce's customer service product. Salesforce now markets it as **Agentforce Service**, and its product pages describe it as formerly Service Cloud. The pitch is one platform for customer, field and employee service, where AI agents and human experts share the same data.[^s6] Much of Salesforce's own setup and learning content still says "Service Cloud", while newer units use "Agentforce Service" as the main name.[^s3][^s2] Treat the two names as the same product. Older content also mentions **Service Cloud Essentials**, a small-business edition with the basic case, console, macro and help-center tools.[^s5]

## How it works

The **Case** is the core record. A rep picks a contact, sets Status and Priority, records the Case Origin (such as Phone, Email or Web), and enters a Subject and Description. The Description also feeds AI features that recommend articles and next best actions.[^s1] Each case has a **Feed** that logs emails, calls, portal messages and internal notes in one timeline, so reps don't repeat work.[^s1][^s5]

Reps work in the **Lightning Service Console**. It shows customer history, assets and past conversations together. Records open as primary tabs, related records open as subtabs, and Split View lets a rep move through a queue without going back to a list view. The utility bar holds History, Macros and Omni-Channel.[^s1] **Macros** turn repetitive multi-step actions into one click. The Knowledge component suggests articles based on the case subject and lets reps attach them to a case or email.[^s1][^s5] Admins build and change console apps in App Manager.[^s1]

Work arrives through several channels. The basic ones are **Email-to-Case** and **Web-to-Case**, which turn a support address or a web form into cases. After that come Chat, Messaging (SMS, WhatsApp, Facebook Messenger) and Voice. Self-service runs on Experience Cloud sites and help centers.[^s2] **Omni-Channel** pushes cases, chats and calls to reps based on availability and skills.[^s1] Standard automation includes **assignment rules** for routing, **auto-response rules** that confirm receipt, and **escalation rules** for cases near their deadlines.[^s2]

## SLAs: entitlements and milestones

Service-level commitments are modeled with **entitlement management**. An entitlement is a customer's support agreement. Its *entitlement process* is a timeline of milestones, such as first response or resolution time. Each milestone has a time trigger in minutes, entry criteria, optional business hours, and warning actions that can alert the case owner before the deadline.[^s4] Salesforce's Trailhead example gives high-priority cases 960 minutes (16 business hours) to resolve.[^s4]

## Limits and gotchas

- Entitlements are **not added to new cases automatically**. Trailhead's own example uses an Apex trigger to fill the Entitlement field from the contact, then from the account.[^s4]
- If no business hours are set, milestone timers use the org default of 24/7, so deadlines can expire overnight.[^s4]
- An entitlement process must be **activated** before you can apply it to an entitlement.[^s4]
- **Service Setup Assistant** can configure queues, Email-to-Case, Omni-Channel, Knowledge, macros, page layouts and reports in one pass. Some of those features need extra licenses, and skipping their prerequisites can leave the setup incomplete. The assistant also offers updates each release.[^s3]

## When to use it (and when not)

Choose Service Cloud when support work needs case tracking, multichannel intake, routing by availability and skills, SLA timers and a knowledge base in one agent workspace. Salesforce's own rollout path starts with Email-to-Case or Web-to-Case and basic rules. Digital channels, entitlements and AI agents come later.[^s2] For a few shared inboxes, a plain case object with assignment rules may be enough. Contact-center scale and AI agents push toward higher editions and add-ons such as Agentforce Contact Center.[^s2][^s6]

## Connections

Service Cloud **has parts** `kt:omni-channel` (its routing engine), `kt:entitlement-management` (SLA timelines) and `kt:lightning-service-console` (the rep workspace).[^s1][^s4] It is **configured via** `kt:service-setup-assistant`.[^s3] It **integrates with** `kt:agentforce`, whose service agents handle conversations next to human reps.[^s2][^s6] It is **related** to `kt:experience-cloud` for self-service portals and to `kt:knowledge-base` for articles.[^s2][^s1] It is also related to `kt:queues`, which hold work before it is routed, and to `kt:flow-builder`, used for automation that goes beyond the classic case rules.[^s2][^s3] It sits under `kt:salesforce-platform`.

## Sources

[^s1]: Trailhead, "Agentforce Service Basics: the Service Console". https://trailhead.salesforce.com/content/learn/modules/service_lex/service_lex_cloud (accessed 2026-10-31)
[^s2]: Trailhead, "Agentforce Service Basics: channels, automation and rollout". https://trailhead.salesforce.com/content/learn/modules/service_lex/service_lex_connect (accessed 2026-10-31)
[^s3]: Trailhead, "Set Up Your Contact Center Instantly". https://trailhead.salesforce.com/content/learn/modules/service-setup-assistant-quick-look/set-up-your-contact-center-instantly (accessed 2026-10-31)
[^s4]: Trailhead, "Set Up Milestones". https://trailhead.salesforce.com/content/learn/modules/entitlement-management-for-lightning-experience/set-up-milestones (accessed 2026-10-31)
[^s5]: Trailhead, "Learn About Macros, Service Console, and Case Feed". https://trailhead.salesforce.com/content/learn/modules/service-cloud-essentials-features/learn-about-macros-service-console-and-case-feed (accessed 2026-10-31)
[^s6]: Salesforce, "Agentforce Service (formerly Service Cloud) product overview". https://www.salesforce.com/tw/products/service-cloud/overview/ (accessed 2026-10-31)
