---
id: kt:data-quality
type: Concept
title: Data Quality
aliases: [Salesforce data quality, data quality management, data hygiene, CRM data quality, data quality dimensions]
domain: data-model
summary: >-
  The degree to which Salesforce records are fresh, complete, accurate, consistent, unduplicated and actually used;
  managed through a plan of standards, platform controls (required fields, validation rules, picklists, duplicate
  management) and ongoing monitoring by data stewards.
release: "Winter '27"
status: concept
broader: [kt:data-architecture, kt:data-governance]
related: [kt:duplicate-management, kt:validation-rules, kt:field-history-tracking, kt:data-migration-strategy]
relations:
  - {predicate: enables, object: kt:agentforce}
  - {predicate: coveredBy, object: kt:platform-data-architect-certification}
sources:
  - id: s1
    title: "Get Started with Data Quality (Data Quality module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data_quality/data_quality_getting_started
    type: official-learning
    accessed: 2026-11-10
  - id: s2
    title: "Assess the Quality of Data (Data Quality module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data_quality/data_quality_assess_your_data
    type: official-learning
    accessed: 2026-11-10
  - id: s3
    title: "Improve Data Quality (Data Quality module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data_quality/data_quality_improve_quality
    type: official-learning
    accessed: 2026-11-10
  - id: s4
    title: "Monitor Data Quality Through Governance and Stewardship (Data Monitoring Fundamentals)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-monitoring-fundamentals/monitor-data-quality-through-governance-and-stewardship
    type: official-learning
    accessed: 2026-11-10
  - id: s5
    title: "Understand Salesforce Capabilities for Reliable Data Readiness (AI Data Readiness Assessment Fundamentals)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/fr/content/learn/modules/ai-data-readiness-assessment-fundamentals/understand-salesforce-capabilities-for-reliable-data-readiness
    type: official-learning
    accessed: 2026-11-10
  - id: s6
    title: "Salesforce Certified Platform Data Architect Exam Guide"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298972&type=1&language=en_US
    type: official-learning
    accessed: 2026-11-10
  - id: s7
    title: "Why Effective Data Stewardship Gives You a Competitive Edge"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2019/why-effective-data-stewardship-gives-you-a-competitive-edge
    type: official-blog
    accessed: 2026-11-10
created: 2026-11-10
---

# Data Quality

Data quality is how fit Salesforce records are for the business uses that depend on them: targeting prospects,
aligning territories, scoring and routing leads, finding cross-sell opportunities, serving customers and complying
with privacy rules such as GDPR.[^s1] Trailhead frames poor data in terms of cost, citing an Econsultancy figure that
the average company loses 12% of revenue to inaccurate data and a Gartner figure that 40% of business initiatives miss
their targeted benefits because of poor data.[^s1] Data also decays on its own: Trailhead notes that, on average,
120 business addresses and 75 phone numbers change every 30 minutes, so quality is a continuous practice rather than a
one-time cleanup.[^s1][^s3]

## Dimensions and how to measure them

Salesforce's Data Quality module assesses data along six dimensions, each with a practical check:[^s2]

- **Age**: how recently records were updated; report on Last Modified Date and see what share is recent.[^s2]
- **Completeness**: whether the fields each business use needs are filled; report on the percentage of blanks.[^s2]
- **Accuracy**: whether values match a trusted source, usually via a matching app from AgentExchange.[^s2]
- **Consistency**: whether formats and values are uniform; count variants in date, currency, state, country and language fields.[^s2]
- **Duplication**: whether records repeat; use Duplicate Management and, if needed, a detection app.[^s2]
- **Usage**: whether the data actually feeds reports, dashboards and apps.[^s2]

The module's hands-on exercise installs the Data Quality Analysis Dashboards package and runs its high-level and
Account, Contact and Opportunity dashboards to spot gaps such as opportunities missing Lead Source or Next Steps.[^s2]
A 2019 Salesforce Admins blog post reported Salesforce findings that CRM systems hold about 15% duplicate sales and
service records and that about 20% of records contain useless or dead data.[^s7]

## How it is improved in Salesforce

