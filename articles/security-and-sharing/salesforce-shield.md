---
id: kt:salesforce-shield
type: Product
title: Salesforce Shield
aliases: [Shield, Shield app, Salesforce Shield suite]
domain: security-and-sharing
summary: >-
  Paid suite of four Salesforce security, compliance and governance products — Shield Platform Encryption, Event
  Monitoring, Field Audit Trail and Data Detect — licensed as a bundle (or component by component) and managed from
  Setup and the Shield app.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:security-compliance-frameworks, kt:transaction-security-policies, kt:data-cloud, kt:classic-encryption]
relations:
  - {predicate: hasPart, object: kt:shield-platform-encryption}
  - {predicate: hasPart, object: kt:event-monitoring}
  - {predicate: hasPart, object: kt:field-audit-trail}
  - {predicate: hasPart, object: kt:data-detect}
  - {predicate: integratesWith, object: kt:crm-analytics}
sources:
  - id: s1
    title: "Salesforce Shield"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=salesforce_shield.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-06
  - id: s2
    title: "Protect Apps with Shield"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/secure-salesforce-configuration/protect-apps-with-shield
    type: official-learning
    accessed: 2026-11-06
  - id: s3
    title: "Strengthen Your Data's Security with Shield Platform Encryption"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.security_pe_overview.htm&type=5
    type: official-docs
    accessed: 2026-11-06
  - id: s4
    title: "Quick Start: Event Monitoring"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=000387928&amp=&type=1
    type: official-docs
    accessed: 2026-11-06
  - id: s5
    title: "Salesforce Event Monitoring Frequently Asked Questions"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=000396295&amp=&type=1
    type: official-docs
    accessed: 2026-11-06
  - id: s6
    title: "Identify and Protect Sensitive Data with Data Detect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-detect-quick-look/get-to-know-data-detect
    type: official-learning
    accessed: 2026-11-06
created: 2026-11-06
---

# Salesforce Shield

Salesforce Shield is a suite of security products that layers extra security, compliance and governance controls on top of an org's business-critical apps.[^s1] It is not a single feature but an umbrella for four products — Data Detect, Event Monitoring, Field Audit Trail and Shield Platform Encryption — each administered through point-and-click tooling in Setup or the dedicated Shield app.[^s1][^s2] Architects usually meet it when a regulated customer asks for encryption at rest with customer-controlled keys, forensic-grade activity logs, or field history kept far beyond the standard window.

## The four components

- **Shield Platform Encryption** encrypts data at rest, either across the database or field by field, while letting the customer control key material, including generating and storing it outside Salesforce.[^s1] By default the Shield Key Management Service derives keys on demand and caches them encrypted; customers can opt out of derivation per key or use external or cache-only key options.[^s2]
- **Event Monitoring** provides detailed performance, security and usage data: who accessed which data, logins and their origin, admins logging in as other users, page performance and more. Data can be analysed in Salesforce or exported to third-party monitoring tools.[^s1][^s2]
- **Field Audit Trail** reconstructs the state and value of data as of any past date, for regulatory compliance, audits, customer service and forensics; archived history lands in the `FieldHistoryArchive` big object under a retention policy deployed through Metadata API.[^s1][^s2]
- **Data Detect** scans the org (and Data Cloud) for sensitive values such as credit card or social security numbers in actual field content, using predefined and custom regex patterns, so admins can classify fields and decide what to protect. It runs natively, without moving data to third-party services.[^s1][^s6]

## How it works in practice

The Shield app is the central hub: it offers shortcuts into Setup, a direct interface for some features, a Setup Assistant per product, and insight into usage, data trends and job status. Salesforce recommends launching day-to-day tasks from it and notes that features may migrate from Setup into the app without changing behaviour.[^s1] Access to each product is granted separately through user permissions; for example, Event Monitoring setup needs the Event Monitoring User permission set, which also unlocks event log files, real-time events and the Threat Detection app.[^s1][^s4]

