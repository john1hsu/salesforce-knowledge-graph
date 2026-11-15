---
id: kt:platform-administrator-ii-certification
type: Certification
title: Platform Administrator II Certification
aliases: [Salesforce Certified Platform Administrator II, Salesforce Certified Advanced Administrator, Advanced Administrator certification, Plat-Admn-301]
domain: platform-architecture
summary: >-
  Salesforce's advanced administrator credential (formerly Advanced Administrator), earned through a proctored exam on
  security and access, objects and applications, auditing, cloud applications, data and analytics, environment management
  and process automation; it requires the Platform Administrator certification.
release: "Winter '27"
status: current
broader: [kt:salesforce-certification-program]
related: [kt:platform-app-builder-certification, kt:salesforce-sharing-model, kt:enterprise-territory-management, kt:order-of-execution, kt:change-sets]
relations:
  - {predicate: dependsOn, object: kt:platform-administrator-certification}
sources:
  - id: s1
    title: "Certification - Salesforce Certified Platform Administrator II"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/platformadministrator-ii
    type: official-learning
    accessed: 2026-11-15
  - id: s2
    title: "Salesforce Certified Platform Administrator II Exam Guide"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298969&language=en_US&type=1
    type: official-learning
    accessed: 2026-11-15
  - id: s3
    title: "Certification - Administrator Overview"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/administratoroverview
    type: official-learning
    accessed: 2026-11-15
  - id: s4
    title: "Prepare for your Salesforce Platform Administrator II Certification (trailmix)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/users/strailhead/trailmixes/prepare-for-your-salesforce-advanced-administrator-credential
    type: official-learning
    accessed: 2026-11-15
  - id: s5
    title: "Salesforce to Change the Name of 35 Certifications: What You Need to Know"
    publisher: Salesforce Ben
    url: https://www.salesforceben.com/salesforce-to-change-the-name-of-35-certifications-what-you-need-to-know/
    type: community
    accessed: 2026-11-15
  - id: s6
    title: "Introducing Annual Salesforce Certification Maintenance"
    publisher: Trailhead (The Trailblazer on Medium)
    url: https://medium.com/trailhead/annual-salesforce-certification-maintenance-eae60b25c1a6
    type: official-blog
    accessed: 2026-11-15
created: 2026-11-15
---

# Platform Administrator II Certification

The **Salesforce Certified Platform Administrator II** is the advanced credential in Salesforce's administrator track. Trailhead describes holders as experienced administrators who apply advanced features and functionality to solve a range of business problems.[^s1] It was previously called the **Salesforce Certified Advanced Administrator**; Salesforce renamed it as part of a broad rebranding of 35 certifications, and existing holders did not have to re-earn it.[^s5] The credential page links to its Trailhead Academy exam listing under the code Plat-Admn-301.[^s1] In the Administrator role track it sits beside Platform Administrator, Platform App Builder, Agentforce Specialist, Business Analyst and the Slack, Tableau and Marketing Cloud administrator credentials.[^s3]

## Who it is for

The official exam guide targets administrators who can work at an expert level across the platform: recommending configuration improvements and best practices, evaluating new features, and handling record and field access, custom objects and relationships, forecasting, Knowledge and entitlements, data quality, sandboxes and data movement, advanced reports and dashboards, and declarative automation.[^s2] The guide recommends the ADX211 course (Administer, Extend, and Automate Salesforce) or equivalent hands-on experience as preparation.[^s2] The **Salesforce Certified Platform Administrator** credential is a hard prerequisite.[^s1][^s2]

## Exam format and outline

Per the exam guide, the exam has 60 scored multiple-choice/multiple-select questions plus up to five unscored ones, a 105-minute time limit and a 65% passing score. Registration is US$200 and a retake US$100, plus applicable taxes. It is proctored online or at a testing centre, with no reference materials allowed.[^s2] The outline weights are:[^s2]

| Section | Weight |
|---|---|
| Security and Access | 20% |
| Objects and Applications | 19% |
| Auditing and Monitoring | 10% |
| Cloud Applications | 11% |
| Data and Analytics Management | 13% |
| Environment Management and Deployment | 7% |
| Process Automation | 20%[^s2] |

