---
id: kt:tableau-architect-certification
type: Certification
title: Tableau Architect Certification
aliases: [Salesforce Certified Tableau Architect, Tableau Certified Architect, Tableau Architect credential]
domain: architecture-practice
summary: >-
  A Salesforce architect credential for people who design, deploy, monitor and maintain a scalable Tableau
  platform (Tableau Server, Tableau Cloud and Tableau Bridge), including migrations from Server to Cloud; it sits
  in the Trailhead architect catalogue alongside the Salesforce platform, MuleSoft and Heroku architect credentials.
release: "Winter '27"
status: current
broader: [kt:salesforce-architect, kt:salesforce-certification-program]
related: [kt:tableau, kt:heroku-architect-certification, kt:certified-technical-architect, kt:tableau-server-administrator-certification]
relations:
  - {predicate: dependsOn, object: kt:tableau-blueprint}
  - {predicate: contrastsWith, object: kt:system-architect-certification}
  - {predicate: contrastsWith, object: kt:tableau-server-administrator-certification}
sources:
  - id: s1
    title: "Certification - Salesforce Certified Tableau Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/tableauarchitect
    type: official-learning
    accessed: 2026-11-17
  - id: s2
    title: "Certification - Architect Overview"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/architectoverview
    type: official-learning
    accessed: 2026-11-17
  - id: s3
    title: "Tableau Certified Architect is available for everyone (Trailblazer Community announcement)"
    publisher: Trailblazer Community (Salesforce)
    url: https://trailhead.salesforce.com/trailblazer-community/feed/0D54V000079RGoPSAW
    type: community
    accessed: 2026-11-17
  - id: s4
    title: "Tableau Blueprint: Tableau Deployment"
    publisher: Tableau (Salesforce)
    url: https://help.tableau.com/current/blueprint/en-us/bp_deployment.htm
    type: official-docs
    accessed: 2026-11-17
  - id: s5
    title: "Tableau Blueprint: Tableau Enterprise Architecture Survey"
    publisher: Tableau (Salesforce)
    url: https://help.tableau.com/current/blueprint/en-us/bp_enterprise_architecture.htm
    type: official-docs
    accessed: 2026-11-17
  - id: s6
    title: "Tableau Blueprint: Move Tableau to the Cloud"
    publisher: Tableau (Salesforce)
    url: https://help.tableau.com/current/blueprint/en-us/bp_move_to_cloud.htm
    type: official-docs
    accessed: 2026-11-17
  - id: s7
    title: "Tableau Server Enterprise Deployment Guide"
    publisher: Tableau (Salesforce)
    url: https://help.tableau.com/current/guides/enterprise-deployment/en-us/edg_intro.htm
    type: official-docs
    accessed: 2026-11-17
  - id: s8
    title: "Certification - Salesforce Certified Tableau Server Administrator"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/tableauserveradministrator
    type: official-learning
    accessed: 2026-11-17
created: 2026-11-17
---

# Tableau Architect Certification

The Salesforce Certified Tableau Architect is the architect-level credential for Tableau's own analytics platform. Trailhead describes holders as people who work with customers to design, deploy, monitor and maintain a scalable Tableau platform that follows best practices and delivers business value.[^s1] It appears in Trailhead's architect catalogue as one of fourteen architect certifications, next to the Salesforce platform domain architects, the MuleSoft and Heroku architects and the Certified Technical Architect. The catalogue lists them under a single heading and does not group them by product.[^s2]

## Who it is for

When the credential opened to all candidates in July 2023, Salesforce's announcement framed it for people who manage Tableau Server infrastructure, including migrations to Tableau Cloud. The announcement recommended at least one year of Tableau experience across Cloud, Server and Bridge, plus a Tableau Server deployment on at least one cloud platform.[^s3] That scope sets it apart from the Tableau Server Administrator credential, which Trailhead aims at candidates with about six months of experience and limits to Server running on a single machine.[^s8] The architect credential therefore assumes multi-node, enterprise-scale and hybrid deployments rather than day-to-day administration.[^s3][^s8]

The credential page gives only a short description. Exam format, outline weightings and maintenance requirements are published in a separate exam guide and on Trailhead Academy, so check those before relying on any figure quoted by third-party prep sites.[^s1]

## What the role covers

Salesforce's Tableau Blueprint methodology describes the deployment decisions such an architect has to make. It compares three hosting options. Tableau Server on premises gives full control of hardware and keeps data behind the firewall but needs dedicated administrators. Tableau Server on public-cloud infrastructure keeps software control while making hardware elastic. Tableau Cloud is hosted and upgraded by Tableau, but runs a single site per tenant and does not support cubes or guest accounts.[^s4]

