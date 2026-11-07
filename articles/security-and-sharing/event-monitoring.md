---
id: kt:event-monitoring
type: Feature
title: Event Monitoring
aliases: [Salesforce Event Monitoring, Event Log Files, EventLogFile, ELF, Event Monitoring add-on]
domain: security-and-sharing
summary: >-
  Salesforce's user-activity logging capability: event log files, queryable event log objects and real-time events
  that record logins, API calls, report exports, page performance and more, for security investigation, adoption and
  performance analysis. Full use needs Salesforce Shield or the Event Monitoring add-on.
release: "Winter '27"
status: current
broader: [kt:salesforce-shield]
related: [kt:field-audit-trail, kt:shield-platform-encryption, kt:big-objects]
relations:
  - {predicate: requiresLicense, object: kt:salesforce-shield}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: queriedWith, object: kt:rest-api}
  - {predicate: integratesWith, object: kt:pub-sub-api}
  - {predicate: enables, object: kt:transaction-security-policies}
  - {predicate: integratesWith, object: kt:crm-analytics}
sources:
  - id: s1
    title: "Get Started with Event Monitoring"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/event_monitoring/event_monitoring_intro
    type: official-learning
    accessed: 2026-11-07
  - id: s2
    title: "Using Event Monitoring (REST API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api/using_resources_event_log_files.htm
    type: official-docs
    accessed: 2026-11-07
  - id: s3
    title: "Differences Between Hourly and 24-Hour Event Logs"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-rest/guide/event-log-file-hourly-diff.html
    type: official-docs
    accessed: 2026-11-07
  - id: s4
    title: "An Architect's Guide to Event Monitoring"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/architect-guide-event-monitoring/
    type: official-blog
    accessed: 2026-11-07
  - id: s5
    title: "Query Event Log Files"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/event_monitoring/event_monitoring_query
    type: official-learning
    accessed: 2026-11-07
created: 2026-11-07
---

# Event Monitoring

Event Monitoring records granular user activity in a Salesforce org, treating each tracked action — a login, a logout, a Lightning page click, an API call, an Apex execution, a report export — as an "event" that lands in a log.[^s1] It is one of the four products in Salesforce Shield and the main source of forensic and usage telemetry on the platform: security teams use it to investigate suspicious logins or data exfiltration, product owners use it to measure adoption, and developers use it to locate performance bottlenecks.[^s1][^s4]

## How it works

Event Monitoring now has three delivery channels, each with different latency and retention.[^s4]

- **Event log files (ELF).** Activity is written to the `EventLogFile` object, which is exposed through the SOAP and REST APIs so it can be pulled into a back-end store or SIEM.[^s2] Salesforce's architect guide counts 74 event types, delivered hourly and daily.[^s4] Each record carries an `EventType`, a `LogDate` marking the start of the covered interval, an `Interval` of `Hourly` or `Daily`, and a `Sequence` that increments for each new hourly file and is always 0 for daily files.[^s3] A file is only generated if at least one event of that type occurred in the period.[^s2] The ELF Browser offers a no-code way to find and download files, and Developer Console can query the object with SOQL — though from Winter '27 Developer Console must first be activated under Web Console in Setup.[^s5]
- **Event log objects.** A smaller set of 43 events can be queried directly through SOQL and APIs, available roughly 25–45 minutes after logging and held for 30 days; this needs the View Event Log Object Data permission.[^s4]
- **Real-Time Event Monitoring.** Twenty streaming events (14 user-activity and 6 anomaly-detection events) are published on Salesforce's Kafka-backed messaging platform and feed Threat Detection, Transaction Security and Event Storage.[^s4] Stored events land in standard objects or big objects for six months by default.[^s4]

Field-level detail is rich enough for diagnosis: for example, comparing `DB_TOTAL_TIME` (database round trip, in nanoseconds) with `CPU_TIME` shows whether slowness comes from the database or custom code, and report events capture the report name, row counts and originating user.[^s5]

## Licensing and limits

Verified against Winter '27:

- **Free tier.** Enterprise, Unlimited and Performance Editions get seven log types free with one-day retention — Apex Unexpected Exception, CORS Violation Record, CSP Violation, Hostname Redirects, Login, Logout and API Total Usage. Other types require extra cost.[^s1] Developer Edition gets all log types with one-day retention.[^s1][^s2]
- **Paid tier.** With Shield or the Event Monitoring add-on, the REST guide says files are kept one year after `CreatedDate` by default, adjustable in Event Monitoring Settings or the `EventSettings` Metadata API type; the hourly-vs-daily reference still describes a 30-day window, so confirm the setting in your org.[^s2][^s3]
- **Latency.** Daily files are generated in non-peak hours the next day; hourly files typically appear 3–6 hours after the event, sometimes later.[^s2]
- **Storage and access.** Log files don't count against data or file storage. Querying needs View Event Log Files plus API Enabled (or View All Data).[^s2]

## Gotchas

Logs are not a durable system of record: site switches, instance refreshes or outages can cause gaps.[^s2][^s4] Hourly files may be incomplete and latent files can contain duplicates, so consumers should de-duplicate and treat the daily file — which replaces earlier versions for that date — as the complete record.[^s2][^s3] Only daily files integrate with the Event Monitoring Analytics app; hourly files must be imported manually into visualization tools.[^s3] Large files (over 100 MB) should be downloaded with cURL.[^s2]

## When to use it (and when not)

Use Event Monitoring when you need evidence of who did what and from where: export auditing, login investigations, least-privilege reviews of Login As and permission changes, adoption metrics and performance triage.[^s1][^s4] For long-term compliance retention, export to an external store rather than relying on in-org retention.[^s4] For configuration-change history alone, Setup Audit Trail and Login History (six months each) may suffice without a licence.[^s4]

## Connections

Event Monitoring is **part of Salesforce Shield** and **requires** a Shield or add-on licence beyond the free types.[^s1] Its log data is **queried with SOQL** and pulled via the **REST API**, while real-time events stream to SIEMs through the **Pub/Sub API**.[^s2][^s4] Real-time events **enable transaction security policies** that can block an action, require MFA or notify admins, and daily logs **integrate with CRM Analytics** through the Event Monitoring Analytics app.[^s3][^s4] Stored real-time events use **big objects**; it complements **Field Audit Trail** (data history) and **Shield Platform Encryption** (data at rest).[^s4]

## Sources

[^s1]: Trailhead, "Get Started with Event Monitoring". https://trailhead.salesforce.com/en/event_monitoring/event_monitoring_intro (accessed 2026-11-07)
[^s2]: Salesforce Developers, "Using Event Monitoring (REST API Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api/using_resources_event_log_files.htm (accessed 2026-11-07)
[^s3]: Salesforce Developers, "Differences Between Hourly and 24-Hour Event Logs". https://developer.salesforce.com/docs/platform/api-rest/guide/event-log-file-hourly-diff.html (accessed 2026-11-07)
[^s4]: Salesforce, "An Architect's Guide to Event Monitoring". https://www.salesforce.com/blog/architect-guide-event-monitoring/ (accessed 2026-11-07)
[^s5]: Trailhead, "Query Event Log Files". https://trailhead.salesforce.com/content/learn/modules/event_monitoring/event_monitoring_query (accessed 2026-11-07)
