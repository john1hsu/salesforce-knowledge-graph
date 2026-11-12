---
id: kt:data-governance
type: Concept
title: Data Governance
aliases: [Salesforce data governance, enterprise data governance, data governance program, data governance framework]
domain: data-model
summary: >-
  The practice of setting and enforcing policies, standards, procedures and accountability so Salesforce data stays
  trusted, secure, usable and compliant across its lifecycle; carried out by data stewards and supported by platform
  features such as field classification metadata, Data 360 tags and policies, access controls and masking.
release: "Winter '27"
status: concept
broader: [kt:data-management]
related: [kt:data-quality, kt:data-sovereignty, kt:data-residency, kt:salesforce-center-of-excellence, kt:salesforce-data-mask]
relations:
  - {predicate: partOf, object: kt:salesforce-governance}
  - {predicate: hasPart, object: kt:data-stewardship}
  - {predicate: hasPart, object: kt:data-classification}
  - {predicate: dependsOn, object: kt:field-level-security}
  - {predicate: integratesWith, object: kt:data-cloud}
  - {predicate: coveredBy, object: kt:platform-data-architect-certification}
  - {predicate: coveredBy, object: kt:data-cloud-consultant-certification}
sources:
  - id: s1
    title: "Describe Data Management (Data Management Fundamentals)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-management-fundamentals/describe-data-management
    type: official-learning
    accessed: 2026-11-12
  - id: s2
    title: "Review Data Management Concepts (Data Management Fundamentals)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/es-MX/content/learn/modules/data-management-fundamentals/review-data-management-concepts
    type: official-learning
    accessed: 2026-11-12
  - id: s3
    title: "Monitor Data Quality Through Governance and Stewardship (Data Monitoring Fundamentals)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-monitoring-fundamentals/monitor-data-quality-through-governance-and-stewardship
    type: official-learning
    accessed: 2026-11-12
  - id: s4
    title: "Understand the Importance of Data Governance (Data 360 Data Governance Strategies)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-cloud-data-governance-strategies/understand-the-importance-of-data-governance
    type: official-learning
    accessed: 2026-11-12
  - id: s5
    title: "Design Your Governance Strategy (Data 360 Data Governance Strategies)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-cloud-data-governance-strategies/design-your-governance-strategy
    type: official-learning
    accessed: 2026-11-12
  - id: s6
    title: "Know Your Metadata (Data Reliability Risk Factors for AI)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/it/content/learn/modules/data-reliability-risk-factors-for-ai/know-your-metadata
    type: official-learning
    accessed: 2026-11-12
  - id: s7
    title: "Salesforce Data Security: The Role of Effective Data Classification"
    publisher: Salesforce Blog (Australia)
    url: https://www.salesforce.com/au/blog/salesforce-data-security-the-role-of-effective-data-classification/
    type: official-blog
    accessed: 2026-11-12
  - id: s8
    title: "Salesforce Certified Platform Data Architect Exam Guide"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298972&type=1&language=en_US
    type: official-learning
    accessed: 2026-11-12
  - id: s9
    title: "Salesforce Certified Data 360 Consultant Exam Guide"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298940&type=1&language=en_US
    type: official-learning
    accessed: 2026-11-12
created: 2026-11-12
---

# Data Governance

Data governance is the practice of setting and enforcing the policies, standards and procedures that keep data managed
effectively and consistently through its whole lifecycle.[^s2] Trailhead describes it as a structured approach for
keeping data trusted, secure, usable and compliant, and stresses that it also assigns accountability: it defines the
rules and the quality bar that everyone else works to.[^s3] Salesforce's Data Management Fundamentals module, which
draws on the DAMA body of knowledge, treats governance as one of seven data management functions alongside data
quality, architecture, application development, integration, security and operations.[^s1]

## What a governance program covers

Trailhead places governance in the planning stage of data management, next to data strategy and data architecture.[^s2]
In practice a program defines who may share what: its example company lets order data flow between retail stores and
ecommerce within one brand so returns are simpler, under explicitly written line-of-business policies.[^s2] Typical
policy areas include:

- **Standards and accountability**: rules, quality expectations and named owners for important data.[^s1][^s3]
- **Retention**: how long data is kept and how it is disposed of, driven by legal and business needs.[^s2]
- **Classification**: marking which fields hold sensitive or regulated data, such as PII or payment card data.[^s6]
- **Access**: least-privilege rules for who can view, edit or see masked values of sensitive data.[^s4]

The retention example shows the level of detail expected: purchase history kept seven years for legal reasons, order
detail archived after three and purged after seven, with order date and amount kept for loyalty programs.[^s2]

## Governance, stewardship and monitoring

Salesforce separates three roles. Governance defines the rules and accountability; stewardship puts them into practice
by monitoring quality, investigating issues and coordinating fixes; and monitoring supplies the evidence of drift, the
gradual loss of quality or business value in data and configuration metadata.[^s3] Trailhead recommends a lightweight
team of business and technology stakeholders that starts with a few business-critical fields, uses reports for
point-in-time checks and adds automated monitoring and alerts to catch drift early.[^s3] Field history, audit logs,
profiling, stakeholder reviews and Flow-triggered alerts are the suggested monitoring tools.[^s3]

