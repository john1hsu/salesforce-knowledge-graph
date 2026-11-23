---
id: kt:setup-audit-trail
type: Feature
title: Setup Audit Trail
aliases: [View Setup Audit Trail, SetupAuditTrail, setup change history, audit trail]
domain: security-and-sharing
summary: >-
  Built-in, always-on Salesforce log of configuration changes made in Setup (who changed what, where and when),
  viewable in Setup, downloadable as a CSV, and queryable through the SetupAuditTrail object for at least 180 days.
release: "Winter '27"
status: current
broader: [kt:security-governance]
related: [kt:event-monitoring, kt:field-audit-trail, kt:login-history, kt:security-health-check, kt:sarbanes-oxley-act, kt:continuous-monitoring]
relations:
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: contrastsWith, object: kt:field-history-tracking}
  - {predicate: consumedBy, object: kt:agentforce-setup-agent}
sources:
  - id: s1
    title: "SetupAuditTrail — Object Reference for the Salesforce Platform"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_setupaudittrail.htm
    type: official-docs
    accessed: 2026-11-23
  - id: s2
    title: "Exercise 1: Using the Audit Trail — Salesforce Admin Security Workshop"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/workshops/admin-security-workshop/monitoring-and-response/1-audit-trail
    type: official-learning
    accessed: 2026-11-23
  - id: s3
    title: "Monitor Your Salesforce Org — Setup with Agentforce for Admins"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/pt-BR/content/learn/modules/setup-with-agentforce-for-admins/monitor-your-salesforce-org
    type: official-learning
    accessed: 2026-11-23
  - id: s4
    title: "Salesforce Audit Trail & Field History: limits & how to extend"
    publisher: Gearset
    url: https://gearset.com/blog/salesforce-audit-trail/
    type: partner
    accessed: 2026-11-23
  - id: s5
    title: "Auditing Salesforce: The Setup Audit Trail and Field History Tracking"
    publisher: Netwrix
    url: https://netwrix.com/en/resources/blog/auditing-salesforce-the-setup-audit-trail-and-field-history-tracking/
    type: partner
    accessed: 2026-11-23
created: 2026-11-23
---

# Setup Audit Trail

Setup Audit Trail is the Salesforce platform's record of configuration changes made in the Setup area by administrators and other privileged users. Each entry captures who made the change, when, in which Setup section, and a readable description of what was done, and the platform exposes this history through the SetupAuditTrail object for at least the last 180 days.[^s1] It is on by default and needs no configuration, which makes it the first place an admin looks when something in the org changed unexpectedly.[^s4]

## What it records

The trail is about metadata and security configuration, not record data.[^s4] Salesforce's admin security workshop uses it to investigate changes to multi-factor authentication requirements, edits to Login IP Ranges, and permission set assignments; its worked example traces a deleted Login IP Range back to the admin who removed it and the time it happened.[^s2] Partner write-ups list a wider span: company and currency information, profiles and permission sets, custom objects and fields, record types, password policies, session settings, network access and single sign-on settings.[^s4][^s5]

Each row in the SetupAuditTrail object carries an action category (for example a permission set creation), a full display description of the change, and the Setup section where it happened, such as Manage Users or Company Profile.[^s1] Since API version 35.0 the object also records the delegate user when an admin acted through Login-As, and since API version 45.0 it can note the context of a change, such as Einstein for cloud-to-cloud changes.[^s1]

## How to use it

In the UI, admins open **Setup → Security → View Setup Audit Trail** and download roughly the last six months of entries as a .csv file, then search the export for keywords such as "Login IP", "MFA" or "Permission Set".[^s2] A partner guide notes that the page itself shows only the 20 most recent entries, that viewing it requires the View Setup and Configuration permission, and that the generated CSV is held temporarily for download.[^s4]

Programmatically, SetupAuditTrail has been available since API version 15.0 and supports query(), retrieve() and count(), so a SOQL query such as selecting the creator name with a small LIMIT returns the last people to change Setup.[^s1] The object cannot be used as a Visualforce standard controller.[^s1]

The Trailhead module on Agentforce for admins shows a conversational route as well: the Setup agent can filter audit trail data on request, for example listing all Setup changes from the last week or only those related to permission sets, and returns them as a list view.[^s3]

## Limits and gotchas

- Retention is about 180 days; entries older than that are removed and cannot be recovered natively, so export or archive them if audits need a longer look-back.[^s1][^s4]
- It records the fact of most changes but not full before-and-after values for most of them, so it rarely answers what an old setting was.[^s4]
- It does not show whether a change was reviewed or approved, and it misses some changes such as list view edits and new report creation.[^s5]
- It is not an activity log: report exports and detailed user behaviour belong to Event Monitoring, and logins belong to Login History.[^s2][^s4]

## When to use it (and when not)

Use Setup Audit Trail for change investigations, release reconciliation and audit evidence about who altered configuration and when.[^s2][^s5] For field-level changes to business records, use Field History Tracking or Shield Field Audit Trail; for user activity and anomaly detection, use Event Monitoring.[^s4][^s5]

## Connections

Setup Audit Trail sits under security governance (`kt:security-governance`) because it is the org's baseline evidence of configuration change.[^s2] It is queried with SOQL (`kt:soql`) through the SetupAuditTrail object.[^s1] It `contrastsWith` Field History Tracking (`kt:field-history-tracking`), which tracks record field values rather than Setup changes, and is related to Field Audit Trail (`kt:field-audit-trail`), the Shield add-on that extends that record history.[^s5][^s4] It is related to Event Monitoring (`kt:event-monitoring`), which covers user activity it does not log, and pairs with Login History (`kt:login-history`) in post-incident reviews.[^s2][^s4] The Agentforce Setup agent (`kt:agentforce-setup-agent`) consumes its data to answer change questions.[^s3] Compliance programs such as SOX (`kt:sarbanes-oxley-act`) and continuous monitoring (`kt:continuous-monitoring`) draw on it as change evidence, alongside the posture view from Security Health Check (`kt:security-health-check`).[^s4][^s5]

## Sources

[^s1]: Salesforce Developers, "SetupAuditTrail — Object Reference for the Salesforce Platform". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_setupaudittrail.htm (accessed 2026-11-23)
[^s2]: Salesforce Developers, "Exercise 1: Using the Audit Trail — Salesforce Admin Security Workshop". https://developer.salesforce.com/workshops/admin-security-workshop/monitoring-and-response/1-audit-trail (accessed 2026-11-23)
[^s3]: Trailhead, "Monitor Your Salesforce Org — Setup with Agentforce for Admins". https://trailhead.salesforce.com/pt-BR/content/learn/modules/setup-with-agentforce-for-admins/monitor-your-salesforce-org (accessed 2026-11-23)
[^s4]: Gearset, "Salesforce Audit Trail & Field History: limits & how to extend". https://gearset.com/blog/salesforce-audit-trail/ (accessed 2026-11-23)
[^s5]: Netwrix, "Auditing Salesforce: The Setup Audit Trail and Field History Tracking". https://netwrix.com/en/resources/blog/auditing-salesforce-the-setup-audit-trail-and-field-history-tracking/ (accessed 2026-11-23)