A typical adoption sequence follows the data: Data Detect finds sensitive fields, classification tags are updated, Platform Encryption policies protect those fields, Event Monitoring and transaction security policies watch and block risky access (such as exporting sensitive reports), and Field Audit Trail extends history for fields that change often.[^s6]

## Licensing, limits and gotchas

Verified against Winter '27:

- **Licensing.** Components are bought either as the full Shield suite or individually; Platform Encryption requires a Salesforce Shield or Shield Platform Encryption licence in Enterprise, Performance and Unlimited Editions, and is free in Developer Edition.[^s3] Event Monitoring likewise needs Shield or an Event Monitoring add-on and is available in Enterprise, Performance, Unlimited and Developer Editions.[^s4]
- **Sandboxes.** Platform Encryption becomes available in sandboxes only after it is provisioned for the production org.[^s3]
- **Free vs. paid event logs.** Without Shield, Enterprise, Performance and Unlimited orgs get a limited set of event types retained for one day; with Shield or the add-on, all log files are available, kept 30 days by default and extendable to 365 days. Paid logs cannot be retrieved for dates before the contract started.[^s5]
- **Event volume.** Turning on event log file generation produces more than 70 EventLogFile types; real-time events can be stored in big objects that do not count against data storage.[^s4]
- **Field history ceilings.** Trailhead contrasts 20 tracked fields per object with standard history against 60 with Field Audit Trail, and says archived data can be kept indefinitely; check the current Field Audit Trail guide for your entitlement.[^s2]
- **Not everything is Shield.** Data Detect's own guidance routes masking to Privacy Center (production) and Data Mask (sandboxes), and field-permission review to Security Center — separate products.[^s6]

## When to use it (and when not)

Shield fits orgs subject to regulatory or contractual controls that the base platform does not satisfy: encryption at rest with customer key control, long-lived audit evidence, and continuous monitoring with alerting. If the only need is basic login and setup auditing, the free event types and standard field history may be enough.[^s5][^s2] Because each component changes how data is stored, logged or retained, roll it out component by component and rehearse in a sandbox once the licence is provisioned for production.[^s3][^s1]

## Connections

Shield is a licensed product on the **Salesforce Platform** and **has parts** Shield Platform Encryption, Event Monitoring, Field Audit Trail and Data Detect.[^s1] Its Platform Encryption **contrasts with Classic Encryption**, and Data Detect extends into **Data Cloud**.[^s1][^s3] Event Monitoring feeds **transaction security policies** and **integrates with CRM Analytics** through the Event Monitoring Analytics app template.[^s4][^s6] Together the components are common controls in **security compliance frameworks** programs.[^s1][^s2]

## Sources

[^s1]: Salesforce Help, "Salesforce Shield". https://help.salesforce.com/s/articleView?id=salesforce_shield.htm&language=en_US&type=5 (accessed 2026-11-06)
[^s2]: Trailhead, "Protect Apps with Shield". https://trailhead.salesforce.com/content/learn/modules/secure-salesforce-configuration/protect-apps-with-shield (accessed 2026-11-06)
[^s3]: Salesforce Help, "Strengthen Your Data's Security with Shield Platform Encryption". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.security_pe_overview.htm&type=5 (accessed 2026-11-06)
[^s4]: Salesforce Help, "Quick Start: Event Monitoring". https://help.salesforce.com/s/articleView?language=en_US&id=000387928&amp=&type=1 (accessed 2026-11-06)
[^s5]: Salesforce Help, "Salesforce Event Monitoring Frequently Asked Questions". https://help.salesforce.com/s/articleView?language=en_US&id=000396295&amp=&type=1 (accessed 2026-11-06)
[^s6]: Trailhead, "Identify and Protect Sensitive Data with Data Detect". https://trailhead.salesforce.com/content/learn/modules/data-detect-quick-look/get-to-know-data-detect (accessed 2026-11-06)
