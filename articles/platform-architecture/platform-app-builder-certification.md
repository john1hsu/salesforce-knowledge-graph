---
id: kt:platform-app-builder-certification
type: Certification
title: Platform App Builder Certification
aliases: [Salesforce Certified Platform App Builder, Salesforce App Builder certification, PAB certification]
domain: platform-architecture
summary: >-
  Salesforce's credential for building custom applications declaratively on the Salesforce Platform, earned through a
  proctored exam weighted towards business logic and process automation, data modeling and Salesforce fundamentals.
release: "Winter '27"
status: current
broader: [kt:salesforce-certification-program]
related: [kt:platform-administrator-certification, kt:platform-developer-certification, kt:flow-builder, kt:lookup-vs-master-detail, kt:roll-up-summary-field, kt:sandbox-types]
relations:
  - {predicate: partOf, object: kt:application-architect-certification}
sources:
  - id: s1
    title: "Certification - Salesforce Certified Platform App Builder"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/platformappbuilder
    type: official-learning
    accessed: 2026-11-07
  - id: s2
    title: "Get Started with Platform App Builder Certification Prep"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/platform-app-builder-pt1/platform-app-builder-getting-started
    type: official-learning
    accessed: 2026-11-07
  - id: s3
    title: "Refresh on Business Logic and Process Automation"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/es/content/learn/modules/platform-app-builder-pt2/platform-app-builder-automation
    type: official-learning
    accessed: 2026-11-07
  - id: s4
    title: "Prepare for Your Salesforce Platform App Builder Certification"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/trails/prepare-for-your-salesforce-platform-app-builder-certification
    type: official-learning
    accessed: 2026-11-07
  - id: s5
    title: "Platform App Builder Certification Maintenance (Winter '26)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/platform-app-builder-certification-maintenance-winter-26
    type: official-learning
    accessed: 2026-11-07
  - id: s6
    title: "Salesforce Certified Platform App Builder"
    publisher: Global Knowledge
    url: https://www.globalknowledge.com/en-ca/certifications/certification-training/salesforce/salesforce-certified-platform-app-builder
    type: partner
    accessed: 2026-11-07
created: 2026-11-07
---

# Platform App Builder Certification

The **Salesforce Certified Platform App Builder** credential validates the ability to design, build and deploy custom applications on the Salesforce Platform using its declarative (clicks-not-code) tools.[^s1] It sits in Trailhead's administrator-oriented catalogue next to Platform Administrator, Platform Administrator II and Agentforce Specialist, which the credential page lists as related certifications.[^s1] Where Platform Administrator focuses on running an org day to day, App Builder focuses on designing the data model, logic and user interface of new applications.

## Who it is for

Trailhead's official prep module frames the exam for people who build custom applications on the platform and extend Salesforce functionality.[^s2] Candidates are expected to have roughly six months of experience with platform capabilities, Salesforce license types and their implications, designing apps that support business processes and reporting, customising the mobile user experience, and Salesforce development environments and deployment options.[^s2] That profile fits admins who are moving into solution building, business analysts who prototype apps, and consultants who configure custom objects and automation for clients.

## Exam outline

The prep module publishes five weighted sections:[^s2]

| Section | Weight |
|---|---|
| Salesforce Fundamentals | 23% |
| Data Modeling and Management | 22% |
| Business Logic and Process Automation | 28% |
| User Interface | 17% |
| App Deployment | 10%[^s2] |

Business logic and automation is the heaviest section. The second prep module lists its focus areas as formula fields, roll-up summary field capabilities, validation rules, approval processes, declarative automation tools, and avoiding errors in automation, along with record types and their behaviour during lead conversion.[^s3] Data modeling questions centre on objects, relationships and data management tools, while App Deployment covers how changes move between environments.[^s4]

Exam logistics are set by Salesforce's exam guide. Global Knowledge, a training provider, summarises them as 60 scored multiple-choice questions in 105 minutes with a 63% passing score, a USD 200 registration fee and a USD 100 retake fee, with no formal prerequisite; confirm these against the official exam guide before booking.[^s6] The exam can be taken online-proctored or in person, under the Salesforce Certification Program Agreement.[^s2]

