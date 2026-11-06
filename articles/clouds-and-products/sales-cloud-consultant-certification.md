---
id: kt:sales-cloud-consultant-certification
type: Certification
title: Agentforce Sales Consultant Certification
aliases: [Salesforce Certified Agentforce Sales Consultant, Sales Cloud Consultant Certification, Salesforce Certified Sales Cloud Consultant, Sales-Con-201]
domain: clouds-and-products
summary: >-
  Salesforce's consultant-level credential for designing and implementing Sales Cloud solutions, renamed from
  Sales Cloud Consultant to Agentforce Sales Consultant on July 24, 2026 with no change to exam content; it requires
  the Platform Administrator credential and is maintained through the Platform Administrator maintenance badge.
release: "Winter '27"
status: current
broader: [kt:salesforce-certification-program]
related: [kt:sales-cloud, kt:collaborative-forecasts, kt:opportunity-splits, kt:enterprise-territory-management, kt:data-migration-strategy, kt:agentforce]
relations:
  - {predicate: dependsOn, object: kt:platform-administrator-certification}
sources:
  - id: s1
    title: "Certification - Salesforce Certified Agentforce Sales Consultant"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/agfsalesconsultant
    type: official-learning
    accessed: 2026-11-06
  - id: s2
    title: "Salesforce Certification Name Changes FAQ"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298915&amp=&language=en_US&amp=&type=1
    type: official-docs
    accessed: 2026-11-06
  - id: s3
    title: "Salesforce Certification Maintenance Schedule"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298922&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-06
  - id: s4
    title: "Certification - Consultant Overview"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/consultantoverview
    type: official-learning
    accessed: 2026-11-06
  - id: s5
    title: "Sales Cloud Consultant Certification Guide & Tips"
    publisher: Salesforce Ben
    url: https://www.salesforceben.com/sales-cloud-certification-guide-tips/
    type: news
    accessed: 2026-11-06
created: 2026-11-06
---

# Agentforce Sales Consultant Certification

The **Salesforce Certified Agentforce Sales Consultant** credential validates that a practitioner can design and implement Sales Cloud solutions that are sustainable and scalable and that support long-term customer success.[^s1] Until July 24, 2026 it was called the **Salesforce Certified Sales Cloud Consultant**. Salesforce renamed it, along with other credentials, so that certification names match current product names.[^s2] The rename did not change the exam content or the annual maintenance requirement. Existing holders keep the credential: their Trailblazer profiles update automatically, and verification shows the new name with the original earned date.[^s2] This node covers both names, since they refer to one certification.

## Place in the certification catalogue

Trailhead files the credential among its consultant certifications. Its siblings include the Agentforce Service, Field Service and Operations, Life Sciences and Nonprofit Consultant credentials, the Data 360 Consultant and the Experience Cloud Consultant.[^s4] The credential page lists the **Salesforce Certified Platform Administrator** as its prerequisite and points candidates to an official prep trailmix and a Trailhead Academy exam page.[^s1] The exam page carries the identifier Sales-Con-201, so search for both names, and that code, when looking for prep material.[^s1]

## Exam scope

The official credential page gives no exam format or outline. It sends candidates to the Trailhead Academy exam page for those details, so check there when you register.[^s1] A practitioner guide last updated in April 2025 describes the Sales Cloud-era exam as 60 scored multiple-choice and multiple-select questions, plus up to five unscored ones, in 105 minutes, with a 69% passing score, a $200 fee and a $100 retake.[^s5] The same guide calls the exam heavily scenario-based. It gives the outline used since June 2024 as five sections:[^s5]

- **Practical application of Sales Cloud expertise (33%)**: lead-to-order processes, products, sharing, multi-currency, and when to choose configuration, AppExchange packages or custom development.[^s5]
- **Sales lifecycle (23%)**: requirements-to-solution scenarios, Sales Cloud AI, Sales Territories, Salesforce Maps, forecasting, and reports and dashboards.[^s5]
- **Implementation strategies (15%)**: change management, enablement, deployment, training and success KPIs.[^s5]
- **Data management (15%)**: migration and data quality, Data Loader and the Data Import Wizard, record locking and duplicate prevention.[^s5]
- **Consulting practices (14%)**: project management and gathering and prioritising requirements.[^s5]

Because Salesforce says renamed exams keep the same content, this outline still describes the subject areas. Product names in exam guides and questions now follow current branding, though.[^s2][^s5] Treat the figures above as secondary and confirm them against the official exam page before booking.[^s1][^s5]

## Maintenance

Every Salesforce certification requires one maintenance badge a year. Badges are released with each Spring, Summer or Winter release and are due one year later, and a missed deadline expires the credential.[^s3] For this credential the required module is not a Sales-specific badge but the **Platform Administrator maintenance badge**, in the Spring '26 cycle (available April 23, 2026, due April 16, 2027). The Agentforce Service Consultant uses the same badge.[^s3] A recently expired credential can be reinstated through a support case, at Salesforce's discretion. After more than one missed cycle, the holder must retake the exam.[^s3]

## Gotchas

- **Two names, one credential.** Résumés, partner records and older prep sites still say "Sales Cloud Consultant". It is the same certification as Agentforce Sales Consultant, not a second one to earn.[^s2]
- **"Agentforce" in the name is branding.** The rename reflects product naming. It did not add new exam content.[^s2]
- **Admin knowledge matters twice.** The Platform Administrator credential is the entry prerequisite, and its maintenance badge is also what keeps this credential current.[^s1][^s3]
- **Prefer standard features.** Practitioners advise choosing standard Sales Cloud functionality over custom builds when both would satisfy a scenario.[^s5]

## Connections

- **broader → `kt:salesforce-certification-program`**: one of the consultant-tier credentials in Salesforce's certification catalogue.[^s4]
- **dependsOn → `kt:platform-administrator-certification`**: the listed prerequisite, whose maintenance badge also keeps this credential active.[^s1][^s3]
- **related → `kt:sales-cloud`**: the product whose solution design the credential validates. The Sales Cloud article marks itself as covered by this exam.[^s1]
- **related → `kt:collaborative-forecasts`, `kt:enterprise-territory-management`, `kt:opportunity-splits`**: forecasting, Sales Territories and opportunity management fall in the sales-lifecycle and practical-application sections. The forecasting and splits articles record a `coveredBy` edge to this node.[^s5]
- **related → `kt:data-migration-strategy`**: migration, data quality and import tooling make up the data-management section.[^s5]
- **related → `kt:agentforce`**: the platform brand added to the credential's name in the July 2026 rename.[^s2]

## Sources
[^s1]: Trailhead, "Certification - Salesforce Certified Agentforce Sales Consultant". https://trailhead.salesforce.com/credentials/agfsalesconsultant (accessed 2026-11-06)
[^s2]: Salesforce Help, "Salesforce Certification Name Changes FAQ". https://help.salesforce.com/s/articleView?id=005298915&amp=&language=en_US&amp=&type=1 (accessed 2026-11-06)
[^s3]: Salesforce Help, "Salesforce Certification Maintenance Schedule". https://help.salesforce.com/s/articleView?id=005298922&language=en_US&type=1 (accessed 2026-11-06)
[^s4]: Trailhead, "Certification - Consultant Overview". https://trailhead.salesforce.com/credentials/consultantoverview (accessed 2026-11-06)
[^s5]: Salesforce Ben, "Sales Cloud Consultant Certification Guide & Tips". https://www.salesforceben.com/sales-cloud-certification-guide-tips/ (accessed 2026-11-06)
