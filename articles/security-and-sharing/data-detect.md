---
id: kt:data-detect
type: Feature
title: Data Detect
aliases: [Salesforce Data Detect, Shield Data Detect, Einstein Data Detect]
domain: security-and-sharing
summary: >-
  Salesforce Shield component that scans the actual contents of text fields for sensitive values such as government
  IDs or card numbers, using predefined and regex-based detection patterns, so admins can classify, encrypt, mask or
  monitor the fields where that data turns up.
release: "Winter '27"
status: current
broader: [kt:salesforce-shield]
related: [kt:salesforce-data-mask, kt:field-audit-trail, kt:event-monitoring]
relations:
  - {predicate: requiresLicense, object: kt:salesforce-shield}
  - {predicate: integratesWith, object: kt:data-classification}
  - {predicate: enables, object: kt:shield-platform-encryption}
  - {predicate: integratesWith, object: kt:transaction-security-policies}
  - {predicate: dependsOn, object: kt:field-level-security}
  - {predicate: queriedWith, object: kt:soql}
sources:
  - id: s1
    title: "Get to Know Data Detect (Data Detect Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-detect-quick-look/get-to-know-data-detect
    type: official-learning
    accessed: 2026-11-15
  - id: s2
    title: "Get Started with Data Detect (Precise Data Detection at Scale)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/precise-data-detection-at-scale/get-started-with-data-detect
    type: official-learning
    accessed: 2026-11-15
  - id: s3
    title: "View Data Detect Policy Scan Results"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/precise-data-detection-at-scale/view-data-detect-policy-scan-results
    type: official-learning
    accessed: 2026-11-15
  - id: s4
    title: "How to Detect Sensitive Data at Scale"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/how-to-detect-sensitive-data-at-scale/
    type: official-blog
    accessed: 2026-11-15
  - id: s5
    title: "Data Detect with Shield (Admin Security Workshop)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/workshops/admin-security-workshop/data-security/1-data-detect-with-shield
    type: official-learning
    accessed: 2026-11-15
  - id: s6
    title: "DataDetectPolicy (Object Reference for the Salesforce Platform)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_datadetectpolicy.htm
    type: official-docs
    accessed: 2026-11-15
created: 2026-11-15
---

# Data Detect

Data Detect is the discovery piece of Salesforce Shield: it finds sensitive data — personally identifiable information, financial data, medical records — that has ended up in an org, often in free-text fields nobody intended to hold it.[^s4] Where the other Shield products encrypt, monitor or retain data, Data Detect answers the prior question of where the sensitive data actually lives.[^s5] It runs as native platform technology, so scans happen inside Salesforce without moving data to third-party services.[^s1] Trailhead lists it for Enterprise, Performance, Unlimited and Developer editions.[^s1]

## How it works

Unlike a metadata review, Data Detect inspects the values stored in fields. If a field repeatedly contains, say, Social Security numbers, that is evidence the field holds sensitive data and should be classified accordingly; multilevel validation and recurring-pattern logic are used to cut false positives from one-off matches.[^s1] Salesforce ships 21 pre-configured detection rules, and admins can add custom patterns written as regular expressions for proprietary identifiers such as employee, student or contract numbers.[^s4][^s1] A custom pattern or keyword is capped at 255 characters.[^s2]

Work is organised into **policies**. A policy names the objects and fields to scan, the sensitive data categories to look for, and the date range of records to examine; it can run once or recur weekly, monthly or yearly, and scans cover records created or changed in that window.[^s1] Policies are built in the Shield app's Data Detect tab, then queued with Run Scan, so admins can carry on while the scan executes.[^s5] Under the hood a policy is stored as a `DataDetectPolicy` record, available from API version 60.0, which holds the data types, filters and object/field scope for a scan.[^s6]

When a scan finishes, Salesforce sends an email and the results appear in the Data Detect Job Sessions tab. Each session is a point-in-time snapshot, so comparing sessions shows whether exposure is growing or shrinking.[^s3] An aggregate view groups detections by object and sensitive data category for stakeholders, while the scan-results view lists record IDs and the exact fields for remediation.[^s3] Results can also be exported as CSV or queried with SOQL and pulled into tools such as Data Loader.[^s4]

## Limits and gotchas

- Only text-based fields are scanned (Text, Text Area, Long Text Area, Rich Text and encrypted text); for Rich Text only the plain-text content is checked.[^s1][^s2]
- In orgs with Person Accounts enabled, the Account object is not supported for scanning.[^s2]
- Users can only view and scan the objects and fields they already have access to, so the scanning admin's field-level security bounds the results.[^s2]
- The results dashboard shows up to 200 results per field, and a CSV download holds up to 10 million results; beyond that, copy the SOQL query and retrieve results via the API.[^s3]
- Badly written regex can slow scans or make them fail; test patterns first, narrow the scope, exclude already-classified fields, and sample a past period before a full scan.[^s2][^s1]

## When to use it (and when not)

Use Data Detect when you need evidence, not assumptions, about where regulated data sits — for GDPR, CCPA or HIPAA programmes, before an encryption rollout, or when users are suspected of typing IDs into Description or Notes fields.[^s2] It is a discovery tool, not a control: it does not itself block entry, encrypt or mask values. Preventing bad entry still needs validation rules or UI design, and protection comes from the follow-up products below.[^s1]

## Connections

Data Detect is part of, and licensed through, **Salesforce Shield**.[^s4] Its main output feeds **data classification**: admins update each field's sensitivity level and compliance categorization directly from results, in a repeating scan-and-reclassify cycle.[^s4] Those classifications in turn drive **Shield Platform Encryption** policies and **transaction security policies** in **Event Monitoring**, for example blocking report exports of sensitive fields.[^s1] For sandboxes, **Salesforce Data Mask** scrubs the values it finds, and **Field Audit Trail** can extend history retention on fields that often hold sensitive data.[^s1][^s3] Because scans honour **field-level security** and results are queryable with **SOQL**, the scanning user's access and query tooling shape what an audit sees.[^s2][^s4]

## Sources
[^s1]: Trailhead, "Get to Know Data Detect". https://trailhead.salesforce.com/content/learn/modules/data-detect-quick-look/get-to-know-data-detect (accessed 2026-11-15)
[^s2]: Trailhead, "Get Started with Data Detect". https://trailhead.salesforce.com/content/learn/modules/precise-data-detection-at-scale/get-started-with-data-detect (accessed 2026-11-15)
[^s3]: Trailhead, "View Data Detect Policy Scan Results". https://trailhead.salesforce.com/content/learn/modules/precise-data-detection-at-scale/view-data-detect-policy-scan-results (accessed 2026-11-15)
[^s4]: Salesforce, "How to Detect Sensitive Data at Scale". https://www.salesforce.com/blog/how-to-detect-sensitive-data-at-scale/ (accessed 2026-11-15)
[^s5]: Salesforce Developers, "Data Detect with Shield" workshop. https://developer.salesforce.com/workshops/admin-security-workshop/data-security/1-data-detect-with-shield (accessed 2026-11-15)
[^s6]: Salesforce Developers, "DataDetectPolicy". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_datadetectpolicy.htm (accessed 2026-11-15)