## Preparation

The official **Prepare for Your Salesforce Platform App Builder Certification** trail runs to about 39 hours and mirrors the outline: an exam overview with the exam guide, then sections on Salesforce fundamentals (data security, user management, reports and dashboards, Salesforce DX), data modeling (Lightning Object Creator, picklists, data import and export, external services), business logic (formulas, validation rules and several app-building projects, including Agentforce setup for admins), user interface customisation (Lightning App Builder, Lightning Web Components basics, mobile app customisation) and app deployment (sandboxes, org and package development models, second-generation managed and unlocked packages).[^s4] The two cert-prep modules add scenarios and flashcards per section.[^s2][^s3] Trailhead recommends approved materials such as exam guides, trailmixes, Trailhead Academy courses and Trailhead LIVE, and community study groups.[^s2]

## Maintenance and gotchas

- **Annual maintenance.** Holders must complete their certification's release maintenance modules once a year, or the credential expires.[^s2] The *Platform App Builder Certification Maintenance (Winter '26)* module, for example, takes about 30 minutes and includes a hands-on unit on sorting list views by multiple columns.[^s5]
- **Exam integrity.** Sharing or requesting exam questions or superbadge solutions can lead to cancelled results or revoked certifications.[^s2]
- **Declarative, but not code-free knowledge.** The prep trail includes Lightning Web Components basics and package development, so candidates need to know when a declarative solution stops being the right fit.[^s4]

## When to pursue it

Pursue App Builder when your work centres on designing custom objects, relationships, automation and Lightning pages rather than user and org administration; the two admin-track credentials complement each other.[^s1][^s2] It is also a common stepping stone towards architect credentials, because its deployment and package-model content overlaps with what architects must reason about.[^s4]

## Connections

- **broader → `kt:salesforce-certification-program`**: one credential in Salesforce's certification catalogue.[^s1]
- **partOf → `kt:application-architect-certification`**: the graph models App Builder as one of the declarative prerequisites that roll up into Application Architect; that node carries the sources for the credential path.
- **related → `kt:platform-administrator-certification`**: the sibling administrator credential listed alongside it.[^s1]
- **related → `kt:platform-developer-certification`**: the programmatic counterpart; the prep trail's LWC and Salesforce DX content marks where declarative building hands off to code.[^s4]
- **related → `kt:flow-builder`, `kt:roll-up-summary-field`**: declarative automation, formulas and roll-up summaries make up the exam's largest section.[^s3]
- **related → `kt:lookup-vs-master-detail`**: relationship design is core to the data modeling section.[^s4]
- **related → `kt:sandbox-types`**: the App Deployment section covers sandboxes and development models.[^s4]

## Sources
[^s1]: Trailhead, "Certification - Salesforce Certified Platform App Builder". https://trailhead.salesforce.com/credentials/platformappbuilder (accessed 2026-11-07)
[^s2]: Trailhead, "Get Started with Platform App Builder Certification Prep". https://trailhead.salesforce.com/content/learn/modules/platform-app-builder-pt1/platform-app-builder-getting-started (accessed 2026-11-07)
[^s3]: Trailhead, "Refresh on Business Logic and Process Automation". https://trailhead.salesforce.com/es/content/learn/modules/platform-app-builder-pt2/platform-app-builder-automation (accessed 2026-11-07)
[^s4]: Trailhead, "Prepare for Your Salesforce Platform App Builder Certification". https://trailhead.salesforce.com/content/learn/trails/prepare-for-your-salesforce-platform-app-builder-certification (accessed 2026-11-07)
[^s5]: Trailhead, "Platform App Builder Certification Maintenance (Winter '26)". https://trailhead.salesforce.com/content/learn/modules/platform-app-builder-certification-maintenance-winter-26 (accessed 2026-11-07)
[^s6]: Global Knowledge, "Salesforce Certified Platform App Builder". https://www.globalknowledge.com/en-ca/certifications/certification-training/salesforce/salesforce-certified-platform-app-builder (accessed 2026-11-07)
