---
id: kt:salesforce-data-mask
type: Product
title: Salesforce Data Mask
aliases: [Data Mask, Data Mask managed package, Data Mask (Legacy), Salesforce Data Mask (Legacy)]
domain: devops-and-alm
summary: >-
  Salesforce's legacy, platform-native managed package that irreversibly masks or deletes sensitive data in Full and
  Partial Copy sandboxes; it is configured from production, runs only in sandboxes, and reaches end of service on
  December 31, 2026, with Data Mask & Seed as its successor.
release: "Winter '27"
status: deprecated
broader: [kt:environment-strategy, kt:data-governance]
related: [kt:sandbox-types, kt:sandbox-templates, kt:field-history-tracking, kt:order-of-execution]
relations:
  - {predicate: replacedBy, object: kt:data-mask-and-seed}
  - {predicate: dependsOn, object: kt:sandbox-types}
  - {predicate: alternativeTo, object: kt:sandbox-templates}
sources:
  - id: s1
    title: "Secure Your Sandbox Data with Salesforce Data Mask (Legacy)"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=platform.data_mask_overview.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-12
  - id: s2
    title: "Run a Data Mask Job"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=data_mask_manual_run.htm&type=5
    type: official-docs
    accessed: 2026-11-12
  - id: s3
    title: "Data Mask Best Practices"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=data_mask_recommended_data.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-12
  - id: s4
    title: "Get to Know Salesforce Data Mask (Trailhead)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-data-mask/get-to-know-salesforce-data-mask
    type: official-learning
    accessed: 2026-11-12
  - id: s5
    title: "Install and Configure Salesforce Data Mask (Trailhead)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-data-mask/install-and-configure-salesforce-data-mask
    type: official-learning
    accessed: 2026-11-12
  - id: s6
    title: "Data Mask: Secure Your Sandbox"
    publisher: Salesforce Blog
    url: https://www.salesforce.com/blog/data-mask-secure-sandbox/
    type: official-blog
    accessed: 2026-11-12
created: 2026-11-12
---

# Salesforce Data Mask

Salesforce Data Mask is a managed package that obfuscates sensitive data in Full and Partial Copy sandboxes, so teams
can develop and test against realistic, production-shaped data without exposing personal information.[^s1][^s4]
Salesforce now labels it the legacy version of its masking solution: service for the package ends on December 31,
2026, and customers are directed to start using Data Mask & Seed before that date.[^s1] It is available in Lightning
Experience for Professional, Enterprise, Unlimited and Developer Editions with the Data Mask managed package (Legacy)
add-on license.[^s1][^s2]

Salesforce announced Data Mask at Dreamforce '19, pitching it as a platform-native way to close the privacy gap that
sandboxes open up when production data is copied for testing, with regulations such as GDPR, PCI DSS and HIPAA as the
backdrop.[^s6] Because masking happens inside Salesforce, data does not leave the platform and there are no external
dependencies.[^s6]

## How it works

The package is installed in production, but masking jobs run only in sandboxes, which keeps production records from
being masked by accident.[^s1][^s2] A masking configuration can be built in production, where it carries into each new
or refreshed sandbox, or directly in an existing sandbox; Salesforce recommends building it in production so policies
are managed in one place.[^s1][^s3] A configuration has a name and API name, options for case comments, emails and
Chatter feeds, and a list of standard and custom objects with a rule for each sensitive field.[^s5]

Field rules fall into a small set of masking levels:[^s1][^s5]

- **Random characters or numbers**: readable but unrecognizable values; numeric rules take a minimum and maximum.[^s5]
- **Library (similarly mapped) values**: realistic substitutes such as first names, companies, emails or cities.[^s5]
- **Pattern**: values generated from a defined pattern, as the sample configuration does for email addresses.[^s1][^s3]
- **Delete**: empties the field; the most compute-efficient choice, but it can block testing of some processes.[^s4]

