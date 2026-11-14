---
id: kt:heroku-architect-certification
type: Certification
title: Heroku Architect Certification
aliases: [Salesforce Certified Heroku Architect, Heroku Architecture Designer, Heroku Architect credential]
domain: architecture-practice
summary: >-
  A Salesforce architect credential for people who design scalable solutions on Heroku, deploy and manage apps, and
  run teams and build workflows there; it is a standalone product credential in the architect catalogue and is kept
  current through an annual Trailhead maintenance module on Heroku platform changes.
release: "Winter '27"
status: current
broader: [kt:salesforce-architect, kt:salesforce-certification-program]
related: [kt:heroku, kt:heroku-fir, kt:twelve-factor-app]
relations:
  - {predicate: contrastsWith, object: kt:mulesoft-platform-architect-certification}
  - {predicate: contrastsWith, object: kt:system-architect-certification}
  - {predicate: integratesWith, object: kt:integration-architect-certification}
  - {predicate: dependsOn, object: kt:heroku-applink}
sources:
  - id: s1
    title: "Certification - Salesforce Certified Heroku Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/credentials/herokuarchitect
    type: official-learning
    accessed: 2026-11-14
  - id: s2
    title: "Architect Certifications Overview"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/credentials/architectoverview
    type: official-learning
    accessed: 2026-11-14
  - id: s3
    title: "Maintain Your Heroku Architect Certification for Summer '26"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/ko/content/learn/modules/heroku-architect-certification-maintenance-summer-26/maintain-your-heroku-architect-certification-for-summer-26
    type: official-learning
    accessed: 2026-11-14
  - id: s4
    title: "Maintain Your Heroku Architect Certification for Summer '25"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/it/content/learn/modules/heroku-architect-certification-maintenance-summer-25/maintain-your-heroku-architect-certification-for-summer-25
    type: official-learning
    accessed: 2026-11-14
  - id: s5
    title: "Heroku Generations"
    publisher: Heroku Dev Center (Salesforce)
    url: https://devcenter.heroku.com/articles/generations
    type: official-docs
    accessed: 2026-11-14
  - id: s6
    title: "An Update on Heroku"
    publisher: Heroku Blog (Salesforce)
    url: https://www.heroku.com/blog/an-update-on-heroku/
    type: official-blog
    accessed: 2026-11-14
  - id: s7
    title: "Passing the Heroku Architecture Designer Certificate"
    publisher: reinteractive
    url: https://reinteractive.com/articles/ace-heroku-architect-exam
    type: partner
    accessed: 2026-11-14
  - id: s8
    title: "Heroku Learning Journey"
    publisher: Heroku (Salesforce)
    url: https://www.heroku.com/heroku-learning-journey
    type: official-learning
    accessed: 2026-11-14
created: 2026-11-14
---

# Heroku Architect Certification

The Salesforce Certified Heroku Architect is the credential for architects who build scalable solutions on Heroku, deploy and manage applications, and manage teams and build workflows on the platform.[^s1] Trailhead lists it alongside Platform Developer, Platform Developer II, Platform Integration Architect and System Architect as related certifications, and points candidates to a curated Trailmix, "Prepare for Your Salesforce Heroku Architecture Certification", as the main study path.[^s1] Older material sometimes calls it the Heroku Architecture Designer credential.[^s7] Heroku's own learning journey has a dedicated Heroku Architect track and directs candidates to the exam guide and the same Trailmix.[^s8]

## Where it sits in the architect catalogue

Trailhead's architect overview lists fourteen architect credentials, and Heroku Architect sits among the product-specific ones, next to B2C Solution Architect, MuleSoft Platform Architect and Tableau Architect.[^s2] Unlike Application Architect and System Architect, which are roll-ups earned automatically from other exams, Heroku Architect is presented as a separate credential, and the overview does not list it as a step towards Certified Technical Architect.[^s2] In practice it signals platform-as-a-service design skill rather than core-platform (org) design skill.

## What the credential expects

