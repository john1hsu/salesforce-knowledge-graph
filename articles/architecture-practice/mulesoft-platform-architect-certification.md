---
id: kt:mulesoft-platform-architect-certification
type: Certification
title: MuleSoft Platform Architect Certification
aliases: [Salesforce Certified MuleSoft Platform Architect, MuleSoft Certified Platform Architect, MCPA, MuleSoft Platform Architect I]
domain: architecture-practice
summary: >-
  Salesforce's architect-tier MuleSoft credential for people who define and own an organization's Anypoint Platform
  strategy, testing application-network design, API governance, runtime-plane deployment and monitoring rather than
  hands-on Mule development.
release: "Winter '27"
status: current
broader: [kt:salesforce-certification-program, kt:salesforce-architect]
related: [kt:api-led-connectivity, kt:non-functional-requirements, kt:salesforce-center-of-excellence]
relations:
  - {predicate: contrastsWith, object: kt:mulesoft-platform-integration-architect-certification}
  - {predicate: contrastsWith, object: kt:integration-architect-certification}
  - {predicate: dependsOn, object: kt:mulesoft-anypoint-platform}
sources:
  - id: s1
    title: "Salesforce Certified MuleSoft Platform Architect Exam Guide"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298956&language=en_US&type=1
    type: official-learning
    accessed: 2026-11-11
  - id: s2
    title: "Certification - Salesforce Certified MuleSoft Platform Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/mulesoftplatformarchitecti
    type: official-learning
    accessed: 2026-11-11
  - id: s3
    title: "Certification - MuleSoft Overview"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/mulesoftoverview
    type: official-learning
    accessed: 2026-11-11
  - id: s4
    title: "Salesforce Certified MuleSoft Platform Integration Architect Exam Guide"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298957&language=en_US&type=1
    type: official-learning
    accessed: 2026-11-11
  - id: s5
    title: "Maintain Your MuleSoft Architect Certification for Summer '26"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/mulesoft-platform-architect-certification-maintenance-summer-26/maintain-your-mulesoft-architect-certification-for-summer-26
    type: official-learning
    accessed: 2026-11-11
created: 2026-11-11
---

# MuleSoft Platform Architect Certification

The Salesforce Certified MuleSoft Platform Architect is the MuleSoft credential aimed at the person who sets an organization's Anypoint Platform strategy. Trailhead describes holders as able to define, and be responsible for, that strategy.[^s2] It sits in the Architect group of the MuleSoft credentials on Trailhead, alongside MuleSoft Catalyst Consultant and MuleSoft Platform Integration Architect, above the Associate (Integration Foundations) and Developer tiers.[^s3] The current Trailhead name has no level suffix, although the credential's web address still ends in "architect i", a trace of its earlier "Platform Architect I" naming.[^s2]

## Who it is for

The official exam guide pitches the exam at enterprise and solution architects who steer an application network built from many individual integrations using API-led connectivity.[^s1] Candidates are expected to tailor Anypoint Platform to their organization's context together with business, infrastructure and InfoSec teams, define how it coexists with other tools, plan the organizational and process changes that keep it sustainable, and push standards, reusable assets and automation so several lines of business can adopt it.[^s1] The guide assumes experience with common integration approaches such as SOA and a basic grasp of the platform's components, not deep Mule coding skill.[^s1]

## Exam format

The exam guide opened for this article gives the following format.[^s1]

- 60 scored multiple-choice questions plus up to five unscored ones, in 120 minutes.[^s1]
- Passing score 70%; registration US$400 (JPY 60,000) and retake US$200 (JPY 30,000), plus taxes.[^s1]
- Proctored at a test center or online; no reference materials and no prerequisite credential.[^s1]

## Exam outline

The guide splits the exam into nine weighted sections.[^s1]