Trailhead recommends starting with a data management plan that sets naming and formatting conventions, record
life-cycle workflow, measurable targets for the six dimensions, record ownership and accountability, security and
privacy levels, and regular monitoring with dashboard metrics.[^s3] The plan is then enforced with platform features:[^s3]

- **Required fields and page layouts** that remove unused fields and put mandatory ones at the top for each role.[^s3]
- **Validation rules** that check formats on save, for example phone numbers or customer IDs, and require key fields.[^s3]
- **Field types and picklists**: Date and Currency types, value lists, and state and country picklists for addresses.[^s3]
- **Duplicate management** to keep one account per customer and block new duplicates at entry.[^s3]
- **Flows** that automate routing, and **enrichment apps** that re-match records against a trusted source.[^s3]

Prevention at the point of entry is cheaper than cleanup later, which is why stewards also run regular duplicate checks
and archive inactive records.[^s7]

## Governance, stewardship and monitoring

Trailhead separates three roles. Data governance sets the policies, standards and accountability that define quality
expectations; data stewardship puts them into practice by monitoring, investigating and coordinating fixes; and data
monitoring links the two by supplying evidence of drift, the gradual decay of data or configuration.[^s4] It advises
starting with a few business-critical fields, using reports for point-in-time checks, adding automated profiling and
alerts for early detection, and drawing on field history, audit logs and Flow-triggered actions.[^s4]

## Data quality for AI

Poor data leads AI to biased or unreliable results, while clean data makes models more accurate and robust.[^s1] For
Agentforce, Trailhead maps data readiness to Salesforce capabilities: Data 360 transforms for standardization,
duplicate management and Data 360 identity resolution for unified profiles, the Object Manager data dictionary or
semantic layer for metadata, permission sets and field-level security to keep unreliable fields away from agents, and
reports, dashboards and alerts for continuous monitoring.[^s5]

## Connections

Data quality sits under `kt:data-architecture` and is defined and owned through `kt:data-governance`.[^s4] Its main
in-platform controls have their own nodes: `kt:validation-rules` for format and completeness checks on save and
`kt:duplicate-management` for blocking and merging duplicates.[^s3] `kt:field-history-tracking` provides the change
history stewards use to see how and when data drifted.[^s4] `kt:data-migration-strategy` is where quality is most at
risk: the Platform Data Architect exam asks candidates to recommend techniques for high data quality at load time, and
its data governance and master data sections also touch this topic, hence the `coveredBy` edge to
`kt:platform-data-architect-certification`.[^s6] Finally, data quality `enables` `kt:agentforce`, since agent answers are
only as reliable as the records they are grounded in.[^s5]

## Sources

[^s1]: Trailhead, "Get Started with Data Quality". https://trailhead.salesforce.com/content/learn/modules/data_quality/data_quality_getting_started (accessed 2026-11-10)
[^s2]: Trailhead, "Assess the Quality of Data". https://trailhead.salesforce.com/content/learn/modules/data_quality/data_quality_assess_your_data (accessed 2026-11-10)
[^s3]: Trailhead, "Improve Data Quality". https://trailhead.salesforce.com/content/learn/modules/data_quality/data_quality_improve_quality (accessed 2026-11-10)
[^s4]: Trailhead, "Monitor Data Quality Through Governance and Stewardship". https://trailhead.salesforce.com/content/learn/modules/data-monitoring-fundamentals/monitor-data-quality-through-governance-and-stewardship (accessed 2026-11-10)
[^s5]: Trailhead, "Understand Salesforce Capabilities for Reliable Data Readiness". https://trailhead.salesforce.com/fr/content/learn/modules/ai-data-readiness-assessment-fundamentals/understand-salesforce-capabilities-for-reliable-data-readiness (accessed 2026-11-10)
[^s6]: Salesforce Help, "Salesforce Certified Platform Data Architect Exam Guide". https://help.salesforce.com/s/articleView?id=005298972&type=1&language=en_US (accessed 2026-11-10)
[^s7]: Salesforce Admins Blog, "Why Effective Data Stewardship Gives You a Competitive Edge". https://admin.salesforce.com/blog/2019/why-effective-data-stewardship-gives-you-a-competitive-edge (accessed 2026-11-10)
