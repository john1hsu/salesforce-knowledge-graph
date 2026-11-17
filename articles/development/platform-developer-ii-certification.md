---
id: kt:platform-developer-ii-certification
type: Certification
title: Platform Developer II Certification
aliases: [Salesforce Certified Platform Developer II, PDII, PD2, Plat-Dev-301]
domain: development
summary: >-
  Salesforce's advanced developer credential, earned through a proctored 60-question exam on advanced Apex fundamentals,
  automation and integration logic, user interfaces, testing and deployment, and performance; it requires the Platform
  Developer certification and shares that credential's annual maintenance badge.
release: "Winter '27"
status: current
broader: [kt:salesforce-certification-program]
related: [kt:platform-developer-certification, kt:apex-managed-sharing, kt:asynchronous-apex, kt:platform-events, kt:lightning-web-components, kt:large-data-volumes]
relations:
  - {predicate: dependsOn, object: kt:platform-developer-certification}
sources:
  - id: s1
    title: "Certification - Salesforce Certified Platform Developer II"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/platformdeveloperii
    type: official-learning
    accessed: 2026-11-17
  - id: s2
    title: "Salesforce Certified Platform Developer II Exam Guide"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298967&language=en_US&type=1
    type: official-learning
    accessed: 2026-11-17
  - id: s3
    title: "Developer Certifications"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/developeroverview
    type: official-learning
    accessed: 2026-11-17
  - id: s4
    title: "Salesforce Certification Maintenance Schedule"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298922&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-17
created: 2026-11-17
---

# Platform Developer II Certification

The Salesforce Certified Platform Developer II (often shortened to PDII) is the advanced credential in Salesforce's developer catalogue. Trailhead describes holders as experts in the platform's advanced programmatic capabilities who also apply data modeling to build complex business logic and interfaces.[^s1] It is listed beside the entry-level Platform Developer credential among Salesforce's developer certifications, which also include JavaScript Developer, Platform App Builder and several product-specific developer exams.[^s3] The credential page lists Platform Developer as the prerequisite and links to a dedicated exam registration page carrying the code Plat-Dev-301.[^s1]

## Who it is for

The exam guide targets developers with about two to four years of development experience, including at least one year designing, implementing and deploying on the Lightning Platform.[^s2] Candidates are expected to combine declarative and programmatic tools, write Apex that scales, build interfaces with Lightning Web Components, Aura and Visualforce, apply the security and sharing model, and work with Apex web services, asynchronous Apex and Jest tests.[^s2] Many objectives are framed as choosing between solutions, diagnosing faulty code and designing for scale rather than recalling features.[^s1][^s2]

## Exam format

As stated in the exam guide checked for this article:[^s2]

- **Questions:** 60 scored multiple-choice questions, plus up to five unscored questions placed at random.[^s2]
- **Time:** 120 minutes.[^s2]
- **Passing score:** 70%.[^s2]
- **Fees:** US$200 to register and US$100 to retake, plus applicable taxes.[^s2]
- **Delivery:** proctored, at a testing centre or online; no hard-copy or online material may be consulted.[^s2]
- **Prerequisite:** the Salesforce Certified Platform Developer credential.[^s1][^s2]
- **Release alignment:** the guide states the exam aligns to Winter '24, several releases behind the platform.[^s2]

## Exam outline

The guide weights five sections:[^s2]

| Section | Weight |
|---|---|
| Advanced Developer Fundamentals | 15%[^s2] |
| Process Automation, Logic, and Integration | 27% |
| User Interface | 20% |
| Testing, Debugging, and Deployment | 20% |
| Performance | 18%[^s2] |

Advanced fundamentals covers how localization and multi-currency affect code, when sharing objects and Apex managed sharing are justified, and best practice for custom metadata types and custom settings.[^s2] The largest section asks candidates to weigh declarative against programmatic solutions, apply trigger best practice, error handling and transaction control, advanced SOQL, dynamic Apex, asynchronous Apex, platform-event publish/subscribe and inbound and outbound integration techniques.[^s2] User-interface objectives centre on reading LWC or Aura code with its Apex controller, component event communication, responsive markup and Visualforce partial refreshes.[^s2] Testing covers mocks and stubs, front-end debugging and planning a source-driven deployment, while the Performance section targets UI performance, large data volumes, asynchronous callouts, code reuse and spotting inefficient code.[^s2]

The guide recommends the official Trailmix plus the Apex Specialist, Apex Callouts and Platform API superbadges, together with the Apex, LWC, API and SOQL/SOSL developer guides.[^s2]

## Maintenance and gotchas

- **Shared maintenance badge.** Platform Developer and Platform Developer II are maintained by the same Platform Developer badge on the Winter cycle, so one badge per year keeps both current.[^s4]
- **Missed deadlines expire the credential.** A lapsed certification may be reinstated by support case at Salesforce's discretion, but one that lapsed more than a cycle ago must be re-earned by exam.[^s4]
- **Exam version lags the platform.** Study to the release the guide names, not the latest release notes; newer features are unlikely to appear.[^s2]
- **Scenario-heavy questions.** Many objectives ask candidates to justify, analyse or find the cause of a problem rather than recall syntax, so hands-on practice such as the recommended superbadges pays off.[^s2]

## When to pursue it

It fits developers who already hold Platform Developer and regularly design trigger logic, integrations, asynchronous processing and component-based interfaces for large orgs.[^s1][^s2] Developers focused mainly on front-end JavaScript may find the JavaScript Developer credential a closer match, while declarative builders are better served by Platform App Builder.[^s3]

## Connections

- **broader → `kt:salesforce-certification-program`**: one credential in Salesforce's developer certification catalogue.[^s3]
- **dependsOn → `kt:platform-developer-certification`**: Platform Developer is the required prerequisite, and the two share a maintenance badge.[^s1][^s4]
- **related → `kt:apex-managed-sharing`, `kt:asynchronous-apex`, `kt:platform-events`**: named objectives in the fundamentals and automation sections.[^s2]
- **related → `kt:lightning-web-components`**: the User Interface section centres on analysing and wiring LWC and Aura components.[^s2]
- **related → `kt:large-data-volumes`**: the Performance section asks for query and logic structures that handle large data volumes.[^s2]

## Sources
[^s1]: Trailhead, "Certification - Salesforce Certified Platform Developer II". https://trailhead.salesforce.com/credentials/platformdeveloperii (accessed 2026-11-17)
[^s2]: Salesforce Help, "Salesforce Certified Platform Developer II Exam Guide". https://help.salesforce.com/s/articleView?id=005298967&language=en_US&type=1 (accessed 2026-11-17)
[^s3]: Trailhead, "Developer Certifications". https://trailhead.salesforce.com/credentials/developeroverview (accessed 2026-11-17)
[^s4]: Salesforce Help, "Salesforce Certification Maintenance Schedule". https://help.salesforce.com/s/articleView?id=005298922&language=en_US&type=1 (accessed 2026-11-17)
