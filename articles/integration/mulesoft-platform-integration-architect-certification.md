---
id: kt:mulesoft-platform-integration-architect-certification
type: Certification
title: MuleSoft Platform Integration Architect Certification
aliases: [Salesforce Certified MuleSoft Platform Integration Architect, MuleSoft Integration Architect I]
domain: integration
summary: >-
  Salesforce's architect-tier MuleSoft credential for people who lead Anypoint Platform implementations, testing
  Mule application design, runtime-plane architecture, persistence, reliability, security and DevOps for integration
  solutions rather than enterprise-wide platform strategy.
release: "Winter '27"
status: current
broader: [kt:salesforce-certification-program, kt:salesforce-architect]
related: [kt:api-led-connectivity, kt:event-driven-architecture, kt:mule-runtime-engine, kt:non-functional-requirements]
relations:
  - {predicate: dependsOn, object: kt:mulesoft-anypoint-platform}
  - {predicate: contrastsWith, object: kt:mulesoft-platform-architect-certification}
  - {predicate: contrastsWith, object: kt:integration-architect-certification}
sources:
  - id: s1
    title: "Salesforce Certified MuleSoft Platform Integration Architect Exam Guide"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298957&language=en_US&type=1
    type: official-learning
    accessed: 2026-11-25
  - id: s2
    title: "Certification - Salesforce Certified MuleSoft Platform Integration Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/mulesoftintegrationarchitecti
    type: official-learning
    accessed: 2026-11-25
  - id: s3
    title: "Maintain Your MuleSoft Platform Integration Arch. Certification for Spring '26"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/mulesoft-platform-integration-architect-certification-maintenance-spring-26/maintain-your-mulesoft-integration-architect-certification-for-spring-26
    type: official-learning
    accessed: 2026-11-25
  - id: s4
    title: "Salesforce Certified MuleSoft Platform Architect Exam Guide"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298956&language=en_US&type=1
    type: official-learning
    accessed: 2026-11-25
created: 2026-11-25
---

# MuleSoft Platform Integration Architect Certification

The Salesforce Certified MuleSoft Platform Integration Architect is the MuleSoft architect credential for the person who designs and leads delivery of integration solutions on Anypoint Platform. Trailhead describes holders as able to work with technical and non-technical stakeholders and turn functional and non-functional requirements into integration interfaces and implementations.[^s2] The credential's web address still ends in "integrationarchitecti", a trace of the older "Integration Architect I" naming.[^s2]

## Who it is for

The official exam guide targets candidates who lead Anypoint Platform implementations with a focus on quality and operationalization, typically solution architects, technical architects and senior developers.[^s1] It expects them to produce high-level integration designs, choose Mule components and patterns, pick between MuleSoft-hosted and customer-hosted control and runtime planes, design Mule applications for those deployment options, and advise teams on performance, reliability and monitoring while building reusable assets and frameworks.[^s1] The MuleSoft Developer credential is recommended background but not a formal prerequisite.[^s1]

## Exam format

The guide opened for this article gives the following format.[^s1]

- 60 scored multiple-choice questions plus up to five unscored ones, in 120 minutes; passing score 70%.[^s1]
- Registration US$400 (JPY 60,000) and retake US$200 (JPY 30,000), plus applicable taxes.[^s1]
- Proctored at a test center or online, with no hard-copy or online references and no required prerequisite.[^s1]

## Exam outline

The guide divides the exam into ten weighted sections.[^s1]

| Section | Weight | Focus (paraphrased)[^s1] |
|---|---|---|
| Initiating integration solutions | 8% | Functional vs non-functional requirements; web and event-driven API features; control- and runtime-plane options |
| Runtime plane technology architecture | 15% | Mule runtime clusters, CloudHub networking, domains, Mule 4 class-loader isolation and reactive event model |
| Integration paradigms | 10% | API-led connectivity, web APIs over HTTP, event-driven APIs, message brokers and messaging patterns |
| Designing and developing Mule applications | 15% | Properties, core routers, Salesforce Connector, core connectors, Transform Message metadata, canonical data models, validation |
| Automated testing | 5% | MUnit suites; when integration or performance testing applies |
| Persistence | 10% | VM queues and connector, Object Store connector and service, stateful components |
| Reliability | 8% | Alternatives to transactions, Until Successful, reconnection and redelivery, HA vs DR, local and XA transactions |
| Performance | 7% | Capacity goals, streaming, large message sequences |
| Security | 8% | Securing control-plane and API access, edge security, vulnerability mitigation, audit logging |
| DevOps and operations | 14% | CI/CD with MuleSoft Maven plugins, automating platform tasks, logging, Anypoint Monitoring |

Runtime architecture, application design and DevOps together make up 44% of the exam, which shows its delivery focus: how a Mule solution is built, run and kept healthy.[^s1]

## Gotchas

- **The question bank lags the product.** The guide says questions align to the Spring '24 release, so newer Anypoint features may be absent from the exam.[^s1]
- **Maintenance signals conflict.** The guide states no maintenance is currently required, yet Trailhead publishes a Spring '26 maintenance module for this credential covering MuleSoft for Flow: Integration, Connector Builder for Anypoint Platform and the MuleSoft Diagnostics Agent.[^s1][^s3]
- **Easy to confuse with its sibling.** The MuleSoft Platform Architect exam has the same question count, time, passing score and fees but targets architects who own enterprise-wide Anypoint strategy and application-network governance.[^s4][^s1]
- **Not the Salesforce Platform integration exam.** Every section tests Mule applications and Anypoint deployment, so it does not replace the separate Salesforce Platform Integration Architect credential.[^s1]

## Connections

- **broader → `kt:salesforce-certification-program`, `kt:salesforce-architect`**: an architect-level MuleSoft credential issued through Trailhead.[^s2]
- **dependsOn → `kt:mulesoft-anypoint-platform`**: every outline section is about designing, deploying or operating solutions on Anypoint Platform.[^s1]
- **contrastsWith → `kt:mulesoft-platform-architect-certification`**: the strategy-focused sibling exam with identical logistics.[^s4]
- **contrastsWith → `kt:integration-architect-certification`**: the Salesforce Platform integration credential that shares the "integration architect" label.[^s1]
- **related → `kt:api-led-connectivity`, `kt:event-driven-architecture`**: both are tested as integration paradigms in their own section.[^s1]
- **related → `kt:mule-runtime-engine`**: runtime clusters, class loading and the reactive event model carry 15% of the exam.[^s1]
- **related → `kt:non-functional-requirements`**: the exam opens with separating functional from non-functional needs and then tests persistence, reliability, performance and security design.[^s1]

## Sources
[^s1]: Salesforce Help, "Salesforce Certified MuleSoft Platform Integration Architect Exam Guide". https://help.salesforce.com/s/articleView?id=005298957&language=en_US&type=1 (accessed 2026-11-25)
[^s2]: Trailhead, "Certification - Salesforce Certified MuleSoft Platform Integration Architect". https://trailhead.salesforce.com/credentials/mulesoftintegrationarchitecti (accessed 2026-11-25)
[^s3]: Trailhead, "Maintain Your MuleSoft Platform Integration Arch. Certification for Spring '26". https://trailhead.salesforce.com/content/learn/modules/mulesoft-platform-integration-architect-certification-maintenance-spring-26/maintain-your-mulesoft-integration-architect-certification-for-spring-26 (accessed 2026-11-25)
[^s4]: Salesforce Help, "Salesforce Certified MuleSoft Platform Architect Exam Guide". https://help.salesforce.com/s/articleView?id=005298956&language=en_US&type=1 (accessed 2026-11-25)