Before sizing and installing, Blueprint has IT complete an Enterprise Architecture Survey and business teams a Data and Analytics Survey.[^s4] The architecture survey's Tableau Server questions cover hardware and operating system, high availability with recovery time and recovery point objectives, authentication and service accounts, SSL and network ports, dev/test/prod environments, backup and restore, licensing, mobile, analytics extensions such as R and Python, automation and APIs, and data rules such as row-level security and geographic restrictions.[^s5] For Tableau Cloud, the questions shift to SSO providers, user provisioning and how Tableau Bridge will reach on-premises data.[^s5]

For self-managed deployments, Tableau's Enterprise Deployment Guide offers a prescriptive reference architecture. It uses web, application and data tiers, each in access-controlled subnets, with users authenticating at the web tier before requests are proxied to the application tier.[^s7] Tableau notes that the guide is no longer updated, so its steps should be checked against current Tableau Server Help.[^s7]

## Migration to Tableau Cloud

Server-to-Cloud migration is a core part of the brief.[^s3] Blueprint lists factors that can block or complicate a move. FedRAMP and PCI are not supported, and on-premises data usually needs Bridge, which does not run Prep flows. Guest access is unavailable and MFA is mandatory. Direct repository queries must be replaced by Admin Insights, and legacy core-based or guest licensing must convert to role-based subscriptions.[^s6] Self-migration suits small sites, roughly 100–150 users or fewer with simple permissions and one site. Larger estates should use Professional Services or a partner.[^s6] For a lift to public-cloud infrastructure, the architect chooses between backup-and-restore and selective content migration. The Content Migration Tool, part of Tableau Advanced Management, can speed up the selective option.[^s6]

## When to pursue it (and when not)

The credential fits consultants and platform owners who run Tableau Server or Tableau Cloud estates or plan migrations between them.[^s3] Its stated scope is Tableau Cloud, Server and Bridge infrastructure, so it does not substitute for the Salesforce platform architect credentials listed beside it, such as System Architect, Application Architect or the Certified Technical Architect.[^s1][^s2][^s3] Teams whose analytics live inside Salesforce workflows rather than on a Tableau Server or Cloud site will find less of their work reflected in it.[^s3]

## Connections

The credential sits under `kt:salesforce-architect` and the `kt:salesforce-certification-program`, which list it in the architect catalogue.[^s2] Its subject is the self-managed and hosted side of `kt:tableau`.[^s1] It `dependsOn` `kt:tableau-blueprint`, Tableau's deployment and governance methodology that supplies the surveys, hosting comparisons and migration guidance above.[^s4][^s6] It `contrastsWith` the `kt:tableau-server-administrator-certification`, which covers single-machine Server administration, and with the `kt:system-architect-certification`, which certifies Salesforce platform design rather than Tableau infrastructure.[^s8][^s2] Like the `kt:heroku-architect-certification`, it is a product-specific credential in the same catalogue as the `kt:certified-technical-architect`.[^s2]

## Sources

[^s1]: Trailhead, "Certification - Salesforce Certified Tableau Architect". https://trailhead.salesforce.com/credentials/tableauarchitect (accessed 2026-11-17)
[^s2]: Trailhead, "Certification - Architect Overview". https://trailhead.salesforce.com/credentials/architectoverview (accessed 2026-11-17)
[^s3]: Trailblazer Community (Salesforce), "Tableau Certified Architect is available for everyone" (Megan Bardin, 2023-07-18). https://trailhead.salesforce.com/trailblazer-community/feed/0D54V000079RGoPSAW (accessed 2026-11-17)
[^s4]: Tableau (Salesforce), "Tableau Blueprint: Tableau Deployment". https://help.tableau.com/current/blueprint/en-us/bp_deployment.htm (accessed 2026-11-17)
[^s5]: Tableau (Salesforce), "Tableau Blueprint: Tableau Enterprise Architecture Survey". https://help.tableau.com/current/blueprint/en-us/bp_enterprise_architecture.htm (accessed 2026-11-17)
[^s6]: Tableau (Salesforce), "Tableau Blueprint: Move Tableau to the Cloud". https://help.tableau.com/current/blueprint/en-us/bp_move_to_cloud.htm (accessed 2026-11-17)
[^s7]: Tableau (Salesforce), "Tableau Server Enterprise Deployment Guide". https://help.tableau.com/current/guides/enterprise-deployment/en-us/edg_intro.htm (accessed 2026-11-17)
[^s8]: Trailhead, "Certification - Salesforce Certified Tableau Server Administrator". https://trailhead.salesforce.com/credentials/tableauserveradministrator (accessed 2026-11-17)
