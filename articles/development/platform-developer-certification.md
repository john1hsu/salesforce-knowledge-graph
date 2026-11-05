---
id: kt:platform-developer-certification
type: Certification
title: Platform Developer Certification
aliases: [Salesforce Certified Platform Developer, Platform Developer I, PD1, Platform Developer credential]
domain: development
summary: >-
  Salesforce's practitioner-level developer credential (formerly titled Platform Developer I), earned through a
  proctored 60-question exam on Apex, automation logic, user interfaces, testing and deployment; it is the prerequisite
  for Platform Developer II and one of the exams that roll up into the Application and System Architect credentials.
release: "Winter '27"
status: current
broader: [kt:salesforce-certification-program]
related: [kt:apex, kt:apex-testing, kt:platform-developer-ii-certification, kt:platform-app-builder-certification]
relations:
  - {predicate: partOf, object: kt:application-architect-certification}
  - {predicate: partOf, object: kt:system-architect-certification}
sources:
  - id: s1
    title: "Certification - Salesforce Certified Platform Developer"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/platformdeveloperi
    type: official-learning
    accessed: 2026-11-05
  - id: s2
    title: "Salesforce Certified Platform Developer Exam Guide"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298965&language=en_US&type=1
    type: official-learning
    accessed: 2026-11-05
  - id: s3
    title: "Developer Certifications"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/developeroverview
    type: official-learning
    accessed: 2026-11-05
  - id: s4
    title: "Platform Developer I Certification Guide: Get Started"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/platform-developer-i-certification-prep-fundamentals-and-database-modeling/pd1-1-get-started
    type: official-learning
    accessed: 2026-11-05
  - id: s5
    title: "Maintain Your Salesforce Certification"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298841&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-05
  - id: s6
    title: "Certification - Salesforce Certified Application Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/applicationarchitect
    type: official-learning
    accessed: 2026-11-05
created: 2026-11-05
---

# Platform Developer Certification

The Salesforce Certified Platform Developer is the entry credential for programmatic work on the Salesforce Platform. Trailhead describes holders as developers who build custom business logic and custom interfaces with the platform's programmatic tools, and who can extend it with Apex and Visualforce.[^s1] The credential was long known as Platform Developer I: the current credential page and exam guide use the shorter title, while its URL and the official prep modules still carry the "Platform Developer I" name, so both names refer to the same certification.[^s1][^s2][^s4] It sits in Salesforce's developer catalogue alongside credentials such as Platform App Builder, JavaScript Developer and Platform Developer II.[^s3]

## Who it is for

The exam guide targets developers with roughly one to two years of development experience, including at least six months on the Lightning Platform, who build, test and deploy basic business logic and user interfaces.[^s2] It is equally explicit about what is out of scope: candidates are not expected to administer standard apps, build mobile apps, publish managed AppExchange packages, tune performance or design integrations.[^s2] That boundary is useful when deciding between credentials, because integration design and large-scale performance are covered by architect-level exams instead.

## Exam format

As stated in the exam guide checked for this article:[^s2]

- **Questions:** 60 scored multiple-choice questions, plus up to five unscored questions mixed in at random.[^s2]
- **Time:** 105 minutes.[^s2]
- **Passing score:** 68%.[^s2]
- **Fees:** US$200 to register and US$100 to retake, plus applicable taxes.[^s2]
- **Delivery:** proctored, at a testing centre or online; no reference material is allowed.[^s2]
- **Prerequisites:** none; the exam is itself the prerequisite for Platform Developer II.[^s2]
- **Release alignment:** the guide says questions align to the Summer '25 release, so it lags the current platform release.[^s2]

## Exam outline

The guide weights four sections:[^s2][^s4]

| Section | Weight |
|---|---|
| Developer Fundamentals | 27%[^s2] |
| Process Automation and Logic | 28% |
| User Interface | 25% |
| Testing, Debugging, and Deployment | 20%[^s2] |

The official Trailhead prep content mirrors this split: one module covers Developer Fundamentals and three companion modules cover the remaining sections, and it recommends Salesforce-approved study material and Trailblazer Community study groups.[^s4] The credential page links a dedicated study trail and Trailmix for the exam.[^s1]

## Maintenance and gotchas

- **Annual maintenance.** Every Salesforce certification needs one maintenance badge per year; Platform Developer and Platform Developer II share a single Platform Developer badge on the Winter cycle, and missing the deadline can expire or suspend the credentials tied to that badge.[^s5]
- **Architect credentials depend on it.** Because Application Architect and System Architect both require Platform Developer, letting its maintenance lapse puts those roll-up credentials at risk too.[^s5][^s6]
- **Exam version lags the platform.** Study against the exam guide's stated release rather than the newest release notes; features introduced after it are unlikely to be examined.[^s2]
- **Old name in the wild.** Job ads, URLs and prep content still say "PD1" or "Platform Developer I"; it is not a separate credential from the renamed one.[^s1][^s4]

## When to pursue it

It suits developers and admins moving into code who need to show competence across the four exam sections: platform fundamentals, automation and logic, user interfaces, and testing and deployment.[^s2][^s4] Declarative builders who rarely write code are better served first by Platform App Builder; developers who already hold Platform Developer and work on advanced programmatic design and complex data modelling move on to Platform Developer II.[^s3] Aspiring architects need it regardless, since it is one of four exams that automatically grant Application Architect.[^s6]

## Connections

- **broader → `kt:salesforce-certification-program`**: one credential in Salesforce's developer certification catalogue.[^s3]
- **partOf → `kt:application-architect-certification`, `kt:system-architect-certification`**: listed as a prerequisite of both roll-up architect credentials, which inherit its maintenance badge requirement.[^s5][^s6]
- **related → `kt:apex`, `kt:apex-testing`**: the exam's logic and testing sections centre on Apex code and its unit tests.[^s1][^s2]
- **related → `kt:platform-developer-ii-certification`**: the advanced follow-on credential, for which this exam is the prerequisite and with which it shares a maintenance badge.[^s2][^s5]
- **related → `kt:platform-app-builder-certification`**: the declarative counterpart, also required for Application Architect.[^s3][^s6]

## Sources
[^s1]: Trailhead, "Certification - Salesforce Certified Platform Developer". https://trailhead.salesforce.com/credentials/platformdeveloperi (accessed 2026-11-05)
[^s2]: Salesforce Help, "Salesforce Certified Platform Developer Exam Guide". https://help.salesforce.com/s/articleView?id=005298965&language=en_US&type=1 (accessed 2026-11-05)
[^s3]: Trailhead, "Developer Certifications". https://trailhead.salesforce.com/credentials/developeroverview (accessed 2026-11-05)
[^s4]: Trailhead, "Platform Developer I Certification Guide: Get Started". https://trailhead.salesforce.com/content/learn/modules/platform-developer-i-certification-prep-fundamentals-and-database-modeling/pd1-1-get-started (accessed 2026-11-05)
[^s5]: Salesforce Help, "Maintain Your Salesforce Certification". https://help.salesforce.com/s/articleView?id=005298841&language=en_US&type=1 (accessed 2026-11-05)
[^s6]: Trailhead, "Certification - Salesforce Certified Application Architect". https://trailhead.salesforce.com/credentials/applicationarchitect (accessed 2026-11-05)