Custom libraries can hold arbitrary strings, including long text, integers and non-English characters.[^s1] Masking is
nondeterministic, so the original values cannot be recovered by reverse engineering or statistical inference, and it
is irreversible: the only way back to real data is to refresh the sandbox from production.[^s1][^s4][^s6]

A job can be started manually from the sandbox or scheduled to run automatically after each sandbox refresh.[^s1][^s2]
The Jobs tab shows each object's stage, the number of records matched, masked, deleted or in error, and per-record
error details, and an email is sent on completion when Email Deliverability allows all email.[^s2]

## Limits and gotchas

- Jobs run asynchronously and can take several hours on large sandboxes.[^s2]
- A job bypasses triggers, workflow rules, validation rules, flows and feed tracking, including managed-package ones.[^s2]
- When a job finishes it deletes all Field History Tracking for the masked object.[^s2]
- Checkbox, lookup and picklist field types aren't supported by masking rules.[^s5]
- Very large objects (over 20 million records, over 400 custom fields) should be split into smaller configurations.[^s3]
- Some records can be left unmasked by a limitation; data filters let a follow-up run target just those records.[^s3]
- Avoid big data loads or complex queries in the sandbox while a job runs, to prevent performance degradation.[^s3]
- Account First Name and Last Name rules apply only when Person Accounts are enabled.[^s3]

Salesforce's own advice is to start with fields that hold PII, mask only the objects and fields you need, copy only
the production data you must test, and spot-check results (for example with queries in the Developer Console) before
giving more users access to the sandbox.[^s2][^s3]

## When to use it (and when not)

Data Mask fits any team that copies real customer data into Full or Partial Copy sandboxes for UAT, training or
performance testing and must keep those copies within privacy obligations.[^s1][^s6] It masks what a refresh copies; it
does not choose which records are copied, so it is paired with sandbox templates that limit a Partial Copy's scope.[^s3]
Its scope is Full and Partial Copy sandboxes, so other environments are out of reach.[^s1][^s4] Given the December 31, 2026 end of service, new implementations should go to Data Mask & Seed instead, and
existing users should plan the migration now.[^s1]

## Connections

Data Mask sits under `kt:environment-strategy`, where deciding how production data reaches lower environments is a core
concern, and under `kt:data-governance`, whose masking controls it enforces for copied data.[^s1][^s3] It **depends on**
`kt:sandbox-types`, since it works only in Full and Partial Copy sandboxes, and it complements `kt:sandbox-templates`,
which decide which records a refresh copies before masking.[^s1][^s3] Its job behaviour touches
`kt:field-history-tracking`, which it clears, and `kt:order-of-execution`, whose automations it bypasses.[^s2] It is
**replaced by** `kt:data-mask-and-seed`, the successor Salesforce names for masking going forward.[^s1]

## Sources

[^s1]: Salesforce Help, "Secure Your Sandbox Data with Salesforce Data Mask (Legacy)". https://help.salesforce.com/s/articleView?id=platform.data_mask_overview.htm&language=en_US&type=5 (accessed 2026-11-12)
[^s2]: Salesforce Help, "Run a Data Mask Job". https://help.salesforce.com/s/articleView?language=en_US&id=data_mask_manual_run.htm&type=5 (accessed 2026-11-12)
[^s3]: Salesforce Help, "Data Mask Best Practices". https://help.salesforce.com/s/articleView?id=data_mask_recommended_data.htm&language=en_US&type=5 (accessed 2026-11-12)
[^s4]: Trailhead, "Get to Know Salesforce Data Mask". https://trailhead.salesforce.com/content/learn/modules/salesforce-data-mask/get-to-know-salesforce-data-mask (accessed 2026-11-12)
[^s5]: Trailhead, "Install and Configure Salesforce Data Mask". https://trailhead.salesforce.com/content/learn/modules/salesforce-data-mask/install-and-configure-salesforce-data-mask (accessed 2026-11-12)
[^s6]: Salesforce Blog, "Data Mask: Secure Your Sandbox". https://www.salesforce.com/blog/data-mask-secure-sandbox/ (accessed 2026-11-12)