The two heaviest sections are scenario-driven. **Security and Access** asks how the sharing model affects record and field access (controlled-by-parent, hierarchies, report, dashboard and email folders, territory management), how profiles, permission sets and delegated administration compare, and how to choose between person accounts, business accounts and contacts related to multiple accounts.[^s2] **Process Automation** asks for the best tool or combination of tools for a complex problem, how to troubleshoot declarative automation, the limits of each tool, and how order of execution affects automation.[^s2] Other sections cover object design and Lightning UI choices, Setup Audit Trail and debug logs, products, quotes, forecasting, Knowledge, entitlements and Omni-Channel, data quality and import tools, advanced reporting, off-platform data such as big objects and external objects, and moving metadata with change sets, sandboxes and packages.[^s2]

## Preparation

The exam guide points to the official Platform Administrator II trailmix, a set of superbadges including Object Relationships, Flow Optimization, Record-Triggered Flows, Formulas and approval-process units, and the Trailhead Academy courses ADX211 and CRT211.[^s2] The trailmix itself is curated by Trailhead specifically to get candidates exam-ready, and the credential page links to it.[^s1][^s4] The guide also advises searching Salesforce Help for each outline topic and combining hands-on work with self-study.[^s2]

## Gotchas

- **Dated release alignment.** The guide states that questions align to the Summer '22 release, so newer features may be absent while some legacy tools still appear.[^s2]
- **Legacy automation is still in scope.** The audience profile still lists workflow rules alongside flows, approval processes and formulas, so expect questions that contrast older and newer declarative tools.[^s2]
- **Maintenance wording varies.** The guide says to complete the Administrator maintenance badge three times a year, but Trailhead moved all certifications to one maintenance module per year in 2020; check your Trailhead deadlines.[^s2][^s6]
- **The prerequisite must stay active.** Because Platform Administrator is required, letting it lapse affects this credential too.[^s1][^s2]

## Connections

- **broader → `kt:salesforce-certification-program`**: one credential in the Administrator role track.[^s3]
- **dependsOn → `kt:platform-administrator-certification`**: the required prerequisite credential.[^s1][^s2]
- **related → `kt:platform-app-builder-certification`**: listed by Trailhead as a related credential in the same track.[^s1]
- **related → `kt:salesforce-sharing-model`, `kt:enterprise-territory-management`**: sharing and territory access are core Security and Access objectives.[^s2]
- **related → `kt:order-of-execution`**: the Process Automation section tests how execution order affects automation.[^s2]
- **related → `kt:change-sets`**: the main deployment tool in the Environment Management and Deployment section.[^s2]

## Sources
[^s1]: Trailhead, "Certification - Salesforce Certified Platform Administrator II". https://trailhead.salesforce.com/credentials/platformadministrator-ii (accessed 2026-11-15)
[^s2]: Salesforce Help, "Salesforce Certified Platform Administrator II Exam Guide". https://help.salesforce.com/s/articleView?id=005298969&language=en_US&type=1 (accessed 2026-11-15)
[^s3]: Trailhead, "Certification - Administrator Overview". https://trailhead.salesforce.com/credentials/administratoroverview (accessed 2026-11-15)
[^s4]: Trailhead, "Prepare for your Salesforce Platform Administrator II Certification" (trailmix). https://trailhead.salesforce.com/users/strailhead/trailmixes/prepare-for-your-salesforce-advanced-administrator-credential (accessed 2026-11-15)
[^s5]: Salesforce Ben, "Salesforce to Change the Name of 35 Certifications: What You Need to Know". https://www.salesforceben.com/salesforce-to-change-the-name-of-35-certifications-what-you-need-to-know/ (accessed 2026-11-15)
[^s6]: Trailhead (The Trailblazer on Medium), "Introducing Annual Salesforce Certification Maintenance". https://medium.com/trailhead/annual-salesforce-certification-maintenance-eae60b25c1a6 (accessed 2026-11-15)