## Platform support in Salesforce

On the core platform, governance starts with field metadata. A Salesforce security architect describes classification
attributes for data sensitivity (defaults such as Public, Internal and Confidential) and compliance category (such as
PII, PCI and HIPAA), both customizable, plus ownership and usage context.[^s7] Security Center's Data Classification tool
applies these in bulk with templates, a wizard and filters, and the resulting labels feed Data Mask for sandboxes,
Transaction Security Policies that block exports, and Privacy Center workflows for retention and data subject
requests.[^s7] Trailhead adds that descriptions, help text, a business owner and usage notes matter for AI: agents
misread or overexpose fields whose metadata is missing.[^s6]

In Data 360, governance is built around four capabilities:[^s4]

- **Tagging and classification**: labels such as pii.email or confidential, grouped into classifications.[^s4]
- **Policies and enforcement**: rules on who can view, edit or mask data, set once and applied to any tagged asset.[^s4]
- **Access controls**: record-level and field-level security plus role-based and attribute-based access control.[^s4]
- **Dynamic data masking**: some users see masked values while authorized users see the real ones.[^s4]

The strategy unit advises tagging only data that affects privacy, compliance or critical decisions, building a
hierarchical tag taxonomy so a child tag inherits its parent's policies, and using Suggest Tags, which reads object and
field metadata (not field values) and needs administrator approval for every suggestion.[^s5] Propagation carries tags
to downstream objects such as unified profiles, but results still need human review for misclassifications.[^s5]

## Gotchas

Over-tagging adds overhead without proportional benefit, and a single misclassification can create a security or
compliance gap.[^s5] Governance failures are costly: Trailhead cites data leaks, inconsistent customer views across
teams, audit failures and fines under privacy laws such as GDPR and CCPA, and wasted manual cleanup.[^s4]

## Connections

Data governance sits under `kt:data-management` as one of its functions, and it is **part of** the wider
`kt:salesforce-governance` framework, typically run through a `kt:salesforce-center-of-excellence`.[^s1] It **has
parts** `kt:data-stewardship` and `kt:data-classification`, and it defines the expectations that `kt:data-quality`
measures.[^s3][^s7] Access policies **depend on** `kt:field-level-security`, and masking of copied data uses
`kt:salesforce-data-mask`.[^s4][^s7] It **integrates with** `kt:data-cloud` (Data 360), whose tags and policies carry
governance to unified data.[^s4] `kt:data-residency` and `kt:data-sovereignty` are location and jurisdiction concerns
that a governance program must address.[^s4] The Platform Data Architect exam gives Data Governance 10% weight,
covering GDPR-compliant data models and enterprise governance programs, and the Data 360 Consultant exam asks
candidates to apply governance requirements to configuration, hence the two `coveredBy` edges.[^s8][^s9]

## Sources

[^s1]: Trailhead, "Describe Data Management". https://trailhead.salesforce.com/content/learn/modules/data-management-fundamentals/describe-data-management (accessed 2026-11-12)
[^s2]: Trailhead, "Review Data Management Concepts". https://trailhead.salesforce.com/es-MX/content/learn/modules/data-management-fundamentals/review-data-management-concepts (accessed 2026-11-12)
[^s3]: Trailhead, "Monitor Data Quality Through Governance and Stewardship". https://trailhead.salesforce.com/content/learn/modules/data-monitoring-fundamentals/monitor-data-quality-through-governance-and-stewardship (accessed 2026-11-12)
[^s4]: Trailhead, "Understand the Importance of Data Governance". https://trailhead.salesforce.com/content/learn/modules/data-cloud-data-governance-strategies/understand-the-importance-of-data-governance (accessed 2026-11-12)
[^s5]: Trailhead, "Design Your Governance Strategy". https://trailhead.salesforce.com/content/learn/modules/data-cloud-data-governance-strategies/design-your-governance-strategy (accessed 2026-11-12)
[^s6]: Trailhead, "Know Your Metadata". https://trailhead.salesforce.com/it/content/learn/modules/data-reliability-risk-factors-for-ai/know-your-metadata (accessed 2026-11-12)
[^s7]: Salesforce Blog (Australia), "Salesforce Data Security: The Role of Effective Data Classification". https://www.salesforce.com/au/blog/salesforce-data-security-the-role-of-effective-data-classification/ (accessed 2026-11-12)
[^s8]: Salesforce Help, "Salesforce Certified Platform Data Architect Exam Guide". https://help.salesforce.com/s/articleView?id=005298972&type=1&language=en_US (accessed 2026-11-12)
[^s9]: Salesforce Help, "Salesforce Certified Data 360 Consultant Exam Guide". https://help.salesforce.com/s/articleView?id=005298940&type=1&language=en_US (accessed 2026-11-12)