The credential is about architecture choices on Heroku rather than day-to-day console use: scaling, deployment and team workflow are named explicitly on the credential page.[^s1] Its recent maintenance modules show what holders are expected to track. Summer '25 covered Router 2.0 replacing the Legacy Router (end-of-life in Spring 2025), the rename of Heroku Data for Redis to Heroku Key-Value Store, general availability of the Fir generation, .NET support, Managed Inference and Agents, a Heroku MCP Server, and wildcard support in Automated Certificate Management.[^s4] Summer '26 covered a GitHub Enterprise Server integration via a GitHub App, Heroku CLI v11, a larger default slug size of 1 GB (up to 2 GB on request), router log redaction of query strings, and new Heroku AppLink capabilities for exposing Heroku APIs to Flow, Apex, Data Cloud and Agentforce.[^s3]

## Platform knowledge that matters now

A large part of current Heroku architecture is choosing between generations. Cedar, the original stack, powers the Common Runtime and Private Spaces, while Fir is a Kubernetes-based generation on AWS offered as Fir Private Spaces, which Heroku recommends for new and actively developed apps.[^s5] Fir supports only Cloud Native Buildpacks, defaults to IPv6, and replaces syslog drains with OpenTelemetry; it does not yet support the Common Runtime, dyno autoscaling, Heroku CI, VPC peering, VPN connections or Shield compliance.[^s5] Those gaps are exactly the kind of trade-off an architect has to weigh before recommending a migration.[^s5]

Commercial context also matters. In February 2026 Heroku announced a move to a sustaining engineering model focused on stability, security, reliability and support rather than new features.[^s6] Enterprise Account contracts are no longer sold to new customers, though existing Enterprise subscriptions are honoured and can renew, and credit-card customers see no change.[^s6] An architect recommending Heroku for a new Salesforce-adjacent workload should factor that roadmap into a build-vs-buy decision.[^s6]

## Maintenance

Holders keep the credential current by completing the annual Heroku Architect maintenance module by the due date in Salesforce's certification maintenance schedule; the Summer '26 module is estimated at about ten minutes.[^s3] Anyone can earn the badge, but it is aimed at certification holders.[^s4]

## Connections

- **broader → `kt:salesforce-architect`, `kt:salesforce-certification-program`**: one of the fourteen architect credentials in Salesforce's certification catalogue.[^s2]
- **related → `kt:heroku`, `kt:heroku-fir`**: the product the credential certifies, and the generation choice that dominates current Heroku design.[^s1][^s5]
- **dependsOn → `kt:heroku-applink`**: AppLink is the current bridge between Heroku and Salesforce, and its features are part of the Summer '26 maintenance content.[^s3]
- **contrastsWith → `kt:mulesoft-platform-architect-certification`, `kt:system-architect-certification`**: a neighbouring product credential and a roll-up credential; Heroku Architect is earned on its own and does not feed a roll-up.[^s1][^s2]
- **integratesWith → `kt:integration-architect-certification`**: listed by Trailhead as a related certification, since Heroku solutions usually integrate with a Salesforce org.[^s1]
- **related → `kt:twelve-factor-app`**: the application methodology Heroku popularised and that Heroku's learning material recommends alongside architect preparation.[^s8]

## Sources
[^s1]: Trailhead, "Certification - Salesforce Certified Heroku Architect". https://trailhead.salesforce.com/en/credentials/herokuarchitect (accessed 2026-11-14)
[^s2]: Trailhead, "Architect Certifications Overview". https://trailhead.salesforce.com/en/credentials/architectoverview (accessed 2026-11-14)
[^s3]: Trailhead, "Maintain Your Heroku Architect Certification for Summer '26". https://trailhead.salesforce.com/ko/content/learn/modules/heroku-architect-certification-maintenance-summer-26/maintain-your-heroku-architect-certification-for-summer-26 (accessed 2026-11-14)
[^s4]: Trailhead, "Maintain Your Heroku Architect Certification for Summer '25". https://trailhead.salesforce.com/it/content/learn/modules/heroku-architect-certification-maintenance-summer-25/maintain-your-heroku-architect-certification-for-summer-25 (accessed 2026-11-14)
[^s5]: Heroku Dev Center, "Heroku Generations". https://devcenter.heroku.com/articles/generations (accessed 2026-11-14)
[^s6]: Heroku Blog, "An Update on Heroku". https://www.heroku.com/blog/an-update-on-heroku/ (accessed 2026-11-14)
[^s7]: reinteractive, "Passing the Heroku Architecture Designer Certificate". https://reinteractive.com/articles/ace-heroku-architect-exam (accessed 2026-11-14)
[^s8]: Heroku, "Heroku Learning Journey". https://www.heroku.com/heroku-learning-journey (accessed 2026-11-14)