| Section | Weight | Focus (paraphrased)[^s1] |
|---|---|---|
| Application network basics | 7% | API-led technologies, web API traits, assigning APIs to tiers, platform components |
| Organizational and platform foundations | 10% | Center for Enablement (C4E) and its KPIs, MuleSoft Catalyst, control- and runtime-plane hosting, identity and client management |
| Designing and sharing APIs | 10% | Reusable API assets, semantic versioning, Bounded Context mapping, idempotency and optimistic concurrency |
| System, Process and Experience layers | 12% | Layering APIs for a business process; enterprise vs Bounded Context data models |
| Governing web APIs | 17% | API Manager instances and environments, policies for NFRs, proxies vs gateways vs service mesh, client ID/secret, OAuth 2.0 with external IdPs |
| Architecting and deploying implementations | 11% | Auto-discovery, Anypoint VPC, runtime-plane options, MUnit, DevOps automation |
| Deploying to CloudHub | 11% | Object Store, worker sizing, shared vs dedicated load balancers, networking, single points of failure |
| Meeting API quality goals | 10% | Caching, client resilience, when horizontal scaling helps |
| Monitoring application networks | 12% | Metrics collected for API invocations and alerts across layers and for Mule apps |

Governance is the heaviest section, which signals the exam's emphasis: controlling and securing a portfolio of APIs matters more than building any one of them.[^s1]

## Gotchas

- **The question bank lags the product.** The guide says questions align to Spring '24, so newer capabilities may not be tested.[^s1]
- **Recent features still matter for maintenance.** Trailhead's Summer '26 maintenance module covers MuleSoft Omni Gateway, Integration Intelligence, Private Cloud Edition 4.2.0 and API Catalog as a hub for hosted MCP servers.[^s5]
- **Check maintenance rules before relying on either page.** The exam guide says no maintenance is currently required, while Trailhead publishes a maintenance badge for this credential and points to the maintenance schedule for due dates.[^s1][^s5]
- **Same logistics, different job.** The Platform Integration Architect exam has the identical question count, time, passing score and fees, but targets architects who lead implementations and covers Mule application design, testing and persistence instead of enterprise-wide strategy.[^s4]
- **No ordering is enforced.** Trailhead lists no prerequisite or required sequence among the MuleSoft credentials.[^s1][^s3]

## Connections

- **broader → `kt:salesforce-certification-program`, `kt:salesforce-architect`**: an Architect-group credential within Salesforce's certification catalog on Trailhead.[^s3]
- **dependsOn → `kt:mulesoft-anypoint-platform`**: every section of the outline is about designing, governing, deploying or monitoring on Anypoint Platform.[^s1]
- **contrastsWith → `kt:mulesoft-platform-integration-architect-certification`**: the sibling MuleSoft architect exam, focused on delivering solutions rather than platform strategy.[^s4]
- **contrastsWith → `kt:integration-architect-certification`**: commonly confused with it; this exam tests MuleSoft's own platform rather than Salesforce Platform integration patterns.[^s1]
- **related → `kt:api-led-connectivity`**: the exam's organizing model of System, Process and Experience APIs.[^s1]
- **related → `kt:non-functional-requirements`, `kt:salesforce-center-of-excellence`**: the guide tests mapping NFRs to API policies and setting up a C4E, MuleSoft's enablement counterpart to a CoE.[^s1]

## Sources
[^s1]: Salesforce Help, "Salesforce Certified MuleSoft Platform Architect Exam Guide". https://help.salesforce.com/s/articleView?id=005298956&language=en_US&type=1 (accessed 2026-11-11)
[^s2]: Trailhead, "Certification - Salesforce Certified MuleSoft Platform Architect". https://trailhead.salesforce.com/credentials/mulesoftplatformarchitecti (accessed 2026-11-11)
[^s3]: Trailhead, "Certification - MuleSoft Overview". https://trailhead.salesforce.com/credentials/mulesoftoverview (accessed 2026-11-11)
[^s4]: Salesforce Help, "Salesforce Certified MuleSoft Platform Integration Architect Exam Guide". https://help.salesforce.com/s/articleView?id=005298957&language=en_US&type=1 (accessed 2026-11-11)
[^s5]: Trailhead, "Maintain Your MuleSoft Architect Certification for Summer '26". https://trailhead.salesforce.com/content/learn/modules/mulesoft-platform-architect-certification-maintenance-summer-26/maintain-your-mulesoft-architect-certification-for-summer-26 (accessed 2026-11-11)
